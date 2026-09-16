# 02 — Oracle E-Business Suite Platform Blueprint

> BuildRight Depot Corp.'s ERP core of record is **Oracle E-Business Suite (EBS) Release
> 12.2**. This folder realizes the model company — [`01-model-company/`](../01-model-company/)
> (728 requirements · 188 value streams · 5,427 workflows · 808 controls) — on the EBS
> platform under one governing doctrine: **maximize standard EBS; configure before
> personalizing; personalize before extending; localize only where Philippine statute
> demands it; build in-house only where the sourcing register says the market cannot
> serve us.**

Back to the [root README](../README.md).

---

## 1. The Platform Decision (Summary)

| Decision | Choice | Rationale |
|---|---|---|
| ERP core of record | **Oracle E-Business Suite 12.2** (latest Release Update Pack; 12.2.12 baseline at blueprint time) | Deepest standard fit for the Core tier (financials, procure-to-pay, inventory ledger, intercompany, statutory tax); one financial control surface for all 5 legal entities and the 808-control register; committed vendor support horizon (Premier Support through at least December 2034 under Oracle's rolling commitment — re-verify the current MOS note at contract time) |
| Deployment model | **On-premises deployment** — BuildRight-controlled data centers (colocation permitted; no public-cloud hosting) with a DMZ tier for iSupplier/external integrations | Oracle EBS is an **on-premises suite, not a cloud/SaaS ERP** — the platform of record runs in facilities under BuildRight control; data residency (RA 10173) is fully under BuildRight control |
| Customization doctrine | **Two-tier sourcing (2026-09-14): if it's in EBS we use it — otherwise we build.** No best-of-breed capability buying; CEMLI-governed extensions only where EBS function is genuinely short ([fit-gap](fit-gap-analysis.md)) | The user doctrine: make the most of the suite; customize only for gaps; buy nothing a build isn't forced to replace |
| Philippine statutory layer | eBTax configuration + the EBS-held **BIR indirect-tax pack** (2307, VAT datasets, CAS inventory lists); **payroll statutory is an in-house build** posting journals to EBS | The payroll engine and its BIR compensation outputs are ours (built, not bought); EBS keeps the indirect-tax localization and the ledger |
| Warehouse & transport execution | **In-suite: Oracle WMS/MSCA + Shipping/Transportation Execution** — adopted under the two-tier doctrine (in EBS → use it) | Resolves the sourcing register's BoB WMS/TMS rows; no best-of-breed buying |
| Already-built platforms (integrate, never rebuild) | **POS estate** (in-house), **custom ecommerce platform** (in-house), **gift-card/loyalty stack** (in-house) | The POS program is integration — flows W533–W541 onto EBS masters and posting — not sourcing |
| In-house builds (new scope) | Payroll PH (engine + statutory outputs), store workforce scheduling & time capture (the genuinely-absent shift-scheduling/optimization layer — Oracle Time & Labor covers timecards, not retail planning), the dispatch experience layer (consumer appointment/route-optimization/contractor portal — the Field Service dispatch core is in-suite, fit-gap D13), space-planning; plus OMO (omnichannel orchestration), TPS (trade & project services), AAP (agentic runtime), IAP (integration platform), DP (data platform) | Register §4 builds + the two-tier doctrine's new scope, each scoped to what the suite genuinely does not ship (the 2026-09-15 exhaustion audit re-pointed the dispatch core in-suite — Field Service, D13 — and timecards to OTL) |
| Foundation-model access | Vendor LLM APIs under tier-1 TPRM contracts | Commodity API procurement, not capability sourcing — the one remaining vendor product line, unchanged |

**Consistency with the sourcing model.** The 2026-09-14 two-tier decision (*in EBS → use it;
otherwise → build*) supersedes the Capability Sourcing Register's four Buy rows
(WMS/TMS/WFM/FSM) and records POS, ecommerce and the loyalty/gift-card stack as
**already-built in-house platforms**. The resolution record and the register amendment
schedule live in [fit-gap §4](fit-gap-analysis.md) (adopted via the W5515 gate's decision
rights); the sourcing-model rewrite shipped the same day (sourcing v3.0, OM v3.11).

---

## 2. Guiding Principles (the "Make the Most of It" Doctrine)

1. **Standard first.** A workflow touchpoint is served by unmodified EBS unless a documented
   gap proves otherwise. The burden of proof sits with the customizer, not the standard.
2. **Configure > Personalize > Extend > Localize > Build.** The lowest CEMLI tier that
   closes the gap wins. "Build" splits two ways: custom code *inside* EBS (CEMLI extensions,
   budget-capped) and in-house products *outside* EBS (the two-tier doctrine's build tier).
3. **Zero modifications (M).** No base-product changes: no Forms modification, no base-table
   DML, no patch-overrides. This is what keeps quarterly Critical Patch Updates and Release
   Update Packs installable without rework.
4. **Upgrade-safe extensions only.** Custom code lives in a custom schema/top (`BDR`),
   registers in the EBS object registry, and follows the online-patching (editioned
   redefinition) rules so ADOP cycles never break on custom objects.
5. **One control surface.** Every workflow's Controls section (CTL-01 – CTL-808) maps to an
   EBS function, setup, AME rule, or interface control — evidence must come from EBS or the
   system the register assigned, never from a spreadsheet beside it.
6. **De-customization triggers.** Every extension carries a review trigger: if a future RUP
   ships the function, the extension is retired (the sourcing register's re-evaluation
   discipline applied *inside* the suite).

---

## 3. Document Map

| Document | What it answers |
|---|---|
| [`ebs-platform-architecture.md`](ebs-platform-architecture.md) | The target platform: organization/ledger model for 5 legal entities · 200 stores · 4 DCs; the EBS module footprint; tech stack (12.2 RUP, Database 19c, WebLogic, ADOP online patching); environment strategy; integration and security architecture |
| [`module-coverage-map.md`](module-coverage-map.md) | "Make the most of it" — the register mapping every generic ERP module in the [workflow-system-touchpoint-map](../01-model-company/workflows/workflow-system-touchpoint-map.md) to the specific EBS module and setup that serves it, per value-stream family |
| [`fit-gap-analysis.md`](fit-gap-analysis.md) | The gap discipline: fit classes (FIT-STD/FIT-CFG/PER/EXT/LOC/INT/BUILD; EDGE retired), the capability disposition register (97 rows incl. the 2026-09-15, 2026-09-16 second-pass and 2026-09-16 third-pass EBS-exhaustion audits: Field Service dispatch core, Lease & Finance Management, Internet Expenses, Teleservice, Advanced Benefits, eAM, Procurement Contracts, Revenue Management & Invoicing (retiring the PFRS 15 extension), Global Order Promising, Oracle Configurator (in-store), In-Memory Cost Management, GL budgetary control, Oracle Alert, then AR Lockbox/Balance Forward Billing/iReceivables (A14), Purchasing Contingent Labor (B13), Engineering ECO/ECN (C17), Install Base + Service Contracts (D16), Depot Repair (D17) and Compensation Workbench (E10) with the Bills-Receivable/rental-family/Product-Hub/Site-Hub/GoldenGate realization trues, then a fourth pass truing three more realization notes (AP Bills Payable outgoing-PDC register A3, eAM delivery-fleet estate F5, Performance Management appraisals E2), then a fifth pass truing the DC workflows' warehouse-optimization vehicle names onto the adopted WMS product's own advanced-function family (WMS Slotting W784/W1402, planned crossdocking W221/W1226/W1279/W1307, WMS Labor Management W796, WMS Yard Management W222/W585/W1353, Cartonization W3099 — C6) and naming Oracle Succession Planning for the W178 talent chain (E2), then a sixth pass adopting Oracle Internal Controls Manager as the VS-21 audit-management/GRC surface (H11 — the workflows' 'Audit Management portal / GRC Tool' touchpoints named the suite's own GRC module; register 96 → 97 rows, standard share 76.0% → 76.3%) and truing H8's environment lifecycle to Rapid Clone + Oracle iSetup), then a seventh pass sweeping the adopted-vehicle class across the workflow corpus — the generic 'audit management system / GRC module', 'facility maintenance module / CMMS', 'lease management module', 'contract management system', 'warranty module', 'rebate module', 'expense modules', 'bank reconciliation module', 'ATP module' and 'benefits / performance management / recruitment module' rows trued to the adopted products (ICM, eAM, Property Manager, Procurement Contracts, Install Base, Trade Management, iExpenses, Cash Management, GOP, OAB/Performance Management/iRecruitment; eleven register rows' evidence extended, no count movement, §4 resolution 31), then an eighth pass naming the remaining adopted-vehicle classes — the 'Inventory/ATP system' availability rows (GOP/INV), the 'demand planning module' rows (Demantra), the four 'Transportation Management System (TMS)' rows (in-suite Shipping/Transportation Execution) and the generic quality-system rows (Oracle Quality) — and truing W5525's learning-platform administration onto the in-suite OLA per resolution 5 (the vendor-SaaS posture vocabulary retired; the vehicle-sense LMS touchpoints corpus-wide name OLA; no count movement; §4 resolution 32)), the resolution record for the formerly-open buy decisions, the Philippine statutory split (EBS-held vs payroll-built), requirement-section (R1–R32) disposition view, and the standard-first KPIs |
| [`customization-governance.md`](customization-governance.md) | How customization stays under control: CEMLI framework operationalized, the Customization Decision Record (CDR) workflow, naming/technical standards, online-patching-safe coding rules, the CEMLI register, de-customization triggers, KPIs |
| [`integrations.md`](integrations.md) | EBS-specific integration patterns for every flow in the canonical [integration architecture](../01-model-company/data-volumes-and-integrations.md): the already-built POS estate and ecommerce platform, in-suite WMS, the in-house builds, banks, BIR/eFPS, statutory bodies, payment gateways, iSupplier — via open interfaces, ISG REST/SOAP, business events, and IAP contracts |
| [`data-migration.md`](data-migration.md) | Loading the model company into EBS: per-object load paths (open interfaces & public APIs), sequence, and validation tied to [`data-migration-mapping.md`](../01-model-company/data-migration-mapping.md), W73 parallel-run and W385 data-quality gates |

---

## 4. Realization Waves (Aligned to the Tier Register)

Go-live follows the workflow criticality tiers
([`workflow-criticality-classification.md`](../01-model-company/workflows/workflow-criticality-classification.md)):
Tier 1 (1,396 workflows) reaches production first or is protected by an equivalent manual
procedure during cutover; Tier 2 (3,296) and Tier 3 (758) follow. The wave plan in full
detail is an implementation-phase deliverable (07-methodology "Future Additions"); the
platform-level wave shape is:

| Wave | Scope | EBS modules | Canon anchors |
|---|---|---|---|
| **W0 — Foundation** | Environments, org/ledger model, CoA, eBTax, security model, CEMLI standards | FND, GL, eBTax, SLA | 5 legal entities, chart of accounts, BIR setup |
| **W1 — Financial core & P2P** | AP/AR/GL close, procurement, iProcurement, iSupplier, treasury cash | AP, AR, PO, CE, XTR, AME | VS-15, VS-17, VS-18; 5-day close (FIN KPI) |
| **W2 — Supply chain ledger** | Item master, inventory orgs, receiving, costing, landed cost, transfers | INV, PO, LCM, BOM, QA | VS-01–VS-05, VS-29; 35,000 active SKUs |
| **W3 — Order-to-cash & retail spine** | Trade/corporate orders, advanced pricing, credit, collections; POS/ecommerce integration go-live | OM, QP, AR, IBY | VS-07/08/10/11/16; 200 stores |
| **W4 — People** | Core HR + in-house payroll build integration (posting, statutory outputs live in the build) | PER + payroll-build interfaces | VS-19, VS-79; 6,911 employees |
| **W5 — Projects, assets, property** | Capex/CIP, fixed assets, lease admin + PFRS 16 extension | PA, FA, PN + EXT | VS-20/35/40/42/148 |
| **W6 — Optimization** | ECC dashboards, de-customization pass, RUP currency | ECC, Web ADI | Tier 3 analytics |

---

## 5. Relationships

- **Upstream (authoritative):** [`01-model-company/`](../01-model-company/) owns the business
  requirements (728), workflows (5,427), and controls (808). Nothing here overrides them.
- **Sourcing decisions:** the two-tier doctrine (2026-09-14) governs: *in EBS → use it;
  otherwise → build.* The [sourcing register](../07-methodology/capability-sourcing-and-engineering-model.md)
  §4's four Buy rows (WMS/TMS/WFM/FSM) are superseded — the rewrite shipped the same day
  (sourcing v3.0, OM v3.11; resolution record and amendment schedule in the
  [fit-gap §4](fit-gap-analysis.md)). POS, ecommerce and the loyalty/gift-card stack are recorded as
  already-built in-house platforms.
- **Statutory vocabulary:** BIR/eFPS/CAS/POS, SSS/PhilHealth/Pag-IBIG, SC/PWD/solo-parent
  discount rules follow the repo canon (VS-79, VS-85, PA-17.3) — no new statutory claims are
  introduced in this folder.
- **Siblings:** future platform folders (03+) would follow the same pattern; today 02 is the
  only platform folder.

---

*Document Version: 2.0 | Date: 2026-09-16 | **Eighth-pass corpus sweep & LMS posture true (document-map row extended):** the fit-gap document-map row's pass list gains the eighth pass — the remaining adopted-vehicle classes ('Inventory/ATP system' rows → GOP/INV, 'demand planning module' rows → Demantra, 'TMS' rows → in-suite Shipping/Transportation Execution, generic quality-system rows → Oracle Quality) and W5525's learning-platform posture trued onto the in-suite OLA per fit-gap §4 resolution 5 (vendor-SaaS posture vocabulary retired; §4 resolution 32). Prior v1.9 | Date: 2026-09-16 | **Seventh-pass adopted-vehicle corpus sweep:** the document-map's fit-gap row extended with the sweep (eleven register rows' evidence extended; §4 resolution 31; register 97 rows unchanged). No decision-table or §1–§5 changes. Prior v1.8 | Date: 2026-09-16 | **Sixth-pass EBS-exhaustion audit:** the document-map's fit-gap row extended with the sixth-pass outcomes (H11 Oracle Internal Controls Manager adopted for the VS-21 audit-management/GRC surface; H8 environment lifecycle trued to Rapid Clone + Oracle iSetup; register 97 rows, standard 74 = 76.3%). No decision-table or §1–§5 changes. Prior v1.7 | Date: 2026-09-16 | **Fifth-pass EBS-exhaustion audit:** the document-map's fit-gap row extended with the fifth-pass trues (C6 WMS advanced-function family: Slotting/planned-crossdocking/Labor/Yard/Cartonization; E2 Succession Planning for W178). No decision-table or §1–§5 changes. Prior v1.6 | Date: 2026-09-16 | **Fourth-pass EBS-exhaustion audit:** the document-map's fit-gap row extended with the three fourth-pass realization trues (A3 AP Bills Payable, F5 delivery-fleet eAM, E2 Performance Management). No decision-table or §1–§5 changes. Prior v1.5 | Date: 2026-09-16 | **Third-pass EBS-exhaustion audit:** the document-map's fit-gap row re-pointed to the 96-row register (A14 Lockbox/Balance Forward Billing/iReceivables, B13 Contingent Labor, C17 Engineering, D16 Install Base + Service Contracts, D17 Depot Repair, E10 Compensation Workbench; standard share 74.4% → 76.0%). No decision-table or §1–§5 changes. Prior v1.4 | Date: 2026-09-16 | **Second-pass EBS-exhaustion audit:** the document-map's fit-gap row re-pointed to the 90-row register (eAM, Procurement Contracts, RM&I with the PFRS 15 EXT retirement, GOP, Configurator in-store, In-Memory Cost Management, GL budgetary control, Oracle Alert; standard share 71.1% → 74.4%). No decision-table or §1–§5 changes. Prior v1.3 | Date: 2026-09-15 | **EBS-exhaustion audit:** the document-map's fit-gap row re-pointed to the 83-row register (Field Service dispatch core, Lease & Finance Management, Internet Expenses, Teleservice and Advanced Benefits added; BUILD 15 → 14). No decision-table or §1–§5 changes. Prior v1.2 | Date: 2026-09-14 | Structure-promotion re-base (profile v3.0 / TO v2.3): the W4 People row's headcount re-based 6,762 → 6,911 (promoted HQ 511). No decision-table or §1–§5 changes. Prior v1.1 | Date: 2026-09-14 | Two-tier sourcing doctrine enacted (in EBS → use it; otherwise → build): decision table re-pointed (in-suite Oracle WMS/MSCA + Shipping/OTE; POS/ecommerce/loyalty recorded as already-built platforms; payroll re-scoped to an in-house build; foundation-model APIs remain commodity procurement), W4 wave re-scoped (Core HR in EBS + payroll-build integration), sourcing-register supersession recorded with the rewrite scheduled. Prior v1.0 (2026-09-14): initial issue — Oracle EBS 12.2 selected as the ERP core of record; blueprint folder established (platform architecture, module coverage map, fit-gap analysis, customization governance, integrations, data migration). Canon references: 188 VS / 569 PA / 5,427 WF / 808 CTL / 728 Req / 6,762 HC current — HQ 511 / 6,911 target.*
