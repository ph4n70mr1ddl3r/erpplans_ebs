# Headcount Reality Check — HQ vs. Workflow Coverage

> **STATUS — ACTIONED 2026-06-20.** This analysis identified that HQ (315) was understaffed and omitted 6 functions. Per direction to apply the **minimum** increase that resolves the gaps, HQ was rebalanced **315 → 357** and total **6,715 → 6,757** (see `model-company-profile.md` §3.3/§4 and the CHANGELOG entry for 2026-06-20). The comfortable/fully-cushioned range estimated below (~440–470) was **not** adopted; the implemented 357 is the floor that (a) fixes the Executive inconsistency, (b) breaks out the 6 hidden departments explicitly, and (c) relieves only the contradictions the workflows themselves expose (e.g., AP "10 clerks", IT archipelago field support). **2026-06-25 update:** Supply Chain & Logistics was subsequently rebalanced **35 → 40** to stand up a dedicated **S&OP/IBP sub-team** (5) — the single accountable owner of [VS-127](workflows/VS-127-sales-operations-planning-integrated-business-planning/README.md) — closing the §4 "S&OP Lead" missing-role gap and the VS-127 "unowned-as-a-program" finding; HQ is now **357 → 362** and total **6,757 → 6,762** (see `model-company-profile.md` §3.3 "Supply Chain & Logistics Team Structure" and the CHANGELOG entry for 2026-06-25). The analysis below is retained as the gap record. **2026-09-02 update:** the comfortable range (~440–470) estimated below has now been **adopted as the target state** — HQ **469** / total **6,869** — via [`optimal-table-of-organization.md`](optimal-table-of-organization.md) (phased per its §11); the implemented 362 remains the current-state baseline, so this analysis now serves as both the gap record and the sizing authority behind the target bands. **2026-09-03 update:** the hybrid capability-sourcing decision (best-of-breed edges + in-house builds around the unified ERP core; [`07-methodology/capability-sourcing-and-engineering-model.md`](../07-methodology/capability-sourcing-and-engineering-model.md)) extends the IT band **65–80 → 65–130** and the comfortable HQ range **~440–470 → ~440–515** (the agentic-AI extension of the same date adds the final +5 of headroom); the adopted target moves to HQ **511** / total **6,911** with IT = 122 ([`optimal-table-of-organization.md`](optimal-table-of-organization.md) v1.5; [`it-product-operating-model.md`](../07-methodology/it-product-operating-model.md) v3.11 §9). **2026-09-09 update:** [`optimal-table-of-organization.md`](optimal-table-of-organization.md) **v2.1** is now the **official table of organization of record** and defines every one of the 511 HQ roles in its new §5.3 role register (titles drawn from the workflow-RACI canon; v2.1 trues the register's own self-descriptions — 188 rows / 187 distinct titles, the §5.3 span-note row counts, and the §5.2 GL & Consolidation mix cell); the need bands below remain the sizing authority behind its department targets. **2026-09-14 update:** the two-tier sourcing doctrine is enacted — [`optimal-table-of-organization.md`](optimal-table-of-organization.md) **v2.2** (two-tier wording conformance + the IT shape note; register, 511 HQ / 6,911 total and every figure unchanged) and [`it-product-operating-model.md`](../07-methodology/it-product-operating-model.md) **v3.12** §9 (WLI's second vendor seat converted to in-suite WMS/OTE functional-analyst depth; one Platform Product Manager per integrate team; commodity-vendor commercial ownership consolidated in the CIO Office — 122 FTE / 17 teams unchanged); the 65–130 two-tier band and the comfortable HQ range ~440–515 stand. **2026-09-14 promotion:** the optimal TO is **promoted to the actual structure of record** by executive direction — the org recognizes one state (HQ 511 / total 6,911; IT = 122 as the 17-team product-centric department): [`optimal-table-of-organization.md`](optimal-table-of-organization.md) **v2.3** (two-state collapse, §11 recast as the promotion record) and [`it-product-operating-model.md`](../07-methodology/it-product-operating-model.md) **v3.13** (the model as the IT department's structure of record); profile v3.0 re-based (§3.3/§4/§11.1/§13.1; revenue/employee re-derived ~PHP 9.01M); this gap record's 6,757/33 figures stand as the historical authoring-time record. **2026-09-15 update:** [`optimal-table-of-organization.md`](optimal-table-of-organization.md) **v2.4** states the §5.3 role-resolution contract honestly — the v2.0 note's 'every workflow owner resolves to exactly one row' claim held for only part of the catalog (owner cells 2,507 resolved / 2,920 carrying variant or newer vocabulary of 5,427; 2,040 distinct uncharted owner forms; 10,829 distinct uncharted forms across all RACI surfaces, per the generated role-coverage matrix's watchlist) — and re-contracts workflow presence at function level (every department has ≥1 catalog-resolved role; specialist/deputy titles may be exercised through their department's broader titles), with the census re-derived and pinned by `07-methodology/validate-repo.sh` Check 71 so the population moves only by conscious re-adjudication; no HC, role, or figure change — 511 / 6,911, IT 122 stand.

**Scope:** Cross-reference the stated HQ department headcounts (`model-company-profile.md` §3.3 / §4) against the actual job roles, volumes, and responsibilities referenced across all workflow markdown files (**569 process-area specs across 188 value streams**).

**Method:** Extracted every `Owner` / `Participants` role title from all workflow PA files (~16,400 internal role mentions after normalization), clustered into role families, mapped to departments, and sized against stated transaction volumes (AP/AR/PO volumes, user counts, store/DC counts, statutory filing frequency).

---

## 1. Bottom Line

The 6,757 total company headcount is **plausible overall**, but the **HQ allocation of 315 was understated**, the department breakdown **omitted 6 entire functions** that appear heavily in the workflows, and at least **4 departments were materially understaffed** for their stated workload (Finance, IT, HR, Legal). Store (5,800) and DC (600) headcounts are defensible.

**Recommended HQ target:** comfortable range ~440–470; **implemented minimum 357** (see status banner above).

---

## 2. Summary Table — Stated vs. Recommended

> **Reading note:** the “Stated” column below reflects the **pre-rebalance (315-HQ) allocation**
> this analysis was performed against — not the current state. The implemented rebalance (315 → 357)
> lives in `model-company-profile.md` §3.3/§4: Executive Office is now 7 (not 5), Finance &
> Accounting 46 (not 37), IT 50 (not 33), HR 26 (not 18), Legal & Compliance 14 (not 9), and the
> six “hidden” departments are now broken out explicitly. The verdicts below are the **historical
> gap record** that drove the rebalance, not a current-state assessment.

| HQ Department | Stated | Realistic Range | Verdict | Key Driver |
|---|---|---|---|---|
| Executive Office | 5 | 7 | ❌ Inconsistent | Org chart (§11.1) lists CEO + 6 C-suite; §3.3 omits CHRO & VP Legal |
| Finance & Accounting | 37 | **58–68** | 🔴 Severely understaffed | ~9,000 AP invoices/mo; 5 entities; PFRS 15; monthly VAT ×5 |
| Merchandising & Buying | 40 | 40–45 | 🟡 Right size, wrong mix | Too few planners/pricing analysts for 35K SKUs |
| Supply Chain & Logistics | 31 | **42–50** | 🔴 Understaffed | 800–1K vendors; 40% imports; S&OP; fleet; 4 DCs |
| Information Technology | 33 | **65–80** | 🔴 Severely understaffed | 6,757 users; 600 POS; 200 stores; ERP; cyber; privacy |
| Human Resources | 18 | **38–48** | 🔴 Severely understaffed | 6,757 staff; ~1,400 hires/yr; 5 entities; payroll ×2/mo |
| Marketing | 23 | 28–34 | 🟡 Slightly low | Ecom + loyalty + retail media + insights |
| Store Operations | 24 | 24 | ✅ OK | Regional model fits 200 stores |
| Legal & Compliance | 9 | **18–24** | 🔴 Severely understaffed | 1,872 workflow mentions; AML/ABC; privacy; SEC; multi-LGU |
| Internal Audit | 5 | 8–10 | 🟡 Low | ERM bundled in; 5 entities; PHP 62B |
| Loss Prevention | 20 | 25–30 | 🟡 Low-ish | VS-23 exception monitoring + investigations + shrink |
| Customer Service / Call Center | 30 | 30–45 | ❓ Depends | OK only if decentralized to stores |
| **Health, Safety & Environment** | **0 (hidden)** | **12–15** | 🔴 **MISSING dept** | DOLE RA 11058; "1 Safety Officer per region (~10–12)" |
| **Quality** | **0 (hidden)** | **5–6** | 🔴 **MISSING dept** | VS-31 incoming inspection, vendor QA, recalls |
| **Facilities & Real Estate** | **0 (hidden)** | **10–15** | 🔴 **MISSING dept** | VS-20/97/138; 200 stores + HQ + DCs |
| **Sustainability / ESG** | **0 (hidden)** | **3–4** | 🔴 **MISSING dept** | VS-25; DENR; ESG reporting |
| **Strategy / Corp Planning** | **0 (hidden)** | **4–5** | 🔴 **MISSING dept** | VS-33; annual plan; CPM |
| **Trade / Account Mgmt** | **0 (hidden)** | **6–8** | 🔴 **MISSING dept** | VS-43 Trade Pro program; 5,200 AR accounts |
| **TOTAL HQ** | **315** | **~440–470** | | +6 functions not enumerated |

> The 6 "hidden" departments sum to ~40–53 people — which almost exactly explains the gap between the **enumerated departments (~275)** and the **stated HQ total (315)**. The profile clearly *included* these functions in the 315, but never broke them out. This is a **documentation defect**, not necessarily a planning omission.
>
> **2026-06-25 follow-up — Supply Chain & Logistics (the one 🔴 row without a dedicated §3 detail).** Profile §3.3 Supply Chain & Logistics rebalanced **35 → 40**, carving out a dedicated **S&OP/IBP sub-team** (5: S&OP/IBP Lead, Senior Demand Planner, 2 Demand Planners, Supply & Allocation Planner) that is the single accountable owner of [VS-127](workflows/VS-127-sales-operations-planning-integrated-business-planning/README.md). This closes the "S&OP Lead" missing-role gap (§4) and partially relieves the 31-vs-42–50 understaffing; HQ is now 357 → **362** and total 6,757 → **6,762**. The comfortable range (~42–50) remains only partially adopted, consistent with the minimum-resolves-the-gap principle.

---

## 3. The Severely Understaffed Departments (detail)

### 3.1 Finance & Accounting — stated 37, need 58–68
**Workload evidence from workflows:**
- **~8,500–9,500 AP invoices/month** (~300/day) — VS-17 / PA-17
- **~3,500 AR invoices/month** + 5,200 active AR accounts + collections — W8
- 5 legal entities, each filing **monthly VAT (BIR 2550M)** — VS-79
- Withholding tax / 2307 management across 5 entities
- PFRS 15 multi-element revenue recognition — VS-157
- Multi-entity consolidation + intercompany (~60–80 IC invoices/mo) — PA-17.2
- Fixed assets + Capex (CIP/AUC) — VS-35, VS-40
- Semi-monthly payroll accounting interface for 6,757 staff

**Roles the workflows demand but the 37 doesn't cover:**
AP Manager, AR Supervisor, Credit Manager, Intercompany Accountant, Revenue Accountant, Cost Accountant, Inventory Accountant, Logistics Finance Analyst, GL Accountant (×4–5 for 5 entities), Tax specialists (5 entities × VAT/WHT/income tax needs a team of 4+, not 1 accountant + 1 manager), FP&A team (only 1 generic "Finance Analyst" listed).

### 3.2 Information Technology — stated 33, need 65–80 (hybrid model: 65–130)
**Workload evidence:**
- **6,757 end users** to support across 200 stores + 4 DCs + HQ
- 600 POS terminals (real-time inventory sync <30s latency)
- ERP, WMS, TMS, OMS, CRM, PIM, CDP, BI, ecommerce — ~10+ platforms
- Cybersecurity & privacy (VS-27.3, VS-91) — NPC/DPA compliance
- Data engineering + BI + advanced analytics/AI (VS-28, VS-30)
- PMO for the ERP program itself

Industry benchmark for retail IT is **1.5–2.5% of headcount = 100–168**; even a heavily outsourced/lean model floors at ~60–70. **33 is roughly half the minimum.** The workflow mentions 14 distinct IT role families (helpdesk, infra, apps, data eng, BI, data scientist, security, privacy, PMO, architect, DBA, dev, DevOps, sysadmin).

> **2026-09-03 amendment (hybrid capability-sourcing model).** The 65–80 band above assumed
> the single-vendor unified-ERP model (no classical developers; configure-first). With the
> hybrid landscape — best-of-breed WMS/TMS/WFM/FSM edges and the in-house OMO/TPS build
> squads on the SEP engineering platform — the band extends to **65–130**
> (`it-product-operating-model.md` v2.0 §9.2 sizes the steady state at 115: 66 domain +
> 49 platform/CIO). The 14 role families listed above — notably dev, DevOps, and data
> scientist — now have permanent structural homes instead of being absorbed by the ERP
> vendor's delivery model. The historical 65–80 band is retained above as the pre-hybrid
> gap record. **Same-day agentic addendum:** the agentic-AI extension (OM v2.1) sizes IT at
> **122** — 66 domain + 56 platform/CIO, the +7 being the AI & Agent Platform team — still
> mid-band at 65–130; the comfortable HQ range tops at ~440–515 accordingly.

### 3.3 Human Resources — stated 18, need 38–48
**Workload evidence:**
- 6,757 employees, **~1,200–1,600 hires/year** (~15–20% turnover)
- 5 payroll entities, semi-monthly = ~13,430 payslips/month
- Labor relations / CBA / grievance (VS-84) — needs dedicated LR staff
- L&D for store onboarding + ongoing (VS-19.4)
- Drug-free workplace program (VS-150), background screening (VS-167), uniform/PPE (VS-169)

Benchmark for retail HR is **1:100–150 = 45–67**. **18 is ~40% of the lean minimum.** Workflows reference 13 HR role families including Labor Relations Director, Workforce Management, and dedicated recruiters (the roster lists essentially 1 recruiter).

### 3.4 Legal & Compliance — stated 9, need 18–24
**Workload evidence — the most role-intensive function per person:**
- **1,872 workflow mentions** (highest density of any function)
- Contract review/approval (W230), litigation (W125), IP portfolio (W126)
- Corporate secretarial + SEC reportorial (W124, W481, ASHM W482)
- Regulatory compliance across 200 stores in **multiple LGUs** (VS-22, VS-76)
- AML/KYC/CDD/sanctions/STR (VS-86) — requires dedicated MLRO
- Anti-bribery & corruption / COI / gifts (VS-86.3)
- Data privacy / DPA / NPC breach response (VS-91)
- Anti-counterfeit (VS-71), customs/trade (VS-87)
- Consumer financing, leasing, insurance legal (VS-38, VS-96, VS-26)

9 people cannot cover 8 distinct sub-disciplines at this scale. Workflows name 8 role families here (Legal staff, Legal Counsel, VP Legal, Compliance staff/officer/manager, DPO, AML Officer, Corporate Secretary).

---

## 4. Missing Roles (named in workflows, absent from roster)

These specialized roles appear repeatedly in workflows but have **no home in the HQ department list**:

| Role | Mentions | Home Dept | Notes |
|---|---|---|---|
| Energy Manager | 42 | Facilities / Sustainability | Utility benchmarking across 200 stores |
| Government Affairs Mgr | 59 | Legal & Compliance | Multi-LGU permits (VS-22, VS-76) |
| Labor Relations Director | 45 | HR | CBA/grievance (VS-84) |
| AML Officer / ABC Officer | 48 | Legal & Compliance | VS-86 — mandatory MLRO |
| Fraud Management | 44 | Loss Prevention / Finance | VS-23.1, VS-80.3 |
| Metrology / Weights & Measures | 28 | Quality | Catch-weight items (lumber, wire) |
| S&OP Lead | 21 | Supply Chain | **✓ Resolved 2026-06-25** — now the S&OP/IBP sub-team in Supply Chain & Logistics (profile §3.3); owns [VS-127](workflows/VS-127-sales-operations-planning-integrated-business-planning/README.md) |
| Third-Party Risk Mgmt (TPRM) | 19 | Risk/Audit | Vendor risk |
| BCP Manager | 17 | Risk/Facilities | VS-26 |
| ITAM (IT Asset Mgr) | 20 | IT | VS-99 |
| AI Governance | 26 | IT/Risk | VS-30.2 |
| Marketplace Manager | 41 | Marketing/Merch | VS-95 |
| Surety / Lease Admin | 46 | Legal/Real Estate | VS-42, VS-96 |
| OpEx / Continuous Improvement | 27 | Store Ops/Strategy | |
| Revenue Assurance Lead | 24 | Finance | VS-157 |
| EEO / DEI | 24 | HR | HR-044 requirement |

---

## 5. Inconsistencies in the Profile Document

1. **Executive count mismatch** — §11.1 org chart shows CEO + **6** direct reports (CFO, COO, CIO, CMO, CHRO, VP Legal), but §3.3 lists "Executive Office (5)" omitting CHRO and VP Legal.
2. **Department sum ≠ HQ total** — enumerated departments sum to ~275; stated HQ is 315. The ~40 gap is the 6 un-enumerated functions (HSE, Quality, Facilities/RE, Sustainability, Strategy, Trade Acct Mgmt).
3. **Revenue/employee footnote** (§4) claims HQ "expanded to 315 to include DPO, Tax Accountant, Logistics Finance Analyst, IT Helpdesk, Regional LP" — but these additions are not reflected in the department line items (Finance still shows ~37, IT ~33), so the expansion is double-counted or invisible.
4. **Buying team** (§13.1) named only VP + 5 Category Managers + 10–12 Buyers + 3 Pricing Analysts + 2 Planners (~22) against a 40-person department — the other ~18 were unexplained. **Resolved 2026-06-20:** §13.1 now breaks the 40 into ten role lines (VP, 5 Category Managers, 10 Buyers, 5 Planners/Allocators, 4 Pricing Analysts, 3 Assortment & Space, 3 Direct Sourcing, 3 Private Brand, 2 Promotions, 4 Merch Ops/MD) that sum to 40, rebalanced toward planning/pricing/assortment per §7.4.
5. **Store staffing 29/store** is internally consistent (§12.1) and defensible; the rationale (4 Stock Associates for replenishment/omnichannel) is sound. No change recommended there.

---

## 6. Store (5,800) and DC (600) Assessment — OK

- **Stores: 29/store** for an 8,000–15,000 sqm big-box with 3 POS terminals and curated 35K SKUs is **lean but defensible** (the doc argues it well). 12 Sales Associates across that footprint is tight during peak; consider a peak-season flex pool rather than changing base FTE.
- **DCs: 150/DC × 4** for cross-dock + WMS + special handling (lumber/tiles/paint) is **reasonable**. No change.

---

## 7. Recommendations

1. **Re-baseline HQ to ~440–470** and republish §3.3 with the 6 missing functions broken out (this alone closes the documentation gap).
2. **Prioritize hiring / capacity in Finance, IT, HR, Legal** — these four carry the highest workflow-to-headcount mismatch and the highest regulatory exposure (BIR, NPC, DOLE, SEC, AMLC).
3. **Staff the mandated roles** that Philippine law effectively requires at this scale: MLRO/AML Officer (AMLA), DPO + privacy staff (DPA), Safety Officers per region (RA 11058 / DO 198), Company Nurse/First Aiders (1 per store).
4. **Fix the role-mix in Merchandising** — shift 3–4 headcount from buyers into planners/pricing analysts/assortment to match VS-57 and the 35K-SKU complexity.
5. **Decide & document the Customer Service model** (centralized call center vs. in-store CSR) — it swings that department between 30 and 45.
6. **Correct the Executive count to 7** and reconcile §3.3, §4, and §11.1.
