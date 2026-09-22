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
| **Accounts Payable (AP)** | Vendor invoices, 3-way match, EWT withholding, payments, PDCs on Bills Payable (W424 issued-but-unmatured instruments, maturity reports) | W7, W100, W244, W424, PA-15.1/15.2 |
| **Accounts Receivable (AR)** | Trade/corporate invoices, credit memos (W540), PDC instruments on Bills Receivable (W423/W1380), Lockbox remittance auto-application + Balance Forward Billing statement cycles (W892/W1117), deposits | VS-11, VS-16, VS-143 |
| **Cash Management (CE)** | Bank statement import & reconciliation, cash positioning feeds | W89, W212/W541 reconciliation, VS-18.1 |
| **Payments (IBY)** | Payment formats, bank payment files, positive pay | W320 electronic payment control, PA-18.2 |
| **Fixed Assets (FA)** | Asset register, depreciation, disposals, CIP via mass additions | W39, W184, W276, VS-35 |
| **E-Business Tax (eBTax)** | PH VAT determination, VAT-exempt/zero-rated (SC/PWD/solo-parent pathways), EWT/ATC (WC 010/WI 010/WP 010 canon) | VS-79, VS-85, W145, W24 |
| **Purchasing (PO)** | Requisitions, POs, blankets (W2C), receipts, receiving 3-way match, contingent-labor POs with timecard-to-invoice (B13) | VS-03, VS-15; W2 family; VS-98 |
| **iProcurement** | Store/HQ self-service requisitioning, non-merchandise catalogues | W136, VS-34 |
| **Internet Expenses (OIE)** | Employee expense reports, policy limits, AME approvals, corporate-card statement loads (fit-gap B11, §4 resolution 10) | W74, PA-15.2 card reconciliation |
| **Sourcing (PON)** | RFQs, auctions, bid tendering (government/institutional) | W166, VS-46 |
| **iSupplier (POS portal)** | Vendor portal: PO view, ASNs, invoicing, catalogs | W422, R28, PA-03.x |
| **Supplier Lifecycle Management** | Supplier onboarding questionnaire/approval flow | W36 vendor onboarding |
| **Procurement Contracts** | Vendor contract authorship from the clause library, deliverables with due dates, expiry/amendment alerts, compliance tracking (fit-gap B12, §4 resolution 14) | VS-03 W669/W62/W62B, VS-98, W241 facility-vendor SLAs |
| **Trade Management (OTM)** | Vendor rebate accrual evaluation & claims — in-suite per fit-gap B10/§4 resolution 3 (license cost is a FinOps decision) | VS-39, W27/W161 |
| **Landed Cost Management (LCM)** | Import true-up: freight, duties, demurrage allocation to item cost | W144, W239, W249, VS-122 |
| **Enterprise Asset Management (eAM)** | Facility, equipment & vehicle maintenance: eAM asset register (FA-linked), work-request intake, PM scheduling with generated work orders, work-order costing (fit-gap F5, §4 resolution 13) | VS-07.2 W47, VS-20.3 W240/W241/W808/W1403, VS-12.2 W1172, VS-06.2 W1348/W1349/W653, VS-115, VS-163.3, VS-108.2 |
| **Inventory (INV)** | Item master (governed through Product Hub — C1) with site attributes on Site Hub (C3), UOM/conversions, onhand, subinventories, min-max, cycle counts, physical inventory, inter-org transfers, consignment | VS-05, VS-29; W3/W4/W6/W22/W42 family |
| **Warehouse Management (WMS) / MSCA** | **Adopted in-suite** — RF-directed putaway/pick, LPN/pallet tracking, directed tasking, plus the advanced-function family the DC workflows invoke: WMS Slotting (W784/W1402), planned crossdocking (W221/W1226/W1279/W1307), WMS Labor Management (W796), WMS Yard Management (W222/W585/W1353), Cartonization (W3099) | VS-04; two-tier doctrine resolution (in EBS → use it) |
| **Bill of Materials (BOM) / WIP** | Kit/BOM definitions, bundle assembly, build-to-order; revision control via Engineering ECO/ECN (below) | W46, VS-92 |
| **Engineering (ENG)** | Engineering Change Orders/Notices with routed approvals over kit/BOM revisions and effectivity control (fit-gap C17, §4 resolution 25) | W302, W46, VS-92, VS-41 private-label specs |
| **Order Management (OM)** | Sales orders, quotes→orders (W58), backorders (W56), sales agreements, drop-ship (W246), ship-confirm | VS-11, VS-16, VS-60 (fulfillment legs) |
| **Global Order Promising (GOP)** | Multi-org available-to-promise over onhand/in-transit/expected supply with allocation rules (fit-gap D15, §4 resolution 17) | W56, W1114, VS-93 W3097, W164/W979 call-offs |
| **Advanced Pricing (QP)** | Price lists, modifiers, qualifiers, coupon/promotion rules, PH mandatory discounts | W40, W61, W93, VS-85, W539 |
| **Oracle Configurator (CZ) — in-store scope** | Rules-driven fabrication configuration & QP-integrated quotes on ATO models (fit-gap C16, §4 resolution 16); B2C storefront configuration stays not-adopted (below) | VS-09.1 W1009 + the W943/W944/W946/W986/W988/W1045/W1054/W1059/W1046 fabrication family |
| **Shipping Execution (WSH)** | Ship confirm, delivery/trip, packing slips | W19, W106 dispatch |
| **Transportation Execution (OTE)** | Carrier tender, freight cost capture — in-suite under the two-tier doctrine (the BoB TMS row is superseded; the forty-fifth-wave review trued the corpus's ~49 surviving bare-'TMS' tokens to this stack — the VS-110 freight rows, PA-15.1's freight audit, PA-04.3's KPI extraction and the PA-69/93/94/111/114 execution rows — with the route-optimization/dispatch senses naming the in-house Route Optimization Engine per the build-candidate clause) | VS-110 freight postings |
| **Oracle Quality (QA)** | Incoming inspection plans, supplier quality data collection | W110 supplier quality, VS-31 |
| **Property Manager (PN)** | Lease administration, rent/CAM/indexation billing, critical dates | VS-42, W117/W118 |
| **Lease & Finance Management (OKL)** | Lessor equipment leasing: lease booking, billing schedules → AR, asset/end-of-term tracking (fit-gap A13, §4 resolution 9) | VS-96, W3165–W3176 |
| **Projects (Project Costing + PM)** | Capex projects, CIP, project vendor bills, asset turnover hand-off | VS-40, VS-20, W21, W276 |
| **Oracle HRMS (PER)** | Org/position/employee master, EITs (licenses, PPE sizes), absence types, performance appraisals/objectives (W72 review cycle), succession planning (W178 talent pools/readiness states/career paths) | VS-19, W15/W43, W72, W178, W292 — Core HR stays in EBS; the payroll engine is the in-house build (below) |
| *Oracle Payroll (PAY)* | ***Not adopted*** — payroll is an in-house build (fit-gap E5–E8): the build owns PH statutory gross-to-net and compensation outputs, posts costing journals into EBS, and pulls people data from PER | VS-19.2; fit-gap §4 resolution 7 |
| **iRecruitment (IRC)** | Vacancy/requisition/candidate self-service | W-recruitment family, VS-121 |
| **Oracle Learning Management (OLA)** | Training calendar, compliance enrollments, learning records | W51, W5525 platform administration, VS-123/183 (basic; deeper LMS function, if ever needed, is a build — the corpus's vehicle-sense LMS rows name OLA per the eighth-pass sweep, the vendor-SaaS posture retired per fit-gap E2/§4-32) |
| **Advanced Benefits (OAB)** | Benefits enrollment/eligibility/life events; deduction envelopes to Payroll PH via the E4 feed (fit-gap E9, §4 resolution 11) | VS-102.2 |
| **Compensation Workbench (CWB)** | Salary budgets with per-manager distribution, merit/increase planning, promotion & off-cycle adjustments, pay-range administration (fit-gap E10, §4 resolution 26) | VS-102.1 W3307/W3327/W3311 |
| **Teleservice / Service Requests** | Complaint/service-request capture, SLA timers, tiered escalation on the TCA party model (fit-gap D14, §4 resolution 12) | W41, VS-13.1 |
| **Oracle Treasury (XTR)** | Cash positioning, investments, debt/covenants, FX exposure & deals | VS-18.1–18.3, W80, W318/W319/W321 |
| **Advanced Collections (IEX)** | Delinquency strategy, dunning, promise-to-pay | VS-16.3, W108 |
| **Credit Management** | Credit scoring rules, limits, hold/release | W24, W328, W229 |
| **Field Service (CSF) + Install Base** | Task assignment, dispatch scheduling, technician debrief & the mobile field device on serviced assets — the in-suite dispatch core (fit-gap D13, §4 resolution 8); the build narrows to the consumer experience layer | VS-12 dispatch; VS-96 serviced assets |
| **Install Base + Service Contracts (OKS)** | Serialized item instances registered at POS/ecommerce/trade with coverage derived from sold warranty terms; extended-warranty/service contracts with entitlement checks and renewal schedules (fit-gap D16, §4 resolution 22) | VS-53 W2118–W2135, W33, W544, VS-155 provenance |
| **Depot Repair (CSD)** | Repair orders on Install Base instances: intake, diagnosis, estimate/approval, parts/labor consumption from service inventory, RO billing (fit-gap D17, §4 resolution 23) | W440, W544, VS-155 refurbishment |
| **Receivables Revenue Management (in-suite AR)** | Multi-element revenue arrangements, SSP-based allocation, contingency & event-based revenue schedules (fit-gap A11, §4 resolution 15 — the PFRS 15 EXT retired; the vehicle naming trued 2026-09-22 per Vision VF-1 — the capability is AR's 'Revenue Management Super User'/program ARBARL, not a standalone application) | VS-11.2 W162/W165, VS-47 W1978, VS-157 |
| **GL Budgets + Budgetary Control** | Budget entry/consolidation, Board lock-down, funds checking at requisition/PO/invoice, budget-vs-actual (fit-gap F6, §4 resolution 19) | W26, W1646–W1651, W21/W1811–W1818, W700 |
| **Oracle Alert (ALR)** | Periodic/event-driven alerting over the EIT statutory registers (fit-gap G9, §4 resolution 20); filing acts stay human-confirmed | W54/W427/W437/W446, W54A, W468, W3634 |
| **In-house Audit & GRC platform (BUILD)** | Audit-management/GRC surface: risk & control library hosting the CTL-01–CTL-808 register, assessment plans & results, findings/CAP routing, Audit-Committee certification evidence (fit-gap H11 — re-dispositioned BUILD 2026-09-22 per Vision VF-2; the 2026-09-16 ICM adoption rode AMW, registered '(Obsolete)' with no installation record on either installation of record; the EBS evidence layer — FND audit, ERES, AME logs — feeds it unchanged) | VS-21 W120/W121/W123/W159/W332/W333/W334/W336/W338/W351 |
| **iSetup + Rapid Clone (env lifecycle)** | Instance cloning via Rapid Clone on the on-premises estate and setup-data templating/verification across the four non-prod environments (fit-gap H8) | W384 environment refresh & post-refresh sanity check |
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
gift-card/loyalty stack (already built), **Payroll PH**, the store workforce platform, the
dispatch experience layer (the Field Service dispatch core being in-suite per fit-gap D13), and
OMO/TPS/AAP/IAP/DP. None of them buys its way in; all of them ledger into EBS.

**Planning products (adopted with the two-tier doctrine):** Oracle Advanced Supply Chain Planning (ASCP) and
Demantra Demand Management — the EBS-family Value Chain Planning stack — are **adopted** as the planning stack
(fit-gap C5, resolution record §4-2): VS-02's statistical forecasting and VS-127's IBP surface ride them, and the
same stack's Inventory Optimization (multi-echelon) and Rapid Planning engines serve VS-136's network/MEIO
engineering (W4129–W4136); license cost is a FinOps decision, not a sourcing decision.

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
| **UAT/TRAIN** | Business validation + the 6,932-user training estate | W73 parallel-run rehearsals |
| **PATCH** | ADOP patch/upgrade rehearsal (RUP, CPU) | Mandatory gate before any PROD patch |
| **PROD** | Production | DR twin via Data Guard |

Cloning cadence: monthly UAT refresh, per-wave SIT refresh, ad-hoc hotfix clone. All
refreshes run the masking profile (W384) — production data never trains unmasked. Cloning
runs **Rapid Clone** (adpreclone/adcfgclone) with storage-snapshot consistency on the
BuildRight data-center estate — no public-cloud hosting (§1); post-refresh configuration
verification is templated through **Oracle iSetup** (ledger/org/AME/QP/eBTax/profile
extracts — fit-gap H8), and the post-clone sanity pass rides Oracle Applications Manager.

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

*Document Version: 2.2 | Date: 2026-09-22 | **Vision-findings re-disposition true.** Two §2 footprint rows re-pointed per fit-gap §4 resolution 36 — Revenue Management & Invoicing → Receivables Revenue Management (in-suite AR; the vehicle naming trued per Vision VF-1) and Internal Controls Manager → the in-house Audit & GRC platform (H11 re-dispositioned BUILD per Vision VF-2 — AMW obsolete/not installed on both installations of record; the EBS evidence layer feeds it unchanged). No §1/§3–§7 changes. Prior v2.1 | Date: 2026-09-21 | **Sixty-second-wave manuals-alignment true (the AP-row vocabulary cell).** The 2026-09-21 capability sweep against the shipped R12.2 manuals trued the AP row's Bills-Payable gloss — 'issued-but-unreleased instruments' → 'issued-but-unmatured instruments', the AP manual's own phrase ('issued but not matured', 122apug) — no row-set, product-boundary or count change. Prior v2.0 | Date: 2026-09-16 | **Forty-fifth-wave consistency review (no new rows):** the Transportation Execution row's evidence names the corpus's bare-'TMS' true (the VS-110 freight estate and the execution-sense rows ride this stack; route-optimization/dispatch senses stay on the in-house Route Optimization Engine per the row's own build-candidate clause — fit-gap C14/§4-33). No other §1/§3/§5–§7 changes. Prior v1.9 | Date: 2026-09-16 | **Eighth-pass corpus sweep & LMS posture true (no new rows):** the Oracle Learning Management row's W-list gains W5525's learning-platform administration (fit-gap E2/§4-32 — the corpus's vendor-SaaS LMS posture retired against the resolution-5 canon; the GOP/Oracle-Quality/OTE/Demantra sweeps ride rows those products already anchor). No other §1/§3/§5–§7 changes. Prior v1.8 | Date: 2026-09-16 | **Sixth-pass EBS-exhaustion audit footprint expansion:** two native products joined the §2 module footprint — Internal Controls Manager (H11, the VS-21 audit-management/GRC surface and CTL-register host, §4 resolution 30; row W-list completed with W123/W159) and iSetup + Rapid Clone (H8, the W384 environment-lifecycle toolchain); §4's cloning-cadence paragraph re-pointed to Rapid Clone/iSetup/OAM on the on-premises estate, and the same deployment-canon class closed across the IT-estate workflows (W55 DR failover, W368 environment lifecycle, W382 backup storage, W396 archive tiers — all trued to the BuildRight estate per A6.2). No other §1/§3/§5–§7 changes. Prior v1.7 | Date: 2026-09-16 | **Fifth-pass EBS-exhaustion audit footprint trues (no new rows):** the WMS/MSCA row names the adopted product's advanced-function family the DC workflows invoke (Slotting W784/W1402, planned crossdocking W221/W1226/W1279/W1307, Labor Management W796, Yard Management W222/W585/W1353, Cartonization W3099 — fit-gap C6) and the HRMS row names Succession Planning for the W178 talent chain (E2). No §1/§3–§7 changes. Prior v1.6 | Date: 2026-09-16 | **Fourth-pass EBS-exhaustion audit footprint trues (no new rows):** the AP row names Bills Payable for the W424 outgoing-PDC instrument register (A3), the HRMS row names performance appraisals/objectives for the W72 review cycle (E2) and the eAM row's estate list gains the VS-06 delivery-fleet vehicles/tires (W1348/W1349/W653); no §1/§3–§7 changes. Prior v1.5 | Date: 2026-09-16 | **Third-pass EBS-exhaustion audit footprint expansion:** five native products/rows joined the §2 module footprint — Install Base + Service Contracts (D16), Depot Repair (D17), Engineering (C17) and Compensation Workbench (E10) as new rows, with the AR row naming Bills Receivable/Lockbox/Balance Forward Billing (A3/A14), the PO row naming contingent labor (B13) and the INV row naming Product Hub/Site Hub (C1/C3); no §1/§3–§7 changes. Prior v1.4 | Date: 2026-09-16 | **Second-pass EBS-exhaustion audit footprint expansion:** seven native products joined the §2 module footprint — Enterprise Asset Management (F5, the §4-13 adoption correcting the 'no native EAM' claim), Procurement Contracts (B12), Global Order Promising (D15), Oracle Configurator scoped to in-store fabrication (C16 — the 'CZ for B2C' non-adoption row unchanged), Revenue Management & Invoicing (A11's EXT retirement), GL Budgets + Budgetary Control (F6) and Oracle Alert (G9); the planning paragraph names Inventory Optimization/Rapid Planning for VS-136. No §1/§3–§7 changes. Prior v1.3 | Date: 2026-09-15 | **EBS-exhaustion audit footprint expansion:** six native products joined the §2 module footprint — Trade Management (B10/§4-3, previously resolved but unlisted), Internet Expenses (B11), Lease & Finance Management (A13), Field Service + Install Base (D13's corrected in-suite dispatch core), Advanced Benefits (E9) and Teleservice/Service Requests (D14); the in-house roster paragraph names the dispatch experience layer as the narrowed build. No §1/§3–§7 changes. Prior v1.2 | Date: 2026-09-14 | Structure-promotion re-base (profile v3.0 / TO v2.3): §4's UAT/TRAIN row training-estate figure re-based 6,762-user → 6,911-user (promoted HQ 511 / total 6,911). No §1–§3/§5–§7 changes. Prior v1.1 | Date: 2026-09-14 | Two-tier sourcing doctrine enacted (in EBS → use it; otherwise → build): Oracle WMS/MSCA and Shipping/OTE adopted in-suite (BoB WMS/TMS superseded), Oracle Payroll marked not-adopted with payroll re-scoped to the in-house build (fit-gap §4 resolution 7), in-house-products roster added (POS/ecommerce/loyalty already built — integration is the program). Prior v1.0 (2026-09-14): initial issue — org/ledger model, module footprint, tech stack, environments, integration and security architecture for the EBS realization. Canon references: 5 legal entities / 200 stores / 4 DCs / 35,000 active SKUs / ~2.8M POS transactions/month (tender-mix canon); Premier-Support horizon re-verified at contract time.*
