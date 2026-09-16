# Requirement-to-Workflow Cross-Reference Matrix

> Maps each ERP requirement from [erp-requirements.md](erp-requirements.md) to the operational
> workflows from the [workflows/](workflows/value-stream-index.md) directory that exercise it.
> Ensures complete traceability from requirements to workflows: every requirement is validated
> by at least one workflow. Workflow-side coverage is currently limited to the core foundational
> workflows; mappings for the Expansion / Statutory / Gap-analysis value streams (VS-53–VS-192)
> are added incrementally (see the Coverage Validation section and the version note).

---

## How to Read This Matrix

- **Req ID**: Requirement identifier from erp-requirements.md
- **Priority**: Must Have (M), Should Have (S), Nice to Have (N)
- **Primary Workflows**: Workflows where this requirement is directly exercised and system touchpoints are listed
- **Supporting Workflows**: Workflows that indirectly involve this requirement

> **Column convention:** every section except R14 uses the 3rd column for **Priority** (M / S / N).
> R14 (Non-Functional Requirements) uses the 3rd column for the **Target** spec value
> (e.g. 99.9%, < 3 sec, 10 years), since the target is the operative spec for an NFR; NFR
> priorities (Must / Should / Nice) are listed in [`erp-requirements.md`](erp-requirements.md) R14.

---

## R1. Financial Management (FIN)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| FIN-001 | Multi-entity GL | M | W9A (month-end close), W14 (IC transactions) | W10 (payroll GL posting), W30 (treasury) |
| FIN-002 | Automated IC Elimination | M | W9A.13, W14.8, W234 (IC profit elimination) | — |
| FIN-003 | Consolidated Financial Reporting | M | W9A.14, W35.8 | W26 (budget) |
| FIN-004 | AP with 3-Way Match | M | W7 (AP processing), W18.9 (DSD 3-way) | W20.11 (VMI settlement), W23.9 (consignment), W7D (AP vendor statement reconciliation), W100 (vendor statement reconciliation — finance), W244 (vendor invoice dispute & discrepancy resolution), W277 (freight bill audit & payment reconciliation — freight vendor 3-way match), W424 (AP PDC issuance & monitoring) |
| FIN-005 | AR for B2B | M | W8 (AR processing), W5B.4c (POS trade accounts), W229 (B2B credit limit exception), W108 (customer credit collection & escalation), W460 (corporate & trade account onboarding) | W58 (corporate accounts), W94 (customer deposit management), W101 (customer refund & credit processing), W1380 (customer PDC receipt, register & bank deposit), W1381 (customer bounced check resolution, BP 22 & BIR reporting) |
| FIN-006 | Philippine VAT (12%) | M | W5B (POS selling), W9A.16 (VAT return), W11/W19 (ecommerce VAT), W217 (SC/PWD VAT-exemption), W239 (customs duty recon), W293 (tax & regulatory master data governance — VAT rate configuration) | W12 (returns — VAT reversal), W284 (customs bonded warehouse operations & duty deferral — deferred VAT on bonded goods) |
| FIN-007 | Withholding Tax (Expanded) | M | W7.9a (EWT computation), W9A.16a (EWT remittance), W293 (tax & regulatory master data governance — ATC code & EWT rate configuration) | W7C (non-PO EWT on services) |
| FIN-008 | BIR Tax Return Generation | M | W9A.16 (VAT, income tax), W9A.16a (EWT), W9A.16c (LBT), W216 (BIR CAS audit), W217 (SC/PWD reporting), W293 (tax & regulatory master data governance — tax code & BIR form mapping) | W10.11 (statutory contribution files), W90 (monthly tax filing & statutory remittance) |
| FIN-009 | Multi-Bank Integration | S | W30.2 (bank statement import), W30.7 (cash sweeps), W309 (bank & banking partner master governance — bank master records, payment file format config), W317 (bank account lifecycle & signatory management — entity bank account setup), W320 (electronic banking security & payment control — bank payment security) | W7.9 (payment file generation), W89 (bank reconciliation), W274 (third-party customer financing / equipment leasing — partner bank settlement) |
| FIN-010 | Cash Management / Treasury | S | W30 (daily treasury), W5F (store cash reconciliation), W232 (LC lifecycle), W233 (liquidity forecasting), W174 (store-level CIT & armored car management), W309 (bank & banking partner master — entity bank account setup, store deposit account linkage), W318 (short-term investment & surplus cash placement), W319 (debt facility & covenant compliance management), W322 (treasury policy, governance & risk appetite framework), W323 (cash concentration & inter-entity pooling), W326 (treasury month-end close & reconciliation) | W25 (petty cash), W89 (bank reconciliation), W99 (payment settlement reconciliation), W423 (AR PDC maturity & clearing execution — treasury companion to W1380), W424 (AP PDC issuance & monitoring), W425 (bounced check reversal & penalty posting — treasury companion to W1381), W1380 (customer PDC receipt & bank deposit), W1381 (customer bounced check resolution) |
| FIN-011 | Fixed Asset Management | M | W21.7–8 (asset creation & depreciation), W39 (disposal), W240 (DC equipment PM), W241 (HQ asset PM), W184 (fixed asset physical verification audit) | W16 (new store capex), W275 (IFRS 16 / PFRS 16 lease accounting — ROU asset management), W276 (asset under construction & mass capitalization — AUC-to-asset conversion) |
| FIN-012 | Budgeting & Variance Analysis | S | W26 (annual budget), W35.9 (monthly variance), W85 (product costing & margin analysis review) | W21.3 (budget check) |
| FIN-013 | Landed Cost Calculation | M | W2B.12 (import landed cost), W239 (customs duty tax recon), W249 (port demurrage fee allocation) | W66.8 (inter-island freight allocation) |
| FIN-014 | Multi-Currency | M | W2B.12–13 (import FX), W9A.5a (FX revaluation), W232 (LC lifecycle), W307 (currency & exchange rate master governance — rate type config, daily rate import, month-end rate lock), W321 (FX exposure analysis & BSP regulatory reporting) | W30.10 (USD accounts), W80 (FX hedging — hedged rate integration) |
| FIN-015 | Period-End Close Workflow | M | W9 (financial close & reporting — parent workflow), W9A (month-end close), W9B (year-end close), W308 (fiscal calendar & posting period master — period control, month-end rate lock) | — |
| FIN-016 | Capex Workflow | M | W21 (capex request & approval), W226 (store renovation capex) | W16 (new store capex), W276 (asset under construction & mass capitalization — capex-to-AUC-to-asset pipeline) |
| FIN-017 | Petty Cash Management | M | W25 (petty cash lifecycle) | W47 (facility maintenance), W82 (small disposal costs) |
| FIN-018 | Consignment Settlement | S | W23 (consignment operations) | W7 (AP settlement) |
| FIN-019 | Vendor Rebate Management | S | W27 (rebate accrual & settlement) | W7.9b (credit memo) |
| FIN-020 | Duplicate Vendor Invoice Detection | M | W7 (duplicate detection engine, blocks and alerts) | W70 (credit note aging — duplicate overrides) |
| FIN-021 | FX Hedging / Forward Contract Management | S | W80 (forward contract lifecycle, settlement, MTM reporting), W321 (FX exposure analysis & BSP regulatory reporting) | W2B (import POs — exposure source), W9A.5a (month-end FX revaluation), W30 (treasury cash position) |
| FIN-022 | Bad Debt Write-Off & Recovery | M | W81 (bad debt provisioning, write-off with BIR documentation, recovery tracking) | W8.8a (AR collection escalation — feeds into write-off), W9A (month-end provision posting), W24 (credit block on written-off accounts) |
| FIN-023 | Insurance Policy Lifecycle Management | S | W59 (insurance policy lifecycle management — registry, premiums, claims, renewal) | W21 (capex — insurance for new assets), W285 (public liability & customer incident claims management — public liability insurance claims) |
| FIN-024 | Employee Gratuity & Retirement Fund (RA 7641) | M | W175 (employee gratuity & retirement fund management per RA 7641) | W10 (payroll — retirement accrual posting), W43 (separation — retirement pay computation) |
| FIN-025 | Cash-in-Transit (CIT) & Armored Car Management | S | W174 (store-level CIT & armored car scheduling, custody transfer, reconciliation) | W30 (treasury — deposit confirmation), W5F (store EOD — cash handoff to CIT) |
| FIN-026 | Product Costing & Margin Analysis | S | W85 (product costing & margin analysis review — standard vs. actual, landed cost roll-up) | W9A (month-end cost variance posting), W35 (margin reporting) |
| FIN-027 | Customer Refund & Credit Processing | M | W101 (customer refund & credit processing — cash, card, store credit, BIR credit notes) | W12A (in-store returns — refund trigger), W99 (payment settlement reconciliation), W282 (subscription billing for recurring home services — subscription credit/refund processing) |
| FIN-028 | Customer Credit Collection & Escalation | M | W108 (customer credit collection & escalation — call logging, promise-to-pay, aging escalation) | W8 (AR processing — collection feed), W81 (bad debt write-off — escalation outcome) |
| FIN-029 | Intercompany Dividend & Loan Management | S | W137 (intercompany dividend & loan management — declaration, interest, amortization), W325 (corporate guarantee & contingent liability management — IC guarantee tracking), W327 (external shareholder dividend declaration & payment) | W14 (IC settlement — net settlement), W9A (month-end — IC interest posting) |
| FIN-030 | Fixed Asset Physical Verification | S | W184 (fixed asset physical verification — tag scanning, missing flagging, reconciliation) | W39 (asset disposal — verification input), W21 (capex — new asset verification) |
| FIN-033 | BOI/PEZA/LGU Tax Incentive Monitoring & Compliance | M | W472 (BOI/PEZA/LGU tax incentive registration, compliance monitoring, benefit tracking, BIR filing integration, transfer pricing impact, expiration management) | W90 (monthly tax filing — incentive rate applied), W260 (BIR eFPS — incentive-qualified returns), W235 (transfer pricing — incentive entity IC scrutiny), W319 (debt covenant — ETR impact), W254 (location master — incentive status per location) |
| FIN-034 | BIR Electronic Invoicing System (EIS) / e-Invoicing Compliance | M | W473 (BIR Electronic Invoicing System (EIS) API Transmission & Reconciliation — sales invoice / POS transaction transmission, digital signature validation, UUID logging, retry queue management) | W5B (POS selling — transaction trigger), W8 (AR — invoice trigger), W11/W19 (ecommerce — online invoice trigger), W90 (monthly tax filing — tax reconciliation), W260 (eFPS — tax reporting integration), W216 (BIR CAS audit — invoice transmission audit trail) |
| FIN-035 | B2B Customer Withholding Tax (CWT) / Form 2307 Management | M | W475 (Customer Creditable Withholding Tax (CWT) Certificate (BIR 2307) Collection & Reconciliation — cash application entry, document validation, ERP logging & clearing, aging & follow-up) | W8 (AR billing — invoice withholding), W24 (Credit application — limit blocks), W90 (Monthly tax filing — tax reconciliation), W108 (Customer collection — follow-ups), W140 (Corporate income tax — tax credit reconciliation), W260 (eFPS filing — digital submission) |
| FIN-036 | BIR Annual Inventory List Submission (RMC 57-2015) | M | W478 (BIR Annual Inventory List Submission — data extraction, validation, format mapping, electronic transmission, reconciliation) | W9A (Month-end close — inventory close value), W42 (Annual physical inventory — count data feed), W90 (Monthly tax filing — reporting calendar), W216 (BIR CAS compliance audit — reporting audit trail), W252 (Item master — SKU cost/status feed) |
| FIN-037 | Credit Card Chargeback Dispute Management | M | W488 (Credit card chargeback dispute management — notification receipt, transaction investigation, representment evidence, submission, resolution, pattern analysis) | W99 (payment settlement reconciliation — chargeback debit/credit matching), W261 (e-wallet settlement — related digital payment disputes), W37 (loss prevention — fraud pattern escalation), W466 (LPAP — fraud investigation handoff), W71 (CCTV — footage for evidence), W5B (POS — transaction data source) |
| FIN-038 | Related Party Transaction Disclosure (PAS 24) | M | W486 (Related party transaction disclosure — register maintenance, transaction capture, arm's-length verification, quarterly disclosure schedule, annual PAS 24 note, external audit coordination) | W14 (IC transactions — transaction data source), W234 (IC profit elimination — elimination data), W235 (transfer pricing — arm's-length documentation), W435 (IC SLA billing — service fee data), W327 (dividend — related party dividend data), W10 (payroll — management compensation data), W481 (SEC filings — AFS filing dependency), W9B (year-end close — PAS 24 note timing) |
| FIN-039 | Revenue Recognition Review (PFRS 15) | M | W487 (Revenue recognition review — revenue stream inventory, performance obligation assessment, deferred revenue calculation, bundle allocation review, consignment timing verification, journal entry posting, annual comprehensive review) | W28 (gift cards — breakage data), W17 (loyalty — points deferred revenue), W104 (loyalty financial governance — liability validation), W23 (consignment — sell-through timing), W75 (layaway — deposit/delivery revenue), W282 (subscription billing — deferred revenue schedule), W138 (installation — bundle allocation), W165 (project billing — over time vs. point in time), W9A (month-end — PFRS 15 adjustments), W9B (year-end — PFRS 15 note) |
| FIN-040 | Store-Level Operating Budget & Cost Control | S | W489 (Store-level operating budget — template distribution, store manager input, regional consolidation, FP&A consolidation, monthly cost review, cost control action, quarterly forecast update, annual performance assessment) | W26 (enterprise budget — top-down targets), W67 (store performance review — actual vs. budget reporting), W72 (employee performance — budget performance feed), W34 (shift scheduling — labor cost driver), W47 (facility maintenance — maintenance cost driver), W111 (utility management — utility cost driver) |
| FIN-045 | Credit Card Installment Sales Reconciliation | M | W750 (installment reconciliation — daily settlement matching, MDR verification, subsidy reconciliation, GL posting) | W747 (POS installment — transaction source), W309 (bank master — MDR rates), W89 (bank reconciliation), W640 (merchant fee analysis), W149 (bank partnership — rate governance) |
| FIN-046 | Store-Level Emergency Cash Float | S | W751 (emergency cash float — request, approval, CIT coordination, reconciliation, float adjustment) | W489 (store budget — cash budget validation), W174 (CIT — expedited delivery), W541 (cash office — receipt and reconciliation), W89 (bank reconciliation) |
| FIN-047 | Intercompany Management Fee Allocation | M | W752 (IC management fee — cost pool compilation, allocation calculation, IC invoice generation, settlement) | W14 (IC transactions — settlement vehicle), W235 (transfer pricing — arm's-length documentation), W486 (PAS 24 — related party disclosure), W234 (IC elimination), W26 (budget — fee budget tracking) |

## R2. Inventory Management (INV)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| INV-001 | Perpetual Inventory | M | W3.7 (GR posting), W5B.8 (POS deduction), W4.12 (transfer receipt), W219 (quarantine status adjustments), W109 (store-level inventory receiving & putaway), W439 (in-store repackaging operations) | W6 (cycle counts), W220 (SLOB actual write-offs), W91 (damaged & defective goods disposition), W92 (inventory adjustment & shrinkage authorization) |
| INV-002 | Real-Time Inventory Visibility | M | W4 (replenishment), W11.1 (BOPIS ATP), W19.1 (delivery ATP) | W22 (transfer availability check) |
| INV-003 | Weighted Average Cost (WAC) | M | W3.7 (receipt WAC recalc), W9A.6a (WAC verification) | W46.7 (kit costing) |
| INV-004 | ABC Classification | M | W31.8 (classification review), W42 (tiered count strategy) | W1 (assortment review) |
| INV-005 | Multi-Location Stock Transfer | M | W4 (DC→Store), W22 (store-to-store, inter-DC), W204 (regional expedited transfer), W214 (store-to-store expedited), W218 (inter-DC push), W22A (store-level outbound transfer fulfillment), W22B (store-to-DC return — excess/damaged) | W45 (closure redistribution), W4B (store-initiated replenishment request) |
| INV-006 | Cycle Counting | M | W6 (cycle counting), W248 (store variance LP investigation), W301 (reason code & disposition master — adjustment reason code governance) | W42 (annual physical inventory) |
| INV-007 | Physical Inventory (Wall-to-Wall) | M | W42 (annual physical inventory), W248 (store variance LP investigation) | W6 (cycle counts feed C-tier validation) |
| INV-008 | Lot & Serial Tracking | S | W5B.4b (POS batch capture), W29 (recall tracing), W421 (shade reconciliation) | W33 (warranty serial lookup) |
| INV-009 | Consignment Inventory | S | W23 (consignment operations) | — |
| INV-010 | Catch-Weight / Variable Measure | M | W5B.2 (POS catch-weight), W3B.3 (yard catch-weight), W22 (transfer catch-weight), W463 (catch-weight & cut-to-length processing) | W18 (DSD catch-weight) |
| INV-011 | Inventory Aging Analysis | S | W1 (slow-mover review), W9A.16b (NRV review), W220 (SLOB provisioning & liquidation) | W13.9b (clearance disposition), W93 (markdown & clearance pricing for aging inventory), W301 (reason code & disposition master) |
| INV-012 | Safety Stock & Reorder Point | M | W2A.1 (ROP calculation), W31.8 (parameter governance) | W56 (backorder — insufficient ROP) |
| INV-013 | Batch/LOT Tracking for Paint | S | W3.4 (shelf-life capture), W4.5 (FEFO picking), W421 (shade reconciliation) | W6 (near-expiry alerting) |
| INV-014 | In-Transit Inventory | M | W4.8 (DC→Store in-transit), W22.6 (transfer in-transit), W250 (supply chain control tower visibility) | W66 (inter-island in-transit) |
| INV-015 | Inventory Valuation Reports | M | W9A.6 (inventory valuation), W42.17 (physical inventory summary) | W35.10 (store P&L) |
| INV-016 | Product Recall Tracking | S | W29 (product recall execution) | — |
| INV-017 | Consignment Inventory Tracking | M | W23 (consignment operations — non-valuated receipt, ownership transfer at sale) | W42 (vendor-owned inventory during physical count) |
| INV-018 | VMI Inventory Tracking | S | W20 (VMI operations) | W42 (vendor-owned inventory during physical count) |
| INV-019 | Multi-Channel Inventory Allocation Governance | S | W105 (multi-channel inventory allocation & priority governance — reservation rules per channel) | W11 (BOPIS — channel reservation), W19 (home delivery — channel reservation) |
| INV-020 | Proactive Store Inventory Rebalancing | S | W154 (proactive store inventory rebalancing — system-suggested rebalancing) | W22 (transfers — execution vehicle), W4B (store-initiated request — demand signal) |

## R3. Procurement & Purchasing (PUR)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| PUR-001 | Purchase Order Management | M | W2 (procurement PO cycle — parent workflow), W2A (auto-replenishment), W2B (import PO), W2C (blanket PO), W246 (drop-ship back-to-back PO) | W38 (special order PO), W60 (emergency PO) |
| PUR-002 | Automated Replenishment | M | W2A.1–2 (ROP/EOQ auto-generate), W31.6 (forecast release) | W57 (promo stock PO) |
| PUR-003 | Vendor Management | M | W36 (vendor onboarding), W44 (vendor scorecard), W230 (legal contract review), W115 (supplier diversity & MSME development), W155 (vendor strategic collaboration & JBP), W62B (3PL/delivery partner onboarding & offboarding) | W62 (non-PO contracts), W160 (private label factory audit) |
| PUR-004 | Import Purchase Orders | M | W2B (import PO lifecycle), W232 (LC lifecycle), W239 (customs duty recon), W249 (port demurrage management), W250 (import shipment control tower tracking), W464 (in-house customs brokerage) | W32 (seasonal import PO), W284 (customs bonded warehouse operations & duty deferral — bonded import storage) |
| PUR-005 | 3-Way Matching | M | W7.2–3 (3-way match engine) | W18.9 (DSD 3-way) |
| PUR-006 | Blanket/Contract POs | S | W2C (blanket PO lifecycle), W324 (supply chain finance & dynamic discounting program — early payment discount integration) | — |
| PUR-007 | Vendor Portal | N | W2A.7 (vendor portal PO access), W36.9 (portal provisioning), W422 (VMI data sharing) | W20.1 (VMI data sharing) |
| PUR-008 | Vendor Performance Scorecard | S | W44 (vendor performance review), W242 (3PL performance review), W245 (supplier compliance chargebacks), W161 (vendor price protection & market markdown claims) | W18B.5 (DSD no-show tracking), W110 (supplier quality CAPA — quality metrics) |
| PUR-009 | Multi-Entity Procurement | M | W2A (central buying), W14 (IC service fees) | — |
| PUR-010 | Approval Workflow | M | W2A.5–6 (PO approval tiers), W21.4 (capex approval), W24.5 (credit approval) | W7C.3 (non-PO approval) |
| PUR-011 | Goods Receipt Processing | M | W3 (DC receiving), W18 (store DSD receiving), W3C (DC inbound delivery scheduling) | W20.6 (VMI receipt) |
| PUR-012 | Return to Vendor | M | W88 (RTV processing — full lifecycle) | W3.6a–b (DC receiving RTV), W23.10 (consignment return), W33.6 (warranty RTV), W301 (reason code & disposition master) |
| PUR-013 | Direct Store Delivery | M | W18 (DSD receiving), W18B (DSD scheduling) | — |
| PUR-014 | Vendor Managed Inventory | S | W20 (VMI operations), W422 (collaborative planning) | — |
| PUR-016 | Configurable AQL Sampling per SKU Category | S | W3 (AQL inspection standards per category at goods receipt) | W44 (vendor scorecard — quality reject rate), W150 (product quality testing & certification) |
| PUR-017 | Supplier Quality & CAPA | S | W110 (supplier quality & CAPA — quality issue logging, corrective action tracking) | W3 (goods receipt — quality hold), W44 (vendor scorecard — quality metrics) |
| PUR-018 | Indirect / Non-Merchandise Procurement | M | W136 (indirect / non-merchandise procurement — supplies, services, IT, facilities) | W21 (capex — equipment procurement), W7C (non-PO recurring expenses) |
| PUR-019 | Vendor Invoice Dispute & Discrepancy Resolution | M | W244 (vendor invoice dispute & discrepancy resolution — case creation, hold payment, resolution) | W7 (AP — 3-way match variance flagging), W7D (AP vendor statement reconciliation) |
| PUR-020 | Vendor Price Protection & Market Markdown Claims | S | W161 (vendor price protection & market markdown claims — claim filing, credit memo) | W40 (price change — trigger for price protection), W27 (rebate — related vendor credits) |
| PUR-021 | Vendor Strategic Collaboration & JBP | S | W155 (vendor strategic collaboration & joint business planning — JBP documentation, scorecard) | W1 (assortment review — JBP input), W13 (promotions — co-investment tracking) |
| PUR-022 | Private Label Factory Audit & Social Compliance | S | W160 (private label factory audit & social compliance — audit scheduling, scoring, corrective action) | W36 (vendor onboarding — factory qualification), W44 (vendor scorecard — compliance score) |
| PUR-023 | Supplier Diversity & MSME Development Program | S | W115 (supplier diversity & MSME development — classification, spend reporting, development tracking) | W36 (vendor onboarding — MSME classification) |
| PUR-024 | Product Quality Testing & Certification | S | W150 (product quality testing & certification — test request, result recording, certificate tracking) | W3 (goods receipt — test trigger), W110 (supplier quality CAPA — failed test feed), W447 (DTI-BPS mandatory product certification) |
| PUR-025a | Commodity Price Index Tracking & Procurement Triggers | M | W760 (commodity price tracking — index monitoring, threshold alerts, forward buy decision, rate benchmarking, quarterly strategy) | W633 (PPV analysis — price variance), W85 (margin analysis — commodity impact), W312 (planning parameters — safety stock override), W589 (cash flow — forward buy impact), W680 (SC cost analysis — cost optimization) |
| PUR-025b | Supplier Innovation & NPI Collaboration | S | W761 (supplier innovation — opportunity pipeline, business case, vendor collaboration, testing, pilot, rollout decision) | W155 (JBP — vendor meeting integration), W625 (product testing — quality testing), W64 (pilot — pilot execution), W564 (NPI rollout — national launch), W130 (competitive intelligence — gap identification) |

## R4. Warehouse Management (WMS)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| WMS-001 | RF/Barcode Directed Operations | M | W3 (receiving), W4 (pick/pack/ship), W6 (cycle count) | W42 (physical inventory) |
| WMS-002 | Cross-Dock Capability | S | W3 (cross-dock flow for fast-movers), W221 (cross-docking fast-moving bulky items) | — |
| WMS-003 | Wave/Zone Picking | S | W4.3–5 (wave planning & picking) | — |
| WMS-004 | Receiving & Putaway | M | W3 (DC receiving & putaway) | W18 (DSD — no putaway), W270 (pallet & RTP tracking — inbound pallet reconciliation), W297 (warehouse location & bin master — bin capacities and rules) |
| WMS-005 | Shipping & Dispatch | M | W4.6–7 (pack & load), W19.6–8 (ecommerce shipping), W106 (DC outbound dispatch & load planning) | W270 (pallet & RTP tracking — shipping pallet reconciliation) |
| WMS-006 | Yard Management | S | W3B (yard & outdoor inventory), W222 (DC container yard & chassis management), W438 (yard dispatch & loading operations) | W188 (fleet spare parts & preventive maintenance — yard equipment) |
| WMS-007 | Label Printing | M | W63 (shelf label distribution) | W46.6 (kit barcode labels) |
| WMS-008 | WMS Integration with ERP | M | W4 (replenishment), W3 (receiving), W19 (ecommerce fulfillment) | W22 (transfers) |

## R5. POS & Retail (POS)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| POS-001 | 600 POS Terminals | M | W5B (in-store selling), W5 (daily store operations — parent workflow), W16 (new store POS setup) | W45 (store closure decommission) |
| POS-002 | Offline Mode | M | W5G (offline POS recovery & reconciliation), W535 (offline capability scope — local operations, capability matrix, offline-to-online recovery, local data store, LAN sync) | W49 (typhoon — degraded mode), W533 (event streaming — offline event replay) |
| POS-003 | Barcode Scanning | M | W5B.4 (barcode scanning at checkout), W311 (barcode, GTIN & item identification master — barcode assignment, multi-level config, custom barcode ranges) | W3.4 (receiving scan), W6.3 (cycle count scan) |
| POS-004 | Multi-Tender | M | W5 (in-store selling — multi-tender payment), W1425 (multi-tender POS daily reconciliation), W12 (split-tender refund) | — |
| POS-005 | Loyalty Integration | M | W5B.5 (loyalty scan), W17 (loyalty program operations) | — |
| POS-006 | Price Override (w/ Auth) | M | W5B.4a (price override with manager authorization) | W61 (competitor price match), W281 (self-checkout exception & intervention — SCO override authorization) |
| POS-007 | Returns & Exchanges | M | W12A (in-store returns), W12B (online returns), W12C (cross-store returns), W215 (home delivery returns) | W301 (reason code & disposition master) |
| POS-008 | Cash Drawer Management | M | W5A.4 (cash float), W5F.2–5 (Z-report & cash count), W212 (Smart Safe deposit) | W89 (bank reconciliation), W99 (payment settlement reconciliation), W278 (mid-day cash skimming / till sweeps — mid-day drawer management) |
| POS-009 | End-of-Day Reconciliation | M | W5F (store closing & EOD), W212.5 (Smart Safe reconciliation) | W30.4 (deposit auto-matching), W89 (bank reconciliation), W99 (payment settlement reconciliation), W5D (in-store customer delivery scheduling — delivery EOD reconciliation), W5E (store opening delay procedure — delayed start EOD impact), W272 (cashier over/short dispute & deduction resolution), W278 (mid-day cash skimming / till sweeps) |
| POS-010 | Quantity Break Pricing | M | W5B.6 (auto quantity breaks), W40.15–19 (quantity break setup) | — |
| POS-011 | Customer Display | S | W5 (customer-facing display during checkout steps) | — |
| POS-012 | Receipt Printing | M | W5 (BIR-registered receipt at sale), W528 (POS digital receipt / e-receipt delivery) | — |
| POS-013 | Real-Time Inventory Deduction | M | W5B.8 (near-real-time inventory deduction via event streaming), W533 (real-time event streaming — continuous event bus, inventory consumer), W5G.5 (offline event replay reconciliation) | W11 (BOPIS — ATP consumer), W19 (home delivery — ATP consumer) |
| POS-014 | Promotional Pricing Auto-Apply | M | W13.7 (auto-apply at POS), W5B.6 (system calculates promos) | W279 (product substitution rules & governance — substitution-based pricing logic) |
| POS-014a | Senior Citizen & PWD Discount Compliance | M | W170 (senior citizen & PWD discount compliance — PH legal, auto-detect and apply 20% discount, VAT-exemption for SC), W432 (Solo Parent discount compliance) | W217 (SC/PWD VAT-exemption reporting), W5B (POS — discount application) |
| POS-015 | Gift Card / Store Credit | S | W28 (gift card & store credit lifecycle) | W12A.6 (store credit from returns) |
| POS-016 | Catch-Weight / Variable Measure at POS | M | W5B.2 (catch-weight selling) | W3B.3 (catch-weight receiving), W22 (catch-weight transfer) |
| POS-017 | Paint Mixing / Custom SKU at POS | M | W1282 (paint mixing station setup & color formula management), W1485 (station calibration & tint replenishment) | — |
| POS-018 | Age-Restricted Product Prompts | S | W520 (age-restricted product verification & compliance at POS) | — |
| POS-019 | Warranty Claim Registration | S | W33 (warranty claim processing) | — |
| POS-020 | Layaway / Installment Sales | S | W75 (layaway agreement lifecycle — exercises POS-004, POS-015, FIN-005) | W273 (in-store endless aisle & vendor direct-to-customer delivery — special order flow), W274 (third-party customer financing / equipment leasing — installment integration) |
| POS-021 | Multi-DC Order Splitting | S | W19 (multi-DC order splitting logic) | — |
| POS-022 | Employee Discount at POS | S | W205 (employee purchase program), W5B.12 (staff discount logic) | W17 (employee purchases excluded from loyalty points) |
| POS-023 | Store-Level Customer Delivery Scheduling | S | W5D (in-store customer delivery scheduling — date/time slot, fee, dispatch) | W19 (home delivery — delivery partner handoff), W52 (fleet — own delivery) |
| POS-024 | DTI Price Freeze Compliance at POS | M | W468 (DTI price freeze implementation — system-enforced price freeze, override block, immediate POS price push) | W5B (in-store selling — override block enforcement), W11/W19 (ecommerce price freeze), W180 (marketplace price freeze), W468.8d (frozen price compliance report) |
| POS-025 | Self-Checkout (SCO) Station Daily Operations | S | W516 (SCO daily operations — startup, self-scan, weight verification, skip-scan detection, payment, SCO-to-assisted escalation, closing reconciliation) | W5B (in-store selling — SCO as parallel channel), W5F (store closing — SCO Z-report), W206 (mPOS — complementary queue busting), W281 (SCO exception management), W37 (loss prevention — SCO shrinkage analytics) |
| POS-026 | POS Cashier Shift Handover & Drawer Accountability | M | W517 (cashier shift handover — X-report, drawer count, variance documentation, sealed drawer swap, handover sign-off) | W5A (store opening — initial float), W5F (store closing — EOD Z-report), W272 (cashier over/short — variance escalation), W278 (mid-day cash skimming), W212 (Smart Safe — sealed drawer storage) |
| POS-027 | Cashier Onboarding, POS Training & Competency Certification | S | W518 (cashier training — training mode, supervised transactions, tender training, special procedures, certification assessment, annual recertification) | W15 (HR onboarding — trigger), W152 (IT provisioning — POS access), W51 (training management — certification log), W292 (employee master — certification status) |
| POS-028 | POS Suspicious Transaction & AML Compliance Reporting | M | W519 (POS suspicious transaction & AML — threshold monitoring, structuring detection, customer identification, legitimacy assessment, STR filing with AMLC, tipping-off prohibition) | W5B (in-store selling — transaction source), W37 (loss prevention — suspicious behavior escalation), W354 (B2B AML screening — parallel process for trade accounts), W51 (training — AML awareness) |
| POS-029 | Age-Restricted Product Verification & ID Capture at POS | M | W520 (age-restricted product verification — SKU flag prompt, ID request, age calculation, approval/denial, compliance log, spot-audit) | W5B.9 (age-restricted prompts), W252 (item master — age-restricted flag), W518 (cashier training — age-restricted procedure), W37 (loss prevention — compliance log review) |
| POS-030 | POS Transaction Suspend, Park & Recall | S | W521 (transaction suspend/park/recall — reason code, suspend ID, cross-terminal recall, auto-cancel timeout, max suspend limits, manager dashboard) | W5B (in-store selling — suspend within checkout), W517 (shift handover — pending transaction transfer), W5F (store closing — auto-cancel remaining at EOD), W37 (loss prevention — suspicious suspend patterns) |
| POS-031 | POS Daily Transaction Review & Cashier Performance Audit | S | W522 (daily transaction review — cashier performance dashboard, exception alerts, high-value spot-check, void/refund review, discount analysis, weekly ranking) | W5B (in-store selling — transaction data source), W5F (store closing — cash variance), W517 (shift handover — handover variance), W529 (void/refund authorization — authorization data source), W37 (loss prevention — fraud escalation), W72 (employee performance — performance feed), W518 (cashier training — retraining trigger) |
| POS-032 | POS Promotional Terminal Setup & Pre-Live Verification | S | W523 (promotional terminal setup — test scan, quick-key verification, customer display check, bank-BIN test, bundle/BOGO test, terminal readiness dashboard, post-promo deactivation) | W13 (promotions — promo calendar and pricing), W262 (store promotional setup — physical display), W40 (price changes — price file), W149 (bank partnership — bank-BIN promo), W48 (helpdesk — terminal issues) |
| POS-033 | Demo / Display Unit Selling at POS | S | W524 (demo/display unit selling — condition assessment, depreciation pricing, customer disclosure, modified warranty, display removal, replacement order) | W97 (sample/demo inventory — display tracking), W445 (display infrastructure — display condition), W86 (planogram compliance — display position), W22 (transfers — replacement sourcing), W33 (warranty — modified warranty terms) |
| POS-034 | POS Continuous Near-Real-Time Sync & Nightly Reconciliation | M | W525 (continuous sync & nightly reconciliation — continuous event streaming, nightly completeness validation, inventory reconciliation, void/return sync, loyalty reconciliation, price file push, new item push, discontinued item push, failure alerting), W533 (real-time event streaming — continuous event bus, multi-consumer processing, continuous price push) | W5A (store opening — local data store verification), W5F (store closing — Z-report as reconciliation input), W5G (offline POS — offline event replay), W252 (item master — new/discontinued feed), W40 (price changes — price update feed), W48 (helpdesk — failure escalation), W535 (offline capability — local data store refresh) |
| POS-035 | POS Customer Queue Management & Express Lane Operations | S | W526 (customer queue management — queue monitoring, threshold alerting, backup terminal activation, express lane criteria, mPOS queue busting, queue analytics) | W206 (mPOS — queue busting), W34 (shift scheduling — staffing from queue patterns), W516 (SCO — complementary queue reduction), W247 (smart locker — BOPIS without queuing), W35 (management reporting — queue analytics) |
| POS-036 | POS Tax Exemption Processing (Government / PEZA / Institutional) | S | W527 (tax exemption processing — certificate verification, zero output VAT application, partial exemption, GL posting, tax-exempt transaction register, monthly Finance review) | W5B (in-store selling — tax exemption within checkout), W8 (AR — B2B billing), W24 (credit application — customer VAT treatment), W253 (customer master — VAT registration), W9A.16 (VAT return — exempt/zero-rated schedule) |
| POS-037 | POS Digital Receipt / E-Receipt Delivery | S | W528 (digital receipt — delivery method selection, BIR-compliant e-receipt generation, email/SMS delivery, paper fallback, delivery confirmation, adoption analytics) | W5B (in-store selling — receipt generation), W54A (BIR CAS — registered receipt format), W17 (loyalty — customer email/mobile), W263 (enrollment — enrollment link in e-receipt), W65 (CSAT/NPS — survey link) |
| POS-038 | POS Void & Refund Tiered Authorization Matrix | M | W529 (void & refund tiered authorization — tiered authorization by amount, reason code, authorizer verification, remote authorization, daily void/refund summary) | W5B.10 (void transaction — reversal logic), W12A (in-store returns — refund processing), W101 (customer refund & credit — credit memo), W272 (cashier over/short — variance feed), W37 (loss prevention — void/refund pattern analysis), W522 (daily transaction review — void/refund summary) |
| POS-039 | POS High-Value Transaction Documentation & Customer ID | S | W530 (high-value transaction documentation — threshold monitoring, customer ID capture, ID type selection, encrypted ID recording, LP anomaly review) | W5B (in-store selling — high-value within checkout), W519 (AML — PHP 500K+ cash trigger), W522 (daily review — high-value spot-check), W37 (loss prevention — anomaly analysis), W17 (loyalty — customer auto-populate) |
| POS-040 | POS Bagging, Carry-Out & Bag Fee Compliance | S | W531 (bagging & bag fee — LGU-specific bag fee rules, reusable bag incentive, bag fee GL posting, carry-out assistance, bag supply tracking) | W5B (in-store selling — bag fee within checkout), W254 (location master — LGU jurisdiction), W136 (indirect procurement — bag supply), W438 (yard dispatch — carry-out for bulky items) |
| POS-041 | POS Clearance & "Final Sale" Item Processing | S | W532 (clearance & final sale — clearance identification, verbal disclosure, customer display notice, return block, sell-through reporting) | W5B (in-store selling — clearance within checkout), W93 (markdown & clearance pricing — clearance price source), W12 (returns — final-sale return block), W220 (SLOB — unsold clearance write-off), W315 (product lifecycle — clearance status flag) |
| POS-042 | POS Real-Time Event-Driven Architecture | M | W533 (real-time event streaming — event bus, discrete events, guaranteed delivery, multi-consumer, event replay) | W525 (nightly reconciliation — completeness validation), W535 (offline capability — offline event queue), W5B (in-store selling — event source), W11/W19 (ecommerce — ATP consumer) |
| POS-043 | POS Local Data Store & Continuous Price Push | M | W535 (offline capability — local embedded data store, continuous push, nightly full refresh), W533 (event streaming — continuous price push to terminals) | W525 (nightly reconciliation — full price file refresh), W5A (store opening — local data store verification), W40 (price changes — price push source), W252 (item master — SKU catalog source) |
| POS-044 | Multi-Origin / Mixed-Basket Fulfillment at POS | M | W534 (multi-origin fulfillment — mixed-basket order creation, per-origin fulfillment routing, unified financial posting) | W536 (unified order management — orchestration engine), W19 (home delivery — DC fulfillment), W22 (inter-store transfer), W246 (drop-ship vendor), W273 (endless aisle), W5B (in-store selling — carry-out), W12 (returns — cross-origin) |
| POS-045 | Unified Order Management & Cross-Channel Fulfillment Orchestration | M | W536 (unified order management — multi-channel intake, ATP evaluation, fulfillment routing, multi-origin execution, cross-channel returns) | W534 (mixed-basket POS — order source), W11 (BOPIS — store fulfillment), W19 (home delivery — DC fulfillment), W19B (ship-from-store), W180 (marketplace), W210 (dark store), W246 (drop-ship), W98 (order exceptions), W105 (multi-channel allocation) |
| POS-046 | POS Offline Terminal-to-Terminal Local Sync | S | W535 (offline capability — terminal-to-terminal LAN sync, store-level ATP consistency during offline) | W5G (offline recovery — store LAN coordination), W533 (event streaming — LAN event broadcast) |
| POS-047 | POS Continuous Price & Promotion Push (Real-Time Activation) | M | W533 (real-time event streaming — continuous price push within 60 sec), W525 (nightly reconciliation — full price file push as fallback) | POS-024 (DTI price freeze — immediate price push activation), W13 (promotions — promo push source), W40 (price changes — price push source) |
| POS-048 | POS Offline Scope Governance & Capability Matrix | M | W535 (offline capability — offline capability matrix, configurable per store, quarterly offline drill) | W5G (offline recovery — exception handling), W5B (in-store selling — offline within checkout), W48 (helpdesk — offline notification) |
| POS-071 | POS Credit Card Installment Selling & 0% Interest Promotion Processing | M | W747 (POS installment selling — bank promo lookup, term selection, authorization, subsidy tracking) | W149 (bank partnership — promo terms), W85 (margin analysis — subsidy cost), W540 (BIR invoice — installment receipt), W427 (DTI promo permit) |
| POS-072 | POS Customer Loyalty On-the-Spot Upselling & Cross-Selling | S | W748 (POS loyalty upselling — basket analysis, targeted suggestions, tier upgrade incentive, service attachment) | W156 (CDP — customer profile), W313 (loyalty config — tier thresholds), W13 (promotions — bundle rules), W522 (cashier performance — upsell tracking) |
| POS-073 | POS Heavy Equipment & Power Tool Safety Acknowledgment | M | W749 (POS safety acknowledgment — high-risk item detection, safety brief, PPE suggestion, digital signature, archival) | W252 (item master — safety classification), W698 (SDS — safety data sheets), W285 (public liability — defense archive), W520 (age-restricted verification) |

## R6. Ecommerce Integration (ECOM)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| ECOM-001 | Real-Time Inventory Sync | M | W11 (BOPIS ATP), W19 (delivery ATP) | W50 (catalog sync), W273 (in-store endless aisle & vendor direct-to-customer delivery — endless aisle ATP check) |
| ECOM-002 | Real-Time Price Sync | M | W13.5 (promo price push), W40.7 (price sync) | — |
| ECOM-003 | BOPIS Order Flow | M | W11 (BOPIS fulfillment) | — |
| ECOM-004 | Home Delivery Order Flow | M | W19 (home delivery fulfillment) | — |
| ECOM-005 | Order Status Tracking | M | W19.9 (tracking link), W41.E (ecommerce issue resolution), W268 (last-mile home delivery tracking & proof-of-delivery) | — |
| ECOM-006 | Payment Gateway Integration | M | W19 (payment reconciliation), W11.1 (BOPIS payment), W267 (ecommerce digital payment reconciliation & dispute handling) | — |
| ECOM-007 | Return Initiation (Online) | M | W12B (online returns), W19.12a (home delivery reverse logistics), W215 (home delivery returns) | — |
| ECOM-008 | Customer Data Sync | M | W17 (loyalty data), W41 (complaint data) | W24 (customer master) |
| ECOM-009 | Product Catalog Sync | M | W50 (PIM / product content management), W311 (barcode, GTIN & item identification master — GTIN in ecommerce catalog feeds) | — |
| ECOM-010 | Promo/Coupon Integration | S | W13 (digital coupon management) | — |
| ECOM-011 | Home Delivery Fulfillment | M | W19 (full home delivery lifecycle including failed delivery), W268 (last-mile home delivery tracking & proof-of-delivery) | — |
| ECOM-012 | Delivery Partner Integration | M | W19.7 (3PL API integration), W66 (inter-island logistics), W242 (3PL performance review), W62B (3PL/delivery partner onboarding & offboarding), W268 (last-mile tracking & carrier status integration) | — |
| ECOM-013 | Marketplace Integration (Lazada/Shopee) | S | W180 (ecommerce marketplace integration — listing sync, order pull, inventory reservation, commission reconciliation) | W50 (PIM — product content feed), W13 (promotions — marketplace pricing) |
| ECOM-014 | Ship-from-Store Fulfillment | S | W19B (ship from store — order routing, store pick & pack, carrier handoff) | W4 (replenishment — store stock for fulfillment), W11 (BOPIS — store pick infrastructure) |
| ECOM-015 | Omni-channel Customer Ticketing & Support | S | W258 (omni-channel customer ticketing & support management — unified tickets, routing, SLA, escalation) | W41 (complaint resolution — ticket source), W17 (loyalty — customer 360) |
| ECOM-016 | Ecommerce Order Exception & Cancellation Management | S | W98 (ecommerce order exception & cancellation management — payment failure, fraud hold, auto-refund), W266 (ecommerce online fraud detection & prevention) | W19 (home delivery — order lifecycle), W12B (online returns — cancellation trigger) |

## R7. Supply Chain Planning (SCP)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| SCP-001 | Demand Forecasting | S | W31 (demand forecasting cycle) | W32 (seasonal planning), W5509 (unfulfilled-demand & lost-sales capture — realized-demand feedback into forecast overrides and safety-stock tuning) |
| SCP-002 | Replenishment Planning | M | W4.1 (auto replenishment), W57 (promo stock allocation), W312 (replenishment & planning parameter master governance — ROP/safety stock/EOQ parameter governance) | — |
| SCP-003 | Reorder Point Calculation | M | W2A.1 (ROP breach), W31.8 (parameter governance), W312 (replenishment & planning parameter master governance — ROP parameter calculation and validation) | — |
| SCP-004 | Safety Stock Optimization | S | W31.8 (safety stock review), W312 (replenishment & planning parameter master governance — safety stock parameter governance and quarterly review) | — |
| SCP-005 | Seasonal Planning | S | W32 (seasonal buy planning), W191 (global supply chain — incoterm & marine insurance tracking) | W13 (promo calendar) |
| SCP-006 | Allocation Management | S | W4.2 (constrained allocation), W57 (promo allocation) | — |
| SCP-007 | Purchase Recommendation | M | W2A.1–2 (auto-suggest POs), W31.6 (forecast-driven POs) | W56 (backorder triggers PO), W133 (S&OP cycle — consensus demand input), W183 (supply chain network optimization review) |
| SCP-013 | Carrier Performance & Freight Rate Benchmarking | S | W762 (carrier performance — weekly scorecard, SLA tracking, freight benchmarking, rate renegotiation, carrier rotation) | W277 (freight bill audit — cost data), W500 (damage claims — damage data), W62B (3PL management — carrier lifecycle), W199 (telematics — own fleet data), W242 (3PL review — strategic review) |
| SCP-014 | Vendor Diversification & Alternative Sourcing | M | W763 (vendor diversification — concentration risk scoring, alternative vendor qualification, trial orders, dual-sourcing, disruption activation) | W558 (supplier risk — risk data), W491 (financial health — vendor viability), W36 (vendor onboarding — qualification), W60 (emergency procurement — disruption activation), W44 (vendor scorecard — performance tracking) |

## R8. HR & Payroll (HR)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| HR-001 | Multi-Entity Payroll | M | W10 (payroll processing — 5 entities × 2 runs) | W43.15 (cross-entity transfer), W280 (court-ordered wage garnishment & third-party deductions — payroll deduction processing), W292 (employee master data governance — cross-entity employee data accuracy) |
| HR-002 | Philippine Statutory Deductions | M | W10.4 (SSS, PhilHealth, Pag-IBIG) | W280 (court-ordered wage garnishment & third-party deductions — legal deduction processing), W292 (employee master data governance — statutory ID validation & completeness) |
| HR-003 | BIR Withholding Tax (Compensation) | M | W10.4 (TRAIN law tables) | W43.10 (final pay computation) |
| HR-004 | 13th Month Pay Computation | M | W10 (13th month auto-calc), W43.10 (pro-rated final pay) | W9B.18 (year-end accrual) |
| HR-005 | Time & Attendance Integration | S | W10.1 (biometric import), W34 (shift scheduling) | — |
| HR-006 | Shift Scheduling | S | W34 (store shift scheduling) | — |
| HR-007 | Leave Management | M | W10.2 (leave verification), W34.1d (leave in scheduling) | — |
| HR-008 | Employee Self-Service | N | W10.10 (payslip distribution), W17.5 (loyalty balance inquiry) | — |
| HR-009 | Recruitment & Onboarding | N | W15 (recruitment & onboarding) | W16 (new store hiring), W292 (employee master data governance — creation & validation) |
| HR-010 | Overtime Calculation | M | W10.3 (OT calculation per Labor Code), W228 (sales commission calculation) | W34.8 (scheduled vs. actual hours), W74 (employee expense reimbursement — OT meal allowance) |
| HR-011 | Holiday Pay Calculation | M | W10.3 (holiday pay rates) | — |
| HR-012 | Bank File Generation | M | W10.7 (bank file for payroll crediting) | — |
| HR-013 | Employee Loan & Advance Management | M | W76 (employee loans & advances) | W10 (payroll processing), W43 (separation — loan balance settlement) |
| HR-014 | Employee Grievance & Whistleblower Case Management | S | W79 (employee grievance & whistleblower process) | W53 (data privacy breach response) |
| HR-015 | Philippine Statutory Benefits & Claims Management | M | W251 (Philippine statutory benefits & claims administration) | W10 (payroll processing statutory deductions) |
| HR-016 | Employee Expense Reimbursement | M | W74 (employee expense reimbursement — receipt attachment, approval, reimbursement via payroll) | W10 (payroll — reimbursement payment), W25 (petty cash — small expense alternative) |
| HR-017 | Employee PPE & Uniform Lifecycle | S | W172 (employee PPE & uniform lifecycle — issuance, replacement, cost allocation) | W15 (onboarding — initial PPE/uniform issuance), W47 (facility maintenance — PPE for maintenance staff) |
| HR-023 | Store-Level Meal Break & Rest Period DOLE Compliance | M | W753 (meal break scheduling — auto-generation from roster, compliance monitoring, escalation, DOLE reporting) | W34 (shift scheduling — roster source), W561 (attendance exception — break violations), W505 (DOLE inspection — compliance documentation), W10 (payroll — break violation deductions) |
| HR-024 | Store-Level New Hire First-30-Day Check-In | S | W754 (first-30-day check-in — Day 7/15/30 structured reviews, early intervention, PIP, probation recommendation) | W15 (onboarding — initial support), W609 (buddy system — buddy feedback), W567 (cross-training — skill assessment), W522 (cashier performance — data source), W628 (exit interview — early exit data) |
| HR-025 | Store-Level Internal Theft Prevention Awareness | S | W755 (internal theft prevention — daily awareness, cash handling verification, stockroom monitoring, employee purchase flags, monthly campaign) | W710 (LP analytics — pattern detection), W562 (LP daily routine — operational integration), W79 (whistleblower — reporting channel), W205 (employee purchases — transaction monitoring) |

## R9. CRM & Loyalty (CRM)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| CRM-001 | Loyalty Points Engine | M | W17 (loyalty program operations), W313 (loyalty program configuration & rule master — tier rules, earning rules, redemption catalog governance) | W5B.5 (POS points earning) |
| CRM-002 | Customer Master (B2C) | M | W17.1–2 (enrollment & dedup), W50 (ecommerce customer sync) | — |
| CRM-003 | Trade Account Management | M | W8 (AR processing, dormant account management), W5B.4c (trade pricing at POS) | W24 (credit application) |
| CRM-004 | Corporate Account Management | M | W58 (corporate/project accounts), W24 (credit application), W162 (Project Quotation), W163 (Contract Pricing), W164 (Staged Delivery), W165 (Milestone Billing), W166 (Tendering) | — |
| CRM-005 | Tiered Loyalty | S | W17.8 (tier movement), W313 (loyalty program configuration & rule master — tier definition and qualification criteria governance) | — |
| CRM-006 | Customer Purchase History | S | W12A.2 (transaction lookup), W17 (loyalty history), W156 (customer data platform — unified profile across channels) | W29 (recall customer tracing) |
| CRM-007 | Marketing Campaign Integration | N | W13 (promotions), W65 (CSAT/NPS surveys) | — |
| CRM-008 | Credit Application Workflow | M | W24 (credit application & approval), W328 (customer credit limit periodic review — annual credit reassessment) | W8.3 (credit limit enforcement) |
| CRM-009 | Government Procurement Compliance (PHILGEPS) | S | W78 (government procurement participation) | W166 (corporate/institutional tendering), W230 (contract review) |
| CRM-010 | Customer Account Reactivation | S | W84 (customer account reactivation — dormant account identification, outreach, reactivation offers) | W8 (AR — dormant account management), W17 (loyalty — reactivation points) |
| CRM-011 | Customer Feedback-to-Action Loop | S | W87 (customer feedback-to-action loop — NPS tracking, feedback categorization, action assignment) | W65 (CSAT/NPS surveys — feedback source), W41 (complaint resolution — feedback from complaints) |
| CRM-012 | Trade Sales Pipeline & Territory Management | S | W103 (trade sales pipeline & territory management — pipeline stages, territory assignment, forecasting) | W58 (corporate accounts — pipeline source), W162 (project quotation — quote from pipeline), W286 (RMN vendor billing & yield management — trade/vendor media spend pipeline) |
| CRM-013 | Trade Counter / Pro Desk Operations | S | W112 (trade counter / pro desk operations — order taking, quick quote, express checkout for trade customers) | W5B (POS — trade pricing at checkout), W138 (home installation — pro referral) |
| CRM-014 | Customer Data Platform & Hyper-Personalization | S | W156 (customer data platform — unified profile, identity resolution, consent management, segmentation) | W17 (loyalty — customer data source), W50 (ecommerce — behavioral data) |
| CRM-017 | Customer Post-Purchase Follow-Up | S | W756 (post-purchase follow-up — qualifying transaction identification, multi-channel follow-up, satisfaction survey, escalation) | W41 (complaint resolution — escalation), W258 (ticketing — ticket creation), W510 (product reviews — review prompt), W156 (CDP — response data), W617 (B2B success — coordination) |
| CRM-018 | Customer On-the-Spot Loyalty Tier Upgrade | S | W757 (tier upgrade offer — proximity detection, personalized suggestion, immediate upgrade, analytics) | W313 (loyalty config — tier thresholds), W5B (POS checkout — delivery channel), W156 (CDP — customer history), W515 (tier re-evaluation — migration processing), W104 (loyalty governance — liability impact) |

## R10. Analytics & Reporting (RPT)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| RPT-001 | Executive Dashboard | M | W35.2 (daily flash), W35.4 (weekly sales), W231 (QBR reporting) | — |
| RPT-002 | Store P&L | M | W35.10 (store P&L with occupancy allocation) | W26 (budget variance) |
| RPT-003 | Sales Analytics | M | W35.4 (week-on-week sales), W13.8 (promo performance) | W31.7 (forecast vs. actual) |
| RPT-004 | Inventory Reports | M | W6 (cycle count variance), W9A.6 (inventory valuation), W102 (category performance review & P&L ownership) | W42.17 (physical inventory summary), W97 (sample & demo inventory reporting) |
| RPT-005 | Purchase Analysis | S | W44 (vendor scorecard), W27 (rebate analytics), W130 (competitor price intelligence gathering) | — |
| RPT-006 | BIR-Compliant Tax Reports | M | W9A.16 (VAT returns), W9A.16a (EWT remittance), W216 (BIR CAS audit), W235 (transfer pricing compliance) | — |
| RPT-007 | Consolidated Financial Statements | M | W9 (financial close & reporting — consolidated statements), W14 (intercompany elimination input) | — |
| RPT-008 | Ad-Hoc Reporting | S | W35.18–19 (ad-hoc reports & BI analyses), W113 (business intelligence & data governance — self-service analytics) | — |
| RPT-009 | Mobile Dashboard | N | W35.2 (CFO mobile dashboard) | — |
| RPT-010 | Scheduled Report Distribution | S | W35 (full reporting rhythm — daily/weekly/monthly), W231 (QBR reporting), W67 (monthly store performance review) | — |
| RPT-011 | Category Performance Review & P&L Ownership | S | W102 (category performance review & P&L ownership — category P&L, buyer scorecard, assortment vs. plan) | W1 (assortment review — category input), W35 (management reporting — category reports) |
| RPT-012 | Pricing Hierarchy Governance & Compliance Audit | S | W107 (pricing hierarchy governance & compliance audit — rule validation, override audit, price gap analysis) | W40 (price change — hierarchy execution), W69 (price compliance audit — store-level check) |

## R11. Intercompany & Transfer Pricing (IC)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| IC-001 | IC AP/AR Automation | M | W14 (IC transactions & settlement), W435 (intercompany SLA billing), W461 (intercompany fulfillment logistics settlement) | — |
| IC-002 | Arm's-Length Transfer Pricing | M | W14 (intercompany transactions — transfer pricing rules, annual TP review), W235 (transfer pricing compliance & documentation), W305 (intercompany transfer pricing rule master — TP rule governance) | — |
| IC-003 | IC Elimination on Consolidation | M | W9A.13 (IC elimination), W234 (IC profit elimination) | — |
| IC-004 | IC Settlement | M | W14.6–7 (net settlement) | — |
| IC-005 | IC Reconciliation | M | W14.4–5 (IC reconciliation) | — |

## R12. Document Management (DOC)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| DOC-001 | Electronic Document Storage | M | W7.1 (invoice capture), W21.1 (capex attachments), W33.3 (warranty photos) | W50 (digital assets) |
| DOC-002 | BIR-Compliant Invoice Format | M | W5B.8 (BIR-registered receipt), W7 (vendor invoices) | — |
| DOC-003 | Delivery Receipt Tracking | M | W18.7 (DR capture), W3 (DC receiving DR) | — |
| DOC-004 | Import Document Management | M | W2B (BL, LC, customs docs), W36 (vendor permits) | — |
| DOC-005 | Document Retention Policy | M | W35 quarterly review, W42 (10-year archive), W256 (enterprise document retention & archiving policy) | W53 (breach register 5-year retention), W81 (bad debt write-off 10-year retention) |
| DOC-006 | Approval Workflow with Attachments | S | W21 (capex with quotes), W62 (contracts with attachments), W243 (POA board approval lifecycle) | — |
| DOC-007 | Hazardous Waste Disposal Tracking | S | W82 (DENR-compliant manifest tracking, per-location generator registration, quarterly reporting), W167 (Recycling / Circular Economy), W236 (hazmat storage DC), W237 (hazmat handling store), W238 (hazmat spill incident) | W52 (fleet — used oil/battery disposal), W68 (discontinued chemical waste) |
| DOC-008 | Enterprise Document Retention & Archiving Policy | M | W255 (electronic document storage & retrieval ERP-wide), W256 (enterprise document retention & archiving policy — configurable periods, legal hold, secure destruction) | W35 (reporting — retention review), W42 (physical inventory — archive) |

## R13. Master Data Management (MDM)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| MDM-001 | Centralized Item Master | M | W1.7 (SKU creation), W46.1 (kit BOM), W64 (pilot SKU), W252 (centralized item master creation & governance), W302 (kit/BOM & bundle structure master — kit component governance), W303 (manufacturer/brand master — brand-to-SKU linkage), W311 (barcode, GTIN & item identification master — barcode assignment at SKU creation) | W50 (PIM content), W181 (store-level price tag printing & verification — item data accuracy) |
| MDM-002 | Item Attribute Management | M | W50.4 (category-specific attributes), W1 (assortment), W298 (product attribute template master governance) | — |
| MDM-003 | Customer Data Quality | M | W17 (deduplication at enrollment), W24 (credit data validation), W253 (customer master data governance & deduplication) | — |
| MDM-004 | Vendor Onboarding Workflow | S | W36 (vendor onboarding lifecycle), W252 (item master governance — vendor-SKU linkage) | — |
| MDM-005 | Pricing Master Governance | M | W289 (pricing master governance — base prices & matrices), W40 (price change), W13 (promo pricing) | W61 (price match analytics) |
| MDM-006 | Location Master | M | W16.4 (new store creation), W54 (LGU permit data), W45 (closure deactivation), W254 (location master lifecycle & hierarchy management), W310 (address & geographic hierarchy master — standardized address linkage per location) | — |
| MDM-007 | Hierarchical Category Structure | M | W290 (hierarchical category structure management), W1 (category management), W50 (category navigation) | — |
| MDM-008 | Vendor Master Data Governance | M | W252 (item master governance — vendor-SKU linkage), W36 (vendor onboarding — creation with approval), W287 (vendor master data governance & deduplication) | W44 (vendor scorecard — vendor data quality feed) |
| MDM-009 | Financial Master Data Governance | M | W288 (financial master data governance — COA & cost centers) | W26 (budget), W9 (close) |
| MDM-010 | Master Data Quality Monitoring | M | W291 (master data quality monitoring & reporting) | — |
| MDM-011 | Employee Master Data Governance | M | W292 (employee master data governance & cross-entity lifecycle), W15 (onboarding — creation trigger), W43 (separation — deactivation trigger) | W10 (payroll — employee data consumer), W152 (IT provisioning — access triggered by position changes), W34 (shift scheduling — position/department data consumer) |
| MDM-012 | Tax & Regulatory Master Data Governance | M | W293 (tax & regulatory master data governance), W260 (BIR eFPS filing — tax code consumer), W90 (monthly tax filing — tax code consumer) | W7 (AP — EWT computation per ATC), W9A.16 (month-end VAT return — tax rate consumer), W10 (payroll — WHT on compensation) |
| MDM-013 | Unit of Measure (UOM) Master & Conversions | M | W294 (UOM master & conversion management) | W5B.2 (POS catch-weight selling — UOM consumer), W3B.3 (yard catch-weight — UOM consumer), W252 (item master — UOM assignment), W289 (pricing — per-UOM pricing) |
| MDM-014 | Payment Terms & Settlement Rule Master | M | W295 (payment terms & settlement rule master governance), W36 (vendor onboarding — term assignment), W24 (credit application — term assignment) | W7 (AP — payment proposal per terms), W8 (AR — due date computation per terms), W30 (treasury — cash flow impact of terms) |
| MDM-015 | Service & Non-Stock Item Master Governance | M | W296 (service & non-stock item master governance), W38 (special order fulfillment — non-stock template consumer), W138 (home installation — service item consumer) | W5B (POS — service item selling), W139 (tool rental — rental item consumer), W168 (paint mixing — custom processing), W169 (lumber cutting — custom processing), W282 (subscription billing — subscription service items) |
| MDM-016 | Currency & Exchange Rate Master Governance | M | W307 (currency & exchange rate master governance — daily rate import, rate type config, month-end rate lock, hedged rate integration) | W2B (import PO — rate consumer), W9A.5a (month-end FX revaluation — rate consumer), W80 (FX hedging — hedged rate source), W233 (cash flow forecasting — rate input), W232 (LC lifecycle — rate input) |
| MDM-017 | Fiscal Calendar & Posting Period Master Governance | M | W308 (fiscal calendar & posting period master — fiscal year variant, posting period control, document numbering series, IC period alignment) | W9A (month-end close — period consumer), W9B (year-end close — period consumer), W54A (BIR CAS registration — numbering series), W216 (BIR CAS audit — numbering compliance), W14 (IC transactions — IC period alignment) |
| MDM-018 | Bank & Banking Partner Master Governance | M | W309 (bank & banking partner master governance — bank master records, entity bank accounts, store deposit linkage, e-wallet partner config, payment file formats) | W7 (AP — payment file generation), W10 (payroll — bank credit file), W30 (treasury — cash position), W89 (bank reconciliation — bank statement matching), W174 (CIT — deposit account linkage), W261 (e-wallet settlement — partner config) |
| MDM-019 | Address & Geographic Hierarchy Master (Philippine-Specific) | M | W310 (address & geographic hierarchy master — PSGC hierarchy, LGU tax jurisdiction mapping, DC coverage areas, BIR RDO linkage, address standardization) | W254 (location master — address linkage), W253 (customer master — address standardization), W287 (vendor master — address standardization), W54 (LGU permits — LGU jurisdiction), W119 (real property tax — LGU tax jurisdiction), W304 (routing — DC coverage area) |
| MDM-020 | Barcode, GTIN & Item Identification Master Governance | M | W311 (barcode, GTIN & item identification master — GS1 prefix management, barcode assignment, multi-level barcodes, custom barcode ranges, vendor barcode verification) | W252 (item master — barcode assignment at creation), W5B (POS — barcode scanning), W3 (DC receiving — case barcode), W50 (PIM — GTIN in catalog), W180 (marketplace — GTIN sync), W168 (paint mixing — custom barcode), W169 (lumber cutting — custom barcode) |
| MDM-021 | Replenishment & Planning Parameter Master Governance | M | W312 (replenishment & planning parameter master governance — ROP, safety stock, EOQ, lead time per SKU per location, channel-specific parameters, seasonal overrides, quarterly review, annual calibration) | W2A (auto-replenishment — parameter consumer), W4 (store replenishment — parameter consumer), W31 (demand forecasting — forecast feeds parameters), W252 (item master — new SKU parameter setup trigger), W254 (location master — new store parameter setup trigger), W299 (assortment matrix — assortment-driven parameter exceptions), W304 (routing — transit time feeds lead time parameter), W306 (seasonal calendar — event-driven parameter overrides), W105 (multi-channel allocation — channel-specific parameters) |
| MDM-022 | Loyalty Program Configuration & Rule Master Governance | M | W313 (loyalty program configuration & rule master — tier definitions, earning rules, redemption catalog, tier recalculation, partner rules, financial liability review) | W17 (loyalty operations — rule consumer), W104 (loyalty financial governance — liability validation), W5B (POS — loyalty scan, tier recognition, points earning), W149 (bank partnership — co-branded earning rules), W180 (marketplace — marketplace earning rules), W156 (CDP — tier-based segmentation), W253 (customer master — tier status on member profile) |
| MDM-023 | Planogram Template & Space Planning Master Governance | S | W314 (planogram template & space planning master — template design, space allocation, SKU-to-position mapping, fixture master, store cluster assignment, quarterly performance review) | W299 (assortment matrix — SKU list feeds planogram), W86 (planogram compliance — template reference for compliance check), W262 (promotional setup — display instructions), W264 (seasonal transition — seasonal planogram refresh), W252 (item master — dimensions for fixture fit), W297 (bin master — fixture capacity), W16 (new store opening — provisional planogram assignment) |
| MDM-024 | Product Lifecycle Status & Transition Rule Master Governance | M | W315 (product lifecycle status & transition rule master — status definitions, status-dependent behaviors, transition prerequisites, automated triggers, downstream cascade, quarterly audit) | W252 (item master — New status at creation), W68 (product discontinuation — EOL/Discontinued transition), W264 (seasonal transition — Seasonal status), W219 (quarantine — Blocked status), W29 (product recall — Blocked status), W110 (supplier quality CAPA — quality-driven blocking), W2A (auto-replenishment — status-driven PO control), W300 (promotional rules — status-driven promo eligibility), W299 (assortment — status-driven inclusion), W314 (planogram — status-driven position management), W312 (planning parameters — status-driven parameter behavior) |
| MDM-025 | Digital Asset & Product Content Master Governance | M | W316 (digital asset & product content master — asset type standards, channel variants, asset creation/ingestion, metadata/SEO, quality review, publication, lifecycle management, quarterly audit) | W50 (PIM — content repository and distribution), W252 (item master — content validation source), W298 (attribute templates — attribute-driven metadata), W180 (marketplace — channel-specific content distribution), W5B (POS — product images), W181 (price tag printing — images on shelf labels), W262 (promotional setup — promotional content), W142 (social media — social-optimized assets), W129 (private label — private label content production), W311 (barcode/GTIN — GTIN-linked Google Shopping content) |
| MDM-026 | Fixed Asset Master Data Governance | M | W399 (fixed asset master data governance) | FIN-011 (fixed asset management) |
| MDM-027 | Equipment & Asset Maintenance (EAM) Master Governance | S | W400 (equipment & asset maintenance master governance) | GOV-006 (facility & asset maintenance) |
| MDM-028 | Fleet & Vehicle Master Governance | S | W401 (fleet & vehicle master governance) | GOV-007 (fleet operations & driver management) |
| MDM-029 | Contract & Agreement Master Governance | S | W402 (contract & agreement master governance) | GOV-001 (corporate governance), DOC-006 (approval workflow with attachments), GOV-027 (3PL contract management) |
| MDM-030 | Competitor & Market Intelligence Master Governance | S | W403 (competitor & market intelligence master governance) | GOV-014 (competitor intelligence) |
| MDM-031 | Point-of-Sale (POS) System & Hardware Master Governance | M | W404 (POS system & hardware master governance) | POS-001 (600 POS terminals) |
| MDM-032 | Data Privacy & Consent Preferences Master Governance | M | W405 (data privacy & consent preferences master governance) | NFR-010 (data privacy), NFR-016 (data privacy breach response) |
| MDM-033 | ESG & Sustainability Metrics Master Governance | S | W406 (ESG & sustainability metrics master governance) | NFR-018 (ESG & sustainability reporting) |

## R14. Non-Functional Requirements (NFR)

| Req ID | Requirement | Target | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| NFR-001 | POS Uptime | 99.9% | W5G (offline recovery), W55 (DR failover), W5E (store opening delay procedure — system-down protocol) | W48 (helpdesk P1 SLA) |
| NFR-002 | Back-Office Uptime | 99.5% | W55 (IT disaster recovery), W366 (network infrastructure), W368 (database & cloud infrastructure), W376 (IT capacity planning) | W48 (incident management), W380 (IT alert & event management) |
| NFR-003 | POS Transaction Speed | < 3 sec | W5 (POS selling transaction flow), W463 (catch-weight transaction processing) | — |
| NFR-004 | Report Generation | < 30 sec | W35 (management reporting), W113 (BI & data governance — query performance) | — |
| NFR-005 | Concurrent Users | 1,000–1,500 | W5B (600 POS terminals), W35 (HQ reporting) | — |
| NFR-006 | Data Retention | 10 years | W42 (physical inventory archive), W35 quarterly retention review | Data Volumes §1.2 |
| NFR-007 | Security | RBAC, audit trails | W37 (POS audit), W48 (change management), W186 (SOP governance), W230 (contract review), W236 (hazmat storage DC), W237 (hazmat handling store), W238 (hazmat spill incident), W243 (POA lifecycle), W152 (employee IT provisioning & access lifecycle management), W132 (software development & change management), W131 (IT asset lifecycle management), W320 (electronic banking security & payment control), W367 (cybersecurity operations), W375 (PAM operations), W383 (IT security incident response), W393 (zero trust connectivity), W397 (threat hunting) | W53 (breach response), W278 (mid-day cash skimming / till sweeps — cash security audit trail), W281 (self-checkout exception & intervention — SCO security monitoring), W372 (security awareness training), W387 (IT compliance CSA), W388 (shadow IT governance) |
| NFR-008 | Scalability | 300+ stores | W16 (new store opening process), W45 (store closure), W223 (store design), W224 (contractor selection), W225 (construction supervision), W226 (store renovation capex), W227 (handover) | — |
| NFR-009 | Localization | Full PH | W9A (BIR compliance), W10 (payroll statutory), W54 (LGU permits), W216 (BIR CAS audit), W217 (SC/PWD VAT-exemption), W54A (BIR CAS registration per location), W310 (address & geographic hierarchy master — Philippine PSGC codes, LGU tax jurisdiction, RDO mapping) | — |
| NFR-010 | Data Privacy | RA 10173 | W53 (breach response), W41 (DSAR handling), W17.2 (consent management), W271 (data subject access & deletion requests — DPA compliance, access/deletion fulfillment), W434 (NPC DPO & system registration) | W389 (DPIA lifecycle) |
| NFR-011 | Offline POS | ≥ 8 hours | W5G (offline POS recovery & reconciliation), W535 (offline capability scope — local operations, capability matrix, local data store, LAN sync, quarterly drill) | W49 (typhoon degraded mode), W533 (event streaming — offline event replay) |
| NFR-012 | Integration Capability | All touchpoints | W3–W7 (core integrations), W19 (3PL), W30 (banking), W257 (enterprise API & systems integration lifecycle management) | Data Volumes §3 |
| NFR-013 | Disaster Recovery | RPO ≤ 1h, RTO ≤ 4h | W55 (IT DR & failover), W382 (IT backup & recovery), W390 (IT service continuity), W465 (network-wide disaster recovery & BCP) | W49 (physical disaster BC) |
| NFR-014 | Data Migration | Legacy → ERP | Data Migration Mapping (data migration standards), W73 (data migration validation & parallel-run testing), W385 (data cleansing & migration operational lifecycle) | — |
| NFR-015 | Batch Processing Windows | Off-peak | Data Volumes §5 (batch windows), W9 (month-end close batch) | — |
| NFR-016 | Data Privacy Breach Response | RA 10173 | W53 (full breach response lifecycle) | W41 (DSAR), W271 (data subject access & deletion — breach-related access requests) |
| NFR-017 | LGU Business Permit Tracking | Per location | W54 (LGU permit renewal per location), W310 (address & geographic hierarchy master — LGU jurisdiction mapping per municipality/city), W430 (LGU business permit inspection), W437 (branch de-registration & permit cancellation), W446 (temporary permits for outdoor sales), W448 (LGU sanitary & health permit), W467 (specialized hardware permits) | W16 (new store initial permit) |
| NFR-018 | ESG & Sustainability Reporting | S | W192 (GHG tracking), W193 (Waste diversion) | W194 (CSR), W195 (Ethical audit) |
| NFR-019 | Advanced Fleet Optimization | S | W196 (Route optimization), W199 (Telematics), W249 (port container turn-around) | W197 (Driver performance), W198 (Fuel) |
| NFR-020 | AI & Innovation Framework | N | W200 (AI Personalization), W201 (RPA), W208 (AI Inventory Optimization) | W202 (Predictive maint), W203 (Computer vision) |
| NFR-021 | Smart Store Operations | S | W206 (Mobile POS), W212 (Smart Safe), W211 (3D Rendering), W214 (expedited transfer), W240 (DC facilities), W241 (HQ facilities), W247 (smart locker), W173 (store-level solar energy monitoring), W420 (AI shelf monitoring) | W205 (Employee purchase), W207 (CCTV audit) |
| NFR-022 | Local & Partner Governance | S | W209 (Barangay relationship), W213 (Contractor audit), W215 (home delivery returns), W216 (BIR CAS audit), W242 (3PL performance review) | W157 (E-waste), W210 (Dark store) |
| NFR-022a | BIR CAS Registration per Location | M | W54A (BIR Computerized Accounting System CAS registration per location, compliance documentation, renewal tracking) | W54 (LGU permits — related regulatory process), W16 (new store — initial CAS registration) |
| NFR-023 | Enterprise API & Integration Lifecycle Management | S | W257 (enterprise API & systems integration lifecycle — gateway, versioning, monitoring, health dashboard) | W19 (3PL integration — API consumer), W11 (BOPIS — API consumer), W30 (banking — API consumer) |
| NFR-024 | IT Asset Lifecycle Management | S | W131 (IT asset lifecycle management — hardware/software registry, procurement, deployment, retirement, license compliance), W369 (IT vendor SLA governance), W370 (SaaS subscription management), W371 (mobile device management), W373 (IT FinOps), W374 (IT project intake), W377 (domain/SSL management), W379 (service catalog fulfillment), W381 (knowledge management), W384 (ERP environment management), W386 (IT strategy development), W391 (software QA & testing), W392 (IT SLM), W394 (technical skills training), W395 (mobile app store management), W396 (ERP database archiving), W398 (IT innovation lifecycle) | W21 (capex — IT asset procurement), W48 (helpdesk — asset support), W378 (IT problem management) |
| NFR-025 | Employee IT Provisioning & Access Lifecycle | M | W152 (employee IT provisioning & access lifecycle — account creation on hire, role-based access, revocation on separation) | W15 (onboarding — provisioning trigger), W43 (separation — revocation trigger) |
| NFR-026 | Business Intelligence & Data Governance | S | W113 (business intelligence & data governance — BI platform, governed semantic layer, data quality monitoring) | W35 (management reporting — BI consumer), W31 (demand forecasting — data consumer) |
| NFR-027 | Omni-channel Customer Data Platform | S | W156 (customer data platform — unified profile, identity resolution, consent management) | W17 (loyalty — data source), W41 (complaint — data source), W258 (ticketing — data source) |

## R15. Installation & Value-Added Services (SRV)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| SRV-001 | Installation & Value-Added Services Management | S | W138 (home installation services management), W139 (tool & equipment rental operations), W148 (home design & consultancy services), W168 (custom paint mixing & tinting), W169 (lumber & board cutting services), W211 (in-store 3D kitchen/bathroom design rendering), W213 (installation service partner quality audit), W440 (power tool service center), W442 (site survey & measurement) | W5B (POS — service item selling), W33 (warranty — installation defect claims), W282 (subscription billing for recurring home services — recurring service revenue) |
| SRV-002 | DIY Workshop & In-Store Event Management | S | W147 (DIY workshop & in-store event management — scheduling, registration, material tracking, ROI) | W83 (marketing campaign — event promotion), W17 (loyalty — event attendance points) |

## R16. Wholesale & Reseller Operations (WSL)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| WSL-001 | Wholesale & Reseller Operations | S | W145 (wholesale reseller onboarding & credit management), W146 (bulk fulfillment & cross-docking for wholesale), W283 (B2B punchout catalog integration cXML — automated B2B ordering) | W24 (credit application — wholesale credit check), W8 (AR — wholesale invoicing) |

## R17. Corporate Governance, Legal & Strategy (GOV)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| GOV-001 | Corporate Governance & Legal Management | S | W124 (corporate secretarial & entity management), W125 (legal case & litigation management), W126 (IP portfolio management), W127 (annual strategic planning & OKRs), W128 (enterprise project management lifecycle), W186 (internal SOP & policy governance lifecycle), W230 (legal contract review & approval), W231 (management performance reporting QBR) | W14 (IC transactions — corporate secretarial support) |
| GOV-002 | Internal Audit & Risk Management | S | W120 (internal audit planning & risk assessment), W121 (operational audit execution store/DC/HQ), W122 (enterprise risk management review), W123 (fraud investigation protocol), W159 (anti-bribery & corruption monitoring & audit), W95 (external audit coordination & support), W331, W332, W333, W334, W335, W336, W337, W338, W339, W340, W341, W342, W343, W344, W345, W346, W347, W348, W349, W350, W351, W352, W353, W354, W355, W356, W357, W358, W359, W360, W361, W362, W363, W364, W365 (operational audit executions - ITGC, CCM, CAP tracking, vendor risk, capex, payroll, SOD, regulatory, cash, ESG, inventory, CAM, rebates, fleet, construction, ecommerce, tax, BCP, fixed assets, sourcing, B2B AML, IP, whistleblower, board governance, physical security, AI, treasury, MDM, insurance, media, workforce planning) | W37 (loss prevention — audit findings feed), W77 (BIR tax audit response — external audit) |
| GOV-003 | Real Estate & Lease Management | S | W116 (site selection & feasibility analysis), W117 (lease administration & renewal), W118 (rent & CAM payment processing), W119 (real property tax amillaramento management), W441 (staff housing & billeting management) | W16 (new store opening — site selection output), W45 (store closure — lease termination), W430 (LGU business permit & real property tax inspection) |
| GOV-004 | Health, Safety & Environment Management | S | W140 (OHS incident management), W141 (workplace safety inspection & audit), W187 (contractor & third-party on-site safety orientation), W330 (in-store emergency response protocol — evacuation, emergency services coordination, incident reporting), W436 (DOLE annual OHS reporting) | W82 (hazardous waste disposal — HSE coordination), W236, W237, W238 (hazmat — safety interface) |
| GOV-005 | Engineering & Construction Management | S | W223 (new store design & engineering standards), W224 (construction bidding & contractor selection), W225 (store construction management & supervision), W226 (store renovation & retrofitting CAPEX), W227 (commissioning & operational handover) | W16 (new store opening — construction handoff), W21 (capex — construction budget) |
| GOV-006 | Facility & Asset Maintenance (Non-Store) | S | W240 (DC facility & warehouse equipment maintenance), W241 (HQ office facility & executive asset maintenance), W242 (3PL & logistics partner performance review), W243 (POA & board resolution lifecycle) | W21 (capex — facility improvement), W39 (asset disposal — decommissioned equipment) |
| GOV-007 | Fleet Operations & Driver Management | S | W196 (route planning & dispatch optimization), W197 (driver performance & safety management), W198 (fuel management & consumption monitoring), W199 (fleet telematics & real-time tracking), W188 (fleet spare parts & preventive maintenance) | W52 (fleet management — fleet admin), W4 (replenishment — fleet scheduling), W277 (freight bill audit & payment reconciliation — fleet freight cost verification), W431 (LGU truck ban & route governance) |
| GOV-008 | Sustainability & Environmental Compliance | S | W192 (GHG emissions tracking), W193 (waste management & circular economy), W194 (social impact & community development CSR), W195 (sustainable sourcing & ethical vendor audit), W167 (store & DC recycling program — circular economy), W114 (sustainability & environmental compliance reporting — aggregate ESG reporting), W433 (DENR SMR/CMR compliance reporting), W443 (salvage & scrap material disposition), W444 (community solicitation & donation processing) | W82 (hazardous waste — environmental compliance), W157 (e-waste — circular economy) |
| GOV-009 | Innovation & Digital Transformation | S | W200 (AI-driven personalization & recommendation engine), W201 (RPA lifecycle), W202 (predictive maintenance for industrial assets), W203 (computer vision for inventory & planogram audit), W208 (retail analytics & AI-driven inventory optimization) | W113 (BI & data governance — AI data pipeline), W19 (ecommerce — personalization output) |
| GOV-010 | Marketing Campaign Management | S | W83 (campaign planning, execution & performance measurement), W104 (loyalty program financial governance), W134 (crisis communication & brand reputation), W135 (CSR program execution), W142 (social media & influencer management), W143 (PR & corporate communications), W149 (bank & credit card partnership management), W151 (CSR impact measurement & reporting), W153 (retail media network operations), W189 (referral program & brand ambassador management), W190 (in-house design & creative production management), W427 (DTI sales promotion permit monitoring) | W13 (promotions — campaign execution), W17 (loyalty — campaign targeting), W286 (RMN vendor billing & yield management — media campaign billing & revenue) |
| GOV-011 | Business Continuity & Disaster Preparedness | S | W158 (business continuity drill & disaster recovery testing) | W49 (natural disaster/typhoon BC — operational response), W55 (IT DR — technical response) |
| GOV-012 | Product Liability & Consumer Safety | S | W185 (product liability & consumer safety incident management — incident logging, regulatory notification, case management) | W29 (product recall — safety trigger), W82 (hazardous waste — disposal of unsafe products), W285 (public liability & customer incident claims management — in-store incident claims) |
| GOV-013 | Anti-Bribery & Corruption Monitoring | S | W159 (anti-bribery & corruption monitoring & audit — risk assessment, gift register, due diligence), W426 (annual COI & gift disclosure) | W79 (grievance & whistleblower — ABC reporting channel), W230 (contract review — ABC due diligence) |
| GOV-014 | Competitor Intelligence & Market Monitoring | S | W130 (competitor price intelligence gathering — price checks, market trend analysis, benchmarking), W329 (competitive price tactical response — rapid-response pricing to competitive threats) | W1 (assortment review — competitive positioning), W40 (price changes — market response) |
| GOV-015 | Private Label Development & Management | S | W129 (private label / in-house brand development — development lifecycle, supplier qualification, quality testing) | W1 (assortment — PL assortment decisions), W160 (factory audit — PL factory compliance) |
| GOV-016 | Employee Training & Development | S | W51 (employee training & skills development — needs assessment, program scheduling, attendance, certification) | W15 (onboarding — initial training), W140 (OHS — safety training) |
| GOV-017 | Employee Performance & Career Development | S | W72 (employee performance management — goal setting, reviews, competency framework), W178 (employee succession & internal mobility), W179 (management trainee cadetship program), W269 (vendor promodizer & third-party staff management — performance tracking, badge issuance, compliance), W429 (vendor promodizer incentive management), W449 (promodizer labor compliance & DOLE 174 governance) | W10 (payroll — performance bonus processing), W34 (scheduling — performance-linked shifts) |
| GOV-018 | Store Performance Management | S | W67 (monthly store performance review — KPIs, manager scorecard, ranking), W96 (store renovation & remodel project), W86 (planogram compliance & store layout verification) | W35 (management reporting — store metrics), W67 (store review — performance data) |
| GOV-019 | Price Compliance & Energy Management (Store) | S | W69 (price compliance audit), W111 (store energy & utility consumption management), W173 (store-level solar energy monitoring), W181 (store-level price tag printing & verification) | W40 (price changes — compliance source), W35 (reporting — energy cost reporting) |
| GOV-020 | Store-Level Security & Loss Prevention | S | W71 (store physical security & access control), W171 (store physical security & yard patrol routine), W182 (gift/home registry lifecycle), W177 (vending & concessionaire management), W5505–W5507 (concession item catalog/barcode/label governance, concessionaire self-service price change & propagation, concession service-fee billing), W466 (LPAP operations) | W37 (loss prevention — security data feed), W5A (store opening — security check), W667/W69 (price verification & audit incl. concession items) |
| GOV-021 | Store-Level Reverse Logistics | S | W176 (store-to-DC reverse logistics consolidation), W109 (store-level inventory receiving & putaway) | W22B (store-to-DC return — damaged/excess), W91 (damaged goods — return feed) |
| GOV-022 | DC Inbound & Outbound Operations | S | W3C (DC inbound delivery scheduling), W106 (DC outbound dispatch & load planning), W221 (cross-docking operations for fast-moving bulky items), W222 (DC container yard & chassis management), W188 (fleet spare parts & PM) | W3 (DC receiving — inbound execution), W4 (store replenishment — outbound execution) |
| GOV-023 | Customer Experience Management | S | W84 (customer account reactivation), W87 (customer feedback-to-action loop), W112 (trade counter / pro desk operations), W258 (omni-channel customer ticketing & support management) | W41 (complaint resolution — feedback source), W156 (CDP — unified customer view) |
| GOV-024 | Employee Financial Benefits Management | S | W175 (employee gratuity & retirement fund management RA 7641) | W10 (payroll — gratuity accrual posting), W43 (separation — retirement eligibility check) |
| GOV-025 | Sales Commission Management | S | W228 (sales commission calculation for trade & project sales — plan configuration, accrual, GL posting) | W10 (payroll — commission payment), W162 (project quotation — commission basis) |
| GOV-026 | Supply Chain Network Optimization | S | W133 (S&OP cycle), W144 (international logistics & import operations), W183 (supply chain network optimization review), W191 (global supply chain incoterm & marine insurance tracking) | W31 (demand forecasting — S&OP input), W250 (control tower — visibility) |
| GOV-027 | 3PL & Delivery Partner Management | S | W62B (3PL/delivery partner onboarding & offboarding), W242 (3PL & logistics partner performance review) | W19 (home delivery — 3PL execution), W66 (inter-island logistics — 3PL partner) |
| GOV-028 | Sample & Demo Inventory Management | S | W97 (sample & demo inventory management — separate tracking, issuance, disposition) | W1 (assortment — sample allocation), W46 (kit assembly — sample kit) |
| GOV-029 | Markdown & Clearance Pricing Management | S | W93 (markdown & clearance pricing execution — trigger rules, approval, budget tracking, performance) | W13 (promotions — clearance promo), W220 (SLOB — markdown trigger) |
| GOV-030 | DTI Price Freeze / Emergency Price Control Implementation | M | W468 (DTI price freeze implementation — trigger detection, SKU/location identification, prevailing price computation, POS/ecommerce/marketplace freeze activation, compliance monitoring, documentation, freeze lift) | W49 (typhoon BC — often coincides with price freeze), W428 (disaster relief — relief pricing separate from freeze), W13 (promotions — suspended during freeze), W40 (price changes — blocked during freeze), W181 (shelf labels — reprint for frozen prices) |
| GOV-031 | Customer Complaint DTI Escalation & Consumer Adjudication | S | W469 (DTI complaint escalation — case logging, internal investigation, response preparation, mediation attendance, adjudication management, corrective action, pattern tracking) | W41 (complaint resolution — internal complaint source), W101 (refund processing — settlement execution), W125 (legal case — external counsel for adjudication), W69 (price compliance — evidence source), W262 (promotional setup — evidence source) |
| GOV-032 | Store-Level Rotational Brownout / Power Outage Management | S | W470 (rotational brownout protocol — schedule monitoring, pre-outage preparation, load priority, generator management, sensitive goods protection, extended outage escalation, power restoration, reconciliation) | W5G (offline POS — transaction queue during outage), W47 (facility maintenance — generator PM), W111 (utility management — fuel cost tracking), W5E (opening delay — if outage before opening), W173 (solar — solar continues during daytime) |
| GOV-033 | Store-Level Security Incident & Police/Barangay Reporting | S | W471 (security incident reporting — classification, police blotter filing, barangay blotter, evidence preservation, insurance claim initiation, LP handoff, employee incidents) | W37 (LP — investigation handoff), W59 (insurance — claim initiation), W71 (physical security — CCTV evidence), W92 (inventory adjustment — theft write-off), W140 (OHS — employee injury), W285 (public liability — customer injury during incident) |
| GOV-034 | Fire Safety Inspection Compliance | M | W476 (LGU / BFP Fire Safety Inspection Certificate (FSIC) Management — pre-inspection testing, fire drills, document compilation, application, inspection, re-inspection, posting) | W54 (LGU permits — business permit dependency), W59 (insurance — GL liability compliance), W47 (store maintenance — systems PM), W240 (DC maintenance — equipment PM) |
| GOV-035 | DENR Air/Water Permit Compliance | M | W477 (DENR Permit to Operate (PTO) & Wastewater Discharge Permit (WDP) Compliance — testing coordination, document compilation, portal submission, payment, inspection, database updates) | W433 (DENR SMR/CMR — permit data feed), W47 (store maintenance — STP servicing), W240 (DC maintenance — genset servicing), W7 (AP — permit fees) |
| GOV-036 | FDA License to Operate (LTO) for Household Hazardous Substances (HHS) | M | W479 (FDA License to Operate for HHS Compliance — credentials verification, compliance check, application, inspection, LTO issuance, product registration tracking) | W36 (vendor onboarding — verify vendor FDA status), W50 (PIM — store FDA registration number per product), W252 (item master — FDA flag), W82 (hazmat waste — disposal of expired/recalled chemicals) |
| GOV-037 | CAAP Height Clearance Permit Compliance | M | W480 (CAAP Height Clearance Permit Compliance — height survey, coordinate capture, document package compilation, clearance application, inspection, permit log) | W116 (site selection — feasibility scan), W223 (store design — height guidelines), W225 (store construction — supervision), W54 (LGU permits — building permit clearance check) |
| GOV-038 | SEC Reportorial Requirements Compliance | M | W481 (SEC reportorial compliance — filing calendar, data gathering, document preparation, review/approval, eFAST/SENS submission, confirmation/archiving, deficiency resolution) | W124 (corporate secretarial — entity management data source), W9B (year-end close — AFS data source), W95/W351 (external audit — AFS dependency), W482 (ASHM — GIS filing trigger), W255 (document management — filing archive) |
| GOV-039 | Annual Stockholders' Meeting Management | M | W482 (ASHM management — meeting planning, notice/agenda, financial presentation, pre-meeting coordination, meeting execution, minutes certification, post-meeting SEC filings, action follow-up) | W481 (SEC filings — GIS/MC 28 triggered by ASHM), W327 (dividend — dividend declaration at ASHM), W351 (external audit — auditor appointment at ASHM), W124 (corporate secretarial — entity data), W9B (year-end close — financial statement presentation) |
| GOV-040 | Labor Union & Collective Bargaining Management | S | W493 (Labor union & CBA management — prevention/engagement, organizing activity response, certification election, CBA negotiation, CBA registration/implementation, CBA administration, grievance handling, strike contingency) | W10 (payroll — CBA wage/benefit implementation), W34 (shift scheduling — CBA work rule constraints), W72 (performance — CBA disciplinary procedures), W79 (grievance — non-union grievance channel), W43 (separation — CBA termination provisions), W186 (SOP governance — CBA policy alignment) |
| GOV-041 | Employee Wellness & Mental Health Program | S | W494 (Employee wellness program — annual planning, EAP operations, physical health programs, mental health awareness, financial wellness, crisis support, effectiveness measurement) | W10 (payroll — wellness benefit administration), W15 (onboarding — wellness orientation), W43 (separation — exit wellness referral), W51 (training — wellness workshop delivery), W140 (OHS — physical health coordination), W471 (security incidents — trauma support), W251 (statutory benefits — health education) |
| GOV-042 | PWD Accessibility Compliance & Store Facilities Audit | M | W497 (PWD accessibility compliance — standards checklist, annual store audit, new store design review, minor/major remediation, customer complaint response, staff training, regulatory inspection coordination) | W223 (store design — accessibility in design standards), W227 (commissioning — accessibility verification), W47 (facility maintenance — remediation execution), W96 (store renovation — major accessibility capital projects), W170 (PWD discount — complementary compliance), W41 (complaints — PWD accessibility complaints), W469 (DTI escalation — accessibility complaint escalation) |
| GOV-045 | Store-Level Fire Safety Equipment Daily Inspection | M | W758 (fire safety daily inspection — equipment checklist, pressure verification, exit light testing, expiry tracking, BFP compliance) | W476 (FSIC — annual inspection), W47 (facility maintenance — repair work orders), W141 (safety inspection — monthly integration), W582 (fire drill — drill coordination) |
| GOV-046 | Store-Level Hazmat Customer Advisory | M | W759 (hazmat customer advisory — GHS classification, safety briefing, SDS distribution, alternative suggestion, quantity flagging, acknowledgment archival) | W252 (item master — GHS attributes), W698 (SDS lifecycle — SDS management), W185 (product liability — defense archive), W479 (FDA LTO — HHS compliance), W467 (FPA permits — regulated products) |

## R18. Additional Cross-Functional Requirements

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| CRM-015 | Call Center Daily Operations & Queue Management | S | W259 (call center daily operations — IVR, queue routing, agent monitoring, SLA tracking) | W258 (ticketing — escalation destination), W156 (CDP — customer 360 in agent console), W34 (scheduling — agent shift scheduling), W65 (CSAT/NPS — post-interaction survey) |
| FIN-031 | BIR eFPS Filing & Electronic Payment Submission | M | W260 (BIR eFPS filing — return generation, eFPS submission, PRN, AAB payment), W5508 (fringe benefits tax — quarterly 1605 filing, gross-up computation, e-Payment linkage) | W9A (month-end close — tax provision posting), W90 (monthly tax filing — high-level process), W216 (BIR CAS audit — filing archive), W239 (customs duty — import tax data source), W217 (SC/PWD reporting — VAT-exemption data source) |
| FIN-032 | E-Wallet & Digital Payment Settlement Reconciliation | M | W261 (e-wallet settlement reconciliation — GCash, Maya, GrabPay, ShopeePay matching, MDR verification, chargeback management), W309 (bank & banking partner master — e-wallet partner configuration, MDR rate, settlement frequency) | W99 (payment settlement reconciliation — card settlement), W89 (bank reconciliation — settlement bank posting), W30 (treasury — cash position impact), W5F (store EOD — e-wallet Z-report), W149 (bank partnership — promo MDR terms), W267 (ecommerce digital payment reconciliation & dispute handling) |
| MER-001 | Store Promotional Setup & Visual Merchandising Execution | S | W262 (store promotional setup — planogram distribution, stock pulling, display construction, signage placement, compliance photo tracking), W445 (display & demo infrastructure maintenance) | W13 (promotions — pricing source), W93 (markdown — clearance disposition), W181 (price tag printing — signage), W190 (creative production — display assets) |
| CRM-016 | Loyalty Member Enrollment & Onboarding Journey | S | W263 (loyalty enrollment — multi-channel capture, dedup, consent, digital card, welcome sequence, conversion tracking) | W17 (loyalty operations — account creation), W253 (customer dedup — enrollment dedup engine), W156 (CDP — unified profile), W259 (call center — enrollment via phone) |
| MER-002 | Seasonal Merchandise Transition & Display Rotation | S | W264 (seasonal transition — planning, markdown trigger, setup brief, display build/teardown, in-season monitoring, post-season review) | W32 (seasonal buy planning — seasonal PO), W31 (demand forecasting — seasonal forecast), W13 (promotions — seasonal pricing), W93 (markdown — seasonal clearance), W1 (assortment review — seasonal assortment) |
| NFR-028 | POS Terminal Hardware Maintenance & Peripheral Management | S | W265 (POS hardware maintenance — incident ticketing, remote diagnosis, spare swap, PM scheduling, warranty/RMA tracking) | W48 (helpdesk — incident ticketing), W131 (IT asset lifecycle — hardware register), W39 (asset disposal — decommissioned peripherals), W5G (offline POS — UPS battery PM) |
| NFR-029 | ERP Patch, Upgrade & Release Management | M | W495 (ERP patch, upgrade & release management — release notification/impact assessment, sandbox testing, customization/integration compatibility, Go/No-Go decision, pre-deployment preparation, production deployment, post-deployment verification, 7-day monitoring, annual major upgrade planning) | W132 (change management — change request/approval tracking), W384 (environment management — sandbox), W382 (backup & recovery — pre-deployment backup/rollback), W380 (alert/event management — post-deployment monitoring), W48 (helpdesk — post-deployment issue tracking), W5G (offline POS — downtime contingency), W257 (API management — integration compatibility), W367 (security — critical patch SLA), W376 (capacity planning — performance verification) |
| COM-001 | DOLE Drug-Free Workplace Program Compliance | M | W483 (DOLE drug-free workplace — policy maintenance, pre-employment testing, annual random testing plan, testing execution, result processing, confirmed positive handling, rehabilitation/reintegration, awareness/education, reasonable suspicion testing, annual compliance report) | W15 (onboarding — pre-employment testing trigger), W51 (training — awareness program delivery), W43 (separation — termination for confirmed positive), W140 (OHS — post-accident testing trigger), W10 (payroll — leave of absence during rehabilitation), W493 (labor union — union escalation risk for testing disputes) |
| COM-002 | Pandemic/Epidemic Business Response Protocol | S | W484 (Pandemic response — monitoring/early warning, PRT activation, employee health measures, store ops adjustment, supply chain resilience, financial contingency, communications, IT continuity, stand-down/recovery, annual plan review) | W49 (typhoon BC — weather-driven BC complement), W158 (BC drill — pandemic tabletop exercise), W465 (network DR — IT disaster recovery), W140 (OHS — health incident interface), W172 (PPE — pandemic PPE), W209 (barangay — community health coordination), W5G (offline POS — degraded connectivity contingency), W111 (utility — generator fuel for essential stores), W19 (ecommerce — channel shift surge capacity) |
| PUR-025 | Supplier Financial Health & Credit Risk Monitoring | S | W491 (Supplier financial health monitoring — vendor risk tiering, Tier 1 full financial review, Tier 2 questionnaire, continuous monitoring signals, watchlist management, vendor failure contingency activation, annual report) | W44 (vendor scorecard — performance data correlation), W36 (vendor onboarding — initial financial assessment), W56 (backorder — supply disruption signal), W60 (emergency procurement — contingency sourcing), W312 (planning parameters — safety stock override for watchlist vendors), W287 (vendor master — risk tiering attribute) |
| SCP-008 | Temperature-Controlled & Sensitive Goods Logistics | S | W492 (Temperature-controlled logistics — sensitive goods classification, DC storage zone management, inbound quality check, outbound transport planning, store receiving/storage, seasonal alert protocol, quality incident investigation, annual storage compliance review) | W3 (DC receiving — temperature-sensitive goods check), W106 (dispatch planning — temperature-aware routing), W109 (store receiving — sensitive goods handling), W236 (hazmat storage — intersection with chemical storage), W240 (DC maintenance — HVAC/cooling system PM), W252 (item master — storage requirement attribute), W297 (warehouse location — climate zone mapping), W298 (product attributes — temperature/humidity sensitivity) |
| SCP-009 | Supplier Risk Assessment & Supply Disruption Contingency Planning | M | W558 (Supplier risk -- annual 6-dimension assessment, 1-5 scoring, Tier A/B/C classification, mandatory contingency for Tier A, disruption response protocol with impact tiers, quarterly dashboard) | SCP-007 (purchase recommendation -- alternatives), PUR-003 (vendor management -- vendor data), PUR-004 (import POs -- import risk), W44 (vendor scorecard -- quality/delivery), W491 (financial health -- financial data), W60 (emergency procurement -- disruption response), W56 (backorder -- customer impact), W31 (forecasting -- demand data), W312 (parameters -- safety stock override), W105 (allocation -- shortage allocation), W279 (substitution -- substitutes), W571 (communication -- notification) |
| AUD-001 | Organized Retail Crime (ORC) Investigation & Task Force | S | W490 (ORC investigation — pattern detection, case file creation, cross-store investigation, evidence compilation, law enforcement coordination, monthly task force review, industry coordination, case closure/lessons learned) | W37 (loss prevention — LP data source), W466 (LPAP — individual incident data source), W248 (inventory variance — shrinkage correlation), W71 (CCTV — multi-store footage), W92 (inventory adjustment — theft write-off), W43 (separation — ORC-related termination), W140 (OHS — injury during incident), W493 (labor union — union coordination during investigation) |
| REG-001 | BIR Branch Registration & RDO Transfer Management | M | W485 (BIR branch registration — requirements gathering, RDO submission, COR issuance, books/receipt registration, system configuration, RDO transfer process, compliance tracking/calendar, annual compliance verification) | W16 (new store — registration trigger), W45 (store relocation — RDO transfer trigger), W54A (CAS registration — complementary BIR process), W54 (LGU permits — business permit dependency), W254 (location master — RDO code/registration status), W293 (tax master — tax code configuration per RDO), W310 (address master — RDO-to-municipality mapping), W260 (eFPS — location enrollment), W473 (EIS — location enrollment) |
| MKT-001 | Customer Loyalty Fraud Detection & Prevention | S | W496 (Loyalty fraud detection — automated scanning, case triage, investigation, fraud confirmation/action, system rule enhancement, monthly fraud report) | W17 (loyalty operations — transaction data source), W104 (loyalty financial governance — liability impact), W156 (CDP — account device/IP tracking), W205 (employee purchases — employee account monitoring), W258 (customer ticketing — account takeover member communication), W263 (enrollment — fake account detection at enrollment), W466 (LPAP — employee fraud escalation), W132 (change management — rule update deployment) |
| MKT-002 | Marketing Campaign ROI & Attribution Analysis | S | W565 (Marketing ROI -- spend data collection, sales lift analysis vs. baseline, multi-touch attribution modeling, channel ROI calculation, campaign ROI with COGS impact, CLV assessment, monthly portfolio report, quarterly executive review, annual benchmark) | CRM-007 (campaign integration -- campaign data), W83 (campaign management -- lifecycle data), W104 (loyalty governance -- loyalty ROI), W286 (RMN billing -- media spend), W149 (bank partnership -- co-branded ROI), W156 (CDP -- acquisition data), W539 (coupon processing -- redemption), W93 (markdown -- discount cost), W57 (promo stock -- inventory impact), W26 (budget -- optimization feed) |
| FIN-041 | Vendor Advance Payment & Prepayment Management | M | W498 (Vendor advance payment — request linked to PO, tiered approval, advance execution, advance aging monitoring, automatic settlement at GR, advance overpayment reconciliation) | W2 (PO cycle — advance source PO), W2B (import PO — primary use case for import advances), W232 (LC lifecycle — alternative to LC for trusted vendors), W7 (AP processing — advance settlement integration), W320 (electronic banking — bank transfer execution), W491 (supplier financial health — vendor risk assessment for advance approval) |
| FIN-042 | BIR Percentage Tax Computation & Payment | S | W499 (BIR percentage tax — revenue stream tax classification, quarterly computation, Form 2551Q generation, eFPS submission, VAT threshold monitoring) | W260 (eFPS filing — electronic submission), W90 (monthly tax filing — high-level tax process), W293 (tax master — percentage tax rate configuration), W9A (month-end close — tax provision posting) |
| FIN-043 | AP Payment Run & Batch Processing Execution | M | W556 (AP payment run execution -- payment proposal generation, discount optimization, cash position verification, tiered approval, multi-bank PESONet file generation, check printing, payment posting, stale-dated check escheatment) | W7 (AP invoice -- approved invoice source), W7C (non-PO -- non-PO payment inclusion), W7D (AP statement -- payment reconciliation), W30 (treasury -- cash position), W89 (bank recon -- payment confirmation), W320 (e-banking -- secure transmission), W317 (bank account -- signatory management), W324 (supply chain finance -- early payment discount), W295 (payment terms -- net due calculation) |
| FIN-044 | Customer Credit Monitoring & Automated Alert Management | M | W572 (Credit monitoring & alerts -- continuous scoring engine, tiered Amber/Red alerts, Credit Analyst daily review, recommended actions with Credit Manager approval, customer outreach, monthly portfolio review, quarterly policy review, annual model calibration) | W24 (credit application -- initial assessment), W8 (AR processing -- transaction data), W108 (credit collection -- escalation partner), W229 (credit limit exception -- exception handling), W328 (credit periodic review -- annual review), W1381 (bounced check -- NSF signal), W253 (customer master -- credit action update), W81 (bad debt -- monitoring feed) |
| INV-021 | Transfer Order In-Transit Damage Claim & Resolution | M | W500 (Transfer order damage claim — damage documentation with photos, severity classification, responsible party identification, carrier claim filing, insurance claim initiation, inventory adjustment, carrier chargeback, damage trend analysis) | W4 (store replenishment — DC→Store damage source), W22 (transfers — store-to-store/inter-DC damage source), W92 (inventory adjustment — damage write-off), W59 (insurance — claim for insured shipments), W7 (AP — carrier chargeback/debit memo), W62B (3PL onboarding — carrier SLA terms), W242 (3PL performance — damage rate in vendor review) |
| INV-022 | Inventory Count Reconciliation & Variance Root Cause Analysis | S | W514 (Inventory count reconciliation — automated variance flagging by ABC threshold, root cause categorization, variance investigation case, corrective action recommendation, quarterly trend analysis, LP escalation) | W6 (cycle counting — variance source), W42 (physical inventory — variance source), W248 (LP investigation — theft-related variance escalation), W3 (DC receiving — receiving error tracing), W18 (DSD receiving — receiving error tracing), W88 (RTV — vendor short shipment claim), W92 (inventory adjustment — approved adjustment posting) |
| PUR-026 | Vendor-Funded Promotional Activity & Co-op Advertising Management | S | W513 (Vendor-funded promotional activity — fund agreement setup, activity logging, proof-of-execution, vendor claim tracking, AP credit memo, fund utilization dashboard, quarterly ROI reporting, annual reconciliation) | W83 (campaign planning — promotional activity source), W155 (JBP — annual fund allocation), W262 (store promotional setup — in-store execution), W190 (creative production — content source), W7 (AP — reimbursement credit memo), W27 (vendor rebate — related vendor credit mechanism) |
| ECOM-017 | Ecommerce Product Return Inspection, Grading & Disposition | S | W509 (Ecommerce return inspection — return barcode scan, physical inspection against grading criteria, Grade A restock, Grade B open-box listing, Grade C disposition/RTV/repair/write-off, grading dashboard, return-to-saleable conversion rate) | W12B (online returns — return order source), W215 (home delivery returns — logistics source), W91 (damaged goods — Grade C disposition), W88 (RTV — vendor-attributable defect), W440 (service center — repairable items), W110 (supplier CAPA — vendor defect rate), W44 (vendor scorecard — return grading data) |
| ECOM-018 | Ecommerce Product Review & Rating Management | S | W510 (Ecommerce product review — verified purchase validation, automated moderation, negative review escalation, vendor response, review analytics, low-rated SKU alerting, quarterly vendor feedback report) | W50 (PIM — review display on product pages), W258 (customer ticketing — negative review escalation), W41 (complaint resolution — review-triggered complaint), W87 (feedback-to-action — review sentiment analysis), W110 (supplier CAPA — quality issue from reviews), W155 (JBP — vendor feedback in JBP) |
| ECOM-019 | E-Commerce Abandoned Cart Recovery & Retargeting | S | W557 (Abandoned cart recovery -- 3-touch automated sequence at 1hr/6hr/24hr, segment-specific incentives, RA 10173 consent check, Facebook/Google retargeting, conversion attribution, weekly root cause analysis, monthly dashboard, quarterly A/B testing) | ECOM-006 (payment gateway -- abandonment point), CRM-007 (campaign integration -- retargeting), W83 (campaign -- ad activation), W156 (CDP -- segmentation), W50 (PIM -- product content), NFR-010 (data privacy -- consent), POS-045 (unified orders -- fulfillment) |
| ECOM-020 | E-Commerce SEO & Digital Merchandising Management | S | W563 (SEO management -- weekly keyword review, product page audit 50/week, on-site search analysis, content gap analysis, category optimization, local SEO 200 stores, technical SEO coordination, monthly report, quarterly strategy, annual full crawl) | ECOM-009 (catalog sync -- catalog data), MDM-002 (item attributes -- spec data), MDM-025 (digital assets -- image optimization), W50 (PIM -- content source), W316 (digital asset -- asset management), W564 (NPI rollout -- new content), W254 (location master -- local SEO), W264 (seasonal -- seasonal content) |
| ECOM-021 | E-Commerce Flash Sale & Limited-Time Offer Operations | S | W568 (Flash sale ops -- T-14 planning, T-7 inventory pre-reservation, T-5 pricing with DTI check, T-3 infrastructure, T-2 staging, real-time monitoring, inventory emergency protocol, post-sale fulfillment surge, T+3 reconciliation, T+7 performance report) | ECOM-010 (promo/coupon -- flash pricing), ECOM-001 (inventory sync -- monitoring), W13 (promotions -- pricing engine), W57 (promo stock -- pre-reservation), W105 (allocation -- ATP exclusion), W98 (order exceptions -- oversell), W266 (fraud -- screening), W267 (payment recon -- reconciliation), W376 (capacity -- infrastructure), W468 (price freeze -- compliance) |
| ECOM-022 | E-Commerce New Product Launch & Go-Live Process | S | W569 (E-com product launch -- product page creation, 5+ images per SKU, SEO metadata optimization, pricing cross-check, inventory pre-allocation, QA staging review, post-launch indexing check, T+7 performance check) | ECOM-009 (catalog sync -- publication), MDM-002 (attributes -- spec data), MDM-025 (digital assets -- media), W50 (PIM -- content repository), W252 (item master -- SKU source), W316 (digital asset -- governance), W289 (pricing master -- verification), W563 (SEO -- optimization), W105 (allocation -- inventory) |
| HR-018 | Employee Cross-Entity & Cross-Location Transfer Processing | M | W511 (Employee transfer — request initiation, eligibility check, transfer type classification, position/salary review, payroll entity change, benefits portability, IT access update, employee master update, 30-day check-in) | W43 (separation — transfer vs. separation routing), W10 (payroll — entity change and proration), W152 (IT provisioning — access update), W254 (location master — location change), W292 (employee master — data update), W251 (statutory benefits — continuity verification), W26 (budget — cost center transfer) |
| HR-019 | Store-Level Health & Safety Committee Operations | S | W512 (Safety committee — monthly meeting scheduling, agenda preparation, incident review, safety inspection findings review, action item tracking, quarterly effectiveness review, annual composition review per DOLE DO 198) | W140 (OHS incidents — incident data for committee review), W141 (safety inspection — findings for committee review), W436 (DOLE OHS reporting — committee documentation source), W51 (training — safety training plan development), W501 (first aid — first aider roster management) |
| HR-020 | Seasonal & Temporary Staffing Process | S | W555 (Seasonal staffing -- DOLE 174 classification, abbreviated recruitment 1-round interview, pre-employment registration/re-activation, 1-day onboarding, payroll setup, mid-season check, abbreviated offboarding, returning worker database) | HR-001 (payroll -- seasonal setup), HR-009 (recruitment -- abbreviated process), HR-005 (attendance -- biometric enrollment), W15 (onboarding -- base process), W34 (scheduling -- seasonal shifts), W43 (separation -- abbreviated offboarding), W10 (payroll -- seasonal run), W172 (PPE -- seasonal issuance) |
| HR-021 | Employee Attendance Exception Management | M | W561 (Attendance exceptions -- daily exception report, severity prioritization, biometric failure manual entry, late deduction auto-calc, unfiled absence classification, undertime deduction, missing punch self-service, unauthorized overtime verification, mass exception blanket directive, payroll update) | HR-005 (time & attendance -- biometric source), HR-010 (overtime -- exception verification), HR-011 (holiday pay -- holiday exception), W10 (payroll -- corrected data), W34 (scheduling -- schedule source), W48 (helpdesk -- biometric repair) |
| HR-022 | Employee Cross-Training & Skill Matrix Management | S | W567 (Cross-training & skill matrix -- multi-department competency matrix, initial assessment, gap analysis, quarterly training plan, shadow sessions, practical assessment, skill matrix update, cross-coverage heatmap, scheduling integration, quarterly re-assessment, succession pipeline) | W51 (training -- delivery), W72 (performance -- performance feed), W34 (scheduling -- cross-trained scheduling), W178 (succession -- pipeline feed), W179 (management trainee -- candidate identification) |
| CRM-019 | Customer Account Dormancy Identification & Deactivation | S | W560 (Account dormancy -- monthly scan, 3-tier classification, automated re-engagement for Early, data quality review for Extended, quarterly deactivation batch, B2B credit zero, loyalty points freeze, quarterly analytics) | CRM-002 (customer master -- data update), CRM-003 (trade account -- B2B deactivation), CRM-008 (credit application -- credit limit zero), W84 (reactivation -- reactivation path), W24 (credit -- status review), W156 (CDP -- data quality), W328 (credit review -- B2B partner), W108 (collection -- balance escalation), W253 (customer master -- status update) |
| CRM-020 | Mystery Shopping Program & CX Compliance Audit | S | W566 (Mystery shopping -- 400-600 visits/month, 4-category evaluation with weights, 4 shopper profiles, mobile app evaluation, agency quality review, < 70% remediation, Regional Manager integration, quarterly review, annual ROI correlation) | CRM-011 (feedback-to-action -- feedback data), W65 (CSAT/NPS -- correlation), W67 (store performance -- integration), W522 (cashier audit -- cashier data), W86 (planogram -- standards data), W503 (pest control -- cleanliness), W170 (SC/PWD discount -- compliance test), W518 (cashier training -- need identification) |
| CRM-021 | Loyalty Points Expiry Management & Annual Liability Cleanup | S | W570 (Points expiry -- T-60 config, T-30 notification sequence, recovery campaign, CS briefing, batch execution, PFRS 15 journal entry, post-expiry notification, re-enrollment incentive, reconciliation, quarterly adjustment, annual audit report) | CRM-001 (loyalty engine -- execution), FIN-039 (revenue recognition -- accounting), W104 (loyalty governance -- liability review), W313 (loyalty rule master -- config), W551 (enrollment -- re-enrollment), W550 (points as tender -- redemption data), W253 (customer master -- member data), W351 (external audit -- audit data) |
| GOV-043 | Store-Level First Aid & Medical Emergency Response | M | W501 (Store first aid — medical emergency response protocol, certified first aider roster, first aid kit inventory and quarterly audit, AED placement and maintenance, incident logging, monthly trend analysis) | W140 (OHS incidents — medical incident interface), W330 (emergency response — emergency coordination), W285 (public liability — customer injury claims), W436 (DOLE OHS reporting — first aid incident data), W51 (training — first aider certification), W136 (indirect procurement — kit restocking) |
| GOV-044 | Store-Level Non-Hazardous Waste Management | S | W502 (Non-hazardous waste — waste stream segregation, cardboard baling and recycling revenue, hauler vendor management, monthly volume tracking, quarterly vendor review, annual waste reduction targets) | W167 (recycling program — recycling stream integration), W82 (hazardous waste — separate hazmat stream), W193 (circular economy — waste diversion reporting), W192 (GHG tracking — waste-related emissions), W62B (vendor onboarding — waste hauler vendor), W489 (store budget — waste cost allocation) |
| GOV-047 | DOLE Labor Inspection Response Protocol | M | W505 (DOLE inspection — inspection type classification, response team assembly, document preparation, inspection attendance, findings documentation, corrective action plan, re-inspection preparation, annual inspection history) | W10 (payroll — payroll records for inspection), W251 (statutory benefits — remittance records), W436 (DOLE OHS reporting — safety committee documentation), W140 (OHS incidents — incident records), W34 (shift scheduling — working hours records), W512 (safety committee — committee minutes), W186 (SOP governance — policy documentation) |
| GOV-048 | Unified Regulatory Compliance Calendar & Dashboard | M | W506 (Unified compliance calendar — multi-body obligation tracking, automated deadline alerting, per-entity/per-location status dashboard, proof-of-submission attachment, weekly compliance review, monthly status report, quarterly risk review, annual compliance report) | W54 (LGU permits — business permit obligations), W54A (CAS registration — BIR CAS obligations), W77 (BIR audit — tax audit obligations), W90 (tax filing — monthly BIR filings), W260 (eFPS — electronic filing), W433 (DENR SMR/CMR — environmental obligations), W436 (DOLE OHS — labor compliance), W476 (FSIC — fire safety), W477 (DENR PTO — air/water permits), W479 (FDA LTO — household hazardous substances), W480 (CAAP — height clearance), W481 (SEC filings — reportorial requirements), W485 (BIR branch registration — registration obligations) |
| MER-003 | Loyalty Tier Re-evaluation & Migration Processing | S | W515 (Loyalty tier re-evaluation — quarterly batch 12-month rolling spend calculation, borderline case grace period, deferred revenue adjustment, upgrade/downgrade notifications, member profile update, migration analytics, annual threshold review) | W17 (loyalty operations — tier status consumer), W104 (loyalty financial governance — liability impact), W313 (loyalty rule master — tier threshold configuration), W5B (POS — tier recognition at checkout), W156 (CDP — tier-based segmentation), W253 (customer master — tier status on profile), W263 (enrollment — new member initial tier) |
| MER-004 | New Product Introduction (NPI) & Full Store Rollout | S | W564 (NPI full rollout -- pilot review, vendor negotiation, item master creation, pricing config, national PO, planogram integration, launch materials, store communication, setup execution T-7, staff training, simultaneous launch, T+7 monitoring, T+30 review) | MER-001 (assortment -- update), W64 (pilot -- results data), W1 (assortment review -- slot), W13 (promotions -- launch promos), W252 (item master -- creation), W289 (pricing -- config), W312 (parameters -- initial), W314 (planogram -- integration), W315 (lifecycle -- status), W316 (digital asset -- content), W262 (promo setup -- display), W181 (label -- printing), W571 (communication -- NPI package), W523 (POS setup -- config), W51 (training -- staff), W83 (campaign -- launch) |
| POS-049 | POS Card Terminal & Acquirer Settlement Operations | M | W537 (Card terminal & acquirer settlement — EMV/contactless processing, shift-end batch close, batch total verification, settlement exception handling, PIN pad troubleshooting, PCI-DSS firmware audit) | W5B (checkout — card tender), W5F (EOD — card settlement), W517 (shift handover — batch close), W99 (payment settlement — next-day reconciliation), W265 (POS hardware — PIN pad maintenance), W48 (helpdesk — terminal issues), W5E (system-down — cash-only fallback) |
| POS-050 | POS Real-Time Loss Prevention Exception Monitoring & Alert Response | M | W538 (Real-time LP exception monitoring — anomaly detection, severity classification, alert triage, store response, weekly analytics, ML model tuning, cross-store serial fraud) | W37 (LP investigation — confirmed cases), W522 (daily review — medium alerts), W281 (SCO exceptions — pass-through detection), W248 (inventory variance — shrinkage correlation), W272 (cashier over/short — drawer anomaly), W533 (event stream — detection data source) |
| POS-051 | POS Promotional Coupon, Voucher & Manufacturer Coupon Processing | S | W539 (Coupon & voucher processing — barcode/QR scanning, validation, stacking rules, digital voucher verification, exception handling, EOD reconciliation, manufacturer coupon reimbursement) | W5B (checkout — coupon application), W523 (promotional setup — coupon configuration), W13 (promotions — coupon master source), W5F (EOD — coupon summary), W538 (LP monitoring — coupon abuse detection), W40 (pricing — coupon pricing rules), FIN-019 (vendor rebate — manufacturer coupon reimbursement) |
| POS-052 | POS BIR Invoice Reprint, Adjustment & Credit Note Issuance | M | W540 (BIR invoice reprint & credit note — reprint with watermark, credit note auto-generation, debit note for price corrections, void documentation, 10-year audit trail) | W5B (checkout — original transaction source), W12/W12A (returns — credit note trigger), W529 (void/refund authorization — void document), W54A (CAS registration — numbering authority), W77 (BIR audit — document retrieval), W528 (digital receipt — e-receipt reprint), W473 (EIS — credit note transmission), DOC-002 (BIR invoice — compliance) |
| POS-053 | POS Cash Office Operations & Bank Deposit Preparation | M | W541 (Cash office operations — drawer receipt and count, variance documentation, non-cash tender verification, bank deposit preparation, cash securing, close report, CIT pickup) | W5A (opening float — next-day float), W5F (EOD close — triggers cash office), W517 (shift handover — drawer submission), W212 (Smart Safe — automated counting), W272 (over/short — variance investigation), W278 (mid-day skim — mid-day deposit), FIN-025 (CIT — armored car), W89 (bank reconciliation — deposit matching) |
| POS-054 | POS Quotation & Estimate Generation with Sales Conversion | S | W542 (Quotation & estimate — creation with ATP check, pricing, discount authorization, document generation, validity tracking, conversion to sale, analytics) | W5B (checkout — sale conversion), W528 (e-receipt — quotation email), W289 (pricing master — standard prices), CRM-003 (trade account — contracted pricing), CRM-013 (trade counter — quotation source), W536 (order management — ATP check), W67 (store performance — quotation KPIs), POS-006 (price override — discount authorization), POS-010 (quantity break pricing) |
| POS-055 | POS Consignment Sell-Through Transaction Processing & Vendor Settlement Trigger | M | W543 (Consignment sell-through — consignment item scan detection, ownership transfer at sale, sell-through data accumulation, consignment return processing, pricing exceptions, vendor settlement trigger) | W5B (checkout — consignment scan), W12 (returns — consignment return), W533 (event stream — ownership transfer), INV-009/INV-017 (consignment inventory), FIN-018 (consignment settlement), W252 (item master — consignment flag), W289 (pricing master — consignment pricing), W525 (nightly reconciliation — consignment inventory) |
| POS-056 | POS Service Work Order Creation & Scheduling | S | W544 (Service work order — service SKU scan, scheduling with technician calendar, work order creation, deferred revenue posting, customer confirmation, technician notification, completion processing, post-service survey) | W5B (checkout — service item scan), W546 (progress payment — large service deposits), W112 (trade counter — trade service orders), SRV-001 (service lifecycle), W292 (employee master — technician skills), FIN-039 (revenue recognition — deferred service revenue), CRM-011 (feedback — post-service survey), MDM-015 (non-stock item — service SKU) |
| POS-057 | POS Special Order & Customer Order Processing | S | W545 (Special order — ATP check, order creation, deposit collection, supply chain fulfillment, customer notification, balance collection at pickup, deadline management, analytics) | W5B (checkout — deposit and balance payment), W536 (order management — ATP and fulfillment), W273 (endless aisle — vendor-direct alternative), W75 (layaway — related payment model), W22 (inter-store transfer — BOPIS alternative), W4 (replenishment — DC fulfillment), W109 (store receiving — item arrival), W533 (event stream — order transmission), FIN-039 (revenue recognition — deposit accounting) |
| POS-058 | POS Deposit & Progress Payment Collection for Project Orders | S | W546 (Deposit & progress payment — project order setup, deposit collection, phase delivery and interim payment, final payment, balance monitoring with aging, project order modification) | W5B (checkout — payment processing), W19 (home delivery — phase delivery), W109 (store receiving — phase pickup), W542 (quotation — project order origin), W545 (special order — single-delivery variant), W75 (layaway — consumer installment variant), CRM-003 (trade account — B2B customer), CRM-013 (trade counter — pro desk), FIN-028 (collection — overdue escalation), FIN-039 (revenue recognition — milestone-based) |
| POS-059 | POS Scan & Go / Mobile Self-Scan Checkout | S | W547 (Scan & Go — session initiation, barcode scanning, basket management, quick-pay terminal, in-app payment, attendant verification, skip-scan detection, EOD reconciliation) | W516 (SCO — shared infrastructure), W206 (mPOS — shared mobile architecture), W528 (digital receipt), W538 (LP monitoring — skip-scan detection), W550 (loyalty points as tender), POS-029 (age-restricted verification), POS-016 (catch-weight handling), POS-043 (local data store — price lookup), W533 (event stream — transaction publishing) |
| POS-060 | POS Third-Party On-Demand Delivery Integration | S | W548 (On-demand delivery — delivery request at POS, courier API dispatch, payment processing, item staging and handoff, delivery tracking, exception handling, weekly settlement) | W5B (checkout — delivery option), W5D (delivery scheduling — own fleet alternative), W273 (endless aisle — vendor-direct alternative), W62B (3PL management — platform relationship), W438 (yard loading — carry-out alternative), W109 (store receiving — returned item restocking), W99 (payment settlement — fee reconciliation), W254 (location master — store address) |
| POS-061 | POS Damaged & Open-Box Item Discount Processing | S | W549 (Damaged item discount — condition assessment, discount application, modified warranty disclosure, shrinkage tracking, shelf replacement trigger) | W5B (checkout — damage discount scan), W524 (demo/display — planned discount comparison), W532 (clearance — clearance discount comparison), W91 (damaged goods — unsellable removal), W248 (inventory variance — shrinkage tracking), W33 (warranty — modified terms), W12 (returns — restricted return processing), W4 (replenishment — shelf replacement), POS-006 (price override — discount authorization) |
| POS-062 | POS Loyalty Points as Payment Tender | S | W550 (Loyalty points as tender — account lookup, points-to-currency conversion, redemption processing, deferred revenue reversal, offline redemption with floor limit, return reversal) | W5B (checkout — points tender), W17 (loyalty operations), W533 (event stream — points redemption event), W535 (offline — cached balance), W12 (returns — points reversal), W104 (loyalty financial governance), CRM-001 (loyalty engine), CRM-005 (tiered loyalty), FIN-039 (revenue recognition), W496 (loyalty fraud — frozen points), POS-004 (multi-tender — points as one tender) |
| POS-063 | POS Customer On-the-Spot Loyalty Enrollment & Account Lookup | S | W551 (On-the-spot loyalty enrollment — quick enroll with minimum data, OTP verification, digital card issuance, account lookup, quick update, enrollment analytics) | W5B (checkout — enrollment trigger), W17 (loyalty operations — account creation), W263 (enrollment journey — POS channel), CRM-001 (loyalty engine — account setup), CRM-005 (tiered loyalty — initial tier), CRM-016 (enrollment journey — POS channel), W528 (e-receipt — email collection), NFR-010 (data privacy — RA 10173 consent), POS-011 (customer display — self-service input), W253 (customer master — dedup check) |
| POS-064 | POS Donation & Charity Round-Up Processing | S | W552 (Donation & round-up — donation prompt on customer display, round-up and fixed amount options, campaign management, segregated GL posting, charity remittance, ESG reporting, analytics) | W5B (checkout — donation prompt after tender), W528 (e-receipt — donation in digital receipt), W533 (event stream — donation event), W5F (EOD — donation summary), W67 (store performance — donation exclusion), GOV-008 (ESG — charitable giving), POS-011 (customer display — prompt), POS-012 (receipt — donation line) |
| POS-065 | POS Pricing Error Detection & Immediate Correction at Checkout | M | W553 (Pricing error correction — discrepancy detection, price verification, immediate price override, shelf label correction task, root cause logging, enterprise-wide verification trigger) | W5B (checkout — price display), W40 (price changes — label update gap), W13 (promotions — promo pricing source), W69 (price compliance — root cause data), W86 (planogram — shelf placement), W181 (shelf label — correction printing), W289 (pricing master — source of truth), W468 (DTI price freeze — freeze price), POS-006 (price override — authorization), POS-047 (price push — enterprise correction), W533 (event stream — discrepancy event) |
| POS-066 | Store-Level Daily Shelf Replenishment & Restocking | S | W554 (Daily shelf replenishment -- system-generated task list, handheld prioritized queue, shelf restocking per planogram, FEFO rotation, bulk bin refilling, yard restacking, label damage flagging, out-of-shelf reporting, supervisor spot-check) | POS-013 (real-time inventory -- sales data feed), INV-001 (perpetual inventory -- stock update), MDM-023 (planogram master -- position reference), W86 (planogram compliance -- monthly audit partner), W109 (store receiving -- inbound feed), W181 (shelf label -- reprint trigger), W420 (AI shelf monitoring -- automated gap detection) |
| POS-067 | Store-Level Non-Emergency Incident & Hazard Reporting | S | W559 (Non-emergency incident reporting -- mobile form with photos, area securing, incident classification, severity grading, escalation, corrective action generation, monthly trend analysis) | W140 (OHS incidents -- escalation path), W330 (emergency response -- upgrade path), W285 (public liability -- data source), W501 (first aid -- medical response), W47 (facility maintenance -- work order), W503 (pest control -- trend partner), GOV-004 (public liability insurance -- claims data) |
| POS-068 | Store-Level Loss Prevention Daily Routine | S | W562 (LP daily routine -- EAS gate test, high-value cage check, overnight alert review, CCTV verification, blind-spot walkthrough, DSD spot-check, till spot-check, shelf count, SCO log review, daily LP log) | W37 (LP exception -- escalation), W248 (inventory variance -- investigation trigger), W466 (LPAP -- framework), W538 (POS LP monitoring -- alert source), W71 (CCTV audit -- camera check), W272 (cashier over/short -- till check), W281 (SCO exception -- exception log), W48 (IT helpdesk -- camera repair) |
| POS-069 | Store-Level Daily Communication & Memo Acknowledgment | S | W571 (Store communication -- priority-based communication module, push/SMS for urgent, Store Manager acknowledgment, task assignment, photo evidence for execution, 4-hour escalation, monthly compliance dashboard) | W67 (store performance -- communication KPI), W186 (SOP governance -- policy distribution), W523 (promo terminal setup -- task source), W40 (price changes -- price update comms), W29 (product recall -- recall notification), W13 (promotions -- promo calendar comms) |
| POS-070 | Store-Level Daily Planogram Execution & Shelf Compliance Check | S | W573 (Daily planogram execution -- handheld planogram walk, product facing, label matching, promo display verification, endcap check, shelf damage reporting, reset section compliance, OOS gap flagging, price accuracy check, supervisor sign-off) | POS-066 (shelf replenishment -- execution partner), MDM-023 (planogram master -- planogram source), W86 (planogram audit -- monthly audit partner), W181 (shelf label -- label reprint), W262 (promo setup -- display reference), W279 (product substitution -- substitute facing), W40 (price changes -- price accuracy), W420 (AI shelf monitoring -- gap detection) |
| WHL-001 | DC Daily Operations & Shift Management | S | W584 (DC daily operations & shift management -- night-before operations plan, shift start-up briefing, labor allocation against daily volume forecast, mid-morning pace check, exception handling, shift handover log, night shift operations, end-of-day KPI snapshot, DC Manager daily review, weekly operations review) | W3 (receiving -- throughput data), W106 (dispatch -- loading data), W585 (dock scheduling -- appointment data), W586 (KPI dashboard -- performance feed), W6 (cycle counting -- night shift data), W188 (fleet maintenance -- equipment availability), W52 (fleet -- carrier performance), W57 (promotions -- pre-positioning priority) |
| WHL-002 | DC Dock Scheduling & Appointment Management | M | W585 (DC dock scheduling & appointment management -- appointment request intake, dock door assignment with capability matching, time slot allocation, carrier/vendor notification, day-of gate check-in, real-time dock door utilization tracking, no-show management with vendor scorecard feed, appointment compliance reporting, monthly dock capacity planning) | W3 (receiving -- appointment feeds gate check), W3C (inbound scheduling -- extended appointment management), W106 (dispatch -- outbound dock slots), W52 (fleet -- carrier notification), W44 (vendor scorecard -- appointment compliance), W242 (3PL review -- carrier compliance), W584 (daily operations -- pace check dashboard), W586 (KPI dashboard -- dock utilization KPI) |
| WHL-003 | DC Daily KPI Dashboard & Performance Tracking | M | W586 (DC daily KPI dashboard & performance tracking -- automated overnight KPI calculation across 6 categories and ~20 KPIs per DC, morning dashboard generation with green/amber/red scorecard, DC Manager morning review, exception flagging with configurable rules, corrective action assignment with lifecycle tracking, VP Supply Chain multi-DC dashboard review, weekly trend analysis, monthly executive DC performance report) | W584 (daily operations -- shift log data), W3 (receiving -- throughput, accuracy, quality KPIs), W106 (dispatch -- departure rate, utilization, delivery on-time), W585 (dock scheduling -- dock utilization), W4 (picking -- productivity, accuracy), W6 (cycle counting -- count accuracy), W44 (vendor scorecard -- quality cross-reference), W52 (fleet -- truck utilization, delivery performance), W242 (3PL review -- carrier performance), W21 (capex -- capacity recommendations) |
| POS-074 | Store-Level Daily Huddle | M | W739 (daily huddle — team briefing, performance flash, priorities, safety minute, policy updates, staffing confirmation) | W665 (KPI dashboard — performance data), W34 (scheduling — attendance verification), W13 (promotions — active promos), W571 (communication — memos) |
| POS-075 | Store-Level On-the-Spot Complaint Resolution | M | W740 (on-the-spot resolution — authority matrix, floor-level resolution, logging, pattern flagging) | W41 (complaint resolution — escalation path), W507 (root cause analysis — pattern data), W608 (CX pulse — satisfaction data), W5B (POS — price adjustment) |
| POS-076 | Store-Level Fuel & Generator Management | S | W741 (fuel inventory — daily level check, reorder, generator testing, PM scheduling, outage event logging) | W470 (brownout protocol — outage event), W47 (maintenance — PM work orders), W489 (store budget — fuel expense) |
| POS-077 | Store-Level Key & Access Card Management | M | W742 (key/access management — issuance, access levels, shift activation, lost credential, quarterly combo change, audit) | W15/W43 (onboarding/separation — lifecycle triggers), W152 (IT provisioning — access configuration), W292 (employee master — credential tracking), W37 (LP — unauthorized access) |
| POS-078 | Store-Level Daily Cleaning Checklist | M | W743 (cleaning checklist — zone verification, failed item remediation, chemical inventory, LGU compliance) | W448 (LGU sanitary permit — compliance documentation), W503 (pest control — sanitation integration), W136 (indirect procurement — cleaning supplies) |
| POS-079 | Store-Level Special Order Follow-Up | S | W744 (special order follow-up — daily review, status check, customer notification, received item inspection, overdue escalation) | W545 (special order — order creation), W250 (control tower — shipment tracking), W109 (store receiving — arrival trigger), W5D/W438 (delivery/carry-out) |
| POS-080 | Store-Level Receiving Dock Scheduling | M | W745 (dock scheduling — schedule compilation, time slot allocation, vendor notification, congestion management, no-show tracking) | W18B (DSD scheduling — vendor appointment feed), W4 (replenishment — DC delivery window), W44 (vendor scorecard — no-show data), W723 (loading bay — outbound coordination) |
| POS-081 | Store-Level Building Material Sample Management | S | W746 (sample management — library maintenance, customer assistance, sample checkout, quantity calculation, replenishment, seasonal rotation) | W50 (PIM — product specs), W542 (quotation — quantity calculation), W1 (assortment — sample performance), W314 (planogram — display position), W17 (loyalty — checkout tracking) |
| INV-023 | Inventory Obsolescence Identification & Write-Off Management | M | W587 | W220, W93, W88, W91, W42, W92 |
| INV-024 | Seasonal Inventory Build-Down & Transition Execution | S | W588 | W32, W93, W220, W262, W554, W583 |
| ECOM-023 | E-Commerce Fulfillment SLA Monitoring & Exception Escalation | M | W591 | W11, W19, W19B, W98, W246, W268 |
| ECOM-024 | E-Commerce Customer Delivery Tracking & Proof of Delivery Management | M | W592 | W19, W268, W12, W98, W509 |
| PUR-027 | Vendor Portal Content Management & Self-Service Operations | S | W593 | W36, W7, W100, W287, W44 |
| NFR-030 | ERP System Daily Health Check & Integration Monitoring | M | W595 | W48, W55, W257, W380, W525, W382 |
| SCP-010 | Store-Level Replenishment Exception Management & Auto-Override | S | W596 | W4, W22, W57, W31, W105, W214 |
| CRM-022 | Customer Complaint Escalation Matrix & Resolution SLA Tracking | M | W597 | W41, W469, W258, W259, W507, W65 |
| WSL-003 | Wholesale Pricing & Quotation Management | S | W598 | W145, W58, W163, W78, W85 |
| WSL-004 | Wholesale Returns, Credit & Adjustment Processing | S | W599 | W12, W146, W70, W88, W145 |
| SRV-003 | Service Contractor Accreditation & Onboarding Management | M | W600 | W138, W213, W33, W544, W187 |


| HR-026 | Store-Level Employee Disciplinary Process & DOLE Due Process Compliance | M | W603 | W10, HR-014, GOV-040, W292 |
| HR-027 | Store-Level New Employee Buddy System & First-Week Onboarding | S | W609 | W15, W51, W567, W292 |
| HR-028 | Employee Exit Interview & Attrition Analysis | S | W628 | HR-008, W43, W10 |
| HR-029 | Employee Engagement Survey & Action Planning | S | W629 | HR-028, W51 |
| HR-030 | Employee Recognition & Rewards Program Management | S | W630 | HR-012, W72 |
| GOV-050 | Store-Level Customer Experience Standards & Daily Service Operations | S | W604 | CRM-011, CRM-015, POS-035 |
| GOV-051 | Return Fraud Detection & Serial Returner Management | M | W605 | POS-007, POS-038, AUD-001, W538 |
| GOV-052 | Store-Level Water & Utility Conservation Operations | S | W606 | GOV-019, GOV-042, FIN-040 |
| GOV-053 | Store-Level Product Demo & Trial Station Daily Operations | S | W607 | SRV-001, POS-033, GOV-028 |
| GOV-054 | Store-Level Customer Feedback Collection & CX Pulse Monitoring | S | W608 | CRM-011, CRM-020, GOV-050 |
| FIN-048 | Payment Gateway Daily Operations & Settlement Monitoring | M | W611 | POS-049, POS-013, FIN-032 |
| FIN-049 | Intercompany Rate Setting & Quarterly Transfer Pricing Review | M | W612 | FIN-002, IC-002, FIN-038 |
| FIN-050 | Store-Level Weekly Payroll Accrual & Labor Cost Flash Report | S | W613 | HR-001, FIN-012, FIN-040 |
| NFR-031 | Data Warehouse & ETL Pipeline Daily Operations & Monitoring | M | W614 | NFR-026, NFR-023 |
| NFR-032 | Customer Mobile App Daily Operations & Content Management | S | W615 | ECOM-009, CRM-014, NFR-024 |
| NFR-033 | ERP Business Change Request & Enhancement Backlog Management | M | W616 | NFR-024, NFR-029 |
| CRM-023 | B2B Customer Success & Quarterly Business Review Operations | S | W617 | CRM-003, CRM-004, CRM-008 |
| CRM-024 | Customer Churn Prediction & Proactive Retention Management | S | W618 | CRM-010, CRM-014, MKT-001 |
| CRM-025 | Customer Account Merge & Deduplication Request Processing | M | W619 | MDM-003, CRM-002 |
| PUR-028 | Vendor Due Diligence & Onboarding Site Visit Management | M | W620 | PUR-003, PUR-022, MDM-004 |
| PUR-029 | VMI Daily Performance Monitoring | S | W621 | PUR-014, INV-018 |
| SCP-011 | Mock Product Recall Exercise & Recall Readiness Testing | M | W622 | INV-016, PUR-017 |
| SCP-012 | Cross-Functional New Store Opening Readiness Review | M | W623 | GOV-005, POS-001, GOV-048 |
| MER-005 | Product Quality Lab Testing & Certification Management | M | W625 | PUR-016, PUR-017, GOV-034, GOV-036 |
| COM-003 | Enterprise Risk Register Maintenance & Quarterly Risk Review | M | W626 | GOV-002, COM-001, GOV-013 |
| COM-004 | Product Recall Effectiveness Verification & Post-Recall Review | M | W627 | INV-016, PUR-017, SCP-011 |
| PUR-030 | Strategic Sourcing & Category Strategy | S | W631 | W44, W36, W155, W624 |
| PUR-031 | Competitive Bidding & Tender Management | M | W632 | W36, W620, W2C |
| PUR-032 | Purchase Price Variance (PPV) Analysis | M | W633 | W85, W2B, W293, W307 |
| FIN-051 | Revenue Assurance & POS Revenue Reconciliation | M | W634 | W99, W522, W538, W89 |
| FIN-052 | PFRS 16 Lease Accounting Operations | M | W635 | W275, W14, W118, W9A |
| FIN-053 | Standardized Balance Sheet Account Reconciliation | M | W636 | W89, W9A, W100 |
| FIN-054 | Financial Controls Testing & Monitoring | M | W637 | W9A, W332, W338 |
| FIN-055 | Period-End Journal Entry Review & Approval | M | W638 | W9A, W9B, W26 |
| FIN-056 | Rolling Forecast & Financial Scenario Planning | S | W639 | W26, W589, W319 |
| FIN-057 | Merchant Fee Analysis & Payment Cost Optimization | M | W640 | W99, W261, W611, POS-049 |
| HR-031 | Off-Cycle & Ad-Hoc Payment Processing | M | W641 | W10, W643, HR-001 |
| HR-032 | HMO & Private Benefits Administration | S | W642 | W15, W43, W292 |
| HR-033 | Final Pay Computation & Separation Settlement | M | W643 | W10, W43, W175 |
| HR-034 | 13th Month Pay Reconciliation & Compliance | M | W644 | W10, HR-001 |
| HR-035 | Strategic Workforce Planning | S | W645 | W15, W178, W127 |
| HR-036 | HR Service Desk Operations | S | W646 | W48, W152 |
| HR-037 | Employee Data Privacy Compliance Operations | M | W647 | W53, W389, W405 |
| WMS-012 | DC Cycle Counting & Inventory Accuracy Program | M | W648 | W6, W514, W301 |
| WMS-013 | DC Safety Operations & Compliance | M | W649 | W140, W141, W584 |
| WMS-014 | Warehouse Equipment Preventive Maintenance | S | W650 | W188, W240 |
| WMS-015 | Reverse Logistics Processing at DC | M | W651 | W12, W88, W110 |
| WMS-016 | Seasonal Warehouse Surge Planning | M | W652 | W32, W584, W555 |
| LOG-001 | Fleet Accident & Incident Management | M | W653 | W199, W654, FIN-023 |
| LOG-002 | Driver Onboarding, Training & Certification | S | W654 | W197, W199 |
| HSE-001 | Safety Training & Certification Tracking | M | W655 | W51, W187, W141 |
| COM-005 | Anti-Bribery & Anti-Corruption (ABAC) Compliance Program | M | W656 | W426, W79, W159 |
| COM-006 | Regulatory Change Management & Impact Assessment | M | W657 | W506, W90, W260 |
| COM-007 | General Regulatory Inspection Response Protocol | M | W658 | W54, W77, W505 |
| ECOM-025 | Ecommerce Platform Incident Management | M | W659 | W48, W55, W595 |
| CRM-026 | Service Recovery & Customer Retention Program | M | W660 | W41, W597, W618, W156 |
| FIN-058 | Fixed Asset Depreciation Run & Component Accounting Operations | M | W661 | W39, W184, W276, W489, W21 |
| FIN-059 | AP Aging Management & Vendor Payment Prioritization | M | W662 | W7, W556, W30, W589, W324, W244 |
| FIN-060 | Customer Credit Portfolio Periodic Review & Collection Strategy | M | W663 | W328, W108, W81, W572, W24 |
| FIN-061 | Cash Flow Variance Analysis & Liquidity Stress Testing | M | W664 | W589, W89, W30, W319, W327 |
| POS-082 | Store-Level Inventory Receiving Quality Control | M | W666 | W109, W3, W22B, PUR-016 |
| POS-083 | Store-Level Price Verification & Daily Compliance Operations | M | W667 | W69, W181, W553, POS-024 |
| POS-084 | Store-Level Home Delivery & Third-Party Logistics Coordination | S | W668 | W548, W19, W242, W237 |
| PUR-033 | Vendor Contract Compliance Monitoring & Enforcement | M | W669 | W62, W44, W244, W27, W110 |
| PUR-034 | Supplier Emergency Onboarding & Rapid Activation | M | W670 | W60, W620, W36, W656 |
| PUR-035 | Commodity Price Monitoring & Procurement Strategy | M | W671 | W633, W31, W2C, W80, W85 |
| PUR-036 | VMI Quarterly Business Review & Program Optimization | S | W672 | W621, W44, W27, W20 |
| CRM-027 | Customer Segmentation & Target Marketing Operations | S | W673 | W156, W83, W618, CRM-014 |
| CRM-028 | Customer Loyalty Program Partner Management | S | W674 | W104, W487, W83, W142 |
| CRM-029 | Customer Data Platform Daily Operations & Data Quality Management | M | W675 | W156, W619, W614, MDM-003 |
| MKT-003 | Digital Marketing Campaign Operations & Cross-Channel Execution | S | W676 | W83, W142, W565, W673 |
| MKT-004 | Marketing Budget Management & Spend Analytics | S | W677 | W83, W26, W565 |
| MER-006 | Multi-Channel Pricing Consistency Monitoring & Governance | M | W678 | W289, W533, POS-024, W180 |
| MER-007 | Assortment Optimization & Rationalization Review | S | W679 | W1, W68, W624, W563, W252, W314 |
| WMS-017 | DC Quality Control & Vendor Compliance Inspection at Receiving | M | W681 | W110, W219, W447, W44, PUR-016 |
| HR-038 | Employee Career Development & Internal Job Posting Operations | S | W682 | W178, W511, W72, W292 |
| HR-039 | Employee Competency Assessment & Certification Management | M | W683 | W51, W567, W655, W292 |
| NFR-034 | Business Intelligence Report Development & Governance Lifecycle | M | W684 | W113, W616, W614 |
| COM-008 | Business Continuity Plan Maintenance & Annual BIA Refresh | M | W685 | W158, W55, W576, W580, W470 |
| DOC-009 | Document Approval Routing & Digital Signature Management | M | W686 | W255, W256, W243, W359, W442 |
| DOC-010 | Document Template Management & Version Control | M | W687 | W255, W256, W686 |
| DOC-011 | Contract & Agreement Lifecycle Management | M | W688 | W62, W124, W243, W620, W669, W635, W686, W687, W508 |
| ESG-006 | Store Energy Efficiency Monitoring & Utility Cost Optimization | M | W692 | W192, W193, W7, W173, W188, W184, W26, W694 |
| ESG-007 | Water Consumption Tracking & Conservation Management | S | W693 | W192, W7, W188, W477, W506, W193, W694 |
| ESG-008 | ESG Data Collection, Validation & Annual Sustainability Report Preparation | M | W694 | W192, W193, W194, W195, W443, W15, W51, W140, W629, W656, W124, W647, W359, W692, W693 |
| HSE-002 | Emergency Response & Evacuation Protocol Management | M | W695 | W140, W141, W238, W470, W576, W580, W685, W506, W655 |
| HSE-003 | Contractor & Visitor Safety Induction & Access Control | M | W696 | W187, W140, W655, W658, W647, W256 |
| HSE-004 | Workplace Ergonomics Assessment & Musculoskeletal Injury Prevention | S | W697 | W140, W141, W188, W184, W655, W436, W685, W647 |
| HAZ-005 | Safety Data Sheet (SDS) Lifecycle Management & Distribution | M | W698 | W236, W237, W238, W1, W36, W141, W506, W110 |
| HAZ-006 | Hazmat Transportation & Carrier Compliance Management | M | W699 | W236, W237, W238, W239, W668, W44, W506, W698 |
| MNT-005 | Facility Condition Assessment & Capital Planning Support | M | W700 | W240, W241, W184, W635, W141, W91, W685, W702 |
| MNT-006 | Utility Infrastructure Management & Metering Operations | S | W701 | W7, W692, W702, W703, W184, W173, W508 |
| POS-085 | New Store Opening Project Management & Go-Live Execution | M | W702 | W16, W623, W223, W224, W225, W227, W96, W86, W679, W109, W667, W15, W518, W655, W508, W701, W54, W142, W184 |
| POS-086 | Store Closure, Consolidation & Asset Recovery | M | W703 | W45, W643, W91, W92, W443, W184, W688, W701, W508, W708, W442 |
| WSL-005 | Wholesale Customer Contract Renewal & Tier Reclassification | M | W704 | W145, W598, W599, W688, W508, W283, W686, W8, W70 |
| PUR-037 | Vendor Self-Service Portal Operations & Supplier Collaboration | M | W705 | W36, W7, W508, W656, W1, W688 |
| PUR-038 | Supplier Performance Scorecard & Quarterly Business Review | M | W706 | W44, W110, W681, W599, W88, W633, W669, W672, W195, W705, W508, W670, W36 |
| CRM-030 | Omnichannel Returns & Refund Orchestration | M | W707 | W12, W599, W651, W442, W668, W83, W110 |
| CRM-031 | Customer Communication Management & Proactive Notification Operations | M | W708 | W142, W83, W673, W707, W627, W647, W100, W687 |
| NFR-035 | Enterprise Data Governance & Quality Management Operations | M | W709 | W508, W595, W442, W256, W647, W359, W619, W614 |
| NFR-036 | Loss Prevention Analytics & Shrinkage Investigation System Operations | M | W710 | W79, W80, W6, W91, W92, W681, W152, W44, W706, W88, W48 |



## R26. Business Continuity & Disaster Recovery (BCP)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| BCP-001 | Business Continuity Plan Annual Review & Update | M | W847 | — |
| BCP-002 | Typhoon & Natural Disaster Store Emergency Protocol | M | W848 | — |
| BCP-003 | IT Disaster Recovery Site Activation & Failover | M | W849 | — |
| BCP-004 | Store Emergency Closure & Reopening Procedure | M | W850 | — |
| BCP-005 | Critical System Recovery & Service Restoration | M | W851 | — |
| BCP-006 | Supply Chain Disruption Business Impact Assessment & Recovery | M | W852 | — |
| BCP-007 | Business Continuity Plan Tabletop Exercise & Drill | S | W853 | — |
| BCP-008 | Pandemic/Epidemic Business Continuity Activation | M | W854 | — |
| BCP-009 | Communication Tree Activation & Crisis Communication | M | W855 | — |
| BCP-010 | Post-Incident Review, Lessons Learned & Plan Update | M | W856 | — |

## R30. Business Intelligence & Analytics Operations (BIA)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| BIA-001 | Daily Report Distribution & Automated Dashboard Refresh | M | W879 | — |
| BIA-002 | BI Dashboard Development & User Request Management | S | W880 | — |
| BIA-003 | Data Warehouse ETL Job Monitoring & Exception Handling | M | W881 | — |
| BIA-004 | Self-Service BI Governance & Access Provisioning | S | W882 | — |
| BIA-005 | Ad-hoc Analytics Request Fulfillment & SLA Management | S | W883 | — |
| BIA-006 | Data Quality Monitoring & Remediation Operations | M | W884 | — |
| BIA-007 | Monthly Executive Reporting Package Preparation | M | W885 | — |

## R31. Customer Credit & Collections Management (CCR)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| CCR-001 | Customer Credit Application Processing & Scoring | M | W886 | — |
| CCR-002 | Customer Credit Limit Review & Adjustment | M | W887 | — |
| CCR-003 | Customer Credit Hold & Order Blocking | M | W888 | — |
| CCR-004 | Customer AR Aging Analysis & Collection Prioritization | M | W889 | — |
| CCR-005 | Customer Collection Call Execution & Promise Tracking | S | W890 | — |
| CCR-006 | Customer Bad Debt Write-Off & Recovery | M | W891 | — |
| CCR-007 | Customer Statement Generation & Distribution | S | W892 | — |
| CCR-008 | Customer Credit Scorecard & Portfolio Analysis | S | W893 | — |

## R19–R24. Additional Compliance Requirements (COM)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| COM-009 | Anti-Money Laundering (AML) Compliance Program Operations | M | W730 | W460, W519 |
| COM-010 | Consumer Act (RA 7394) Compliance Monitoring & Enforcement | M | W731 | W12, W447, W469 |
| COM-011 | Vendor Tax Compliance Monitoring & BIR TIN Validation | M | W732 | W293, W36, W711 |
| COM-012 | Customer Account Data Deletion & RA 10173 Privacy Compliance Processing | M | W834 | W156, W257, W675 |

## Additional CRM Requirements (CRM)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| CRM-032 | Customer Onboarding Journey Management & First-90-Day Engagement | S | W735 | W65 |
| CRM-033 | Customer Store Credit Issuance & Lifecycle Management | M | W781 | W5, W660 |
| CRM-034 | Customer B2B Order-to-Cash Cycle Monitoring & Proactive Communication | S | W782 | — |
| CRM-035 | Customer Credit Application Scoring & Risk Assessment Processing | M | W783 | W24, W572, W732 |
| CRM-036 | Customer Project BOM Estimation & Material Planning Service | S | W820 | W252, W289, W542 |
| CRM-037 | Customer Project Warranty Registration & Multi-Year Tracking | M | W821 | W33, W487, W708, W88 |
| CRM-038 | Customer Loyalty Tier Benefit Fulfillment & Welcome Package Processing | S | W822 | W104, W11, W5, W615, W708 |
| CRM-039 | Customer Loyalty Account Deceased Member Processing & Points Estate Transfer | S | W933 | — |
| CRM-040 | Customer B2B Self-Service Portal Order Management & Account Access | S | W936 | — |
| CRM-041 | Customer Loyalty Family/Household Account Linking & Shared Benefits Management | S | W942 | W515 |
| CRM-042 | Customer Complaint Root Cause Analysis & Systemic Improvement | S | W507 (Complaint root cause analysis — monthly pattern detection, systemic issue threshold alerting, cross-departmental corrective action assignment, 60-day effectiveness monitoring, quarterly complaint-to-improvement reporting) | W41, W87, W110, W67, W40, W4 |
| CRM-043 | Customer Account Maintenance & B2B Information Update | S | W508 (Customer account maintenance — update request intake, document verification, change type classification, customer master update with audit trail, downstream propagation, annual re-verification of 5,400 B2B accounts) | W24, W460, W253, W328, W293, W112 |
| CRM-044 | Customer Price Protection & Price Adjustment Policy Processing | M | W928 | — |

## Additional Ecommerce Requirements (ECOM)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| ECOM-026 | Marketplace Channel Daily Operations & Order Management (Lazada/Shopee) | M | W724 | W180, W19, W246, W99 |
| ECOM-027 | Ecommerce Platform Daily Health Monitoring & Performance Dashboard | M | W725 | — |
| ECOM-028 | Ecommerce Product Content Enrichment & Catalog Daily Operations | M | W726 | W180, W264, W298, W564 |
| ECOM-029 | Ecommerce Platform Feature Release, A/B Testing & UX Optimization | S | W828 | W132, W659 |
| ECOM-030 | Customer Ecommerce Order Split & Partial Delivery Proactive Communication | M | W829 | W101, W592 |
| ECOM-031 | Customer Back-in-Stock Notification Subscription & Alert Management | S | W930 | — |
| ECOM-032 | Ecommerce Customer Wishlist, Save-for-Later & Price Drop Alert | S | W934 | — |
| ECOM-033 | Ecommerce Customer Product Comparison Tool & Buying Guide Content Management | S | W940 | — |

## Additional Engineering & Construction Requirements (ENG)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| ENG-001 | Construction Safety Management & DOLE DO 13 Compliance | M | W789 | — |
| ENG-002 | Construction Quality Assurance & Milestone Inspection | M | W790 | — |
| ENG-003 | Construction Document Control & As-Built Management | M | W791 | — |

## Additional ESG Requirements (ESG)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| ESG-009 | Green Building Certification (BERDE) & Sustainable Store Design Standards | S | W800 | — |
| ESG-010 | ESG Incident Response, Regulatory Citation & Stakeholder Communication | M | W801 | — |

## Additional Financial Management Requirements (FIN)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| FIN-062 | BIR Withholding Tax (EWT) Certificate Form 2307 Issuance to Vendors | M | W711 | W260, W293, W556, W705 |
| FIN-063 | Financial Restatement & Prior-Year Adjustment Processing | M | W712 | W260, W351, W481, W637 |
| FIN-064 | Corporate Credit Card Program Management & Expense Reconciliation | S | W713 | W43, W435 |
| FIN-065 | Store-Level Daily Financial Summary & Flash P&L | M | W714 | W489, W533, W561, W85 |
| FIN-066 | Store-Level Daily Opening Safe Count & Cash Float Preparation | M | W764 | W25, W272, W5, W541 |
| FIN-067 | Multi-Entity Consolidation Monthly Execution & Elimination Processing | M | W765 | W137, W234, W351, W635, W752 |
| FIN-068 | Customer Credit Note Aging Management & Unredeemed Credit Write-Off | M | W766 | W540, W708 |
| FIN-069 | Vendor Rebate Claim Filing & Settlement Documentation Processing | M | W767 | W244, W556, W705 |
| FIN-070 | BIR VAT Refund Claim Processing & Input VAT Recovery | S | W768 | W590 |
| FIN-071 | Customer Overpayment Detection & Refund Processing | M | W769 | W708, W99 |
| FIN-072 | AP Vendor Debit Memo Processing & Account Deduction Management | M | W770 | W110, W244, W500, W513, W556, W669, W705, W5510 (supplier service-fee billing for store-rendered barcode labels & promotional collaterals, settling as W770-type debit memos) |
| FIN-073 | Customer Credit Field Collection Operations & Legal Escalation | M | W812 | W196, W280 |
| FIN-074 | AP Vendor Invoice Duplicate Detection & Resolution | M | W813 | W244, W705 |
| FIN-075 | Credit Card Settlement Exception & Chargeback Recovery Processing | M | W814 | — |
| FIN-076 | Weekly Cash Flow Forecast & Treasury Planning | S | W589 | W10, W14, W30, W80, W89, W99, W144, W232, W318, W319, W556 |
| FIN-077 | Monthly Tax Provision & Compliance Review | M | W590 | W9, W90, W260, W407, W473, W475, W499 |
| FIN-078 | Insurance Claims Processing & Recovery Management | M | W610 | FIN-023, GOV-012, GOV-033 |
| FIN-079 | Customer Store Credit Expiration Management & Unclaimed Credit Processing | M | W939 | — |

## Additional Governance Requirements (GOV)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| GOV-055 | Store-Level Pest Control & Sanitation Management | S | W503 (Pest control — monthly vendor service visits, zone-by-zone findings, pest incident emergency response, monthly sanitation self-audit, quarterly deep treatment, annual vendor review) | W448, W436, W237, W47, W242 |
| GOV-056 | Store-Level Digital Signage & Content Management | S | W504 (Digital signage — content scheduling, zone-based targeting, automated content validation, remote distribution, playback compliance monitoring, ad-hoc request workflow) | W190, W262, W83, W265, W289 |

## Additional Hazardous Materials Requirements (HAZ)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| HAZ-001 | Hazmat Regulatory Change Management & Compliance Update | M | W803 | — |

## Additional HR & Payroll Requirements (HR)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| HR-040 | Employee Referral Program Management & Reward Processing | S | W715 | — |
| HR-041 | Internal Communication & Company-Wide Announcement Management | M | W716 | W504 |
| HR-042 | Workplace Violence Prevention & Response Protocol | M | W717 | W207, W251, W494 |
| HR-043 | Employee Relocation & Housing Assistance Management | S | W718 | W441, W511, W74 |
| HR-044 | Diversity, Equity & Inclusion (DEI) Program Management | M | W719 | W694 |
| HR-045 | Employee Leave Balance Management & Annual Leave Carry-Forward Processing | M | W777 | W10, W34 |
| HR-046 | Employee Benefits Annual Open Enrollment & Plan Selection Management | S | W778 | W10, W504, W716 |
| HR-047 | Store-Level Employee Injury Incident Reporting & Workers' Compensation Claim Processing | M | W779 | W140, W642 |
| HR-048 | Store-Level Employee Uniform & PPE Periodic Issuance & Replacement Processing | M | W780 | W43, W655 |
| HR-049 | Employee Business Travel Request, Approval & Expense Management | M | W815 | W74 |
| HR-050 | Multi-Entity Payroll Consolidation & Cross-Entity Reconciliation | M | W816 | W10, W235, W251, W638, W752 |
| HR-051 | Employee Sabbatical, Study Leave & Secondment Management | S | W817 | W34, W511, W603, W72 |
| HR-052 | Store-Level Employee Daily Attendance Verification & Exception Processing | S | W594 | W10, W34, W561 |
| HR-053 | Store-Level Daily HR Operations & People Management | M | W601 | W34, W10, W511, W561, HR-005, HR-007 |
| HR-054 | Store-Level Labor Cost Monitoring & Overtime Budget Control | S | W602 | W489, W10, HR-010, HR-011 |

## Additional Health & Safety Requirements (HSE)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| HSE-005 | Occupational Health Surveillance & Employee Medical Monitoring | M | W804 | — |
| HSE-006 | Workers' Compensation, SSS/ECC Claims & Return-to-Work Processing | M | W805 | — |
| HSE-007 | Annual Fire Safety System Testing & BFP Compliance | M | W806 | W54, W610 |

## R27. Insurance & Claims Management (INS)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| INS-001 | Store & DC Property Insurance Claim Filing | M | W857 | — |
| INS-002 | Typhoon & Natural Disaster Catastrophic Insurance Claim | M | W858 | — |
| INS-003 | Vehicle & Fleet Insurance Claim Processing | M | W859 | — |
| INS-004 | Business Interruption Insurance Claim & Loss Documentation | S | W860 | — |
| INS-005 | Employee Injury Insurance Claim & SSS/ECC Filing | M | W861 | — |
| INS-006 | Insurance Policy Annual Renewal & Coverage Review | M | W862 | — |
| INS-007 | Third-Party Liability Claim & Customer Incident Response | S | W863 | — |
| INS-008 | Insurance Claim Recovery, Settlement & Accounting | M | W864 | — |

## Additional Inventory Requirements (INV)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| INV-025 | AI/ML Model Governance, Bias Audit & Ethical Review | M | W689 | W200, W201, W203, W208, W618, W647, W359 |
| INV-026 | Digital Transformation Initiative Portfolio Management | S | W690 | W200, W201, W202, W203, W208, W596, W677 |
| INV-027 | Emerging Technology Scouting & Proof-of-Concept Evaluation | S | W691 | W36, W624, W677, W690 |

## Additional Logistics Requirements (LOG)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| LOG-003 | Vehicle Acquisition, Registration, Insurance & Disposal Lifecycle Management | M | W799 | — |

## R25. Loss Prevention & Asset Protection (LP)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| LP-001 | Daily Store Exception-Based Reporting & Transaction Monitoring | M | W837 | — |
| LP-002 | CCTV & Surveillance System Daily Operations & Incident Review | M | W838 | — |
| LP-003 | Internal Theft Investigation & Employee Dishonesty Case Management | M | W839 | — |
| LP-004 | Organized Retail Crime (ORC) Detection & Multi-Store Task Force | M | W840 | — |
| LP-005 | Refund & Return Fraud Detection & Prevention System | M | W841 | — |
| LP-006 | Cash Handling Exception Monitoring & Sweethearting Detection | M | W842 | — |
| LP-007 | Vendor & Delivery Fraud Detection & Dock Security Audit | M | W843 | — |
| LP-008 | Store Entrance/Exit Audit & Electronic Article Surveillance (EAS) | M | W844 | — |
| LP-009 | Shrinkage Analysis, Root Cause Investigation & Reduction Program | M | W845 | — |
| LP-010 | Loss Prevention Training, Awareness & Compliance Program | M | W846 | — |

## Additional Merchandising Requirements (MER)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| MER-008 | Markdown Optimization & Analytics Operations | S | W737 | W161 |
| MER-009 | Vendor Trade Fund Management & Promotional Budget Tracking | S | W738 | W155, W27, W513 |
| MER-010 | Product Phase-Out Inventory Disposition Planning & Execution | M | W830 | W180, W2, W312, W315, W443, W444, W62, W636 |
| MER-011 | Competitor Store Visit Program & Market Intelligence Operations | S | W624 | MDM-030, MER-003 |

## Additional Marketing Requirements (MKT)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| MKT-005 | Marketing Data Platform Daily Operations & Campaign Analytics | S | W736 | — |
| MKT-006 | Marketing Campaign Compliance Review & Regulatory Approval | M | W833 | W126, W149, W170, W289, W427 |

## Additional Maintenance Requirements (MNT)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| MNT-007 | Generator Preventive Maintenance, Fuel Management & Load Testing | M | W808 | W492, W535 |

## Additional Non-Functional Requirements (NFR)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| NFR-037 | Enterprise API Gateway Daily Monitoring & Health Dashboard | M | W733 | — |
| NFR-038 | Data Quality Daily Triage & Remediation Operations | M | W734 | W253, W292, W732 |
| NFR-039 | ERP System Monthly Performance Review & Capacity Planning Update | M | W787 | — |
| NFR-040 | POS Terminal Emergency Swap & Rapid Replacement Protocol | M | W831 | W265, W404, W48 |
| NFR-041 | ERP User Access Quarterly Recertification & Compliance Review | M | W832 | W338, W511 |

## Additional POS & Retail Requirements (POS)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| POS-091 | Store-Level Daily Safety Briefing & Toolbox Talk | S | W720 | W559 |
| POS-092 | Store-Level Vendor Promodizer Floor Activity Coordination | M | W721 | W237, W269, W449, W581 |
| POS-093 | Store-Level Exterior Display & Garden Center Operations | S | W722 | W438, W93 |
| POS-094 | Store-Level Loading Bay Traffic & Truck Queue Management | M | W723 | W575 |
| POS-095 | Store-Level BOPIS Order Aging & Abandoned Pickup Processing | M | W771 | W101, W708, W86 |
| POS-096 | Store-Level Rain Check Issuance for Out-of-Stock Promotional Items | M | W772 | W529, W708 |
| POS-097 | Store-Level Customer Hold & Will-Call Order Management | S | W773 | W708 |
| POS-098 | Store-Level Parking Lot & Exterior Facility Daily Management | S | W774 | W238, W497 |
| POS-099 | Store-Level Customer Loyalty Card Replacement & Account Recovery | S | W775 | W496, W708 |
| POS-100 | Store-Level Product Recall Customer Notification Execution | M | W776 | W12, W29, W617, W627, W708 |
| POS-101 | Store-Level Customer Material Calculator & Quantity Estimation Service | S | W823 | W252, W5 |
| POS-102 | Store-Level Lumber Yard & Outdoor Area Daily Operations | M | W824 | W463, W576, W579, W780 |
| POS-103 | Store-Level Bulky Item Delivery Proof Collection & Documentation | M | W825 | W255, W438, W487, W5, W541 |
| POS-104 | Store-Level Layaway Payment Reminder & Forfeiture Processing | M | W826 | W28, W708 |
| POS-105 | Store-Level Building Material Load Calculation & Safety Advisory | S | W827 | W148 |
| POS-106 | Store-Level Daily Closing Procedure | M | W574 | W5, W71, W272, W517, W541 |
| POS-107 | Store-Level Weekly Sales & Operations Review | S | W575 | W35, W67, W522, W562 |
| POS-108 | Store-Level Typhoon & Severe Weather Preparedness | M | W576 | W49, W111, W330, W428, W580 |
| POS-109 | Store-Level Holiday Season (Ber Months) Operational Ramp-Up | S | W577 | W13, W262, W555 |
| POS-110 | Store-Level Payday Weekend & Peak Day Operational Readiness | S | W578 | W206, W212, W278, W34, W547 |
| POS-111 | Store-Level Daily Equipment & Specialized Fixture Safety Check | M | W579 | W139, W168, W169, W47 |
| POS-112 | Store-Level Emergency Manual Operations Protocol | M | W580 | — |
| POS-113 | Store-Level Vendor Representative Access & Activity Management | S | W581 | W269, W449, W71 |
| POS-114 | Store-Level Fire Drill Execution & Documentation | S | W582 | W141, W330, W476 |
| POS-115 | Store-Level Seasonal Promotional Transition & Display Reset | S | W583 | W13, W181, W262, W523, W554, W63, W86 |
| POS-116 | Store-Level KPI Dashboard & Daily Performance Monitoring | M | W665 | W34, W67, W522, W526, W586 |
| POS-117 | Store-Level Lost & Found Item Management | S | W929 | — |
| POS-118 | Store-Level Customer Comfort Room & Amenity Daily Operations | M | W931 | W47 |
| POS-119 | Customer Product Registration at POS for Vendor Extended Warranty | S | W935 | W911 |
| POS-120 | Store-Level Customer Wheelchair & PWD Mobility Assistance Service | M | W937 | W170, W438, W497 |
| POS-121 | Store-Level Customer Baggage Hold & Parcel Custody Service | S | W941 | W929 |

## Additional Project Management Requirements (PRJ)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| PRJ-001 | Project Change Order Management & Margin Re-Impact Assessment | M | W792 | — |
| PRJ-002 | Project Close-Out, Final Reconciliation & Warranty Handover | M | W793 | — |

## Additional Property Requirements (PROP)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| PROP-001 | Store Closure, Lease Termination & Asset Recovery Management | M | W807 | W117, W43 |

## Additional Procurement Requirements (PUR)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| PUR-039 | Vendor New Product Submission Review & Evaluation Processing | S | W788 | W625, W679, W705 |
| PUR-040 | Vendor Insurance Certificate & Compliance Documentation Tracking | M | W818 | W36, W59, W705, W706 |
| PUR-041 | Vendor Quality Incoming Inspection Failure & Material Review Board | M | W819 | W110, W681, W770, W88, W92 |
| PUR-042 | Vendor Catalog Price Change Intake, Assessment & ERP Synchronization | M | W932 | — |
| PUR-043 | Vendor Managed Inventory (VMI) Periodic Data Accuracy Audit & Reconciliation | S | W938 | — |

## R29. Product Recall Management (RCL)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| RCL-001 | Product Safety Incident Triage & Recall Risk Assessment | M | W873 | — |
| RCL-002 | Product Recall Customer Notification Campaign | M | W874 | — |
| RCL-003 | Product Recall Inventory Quarantine & Disposition | M | W875 | — |
| RCL-004 | Product Recall Regulatory Reporting & Compliance | M | W876 | — |
| RCL-005 | Product Recall Vendor Recovery & Cost Reimbursement | S | W877 | — |
| RCL-006 | Product Recall Effectiveness Audit & Close-Out | M | W878 | — |

## Additional Regulatory Requirements (REG)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| REG-002 | LGU Local Business Tax Computation, Payment & Receipt Management | M | W802 | — |

## Additional Supply Chain Planning Requirements (SCP)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| SCP-015 | Port & Customs Clearance Daily Status Tracking & Escalation | M | W728 | — |
| SCP-016 | Supply Chain Disruption Rapid Response & Escalation Protocol | M | W729 | W60, W670 |
| SCP-017 | DC-to-Store Delivery Route Optimization & Multi-Stop Planning | M | W786 | W199, W431 |
| SCP-018 | Store-Level Replenishment Forecast Accuracy Review & Parameter Tuning | M | W835 | W312 |
| SCP-019 | Supply Chain Cost Analysis & Logistics Optimization Review | S | W680 | W85, W196, W242, W277, W584 |
| SCP-020 | Carrier & Freight Forwarder Daily Performance Monitoring | M | W727 | W304, W500 |

## Additional Service Requirements (SRV)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| SRV-004 | Service SKU Catalog Management, Pricing & Material Linkage | M | W794 | — |
| SRV-005 | Service Customer Complaint, Rework & Warranty Claim Management | M | W795 | W600 |

## R28. Vendor Portal & Supplier Collaboration (VPP)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| VPP-001 | Vendor Portal User Onboarding & Access Provisioning | M | W865 | — |
| VPP-002 | Vendor Self-Service PO Acknowledgment & Confirmation | M | W866 | — |
| VPP-003 | Vendor Self-Service Invoice Submission & Payment Inquiry | M | W867 | — |
| VPP-004 | Vendor Catalog & Product Information Self-Service | S | W868 | — |
| VPP-005 | Vendor Dispute Resolution & Issue Ticketing | M | W869 | — |
| VPP-006 | Vendor Compliance Document Upload & Expiration Tracking | M | W870 | — |
| VPP-007 | Supplier Scorecard Portal Publication & Transparency | S | W871 | — |
| VPP-008 | Vendor RFQ & Bid Submission Portal Management | M | W872 | — |

## Additional Warehouse Management Requirements (WMS)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| WMS-018 | DC Inventory Slotting Optimization & Periodic Re-Slotting Execution | S | W784 | W236, W586, W71 |
| WMS-019 | Vendor Returnable Transport Packaging Reconciliation & Settlement | M | W785 | W106, W22, W3, W7 |
| WMS-020 | DC Workforce Scheduling, Labor Planning & Productivity Tracking | M | W796 | — |
| WMS-021 | DC Security Operations, Perimeter Management & Access Control | M | W797 | — |
| WMS-022 | DC Building Maintenance, Utility Operations & Facility Condition Monitoring | M | W798 | W700 |
| WMS-023 | DC Outbound Load Verification & Pre-Dispatch Quality Check | M | W836 | W106, W109, W199, W236, W463 |

## Additional Wholesale Requirements (WSL)

| Req ID | Requirement | Priority | Primary Workflows | Supporting Workflows |
|---|---|---|---|---|
| WSL-006 | Wholesale Consignment Inventory Management & Settlement | S | W809 | — |
| WSL-007 | Wholesale Backorder Management, Allocation & Customer Communication | M | W810 | — |
| WSL-008 | Wholesale Delivery Proof, Discrepancy Resolution & POD Reconciliation | M | W811 | — |


## Coverage Validation

- **Total requirements**: 728 across 38 distinct requirement-ID prefixes, organized into 32 sections (R1–R32, of which R19–R24 and R32 are gap-closure rounds)
- **Requirements with primary workflow mapping**: All ✅
- **Total workflows referenced**: the core foundational workflows; mappings for the Expansion / Statutory / Gap-analysis value streams (VS-53–VS-192) are added incrementally and remain pending. The full 5,427-workflow / 188-value-stream inventory is in [value-stream-index.md](workflows/value-stream-index.md)
- **Must Have requirements**: 429 (any scored 0 is a disqualifier)
- **Should Have requirements**: 293
- **Nice to Have requirements**: 6

---

*Date: 2026-09-15 (v79 — thirty-seventh-wave consistency review: the BCP section's heading corrected '## R25.' → '## R26.' — the canonical erp-requirements.md scheme holds R25 = Loss Prevention & Asset Protection and R26 = Business Continuity & Disaster Recovery, so the old number duplicated the matrix's own R25 (LP) section and contradicted the register, the fit-gap §5 R-view and this document's own Coverage-Validation '32 sections (R1–R32)' claim; the section's rows are unchanged (BCP-001–BCP-010 = canonical R26 exactly). Heading-numbering + tail-section-population mirror now guarded by validator Check 61. Prior 2026-09-10 (v78 — batch 24: W5574 concessionaire connectivity request, approval & independent-circuit governance added in VS-07.1 (extending the W177 concessionaire lineage), confirmed directly Tier 2; closing inventory line re-pointed 5,426 → 5,427 workflows). Prior 2026-08-26 (v77 — post-catalog batch 5: one workflow-level gap fill mapped — W5510 supplier service-fee billing & account deduction for store-rendered services (barcode labels & promotional collaterals) added to FIN-072's supporting list (VS-15.1); closing inventory line re-pointed 5,362 → 5,363 workflows). Prior 2026-08-26 (v76 — post-catalog batch 4: two workflow-level gap fills mapped — W5508 fringe benefits tax determination/valuation & quarterly BIR 1605 filing added to FIN-031's primary list (VS-79.2) and W5509 unfulfilled-demand & lost-sales capture added to SCP-001's supporting list (VS-02.1); closing inventory line re-pointed 5,360 → 5,362 workflows). Prior 2026-08-25 (v75 — consistency review #28: closing inventory line re-pointed 5,357 → 5,360 workflows (stale from post-catalog batch 3; guarded by validator Check 45); GOV-020 gained the batch-3 concession workflows W5505–W5507). Prior 2026-08-24 (v74 — consistency review #22: removed five exact-duplicate requirement rows (PUR-015 = FIN-019; WSL-002 = CRM-012 + CRM-013; WMS-009/010/011 = WHL-001/002/003 — same titles, same primary workflows); totals now **728 requirements / 429 Must / 293 Should / 6 Nice**). Prior v73 (2026-06-25): VS-127 PA-127.4 added: +1 process area / +8 workflows (W5489–W5496, Plan & Source), specializing the S&OP/IBP consensus cycle for BuildRight's PH-retail context (calamity/typhoon surge, ber-months & summer seasonality, inter-island rebalancing, B2B/trade-project & new-store demand induction, VMI/consignment, DTI/Price-Act mandated price events); totals reconciled to **5,349 workflows / 188 value streams / 569 process areas**; unclassified **2,588 → 2,596**, all carrying a proposed tier (regenerated via classify-workflows.py); pending-mapping range extends to VS-53–VS-192. v72 — Pass 30 added VS-192 Green Fleet Transition, EV Fleet Operations & Sustainable Transportation: +1 value stream / +3 process areas / +24 workflows (W5465–W5488, Make & Move); totals reconciled to **5,341 workflows / 188 value streams / 568 process areas**; unclassified **2,564 → 2,588**, all carrying a proposed tier (regenerated via classify-workflows.py); pending-mapping range extends to VS-53–VS-192. v71 — Pass 26–29 criticality confirmation: 336 VS-178–VS-191 workflows promoted from the keyword proposal into the confirmed register; unclassified reconciled **2,900 → 2,564**, confirmed **2,417 → 2,753** unique (2,440 → 2,776 rows). v70 — consistency review #6: grand total reconciled to **5,317 workflows / 187 value streams**; the pending-mapping range now extends to VS-53–VS-191. v69 — consistency review #4: trimmed the v68 run-on footer (which nested v49–v68 with the "core foundational workflows" boilerplate repeated ~6×, duplicating CHANGELOG) and corrected its stale "unclassified 3,835→3,836" to 2,564 (as of the 2026-06-20 hand-confirmation batches, when the total was 4,981). Requirement-to-workflow mappings currently reference the core foundational workflows; mappings extending to the Expansion / Statutory / Gap-analysis value streams (VS-53–VS-192) are added incrementally. All requirement mappings (728 since v74) reconcile with erp-requirements.md. Per-version history is in [CHANGELOG.md](../CHANGELOG.md).)*
