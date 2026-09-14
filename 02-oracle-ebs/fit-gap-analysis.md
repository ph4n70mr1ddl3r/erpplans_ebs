# Fit-Gap Analysis — Oracle EBS vs. the Model Company

> The governing document of the "make the most of it" doctrine. Every capability domain the
> 5,427 workflows demand is dispositioned against standard Oracle EBS 12.2 in one of nine
> fit classes. **Only 2 of 76 capability rows require true extensions**; 4 are Philippine
> statutory localizations; 7 are the sourcing register's edge products; 4 are the register's
> in-house builds. Everything else — 52 rows — runs on unmodified EBS via setup and
> configuration alone.

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
| **EDGE** | Executed by a best-of-breed product per the [sourcing register](../07-methodology/capability-sourcing-and-engineering-model.md) §4; EBS holds the masters/ledger | — (Buy) | Register row, IAP contract |
| **BUILD** | Executed by an in-house product per the register §4 (OMO, TPS, AAP, IAP, DP) | — (Build) | Register row |
| **OPEN** | Genuine open decision — scheduled for the SIB with a scored assessment (W5515 gate) | — | SIB agenda item |

Ladder rule: the lowest class that closes the gap wins. An EXT is admitted only after a
FIT-CFG, PER, and (where applicable) EDGE alternative is documented as inadequate.

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

### C. Supply chain & inventory (VS-01, VS-02, VS-04, VS-05, VS-29, VS-31, VS-45, VS-92, VS-111, VS-127)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| C1 | Item master, catalog categories, templates (W252, W290) | INV + EGO item catalogs/templates + Web ADI mass maintenance | FIT-CFG | VS-29 governance runs via workflow; ~55,000 item-master records |
| C2 | UOM & conversions, catch-weight flags (W294) | INV UOM classes & conversions | FIT-STD | Lumber/wire catch-weight per data-migration mapping |
| C3 | Org/subinventory/locator model (200 stores + 4 DCs + master org) | INV organizations + MOAC security profiles | FIT-CFG | Architecture §1; W16 add-org runbook |
| C4 | Replenishment — min-max/reorder points (W2, W2A, W4) | INV min-max planning + reorder-point planning | FIT-STD | Parameter governance W312 |
| C5 | Statistical forecasting, S&OP/IBP surface (W31, W133, VS-127) | ASCP + Demantra (license-flagged) vs in-house forecast pipeline | OPEN | Scored SIB assessment (§4); neither adopted by default |
| C6 | RF-directed warehouse execution (putaway/pick, LPNs) | BoB WMS per register; Oracle WMS/MSCA satisfies the register's parity trigger | EDGE | SIB parity assessment scheduled (§4) — register default stands until re-affirmed |
| C7 | Cycle counting & physical inventory (W6, W42) | INV cycle counts (ABC classes), physical inventory tags | FIT-STD | Vendor-owned counts via consignment receipt revaluation |
| C8 | Inter-org transfers & in-transit tracking (W22, W204, W218) | INV internal requisitions, in-transit inventory | FIT-STD | Inter-island freight allocation via landed cost/payload DFFs |
| C9 | Kits, bundles, build-to-order assembly (W46, VS-92) | BOM + WIP (light) / OM kits | FIT-STD | Assemble-to-order kits for VS-92 |
| C10 | Supplier consignment (W20, W23, VS-45) | EBS consigned inventory (supplier-owned onhand, consumption trigger) | FIT-STD | Sell-through triggers vendor settlement per W543 |
| C11 | VMI data collaboration (W20/W422) | iSupplier planning reports + onhand feeds | FIT-CFG | Vendor-side optimization is the vendor's system |
| C12 | Incoming inspection, supplier quality data (W110, VS-31) | Oracle Quality collection plans | FIT-STD | CAPA workflow on quality notices; deep QMS stays process |
| C13 | Pallets/RTI & packaging tracking (VS-111, W270) | LPN tracking + deposit-bearing DFFs | FIT-CFG | Deposit accounting via AP/AR; pooling stays contractual |

### D. Order-to-cash & retail (VS-07, VS-08, VS-10, VS-11, VS-16, VS-32, VS-54, VS-57, VS-60, VS-95)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| D1 | Trade/corporate orders: quotes (W58), agreements & call-offs (W163/W164), drop-ship (W246) | OM quotes, sales agreements, blanket releases, back-to-back orders | FIT-STD | Retention/milestone billing via Projects (F1) |
| D2 | Pricing: lists, modifiers, quantity breaks, coupons (W40/W93/W539), PH mandatory discounts (VS-85) | Advanced Pricing lists/qualifiers/modifiers + eBTax | FIT-CFG | Senior/PWD/solo-parent qualifiers; price-change governance W107/W289 |
| D3 | Credit management & holds (W24, W328, W229) | Oracle Credit Management + OM holds | FIT-STD | Scoring rules + exception approvals via AME |
| D4 | Collections & dunning (W108, VS-16.3) | Advanced Collections strategy/dunning | FIT-STD | PDC aging from AR terms |
| D5 | Customer master, dedup, hierarchy (W253, W460) | TCA + Data Quality Management | FIT-STD | ~5,400 AR accounts canon; party/site/account model |
| D6 | POS estate & checkout execution (VS-08) | POS edge under EBS item/price/tax masters | EDGE | Core-tier capability, edge realization — architecture §1 rationale; no EBS POS exists |
| D7 | Ecommerce platform (VS-10) | Ecom edge; EBS order import + availability feeds | EDGE | iStore deliberately not adopted (module-coverage §3) |
| D8 | Gift cards & stored value (VS-54) | Gift-edge ledger; EBS holds GL liability + IC settlement (W28) | EDGE | Breakage/dormancy per W5511 remains process on the GL |
| D9 | Loyalty program engine (W17, VS-13) | Loyalty edge; points-as-tender posts to AR/POS settlement (W550) | EDGE | TCA remains the member master of record |
| D10 | Omnichannel order routing & mixed-basket orchestration (VS-60) | In-house OMO per register §4 | BUILD | EBS OM carries the fulfillment legs OMO routes |
| D11 | Marketplace operator / 3P-seller settlement (VS-95) | Marketplace edge; AR reconciliation of commissions | EDGE | Payout files reconcile to AR/AP via IAP |
| D12 | Cross-channel returns & exchanges (VS-32, W12 family) | OM RMAs + AR credit memos + INV adjustments | FIT-CFG | Edge executes the counter transaction; EBS owns the RMA/credit lifecycle |

### E. HR & payroll (VS-19, VS-102, VS-121, VS-123, VS-183)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| E1 | Core HR: org/positions/employees/EITs, absence types | Oracle HRMS (PER) | FIT-STD | W15/W43/W292; license/EIT data for VS-166 registers |
| E2 | Recruitment, self-service, learning & performance (W51, VS-121) | iRecruitment + Self-Service HR + OLA | FIT-STD | Deep ATS/LMS = future SIB candidates if adoption lags (§4) |
| E3 | Store time & attendance → payroll | BoB WFM feeds → BEE (Batch Element Entry) | INT | Payroll rules stay in EBS; capture stays at the WFM edge |
| E4 | PH statutory payroll engine (W10) | Oracle Payroll configured for PH + localization pack | LOC | Gross-to-net with SSS/PhilHealth/Pag-IBIG tables, PD 851 13th month, night differential/OT elements, BIR withholding tables — see §6 |
| E5 | Statutory contributions & loan deductions (W251, W76) | PAY element links + deduction AR/AP interfaces | LOC | Agency file formats (R3/RF1/PF-class) in the pack |
| E6 | BIR compensation reporting: 2316, 1601-C, 1604-C, alphalist (W90, W5533) | BI Publisher formats from PAY balances | LOC | Per BIR publish formats; eFPS submission via G3/G5 channels |
| E7 | Payroll costing to GL | PAY costing → SLA → GL | FIT-STD | Included in E4 pack scope but standard machinery |

### F. Projects, assets & property (VS-20, VS-35, VS-40, VS-42, VS-55, VS-97, VS-109)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| F1 | Capex request → PO → CIP → asset turnover (W21, W276) | Projects (costing) + PO + FA mass additions | FIT-STD | VS-40 chain is fully native |
| F2 | Construction/new-store cost capture (W223–W227) | Projects cost capture against store WBS | FIT-STD | VS-20/109; PMO scheduling stays external |
| F3 | Lease administration, rent/CAM/indexation, real-property tax (W117/W118/W119) | Property Manager leases, payment schedules, indexation | FIT-STD | Critical-date workflows; PFRS-16 accounting via A12 |
| F4 | Planogram & space optimization (W86, VS-55) | No EBS function | EDGE | Space-planning edge; compliance checks feed VS-55 processes |

### G. Statutory & compliance (VS-79, VS-85, VS-118)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| G1 | PH VAT determination & return data (2550M, 2551Q) | eBTax configuration (rates, VATEX classes, per-document tax lines) | FIT-CFG | VS-79.1; zero-rated/VAT-exempt certification data |
| G2 | EWT / expanded withholding at AP | eBTax withholding + AP withholding tax groups | FIT-CFG | ATC canon; 2307 generation via G4 pack |
| G3 | BIR eFPS filing submission (W260) | File generation + IAP submission to eFPS | INT | Filing acts remain human-confirmed (agentic hard boundary, sourcing model §12.1) |
| G4 | BIR statutory report pack: CAS/POS inventory lists (W478), 2307, alphalist data, 1604-C pack | BI Publisher statutory formats from EBS/PAY | LOC | Format-versioned pack under VS-79 change control |
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
| FIT-STD | 30 | 39.5% |
| FIT-CFG | 22 | 28.9% |
| **Standard total (STD + CFG)** | **52** | **68.4%** |
| PER | 2 | 2.6% |
| EXT | 2 | 2.6% |
| LOC | 4 | 5.3% |
| INT | 4 | 5.3% |
| EDGE | 7 | 9.2% |
| BUILD | 4 | 5.3% |
| OPEN | 1 | 1.3% |
| **Total register rows** | **76** | 100% |

> Reading: two-thirds of the model company runs on EBS untouched or configured. The 2
> extensions are both accounting-schedule builds (PFRS 15/16) with clean edges; the 4
> localizations are Philippine statutory outputs the suite could never ship; every EDGE and
> BUILD row was already decided by the sourcing register — this analysis adds no new buys
> and no new builds.

---

## 4. Open Decisions Scheduled for the SIB (W5515 Gate)

| # | Decision | Options | Register tie-in | Target |
|---|---|---|---|---|
| 1 | **Warehouse execution: Oracle WMS/MSCA vs BoB WMS** | In-suite Oracle WMS (licensed with EBS, RF-directed, LPN-native) vs the register's BoB WMS | The register's own re-evaluation trigger — "ERP vendor ships native WMS at parity" — is satisfied by Oracle WMS's existence; the parity assessment must be run, not assumed | Before Wave-2 build |
| 2 | **Planning: ASCP + Demantra vs in-house forecast/ROP pipeline** | License the EBS-stack planners vs extend the VS-02/127 automation surface | C5 is the only OPEN row | Before Wave-2 planning setup |
| 3 | **Oracle Trade Management for vendor rebates/claims (VS-39)** | OTM license vs PO-accrual + claims workflow | B10 license flag | Before Wave-1 P2P cutover |
| 4 | **TPRM tooling depth (VS-161)** | EIT/AME registers (current disposition) vs specialist TPRM product | B7; no register change unless bought | Annual review |
| 5 | **ATS/LMS depth (VS-121/123)** | iRecruitment/OLA (current) vs specialist products | E2 note | Post-stabilization review |

Each decision follows the sourcing gate's mandatory appendices (IAP estimate,
control-mapping, TCO, exit/run plan, re-evaluation trigger) — sourcing model §3.3.

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
| R4 | Warehouse Management | EDGE + FIT-STD ledger (C6) |
| R5 | POS & Retail | EDGE + EBS masters (D2/D6, G6) |
| R6 | Ecommerce Integration | EDGE + EBS fulfillment (D7) |
| R7 | Supply Chain Planning | OPEN (C5) + FIT-STD (C4) |
| R8 | HR & Payroll | FIT-STD + LOC pack (E1–E7) |
| R9 | CRM & Loyalty | EDGE + TCA master (D5/D9) |
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

## 6. The Philippine Localization Pack (the Genuine Gaps)

The four LOC rows are the only places where Philippine statute forces country-specific
builds. They are bounded, format-driven, and versioned — not open-ended customization.

| Pack component | Builds | Statutory anchors (repo canon) |
|---|---|---|
| **PAY-PH gross-to-net** | Elements & formulas: basic/OT/night differential, 13th-month (PD 851), SSS/PhilHealth/Pag-IBIG employee/employer shares, BIR withholding tables; BEE import path (INT E3 feeds it) | W10, W251, VS-19.2 |
| **Agency file interfaces** | Contribution/loan file formats and posting reconciliation | W251, VS-19.2 |
| **BIR compensation pack** | 2316, 1601-C, 1604-C, alphalist per current BIR publish formats | W90, W5533, VS-79 |
| **BIR indirect-tax pack** | 2307/CWT certificates, alphalist data, CAS/POS annual inventory list (W478), VAT return datasets (2550M/2551Q) | W475, W478, VS-79.1/79.2 |

Rules: every pack output carries its statute/format citation; format-version changes are
handled as pack releases (never as edits inside month-end); the pack never touches
base-product objects (customization-governance §6). Statutory filing acts remain
human-confirmed — the agentic hard boundary (sourcing model §12.1) applies.

---

## 7. Standard-First KPIs

| KPI | Target | Enforcement |
|---|---|---|
| Capability rows on standard EBS (STD+CFG) | ≥ 65% steady state (current 68.0%) | This register, re-run per wave |
| Extensions (EXT) in production | ≤ 10; each with a CDR + de-customization trigger | CEMLI register (customization-governance §7) |
| Modifications (M-class) | **0** — absolute | CEMLI register gate; patch rehearsal (PATCH env) |
| Personalizations | ≤ 150; metadata-only | Personalization export inventory |
| Localization pack outputs with statute citation | 100% | Pack release checklist |
| RUP currency | Within one RUP of current 12.2 RU; CPU applied ≤ 30 days | PATCH-env rehearsal record (W1409 change control) |
| OPEN decisions lingering | 0 past their SIB date | §4 table review at each QBR |

---

*Document Version: 1.0 | Date: 2026-09-14 | Initial issue — fit classes, 76-row capability disposition register (52 standard / 2 PER / 2 EXT / 4 LOC / 4 INT / 7 EDGE / 4 BUILD / 1 OPEN), SIB open-decision schedule, R1–R32 orientation view, PH localization pack definition, standard-first KPIs. Register counts pinned above; canon anchors: 728 Req / 5,427 WF / 808 CTL / sourcing register §4 / ATC & statutory forms per repo canon.*
