# Oracle EBS 12.2 — Platform Architecture

> How the model company is realized on Oracle E-Business Suite 12.2: the organization and
> ledger model for 5 legal entities / 200 stores / 4 DCs, the module footprint, the
> technology stack, environment and patching strategy, and the integration + security
> architecture that the [integration register](integrations.md) and
> [sourcing register](../07-methodology/capability-sourcing-and-engineering-model.md) ride on.

Part of the [02-oracle-ebs blueprint](README.md).

---

## 1. Organization Model (the Spine of the Whole Suite)

EBS multi-org is configured once, correctly, and everything else inherits it.

### 1.1 Structure

| EBS construct | BuildRight realization | Count | Canon anchor |
|---|---|---|---|
| Business Group | **BuildRight Depot Corp. PH** (single BG) | 1 | VS-19 HR foundation |
| Legal Entity (E-Business Tax regime owner) | BRDC Retail Inc. · BRDC Imports & Trading · BRDC Property Holdings · BRDC Services Corp. · BRDC Foundation | 5 | Profile §9 — 5 legal entities |
| Primary Ledger | One per legal entity, **shared chart of accounts, PHP ledger currency** | 5 | VS-17 record-to-report |
| Secondary Ledger / reporting currency | USD reporting ledger where required (import financing, LC reporting) | as needed | VS-18.3 FX |
| Operating Unit | One OU per legal entity; trade/corporate AR and AP live in the retail OU by default | 5 | MO: Operating Unit |
| Inventory Organization — master item org | **HQ Master Org** (item definitions, catalogs, item templates) | 1 | VS-29 master data |
| Inventory Organization — distribution centers | One org per DC (organized by DC role: import hub, regional DCs) | 4 | Profile §3.2 — 4 DCs, catchments 20–80 stores |
| Inventory Organization — stores | One standard (non-WMS) org per store, under the owning legal entity's OU | 200 | Profile §3.1 — 200 stores |
| Cost organization / costing group | Perpetual **weighted-average cost** chain-wide, cost org per DC cluster | as needed | W3 (perpetual WAC at receipt), W85 |
| HR Location / store hierarchy | 200 store locations + 4 DC locations + HQ, mapped to the organization hierarchy for security and reporting | — | TO §7 store roster |

### 1.2 Why this shape

- **One chart of accounts, five ledgers**: consolidation (W234 profit elimination) works on
  GL Consolidation/FSG without translation; the company segment carries the entity, so the
  808 controls' SoD and entity-scoping rules are enforceable by setup, not by convention.
- **Store orgs are inventory organs, not accounting units**: stores transact in their org;
  the accounting entries flow to the legal entity's ledger through the OU. New store
  opening (W16) is an **add-org runbook** (org, subinventory, locators, security profile,
  MOAC, price list assignment, POS mapping) — measured in hours, not days.
- **MOAC (Multi-Org Access Control)**: HQ roles see all OUs through security profiles;
  store and DC roles see exactly their own org. This is the EBS-native enforcement of the
  touchpoint map's location-scoped workflows (e.g., W109, W212, W219).

---

## 2. Module Footprint (What We License and Use)

Every row cites where the module carries model-company workflows. Anything not listed is
deliberately not adopted (see the [fit-gap register](fit-gap-analysis.md) for the evidence).

| EBS product (module) | Used for | Value streams / workflows served |
|---|---|---|
| **General Ledger (GL)** | Ledgers, CoA, journals, consolidation, FSG financial statements, budgets | VS-17 (close W9/W9A/W9B, W26 budget), W234 |
| **Subledger Accounting (SLA)** | Accounting rules for all subledgers; PH-compliant journal derivations | VS-17; every transactional VS |
| **Accounts Payable (AP)** | Vendor invoices, 3-way match, EWT withholding, payments, PDCs | W7, W100, W244, W424, PA-15.1/15.2 |
| **Accounts Receivable (AR)** | Trade/corporate invoices, credit memos (W540), PDC registers (W423), deposits | VS-11, VS-16, VS-143 |
| **Cash Management (CE)** | Bank statement import & reconciliation, cash positioning feeds | W89, W212/W541 reconciliation, VS-18.1 |
| **Payments (IBY)** | Payment formats, bank payment files, positive pay | W320 electronic payment control, PA-18.2 |
| **Fixed Assets (FA)** | Asset register, depreciation, disposals, CIP via mass additions | W39, W184, W276, VS-35 |
| **E-Business Tax (eBTax)** | PH VAT determination, VAT-exempt/zero-rated (SC/PWD/solo-parent pathways), EWT/ATC (WC 010/WI 010/WP 010 canon) | VS-79, VS-85, W145, W24 |
| **Purchasing (PO)** | Requisitions, POs, blankets (W2C), receipts, receiving 3-way match | VS-03, VS-15; W2 family |
| **iProcurement** | Store/HQ self-service requisitioning, non-merchandise catalogues | W136, VS-34 |
| **Sourcing (PON)** | RFQs, auctions, bid tendering (government/institutional) | W166, VS-46 |
| **iSupplier (POS portal)** | Vendor portal: PO view, ASNs, invoicing, catalogs | W422, R28, PA-03.x |
| **Supplier Lifecycle Management** | Supplier onboarding questionnaire/approval flow | W36 vendor onboarding |
| **Landed Cost Management (LCM)** | Import true-up: freight, duties, demurrage allocation to item cost | W144, W239, W249, VS-122 |
| **Inventory (INV)** | Item master, UOM/conversions, onhand, subinventories, min-max, cycle counts, physical inventory, inter-org transfers, consignment | VS-05, VS-29; W3/W4/W6/W22/W42 family |
| **Warehouse Management (WMS) / MSCA** | **Adopted in-suite** — RF-directed putaway/pick, LPN/pallet tracking, directed tasking | VS-04; two-tier doctrine resolution (in EBS → use it) |
| **Bill of Materials (BOM) / WIP** | Kit/BOM definitions, bundle assembly, build-to-order | W46, VS-92 |
| **Order Management (OM)** | Sales orders, quotes→orders (W58), backorders (W56), sales agreements, drop-ship (W246), ship-confirm | VS-11, VS-16, VS-60 (fulfillment legs) |
| **Advanced Pricing (QP)** | Price lists, modifiers, qualifiers, coupon/promotion rules, PH mandatory discounts | W40, W61, W93, VS-85, W539 |
| **Shipping Execution (WSH)** | Ship confirm, delivery/trip, packing slips | W19, W106 dispatch |
| **Transportation Execution (OTE)** | Carrier tender, freight cost capture — in-suite under the two-tier doctrine (the BoB TMS row is superseded); optimization beyond OTE is a build candidate, never a buy | VS-110 freight postings |
| **Oracle Quality (QA)** | Incoming inspection plans, supplier quality data collection | W110 supplier quality, VS-31 |
| **Property Manager (PN)** | Lease administration, rent/CAM/indexation billing, critical dates | VS-42, W117/W118 |
| **Projects (Project Costing + PM)** | Capex projects, CIP, project vendor bills, asset turnover hand-off | VS-40, VS-20, W21, W276 |
| **Oracle HRMS (PER)** | Org/position/employee master, EITs (licenses, PPE sizes), absence types | VS-19, W15/W43, W292 — Core HR stays in EBS; the payroll engine is the in-house build (below) |
| *Oracle Payroll (PAY)* | ***Not adopted*** — payroll is an in-house build (fit-gap E5–E8): the build owns PH statutory gross-to-net and compensation outputs, posts costing journals into EBS, and pulls people data from PER | VS-19.2; fit-gap §4 resolution 7 |
| **iRecruitment (IRC)** | Vacancy/requisition/candidate self-service | W-recruitment family, VS-121 |
| **Oracle Learning Management (OLA)** | Training calendar, compliance enrollments | W51, VS-123/183 (basic; deeper LMS function, if ever needed, is a build) |
| **Oracle Treasury (XTR)** | Cash positioning, investments, debt/covenants, FX exposure & deals | VS-18.1–18.3, W80, W318/W319/W321 |
| **Advanced Collections (IEX)** | Delinquency strategy, dunning, promise-to-pay | VS-16.3, W108 |
| **Credit Management** | Credit scoring rules, limits, hold/release | W24, W328, W229 |
| **Approvals Management (AME)** | Rule-driven approvals across PO/AP/AR/HR (PHP tier ladders) | The DMN authorization ladders' system enforcement |
| **Oracle Workflow / Business Events** | Document approvals, event subscription for integrations | Cross-cutting |
| **Integrated SOA Gateway (ISG)** | REST/SOAP exposure of EBS interfaces for IAP/edges | [integrations.md](integrations.md) |
| **XML Gateway (ECX)** | Standard cXML/EDI transactions (ASN, invoice, PO) | W245 chargebacks, iSupplier flows |
| **BI Publisher (XDO)** | Statutory & operational document formats (BIR pack, PO/INV prints) | [fit-gap §6](fit-gap-analysis.md), VS-79 |
| **Web ADI** | Mass maintenance (items, price lists, budgets, journals) from spreadsheets | VS-29 governance runs |
| **Enterprise Command Centers (ECC)** | Embedded operational dashboards (payables, receivables, inventory, procurement) | Tier-3 analytics, PA-28.x |
| **Enterprise Repository Engines (ERES)** | E-signature evidence on controlled documents/approvals | Control evidence for CTL register |
| **Not adopted** | iStore (legacy storefront), Discoverer, Forms-customization of shipping forms, Oracle Configurator (CZ) for B2C, **Oracle Payroll** — gaps dispositioned in the fit-gap register | VS-10, VS-07, VS-19.2 |

**In-house products riding EBS (outside the suite, integrated via IAP):** the **POS estate**
and the **custom ecommerce platform** (both already built — integration is the program), the
gift-card/loyalty stack (already built), **Payroll PH**, the store workforce platform, and
OMO/TPS/AAP/IAP/DP. None of them buys its way in; all of them ledger into EBS.

**Planning products (adopted with the two-tier doctrine):** Oracle Advanced Supply Chain Planning (ASCP) and
Demantra Demand Management — the EBS-family Value Chain Planning stack — are **adopted** as the planning stack
(fit-gap C5, resolution record §4-2): VS-02's statistical forecasting and VS-127's IBP surface ride them; license
cost is a FinOps decision, not a sourcing decision.

---

## 3. Technology Stack

| Layer | Standard | Notes |
|---|---|---|
| EBS release | **12.2**, Release Update Pack baseline **12.2.12** + quarterly RUP/monthly update streams | Keep within one RUP of current; RUP currency is a KPI (customization-governance §9) |
| Database | **Oracle Database 19c**, RAC/Active Data Guard for HA/DR | Typhoon-season resilience (sourcing model §7 rule 7): ADG to a second zone; RPO/RTO targets per VS-26.1 BCP |
| Middleware | Oracle WebLogic Server (12.2 stack), Oracle HTTP Server, DMZ reverse proxy tier for iSupplier/ISG endpoints | External endpoints terminate in DMZ per [technical-guidelines](../07-methodology/technical-guidelines.md) |
| UI | Forms (back-office power users) + OA Framework/HTML (self-service, iProcurement, iSupplier) | No Forms modification (doctrine rule 3) |
| Patching | **ADOP online patching** (edition-based redefinition) | Custom code must be edition-enabled — rules in [customization-governance §6](customization-governance.md) |
| SSO/IAM | Oracle Internet Directory + Access Manager federation to the corporate IdP | W152 joiner/mover/leaver provisioning drives FND users & responsibilities |
| Print/labels | BI Publisher server + store label printers via the POS platform/WMS | W63/W181 shelf tags print from the in-house POS platform, not Forms |

---

## 4. Environment Strategy

| Environment | Purpose | Notes |
|---|---|---|
| **DEV** | Configuration build, extension development | Refresh-masked clones per W384 |
| **TEST/SIT** | Integration testing with the integrated platforms (POS/ecommerce/WMS stubs) | IAP contract tests run here (sourcing model §7 rule 3) |
| **UAT/TRAIN** | Business validation + the 6,762-user training estate | W73 parallel-run rehearsals |
| **PATCH** | ADOP patch/upgrade rehearsal (RUP, CPU) | Mandatory gate before any PROD patch |
| **PROD** | Production | DR twin via Data Guard |

Cloning cadence: monthly UAT refresh, per-wave SIT refresh, ad-hoc hotfix clone. All
refreshes run the masking profile (W384) — production data never trains unmasked.

---

## 5. Integration Architecture (Summary)

The full pattern register lives in [integrations.md](integrations.md); the platform-level
rules:

1. **IAP is the only integration path.** No integrated system writes EBS tables directly.
   Integrated systems — the already-built POS estate and ecommerce platform, the in-suite
   WMS, the in-house builds, loyalty — speak IAP contracts; IAP adapters speak EBS in its
   native tongues — open interface
   tables, public PL/SQL APIs, ISG REST/SOAP, business events (WF_EVENT), XML Gateway.
2. **High-volume flows are asynchronous and interface-table-based.** POS sales land in
   staging → validated → OM/AR/INV interfaces; the 30-second POS→ERP latency SLA is met by
   streaming into IAP, not by hammering EBS forms.
3. **Master data flows outward from EBS** (items, prices, tax codes to POS/ecommerce/WMS);
   **transaction facts flow inward** (sales, receipts, picks, payments). The one ledger
   stays in EBS — this is what "inventory ledger of record" means in the sourcing register.
4. **Every interface is a control point.** Each flow in the
   [integration detail matrix](../01-model-company/data-volumes-and-integrations.md) §3
   carries reconciliation counts into the CTL register (the nightly POS completeness batch
   is control evidence, not just plumbing).

---

## 6. Security Architecture (Summary)

- **RBAC via responsibilities + UMX roles**, provisioned only through the W152 lifecycle;
  direct user-responsibility grants are prohibited (audit finding class).
- **MOAC security profiles** enforce org-scoping (a store cashier-role touches one org; a
  merchandising role sees the master org).
- **AME rule sets** encode the DMN tiered PHP authorization ladders — approvals cannot be
  delegated outside the ladder without an AME exception record (control evidence).
- **SoD**: function-security pairs (vendor-create vs payment-approve; item-cost vs count
  approval; journal-create vs post) map to the internal-controls register; the W338 SoD
  review queries EBS role assignments directly.
- **DMZ hardening** for iSupplier/ISG: reverse proxy, TLS, WAF, no direct DB listeners.
- Full detail incl. the role matrix is an implementation-phase deliverable (07-methodology
  "Future Additions — Security hardening guide"); the fit-gap register's security rows pin
  the platform capabilities.

---

## 7. Non-Functional Fit (R14 View)

| NFR theme | EBS platform answer |
|---|---|
| Scale (14,000 POS txn/store/month × 200) | 600-terminal POS estate posts ~2.8M POS transactions plus ~42,900 ecommerce orders/month chain-wide (the ecommerce total per the profile's Total-Ecommerce-Orders canon and data-volumes §1.2's ~515,000/year; the e-wallet tender subset — about 420,000 POS and 17,000 ecommerce e-wallet transactions per month, per W1268/PA-15.2 — rides the same flows) — interface-table throughput well inside EBS reference capacity; nightly reconciliation batch validates completeness (W533/W537) |
| Availability | RAC + Data Guard; the in-house POS platform runs offline (≥ 8h) with event replay (W535) — EBS availability never gates a store |
| Batch windows | Close, costing, planning and interface-restore jobs run inside the [batch window table](../01-model-company/data-volumes-and-integrations.md) §5 |
| Auditability | ERES e-signatures, FND audit options on master-data tables, SLA/audit trails — evidence for the 808-control register |
| Data residency | Fully under BuildRight control (on-premises deployment), RA 10173-aligned (W434 NPC registration scope) |

---

*Document Version: 1.1 | Date: 2026-09-14 | Two-tier sourcing doctrine enacted (in EBS → use it; otherwise → build): Oracle WMS/MSCA and Shipping/OTE adopted in-suite (BoB WMS/TMS superseded), Oracle Payroll marked not-adopted with payroll re-scoped to the in-house build (fit-gap §4 resolution 7), in-house-products roster added (POS/ecommerce/loyalty already built — integration is the program). Prior v1.0 (2026-09-14): initial issue — org/ledger model, module footprint, tech stack, environments, integration and security architecture for the EBS realization. Canon references: 5 legal entities / 200 stores / 4 DCs / 35,000 active SKUs / ~2.8M POS transactions/month (tender-mix canon); Premier-Support horizon re-verified at contract time.*
