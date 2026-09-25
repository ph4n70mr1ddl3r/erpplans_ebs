# BuildRight Depot Corp. — Role–Workflow Coverage Matrix (generated)

> **Generated artifact — do not hand-edit.** Produced by
> [`../07-methodology/generate-role-coverage.py`](../07-methodology/generate-role-coverage.py)
> from the canonical registers: every PA file's Owner / Participants /
> Steps-table Role (R) / Role (A) fields (the workflow catalog's canonical
> RACI vocabulary), the criticality register's confirmed Tier assignment,
> and the official table of organization (§5.3 Enterprise Role Register,
> §7.2 store roster, §7.3 DC roster). Regenerate after any PA, role, or
> register change; `generate-role-coverage.py --check` byte-verifies this
> file. Resolution order: §5.3 register (incl. C-suite/role aliases) →
> §7.3/§7.2 field rosters → IT product-model seats → department-level
> actors → system actors → governance bodies → generic workforce →
> external counterparties → Uncharted watchlist (reported, never dropped).
> Cells that do not resolve whole are split on commas and slashes and the
> parts resolved individually; canonical titles containing slashes (e.g.
> Sustainability / ESG Manager) resolve whole first.

## Summary

| Measure | Value |
|---|---|
| Workflows mapped | 5433 (exactly one Owner each — asserted) |
| Confirmed Tier register | 5456 rows (Tier 1: 1396 · Tier 2: 3302 · Tier 3: 758) |
| Distinct resolved actors | 4211 — §5.3 register roles 194 · IT product-model seats 32 · store field 12 · DC field 27 · department-level actors 2954 · system actors 31 · governance 59 · workforce 101 · external 801 · uncharted 0 |

> Tier mix = confirmed tiers of the workflows a role touches (a workflow
> counts once per role regardless of how many steps mention it). HC is
> shown for §5.3 register roles; field rosters are per-store/per-DC and
> external/system actors carry no headcount by definition.

## Role-Anchoring Contract (chartered roles × explicit workflow presence)

> **Contract (by direction 2026-09-23; supersedes the function-level contract
> of TO v2.4/v2.5).** A role that is not explicitly in a workflow cannot be
> measured: no Owner / Participant / Step presence means no demand signal, no
> cycle time, no handoff count — nothing to optimize. Every chartered role
> therefore carries at least one explicit RACI anchor in the catalog, and no
> headcount or structure decision may touch an unanchored or demand-unverified
> role: anchor it into its owning workflow (or consciously re-scope the
> charter), and verify per-role annual demand via
> [`virtual-gemba-walk.py`](../07-methodology/virtual-gemba-walk.py) against
> the chartered TO capacity first. The zero-anchor rows are the anchoring
> worklist; the weak-anchor rows (anchored in only 1–2 workflows) are the
> demand-verification watchlist. The census numbers below are pinned by
> `validate-repo.sh` Check 71 — any movement is a conscious re-adjudication.

| Measure | Value |
|---|---|
| Chartered roles (register 192 + IT seats 32 + store 8 + DC 27) | 259 |
| With ≥1 explicit RACI anchor | 259 (100%) |
| ZERO-anchor — the anchoring worklist | 0 (hq 0 · it 0 · store 0 · dc 0) |
| Weakly anchored (1–2 workflows) — demand-verification watchlist | 53 |

### Weak-anchor watchlist — 53 chartered roles anchored in only 1–2 workflows

| Role | Charter source | HC | Workflows touched |
|---|---|---|---|
| Accounting Policy Analyst | §5.3 register — Finance & Accounting | 1 | 1 |
| Contracts & Commercial Manager (Senior Counsel) | §5.3 register — Legal & Compliance | 1 | 1 |
| Ecommerce Marketing Specialist | §5.3 register — Marketing | 2 | 1 |
| Field Communications Manager | §5.3 register — Store Operations | 1 | 1 |
| Payroll & Statutory Remittance Officer | §5.3 register — Human Resources | 1 | 1 |
| Promotions & Vendor-Funding Coordinator | §5.3 register — Merchandising & Buying | 3 | 1 |
| Promotions Specialist | §5.3 register — Marketing | 2 | 1 |
| Quality & Workforce Analyst | §5.3 register — Customer Service | 2 | 1 |
| Senior LP Analytics Analyst | §5.3 register — Regional Loss Prevention | 1 | 1 |
| TA Coordinator | §5.3 register — Human Resources | 1 | 1 |
| Technical Accounting Manager | §5.3 register — Finance & Accounting | 1 | 1 |
| IAP Integration Engineer | IT product-model seats — Information Technology (product model) | — | 1 |
| ASM | §7.2 store roster — Store (field, per-store roster) | — | 1 |
| Assistant DC Manager — Outbound | §7.3 DC roster — DC (field, per-DC roster) | — | 1 |
| Cycle Counters | §7.3 DC roster — DC (field, per-DC roster) | — | 1 |
| DC Office Administrator | §7.3 DC roster — DC (field, per-DC roster) | — | 1 |
| Discrepancy Analysts | §7.3 DC roster — DC (field, per-DC roster) | — | 1 |
| Facilities/Utility | §7.3 DC roster — DC (field, per-DC roster) | — | 1 |
| Special Handling Lead | §7.3 DC roster — DC (field, per-DC roster) | — | 1 |
| Tile & Heavy/Breakbulk Crew | §7.3 DC roster — DC (field, per-DC roster) | — | 1 |
| Audit Manager | §5.3 register — Internal Audit & Risk | 1 | 2 |
| Banking & Cash-Management Specialist | §5.3 register — Finance & Accounting | 2 | 2 |
| Business Process & IMS Lead | §5.3 register — Strategy / Corporate Planning | 1 | 2 |
| Corporate Secretary Analyst | §5.3 register — Legal & Compliance | 1 | 2 |
| CPM (Corporate Performance Management) Analyst | §5.3 register — Strategy / Corporate Planning | 1 | 2 |
| DC Cost-to-Serve Analyst | §5.3 register — Finance & Accounting | 1 | 2 |
| DC Operations Analyst | §5.3 register — Supply Chain & Logistics | 1 | 2 |
| Ecommerce Support Specialist | §5.3 register — Customer Service | 3 | 2 |
| ESG Reporting & Data Analyst | §5.3 register — Sustainability / ESG | 1 | 2 |
| Facilities Coordination Specialist | §5.3 register — Store Operations | 1 | 2 |
| Forensic / Fraud Investigator | §5.3 register — Internal Audit & Risk | 1 | 2 |
| Import Documentation Specialist | §5.3 register — Supply Chain & Logistics | 1 | 2 |
| Legal Counsel — Contracts | §5.3 register — Legal & Compliance | 2 | 2 |
| Maintenance & Projects Coordinator | §5.3 register — Facilities & Real Estate | 2 | 2 |
| Marketing Comms Specialist | §5.3 register — Marketing | 1 | 2 |
| Operations Compliance Lead | §5.3 register — Internal Audit & Risk | 1 | 2 |
| Paralegal / Contracts Specialist | §5.3 register — Legal & Compliance | 2 | 2 |
| Payroll Supervisor | §5.3 register — Human Resources | 1 | 2 |
| Privacy Officer | §5.3 register — Legal & Compliance | 1 | 2 |
| Purchasing / PO Specialist | §5.3 register — Supply Chain & Logistics | 6 | 2 |
| Replenishment & Allocation Analyst | §5.3 register — Supply Chain & Logistics | 2 | 2 |
| Retail Media Operations Specialist | §5.3 register — Marketing | 1 | 2 |
| Sourcing & Screening Coordinator | §5.3 register — Human Resources | 1 | 2 |
| Strategy Analyst | §5.3 register — Strategy / Corporate Planning | 1 | 2 |
| Vendor Portal & Collaboration Specialist | §5.3 register — Supply Chain & Logistics | 2 | 2 |
| Wellness Coordinator | §5.3 register — Health, Safety & Environment | 1 | 2 |
| AAP Agent Engineer | IT product-model seats — Information Technology (product model) | — | 2 |
| Build-Squad Tech Lead | IT product-model seats — Information Technology (product model) | — | 2 |
| IAP Integration Support Engineer | IT product-model seats — Information Technology (product model) | — | 2 |
| INFRA Site Reliability Engineer | IT product-model seats — Information Technology (product model) | — | 2 |
| Assistant DC Manager — Inbound | §7.3 DC roster — DC (field, per-DC roster) | — | 2 |
| Cross-Dock Team | §7.3 DC roster — DC (field, per-DC roster) | — | 2 |
| Lumber / Long-Length Crew | §7.3 DC roster — DC (field, per-DC roster) | — | 2 |

## §5.3 Enterprise Role Register (HQ roles)

| Role | Dept / source | HC | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|---|
| Chief Finance Officer (CFO) | Executive Office | 1 | 63 | 358 | 265 | 1833 | 1211 | 318 | 687 | 206 |
| Chief Operating Officer (COO) | Executive Office | 1 | 59 | 161 | 129 | 1081 | 681 | 109 | 410 | 162 |
| Chief Human Resources Officer (CHRO) | Executive Office | 1 | 35 | 88 | 93 | 676 | 369 | 78 | 237 | 54 |
| Chief Information Officer (CIO) | Executive Office | 1 | 31 | 88 | 75 | 585 | 329 | 71 | 201 | 57 |
| Chief Marketing Officer (CMO) | Executive Office | 1 | 26 | 72 | 73 | 361 | 228 | 21 | 135 | 72 |
| CEO / President | Executive Office | 1 | 10 | 113 | 62 | 651 | 457 | 87 | 265 | 105 |
| VP Finance & Accounting / Corporate Controller | Finance & Accounting | 1 | 83 | 274 | 318 | 863 | 540 | 226 | 263 | 51 |
| Treasury Manager | Finance & Accounting | 1 | 66 | 57 | 205 | 205 | 133 | 38 | 79 | 16 |
| FP&A Manager | Finance & Accounting | 1 | 64 | 168 | 253 | 23 | 216 | 19 | 135 | 62 |
| Tax Manager | Finance & Accounting | 1 | 46 | 60 | 144 | 132 | 97 | 73 | 22 | 2 |
| Tax Accountant | Finance & Accounting | 4 | 44 | 62 | 216 | 33 | 87 | 69 | 16 | 2 |
| Revenue Assurance Lead | Finance & Accounting | 1 | 40 | 47 | 106 | 119 | 69 | 26 | 33 | 10 |
| AR & Credit Manager | Finance & Accounting | 1 | 38 | 50 | 107 | 243 | 104 | 36 | 60 | 8 |
| Manager, GL & Consolidation (Assistant Controller) | Finance & Accounting | 1 | 37 | 43 | 45 | 123 | 107 | 37 | 66 | 4 |
| AR Supervisor | Finance & Accounting | 1 | 30 | 34 | 103 | 97 | 57 | 39 | 18 | 0 |
| Credit Analyst | Finance & Accounting | 2 | 27 | 62 | 149 | 21 | 85 | 28 | 50 | 7 |
| GL Accountant (one per entity) | Finance & Accounting | 5 | 27 | 55 | 123 | 30 | 71 | 30 | 39 | 2 |
| Senior Revenue Accountant | Finance & Accounting | 1 | 26 | 6 | 74 | 0 | 30 | 9 | 20 | 1 |
| Leases Accountant | Finance & Accounting | 1 | 25 | 5 | 60 | 0 | 25 | 6 | 17 | 2 |
| Treasury Analyst | Finance & Accounting | 3 | 23 | 64 | 209 | 28 | 88 | 56 | 26 | 6 |
| AR Clerk | Finance & Accounting | 2 | 17 | 49 | 132 | 20 | 66 | 40 | 22 | 4 |
| AP Manager | Finance & Accounting | 1 | 17 | 33 | 65 | 30 | 41 | 18 | 20 | 3 |
| Logistics & Cost Finance Analyst | Finance & Accounting | 3 | 15 | 4 | 26 | 14 | 16 | 5 | 7 | 4 |
| FP&A Analyst | Finance & Accounting | 3 | 12 | 20 | 34 | 2 | 27 | 8 | 8 | 11 |
| AP Supervisor | Finance & Accounting | 2 | 11 | 26 | 52 | 70 | 51 | 28 | 22 | 1 |
| Consolidation & Intercompany Accountant | Finance & Accounting | 1 | 7 | 16 | 22 | 1 | 19 | 15 | 4 | 0 |
| AP Clerk | Finance & Accounting | 13 | 6 | 68 | 118 | 8 | 92 | 43 | 42 | 7 |
| Collections Specialist | Finance & Accounting | 2 | 4 | 13 | 16 | 1 | 15 | 7 | 8 | 0 |
| Revenue Assurance Analyst | Finance & Accounting | 1 | 3 | 0 | 6 | 2 | 4 | 1 | 3 | 0 |
| S&OP Finance Partner | Finance & Accounting | 1 | 2 | 8 | 10 | 0 | 8 | 0 | 3 | 5 |
| Payroll Accounting Liaison | Finance & Accounting | 1 | 0 | 3 | 3 | 2 | 4 | 3 | 0 | 1 |
| Senior FP&A Analyst | Finance & Accounting | 2 | 0 | 2 | 1 | 0 | 3 | 2 | 0 | 1 |
| Tax Compliance & eFPS Specialist | Finance & Accounting | 1 | 0 | 2 | 1 | 0 | 3 | 3 | 0 | 0 |
| Banking & Cash-Management Specialist | Finance & Accounting | 2 | 0 | 2 | 1 | 0 | 2 | 1 | 1 | 0 |
| DC Cost-to-Serve Analyst | Finance & Accounting | 1 | 0 | 2 | 1 | 0 | 2 | 0 | 1 | 1 |
| Accounting Policy Analyst | Finance & Accounting | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Technical Accounting Manager | Finance & Accounting | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Category Manager | Merchandising & Buying | 5 | 127 | 616 | 656 | 560 | 733 | 119 | 482 | 132 |
| VP for Merchandising | Merchandising & Buying | 1 | 59 | 182 | 123 | 919 | 542 | 87 | 353 | 102 |
| Merchandise Planner / Allocator | Merchandising & Buying | 6 | 51 | 105 | 171 | 23 | 122 | 12 | 91 | 19 |
| Buyer (incl. Senior Buyers) | Merchandising & Buying | 10 | 36 | 134 | 263 | 39 | 173 | 62 | 100 | 11 |
| Pricing Analyst | Merchandising & Buying | 4 | 35 | 74 | 133 | 13 | 99 | 15 | 75 | 9 |
| Merchandising Operations & Master Data Manager | Merchandising & Buying | 1 | 30 | 6 | 55 | 69 | 48 | 15 | 29 | 4 |
| Direct Sourcing / Import Buyer | Merchandising & Buying | 3 | 17 | 49 | 43 | 34 | 54 | 7 | 43 | 4 |
| Merchandising Operations Specialist | Merchandising & Buying | 3 | 11 | 5 | 5 | 2 | 16 | 2 | 14 | 0 |
| Pricing Manager | Merchandising & Buying | 1 | 8 | 6 | 17 | 14 | 16 | 4 | 11 | 1 |
| Private Brand Product Manager | Merchandising & Buying | 3 | 4 | 13 | 14 | 6 | 15 | 4 | 11 | 0 |
| Assortment & Space Analyst | Merchandising & Buying | 3 | 4 | 8 | 16 | 0 | 8 | 3 | 5 | 0 |
| Promotions & Vendor-Funding Coordinator | Merchandising & Buying | 3 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| VP Supply Chain & Logistics (dual-hat GM, BuildRight Logistics, Inc.) | Supply Chain & Logistics | 1 | 58 | 128 | 112 | 528 | 338 | 85 | 180 | 73 |
| Fleet Compliance & Safety Specialist | Supply Chain & Logistics | 1 | 49 | 35 | 146 | 20 | 37 | 22 | 13 | 2 |
| Fleet & Logistics Manager | Supply Chain & Logistics | 1 | 45 | 57 | 148 | 200 | 145 | 27 | 93 | 25 |
| DC Operations Manager | Supply Chain & Logistics | 1 | 38 | 33 | 67 | 110 | 84 | 29 | 48 | 7 |
| Procurement Manager | Supply Chain & Logistics | 1 | 35 | 55 | 87 | 99 | 97 | 35 | 45 | 17 |
| Logistics Coordinator | Supply Chain & Logistics | 2 | 28 | 34 | 71 | 24 | 47 | 9 | 37 | 1 |
| Import Coordinator | Supply Chain & Logistics | 2 | 15 | 38 | 70 | 15 | 50 | 25 | 22 | 3 |
| S&OP/IBP Lead | Supply Chain & Logistics | 1 | 13 | 20 | 47 | 90 | 33 | 13 | 17 | 3 |
| DC Operations Coordinator | Supply Chain & Logistics | 8 | 11 | 17 | 36 | 12 | 19 | 10 | 8 | 1 |
| Vendor Management Manager | Supply Chain & Logistics | 1 | 9 | 29 | 8 | 16 | 46 | 15 | 24 | 7 |
| Procurement Coordinator | Supply Chain & Logistics | 2 | 6 | 9 | 17 | 5 | 13 | 4 | 8 | 1 |
| Customs Broker | Supply Chain & Logistics | 2 | 5 | 26 | 30 | 11 | 27 | 20 | 5 | 2 |
| Inventory Planning Manager | Supply Chain & Logistics | 1 | 4 | 2 | 12 | 10 | 13 | 5 | 8 | 0 |
| Supply & Allocation Planner | Supply Chain & Logistics | 1 | 3 | 21 | 43 | 9 | 29 | 10 | 18 | 1 |
| Demand Planner | Supply Chain & Logistics | 2 | 3 | 8 | 25 | 2 | 11 | 6 | 3 | 2 |
| Inventory Planner | Supply Chain & Logistics | 2 | 3 | 6 | 16 | 5 | 11 | 7 | 4 | 0 |
| Imports & Customs Manager | Supply Chain & Logistics | 1 | 3 | 1 | 0 | 2 | 3 | 2 | 1 | 0 |
| Vendor Scorecard & Performance Analyst | Supply Chain & Logistics | 1 | 2 | 7 | 6 | 4 | 8 | 3 | 4 | 1 |
| 3PL & Freight Specialist | Supply Chain & Logistics | 2 | 2 | 0 | 9 | 8 | 3 | 0 | 3 | 0 |
| Vendor Portal & Collaboration Specialist | Supply Chain & Logistics | 2 | 1 | 2 | 12 | 1 | 2 | 1 | 1 | 0 |
| Senior Demand Planner | Supply Chain & Logistics | 1 | 0 | 2 | 1 | 0 | 3 | 3 | 0 | 0 |
| DC Operations Analyst | Supply Chain & Logistics | 1 | 0 | 2 | 1 | 0 | 2 | 0 | 1 | 1 |
| Import Documentation Specialist | Supply Chain & Logistics | 1 | 0 | 2 | 1 | 0 | 2 | 1 | 1 | 0 |
| Purchasing / PO Specialist | Supply Chain & Logistics | 6 | 0 | 2 | 1 | 0 | 2 | 2 | 0 | 0 |
| Replenishment & Allocation Analyst | Supply Chain & Logistics | 2 | 0 | 1 | 1 | 0 | 2 | 1 | 1 | 0 |
| Learning & Development Manager | Human Resources | 1 | 39 | 38 | 115 | 18 | 47 | 9 | 34 | 4 |
| Compensation & Benefits Manager | Human Resources | 1 | 24 | 38 | 79 | 2 | 41 | 7 | 30 | 4 |
| HR Shared Services Lead | Human Resources | 1 | 21 | 7 | 11 | 18 | 31 | 2 | 26 | 3 |
| Labor Relations Director | Human Resources | 1 | 19 | 21 | 40 | 4 | 26 | 12 | 12 | 2 |
| People Analytics Analyst | Human Resources | 1 | 13 | 21 | 40 | 0 | 26 | 0 | 9 | 17 |
| Payroll Manager | Human Resources | 1 | 11 | 15 | 31 | 51 | 30 | 19 | 10 | 1 |
| HR Business Partner (one per region) | Human Resources | 6 | 10 | 47 | 84 | 17 | 55 | 22 | 28 | 5 |
| Labor Relations Specialist | Human Resources | 2 | 6 | 26 | 20 | 0 | 28 | 4 | 24 | 0 |
| Benefits Specialist | Human Resources | 2 | 5 | 1 | 10 | 2 | 6 | 5 | 1 | 0 |
| L&D Specialist / Trainer | Human Resources | 4 | 5 | 0 | 11 | 12 | 6 | 0 | 5 | 1 |
| Payroll Specialist | Human Resources | 4 | 4 | 21 | 58 | 8 | 29 | 18 | 10 | 1 |
| Store HR Coordinator (one per district) | Human Resources | 13 | 4 | 3 | 13 | 16 | 7 | 1 | 6 | 0 |
| HRIS & HR-Technology Administrator | Human Resources | 1 | 4 | 2 | 11 | 5 | 5 | 1 | 4 | 0 |
| VP Human Resources | Human Resources | 1 | 3 | 7 | 20 | 37 | 22 | 7 | 15 | 0 |
| Talent Acquisition Manager | Human Resources | 1 | 3 | 3 | 9 | 34 | 16 | 0 | 13 | 3 |
| Talent Acquisition Specialist | Human Resources | 5 | 3 | 2 | 9 | 8 | 5 | 1 | 2 | 2 |
| HR Services Specialist | Human Resources | 4 | 2 | 1 | 8 | 8 | 3 | 2 | 1 | 0 |
| Compensation Analyst | Human Resources | 1 | 0 | 2 | 1 | 0 | 3 | 0 | 2 | 1 |
| Timekeeping & Attendance Analyst | Human Resources | 1 | 0 | 2 | 1 | 0 | 3 | 2 | 1 | 0 |
| Payroll Supervisor | Human Resources | 1 | 0 | 2 | 1 | 0 | 2 | 1 | 1 | 0 |
| Sourcing & Screening Coordinator | Human Resources | 1 | 0 | 1 | 2 | 0 | 2 | 0 | 2 | 0 |
| Payroll & Statutory Remittance Officer | Human Resources | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| TA Coordinator | Human Resources | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Marketplace Manager | Marketing | 2 | 34 | 66 | 59 | 92 | 79 | 10 | 53 | 16 |
| Marketing Operations Manager | Marketing | 1 | 25 | 30 | 52 | 56 | 56 | 7 | 31 | 18 |
| Loyalty & CRM Manager | Marketing | 1 | 25 | 30 | 68 | 41 | 43 | 3 | 28 | 12 |
| Retail Media & Marketplace Manager | Marketing | 1 | 25 | 7 | 53 | 19 | 30 | 2 | 22 | 6 |
| Promotions & Campaigns Manager | Marketing | 1 | 22 | 0 | 0 | 0 | 22 | 1 | 20 | 1 |
| Consumer Insights Manager | Marketing | 1 | 21 | 24 | 35 | 4 | 34 | 1 | 11 | 22 |
| Brand & Communications Manager | Marketing | 1 | 19 | 67 | 75 | 4 | 86 | 21 | 57 | 8 |
| Digital Marketing Manager | Marketing | 3 | 19 | 23 | 57 | 10 | 28 | 1 | 13 | 14 |
| Content & Creative Specialist | Marketing | 2 | 17 | 19 | 71 | 36 | 28 | 3 | 15 | 10 |
| Insights Analyst | Marketing | 2 | 16 | 26 | 46 | 4 | 26 | 1 | 13 | 12 |
| VP Marketing | Marketing | 1 | 10 | 45 | 20 | 174 | 110 | 9 | 69 | 32 |
| Brand Manager | Marketing | 1 | 8 | 17 | 25 | 1 | 26 | 0 | 22 | 4 |
| CRM Manager | Marketing | 1 | 4 | 6 | 6 | 16 | 10 | 3 | 2 | 5 |
| CRM Data Steward | Marketing | 2 | 3 | 5 | 11 | 4 | 5 | 3 | 2 | 0 |
| Campaign Manager | Marketing | 2 | 2 | 14 | 28 | 5 | 14 | 3 | 8 | 3 |
| Performance-Marketing Specialist | Marketing | 2 | 1 | 4 | 16 | 0 | 4 | 0 | 1 | 3 |
| Marketing Comms Specialist | Marketing | 1 | 1 | 0 | 2 | 0 | 2 | 0 | 1 | 1 |
| Retail Media Operations Specialist | Marketing | 1 | 0 | 2 | 1 | 0 | 2 | 0 | 1 | 1 |
| Ecommerce Marketing Specialist | Marketing | 2 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Promotions Specialist | Marketing | 2 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| VP Store Operations (Director Field Retail Operations) | Store Operations | 1 | 98 | 166 | 212 | 539 | 366 | 66 | 242 | 58 |
| Retail Standards & Store-Opening Manager (Store Support Center lead) | Store Operations | 1 | 31 | 26 | 24 | 37 | 53 | 9 | 42 | 2 |
| Regional Manager | Store Operations | 6 | 28 | 116 | 140 | 201 | 209 | 62 | 125 | 22 |
| OpEx / Continuous-Improvement Process Lead | Store Operations | 1 | 27 | 34 | 104 | 26 | 56 | 1 | 28 | 27 |
| District Manager | Store Operations | 13 | 9 | 11 | 26 | 25 | 23 | 5 | 17 | 1 |
| Facilities Coordination Specialist | Store Operations | 1 | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Field Communications Manager | Store Operations | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| VP Legal & Compliance | Legal & Compliance | 1 | 109 | 131 | 184 | 1114 | 636 | 200 | 388 | 48 |
| Compliance Manager / MLRO | Legal & Compliance | 1 | 60 | 31 | 104 | 167 | 125 | 45 | 67 | 13 |
| Government Affairs Manager | Legal & Compliance | 1 | 43 | 41 | 95 | 25 | 59 | 5 | 51 | 3 |
| Data Privacy Officer (DPO) | Legal & Compliance | 1 | 38 | 103 | 159 | 127 | 136 | 52 | 74 | 10 |
| Corporate Secretary | Legal & Compliance | 1 | 38 | 41 | 123 | 19 | 61 | 21 | 35 | 5 |
| Regulatory Affairs Specialist | Legal & Compliance | 3 | 29 | 5 | 74 | 58 | 38 | 20 | 17 | 1 |
| Litigation & IP Counsel | Legal & Compliance | 2 | 20 | 30 | 73 | 21 | 43 | 17 | 25 | 1 |
| Customs & Trade Compliance Specialist | Legal & Compliance | 1 | 13 | 25 | 48 | 10 | 27 | 16 | 11 | 0 |
| Compliance Analyst | Legal & Compliance | 1 | 12 | 0 | 12 | 3 | 12 | 7 | 5 | 0 |
| AML / ABC Officer | Legal & Compliance | 1 | 7 | 42 | 26 | 4 | 45 | 19 | 23 | 3 |
| Paralegal / Contracts Specialist | Legal & Compliance | 2 | 2 | 0 | 2 | 4 | 2 | 0 | 2 | 0 |
| Legal Counsel — Contracts | Legal & Compliance | 2 | 1 | 0 | 1 | 4 | 2 | 0 | 1 | 1 |
| Privacy Officer | Legal & Compliance | 1 | 1 | 0 | 1 | 0 | 2 | 1 | 1 | 0 |
| Corporate Secretary Analyst | Legal & Compliance | 1 | 0 | 2 | 1 | 0 | 2 | 1 | 1 | 0 |
| Contracts & Commercial Manager (Senior Counsel) | Legal & Compliance | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| ERM & TPRM Analyst | Internal Audit & Risk | 1 | 29 | 28 | 106 | 60 | 59 | 11 | 44 | 4 |
| Head of Internal Audit & Risk | Internal Audit & Risk | 1 | 27 | 11 | 76 | 276 | 148 | 17 | 85 | 46 |
| Internal Auditor | Internal Audit & Risk | 2 | 7 | 8 | 25 | 14 | 14 | 5 | 8 | 1 |
| IT / ERP Auditor | Internal Audit & Risk | 2 | 6 | 0 | 25 | 6 | 13 | 0 | 0 | 13 |
| Senior Internal Auditor | Internal Audit & Risk | 1 | 3 | 0 | 2 | 45 | 21 | 0 | 0 | 21 |
| Field Compliance Auditor | Internal Audit & Risk | 4 | 0 | 3 | 2 | 0 | 3 | 0 | 2 | 1 |
| Audit Manager | Internal Audit & Risk | 1 | 0 | 2 | 1 | 0 | 2 | 0 | 0 | 2 |
| Forensic / Fraud Investigator | Internal Audit & Risk | 1 | 0 | 2 | 1 | 0 | 2 | 2 | 0 | 0 |
| Operations Compliance Lead | Internal Audit & Risk | 1 | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Customer Service Representative | Customer Service | 22 | 24 | 44 | 54 | 3 | 64 | 9 | 48 | 7 |
| Head of Customer Service | Customer Service | 1 | 21 | 18 | 18 | 68 | 53 | 10 | 38 | 5 |
| Contact Center Supervisor | Customer Service | 2 | 8 | 17 | 14 | 25 | 24 | 8 | 12 | 4 |
| Services Manager | Customer Service | 1 | 5 | 10 | 15 | 45 | 24 | 9 | 10 | 5 |
| Ecommerce Support Specialist | Customer Service | 3 | 2 | 2 | 1 | 0 | 2 | 2 | 0 | 0 |
| B2B Support Representative | Customer Service | 4 | 0 | 2 | 1 | 0 | 3 | 0 | 2 | 1 |
| Quality & Workforce Analyst | Customer Service | 2 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Director, Regional Loss Prevention | Regional Loss Prevention | 1 | 54 | 28 | 101 | 169 | 103 | 24 | 70 | 9 |
| LP Analytics Analyst | Regional Loss Prevention | 2 | 20 | 30 | 95 | 9 | 50 | 20 | 23 | 7 |
| Regional LP Officer | Regional Loss Prevention | 20 | 12 | 47 | 77 | 26 | 59 | 29 | 29 | 1 |
| LP Investigator | Regional Loss Prevention | 2 | 3 | 8 | 25 | 0 | 12 | 8 | 3 | 1 |
| Senior LP Investigator | Regional Loss Prevention | 1 | 3 | 3 | 7 | 0 | 3 | 3 | 0 | 0 |
| Senior LP Analytics Analyst | Regional Loss Prevention | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Head of HSE | Health, Safety & Environment | 1 | 24 | 9 | 35 | 163 | 86 | 28 | 53 | 5 |
| Safety Officer (HSE Officer, DOLE-accredited SO2) | Health, Safety & Environment | 10 | 23 | 78 | 145 | 63 | 107 | 51 | 46 | 10 |
| Company Nurse | Health, Safety & Environment | 1 | 9 | 35 | 40 | 0 | 27 | 11 | 16 | 0 |
| Wellness Coordinator | Health, Safety & Environment | 1 | 1 | 1 | 2 | 0 | 2 | 0 | 2 | 0 |
| Head of Quality Management | Quality Management | 1 | 34 | 38 | 128 | 170 | 117 | 29 | 79 | 9 |
| Metrology & Weights-Measures Specialist | Quality Management | 1 | 25 | 39 | 85 | 5 | 29 | 3 | 22 | 4 |
| Quality Inspector (Incoming Inspection) | Quality Management | 2 | 3 | 15 | 27 | 1 | 20 | 5 | 13 | 2 |
| Supplier-Quality (Vendor QA) Auditor | Quality Management | 1 | 1 | 2 | 5 | 4 | 3 | 0 | 3 | 0 |
| Energy Manager | Facilities & Real Estate | 1 | 51 | 66 | 143 | 104 | 73 | 4 | 52 | 17 |
| Facilities Manager | Facilities & Real Estate | 2 | 24 | 23 | 90 | 67 | 60 | 7 | 36 | 17 |
| Surety Program Manager | Facilities & Real Estate | 1 | 23 | 24 | 65 | 1 | 24 | 4 | 16 | 4 |
| Director, Facilities & Real Estate (dual-hat GM, BuildRight Property Mgmt, Inc.) | Facilities & Real Estate | 1 | 14 | 0 | 0 | 0 | 14 | 3 | 10 | 1 |
| Lease Administrator | Facilities & Real Estate | 1 | 13 | 25 | 35 | 4 | 30 | 4 | 24 | 2 |
| Facilities Coordinator | Facilities & Real Estate | 3 | 8 | 27 | 40 | 23 | 35 | 10 | 24 | 1 |
| Real-Estate & Site-Selection Analyst | Facilities & Real Estate | 1 | 0 | 2 | 2 | 0 | 3 | 0 | 3 | 0 |
| Maintenance & Projects Coordinator | Facilities & Real Estate | 2 | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Head of Sustainability / ESG (Sustainability/ESG Manager) | Sustainability / ESG | 1 | 75 | 51 | 173 | 182 | 138 | 16 | 76 | 46 |
| Environmental Compliance Specialist | Sustainability / ESG | 1 | 25 | 13 | 84 | 59 | 37 | 15 | 19 | 3 |
| Sustainability Coordinator | Sustainability / ESG | 1 | 20 | 40 | 77 | 3 | 49 | 2 | 33 | 14 |
| ESG Reporting & Data Analyst | Sustainability / ESG | 1 | 1 | 0 | 6 | 0 | 2 | 1 | 0 | 1 |
| Head of Strategy & Corporate Planning | Strategy / Corporate Planning | 1 | 32 | 78 | 109 | 31 | 95 | 3 | 79 | 13 |
| Competitive Intelligence Manager | Strategy / Corporate Planning | 1 | 2 | 4 | 0 | 1 | 5 | 0 | 3 | 2 |
| Document Control Coordinator | Strategy / Corporate Planning | 1 | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Business Process & IMS Lead | Strategy / Corporate Planning | 1 | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| CPM (Corporate Performance Management) Analyst | Strategy / Corporate Planning | 1 | 0 | 2 | 1 | 0 | 2 | 0 | 1 | 1 |
| Strategy Analyst | Strategy / Corporate Planning | 1 | 0 | 2 | 1 | 0 | 2 | 1 | 0 | 1 |
| Trade Account Manager | Trade / Account Management | 2 | 22 | 54 | 90 | 13 | 56 | 13 | 38 | 5 |
| Key Account Manager | Trade / Account Management | 2 | 16 | 25 | 52 | 18 | 34 | 7 | 25 | 2 |
| Head of Trade & Account Management | Trade / Account Management | 1 | 11 | 4 | 20 | 58 | 41 | 2 | 29 | 10 |
| Trade Operations & Analytics Specialist | Trade / Account Management | 1 | 7 | 8 | 27 | 19 | 10 | 2 | 8 | 0 |
| Trade Professional Program Coordinator | Trade / Account Management | 1 | 3 | 2 | 7 | 5 | 4 | 0 | 3 | 1 |
| Shift Supervisor (DC roster) | Information Technology (product model) | — | 11 | 32 | 57 | 129 | 81 | 39 | 41 | 1 |
| Board of Directors | Information Technology (product model) | — | 1 | 20 | 6 | 37 | 31 | 5 | 18 | 8 |

## Information Technology product-model seats (§5.3 by reference)

| Role | Dept / source | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|
| DP BI Platform | Information Technology (product model) | 98 | 255 | 521 | 67 | 378 | 39 | 154 | 185 |
| IT Product Manager (build squad) | Information Technology (product model) | 54 | 32 | 88 | 95 | 88 | 19 | 52 | 17 |
| Head of Enterprise Architecture (CIO Office) | Information Technology (product model) | 48 | 80 | 136 | 54 | 88 | 6 | 72 | 10 |
| SEC (Cybersecurity, Privacy & OT Security) | Information Technology (product model) | 35 | 201 | 233 | 2 | 224 | 74 | 141 | 9 |
| IT Operations (FS/INFRA) | Information Technology (product model) | 29 | 48 | 57 | 42 | 81 | 22 | 48 | 11 |
| AAP AI-Governance Liaison | Information Technology (product model) | 28 | 25 | 72 | 56 | 27 | 13 | 10 | 4 |
| SEC Security Engineer | Information Technology (product model) | 27 | 16 | 83 | 47 | 50 | 13 | 31 | 6 |
| FS ITAM Administrator | Information Technology (product model) | 25 | 40 | 68 | 66 | 58 | 8 | 44 | 6 |
| DP Customer Data Platform | Information Technology (product model) | 25 | 32 | 83 | 73 | 34 | 2 | 24 | 8 |
| DP MDM Steward | Information Technology (product model) | 22 | 28 | 72 | 30 | 43 | 14 | 24 | 5 |
| Build-Squad Software Engineer | Information Technology (product model) | 21 | 27 | 49 | 6 | 34 | 11 | 18 | 5 |
| SEC OT Security Lead | Information Technology (product model) | 13 | 0 | 30 | 76 | 24 | 4 | 17 | 3 |
| DP Data Scientist / ML | Information Technology (product model) | 11 | 18 | 50 | 7 | 23 | 5 | 5 | 13 |
| IT Helpdesk Agent (FS) | Information Technology (product model) | 9 | 34 | 69 | 17 | 47 | 19 | 25 | 3 |
| DP / Data & Analytics (VS-28) | Information Technology (product model) | 8 | 28 | 22 | 0 | 38 | 6 | 20 | 12 |
| INFRA System Administrator | Information Technology (product model) | 6 | 12 | 29 | 6 | 17 | 8 | 7 | 2 |
| IT Product Owner | Information Technology (product model) | 6 | 0 | 1 | 0 | 7 | 0 | 7 | 0 |
| SEC Security Analyst | Information Technology (product model) | 4 | 9 | 52 | 15 | 31 | 5 | 22 | 4 |
| INFRA DBA / SaaS Administrator | Information Technology (product model) | 4 | 22 | 35 | 3 | 25 | 15 | 10 | 0 |
| INFRA Cloud Engineer | Information Technology (product model) | 4 | 1 | 0 | 0 | 5 | 1 | 3 | 1 |
| DP Data & Reporting Analyst | Information Technology (product model) | 3 | 9 | 26 | 1 | 17 | 2 | 6 | 9 |
| DP Data Engineer | Information Technology (product model) | 3 | 6 | 24 | 2 | 9 | 3 | 2 | 4 |
| ERP Functional Analyst | Information Technology (product model) | 3 | 3 | 10 | 0 | 7 | 2 | 1 | 4 |
| Strategy / Corporate Planning (PMO) | Information Technology (product model) | 3 | 4 | 15 | 12 | 7 | 1 | 6 | 0 |
| INFRA Network Engineer | Information Technology (product model) | 1 | 14 | 73 | 33 | 37 | 7 | 25 | 5 |
| Build-Squad QA Automation Engineer | Information Technology (product model) | 1 | 3 | 12 | 5 | 5 | 0 | 4 | 1 |
| AAP Agent Engineer | Information Technology (product model) | 1 | 2 | 4 | 5 | 2 | 0 | 2 | 0 |
| INFRA Site Reliability Engineer | Information Technology (product model) | 1 | 2 | 5 | 0 | 2 | 0 | 2 | 0 |
| Information Technology (department) | Information Technology (product model) | 0 | 1 | 22 | 1 | 15 | 8 | 6 | 1 |
| Build-Squad Tech Lead | Information Technology (product model) | 0 | 1 | 2 | 0 | 2 | 0 | 1 | 1 |
| IAP Integration Support Engineer | Information Technology (product model) | 0 | 2 | 2 | 1 | 2 | 1 | 1 | 0 |
| IAP Integration Engineer | Information Technology (product model) | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |

## Store field roles (§7.2 roster)

| Role | Dept / source | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|
| Store Manager | Store (field, per-store roster) | 257 | 677 | 1027 | 1197 | 998 | 354 | 549 | 95 |
| Department Supervisor | Store (field, per-store roster) | 120 | 57 | 190 | 316 | 238 | 53 | 167 | 18 |
| Department Supervisors | Store (field, per-store roster) | 117 | 190 | 275 | 477 | 290 | 83 | 185 | 22 |
| Sales Associate | Store (field, per-store roster) | 78 | 288 | 799 | 99 | 376 | 85 | 253 | 38 |
| Customer Service Rep | Store (field, per-store roster) | 60 | 99 | 295 | 36 | 136 | 45 | 81 | 10 |
| Cashiers | Store (field, per-store roster) | 31 | 106 | 273 | 11 | 169 | 69 | 84 | 16 |
| Cashier | Store (field, per-store roster) | 26 | 26 | 77 | 18 | 45 | 19 | 19 | 7 |
| Maintenance | Store (field, per-store roster) | 24 | 87 | 164 | 18 | 109 | 34 | 62 | 13 |
| Assistant Store Manager | Store (field, per-store roster) | 10 | 15 | 14 | 20 | 25 | 11 | 13 | 1 |
| Receiving lead | Store (field, per-store roster) | 9 | 17 | 20 | 1 | 22 | 13 | 9 | 0 |
| Stock Associate | Store (field, per-store roster) | 8 | 106 | 268 | 6 | 164 | 61 | 92 | 11 |
| ASM | Store (field, per-store roster) | 0 | 0 | 6 | 2 | 1 | 1 | 0 | 0 |

## DC field roles (§7.3 roster)

| Role | Dept / source | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|
| DC Manager | DC (field, per-DC roster) | 18 | 133 | 99 | 147 | 209 | 82 | 98 | 29 |
| Receiving Clerks | DC (field, per-DC roster) | 18 | 72 | 166 | 9 | 112 | 35 | 71 | 6 |
| Shift Supervisors | DC (field, per-DC roster) | 14 | 7 | 9 | 31 | 17 | 12 | 4 | 1 |
| Inventory Control Supervisor | DC (field, per-DC roster) | 11 | 22 | 27 | 30 | 26 | 7 | 17 | 2 |
| Dispatch Coordinators | DC (field, per-DC roster) | 9 | 19 | 49 | 27 | 35 | 18 | 12 | 5 |
| Returns Processors | DC (field, per-DC roster) | 8 | 13 | 18 | 0 | 16 | 5 | 11 | 0 |
| Outbound/Shipping Supervisor | DC (field, per-DC roster) | 6 | 8 | 12 | 7 | 11 | 7 | 1 | 3 |
| Incoming Inspection Checkers | DC (field, per-DC roster) | 5 | 11 | 31 | 0 | 14 | 4 | 10 | 0 |
| Safety & Compliance Coordinator | DC (field, per-DC roster) | 5 | 5 | 17 | 12 | 9 | 3 | 4 | 2 |
| Receiving Supervisor | DC (field, per-DC roster) | 4 | 15 | 17 | 17 | 19 | 9 | 8 | 2 |
| MHE Maintenance Technicians | DC (field, per-DC roster) | 4 | 3 | 4 | 8 | 5 | 0 | 4 | 1 |
| Loaders / Staging | DC (field, per-DC roster) | 3 | 8 | 12 | 0 | 9 | 2 | 6 | 1 |
| Assistant DC Manager — Inbound | DC (field, per-DC roster) | 2 | 2 | 8 | 1 | 2 | 1 | 1 | 0 |
| Lumber / Long-Length Crew | DC (field, per-DC roster) | 2 | 1 | 3 | 2 | 2 | 0 | 2 | 0 |
| Certified Hazmat/Paint Handlers | DC (field, per-DC roster) | 1 | 3 | 4 | 0 | 3 | 3 | 0 | 0 |
| Order Pickers | DC (field, per-DC roster) | 0 | 15 | 19 | 0 | 18 | 8 | 8 | 2 |
| Forklift Operators (inbound) | DC (field, per-DC roster) | 0 | 15 | 9 | 0 | 15 | 5 | 8 | 2 |
| Packers / Load Builders | DC (field, per-DC roster) | 0 | 5 | 9 | 0 | 8 | 6 | 2 | 0 |
| Putaway Staff | DC (field, per-DC roster) | 0 | 4 | 4 | 0 | 4 | 2 | 0 | 2 |
| Cross-Dock Team | DC (field, per-DC roster) | 0 | 2 | 1 | 0 | 2 | 0 | 1 | 1 |
| Assistant DC Manager — Outbound | DC (field, per-DC roster) | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Cycle Counters | DC (field, per-DC roster) | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| DC Office Administrator | DC (field, per-DC roster) | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Discrepancy Analysts | DC (field, per-DC roster) | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Facilities/Utility | DC (field, per-DC roster) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Special Handling Lead | DC (field, per-DC roster) | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Tile & Heavy/Breakbulk Crew | DC (field, per-DC roster) | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |

## Department-level actors (department or generic form named as performer)

| Role | Dept / source | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|
| Chief Of Staff | Executive Office | 1 | 0 | 1 | 0 | 2 | 1 | 0 | 1 |
| Ceo Office | Executive Office | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Vp | Executive Office | 0 | 0 | 4 | 10 | 9 | 6 | 3 | 0 |
| Head Of Corp Dev | Executive Office | 0 | 1 | 0 | 12 | 7 | 0 | 7 | 0 |
| Corp Sec | Executive Office | 0 | 2 | 9 | 3 | 6 | 2 | 1 | 3 |
| Executive | Executive Office | 0 | 5 | 1 | 0 | 6 | 1 | 5 | 0 |
| Entity Controllers | Executive Office | 0 | 5 | 3 | 1 | 5 | 4 | 1 | 0 |
| All Vps | Executive Office | 0 | 0 | 4 | 0 | 4 | 0 | 2 | 2 |
| C-Suite Sponsor | Executive Office | 0 | 0 | 0 | 5 | 4 | 0 | 4 | 0 |
| Corporate Affairs | Executive Office | 0 | 3 | 1 | 0 | 3 | 1 | 1 | 1 |
| Function Vps | Executive Office | 0 | 2 | 0 | 1 | 3 | 1 | 2 | 0 |
| Affected Executives | Executive Office | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| All Directors | Executive Office | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Corp Affairs | Executive Office | 0 | 0 | 2 | 0 | 2 | 0 | 1 | 1 |
| Corporate Customer | Executive Office | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Digital Commerce Entity | Executive Office | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Entity Accountants | Executive Office | 0 | 2 | 3 | 0 | 2 | 2 | 0 | 0 |
| Entity Cfo | Executive Office | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Entity Heads | Executive Office | 0 | 0 | 2 | 0 | 2 | 1 | 1 | 0 |
| Principals' Offices | Executive Office | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Affected Site Leadership | Executive Office | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| All Affected Function Vps | Executive Office | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| All C-Suite | Executive Office | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| All Function Vps | Executive Office | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| All Functional Vps | Executive Office | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| C-Suite Executives | Executive Office | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Corporate Approver | Executive Office | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| Corporate Buyer | Executive Office | 0 | 1 | 2 | 0 | 1 | 0 | 0 | 1 |
| Corporate Sales Mgr | Executive Office | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Corporate Secretariat | Executive Office | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Corporate Sponsors | Executive Office | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Corporate Treasurer | Executive Office | 0 | 0 | 0 | 6 | 1 | 0 | 1 | 0 |
| Customer C-Suite | Executive Office | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Entity | Executive Office | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Entity Accountant | Executive Office | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Entity Hr-Legal | Executive Office | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Entity Leadership | Executive Office | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Executive Assistant | Executive Office | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Executives Attending Industry Forums | Executive Office | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Exposed Function'S Vp | Executive Office | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Function Heads | Executive Office | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Functional Vps | Executive Office | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Ic Settlement Team | Executive Office | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Management Presenters | Executive Office | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ops Leadership | Executive Office | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Pilot Site Leadership | Executive Office | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Principals' Households | Executive Office | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Requesting Entity Dept. Head | Executive Office | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Requesting Entity Staff | Executive Office | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Respective Vp | Executive Office | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Responsible Vp | Executive Office | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Sales Leadership | Executive Office | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 |
| Unit Leadership | Executive Office | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Vendor Executives | Executive Office | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Finance | Finance & Accounting | 144 | 1044 | 1130 | 54 | 1223 | 253 | 753 | 217 |
| Treasury | Finance & Accounting | 50 | 256 | 258 | 4 | 297 | 89 | 180 | 28 |
| Finance Analyst | Finance & Accounting | 30 | 60 | 158 | 5 | 116 | 29 | 62 | 25 |
| Vp Investor Relations | Finance & Accounting | 24 | 0 | 0 | 0 | 24 | 3 | 18 | 3 |
| Abl & Collateral Operations Manager | Finance & Accounting | 23 | 0 | 0 | 0 | 23 | 10 | 11 | 2 |
| Finance Manager | Finance & Accounting | 22 | 78 | 80 | 283 | 197 | 81 | 98 | 18 |
| Payment Ops | Finance & Accounting | 19 | 6 | 41 | 1 | 27 | 7 | 16 | 4 |
| Insurance Coordinator | Finance & Accounting | 7 | 19 | 38 | 8 | 26 | 11 | 14 | 1 |
| Project Accountant | Finance & Accounting | 7 | 11 | 28 | 9 | 16 | 3 | 13 | 0 |
| Cit Operations Manager | Finance & Accounting | 7 | 0 | 2 | 16 | 10 | 2 | 5 | 3 |
| Risk & Insurance Manager | Finance & Accounting | 7 | 0 | 5 | 9 | 9 | 1 | 8 | 0 |
| Insurance | Finance & Accounting | 6 | 96 | 64 | 0 | 108 | 36 | 68 | 4 |
| Actuarial | Finance & Accounting | 6 | 7 | 21 | 0 | 16 | 2 | 13 | 1 |
| Finance Desk | Finance & Accounting | 6 | 3 | 17 | 0 | 10 | 1 | 9 | 0 |
| Lease Operations Manager | Finance & Accounting | 6 | 0 | 0 | 13 | 8 | 2 | 6 | 0 |
| Lease Origination Manager | Finance & Accounting | 6 | 0 | 0 | 5 | 6 | 0 | 6 | 0 |
| Chief Accountant | Finance & Accounting | 5 | 20 | 47 | 14 | 25 | 17 | 8 | 0 |
| Fraud | Finance & Accounting | 5 | 21 | 20 | 0 | 25 | 3 | 20 | 2 |
| O2C | Finance & Accounting | 5 | 9 | 21 | 0 | 15 | 3 | 11 | 1 |
| Ar Analyst | Finance & Accounting | 5 | 6 | 26 | 6 | 9 | 3 | 6 | 0 |
| Ar | Finance & Accounting | 4 | 60 | 42 | 2 | 64 | 30 | 31 | 3 |
| Ar Accountant | Finance & Accounting | 4 | 7 | 26 | 4 | 10 | 6 | 4 | 0 |
| Claims Manager | Finance & Accounting | 4 | 0 | 0 | 9 | 6 | 1 | 3 | 2 |
| Ar Settlement Accountant | Finance & Accounting | 4 | 4 | 5 | 3 | 4 | 4 | 0 | 0 |
| Lease Portfolio Manager | Finance & Accounting | 4 | 0 | 0 | 4 | 4 | 0 | 1 | 3 |
| Leasing Manager | Finance & Accounting | 4 | 0 | 0 | 0 | 4 | 0 | 4 | 0 |
| Finance Business Partner | Finance & Accounting | 3 | 3 | 21 | 4 | 17 | 2 | 9 | 6 |
| Logistics Finance | Finance & Accounting | 3 | 8 | 5 | 0 | 9 | 2 | 4 | 3 |
| Consolidation | Finance & Accounting | 3 | 6 | 10 | 0 | 6 | 5 | 1 | 0 |
| Risk & Insurance | Finance & Accounting | 3 | 3 | 9 | 0 | 5 | 1 | 4 | 0 |
| Lease Credit Manager | Finance & Accounting | 3 | 0 | 1 | 3 | 3 | 0 | 3 | 0 |
| Ap | Finance & Accounting | 2 | 59 | 53 | 2 | 72 | 41 | 30 | 1 |
| Revenue Assurance | Finance & Accounting | 2 | 17 | 11 | 0 | 20 | 3 | 15 | 2 |
| Payments | Finance & Accounting | 2 | 15 | 11 | 0 | 16 | 13 | 3 | 0 |
| Gl | Finance & Accounting | 2 | 11 | 16 | 0 | 13 | 9 | 4 | 0 |
| Asset | Finance & Accounting | 2 | 6 | 5 | 0 | 7 | 0 | 7 | 0 |
| Cash Office | Finance & Accounting | 2 | 4 | 8 | 0 | 6 | 3 | 3 | 0 |
| Cash Office Clerk | Finance & Accounting | 2 | 4 | 13 | 0 | 5 | 5 | 0 | 0 |
| Finance Fp&A | Finance & Accounting | 2 | 3 | 2 | 0 | 5 | 0 | 3 | 2 |
| Marketing Finance | Finance & Accounting | 2 | 0 | 6 | 2 | 4 | 0 | 1 | 3 |
| Chargeback Analyst | Finance & Accounting | 2 | 2 | 4 | 1 | 3 | 0 | 3 | 0 |
| Fixed-Asset | Finance & Accounting | 2 | 3 | 1 | 0 | 3 | 1 | 2 | 0 |
| It Finance Lead | Finance & Accounting | 2 | 1 | 3 | 0 | 3 | 1 | 2 | 0 |
| B2B Account Billing Clerk | Finance & Accounting | 2 | 0 | 2 | 8 | 2 | 2 | 0 | 0 |
| Cash Application Clerk | Finance & Accounting | 2 | 0 | 8 | 8 | 2 | 1 | 1 | 0 |
| Finance Fp&A Analyst | Finance & Accounting | 2 | 0 | 8 | 8 | 2 | 1 | 0 | 1 |
| Fixed Assets | Finance & Accounting | 2 | 1 | 2 | 0 | 2 | 0 | 2 | 0 |
| Fuel & Fleet Cost Manager | Finance & Accounting | 2 | 0 | 4 | 9 | 2 | 0 | 2 | 0 |
| Import Finance | Finance & Accounting | 2 | 0 | 6 | 0 | 2 | 2 | 0 | 0 |
| It Finance Analyst | Finance & Accounting | 2 | 2 | 5 | 0 | 2 | 0 | 1 | 1 |
| Leasing Product Manager | Finance & Accounting | 2 | 0 | 0 | 1 | 2 | 0 | 1 | 1 |
| Payment Operations | Finance & Accounting | 2 | 0 | 0 | 0 | 2 | 1 | 1 | 0 |
| Workout/Recovery Manager | Finance & Accounting | 2 | 0 | 0 | 0 | 2 | 1 | 1 | 0 |
| Abl Manager | Finance & Accounting | 1 | 0 | 33 | 12 | 20 | 7 | 12 | 1 |
| Shared Services | Finance & Accounting | 1 | 13 | 11 | 0 | 13 | 5 | 7 | 1 |
| Asset Mgmt | Finance & Accounting | 1 | 7 | 15 | 0 | 11 | 0 | 11 | 0 |
| Cash Mgmt | Finance & Accounting | 1 | 8 | 9 | 0 | 9 | 6 | 3 | 0 |
| Claims | Finance & Accounting | 1 | 6 | 7 | 0 | 8 | 1 | 5 | 2 |
| Accountant | Finance & Accounting | 1 | 2 | 6 | 1 | 5 | 3 | 2 | 0 |
| Ar Specialist | Finance & Accounting | 1 | 4 | 4 | 4 | 5 | 0 | 5 | 0 |
| Inventory Accountant | Finance & Accounting | 1 | 3 | 7 | 2 | 5 | 1 | 4 | 0 |
| Risk Manager | Finance & Accounting | 1 | 2 | 10 | 5 | 5 | 2 | 2 | 1 |
| Insurance Administrator | Finance & Accounting | 1 | 3 | 5 | 4 | 4 | 1 | 3 | 0 |
| Cit | Finance & Accounting | 1 | 3 | 2 | 0 | 3 | 2 | 1 | 0 |
| Services Finance Analyst | Finance & Accounting | 1 | 0 | 5 | 0 | 3 | 0 | 2 | 1 |
| Trade Credit | Finance & Accounting | 1 | 3 | 2 | 0 | 3 | 1 | 2 | 0 |
| Treasury-Surety | Finance & Accounting | 1 | 1 | 4 | 0 | 3 | 0 | 2 | 1 |
| Accounts Payable | Finance & Accounting | 1 | 1 | 2 | 0 | 2 | 2 | 0 | 0 |
| Insurance & Risk Officer | Finance & Accounting | 1 | 2 | 3 | 2 | 2 | 0 | 2 | 0 |
| Property Controller | Finance & Accounting | 1 | 1 | 2 | 3 | 2 | 0 | 2 | 0 |
| Vault Operations Supervisor | Finance & Accounting | 1 | 0 | 0 | 3 | 2 | 2 | 0 | 0 |
| Ar & Settlement Accountant | Finance & Accounting | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Ar Finance | Finance & Accounting | 1 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| B2B Ar Specialist | Finance & Accounting | 1 | 0 | 4 | 4 | 1 | 1 | 0 | 0 |
| B2B Finance Lead | Finance & Accounting | 1 | 0 | 4 | 4 | 1 | 0 | 0 | 1 |
| B2B Risk Manager | Finance & Accounting | 1 | 0 | 4 | 4 | 1 | 0 | 1 | 0 |
| Bulky-Delivery Finance | Finance & Accounting | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Cash Applications | Finance & Accounting | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Claims Analyst | Finance & Accounting | 1 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Cod Controller | Finance & Accounting | 1 | 0 | 4 | 4 | 1 | 1 | 0 | 0 |
| Consolidation Manager | Finance & Accounting | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Controllership | Finance & Accounting | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Damage Claims | Finance & Accounting | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ecommerce Finance | Finance & Accounting | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Factoring Operations Lead | Finance & Accounting | 1 | 0 | 4 | 0 | 1 | 0 | 1 | 0 |
| Finance Capex | Finance & Accounting | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Finance Partner | Finance & Accounting | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Finance — Cost Accountant | Finance & Accounting | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Finance — Payment Settlement Specialist | Finance & Accounting | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Finance — Treasury | Finance & Accounting | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Finance-Treasury | Finance & Accounting | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Fleet Accountant | Finance & Accounting | 1 | 1 | 0 | 2 | 1 | 0 | 0 | 1 |
| Fraud Prevention Specialist | Finance & Accounting | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Hr Finance | Finance & Accounting | 1 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| Hr Finance Analyst | Finance & Accounting | 1 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Insurance & Risk Manager | Finance & Accounting | 1 | 1 | 8 | 1 | 1 | 0 | 1 | 0 |
| Insurance Claim Specialist | Finance & Accounting | 1 | 0 | 3 | 4 | 1 | 0 | 1 | 0 |
| Inventory Finance | Finance & Accounting | 1 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Lease Administration Manager | Finance & Accounting | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Opex Finance Partner | Finance & Accounting | 1 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| Project Billing Clerk | Finance & Accounting | 1 | 0 | 4 | 4 | 1 | 0 | 1 | 0 |
| Project Billing Specialist | Finance & Accounting | 1 | 0 | 4 | 4 | 1 | 1 | 0 | 0 |
| Project Controller | Finance & Accounting | 1 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Property Ar Manager | Finance & Accounting | 1 | 0 | 0 | 2 | 1 | 0 | 1 | 0 |
| Property Tax Manager | Finance & Accounting | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Real Estate & Operations Controller | Finance & Accounting | 1 | 0 | 4 | 4 | 1 | 0 | 1 | 0 |
| Rental Billing Lead | Finance & Accounting | 1 | 0 | 2 | 4 | 1 | 1 | 0 | 0 |
| Reporting | Finance & Accounting | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Revenue | Finance & Accounting | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Risk Transfer | Finance & Accounting | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Valuation Manager | Finance & Accounting | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Finance Mgr | Finance & Accounting | 0 | 11 | 2 | 18 | 28 | 8 | 17 | 3 |
| Cost Accounting | Finance & Accounting | 0 | 1 | 70 | 0 | 25 | 4 | 19 | 2 |
| Vp Ir | Finance & Accounting | 0 | 1 | 65 | 29 | 24 | 3 | 18 | 3 |
| Fraud Management Lead | Finance & Accounting | 0 | 1 | 0 | 64 | 23 | 15 | 8 | 0 |
| Cit Operations | Finance & Accounting | 0 | 10 | 12 | 0 | 12 | 2 | 5 | 5 |
| Credit | Finance & Accounting | 0 | 9 | 9 | 0 | 11 | 2 | 9 | 0 |
| Opex Coe | Finance & Accounting | 0 | 8 | 8 | 0 | 10 | 0 | 7 | 3 |
| Capex | Finance & Accounting | 0 | 9 | 4 | 0 | 9 | 0 | 7 | 2 |
| Lease Operations Mgr | Finance & Accounting | 0 | 9 | 11 | 0 | 9 | 3 | 6 | 0 |
| Finance Desk Lead | Finance & Accounting | 0 | 0 | 0 | 13 | 8 | 1 | 7 | 0 |
| Lease Origination Mgr | Finance & Accounting | 0 | 6 | 9 | 0 | 7 | 0 | 7 | 0 |
| R2R | Finance & Accounting | 0 | 7 | 0 | 0 | 7 | 1 | 6 | 0 |
| Claims Mgr | Finance & Accounting | 0 | 6 | 6 | 0 | 6 | 1 | 3 | 2 |
| External Tax Counsel | Finance & Accounting | 0 | 6 | 2 | 1 | 6 | 6 | 0 | 0 |
| Insurance Provider | Finance & Accounting | 0 | 6 | 1 | 0 | 6 | 2 | 3 | 1 |
| Collections | Finance & Accounting | 0 | 5 | 3 | 0 | 5 | 2 | 3 | 0 |
| Lease Portfolio Mgr | Finance & Accounting | 0 | 5 | 6 | 0 | 5 | 0 | 2 | 3 |
| Leasing Mgr | Finance & Accounting | 0 | 5 | 12 | 0 | 5 | 0 | 5 | 0 |
| O2C Manager | Finance & Accounting | 0 | 0 | 0 | 10 | 5 | 2 | 3 | 0 |
| Ap Analyst | Finance & Accounting | 0 | 4 | 3 | 0 | 4 | 3 | 1 | 0 |
| Billing | Finance & Accounting | 0 | 3 | 5 | 0 | 4 | 2 | 2 | 0 |
| Cit Ops Mgr | Finance & Accounting | 0 | 4 | 0 | 0 | 4 | 2 | 1 | 1 |
| Financial Analyst | Finance & Accounting | 0 | 3 | 8 | 1 | 4 | 1 | 2 | 1 |
| Insurance Claims Coordinator | Finance & Accounting | 0 | 4 | 3 | 0 | 4 | 3 | 1 | 0 |
| Ir | Finance & Accounting | 0 | 3 | 3 | 0 | 4 | 2 | 2 | 0 |
| Senior Accountant | Finance & Accounting | 0 | 4 | 9 | 1 | 4 | 4 | 0 | 0 |
| Close | Finance & Accounting | 0 | 3 | 0 | 0 | 3 | 1 | 2 | 0 |
| Cooperative Finance Officer | Finance & Accounting | 0 | 3 | 0 | 0 | 3 | 1 | 2 | 0 |
| Developer Finance Director | Finance & Accounting | 0 | 3 | 0 | 0 | 3 | 1 | 2 | 0 |
| Finance Clerk | Finance & Accounting | 0 | 2 | 3 | 0 | 3 | 0 | 3 | 0 |
| Finance Department | Finance & Accounting | 0 | 2 | 5 | 1 | 3 | 2 | 0 | 1 |
| Finance Team | Finance & Accounting | 0 | 2 | 3 | 0 | 3 | 1 | 1 | 1 |
| Fpa | Finance & Accounting | 0 | 3 | 0 | 0 | 3 | 2 | 1 | 0 |
| Fx | Finance & Accounting | 0 | 3 | 0 | 0 | 3 | 2 | 1 | 0 |
| Lease Credit Mgr | Finance & Accounting | 0 | 3 | 3 | 0 | 3 | 0 | 3 | 0 |
| M&A | Finance & Accounting | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Project Finance | Finance & Accounting | 0 | 3 | 3 | 0 | 3 | 1 | 2 | 0 |
| Risk & Insurance Mgr | Finance & Accounting | 0 | 2 | 7 | 0 | 3 | 0 | 3 | 0 |
| Tax Lead | Finance & Accounting | 0 | 0 | 0 | 6 | 3 | 2 | 1 | 0 |
| Treasury Lead | Finance & Accounting | 0 | 1 | 7 | 0 | 3 | 0 | 2 | 1 |
| Vp Tax | Finance & Accounting | 0 | 0 | 0 | 5 | 3 | 1 | 2 | 0 |
| Abl | Finance & Accounting | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| Accounting | Finance & Accounting | 0 | 1 | 2 | 0 | 2 | 0 | 2 | 0 |
| Ap Team | Finance & Accounting | 0 | 0 | 2 | 0 | 2 | 1 | 1 | 0 |
| Asset Accountant | Finance & Accounting | 0 | 1 | 3 | 0 | 2 | 0 | 1 | 1 |
| Capex Accounting | Finance & Accounting | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Captive Board Uw Committee | Finance & Accounting | 0 | 0 | 1 | 1 | 2 | 0 | 2 | 0 |
| Collateral | Finance & Accounting | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| Collection Agency | Finance & Accounting | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Collection Officer | Finance & Accounting | 0 | 2 | 3 | 0 | 2 | 2 | 0 | 0 |
| Collections Mgr | Finance & Accounting | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Consolidation Mgr | Finance & Accounting | 0 | 0 | 4 | 1 | 2 | 0 | 2 | 0 |
| Cost Center Managers | Finance & Accounting | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Credit Control Clerk | Finance & Accounting | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| External Insurance Broker | Finance & Accounting | 0 | 2 | 1 | 0 | 2 | 1 | 0 | 1 |
| Finance Specialist | Finance & Accounting | 0 | 1 | 3 | 0 | 2 | 0 | 2 | 0 |
| Fixed Asset | Finance & Accounting | 0 | 2 | 3 | 0 | 2 | 0 | 2 | 0 |
| Insurance Manager | Finance & Accounting | 0 | 0 | 0 | 2 | 2 | 0 | 2 | 0 |
| Lease Accounting Specialist | Finance & Accounting | 0 | 2 | 4 | 0 | 2 | 1 | 1 | 0 |
| Leasing Product Mgr | Finance & Accounting | 0 | 2 | 3 | 0 | 2 | 0 | 1 | 1 |
| Order-To-Cash | Finance & Accounting | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Partner Bank Loan Officer | Finance & Accounting | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| Project Accounting | Finance & Accounting | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Tax Counsel | Finance & Accounting | 0 | 0 | 2 | 0 | 2 | 2 | 0 | 0 |
| Tax Tech Lead | Finance & Accounting | 0 | 2 | 3 | 0 | 2 | 2 | 0 | 0 |
| Treasury Operations | Finance & Accounting | 0 | 2 | 0 | 0 | 2 | 1 | 0 | 1 |
| Valuation Mgr | Finance & Accounting | 0 | 1 | 3 | 0 | 2 | 0 | 1 | 1 |
| Vault Ops | Finance & Accounting | 0 | 2 | 3 | 0 | 2 | 2 | 0 | 0 |
| Vs-26 Insurance | Finance & Accounting | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| 3Rd Party Finance Provider | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Accredited Credit Counselors | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ap Finance | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ap-Ar | Finance & Accounting | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Ar Settlement | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ar Team | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| B2B Credit Analyst | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Bank Reconciliation | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Bank Trade Finance Officer | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Banking Partners | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Billing Clerk | Finance & Accounting | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Bir-Accredited Tax Counsel | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Board Finance | Finance & Accounting | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Board Finance Committee | Finance & Accounting | 0 | 1 | 0 | 2 | 1 | 0 | 1 | 0 |
| Budget Analyst | Finance & Accounting | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Budget Owners | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Capex Analyst | Finance & Accounting | 0 | 0 | 2 | 0 | 1 | 1 | 0 | 0 |
| Captive | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Captive Board Chair | Finance & Accounting | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Captive Manager | Finance & Accounting | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Cash | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Cash Council Members | Finance & Accounting | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Client Finance Officer | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Collection Agents | Finance & Accounting | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Collection Team | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Corporate Accounting | Finance & Accounting | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Cost Center Owner | Finance & Accounting | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| Costing | Finance & Accounting | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Credit Bureau | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Credit Insurance Provider | Finance & Accounting | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Credit Insurance Underwriter | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Credit Insurer | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Debt-Holder Relations | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Developer Finance Team | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| E-Commerce Finance Analyst | Finance & Accounting | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| Ecom Finance | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Entity Finance | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Entity Finance Lead | Finance & Accounting | 0 | 0 | 2 | 0 | 1 | 1 | 0 | 0 |
| Entity Finance Leads | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Entity Tax Specialist | Finance & Accounting | 0 | 0 | 5 | 0 | 1 | 1 | 0 | 0 |
| Entity Tax Specialists | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Epr Credit Sellers | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Ar Development Partner | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| External Ar Partner | Finance & Accounting | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| External Credit Agency | Finance & Accounting | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 |
| External Financial | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Tax Auditor | Finance & Accounting | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Fa Accountant | Finance & Accounting | 0 | 0 | 4 | 1 | 1 | 0 | 1 | 0 |
| Finance Ar | Finance & Accounting | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| Finance Lead | Finance & Accounting | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Finance Managers | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Finance Supervisor | Finance & Accounting | 0 | 1 | 1 | 3 | 1 | 1 | 0 | 0 |
| Finance) | Finance & Accounting | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Financial | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Financial Reporting | Finance & Accounting | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Financing Institution | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Financing Partner → Treasury | Finance & Accounting | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Financing Partners | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Financing Rep | Finance & Accounting | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Financing Representative | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Fixed-Asset Accountant | Finance & Accounting | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Ic Accountant | Finance & Accounting | 0 | 0 | 4 | 0 | 1 | 1 | 0 | 0 |
| Insurance Claims Processor | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Insurance Companies | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Insurance Company Representative | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Insurance Officer | Finance & Accounting | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Insurance Partner | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Insurance Underwriter Broker | Finance & Accounting | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Interentity | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Ir If Material | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Lease Manager | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Lgu Treasury | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Merchandise Finance | Finance & Accounting | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Opex Benefit | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Opex Lead | Finance & Accounting | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 |
| Payment Settlement | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Payment Settlement Specialist | Finance & Accounting | 0 | 0 | 7 | 0 | 1 | 1 | 0 | 0 |
| Petty Cash Custodian | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Property Ar Mgr | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Property Tax Mgr | Finance & Accounting | 0 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Risk & Insurance Lead | Finance & Accounting | 0 | 0 | 0 | 3 | 1 | 1 | 0 | 0 |
| Segment Finance Leads | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Tax Admin | Finance & Accounting | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Tax Compliance Associate | Finance & Accounting | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| Tax Dd Advisors | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Tax Management | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Tax Specialists | Finance & Accounting | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Tp Mgr | Finance & Accounting | 0 | 0 | 3 | 0 | 1 | 1 | 0 | 0 |
| Trade Finance | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Treasury & Insurance | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Treasury Clerk | Finance & Accounting | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Valuation | Finance & Accounting | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Merchandising | Merchandising & Buying | 38 | 274 | 174 | 1 | 310 | 43 | 208 | 59 |
| Pricing | Merchandising & Buying | 15 | 61 | 82 | 0 | 75 | 9 | 52 | 14 |
| Store Design | Merchandising & Buying | 4 | 6 | 13 | 0 | 8 | 0 | 7 | 1 |
| Visual Merch | Merchandising & Buying | 3 | 4 | 8 | 0 | 6 | 1 | 5 | 0 |
| Merchandising Manager | Merchandising & Buying | 2 | 9 | 5 | 4 | 13 | 4 | 9 | 0 |
| Visual Merchandiser | Merchandising & Buying | 2 | 8 | 11 | 0 | 9 | 0 | 7 | 2 |
| Store Design Manager | Merchandising & Buying | 2 | 0 | 2 | 1 | 3 | 0 | 2 | 1 |
| Merchandising-Pricing | Merchandising & Buying | 2 | 0 | 0 | 0 | 2 | 1 | 1 | 0 |
| Master Data Analyst | Merchandising & Buying | 1 | 35 | 71 | 0 | 36 | 9 | 27 | 0 |
| Buyers | Merchandising & Buying | 1 | 28 | 19 | 0 | 31 | 4 | 22 | 5 |
| Category | Merchandising & Buying | 1 | 24 | 11 | 0 | 26 | 2 | 19 | 5 |
| Merchandising Team | Merchandising & Buying | 1 | 4 | 3 | 0 | 5 | 1 | 2 | 2 |
| Visual Merchandising Associate | Merchandising & Buying | 1 | 3 | 1 | 0 | 3 | 1 | 2 | 0 |
| Merchandising Analytics Manager | Merchandising & Buying | 1 | 0 | 0 | 3 | 2 | 0 | 0 | 2 |
| Rental Pricing Analyst | Merchandising & Buying | 1 | 0 | 6 | 0 | 2 | 0 | 1 | 1 |
| Visual Merchandising | Merchandising & Buying | 1 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Category Management | Merchandising & Buying | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Concept Manager | Merchandising & Buying | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Markdown | Merchandising & Buying | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Merch Analytics | Merchandising & Buying | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Merchandise Admin | Merchandising & Buying | 1 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| Merchandising Onboarding | Merchandising & Buying | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Merchandising Operations | Merchandising & Buying | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sample Mgmt | Merchandising & Buying | 1 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Store Design Lead | Merchandising & Buying | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Head Of Merch | Merchandising & Buying | 0 | 0 | 0 | 21 | 12 | 0 | 10 | 2 |
| Merch Coordinator | Merchandising & Buying | 0 | 7 | 14 | 2 | 12 | 1 | 11 | 0 |
| Commodity | Merchandising & Buying | 0 | 9 | 2 | 0 | 9 | 2 | 6 | 1 |
| Merch | Merchandising & Buying | 0 | 1 | 6 | 0 | 6 | 0 | 5 | 1 |
| Merch Coord | Merchandising & Buying | 0 | 5 | 1 | 0 | 5 | 0 | 5 | 0 |
| Planning | Merchandising & Buying | 0 | 0 | 4 | 0 | 4 | 2 | 1 | 1 |
| Vp Visual Merch | Merchandising & Buying | 0 | 0 | 0 | 4 | 4 | 1 | 3 | 0 |
| Merchandising Analyst | Merchandising & Buying | 0 | 3 | 5 | 0 | 3 | 0 | 1 | 2 |
| Merchandising Planning | Merchandising & Buying | 0 | 3 | 3 | 0 | 3 | 0 | 3 | 0 |
| Planogram | Merchandising & Buying | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Rebate | Merchandising & Buying | 0 | 3 | 2 | 0 | 3 | 0 | 2 | 1 |
| Transfer Pricing Advisor | Merchandising & Buying | 0 | 1 | 2 | 0 | 3 | 1 | 2 | 0 |
| Catalog Manager | Merchandising & Buying | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| Catalog Mgr | Merchandising & Buying | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Category Mgmt | Merchandising & Buying | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Category Specialist | Merchandising & Buying | 0 | 2 | 2 | 1 | 2 | 1 | 0 | 1 |
| Cooperative Sourcing | Merchandising & Buying | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| External Transfer Pricing Advisor | Merchandising & Buying | 0 | 2 | 1 | 0 | 2 | 2 | 0 | 0 |
| Marketing Promotions Mgr | Merchandising & Buying | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Master Data Team | Merchandising & Buying | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Merch Ops | Merchandising & Buying | 0 | 1 | 3 | 0 | 2 | 0 | 2 | 0 |
| Merch Planners | Merchandising & Buying | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Merchandising Ops & Master Data | Merchandising & Buying | 0 | 1 | 1 | 0 | 2 | 2 | 0 | 0 |
| Planner | Merchandising & Buying | 0 | 0 | 2 | 0 | 2 | 0 | 1 | 1 |
| Pricing Director | Merchandising & Buying | 0 | 0 | 0 | 2 | 2 | 0 | 2 | 0 |
| Product Info | Merchandising & Buying | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Services Category Mgr | Merchandising & Buying | 0 | 0 | 11 | 2 | 2 | 0 | 0 | 2 |
| Sourcing Manager | Merchandising & Buying | 0 | 2 | 2 | 0 | 2 | 1 | 0 | 1 |
| Space Planning Analyst | Merchandising & Buying | 0 | 2 | 3 | 0 | 2 | 0 | 2 | 0 |
| Affected Category Manager | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Brands | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Category Buyers | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Category Director | Merchandising & Buying | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Consignment | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Forecast | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Head Of Merch Ops | Merchandising & Buying | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Master Data Analysts | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Master Data Lead | Merchandising & Buying | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Merch Mgr | Merchandising & Buying | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| Merchandising Admin | Merchandising & Buying | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Merchandising Category Managers | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Merchandising Mgr | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Merchandising Operations & Master Data | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Merchandising Pricing | Merchandising & Buying | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Merchandising Pricing Team | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Planogram Analyst | Merchandising & Buying | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Pricing Specialist | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Private Brand Team | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Private-Label | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Product Developers | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Promotion | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| R&D | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Responsible Sourcing | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Scorecard | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Should-Cost | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sourcing Spec | Merchandising & Buying | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Space | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Space Planning | Merchandising & Buying | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Store Manager Or Category Manager | Merchandising & Buying | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Transfer Pricing | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Transfer Pricing Mgr | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Used-Equipment Buyer | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vendor Master Data | Merchandising & Buying | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Vendor Master Data Steward | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vs-67 Vendor Scorecard | Merchandising & Buying | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Procurement | Supply Chain & Logistics | 63 | 319 | 391 | 6 | 383 | 54 | 270 | 59 |
| Logistics | Supply Chain & Logistics | 44 | 159 | 184 | 1 | 173 | 48 | 107 | 18 |
| Ev Program Manager | Supply Chain & Logistics | 21 | 0 | 6 | 45 | 23 | 3 | 17 | 3 |
| Transport Lead | Supply Chain & Logistics | 20 | 1 | 32 | 15 | 24 | 2 | 19 | 3 |
| Supply Planning | Supply Chain & Logistics | 14 | 82 | 86 | 0 | 94 | 15 | 58 | 21 |
| Procurement Specialist | Supply Chain & Logistics | 14 | 24 | 42 | 27 | 33 | 6 | 26 | 1 |
| S&Op | Supply Chain & Logistics | 13 | 5 | 41 | 0 | 25 | 9 | 14 | 2 |
| Supply Planning Manager | Supply Chain & Logistics | 12 | 21 | 45 | 49 | 42 | 19 | 17 | 6 |
| Fleet | Supply Chain & Logistics | 11 | 36 | 46 | 0 | 50 | 11 | 34 | 5 |
| Fleet Manager | Supply Chain & Logistics | 10 | 19 | 46 | 34 | 29 | 10 | 11 | 8 |
| Procurement Director | Supply Chain & Logistics | 10 | 16 | 5 | 38 | 24 | 3 | 20 | 1 |
| Packaging Engineering | Supply Chain & Logistics | 10 | 0 | 0 | 0 | 10 | 0 | 5 | 5 |
| Inventory | Supply Chain & Logistics | 9 | 50 | 50 | 0 | 54 | 19 | 33 | 2 |
| Supply Planner | Supply Chain & Logistics | 9 | 37 | 65 | 9 | 49 | 20 | 25 | 4 |
| Demand Planning | Supply Chain & Logistics | 9 | 16 | 25 | 0 | 18 | 6 | 9 | 3 |
| Scm | Supply Chain & Logistics | 9 | 14 | 25 | 0 | 14 | 2 | 8 | 4 |
| Fleet Supervisor | Supply Chain & Logistics | 8 | 3 | 16 | 8 | 11 | 1 | 9 | 1 |
| Vendor Mgmt | Supply Chain & Logistics | 7 | 63 | 75 | 0 | 77 | 25 | 46 | 6 |
| Vendor Management | Supply Chain & Logistics | 7 | 5 | 0 | 0 | 11 | 4 | 7 | 0 |
| Dc Ops | Supply Chain & Logistics | 6 | 101 | 59 | 0 | 114 | 19 | 83 | 12 |
| Dc Operations | Supply Chain & Logistics | 6 | 45 | 13 | 3 | 49 | 19 | 28 | 2 |
| Supply | Supply Chain & Logistics | 5 | 23 | 24 | 0 | 34 | 7 | 22 | 5 |
| Import | Supply Chain & Logistics | 5 | 30 | 16 | 0 | 31 | 16 | 13 | 2 |
| Logistics Planner | Supply Chain & Logistics | 5 | 11 | 18 | 4 | 14 | 6 | 6 | 2 |
| Supply Chain Planning Manager | Supply Chain & Logistics | 5 | 0 | 0 | 10 | 8 | 1 | 6 | 1 |
| Bulky-Delivery Operations | Supply Chain & Logistics | 5 | 0 | 0 | 0 | 5 | 2 | 1 | 2 |
| Bulky-Delivery Service Ops | Supply Chain & Logistics | 5 | 0 | 0 | 0 | 5 | 1 | 4 | 0 |
| Last-Mile | Supply Chain & Logistics | 4 | 11 | 10 | 0 | 14 | 4 | 8 | 2 |
| Logistics Analyst | Supply Chain & Logistics | 4 | 4 | 10 | 0 | 6 | 0 | 2 | 4 |
| Packaging Engineer | Supply Chain & Logistics | 4 | 0 | 0 | 0 | 4 | 0 | 4 | 0 |
| Bulky-Delivery Reverse Logistics | Supply Chain & Logistics | 3 | 0 | 0 | 0 | 3 | 1 | 2 | 0 |
| Fleet Maintenance Manager | Supply Chain & Logistics | 3 | 0 | 0 | 15 | 3 | 0 | 3 | 0 |
| Last-Mile Ops | Supply Chain & Logistics | 3 | 0 | 0 | 4 | 3 | 1 | 2 | 0 |
| Transportation | Supply Chain & Logistics | 3 | 0 | 1 | 0 | 3 | 1 | 2 | 0 |
| Ev Program | Supply Chain & Logistics | 2 | 0 | 38 | 0 | 19 | 4 | 13 | 2 |
| Freight | Supply Chain & Logistics | 2 | 15 | 13 | 0 | 15 | 7 | 7 | 1 |
| Supply Planning Analyst | Supply Chain & Logistics | 2 | 7 | 20 | 0 | 8 | 2 | 5 | 1 |
| Bulky-Delivery Ops | Supply Chain & Logistics | 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 |
| Fleet Planning | Supply Chain & Logistics | 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 |
| Last-Mile Operations Supervisor | Supply Chain & Logistics | 2 | 1 | 0 | 0 | 2 | 1 | 1 | 0 |
| Logistics Supervisor | Supply Chain & Logistics | 2 | 1 | 3 | 4 | 2 | 0 | 2 | 0 |
| Transport Dispatcher | Supply Chain & Logistics | 2 | 0 | 0 | 0 | 2 | 1 | 1 | 0 |
| Supply Chain | Supply Chain & Logistics | 1 | 27 | 14 | 0 | 31 | 3 | 21 | 7 |
| Returns Manager | Supply Chain & Logistics | 1 | 0 | 1 | 3 | 4 | 1 | 3 | 0 |
| Supply Chain Analyst | Supply Chain & Logistics | 1 | 1 | 2 | 0 | 4 | 1 | 1 | 2 |
| Freight Coordinator | Supply Chain & Logistics | 1 | 2 | 4 | 4 | 3 | 1 | 2 | 0 |
| Clearance | Supply Chain & Logistics | 1 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Fleet Logistics | Supply Chain & Logistics | 1 | 1 | 0 | 0 | 2 | 0 | 2 | 0 |
| Inventory Lifecycle | Supply Chain & Logistics | 1 | 2 | 0 | 0 | 2 | 0 | 0 | 2 |
| Logistics Fleet Supervisor | Supply Chain & Logistics | 1 | 1 | 3 | 4 | 2 | 0 | 2 | 0 |
| Bulky-Delivery Dispatch | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Bulky-Delivery Fleet | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Bulky-Delivery Network Planning | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Bulky-Delivery Partner Mgmt | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Bulky-Delivery Scheduling | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Control Tower | Supply Chain & Logistics | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Dc Dispatch Planner | Supply Chain & Logistics | 1 | 1 | 6 | 0 | 1 | 1 | 0 | 0 |
| Dc Inbound | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Delivery Dispatch Coordinator | Supply Chain & Logistics | 1 | 1 | 5 | 1 | 1 | 0 | 1 | 0 |
| Demand & Supply Planning | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Director Of Supply Chain Planning | Supply Chain & Logistics | 1 | 0 | 4 | 4 | 1 | 0 | 1 | 0 |
| Ev Charging Network Program Manager | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Fleet & Asset | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Fleet Analytics & Continuous Improvement Lead | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Fleet Charging Operations Supervisor | Supply Chain & Logistics | 1 | 0 | 0 | 5 | 1 | 0 | 1 | 0 |
| Fleet Driver Mgmt | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Fleet Procurement Lead | Supply Chain & Logistics | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Fleet Telematics | Supply Chain & Logistics | 1 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| Fleet Training & Enablement Lead | Supply Chain & Logistics | 1 | 0 | 0 | 5 | 1 | 0 | 1 | 0 |
| Freight Procurement & Carrier Manager | Supply Chain & Logistics | 1 | 0 | 0 | 5 | 1 | 0 | 0 | 1 |
| Hauling Safety Manager | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Head Of Bulky | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Home Delivery | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Import Compliance | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Import Specialist | Supply Chain & Logistics | 1 | 1 | 4 | 0 | 1 | 1 | 0 | 0 |
| Last-Mile Dispatch | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Last-Mile Dispatch Coordinator | Supply Chain & Logistics | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Last-Mile Logistics | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Logistics Analytics | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Logistics Capacity | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Logistics Control Tower Lead | Supply Chain & Logistics | 1 | 0 | 4 | 4 | 1 | 0 | 0 | 1 |
| Logistics Emergency Response | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Logistics Fleet | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Network & Transportation Planning Lead | Supply Chain & Logistics | 1 | 0 | 0 | 5 | 1 | 0 | 1 | 0 |
| Order Fulfillment | Supply Chain & Logistics | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Packaging | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Procurement Strategy | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Procurement — Supplier Risk Manager | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Reverse | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Site Transport Coordinator | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Supply Chain Strategy | Supply Chain & Logistics | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Supply Risk | Supply Chain & Logistics | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vmi Coordinator | Supply Chain & Logistics | 1 | 1 | 5 | 0 | 1 | 0 | 1 | 0 |
| Customs | Supply Chain & Logistics | 0 | 25 | 8 | 0 | 26 | 10 | 13 | 3 |
| Packaging Eng | Supply Chain & Logistics | 0 | 19 | 42 | 0 | 19 | 2 | 11 | 6 |
| Supply Chain Manager | Supply Chain & Logistics | 0 | 3 | 4 | 31 | 15 | 5 | 10 | 0 |
| Logistics Mgr | Supply Chain & Logistics | 0 | 2 | 4 | 11 | 13 | 4 | 7 | 2 |
| Cpo | Supply Chain & Logistics | 0 | 9 | 4 | 1 | 12 | 3 | 9 | 0 |
| Dc Team | Supply Chain & Logistics | 0 | 2 | 13 | 0 | 12 | 4 | 6 | 2 |
| Dc Receiving Clerk | Supply Chain & Logistics | 0 | 4 | 11 | 0 | 10 | 8 | 1 | 1 |
| Head Of Bulky Delivery | Supply Chain & Logistics | 0 | 0 | 2 | 18 | 10 | 1 | 7 | 2 |
| Mechanic | Supply Chain & Logistics | 0 | 5 | 14 | 0 | 10 | 4 | 5 | 1 |
| Transport | Supply Chain & Logistics | 0 | 1 | 10 | 0 | 9 | 1 | 6 | 2 |
| Warehouse Supervisor | Supply Chain & Logistics | 0 | 7 | 9 | 1 | 9 | 4 | 5 | 0 |
| Delivery Coordinator | Supply Chain & Logistics | 0 | 6 | 14 | 3 | 8 | 1 | 6 | 1 |
| Dispatcher | Supply Chain & Logistics | 0 | 1 | 12 | 0 | 8 | 3 | 4 | 1 |
| Dc Receiving | Supply Chain & Logistics | 0 | 7 | 4 | 0 | 7 | 3 | 4 | 0 |
| Dc Staff | Supply Chain & Logistics | 0 | 1 | 7 | 0 | 7 | 1 | 4 | 2 |
| Dispatch | Supply Chain & Logistics | 0 | 5 | 4 | 0 | 7 | 1 | 4 | 2 |
| Scm Manager | Supply Chain & Logistics | 0 | 0 | 0 | 18 | 7 | 1 | 6 | 0 |
| 3Pl Partner | Supply Chain & Logistics | 0 | 4 | 2 | 0 | 6 | 2 | 4 | 0 |
| 3Pl Partners | Supply Chain & Logistics | 0 | 6 | 0 | 0 | 6 | 1 | 2 | 3 |
| Allocation | Supply Chain & Logistics | 0 | 6 | 3 | 0 | 6 | 1 | 4 | 1 |
| Dc Shift Supervisor | Supply Chain & Logistics | 0 | 3 | 15 | 0 | 6 | 5 | 0 | 1 |
| Delivery Ops | Supply Chain & Logistics | 0 | 0 | 12 | 0 | 6 | 1 | 3 | 2 |
| Network Planning | Supply Chain & Logistics | 0 | 4 | 5 | 0 | 6 | 2 | 3 | 1 |
| Supply Planning Mgr | Supply Chain & Logistics | 0 | 2 | 2 | 4 | 6 | 3 | 2 | 1 |
| Receiving | Supply Chain & Logistics | 0 | 4 | 2 | 0 | 5 | 2 | 3 | 0 |
| Reverse Logistics | Supply Chain & Logistics | 0 | 5 | 7 | 0 | 5 | 1 | 3 | 1 |
| Yard Staff | Supply Chain & Logistics | 0 | 2 | 6 | 0 | 5 | 2 | 2 | 1 |
| Dc Dispatcher | Supply Chain & Logistics | 0 | 4 | 4 | 1 | 4 | 1 | 3 | 0 |
| Dc Leadership | Supply Chain & Logistics | 0 | 4 | 0 | 0 | 4 | 0 | 3 | 1 |
| Dc Shift Supervisors | Supply Chain & Logistics | 0 | 4 | 0 | 0 | 4 | 1 | 1 | 2 |
| Fleet Ops | Supply Chain & Logistics | 0 | 2 | 5 | 0 | 4 | 0 | 1 | 3 |
| Inventory Mgr | Supply Chain & Logistics | 0 | 3 | 0 | 1 | 4 | 1 | 3 | 0 |
| Warehouse | Supply Chain & Logistics | 0 | 4 | 1 | 0 | 4 | 1 | 0 | 3 |
| 3Pl Account Manager | Supply Chain & Logistics | 0 | 2 | 2 | 0 | 3 | 1 | 2 | 0 |
| Bureau Of Customs | Supply Chain & Logistics | 0 | 3 | 0 | 0 | 3 | 2 | 1 | 0 |
| Dc Logistics | Supply Chain & Logistics | 0 | 1 | 3 | 0 | 3 | 0 | 3 | 0 |
| Dc Pick | Supply Chain & Logistics | 0 | 3 | 1 | 0 | 3 | 2 | 1 | 0 |
| Dc Receiving Team | Supply Chain & Logistics | 0 | 3 | 1 | 0 | 3 | 3 | 0 | 0 |
| Delivery Team | Supply Chain & Logistics | 0 | 0 | 3 | 0 | 3 | 0 | 3 | 0 |
| Fleet Analyst | Supply Chain & Logistics | 0 | 0 | 7 | 0 | 3 | 0 | 0 | 3 |
| Imports | Supply Chain & Logistics | 0 | 3 | 3 | 0 | 3 | 1 | 2 | 0 |
| Inventory Planning | Supply Chain & Logistics | 0 | 3 | 0 | 0 | 3 | 1 | 2 | 0 |
| Last-Mile Supervisor | Supply Chain & Logistics | 0 | 1 | 3 | 10 | 3 | 2 | 1 | 0 |
| Receiving Store Manager | Supply Chain & Logistics | 0 | 3 | 2 | 0 | 3 | 1 | 2 | 0 |
| Store Receiving | Supply Chain & Logistics | 0 | 3 | 0 | 0 | 3 | 1 | 2 | 0 |
| Transportation Planner | Supply Chain & Logistics | 0 | 3 | 5 | 1 | 3 | 2 | 0 | 1 |
| 3Pl Transport Coordinator | Supply Chain & Logistics | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Cutter | Supply Chain & Logistics | 0 | 1 | 6 | 0 | 2 | 0 | 1 | 1 |
| Dc Assembly Staff | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 2 | 1 | 1 | 0 |
| Dc Clerk | Supply Chain & Logistics | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| Dc Receiving Lead | Supply Chain & Logistics | 0 | 2 | 5 | 0 | 2 | 2 | 0 | 0 |
| Dc Warehouse Crew | Supply Chain & Logistics | 0 | 0 | 2 | 0 | 2 | 1 | 1 | 0 |
| Delivery | Supply Chain & Logistics | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Delivery Leads | Supply Chain & Logistics | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Drayage Carrier Dispatcher | Supply Chain & Logistics | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Ecommerce Fulfillment Team | Supply Chain & Logistics | 0 | 2 | 2 | 0 | 2 | 0 | 0 | 2 |
| Fleet Drivers | Supply Chain & Logistics | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Fleet Maintenance | Supply Chain & Logistics | 0 | 0 | 6 | 0 | 2 | 0 | 2 | 0 |
| Fulfillment Analyst | Supply Chain & Logistics | 0 | 2 | 5 | 0 | 2 | 2 | 0 | 0 |
| Fulfillment Team | Supply Chain & Logistics | 0 | 2 | 1 | 0 | 2 | 0 | 1 | 1 |
| Hauling 3Pl | Supply Chain & Logistics | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Logistics Team | Supply Chain & Logistics | 0 | 2 | 2 | 0 | 2 | 0 | 1 | 1 |
| Mechanics | Supply Chain & Logistics | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Packaging Designer | Supply Chain & Logistics | 0 | 2 | 3 | 0 | 2 | 0 | 2 | 0 |
| Parts | Supply Chain & Logistics | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Parts Coordinator | Supply Chain & Logistics | 0 | 2 | 3 | 0 | 2 | 0 | 2 | 0 |
| Purchasing | Supply Chain & Logistics | 0 | 2 | 5 | 0 | 2 | 0 | 2 | 0 |
| Receiving Staff | Supply Chain & Logistics | 0 | 0 | 2 | 0 | 2 | 2 | 0 | 0 |
| Replenishment | Supply Chain & Logistics | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Returns Lead | Supply Chain & Logistics | 0 | 0 | 0 | 4 | 2 | 0 | 2 | 0 |
| Supply Chain Planners | Supply Chain & Logistics | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Supply Chain Planning | Supply Chain & Logistics | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| Supply Chain Planning Team | Supply Chain & Logistics | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Yard Coordinator | Supply Chain & Logistics | 0 | 2 | 1 | 1 | 2 | 1 | 0 | 1 |
| 3Pl Air Freight Broker | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| 3Pl Carrier Coordinator | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| 3Pl Carrier Dispatcher | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| 3Pl Courier | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| 3Pl Couriers | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| 3Pl Delivery Partner | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| 3Pl Depot | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| 3Pl Dispatch | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| 3Pl Dispatch Coordinator | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| 3Pl Drivers | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| 3Pl Dump Truck Partner | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| 3Pl Express Courier | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| 3Pl Heavy Equipment Partner | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| 3Pl Logistics Partner | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| 3Pl Partner Account Manager | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| 3Pl Partner Account Managers | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| 3Pl Partner Driver | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| 3Pl Partner Manager | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| 3Pl Provider | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| 3Pl Rider | Supply Chain & Logistics | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| 3Pl Truck Driver | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Carrier Fleet Manager | Supply Chain & Logistics | 0 | 1 | 4 | 0 | 1 | 1 | 0 | 0 |
| Contractor Jobsite Delivery | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Cross-Dock Coord | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Cross-Dock Sortation Team | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Dark Store Ops | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Dc Controller | Supply Chain & Logistics | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| Dc Dispatch Team | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Dc Driver | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Dc Facility Vendor | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Dc Fulfillment Supervisor | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Dc Fulfillment Team | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Dc Inventory Controller | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Dc Inventory Planner | Supply Chain & Logistics | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Dc Kitting | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Dc Maintenance Supervisors | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Dc Ops Supervisor | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Dc Planner | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Dc Quality Inspectors | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Dc Receiver | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Dc Receiving Clerks | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Dc Receiving Inspector | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Dc Returns Processing | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Dc Returns Team | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Dc Safety Officers | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Dc Security Guard | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Dc Supervisors | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Dc Warehouse | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Delivery Carrier | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Delivery Partner Driver | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Delivery Partners | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Delivery Rider | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Delivery Staff | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Delivery Supervisor | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Delivery-Domain | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Delivery-Domain Leads | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Demand Planning Manager | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Demand Planning Mgr | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Depot | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Dispatch Clerk | Supply Chain & Logistics | 0 | 1 | 3 | 0 | 1 | 1 | 0 | 0 |
| Dispatch Crew | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Dp | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Drayage Carrier | Supply Chain & Logistics | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| Drayage Carrier Driver | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Drayage Driver | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Dswd Warehouse Receiver | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ecom Logistics Coord | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Ecom Logistics Coordinator | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Ecommerce Fulfillment Mgr | Supply Chain & Logistics | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Equipment Technician | Supply Chain & Logistics | 0 | 1 | 3 | 0 | 1 | 0 | 0 | 1 |
| External Logistics Consultant | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Fleet Admin | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Fleet Assistant | Supply Chain & Logistics | 0 | 1 | 4 | 0 | 1 | 1 | 0 | 0 |
| Fleet Charging Ops | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Fleet Dispatch | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Fleet Driver | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Fleet Duty | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Fleet Lead | Supply Chain & Logistics | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Fleet Maintenance Analyst | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Fleet Procurement | Supply Chain & Logistics | 0 | 0 | 4 | 0 | 1 | 0 | 1 | 0 |
| Fleet Safety Manager | Supply Chain & Logistics | 0 | 0 | 3 | 1 | 1 | 1 | 0 | 0 |
| Forklift Op | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Freight Analyst | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Freight Carrier | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Freight Forwarder Partners | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Freight Procurement | Supply Chain & Logistics | 0 | 0 | 4 | 0 | 1 | 0 | 0 | 1 |
| Fuel Manager | Supply Chain & Logistics | 0 | 0 | 4 | 0 | 1 | 0 | 1 | 0 |
| Fulfillment Partner | Supply Chain & Logistics | 0 | 0 | 3 | 0 | 1 | 0 | 0 | 1 |
| Hazmat Contractor | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Hazmat Hauler | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Hazmat Vendor | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Head Of Supply Chain | Supply Chain & Logistics | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Hub Coordinator | Supply Chain & Logistics | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| Import Logistics Coordinator | Supply Chain & Logistics | 0 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Import Manager | Supply Chain & Logistics | 0 | 0 | 5 | 2 | 1 | 1 | 0 | 0 |
| Import Team | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Imports & Customs Coordinator | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Imports Coordinator | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| In-House Broker | Supply Chain & Logistics | 0 | 0 | 3 | 0 | 1 | 1 | 0 | 0 |
| In-House Customs Broker | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Indent | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Inter-Island Freight | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Inventory Clerk | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Inventory Control Clerk | Supply Chain & Logistics | 0 | 1 | 5 | 0 | 1 | 1 | 0 | 0 |
| Inventory Control Mgr | Supply Chain & Logistics | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 |
| Inventory Count Teams | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Inventory Lead | Supply Chain & Logistics | 0 | 0 | 0 | 2 | 1 | 1 | 0 | 0 |
| Licensed Hazmat Vendor | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Loading Supervisor | Supply Chain & Logistics | 0 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Loading Team Lead | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Logistics Operators | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Logistics Route | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Logistics Routing | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Lumber Yard Associate | Supply Chain & Logistics | 0 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Lumber Yard Sales Associate | Supply Chain & Logistics | 0 | 1 | 4 | 0 | 1 | 0 | 1 | 0 |
| Marketplace Logistics | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Network Planning Analyst | Supply Chain & Logistics | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Own Fleet | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Pack | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Packaging Engineers | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Packaging Team | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Parts Clerk | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Parts Specialist | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Pmo For Initiative-Sized Routing | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Pnp Units With Jurisdiction Over The Route | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Procurement Specialists | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Project Delivery | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Reach Stacker Operator | Supply Chain & Logistics | 0 | 1 | 3 | 0 | 1 | 0 | 0 | 1 |
| Receiving Associate | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Receiving Dc Supervisor | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Receiving Department Manager | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Receiving Dept Manager | Supply Chain & Logistics | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Receiving Employee | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Receiving Location Manager | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Receiving Manager | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Receiving Store | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Reseller Receiving Clerk | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Returns Clerk | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Returns Mgr | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Returns Supervisor | Supply Chain & Logistics | 0 | 0 | 1 | 5 | 1 | 1 | 0 | 0 |
| Reverse-Logistics | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Reward Fulfillment Partner | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Route Planners | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| S&Op Planner | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| S&Op Team | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sc | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sc Director | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Scheduling | Supply Chain & Logistics | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Shipping Clerk | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Shipping Coordinator | Supply Chain & Logistics | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| Shipping Dc Supervisor | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Shipping Line Coordinator | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Shipping Line Representative | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Shipping Lines | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Shipping Supervisor | Supply Chain & Logistics | 0 | 1 | 7 | 1 | 1 | 0 | 1 | 0 |
| Stage Clerk | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Staging Lead | Supply Chain & Logistics | 0 | 0 | 3 | 2 | 1 | 1 | 0 | 0 |
| Staging Staff | Supply Chain & Logistics | 0 | 1 | 3 | 0 | 1 | 1 | 0 | 0 |
| Stock Clerk | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Store & Dc Leadership | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Store Fulfillment Associate | Supply Chain & Logistics | 0 | 0 | 2 | 0 | 1 | 1 | 0 | 0 |
| Store Fulfillment Team | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Supply Chain Coordinator | Supply Chain & Logistics | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Third-Party Fleet Manager | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Tiktok Logistics Partner | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Trade Ops | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Transport Coordinator | Supply Chain & Logistics | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Transport Manager | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Transportation Coordinator | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Transportation Manager | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Vendor Logistics | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Vendor Logistics Contact | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vendor Logistics Contacts | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Virtual Receiving Clerk | Supply Chain & Logistics | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 |
| Vs-187 Hazmat | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Vs-187 Hazmat Tsd | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Warehouse Associate | Supply Chain & Logistics | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Warehouse Clerk | Supply Chain & Logistics | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Warehouse Planner | Supply Chain & Logistics | 0 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Warehouse Receiving Lead | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Warehouse Receiving Team | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Warehouse Supervisors | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Wms Dispatch | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Yard Associate | Supply Chain & Logistics | 0 | 1 | 3 | 0 | 1 | 1 | 0 | 0 |
| Yard Dispatch | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Yard Helper | Supply Chain & Logistics | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| It | Information Technology | 66 | 374 | 493 | 5 | 487 | 124 | 317 | 46 |
| Finops Lead | Information Technology | 23 | 0 | 66 | 12 | 23 | 1 | 16 | 6 |
| Auto-Id Lead | Information Technology | 18 | 5 | 36 | 0 | 23 | 7 | 15 | 1 |
| Network Strategy Lead | Information Technology | 16 | 0 | 42 | 0 | 16 | 2 | 6 | 8 |
| It Integration Lead | Information Technology | 9 | 3 | 12 | 5 | 10 | 1 | 8 | 1 |
| It Innovation Lead | Information Technology | 6 | 4 | 21 | 0 | 6 | 2 | 0 | 4 |
| Integration Lead | Information Technology | 5 | 5 | 13 | 0 | 8 | 0 | 7 | 1 |
| It Project Manager | Information Technology | 3 | 2 | 1 | 2 | 5 | 2 | 2 | 1 |
| It System Admin | Information Technology | 3 | 1 | 2 | 2 | 4 | 0 | 3 | 1 |
| It Application Manager | Information Technology | 2 | 3 | 3 | 0 | 5 | 1 | 4 | 0 |
| Cio Office | Information Technology | 2 | 2 | 4 | 0 | 4 | 0 | 3 | 1 |
| It Integration Manager | Information Technology | 2 | 1 | 3 | 0 | 3 | 1 | 2 | 0 |
| Facilities-It | Information Technology | 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 |
| It Change Manager | Information Technology | 2 | 1 | 5 | 3 | 2 | 0 | 2 | 0 |
| It Compliance Lead | Information Technology | 2 | 0 | 11 | 0 | 2 | 0 | 2 | 0 |
| Mobility Lead | Information Technology | 2 | 0 | 5 | 4 | 2 | 0 | 2 | 0 |
| Store Operations It | Information Technology | 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 |
| It Manager | Information Technology | 1 | 11 | 13 | 22 | 22 | 9 | 10 | 3 |
| It Infrastructure Lead | Information Technology | 1 | 6 | 4 | 0 | 9 | 4 | 5 | 0 |
| Application Manager | Information Technology | 1 | 7 | 2 | 0 | 8 | 1 | 6 | 1 |
| Domain Owner | Information Technology | 1 | 0 | 13 | 1 | 8 | 0 | 8 | 0 |
| Pos-It | Information Technology | 1 | 0 | 7 | 0 | 6 | 5 | 1 | 0 |
| Data Office | Information Technology | 1 | 5 | 3 | 0 | 5 | 0 | 5 | 0 |
| It Analyst | Information Technology | 1 | 3 | 9 | 2 | 5 | 2 | 1 | 2 |
| Pos Administrator | Information Technology | 1 | 4 | 5 | 5 | 5 | 5 | 0 | 0 |
| Application Owners | Information Technology | 1 | 4 | 3 | 0 | 4 | 0 | 4 | 0 |
| Solution Architect | Information Technology | 1 | 1 | 7 | 0 | 4 | 0 | 4 | 0 |
| Domain Architects | Information Technology | 1 | 3 | 4 | 0 | 3 | 0 | 3 | 0 |
| Knowledge Mgmt | Information Technology | 1 | 2 | 4 | 0 | 2 | 0 | 2 | 0 |
| Automation Coe | Information Technology | 1 | 1 | 2 | 0 | 1 | 0 | 0 | 1 |
| B2B Portal Administrator | Information Technology | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Cloud Cost Manager | Information Technology | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Data Lead | Information Technology | 1 | 0 | 1 | 3 | 1 | 1 | 0 | 0 |
| Data Manager | Information Technology | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Domain Renewal Owners | Information Technology | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Erp Application Manager | Information Technology | 1 | 1 | 1 | 3 | 1 | 1 | 0 | 0 |
| Financial Systems Administrator | Information Technology | 1 | 0 | 3 | 4 | 1 | 1 | 0 | 0 |
| Head Of Frontend | Information Technology | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Integration Architect | Information Technology | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| It Adoption | Information Technology | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| It Adoption Lead | Information Technology | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| It Field | Information Technology | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| It Finops Analyst | Information Technology | 1 | 0 | 2 | 1 | 1 | 0 | 1 | 0 |
| It Knowledge Coordinator | Information Technology | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| It Portal Administrator | Information Technology | 1 | 1 | 4 | 0 | 1 | 0 | 0 | 1 |
| It Problem Manager | Information Technology | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| It Procurement Manager | Information Technology | 1 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| It Service Delivery Lead | Information Technology | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| It Service Delivery Manager | Information Technology | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| It Service Mgmt | Information Technology | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| It Store Operations Manager | Information Technology | 1 | 0 | 0 | 2 | 1 | 1 | 0 | 0 |
| It Training Lead | Information Technology | 1 | 1 | 4 | 0 | 1 | 0 | 1 | 0 |
| It Training Specialist | Information Technology | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| It – Applications | Information Technology | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Lead Solution Architect | Information Technology | 1 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Finops | Information Technology | 0 | 9 | 4 | 0 | 11 | 0 | 9 | 2 |
| It Infrastructure | Information Technology | 0 | 6 | 13 | 0 | 10 | 7 | 3 | 0 |
| Data Engineering | Information Technology | 0 | 7 | 4 | 0 | 9 | 1 | 7 | 1 |
| It Leadership | Information Technology | 0 | 8 | 2 | 0 | 9 | 0 | 7 | 2 |
| Pos System Administrator | Information Technology | 0 | 9 | 3 | 0 | 9 | 8 | 1 | 0 |
| It Infra Mgr | Information Technology | 0 | 0 | 3 | 26 | 8 | 4 | 3 | 1 |
| It Infra Lead | Information Technology | 0 | 0 | 9 | 7 | 7 | 2 | 4 | 1 |
| Software Asset Mgr | Information Technology | 0 | 7 | 17 | 0 | 7 | 2 | 5 | 0 |
| Tbm | Information Technology | 0 | 7 | 3 | 0 | 7 | 0 | 5 | 2 |
| App Manager | Information Technology | 0 | 0 | 5 | 6 | 6 | 1 | 4 | 1 |
| It Infrastructure Team | Information Technology | 0 | 4 | 7 | 0 | 6 | 4 | 2 | 0 |
| It Specialist | Information Technology | 0 | 1 | 9 | 1 | 6 | 3 | 3 | 0 |
| App Team | Information Technology | 0 | 0 | 5 | 0 | 5 | 0 | 5 | 0 |
| Architect | Information Technology | 0 | 3 | 6 | 0 | 5 | 1 | 1 | 3 |
| Data Analytics | Information Technology | 0 | 5 | 4 | 0 | 5 | 2 | 3 | 0 |
| Data Stewards | Information Technology | 0 | 4 | 5 | 1 | 5 | 2 | 3 | 0 |
| Devops | Information Technology | 0 | 2 | 5 | 0 | 5 | 3 | 2 | 0 |
| Digital Pm | Information Technology | 0 | 5 | 3 | 2 | 5 | 0 | 3 | 2 |
| Dr | Information Technology | 0 | 5 | 0 | 0 | 5 | 4 | 1 | 0 |
| Field It | Information Technology | 0 | 4 | 6 | 0 | 5 | 1 | 4 | 0 |
| Hr Analytics | Information Technology | 0 | 4 | 2 | 0 | 5 | 0 | 1 | 4 |
| It Data Engineer | Information Technology | 0 | 3 | 3 | 0 | 5 | 2 | 2 | 1 |
| It Integration | Information Technology | 0 | 5 | 1 | 0 | 5 | 1 | 4 | 0 |
| Owning Po & Bpo | Information Technology | 0 | 2 | 8 | 0 | 5 | 0 | 5 | 0 |
| Owning Team It Po | Information Technology | 0 | 3 | 2 | 5 | 5 | 0 | 5 | 0 |
| Ai Ethics Review Board | Information Technology | 0 | 4 | 1 | 0 | 4 | 0 | 3 | 1 |
| Cloud Arch | Information Technology | 0 | 0 | 4 | 3 | 4 | 0 | 3 | 1 |
| Cloud Architect | Information Technology | 0 | 3 | 4 | 0 | 4 | 2 | 2 | 0 |
| Crm Analyst | Information Technology | 0 | 3 | 12 | 0 | 4 | 1 | 1 | 2 |
| Infrastructure Team | Information Technology | 0 | 3 | 7 | 0 | 4 | 3 | 1 | 0 |
| It Database Administrator | Information Technology | 0 | 4 | 1 | 0 | 4 | 2 | 1 | 1 |
| It Integration Specialist | Information Technology | 0 | 4 | 1 | 0 | 4 | 4 | 0 | 0 |
| It Leads | Information Technology | 0 | 3 | 5 | 1 | 4 | 0 | 4 | 0 |
| Portal System | Information Technology | 0 | 0 | 5 | 0 | 4 | 2 | 2 | 0 |
| Service Desk | Information Technology | 0 | 3 | 4 | 0 | 4 | 1 | 3 | 0 |
| Ux Designer | Information Technology | 0 | 4 | 4 | 0 | 4 | 0 | 1 | 3 |
| Av | Information Technology | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Change Management | Information Technology | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Evaluation-Ai-Qa | Information Technology | 0 | 0 | 5 | 0 | 3 | 0 | 3 | 0 |
| Immigration Agent | Information Technology | 0 | 3 | 0 | 0 | 3 | 2 | 1 | 0 |
| Infosec | Information Technology | 0 | 3 | 1 | 0 | 3 | 0 | 2 | 1 |
| Infra Mgr | Information Technology | 0 | 0 | 0 | 3 | 3 | 1 | 2 | 0 |
| It Admin | Information Technology | 0 | 0 | 2 | 3 | 3 | 2 | 0 | 1 |
| It Applications | Information Technology | 0 | 3 | 2 | 0 | 3 | 1 | 2 | 0 |
| It Asset Mgmt | Information Technology | 0 | 3 | 1 | 0 | 3 | 0 | 3 | 0 |
| Merchandising Analytics | Information Technology | 0 | 3 | 3 | 0 | 3 | 0 | 1 | 2 |
| Network Engineering | Information Technology | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Ot Soc | Information Technology | 0 | 3 | 0 | 0 | 3 | 1 | 0 | 2 |
| Qa Specialist | Information Technology | 0 | 0 | 4 | 1 | 3 | 1 | 1 | 1 |
| Service Desk Lead | Information Technology | 0 | 3 | 3 | 0 | 3 | 0 | 3 | 0 |
| Solution Architects | Information Technology | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Ssp | Information Technology | 0 | 2 | 1 | 0 | 3 | 2 | 1 | 0 |
| App Developers | Information Technology | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| App Lead | Information Technology | 0 | 0 | 0 | 3 | 2 | 1 | 1 | 0 |
| Application Support | Information Technology | 0 | 2 | 1 | 0 | 2 | 2 | 0 | 0 |
| Architecture | Information Technology | 0 | 2 | 1 | 0 | 2 | 0 | 1 | 1 |
| Automation Vendor | Information Technology | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Bc | Information Technology | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Business Data Stewards | Information Technology | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Cash App | Information Technology | 0 | 2 | 1 | 0 | 2 | 2 | 0 | 0 |
| Collection Agent | Information Technology | 0 | 2 | 1 | 0 | 2 | 2 | 0 | 0 |
| Data Architect | Information Technology | 0 | 2 | 2 | 0 | 2 | 0 | 1 | 1 |
| Data Gov | Information Technology | 0 | 0 | 3 | 0 | 2 | 0 | 2 | 0 |
| Data Science Team | Information Technology | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 2 |
| Devops Engineer | Information Technology | 0 | 2 | 2 | 0 | 2 | 1 | 1 | 0 |
| Erp Admin | Information Technology | 0 | 0 | 4 | 0 | 2 | 0 | 1 | 1 |
| Escrow Bank Agent | Information Technology | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Global Sourcing Agent | Information Technology | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Information Security | Information Technology | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 2 |
| Integration | Information Technology | 0 | 1 | 4 | 0 | 2 | 0 | 2 | 0 |
| Iot Engineer | Information Technology | 0 | 2 | 3 | 0 | 2 | 0 | 0 | 2 |
| It Asset Coordinator | Information Technology | 0 | 1 | 4 | 0 | 2 | 1 | 0 | 1 |
| It Change Mgr | Information Technology | 0 | 0 | 7 | 4 | 2 | 0 | 2 | 0 |
| It Data Quality Analyst | Information Technology | 0 | 2 | 1 | 0 | 2 | 2 | 0 | 0 |
| It Dba | Information Technology | 0 | 0 | 2 | 2 | 2 | 1 | 1 | 0 |
| It Development | Information Technology | 0 | 2 | 2 | 0 | 2 | 0 | 0 | 2 |
| It Engineer | Information Technology | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| It Integration Mgr | Information Technology | 0 | 1 | 4 | 0 | 2 | 1 | 1 | 0 |
| It Project Mgr | Information Technology | 0 | 0 | 5 | 1 | 2 | 0 | 2 | 0 |
| It Service Lead | Information Technology | 0 | 0 | 0 | 3 | 2 | 0 | 1 | 1 |
| It Specialists | Information Technology | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| It Staff | Information Technology | 0 | 0 | 2 | 0 | 2 | 1 | 1 | 0 |
| It Vendor Mgr | Information Technology | 0 | 0 | 5 | 1 | 2 | 0 | 2 | 0 |
| It-Asset | Information Technology | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Marketing Analytics | Information Technology | 0 | 1 | 1 | 0 | 2 | 0 | 0 | 2 |
| Mdm Manager | Information Technology | 0 | 0 | 0 | 2 | 2 | 0 | 2 | 0 |
| Network Team | Information Technology | 0 | 1 | 1 | 0 | 2 | 1 | 1 | 0 |
| Recovery | Information Technology | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Resolver | Information Technology | 0 | 0 | 3 | 0 | 2 | 0 | 1 | 1 |
| Sec Lead | Information Technology | 0 | 1 | 0 | 1 | 2 | 0 | 2 | 0 |
| Source System Owner | Information Technology | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 2 |
| Support Center Agent | Information Technology | 0 | 0 | 3 | 0 | 2 | 1 | 1 | 0 |
| Tbm Analyst | Information Technology | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Technical Specialist | Information Technology | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Affected Data Subjects | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Ai | Information Technology | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Ai Chatbot | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Ai System | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| All It Staff | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| App Leads | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| App Mgr | Information Technology | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| App Owners | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Application Developers | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Application Lifecycle Owner | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Application Support Lead | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Application Support Team | Information Technology | 0 | 1 | 3 | 0 | 1 | 1 | 0 | 0 |
| Applications Manager | Information Technology | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 |
| Appsec Engineer | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| B2B It Admin | Information Technology | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 |
| Bank Escrow Agent | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Bank It Team | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Bank System Administrator | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Bcp Lead | Information Technology | 0 | 0 | 0 | 2 | 1 | 1 | 0 | 0 |
| Bcp Manager | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Bi Lead | Information Technology | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| Bi System | Information Technology | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| Bi Team | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Bir Eis Helpdesk | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Bsa | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Build Sre | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Buildright Loyalty System | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Cash Application | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Client Erp System | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Cloud Cost Mgr | Information Technology | 0 | 1 | 3 | 0 | 1 | 0 | 0 | 1 |
| Cloud Provider | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Co-Op Verification Hotline Agent | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Commissioning Agent | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Contact-Center Agent | Information Technology | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Corporate Customer It | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Credit Data Providers | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Crm Data Manager | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Crm Data Mgr | Information Technology | 0 | 0 | 0 | 6 | 1 | 0 | 1 | 0 |
| Crm Specialist | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Crm System | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Crm Team | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Customer It | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Cyber Ir | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Cybersecurity | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Data Center Facility Vendor | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Data Governance Committee | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Data Governance Council | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Data Providers | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Data Quality System | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Dev | Information Technology | 0 | 0 | 3 | 0 | 1 | 1 | 0 | 0 |
| Devex Engineers | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Digital Forensics | Information Technology | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Digital Steering | Information Technology | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Domain Qa & Release Analysts | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Engineer | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Engineering & Construction | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Engineering & Director | Information Technology | 0 | 0 | 0 | 3 | 1 | 1 | 0 | 0 |
| Engineering Consultant | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Engineering Lead | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Engineering Manager | Information Technology | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 |
| Engineering Team | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Erp Finance Module | Information Technology | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Erp It Specialist | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Erp Message Bus | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Erp Modules | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Erp System Admin | Information Technology | 0 | 0 | 4 | 1 | 1 | 1 | 0 | 0 |
| Erp Systems Admin | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Escrow Agent | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Esg Data Analyst | Information Technology | 0 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| External Engineering Consultant | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Facilities Helpdesk Lead | Information Technology | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Finance Systems Analyst | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Financing Partner → System | Information Technology | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Fleet Analytics | Information Technology | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| Fleet Analytics & Ci Lead | Information Technology | 0 | 0 | 0 | 4 | 1 | 0 | 0 | 1 |
| Forensics | Information Technology | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Hr Data Specialist | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Hr Service Desk | Information Technology | 0 | 1 | 3 | 0 | 1 | 1 | 0 | 0 |
| Hr System | Information Technology | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| Human Agent | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Industry Orc Intelligence Network | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Infra | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Infra Sre | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Infrastructure | Information Technology | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Infrastructure Lead | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Infrastructure Mgr | Information Technology | 0 | 0 | 0 | 2 | 1 | 1 | 0 | 0 |
| Innovation Lead | Information Technology | 0 | 0 | 3 | 2 | 1 | 0 | 0 | 1 |
| Integration Arch | Information Technology | 0 | 0 | 2 | 3 | 1 | 1 | 0 | 0 |
| Integration Developers | Information Technology | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Integration Leads | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Integration Middleware | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Integration Steering | Information Technology | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 |
| Iot | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Iot System | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| It & Cas Vendor | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| It Ai | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| It App Lead | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| It App Manager | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| It App Mgr | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| It App Support | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| It Apps | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| It Asset Administrator | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| It Data Custodians | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| It Data Engineering | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| It Developers | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| It Development Lead | Information Technology | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| It Devs | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| It Digital Team | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| It Disaster Recovery Lead | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| It Erp Team | Information Technology | 0 | 1 | 3 | 0 | 1 | 1 | 0 | 0 |
| It Field Team | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| It Field Technician | Information Technology | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| It Gis Analyst | Information Technology | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| It Governance | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| It Help Desk | Information Technology | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| It Helpdesk Tier 1 | Information Technology | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| It Helpdesk Tier 2 | Information Technology | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| It Incident | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| It Infra Manager | Information Technology | 0 | 0 | 3 | 2 | 1 | 0 | 1 | 0 |
| It Infrastructure Engineer | Information Technology | 0 | 1 | 0 | 2 | 1 | 1 | 0 | 0 |
| It Innovation | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| It Integration Support | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| It Iot Engineer | Information Technology | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| It Lead | Information Technology | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 |
| It Mgr | Information Technology | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| It Network Operations | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| It On-Call Engineer | Information Technology | 0 | 1 | 4 | 0 | 1 | 1 | 0 | 0 |
| It Payments Lead | Information Technology | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| It Platform | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| It Pos Administrator | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| It Pos System Administrator | Information Technology | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| It Pos Team | Information Technology | 0 | 1 | 3 | 0 | 1 | 1 | 0 | 0 |
| It Security Lead | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| It Service Desk & Erp Payroll Support | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| It Service Desk Analyst | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| It Support Lead | Information Technology | 0 | 0 | 0 | 7 | 1 | 1 | 0 | 0 |
| It System Administrator | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| It Systems | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| It Systems Admin | Information Technology | 0 | 0 | 4 | 0 | 1 | 1 | 0 | 0 |
| It Team Member | Information Technology | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| It Threat Intel | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Itoc | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Knowledge Coord | Information Technology | 0 | 0 | 2 | 1 | 1 | 0 | 1 | 0 |
| Legacy System Admins | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Lgu Engineering | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Loyalty System | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lp Agent | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Marketing Automation | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Marketing Automation Specialist | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Mdm Admin | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Mdm Lead | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Ml Engineer | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Ml Model | Information Technology | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Ml Team | Information Technology | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Mlops | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Network Analyst | Information Technology | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Network Design | Information Technology | 0 | 1 | 2 | 0 | 1 | 0 | 0 | 1 |
| Network Infrastructure Team | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Network Planner | Information Technology | 0 | 0 | 5 | 0 | 1 | 0 | 1 | 0 |
| Ocm Coe | Information Technology | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| Ot Security | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Owning Team Pm | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Owning Team Product Manager | Information Technology | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Partner It | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Pim Lead | Information Technology | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 |
| Pim Qa | Information Technology | 0 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Pim System | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Platform & Erp Teams | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Pm | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Pos Data Analyst | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Pos System Vendor | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Problem Mgr | Information Technology | 0 | 0 | 2 | 3 | 1 | 0 | 1 | 0 |
| Qa & Release Analyst | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Qa Automation Lead | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Qa Mgr | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Qa Tester | Information Technology | 0 | 1 | 2 | 0 | 1 | 0 | 0 | 1 |
| Recovery Agent | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Regional It Field Technician | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Repo Agent | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Resilience | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sam | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sec Grc Cell | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sep | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Sep Build Sre | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Sep Devex Engineers | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sep Qa-Automation Lead | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Service Desk Clerk | Information Technology | 0 | 1 | 3 | 0 | 1 | 0 | 0 | 1 |
| Services Analytics | Information Technology | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Soc | Information Technology | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Soc Lead | Information Technology | 0 | 0 | 0 | 4 | 1 | 1 | 0 | 0 |
| Squad Engineers | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Squad Tech Lead | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Stewards | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Stock Transfer Agent | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Store Network | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Surety Company Agent | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Tester | Information Technology | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| The Caretaker Network | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Tps Tech Leads & Squad Pms | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Transit Underwriter Agent | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ui | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ui Designer | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ux | Information Technology | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Vendor It | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vendor → System | Information Technology | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Vp It | Information Technology | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Vs-103.3 People-Data Integration | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vs-99 Itam | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Web | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Web Scraping Tools | Information Technology | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hr | Human Resources | 64 | 389 | 391 | 18 | 442 | 96 | 292 | 54 |
| Hr Manager | Human Resources | 26 | 41 | 96 | 110 | 89 | 36 | 43 | 10 |
| Screening Program Manager | Human Resources | 23 | 1 | 66 | 2 | 24 | 4 | 18 | 2 |
| L&D | Human Resources | 19 | 72 | 76 | 0 | 78 | 4 | 67 | 7 |
| Ta Marketing | Human Resources | 17 | 19 | 47 | 2 | 20 | 0 | 16 | 4 |
| Ocm Lead | Human Resources | 16 | 0 | 3 | 18 | 17 | 0 | 16 | 1 |
| Head Of Global Mobility | Human Resources | 13 | 0 | 3 | 62 | 23 | 7 | 14 | 2 |
| Ta Operations | Human Resources | 8 | 7 | 19 | 0 | 9 | 0 | 8 | 1 |
| Contingent Workforce Coordinator | Human Resources | 7 | 1 | 0 | 0 | 7 | 2 | 5 | 0 |
| Contingent Workforce Manager | Human Resources | 7 | 0 | 0 | 0 | 7 | 0 | 5 | 2 |
| Immigration Operations Lead | Human Resources | 7 | 0 | 0 | 0 | 7 | 3 | 4 | 0 |
| Employee Experience Manager | Human Resources | 6 | 0 | 0 | 0 | 6 | 0 | 5 | 1 |
| Ex | Human Resources | 5 | 21 | 13 | 0 | 21 | 1 | 11 | 9 |
| Hr Compliance Manager | Human Resources | 5 | 4 | 10 | 8 | 9 | 4 | 5 | 0 |
| Hr Operations Manager | Human Resources | 5 | 1 | 7 | 0 | 5 | 0 | 5 | 0 |
| Eap Manager | Human Resources | 4 | 2 | 15 | 4 | 7 | 2 | 4 | 1 |
| Recruiting | Human Resources | 3 | 13 | 12 | 0 | 13 | 0 | 13 | 0 |
| Compensation | Human Resources | 3 | 5 | 2 | 0 | 7 | 1 | 6 | 0 |
| Hr-Ex | Human Resources | 3 | 0 | 3 | 0 | 3 | 0 | 2 | 1 |
| Hr Assistant | Human Resources | 2 | 13 | 42 | 2 | 20 | 12 | 8 | 0 |
| Workforce Planning | Human Resources | 2 | 11 | 3 | 1 | 11 | 0 | 8 | 3 |
| Hr Specialist | Human Resources | 2 | 6 | 18 | 5 | 7 | 5 | 2 | 0 |
| Admin | Human Resources | 2 | 0 | 8 | 0 | 6 | 1 | 3 | 2 |
| Benefits | Human Resources | 2 | 5 | 8 | 0 | 5 | 2 | 3 | 0 |
| Eap | Human Resources | 2 | 5 | 7 | 0 | 5 | 0 | 5 | 0 |
| Talent Acquisition | Human Resources | 2 | 3 | 3 | 0 | 4 | 0 | 3 | 1 |
| Hr Policy | Human Resources | 2 | 1 | 6 | 0 | 3 | 1 | 2 | 0 |
| Hr Supervisor | Human Resources | 2 | 3 | 11 | 5 | 3 | 2 | 1 | 0 |
| Total Rewards | Human Resources | 2 | 2 | 4 | 0 | 3 | 0 | 3 | 0 |
| Early-Career Lead | Human Resources | 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 |
| Employee Experience | Human Resources | 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 |
| Employer Brand Lead | Human Resources | 2 | 0 | 0 | 2 | 2 | 0 | 2 | 0 |
| Hr Operations | Human Resources | 2 | 1 | 2 | 1 | 2 | 0 | 2 | 0 |
| Hr Strategy | Human Resources | 2 | 0 | 1 | 0 | 2 | 0 | 1 | 1 |
| Relocation Manager | Human Resources | 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 |
| Ocm | Human Resources | 1 | 8 | 63 | 0 | 32 | 0 | 30 | 2 |
| Hr Coordinator | Human Resources | 1 | 7 | 8 | 6 | 10 | 6 | 4 | 0 |
| Contingent | Human Resources | 1 | 5 | 4 | 0 | 7 | 1 | 6 | 0 |
| Dei | Human Resources | 1 | 6 | 2 | 0 | 6 | 0 | 5 | 1 |
| Contingent Workforce | Human Resources | 1 | 5 | 0 | 0 | 5 | 0 | 5 | 0 |
| Head Of People Services | Human Resources | 1 | 0 | 0 | 3 | 4 | 0 | 3 | 1 |
| Hris | Human Resources | 1 | 3 | 4 | 0 | 4 | 1 | 3 | 0 |
| Change | Human Resources | 1 | 2 | 0 | 0 | 3 | 0 | 3 | 0 |
| Hr Administrator | Human Resources | 1 | 1 | 3 | 4 | 2 | 2 | 0 | 0 |
| Travel Coordinator | Human Resources | 1 | 1 | 1 | 0 | 2 | 1 | 1 | 0 |
| Wfm | Human Resources | 1 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Admin Manager | Human Resources | 1 | 1 | 2 | 1 | 1 | 0 | 1 | 0 |
| Contingent-Workforce Lead | Human Resources | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Drug-Free Program | Human Resources | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hr Employee Relations Officer | Human Resources | 1 | 0 | 3 | 4 | 1 | 0 | 1 | 0 |
| Mobility Benefits Manager | Human Resources | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Mobility Payroll Manager | Human Resources | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Mobility Tax Manager | Human Resources | 1 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Ocm Data Lead | Human Resources | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Sales Comp Admin | Human Resources | 1 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Ta Sourcing | Human Resources | 1 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Workforce Vetting Specialist | Human Resources | 1 | 0 | 4 | 4 | 1 | 1 | 0 | 0 |
| Training | Human Resources | 0 | 10 | 15 | 0 | 21 | 2 | 18 | 1 |
| Contingent Workforce Mgr | Human Resources | 0 | 13 | 20 | 18 | 20 | 4 | 13 | 3 |
| Global Mobility | Human Resources | 0 | 1 | 35 | 0 | 14 | 2 | 10 | 2 |
| Hrss | Human Resources | 0 | 2 | 19 | 0 | 10 | 0 | 10 | 0 |
| Hr Shared Services Mgr | Human Resources | 0 | 0 | 4 | 19 | 8 | 0 | 7 | 1 |
| Hrss Team | Human Resources | 0 | 8 | 17 | 0 | 8 | 0 | 7 | 1 |
| Immigration Operations | Human Resources | 0 | 0 | 20 | 0 | 7 | 3 | 4 | 0 |
| Ta Marketing Lead | Human Resources | 0 | 0 | 0 | 18 | 7 | 0 | 5 | 2 |
| Ex Manager | Human Resources | 0 | 6 | 17 | 0 | 6 | 0 | 5 | 1 |
| Hr Training Coordinator | Human Resources | 0 | 5 | 9 | 0 | 6 | 0 | 1 | 5 |
| Entity Hr | Human Resources | 0 | 3 | 1 | 0 | 4 | 0 | 3 | 1 |
| Hr Benefits | Human Resources | 0 | 2 | 6 | 0 | 4 | 1 | 3 | 0 |
| Hr Compliance Mgr | Human Resources | 0 | 1 | 14 | 4 | 4 | 2 | 2 | 0 |
| Labor Compliance Mgr | Human Resources | 0 | 4 | 10 | 0 | 4 | 2 | 2 | 0 |
| Mobility | Human Resources | 0 | 2 | 5 | 0 | 4 | 1 | 3 | 0 |
| C&B | Human Resources | 0 | 3 | 0 | 0 | 3 | 0 | 1 | 2 |
| Compensation Committee | Human Resources | 0 | 3 | 0 | 4 | 3 | 0 | 3 | 0 |
| Contingent Coordinator | Human Resources | 0 | 2 | 3 | 0 | 3 | 0 | 2 | 1 |
| Contingent Lead | Human Resources | 0 | 1 | 1 | 2 | 3 | 0 | 3 | 0 |
| Eap Mgr | Human Resources | 0 | 3 | 0 | 0 | 3 | 1 | 2 | 0 |
| Hr Ops Mgr | Human Resources | 0 | 2 | 1 | 0 | 3 | 0 | 3 | 0 |
| Hr Training | Human Resources | 0 | 0 | 3 | 0 | 3 | 3 | 0 | 0 |
| Immigration | Human Resources | 0 | 2 | 2 | 0 | 3 | 0 | 2 | 1 |
| Relocation | Human Resources | 0 | 0 | 6 | 0 | 3 | 0 | 3 | 0 |
| Ta | Human Resources | 0 | 2 | 2 | 0 | 3 | 0 | 2 | 1 |
| Training Coordinator | Human Resources | 0 | 3 | 3 | 0 | 3 | 0 | 3 | 0 |
| Training Mgr | Human Resources | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Training Officer | Human Resources | 0 | 3 | 7 | 1 | 3 | 0 | 3 | 0 |
| Travel | Human Resources | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Development | Human Resources | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Entity Hr Leads | Human Resources | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| External Labor Counsel | Human Resources | 0 | 2 | 2 | 0 | 2 | 1 | 1 | 0 |
| External Training Provider | Human Resources | 0 | 2 | 0 | 0 | 2 | 1 | 0 | 1 |
| Foreign Worker | Human Resources | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Hr Admin | Human Resources | 0 | 1 | 1 | 2 | 2 | 1 | 1 | 0 |
| Hr Department | Human Resources | 0 | 2 | 4 | 0 | 2 | 2 | 0 | 0 |
| Hr For Employee Cases | Human Resources | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Hr Functions | Human Resources | 0 | 2 | 1 | 0 | 2 | 0 | 1 | 1 |
| Hr Mgr | Human Resources | 0 | 1 | 0 | 1 | 2 | 0 | 2 | 0 |
| Hr Ops Manager | Human Resources | 0 | 0 | 0 | 3 | 2 | 0 | 2 | 0 |
| Hr Recruitment | Human Resources | 0 | 2 | 3 | 0 | 2 | 0 | 2 | 0 |
| Hr Training Mgr | Human Resources | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Hr Training Team | Human Resources | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Mobility Payroll | Human Resources | 0 | 0 | 4 | 0 | 2 | 1 | 1 | 0 |
| Payroll Clerk | Human Resources | 0 | 0 | 5 | 0 | 2 | 1 | 1 | 0 |
| Property Development Mgr | Human Resources | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Recognition | Human Resources | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Recruitment Officer | Human Resources | 0 | 1 | 6 | 1 | 2 | 1 | 1 | 0 |
| Recruitment Specialist | Human Resources | 0 | 2 | 3 | 0 | 2 | 0 | 2 | 0 |
| Relocation Vendor | Human Resources | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Screening | Human Resources | 0 | 0 | 2 | 0 | 2 | 1 | 1 | 0 |
| Trainer | Human Resources | 0 | 1 | 1 | 0 | 2 | 0 | 1 | 1 |
| Training Facilitator | Human Resources | 0 | 1 | 1 | 0 | 2 | 0 | 0 | 2 |
| Associate-Enablement | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Background Screening | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Benefits Lead | Human Resources | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Benefits Manager | Human Resources | 0 | 0 | 0 | 3 | 1 | 1 | 0 | 0 |
| Business Development | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Chro Delegate | Human Resources | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Codi Chair & Members | Human Resources | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Codi Members | Human Resources | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Corporate Development | Human Resources | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Corporate Performance | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Counselors | Human Resources | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Dc Hr Administrators | Human Resources | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Drug-Free Officer | Human Resources | 0 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Ec Claims | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Employee Relations | Human Resources | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Fleet Training | Human Resources | 0 | 0 | 4 | 0 | 1 | 0 | 1 | 0 |
| Home-Country Schemes | Human Resources | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Hr Analyst | Human Resources | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Hr Benefits Admin | Human Resources | 0 | 1 | 6 | 0 | 1 | 1 | 0 | 0 |
| Hr Business Partner And Eap Counselor | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hr Er Officer | Human Resources | 0 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Hr For Multi-Store P&L Literacy | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hr Front Desk | Human Resources | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Hr Labor Relations Manager | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hr Ops | Human Resources | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Hr Payroll Specialist | Human Resources | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Hr Recruitment Manager | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hr Recruitment Specialist | Human Resources | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Hr Role Design | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hr Team | Human Resources | 0 | 0 | 2 | 0 | 1 | 1 | 0 | 0 |
| Hr Technology | Human Resources | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Hr Technology Mgr | Human Resources | 0 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Hr Training & Development | Human Resources | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Hr Workforce Analyst | Human Resources | 0 | 1 | 2 | 0 | 1 | 0 | 0 | 1 |
| Hr Workforce Planning | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hris Analyst | Human Resources | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Hrss Mgr | Human Resources | 0 | 1 | 3 | 0 | 1 | 0 | 0 | 1 |
| L&D Coordinator | Human Resources | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| L&D Team | Human Resources | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Labor | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Labor Planning | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Labor Relations Director Where The Employee Is Union-Covered | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Labor Relations Director Where Workers Are Covered | Human Resources | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Labor Relations Manager | Human Resources | 0 | 0 | 6 | 0 | 1 | 0 | 1 | 0 |
| Learning | Human Resources | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Learning & Dev | Human Resources | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Learning & Development Team | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Municipal Planning & Development Coordinator | Human Resources | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Openings | Human Resources | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Payroll Admin | Human Resources | 0 | 0 | 2 | 0 | 1 | 1 | 0 | 0 |
| Payroll Administrator | Human Resources | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Payroll Clerks | Human Resources | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Payroll Funding Partner | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Performance | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Performance Mgmt | Human Resources | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Performance Owners | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Product Development Team | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Product Trainer | Human Resources | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Product Trainers | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Regional Hr | Human Resources | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Retention | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Schooling | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Separation | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Staffing | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Store Managers And Hr Front Desk | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Succession Committee | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Talent Acquisition Operations | Human Resources | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Total Rewards Director | Human Resources | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 |
| Trainers | Human Resources | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Travel Booking | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Travel Coord | Human Resources | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Vendor Training Specialist | Human Resources | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Vs-98 Contingent Workforce | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Wellness | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Wellness Vendors | Human Resources | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Wfm Lead | Human Resources | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Sales Enablement | Marketing | 28 | 35 | 77 | 0 | 37 | 1 | 27 | 9 |
| Marketing | Marketing | 16 | 248 | 189 | 3 | 284 | 21 | 205 | 58 |
| Insights | Marketing | 10 | 67 | 68 | 0 | 76 | 8 | 47 | 21 |
| Crm | Marketing | 6 | 29 | 13 | 1 | 35 | 4 | 24 | 7 |
| Marketing Analyst | Marketing | 5 | 2 | 5 | 0 | 6 | 0 | 2 | 4 |
| Dam Manager | Marketing | 5 | 0 | 13 | 8 | 5 | 0 | 5 | 0 |
| Marketing Team | Marketing | 4 | 13 | 25 | 0 | 17 | 3 | 10 | 4 |
| Event Lead | Marketing | 3 | 0 | 7 | 6 | 4 | 0 | 4 | 0 |
| Enablement | Marketing | 2 | 5 | 4 | 0 | 6 | 1 | 4 | 1 |
| Marketing Events Coordinator | Marketing | 2 | 1 | 5 | 4 | 2 | 0 | 2 | 0 |
| Marketing Coordinator | Marketing | 1 | 18 | 22 | 3 | 18 | 1 | 11 | 6 |
| Dam | Marketing | 1 | 6 | 8 | 0 | 10 | 0 | 9 | 1 |
| Promotions | Marketing | 1 | 7 | 3 | 0 | 7 | 3 | 4 | 0 |
| Yield Mgmt | Marketing | 1 | 3 | 4 | 0 | 4 | 1 | 1 | 2 |
| Partnerships | Marketing | 1 | 0 | 4 | 0 | 2 | 0 | 2 | 0 |
| Brand & Promotions Manager | Marketing | 1 | 0 | 4 | 4 | 1 | 0 | 1 | 0 |
| Brand Governance | Marketing | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Content Marketing | Marketing | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Content Marketing Lead | Marketing | 1 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Content Marketing Manager | Marketing | 1 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Content Marketing Specialist | Marketing | 1 | 1 | 4 | 2 | 1 | 0 | 1 | 0 |
| Crisis Mgmt | Marketing | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Dam Lead | Marketing | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Email Marketing Specialist | Marketing | 1 | 0 | 3 | 1 | 1 | 0 | 0 | 1 |
| Exhibit Designer | Marketing | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Field Sales Enablement Lead | Marketing | 1 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Localization Coordinator | Marketing | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Marketing & Cx | Marketing | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Marketing Campaigns | Marketing | 1 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Marketing Manager — Category | Marketing | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Partnerships Manager | Marketing | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Store Marketing Coordinator | Marketing | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Studio Lead | Marketing | 1 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Event Marketing Mgr | Marketing | 0 | 0 | 57 | 53 | 24 | 1 | 22 | 1 |
| Sales Enablement Lead | Marketing | 0 | 0 | 0 | 63 | 22 | 0 | 14 | 8 |
| Communications | Marketing | 0 | 19 | 9 | 0 | 20 | 2 | 16 | 2 |
| Retail Media | Marketing | 0 | 13 | 9 | 0 | 13 | 1 | 12 | 0 |
| Channels | Marketing | 0 | 5 | 3 | 0 | 7 | 3 | 4 | 0 |
| Design | Marketing | 0 | 6 | 1 | 0 | 7 | 0 | 7 | 0 |
| Pr | Marketing | 0 | 7 | 1 | 0 | 7 | 0 | 6 | 1 |
| Visual Merchandising Coordinator | Marketing | 0 | 7 | 4 | 0 | 7 | 1 | 5 | 1 |
| Competitive Intel | Marketing | 0 | 4 | 6 | 0 | 6 | 0 | 3 | 3 |
| Content Creator | Marketing | 0 | 6 | 4 | 0 | 6 | 0 | 3 | 3 |
| Digital Marketing Specialist | Marketing | 0 | 6 | 11 | 2 | 6 | 0 | 1 | 5 |
| Marketing Comms Manager | Marketing | 0 | 1 | 15 | 2 | 6 | 1 | 3 | 2 |
| Marketing Mgr | Marketing | 0 | 5 | 0 | 1 | 6 | 0 | 5 | 1 |
| External Pr Agency | Marketing | 0 | 5 | 0 | 0 | 5 | 3 | 1 | 1 |
| Digital Marketing | Marketing | 0 | 3 | 1 | 0 | 3 | 0 | 2 | 1 |
| Events | Marketing | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Marketing Specialist | Marketing | 0 | 3 | 3 | 0 | 3 | 1 | 1 | 1 |
| Print | Marketing | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Promo | Marketing | 0 | 3 | 0 | 0 | 3 | 1 | 1 | 1 |
| Seo | Marketing | 0 | 2 | 4 | 0 | 3 | 0 | 2 | 1 |
| Social Mgr | Marketing | 0 | 0 | 4 | 1 | 3 | 0 | 0 | 3 |
| Store Communications | Marketing | 0 | 3 | 0 | 0 | 3 | 1 | 2 | 0 |
| Vm Coordinator | Marketing | 0 | 0 | 3 | 0 | 3 | 0 | 3 | 0 |
| Vp Corp Comms | Marketing | 0 | 3 | 3 | 1 | 3 | 1 | 2 | 0 |
| Brand Protection | Marketing | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Channel | Marketing | 0 | 0 | 2 | 0 | 2 | 1 | 0 | 1 |
| Ci | Marketing | 0 | 0 | 3 | 0 | 2 | 0 | 1 | 1 |
| Content | Marketing | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Content Team | Marketing | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Creative Team | Marketing | 0 | 1 | 4 | 0 | 2 | 0 | 0 | 2 |
| Designer | Marketing | 0 | 1 | 2 | 0 | 2 | 0 | 1 | 1 |
| Director Marketing | Marketing | 0 | 0 | 0 | 6 | 2 | 0 | 2 | 0 |
| Ecommerce Content Specialist | Marketing | 0 | 2 | 2 | 0 | 2 | 1 | 0 | 1 |
| External Media Agency | Marketing | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| Graphic Designer | Marketing | 0 | 1 | 2 | 0 | 2 | 0 | 2 | 0 |
| Internal Comms Mgr | Marketing | 0 | 2 | 6 | 0 | 2 | 0 | 2 | 0 |
| Loyalty Ops | Marketing | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| Loyalty Program Admin | Marketing | 0 | 0 | 3 | 3 | 2 | 0 | 2 | 0 |
| Loyalty Program Administrator | Marketing | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Market Research | Marketing | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Media | Marketing | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Media Agencies | Marketing | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 2 |
| Product Content Writer | Marketing | 0 | 2 | 6 | 0 | 2 | 0 | 1 | 1 |
| Social Media Mgr | Marketing | 0 | 0 | 4 | 1 | 2 | 1 | 0 | 1 |
| Social Media Specialist | Marketing | 0 | 2 | 3 | 0 | 2 | 0 | 0 | 2 |
| Studio | Marketing | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Videographer | Marketing | 0 | 1 | 2 | 0 | 2 | 0 | 1 | 1 |
| 3D Modeler | Marketing | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| Accredited Third-Party Social Auditors | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Brand Ambassador | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Brand Designer | Marketing | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Brand Lead | Marketing | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Brand Principals | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Competitive Intel Lead | Marketing | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Content Designer | Marketing | 0 | 1 | 2 | 0 | 1 | 0 | 0 | 1 |
| Content Lead | Marketing | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Content Marketing Mgr | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Content Mgr | Marketing | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| Content Owner | Marketing | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Content Rep | Marketing | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Content Specialists | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Content Teams | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Copywriters | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Corp Communications | Marketing | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Corporate Communications Director | Marketing | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Coupons | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Creative Designer | Marketing | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Customer Loyalty | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Customer Marketing | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Digital Content Team | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Digital Marketing Team | Marketing | 0 | 1 | 2 | 0 | 1 | 0 | 0 | 1 |
| Digital Mktg | Marketing | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Digital Mktg Mgr | Marketing | 0 | 0 | 1 | 2 | 1 | 0 | 1 | 0 |
| Ecommerce Content Mgr | Marketing | 0 | 0 | 3 | 1 | 1 | 0 | 0 | 1 |
| Event Host | Marketing | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| External Content Agency | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| External Content Vendors | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Creative | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Graphic Designers | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| In-House Designer | Marketing | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Internal Comms Manager | Marketing | 0 | 0 | 2 | 1 | 1 | 1 | 0 | 0 |
| Local Media | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Loyalty Analyst | Marketing | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Loyalty Lead | Marketing | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| Loyalty Mgr | Marketing | 0 | 0 | 3 | 0 | 1 | 0 | 0 | 1 |
| Loyalty Program | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Loyalty Program Mgr | Marketing | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Loyalty Team | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Marcom Manager | Marketing | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Market Intelligence | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Marketing Associate | Marketing | 0 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Marketing Comm Mgr | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Marketing Designer | Marketing | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Marketing Digital Mgr | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Marketing Host | Marketing | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Marketing Lead | Marketing | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 |
| Marketing Operations | Marketing | 0 | 1 | 2 | 2 | 1 | 0 | 1 | 0 |
| Marketing Ops | Marketing | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| Marketing Production Coordinator | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Marketing Research | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Marketing Research Mgr | Marketing | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Marketing Tech | Marketing | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Mdf | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Media Buyer | Marketing | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Mi | Marketing | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Paid Media | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Partnership Manager | Marketing | 0 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Partnerships Mgr | Marketing | 0 | 0 | 2 | 1 | 1 | 0 | 0 | 1 |
| Photography | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Pr Head | Marketing | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| Pr Officer | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Product Photographer | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Research | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Rmn Manager | Marketing | 0 | 0 | 2 | 2 | 1 | 0 | 0 | 1 |
| Rmn Mgr | Marketing | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Signage | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Social | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Subscription | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Trade Marketing Mgr | Marketing | 0 | 0 | 5 | 0 | 1 | 0 | 1 | 0 |
| Vendor Brand Ambassador | Marketing | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Vendor Brand Manager | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Vendor Brand Protection | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vendor Brand Protection Team | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vendor Marketing | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vendor Marketing Partners | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Video Editors | Marketing | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Visual Merchandising Lead | Marketing | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Visual Merchandising Manager | Marketing | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Store Ops | Store Operations | 71 | 377 | 244 | 0 | 417 | 77 | 292 | 48 |
| Locker Program Manager | Store Operations | 22 | 0 | 9 | 46 | 24 | 4 | 17 | 3 |
| Uniform Program Manager | Store Operations | 16 | 0 | 0 | 0 | 16 | 2 | 12 | 2 |
| Stores | Store Operations | 11 | 18 | 22 | 0 | 32 | 6 | 26 | 0 |
| Rental Fleet Manager | Store Operations | 9 | 10 | 35 | 24 | 16 | 4 | 8 | 4 |
| Director, Storage & Rental Services | Store Operations | 8 | 0 | 0 | 0 | 8 | 1 | 6 | 1 |
| Uniform & Workwear Program Manager | Store Operations | 8 | 0 | 0 | 0 | 8 | 0 | 8 | 0 |
| Store Operations | Store Operations | 3 | 41 | 17 | 2 | 51 | 10 | 34 | 7 |
| Director Storage | Store Operations | 3 | 1 | 16 | 30 | 11 | 2 | 6 | 3 |
| Store | Store Operations | 2 | 69 | 33 | 33 | 85 | 26 | 48 | 11 |
| Locker Program | Store Operations | 1 | 0 | 22 | 0 | 13 | 2 | 10 | 1 |
| Store Operations Coordinator | Store Operations | 1 | 6 | 5 | 1 | 6 | 2 | 4 | 0 |
| Self-Haul Rental | Store Operations | 1 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Rental Compliance | Store Operations | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Rental Fleet Compliance Officer | Store Operations | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Rental Operations Supervisor | Store Operations | 1 | 0 | 1 | 5 | 1 | 0 | 1 | 0 |
| Self-Haul Rental Program Manager | Store Operations | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Services Ops Manager | Store Operations | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Smart-Locker Network Program Manager | Store Operations | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Store Operations Support | Store Operations | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Garden Ops Lead | Store Operations | 0 | 0 | 0 | 28 | 16 | 3 | 13 | 0 |
| Coordinator | Store Operations | 0 | 9 | 28 | 1 | 14 | 3 | 11 | 0 |
| Cx Lead | Store Operations | 0 | 0 | 1 | 17 | 12 | 2 | 10 | 0 |
| Services | Store Operations | 0 | 9 | 13 | 0 | 12 | 0 | 11 | 1 |
| Service Quality Lead | Store Operations | 0 | 0 | 0 | 14 | 9 | 2 | 7 | 0 |
| All Department Heads | Store Operations | 0 | 7 | 2 | 0 | 8 | 1 | 6 | 1 |
| Service Mgr | Store Operations | 0 | 0 | 0 | 15 | 7 | 1 | 6 | 0 |
| Service Partner | Store Operations | 0 | 7 | 1 | 0 | 7 | 2 | 5 | 0 |
| Store Associate | Store Operations | 0 | 2 | 10 | 0 | 7 | 3 | 2 | 2 |
| Counter Lead | Store Operations | 0 | 0 | 0 | 6 | 6 | 5 | 1 | 0 |
| Dept Heads | Store Operations | 0 | 3 | 5 | 0 | 6 | 1 | 2 | 3 |
| Regional Sales Manager | Store Operations | 0 | 1 | 1 | 5 | 6 | 0 | 6 | 0 |
| Building Materials Dept Supervisor | Store Operations | 0 | 0 | 0 | 14 | 5 | 0 | 4 | 1 |
| Location Manager | Store Operations | 0 | 3 | 10 | 0 | 5 | 1 | 4 | 0 |
| Operations | Store Operations | 0 | 2 | 4 | 0 | 5 | 1 | 4 | 0 |
| Department Manager | Store Operations | 0 | 4 | 1 | 1 | 4 | 3 | 0 | 1 |
| Duty Supervisors | Store Operations | 0 | 0 | 5 | 1 | 4 | 2 | 2 | 0 |
| Service | Store Operations | 0 | 4 | 1 | 0 | 4 | 0 | 3 | 1 |
| Service Ops | Store Operations | 0 | 1 | 6 | 0 | 4 | 0 | 4 | 0 |
| Vendor Service | Store Operations | 0 | 4 | 0 | 0 | 4 | 0 | 4 | 0 |
| Affected Department Head | Store Operations | 0 | 3 | 0 | 0 | 3 | 2 | 1 | 0 |
| Auto-Id | Store Operations | 0 | 3 | 2 | 0 | 3 | 0 | 3 | 0 |
| Booth Staff | Store Operations | 0 | 3 | 3 | 0 | 3 | 0 | 3 | 0 |
| Cashier Supervisor | Store Operations | 0 | 1 | 2 | 5 | 3 | 0 | 2 | 1 |
| Dept Manager | Store Operations | 0 | 0 | 3 | 2 | 3 | 2 | 0 | 1 |
| Floor Associate | Store Operations | 0 | 3 | 0 | 0 | 3 | 1 | 2 | 0 |
| Front-End | Store Operations | 0 | 1 | 4 | 0 | 3 | 1 | 2 | 0 |
| Pro Desk Staff | Store Operations | 0 | 3 | 4 | 0 | 3 | 0 | 2 | 1 |
| Regional Teams | Store Operations | 0 | 3 | 1 | 0 | 3 | 2 | 1 | 0 |
| Rental Counter Staff | Store Operations | 0 | 0 | 11 | 0 | 3 | 0 | 3 | 0 |
| Requesting Dept | Store Operations | 0 | 2 | 1 | 0 | 3 | 1 | 0 | 2 |
| Service Partners | Store Operations | 0 | 3 | 0 | 0 | 3 | 0 | 1 | 2 |
| Store Admin | Store Operations | 0 | 3 | 3 | 0 | 3 | 1 | 2 | 0 |
| Store Cashier | Store Operations | 0 | 3 | 1 | 0 | 3 | 2 | 0 | 1 |
| Vendor Service Center | Store Operations | 0 | 3 | 0 | 0 | 3 | 1 | 2 | 0 |
| Vendor Service Teams | Store Operations | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Bir Revenue District Office | Store Operations | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Bir Revenue District Officer | Store Operations | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Cashier Lead | Store Operations | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Cit Service | Store Operations | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Clienteling | Store Operations | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| Closure | Store Operations | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Department Managers | Store Operations | 0 | 2 | 1 | 0 | 2 | 0 | 1 | 1 |
| Department Mentor | Store Operations | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Dept Users | Store Operations | 0 | 0 | 2 | 0 | 2 | 1 | 0 | 1 |
| Dole Regional Office | Store Operations | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Duty Supervisor | Store Operations | 0 | 0 | 3 | 0 | 2 | 1 | 1 | 0 |
| Field | Store Operations | 0 | 1 | 1 | 0 | 2 | 0 | 1 | 1 |
| Front-End Supervisor | Store Operations | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Home Décor & Furniture Dept Supervisor | Store Operations | 0 | 0 | 0 | 7 | 2 | 0 | 1 | 1 |
| Local Emergency Services | Store Operations | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Op Excellence | Store Operations | 0 | 2 | 2 | 0 | 2 | 0 | 0 | 2 |
| Paint Dept Supervisor | Store Operations | 0 | 1 | 2 | 0 | 2 | 1 | 1 | 0 |
| Service Technician | Store Operations | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Services Coordinator | Store Operations | 0 | 2 | 4 | 3 | 2 | 1 | 1 | 0 |
| Services Mgr | Store Operations | 0 | 0 | 3 | 3 | 2 | 0 | 0 | 2 |
| Special Order Coordinator | Store Operations | 0 | 2 | 3 | 0 | 2 | 0 | 2 | 0 |
| Store Comms | Store Operations | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Store Operations Rep | Store Operations | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Store Ops It | Store Operations | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Store Ops Manager | Store Operations | 0 | 0 | 3 | 0 | 2 | 0 | 2 | 0 |
| Store Ops Regional | Store Operations | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Store Ops Vp | Store Operations | 0 | 2 | 0 | 0 | 2 | 1 | 0 | 1 |
| Tools & Hardware Dept Supervisor | Store Operations | 0 | 0 | 0 | 8 | 2 | 0 | 2 | 0 |
| User Dept Head | Store Operations | 0 | 0 | 0 | 3 | 2 | 1 | 1 | 0 |
| Affected Department Heads | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| All Floor | Store Operations | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| All On-Shift Store Associates | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| All On-Shift Store Staff | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| All Store Staff On Duty | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| All Store Staff On Duty During Failure | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Armored Car Service | Store Operations | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Armored Car Service Partner | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Assigned Department | Store Operations | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Authorized Service Center | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Bfp Regional Office | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Bfp-Accredited Service Provider | Store Operations | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Bid Mgr | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Business Department Heads | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Carry-Out Staff | Store Operations | 0 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Cleaning Service | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Closing Store Staff | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Concept | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Counter Supervisor | Store Operations | 0 | 0 | 0 | 3 | 1 | 0 | 1 | 0 |
| Cross-Entity Services | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Customer Experience Mgr | Store Operations | 0 | 0 | 2 | 4 | 1 | 0 | 1 | 0 |
| Customer Experience Representative | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Customer Experience Team | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Cx Assurance | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Cx Rep | Store Operations | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| Dark-Store | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Demo Station Attendant | Store Operations | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Department Custodians | Store Operations | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Department Of Agrarian Reform | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Department Of Agrarian Reform Municipal | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Department Owner | Store Operations | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Department Owners | Store Operations | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Department Power Users | Store Operations | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Department Sme | Store Operations | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| Department Smes | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Dept Head'S Vp | Store Operations | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Dept Owners | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Dept Requestors | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Design Services | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Designated Store Manager On-Duty | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Dole Regional Director | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Emergency Services | Store Operations | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Equipment Rental Partner | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Equipment Vendor Service Engineer | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Estimating | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Estimation | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Estimation Specialist | Store Operations | 0 | 0 | 4 | 0 | 1 | 0 | 1 | 0 |
| Existing Regional Managers | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Dr Service Provider | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| External Emergency Services | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| External Monitoring Services | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Service Providers | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Fabrication Service Partner | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Field Ops | Store Operations | 0 | 1 | 3 | 0 | 1 | 1 | 0 | 0 |
| Field Recovery | Store Operations | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Field Service | Store Operations | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Field Service Tech | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Field Services | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Garden | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Garden & Outdoor Dept Supervisor | Store Operations | 0 | 0 | 0 | 3 | 1 | 0 | 0 | 1 |
| Garden Center Associate | Store Operations | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| Garden Center Lead | Store Operations | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Generator Service Technician | Store Operations | 0 | 1 | 2 | 0 | 1 | 0 | 0 | 1 |
| Greeter | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Home Appliances Dept Supervisor | Store Operations | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 |
| Hq Department Lead | Store Operations | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Industrial Engineer | Store Operations | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Installation Service Partner | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| It Store Ops Mgr | Store Operations | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Labeling | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Local Fire Department | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Local Fire Dept | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Lumber Dept Supervisor | Store Operations | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Mandatory Discount | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Mhe Service Vendor | Store Operations | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| New Store Manager | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| New Store Staff | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Night Shift Associates | Store Operations | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| Night Shift Supervisor | Store Operations | 0 | 1 | 4 | 2 | 1 | 1 | 0 | 0 |
| Oem Authorized Service | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Oem Service Partner | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Operations Specialist | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Ops-Standards | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Or The Regional Cluppi For Smaller Tracts | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Order Processing | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Paint Associate | Store Operations | 0 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Paint Dept | Store Operations | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Paint Desk Associate | Store Operations | 0 | 1 | 6 | 0 | 1 | 1 | 0 | 0 |
| Paint Mixing Operator | Store Operations | 0 | 0 | 4 | 0 | 1 | 0 | 0 | 1 |
| Paint Section Lead | Store Operations | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Paint Technician | Store Operations | 0 | 1 | 7 | 0 | 1 | 0 | 0 | 1 |
| People Services | Store Operations | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Pilot Site | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Pilot Store Managers | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Pilot Stores | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Plumbing Dept Supervisor | Store Operations | 0 | 0 | 0 | 3 | 1 | 0 | 1 | 0 |
| Pro Desk Associate | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Process Excellence | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Product Experts | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Purchasing Dept | Store Operations | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| Regional Facilities Manager | Store Operations | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Regional Lp Manager | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Regional Manager & Store Manager | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Regional Manager Closure Authority | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Regional Merchandiser | Store Operations | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Regional Safety Coordinator | Store Operations | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Regional Safety Officer | Store Operations | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Regional Sales | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Regional Sales Coordinator | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Regional Sales Managers | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Regional Store Managers | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Regional Store Ops | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Regional Vps | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Rental Desk | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Requesting Dept Head | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sales Tech | Store Operations | 0 | 0 | 3 | 1 | 1 | 0 | 1 | 0 |
| Sari-Sari | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Scan-And-Go Attendant | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Sco Supervisor | Store Operations | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| Seasonal | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Selling-Enablement | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Sending Location | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Sending Location Manager | Store Operations | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Sending Store Manager | Store Operations | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Service Contractor | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Service Del Lead | Store Operations | 0 | 0 | 0 | 3 | 1 | 0 | 1 | 0 |
| Service Del Mgr | Store Operations | 0 | 0 | 5 | 1 | 1 | 0 | 1 | 0 |
| Service Installation Manager | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Service Installation Mgr | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Service Operations Manager | Store Operations | 0 | 1 | 1 | 2 | 1 | 0 | 0 | 1 |
| Service Operations Team | Store Operations | 0 | 1 | 2 | 1 | 1 | 0 | 1 | 0 |
| Service Providers | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Service Warranty Specialist | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Service Workshop | Store Operations | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Services Admin | Store Operations | 0 | 1 | 0 | 3 | 1 | 0 | 0 | 1 |
| Services Qual Mgr | Store Operations | 0 | 0 | 3 | 1 | 1 | 0 | 0 | 1 |
| Services Quality Mgr | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Special Orders | Store Operations | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Store A Clerk | Store Operations | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Store Assoc | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Store Associates | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Store Clerk | Store Operations | 0 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Store Communication | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Store Csr | Store Operations | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Store Department Supervisors | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Store Garden Center Associate | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Store Liaison | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Store Manager A | Store Operations | 0 | 0 | 0 | 2 | 1 | 1 | 0 | 0 |
| Store Manager And Department Staff | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Store Manager B | Store Operations | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| Store Manager Representatives | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Store Managers & Front-End | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Store Managers & Front-End Supervisors | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Store Opening Pm | Store Operations | 0 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Store Opening Team | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Store Operations & Service Desks | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Store Operations Finance | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Store Operations Leadership | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Store Operations Team Members | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Store Ops [Unaware] | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Store Ops Coordinator | Store Operations | 0 | 0 | 3 | 0 | 1 | 1 | 0 | 0 |
| Store Ops Standards Manager | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Store Picker | Store Operations | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Store Safety Officers | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Store Sales Associate | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Store Services | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Store Supervisor | Store Operations | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Store Team | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Store Teams | Store Operations | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Stores Clerk | Store Operations | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Task Mgmt | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Tesda Regional Inspector | Store Operations | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Tesda Regional Officer | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Third-Party Rental Partner | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Tiles & Flooring Dept Supervisor | Store Operations | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 |
| Tool Demo Station Attendant | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Tool Rental | Store Operations | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Tool Rental Coordinator | Store Operations | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Vendor Demo Representative | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Vendor Service Engineers | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vendor Service Technician | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Vp Department | Store Operations | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Vp Store Dev | Store Operations | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Vp Store Operations & Regional Managers | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Vs-13 Cx | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Vs-146 Service Qa | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Warranty Manager | Store Operations | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 |
| Will-Call Counter Staff | Store Operations | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Workshop | Store Operations | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Workshop Supervisor | Store Operations | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Legal | Legal & Compliance | 90 | 824 | 1010 | 50 | 950 | 276 | 620 | 54 |
| Compliance | Legal & Compliance | 71 | 332 | 386 | 13 | 378 | 114 | 239 | 25 |
| Pcab Compliance Lead | Legal & Compliance | 24 | 0 | 70 | 0 | 24 | 6 | 16 | 2 |
| Ethics & Compliance Officer | Legal & Compliance | 23 | 24 | 66 | 58 | 24 | 7 | 13 | 4 |
| Legal Counsel | Legal & Compliance | 16 | 97 | 110 | 49 | 144 | 60 | 71 | 13 |
| Compliance Specialist | Legal & Compliance | 13 | 9 | 54 | 42 | 24 | 15 | 9 | 0 |
| Privacy | Legal & Compliance | 10 | 108 | 83 | 2 | 113 | 35 | 73 | 5 |
| Legal Compliance Officer | Legal & Compliance | 9 | 16 | 30 | 2 | 17 | 8 | 8 | 1 |
| Legal Operations Manager | Legal & Compliance | 9 | 0 | 0 | 0 | 9 | 0 | 7 | 2 |
| Trade Compliance Manager | Legal & Compliance | 8 | 1 | 1 | 45 | 23 | 13 | 10 | 0 |
| Compliance Operations | Legal & Compliance | 8 | 0 | 36 | 0 | 17 | 3 | 11 | 3 |
| Records | Legal & Compliance | 6 | 53 | 54 | 0 | 62 | 28 | 34 | 0 |
| Legal & Compliance Officer | Legal & Compliance | 5 | 8 | 15 | 2 | 11 | 3 | 8 | 0 |
| Governance | Legal & Compliance | 3 | 18 | 10 | 1 | 21 | 3 | 14 | 4 |
| Legal & Compliance Counsel | Legal & Compliance | 3 | 0 | 12 | 12 | 3 | 0 | 3 | 0 |
| Ethics | Legal & Compliance | 2 | 12 | 9 | 0 | 15 | 1 | 14 | 0 |
| Legal Operations | Legal & Compliance | 2 | 12 | 8 | 8 | 14 | 5 | 9 | 0 |
| Compliance Portfolio | Legal & Compliance | 2 | 2 | 16 | 0 | 11 | 3 | 5 | 3 |
| Legal Specialist | Legal & Compliance | 2 | 0 | 9 | 9 | 2 | 1 | 1 | 0 |
| Department Records Custodian | Legal & Compliance | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Director Of Legal Operations | Legal & Compliance | 1 | 0 | 4 | 4 | 1 | 0 | 1 | 0 |
| Land Legal Specialist | Legal & Compliance | 1 | 0 | 5 | 5 | 1 | 1 | 0 | 0 |
| Legal & Compliance Manager | Legal & Compliance | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Legal-Compliance | Legal & Compliance | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Legal-Regulatory | Legal & Compliance | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lgu Compliance | Legal & Compliance | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Lgu Compliance Liaison | Legal & Compliance | 1 | 0 | 4 | 4 | 1 | 1 | 0 | 0 |
| Compliance Lead | Legal & Compliance | 0 | 0 | 0 | 44 | 23 | 9 | 13 | 1 |
| Legal Ops Mgr | Legal & Compliance | 0 | 15 | 33 | 0 | 21 | 5 | 13 | 3 |
| Regulatory | Legal & Compliance | 0 | 8 | 9 | 0 | 14 | 8 | 6 | 0 |
| Records Mgr | Legal & Compliance | 0 | 9 | 0 | 0 | 9 | 2 | 7 | 0 |
| Ip | Legal & Compliance | 0 | 4 | 1 | 0 | 5 | 2 | 3 | 0 |
| Legal Assistant | Legal & Compliance | 0 | 0 | 9 | 0 | 5 | 0 | 1 | 4 |
| Domain Compliance Owners | Legal & Compliance | 0 | 4 | 0 | 0 | 4 | 0 | 4 | 0 |
| Compliance Mgr | Legal & Compliance | 0 | 0 | 7 | 0 | 3 | 0 | 2 | 1 |
| Compliance Team | Legal & Compliance | 0 | 2 | 1 | 1 | 3 | 2 | 1 | 0 |
| Dole Compliance Officer | Legal & Compliance | 0 | 3 | 0 | 0 | 3 | 2 | 1 | 0 |
| Ethics Lead | Legal & Compliance | 0 | 0 | 0 | 3 | 3 | 0 | 3 | 0 |
| External Affairs | Legal & Compliance | 0 | 3 | 3 | 0 | 3 | 0 | 3 | 0 |
| External Competition Counsel | Legal & Compliance | 0 | 3 | 0 | 0 | 3 | 2 | 1 | 0 |
| Legal & Compliance | Legal & Compliance | 0 | 2 | 0 | 1 | 3 | 1 | 2 | 0 |
| Aml Officer | Legal & Compliance | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Document Control | Legal & Compliance | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| External Regulatory Consultant | Legal & Compliance | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| In-House Counsel | Legal & Compliance | 0 | 2 | 5 | 0 | 2 | 0 | 2 | 0 |
| Kyc | Legal & Compliance | 0 | 2 | 3 | 0 | 2 | 1 | 1 | 0 |
| Legal Department | Legal & Compliance | 0 | 2 | 0 | 0 | 2 | 1 | 0 | 1 |
| Legal Manager | Legal & Compliance | 0 | 1 | 4 | 3 | 2 | 0 | 2 | 0 |
| Lgu Affairs | Legal & Compliance | 0 | 2 | 1 | 0 | 2 | 1 | 1 | 0 |
| Localization | Legal & Compliance | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Speak-Up | Legal & Compliance | 0 | 2 | 1 | 0 | 2 | 2 | 0 | 0 |
| Abc Officer | Legal & Compliance | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Advising | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Afc | Legal & Compliance | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| All Domain Compliance Owners | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Aml Analyst | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Aml Lead | Legal & Compliance | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Anti-Corruption | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Approver Per Policy Type | Legal & Compliance | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Business Permit Licensing Office | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Center For Land Use Policy | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Compliance Head | Legal & Compliance | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Compliance Liaison | Legal & Compliance | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Compliance Team Per W657 | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Contract Management | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Contract Mgmt | Legal & Compliance | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Denr Compliance Officer | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Developer Legal Counsel | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Dg Compliance | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Domiciliary Rules | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Dpo-Function | Legal & Compliance | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Energy Regulatory Commission | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| External Litigation Counsel | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Fleet Compliance | Legal & Compliance | 0 | 0 | 3 | 0 | 1 | 1 | 0 | 0 |
| Governance Function Per W1721 | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Government Relations | Legal & Compliance | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Hq Compliance | Legal & Compliance | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| Import Compliance Mgr | Legal & Compliance | 0 | 0 | 0 | 3 | 1 | 0 | 1 | 0 |
| Ip Community Leader | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ip Office | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Legal Officer | Legal & Compliance | 0 | 0 | 2 | 1 | 1 | 0 | 1 | 0 |
| Lender Legal | Legal & Compliance | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Lgu Business Permit And Licensing Office | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lgu Specialist | Legal & Compliance | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Litigation | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Localization Coord | Legal & Compliance | 0 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Permitting | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Platform Fraud Channels & Marketplace Ip Desks | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Policy Owner | Legal & Compliance | 0 | 1 | 3 | 1 | 1 | 0 | 1 | 0 |
| Property Compliance Mgr | Legal & Compliance | 0 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Records Custodian | Legal & Compliance | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Regulatory Affairs | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sanctions | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Sec Privacy | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Speak-Up Intake Team | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Store Manager Or Legal Rep | Legal & Compliance | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Supplier Compliance | Legal & Compliance | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Supplier Compliance Mgr | Legal & Compliance | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| The Business Compliance Partners | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Trade Compliance Mgr | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Vendor Compliance | Legal & Compliance | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Internal Audit | Internal Audit & Risk | 54 | 155 | 137 | 19 | 215 | 57 | 109 | 49 |
| Risk | Internal Audit & Risk | 36 | 120 | 129 | 1 | 148 | 25 | 103 | 20 |
| Audit | Internal Audit & Risk | 13 | 122 | 136 | 0 | 148 | 45 | 84 | 19 |
| Bc Manager | Internal Audit & Risk | 5 | 12 | 31 | 2 | 17 | 16 | 1 | 0 |
| Bcp | Internal Audit & Risk | 4 | 24 | 25 | 0 | 28 | 8 | 18 | 2 |
| Business Continuity Manager | Internal Audit & Risk | 3 | 0 | 0 | 4 | 3 | 3 | 0 | 0 |
| Travel Risk Manager | Internal Audit & Risk | 3 | 0 | 4 | 0 | 3 | 0 | 3 | 0 |
| Model Risk | Internal Audit & Risk | 2 | 11 | 16 | 0 | 12 | 5 | 7 | 0 |
| Lp Auditor | Internal Audit & Risk | 1 | 2 | 7 | 0 | 2 | 0 | 2 | 0 |
| Director Of Business Continuity | Internal Audit & Risk | 1 | 0 | 4 | 4 | 1 | 1 | 0 | 0 |
| Risk & Compliance Officer | Internal Audit & Risk | 1 | 1 | 6 | 1 | 1 | 0 | 1 | 0 |
| Risk & Controls | Internal Audit & Risk | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Risk Management Specialist | Internal Audit & Risk | 1 | 0 | 4 | 4 | 1 | 0 | 1 | 0 |
| Speak-Up Intake | Internal Audit & Risk | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Third-Party Risk | Internal Audit & Risk | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Third-Party Risk Lead | Internal Audit & Risk | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Auditor | Internal Audit & Risk | 0 | 4 | 126 | 0 | 33 | 0 | 5 | 28 |
| Audit Team | Internal Audit & Risk | 0 | 3 | 20 | 0 | 7 | 0 | 0 | 7 |
| External Audit | Internal Audit & Risk | 0 | 7 | 1 | 0 | 7 | 3 | 4 | 0 |
| Audit Lead | Internal Audit & Risk | 0 | 0 | 0 | 7 | 6 | 1 | 5 | 0 |
| Bcm | Internal Audit & Risk | 0 | 4 | 7 | 0 | 5 | 5 | 0 | 0 |
| External Audit Team | Internal Audit & Risk | 0 | 4 | 0 | 0 | 4 | 4 | 0 | 0 |
| Internal Controls | Internal Audit & Risk | 0 | 1 | 4 | 0 | 4 | 1 | 2 | 1 |
| Risk Analyst | Internal Audit & Risk | 0 | 1 | 6 | 0 | 4 | 1 | 1 | 2 |
| Risk Committee | Internal Audit & Risk | 0 | 3 | 0 | 1 | 4 | 0 | 1 | 3 |
| Audit & Risk Committee | Internal Audit & Risk | 0 | 2 | 1 | 0 | 3 | 1 | 0 | 2 |
| Erm | Internal Audit & Risk | 0 | 2 | 1 | 0 | 3 | 0 | 1 | 2 |
| Assurance | Internal Audit & Risk | 0 | 1 | 2 | 0 | 2 | 0 | 1 | 1 |
| Board Audit | Internal Audit & Risk | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| Crisis Comms | Internal Audit & Risk | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Energy Audit Partner | Internal Audit & Risk | 0 | 2 | 2 | 0 | 2 | 0 | 1 | 1 |
| Fraud Analyst | Internal Audit & Risk | 0 | 1 | 2 | 0 | 2 | 0 | 2 | 0 |
| Fraud Investigators | Internal Audit & Risk | 0 | 2 | 4 | 0 | 2 | 2 | 0 | 0 |
| Fraud Ops Analyst | Internal Audit & Risk | 0 | 2 | 3 | 1 | 2 | 0 | 2 | 0 |
| Head Of Fraud | Internal Audit & Risk | 0 | 0 | 0 | 3 | 2 | 0 | 2 | 0 |
| Internal Audit Manager | Internal Audit & Risk | 0 | 0 | 0 | 2 | 2 | 2 | 0 | 0 |
| Risk Management | Internal Audit & Risk | 0 | 2 | 0 | 0 | 2 | 1 | 0 | 1 |
| Ai Incident Management | Internal Audit & Risk | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Audit Analyst | Internal Audit & Risk | 0 | 0 | 3 | 0 | 1 | 0 | 0 | 1 |
| Audit Committee Chair | Internal Audit & Risk | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Bank Fraud Desk | Internal Audit & Risk | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Barangay Crisis Responders Where Engaged | Internal Audit & Risk | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Buildright'S Bank Fraud Desk And The Beneficiary Bank | Internal Audit & Risk | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Crisis Comms Firm | Internal Audit & Risk | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Crisis Team | Internal Audit & Risk | 0 | 0 | 2 | 0 | 1 | 1 | 0 | 0 |
| External Risk Advisor | Internal Audit & Risk | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Fraud Specialist | Internal Audit & Risk | 0 | 0 | 3 | 4 | 1 | 1 | 0 | 0 |
| Head Of Internal Audit & Risk-Function | Internal Audit & Risk | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Internal Audit Head | Internal Audit & Risk | 0 | 1 | 2 | 2 | 1 | 0 | 0 | 1 |
| Internal Audit Per W338 | Internal Audit & Risk | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| It Incident Management | Internal Audit & Risk | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lgu Disaster Risk Reduction Office | Internal Audit & Risk | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Marketing Audit | Internal Audit & Risk | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Marketing Audit Team | Internal Audit & Risk | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Model Risk Lead | Internal Audit & Risk | 0 | 0 | 0 | 2 | 1 | 1 | 0 | 0 |
| Risk Mgr | Internal Audit & Risk | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Risk Officer | Internal Audit & Risk | 0 | 0 | 8 | 0 | 1 | 0 | 0 | 1 |
| Risk Specialist | Internal Audit & Risk | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Third-Party Audit Firm | Internal Audit & Risk | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Cx | Customer Service | 25 | 96 | 100 | 2 | 104 | 14 | 70 | 20 |
| Customer Service | Customer Service | 10 | 81 | 63 | 1 | 91 | 35 | 49 | 7 |
| Customer Experience Manager | Customer Service | 8 | 3 | 8 | 6 | 10 | 0 | 7 | 3 |
| Customer Experience | Customer Service | 4 | 2 | 1 | 0 | 6 | 0 | 4 | 2 |
| Customer Experience Analyst | Customer Service | 4 | 0 | 0 | 0 | 4 | 0 | 3 | 1 |
| Warranty | Customer Service | 3 | 7 | 8 | 0 | 9 | 0 | 9 | 0 |
| Cs Manager | Customer Service | 2 | 9 | 35 | 34 | 14 | 2 | 11 | 1 |
| Warranty Administrator | Customer Service | 2 | 2 | 2 | 0 | 4 | 0 | 3 | 1 |
| Solar Technical Support | Customer Service | 2 | 0 | 0 | 0 | 2 | 0 | 1 | 1 |
| Cx Manager | Customer Service | 1 | 5 | 17 | 15 | 13 | 3 | 8 | 2 |
| Customer Support | Customer Service | 1 | 9 | 8 | 0 | 10 | 0 | 10 | 0 |
| Cx Analyst | Customer Service | 1 | 6 | 11 | 1 | 7 | 0 | 4 | 3 |
| Contact Center | Customer Service | 1 | 4 | 3 | 0 | 4 | 1 | 2 | 1 |
| Cs Agent | Customer Service | 1 | 3 | 8 | 1 | 4 | 0 | 3 | 1 |
| Cx Analytics Lead | Customer Service | 1 | 2 | 6 | 8 | 3 | 1 | 1 | 1 |
| Vendor Warranty Coordinator | Customer Service | 1 | 1 | 0 | 0 | 2 | 0 | 2 | 0 |
| Customer Relations Officer | Customer Service | 1 | 0 | 2 | 4 | 1 | 0 | 1 | 0 |
| Customer Service — Ecommerce Returns Specialist | Customer Service | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Cx Recovery Specialist | Customer Service | 1 | 0 | 5 | 1 | 1 | 1 | 0 | 0 |
| Ecommerce Customer Service Manager | Customer Service | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Extended Warranty Claims Specialist | Customer Service | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Marketing — Cs Manager | Customer Service | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Service Center Coordinator | Customer Service | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Store Customer Experience Supervisor | Customer Service | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Cs | Customer Service | 0 | 12 | 10 | 0 | 13 | 3 | 9 | 1 |
| Cs Director | Customer Service | 0 | 3 | 3 | 4 | 6 | 0 | 5 | 1 |
| Customer Service Counter Staff | Customer Service | 0 | 4 | 0 | 0 | 4 | 1 | 3 | 0 |
| Customer Service Mgr | Customer Service | 0 | 4 | 0 | 4 | 4 | 1 | 3 | 0 |
| Cs Counter Staff | Customer Service | 0 | 0 | 3 | 0 | 3 | 1 | 2 | 0 |
| Support Center Lead | Customer Service | 0 | 0 | 2 | 4 | 3 | 1 | 2 | 0 |
| Call Center | Customer Service | 0 | 0 | 2 | 0 | 2 | 0 | 1 | 1 |
| Customer Service Counter | Customer Service | 0 | 2 | 2 | 0 | 2 | 0 | 0 | 2 |
| Support Center | Customer Service | 0 | 0 | 2 | 0 | 2 | 1 | 1 | 0 |
| Voc | Customer Service | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| Actuarial Support | Customer Service | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Cs Agents | Customer Service | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Cs Rep | Customer Service | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Cs Staff | Customer Service | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Cs Team | Customer Service | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Customer Service Dir | Customer Service | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Customer Service Team | Customer Service | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Customer Support Lead | Customer Service | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Dedicated Call Center Agent | Customer Service | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Desktop Support | Customer Service | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Electric Utility Customer Service | Customer Service | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Marketplace Cs Tools | Customer Service | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Pos Vendor Support | Customer Service | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Third-Party Hotline Provider | Customer Service | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Third-Party Hotline Vendor | Customer Service | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Vendor Support | Customer Service | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vendor Technical Support | Customer Service | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vip Call Center Agent | Customer Service | 0 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Warranty Claims Team | Customer Service | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Lp | Regional Loss Prevention | 18 | 120 | 148 | 4 | 155 | 49 | 95 | 11 |
| Loss Prevention | Regional Loss Prevention | 14 | 44 | 28 | 0 | 59 | 23 | 30 | 6 |
| Lp Manager | Regional Loss Prevention | 12 | 30 | 62 | 107 | 74 | 30 | 36 | 8 |
| Loss Prevention Manager | Regional Loss Prevention | 8 | 2 | 5 | 8 | 9 | 3 | 4 | 2 |
| Lp Training Coordinator | Regional Loss Prevention | 1 | 1 | 3 | 0 | 2 | 1 | 1 | 0 |
| Loss Prevention Supervisor | Regional Loss Prevention | 1 | 0 | 2 | 4 | 1 | 1 | 0 | 0 |
| Lp & Safety | Regional Loss Prevention | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lp Supervisor | Regional Loss Prevention | 1 | 1 | 4 | 0 | 1 | 0 | 1 | 0 |
| Security & Lp | Regional Loss Prevention | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Security & Lp Manager | Regional Loss Prevention | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Store Security Lead | Regional Loss Prevention | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lp Lead | Regional Loss Prevention | 0 | 0 | 0 | 27 | 18 | 3 | 14 | 1 |
| Gsoc | Regional Loss Prevention | 0 | 5 | 9 | 0 | 9 | 2 | 7 | 0 |
| Ep | Regional Loss Prevention | 0 | 2 | 3 | 0 | 4 | 0 | 4 | 0 |
| Loss Prevention Mgr | Regional Loss Prevention | 0 | 4 | 0 | 7 | 4 | 0 | 4 | 0 |
| Lp Team | Regional Loss Prevention | 0 | 2 | 3 | 0 | 4 | 1 | 3 | 0 |
| Ep Agents | Regional Loss Prevention | 0 | 3 | 2 | 0 | 3 | 0 | 3 | 0 |
| Travel Risk | Regional Loss Prevention | 0 | 1 | 4 | 0 | 3 | 0 | 3 | 0 |
| Investigations Manager | Regional Loss Prevention | 0 | 0 | 3 | 0 | 2 | 2 | 0 | 0 |
| Investigator | Regional Loss Prevention | 0 | 0 | 2 | 0 | 2 | 1 | 1 | 0 |
| Lp Associate | Regional Loss Prevention | 0 | 1 | 3 | 0 | 2 | 0 | 2 | 0 |
| Lp Operations | Regional Loss Prevention | 0 | 1 | 4 | 0 | 2 | 0 | 2 | 0 |
| Lp Specialist | Regional Loss Prevention | 0 | 1 | 2 | 0 | 2 | 1 | 1 | 0 |
| Protective Intelligence | Regional Loss Prevention | 0 | 1 | 2 | 0 | 2 | 0 | 2 | 0 |
| Security Lead | Regional Loss Prevention | 0 | 2 | 1 | 0 | 2 | 0 | 0 | 2 |
| Security Mgr | Regional Loss Prevention | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Cmt | Regional Loss Prevention | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Cmt Lead | Regional Loss Prevention | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| Ep Advance | Regional Loss Prevention | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Gsoc Analysts | Regional Loss Prevention | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Industry Lp Association | Regional Loss Prevention | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Intelligence | Regional Loss Prevention | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Investigations Team | Regional Loss Prevention | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Loss Prevention Associate | Regional Loss Prevention | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lp Agents | Regional Loss Prevention | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lp Duty | Regional Loss Prevention | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Lp Equipment Vendor | Regional Loss Prevention | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Lp Operations Center | Regional Loss Prevention | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lp Ops Center | Regional Loss Prevention | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Lp Ops Center Mgr | Regional Loss Prevention | 0 | 0 | 0 | 7 | 1 | 0 | 1 | 0 |
| Lp Team Per W466 | Regional Loss Prevention | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Protective Intel | Regional Loss Prevention | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Residential Security | Regional Loss Prevention | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Security Team Lead | Regional Loss Prevention | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Traveling Ep | Regional Loss Prevention | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Hse | Health, Safety & Environment | 51 | 205 | 234 | 6 | 219 | 53 | 152 | 14 |
| Customer Safety | Health, Safety & Environment | 21 | 24 | 40 | 0 | 37 | 7 | 29 | 1 |
| Occupational Health | Health, Safety & Environment | 17 | 38 | 42 | 0 | 39 | 11 | 26 | 2 |
| Safety | Health, Safety & Environment | 1 | 10 | 8 | 0 | 12 | 2 | 9 | 1 |
| Hse Mgr | Health, Safety & Environment | 0 | 0 | 0 | 18 | 10 | 6 | 4 | 0 |
| Occupational Health Lead | Health, Safety & Environment | 0 | 0 | 0 | 10 | 6 | 1 | 5 | 0 |
| Oh | Health, Safety & Environment | 0 | 5 | 7 | 0 | 6 | 0 | 6 | 0 |
| Safety Mgr | Health, Safety & Environment | 0 | 1 | 1 | 6 | 3 | 1 | 2 | 0 |
| Bfp Fire Safety Inspector | Health, Safety & Environment | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Dole-Accredited Safety Practitioner | Health, Safety & Environment | 0 | 2 | 0 | 0 | 2 | 1 | 0 | 1 |
| Ehs | Health, Safety & Environment | 0 | 2 | 3 | 0 | 2 | 1 | 1 | 0 |
| Lgu Health Office | Health, Safety & Environment | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Occupational Health Physician | Health, Safety & Environment | 0 | 2 | 5 | 0 | 2 | 1 | 1 | 0 |
| Pco | Health, Safety & Environment | 0 | 0 | 2 | 2 | 2 | 1 | 1 | 0 |
| Safety Committee Members | Health, Safety & Environment | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Safety Practitioner | Health, Safety & Environment | 0 | 0 | 2 | 0 | 2 | 1 | 0 | 1 |
| Bfp Fire Safety | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Bfp-Accredited Fire Safety Inspector | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Bfp-Accredited Fire Safety Service Provider | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Bfp-Licensed Fire Safety Inspector | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Certified First Aider | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Contractor Safety Officer | Health, Safety & Environment | 0 | 0 | 3 | 0 | 1 | 0 | 0 | 1 |
| Contractor Site Safety Manager | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Dole-Qualified Safety Officer | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Safety Consultant | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Fire Safety | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Fire Safety Inspector | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Fire Safety Officer | Health, Safety & Environment | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Fire Warden | Health, Safety & Environment | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| First Aid Certified Staff | Health, Safety & Environment | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| First-Aid | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| General Contractor Safety Officer | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Hr & Occupational Health | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hse Coordinator | Health, Safety & Environment | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Hse Specialist | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lgu Health | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lgu Health Inspector | Health, Safety & Environment | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Nurse | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Occupational Health Nurse | Health, Safety & Environment | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| Occupational Health Provider | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Osh Officer | Health, Safety & Environment | 0 | 1 | 2 | 2 | 1 | 1 | 0 | 0 |
| Pest Control Vendor Technician | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Safety Committee | Health, Safety & Environment | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Safety Committee Representative | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Safety Inspector | Health, Safety & Environment | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Safety Inspectors | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Trained First-Aider | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Trained First-Aiders Per W501 | Health, Safety & Environment | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vp Hse | Health, Safety & Environment | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Quality | Quality Management | 34 | 172 | 157 | 0 | 190 | 46 | 127 | 17 |
| Service Quality | Quality Management | 23 | 19 | 51 | 0 | 24 | 2 | 19 | 3 |
| Product Compliance Manager | Quality Management | 22 | 24 | 65 | 61 | 24 | 19 | 3 | 2 |
| Product Safety & Compliance Manager | Quality Management | 7 | 0 | 9 | 15 | 10 | 7 | 2 | 1 |
| Quality & Compliance Manager | Quality Management | 2 | 0 | 0 | 0 | 2 | 1 | 1 | 0 |
| Qa | Quality Management | 1 | 1 | 4 | 0 | 4 | 0 | 4 | 0 |
| Standards Lab | Quality Management | 1 | 4 | 5 | 0 | 4 | 0 | 4 | 0 |
| B2B Sourcing Quality Inspector | Quality Management | 1 | 0 | 3 | 4 | 1 | 1 | 0 | 0 |
| Quality Assurance Analyst | Quality Management | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Quality Assurance Engineer | Quality Management | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Quality Coordinator | Quality Management | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Services Quality Inspector | Quality Management | 1 | 1 | 1 | 2 | 1 | 0 | 1 | 0 |
| Services Quality Manager | Quality Management | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Calibration | Quality Management | 0 | 10 | 3 | 0 | 10 | 3 | 7 | 0 |
| Quality Assurance | Quality Management | 0 | 9 | 1 | 0 | 9 | 2 | 3 | 4 |
| Product Safety | Quality Management | 0 | 7 | 10 | 0 | 8 | 5 | 2 | 1 |
| Quality Mgr | Quality Management | 0 | 5 | 6 | 5 | 7 | 0 | 7 | 0 |
| Quality Checker | Quality Management | 0 | 5 | 7 | 0 | 6 | 5 | 1 | 0 |
| Quality Lead | Quality Management | 0 | 0 | 0 | 8 | 6 | 1 | 5 | 0 |
| Product Safety Mgr | Quality Management | 0 | 5 | 0 | 0 | 5 | 5 | 0 | 0 |
| Qc | Quality Management | 0 | 5 | 6 | 0 | 5 | 1 | 4 | 0 |
| Quality Assurance Specialist | Quality Management | 0 | 4 | 0 | 0 | 4 | 2 | 1 | 1 |
| Recall | Quality Management | 0 | 3 | 1 | 0 | 3 | 2 | 1 | 0 |
| Recall Committee | Quality Management | 0 | 1 | 2 | 0 | 3 | 3 | 0 | 0 |
| Quality Team | Quality Management | 0 | 0 | 1 | 1 | 2 | 1 | 0 | 1 |
| Vendor Quality Representative | Quality Management | 0 | 2 | 0 | 0 | 2 | 1 | 0 | 1 |
| Vendor Quality Team | Quality Management | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Coop Quality Lead | Quality Management | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Dc-Qc | Quality Management | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Ecom Quality Coord | Quality Management | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Ecom Quality Coordinator | Quality Management | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| External Calibration Labs | Quality Management | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Factory Quality Team | Quality Management | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lab Tech | Quality Management | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Measurement Technician | Quality Management | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| National Metrology Laboratory | Quality Management | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Procurement Quality Engineer | Quality Management | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| Product Quality Analyst | Quality Management | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Qa Lab Technician | Quality Management | 0 | 1 | 3 | 0 | 1 | 0 | 0 | 1 |
| Quality Assurance Associate | Quality Management | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Quality Check | Quality Management | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Quality Checkers | Quality Management | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Quality Control Inspector | Quality Management | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| Quality Representative | Quality Management | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Recall Assessment Team | Quality Management | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Recall Committee Chair | Quality Management | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Scale Calibration Technician | Quality Management | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Weights & Measures | Quality Management | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Facilities | Facilities & Real Estate | 29 | 146 | 205 | 2 | 173 | 34 | 119 | 20 |
| Real Estate | Facilities & Real Estate | 24 | 73 | 49 | 0 | 79 | 5 | 59 | 15 |
| Housing Ops | Facilities & Real Estate | 22 | 11 | 37 | 0 | 22 | 5 | 16 | 1 |
| Property Manager | Facilities & Real Estate | 17 | 17 | 5 | 30 | 25 | 6 | 17 | 2 |
| Land Liaison Officer | Facilities & Real Estate | 6 | 0 | 24 | 20 | 6 | 2 | 4 | 0 |
| Land Acquisition Manager | Facilities & Real Estate | 5 | 0 | 22 | 22 | 5 | 3 | 2 | 0 |
| Facilities Maintenance Lead | Facilities & Real Estate | 4 | 0 | 10 | 5 | 5 | 1 | 4 | 0 |
| Real Estate Investment Manager | Facilities & Real Estate | 4 | 0 | 0 | 0 | 4 | 0 | 4 | 0 |
| Ifm | Facilities & Real Estate | 3 | 36 | 15 | 0 | 36 | 3 | 31 | 2 |
| Site Cleanup Coordinator | Facilities & Real Estate | 3 | 2 | 18 | 1 | 12 | 5 | 7 | 0 |
| Geodetic Engineer | Facilities & Real Estate | 3 | 7 | 14 | 12 | 9 | 3 | 6 | 0 |
| Site Cleanup Supervisor | Facilities & Real Estate | 3 | 0 | 5 | 10 | 6 | 3 | 3 | 0 |
| Facilities Workplace-Services Lead | Facilities & Real Estate | 3 | 0 | 8 | 3 | 3 | 0 | 3 | 0 |
| Land Acquisition Specialist | Facilities & Real Estate | 3 | 0 | 14 | 8 | 3 | 1 | 2 | 0 |
| Maintenance Manager | Facilities & Real Estate | 3 | 1 | 2 | 0 | 3 | 0 | 1 | 2 |
| Site Managers | Facilities & Real Estate | 2 | 9 | 1 | 0 | 10 | 1 | 7 | 2 |
| Real Estate Manager | Facilities & Real Estate | 2 | 8 | 15 | 2 | 9 | 2 | 5 | 2 |
| Facilities Engineer | Facilities & Real Estate | 2 | 4 | 8 | 1 | 4 | 1 | 2 | 1 |
| Facilities Soft-Services Lead | Facilities & Real Estate | 2 | 0 | 7 | 7 | 3 | 0 | 3 | 0 |
| Facilities & Real Estate Manager | Facilities & Real Estate | 2 | 0 | 0 | 0 | 2 | 1 | 1 | 0 |
| Facilities Project Lead | Facilities & Real Estate | 2 | 0 | 5 | 0 | 2 | 0 | 2 | 0 |
| Property Development Manager | Facilities & Real Estate | 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 |
| Site Cleanup Crew Lead | Facilities & Real Estate | 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 |
| Vp For Engineering & Construction | Facilities & Real Estate | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 2 |
| Construction | Facilities & Real Estate | 1 | 4 | 3 | 0 | 6 | 1 | 5 | 0 |
| Mep Engineer | Facilities & Real Estate | 1 | 1 | 4 | 0 | 5 | 0 | 1 | 4 |
| Head Of Engineering | Facilities & Real Estate | 1 | 4 | 1 | 4 | 4 | 0 | 3 | 1 |
| Employee Accommodation | Facilities & Real Estate | 1 | 2 | 0 | 0 | 3 | 0 | 3 | 0 |
| Facilities Soft | Facilities & Real Estate | 1 | 0 | 1 | 0 | 2 | 0 | 2 | 0 |
| Facilities Tech Lead | Facilities & Real Estate | 1 | 0 | 6 | 1 | 2 | 0 | 0 | 2 |
| Green Building | Facilities & Real Estate | 1 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Hard-Services Lead | Facilities & Real Estate | 1 | 0 | 1 | 0 | 2 | 0 | 2 | 0 |
| Warden | Facilities & Real Estate | 1 | 0 | 3 | 0 | 2 | 0 | 2 | 0 |
| Contractor Safety Manager | Facilities & Real Estate | 1 | 0 | 1 | 4 | 1 | 0 | 1 | 0 |
| Dc Facilities Manager | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Demolition | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Dormitory Warden | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Engineering & Director, Facilities & Real Estate | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Facilities & Construction | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Facilities & Hse | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Facilities Asset Manager | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Facilities Av Lead | Facilities & Real Estate | 1 | 0 | 1 | 2 | 1 | 0 | 1 | 0 |
| Facilities Compliance Lead | Facilities & Real Estate | 1 | 0 | 3 | 2 | 1 | 0 | 1 | 0 |
| Facilities Engineering Lead | Facilities & Real Estate | 1 | 0 | 2 | 4 | 1 | 1 | 0 | 0 |
| Facilities Engineering Specialist | Facilities & Real Estate | 1 | 0 | 1 | 4 | 1 | 0 | 1 | 0 |
| Facilities Helpdesk | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Facilities Security Coordinator | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Facilities Site Coordinator | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Facilities Sustainability Lead | Facilities & Real Estate | 1 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Facilities Technology Lead | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Fleet & Facilities | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| House Parent | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Housing Portfolio | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hq Facilities Manager | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Mailroom | Facilities & Real Estate | 1 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Mro | Facilities & Real Estate | 1 | 1 | 3 | 2 | 1 | 0 | 1 | 0 |
| Property Compliance Manager | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Real Estate Compliance | Facilities & Real Estate | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Renewable Program | Facilities & Real Estate | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Transport Helpdesk | Facilities & Real Estate | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Facilities & Real Estate | Facilities & Real Estate | 0 | 26 | 35 | 128 | 60 | 10 | 40 | 10 |
| Engineering | Facilities & Real Estate | 0 | 27 | 21 | 0 | 30 | 5 | 17 | 8 |
| Property Mgr | Facilities & Real Estate | 0 | 5 | 40 | 3 | 21 | 5 | 15 | 1 |
| Housing Ops Lead | Facilities & Real Estate | 0 | 0 | 0 | 29 | 14 | 3 | 11 | 0 |
| Lgu Building Official | Facilities & Real Estate | 0 | 8 | 0 | 0 | 8 | 5 | 1 | 2 |
| Solar Sales Coord | Facilities & Real Estate | 0 | 7 | 1 | 0 | 7 | 1 | 6 | 0 |
| Store Design Mgr | Facilities & Real Estate | 0 | 7 | 0 | 0 | 7 | 0 | 4 | 3 |
| Ifm Lead | Facilities & Real Estate | 0 | 0 | 0 | 7 | 6 | 1 | 5 | 0 |
| Maintenance Technician | Facilities & Real Estate | 0 | 3 | 6 | 0 | 5 | 2 | 3 | 0 |
| Real Estate Investment Mgr | Facilities & Real Estate | 0 | 5 | 4 | 0 | 5 | 0 | 5 | 0 |
| Renewable | Facilities & Real Estate | 0 | 4 | 3 | 0 | 5 | 0 | 5 | 0 |
| Facilities Lead | Facilities & Real Estate | 0 | 0 | 0 | 6 | 4 | 0 | 4 | 0 |
| Facilities Maintenance | Facilities & Real Estate | 0 | 4 | 4 | 2 | 4 | 1 | 3 | 0 |
| Accommodation | Facilities & Real Estate | 0 | 1 | 5 | 0 | 3 | 0 | 3 | 0 |
| Facilities Tech | Facilities & Real Estate | 0 | 0 | 4 | 0 | 3 | 0 | 2 | 1 |
| O&M | Facilities & Real Estate | 0 | 2 | 2 | 0 | 3 | 0 | 3 | 0 |
| Property | Facilities & Real Estate | 0 | 3 | 3 | 0 | 3 | 0 | 2 | 1 |
| Re | Facilities & Real Estate | 0 | 0 | 3 | 0 | 3 | 0 | 3 | 0 |
| Solar Installer | Facilities & Real Estate | 0 | 2 | 3 | 0 | 3 | 0 | 3 | 0 |
| Waste Mgmt | Facilities & Real Estate | 0 | 3 | 2 | 0 | 3 | 1 | 1 | 1 |
| Bms | Facilities & Real Estate | 0 | 2 | 2 | 0 | 2 | 0 | 0 | 2 |
| Charging Ops | Facilities & Real Estate | 0 | 2 | 2 | 0 | 2 | 1 | 0 | 1 |
| Construction Contractor | Facilities & Real Estate | 0 | 1 | 3 | 0 | 2 | 1 | 1 | 0 |
| Construction Manager | Facilities & Real Estate | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Construction Mgr | Facilities & Real Estate | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| Energy Analyst | Facilities & Real Estate | 0 | 0 | 4 | 0 | 2 | 0 | 2 | 0 |
| Evse Technician | Facilities & Real Estate | 0 | 2 | 1 | 0 | 2 | 1 | 1 | 0 |
| External Energy Auditor | Facilities & Real Estate | 0 | 1 | 2 | 0 | 2 | 0 | 0 | 2 |
| External Real Estate Broker | Facilities & Real Estate | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| Facilities & Real Estate & Land Acquisition | Facilities & Real Estate | 0 | 0 | 8 | 8 | 2 | 0 | 2 | 0 |
| Facilities Standards Manager | Facilities & Real Estate | 0 | 1 | 2 | 0 | 2 | 1 | 1 | 0 |
| Facilities Technician | Facilities & Real Estate | 0 | 1 | 3 | 0 | 2 | 0 | 2 | 0 |
| Maintenance Technicians | Facilities & Real Estate | 0 | 2 | 1 | 0 | 2 | 0 | 1 | 1 |
| Property Dev Mgr | Facilities & Real Estate | 0 | 1 | 3 | 0 | 2 | 0 | 2 | 0 |
| Property Mgr Inc | Facilities & Real Estate | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| Real Estate Mgr | Facilities & Real Estate | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Scrap Buyer | Facilities & Real Estate | 0 | 1 | 1 | 0 | 2 | 0 | 1 | 1 |
| Solar O&M | Facilities & Real Estate | 0 | 1 | 3 | 0 | 2 | 0 | 2 | 0 |
| Tsd Facility | Facilities & Real Estate | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Accredited Scrap Buyer | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Base-Building Facilities | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Buildright Property Management | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Buildright Property Management Inc | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Cafeteria | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Charge Ops Supervisor | Facilities & Real Estate | 0 | 0 | 4 | 0 | 1 | 0 | 1 | 0 |
| City Zoning Board | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Comfort | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Construction Pmo | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Construction Worker | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Corporate Housing Coordinator | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Denr-Certified E-Waste Vendor | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Denr-Certified Hazardous Waste Vendor | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Disposal Facility | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Doe-Accredited Energy Auditor | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| E-Waste Recycler Partner | Facilities & Real Estate | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Energy Consultant | Facilities & Real Estate | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Entity Facilities | Facilities & Real Estate | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Ev | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ev Channel Owners | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Evse Vendor | Facilities & Real Estate | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Evse Vendors | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Maintenance Contractor | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| External Solar Provider | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Facilities & Energy | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Facilities & Maintenance | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Facilities Analyst | Facilities & Real Estate | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Facilities Asset Mgr | Facilities & Real Estate | 0 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Facilities Security Coord | Facilities & Real Estate | 0 | 0 | 2 | 1 | 1 | 0 | 1 | 0 |
| Facilities Site Coord | Facilities & Real Estate | 0 | 0 | 3 | 3 | 1 | 0 | 1 | 0 |
| Facilities Standards Mgr | Facilities & Real Estate | 0 | 0 | 7 | 0 | 1 | 1 | 0 | 0 |
| Facilities Team | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Housekeeping | Facilities & Real Estate | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Ifm Manager | Facilities & Real Estate | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Junk Shop Owners | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Landscaping Vendor | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lease Admin Mgr | Facilities & Real Estate | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| Lgu Building Inspector | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lgu Solid Waste Management Board | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lgu Zoning Administrator | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Local Zoning Board Of Appeals | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Maint Mgr | Facilities & Real Estate | 0 | 0 | 6 | 0 | 1 | 0 | 0 | 1 |
| Maint Supervisor | Facilities & Real Estate | 0 | 0 | 2 | 1 | 1 | 0 | 1 | 0 |
| Maintenance Analyst | Facilities & Real Estate | 0 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Maintenance Engineer | Facilities & Real Estate | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Maintenance Mgr | Facilities & Real Estate | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| Maintenance Team | Facilities & Real Estate | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Maintenance Vendor | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Municipal Building Official | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Partner Waste Hauler | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Property Acquisition Manager | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Property Admin | Facilities & Real Estate | 0 | 1 | 5 | 0 | 1 | 0 | 1 | 0 |
| Property Mgmt | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Real Estate Controller | Facilities & Real Estate | 0 | 0 | 3 | 3 | 1 | 0 | 1 | 0 |
| Real Estate Team | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Recycling Partners | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Recycling Plant Owners | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Recycling Vendor | Facilities & Real Estate | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Recycling Vendors | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Renewable Ops | Facilities & Real Estate | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Scrap | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Scrap Collector | Facilities & Real Estate | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Scrap Dealer | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Scrap Metal Collector | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Scrap Vendor | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Solar | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Solar Epc | Facilities & Real Estate | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Solar Epc Contractor | Facilities & Real Estate | 0 | 1 | 2 | 0 | 1 | 0 | 0 | 1 |
| Solar Ops | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Solar Vendor | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Solar Vendor Trainers | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Store Design Architect | Facilities & Real Estate | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Store Maintenance Staff | Facilities & Real Estate | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Vendor Maintenance | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vp Construction | Facilities & Real Estate | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Vs-138 Facilities | Facilities & Real Estate | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Vs-73 Abatement | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Vs-73 Asbestos | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Waste Collectors | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Waste Hauler Vendor | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Waste Management | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Waste Management Contractor | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Waste Management Partner | Facilities & Real Estate | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Waste Vendor | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Zoning Officer | Facilities & Real Estate | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Sustainability | Sustainability / ESG | 49 | 82 | 160 | 35 | 99 | 13 | 61 | 25 |
| Foundation Ed | Sustainability / ESG | 22 | 1 | 45 | 17 | 24 | 4 | 18 | 2 |
| Esg | Sustainability / ESG | 7 | 45 | 36 | 5 | 51 | 6 | 31 | 14 |
| Circular | Sustainability / ESG | 1 | 2 | 4 | 0 | 4 | 0 | 3 | 1 |
| Circular Lead | Sustainability / ESG | 1 | 0 | 1 | 1 | 3 | 0 | 2 | 1 |
| M&E | Sustainability / ESG | 1 | 1 | 5 | 0 | 3 | 0 | 2 | 1 |
| Circular-Economy Lead | Sustainability / ESG | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Csr Foundation Manager | Sustainability / ESG | 1 | 0 | 4 | 4 | 1 | 0 | 1 | 0 |
| Foundation Executive Director | Sustainability / ESG | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| M&E Lead | Sustainability / ESG | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sustainability Officer | Sustainability / ESG | 0 | 4 | 6 | 0 | 4 | 0 | 1 | 3 |
| Board Esg Committee | Sustainability / ESG | 0 | 1 | 0 | 5 | 3 | 0 | 1 | 2 |
| Csr Foundation | Sustainability / ESG | 0 | 3 | 0 | 0 | 3 | 2 | 1 | 0 |
| Environmental | Sustainability / ESG | 0 | 3 | 0 | 0 | 3 | 2 | 1 | 0 |
| Esg Coordinator | Sustainability / ESG | 0 | 1 | 9 | 1 | 3 | 0 | 1 | 2 |
| External Sustainability Auditor | Sustainability / ESG | 0 | 3 | 0 | 0 | 3 | 1 | 1 | 1 |
| Sustainability Committee | Sustainability / ESG | 0 | 1 | 0 | 2 | 3 | 0 | 2 | 1 |
| Csr Team | Sustainability / ESG | 0 | 1 | 1 | 0 | 2 | 0 | 1 | 1 |
| Environmental Officer | Sustainability / ESG | 0 | 1 | 1 | 0 | 2 | 1 | 0 | 1 |
| Esg Analyst | Sustainability / ESG | 0 | 0 | 6 | 0 | 2 | 0 | 0 | 2 |
| Esg Committee | Sustainability / ESG | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 2 |
| External Carbon Verification Auditor | Sustainability / ESG | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| Foundation | Sustainability / ESG | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Foundation Board Programs Committee | Sustainability / ESG | 0 | 0 | 0 | 2 | 2 | 0 | 2 | 0 |
| Human Rights | Sustainability / ESG | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Human-Rights Dd | Sustainability / ESG | 0 | 1 | 2 | 0 | 2 | 0 | 2 | 0 |
| Sustainability Team | Sustainability / ESG | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| Board Csr Committee | Sustainability / ESG | 0 | 0 | 0 | 3 | 1 | 0 | 1 | 0 |
| Community | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Community Group | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Community Leaders | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Csr Coord | Sustainability / ESG | 0 | 0 | 2 | 2 | 1 | 0 | 0 | 1 |
| Csr Foundation Team | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Csr Lead | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Csr Mgr | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Denr Environmental Management Bureau | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Environmental Eng | Sustainability / ESG | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Environmental Engineer | Sustainability / ESG | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Environmental Engr | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Esg Mgr | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Esg Reporting | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Esg Reporting Analyst | Sustainability / ESG | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| External Environmental Auditor | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| External Esg Advisors | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Esg Auditor | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Sustainability Advisor | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Foundation Director | Sustainability / ESG | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Head Of Esg | Sustainability / ESG | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 |
| Indigenous Community Representatives | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Indigenous Cultural Community Tribal Council | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Local Community | Sustainability / ESG | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vp Esg | Sustainability / ESG | 0 | 1 | 0 | 3 | 1 | 0 | 0 | 1 |
| Strategy | Strategy / Corporate Planning | 26 | 128 | 138 | 0 | 148 | 8 | 89 | 51 |
| Head Of Corporate Development | Strategy / Corporate Planning | 17 | 0 | 0 | 0 | 17 | 0 | 16 | 1 |
| Programs | Strategy / Corporate Planning | 7 | 5 | 24 | 0 | 13 | 1 | 11 | 1 |
| Innovation | Strategy / Corporate Planning | 4 | 24 | 13 | 0 | 24 | 1 | 11 | 12 |
| Corp Dev | Strategy / Corporate Planning | 2 | 22 | 55 | 0 | 25 | 2 | 22 | 1 |
| Sponsor | Strategy / Corporate Planning | 1 | 20 | 16 | 43 | 37 | 0 | 32 | 5 |
| Executive Sponsor | Strategy / Corporate Planning | 1 | 3 | 0 | 3 | 5 | 0 | 5 | 0 |
| Project Sponsor | Strategy / Corporate Planning | 1 | 3 | 1 | 0 | 4 | 1 | 2 | 1 |
| Transformation | Strategy / Corporate Planning | 1 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Sponsors | Strategy / Corporate Planning | 0 | 12 | 0 | 0 | 12 | 0 | 9 | 3 |
| Pro-Referral Network Manager | Trade / Account Management | 24 | 0 | 0 | 0 | 24 | 1 | 21 | 2 |
| Account Manager | Trade / Account Management | 21 | 36 | 80 | 3 | 46 | 2 | 35 | 9 |
| Commercial | Trade / Account Management | 21 | 3 | 35 | 0 | 25 | 3 | 18 | 4 |
| Trade Sales Manager | Trade / Account Management | 16 | 16 | 49 | 29 | 42 | 9 | 28 | 5 |
| Trade Sales | Trade / Account Management | 12 | 52 | 50 | 0 | 64 | 13 | 47 | 4 |
| Msme Sales Manager | Trade / Account Management | 11 | 0 | 0 | 30 | 16 | 2 | 14 | 0 |
| Trade Sales Representative | Trade / Account Management | 10 | 1 | 0 | 0 | 11 | 1 | 9 | 1 |
| Sales Operations | Trade / Account Management | 9 | 1 | 1 | 0 | 10 | 0 | 8 | 2 |
| Head Of Strategic Accounts | Trade / Account Management | 8 | 8 | 15 | 45 | 23 | 0 | 17 | 6 |
| B2B Sales Manager | Trade / Account Management | 8 | 8 | 28 | 19 | 10 | 1 | 8 | 1 |
| Solar Sales Coordinator | Trade / Account Management | 7 | 3 | 20 | 3 | 10 | 1 | 9 | 0 |
| Field Sales Rep | Trade / Account Management | 6 | 0 | 18 | 0 | 7 | 0 | 7 | 0 |
| Trade | Trade / Account Management | 5 | 57 | 19 | 0 | 63 | 8 | 49 | 6 |
| B2B Sourcing Manager | Trade / Account Management | 4 | 8 | 18 | 16 | 12 | 0 | 11 | 1 |
| Project Design | Trade / Account Management | 4 | 5 | 5 | 0 | 9 | 1 | 8 | 0 |
| Account Management | Trade / Account Management | 3 | 4 | 5 | 28 | 27 | 2 | 18 | 7 |
| Installation | Trade / Account Management | 3 | 12 | 6 | 0 | 15 | 2 | 13 | 0 |
| Field Sales | Trade / Account Management | 3 | 8 | 8 | 0 | 10 | 1 | 9 | 0 |
| Project Estimator | Trade / Account Management | 3 | 4 | 18 | 0 | 4 | 0 | 2 | 2 |
| Trade Marketing Manager | Trade / Account Management | 3 | 0 | 10 | 1 | 3 | 0 | 3 | 0 |
| Head Of Trade / Account Management | Trade / Account Management | 2 | 24 | 1 | 66 | 55 | 4 | 39 | 12 |
| Sales Ops | Trade / Account Management | 2 | 8 | 38 | 0 | 24 | 0 | 16 | 8 |
| Sales Manager | Trade / Account Management | 2 | 13 | 25 | 9 | 17 | 5 | 11 | 1 |
| Government Sales | Trade / Account Management | 2 | 5 | 4 | 0 | 7 | 0 | 6 | 1 |
| Trade Program | Trade / Account Management | 2 | 6 | 5 | 0 | 7 | 0 | 6 | 1 |
| Project Sales | Trade / Account Management | 2 | 1 | 0 | 0 | 3 | 1 | 2 | 0 |
| Trade Marketing | Trade / Account Management | 2 | 1 | 1 | 0 | 3 | 0 | 3 | 0 |
| B2B Technical Support | Trade / Account Management | 2 | 0 | 8 | 8 | 2 | 0 | 2 | 0 |
| Field Sales Ops | Trade / Account Management | 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 |
| Project Sales Manager | Trade / Account Management | 2 | 1 | 0 | 0 | 2 | 0 | 1 | 1 |
| Vp Trade Sales | Trade / Account Management | 2 | 0 | 0 | 1 | 2 | 0 | 2 | 0 |
| Sales | Trade / Account Management | 1 | 13 | 15 | 1 | 20 | 3 | 17 | 0 |
| B2B | Trade / Account Management | 1 | 7 | 3 | 0 | 8 | 2 | 6 | 0 |
| Master Tradespersons | Trade / Account Management | 1 | 8 | 6 | 0 | 8 | 0 | 7 | 1 |
| Apprenticeship | Trade / Account Management | 1 | 3 | 1 | 0 | 4 | 0 | 4 | 0 |
| B2G Sales | Trade / Account Management | 1 | 3 | 0 | 0 | 4 | 2 | 2 | 0 |
| Trade-Pro Program | Trade / Account Management | 1 | 2 | 0 | 0 | 3 | 0 | 3 | 0 |
| B2B Vp | Trade / Account Management | 1 | 1 | 4 | 4 | 2 | 0 | 2 | 0 |
| Bid Manager | Trade / Account Management | 1 | 1 | 6 | 0 | 2 | 0 | 2 | 0 |
| Sales Coordinator | Trade / Account Management | 1 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Services Dispatch Coordinator | Trade / Account Management | 1 | 1 | 5 | 1 | 2 | 1 | 1 | 0 |
| Bid & Tender Manager | Trade / Account Management | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Commercial Leadership | Trade / Account Management | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Commercial Operations | Trade / Account Management | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Corporate Sales Manager | Trade / Account Management | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Customer Site Coordinator | Trade / Account Management | 1 | 0 | 3 | 4 | 1 | 0 | 1 | 0 |
| Estimating Specialist | Trade / Account Management | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Installation Services | Trade / Account Management | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Msme Operations Manager | Trade / Account Management | 1 | 0 | 0 | 3 | 1 | 0 | 1 | 0 |
| Project Sales Lead | Trade / Account Management | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sales Operations Manager | Trade / Account Management | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sales Technology | Trade / Account Management | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Trade & Institutional Sales Manager | Trade / Account Management | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Trade Pro & Services | Trade / Account Management | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| B2B Sales | Trade / Account Management | 0 | 21 | 8 | 0 | 22 | 3 | 16 | 3 |
| Trade Capability Lead | Trade / Account Management | 0 | 0 | 0 | 60 | 22 | 4 | 15 | 3 |
| Trade Sales Rep | Trade / Account Management | 0 | 18 | 34 | 0 | 22 | 1 | 19 | 2 |
| Msme Sales | Trade / Account Management | 0 | 19 | 16 | 0 | 19 | 2 | 16 | 1 |
| Trade Sales Mgr | Trade / Account Management | 0 | 12 | 3 | 1 | 14 | 1 | 12 | 1 |
| Key Account | Trade / Account Management | 0 | 11 | 4 | 0 | 11 | 1 | 8 | 2 |
| B2G | Trade / Account Management | 0 | 10 | 2 | 0 | 10 | 3 | 6 | 1 |
| Sales Representative | Trade / Account Management | 0 | 9 | 16 | 3 | 9 | 4 | 5 | 0 |
| Trade Professional | Trade / Account Management | 0 | 8 | 1 | 0 | 8 | 0 | 8 | 0 |
| Trade Specialists | Trade / Account Management | 0 | 7 | 3 | 0 | 8 | 0 | 8 | 0 |
| Account Managers | Trade / Account Management | 0 | 6 | 0 | 0 | 6 | 0 | 4 | 2 |
| Trade Professionals | Trade / Account Management | 0 | 5 | 0 | 0 | 5 | 0 | 5 | 0 |
| Account Mgr | Trade / Account Management | 0 | 1 | 7 | 0 | 4 | 0 | 3 | 1 |
| Am | Trade / Account Management | 0 | 0 | 5 | 0 | 4 | 0 | 4 | 0 |
| Account | Trade / Account Management | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| B2B Sales Mgr | Trade / Account Management | 0 | 0 | 1 | 3 | 3 | 0 | 0 | 3 |
| Master Associates | Trade / Account Management | 0 | 3 | 3 | 0 | 3 | 0 | 3 | 0 |
| Trade Specialist | Trade / Account Management | 0 | 0 | 3 | 0 | 3 | 0 | 3 | 0 |
| Account Director | Trade / Account Management | 0 | 0 | 0 | 3 | 2 | 0 | 2 | 0 |
| B2B Controller | Trade / Account Management | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| B2B Sales Rep | Trade / Account Management | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Carrier Account Manager | Trade / Account Management | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Isp Account Managers | Trade / Account Management | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Partner Account Manager | Trade / Account Management | 0 | 2 | 2 | 0 | 2 | 1 | 1 | 0 |
| Pro Representatives | Trade / Account Management | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Project Sales Mgr | Trade / Account Management | 0 | 0 | 2 | 5 | 2 | 0 | 1 | 1 |
| Trade Account Customer | Trade / Account Management | 0 | 2 | 0 | 0 | 2 | 1 | 0 | 1 |
| Trade Credit Insurer | Trade / Account Management | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Trade Manager | Trade / Account Management | 0 | 0 | 0 | 2 | 2 | 0 | 2 | 0 |
| Vendor Account Mgr | Trade / Account Management | 0 | 0 | 2 | 1 | 2 | 0 | 2 | 0 |
| Vp For Sales | Trade / Account Management | 0 | 2 | 2 | 4 | 2 | 0 | 2 | 0 |
| Account Contact | Trade / Account Management | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Account Management & Operations | Trade / Account Management | 0 | 0 | 0 | 4 | 1 | 0 | 1 | 0 |
| Accounts Receivable | Trade / Account Management | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Accounts Receivable Clerk | Trade / Account Management | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Agency Account Manager | Trade / Account Management | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| B2B Account Managers | Trade / Account Management | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| B2B Portal Admin | Trade / Account Management | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 |
| B2B Sales Vp | Trade / Account Management | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Business Dev | Trade / Account Management | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Carrier Account Managers | Trade / Account Management | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Contractor Account Manager | Trade / Account Management | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Kam | Trade / Account Management | 0 | 0 | 5 | 2 | 1 | 0 | 1 | 0 |
| Key Account Vendors | Trade / Account Management | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Marketplace Account Manager | Trade / Account Management | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Quotation Specialist | Trade / Account Management | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sales Ops Mgr | Trade / Account Management | 0 | 0 | 1 | 3 | 1 | 0 | 1 | 0 |
| Trade Area | Trade / Account Management | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Trade Association Partners | Trade / Account Management | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Trade Leadership | Trade / Account Management | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Trade Sales Vp | Trade / Account Management | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vmi Vendor Account Manager | Trade / Account Management | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vp Commercial | Trade / Account Management | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Wholesale Manager | Trade / Account Management | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Global Sourcing | Merchandising & Buying (Direct Sourcing) | 25 | 35 | 73 | 0 | 36 | 5 | 27 | 4 |
| Project Manager | Strategy / Corporate Planning (PMO) | 18 | 36 | 73 | 15 | 47 | 2 | 37 | 8 |
| Ecommerce | Digital Commerce (IT-built platforms) | 15 | 116 | 60 | 0 | 128 | 31 | 81 | 16 |
| Regulatory Officer | Regulatory Affairs Specialist | 10 | 24 | 78 | 11 | 35 | 20 | 14 | 1 |
| Tax | Finance & Accounting (Tax) | 9 | 84 | 76 | 0 | 96 | 33 | 60 | 3 |
| Master Data | Merchandising & Buying (Master Data) | 9 | 40 | 36 | 0 | 49 | 16 | 32 | 1 |
| Data Science | DP Data Scientist / ML | 8 | 34 | 39 | 0 | 37 | 13 | 16 | 8 |
| Gm, Digital Commerce Inc | Digital Commerce (IT-built platforms) | 6 | 0 | 0 | 0 | 6 | 0 | 4 | 2 |
| Department Head | Generic / cross-department | 5 | 27 | 31 | 24 | 50 | 15 | 29 | 6 |
| Ecommerce Operations | Digital Commerce (IT-built platforms) | 5 | 9 | 3 | 12 | 14 | 2 | 10 | 2 |
| Digital | Digital Commerce (IT-built platforms) | 5 | 12 | 10 | 0 | 13 | 0 | 12 | 1 |
| Loyalty | Marketing (Loyalty) | 4 | 56 | 26 | 0 | 56 | 15 | 30 | 11 |
| Payroll | Human Resources (Payroll) | 4 | 43 | 46 | 1 | 49 | 16 | 33 | 0 |
| Department Heads | Generic / cross-department | 4 | 33 | 15 | 3 | 44 | 15 | 22 | 7 |
| Cross-Entity | Generic / cross-department | 3 | 9 | 12 | 0 | 14 | 6 | 7 | 1 |
| Requesting Department Head | Generic / cross-department | 3 | 3 | 0 | 0 | 5 | 2 | 2 | 1 |
| E-Commerce Operations Manager | Digital Commerce (IT-built platforms) | 3 | 1 | 3 | 1 | 3 | 2 | 0 | 1 |
| Ecommerce Merchandiser | Digital Commerce (IT-built platforms) | 3 | 3 | 6 | 4 | 3 | 0 | 0 | 3 |
| Ecommerce Product Manager | Digital Commerce (IT-built platforms) | 3 | 2 | 4 | 1 | 3 | 0 | 2 | 1 |
| Program Manager | Strategy / Corporate Planning (PMO) | 2 | 2 | 61 | 40 | 33 | 2 | 28 | 3 |
| App | Digital Commerce (IT-built platforms) | 2 | 10 | 6 | 1 | 11 | 1 | 10 | 0 |
| Cross-Entity Shared Services | Generic / cross-department | 2 | 8 | 1 | 0 | 8 | 4 | 4 | 0 |
| Pim | Merchandising & Buying (Master Data) | 2 | 5 | 3 | 0 | 6 | 0 | 6 | 0 |
| Digital Analytics Manager | Digital Commerce (IT-built platforms) | 2 | 3 | 6 | 0 | 4 | 0 | 2 | 2 |
| Ecommerce Content Manager | Digital Commerce (IT-built platforms) | 2 | 2 | 5 | 3 | 4 | 0 | 3 | 1 |
| Director Of Construction Pmo | Strategy / Corporate Planning (PMO) | 2 | 1 | 8 | 8 | 3 | 1 | 2 | 0 |
| Adverse-Action Review Board | Generic / cross-department | 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 |
| Ecommerce Catalog Manager | Digital Commerce (IT-built platforms) | 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 |
| Ecommerce Content Moderator | Digital Commerce (IT-built platforms) | 2 | 2 | 3 | 0 | 2 | 0 | 2 | 0 |
| Tax Technology Lead | Finance & Accounting (Tax) | 2 | 0 | 0 | 1 | 2 | 2 | 0 | 0 |
| Unified Order Management Engine | Generic / cross-department | 2 | 1 | 0 | 0 | 2 | 2 | 0 | 0 |
| Govt Affairs | Government Affairs Manager | 1 | 35 | 47 | 0 | 37 | 7 | 28 | 2 |
| Domain Owners | Generic / cross-department | 1 | 18 | 25 | 0 | 27 | 2 | 20 | 5 |
| Supervisor | Generic / cross-department | 1 | 5 | 23 | 23 | 25 | 6 | 16 | 3 |
| Ecommerce Ops | Digital Commerce (IT-built platforms) | 1 | 13 | 20 | 5 | 23 | 6 | 15 | 2 |
| Business Ai Owners | AAP AI-Governance Liaison | 1 | 18 | 0 | 0 | 18 | 10 | 6 | 2 |
| Manager | Generic / cross-department | 1 | 3 | 17 | 4 | 16 | 5 | 8 | 3 |
| Foundation Board | Generic / cross-department | 1 | 0 | 0 | 25 | 14 | 2 | 11 | 1 |
| Principals | Generic / cross-department | 1 | 8 | 6 | 0 | 9 | 5 | 4 | 0 |
| Requestor | Generic / cross-department | 1 | 2 | 14 | 1 | 9 | 7 | 1 | 1 |
| Transformation Board | Generic / cross-department | 1 | 1 | 1 | 7 | 8 | 0 | 8 | 0 |
| Contract Owner | Generic / cross-department | 1 | 4 | 12 | 5 | 5 | 0 | 4 | 1 |
| Project Mgmt | Strategy / Corporate Planning (PMO) | 1 | 3 | 2 | 0 | 4 | 1 | 3 | 0 |
| Captive Board Audit Committee | Generic / cross-department | 1 | 0 | 0 | 4 | 3 | 0 | 3 | 0 |
| Crisis Management Team | Generic / cross-department | 1 | 1 | 0 | 0 | 2 | 0 | 0 | 2 |
| E-Commerce Content Manager | Digital Commerce (IT-built platforms) | 1 | 1 | 0 | 0 | 2 | 0 | 1 | 1 |
| Ecommerce Fulfillment | Digital Commerce (IT-built platforms) | 1 | 1 | 0 | 0 | 2 | 0 | 1 | 1 |
| Evaluation | Generic / cross-department | 1 | 2 | 0 | 5 | 2 | 0 | 2 | 0 |
| Resource Owners | Generic / cross-department | 1 | 1 | 0 | 0 | 2 | 0 | 2 | 0 |
| Accessibility Lead | Digital Commerce (IT-built platforms) | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Approver Per Doa Matrix | Generic / cross-department | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| B2B E-Commerce Manager | Digital Commerce (IT-built platforms) | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| Captive Board Investment Committee | Generic / cross-department | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Captive Board Underwriting Committee | Generic / cross-department | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Construction Pmo Leader | Strategy / Corporate Planning (PMO) | 1 | 0 | 3 | 4 | 1 | 0 | 1 | 0 |
| Customer Communication System | Generic / cross-department | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Dc & Store Operations | Generic / cross-department | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Department Lead | Generic / cross-department | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Document Owner | Generic / cross-department | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 |
| E-Commerce Operations Supervisor | Digital Commerce (IT-built platforms) | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Ecommerce Catalog Specialist | Digital Commerce (IT-built platforms) | 1 | 1 | 3 | 1 | 1 | 0 | 1 | 0 |
| Ecommerce Fulfillment Coordinator | Digital Commerce (IT-built platforms) | 1 | 1 | 1 | 2 | 1 | 0 | 1 | 0 |
| Ecommerce Fulfillment Manager | Digital Commerce (IT-built platforms) | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Ecommerce Logistics Coordinator | Digital Commerce (IT-built platforms) | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Ecommerce Logistics Manager | Digital Commerce (IT-built platforms) | 1 | 0 | 4 | 1 | 1 | 1 | 0 | 0 |
| Ecommerce Marketplace | Digital Commerce (IT-built platforms) | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ecommerce Operations Specialist | Digital Commerce (IT-built platforms) | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Ecommerce Quality Coordinator | Digital Commerce (IT-built platforms) | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Engaging Department Head | Generic / cross-department | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Head Of Digital Commerce | Digital Commerce (IT-built platforms) | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hq Function Manager | Generic / cross-department | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Incident Owner | Generic / cross-department | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Installation Services Manager | Services Manager | 1 | 0 | 5 | 0 | 1 | 0 | 0 | 1 |
| Jv Gm | Generic / cross-department | 1 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Loyalty-Gift-Card | Marketing (Loyalty) | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Order Mgmt | Digital Commerce (IT-built platforms) | 1 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Program Operations Lead | Strategy / Corporate Planning (PMO) | 1 | 0 | 3 | 4 | 1 | 0 | 1 | 0 |
| Project Document Controller | Strategy / Corporate Planning (PMO) | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Respective Department Heads | Generic / cross-department | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| User Department Head | Generic / cross-department | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Director | Generic / cross-department | 0 | 26 | 43 | 130 | 62 | 10 | 42 | 10 |
| Digital Commerce Inc | Digital Commerce (IT-built platforms) | 0 | 9 | 7 | 74 | 54 | 8 | 34 | 12 |
| Gm | Generic / cross-department | 0 | 7 | 7 | 74 | 52 | 7 | 33 | 12 |
| Vp Merch | VP for Merchandising | 0 | 10 | 3 | 48 | 41 | 2 | 27 | 12 |
| Business Owners | Generic / cross-department | 0 | 21 | 12 | 0 | 28 | 5 | 18 | 5 |
| Process Owners | OpEx / Continuous-Improvement Process Lead | 0 | 18 | 13 | 4 | 26 | 4 | 14 | 8 |
| Approver | Generic / cross-department | 0 | 0 | 27 | 12 | 23 | 13 | 7 | 3 |
| Affected Business Unit | Generic / cross-department | 0 | 20 | 0 | 0 | 20 | 3 | 17 | 0 |
| Leadership | Generic / cross-department | 0 | 15 | 11 | 0 | 19 | 0 | 14 | 5 |
| Dept Head | Generic / cross-department | 0 | 0 | 9 | 16 | 18 | 6 | 8 | 4 |
| Channel Owners | Generic / cross-department | 0 | 16 | 2 | 0 | 16 | 7 | 6 | 3 |
| Managers | Generic / cross-department | 0 | 16 | 6 | 0 | 16 | 0 | 16 | 0 |
| Dark Store Ops Mgr | Digital Commerce (IT-built platforms) | 0 | 13 | 3 | 0 | 14 | 3 | 8 | 3 |
| Ecom Ops Manager | Digital Commerce (IT-built platforms) | 0 | 12 | 5 | 9 | 13 | 3 | 9 | 1 |
| Pim Owner | Generic / cross-department | 0 | 0 | 16 | 18 | 13 | 0 | 13 | 0 |
| User Dept | Generic / cross-department | 0 | 12 | 14 | 0 | 13 | 2 | 10 | 1 |
| Hiring Manager | Generic / cross-department | 0 | 9 | 6 | 5 | 11 | 4 | 6 | 1 |
| Mobile App | Digital Commerce (IT-built platforms) | 0 | 11 | 0 | 0 | 11 | 1 | 8 | 2 |
| Director Ecommerce | Digital Commerce (IT-built platforms) | 0 | 0 | 0 | 23 | 10 | 0 | 8 | 2 |
| Business Process Owners | Generic / cross-department | 0 | 9 | 1 | 0 | 9 | 4 | 0 | 5 |
| Seller Operations | Generic / cross-department | 0 | 9 | 9 | 0 | 9 | 1 | 7 | 1 |
| Affected Business Units | Generic / cross-department | 0 | 8 | 0 | 0 | 8 | 0 | 8 | 0 |
| Business Owner | Generic / cross-department | 0 | 7 | 4 | 2 | 8 | 1 | 6 | 1 |
| Project | Strategy / Corporate Planning (PMO) | 0 | 7 | 3 | 0 | 8 | 0 | 8 | 0 |
| Digital Product Mgr | Digital Commerce (IT-built platforms) | 0 | 7 | 0 | 0 | 7 | 0 | 4 | 3 |
| Ecommerce Ops Manager | Digital Commerce (IT-built platforms) | 0 | 3 | 9 | 7 | 7 | 2 | 5 | 0 |
| Ecommerce Ops Mgr | Digital Commerce (IT-built platforms) | 0 | 0 | 6 | 20 | 7 | 5 | 0 | 2 |
| Functions | Generic / cross-department | 0 | 1 | 7 | 0 | 7 | 4 | 3 | 0 |
| Hiring Managers | Generic / cross-department | 0 | 7 | 3 | 0 | 7 | 0 | 7 | 0 |
| Smes | Generic / cross-department | 0 | 0 | 8 | 0 | 7 | 0 | 6 | 1 |
| Stakeholders | Generic / cross-department | 0 | 5 | 2 | 0 | 7 | 0 | 6 | 1 |
| Ecommerce Lead | Digital Commerce (IT-built platforms) | 0 | 2 | 1 | 4 | 6 | 0 | 6 | 0 |
| Ecommerce Team | Digital Commerce (IT-built platforms) | 0 | 5 | 4 | 1 | 6 | 2 | 2 | 2 |
| Ir Analyst | Generic / cross-department | 0 | 1 | 8 | 0 | 6 | 0 | 5 | 1 |
| Management | Generic / cross-department | 0 | 4 | 4 | 0 | 6 | 2 | 4 | 0 |
| Project Managers | Strategy / Corporate Planning (PMO) | 0 | 6 | 3 | 0 | 6 | 0 | 5 | 1 |
| User Depts | Generic / cross-department | 0 | 6 | 1 | 0 | 6 | 1 | 4 | 1 |
| Business Capability Owners | Generic / cross-department | 0 | 5 | 0 | 0 | 5 | 0 | 5 | 0 |
| Ecom Team | Digital Commerce (IT-built platforms) | 0 | 2 | 4 | 0 | 5 | 1 | 3 | 1 |
| Ecommerce Mgr | Digital Commerce (IT-built platforms) | 0 | 3 | 0 | 2 | 5 | 2 | 2 | 1 |
| Functional Leads | Generic / cross-department | 0 | 4 | 2 | 0 | 5 | 1 | 4 | 0 |
| Security Admin | Generic / cross-department | 0 | 4 | 4 | 0 | 5 | 3 | 2 | 0 |
| Sme | Generic / cross-department | 0 | 0 | 6 | 0 | 5 | 0 | 3 | 2 |
| Affected Bu | Generic / cross-department | 0 | 0 | 4 | 0 | 4 | 0 | 4 | 0 |
| Closure Pm | Generic / cross-department | 0 | 4 | 4 | 0 | 4 | 1 | 3 | 0 |
| Device Owners | Generic / cross-department | 0 | 4 | 0 | 0 | 4 | 0 | 4 | 0 |
| Digital Commerce | Digital Commerce (IT-built platforms) | 0 | 3 | 2 | 0 | 4 | 2 | 2 | 0 |
| Ecommerce Platform | Digital Commerce (IT-built platforms) | 0 | 4 | 0 | 0 | 4 | 0 | 3 | 1 |
| Function Owners | Generic / cross-department | 0 | 2 | 2 | 0 | 4 | 0 | 3 | 1 |
| Lms Administrator | Generic / cross-department | 0 | 4 | 5 | 0 | 4 | 0 | 4 | 0 |
| Participants | Generic / cross-department | 0 | 1 | 3 | 0 | 4 | 0 | 2 | 2 |
| Project Mgr | Strategy / Corporate Planning (PMO) | 0 | 0 | 6 | 2 | 4 | 0 | 1 | 3 |
| Supplier Mgmt | Generic / cross-department | 0 | 3 | 4 | 0 | 4 | 1 | 3 | 0 |
| Team | Generic / cross-department | 0 | 3 | 3 | 0 | 4 | 0 | 4 | 0 |
| Vs-161 Tprm | Generic / cross-department | 0 | 4 | 0 | 0 | 4 | 0 | 4 | 0 |
| Ai-Governance Liaison | Generic / cross-department | 0 | 3 | 3 | 0 | 3 | 0 | 3 | 0 |
| All Participants | Generic / cross-department | 0 | 0 | 3 | 0 | 3 | 1 | 1 | 1 |
| Approving Manager | Generic / cross-department | 0 | 3 | 1 | 0 | 3 | 1 | 2 | 0 |
| Business | Generic / cross-department | 0 | 2 | 1 | 0 | 3 | 0 | 3 | 0 |
| Business Requestor | Generic / cross-department | 0 | 3 | 4 | 1 | 3 | 0 | 1 | 2 |
| Business Sponsors | Generic / cross-department | 0 | 3 | 0 | 0 | 3 | 0 | 2 | 1 |
| Business User | Generic / cross-department | 0 | 2 | 2 | 1 | 3 | 1 | 1 | 1 |
| Change Mgmt | Generic / cross-department | 0 | 2 | 2 | 0 | 3 | 0 | 3 | 0 |
| Channel Owner | Generic / cross-department | 0 | 1 | 3 | 0 | 3 | 3 | 0 | 0 |
| Custodians | Generic / cross-department | 0 | 3 | 0 | 0 | 3 | 3 | 0 | 0 |
| Disaster Response | Generic / cross-department | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Dti Liaison | Generic / cross-department | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Gift Card | Digital Commerce (IT-built platforms) | 0 | 3 | 1 | 0 | 3 | 2 | 1 | 0 |
| Ot Soc Analyst | Generic / cross-department | 0 | 0 | 6 | 0 | 3 | 0 | 3 | 0 |
| Owner | Generic / cross-department | 0 | 2 | 1 | 0 | 3 | 0 | 3 | 0 |
| Owning Team | Generic / cross-department | 0 | 0 | 6 | 0 | 3 | 0 | 3 | 0 |
| Per Tier Above | Generic / cross-department | 0 | 0 | 3 | 1 | 3 | 2 | 1 | 0 |
| Pim Team | Generic / cross-department | 0 | 3 | 2 | 0 | 3 | 0 | 3 | 0 |
| Pos Team | Generic / cross-department | 0 | 2 | 2 | 0 | 3 | 2 | 0 | 1 |
| Product | Generic / cross-department | 0 | 3 | 1 | 0 | 3 | 0 | 3 | 0 |
| Project Design Manager | Strategy / Corporate Planning (PMO) | 0 | 0 | 0 | 3 | 3 | 1 | 2 | 0 |
| Sales Team | Generic / cross-department | 0 | 3 | 2 | 0 | 3 | 0 | 3 | 0 |
| Seller Ops | Digital Commerce (IT-built platforms) | 0 | 0 | 3 | 0 | 3 | 0 | 3 | 0 |
| Tprm Analyst | Generic / cross-department | 0 | 1 | 4 | 0 | 3 | 1 | 2 | 0 |
| Trade Pro Program | Strategy / Corporate Planning (PMO) | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Vendor Representatives | Generic / cross-department | 0 | 3 | 0 | 0 | 3 | 1 | 2 | 0 |
| Vendor-Portfolio Analyst | Generic / cross-department | 0 | 2 | 5 | 0 | 3 | 0 | 3 | 0 |
| Vs-27.3 | Generic / cross-department | 0 | 3 | 2 | 0 | 3 | 0 | 3 | 0 |
| Vs-91 | Generic / cross-department | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| VS-91 / DPO | Generic / cross-department | 0 | 0 | 3 | 0 | 3 | 0 | 3 | 0 |
| Warranty Admin | Generic / cross-department | 0 | 2 | 2 | 2 | 3 | 0 | 3 | 0 |
| Affected Individual | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Affected Process Owners | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Affected Workers | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| All Functional Leads | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Approver Per Tier | Generic / cross-department | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| As Per Tier | Generic / cross-department | 0 | 0 | 0 | 2 | 2 | 2 | 0 | 0 |
| Bpo | Generic / cross-department | 0 | 0 | 2 | 1 | 2 | 0 | 1 | 1 |
| Business Analyst | Generic / cross-department | 0 | 1 | 3 | 0 | 2 | 1 | 0 | 1 |
| Business Process Owner | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 1 | 0 | 1 |
| Business Sponsor | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Business Units | Generic / cross-department | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Catalog Ops | Generic / cross-department | 0 | 2 | 3 | 0 | 2 | 0 | 2 | 0 |
| Client Project Manager | Strategy / Corporate Planning (PMO) | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Coo Office | Generic / cross-department | 0 | 0 | 1 | 1 | 2 | 0 | 2 | 0 |
| Custodian | Generic / cross-department | 0 | 0 | 6 | 0 | 2 | 2 | 0 | 0 |
| Customer Project Design Specialist | Strategy / Corporate Planning (PMO) | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Dam Team | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Design Team | Generic / cross-department | 0 | 1 | 3 | 0 | 2 | 0 | 0 | 2 |
| E-Commerce Ops Supervisor | Digital Commerce (IT-built platforms) | 0 | 0 | 3 | 6 | 2 | 2 | 0 | 0 |
| E-Wallet Provider Operations | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Ecom Manager | Digital Commerce (IT-built platforms) | 0 | 1 | 0 | 1 | 2 | 1 | 1 | 0 |
| Ecommerce Associate | Digital Commerce (IT-built platforms) | 0 | 2 | 7 | 0 | 2 | 0 | 1 | 1 |
| Ecommerce Specialist | Digital Commerce (IT-built platforms) | 0 | 2 | 1 | 0 | 2 | 1 | 0 | 1 |
| Ev-Host Ops | Generic / cross-department | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Executive Office | Generic / cross-department | 0 | 1 | 1 | 0 | 2 | 2 | 0 | 0 |
| Executive Sponsors | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Function Leads | Generic / cross-department | 0 | 0 | 2 | 0 | 2 | 0 | 1 | 1 |
| Functional Smes | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Government Ops | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Hq Function Mgr | Generic / cross-department | 0 | 2 | 1 | 2 | 2 | 0 | 2 | 0 |
| Impact Analyst | Generic / cross-department | 0 | 2 | 3 | 0 | 2 | 0 | 2 | 0 |
| Initiative Team | Strategy / Corporate Planning (PMO) | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Leaders | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Ltfrb Liaison | Generic / cross-department | 0 | 2 | 1 | 0 | 2 | 2 | 0 | 0 |
| Marketplace Ops | Digital Commerce (IT-built platforms) | 0 | 2 | 3 | 0 | 2 | 0 | 2 | 0 |
| Ncip Provincial Office | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Office | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Omnichannel | Digital Commerce (IT-built platforms) | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Ops | Generic / cross-department | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Ot Ir Analyst | Generic / cross-department | 0 | 0 | 2 | 0 | 2 | 2 | 0 | 0 |
| Owners | Generic / cross-department | 0 | 0 | 2 | 0 | 2 | 0 | 1 | 1 |
| Owning Team Business Process Owner | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Permit Portfolio | Strategy / Corporate Planning (PMO) | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Pm & Bpo | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Process Architects | Generic / cross-department | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Project Consultants | Strategy / Corporate Planning (PMO) | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 2 |
| Project Lead | Strategy / Corporate Planning (PMO) | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| Qa Team | Generic / cross-department | 0 | 1 | 2 | 0 | 2 | 2 | 0 | 0 |
| Requesting Manager | Generic / cross-department | 0 | 1 | 3 | 0 | 2 | 0 | 2 | 0 |
| Reviewers | Generic / cross-department | 0 | 0 | 2 | 0 | 2 | 1 | 0 | 1 |
| Sec Liaison | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Senior Management | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Social Commerce Specialist | Digital Commerce (IT-built platforms) | 0 | 2 | 3 | 0 | 2 | 0 | 2 | 0 |
| Strategic Planning | Strategy / Corporate Planning (PMO) | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| Strategy Lead | Strategy / Corporate Planning (PMO) | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 2 |
| Strategy Team | Strategy / Corporate Planning (PMO) | 0 | 0 | 2 | 0 | 2 | 1 | 0 | 1 |
| Subject Experts | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Subject-Matter Experts | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| Vault Custodian | Generic / cross-department | 0 | 1 | 2 | 0 | 2 | 1 | 1 | 0 |
| Vs-125 | Generic / cross-department | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Vs-26 | Generic / cross-department | 0 | 1 | 1 | 0 | 2 | 1 | 1 | 0 |
| Vs-63 | Generic / cross-department | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Warranty Mgmt | Generic / cross-department | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Workstream Leads | Generic / cross-department | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| Workstreams | Generic / cross-department | 0 | 0 | 4 | 0 | 2 | 0 | 2 | 0 |
| Accused Party'S Supervisor | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Action Owner | Generic / cross-department | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| Affected Business Leads | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Affected Business Owners | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Affected Business Process Owners | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Affected Leaders | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Affected Regions | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Affected-Function Deputies | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Agency Liaison | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| All | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| All Affected | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| All Departments | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| All Functional Leaders | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| All Managers And Above | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| All Process Owners | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| All Validators | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| All Workstreams | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Applications Team | Generic / cross-department | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| Approver Per Threshold | Generic / cross-department | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Approvers | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Assigned Team | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Auditee | Generic / cross-department | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| Auditees | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Authorized Signatories | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Authorizer | Generic / cross-department | 0 | 0 | 3 | 0 | 1 | 1 | 0 | 0 |
| Backup Admin | Generic / cross-department | 0 | 1 | 3 | 0 | 1 | 1 | 0 | 0 |
| Bank Acquiring Operations | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Basis Team | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Bid Team | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Bir Efps Administrator | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Bsa-Aml Analyst | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Buildright Depot Inc | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Business Analysts | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Business Domain Owner | Generic / cross-department | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| Business Representative | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Business Requestors | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Business Stakeholders | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Business Unit Leaders | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Business-Unit Leaders | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Card Acquirer Operations | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Change Requestor | Generic / cross-department | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Cio Office Vendor-Portfolio Analyst | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Client Project Engineer | Strategy / Corporate Planning (PMO) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Commercial Ops | Generic / cross-department | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Contingent-Workforce Mgmt | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Core-Systems Owners | Generic / cross-department | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Count Teams | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Cross-Functional | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Current Manager | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Customer Project Manager | Strategy / Corporate Planning (PMO) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Customer Stakeholders | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Denr-Emb Liaison | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Developer Project Manager | Strategy / Corporate Planning (PMO) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Device Owner | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Digital Commerce Gm | Digital Commerce (IT-built platforms) | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Digital Commerce Mgr | Digital Commerce (IT-built platforms) | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Direct Supervisor | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Document Controller | Generic / cross-department | 0 | 0 | 7 | 0 | 1 | 0 | 0 | 1 |
| Domain | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Domain Accountable Owner | Generic / cross-department | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 |
| E-Commerce Ops Manager | Digital Commerce (IT-built platforms) | 0 | 1 | 1 | 3 | 1 | 1 | 0 | 0 |
| E-Commerce Platform | Digital Commerce (IT-built platforms) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| E-Commerce Team | Digital Commerce (IT-built platforms) | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Ecom Ops | Digital Commerce (IT-built platforms) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ecom Ops Mgr | Digital Commerce (IT-built platforms) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ecommerce Coordinator | Digital Commerce (IT-built platforms) | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Ecommerce Engine | Digital Commerce (IT-built platforms) | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Ecommerce Operations Coordinator | Digital Commerce (IT-built platforms) | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Ecommerce Ops Lead | Digital Commerce (IT-built platforms) | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Ecommerce Ops Specialist | Digital Commerce (IT-built platforms) | 0 | 0 | 3 | 6 | 1 | 1 | 0 | 0 |
| Ecommerce Platform Administrator | Digital Commerce (IT-built platforms) | 0 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Ecommerce Platform Vendor | Digital Commerce (IT-built platforms) | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Ecommerce Product Mgr | Digital Commerce (IT-built platforms) | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 |
| Ecommerce Returns Specialist | Digital Commerce (IT-built platforms) | 0 | 1 | 1 | 2 | 1 | 0 | 1 | 0 |
| Economic-Crime Units | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Employee Representatives | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Employee'S Direct Manager | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Enterprise | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Escalation Desk Analyst | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Event Team | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Exec Team | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| External Adjuster Team | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Function Sponsors | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Functional Approvers | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Functional Lead | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Functional Owners | Generic / cross-department | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Functional Sme | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Gift-Card Ops | Digital Commerce (IT-built platforms) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Government Agency Liaison | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Head Digital Commerce | Digital Commerce (IT-built platforms) | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Head Of Strategy | Strategy / Corporate Planning (PMO) | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| Heirs Of The Deceased Owner | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Hq Admin | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hq Function | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Hq Vault Custodian | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Inc | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Initiative Lead | Strategy / Corporate Planning (PMO) | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Initiative Leads | Strategy / Corporate Planning (PMO) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Initiative Owners | Strategy / Corporate Planning (PMO) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Initiative Sponsors | Strategy / Corporate Planning (PMO) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Initiator | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Intake | Generic / cross-department | 0 | 0 | 3 | 0 | 1 | 1 | 0 | 0 |
| Internal Specialists | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Itoc Analyst | Generic / cross-department | 0 | 0 | 3 | 0 | 1 | 1 | 0 | 0 |
| Itoc Analysts | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Knowledge | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Landlord Management | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Law-Enforcement Liaison | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Legacy Admin | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Lgu Drrm Office | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Lgu Liaison | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Lgu Planning Office | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lgu Representatives | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lgu Traffic Office | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Liaison | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Local Ancestral Domain Office | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Local Government Liaison | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Local Lgu Liaison | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Local Stakeholders | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Locker Ops | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lpg Program Lead | Strategy / Corporate Planning (PMO) | 0 | 1 | 1 | 2 | 1 | 0 | 1 | 0 |
| Lpg Supplier Emergency-Response Desk | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Management Reps | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Marketplace Specialist | Digital Commerce (IT-built platforms) | 0 | 1 | 5 | 0 | 1 | 1 | 0 | 0 |
| Marketplace Tech Team | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Msme Ops | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Multi-Entity Approvers | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Multiple | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Multiple Reviewers | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Ncip Liaison | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| New-Store Team | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ngo Liaison | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Office Admin | Generic / cross-department | 0 | 1 | 4 | 0 | 1 | 0 | 1 | 0 |
| Omo | Digital Commerce (IT-built platforms) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Operational Stakeholder | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Ops Owner | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Origin Owner | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Origin Owners | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Ot Threat Intel Analyst | Generic / cross-department | 0 | 0 | 4 | 0 | 1 | 0 | 1 | 0 |
| Owning Product Team Product Manager & Business Process Owner | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Owning Product Team Qa Analyst | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Owning Qa Analyst | Generic / cross-department | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Pack Team | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Pag-Ibig Branch Representatives | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Pag-Ibig Portal Administrators | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Partner Mgmt | Generic / cross-department | 0 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Partner Representatives | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Per Authorization Matrix | Generic / cross-department | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Per Authorization Tier | Generic / cross-department | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Per Doa | Generic / cross-department | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Per Escalation Matrix | Generic / cross-department | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Per The Matrix | Generic / cross-department | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Per Tier | Generic / cross-department | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Per Trigger Workflow | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Per W4 | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Pim Administrator | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Planning And Implementation At The Central Office | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Platform Owners | Generic / cross-department | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Platform Teams | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Pmo Lead | Strategy / Corporate Planning (PMO) | 0 | 0 | 2 | 1 | 1 | 0 | 0 | 1 |
| Pnp & Pnp-Women And Children Protection Desk | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Pnp Scene Of The Crime Operations Team | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Police Liaison | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Portfolio | Strategy / Corporate Planning (PMO) | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Pos Admin | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Presenter | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Procurement Team | Generic / cross-department | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| Program Managers | Strategy / Corporate Planning (PMO) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Program Sponsor | Strategy / Corporate Planning (PMO) | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Project Account Mgr | Strategy / Corporate Planning (PMO) | 0 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Project Leads | Strategy / Corporate Planning (PMO) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Project Management | Strategy / Corporate Planning (PMO) | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Project Management Office | Strategy / Corporate Planning (PMO) | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Project Pmo | Strategy / Corporate Planning (PMO) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Project Team | Strategy / Corporate Planning (PMO) | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Proposal | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Qa Analyst | Generic / cross-department | 0 | 1 | 6 | 0 | 1 | 1 | 0 | 0 |
| Rebate Ops | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Recipient | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Recount Team | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Registry Of Deeds Liaison | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Reporter | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Reporting Person | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Representatives | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Requester | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Requesting Party | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Resource Management | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Response Team | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Responsible Person | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Rmn Platform Admin | Generic / cross-department | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| Sales Reps | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Scf Program Lead | Strategy / Corporate Planning (PMO) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| School Administrator | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sec Tprm Analyst | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Security Team | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Sender | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Senior Programs | Strategy / Corporate Planning (PMO) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ship Team | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Site Mgmt | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Site Operations | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Social Commerce Associate | Digital Commerce (IT-built platforms) | 0 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Specialist Teams | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Stakeholder Representatives | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Statistics | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Store Hr Administrators | Store HR Coordinator | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Subcontractor Mgmt | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Subject Matter Expert | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Subject Matter Experts | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Subjects | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Technical | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| The Reporter | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| The Subject'S Management | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Threat Assessment Team | Generic / cross-department | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Tprm Pre-Read For Customer-Data Surfaces | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Trained Staff Search Teams | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Uniform Custodian | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Union Representatives | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Union Reps | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Unit | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Unit Lead | Generic / cross-department | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Various | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Vendor Factory Management | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Vendor Innovation Team | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Vendor Vmi Analyst | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Video Shopping Associate | Digital Commerce (IT-built platforms) | 0 | 1 | 4 | 0 | 1 | 0 | 0 | 1 |
| Visit Team | Generic / cross-department | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| Vp E-Commerce | Digital Commerce (IT-built platforms) | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| Vp Of Affected Function | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vs-03 Portal Admin | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Vs-04 | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| VS-08/VS-149 (POS/SCO) | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vs-100 | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vs-108 | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| VS-125 fraud/insider | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vs-13 | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| VS-13 / VS-125 | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| VS-13/VS-07 (inbound customer-inquiry scripts) | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vs-138 | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vs-14.3 | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| VS-14.3 / Brand | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Vs-147.3 | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Vs-163 | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| VS-163/VS-164/VS-149 channel owners | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vs-164 | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vs-167 | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Vs-167 Vetting | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vs-178 Land Team Where Banked Parcels Are Affected | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vs-19.3 | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vs-23 Channel Owners | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vs-26 Claims | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Vs-35 | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| VS-63 / Communications | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| VS-63 / Store & DC Receiving | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Vs-69 Execution Chain Where The Surge Rides A Typhoon | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| W55 Execution Team | Generic / cross-department | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| W55 Failover Execution Team | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| W5563 | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Warranty Ops | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Witness'S Management | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Wms Administrator | Generic / cross-department | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Wms Analyst | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Wms Team | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Workforce Planning Analyst | Generic / cross-department | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| — | Generic / cross-department | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |

## System & automated actors

| Role | Dept / source | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|
| System | System & automated actors | 8 | 29 | 2481 | 5 | 1192 | 394 | 626 | 172 |
| Order Management System | System & automated actors | 6 | 0 | 0 | 0 | 6 | 0 | 6 | 0 |
| Pos | System & automated actors | 4 | 37 | 9 | 0 | 42 | 27 | 11 | 4 |
| Ecommerce System | System & automated actors | 4 | 0 | 5 | 0 | 5 | 0 | 5 | 0 |
| Pos System | System & automated actors | 3 | 1 | 7 | 0 | 8 | 5 | 3 | 0 |
| Wms | System & automated actors | 0 | 4 | 16 | 0 | 14 | 6 | 7 | 1 |
| Erp | System & automated actors | 0 | 1 | 11 | 0 | 12 | 7 | 5 | 0 |
| Oms | System & automated actors | 0 | 4 | 10 | 0 | 9 | 2 | 7 | 0 |
| Payment Gateway | System & automated actors | 0 | 6 | 1 | 0 | 7 | 3 | 3 | 1 |
| Agent | System & automated actors | 0 | 2 | 6 | 0 | 5 | 1 | 4 | 0 |
| Telematics Platform | System & automated actors | 0 | 3 | 2 | 0 | 4 | 0 | 3 | 1 |
| Automated | System & automated actors | 0 | 0 | 0 | 4 | 3 | 0 | 3 | 0 |
| Erp System | System & automated actors | 0 | 0 | 4 | 0 | 3 | 2 | 1 | 0 |
| Iap | System & automated actors | 0 | 2 | 2 | 0 | 3 | 0 | 3 | 0 |
| Automation | System & automated actors | 0 | 2 | 1 | 0 | 2 | 0 | 0 | 2 |
| Network | System & automated actors | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Payment Gateways | System & automated actors | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Platform | System & automated actors | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Application | System & automated actors | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| BIR EIS Portal | System & automated actors | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Chatbot | System & automated actors | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| CMMS | System & automated actors | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Email Engine | System & automated actors | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| ESS Portal | System & automated actors | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| IDP Platform | System & automated actors | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| LMS | System & automated actors | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Marketplace Portal | System & automated actors | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| POS Terminal | System & automated actors | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| POS-ERP Integration | System & automated actors | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| SCO Terminal | System & automated actors | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Vendor Portal | System & automated actors | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |

## Governance bodies

| Role | Dept / source | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|
| Captive Board | Governance bodies | 7 | 4 | 11 | 19 | 15 | 2 | 13 | 0 |
| Board | Governance bodies | 1 | 59 | 26 | 154 | 166 | 27 | 102 | 37 |
| Arb | Governance bodies | 1 | 7 | 6 | 1 | 7 | 0 | 7 | 0 |
| Architecture Review Board | Governance bodies | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ethics Committee Chair | Governance bodies | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Audit Committee | Governance bodies | 0 | 6 | 1 | 70 | 56 | 8 | 35 | 13 |
| Board Audit Committee | Governance bodies | 0 | 11 | 1 | 32 | 34 | 11 | 17 | 6 |
| C-Suite | Governance bodies | 0 | 6 | 11 | 8 | 15 | 2 | 10 | 3 |
| Ethics Committee | Governance bodies | 0 | 8 | 1 | 9 | 12 | 4 | 3 | 5 |
| Executive Committee | Governance bodies | 0 | 8 | 4 | 0 | 12 | 2 | 8 | 2 |
| Dept. Head | Governance bodies | 0 | 2 | 19 | 17 | 11 | 9 | 2 | 0 |
| Executive Team | Governance bodies | 0 | 10 | 6 | 0 | 10 | 2 | 1 | 7 |
| Exco | Governance bodies | 0 | 9 | 0 | 0 | 9 | 0 | 2 | 7 |
| Executives | Governance bodies | 0 | 6 | 5 | 0 | 8 | 1 | 6 | 1 |
| SIB | Governance bodies | 0 | 6 | 4 | 1 | 7 | 0 | 7 | 0 |
| Board Risk Committee | Governance bodies | 0 | 3 | 0 | 4 | 6 | 0 | 5 | 1 |
| Shareholders | Governance bodies | 0 | 5 | 1 | 1 | 6 | 0 | 6 | 0 |
| Board Audit & Risk Committee | Governance bodies | 0 | 2 | 0 | 3 | 5 | 1 | 2 | 2 |
| Change Advisory Board | Governance bodies | 0 | 4 | 0 | 2 | 5 | 1 | 4 | 0 |
| Credit Committee | Governance bodies | 0 | 2 | 3 | 1 | 4 | 1 | 3 | 0 |
| Investment Committee | Governance bodies | 0 | 2 | 3 | 0 | 4 | 0 | 3 | 1 |
| Site Leadership | Governance bodies | 0 | 0 | 4 | 0 | 4 | 1 | 2 | 1 |
| Steering Committee | Governance bodies | 0 | 3 | 2 | 0 | 4 | 1 | 2 | 1 |
| Dept. Heads | Governance bodies | 0 | 0 | 5 | 0 | 3 | 3 | 0 | 0 |
| Cab | Governance bodies | 0 | 0 | 2 | 0 | 2 | 1 | 1 | 0 |
| Chairman | Governance bodies | 0 | 0 | 0 | 3 | 2 | 0 | 0 | 2 |
| Committee | Governance bodies | 0 | 0 | 4 | 0 | 2 | 1 | 1 | 0 |
| Committee Chair | Governance bodies | 0 | 0 | 3 | 1 | 2 | 0 | 2 | 0 |
| Dgc Chair | Governance bodies | 0 | 0 | 0 | 2 | 2 | 1 | 0 | 1 |
| Disclosure Committee | Governance bodies | 0 | 1 | 0 | 3 | 2 | 0 | 2 | 0 |
| Management Panel | Governance bodies | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Nomination & Compensation Committee | Governance bodies | 0 | 2 | 1 | 1 | 2 | 0 | 2 | 0 |
| Review Board | Governance bodies | 0 | 0 | 5 | 0 | 2 | 0 | 2 | 0 |
| Adverse-Action Board | Governance bodies | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Advisory Board Members | Governance bodies | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Anti-Money Laundering Council | Governance bodies | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Board Committee | Governance bodies | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| Board Investment Committee | Governance bodies | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Board Remuneration Committee | Governance bodies | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Cab Members | Governance bodies | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Codi Chair | Governance bodies | 0 | 0 | 4 | 1 | 1 | 1 | 0 | 0 |
| Coe Members | Governance bodies | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Committee Chairs | Governance bodies | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Committee Members | Governance bodies | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Cooperative Members | Governance bodies | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Dei Committee | Governance bodies | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Dgc Members | Governance bodies | 0 | 0 | 3 | 0 | 1 | 0 | 0 | 1 |
| Directors | Governance bodies | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Executive Leadership | Governance bodies | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Group Board | Governance bodies | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Independent Directors | Governance bodies | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Installer Council | Governance bodies | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Job-Evaluation Committee | Governance bodies | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Material Review Board | Governance bodies | 0 | 0 | 2 | 0 | 1 | 1 | 0 | 0 |
| Members | Governance bodies | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Prioritization Committee | Governance bodies | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| Product Council | Governance bodies | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Tier & Control Board | Governance bodies | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Union Panel | Governance bodies | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |

## Generic workforce mentions

| Role | Dept / source | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|
| Employee | Workforce (generic) | 1 | 49 | 69 | 1 | 74 | 46 | 25 | 3 |
| Crew Lead | Workforce (generic) | 0 | 0 | 10 | 13 | 13 | 5 | 8 | 0 |
| Employees | Workforce (generic) | 0 | 13 | 1 | 0 | 13 | 2 | 11 | 0 |
| Operator | Workforce (generic) | 0 | 7 | 24 | 0 | 13 | 1 | 12 | 0 |
| All Staff | Workforce (generic) | 0 | 1 | 11 | 0 | 9 | 5 | 4 | 0 |
| Student Trainee | Workforce (generic) | 0 | 9 | 3 | 0 | 9 | 1 | 8 | 0 |
| Technician | Workforce (generic) | 0 | 2 | 12 | 0 | 8 | 1 | 4 | 3 |
| Staff | Workforce (generic) | 0 | 3 | 5 | 0 | 7 | 2 | 5 | 0 |
| Take-Back Associate | Workforce (generic) | 0 | 0 | 26 | 0 | 7 | 3 | 4 | 0 |
| Attendants | Workforce (generic) | 0 | 3 | 3 | 0 | 6 | 2 | 4 | 0 |
| Attendant | Workforce (generic) | 0 | 0 | 8 | 0 | 5 | 1 | 3 | 1 |
| Buddy | Workforce (generic) | 0 | 1 | 11 | 0 | 5 | 0 | 4 | 1 |
| Champions | Workforce (generic) | 0 | 5 | 3 | 0 | 5 | 0 | 5 | 0 |
| All Employees | Workforce (generic) | 0 | 4 | 1 | 0 | 4 | 2 | 2 | 0 |
| Floor Associates | Workforce (generic) | 0 | 4 | 0 | 0 | 4 | 3 | 1 | 0 |
| Loader | Workforce (generic) | 0 | 0 | 4 | 0 | 4 | 0 | 4 | 0 |
| Mentors | Workforce (generic) | 0 | 3 | 6 | 0 | 4 | 0 | 4 | 0 |
| Specialist | Workforce (generic) | 0 | 2 | 7 | 0 | 4 | 0 | 4 | 0 |
| End User | Workforce (generic) | 0 | 0 | 4 | 0 | 3 | 1 | 2 | 0 |
| Injured Employee | Workforce (generic) | 0 | 3 | 0 | 0 | 3 | 1 | 2 | 0 |
| New Employee | Workforce (generic) | 0 | 3 | 5 | 0 | 3 | 0 | 3 | 0 |
| New Hire | Workforce (generic) | 0 | 1 | 2 | 0 | 3 | 1 | 2 | 0 |
| Process Participants | Workforce (generic) | 0 | 3 | 0 | 0 | 3 | 0 | 2 | 1 |
| Spotter | Workforce (generic) | 0 | 0 | 5 | 0 | 3 | 0 | 3 | 0 |
| Spotters | Workforce (generic) | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Associates | Workforce (generic) | 0 | 1 | 2 | 0 | 2 | 0 | 1 | 1 |
| Device Operators | Workforce (generic) | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| Early-Career | Workforce (generic) | 0 | 1 | 4 | 0 | 2 | 0 | 2 | 0 |
| End Users | Workforce (generic) | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| End-Users | Workforce (generic) | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Heavy Equipment Operator | Workforce (generic) | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Loading Crew | Workforce (generic) | 0 | 0 | 2 | 0 | 2 | 2 | 0 | 0 |
| Mentor | Workforce (generic) | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Nearest Staff | Workforce (generic) | 0 | 0 | 2 | 0 | 2 | 2 | 0 | 0 |
| Onboarding Buddy | Workforce (generic) | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Technicians | Workforce (generic) | 0 | 1 | 1 | 0 | 2 | 1 | 0 | 1 |
| Trained Staff | Workforce (generic) | 0 | 0 | 2 | 0 | 2 | 2 | 0 | 0 |
| Trainee | Workforce (generic) | 0 | 1 | 2 | 0 | 2 | 0 | 2 | 0 |
| Various Staff | Workforce (generic) | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| Worker | Workforce (generic) | 0 | 1 | 3 | 0 | 2 | 0 | 2 | 0 |
| Affected Employees | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| All 29 Staff | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| All Associates | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| All Customer-Facing Staff | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| All Floor Staff | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| All Trained Belts | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Any Employee | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Assembly Staff | Workforce (generic) | 0 | 0 | 3 | 0 | 1 | 1 | 0 | 0 |
| Attendee | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Business Users | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Contractor Personnel | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Crane Operator | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Crew Leads | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Crews | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Customer-Facing Staff | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Cutting Staff | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Departing Employee | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Driver & Helper | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Employee Attendees | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Ferry Operator | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Frontline Staff | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Helper | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| High-Potential Employees | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Host Employee | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Hq Staff | Workforce (generic) | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Hub Packer | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Hub Packers | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hub Picker | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Hub Pickers | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Incident Personnel | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Janitorial Staff | Workforce (generic) | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Key Users | Workforce (generic) | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| Kitting Associates | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| New Hire Employee | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| New Hires | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Operators | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Pack Staff | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Pick Staff | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| POS Staff | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Provider Workforce | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Referring Employee | Workforce (generic) | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Requesting Employee | Workforce (generic) | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Resigned Employee | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Shift Staff | Workforce (generic) | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| SOC Operator | Workforce (generic) | 0 | 0 | 2 | 0 | 1 | 1 | 0 | 0 |
| Solar-Trained Sales Associate | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Staff Member | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Supervisors | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Talent | Workforce (generic) | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Team Leader | Workforce (generic) | 0 | 0 | 2 | 1 | 1 | 1 | 0 | 0 |
| Temporary Staff | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Toll Operator | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Trainees | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Transferring Employee | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Traveling Employee | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Unloading Crew | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Users | Workforce (generic) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Water Tanker Operator | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Weighbridge Operator | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Workshop Staff | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Zone Staff | Workforce (generic) | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |

## External counterparties (not staff)

| Role | Dept / source | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|
| Project Consultant | External / counterparty | 12 | 19 | 22 | 6 | 19 | 0 | 19 | 0 |
| Bank | External / counterparty | 10 | 42 | 40 | 1 | 58 | 19 | 37 | 2 |
| Driver | External / counterparty | 7 | 63 | 122 | 2 | 92 | 27 | 55 | 10 |
| Vendor | External / counterparty | 4 | 204 | 162 | 4 | 270 | 69 | 177 | 24 |
| 3Pl | External / counterparty | 4 | 35 | 17 | 0 | 42 | 10 | 28 | 4 |
| Delivery Crew | External / counterparty | 3 | 6 | 13 | 0 | 12 | 4 | 8 | 0 |
| Transfer Agent | External / counterparty | 2 | 4 | 5 | 0 | 4 | 1 | 3 | 0 |
| Customer | External / counterparty | 1 | 440 | 284 | 26 | 469 | 97 | 313 | 59 |
| Contractor | External / counterparty | 1 | 43 | 58 | 0 | 64 | 4 | 51 | 9 |
| Security Guard (contracted) | External / counterparty | 1 | 37 | 84 | 1 | 44 | 18 | 24 | 2 |
| Insurance Broker | External / counterparty | 1 | 33 | 22 | 1 | 38 | 10 | 26 | 2 |
| Supplier | External / counterparty | 1 | 29 | 17 | 0 | 30 | 6 | 23 | 1 |
| Structural Engineer | External / counterparty | 1 | 9 | 14 | 4 | 11 | 5 | 5 | 1 |
| Contractor Site Manager | External / counterparty | 1 | 3 | 3 | 1 | 6 | 1 | 5 | 0 |
| Site Engineer | External / counterparty | 1 | 4 | 4 | 4 | 5 | 2 | 3 | 0 |
| Project Engineer | External / counterparty | 1 | 3 | 3 | 4 | 4 | 1 | 3 | 0 |
| Environmental Consultant | External / counterparty | 1 | 1 | 5 | 4 | 2 | 2 | 0 | 0 |
| Fronting Carrier | External / counterparty | 1 | 1 | 2 | 0 | 2 | 0 | 2 | 0 |
| Licensed Installer | External / counterparty | 1 | 1 | 0 | 0 | 2 | 1 | 1 | 0 |
| Quantity Surveyor | External / counterparty | 1 | 1 | 3 | 4 | 2 | 1 | 1 | 0 |
| Solar Installation Partner | External / counterparty | 1 | 1 | 0 | 0 | 2 | 0 | 1 | 1 |
| TPA | External / counterparty | 1 | 1 | 4 | 0 | 2 | 0 | 2 | 0 |
| Appraisers | External / counterparty | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Cleaning Provider | External / counterparty | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Contractor Site Representative | External / counterparty | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Grounds Provider | External / counterparty | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Housekeeping Provider | External / counterparty | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Mystery Shopper | External / counterparty | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Pest-Control Provider | External / counterparty | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| Security Vendor | External / counterparty | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Service Partner Technician | External / counterparty | 1 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Trades Contractors | External / counterparty | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Auditor | External / counterparty | 0 | 61 | 30 | 5 | 71 | 26 | 40 | 5 |
| External Counsel | External / counterparty | 0 | 26 | 29 | 0 | 35 | 12 | 21 | 2 |
| Carrier | External / counterparty | 0 | 22 | 26 | 0 | 30 | 12 | 17 | 1 |
| Vendors | External / counterparty | 0 | 26 | 4 | 0 | 29 | 1 | 24 | 4 |
| Dole | External / counterparty | 0 | 22 | 1 | 0 | 22 | 16 | 5 | 1 |
| Bfp | External / counterparty | 0 | 22 | 4 | 0 | 21 | 17 | 4 | 0 |
| Lgu | External / counterparty | 0 | 19 | 2 | 0 | 21 | 8 | 13 | 0 |
| Cooperative Representatives | External / counterparty | 0 | 19 | 2 | 0 | 19 | 2 | 17 | 0 |
| Marketing Agency | External / counterparty | 0 | 15 | 5 | 0 | 15 | 2 | 10 | 3 |
| Marketplace Seller | External / counterparty | 0 | 13 | 10 | 0 | 15 | 4 | 11 | 0 |
| Surety | External / counterparty | 0 | 14 | 7 | 0 | 15 | 3 | 12 | 0 |
| Utility | External / counterparty | 0 | 9 | 14 | 0 | 13 | 2 | 11 | 0 |
| Vendor Representative | External / counterparty | 0 | 10 | 9 | 0 | 13 | 1 | 7 | 5 |
| Bir | External / counterparty | 0 | 11 | 2 | 0 | 12 | 8 | 4 | 0 |
| Dealer | External / counterparty | 0 | 12 | 0 | 0 | 12 | 3 | 9 | 0 |
| Delivery Partner | External / counterparty | 0 | 11 | 9 | 0 | 12 | 4 | 8 | 0 |
| External Tax Advisor | External / counterparty | 0 | 10 | 5 | 0 | 12 | 9 | 2 | 1 |
| Funder | External / counterparty | 0 | 12 | 2 | 0 | 12 | 6 | 6 | 0 |
| Installation Partner | External / counterparty | 0 | 8 | 10 | 0 | 12 | 1 | 10 | 1 |
| Law Enforcement | External / counterparty | 0 | 12 | 0 | 0 | 12 | 7 | 5 | 0 |
| External Advisor | External / counterparty | 0 | 5 | 12 | 1 | 11 | 5 | 5 | 1 |
| External Auditors | External / counterparty | 0 | 10 | 4 | 0 | 11 | 0 | 9 | 2 |
| Provider | External / counterparty | 0 | 2 | 19 | 0 | 11 | 0 | 10 | 1 |
| 3Pl Carrier | External / counterparty | 0 | 10 | 1 | 0 | 10 | 9 | 0 | 1 |
| Denr | External / counterparty | 0 | 10 | 0 | 0 | 10 | 6 | 3 | 1 |
| Factor | External / counterparty | 0 | 10 | 0 | 0 | 10 | 4 | 6 | 0 |
| LTO | External / counterparty | 0 | 10 | 1 | 0 | 10 | 8 | 2 | 0 |
| Contractors | External / counterparty | 0 | 9 | 0 | 0 | 9 | 0 | 8 | 1 |
| Dti | External / counterparty | 0 | 9 | 0 | 0 | 9 | 5 | 4 | 0 |
| HMO Provider | External / counterparty | 0 | 9 | 0 | 0 | 9 | 4 | 5 | 0 |
| Providers | External / counterparty | 0 | 6 | 4 | 0 | 9 | 2 | 6 | 1 |
| Sss | External / counterparty | 0 | 9 | 0 | 0 | 9 | 4 | 5 | 0 |
| Affected MSMEs | External / counterparty | 0 | 8 | 0 | 0 | 8 | 0 | 8 | 0 |
| Courier | External / counterparty | 0 | 2 | 9 | 0 | 8 | 3 | 4 | 1 |
| External Advisors | External / counterparty | 0 | 5 | 5 | 0 | 8 | 0 | 8 | 0 |
| Freight Forwarder | External / counterparty | 0 | 7 | 4 | 0 | 8 | 5 | 3 | 0 |
| Hauler | External / counterparty | 0 | 7 | 4 | 0 | 8 | 3 | 5 | 0 |
| Partner Bank | External / counterparty | 0 | 7 | 5 | 0 | 8 | 1 | 4 | 3 |
| PNP | External / counterparty | 0 | 7 | 1 | 0 | 8 | 3 | 4 | 1 |
| TVI Coordinator | External / counterparty | 0 | 8 | 0 | 0 | 8 | 3 | 5 | 0 |
| Vendor Contact | External / counterparty | 0 | 8 | 12 | 0 | 8 | 3 | 4 | 1 |
| Banks | External / counterparty | 0 | 7 | 0 | 0 | 7 | 1 | 5 | 1 |
| DENR-EMB | External / counterparty | 0 | 7 | 0 | 0 | 7 | 4 | 3 | 0 |
| Distribution Utility | External / counterparty | 0 | 6 | 4 | 1 | 7 | 1 | 6 | 0 |
| Financing Partner | External / counterparty | 0 | 5 | 3 | 0 | 7 | 2 | 3 | 2 |
| Labor Union | External / counterparty | 0 | 7 | 1 | 0 | 7 | 5 | 2 | 0 |
| OEM | External / counterparty | 0 | 5 | 3 | 0 | 7 | 1 | 6 | 0 |
| Police | External / counterparty | 0 | 7 | 3 | 0 | 7 | 2 | 5 | 0 |
| Smart-Locker Platform Operator | External / counterparty | 0 | 0 | 9 | 0 | 7 | 1 | 6 | 0 |
| Acquirer | External / counterparty | 0 | 6 | 0 | 0 | 6 | 3 | 3 | 0 |
| Bank Relationship Manager | External / counterparty | 0 | 6 | 0 | 0 | 6 | 3 | 2 | 1 |
| BFP Inspector | External / counterparty | 0 | 3 | 3 | 2 | 6 | 5 | 1 | 0 |
| CIT Vendor | External / counterparty | 0 | 4 | 3 | 0 | 6 | 2 | 3 | 1 |
| Landlord | External / counterparty | 0 | 5 | 1 | 0 | 6 | 1 | 5 | 0 |
| Lender Uw Manager | External / counterparty | 0 | 0 | 0 | 11 | 6 | 1 | 5 | 0 |
| Outside Counsel | External / counterparty | 0 | 5 | 10 | 0 | 6 | 2 | 4 | 0 |
| SCF Partner | External / counterparty | 0 | 6 | 1 | 0 | 6 | 1 | 5 | 0 |
| Site Staff | External / counterparty | 0 | 5 | 5 | 0 | 6 | 1 | 5 | 0 |
| Third Party | External / counterparty | 0 | 6 | 0 | 0 | 6 | 2 | 4 | 0 |
| Vendor Driver | External / counterparty | 0 | 5 | 2 | 0 | 6 | 1 | 5 | 0 |
| Barangay | External / counterparty | 0 | 5 | 0 | 0 | 5 | 3 | 2 | 0 |
| Bsp | External / counterparty | 0 | 5 | 0 | 0 | 5 | 3 | 2 | 0 |
| Concessionaire | External / counterparty | 0 | 5 | 6 | 0 | 5 | 1 | 3 | 1 |
| Coop | External / counterparty | 0 | 0 | 5 | 0 | 5 | 1 | 4 | 0 |
| Customers | External / counterparty | 0 | 5 | 0 | 0 | 5 | 2 | 1 | 2 |
| Epc | External / counterparty | 0 | 4 | 7 | 0 | 5 | 0 | 5 | 0 |
| Estimator | External / counterparty | 0 | 3 | 4 | 0 | 5 | 1 | 3 | 1 |
| External Consultant | External / counterparty | 0 | 3 | 7 | 0 | 5 | 2 | 2 | 1 |
| Fire-Safety Consultant | External / counterparty | 0 | 5 | 3 | 0 | 5 | 3 | 2 | 0 |
| Fuel Supplier | External / counterparty | 0 | 5 | 1 | 0 | 5 | 1 | 2 | 2 |
| Government Inspector | External / counterparty | 0 | 2 | 4 | 0 | 5 | 1 | 4 | 0 |
| NPC | External / counterparty | 0 | 5 | 0 | 0 | 5 | 2 | 3 | 0 |
| PCAB | External / counterparty | 0 | 5 | 0 | 0 | 5 | 3 | 2 | 0 |
| Philhealth | External / counterparty | 0 | 5 | 0 | 0 | 5 | 4 | 1 | 0 |
| Reseller | External / counterparty | 0 | 3 | 4 | 0 | 5 | 1 | 2 | 2 |
| Security Guard Force | External / counterparty | 0 | 5 | 4 | 0 | 5 | 0 | 5 | 0 |
| Subcontractor | External / counterparty | 0 | 5 | 4 | 0 | 5 | 1 | 3 | 1 |
| Suppliers | External / counterparty | 0 | 5 | 0 | 0 | 5 | 0 | 5 | 0 |
| TESDA | External / counterparty | 0 | 5 | 0 | 0 | 5 | 2 | 3 | 0 |
| AMLC | External / counterparty | 0 | 4 | 0 | 0 | 4 | 4 | 0 | 0 |
| BOC | External / counterparty | 0 | 4 | 1 | 0 | 4 | 3 | 1 | 0 |
| CIAP | External / counterparty | 0 | 4 | 0 | 0 | 4 | 2 | 2 | 0 |
| City LGU | External / counterparty | 0 | 4 | 0 | 0 | 4 | 2 | 2 | 0 |
| Clinic | External / counterparty | 0 | 2 | 2 | 0 | 4 | 2 | 2 | 0 |
| Co-op Chairman | External / counterparty | 0 | 4 | 0 | 0 | 4 | 1 | 3 | 0 |
| Commercial Music Provider | External / counterparty | 0 | 4 | 0 | 0 | 4 | 1 | 3 | 0 |
| Contractor Supervisor | External / counterparty | 0 | 4 | 3 | 0 | 4 | 0 | 3 | 1 |
| Customer Contact | External / counterparty | 0 | 4 | 0 | 0 | 4 | 4 | 0 | 0 |
| Drop-Ship Vendor | External / counterparty | 0 | 4 | 0 | 0 | 4 | 3 | 1 | 0 |
| DTI-BPS | External / counterparty | 0 | 3 | 2 | 0 | 4 | 2 | 1 | 1 |
| EAP Provider | External / counterparty | 0 | 3 | 3 | 0 | 4 | 1 | 3 | 0 |
| External Assurance Provider | External / counterparty | 0 | 4 | 0 | 0 | 4 | 1 | 1 | 2 |
| External Tp Advisor | External / counterparty | 0 | 2 | 4 | 1 | 4 | 4 | 0 | 0 |
| Forwarder | External / counterparty | 0 | 3 | 3 | 0 | 4 | 0 | 4 | 0 |
| General Contractor | External / counterparty | 0 | 4 | 0 | 0 | 4 | 0 | 1 | 3 |
| Insurer | External / counterparty | 0 | 4 | 0 | 0 | 4 | 1 | 3 | 0 |
| Lab | External / counterparty | 0 | 0 | 5 | 0 | 4 | 3 | 1 | 0 |
| LGU Officials | External / counterparty | 0 | 4 | 0 | 0 | 4 | 0 | 4 | 0 |
| Meralco | External / counterparty | 0 | 4 | 0 | 0 | 4 | 0 | 2 | 2 |
| Photographer | External / counterparty | 0 | 3 | 4 | 0 | 4 | 0 | 2 | 2 |
| PNP Anti-Cybercrime Group | External / counterparty | 0 | 4 | 0 | 0 | 4 | 1 | 3 | 0 |
| Regulators | External / counterparty | 0 | 4 | 0 | 0 | 4 | 3 | 0 | 1 |
| Shopper | External / counterparty | 0 | 1 | 6 | 0 | 4 | 0 | 4 | 0 |
| Site Mgrs | External / counterparty | 0 | 0 | 4 | 0 | 4 | 0 | 4 | 0 |
| Third Parties | External / counterparty | 0 | 4 | 0 | 0 | 4 | 0 | 4 | 0 |
| TVI Director | External / counterparty | 0 | 4 | 0 | 0 | 4 | 1 | 3 | 0 |
| Utility Providers | External / counterparty | 0 | 4 | 0 | 0 | 4 | 0 | 2 | 2 |
| Volunteers | External / counterparty | 0 | 4 | 3 | 0 | 4 | 0 | 4 | 0 |
| Assessors | External / counterparty | 0 | 2 | 1 | 0 | 3 | 0 | 3 | 0 |
| Authorities | External / counterparty | 0 | 3 | 0 | 0 | 3 | 2 | 1 | 0 |
| BIR RDO | External / counterparty | 0 | 3 | 2 | 0 | 3 | 3 | 0 | 0 |
| Capacity-Building Partner | External / counterparty | 0 | 3 | 3 | 0 | 3 | 0 | 3 | 0 |
| Cooperative Member | External / counterparty | 0 | 3 | 1 | 0 | 3 | 2 | 1 | 0 |
| Cooperative Treasurer | External / counterparty | 0 | 3 | 0 | 0 | 3 | 1 | 1 | 1 |
| Customer Site Representative | External / counterparty | 0 | 0 | 3 | 0 | 3 | 0 | 3 | 0 |
| DOH | External / counterparty | 0 | 3 | 0 | 0 | 3 | 1 | 2 | 0 |
| ERC | External / counterparty | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| External Actuary | External / counterparty | 0 | 3 | 0 | 0 | 3 | 0 | 2 | 1 |
| External Broker | External / counterparty | 0 | 0 | 3 | 0 | 3 | 0 | 1 | 2 |
| External Labs | External / counterparty | 0 | 3 | 0 | 0 | 3 | 0 | 2 | 1 |
| External Legal Counsel | External / counterparty | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| External Vendor | External / counterparty | 0 | 1 | 2 | 0 | 3 | 2 | 0 | 1 |
| Influencer | External / counterparty | 0 | 2 | 4 | 0 | 3 | 0 | 0 | 3 |
| Installation Partner Technician | External / counterparty | 0 | 3 | 0 | 0 | 3 | 2 | 1 | 0 |
| LGU Assessor | External / counterparty | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| MSME | External / counterparty | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Pag-Ibig | External / counterparty | 0 | 3 | 0 | 0 | 3 | 1 | 2 | 0 |
| Partner Bank Officer | External / counterparty | 0 | 3 | 2 | 0 | 3 | 1 | 2 | 0 |
| Registry Of Deeds | External / counterparty | 0 | 3 | 0 | 0 | 3 | 1 | 2 | 0 |
| Reinsurers | External / counterparty | 0 | 3 | 0 | 0 | 3 | 1 | 2 | 0 |
| Residents | External / counterparty | 0 | 2 | 1 | 0 | 3 | 0 | 3 | 0 |
| Screening Vendor | External / counterparty | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Security Guards | External / counterparty | 0 | 3 | 1 | 0 | 3 | 1 | 2 | 0 |
| Shipping Line | External / counterparty | 0 | 3 | 1 | 0 | 3 | 0 | 3 | 0 |
| Smart-Locker Vendor | External / counterparty | 0 | 3 | 2 | 0 | 3 | 0 | 3 | 0 |
| Surveyor | External / counterparty | 0 | 2 | 3 | 0 | 3 | 1 | 1 | 1 |
| Third-Party Auditor | External / counterparty | 0 | 3 | 3 | 0 | 3 | 0 | 3 | 0 |
| Third-Party Testing Laboratory | External / counterparty | 0 | 3 | 0 | 0 | 3 | 1 | 1 | 1 |
| Trading Partner | External / counterparty | 0 | 1 | 2 | 0 | 3 | 0 | 1 | 2 |
| Vendor Technician | External / counterparty | 0 | 0 | 7 | 0 | 3 | 1 | 2 | 0 |
| Waste Disposer | External / counterparty | 0 | 3 | 2 | 0 | 3 | 1 | 2 | 0 |
| Accredited Clinic | External / counterparty | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Accredited Contractor | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 2 |
| Accredited Lab | External / counterparty | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Acquiring Bank | External / counterparty | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Adjacent Landowners | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Applicant | External / counterparty | 0 | 1 | 2 | 0 | 2 | 0 | 2 | 0 |
| Appointed Actuary | External / counterparty | 0 | 1 | 2 | 0 | 2 | 0 | 2 | 0 |
| Barangay Officials | External / counterparty | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| BIR Officer | External / counterparty | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Cardholder | External / counterparty | 0 | 2 | 2 | 0 | 2 | 1 | 1 | 0 |
| Carriers | External / counterparty | 0 | 2 | 0 | 0 | 2 | 1 | 0 | 1 |
| Catering Provider | External / counterparty | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| CIT Guard | External / counterparty | 0 | 2 | 2 | 0 | 2 | 1 | 1 | 0 |
| Co-op Treasurer | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Collateral Registry | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Contractor MEP Engineer | External / counterparty | 0 | 1 | 4 | 0 | 2 | 1 | 1 | 0 |
| Contractor Site Engineer | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Contractor Site Supervisors | External / counterparty | 0 | 2 | 1 | 0 | 2 | 1 | 1 | 0 |
| Counterparty | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Customer Counterparts | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Customer PM | External / counterparty | 0 | 1 | 1 | 0 | 2 | 1 | 1 | 0 |
| Customer Site Engineer | External / counterparty | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Denr-Accredited Recycler | External / counterparty | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Denr-Certified Vendor | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Developer Attorney | External / counterparty | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Disposal Vendor | External / counterparty | 0 | 1 | 1 | 0 | 2 | 1 | 1 | 0 |
| Domiciliary Regulator | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Drop-Ship Vendor Coordinator | External / counterparty | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| DSWD | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Dti Inspector | External / counterparty | 0 | 1 | 1 | 0 | 2 | 1 | 0 | 1 |
| EAP Counselor | External / counterparty | 0 | 1 | 2 | 0 | 2 | 1 | 1 | 0 |
| Emergency Responders | External / counterparty | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| EMS | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Erp Vendor | External / counterparty | 0 | 0 | 2 | 0 | 2 | 2 | 0 | 0 |
| External Adjuster | External / counterparty | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| External Agency | External / counterparty | 0 | 1 | 1 | 0 | 2 | 0 | 0 | 2 |
| External Contractors | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| External Testing Laboratory | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| External Trainers | External / counterparty | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Fabrication Partner | External / counterparty | 0 | 1 | 3 | 0 | 2 | 0 | 2 | 0 |
| Family | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Family Member | External / counterparty | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| FILSCAP | External / counterparty | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| First Responder | External / counterparty | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| Gc | External / counterparty | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Gift Givers | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 2 |
| Government Partners | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Hazwaste Vendor | External / counterparty | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| Ic | External / counterparty | 0 | 1 | 1 | 0 | 2 | 1 | 1 | 0 |
| Industry Associations | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Industry Peers | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Installation Contractor | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| Installation Partner Manager | External / counterparty | 0 | 0 | 0 | 4 | 2 | 1 | 1 | 0 |
| Installation Partners | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| IPOPHL Agent | External / counterparty | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Jobsite Contact | External / counterparty | 0 | 0 | 4 | 0 | 2 | 0 | 2 | 0 |
| Key Vendors | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| LGU Inspector | External / counterparty | 0 | 1 | 1 | 0 | 2 | 1 | 1 | 0 |
| LGU Permit Officer | External / counterparty | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Local Electric Cooperative | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 2 |
| Locker Vendor Technician | External / counterparty | 0 | 1 | 1 | 0 | 2 | 1 | 1 | 0 |
| Locker Vendors | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Loss Adjuster | External / counterparty | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Marketplaces | External / counterparty | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Media Agency | External / counterparty | 0 | 0 | 3 | 0 | 2 | 0 | 1 | 1 |
| Medical Provider | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| MEP | External / counterparty | 0 | 2 | 4 | 0 | 2 | 0 | 2 | 0 |
| MEP Engineers | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 2 |
| MMDA | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Msme Partner | External / counterparty | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Municipal LGU | External / counterparty | 0 | 3 | 0 | 0 | 2 | 1 | 1 | 0 |
| Mystery Shopping Agency | External / counterparty | 0 | 2 | 5 | 0 | 2 | 0 | 1 | 1 |
| Mystery-Shopping Provider | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Nbi | External / counterparty | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| NCIP | External / counterparty | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| NGO Partner | External / counterparty | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| Notary | External / counterparty | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 0 |
| NSWMC Officer | External / counterparty | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| O&M Vendor | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Partner Bank Representative | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Partners | External / counterparty | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Payment Gateway Provider | External / counterparty | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Philippine National Police | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Port Authority | External / counterparty | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| POS Vendor | External / counterparty | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Print Vendor | External / counterparty | 0 | 2 | 3 | 0 | 2 | 0 | 2 | 0 |
| Pwd Customer | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Qsa | External / counterparty | 0 | 2 | 2 | 0 | 2 | 1 | 1 | 0 |
| Reblending Partner | External / counterparty | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 0 |
| Recycler | External / counterparty | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 2 |
| Red Cross | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Research Agency | External / counterparty | 0 | 1 | 3 | 0 | 2 | 0 | 0 | 2 |
| Security Agency | External / counterparty | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Service Provider | External / counterparty | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Sheriff | External / counterparty | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Site Foreman | External / counterparty | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| Solar Tech Support | External / counterparty | 0 | 2 | 6 | 0 | 2 | 0 | 1 | 1 |
| Speakers | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Subcontractors | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Surety / Bonds | External / counterparty | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Surety Companies | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Telematics Vendor | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 2 |
| Tenant | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Third-Party Inspector | External / counterparty | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Title Officer | External / counterparty | 0 | 1 | 3 | 0 | 2 | 0 | 2 | 0 |
| Trade Customer | External / counterparty | 0 | 2 | 2 | 0 | 2 | 1 | 1 | 0 |
| Transporter | External / counterparty | 0 | 0 | 2 | 0 | 2 | 1 | 1 | 0 |
| Trustee | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Tsd Transporter | External / counterparty | 0 | 2 | 2 | 0 | 2 | 2 | 0 | 0 |
| Underwriter | External / counterparty | 0 | 1 | 1 | 1 | 2 | 0 | 2 | 0 |
| Vendor Partners | External / counterparty | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Vendor Promodizer | External / counterparty | 0 | 2 | 1 | 0 | 2 | 1 | 1 | 0 |
| Vendor Technical Representative | External / counterparty | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Vendor Trainers | External / counterparty | 0 | 1 | 2 | 0 | 2 | 0 | 2 | 0 |
| Visitor | External / counterparty | 0 | 1 | 1 | 0 | 2 | 1 | 1 | 0 |
| VMI Vendor Coordinator | External / counterparty | 0 | 2 | 1 | 0 | 2 | 2 | 0 | 0 |
| Witnesses | External / counterparty | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Workout Manager | External / counterparty | 0 | 0 | 4 | 6 | 2 | 1 | 1 | 0 |
| Academic Institution | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Accessibility Auditor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Accredited Contractors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Accredited Recycler | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Accredited Recyclers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Accredited Stack Testing Firm | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Accredited Transporter | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Acquirer Relationship Manager | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Acquirers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| ACS | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| ACS Guard | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Actuarial Advisor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Advisers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Advisors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Affected Communities | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Affected Suppliers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Affected Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Agencies | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Aggregator | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Airport Authority | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Alarm-Monitoring Company | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| All Vendors | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Alternate Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| AMC | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Amr Vendor | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Arbitrator | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Architects | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Armored Car Driver | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Armored-Car Guard | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Armoured Car Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Assigned Visitor | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Assignment-Payroll Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Assignment-Tax Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| ASV | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Audit Firm | External / counterparty | 0 | 0 | 2 | 0 | 1 | 1 | 0 | 0 |
| Authorized Verifier | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| B2B Customers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Bank Branch | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Bank Escrow Auditor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Bank Inspector | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Bank Officer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Bank Scf Partner | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Bank Teller | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Bank Trust Representative | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Bankers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Barangay & LGU Officials | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Barangay Captain | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Barangay Captains | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Barangay Chairman | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Battery Recycler | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Battery Recycler Partner | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Battery Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| BERDE Assessor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| BFP Consultant | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| BFP Inspectors | External / counterparty | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Bfp-Licensed Inspector | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Bidder | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Bidders | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Biometric Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| BIR Liaison | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| BIR Officers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| BIR Relationship Officer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| BIR Revenue Officers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Bnpl Provider | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| BOC Inspector | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| BOC Officer | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| BPI | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Brokers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| BSP Regulators | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Builder | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| CAAP | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| CAAP Engineers | External / counterparty | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Card Networks | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Card Processor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Caretaker | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Catastrophe-Modeling Advisers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Catering Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| CCO | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| CDA Cooperative-Development Specialist | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| CDA Registration Officer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Cement Manufacturers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Certified Fire Protection Contractor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Channel Provider | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Charger Vendor | External / counterparty | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |
| Charity Partner | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| CIDG | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Circular Partner | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| CIT Partner | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| CIT Provider | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| City Engineer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| City Planning Officer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| City Treasurer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Claimants | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Cleaning Agency | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Clearing Officers | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Client | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Co-Op | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Co-op Board Secretary | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Co-op Secretary | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| COA | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Collective Management Societies | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Commercial Provider | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Compost Partner | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Computer Vision Vendor | External / counterparty | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Concessionaire-Contracted Isp | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Confirming Bank | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Consignment Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Consignment Vendor Coordinator | External / counterparty | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Consumers | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Contractor Foreman | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Contractor Representative | External / counterparty | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| Contractor Site Foreman | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Contractor Technician | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Cooperative | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Couriers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Csms Vendor | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Custom Fabricator | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Customer Procurement | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Customer Success (counterparty) | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Cylinder Disposal Partner | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| DAR Agrarian-Reform Officer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Dealer Partners | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Dealers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Deceased Employee'S Beneficiary | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| DENR Emergency Response | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| DENR Inspector | External / counterparty | 0 | 1 | 3 | 0 | 1 | 1 | 0 | 0 |
| DENR Land Management Bureau | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| DENR Partner | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Denr-Accredited Recyclers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| DENR-Accredited Treater | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| DENR-Accredited TSD | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Denr-Certified Lead Recycler | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Denr-Emb Inspectors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Denr-Emb-Accredited Transporter | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| DENR-LMS | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Design Consultants | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Destruction Vendor | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Developer Accountant | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Developer Procurement Manager | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Digital-Forensics Firm | External / counterparty | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Disbursement Bank | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Distribution Utility Technician | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| DOF | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Doh-Accredited Lab | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| DOLE Conciliator | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| DOLE Conciliator-Mediator | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| DOLE Inspector | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| DOLE Representative | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Dole-Accredited Drug Testing Laboratory | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Dole-Accredited Elevator Inspector | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Dole-Accredited Inspector | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| DOLE-Accredited Trainer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| DPWH | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| DRRMC Officers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Dti Inspectors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| DTI Representative | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Dti-Bps Inspector | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| DTI-BPS Officer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| E-Money Issuer Principal | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| E-Wallet Partner | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| ECC | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Electric Cooperative | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Electric Cooperatives | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Electrical Contractor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Elevator-Maintenance Contractor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| EMB Inspectors | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Embassy | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Emergency Hotline | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| EMSP | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Emsp Vendors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Entrance Monitor | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Ep-Trained Drivers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Epc Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Escrow Bank | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Ev-Charger Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Exhibit Vendor | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Existing Contractor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Express Courier | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| External Accountant | External / counterparty | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| External Appraiser | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| External Assessor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| External Assessors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Bank | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Bc Consultant | External / counterparty | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| External Benchmarking Firm | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| External Carriers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Cas Consultant | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| External Certification Body | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| External Certifier | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| External Commercial Advisors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Contractor | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| External Dealer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| External Dei Consultant | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| External DEI Trainer | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| External Director-Education Providers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External EAP Provider | External / counterparty | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| External Engineer | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| External Ergonomics Consultant | External / counterparty | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| External Financial-Education Provider | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Firm | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| External Grievance-Channel Providers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Human-Rights Advisors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Intelligence Provider | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External IOT Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| External IR Provider | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| External Lab | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| External Lawyer | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| External Leadership-Program & Coaching Providers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Medical Advisor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| External Mineral-Dd Providers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Monitor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External NGOS | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| External O&M Provider | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| External Party | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| External Pen-Test Firm | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| External Pen-Tester | External / counterparty | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| External Pentest Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| External Provider | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| External Providers | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| External Repair Shop | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| External Research Agency | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| External Retainer | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| External Risk-Intelligence Provider | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| External Security Agency | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| External T&A Partner | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Technicians | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Technology Partners | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| External Valuation Advisors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Valuer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| External Vendors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| External Vetting Firm | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| External Wage-Benchmark Providers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Factors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Factory | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Family Members | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Fda Inspectors | External / counterparty | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Fintech Partner | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Fire Vendor | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Fire-Protection Contractor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Fire-Safety Contractor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Fire-System Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Firm | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Foreman | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Forensics Retainer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Franchise Partner | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Fuel Card Provider | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Fuel Vendor | External / counterparty | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| Fund Manager | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Gas Station | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Gas Utility | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Generator Vendor | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Gift Giver | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Government | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Government Bureau | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Government Procurement Officer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Green-Building Advisor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| GS1 Philippines | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Guard Agencies | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Guard-Agency Manager | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Guard-Agency Supervisor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Guarding Provider | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hauling Vendors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hazwaste Transporter | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| HMO Provider Representative | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| HMO Providers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| HOA | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Home-Country Employer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hospital | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Host Partners | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Hvac Contractor | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| IDP Vendor | External / counterparty | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Incoming Provider | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Indoor Positioning Vendor | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Industry ORC Alliance | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Industry Partners | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Influencers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Inspection Firm | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Installation Partner Coordinator | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Installation Partner Supervisor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Installers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Installing Contractors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Insurance Adjuster | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Investment Bank | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Investment Manager | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Investment Managers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Investor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Investors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| IPOPHL | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Issuing Bank | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Janitorial Provider | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| JV General Manager | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| K&R Consultant | External / counterparty | 0 | 0 | 3 | 0 | 1 | 1 | 0 | 0 |
| K&R Insurer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Laboratory | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Lamp Recycler Partner | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Landfill | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Landlord Representative | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Landowner | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Laundry Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Lead Recycler | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Leed Assessor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Lender | External / counterparty | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Lender Servicing Manager | External / counterparty | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Lending Partner | External / counterparty | 0 | 1 | 3 | 0 | 1 | 0 | 0 | 1 |
| LGU DRRMO | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| LGU Electrical Inspector | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| LGU Processing Officer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| LGU Road Officials | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| LGU Traffic Enforcers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Licensed Contractor | External / counterparty | 0 | 1 | 3 | 0 | 1 | 0 | 1 | 0 |
| Licensed Disposal Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Licensed Engineer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Licensed Structural Engineer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Local Barangay Officials | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Local Courier | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Local Distributors | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Local Fixer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Local Fixers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Local Government | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Local Police | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Local Vendor | External / counterparty | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Local Vendors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Locksmith Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Loyalty Member | External / counterparty | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| LTFRB | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Mall Administration | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Marketplace Courier | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Medevac Provider | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Mediator | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Medical-Evac Provider | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Mentor Driver | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| MEP Inspector | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Mercury Drug | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Motor Vehicle Inspection Center | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Municipal Engineer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Municipal Treasurer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Music-Service Vendors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| MVIC Technician | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Mystery Shopping Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| NCDA | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| NCIP Elders | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| NCIP Representative | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| NCMB | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Neighbors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Next-in-Queue Renter | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| NGO | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| NGO Partners | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| NLRC | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Notary Public | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| NSWMC | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| NVOCC | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Occupant | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| OEM-Authorized Trainers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Off-Site Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Oil Re-Refinery Partner | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| On-Demand Courier | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Originator | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Originators | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Other Creditors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Own Drivers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Own-Fleet Driver | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Owner Agency | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Owner And Its Car Insurer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Paint Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Partner Bank Auditor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Partner Brands | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Partner Charity | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Partner Driver | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Partner Financier | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Partner NGOS | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Partner Representative | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Partner TVI Director | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Partner Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Payment Gateway Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| PCI QSA | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Pest-Control Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Physician | External / counterparty | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Platform Trust-&-Safety | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Plumbing Installation Subcontractor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Plumbing Subcontractor | External / counterparty | 0 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| PNP Traffic Investigator | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| PNP-ACG / CERT-PH | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| PNP-EOD | External / counterparty | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Pool Provider | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Port Liaison Officer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| PRC | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Principal | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Process Server | External / counterparty | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Promodizer | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Prosecutors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Prospective Franchisee | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Provincial Offices | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| PSPS | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| QA Inspector | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Qualified Person | External / counterparty | 0 | 1 | 3 | 1 | 1 | 1 | 0 | 0 |
| REC Registry | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Recovery Partners | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Recovery Technician | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Recycler Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Recyclers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Referred Contractor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Refill Vendor | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Refurb Partner | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Relationship Banks | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Retail Electricity Supplier | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Retail Electricity Suppliers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Returns Inspector | External / counterparty | 0 | 1 | 5 | 0 | 1 | 1 | 0 | 0 |
| Rfid Vendor | External / counterparty | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Rider Partners | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Roadside Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Roaming-Hub Partners | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| RORO Carrier | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Salvage Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Sangguniang Bayan | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sangguniang Panglungsod | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sanitation Office / Utility | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Scf Bank Partner | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Schools | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Screening Provider | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Security Agencies | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Security Equipment Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Security Guard Agency | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sellers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Sellers' Counsel | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Shipper | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Shoppers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Site Hosts | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Smart-Home Technician | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| SME Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Software Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Solo Parent Customer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Sponsor Vendors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| SPV | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| SSS Representative | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Storage Provider | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Strategic Vendors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Subtenant | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Supplier Representative | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Survey Providers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Technical Assessors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Technical Standards Officer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Technical Surveyor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Telco Partner | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Telecom | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Telecom Providers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Temporary Staffing Agency | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Tenant Farmers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Terminal Vendor | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| TESDA Assessor | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| TESDA Representative | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| TESDA-Qualified Mechanic | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Testing Laboratory | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| The Adjacent Contractor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Third-Party Auditors | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Third-Party Carriers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Third-Party Courier | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Third-Party Hauler | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Third-Party Inspection Agency | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Third-Party Insurer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Third-Party Lab | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| Third-Party Payee | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Third-Party Providers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Third-Party Risk-Data Providers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Third-Party Testing Lab | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| Third-Party Water Lab | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Third-Party Water Tanker Operator | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Tile Installation Subcontractor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Tile Subcontractor | External / counterparty | 0 | 0 | 3 | 0 | 1 | 0 | 1 | 0 |
| Tire Supplier | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Towing Operator | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Towing Vendor | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Trades Contractor | External / counterparty | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| Transfer-Pricing Advisor | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Transferee | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Transferor | External / counterparty | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| Travel Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Treater | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Treatment, Storage & Disposal Facility | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Truck Drivers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Trust Bank | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Trust Corporation | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| TVI Assessor | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Underwriters | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Union Representative | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Union Steward | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Utility Companies | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Utility Company | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Utility Partner Representative | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Utility Technician | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Valuer | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Vendor Co-op Advertising | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vendor Coordinator | External / counterparty | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 |
| Vendor Pm | External / counterparty | 0 | 0 | 4 | 0 | 1 | 0 | 1 | 0 |
| Vendor Product Managers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vendor Promodizers | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Vendor Relations Coordinator | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Vendor Sales Representative | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vendor Trainer | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vendor Verified Contacts | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Venue Security | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Verifier | External / counterparty | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| Vetting Firm | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| VMI Vendor | External / counterparty | 0 | 1 | 3 | 1 | 1 | 0 | 1 | 0 |
| VMI Vendor Representative | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Vp Customer | External / counterparty | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Wallet-Provider Relationship Manager | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Waste Hauler | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| Witness | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Worker-Voice Provider | External / counterparty | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Worker-Voice Technology Providers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |

