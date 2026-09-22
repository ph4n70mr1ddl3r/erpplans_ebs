# License Bill of Materials — EBS vs Fusion

> Derived from the model company profile ([`../01-model-company/model-company-profile.md`](../01-model-company/model-company-profile.md))
> and the EBS module footprint ([`module-coverage-map.md`](module-coverage-map.md), [`ebs-platform-architecture.md`](ebs-platform-architecture.md)),
> priced against Oracle's **public global price lists dated September 10, 2026**:
>
> - Oracle E-Business Suite Applications Component Global Price List (perpetual, USD list) —
>   in-repo as [`../applications-price-list-070574.pdf`](../applications-price-list-070574.pdf)
> - Oracle Fusion Cloud Service Global Price List (SaaS, USD list, monthly)
> - Oracle Technology Global Price List (DB tier, for the EBS scenario)
>
> **All prices are US-Dollar list prices before discount.** Oracle enterprise deals commonly close
> 20–50%+ off list (and SaaS on multi-year commitments further below list); this BOM is the
> negotiation baseline, not a budget number. Final counts must be confirmed through an Oracle
> License Determination / SaaS scoping exercise before ordering.
>
> **Version 2.0 — the full-implementation edition.** v1.0 priced the pre-exhaustion footprint.
> The fit-gap register's exhaustion-audit passes then adopted further in-suite products
> (A11 RM&I, A13 L&FM, B11 iExpenses, C9 BOM/WIP, C12 Quality, C15 In-Memory Cost, C17
> Engineering, D3 Credit Management, H11 Internal Controls Manager, plus Project Management);
> this edition licenses **every product the register adopts**, on both the EBS and Fusion
> sides. Rows marked **†** (now Fusion-side only — the v2.8 GPL true-up verified every
> EBS-side row against the in-repo Component GPL) carry part numbers and list prices to be
> confirmed against the Fusion Cloud GPL extract — planning placeholders, not quotes.
> Products that ship included with already-licensed bases carry no line (decision 6).

---

## 1. License basis (from the model company)

| Driver | Value | Source |
|---|---|---|
| Total employees | **6,932** (5,800 store + 600 DC + 532 HQ) | profile §4 |
| ERP authorized (named) users | **3,532** → licensed **3,600** | build-up below |
| — HQ staff | 532 (all 18 departments touch the ERP; 2026-09-18 actual-org gap-fill) | profile §3.3 |
| — Store ERP users | 2,400 = 12/store × 200 (SM, ASM, 4 dept supervisors, 2 receiving clerks, 4 stock associates) | profile §12.1 |
| — DC staff (WMS/RF users) | 600 = 150/DC × 4 | profile §3.2 |
| Peak *concurrent* users | ~1,000–1,500 — **not the license basis**; Oracle "Application User" / "Hosted Named User" are *named*-user metrics | profile §15.3 |
| SKU master | 55,000 records (35,000 active) | profile §6.1 |
| Annual COGS | PHP 42–45B ≈ USD 750–800M @ ₱56/$ (LCM metric) | profile §9.4 |
| Ecommerce orders | ~515,000/yr (≈2.3M OM order lines at ~4.5 lines/order — a derived planning basis, not a profile figure; the profile carries no lines-per-order canon, so confirm the platform's actual line histogram before ordering) | profile §8.5 |
| AR invoices | ~42,000/yr | profile §15.1 |
| Governance/assurance HQ teams (QA/Credit user basis) | Internal Audit & Risk 14 · Quality 5 (+24 DC checkers) · AR & Credit 8 | TO §5.3 |

> **Metric rule that dominates the HRMS lines:** the "Employee" / "Hosted Employee" metric counts
> **all** employees (plus any tracked contractors) — *not* actual users. Every Employee-metric
> product therefore licenses 6,932, even if only managers use it.

### Design decisions embedded in this BOM

1. **POS retail sales post to AR via AutoInvoice + inventory interface — deliberately *not*
   through Order Management.** Routing 134.4M POS line-items/year through OM would require
   ~134.4M Electronic Order Line licenses (~$30.9M list). Only ecommerce order lines (~2.3M/yr)
   are licensed as Electronic Order Lines / Pooled Order Lines. *(Verify this interface design
   with Oracle's licensing team — it is the single largest swing factor in the EBS BOM.)*
2. **Payroll is not licensed in either scenario** — Payroll PH is the in-house build
   (E5–E8); EBS Payroll A74656 is skipped (saves $1.55M + 22% support). Fusion has **no
   Philippine payroll** on the GPL, so the in-house build is retained in the Fusion scenario too.
3. **The Value Chain Planning products the repo adopted (ASCP, Demantra, GOP, Inventory
   Optimization/Rapid Planning) are no longer on the current EBS public GPL** — they require a
   custom quote. The Fusion scenario prices their cloud equivalents (Demand Management,
   Supply Planning, S&OP Cloud). Note EBS OM's *embedded* multi-org ATP covers W56 back-order
   promising without standalone GOP.
4. Employee-metric counts assume **no tracked contractors**; every contractor/agent tracked by
   HR programs adds to the 6,932.
5. **Full-implementation edition:** the BOM now licenses **every product the fit-gap register
   adopts** — the v1.0 footprint plus Lease & Finance Management (A13), Internet Expenses
   (B11), BOM/WIP (C9), Oracle Quality (C12), In-Memory Cost Management (C15), Engineering
   (C17), Credit Management (D3) and Project Management. GOP (D15) rides decision 3's
   custom-quote register. Payroll stays unadopted (decision 2 unchanged). Re-disposition
   executed 2026-09-22 (fit-gap §4 resolution 36): Revenue Management & Invoicing (A11)
   folds into the AR/Financials base per Vision VF-1, and Internal Controls Manager (H11)
   re-dispositions to the in-house Audit & GRC platform build per Vision VF-2 — both former
   lines removed. The 2026-09-22 GPL true-up (v2.8) then verified every remaining EBS-side
   line against the in-repo Component GPL and moved the five adopted products with **no
   Component-GPL SKU** — Credit Management (D3), Oracle Quality (C12), Engineering (C17),
   Project Management and Environmental Accounting & Reporting (H13) — into §2.11's
   custom-quote register (their placeholder lines retired).
6. **Included entitlements ride the base licenses — no separate line:** GL budgets + budgetary
   control (F6), Oracle Alert (G9), AME/Workflow/ERES, AGIS, AR Bills Receivable + Lockbox +
   Balance Forward Billing, AP Bills Payable, Purchasing contingent labor (B13), Shipping +
   Transportation Execution (C14 — OTE is in-suite with Shipping), Install Base, TCA DQM
   (entitlement verify), SLA/eBTax, iSetup + Rapid Clone, BI Publisher/Web ADI/ECC,
   ISG/XML Gateway — and the batch-27 riders: Knowledge Management + Customer Interaction
   History inside the TeleService base (D19/D14), Asset Tracking + iAssets inside the Install
   Base/Inventory bases (F7 — **verify at RFQ: the Component GPL sells Asset Tracking
   separately, `L11496` @ $6,895/AU min 50 — a ~$344,750 minimum if Oracle declines the rider
   claim; coverage register §7 / fit-gap resolution 37**), Report Manager inside GL (H18),
   e-Commerce Gateway inside the EBS base (B14 — verify at RFQ), and the
   procurement/project-procurement ECC dashboards inside the adopted ECC (H5).

---

## 2. Scenario A — Oracle E-Business Suite 12.2 (perpetual, USD list)

### 2.1 Financials

| Product | Part # | Metric | List $/unit | Qty | License $ |
|---|---|---|---:|---:|---:|
| Financials (GL, AP, AR, FA, CE, SLA) | A80561 | Application User | 4,595 | 650 | 2,986,750 |
| Financials — Applications Read-Only User | A76295 | App Read-Only User | 1,725 | 250 | 431,250 |
| Advanced Collections (IEX) | A92235 | Application User | 1,395 | 15 | 20,925 |
| iReceivables | A85986 | 1K Invoice Line | 58 | 200 | 11,600 |
| Treasury | A76322 | Application User | 28,795 | 6 | 172,770 |


*Financials AUs: HQ finance/audit/legal/facilities/QM/LP/IT ≈ 177 + store SM/ASM 400 + DC mgmt 20 = 597, rounded to 650.
Read-only covers merch/store-ops/marketing analytics viewers (cheaper than full AUs).
Credit Management (D3) carries no Component-GPL SKU (2026-09-22 GPL verification) — the
vehicle joins §2.11's custom-quote register; its named users (AR & Credit manager + 2 credit
analysts + AR supervisor + trade-ops credit liaison — TO §5.3; the 5,200-trade + 200-corporate
account base) hold no separate line pending the quote. Re-disposition executed
2026-09-22 (Vision verification VF-1; fit-gap §4 resolution 36): the A11 vehicle is AR's
in-suite Revenue Management capability ('Revenue Management Super User'; program ARBARL),
not a standalone product — the former RM&I line (3,495 × 6 AU = $20,970) is folded into the
AR/Financials base per this BOM's own included-entitlements convention; its users (revenue
accounting manager + 3, project billing 2 — the PFRS-15 schedules for project sales, service
bundles and subscription deferrals, VS-157) ride the Financials AU count above. AGIS, Bills
Receivable/Payable, Lockbox, Balance Forward Billing and GL budgetary control ship inside
the Financials/AR/AP/CE bases — no lines. The 2026-09-23 GPL sweep confirms the read-only
part on the price list itself: `A76295` appears in the Other section's per-product annotation
("Licensed per product for Financials (`A76295`)…", $1,725 per Application Read-Only User —
price and metric match this line).*

### 2.2 Order management, pricing, fulfillment

| Product | Part # | Metric | List $/unit | Qty | License $ |
|---|---|---|---:|---:|---:|
| Order Management (incl. Shipping Execution) | A81406 | Application User | 4,595 | 300 | 1,378,500 |
| Electronic Order Line (ecommerce) | L10128 | Electronic Order Line | 0.23 | 2,500,000 | 575,000 |
| Option: Advanced Pricing (QP) | L30507 | Application User | 2,295 | 25 | 57,375 |
| Configurator (in-store fabrication quotes) | L11093 | Application User | 3,495 | 200 | 699,000 |
| AR Deductions Settlement (Trade Mgmt vehicle) | L72178 | Application User | 8,000 | 25 | 200,000 |
| Option: Channel Rebates & POS Management | L72189 | Application User | 6,000 | 25 | 150,000 |
| Price Protection (vendor price-protection claims on covered inventory — H12) | L72200 | Application User | 3,000 | 20 ⚠ | 60,000 |
| Sales Contracts (sell-side contract spine — D18) | A92469 | Application User | 6,895 | 8 | 55,160 |

*No iStore (deliberately not adopted). Trade Management no longer exists as a product line on the
GPL — VS-39's rebate/claims function maps to the Channel Revenue Management family above.
Configurator processor alternative: A90749 @ $172,500/processor. **GOP (D15)** — adopted as
the multi-org promising engine behind W56/W1114/VS-93 — is not on the current public GPL; it
joins the VCP stack in the custom-quote register (§2.11 note). Shipping + Transportation
Execution (WSH/OTE, C14) ship inside the OM base — no line. Sales Contracts users: trade/corporate
sales desk + project-sales contract administrators (W162/W163; VS-11) — 8 AU (GPL-verified
A92469 @ $6,895, min 5). Price Protection (GPL-verified L72200 @ $3,000 — the placeholder's
$2,295 was wrong) is an option to the AR Deductions Settlement base and minimum-bounds at
20 AU ⚠ (the claims-processing population was 10). The 2026-09-23 GPL sweep adds three
verification items in this family: the Supplier Ship and Debit option (`L72211`, $3,000/AU
min 20) is unlicensed while EDC-10/B10 name the accrual-offer mechanism — RFQ to confirm it
rides the licensed L72178 base + Advanced Pricing; the QP-family EOL component (`L31659`) is
unlicensed beside decision 1's OM EOL line (L10128) — confirm QP-modified ecommerce lines
consume only the OM metric; and the `L72189` option's scope against the coverage register §5
Channel-Rebate record is a naming-collision reconciliation item.*

### 2.3 Logistics & warehouse

| Product | Part # | Metric | List $/unit | Qty | License $ |
|---|---|---|---:|---:|---:|
| Inventory Management | L31544 | Application User | 4,595 | 3,600 | 16,542,000 |
| Option: Mobile Supply Chain Applications (RF) | L31704 | Application User | 1,725 | 2,700 | 4,657,500 |
| Warehouse Management (WMS) | A89486 | Application User | 9,595 | 650 | 6,236,750 |
| Landed Cost Management | L72151 | $M COGS | 350 | 800 | 280,000 |
| Discrete Manufacturing — the BOM/WIP vehicle (kits, bundles, build-to-order — C9) | A81412 | Application User | 4,595 | 50 | 229,750 |
| In-Memory Cost Management for Discrete Industries (real-time costing/margin analytics — C15) | L98184 | Application User | 25,000 | 25 ⚠ | 625,000 |

*INV must cover all WMS/MSCA users. MSCA RF users: store RC/stock/supervisors 2,000 + DC 600
(§1) + QM/IT 50 = 2,650, rounded to 2,700. LCM quantity tracks COGS — grows with revenue (true-up annually). BOM/WIP users:
DC kit/BTO assembly 32 + fabrication leads 15 + private-label line 3 — the GPL vehicle is
Discrete Manufacturing A81412 @ $4,595 (the placeholder's $3,845 'BOM/WIP' SKU does not exist
on the GPL). Oracle Quality (C12) and Engineering (C17) carry no Component-GPL SKU (2026-09-22
GPL verification) — both join §2.11's custom-quote register, the RFQ to confirm whether they
ride the manufacturing-base entitlement (their former user bases — Quality: QM team 5 + DC
checkers 24 + fabrication QC 6 + supplier-quality analysts 5; Engineering: private-label
product development + kit/BOM master governance, W302/W129 — hold no line pending the quote).
IMC is GPL-verified L98184 @ $25,000/AU — the placeholder's $5,750 was wrong — and
minimum-bounds at 25 AU ⚠ (users: logistics & cost finance + merch-finance margin analysts,
15 — W85/W633/VS-101; enterprise BI stays with DP).*

### 2.4 Procurement

| Product | Part # | Metric | List $/unit | Qty | License $ |
|---|---|---|---:|---:|---:|
| Purchasing | A81402 | Application User | 4,595 | 700 | 3,216,500 |
| Option: Sourcing | L31792 | Application User | 9,195 | 40 | 367,800 |
| Option: iSupplier Portal | L31806 | Application User | 9,195 | 10 | 91,950 |
| Option: Procurement Contracts | L31813 | Application User | 6,895 | 30 | 206,850 |
| Option: Services Procurement | L31820 | Application User | 4,595 | 50 | 229,750 |
| iProcurement | L28328 | Application User | 115 | 1,850 | 212,750 |
| Supplier Lifecycle Management | L77741 | Record | 25 | 10,000 ⚠ | 250,000 |
| Internet Expenses (T&E reports + corporate-card program — B11) | A85655 | Expense Report | 6 | 8,000 | 48,000 |

*⚠ minimum-bound at 10,000 records (actual vendor master ~1,000). iSupplier external supplier
users are included with the internal AU licenses. iExpenses: the GPL metric is the Expense
Report (A85655 @ $6, min 1,000), not the Application User — the 657-filer population (all HQ
532 + DC office staff ~100 + district/region field ~25) files ~12 reports/yr ≈ 7,884, licensed
as 8,000 reports per 12-month period (an annual-volume metric — true up with volume).
Contingent labor (B13) ships inside
Purchasing — no separate line.*

### 2.5 Asset lifecycle & real estate

| Product | Part # | Metric | List $/unit | Qty | License $ |
|---|---|---|---:|---:|---:|
| Enterprise Asset Management (eAM) | L39451 | Application User | 4,595 | 60 | 275,700 |
| Option: Self-Service Work Requests | L39457 | Application User | 575 | 250 | 143,750 |
| Property Manager | L16535 | Application User | 4,595 | 15 | 68,925 |
| Lease & Finance Management (lessor leasing + the rental family — A13) | L10090 | $M Managed Assets | 2,300 | 500 ⚠ | 1,150,000 |

*L&FM users: corporate equipment-leasing desk (VS-96) + rental-fleet/service coordinators
(VS-12.2 tool rental, VS-162 self-haul, VS-174 portable storage, VS-186 equipment rental). The
GPL metric is $M Managed Assets (L10090 @ $2,300, min 500), not the Application User the
placeholder assumed — the profile carries no leasing-book/fleet-value canon, so the line
minimum-bounds at 500 ⚠ ($500M of managed assets); size from the desk's and rental fleet's
book value at RFQ (a perpetual true-up, not a re-buy). Asset Tracking carries no line per
decision 6 (F7) — flagged by the 2026-09-23 GPL sweep: the GPL sells it separately (`L11496`
@ $6,895/AU, min 50 ⇒ ~$344,750 if Oracle declines the rider claim); verify the entitlement
at RFQ.*

### 2.6 Service

| Product | Part # | Metric | List $/unit | Qty | License $ |
|---|---|---|---:|---:|---:|
| TeleService (+ Escalation Mgmt) | A85666 | Application User | 4,595 | 50 | 229,750 |
| Service Contracts | A92483 | Application User | 6,895 | 15 | 103,425 |
| Field Service (dispatch core, D13) | A96839 | Field Technician | 3,495 | 100 * | 349,500 |
| Option: Mobile Field Service | L31914 | Field Technician | 1,145 | 100 | 114,500 |
| Option: Advanced Scheduler | L31907 | Field Technician | 1,725 | 100 | 172,500 |
| Depot Repair | A85565 | Application User | 4,595 | 25 | 114,875 |

*\* technician count is an assumption — not stated in the profile; size from the actual
installation/home-service crew roster before ordering. Install Base ships with the OM/Service
family (no separate GPL line). Knowledge Management and Customer Interaction History (with the
Common Application Calendar substrate) ride the TeleService base (batch-27 adoptions D19/D14 —
verify entitlement at RFQ); no lines.*

### 2.7 Projects

| Product | Part # | Metric | List $/unit | Qty | License $ |
|---|---|---|---:|---:|---:|
| Project Costing | A85888 | Application User | 4,595 | 60 | 275,700 |
| Option: Project Billing | L31923 | Application User | 3,495 | 15 | 52,425 |

*Project Management carries no Component-GPL SKU (2026-09-22 GPL verification — UPK content
exists for it, the product does not price): it joins §2.11's custom-quote register, with the
RFQ to confirm whether it rides the Project Costing/Foundation entitlement. Its named users —
corporate PMO (VS-112) + construction/capex project controllers (VS-20/40/109) — hold no
separate line pending the quote.*

### 2.8 HRMS — all Employee-metric @ 6,932

| Product | Part # | List $/emp | License $ |
|---|---|---:|---:|
| Human Resources (PER) | L31953 | 185 | 1,282,420 |
| Self-Service Human Resources | L31958 | 40 | 277,280 |
| Advanced Benefits (OAB) | A92408 | 85 | 589,220 |
| Compensation Workbench | L46808 | 70 | 485,240 |
| iRecruitment | L31969 | 75 | 519,900 |
| Performance Management | L46799 | 105 | 727,860 |
| Time and Labor | A92407 | 110 | 762,520 |
| Succession Planning | L74875 | 70 | 485,240 |
| Learning Management (OLA) | L44374 | 105 | 727,860 |
| ~~Payroll~~ — **not licensed** (in-house Payroll PH) | A74656 | (225) | 0 |

*Metrics per the Component GPL: every row is Employee-metric except Learning Management,
whose GPL metric is the Trainee (any person recorded by the program) — the 6,932 basis
assumes the whole population is recorded in OLA; re-scope at RFQ if only a subset is.
Payroll's $225/employee is shown for the decision-2 record only.*

### 2.9 Master data management

| Product | Part # | Metric | List $/unit | Qty | License $ |
|---|---|---|---:|---:|---:|
| Product Hub | L42168 | Record | 14 | 60,000 | 840,000 |
| Product Hub Data Steward | L42140 | Application User | 5,795 | 20 | 115,900 |
| Site Hub | L69431 | Record | 200 | 1,000 ⚠ | 200,000 |
| Site Hub Add-On for EBS | L69447 | Record | 100 | 1,000 | 100,000 |
| Site Hub Data Steward | L69463 | Application User | 5,795 | 1 | 5,795 |
| Customer Hub Steward — Customer Data Librarian + Customers Online (TCA steward surface — D20) | L42119 | Application User | 5,795 | 10 ⚠ | 57,950 |

*Customer master is TCA inside EBS Financials — no Customer Hub *record* licensing needed for
the master itself; the batch-27 steward adoption (D20) licenses the Customer Hub *steward* SKU
for the CDL/Customers Online console (W253 dedup workbench; VS-29.2 governance) — the named
steward population is 4, GPL-verified as L42119 @ $5,795 with a 10-AU SKU minimum ⚠ (the line
minimum-bounds at 10). ⚠ minimum-bound. TCA DQM dedup (W253): if the built-in TCA DQM is deemed insufficient, Enterprise Data Quality
Standardization & Match (L99899) is $275,000/processor min 4 = $1.1M — **verify entitlement
before budgeting**; not included in the totals below (the sweep's other EDQ SKUs — `L94196`,
`L90986` — join the same verify-only posture, coverage register §7). Product Hub Add-on
(`L42175`) flagged by the same sweep — the Site Hub precedent licenses its EBS add-on
(`L69447`); confirm whether the licensed Product Hub (L42168) requires it. The Supplier Hub
family and the Customer Hub B2B/B2C families are recorded not-needed (coverage register §7).*

### 2.10 Governance & controls (full-implementation)

| Product | Part # | Metric | List $/unit | Qty | License $ |
|---|---|---|---:|---:|---:|
| Incentive Compensation (sales-commission & trade-incentive plans, crediting, calculation, payout — H14) | A80531 | Compensated Individual | 750 | 10 ⚠ | 7,500 |

*Re-disposition executed 2026-09-22 (Vision verification VF-2; fit-gap §4 resolution 36): the former
Internal Controls Manager line (2,875 × 45 AU = $129,375; users: Internal Audit & Risk 14 + finance
process owners 21 + business control owners 10) is removed — ICM/AMW is registered '(Obsolete)' with no
installation record on either installation of record, and the audit-management/GRC surface re-houses
onto the in-house Audit & GRC platform build (fit-gap H11 → BUILD), hosting the CTL-01–808 register on
BuildRight infrastructure with the EBS evidence layer (FND audit, ERES, AME logs) unchanged.
Oracle Alert (G9) rides the base applications; GL budgets/budgetary control (F6) rides GL —
no lines. The 2026-09-22 GPL verification trued OIC to the Compensated Individual metric
(A80531 @ $750, min 10 — the placeholder's $3,495/AU was wrong): the named compensated
population is the Trade/Account Management desk of 7 (TO §5.1; store/branch incentives ride
payroll, not OIC), so the line minimum-bounds at 10 Compensated Individuals ⚠. Environmental
Accounting & Reporting (H13) carries no Component-GPL SKU — it joins §2.11's custom-quote
register.*

### 2.11 Scenario A totals

| | USD list |
|---|---:|
| **Perpetual license total** | **$50,228,665** |
| Annual SUL&S (22%) | $11,050,306/yr |
| 3-yr TCO (license + 3× support) | $83,379,583 |
| 5-yr TCO (license + 5× support) | **$105,480,195** |

*Full-implementation delta vs v1.0: **+$708,130** of perpetual license (+$155,789/yr support)
across the ten newly licensed products — ~1.5% of the license base; the 2026-09-18 actual-org
gap-fill adds a further **+$32,120** of perpetual (+$7,066/yr support: HRMS re-based to 6,932
employees, ICM 40 → 45 with Internal Audit & Risk 14) and the 2026-09-21 batch-27
documentation-coverage adoptions a further **+$51,140** of perpetual (+$11,251/yr support:
Sales Contracts 8 AU §2.2, Customer Hub Steward 4 AU §2.9) across two more † lines; and the
2026-09-22 re-disposition removes **−$150,345** of perpetual (−$33,076/yr support: the A11
RM&I line −$20,970 folded into the AR/Financials base per Vision VF-1, the §2.10 ICM line
−$129,375 re-housed onto the in-house Audit & GRC platform build per Vision VF-2) — ranking
vs Fusion is unchanged.*

*2026-09-22 GPL true-up (v2.8): every EBS-side line verified against the in-repo Component
GPL — eight part numbers filled, five placeholder lines retired to the custom-quote register,
three metrics trued (iExpenses → Expense Report, L&FM → $M Managed Assets, OIC → Compensated
Individual), the BOM/WIP placeholder trued to its real GPL vehicle (Discrete Manufacturing
A81412), two placeholder prices corrected (IMC $5,750 → $25,000; Price Protection
$2,295 → $3,000) and four SKU minimums enforced (Price Protection 20 AU, IMC 25 AU, L&FM
500 $M, steward/OIC 10) — net **+$1,516,325** of perpetual (+$333,591/yr support, +3.11%),
dominated by the L&FM metric change (+$1,113,240) and IMC's price-plus-minimum (+$538,750)
against the five retired placeholders (−$194,760), the OIC metric saving (−$44,925) and the
iExpenses metric saving (−$32,500); ranking vs Fusion unchanged.*

***Custom-quote register (adopted, unpriced — excluded from the totals):** the EBS-family
Value Chain Planning stack — ASCP, Demantra, Inventory Optimization/Rapid Planning (C5) — and
**Global Order Promising** (D15) are off the current public GPL; budget placeholder $2–4M
perpetual pending the Oracle VCP quote. The 2026-09-22 GPL verification adds five adopted
products with **no Component-GPL SKU** to the same register — Credit Management (D3), Oracle
Quality (C12), Engineering (C17), Project Management and Environmental Accounting & Reporting
(H13): each prices only by custom quote or rides an unverified base entitlement (confirm at
RFQ; planning placeholder ~$0.3–0.6M perpetual combined). Payroll A74656 remains unadopted — reversing decision 2
would add $225/emp × 6,932 = **$1,559,700** (+$343,134/yr support).*

*2026-09-23 GPL sellable-SKU sweep (coverage register §7): every distinct priced part number
on the in-repo Component GPL now carries a recorded disposition — licensed, recorded at a
prior pass, or recorded not-needed in the sweep table (307 = 55 + 7 + 11 + 234; 0 unexamined).
Contingency flags carried in place, no totals moved: `A76295` verified as the Other section's
per-product read-only annotation (§2.1 note); Asset Tracking `L11496` rider entitlement
(decision 6; §2.5 note); Supplier Ship and Debit `L72211` and the QP EOL component `L31659`
(§2.2 note); Product Hub Add-on `L42175` (§2.9 note); the `L72189` naming-collision
reconciliation (§2.2 note).*

### 2.12 Technology stack (EBS scenario — illustrative, from Technology GPL)

EBS 12.2 includes a restricted-use WebLogic Server (no separate WLS license for EBS use);
BI Publisher, FSG and Enterprise Command Centers are included with the applications. The Oracle
Database tier is licensed separately (per-processor, core factor 0.5 on x86):

| Product | Part basis | List $/proc | Illustrative qty |
|---|---|---:|---:|
| Database Enterprise Edition | (tech GPL) | 950 | 64 (32 prod RAC + 32 DR/non-prod) |
| Real Application Clusters | option | 460 | 32 |
| Active Data Guard | option | 230 | 32 |
| Partitioning | option | 230 | 32 |
| Diagnostics Pack | option | 150 | 64 |
| Tuning Pack | option | 100 | 64 |

*≈ $0.15–0.25M perpetual depending on final architecture — small next to the application layer,
but quantity depends entirely on the DB server sizing (architecture §4).*

---

## 3. Scenario B — Oracle Fusion Cloud (SaaS, USD list, monthly per unit)

### 3.1 Option B1 — à-la-carte Fusion Cloud Applications

| Service | Part # | Metric | List $/mo | Qty | $/month |
|---|---|---|---:|---:|---:|
| Fusion ERP Cloud (Financials, Procurement, Projects) | B91079 | Hosted Named User | 625 | 1,000 | 625,000 |
| Fusion Procurement Self-Service (requesters) | B91083 | Hosted Named User | 8 | 2,000 | 16,000 |
| Fusion Risk Management (the H11 audit/GRC surface's Fusion-side equivalent) | B91081 | Hosted Named User | 180 | 60 | 10,800 |
| Fusion Product Management (items) | B91056 | Hosted Named User | 500 | 100 | 50,000 |
| Fusion Product Management Reviewer | B95242 | Hosted Named User | 100 | 100 | 10,000 |
| Fusion Order Management (power users) | B93429 | Hosted Named User | 875 | 75 | 65,625 |
| Fusion OM — Pooled Order Lines (ecommerce) | B111914 | 10K lines/mo | 625 | 20 | 12,500 |
| Fusion Supply Chain Execution (ship/receive) | B91057 | Hosted Named User | 350 | 450 | 157,500 |
| Fusion Advanced Inventory Management | B111756 | Hosted Named User | 200 | 3,200 | 640,000 |
| WMS Enterprise (DC execution) | B90536 | Hosted Named User | 550 | 620 | 341,000 |
| Fusion Demand Management (Demantra eq.) | B91060 | Hosted Named User | 1,250 | 10 | 12,500 |
| Fusion Supply Planning (ASCP eq.) | B91059 | Hosted Named User | 1,250 | 10 | 12,500 |
| Fusion S&OP Cloud | B91061 | Hosted Named User | 625 | 15 | 9,375 |
| Fusion Enterprise Contracts | B86732 | Hosted Named User | 150 | 30 | 4,500 |
| Fusion Supply Chain Collaboration (iSupplier eq.) | B87862 | Hosted Named User | 625 | 20 | 12,500 |
| Fusion CPQ (Configurator eq., in-store quotes) | B111751 | Hosted Named User | 240 | 200 | 48,000 |
| Fusion HCM Base (Global HR/absence/benefits) | B85800 | Hosted Employee | 15 | 6,932 | 103,980 |
| Fusion Time and Labor | B75365 | Hosted Named User | 3 | 3,000 | 9,000 |
| Fusion Workforce Compensation (CWB eq.) | B109620 | Hosted Comp. Individual | 4 | 6,932 | 27,728 |
| Fusion Learning (OLA eq.) | B85242 | Hosted Named User | 5 | 6,932 | 34,660 |
| Fusion Recruiting (iRecruitment eq.) | B87675 | Hosted Employee | 8 | 6,932 | 55,456 |
| Fusion Talent Management (perf + succession) | B94925 | Hosted Named User | 7 | 6,932 | 48,524 |
| Field Service Cloud (dispatch core, D13) | B110413 | Pooled Named User | 225 | 360 ⚠ | 81,000 |
| Fusion Revenue Management (Receivables-Revenue-Management eq., PFRS 15 — A11) | TBD † | Hosted Named User | 150 | 6 | 900 |
| Fusion Quality Management (Oracle Quality eq. — C12) | TBD † | Hosted Named User | 200 | 40 | 8,000 |
| Fusion Global Order Promising (GOP eq. — D15) | TBD † | Hosted Named User | 425 | 10 | 4,250 |
| Fusion Transportation Management (OTE eq., freight audit — C14) | TBD † | Hosted Named User | 650 | 25 | 16,250 |
| **Total** | | | | | **$2,417,548/mo** |

**B1 totals: $29,010,576/yr · $87,031,728 (3-yr) · $145,052,880 (5-yr)**

*⚠ Field Service Cloud minimum-bound at 360 pooled users (~100 techs assumed).
Full-implementation parity: Risk Management 20 → 60 (audit + process/control owners hosting
the 808-control register); Revenue/Quality/GOP/Transportation added. Riding the base
entitlements (verify): Expenses & Credit inside ERP Financials; costing & PLM change orders
inside SCM/Product Management; Channel Revenue Management (vendor rebates) inside Order
Management.*

### 3.2 Option B2 — Fusion Suite bundle (36-month minimum term, no mix-and-match)

The Fusion Suite bundle ($330/professional-user + $5/employee) covers the ERP+SCM+HCM bases and
is ~20% cheaper than à-la-carte at this footprint, but planning products, WMS, CPQ and Field
Service are *not* in the bundle and price as add-ons:

| Service | Part # | Metric | List $/mo | Qty | $/month |
|---|---|---|---:|---:|---:|
| Fusion Suite Professional (ERP+SCM+HCM bases) | B108674 | Hosted Named User | 330 | 3,600 | 1,188,000 |
| Fusion Suite Employee (self-service tier) | B108675 | Hosted Employee | 5 | 3,332 | 16,660 |
| Fusion Demand Management | B91060 | Hosted Named User | 1,250 | 10 | 12,500 |
| Fusion Supply Planning | B91059 | Hosted Named User | 1,250 | 10 | 12,500 |
| Fusion S&OP Cloud | B91061 | Hosted Named User | 625 | 15 | 9,375 |
| Fusion Time and Labor | B75365 | Hosted Named User | 3 | 3,000 | 9,000 |
| Fusion Learning | B85242 | Hosted Named User | 5 | 6,932 | 34,660 |
| Fusion Recruiting | B87675 | Hosted Employee | 8 | 6,932 | 55,456 |
| Fusion Talent Management | B94925 | Hosted Named User | 7 | 6,932 | 48,524 |
| Fusion Workforce Compensation | B109620 | Hosted Comp. Individual | 4 | 6,932 | 27,728 |
| WMS Enterprise add-on | B90536 | Hosted Named User | 550 | 620 | 341,000 |
| Fusion CPQ add-on | B111751 | Hosted Named User | 240 | 200 | 48,000 |
| Field Service Cloud add-on | B110413 | Pooled Named User | 225 | 360 | 81,000 |
| Fusion Risk Management add-on (the H11 audit/GRC eq.) | B91081 | Hosted Named User | 180 | 60 | 10,800 |
| Fusion Revenue Management add-on (A11) | TBD † | Hosted Named User | 150 | 6 | 900 |
| Fusion Quality Management add-on (C12) | TBD † | Hosted Named User | 200 | 40 | 8,000 |
| Fusion Global Order Promising add-on (D15) | TBD † | Hosted Named User | 425 | 10 | 4,250 |
| Fusion Transportation Management add-on (C14) | TBD † | Hosted Named User | 650 | 25 | 16,250 |
| **Total** | | | | | **$1,924,603/mo** |

**B2 totals: $23,095,236/yr · $69,285,708 (3-yr) · $115,476,180 (5-yr)**

*Suite Employee tier = the employee population outside the professional tier: 6,932 − 3,600 =
3,332 (§1 drivers; the §1 Employee-metric rule governs the HRMS product lines, not this bundle
tier, which is a complement by construction). The bundle's ERP+SCM+HCM bases already cover
Expenses, Credit, costing and PLM change orders; Risk, Revenue, Quality, GOP and Transportation
Management sit outside the bundle and price à-la-carte as add-ons.*

### 3.3 Fusion functional gaps vs the EBS footprint (quote/decide)

- **No Maintenance/eAM equivalent on the GPL** — Fusion Maintenance would need a custom quote,
  or facility PM stays on the fleet/CMMS build side.
- **No Property Manager equivalent** — lease administration (W117–W119) has no Fusion SKU on
  this list; stays EBS-only or process-owned.
- **No Lease & Finance Management equivalent** — the lessor/rental lifecycles (VS-96/162/174/186)
  have no Fusion SKU on this list; process-owned or custom quote in the Fusion scenario.
- **No Philippine payroll** — Payroll PH in-house build retained (same as EBS scenario).
- **Store workforce scheduling** — in-house build retained (Workforce Scheduling Cloud exists
  at $7/HNU if ever consolidated).
- **Full-implementation parity adds († verify against the GPL extract):** Fusion Revenue
  Management (A11), Quality (C12), Global Order Promising (D15), Transportation Management
  (C14/OTE parity) and the Risk Management bump 20 → 60 (the H11 audit/GRC surface's
  Fusion-side counterpart) — modeled as
  explicit lines in B1/B2 above; vendor rebates assumed inside Fusion OM's Channel Revenue
  Management entitlement.
- WMS Enterprise is the largest avoidable line ($4.1M/yr): running DC RF execution on
  Advanced Inventory/SCE mobile (instead of full WMS Enterprise) drops it — at the cost of
  slotting/labor/yard/cartonization parity with the repo's in-suite WMS decision.

---

## 4. Comparison & recommendations

| Scenario | Up-front | Annual | 3-yr list TCO | 5-yr list TCO |
|---|---:|---:|---:|---:|
| **A — EBS 12.2 perpetual + 22% SUL&S** | $50.23M | $11.05M (support) | $83.4M | $105.5M |
| **B1 — Fusion Cloud à-la-carte** | — | $29.01M | $87.0M | $145.1M |
| **B2 — Fusion Suite bundle (36-mo)** | — | $23.10M | $69.3M | $115.5M |

1. **At list price, EBS is cheapest over 5 years** (~$105.5M vs $115.5M Suite / $145.1M
   à-la-carte) and becomes more so after year 5 (support-only vs perpetual subscription).
   The EBS cash profile is also front-loaded — relevant at ~PHP 62B revenue. The
   full-implementation delta (v1.0 → v2.0: +$708K EBS license; +$0.44–0.48M/yr Fusion) does
   not change the ranking.
2. **The swing factors dwarf the scenario deltas** — the POS→AR-vs-OM posting decision
   (±$31M of EOL licenses), WMS user counts, the minimum-bound lines (SLM, Site Hub, Field
   Service Cloud), and OLA/Learning scoping. Nail these before comparing vendors.
3. **The adopted planning stack is unpriceable from the current EBS GPL** (ASCP/Demantra/GOP/
   Inventory Optimization removed) — either obtain a VCP quote, rely on OM-embedded ATP +
   min-max + the DP platform, or price Fusion planning (already modeled above).
4. **Negotiation levers:** Fusion Suite bundle (already modeled, 36-mo), EBS license nets
   typically 20–50% off list with support capped; the Employee-metric HRMS block (~$5.8M
   license + $1.3M/yr support) is the natural discount anchor; Performance/Succession/Learning
   (≈$1.9M license) could be deferred or replaced by the in-house builds if adoption is thin.
5. All quantities include a ~3% growth buffer but assume 200 stores / 6,932 employees —
   growing to 300 stores adds ~1,200 store users (+INV/MSCA/iProc/iExpenses-class licenses)
   and is **metric-true-up free on EBS perpetual** but re-priced every renewal on Fusion.

---

*Document Version: 2.10 | Date: 2026-09-23 | **GPL sellable-SKU sweep flags (coverage register §7).** The price-list direction completed in the coverage register — every distinct priced part number on the in-repo Component GPL now carries a recorded disposition (307 = 55 licensed + 7 read-only-annotation + 11 prior + 234 annexed; 0 unexamined) — and the sweep's four entitlement flags land on this BOM without moving a line item, quantity, price, scenario total or §4 cell: decision 6's Asset Tracking + iAssets rider now carries the verify-at-RFQ flag (the GPL sells Asset Tracking separately, `L11496` @ $6,895/AU min 50 ⇒ ~$344,750 if Oracle declines the rider claim; the §2.5 note mirrors it); the §2.2 note gains the Supplier Ship and Debit flag (`L72211` unlicensed while EDC-10/B10 name the accrual-offer mechanism — confirm it rides the licensed L72178 base + Advanced Pricing), the QP-EOL component flag (`L31659` beside decision 1's L10128) and the `L72189` naming-collision reconciliation against coverage §5's Channel-Rebate record; the §2.9 note gains the EDQ verify-only posture extension (`L94196`/`L90986`) and the Product Hub Add-on flag (`L42175` — the Site-Hub `L69447` precedent); the §2.1 note gains the A76295 annotation confirmation (the part exists as the Other section's per-product read-only annotation — price and metric verify; no line change); and §2.11 gains the sweep-pointer paragraph. A-vs-B ranking unchanged. Guard: `gpl_sku_sweep_hits` re-derives the coverage register's §7 arithmetic, part-number universe, flag pins and the UPK band count from the price-list PDF every run; the existing licensing_bom_hits arms untouched. Prior v2.9 | Date: 2026-09-22 | **Sixty-fifth-wave review (the Fusion parity tags' retired ICM anchor).** The two Fusion Risk Management line tags (B1 §3.1 and the B2 add-on) and the §3 parity note still anchored on the retired EBS product name ('GRC/ICM equivalent — ICM parity', 'ICM eq.', 'ICM parity') — the VF-2 re-disposition retired ICM/AMW as a vehicle (registered '(Obsolete)', no installation record on either installation of record; the H11 vehicle of record is the in-house Audit & GRC platform), and the same-day VF-1 pass had already re-worded the sibling Fusion Revenue Management tag to its surviving vehicle ('Receivables-Revenue-Management eq.') — the three tags trued to the H11 capability naming ('the H11 audit/GRC surface's Fusion-side equivalent' / 'the H11 audit/GRC eq.' / 'the H11 audit/GRC surface's Fusion-side counterpart'). No line item, quantity, price, scenario total or §4 cell changed; the EBS scenario untouched. Guard: licensing_bom_hits gains the retired-anchor arm (the 'ICM parity'/'ICM eq.' forms banned on the footer-stripped body, the H11-anchored tag forms required). Prior v2.8 | Date: 2026-09-22 | **Component-GPL true-up (the in-repo price list).** Every EBS-side line verified against `applications-price-list-070574.pdf` (Oracle E-Business Suite Applications Component Global Price List, September 10, 2026): eight † part numbers filled and verified — Price Protection L72200 $3,000 (was a 2,295 placeholder; minimum-bound 20 AU), Sales Contracts A92469 $6,895 (was 3,495), BOM/WIP trued to its real GPL vehicle Discrete Manufacturing A81412 $4,595 (the 3,845 placeholder SKU does not exist), In-Memory Cost Management L98184 $25,000 (was 5,750; minimum-bound 25 AU), Lease & Finance Management L10090 re-metriced to $2,300 per $M Managed Assets (minimum-bound 500 — no fleet-book canon in the profile), Internet Expenses A85655 re-metriced to $6 per Expense Report (8,000 reports/yr ≈ the 657 filers × ~12), Customer Hub Steward L42119 $5,795 confirmed (minimum-bound 10 AU), Incentive Compensation A80531 re-metriced to $750 per Compensated Individual (minimum-bound 10 — the named compensated population is the Trade/Account Management desk of 7, TO §5.1); five adopted products with no Component-GPL SKU retired from the line tables into §2.11's custom-quote register (Credit Management D3, Oracle Quality C12, Engineering C17, Project Management, EAR H13 — RFQ to confirm base-entitlement rides); §2.8 gains the Trainee-metric note for Learning Management. Scenario A $48,712,340 → **$50,228,665** (+$1,516,325, +3.11%) with support/3-yr/5-yr restated ($11,050,306/yr; $83,379,583; $105,480,195) and the §4 cells re-derived at their stated rounding ($48.71M → $50.23M, $10.72M → $11.05M, $80.9M → $83.4M, $102.3M → $105.5M); A-vs-B ranking unchanged (EBS still cheapest at 5 years). Prior v2.7 | Date: 2026-09-22 | **Vision-findings re-disposition (fit-gap §4 resolution 36).** Two lines removed and totals re-derived — the §2.1 Revenue Management & Invoicing line (−$20,970) folds into the AR/Financials base per Vision VF-1 (the A11 vehicle is AR's 'Revenue Management Super User'/ARBARL capability, not a standalone product), and the §2.10 Internal Controls Manager line (−$129,375) re-houses onto the in-house Audit & GRC platform build per Vision VF-2 (AMW registered '(Obsolete)', no installation record on either installation of record; fit-gap H11 → BUILD); decision 5's adopted-product set re-stated, the §1 governance-teams driver row's label trued (QA/Credit basis) and the §3.1 Fusion parity line's tag re-worded. Scenario A $48,862,685 → $48,712,340 (−$150,345, −0.31%) with support/3-yr/5-yr restated and the §4 cells re-derived at their stated rounding ($48.86M → $48.71M, $10.75M → $10.72M, $81.1M → $80.9M, $102.6M → $102.3M); A-vs-B ranking unchanged. Prior v2.6 | Date: 2026-09-21 | **Batch-27 documentation-coverage adoptions.** Two separately licensed products join the BOM as † lines pending GPL verification — Sales Contracts (§2.2, 8 AU: trade/corporate sales desk + project-sales contract administrators per W162/W163/VS-11) and Customer Hub Steward for the Customer Data Librarian + Customers Online console (§2.9, 4 AU: the W253 dedup workbench stewards; the §2.9 note trued to distinguish master-record licensing from the steward SKU) — moving Scenario A $48,811,545 → $48,862,685 (+$51,140, +0.10%) with support/3-yr/5-yr restated and the §4 cells re-derived at their stated rounding ($48.81M → $48.86M, $10.74M → $10.75M, $81.0M → $81.1M, $102.5M → $102.6M); A-vs-B ranking unchanged. Five products ride already-licensed bases and carry no line per decision 6 — Knowledge Management + Customer Interaction History inside TeleService (D19/D14), Asset Tracking + iAssets inside the Install Base/Inventory bases (F7), Report Manager inside GL (H18), e-Commerce Gateway inside the EBS base (B14, verify at RFQ), and the procurement/project-procurement ECC dashboards inside the adopted ECC (H5); the VCP custom-quote scope componentized per C5 (in: VCP Collections, AIA pack, APCC; out: Collaborative Planning/SNO/SPP/IM-PDP). FAH not adopted — the AutoInvoice architecture of record stands (A10; BOM decision 1's licensing-verification flag intact). Prior v2.5 | Date: 2026-09-21 | **Sixty-second-wave consistency review (derived-cell arithmetic — the §2.11 5-yr TCO off-by-one).** The 5-yr TCO stated **$102,504,244** against the section's own stated components — perpetual $48,811,545 + 5 × the stated $10,738,540 support = **$102,504,245**; the licensing_bom_hits chain arm re-derived the cell from the ×2.1 license approximation at ±1.5 tolerance (the product 102,504,244.5 straddles both integers), so the off-by-one shipped through the batch-26 restatement undetected. Cell trued; the chain arm tightened to the exact derivation from the stated support cell (tolerance ±0.5), so a TCO cell can no longer disagree with its own row's components. No line item, quantity, support, 3-yr or §4 rounding cell changed ($102.5M holds at the stated 1-dp); A-vs-B ranking unchanged. Prior v2.4 | Date: 2026-09-21 | **EBS documentation-coverage adoptions (batch 26).** The inward-direction register's six highest-confidence closures (fit-gap H12–H17) reach the BOM: three are separately licensed and gain lines — Price Protection (§2.2, 10 AU), Incentive Compensation and Environmental Accounting & Reporting (§2.10, 15 AU and 8 AU) — all † planning placeholders pending GPL verification; three ride already-licensed bases and carry no line per decision 6 — Bill Presentment Architecture inside Receivables, E-Business Tax Reporting inside E-Business Tax, and Copy Inventory Organization inside Inventory. Scenario A moves $48,717,810 → $48,811,545 (+$93,735, +0.19%) with support/3-yr/5-yr restated and the §4 comparison cells re-derived at their stated rounding ($48.72M → $48.81M, $10.72M → $10.74M, $80.9M → $81.0M, $102.3M → $102.5M); the A-vs-B ranking is unchanged and Fusion parity for these three is deferred to the next Fusion pass. Prior v2.3 | Date: 2026-09-21 | **Sixtieth-wave consistency review (gap-fill straggler — the derived employee cell):** the v2.2 re-base moved every cell that states the employee total as a literal but missed the one that derives it by arithmetic — §3.2's Fusion Suite Employee (self-service tier) quantity, the complement of the professional tier, still stood at 3,311 = 6,911 − 3,600 under the retired headcount canon; re-based to 3,332 = 6,932 − 3,600 (+$105/mo), moving the B2 monthly total $1,924,498 → $1,924,603 and its bold chain to $23,095,236/yr · $69,285,708 (3-yr) · $115,476,180 (5-yr), with the §4 comparison cell re-derived at its stated rounding ($23.09M → $23.10M; the 3-yr/5-yr cells hold at $69.3M / $115.5M and the A-vs-B ranking is unchanged). §3.2 gains the explicit footing clause the §2 build-up notes already carry, so the complement is stated rather than implied. No other line item, quantity, price or total changed; Scenario A and B1 untouched. Prior v2.2 | Date: 2026-09-18 | **Actual-org gap-fill re-base (+$32,120 EBS perpetual; B1/B2 employee-metric rows):** the 2026-09-18 HQ gap-fill (511 → 532; IA 14) re-based every employee-derived cell — §1 drivers (HQ staff 532, ERP named users 3,532 → licensed 3,600, governance teams IA 14), §2.1 Financials-AU footing (≈ 177 + 400 + 20 = 597, rounded to 650), §2.1 iExpenses footing (all HQ 532 + ~100 + ~25 = 657, rounded to 700), §2.8 HRMS @ 6,932 employees (+$17,745), §2.10 ICM 40 → 45 (+$14,375) — moving the Scenario-A base $48,685,690 → $48,717,810 and B1/B2 to $2,417,548 / $1,924,498 per month; §4 comparison cells re-derived at their stated rounding. Prior v2.1 (2026-09-17) | **Fifty-fourth-wave consistency review (driver/note footing):** the surfaces the §2–§3 line-item re-derivations cannot read trued — §1's ecommerce driver now states the derived basis its order-line pricing rides (≈2.3M OM order lines at ~4.5 lines/order; the profile carries no lines-per-order canon — confirm the line histogram before ordering), §2.1's Financials AU build-up carries its explicit footing (= 592, rounded to 650 — the iExpenses rounding convention the note had silently omitted), and §2.3's MSCA RF build-up is trued to §1's own DC driver (DC 600 per §1, not 550; = 2,650, rounded to 2,700) — no line-item, quantity or total change, EBS/Fusion scenarios untouched. Prior v2.0 (full-implementation edition) | Date: 2026-09-17 | **v2.0 delta:** licenses the exhaustion-audit adoptions — EBS: RM&I (A11), L&FM (A13), iExpenses (B11), BOM/WIP (C9), Quality (C12), In-Memory Cost (C15), Engineering (C17), Credit Management (D3), Internal Controls Manager (H11), Project Management; Fusion: Risk 20 → 60, Revenue, Quality, GOP, Transportation Management — moving the EBS license base $47,977,560 → $48,685,690 and B1/B2 to $2,416,729 / $1,923,994 per month; † part numbers/prices pending GPL verification; GOP added to the VCP custom-quote register. Prior v1.0 (2026-09-17): initial issue. Sources: model-company-profile.md (§3, §4, §8, §9, §12, §15); module-coverage-map.md v2.0; ebs-platform-architecture.md v2.0 §2; fit-gap-analysis.md §2; optimal-table-of-organization.md §5.3; Oracle E-Business Suite Applications Component Global Price List 2026-09-10 (in-repo: `applications-price-list-070574.pdf`); Oracle Fusion Cloud Service Global Price List 2026-09-10; Oracle Technology Global Price List 2026-09-10. Prices are US-Dollar list, subject to change without notice; quantities are planning estimates pending an Oracle License Determination.*
