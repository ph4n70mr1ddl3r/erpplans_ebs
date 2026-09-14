# Technical Implementation Guidelines

> This document provides technical guidelines and reference specifications for BuildRight Depot Corp.'s unified ERP system architecture (Oracle E-Business Suite 12.2 under the two-tier doctrine). The POS architecture is designed for **real-time/near-real-time operation** with **offline resilience** and **multi-origin fulfillment** capability.

---

## 1. POS Hardware Reference Specification

The following is the POS hardware specification that meets the business requirements
(offline capability, barcode scanning, multi-tender, receipt printing).

| Component | Reference Spec |
|---|---|
| **Terminal Type** | All-in-one POS terminal (touchscreen) |
| **Screen Size** | 15" touchscreen (cashier) + customer-facing display |
| **Barcode Scanner** | Integrated 2D imager (1D + 2D: QR, DataMatrix) + handheld scanner |
| **Receipt Printer** | 80mm thermal printer (BIR-registered format) |
| **Cash Drawer** | Triggered by POS; 4-bill / 8-coin compartments |
| **Payment Device** | PIN pad for card (EMV/chip & contactless); e-wallet QR support |
| **Offline Storage** | Must store ≥ 8 hours of transactions locally (~933 peak-day transactions per store = 467 avg/day × 2.0 peak factor, buffered to ~1,500 capacity for an extended-outage safety margin) |
| **Local Data Store** | Embedded local database on each terminal containing: active SKU catalog (barcode, description, price, UOM, promo rules, flags), cached customer records (loyalty members + trade accounts), terminal configuration; enables full offline selling with accurate pricing and customer recognition |
| **Connectivity** | Primary link + failover connectivity; POS operates offline with full capability during WAN outage; store LAN enables terminal-to-terminal sync when WAN is down |
| **Central Management** | Centrally managed (MDM or equivalent); OTA updates across 600 terminals |

### POS Cost Estimate (Reference)

| Item | Unit Cost (PHP) | Qty | Total (PHP) |
|---|---|---|---|
| POS Terminal (all-in-one) | ~20,000 | 600 | 12,000,000 |
| Barcode Scanner (handheld) | ~5,000 | 600 | 3,000,000 |
| Receipt Printer | ~8,000 | 600 | 4,800,000 |
| Cash Drawer | ~5,000 | 600 | 3,000,000 |
| Payment PIN Pad | ~15,000 | 600 | 9,000,000 |
| **Per-Store Total (3 terminals)** | | | **~PHP 159,000** |
| **All 200 Stores** | | | **~PHP 31,800,000** |

> Note: POS hardware costs are standardized across all locations.

### POS Architecture Principles

The POS system architecture follows three core principles:

#### 1. Real-Time / Near-Real-Time Event-Driven Architecture

| Principle | Implementation |
|---|---|
| **Event streaming** | Each POS transaction (sale, void, return, refund) is published as a discrete event to the ERP message bus within 30 seconds of occurrence |
| **Decoupled processing** | POS terminals operate independently of downstream processing latency; events are queued locally and transmitted asynchronously |
| **Guaranteed delivery** | At-least-once delivery semantics with idempotent event processing and deduplication at ERP; zero data loss tolerance |
| **Event replay** | On reconnection after offline period, events are replayed from last-acknowledged sequence number |
| **Multi-consumer** | Downstream systems (inventory, GL, loyalty, ecommerce ATP, BI dashboards) subscribe to events independently and process at their own pace |
| **Continuous price push** | ERP pushes price changes, new items, discontinued flags, and promotional rules to terminals continuously throughout the day (not nightly batch only); price updates applied within 60 seconds of central activation |

#### 2. Multi-Origin / Mixed Fulfillment

| Principle | Implementation |
|---|---|
| **Unified order management** | Centralized order engine accepts orders from all channels (POS, ecommerce, marketplace, mobile app, trade counter) |
| **Mixed-basket support** | A single POS transaction can contain items fulfilled from different origins: in-store, another store (inter-store transfer), DC home delivery, drop-ship vendor, or endless aisle special order |
| **Fulfillment routing** | Intelligent routing engine evaluates ATP across all locations and fulfillment sources to determine optimal origin per line item |
| **Split fulfillment** | System creates separate fulfillment orders per origin while linking to a single sales order for unified financial posting |
| **Cross-channel returns** | Buy online return in-store, buy in-store return online, with unified credit/refund processing |

#### 3. Offline Resilience

| Principle | Implementation |
|---|---|
| **Full offline selling** | POS terminals continue complete selling operations during network outage for ≥ 8 hours with local embedded data store |
| **Local data scope** | Active SKU catalog, price file, promotional rules, cached customer records (loyalty + trade), terminal configuration stored locally |
| **Terminal-to-terminal LAN sync** | When WAN is down but store LAN is operational, terminals synchronize transactions and inventory deductions peer-to-peer, preventing overselling |
| **Offline capability matrix** | Configurable per-store: full capability (scanning, pricing, cash, offline card, receipts, voids), degraded capability (loyalty queued, trade account floor limit), unavailable functions (e-wallet, digital receipts, new enrollment) |
| **Automatic reconciliation** | On reconnection: encrypted offline transactions uploaded, inventory conflicts resolved, GL posted, loyalty reconciled, stale price flagged — all automatically with Store Manager exception review only |

---

## 2. Infrastructure & Deployment Reference

The following is the infrastructure topology that satisfies the NFRs in [erp-requirements.md](../01-model-company/erp-requirements.md).

### 2.1 Deployment Model Considerations

| Consideration | Notes |
|---|---|
| 200 store locations with POS | Requires reliable connectivity or robust offline mode |
| 4 DCs with WMS/RF guns | Low-latency connection needed for real-time pick/ship |
| 600 POS terminals | Centralized management is essential |
| 6,762 employees | Core HR lives in the on-premises EBS suite; statutory payroll is computed on the in-house Payroll PH build on BuildRight-run infrastructure — nothing rides a public cloud (the platform of record is not a cloud/SaaS ERP) |
| Philippine regulatory filing | BIR, SSS, PhilHealth, Pag-IBIG file generation |
| Data residency | The platform of record (Oracle EBS 12.2) runs **on-premises** in BuildRight-controlled facilities per [`02-oracle-ebs/`](../02-oracle-ebs/README.md) §1; Philippine facility placement favored for latency |

### 2.2 Network Bandwidth Reference Estimates

These are estimates based on transaction volumes. Actual bandwidth depends on the chosen
ERP's data sync requirements.

| Site Type | Count | Reference Bandwidth | Rationale |
|---|---|---|---|
| Store | 200 | ≥ 2 Mbps stable + failover link | POS sync, price updates, inventory updates |
| DC | 4 | ≥ 10 Mbps stable, redundant | WMS real-time operations, ~80 RF guns per DC |
| HQ | 1 | ≥ 100 Mbps | ~362 HQ staff (≈325 concurrent users), reporting, batch processing |
| **Total WAN** | **205** | **~540 Mbps aggregate** | |

### 2.3 DR & Business Continuity Reference

| Parameter | Target | Notes |
|---|---|---|
| RPO (back-office) | ≤ 1 hour | Financial data, inventory |
| RTO (back-office) | ≤ 4 hours | Core ERP functions |
| POS offline endurance | ≥ 8 hours | Must continue selling without connectivity |
| POS sync on reconnection | Automatic | No manual intervention; reconcile all offline transactions |
| Data backup | Daily | 30-day rolling + 10-year archive |
| Data retention | 10 years | BIR requirement (TRAIN/NIRC — Sec. 235, as amended by RA 10963) |

---

## 3. Integration Architecture Reference

### 3.1 Integration Methods by Touchpoint

The model company's [integration touchpoints](../01-model-company/model-company-profile.md#143-active-integration-touchpoints)
define what connects. The table below details how these systems are integrated.

| Touchpoint | Suggested Method | Notes |
|---|---|---|
| POS ↔ ERP | Event-driven API (near-real-time, < 30 sec latency) | POS publishes transaction events continuously; nightly reconciliation batch validates completeness; offline events queued locally and replayed on reconnection |
| Ecommerce ↔ ERP | REST API | Real-time for orders; near-real-time for inventory |
| Payment Gateway → ERP | Webhook / API | Real-time payment confirmation |
| Bank ↔ ERP | File-based (CSV/XML) or API | Bank-specific formats (BDO, BPI, Metrobank, Chinabank) |
| BIR eFPS ← ERP | File export | BIR-formatted tax return files |
| SSS / PhilHealth / Pag-IBIG ← ERP | File export | Monthly contribution files with PRN |
| Delivery Partners ↔ ERP | API | Real-time order dispatch and status tracking |
| Loyalty Engine ↔ ERP | API | Real-time points earn/redeem |
| WMS ↔ ERP | API or middleware | Real-time for pick/ship confirmations |
| Supplier Portal ↔ ERP | Web portal / EDI | PO viewing, ASN, invoice submission |

### 3.2 Integration Architecture Diagram (Reference)

> The canonical integration architecture diagram is maintained in [data-volumes-and-integrations.md](../01-model-company/data-volumes-and-integrations.md). The diagram below is a duplicate for convenience; if updates are needed, update the canonical version first.

```
┌─────────────────────────────────────────────────────────────────────┐
│                        BUILDRIGHT DEPOT CORP                        │
│                      INTEGRATION ARCHITECTURE                       │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐   │
│  │ 600 POS  │  │ 4 WMS    │  │ Ecommerce │  │ Loyalty Engine   │   │
│  │Terminals │  │Systems   │  │ Platform │  │ (CRM)            │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────────┬─────────┘   │
│       │              │              │                  │             │
│       └──────────────┴──────┬───────┴──────────────────┘             │
│                             │                                        │
│                    ┌────────▼────────┐                               │
│                    │   ERP SYSTEM    │                               │
│                    │   (Core Hub)    │                               │
│                    └────────┬────────┘                               │
│                             │                                        │
│       ┌─────────────┬──────┴──────┬──────────────┐                  │
│       │             │             │              │                   │
│  ┌────▼─────┐ ┌────▼─────┐ ┌────▼─────┐  ┌────▼──────┐            │
│  │   Banks   │ │ BIR/eFPS │ │ SSS/PH/  │  │ Delivery  │            │
│  │(BDO, BPI, │ │ (Tax     │ │ Pag-IBIG │  │ Partners  │            │
│  │MB, CB)    │ │ filing)  │ │ (Stat.)  │  │(Lalamove, │            │
│  └──────────┘ └──────────┘ └──────────┘  │ Transp.)  │            │
│                                           └───────────┘            │
│       ┌─────────────┐         ┌─────────────────┐                  │
│       │  Payment     │         │   Supplier       │                 │
│       │  Gateways    │         │   Portal         │                 │
│       │(PayMongo,   │         │                   │                 │
│       │ Dragonpay)  │         └─────────────────┘                  │
│       └─────────────┘                                               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 4. Security Reference Requirements

These are the active security controls implemented across the unified ERP platform.

| Area | Expectation |
|---|---|
| **Access Control** | Role-based access control (RBAC) with per-entity, per-location, per-function permissions |
| **Audit Trail** | All financial and inventory transactions must have immutable audit logs |
| **Data Encryption** | Encryption at rest and in transit for all sensitive data |
| **POS Security** | Endpoint protection on all POS devices; tamper-resistant payment processing; BIR CAS registration per location |
| **Customer Data** | RA 10173 (Data Privacy Act) compliance; consent management; data subject access requests |
| **Vulnerability Management** | Regular patching; annual penetration testing |
| **Compliance** | SOC 2 Type II or ISO 27001 certification target for ERP provider |

---

## 5. Multi-Vendor Sourcing-Architecture Reference

> Added with the hybrid capability-sourcing decision (2026-09-03); **re-scoped 2026-09-14 to
> the two-tier doctrine** — the EBS suite (incl. Oracle WMS/MSCA and Shipping/Transportation
> Execution) is the **in-suite core**; the already-built POS/ecommerce platforms and the
> in-house builds (OMO/TPS, Payroll PH, store workforce) surround it (see
> [`capability-sourcing-and-engineering-model.md`](capability-sourcing-and-engineering-model.md)
> and `model-company-profile.md` §14.1). The external integration clusters of §3.2 and
> `data-volumes-and-integrations.md` are unchanged; this section governs the
> **product-to-product** integration layer.

| Rule | Requirement |
|---|---|
| **Single integration path** | Every product-to-product flow runs on the IAP middleware/event backbone (published event or API contract). Direct database-to-database access between products is prohibited. |
| **Canonical contracts** | IAP owns the canonical event/API contract catalog with consumer-driven contract tests; every consuming product pins a contract version and passes tests in CI before release. |
| **Inventory truth** | The ERP remains the inventory **ledger of record**; Oracle WMS/MSCA (in-suite) owns execution state. Stock-truth reconciliation runs as a continuous IAP-monitored flow (drift alerting, replay from last-acknowledged sequence — same at-least-once/idempotency semantics as the POS event bus in §1). |
| **POS offline resilience preserved** | No sourcing decision may weaken the ≥ 8h offline POS architecture and event replay of §1 — the POS/omnichannel commerce core stays in the ERP. |
| **Built products (OMO/TPS)** | Deploy on the SEP paved road (golden-path templates, feature flags, ring deployment); expose only IAP contracts; publish datasets to DP under tested data contracts. |
| **Vendor release intake** | Vendor commodity releases and in-suite RUPs/CPUs pass the owning team's staging ring and the Tier-1 regression pack before production (same standard as ERP vendor releases). |
| **Statutory boundary** | BIR/SSS/PhilHealth/Pag-IBIG filing acts remain human-confirmed: Payroll PH (built) computes statutory results and generates outputs, and no product — built or otherwise — may complete a statutory filing autonomously; the EBS ledger of record receives payroll postings (fit-gap E8). |
| **DR posture** | Every product — in-suite, already-built, or built — must meet the §2.3 DR/BCP targets and join the annual pre-typhoon-season exercise; ring-deployed built products must demonstrate rollback within the exercise. |

---

## 6. Agentic Runtime Reference

> Added with the agentic-AI extension (2026-09-03, OM v2.1): AI agents that execute manual
> tasks run on the **AI & Agent Platform (AAP)** runtime under VS-128 governance. Full program
> definition in [`capability-sourcing-and-engineering-model.md`](capability-sourcing-and-engineering-model.md)
> §12; the rules below are the runtime's non-negotiables.

| Rule | Requirement |
|---|---|
| **Tools are contracts** | An agent's action surface is the AAP tool registry, and every tool wraps an IAP-published event/API contract. Agents never touch another product's database, file share, or admin console directly. |
| **Non-human identity** | Every agent runs under its own registered identity with least-privilege ERP/product roles; SEC's access reviews and SOD enforcement cover non-human identities exactly as for humans; an agent may never hold SoD-conflicting roles (e.g., vendor-create + payment-approve). |
| **Autonomy ladder** | Tier-1 workflows: human-approval-gated only (agent drafts, a named human decides — approval-matrix evidence retained). Tier-2: bounded autonomy inside hard guardrails (value caps, whitelists, sampled audit). Tier-3: autonomous-in-bounds with full audit trail. Promotion between rungs requires evaluation evidence and Tier & Control Board sign-off when Tier-1 workflows are touched. |
| **Statutory boundary** | No agent owns a BIR/SSS/PhilHealth/Pag-IBIG filing path — the terminal step on any statutory workflow is a human sign-off (extension of the §5 statutory rule). |
| **OT/POS exclusion** | No agent may act on the POS terminal estate, RF guns, or OT/ICS surfaces; consumption of their event streams is permitted. |
| **Registration & kill-switch** | Every agent is registered in the VS-128 registry (risk tier, owner team, tools, guardrails) before first production action; the kill-switch reverts to rule-based fallback instantly; quarterly re-registration or retirement. |
| **Evaluation gates** | Offline evals → shadow mode (no actions) → canary (bounded, sampled) before any production autonomy; graduation signed by the AAP evaluation engineer and the owning team's QA analyst. |
| **Audit as control evidence** | Every agent action, approval, escalation, and override is immutably logged and mapped to the 808-control register — agent audit trails are audit evidence, not telemetry nice-to-haves. |
| **Privacy** | Agents processing personal data operate under VS-128's RA 10173 automated-decision/profiling rules and VS-91; DPIA before any agent making decisions about data subjects. |
| **Foundation-model vendors** | LLM/API providers are tier-1 TPRM vendors (VS-161): data-processing terms, PH data handling, no training on BuildRight data without explicit approval, model-change notification clauses. |
| **Cost telemetry** | Per-agent, per-task token/cost telemetry is mandatory (FinOps-tagged to the owning product); runaway-cost kill thresholds are guardrail parameters. |

---

*Document Version: 3.3 | Date: 2026-09-14 | §5 re-scoped to the two-tier sourcing doctrine (sourcing model v3.0): in-suite Oracle WMS/MSCA + Shipping/OTE (BoB WMS/TMS superseded), vendor-commodity release intake, statutory boundary re-worded for the built Payroll PH (human-confirmed filing acts; EBS ledger of record via postings), DR posture wording. No §1–§4/§6 changes. Prior v3.2 (2026-09-03): §6 blockquote continuation lines re-prefixed (the v3.1 note's second and third lines had lost their `>` markers — formatting only, no content change). Prior v3.1 (2026-09-03): §6 agentic runtime reference added with the agentic-AI extension (OM v2.1): tools-are-contracts, non-human identity & SoD, Tier-based autonomy ladder, statutory-boundary extension (human sign-off on filings), OT/POS exclusion, VS-128 registration & kill-switch, evaluation gates, audit-as-control-evidence, privacy/DPIA rules, foundation-model vendors as tier-1 TPRM, cost telemetry. Prior v3.0 (2026-09-03): §5 multi-vendor sourcing-architecture reference added with the hybrid capability-sourcing decision (single integration path, canonical contracts, inventory-ledger-of-record rule, POS-offline preservation, SEP paved road, vendor release intake, statutory boundary, DR posture). Prior v2.5 (2026-06-26): §2.2 HQ bandwidth row reconciled with the 2026-06-25 headcount change — `~357 HQ staff (≈320 concurrent users)` → `~362 HQ staff (≈325 concurrent users)` (the +5 Supply Chain & Logistics S&OP/IBP sub-team; concurrent estimate held at the same ~90% ratio). §2.1 already carried 6,762 employees. Prior v2.4: §3.1 fixed broken in-page anchor `#143-integration-touchpoints` → `#143-active-integration-touchpoints` to match the `### 14.3 Active Integration Touchpoints` heading in `model-company-profile.md` (same fix applied to NFR-012 in `erp-requirements.md`). Prior v2.3: §2.3 Data-retention row and §2.3 backup archive updated to **10 years (BIR per TRAIN/NIRC — Sec. 235, as amended by RA 10963)**; was 7 years. Prior v2.2: Integration diagram canonical reference updated; bank list reconciled to 4 banks (BDO, BPI, Metrobank, Chinabank); POS offline-capacity figure tied to the documented 2.0× peak factor (~933/store peak-day); counts reconciled with README.md*
