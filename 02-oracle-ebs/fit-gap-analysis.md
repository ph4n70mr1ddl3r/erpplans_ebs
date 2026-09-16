# Fit-Gap Analysis — Oracle EBS vs. the Model Company

> The governing document of the doctrine. Per the 2026-09-14 **two-tier sourcing decision**: *if it's in Oracle EBS we use it; otherwise we build.* Every capability domain the
> 5,427 workflows demand is dispositioned against standard Oracle EBS 12.2 in one of the fit
> classes below. In the **97-row register**: **74 rows (76.3%) run on standard or configured
> EBS**; 2 are personalizations; **1 is a true extension** (the PFRS 16 ROU schedule — its
> PFRS 15 sibling was retired when the 2026-09-16 second-pass exhaustion audit found Oracle
> Revenue Management and Invoicing in-suite); 1 is the EBS-held Philippine indirect-tax
> localization; 5 are interfaces; and **14 are in-house builds — of which 5 are already-built
> platforms (the in-house POS estate, the custom ecommerce platform, and the gift-card/loyalty
> stack) that integrate rather than get bought or rebuilt**. The former best-of-breed buy tier
> is retired (zero rows); the two formerly-OPEN planning decisions resolved in-suite; the
> 2026-09-15 **EBS-exhaustion audit** re-pointed five capabilities in-suite (dispatch core →
> Field Service, D13; lessor leasing → Lease & Finance Management, A13; T&E expenses →
> Internet Expenses, B11; benefits enrollment → Advanced Benefits, E9; service requests →
> Teleservice, D14); and the 2026-09-16 **second-pass exhaustion audit** adopted seven more
> native vehicles the register had left unnamed or mis-dispositioned — Enterprise Asset
> Management (F5), Procurement Contracts (B12), Global Order Promising (D15), Oracle
> Configurator for in-store fabrication (C16), In-Memory Cost Management (C15), GL budgets +
> budgetary control (F6) and Oracle Alert (G9) — and retired the PFRS 15 extension through
> its de-customization trigger (A11 → Revenue Management and Invoicing), re-auditing every
> 'Not in EBS' and 'no native vehicle' claim against the suite's full 12.2 catalog; and the
> 2026-09-16 **third-pass exhaustion audit** swept the workflows' still-generic vehicle names
> against the suite's receivables-instrument, service-chain and people modules, adopting six
> more native vehicles the 5,427 workflows invoke without naming — AR Lockbox + Balance
> Forward Billing + iReceivables for the trade collections/statement spine (A14), Purchasing
> Contingent Labor for the outsourced-workforce spend (B13), Engineering ECO/ECN for kit/BOM
> revision governance (C17), Install Base + Service Contracts for the warranty/extended-
> warranty chain (D16), Depot Repair for in-house repair orders (D17) and Compensation
> Workbench for the merit/salary-cycle surface (E10) — and trued the realization notes on
> five rows (A3 → AR Bills Receivable for the PDC instrument register; A13 extended to the
> tool/self-haul/storage/equipment rental family; C1 → Product Hub item governance; C3 →
> Site Hub site-attribute register; H6 → GoldenGate CDC as the DP feed); and the 2026-09-16
> **fourth-pass exhaustion audit** trued three more realization notes the register still
> carried as generic function — AP Bills Payable for the outgoing-PDC instrument register
> (A3, the AR-side Bills-Receivable counterpart), Oracle eAM for the delivery-fleet vehicle
> estate (F5, retiring the coverage-map's 'no EBS fleet product' claim) and Oracle
> Performance Management appraisals/objectives for the W72 review cycle (E2); and the
> 2026-09-16 **fifth-pass exhaustion audit** trued the DC workflows' still-generic
> warehouse-optimization vehicle names onto the adopted WMS product's own advanced-function
> family — **WMS Slotting** (W784/W1402), **planned crossdocking** (W221/W1226/W1279/W1307
> and the W3 cross-dock variant), **WMS Labor Management** (W796), **WMS Yard Management**
> (W222/W585/W1353) and **Cartonization** (W3099 dark-store pack) — and named **Oracle
> Succession Planning** as the W178 talent-pool/readiness/career-path vehicle (E2); and the
> 2026-09-16 **sixth-pass exhaustion audit** swept the governance and platform surfaces one
> more time: the VS-21 audit workflows' generic 'Audit Management portal / GRC Tool'
> vehicles named a module the suite itself ships — **Oracle Internal Controls Manager
> (ICM)** adopted as the audit-management/controls-governance surface (H11: the audit plan
> & risk register W120, assessments & reporting W121/W336, findings/CAP & investigation
> case tracking W333/W334/W123/W159, PBC evidence W351, and the CTL-01–CTL-808 control
> library itself; W332's continuous-
> monitoring analytics and W338's SoD role queries stay the detection/evidence feeds) —
> and the environment-lifecycle row (H8) trued to the suite's native toolchain (**Rapid
> Clone** cloning on the on-premises estate, **Oracle iSetup** setup-data templating and
> post-refresh verification across the four non-prod environments — retiring W384's stray
> AWS/Azure-console touchpoint against the on-premises deployment canon).

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
| A3 | AR invoicing, credit memos (W540), PDC registers — customer-side (W423/W1380) and AP-side outgoing (W424) | AR + AutoInvoice + special terms; **customer PDC instruments ride AR Bills Receivable** — BR creation at receipt, maturity reports, bank remittance batches, unpaid-BR (dishonor) handling; **outgoing PDCs ride AP Bills Payable** — future-dated payment instruments with issued-but-unreleased memo treatment, maturity reports and clearing to CE | FIT-CFG | Customer-side PDC maturity via the BR register + CE reconciliation (W423/W1380/W425/W1381). The 2026-09-16 fourth-pass audit trues the AP side: W424's 'Issued PDC Register' with its memo liability (Unreleased PDCs) and 'Daily AP PDC Maturity Report' is Bills Payable's native instrument register — the AR-side Bills-Receivable counterpart the third pass left on special terms |
| A4 | Bank statement reconciliation | Cash Management (CE) auto-reconciliation | FIT-STD | W89, W537/W541 feeds |
| A5 | Bank payment files, positive-pay controls | Payments (IBY) formats | FIT-CFG | Per-bank formats for BDO/BPI/MB/CB (integration map) |
| A6 | Fixed assets, depreciation, disposals, CIP turnover | FA + mass additions | FIT-STD | W39, W184, W276 |
| A7 | Intercompany billing & settlement | Advanced Global Intercompany System (AGIS) | FIT-STD | W14, W461, W435 IC SLA billing |
| A8 | Cash positioning, investments, debt/covenants, FX deals | Oracle Treasury (XTR) + CE | FIT-CFG | VS-18.1–18.3; W80 hedging; BSP-report data via XTR extracts |
| A9 | Bad-debt provisioning & write-offs | AR aging buckets + approval workflows | FIT-CFG | W81 provision ladder as AME-governed journals |
| A10 | Revenue recognition — retail & wholesale point-of-sale revenue | Standard AR/OM invoicing | FIT-STD | Single-performance-obligation sales need no RevRec engine |
| A11 | PFRS 15 — complex multi-element contracts (project sales, service bundles, subscription deferral) | **Oracle Revenue Management and Invoicing (RM&I)** — multi-element arrangements, SSP-based allocation, contingency & event-based revenue schedules, invoicing coordination | FIT-CFG | The 2026-09-16 second-pass audit **corrects this row's original 'No native multi-element schedules' claim**: RM&I ships in-suite, so per the doctrine the planned bounded schedule engine is **retired through its de-customization trigger before any build lands** (customization-governance §7). Serves W162 project quotes, W165 retention/milestone billing, W1018/W1288/W1426 progress billing, W1978 subscription deferred revenue, W793 close-out; VS-157 |
| A12 | PFRS 16 — ROU asset & lease-liability schedules | Property Manager administers leases, not ROU amortization | EXT | Amortization schedule build feeding GL/FA from PN contracts; VS-148 |
| A13 | Lessor equipment leasing: booking, billing, assets, end-of-term (VS-96, W3165–W3176) | Lease & Finance Management (lease contracts, billing schedules → AR, asset/end-of-term tracking) | FIT-CFG | The 2026-09-15 exhaustion audit names the vehicle the VS-96 workflows' 'lease management system' touchpoint assumed: it ships in-suite, so per the doctrine we use it; insurance/maintenance bundling rides Service Contracts. The 2026-09-16 third-pass audit extends the same vehicle to the whole rental family — the rental-transaction lifecycles of VS-12.2 tool rental (W139), VS-162 self-haul truck/van rental, VS-174 portable-container rental and VS-186 equipment rental (W5325–W5334) ride L&FM rental contracts and reservations (per-unit serial + availability windows, with eAM holding maintenance availability); the PA-186.2 'Rental reservation module' touchpoint names this vehicle |
| A14 | Trade collections acceleration & statement billing: remittance auto-application, consolidated monthly statements, customer self-service inquiry (W892, W1117, W1022, W99, W108, W1382; ~5,400 trade/corporate accounts) | **AR Lockbox** (bank remittance files auto-applied to open invoices — check-heavy trade receipts), **AR Balance Forward Billing** (consolidated statement cycles: opening balance → transactions → closing balance per W1117's SOA canon), **iReceivables** (account self-service inquiry feeding the W936 trade-portal data) | FIT-CFG | The 2026-09-16 third-pass audit: W1117's SOA generation and W892's statement runs named a generic 'document generation engine over the AR module' while the suite ships the statement-cycle engine natively; electronic receipts (PESONet/InstaPay) keep the W1382 CE/AR matching feed, Lockbox carries the remittance-advice form |

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
| B10 | Vendor rebates, promotions & claims (VS-39, W27, W161) | PO accruals + Trade Management evaluation | FIT-CFG | **Resolved in-suite per §4 resolution 3**: Oracle Trade Management is the vehicle (license cost is a FinOps decision, not a sourcing decision); PO accruals remain the staging surface feeding OTM claims |
| B11 | Employee expense reports & the corporate-card program (W74, PA-15.2 card reconciliation) | Internet Expenses (iExpenses): expense reports, receipt upload, policy limits, AME approvals, GL/cost-center coding; AP card-program statement loads | FIT-CFG | The 2026-09-15 exhaustion audit names the vehicle the W74 self-service claim form assumed: expense capture, policy validation and card-statement reconciliation are native; reimbursement lines flow to payroll/AP as today |
| B12 | Vendor contract authoring, clause governance, deliverables & expiry/compliance tracking (W62/W62B lifecycle, W669 compliance monitoring & enforcement, W241 facility-vendor SLAs) | **Oracle Procurement Contracts** — contract authorship from the standard clause library, deliverables with due dates, expiration/amendment alerts, integration with PO agreements and receipts | FIT-CFG | The 2026-09-16 second-pass audit names the vehicle the W669 'contract management module' touchpoint assumed: authoring, deliverables and compliance tracking are native; legal review rides W230 with the contract record as evidence spine. Serves W669, W155 JBP terms, W513 vendor-funded-promo terms, W62/W62B 3PL & services contracts, W241 cleaning/security/canteen SLAs |
| B13 | Contingent & outsourced workforce procurement: agency/staffing workers on rate terms, timecard-to-invoice flows, contingent-worker registration (VS-98, W3209–W3232 — agency & service-contractor sourcing W3210, onboarding/access W3215-class, time operations W3220, consolidated agency invoicing W3221) | **Purchasing Contingent Labor** — contingent-worker POs against staffing agreements with negotiated rate terms, timecard-driven invoice generation to AP, and contingent-worker registration in HR (_vs._ employee hiring in E1) | FIT-STD | The 2026-09-16 third-pass audit: the VS-98 workflows' 'work-order/agency portal' touchpoints named no procurement vehicle while the suite ships contingent-labor purchasing natively; the pa-98.2 ST row names it. Promodizers (W269/W429/W449) and the in-house workforce platform (E3) are unaffected — contingent labor covers the agency/outsourced-function spend |

### C. Supply chain & inventory (VS-01, VS-02, VS-04, VS-05, VS-06, VS-29, VS-31, VS-45, VS-92, VS-111, VS-127)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| C1 | Item master, catalog categories, templates (W252, W290) | INV + EGO item catalogs/templates + **Oracle Product Hub** as the item-governance layer (data-quality rules, item-request workflow, template-driven multi-org rollout) + Web ADI mass maintenance | FIT-CFG | VS-29 governance runs via workflow; ~55,000 item-master records. The 2026-09-16 third-pass audit names the governance layer above INV/EGO — the W252 item-request/approval chain and the VS-29 quality registers are Product Hub's native function; customer-facing PIM/DAM content stays with the in-house build (VS-137) |
| C2 | UOM & conversions, catch-weight flags (W294) | INV UOM classes & conversions | FIT-STD | Lumber/wire catch-weight per data-migration mapping |
| C3 | Org/subinventory/locator model (200 stores + 4 DCs + master org) | INV organizations + MOAC security profiles; **Oracle Site Hub** carries the site-attribute register on the location model (permits/COI/utilities/contacts per site, open/close milestones — W254/W16/W54; G8 capture pattern) | FIT-CFG | Architecture §1; W16 add-org runbook. The 2026-09-16 third-pass audit names the site-attribute vehicle behind the W254 location-master lifecycle and the G8 EIT register |
| C4 | Replenishment — min-max/reorder points (W2, W2A, W4) | INV min-max planning + reorder-point planning | FIT-STD | Parameter governance W312 |
| C5 | Statistical forecasting, S&OP/IBP surface (W31, W133, VS-127) | **Oracle ASCP + Demantra** (EBS-family Value Chain Planning stack) | FIT-CFG | Resolved per the two-tier doctrine — the planning stack is Oracle's, so we use it; license cost is a FinOps decision, not a sourcing decision. The 2026-09-16 second-pass audit names the same stack's **Inventory Optimization** (multi-echelon) and **Rapid Planning** engines for VS-136's network/MEIO engineering (W4129–W4136) — same adoption, same FinOps posture |
| C6 | RF-directed warehouse execution (putaway/pick, LPNs) and the warehouse-optimization layer the DC workflows invoke: slotting, crossdocking, labor productivity, yard/dock, cartonization (W784/W1402; W221/W1226/W1279/W1307 + the W3 cross-dock variant; W796; W222/W585/W1353; W3099) | **Oracle WMS/MSCA — in-suite, adopted**, including its advanced-function family: **WMS Slotting** (velocity classification, golden-zone assignment, re-slot move lists), **planned crossdocking** (ASN-to-order allocation, staging lanes, putaway bypass), **WMS Labor Management** (engineered standards, real-time productivity), **WMS Yard Management** (dock-door calendars/appointments, gate check-in, trailer & slot tracking), **Cartonization** (cube-based right-box selection at pack) | FIT-STD | Resolved per the two-tier doctrine: warehouse execution ships with EBS, so we use it; the sourcing register's BoB WMS row is superseded (§4 resolution record). The 2026-09-16 fifth-pass audit trues the generic 'WMS slotting optimization module' / 'cross-dock allocation module' / 'WMS labor management module' / 'Yard Management System (YMS)' / dock-calendar touchpoints to the adopted product's own advanced-function family |
| C7 | Cycle counting & physical inventory (W6, W42) | INV cycle counts (ABC classes), physical inventory tags | FIT-STD | Vendor-owned counts via consignment receipt revaluation |
| C8 | Inter-org transfers & in-transit tracking (W22, W204, W218) | INV internal requisitions, in-transit inventory | FIT-STD | Inter-island freight allocation via landed cost/payload DFFs |
| C9 | Kits, bundles, build-to-order assembly (W46, VS-92) | BOM + WIP (light) / OM kits | FIT-STD | Assemble-to-order kits for VS-92 |
| C10 | Supplier consignment (W20, W23, VS-45) | EBS consigned inventory (supplier-owned onhand, consumption trigger) | FIT-STD | Sell-through triggers vendor settlement per W543 |
| C11 | VMI data collaboration (W20/W422) | iSupplier planning reports + onhand feeds | FIT-CFG | Vendor-side optimization is the vendor's system |
| C12 | Incoming inspection, supplier quality data (W110, VS-31) | Oracle Quality collection plans | FIT-STD | CAPA workflow on quality notices; deep QMS stays process |
| C13 | Pallets/RTI & packaging tracking (VS-111, W270) | LPN tracking + deposit-bearing DFFs | FIT-CFG | Deposit accounting via AP/AR; pooling stays contractual |
| C14 | Transport planning, carrier tendering & freight audit (VS-06, VS-110) | Shipping Execution + Transportation Execution (in-suite) | FIT-STD | The register's BoB TMS row is superseded — tender, ship-confirm and freight-cost capture are in-suite; optimization beyond OTE is a build candidate, never a buy |
| C15 | Perpetual costing & margin analytics (W85 costing/margin review, W633 PPV, W4136 inventory-investment optimization, VS-101 OTB margin) | **Oracle In-Memory Cost Management** — real-time cost/margin analytics over the 12.2 in-memory column store on the INV/OM ledger | FIT-STD | The 2026-09-16 second-pass audit: the 12.2-native in-memory cost analytics serve W85, W633 and W4136 without leaving the suite; enterprise BI stays with DP (H6) — in-suite analytics cover the operational questions, DP the cross-domain ones |
| C16 | Rules-driven configuration & quoting for in-store custom fabrication (cut-to-length lumber/wire, glass, pipe, rebar, screens, countertops, door/window sizing) | **Oracle Configurator (CZ)** — dimension/attribute rules driving ATO models (BOM) and QP-integrated configuration quotes, **in-store counter scope** | FIT-CFG | The 2026-09-16 second-pass audit: CZ is adopted **for in-store counter services only** — the architecture's 'CZ for B2C' non-adoption stands (storefront configuration stays with the in-house ecommerce platform, D7). Serves W1009 custom-order quotation lifecycle, W943 glass, W944 pipe, W946 screens, W986 rebar, W988 welding, W1045 PVC, W1054 wire cut-to-length, W1059 countertops, W1046 door/window sizing |
| C17 | Kit/BOM revision & private-label spec change control: structured change requests with approval workflow, effectivity dates, revision history (W302 kit/BOM structure master governance, W46 kit assembly definitions, VS-92 build-to-order structures, VS-41 private-label product development W129-family spec changes) | **Oracle Engineering (ENG)** — Engineering Change Orders/Notices with routed approvals over BOM/routing revisions and effectivity control, feeding BOM/WIP execution | FIT-STD | The 2026-09-16 third-pass audit: the kit/BOM master-governance and private-label spec chains name no revision-control vehicle while the suite ships ECO/ECN workflow natively — W302's versioned structure changes and W129's private-label spec revisions ride ECOs; mass rule changes stay with the C1 governance layer |

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
| D13 | Installation & home-service dispatch, technician mobile app (VS-12) | **Oracle Field Service** — task assignment, dispatch scheduling, technician debrief & the mobile field device, on Install Base serviced assets | FIT-CFG | The 2026-09-15 exhaustion audit **corrects this row's original 'Not in EBS' claim**: the dispatch core ships in-suite, so per the doctrine we use it. The in-house build (register §4 resolution 8; product remit at the SIB/OM) narrows to what Field Service does not ship — the consumer appointment/route-optimization experience and the contractor portal for the third-party installer network (VS-172) |
| D14 | Customer service requests & complaint escalation (W41, VS-13.1) | Teleservice / Service Requests + Escalation Management on the TCA party model | FIT-CFG | The 2026-09-15 exhaustion audit: multi-channel capture stays with the in-house CX surfaces; the ticket, SLA timers, tiered escalation and resolution coding are native — CSAT analytics may ride either side |
| D15 | Multi-org available-to-promise & allocation-aware promising (W56 backorders, W1114 availability lookup & reservation, VS-93 dark-store wave promising, W164/W979 call-off scheduling) | **Oracle Global Order Promising (GOP)** — cross-org promising over onhand, in-transit and expected supply, with allocation rules and ATP time series | FIT-STD | The 2026-09-16 second-pass audit names the native engine behind the 'ATP + scheduling' shorthand: promising spans DC, store and in-transit inventory with allocation rules for scarce stock — the omnichannel orchestrator (D10, in-house) stays the router, GOP is the promising engine it queries |
| D16 | Warranty & extended-warranty/service-contract lifecycle: registration at POS/ecommerce/trade with serial capture, coverage verification, claims, transfers, expiry alerts, renewal offers (VS-53 W2118–W2135, W33 warranty claims at POS, W544 service work orders, VS-155 trade-in provenance checks) | **Oracle Install Base** (serialized item instances registered at the sales channels, coverage derived from the sold warranty terms) + **Oracle Service Contracts (OKS)** (extended-warranty/service contracts: contract terms, entitlement checks at claim time, renewal/expiry schedules) on the TCA party model | FIT-CFG | The 2026-09-16 third-pass audit: the VS-53 workflows' 'CRM warranty module' touchpoint named a generic record-keeper while the suite ships the warranty chain natively — the PA-53.x ST rows name Install Base + Service Contracts; CDP/engagement surfaces stay with the in-house stack (D9); claims link to Teleservice SRs (D14) and Field Service dispatch (D13) |
| D17 | In-house repair & refurbishment orders: intake & diagnosis, estimate with customer approval, parts/labor consumption from service inventory, release & billing (W440 Power Tool Service & Repair ~20,000–30,000 repairs/yr, W544 service work orders, VS-53 out-of-warranty paid-repair path, VS-155 refurbishment-before-resale) | **Oracle Depot Repair (CSD)** — repair orders on Install Base instances: RO intake, diagnosis & estimate/approval workflow, material/labor issue to the RO, RO billing to POS/AR | FIT-CFG | The 2026-09-16 third-pass audit: the W440 'Service Desk module' touchpoint named no repair vehicle while the suite ships Depot Repair natively — service-inventory segregation rides subinventory restrictions; vendor (RTV) repairs stay on the purchasing/RTV path (W88/W33) |

### E. HR & payroll (VS-19, VS-102, VS-121, VS-123, VS-183)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| E1 | Core HR: org/positions/employees/EITs, absence types | Oracle HRMS (PER) | FIT-STD | W15/W43/W292; license/EIT data for VS-166 registers. Core HR **stays in EBS** — the build decision covers payroll, not the people data of record |
| E2 | Recruitment, self-service, learning, performance & succession (W51 training, W72 performance cycle, W178 succession & internal mobility, VS-121) | iRecruitment + Self-Service HR + **Performance Management (appraisals/objectives)** + **Succession Planning (talent pools, readiness states, career paths — W178)** + OLA | FIT-STD | In-suite per the doctrine; a deeper build is the doctrine-compliant path if adoption ever lags. The 2026-09-16 fourth-pass audit names the appraisal vehicle the W72 ST rows left generic — goals as objectives, annual assessments as appraisals with routed approval and ERES signature evidence on the Core HR person record. The 2026-09-16 fifth-pass audit names the succession vehicle the W178 ST rows left generic — HiPo identification as talent-pool tagging, 'Ready Now / Ready in 1–2 Years' mapping as readiness states, IDP/career paths on the succession plan record, internal-posting alerts via iRecruitment |
| E3 | Store workforce scheduling & time-capture platform | Not in EBS — shift scheduling/optimization has no native EBS vehicle (Oracle Time & Labor covers timecards, not retail shift planning); capture retires in-suite through OTL/BEE per E4 | BUILD | The register's BoB WFM row flips to build; owns VS-07 staffing/attendance execution — the build owns the genuinely-absent layer (scheduling/optimization), not timecard mechanics |
| E4 | Time & attendance → payroll/EBS import | In-house WFM feed → **Oracle Time & Labor's BEE batch engine** staging | INT | Capture stays in the build; validated feeds drive scheduling compliance and pay inputs — BEE is the native retirement surface the feed lands in |
| E5 | In-house payroll engine — PH statutory gross-to-net (W10) | **In-house build (Payroll PH)** | BUILD | Per decision: *payroll we build.* SSS/PhilHealth/Pag-IBIG tables, PD 851 13th month, night differential/OT elements, BIR withholding tables — built in-house, not localized on Oracle Payroll (which stays unadopted; see architecture §2) |
| E6 | Payroll statutory outputs & agency files (W251) | In-house build outputs | BUILD | Contribution/loan file formats (R3/RF1/PF-class) and posting reconciliation |
| E7 | BIR compensation reporting: 2316, 1601-C, 1604-C, alphalist (W90, W5533) | In-house build outputs from payroll balances | BUILD | Per current BIR publish formats; eFPS submission rides the G3 channel |
| E8 | Payroll costing → GL posting | Interface posting into GL/SLA | INT | EBS remains the ledger of record: the build posts period costing journals; balances tie out per period |
| E9 | Benefits enrollment, eligibility & life events (VS-102.2) | Advanced Benefits (OAB): plan/enrollment/eligibility design, life-event processing | FIT-CFG | The 2026-09-15 exhaustion audit names the vehicle the 'Benefits administration platform' touchpoint assumed; Oracle Payroll stays unadopted — OAB communicates deduction envelopes to Payroll PH through the E4 feed |
| E10 | Compensation planning & merit cycles: salary-budget distribution, merit/increase planning, promotion & off-cycle adjustments, pay-range administration (VS-102.1 — W3307 salary structures, W3327 merit/budget planning, W3311 pay-range administration) | **Oracle Compensation Workbench** — salary budgets with per-manager distribution, planned increases/promotions against the pay structures, off-cycle adjustments, workforce-model integration with Core HR | FIT-STD | The 2026-09-16 third-pass audit: the VS-102.1 workflows' 'Compensation planning module' touchpoint named a generic vehicle while the suite ships CWB natively; approved changes feed Payroll PH through the E4-class feed — market benchmarking (W3308) stays with the survey tools |

### F. Projects, assets & property (VS-20, VS-35, VS-40, VS-42, VS-55, VS-97, VS-109)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| F1 | Capex request → PO → CIP → asset turnover (W21, W276) | Projects (costing) + PO + FA mass additions | FIT-STD | VS-40 chain is fully native |
| F2 | Construction/new-store cost capture (W223–W227) | Projects cost capture against store WBS | FIT-STD | VS-20/109; PMO scheduling stays external |
| F3 | Lease administration, rent/CAM/indexation, real-property tax (W117/W118/W119) | Property Manager leases, payment schedules, indexation | FIT-STD | Critical-date workflows; PFRS-16 accounting via A12 |
| F4 | Planogram & space optimization (W86, VS-55) | Not in EBS → build; masters in EBS (W314) | BUILD | In-house space-planning build; template/compliance data governed as EBS-adjacent masters |
| F5 | Facility, equipment, vehicle & asset maintenance: work orders, PM schedules, asset registers (W47 store work orders, W240/W241/W700/W808/W1403 facility & equipment PM, W1172 tool-rental fleet, W4785/W4786 EVSE O&M, W3459/W3460 renewable O&M, W3620/W3625/W3634 calibration device estate, W1348 delivery-fleet vehicle PM, W1349 tire lifecycle, W653 accident-repair work orders) | **Oracle eAM (Enterprise Asset Management)** — eAM asset register (FA-linked), work-request intake, PM scheduling with generated work orders, EAM work-order costing to GL/AP | FIT-STD | The 2026-09-16 second-pass audit **corrects the coverage-map's 'no native EAM in this footprint' claim**: eAM ships in-suite, so per the doctrine (the same logic as the WMS adoption, §4-1) maintenance work orders move in-suite. Work requests, PM calendars, device/calibration registers and work-order costing are native; any CMMS breadth beyond eAM goes through a CDR, never a buy. The 2026-09-16 fourth-pass audit extends the same vehicle to the delivery-fleet vehicle estate — the coverage-map's 'no EBS fleet product in footprint' claim named the absent fleet *optimization* layer while the maintenance *work-order* layer the VS-06 workflows describe (odometer-meter PM triggers, work-order parts issue, per-asset maintenance history and costing) is eAM's native function; telematics/fuel stay feeds (W198/W199) and route/dispatch optimization stays build-side per C14 |
| F6 | Budget loading, funds checking & budget-vs-actual control (W26 annual budget cycle, W1646–W1651 planning cycle, W21/W1811–W1818 capex chain, W700 capital planning, W1814 commitment tracking) | **GL budgets + budgetary control (funds checking)** — budget entry/consolidation, Board lock-down, absolute/advisory funds checking at requisition/PO/invoice, budget-vs-actual inquiry | FIT-CFG | The 2026-09-16 second-pass audit: budget load, lock-down and commitment-vs-incurred tracking (W1814's own ST wording) are native GL function — capex requisitions and POs funds-check against the Board-approved budget before commitment; variance reporting rides W26/W35 |

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
| G9 | Statutory & compliance date alerting on the captured registers (LGU/DTI permits W54/W427/W437/W446, BIR CAS W54A, price-freeze windows W468, calibration due dates W3634, COI renewals) | **Oracle Alert (ALR)** — periodic/event-driven alert definitions over application data, routing to workflow/e-mail escalation | FIT-CFG | The 2026-09-16 second-pass audit: the native alert engine monitors the G8 capture layer — licence/expiry/inspection dates raise AME-routed alerts without custom code; filing acts stay human-confirmed (the G3 agentic hard boundary) |

### H. Technology & platform (VS-27, VS-28, VS-30, VS-113, VS-135)

| # | Capability | Standard EBS vehicle | Class | Disposition notes |
|---|---|---|---|---|
| H1 | Rule-driven approvals across modules | Approvals Management (AME) rule sets | FIT-STD | Encodes the DMN PHP authorization ladders |
| H2 | Document workflow & business events | Oracle Workflow + WF_EVENT | FIT-STD | Integration eventing per [integrations.md](integrations.md) |
| H3 | E-signature evidence on controlled approvals | ERES | FIT-STD | Control evidence for the 808 register |
| H4 | RBAC, MOAC security profiles, SSO federation | FND RBAC/UMX + OID/OAM → corporate IdP | FIT-CFG | W152 lifecycle provisioning; W338 SoD queries |
| H5 | Operational dashboards (payables/receivables/inventory/procurement) | Enterprise Command Centers | FIT-STD | Tier-3 analytics without leaving the suite |
| H6 | Enterprise BI & data platform (VS-28) | In-house DP per operating model §5, fed by **Oracle GoldenGate CDC** over the EBS database (the Oracle-stack native replication vehicle; license cost is a FinOps decision like C5) | BUILD | EBS feeds DP; FSG/BIP/ECC own in-suite reporting |
| H7 | Integration platform & API management (W257) | In-house IAP per register; EBS natives (ISG, open interfaces, AQ, XML Gateway) behind it | BUILD | Architecture §5 rules |
| H8 | Archiving, masking, environment lifecycle (W384, W396) | EBS archiving strategy + **Rapid Clone** instance cloning on the on-premises estate + **Oracle iSetup** setup-data templating & post-refresh verification across the four non-prod environments + clone masking profiles | FIT-CFG | RA 10173-aligned masking. The 2026-09-16 sixth-pass audit trues the environment-lifecycle vehicle names to the suite's native toolchain — W384's 'Cloud Management Console (AWS/Azure)' cloning touchpoint and, in the same canon class, W396's 'Cloud Storage Tiers (AWS/Azure)' archive-tier touchpoint + S3-Glacier tiering step retired against the on-premises canon (README §1; the assumptions register's A6.2 correction, thirty-fifth wave): cloning runs Rapid Clone (adpreclone/adcfgclone) with storage-snapshot consistency, archiving tiers to on-premises storage on the BuildRight estate, and iSetup extracts/verifies the ledger/org/AME/QP/eBTax/profile configuration after each refresh |
| H9 | Agentic automation runtime (VS-30/128) | In-house AAP per register §12 | BUILD | Tools reach EBS only through IAP contracts |
| H10 | Store/back-office UX adjustments | OAF personalizations + flexfields | PER | Metadata only; page-personalization export is the evidence |
| H11 | Controls & audit governance: internal-audit plan & risk register, control assessments, findings/CAP tracking, QAIP metrics, external-audit PBC evidence, and the hosting surface for the 808-control CTL register (VS-21 — W120/W121/W123/W159/W332/W333/W334/W336/W338/W351; [internal-controls-matrix](../01-model-company/internal-controls-matrix.md)) | **Oracle Internal Controls Manager (ICM)** — the in-suite GRC module: risk/control library mapped to the CTL register, assessment plans & results, deficiency/CAP routing through Oracle Workflow/AME, certification evidence for the Audit Committee | FIT-CFG | The 2026-09-16 sixth-pass audit: the VS-21 workflows' generic 'Audit Management portal / GRC Tool' touchpoints named a vehicle the suite ships natively — per the doctrine we use it. W332's continuous-monitoring analytics (ACL/IDEA-class scripts over ERP extracts) and W338's SoD role-matrix queries (H4) stay the detection/evidence feeds; their escalated findings, mitigating controls and remediation tracking land in ICM; analytics beyond the suite stay with DP/BI (H6) — never a buy |

---

## 3. Register Counts (Pinned)

| Class | Rows | Share |
|---|---|---|
| FIT-STD | 37 | 38.1% |
| FIT-CFG | 37 | 38.1% |
| **Standard total (STD + CFG)** | **74** | **76.3%** |
| PER | 2 | 2.1% |
| EXT | 1 | 1.0% |
| LOC | 1 | 1.0% |
| INT | 5 | 5.2% |
| EDGE | 0 *(retired)* | — |
| BUILD | 14 *(of which 5 already-built platforms: D6 POS, D7 ecommerce, D8 gift cards, D9 loyalty, D11 marketplace)* | 14.4% |
| OPEN | 0 *(resolved 2026-09-14)* | — |
| **Total register rows** | **97** | 100% |

> Reading: the two-tier doctrine (*in EBS → use it; otherwise → build*) leaves nothing to
> buy. More than three-quarters of the model company runs on EBS untouched or configured; the
> single remaining extension is the PFRS 16 ROU-schedule build with clean edges (its PFRS 15
> sibling retired 2026-09-16 when Revenue Management and Invoicing was found in-suite); the
> single EBS-held localization is the BIR indirect-tax pack; the 14 BUILD rows split into
> 5 platforms that
> already exist (integrate, don't rebuild) and 9 planned builds — of which 4 rows predate
> this doctrine (OMO D10, DP H6, IAP H7, AAP H9; the register's other pre-doctrine product,
> TPS, carries no fit-gap row of its own — it is the candidate remit for the dispatch
> experience layer) and 5 rows are new scope the doctrine creates (the payroll engine and
> its two statutory-output rows E5–E7, the store workforce platform E3, and space-planning
> F4). The 2026-09-15 EBS-exhaustion audit re-pointed the dispatch core in-suite (D13 →
> Oracle Field Service; the build narrows to the consumer experience layer) and added four
> native vehicles the original register had left unnamed (A13 Lease & Finance Management,
> B11 Internet Expenses, D14 Teleservice, E9 Advanced Benefits). The 2026-09-16 third-pass
> audit added six more (A14, B13, C17, D16, D17, E10) without moving any BUILD row — the
> planned-build split above is unchanged. The 2026-09-16 sixth-pass audit added H11 (Oracle
Internal Controls Manager) — the planned-build split above stays unchanged.

---

## 4. Resolution Record — formerly-open decisions (2026-09-14) & the EBS-exhaustion audit (2026-09-15)

The two-tier sourcing decision (*in EBS → use it; otherwise → build*) resolved the open
schedule and superseded the sourcing register's Buy rows. The register amendment is
recorded here and executed in the same wave: the sourcing-model rewrite shipped as
capability-sourcing-and-engineering-model.md **v3.0** (§2 two-tier landscape with the
no-buy guardrail, §4 re-issued register, §3 use-EBS/build gate, §5 'Configure-and-integrate'
archetype, §8 Vendor & Platform Lifecycle Management) and the operating model aligned as
**v3.11** (archetype rename, product/vendor-management remit, §8/§9 cadences and Phase-2
re-scope); this register remains the fit/disposition source of truth.

| # | Decision | Resolution | Supersedes |
|---|---|---|---|
| 1 | Warehouse execution | **Resolved: Oracle WMS/MSCA adopted** — it ships in-suite, so per the doctrine we use it. The register's "re-evaluate when the ERP vendor ships native WMS at parity" trigger is answered by adoption, not assessment | Register row "Buy — BoB WMS" |
| 2 | Planning (forecasting/S&OP) | **Resolved: Oracle ASCP + Demantra** (EBS-family Value Chain Planning) are the planning stack; license cost is a FinOps decision, not a sourcing decision | Former OPEN row C5 |
| 3 | Vendor rebates/claims (VS-39) | **Resolved: Oracle Trade Management** (EBS-family) is the vehicle; license cost FinOps | B10's "evaluation" flag |
| 4 | TPRM tooling depth (VS-161) | Unchanged: EIT/AME registers in EBS. A specialist product would violate the doctrine; a build is admitted only through a CDR if the registers prove inadequate | B7 |
| 5 | ATS/LMS depth (VS-121/123) | Unchanged: in-suite iRecruitment/OLA per the doctrine; deeper function, if ever needed, is built — never bought | E2 |
| 6 | **POS estate** | **Recorded as an already-built in-house platform** — the program is integration (flows W533–W541), not sourcing | Register's Core-row POS treatment |
| 7 | **Payroll** | **Build decision: in-house Payroll PH** replaces the Oracle-Payroll-plus-localization plan; Oracle Payroll not adopted; Core HR (PER) and the GL stay in EBS; posting is E8 | Register Core-row "HR & payroll (PH statutory)" |
| 8 | Store workforce scheduling & dispatch | Workforce (E3) unchanged: build, scoped to the genuinely-absent layer (shift scheduling/optimization — OTL covers timecards, not planning). **Dispatch corrected 2026-09-15: Oracle Field Service is the in-suite dispatch core (D13 FIT-CFG)** — the original 'Not in EBS' claim was wrong; the build narrows to the consumer appointment/route-optimization/contractor-portal experience layer, remit at the SIB/OM | Register's BoB WFM/FSM rows |
| 9 | Lessor equipment leasing (VS-96) | **Resolved 2026-09-15: Lease & Finance Management** — booking, billing schedules → AR, asset/end-of-term; the in-suite vehicle the workflows' unnamed 'lease management system' touchpoint assumed | New row A13 |
| 10 | Employee T&E expenses & corporate cards (W74) | **Resolved 2026-09-15: Internet Expenses (iExpenses)** — expense reports, policy limits, AME approvals, AP card-statement loads | New row B11 |
| 11 | Benefits enrollment & life events (VS-102.2) | **Resolved 2026-09-15: Advanced Benefits (OAB)** — deduction envelopes to the Payroll PH build via the E4 feed | New row E9 |
| 12 | Customer service requests & complaints (W41) | **Resolved 2026-09-15: Teleservice/Service Requests + Escalation Management** on TCA; channel capture stays with the in-house CX surfaces | New row D14 |
| 13 | Facility, equipment & asset maintenance (W47/W240/W241/W808/W1403, tool-rental fleet, EVSE & renewable O&M, calibration devices) | **Adopted 2026-09-16: Oracle eAM** — the coverage-map's 'no native EAM in this footprint' claim was wrong; eAM ships in-suite, so per the doctrine (the §4-1 WMS logic) work orders and PM move in-suite | New row F5 |
| 14 | Vendor contract lifecycle & compliance (W669) | **Adopted 2026-09-16: Procurement Contracts** — clause library, deliverables, expiry/amendment alerts; the DFF-based disposition retired | New row B12 |
| 15 | PFRS 15 multi-element revenue schedules (A11) | **Adopted 2026-09-16: Revenue Management and Invoicing** — the 'no native multi-element schedules' claim was wrong; the planned EXT is retired through its de-customization trigger before any build lands (A11 → FIT-CFG; register EXT 2 → 1) | A11 re-dispositioned |
| 16 | In-store fabrication configuration & quoting (W1009 fabrication family) | **Adopted 2026-09-16: Oracle Configurator (CZ), in-store counter scope** — the architecture's 'CZ for B2C' non-adoption stands (storefront stays in-house, D7) | New row C16 |
| 17 | Multi-org order promising (W56/W1114/W3097) | **Adopted 2026-09-16: Global Order Promising** — the native ATP/allocation engine behind the 'ATP + scheduling' shorthand | New row D15 |
| 18 | Costing & margin analytics (W85/W633/W4136) | **Adopted 2026-09-16: In-Memory Cost Management** — the 12.2-native in-memory analytics surface | New row C15 |
| 19 | Budget funds checking & commitment control (W26/W1814/W1811–W1818) | **Adopted 2026-09-16: GL budgets + budgetary control** — budget load/lock-down and funds checking are native GL function | New row F6 |
| 20 | Statutory date alerting (W54/W427/W437/W446/W3634) | **Adopted 2026-09-16: Oracle Alert (ALR)** — native periodic/event alerting over the EIT registers; filing acts stay human-confirmed | New row G9 |
| 21 | Trade PDC instruments & collections acceleration (W1380/W423/W425/W1381; W892/W1117/W1022/W99/W108) | **Adopted 2026-09-16: AR Bills Receivable** carries the customer-PDC instrument register (A3 note) and **AR Lockbox + Balance Forward Billing + iReceivables** the trade collections/statement spine (A14) — the 'PDC register' and 'document generation engine over AR' touchpoints named the vehicles' function, not the products | A3 note extension; new row A14 |
| 22 | Warranty & extended-warranty lifecycle (VS-53, W33, W544, VS-155) | **Adopted 2026-09-16: Install Base + Service Contracts (OKS)** — serialized item instances with coverage/entitlement and the extended-warranty contracts; the 'CRM warranty module' record-keeper claim retired | New row D16 |
| 23 | In-house repair & refurbishment orders (W440, W544, VS-155 refurbish-before-resale) | **Adopted 2026-09-16: Depot Repair (CSD)** — repair orders on Install Base instances with estimate/approval and parts/labor consumption | New row D17 |
| 24 | Contingent & outsourced workforce procurement (VS-98) | **Adopted 2026-09-16: Purchasing Contingent Labor** — rate-terms POs, timecard-to-invoice, HR contingent-worker registration | New row B13 |
| 25 | Kit/BOM revision & private-label spec change control (W302/W46, VS-92, VS-41) | **Adopted 2026-09-16: Engineering ECO/ECN** — routed change orders with effectivity over BOM/kit revisions | New row C17 |
| 26 | Compensation planning & merit cycles (W3307/W3327/W3311) | **Adopted 2026-09-16: Compensation Workbench** — salary budgets, merit distributions, pay-range administration | New row E10 |
| 27 | Realization trues (no new rows): item governance → **Product Hub** (C1), site-attribute register → **Site Hub** (C3), rental family → **Lease & Finance Management** rental contracts (A13 extension), DP feed → **GoldenGate CDC** (H6 note) | **Trued 2026-09-16 (third pass)** — the doctrine's FinOps posture applies to the two license-bearing products named (GoldenGate; Product/Site Hub and the L&FM extension ride the suite's existing footprint) | C1/C3/A13/H6 notes |
| 28 | Realization trues (no new rows): outgoing-PDC register → **AP Bills Payable** (A3 — W424's issued-but-unreleased instrument register, maturity report, clearing), delivery-fleet vehicle estate → **eAM** (F5 — W1348 PM work orders/W1349 tire lifecycle/W653 accident repair; the 'no EBS fleet product' claim named the absent optimization layer, not the maintenance layer), performance cycle → **Performance Management appraisals/objectives** (E2 — W72's goals/assessments/rating chain) | **Trued 2026-09-16 (fourth pass)** — all three ride products already in the footprint (Bills Payable within the AP row; eAM per §4-13; Performance Management within Core HR) | A3/E2/F5 notes |
| 29 | DC warehouse-optimization surfaces (slotting W784/W1402, crossdocking W221/W1226/W1279/W1307 + W3 variant, labor productivity W796, yard/dock W222/W585/W1353, cartonization W3099) and the succession chain (W178) | **Trued 2026-09-16 (fifth pass)** — all ride products already in the footprint: the adopted in-suite WMS/MSCA's advanced-function family (WMS Slotting, planned crossdocking, WMS Labor Management, WMS Yard Management, Cartonization) and Succession Planning within Core HR (E2) | C6/E2 notes |
| 30 | Audit-management/GRC surface (VS-21 — the W120/W121/W123/W159/W333/W334/W336/W351 'Audit Management portal / GRC Tool' touchpoints) and the environment-lifecycle toolchain (W384) | **Adopted/Trued 2026-09-16 (sixth pass): Oracle Internal Controls Manager** is the in-suite audit-management surface — risk/control library (the CTL-01–CTL-808 register), assessment plans & results, findings/CAP routing, certification evidence (new row H11); H8's environment lifecycle trued to **Rapid Clone + Oracle iSetup** (setup templating/verification; the AWS/Azure-console cloning form retired against the on-premises canon) | New row H11; H8 note |

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
| R1 | Financial Management | FIT-STD/FIT-CFG (A1–A11, A13–A14) |
| R2 | Inventory Management | FIT-STD (C2/C4/C7–C10, C15) |
| R3 | Procurement & Purchasing | FIT-STD (B1/B2/B4/B5/B8, B13) + FIT-CFG (B10–B12) |
| R4 | Warehouse Management | FIT-STD in-suite (C6: Oracle WMS/MSCA) |
| R5 | POS & Retail | Existing in-house POS — integrate (D6) + EBS masters (D2, G6) |
| R6 | Ecommerce Integration | Existing in-house platform — integrate (D7) + EBS fulfillment (D1) |
| R7 | Supply Chain Planning | FIT-CFG Oracle VCP stack (C5) + FIT-STD (C4, C14) |
| R8 | HR & Payroll | Core HR FIT-STD (E1/E2/E9/E10); payroll & workforce builds (E3, E5–E7) + interfaces (E4, E8) |
| R9 | CRM & Loyalty | Existing in-house loyalty stack (D9) + TCA master (D5) + Service Requests (D14) |
| R10 | Analytics & Reporting | FIT-STD in-suite + BUILD DP (H5/H6) |
| R11 | Intercompany & Transfer Pricing | FIT-STD (A7) |
| R12 | Document Management | Process-owned + ERES/attachments |
| R13 | Master Data Management | FIT-STD/FIT-CFG (C1, D5, B6) |
| R14 | Non-Functional | Platform provisions (architecture §7) |
| R15 | Installation & Services | Field Service dispatch core FIT-CFG (D13) + FIT-STD-light (D1, F2) + eAM equipment/work-order maintenance (F5) + fabrication configuration (C16) + GOP promising (D15) + the warranty/repair service chain (D16/D17) + ECO/ECN revision control (C17) |
| R16 | Wholesale & Reseller | FIT-STD (D1) |
| R17 | Governance, Legal & Strategy | Process-owned + PER capture (G8) + in-suite controls/audit governance (H11) |
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
| Capability rows on standard EBS (STD+CFG) | ≥ 65% steady state (current 76.3%) | This register, re-run per wave |
| Best-of-breed capability products | **0 — absolute under the two-tier doctrine** | Sourcing register (amendment per §4) |
| Extensions (EXT) in production | ≤ 10; each with a CDR + de-customization trigger (current 1 — the PFRS 16 schedule; the PFRS 15 sibling retired 2026-09-16 to RM&I) | CEMLI register (customization-governance §7) |
| Modifications (M-class) | **0** — absolute | CEMLI register gate; patch rehearsal (PATCH env) |
| Personalizations | ≤ 150; metadata-only | Personalization export inventory |
| Localization pack outputs with statute citation | 100% | Pack release checklist |
| RUP currency | Within one RUP of current 12.2 RU; CPU applied ≤ 30 days | PATCH-env rehearsal record (W1409 change control) |
| OPEN decisions lingering | 0 past their SIB date — currently 0 rows | §4 resolution record review at each QBR |

---

*Document Version: 1.7 | Date: 2026-09-16 | **Sixth-pass EBS-exhaustion audit:** H11 **Oracle Internal Controls Manager** adopted as the VS-21 audit-management/GRC surface (the workflows' 'Audit Management portal / GRC Tool' touchpoints named the suite's own GRC module; the row's workflow list completed with W123 — PA-21.2's fraud-investigation case-tracking touchpoint the first sweep left standing — and W159) — register 96 → 97 rows (FIT-CFG 36 → 37; standard 73 → 74 = 76.3%); H8's environment-lifecycle vehicle names trued to **Rapid Clone + Oracle iSetup** (W384's AWS/Azure-console form retired against the on-premises canon, and the same canon class swept to its end: W55's 'secondary cloud region' DR failover, W368's environment-lifecycle console row, W382's backup storage and W396's archive tiers all trued to the BuildRight estate); §4 resolution 30 added; §5 R17 row and §7 KPI figure re-derived. Prior v1.6 | Date: 2026-09-16 | **Fifth-pass EBS-exhaustion audit:** no new rows and no count movement — the DC workflows' still-generic warehouse-optimization vehicle names trued onto the adopted WMS product's own advanced-function family (C6: WMS Slotting W784/W1402; planned crossdocking W221/W1226/W1279/W1307 + W3 variant; WMS Labor Management W796; WMS Yard Management W222/W585/W1353; Cartonization W3099) and the W178 talent chain named to Oracle Succession Planning (E2); the PA-04.1/PA-04.2/PA-04.3/PA-93.2 and PA-19.1/PA-19.3/PA-19.4 ST rows re-pointed; §4 resolution 29 added; the coverage-map's Warehouse-Management/HR & Payroll rows and the architecture's WMS/HRMS rows trued in cascade. Register unchanged at 96 rows (73 standard = 76.0%; EXT/LOC/INT/PER/BUILD unchanged). Prior v1.5 | Date: 2026-09-16 | **Fourth-pass EBS-exhaustion audit:** three realization-note trues, no new rows and no count movement — A3 names AP Bills Payable as the outgoing-PDC instrument register (W424), F5 extends the adopted eAM to the delivery-fleet vehicle estate (W1348/W1349/W653 — the coverage-map's 'no EBS fleet product' claim retired as a category error between the optimization and maintenance layers), E2 names Performance Management appraisals/objectives as the W72 review-cycle vehicle; §4 resolution 28 added; the coverage-map's Fleet Management/Financials/HR & Payroll/Facility Maintenance rows, the architecture's AP/HRMS/eAM rows and data-migration row 23 trued in cascade. Register unchanged at 96 rows (73 standard = 76.0%; EXT/LOC/INT/PER/BUILD unchanged). Prior v1.4 | Date: 2026-09-16 | **Third-pass EBS-exhaustion audit:** by direction, every Oracle EBS capability that can be used is used — the register swept the 5,427 workflows' still-generic vehicle names against the suite's receivables-instrument, service-chain and people modules: six native vehicles adopted where capabilities were invoked without naming (A14 AR Lockbox + Balance Forward Billing + iReceivables for the W892/W1117/W1022/W99/W108 trade collections/statement spine; B13 Purchasing Contingent Labor for VS-98; C17 Engineering ECO/ECN for kit/BOM revision governance W302/W46/VS-92/VS-41; D16 Install Base + Service Contracts for the VS-53/W33/W544/VS-155 warranty chain — retiring the 'CRM warranty module' record-keeper claim; D17 Depot Repair for the W440/W544 repair-order lifecycle; E10 Compensation Workbench for the W3307/W3327/W3311 merit-cycle surface), and five realization notes trued (A3 → AR Bills Receivable PDC instruments; A13 extended to the tool/self-haul/storage/equipment rental family; C1 → Product Hub; C3 → Site Hub; H6 → GoldenGate CDC), with §4 gaining resolutions 21–27 and the PA-11.1/PA-12.1/PA-16.3/PA-53.x/PA-98.2/PA-102.1/PA-186.2 touchpoints re-pointed. Register 90 → 96 rows (67+6 standard → 73 = 76.0%; BUILD unchanged at 14 of which 5 already-built). Prior v1.3 | Date: 2026-09-16 | **Second-pass EBS-exhaustion audit:** by direction, every Oracle EBS capability that can be used is used — the register re-audited against the suite's full 12.2 catalog a second time: A11's 'No native multi-element schedules' claim corrected (Oracle Revenue Management and Invoicing is the in-suite vehicle; the planned PFRS 15 EXT retired through its de-customization trigger before any build lands), the coverage-map's 'no native EAM in this footprint' claim corrected (Oracle eAM adopted — F5), and five native vehicles added where the register had left capabilities unnamed or under-served (B12 Procurement Contracts, C15 In-Memory Cost Management, C16 Oracle Configurator for in-store fabrication, D15 Global Order Promising, F6 GL budgets + budgetary control, G9 Oracle Alert), with C5 extended to name Inventory Optimization/Rapid Planning for VS-136 and §4 gaining resolutions 13–20. Register 83 → 90 rows (54+5 standard → 67 = 74.4%; EXT 2 → 1; BUILD unchanged at 14). Prior v1.2 | Date: 2026-09-15 | **EBS-exhaustion audit:** by direction, every Oracle EBS capability that can be used is used — the register re-audited against the suite's native catalog: D13's 'Not in EBS' claim corrected (Oracle Field Service is the in-suite dispatch core; the build narrows to the consumer experience layer), four native vehicles added where the register had left capabilities unnamed (A13 Lease & Finance Management for VS-96 lessor leasing; B11 Internet Expenses for W74 T&E; D14 Teleservice/Service Requests for W41 complaints; E9 Advanced Benefits for VS-102.2 enrollment), B10's stale SIB note re-pointed to its §4 resolution-3 OTM adoption, E3/E4's notes trued to name Oracle Time & Labor/BEE as the capture-retirement surface, §4 gains resolutions 9–12. Register 79 → 83 rows (54 standard → 59 = 71.1%; BUILD 15 → 14 of which 5 already-built). Prior v1.1 (2026-09-14): Two-tier sourcing doctrine enacted (*in EBS → use it; otherwise → build*): register re-dispositioned 76 → 79 rows (54 standard / 2 PER / 2 EXT / 1 LOC / 5 INT / 15 BUILD of which 5 already-built / 0 EDGE / 0 OPEN); Oracle WMS/MSCA adopted in-suite (C6), Oracle ASCP + Demantra adopted (C5), OTM resolved (B10), POS/ecommerce/loyalty/gift-card recorded as already-built platforms (D6–D11), payroll re-scoped to an in-house build with Oracle Payroll unadopted (E3–E8), BoB WMS/TMS/WFM/FSM rows superseded (§4 resolution record, incl. the sourcing-register amendment schedule). Prior v1.0 (2026-09-14): initial issue — fit classes, 76-row capability disposition register (52 standard / 2 PER / 2 EXT / 4 LOC / 4 INT / 7 EDGE / 4 BUILD / 1 OPEN), SIB open-decision schedule, R1–R32 orientation view, PH localization pack definition, standard-first KPIs. Register counts pinned above; canon anchors: 728 Req / 5,427 WF / 808 CTL / sourcing register §4 / ATC & statutory forms per repo canon.*
