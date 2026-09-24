# BuildRight Depot Corp. — Executive Summary

> One-page overview of the model company and its IT landscape — Oracle E-Business Suite 12.2 as the in-suite ERP core, with built and already-built platforms around it under the two-tier doctrine — for C-suite stakeholders.

---

## The Company

**BuildRight Depot Corp.** is a model big-box hardware/home improvement retail chain in the Philippines, operating with all its capabilities and systems fully enabled on a modern hybrid IT landscape: the ERP core of record — **Oracle E-Business Suite 12.2**, realized in `02-oracle-ebs/` under the two-tier sourcing doctrine (*if it's in EBS we use it; otherwise we build*) — plus **in-house built** and **already-built** differentiating platforms (sourcing governed by `07-methodology/capability-sourcing-and-engineering-model.md`).

| Parameter | Value |
|---|---|
| Format | Hardware / DIY / Home Improvement Big Box |
| Stores | 200 (nationwide: Luzon, Visayas, Mindanao) |
| Distribution Centers | 4 (Davao, Cebu, Laguna, Clark) |
| HQ | Davao City, Philippines |
| Legal Entities | 5 (Holdings, Depot, Logistics, Digital Commerce, Property Mgmt) |
| Annual Revenue | ~PHP 62.3 Billion |
| Employees | 6,918 active (Trade / Account Management disabled — prepared (x); the IT estate's TPS build squad deferred — prepared (ad); the TO design holds 532 HQ) |
| Active SKUs | 35,000 |
| POS Terminals | 600 (3 per store) |
| Monthly Transactions | 2.8 million |
| Ecommerce | Yes — BOPIS (Buy Online, Pick Up In Store) + Home Delivery |
| Loyalty Members | ~600,000 |

---



## IT Landscape (Two-Tier Doctrine — In-Suite Core + Built & Already-Built Platforms)

The business runs on **Oracle E-Business Suite 12.2** as the in-suite ERP core under the two-tier sourcing doctrine (2026-09-14: *if it's in EBS we use it; otherwise we build*); warehouse and transport execution run in-suite, and every differentiating capability is built in-house or already built:

| Platform | Provider | Status |
|---|---|---|
| ERP Core — Oracle E-Business Suite 12.2 (financials, P2P, inventory ledger, POS masters & posting, HR core, approvals) | In-suite (realization blueprint: `02-oracle-ebs/`) | Fully Operational (core) |
| Warehouse & transport execution — Oracle WMS/MSCA, Shipping/Transportation Execution | In-suite (two-tier doctrine) | Fully Operational (in-suite) |
| Order Orchestration (OMO) | Built in-house (SEP paved road) | Fully Operational (differentiator) |
| Trade & Project Services (TPS) | Built in-house (SEP paved road) | Deferred — prepared (2026-09-23 (ad): the squad's 7 seats stand down with the trade desk disabled (x); project services dormant; consumer bulky install/haul-away rides the in-suite Field Service dispatch core and the dispatch experience layer; re-stands at CAP-B01 re-enablement) |
| Already-built platforms — POS estate, ecommerce platform, gift-card/loyalty stack | Built in-house (existing; integrated via the IAP/event backbone) | Fully Operational (integrated) |
| Payroll PH · store workforce scheduling · the dispatch experience layer (Field Service dispatch core in-suite) | Built in-house | Fully Operational (builds) |
| AI & Agent Platform (AAP) | Built in-house on bought foundation-model APIs (VS-128 governance) | Fully Operational (agentic automation) |

---

## Critical Requirements

The ERP must handle these non-negotiables:

1. **High-volume retail POS** — 2.8M transactions/month, 600 terminals, offline capability (≥ 8 hours), real-time event-driven architecture
2. **Multi-entity Philippine operations** — 5 legal entities with intercompany consolidation, BIR (Bureau of Internal Revenue) compliance (VAT, EWT/Expanded Withholding Tax, income tax), SSS (Social Security System)/PhilHealth (Philippine Health Insurance)/Pag-IBIG (Home Development Mutual Fund) payroll
3. **Complex supply chain** — 4 DCs, import management (LC, customs, landed cost), catch-weight items (lumber, wire), consignment, VMI
4. **Omnichannel with multi-origin fulfillment** — BOPIS + home delivery + ship-from-store + drop-ship with real-time inventory sync across 200 stores; mixed-basket orders from a single POS transaction
5. **Scalability** — must grow to 300+ stores without architectural limits

---

## Key Operational Metrics

| Metric | Target | Rationale |
|---|---|---|
| POS uptime | 99.9% | Revenue stops if registers go down |
| POS offline endurance | ≥ 8 hours | Philippine internet reliability |
| Month-end close | ≤ 5 working days | Financial reporting agility |
| Inventory accuracy | ≥ 97% | Shrinkage control at PHP 62B scale |

---

## Repository Structure

```
erpplans/
├── 01-model-company/       ← Company profile, requirements, and workflows (LIVE)
├── 02-oracle-ebs/          ← Oracle EBS 12.2 platform blueprint (the ERP core of record)
├── ebs_docs/               ← Oracle EBS R12.2 official documentation library (376 guides / 133,782 pages; reconciled against this model by 02-oracle-ebs/ebs-documentation-coverage.md)
├── bpmn/                   ← Generated BPMN 2.0 process models (5,456 processes; regenerates via 07-methodology/generate-bpmn.py)
├── dmn/                    ← Generated DMN 1.3 decision models (80 decisions; regenerates via 07-methodology/generate-dmn.py)
└── 07-methodology/         ← Technical guidelines & reference specs (see 07-methodology/README.md; platform selection recorded in 02-oracle-ebs/)
```

---

## Ongoing Operations & Maintenance

1. Monitor live interfaces and transaction queues across all 200 stores and 4 distribution centers.
2. Maintain compliance with BIR requirements, including e-invoicing and statutory reporting.
3. Review nightly intercompany reconciliations and monthly financial consolidation routines.
4. Periodically audit active workflows against standard operating procedures.

---

*Date: 2026-09-23 (TPS build squad deferred — prepared, 2026-09-23 (ad): with the trade desk disabled (x) the TPS build squad's project-side workload is dormant; by direction the squad's 7 seats defer — IT 122 → 115 active, 16 of 17 teams active, the 122-FTE 17-team design of record retained (OM v3.25; sourcing register §4 amendment, v3.15; TO v3.1); consumer bulky install/haul-away rides the in-suite Field Service dispatch core and the dispatch experience layer; active headcount re-based 6,925 → 6,918 (HQ 518), revenue/employee ~PHP 9.01M — 728 requirements, 5,433 workflows, 188 value streams, 6,918 employees — HQ 518 — see CHANGELOG 2026-09-23 (ad)).*
*Date: 2026-09-23 (trade-desk disablement, 2026-09-23 (x): the Trade / Account Management department (7 HQ roles) is DISABLED — PREPARED — not staffed, design retained (TO §5.3; registry CAP-B01–B04); B2B customers are retail POS customers at any store — every sale still completes as a regular POS sale; active headcount re-based 6,932 → 6,925 (HQ 525), revenue/employee ~PHP 9.00M — 728 requirements, 5,433 workflows, 188 value streams, 6,925 employees — HQ 525 — see CHANGELOG 2026-09-23 (x)).*

*Date: 2026-09-23 (capability-switchboard admission, batch 30: W5580 Capability Switchboard Operation & Channel Enablement Impact Governance added in PA-113.2 (VS-113) — the owning workflow for the channel-capability registry's enable/disable state changes; corpus 728 requirements, 5,433 workflows, 188 value streams, 6,932 employees — HQ 532 — unchanged otherwise; see CHANGELOG 2026-09-23 (v)).*

*Date: 2026-09-14 (structure promotion — the adopted optimal table of organization is promoted to the actual structure of record (TO v2.3; profile v3.0): HQ 511 / total 6,911, IT = 122 as the 17-team product-centric department (OM v3.13); the Employees row above re-based 6,762 → 6,911 — 728 requirements, 5,432 workflows, 188 value streams unchanged).*

*Date: 2026-09-14 (twentieth-wave consistency review — IT-landscape section trued to the two-tier sourcing doctrine enacted the same day (sourcing model v3.0): the banner, the Company overview and the landscape section no longer describe the retired hybrid posture ('unified cloud ERP core provided by a theoretical software vendor, surrounded by best-of-breed edge products'); the ERP core of record is Oracle E-Business Suite 12.2 (realization blueprint `02-oracle-ebs/`), warehouse/transport execution runs in-suite (Oracle WMS/MSCA, Shipping/Transportation Execution), and the landscape table now lists the in-suite core, the in-suite execution tier, the built differentiators, the already-built POS/ecommerce/loyalty platforms, the Payroll PH/workforce/dispatch builds and the AAP; no figures move — 728 requirements, 5,427 workflows, 188 value streams, 6,762 employees unchanged).*
*Date: 2026-09-10 (repository-structure rows added for the generated `bpmn/` and `dmn/` model trees — 569 BPMN process files / 40 DMN definitions regenerated from this corpus by `07-methodology/generate-bpmn.py` / `generate-dmn.py`; counts as of the 2026-09-10 batch-24 update: 728 requirements, 5,432 workflows across 188 value streams, 6,762 employees — W5574 concessionaire connectivity request, approval & independent-circuit governance added by the batch-24 gap-fill pass ([workflow-gap-analysis.md](workflows/workflow-gap-analysis.md)) in PA-07.1, owning the contract-governed exception path when a concessionaire wants its own internet circuit — BuildRight-provided-utility default restated, segmented Wi-Fi on the BuildRight link evaluated first, eligibility gate, isolation envelope, connectivity addendum with incident demarcation and the commission-integrity clause, restoration holdback at exit — 1 confirmed Tier 2; prior 2026-09-05 (batch-23): 5,426 workflows — W5570–W5573 gas-leak, tsunami/storm-surge, media-exposé & server-room-environmental workflows added by the batch-23 gap-fill pass ([workflow-gap-analysis.md](workflows/workflow-gap-analysis.md)): gas-leak event response (LPG/natural-gas odor on premises) in PA-24.2, tsunami & storm-surge coastal-intrusion response in PA-26.1, undercover-investigation & media-exposé response in PA-14.3, and server-room & data-center environmental event response in PA-27.2 — 2 confirmed Tier 1, 2 Tier 2; the same pass added the custody register's tenth wave (events E-46–E-49); prior 2026-09-05: W5566–W5569 terminal-tampering, procurement-impersonation, account-takeover & commute-disruption workflows added by the batch-22 gap-fill pass ([workflow-gap-analysis.md](workflows/workflow-gap-analysis.md)): payment-terminal tampering & card-skimmer response in PA-08.2, procurement-impersonation & fake-PO goods-diversion response in PA-03.2, official-channel account-takeover response in PA-14.2, and mass-commute disruption & transport-strike continuity in PA-141.2 — 4 confirmed Tier 2; the same pass added the custody register's ninth wave (events E-42–E-45); prior 2026-09-05: W5558–W5561 cyber-extortion, payment-diversion, land-occupation & water-continuity workflows added by the batch-20 gap-fill pass ([workflow-gap-analysis.md](workflows/workflow-gap-analysis.md)): ransomware & destructive cyber-attack enterprise response in PA-27.3, vendor payment-diversion & BEC fraud response in PA-18.2, informal-settler invasion of banked land in PA-178.1, and sustained water-service interruption response in PA-07.2 — 1 confirmed Tier 1, 3 Tier 2; the same pass added the custody register's seventh wave (events E-34–E-37); prior 2026-09-05: W5554–W5557 in-transit-security, fatality-scene, tampering-extortion & recruitment-fraud workflows added by the batch-19 gap-fill pass ([workflow-gap-analysis.md](workflows/workflow-gap-analysis.md)): in-transit cargo hijacking & driver-safety first response in PA-06.2, customer/visitor death-on-premises scene protocol & trading-continuity decision in PA-147.3, product-tampering threat & merchandise-integrity sweep protocol in PA-89.1, and recruitment-fraud/fake job-offer scam response & victim guidance in PA-121.1 — 2 confirmed Tier 1, 2 Tier 2; the same pass added the custody register's sixth wave (events E-30–E-33); prior 2026-09-05: W5550–W5553 channel-enforcement, employee-legal-status, OSH-enforcement & app-store-removal workflows added by the batch-18 gap-fill pass ([workflow-gap-analysis.md](workflows/workflow-gap-analysis.md)): marketplace account suspension, enforcement freeze & appeal recovery in PA-10.3, employee arrest/detention & criminal-case employment-status response in PA-19.1, DOLE imminent-danger work-stoppage order response in PA-24.1, and mobile app store removal & re-listing recovery in PA-75.1 — 1 confirmed Tier 1, 3 Tier 2; the same pass added the custody register's fifth wave (events E-27–E-29); prior 2026-09-05: W5544–W5549 regulatory-shock, platform-outage & governance-continuity workflows added by the batch-17 gap-fill pass (workflow-gap-analysis.md): emergency executive succession & decision-rights continuity in PA-36.1, BIR Oplan Kandado enforcement-closure response and eFPS/portal-outage filing contingency in PA-79.3, card-network/acquirer outage response in PA-08.1, stored-value & loyalty platform outage protocol in PA-54.2, and suicide/self-harm incident response & psychosocial aftermath in PA-24.1 — 2 confirmed Tier 1, 4 Tier 2; the same pass added the custody register's fourth wave (events E-23–E-26); prior 2026-09-05: W5536–W5543 emergency & continuity workflows added by the emergency & continuity gap-fill pass ([workflow-gap-analysis.md](workflows/workflow-gap-analysis.md) batch 16), owning the missing-child/Code Adam response and elevator/escalator entrapment response in PA-07.2, the fire-event response & post-fire BFP clearance and bomb-threat response in PA-24.2, the payroll run failure & emergency off-cycle payment in PA-19.2, the bank-failure/frozen-deposit contingency in PA-18.3, the liquidity-stress & payment-prioritization escalation in PA-105.3, and the price-file integrity event & mass-mispricing rollback in PA-118.2 end-to-end — 3 confirmed Tier 1, 5 Tier 2; the same pass added the custody register's third wave (events E-19–E-22); prior 2026-09-04: W5535 capability demand-intake & backlog-triage workflow added by the demand-intake gap-fill pass (workflow-gap-analysis.md batch 15), owning the stakeholder capability-demand front door — raise → log & triage → route (team backlog / workflow-catalog gap-admission / W5515 sourcing gate) → Product-Council capacity funding — end-to-end in PA-113.2 (VS-113) — 1 confirmed Tier 2; prior 2026-09-04: W5532–W5534 operations-workflow gap fills added by the operations-workflow gap-fill pass ([workflow-gap-analysis-operations.md](workflows/workflow-gap-analysis-operations.md)), owning the workforce time-&-attendance (biometric/time-clock) platform-estate & punch-data surface in PA-19.3, the BIR Form 2316 annual-issuance/acknowledgment/certificate-lifecycle surface in PA-79.2, and the company-property gate-pass & asset-exit control surface in PA-23.2 end-to-end — 1 confirmed Tier 1, 2 Tier 2; prior 2026-09-03: W5529–W5531 finance-workflow gap fills added by the finance-workflow gap-fill pass ([workflow-gap-analysis-finance.md](workflows/workflow-gap-analysis-finance.md)), owning the utility/telecommunications/site deposits-paid lifecycle (register, interest reconciliation, surety replacement & recovery-on-closure) in PA-42.3, the minimum corporate income tax (MCIT) computation/regime-evaluation/excess-credit carry-forward surface in PA-17.3, and the PFRS 8 operating-segment reporting & CODM disclosure-package surface in PA-17.4 end-to-end — 2 confirmed Tier 1, 1 Tier 2; prior 2026-09-03: W5525–W5528 people-capability & reporting-policy workflows added by the people-workflow gap-fill pass ([workflow-gap-analysis-people.md](workflows/workflow-gap-analysis-people.md)), owning the learning-platform (LMS) administration/integration/learning-records, learning-content development & course-catalog lifecycle, and leadership development & management-capability (HiPo) surfaces in PA-19.4 plus the accounting-policy/technical-accounting (PFRS) & new-standard adoption surface in PA-17.4 end-to-end — 4 confirmed Tier 2; prior 2026-09-03: W5518–W5524 IT operating-model workflows added in VS-27 by the IT workflow gap-fill pass ([workflow-gap-analysis-it.md](workflows/workflow-gap-analysis-it.md)), owning the collaboration/productivity tenant (M365/email/Teams), store telephony/UCC, core network services & IPAM, enterprise release calendar & peak-season change freeze, ISMS/security certification & policy lifecycle, enterprise pentest/red-team & attack-surface management, and enterprise DLP & insider-risk monitoring surfaces end-to-end — 5 confirmed Tier 2, 2 Tier 3; prior 2026-09-03: W5515–W5517 capability-sourcing & engineering workflows added in VS-113 by the sourcing-model gap-fill pass, owning the hybrid sourcing machinery end-to-end (W5515 Sourcing Decision Gate Operation & Capability Sourcing Register in PA-113.3, W5516 Best-of-Breed Product Lifecycle Management, Vendor Release Intake & Exit Reserves in PA-113.2, W5517 SEP Paved Road & Engineering Standard Governance for Built Products in PA-113.1 — sourcing model §3–§9); prior 2026-09-03: W5512–W5514 agentic-AI platform lifecycle workflows added in VS-128.3 by the agentic gap-fill pass, owning the sourcing-model §12 agent lifecycle end-to-end (intake/sourcing/registration, shadow & canary evaluation with autonomy-tier ratification, runtime/guardrail/kill-switch telemetry with quarterly re-registration & sunset); W5511 gift-card dormancy/escheat/expired-liability derecognition added in VS-54.3 by the event-custody pass; the IT landscape re-framed by the hybrid capability-sourcing decision — unified ERP core + best-of-breed edges + in-house OMO/TPS differentiators on the SEP paved road — plus the AI & Agent Platform agentic extension, per `07-methodology/capability-sourcing-and-engineering-model.md` and `07-methodology/it-product-operating-model.md`; prior 2026-08-26: post-catalog batch 5 added — W5510 supplier service-fee billing & account deduction for store-rendered services (barcode labels & promotional collaterals), transposing the concessionaire W5507 pattern onto merchandise suppliers and settling via W770 debit memos against AP — joining the 2026-08-24/25/26 thirteen: fringe benefits tax determination & quarterly BIR 1605 filing, unfulfilled-demand & lost-sales capture, concession item catalog/barcode/label governance, concessionaire self-service price change & label-first propagation, concession service-fee billing, restricted-substance & chemical-content product compliance, extreme-heat work interruption & heat-stress management, POSH/Safe Spaces CODI, RA 11165 telecommuting, director education, customer digital accessibility/WCAG, climate physical & transition risk, and employee financial wellness).
*Corrected 2026-08-24 — consistency review #25:* the 2026-06-25 footer below recorded 733 requirements; review #22 (2026-08-24) subsequently removed five exact-duplicate requirement rows (733 → 728; 429 Must / 293 Should / 6 Nice). Original 2026-06-25 note: VS-127 PA-127.4 added — 8 workflows W5489–W5496 — specializing the S&OP/IBP consensus cycle for BuildRight's PH-retail context; total headcount 6,757 → 6,762 with the dedicated S&OP/IBP sub-team in Supply Chain & Logistics; VS-49–VS-52 retired after placeholder-content review; VS-89–VS-192 added across thirty gap-analysis passes — see [CHANGELOG.md](../CHANGELOG.md) and [`workflow-gap-analysis.md`](workflows/workflow-gap-analysis.md) for per-pass detail.*
