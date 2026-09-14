# EBS Integration Architecture

> How every flow in the canonical
> [integration architecture map](../01-model-company/data-volumes-and-integrations.md) §2–§3
> is realized against Oracle EBS: the native mechanisms EBS offers, the IAP-first rule, the
> per-flow pattern register, error handling, and the reconciliation controls that make each
> interface audit evidence for the 808-control register.

Part of the [02-oracle-ebs blueprint](README.md). Extends — never overrides — the
[technical guidelines](../07-methodology/technical-guidelines.md) and the sourcing model's
contract-first rule.

---

## 1. Prime Rule: IAP Is the Only Integration Path

No external system touches EBS tables, forms, or URLs directly. Integrated systems — the
**already-built POS estate and ecommerce platform**, the in-suite WMS, the in-house builds
(workforce, payroll, OMO/TPS/AAP/IAP/DP), loyalty, marketplaces — speak **IAP contracts**;
IAP adapters translate to EBS's native tongues. Inside EBS the permitted mechanisms are:

| Mechanism | What it is | Used for |
|---|---|---|
| **Open interface tables** | Staged, validated, error-queued loads (e.g., `MTL_TRANSACTIONS_INTERFACE`, AutoInvoice lines, `AP_INVOICES_INTERFACE`, `GL_INTERFACE`, PO/RCV interfaces) | All high-volume inbound transaction loads |
| **Public PL/SQL APIs** | Supported packages (TCA `HZ_*`, `EGO_ITEM_PUB`, `QP_*`, `HR_*`, receiving processing, order import) | Master data and transactional creates where APIs beat tables |
| **ISG (Integrated SOA Gateway)** | REST/SOAP exposure of interfaces & business-service objects | IAP→EBS synchronous calls (price/ATP lookups, order status) |
| **Business Events (WF_EVENT)** | Publish/subscribe on EBS transaction milestones | Outbound facts (order shipped, invoice created) to IAP topics |
| **XML Gateway (ECX)** | Standards-based cXML/EDI (PO, ASN, invoice) | iSupplier and strategic-supplier document exchange |
| **Concurrent program outputs & reports** | Structured extracts (BI Publisher data templates) | File feeds: banks, BIR, agencies, DP lakehouse |

Direct DB links, direct table writes by external systems, and screen-scraping are
prohibited (customization-governance §5 applies to integration code equally).

---

## 2. Pattern Register (per Integration-Matrix Flow)

Column "Flow" quotes the canonical matrix rows
([data-volumes §3](../01-model-company/data-volumes-and-integrations.md)).

| Flow | SLA | EBS-side pattern | Reconciliation control |
|---|---|---|---|
| POS → ERP: sales transactions | Near-real-time (< 30 s) + nightly completeness | In-house POS platform events → IAP stream → staging → OM order import / AR invoice interface + INV issue transactions; batched in waves, committed per store-hour | Nightly per-store completeness batch (W533/W537): POS journal count vs EBS transaction count → zero-difference or LP incident |
| ERP → POS: price file, item master, promos | < 60 s on activation + nightly full refresh | QP/INV/eBTax change events → IAP topics → in-house POS price service; versioned full-file rebuild nightly | Price-version manifest per store; W553/W69 audit sampling |
| ERP → POS: customer lookup | Real-time; offline cache | TCA REST (ISG) lookup with loyalty/trade flags; POS-local cache for offline (W535) | Cache-hash spot audits; W253 dedup keeps source clean |
| Ecommerce → ERP: orders, registrations | Real-time (< 1 min) | IAP → OM order import (W536/W534 legs from OMO); TCA party create via `HZ_*` on registration | Order-count tie-out per channel daily; W98 exception queue |
| ERP → Ecommerce: availability, prices, catalog | 5 min | ATP/availability extract (planned onhand) → IAP topic; catalog via item API extracts | Availability drift check vs onhand snapshot |
| ERP → Ecommerce: fulfillment status | Real-time | OM ship-confirm business events → IAP → ecommerce | Status-echo reconciliation |
| ERP → WMS: transfer orders, PO receipts | Real-time | Internal requisitions/receipts → IAP → WMS tasking | Task-completion feed mirrors C8/C7 counts |
| WMS → ERP: pick/ship/inventory confirmations | Real-time (< 1 min) | WMS events → IAP → ship-confirm (WSH), MTL transactions interface | Ship-confirm vs pick-ticket count; W22 discrepancy workflow |
| ERP → Loyalty: earn triggers | Real-time | Sales events → IAP → loyalty engine | Earn/redemption netting vs AR/POS settlement (W550) |
| CRM/POS → ERP: redemption | Real-time | Redemption event → AR credit/invoice adjustment via interface | Daily redemption ledger tie-out |
| ERP → Banks: AP payment files | Daily batch | IBY payment process → bank formats → IAP delivery | Payment-file vs payment-batch hash; W320 controls |
| Banks → ERP: statements | Daily batch | Statement files → CE statement import → auto-reconciliation | W89 recon-rate KPI; unmatched → W272-class queues |
| ERP → BIR eFPS: returns | Monthly/quarterly | eBTax/SLA balances → BI Publisher return datasets → IAP submission channel | Return dataset vs GL balance certification (VS-79 control) |
| ERP → SSS/PhilHealth/Pag-IBIG | Monthly | Payroll PH build statutory-file generation (E6) → IAP delivery | Contribution registers vs payroll registers (W251) |
| ERP → Delivery partners (3PL) | Real-time | Delivery orders from WSH/OMO → IAP → partner APIs; status back into shipping | Delivery-order vs ship-confirm tie-out (W548) |
| Payment GW → ERP: confirmations | Real-time | Gateway events → IAP → AR receipts (fast path) + settlement batches | W99/W261/W267 settlement reconciliation |
| ERP → Supplier portal (iSupplier) | Real-time | Native iSupplier portal (DMZ) for PO/ASN/invoice; XML Gateway for cXML suppliers | ASN vs receipt match (W422); supplier-invoice tie-out |
| Gateways → ERP: chargebacks/fees | Monthly | Gateway fee/chargeback files → IAP → AP invoices/AR deductions | W267/W348 revenue-assurance audit trail |
| **Payroll (in-house build) → ERP: costing journals & statutory accruals** | Monthly | Payroll PH period costing → IAP → `GL_INTERFACE` posting (E8); EBS stays the ledger of record | Journal tie-out vs the payroll register per period; SLA derivation review |

**Built differentiators note:** OMO/TPS/AAP — and the already-built POS/ecommerce/loyalty
platforms — do not integrate "differently": they are IAP consumers/producers like any
integrated system; their EBS-facing contracts land in this register like everyone else's.

---

## 3. Government & Statutory Interfaces (LOC/INT rows)

The [fit-gap §6 pack](fit-gap-analysis.md) owns formats; this section fixes the
architecture:

1. **One government-channel adapter per authority** (BIR/eFPS, SSS, PhilHealth, Pag-IBIG),
   owned by IAP; EBS and the in-house payroll build generate the datasets; the adapter
   handles transport, retry, receipt archival.
2. **Filing acts stay human**: no agent or automation completes a statutory filing
   (sourcing model §12.1 hard boundary) — the adapter submits only on human confirmation
   recorded as control evidence.
3. **Receipts are records**: government acknowledgements archive against the period's pack
   release id, citable in BIR audit response (W77).

---

## 4. Latency & Batch Discipline

The 30/60-second and 5-minute SLAs ([data-volumes §4](../01-model-company/data-volumes-and-integrations.md))
are met by streaming through IAP into **staged interface loads** — never by synchronous
form-level entry. EBS-side batch jobs (import runners, cost manager, planning, reconciliation)
run inside the canonical batch windows ([data-volumes §5](../01-model-company/data-volumes-and-integrations.md));
a job that overruns its window is an incident with a documented recovery path (restartable
per customization-governance §5).

## 5. Master-Data Flow Direction

| Data | System of record | Flows |
|---|---|---|
| Items, UOM, barcodes, tax codes, cost | EBS (INV/eBTax/CST) | Out to POS/ecommerce/WMS/loyalty |
| Price lists, modifiers, promo calendar | EBS (QP) — masters; POS executes | Out to POS/ecommerce |
| Customers | EBS TCA | Out (lookup/cache); engagement attributes stay in the owning platforms and reconcile back |
| Suppliers | EBS (PO/TCA) | Out to iSupplier/integrated platforms |
| Stock onhand | EBS ledger (INV) | Out (availability); WMS/POS hold operational views only |
| Orders | Channel-owned until accepted; EBS OM from acceptance | Inbound |
| Sales facts | POS/ecommerce execute; EBS posts the ledger | Inbound |
| Agency/government data | External | Bidirectional via channel adapters |

---

## 6. Error Handling & the Error Taxonomy

| Class | Meaning | Handling |
|---|---|---|
| **E1 Validation** | Failed interface-transport validation (missing UOM, bad TIN format) | Reject at staging; source-system fix queue; never partially post |
| **E2 Business** | Failed EBS import (no period, credit hold, lot rules) | Interface error table → owning team queue → reprocess API |
| **E3 Latency** | SLA breach without data loss | Alert (W380-class event monitoring); drain plan; no manual re-keying |
| **E4 Divergence** | Reconciliation mismatch (POS vs EBS counts) | LP incident path (W537/W541); owner: domain controller |
| **E5 Downtime** | Platform offline / EBS unavailable | In-house POS offline mode ≥ 8h with event replay (W535); IAP spool-and-forward |

Every IAP→EBS adapter emits the taxonomy codes; the weekly integration-health review
(VS-27 surface) reads only exceptions.

---

## 7. Adding a New Interface

New flows pass the same gates as everything else: demand intake (W5535) → architecture
review (pattern must be one of §2; a new pattern is an ARB record) → CDR if any BDR object
is involved → the integration is added to *this* register with its reconciliation control
named. An interface without a reconciliation control is not shippable.

---

*Document Version: 1.1 | Date: 2026-09-14 | Two-tier sourcing doctrine enacted: integrated-systems wording (already-built POS/ecommerce/loyalty platforms; in-suite WMS; in-house builds), payroll posting row added to the pattern register (GL_INTERFACE via IAP, E8), government-channel adapters fed by EBS and the payroll build. Prior v1.0 (2026-09-14): initial issue — EBS-native mechanism set, IAP-first rule, per-flow pattern register mirroring the canonical integration matrix, government-channel adapter rule, master-data flow directions, error taxonomy, new-interface gate. Canon anchors: data-volumes-and-integrations §2–§5; sourcing model §7 rule 3 (contract-first); fit-gap LOC/INT rows.*
