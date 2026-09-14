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
| Deployment model | Hosted private deployment (colocation or OCI compute) with DMZ tier for iSupplier/external integrations | EBS is not SaaS; the sourcing model's "unified core" is realized on-premises-grade. Data residency (RA 10173) is fully under BuildRight control |
| Customization doctrine | **Fit-to-standard first**, CEMLI-governed (see [`customization-governance.md`](customization-governance.md)) | The user doctrine: make the most of the suite; customize only for gaps |
| Philippine statutory layer | eBTax configuration + a bounded **localization pack** (payroll statutory, BIR report/file formats) | The one area EBS genuinely needs country-specific builds — see [`fit-gap-analysis.md`](fit-gap-analysis.md) §6 |
| Edge systems | Best-of-breed WMS/TMS/WFM/FSM, POS, ecommerce, loyalty — unchanged from the [Capability Sourcing Register](../07-methodology/capability-sourcing-and-engineering-model.md) §4 | EBS has no native products for these; the register already decided Buy/Build. Oracle WMS/MSCA **satisfies the register's own WMS re-evaluation trigger** and goes to the SIB for the parity assessment (§4 of the fit-gap doc) |
| In-house builds | OMO (omnichannel order orchestration), TPS (trade & project services), AAP (agentic runtime), IAP (integration platform), DP (data platform) — unchanged | Register §4; EBS offers no credible substitute |

**Consistency with the sourcing model.** The Capability Sourcing Register
([`07-methodology/capability-sourcing-and-engineering-model.md`](../07-methodology/capability-sourcing-and-engineering-model.md) §4)
remains the single record of sourcing decisions. This folder does not re-decide anything it
owns; it names the *product* that realizes the "unified ERP core" row (**Oracle EBS 12.2**)
and dispositions every model-company capability against EBS standard function. Any change to
a register row (e.g., WMS BoB → Oracle WMS) routes through the W5515 sourcing gate as usual.

---

## 2. Guiding Principles (the "Make the Most of It" Doctrine)

1. **Standard first.** A workflow touchpoint is served by unmodified EBS unless a documented
   gap proves otherwise. The burden of proof sits with the customizer, not the standard.
2. **Configure > Personalize > Extend > Localize > Build.** The lowest CEMLI tier that
   closes the gap wins. "Build" in this ladder means custom code *inside* EBS — the
   in-house products (OMO/TPS/AAP) are outside EBS and governed by the sourcing register.
3. **Zero modifications (M).** No base-product changes: no Forms modification, no base-table
   DML, no patch-overrides. This is what keeps quarterly Critical Patch Updates and Release
   Update Packs installable without rework.
4. **Upgrade-safe extensions only.** Custom code lives in a custom schema/top (`BDR`),
   registers in the EBS object registry, and follows the online-patching (editioned
   redefinition) rules so ADOP cycles never break on custom objects.
5. **One control surface.** Every workflow's Controls section (CTL-1 – CTL-808) maps to an
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
| [`fit-gap-analysis.md`](fit-gap-analysis.md) | The gap discipline: fit classes (FIT-STD/FIT-CFG/PER/EXT/LOC/INT/EDGE/BUILD), the capability disposition register (76 rows), the Philippine localization register, requirement-section (R1–R32) disposition view, SIB re-assessment items, and the standard-first KPIs |
| [`customization-governance.md`](customization-governance.md) | How customization stays under control: CEMLI framework operationalized, the Customization Decision Record (CDR) workflow, naming/technical standards, online-patching-safe coding rules, the CEMLI register, de-customization triggers, KPIs |
| [`integrations.md`](integrations.md) | EBS-specific integration patterns for every flow in the canonical [integration architecture](../01-model-company/data-volumes-and-integrations.md): POS, ecommerce, WMS/TMS/WFM/FSM edges, banks, BIR/eFPS, statutory bodies, payment gateways, iSupplier — via open interfaces, ISG REST/SOAP, business events, and IAP contracts |
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
| **W4 — HR statutory** | Core HR, PH payroll localization pack, statutory filings | PER, PAY + LOC pack | VS-19, VS-79; 6,762 employees |
| **W5 — Projects, assets, property** | Capex/CIP, fixed assets, lease admin + PFRS 16 extension | PA, FA, PN + EXT | VS-20/35/40/42/148 |
| **W6 — Optimization** | ECC dashboards, de-customization pass, RUP currency | ECC, Web ADI | Tier 3 analytics |

---

## 5. Relationships

- **Upstream (authoritative):** [`01-model-company/`](../01-model-company/) owns the business
  requirements (728), workflows (5,427), and controls (808). Nothing here overrides them.
- **Sourcing decisions:** [`07-methodology/capability-sourcing-and-engineering-model.md`](../07-methodology/capability-sourcing-and-engineering-model.md)
  §4 register governs Configure/Buy/Build; this folder realizes the Configure tier on EBS.
- **Statutory vocabulary:** BIR/eFPS/CAS/POS, SSS/PhilHealth/Pag-IBIG, SC/PWD/solo-parent
  discount rules follow the repo canon (VS-79, VS-85, PA-17.3) — no new statutory claims are
  introduced in this folder.
- **Siblings:** future platform folders (03+) would follow the same pattern; today 02 is the
  only platform folder.

---

*Document Version: 1.0 | Date: 2026-09-14 | Initial issue — Oracle EBS 12.2 selected as the ERP core of record; blueprint folder established (platform architecture, module coverage map, fit-gap analysis, customization governance, integrations, data migration). Canon references: 188 VS / 569 PA / 5,427 WF / 808 CTL / 728 Req / 6,762 HC current — HQ 511 / 6,911 target.*
