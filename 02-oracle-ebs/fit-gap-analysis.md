# Fit-Gap Analysis — Oracle EBS vs. the Model Company

> The governing document of the doctrine. Per the 2026-09-14 **two-tier sourcing decision**: *if it's in Oracle EBS we use it; otherwise we build.* Every capability domain the
> 5,427 workflows demand is dispositioned against standard Oracle EBS 12.2 in one of the fit
> classes below. In the **79-row register**: **54 rows (68.4%) run on standard or configured
> EBS**; 2 are personalizations; only 2 are true extensions (the PFRS 15/16 accounting
> schedules); 1 is the EBS-held Philippine indirect-tax localization; 5 are interfaces; and
> **15 are in-house builds — of which 5 are already-built platforms (the in-house POS estate,
> the custom ecommerce platform, and the gift-card/loyalty stack) that integrate rather than
> get bought or rebuilt**. The former best-of-breed buy tier is retired (zero rows); the two
> formerly-OPEN planning decisions resolved in-suite.

Part of the [02-oracle-ebs blueprint](README.md). The constructive half (what standard EBS
does) lives in the [module coverage map](module-coverage-map.md).

---

## 1. Fit Classes

| Class | Meaning | CEMLI tier | Typical evidence |
|---|---|---|---|
| **FIT-STD** | Served by unmodified EBS out of the box; setup only | — (Configuration in the register's sense) | Oracle implementation guides; config docs |
| **FIT-CFG** | Served by EBS with substantial configuration (CoA design, AME rule sets, QP modifiers, SLA derivations, eBTax rules) — no code | C | BRD/config guides, setup audits |
| **PER** | Personalization: OAF page personalizations, Descriptive/Flexfield capture — metadata only, survives patching | E-lite (personalization) | Personalization export, DFF registry |
| **EXT** | Custom code inside EBS (custom schema/top objects, PL/SQL APIs, OAF extensions, scheduled concurrent programs) | E | Customization Decision Record (CDR) |
| **LOC** | Philippine statutory localization build (legal-format outputs, statutory calculation tables, government file interfaces) | L | Statute citation + format spec + BIR/agency acceptance |
| **INT** | Interface to/from an external government or partner system | I | Interface spec, reconciliation control |
| **BUILD** | Executed by an in-house product per the two-tier doctrine (*in EBS → use it; otherwise → build*): planned builds (OMO, TPS, AAP, IAP, DP) and **already-built platforms** (the POS estate, the ecommerce platform, the gift-card/loyalty stack) that integrate rather than get bought — the row notes which | — (Build) | Register row / existing platform record |
| **EDGE** | *(Retired 2026-09-14 — zero rows.)* Formerly best-of-breed buy. The two-tier doctrine eliminated capability buying: every former EDGE row is re-dispositioned in-suite (FIT-STD, e.g. Oracle WMS/MSCA) or as BUILD | — | §4 resolution record |
| **OPEN** | *(Currently zero rows.)* Genuine open decision — scheduled for the SIB with a scored assessment (W5515 gate) | — | SIB agenda item |

Ladder rule: the lowest class that closes the gap wins. An EXT is admitted only after a
FIT-CFG, PER, and (where applicable) BUILD alternative is documented as inadequate.

---

## 2. Capability Disposition Register

Legend: **VS** = owning value stream(s). Classes per §1. Counts are pinned in §3.

### A. Financial core (VS-17, VS-18, VS-105, VS-157, VS-148)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| A1 | Ledgers, CoA, consolidation & eliminations for 5 legal entities | GL: 5 primary ledgers, shared CoA, GL Consolidation, FSG | FIT-CFG | One-CoA-five-ledgers design; elimination journals per W234 |
| A2 | AP invoice processing, 3-way match, EWT withholding | AP + eBTax withholding tax groups | FIT-CFG | ATC canon (WC 010/WI 010/WP 010) as withholding codes; W7/W100/W244 |
| A3 | AR invoicing, credit memos (W540), PDC registers (W423/W1380) | AR + AutoInvoice + special terms | FIT-CFG | PDC maturity via AR terms + CE reconciliation |
| A4 | Bank statement reconciliation | Cash Management (CE) auto-reconciliation | FIT-STD | W89, W537/W541 feeds |
| A5 | Bank payment files, positive-pay controls | Payments (IBY) formats | FIT-CFG | Per-bank formats for BDO/BPI/MB/CB (integration map) |
| A6 | Fixed assets, depreciation, disposals, CIP turnover | FA + mass additions | FIT-STD | W39, W184, W276 |
| A7 | Intercompany billing & settlement | Advanced Global Intercompany System (AGIS) | FIT-STD | W14, W461, W435 IC SLA billing |
| A8 | Cash positioning, investments, debt/covenants, FX deals | Oracle Treasury (XTR) + CE | FIT-CFG | VS-18.1–18.3; W80 hedging; BSP-report data via XTR extracts |
| A9 | Bad-debt provisioning & write-offs | AR aging buckets + approval workflows | FIT-CFG | W81 provision ladder as AME-governed journals |
| A10 | Revenue recognition — retail & wholesale point-of-sale revenue | Standard AR/OM invoicing | FIT-STD | Single-performance-obligation sales need no RevRec engine |
| A11 | PFRS 15 — complex multi-element contracts (project sales, service bundles) | No native multi-element schedules | EXT | Bounded schedule engine (custom concurrent program) posting via SLA; VS-157 |
| A12 | PFRS 16 — ROU asset & lease-liability schedules | Property Manager administers leases, not ROU amortization | EXT | Amortization schedule build feeding GL/FA from PN contracts; VS-148 |

### B. Procure-to-pay & sourcing (VS-03, VS-15, VS-34, VS-39, VS-87, VS-122, VS-161)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| B1 | Req → PO → receipt → match cycle | Purchasing + AME approvals | FIT-STD | W2 family, W60 emergency path via type-based workflow |
| B2 | Blankets & contract POs (W2C) | PO blanket agreements + releases | FIT-STD | Period/quantity releases feed vendor scorecards |
| B3 | Self-service requisitioning & non-merchandise catalogs (W136) | iProcurement catalogues + expense invoices | FIT-CFG | Content-managed punch-out for strategic suppliers |
| B4 | Vendor portal — POs, ASNs, invoices | iSupplier | FIT-STD | W422 VMI collaboration, R28 |
| B5 | RFQs, auctions, institutional tendering (W166) | Sourcing (PON) | FIT-STD | Government/institutional bid records for VS-46 |
| B6 | Supplier onboarding & lifecycle | Supplier Lifecycle Management + TCA | FIT-CFG | W36 onboarding questionnaire/approval; TIN/ATC validation |
| B7 | Vendor TPRM scoring & reassessment (VS-161) | EIT/DFF risk attributes + AME reassessment workflow | FIT-CFG | Tiering registers on supplier records; deep TPRM tooling = SIB candidate (§4) |
| B8 | Landed cost true-up (freight, duties, demurrage) | Landed Cost Management | FIT-STD | W144, W239, W249; arms VS-122 imports |
| B9 | Customs broker / BOC filings coordination | File exchange via IAP to broker systems | INT | Declarations live in broker/BIR systems; EBS receives duty true-ups via B8 |
| B10 | Vendor rebates, promotions & claims (VS-39, W27, W161) | PO accruals + Trade Management evaluation | FIT-CFG | OTM license-flagged — SIB check (§4); fallback: accrual + claims workflow |

### C. Supply chain & inventory (VS-01, VS-02, VS-04, VS-05, VS-06, VS-29, VS-31, VS-45, VS-92, VS-111, VS-127)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| C1 | Item master, catalog categories, templates (W252, W290) | INV + EGO item catalogs/templates + Web ADI mass maintenance | FIT-CFG | VS-29 governance runs via workflow; ~55,000 item-master records |
| C2 | UOM & conversions, catch-weight flags (W294) | INV UOM classes & conversions | FIT-STD | Lumber/wire catch-weight per data-migration mapping |
| C3 | Org/subinventory/locator model (200 stores + 4 DCs + master org) | INV organizations + MOAC security profiles | FIT-CFG | Architecture §1; W16 add-org runbook |
| C4 | Replenishment — min-max/reorder points (W2, W2A, W4) | INV min-max planning + reorder-point planning | FIT-STD | Parameter governance W312 |
| C5 | Statistical forecasting, S&OP/IBP surface (W31, W133, VS-127) | **Oracle ASCP + Demantra** (EBS-family Value Chain Planning stack) | FIT-CFG | Resolved per the two-tier doctrine — the planning stack is Oracle's, so we use it; license cost is a FinOps decision, not a sourcing decision |
| C6 | RF-directed warehouse execution (putaway/pick, LPNs) | **Oracle WMS/MSCA — in-suite, adopted** | FIT-STD | Resolved per the two-tier doctrine: warehouse execution ships with EBS, so we use it; the sourcing register's BoB WMS row is superseded (§4 resolution record) |
| C7 | Cycle counting & physical inventory (W6, W42) | INV cycle counts (ABC classes), physical inventory tags | FIT-STD | Vendor-owned counts via consignment receipt revaluation |
| C8 | Inter-org transfers & in-transit tracking (W22, W204, W218) | INV internal requisitions, in-transit inventory | FIT-STD | Inter-island freight allocation via landed cost/payload DFFs |
| C9 | Kits, bundles, build-to-order assembly (W46, VS-92) | BOM + WIP (light) / OM kits | FIT-STD | Assemble-to-order kits for VS-92 |
| C10 | Supplier consignment (W20, W23, VS-45) | EBS consigned inventory (supplier-owned onhand, consumption trigger) | FIT-STD | Sell-through triggers vendor settlement per W543 |
| C11 | VMI data collaboration (W20/W422) | iSupplier planning reports + onhand feeds | FIT-CFG | Vendor-side optimization is the vendor's system |
| C12 | Incoming inspection, supplier quality data (W110, VS-31) | Oracle Quality collection plans | FIT-STD | CAPA workflow on quality notices; deep QMS stays process |
| C13 | Pallets/RTI & packaging tracking (VS-111, W270) | LPN tracking + deposit-bearing DFFs | FIT-CFG | Deposit accounting via AP/AR; pooling stays contractual |
| C14 | Transport planning, carrier tendering & freight audit (VS-06, VS-110) | Shipping Execution + Transportation Execution (in-suite) | FIT-STD | The register's BoB TMS row is superseded — tender, ship-confirm and freight-cost capture are in-suite; optimization beyond OTE is a build candidate, never a buy |

### D. Order-to-cash & retail (VS-07, VS-08, VS-10, VS-11, VS-12, VS-16, VS-32, VS-54, VS-57, VS-60, VS-95)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| D1 | Trade/corporate orders: quotes (W58), agreements & call-offs (W163/W164), drop-ship (W246) | OM quotes, sales agreements, blanket releases, back-to-back orders | FIT-STD | Retention/milestone billing via Projects (F1) |
| D2 | Pricing: lists, modifiers, quantity breaks, coupons (W40/W93/W539), PH mandatory discounts (VS-85) | Advanced Pricing lists/qualifiers/modifiers + eBTax | FIT-CFG | Senior/PWD/solo-parent qualifiers; price-change governance W107/W289 |
| D3 | Credit management & holds (W24, W328, W229) | Oracle Credit Management + OM holds | FIT-STD | Scoring rules + exception approvals via AME |
| D4 | Collections & dunning (W108, VS-16.3) | Advanced Collections strategy/dunning | FIT-STD | PDC aging from AR terms |
| D5 | Customer master, dedup, hierarchy (W253, W460) | TCA + Data Quality Management | FIT-STD | ~5,400 AR accounts canon; party/site/account model |
| D6 | POS estate & checkout execution (VS-08) | **Already-built in-house POS platform** — integrates; EBS owns item/price/tax masters, store orgs, and the sales/AR posting | BUILD *(existing)* | No EBS POS exists and none is needed — the platform is built; this is an integration program (W533–W541 flows), not a sourcing decision |
| D7 | Ecommerce platform (VS-10) | **Already-built custom ecommerce platform** — integrates; EBS order import + availability feeds | BUILD *(existing)* | iStore deliberately not adopted; the canonical migration table itself records the platform as the in-house custom ecommerce estate |
| D8 | Gift cards & stored value (VS-54) | Stored-value engine lives in the in-house POS/ecommerce stack; EBS holds the GL liability + IC settlement (W28) | BUILD *(existing)* | Breakage/dormancy per W5511 remains process on the GL |
| D9 | Loyalty program engine (W17, VS-13) | **Already-built loyalty stack** in the in-house estate; points-as-tender posts to AR/POS settlement (W550) | BUILD *(existing)* | TCA remains the member master of record |
| D10 | Omnichannel order routing & mixed-basket orchestration (VS-60) | In-house OMO per register §4 | BUILD | EBS OM carries the fulfillment legs OMO routes |
| D11 | Marketplace operator / 3P-seller settlement (VS-95) | Marketplace integrations on the in-house ecommerce platform; AR reconciliation of commissions | BUILD *(existing)* | Payout files reconcile to AR/AP via IAP |
| D12 | Cross-channel returns & exchanges (VS-32, W12 family) | OM RMAs + AR credit memos + INV adjustments | FIT-CFG | The POS/ecommerce platforms execute the counter transaction; EBS owns the RMA/credit lifecycle |
| D13 | Installation & home-service dispatch, technician mobile app (VS-12) | Not in EBS, not already built → build | BUILD | The register's BoB FSM row flips to build; product remit (extend TPS vs new squad) assigned at the SIB/OM |

### E. HR & payroll (VS-19, VS-102, VS-121, VS-123, VS-183)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| E1 | Core HR: org/positions/employees/EITs, absence types | Oracle HRMS (PER) | FIT-STD | W15/W43/W292; license/EIT data for VS-166 registers. Core HR **stays in EBS** — the build decision covers payroll, not the people data of record |
| E2 | Recruitment, self-service, learning & performance (W51, VS-121) | iRecruitment + Self-Service HR + OLA | FIT-STD | In-suite per the doctrine; a deeper build is the doctrine-compliant path if adoption ever lags |
| E3 | Store workforce scheduling & time-capture platform | Not in EBS, not already built → build | BUILD | The register's BoB WFM row flips to build; owns VS-07 staffing/attendance execution |
| E4 | Time & attendance → payroll/EBS import | In-house WFM feed → interface (BEE-class staging) | INT | Capture stays in the build; validated feeds drive scheduling compliance and pay inputs |
| E5 | In-house payroll engine — PH statutory gross-to-net (W10) | **In-house build (Payroll PH)** | BUILD | Per decision: *payroll we build.* SSS/PhilHealth/Pag-IBIG tables, PD 851 13th month, night differential/OT elements, BIR withholding tables — built in-house, not localized on Oracle Payroll (which stays unadopted; see architecture §2) |
| E6 | Payroll statutory outputs & agency files (W251) | In-house build outputs | BUILD | Contribution/loan file formats (R3/RF1/PF-class) and posting reconciliation |
| E7 | BIR compensation reporting: 2316, 1601-C, 1604-C, alphalist (W90, W5533) | In-house build outputs from payroll balances | BUILD | Per current BIR publish formats; eFPS submission rides the G3 channel |
| E8 | Payroll costing → GL posting | Interface posting into GL/SLA | INT | EBS remains the ledger of record: the build posts period costing journals; balances tie out per period |

### F. Projects, assets & property (VS-20, VS-35, VS-40, VS-42, VS-55, VS-97, VS-109)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| F1 | Capex request → PO → CIP → asset turnover (W21, W276) | Projects (costing) + PO + FA mass additions | FIT-STD | VS-40 chain is fully native |
| F2 | Construction/new-store cost capture (W223–W227) | Projects cost capture against store WBS | FIT-STD | VS-20/109; PMO scheduling stays external |
| F3 | Lease administration, rent/CAM/indexation, real-property tax (W117/W118/W119) | Property Manager leases, payment schedules, indexation | FIT-STD | Critical-date workflows; PFRS-16 accounting via A12 |
| F4 | Planogram & space optimization (W86, VS-55) | Not in EBS → build; masters in EBS (W314) | BUILD | In-house space-planning build; template/compliance data governed as EBS-adjacent masters |

### G. Statutory & compliance (VS-79, VS-85, VS-118)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| G1 | PH VAT determination & return data (2550M, 2551Q) | eBTax configuration (rates, VATEX classes, per-document tax lines) | FIT-CFG | VS-79.1; zero-rated/VAT-exempt certification data |
| G2 | EWT / expanded withholding at AP | eBTax withholding + AP withholding tax groups | FIT-CFG | ATC canon; 2307 generation via G4 pack |
| G3 | BIR eFPS filing submission (W260) | File generation + IAP submission to eFPS | INT | Filing acts remain human-confirmed (agentic hard boundary, sourcing model §12.1) |
| G4 | BIR indirect-tax report pack: CAS/POS inventory lists (W478), 2307/CWT certificates (AP-side), VAT return datasets (2550M, 2551Q) | BI Publisher statutory formats from eBTax/AP | LOC | The only EBS-held localization: EBS-side statutory outputs under VS-79 change control. Employee-side outputs (2316/1601-C/1604-C/alphalist) are built in the payroll product (E7), not here |
| G5 | BIR EIS e-invoicing compliance (W473) | Invoice data stream + IAP to accredited channels | INT | POS edge is the accredited device; EBS supplies the invoice spine |
| G6 | Senior/PWD/solo-parent discount control (W432, VS-85) | QP qualifiers + eBTax exempt classes + audit reports | FIT-CFG | Eligibility capture at POS edge; EBS enforces pricing/tax and evidence |
| G7 | DTI price-freeze compliance (W468) | QP effective-date control + price-change audit report | FIT-CFG | Freeze windows as dated list activation |
| G8 | Compliance attribute capture (LGU permits W54, DENR/DOLE dates, COI) | EITs/DFFs on location, item, supplier entities | PER | Structured capture with alerts via workflow — no code |

### H. Technology & platform (VS-27, VS-28, VS-30, VS-113, VS-135)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| H1 | Rule-driven approvals across modules | Approvals Management (AME) rule sets | FIT-STD | Encodes the DMN PHP authorization ladders |
| H2 | Document workflow & business events | Oracle Workflow + WF_EVENT | FIT-STD | Integration eventing per [integrations.md](integrations.md) |
| H3 | E-signature evidence on controlled approvals | ERES | FIT-STD | Control evidence for the 808 register |
| H4 | RBAC, MOAC security profiles, SSO federation | FND RBAC/UMX + OID/OAM → corporate IdP | FIT-CFG | W152 lifecycle provisioning; W338 SoD queries |
| H5 | Operational dashboards (payables/receivables/inventory/procurement) | Enterprise Command Centers | FIT-STD | Tier-3 analytics without leaving the suite |
| H6 | Enterprise BI & data platform (VS-28) | In-house DP per operating model §5 | BUILD | EBS feeds DP; FSG/BIP/ECC own in-suite reporting |
| H7 | Integration platform & API management (W257) | In-house IAP per register; EBS natives (ISG, open interfaces, AQ, XML Gateway) behind it | BUILD | Architecture §5 rules |
| H8 | Archiving, masking, environment lifecycle (W384, W396) | EBS archiving strategy + clone masking profiles | FIT-CFG | RA 10173-aligned masking |
| H9 | Agentic automation runtime (VS-30/128) | In-house AAP per register §12 | BUILD | Tools reach EBS only through IAP contracts |
| H10 | Store/back-office UX adjustments | OAF personalizations + flexfields | PER | Metadata only; page-personalization export is the evidence |

---

## 3. Register Counts (Pinned)

| Class | Rows | Share |
|---|---|---|
| FIT-STD | 31 | 39.2% |
| FIT-CFG | 23 | 29.1% |
| **Standard total (STD + CFG)** | **54** | **68.4%** |
| PER | 2 | 2.5% |
| EXT | 2 | 2.5% |
| LOC | 1 | 1.3% |
| INT | 5 | 6.3% |
| EDGE | 0 *(retired)* | — |
| BUILD | 15 *(of which 5 already-built platforms: D6 POS, D7 ecommerce, D8 gift cards, D9 loyalty, D11 marketplace)* | 19.0% |
| OPEN | 0 *(resolved 2026-09-14)* | — |
| **Total register rows** | **79** | 100% |

> Reading: the two-tier doctrine (*in EBS → use it; otherwise → build*) leaves nothing to
> buy. Over two-thirds of the model company runs on EBS untouched or configured; the 2
> extensions are accounting-schedule builds with clean edges; the single EBS-held
> localization is the BIR indirect-tax pack; the 15 BUILD rows split into 5 platforms that
> already exist (integrate, don't rebuild) and 10 builds — of which 6 (OMO, TPS, AAP, IAP,
> DP) predate this doctrine and 4 are new scope it creates (payroll engine + statutory
> outputs, store workforce platform, dispatch, space-planning).

---

## 4. Formerly-Open Decisions — Resolution Record (2026-09-14)

The two-tier sourcing decision (*in EBS → use it; otherwise → build*) resolved the open
schedule and superseded the sourcing register's Buy rows. The register amendment is
recorded here as the authoritative interim decision; the sourcing-model rewrite
(§2 tier table, §4 rows, §5 archetype wording, §8 scope) is scheduled as the next
consistency wave.

| # | Decision | Resolution | Supersedes |
|---|---|---|---|
| 1 | Warehouse execution | **Resolved: Oracle WMS/MSCA adopted** — it ships in-suite, so per the doctrine we use it. The register's "re-evaluate when the ERP vendor ships native WMS at parity" trigger is answered by adoption, not assessment | Register row "Buy — BoB WMS" |
| 2 | Planning (forecasting/S&OP) | **Resolved: Oracle ASCP + Demantra** (EBS-family Value Chain Planning) are the planning stack; license cost is a FinOps decision, not a sourcing decision | Former OPEN row C5 |
| 3 | Vendor rebates/claims (VS-39) | **Resolved: Oracle Trade Management** (EBS-family) is the vehicle; license cost FinOps | B10's "evaluation" flag |
| 4 | TPRM tooling depth (VS-161) | Unchanged: EIT/AME registers in EBS. A specialist product would violate the doctrine; a build is admitted only through a CDR if the registers prove inadequate | B7 |
| 5 | ATS/LMS depth (VS-121/123) | Unchanged: in-suite iRecruitment/OLA per the doctrine; deeper function, if ever needed, is built — never bought | E2 |
| 6 | **POS estate** | **Recorded as an already-built in-house platform** — the program is integration (flows W533–W541), not sourcing | Register's Core-row POS treatment |
| 7 | **Payroll** | **Build decision: in-house Payroll PH** replaces the Oracle-Payroll-plus-localization plan; Oracle Payroll not adopted; Core HR (PER) and the GL stay in EBS; posting is E8 | Register Core-row "HR & payroll (PH statutory)" |
| 8 | Store workforce scheduling & dispatch | New build scope created by the doctrine (rows E3, D13); product remit (extend TPS vs new squads) assigned at the SIB/OM | Register's BoB WFM/FSM rows |

Each resolution above inherits the sourcing gate's control-mapping appendix duty
(sourcing model §3.3): the CTL evidence path for every re-scoped capability is named in
the re-dispositioned register rows.

---

## 5. Requirement-Section View (R1–R32)

How the 728 requirements' sections land against the register. This is orientation, not a
row-per-requirement register; the requirement-workflow matrix remains the
requirement-level source of truth.

| Section | Domain | Dominant disposition |
|---|---|---|
| R1 | Financial Management | FIT-STD/FIT-CFG (A1–A10) |
| R2 | Inventory Management | FIT-STD (C2/C4/C7–C10) |
| R3 | Procurement & Purchasing | FIT-STD (B1/B2/B4/B5/B8) |
| R4 | Warehouse Management | FIT-STD in-suite (C6: Oracle WMS/MSCA) |
| R5 | POS & Retail | Existing in-house POS — integrate (D6) + EBS masters (D2, G6) |
| R6 | Ecommerce Integration | Existing in-house platform — integrate (D7) + EBS fulfillment (D1) |
| R7 | Supply Chain Planning | FIT-CFG Oracle VCP stack (C5) + FIT-STD (C4, C14) |
| R8 | HR & Payroll | Core HR FIT-STD (E1/E2); payroll & workforce builds (E3, E5–E7) + interfaces (E4, E8) |
| R9 | CRM & Loyalty | Existing in-house loyalty stack (D9) + TCA master (D5) |
| R10 | Analytics & Reporting | FIT-STD in-suite + BUILD DP (H5/H6) |
| R11 | Intercompany & Transfer Pricing | FIT-STD (A7) |
| R12 | Document Management | Process-owned + ERES/attachments |
| R13 | Master Data Management | FIT-STD/FIT-CFG (C1, D5, B6) |
| R14 | Non-Functional | Platform provisions (architecture §7) |
| R15 | Installation & Services | FIT-STD-light (D1, F2) |
| R16 | Wholesale & Reseller | FIT-STD (D1) |
| R17 | Governance, Legal & Strategy | Process-owned + PER capture (G8) |
| R18–R24 | Cross-functional & gap-closure rounds | Follow the owning VS row above |
| R25 | Loss Prevention | Split: edge detection, EBS financial terminus |
| R26 | Business Continuity & DR | Platform-provided (Data Guard, offline POS replay) |
| R27 | Insurance & Claims | Process-owned + AP/FA entries |
| R28 | Vendor Portal & Supplier Collaboration | FIT-STD (B4) |
| R29 | Product Recall Management | Process + INV quarantine (C7/C10 support) |
| R30 | BI & Analytics Operations | BUILD DP + in-suite ECC |
| R31 | Customer Credit & Collections | FIT-STD (D3/D4) |
| R32 | Gap-closure round | Follow the owning VS row above |

---

## 6. The Philippine Statutory Split (EBS-held vs Payroll-built)

Under the two-tier doctrine the statutory surface splits cleanly along system ownership:
what EBS owns is localized once, in a bounded, format-driven pack; what the in-house
payroll build owns is built there. Nothing is duplicated across the two.

**EBS-held (the localization pack — 1 LOC row, G4):**

| Pack component | Builds | Statutory anchors (repo canon) |
|---|---|---|
| **BIR indirect-tax pack** | 2307/CWT certificates from AP withholding, VAT return datasets (2550M, 2551Q) from eBTax/SLA, CAS/POS annual inventory list (W478) | W475, W478, VS-79.1/79.2 |
| **eFPS/EIS submission datasets** | File generation for the G3/G5 channels (filing acts stay human-confirmed) | W260, W473 |

**Payroll-built (rows E5–E7, the in-house Payroll PH product):** SSS/PhilHealth/Pag-IBIG
tables, PD 851 13th month, BIR withholding tables and gross-to-net elements; agency
contribution/loan file formats; and the employee-side BIR outputs (2316, 1601-C, 1604-C,
alphalist). The build posts period costing journals to EBS (E8) — the ledger of record
never moves.

Rules: every pack output carries its statute/format citation; format-version changes are
handled as pack releases (never as edits inside month-end); neither the pack nor the
payroll build touches base-product objects (customization-governance §6); statutory filing
acts remain human-confirmed — the agentic hard boundary (sourcing model §12.1) applies.

---

## 7. Standard-First KPIs

| KPI | Target | Enforcement |
|---|---|---|
| Capability rows on standard EBS (STD+CFG) | ≥ 65% steady state (current 68.4%) | This register, re-run per wave |
| Best-of-breed capability products | **0 — absolute under the two-tier doctrine** | Sourcing register (amendment per §4) |
| Extensions (EXT) in production | ≤ 10; each with a CDR + de-customization trigger | CEMLI register (customization-governance §7) |
| Modifications (M-class) | **0** — absolute | CEMLI register gate; patch rehearsal (PATCH env) |
| Personalizations | ≤ 150; metadata-only | Personalization export inventory |
| Localization pack outputs with statute citation | 100% | Pack release checklist |
| RUP currency | Within one RUP of current 12.2 RU; CPU applied ≤ 30 days | PATCH-env rehearsal record (W1409 change control) |
| OPEN decisions lingering | 0 past their SIB date — currently 0 rows | §4 resolution record review at each QBR |

---

*Document Version: 1.1 | Date: 2026-09-14 | Two-tier sourcing doctrine enacted (*in EBS → use it; otherwise → build*): register re-dispositioned 76 → 79 rows (54 standard / 2 PER / 2 EXT / 1 LOC / 5 INT / 15 BUILD of which 5 already-built / 0 EDGE / 0 OPEN); Oracle WMS/MSCA adopted in-suite (C6), Oracle ASCP + Demantra adopted (C5), OTM resolved (B10), POS/ecommerce/loyalty/gift-card recorded as already-built platforms (D6–D11), payroll re-scoped to an in-house build with Oracle Payroll unadopted (E3–E8), BoB WMS/TMS/WFM/FSM rows superseded (§4 resolution record, incl. the sourcing-register amendment schedule). Prior v1.0 (2026-09-14): initial issue — fit classes, 76-row capability disposition register (52 standard / 2 PER / 2 EXT / 4 LOC / 4 INT / 7 EDGE / 4 BUILD / 1 OPEN), SIB open-decision schedule, R1–R32 orientation view, PH localization pack definition, standard-first KPIs. Register counts pinned above; canon anchors: 728 Req / 5,427 WF / 808 CTL / sourcing register §4 / ATC & statutory forms per repo canon.*
