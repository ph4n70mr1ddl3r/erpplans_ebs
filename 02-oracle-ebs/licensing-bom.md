# License Bill of Materials — EBS vs Fusion

> Derived from the model company profile ([`../01-model-company/model-company-profile.md`](../01-model-company/model-company-profile.md))
> and the EBS module footprint ([`module-coverage-map.md`](module-coverage-map.md), [`ebs-platform-architecture.md`](ebs-platform-architecture.md)),
> priced against Oracle's **public global price lists dated September 10, 2026**:
>
> - Oracle E-Business Suite Applications Component Global Price List (perpetual, USD list)
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
> sides. Rows marked **†** carry part numbers and list prices to be confirmed against the
> current GPL extract — planning placeholders, not quotes. Products that ship included with
> already-licensed bases carry no line (decision 6).

---

## 1. License basis (from the model company)

| Driver | Value | Source |
|---|---|---|
| Total employees | **6,911** (5,800 store + 600 DC + 511 HQ) | profile §4 |
| ERP authorized (named) users | **3,511** → licensed **3,600** | build-up below |
| — HQ staff | 511 (all 18 departments touch the ERP) | profile §3.3 |
| — Store ERP users | 2,400 = 12/store × 200 (SM, ASM, 4 dept supervisors, 2 receiving clerks, 4 stock associates) | profile §12.1 |
| — DC staff (WMS/RF users) | 600 = 150/DC × 4 | profile §3.2 |
| Peak *concurrent* users | ~1,000–1,500 — **not the license basis**; Oracle "Application User" / "Hosted Named User" are *named*-user metrics | profile §15.3 |
| SKU master | 55,000 records (35,000 active) | profile §6.1 |
| Annual COGS | PHP 42–45B ≈ USD 750–800M @ ₱56/$ (LCM metric) | profile §9.4 |
| Ecommerce orders | ~515,000/yr (≈2.3M OM order lines at ~4.5 lines/order — a derived planning basis, not a profile figure; the profile carries no lines-per-order canon, so confirm the platform's actual line histogram before ordering) | profile §8.5 |
| AR invoices | ~42,000/yr | profile §15.1 |
| Governance/assurance HQ teams (ICM/QA/Credit/RM&I user basis) | Internal Audit & Risk 9 · Quality 5 (+24 DC checkers) · AR & Credit 8 | TO §5.3 |

> **Metric rule that dominates the HRMS lines:** the "Employee" / "Hosted Employee" metric counts
> **all** employees (plus any tracked contractors) — *not* actual users. Every Employee-metric
> product therefore licenses 6,911, even if only managers use it.

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
   HR programs adds to the 6,911.
5. **Full-implementation edition:** the BOM now licenses **every product the fit-gap register
   adopts** — the v1.0 footprint plus Revenue Management & Invoicing (A11), Lease & Finance
   Management (A13), Internet Expenses (B11), BOM/WIP (C9), Oracle Quality (C12), In-Memory
   Cost Management (C15), Engineering (C17), Credit Management (D3), Project Management and
   Internal Controls Manager (H11). GOP (D15) rides decision 3's custom-quote register.
   Payroll stays unadopted (decision 2 unchanged).
6. **Included entitlements ride the base licenses — no separate line:** GL budgets + budgetary
   control (F6), Oracle Alert (G9), AME/Workflow/ERES, AGIS, AR Bills Receivable + Lockbox +
   Balance Forward Billing, AP Bills Payable, Purchasing contingent labor (B13), Shipping +
   Transportation Execution (C14 — OTE is in-suite with Shipping), Install Base, TCA DQM
   (entitlement verify), SLA/eBTax, iSetup + Rapid Clone, BI Publisher/Web ADI/ECC,
   ISG/XML Gateway.

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
| Credit Management (scoring rules, limits, hold/release — D3) | TBD † | Application User | 2,295 | 5 | 11,475 |
| Revenue Management & Invoicing (PFRS 15 multi-element schedules — A11) | TBD † | Application User | 3,495 | 6 | 20,970 |

*Financials AUs: HQ finance/audit/legal/facilities/QM/LP/IT ≈ 172 + store SM/ASM 400 + DC mgmt 20 = 592, rounded to 650.
Read-only covers merch/store-ops/marketing analytics viewers (cheaper than full AUs).
Credit users = AR & Credit manager + 2 credit analysts + AR supervisor + trade-ops credit
liaison (TO §5.3; the 5,200-trade + 200-corporate account base). RM&I users = revenue
accounting (manager + 3) + project billing 2 — the PFRS-15 schedules for project sales,
service bundles and subscription deferrals (VS-157). AGIS, Bills Receivable/Payable, Lockbox,
Balance Forward Billing and GL budgetary control ship inside the Financials/AR/AP/CE bases —
no lines.*

### 2.2 Order management, pricing, fulfillment

| Product | Part # | Metric | List $/unit | Qty | License $ |
|---|---|---|---:|---:|---:|
| Order Management (incl. Shipping Execution) | A81406 | Application User | 4,595 | 300 | 1,378,500 |
| Electronic Order Line (ecommerce) | L10128 | Electronic Order Line | 0.23 | 2,500,000 | 575,000 |
| Option: Advanced Pricing (QP) | L30507 | Application User | 2,295 | 25 | 57,375 |
| Configurator (in-store fabrication quotes) | L11093 | Application User | 3,495 | 200 | 699,000 |
| AR Deductions Settlement (Trade Mgmt vehicle) | L72178 | Application User | 8,000 | 25 | 200,000 |
| Option: Channel Rebates & POS Management | L72189 | Application User | 6,000 | 25 | 150,000 |

*No iStore (deliberately not adopted). Trade Management no longer exists as a product line on the
GPL — VS-39's rebate/claims function maps to the Channel Revenue Management family above.
Configurator processor alternative: A90749 @ $172,500/processor. **GOP (D15)** — adopted as
the multi-org promising engine behind W56/W1114/VS-93 — is not on the current public GPL; it
joins the VCP stack in the custom-quote register (§2.11 note). Shipping + Transportation
Execution (WSH/OTE, C14) ship inside the OM base — no line.*

### 2.3 Logistics & warehouse

| Product | Part # | Metric | List $/unit | Qty | License $ |
|---|---|---|---:|---:|---:|
| Inventory Management | L31544 | Application User | 4,595 | 3,600 | 16,542,000 |
| Option: Mobile Supply Chain Applications (RF) | L31704 | Application User | 1,725 | 2,700 | 4,657,500 |
| Warehouse Management (WMS) | A89486 | Application User | 9,595 | 650 | 6,236,750 |
| Landed Cost Management | L72151 | $M COGS | 350 | 800 | 280,000 |
| Bill of Materials / WIP (kits, bundles, build-to-order — C9) | TBD † | Application User | 3,845 | 50 | 192,250 |
| Oracle Quality (incoming inspection, supplier quality, CAPA — C12) | TBD † | Application User | 2,295 | 40 | 91,800 |
| Engineering (ECO/ECN over kit/BOM revisions — C17) | TBD † | Application User | 1,725 | 12 | 20,700 |
| In-Memory Cost Management (real-time costing/margin analytics — C15) | TBD † | Application User | 5,750 | 15 | 86,250 |

*INV must cover all WMS/MSCA users. MSCA RF users: store RC/stock/supervisors 2,000 + DC 600
(§1) + QM/IT 50 = 2,650, rounded to 2,700. LCM quantity tracks COGS — grows with revenue (true-up annually). BOM/WIP users:
DC kit/BTO assembly 32 + fabrication leads 15 + private-label line 3. Quality users: QM team 5
+ DC checkers 24 + fabrication QC 6 + supplier-quality analysts 5. Engineering users: private-
label product development + kit/BOM master governance (W302/W129). IMC users: logistics &
cost finance + merch-finance margin analysts (W85/W633/VS-101); enterprise BI stays with DP.*

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
| Internet Expenses (T&E reports + corporate-card program — B11) | TBD † | Application User | 115 | 700 | 80,500 |

*⚠ minimum-bound at 10,000 records (actual vendor master ~1,000). iSupplier external supplier
users are included with the internal AU licenses. iExpenses users: all HQ 511 + DC office
staff ~100 + district/region field ~25, rounded to 700. Contingent labor (B13) ships inside
Purchasing — no separate line.*

### 2.5 Asset lifecycle & real estate

| Product | Part # | Metric | List $/unit | Qty | License $ |
|---|---|---|---:|---:|---:|
| Enterprise Asset Management (eAM) | L39451 | Application User | 4,595 | 60 | 275,700 |
| Option: Self-Service Work Requests | L39457 | Application User | 575 | 250 | 143,750 |
| Property Manager | L16535 | Application User | 4,595 | 15 | 68,925 |
| Lease & Finance Management (lessor leasing + the rental family — A13) | TBD † | Application User | 4,595 | 8 | 36,760 |

*L&FM users: corporate equipment-leasing desk (VS-96) + rental-fleet/service coordinators
(VS-12.2 tool rental, VS-162 self-haul, VS-174 portable storage, VS-186 equipment rental).*

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
family (no separate GPL line).*

### 2.7 Projects

| Product | Part # | Metric | List $/unit | Qty | License $ |
|---|---|---|---:|---:|---:|
| Project Costing | A85888 | Application User | 4,595 | 60 | 275,700 |
| Option: Project Billing | L31923 | Application User | 3,495 | 15 | 52,425 |
| Project Management (project performance reporting) | TBD † | Application User | 3,495 | 15 | 52,425 |

*PM users: corporate PMO (VS-112) + construction/capex project controllers (VS-20/40/109).*

### 2.8 HRMS — all Employee-metric @ 6,911

| Product | Part # | List $/emp | License $ |
|---|---|---:|---:|
| Human Resources (PER) | L31953 | 185 | 1,278,535 |
| Self-Service Human Resources | L31958 | 40 | 276,440 |
| Advanced Benefits (OAB) | A92408 | 85 | 587,435 |
| Compensation Workbench | L46808 | 70 | 483,770 |
| iRecruitment | L31969 | 75 | 518,325 |
| Performance Management | L46799 | 105 | 725,655 |
| Time and Labor | A92407 | 110 | 760,210 |
| Succession Planning | L74875 | 70 | 483,770 |
| Learning Management (OLA) | L44374 | 105 | 725,655 |
| ~~Payroll~~ — **not licensed** (in-house Payroll PH) | A74656 | (225) | 0 |

### 2.9 Master data management

| Product | Part # | Metric | List $/unit | Qty | License $ |
|---|---|---|---:|---:|---:|
| Product Hub | L42168 | Record | 14 | 60,000 | 840,000 |
| Product Hub Data Steward | L42140 | Application User | 5,795 | 20 | 115,900 |
| Site Hub | L69431 | Record | 200 | 1,000 ⚠ | 200,000 |
| Site Hub Add-On for EBS | L69447 | Record | 100 | 1,000 | 100,000 |
| Site Hub Data Steward | L69463 | Application User | 5,795 | 1 | 5,795 |

*Customer master is TCA inside EBS Financials (no Customer Hub needed). ⚠ minimum-bound.
TCA DQM dedup (W253): if the built-in TCA DQM is deemed insufficient, Enterprise Data Quality
Standardization & Match (L99899) is $275,000/processor min 4 = $1.1M — **verify entitlement
before budgeting**; not included in the totals below.*

### 2.10 Governance & controls (full-implementation)

| Product | Part # | Metric | List $/unit | Qty | License $ |
|---|---|---|---:|---:|---:|
| Internal Controls Manager (audit-management/GRC surface; hosts the CTL-01–808 register — H11) | TBD † | Application User | 2,875 | 40 | 115,000 |

*ICM users: Internal Audit & Risk 9 (TO §5.3) + finance process owners 21 + business control
owners 10 — assessment performers and CAPA approvers, not the whole control population.
Oracle Alert (G9) rides the base applications; GL budgets/budgetary control (F6) rides GL —
no lines.*

### 2.11 Scenario A totals

| | USD list |
|---|---:|
| **Perpetual license total** | **$48,685,690** |
| Annual SUL&S (22%) | $10,710,852/yr |
| 3-yr TCO (license + 3× support) | $80,818,246 |
| 5-yr TCO (license + 5× support) | **$102,239,950** |

*Full-implementation delta vs v1.0: **+$708,130** of perpetual license (+$155,789/yr support)
across the ten newly licensed products — ~1.5% of the license base; ranking vs Fusion is
unchanged.*

***Custom-quote register (adopted, unpriced — excluded from the totals):** the EBS-family
Value Chain Planning stack — ASCP, Demantra, Inventory Optimization/Rapid Planning (C5) — and
**Global Order Promising** (D15) are off the current public GPL; budget placeholder $2–4M
perpetual pending the Oracle VCP quote. Payroll A74656 remains unadopted — reversing decision 2
would add $225/emp × 6,911 = **$1,554,975** (+$342,095/yr support).*

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
| Fusion Risk Management (GRC/ICM equivalent — ICM parity, H11) | B91081 | Hosted Named User | 180 | 60 | 10,800 |
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
| Fusion HCM Base (Global HR/absence/benefits) | B85800 | Hosted Employee | 15 | 6,911 | 103,665 |
| Fusion Time and Labor | B75365 | Hosted Named User | 3 | 3,000 | 9,000 |
| Fusion Workforce Compensation (CWB eq.) | B109620 | Hosted Comp. Individual | 4 | 6,911 | 27,644 |
| Fusion Learning (OLA eq.) | B85242 | Hosted Named User | 5 | 6,911 | 34,555 |
| Fusion Recruiting (iRecruitment eq.) | B87675 | Hosted Employee | 8 | 6,911 | 55,288 |
| Fusion Talent Management (perf + succession) | B94925 | Hosted Named User | 7 | 6,911 | 48,377 |
| Field Service Cloud (dispatch core, D13) | B110413 | Pooled Named User | 225 | 360 ⚠ | 81,000 |
| Fusion Revenue Management (RM&I eq., PFRS 15 — A11) | TBD † | Hosted Named User | 150 | 6 | 900 |
| Fusion Quality Management (Oracle Quality eq. — C12) | TBD † | Hosted Named User | 200 | 40 | 8,000 |
| Fusion Global Order Promising (GOP eq. — D15) | TBD † | Hosted Named User | 425 | 10 | 4,250 |
| Fusion Transportation Management (OTE eq., freight audit — C14) | TBD † | Hosted Named User | 650 | 25 | 16,250 |
| **Total** | | | | | **$2,416,729/mo** |

**B1 totals: $29,000,748/yr · $87,002,244 (3-yr) · $145,003,740 (5-yr)**

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
| Fusion Suite Employee (self-service tier) | B108675 | Hosted Employee | 5 | 3,311 | 16,555 |
| Fusion Demand Management | B91060 | Hosted Named User | 1,250 | 10 | 12,500 |
| Fusion Supply Planning | B91059 | Hosted Named User | 1,250 | 10 | 12,500 |
| Fusion S&OP Cloud | B91061 | Hosted Named User | 625 | 15 | 9,375 |
| Fusion Time and Labor | B75365 | Hosted Named User | 3 | 3,000 | 9,000 |
| Fusion Learning | B85242 | Hosted Named User | 5 | 6,911 | 34,555 |
| Fusion Recruiting | B87675 | Hosted Employee | 8 | 6,911 | 55,288 |
| Fusion Talent Management | B94925 | Hosted Named User | 7 | 6,911 | 48,377 |
| Fusion Workforce Compensation | B109620 | Hosted Comp. Individual | 4 | 6,911 | 27,644 |
| WMS Enterprise add-on | B90536 | Hosted Named User | 550 | 620 | 341,000 |
| Fusion CPQ add-on | B111751 | Hosted Named User | 240 | 200 | 48,000 |
| Field Service Cloud add-on | B110413 | Pooled Named User | 225 | 360 | 81,000 |
| Fusion Risk Management add-on (ICM eq., H11) | B91081 | Hosted Named User | 180 | 60 | 10,800 |
| Fusion Revenue Management add-on (A11) | TBD † | Hosted Named User | 150 | 6 | 900 |
| Fusion Quality Management add-on (C12) | TBD † | Hosted Named User | 200 | 40 | 8,000 |
| Fusion Global Order Promising add-on (D15) | TBD † | Hosted Named User | 425 | 10 | 4,250 |
| Fusion Transportation Management add-on (C14) | TBD † | Hosted Named User | 650 | 25 | 16,250 |
| **Total** | | | | | **$1,923,994/mo** |

**B2 totals: $23,087,928/yr · $69,263,784 (3-yr) · $115,439,640 (5-yr)**

*The bundle's ERP+SCM+HCM bases already cover Expenses, Credit, costing and PLM change orders;
Risk, Revenue, Quality, GOP and Transportation Management sit outside the bundle and price
à-la-carte as add-ons.*

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
  (C14/OTE parity) and the Risk Management bump 20 → 60 (ICM parity, H11) — modeled as
  explicit lines in B1/B2 above; vendor rebates assumed inside Fusion OM's Channel Revenue
  Management entitlement.
- WMS Enterprise is the largest avoidable line ($4.1M/yr): running DC RF execution on
  Advanced Inventory/SCE mobile (instead of full WMS Enterprise) drops it — at the cost of
  slotting/labor/yard/cartonization parity with the repo's in-suite WMS decision.

---

## 4. Comparison & recommendations

| Scenario | Up-front | Annual | 3-yr list TCO | 5-yr list TCO |
|---|---:|---:|---:|---:|
| **A — EBS 12.2 perpetual + 22% SUL&S** | $48.69M | $10.71M (support) | $80.8M | $102.2M |
| **B1 — Fusion Cloud à-la-carte** | — | $29.00M | $87.0M | $145.0M |
| **B2 — Fusion Suite bundle (36-mo)** | — | $23.09M | $69.3M | $115.4M |

1. **At list price, EBS is cheapest over 5 years** (~$102.2M vs $115.4M Suite / $145.0M
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
5. All quantities include a ~3% growth buffer but assume 200 stores / 6,911 employees —
   growing to 300 stores adds ~1,200 store users (+INV/MSCA/iProc/iExpenses-class licenses)
   and is **metric-true-up free on EBS perpetual** but re-priced every renewal on Fusion.

---

*Document Version: 2.1 | Date: 2026-09-17 | **Fifty-fourth-wave consistency review (driver/note footing):** the surfaces the §2–§3 line-item re-derivations cannot read trued — §1's ecommerce driver now states the derived basis its order-line pricing rides (≈2.3M OM order lines at ~4.5 lines/order; the profile carries no lines-per-order canon — confirm the line histogram before ordering), §2.1's Financials AU build-up carries its explicit footing (= 592, rounded to 650 — the iExpenses rounding convention the note had silently omitted), and §2.3's MSCA RF build-up is trued to §1's own DC driver (DC 600 per §1, not 550; = 2,650, rounded to 2,700) — no line-item, quantity or total change, EBS/Fusion scenarios untouched. Prior v2.0 (full-implementation edition) | Date: 2026-09-17 | **v2.0 delta:** licenses the exhaustion-audit adoptions — EBS: RM&I (A11), L&FM (A13), iExpenses (B11), BOM/WIP (C9), Quality (C12), In-Memory Cost (C15), Engineering (C17), Credit Management (D3), Internal Controls Manager (H11), Project Management; Fusion: Risk 20 → 60, Revenue, Quality, GOP, Transportation Management — moving the EBS license base $47,977,560 → $48,685,690 and B1/B2 to $2,416,729 / $1,923,994 per month; † part numbers/prices pending GPL verification; GOP added to the VCP custom-quote register. Prior v1.0 (2026-09-17): initial issue. Sources: model-company-profile.md (§3, §4, §8, §9, §12, §15); module-coverage-map.md v2.0; ebs-platform-architecture.md v2.0 §2; fit-gap-analysis.md §2; optimal-table-of-organization.md §5.3; Oracle E-Business Suite Applications Component Global Price List 2026-09-10; Oracle Fusion Cloud Service Global Price List 2026-09-10; Oracle Technology Global Price List 2026-09-10. Prices are US-Dollar list, subject to change without notice; quantities are planning estimates pending an Oracle License Determination.*
