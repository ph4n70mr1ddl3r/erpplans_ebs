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
| Workflows mapped | 5427 (exactly one Owner each — asserted) |
| Confirmed Tier register | 5450 rows (Tier 1: 1396 · Tier 2: 3296 · Tier 3: 758) |
| Distinct resolved actors | 11151 — §5.3 register roles 93 · IT product-model seats 20 · store field 11 · DC field 8 · department-level actors 130 · system actors 9 · governance 7 · workforce 4 · external 40 · uncharted 10829 |

> Tier mix = confirmed tiers of the workflows a role touches (a workflow
> counts once per role regardless of how many steps mention it). HC is
> shown for §5.3 register roles; field rosters are per-store/per-DC and
> external/system actors carry no headcount by definition.

## §5.3 Enterprise Role Register (HQ roles)

| Role | Dept / source | HC | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|---|
| Chief Finance Officer (CFO) | Executive Office | 1 | 38 | 355 | 217 | 1725 | 1149 | 311 | 644 | 194 |
| Chief Operating Officer (COO) | Executive Office | 1 | 38 | 161 | 116 | 1025 | 655 | 103 | 393 | 159 |
| Chief Human Resources Officer (CHRO) | Executive Office | 1 | 25 | 86 | 63 | 591 | 332 | 72 | 211 | 49 |
| Chief Information Officer (CIO) | Executive Office | 1 | 22 | 88 | 60 | 530 | 306 | 68 | 182 | 56 |
| Chief Marketing Officer (CMO) | Executive Office | 1 | 22 | 72 | 68 | 349 | 221 | 21 | 130 | 70 |
| CEO / President | Executive Office | 1 | 7 | 110 | 46 | 639 | 451 | 86 | 261 | 104 |
| Treasury Manager | Finance & Accounting | 1 | 54 | 57 | 180 | 159 | 104 | 29 | 62 | 13 |
| VP Finance & Accounting / Corporate Controller | Finance & Accounting | 1 | 48 | 245 | 240 | 812 | 517 | 218 | 251 | 48 |
| Tax Manager | Finance & Accounting | 1 | 41 | 53 | 108 | 123 | 90 | 68 | 20 | 2 |
| Tax Accountant | Finance & Accounting | 4 | 39 | 62 | 194 | 25 | 83 | 66 | 16 | 1 |
| AR & Credit Manager | Finance & Accounting | 1 | 24 | 43 | 70 | 179 | 77 | 21 | 48 | 8 |
| Credit Analyst | Finance & Accounting | 2 | 23 | 61 | 130 | 13 | 82 | 27 | 49 | 6 |
| Treasury Analyst | Finance & Accounting | 3 | 20 | 61 | 202 | 20 | 83 | 53 | 24 | 6 |
| Revenue Assurance Lead | Finance & Accounting | 1 | 19 | 24 | 50 | 72 | 27 | 18 | 6 | 3 |
| AP Manager | Finance & Accounting | 1 | 17 | 33 | 60 | 30 | 40 | 18 | 20 | 2 |
| AR Supervisor | Finance & Accounting | 1 | 16 | 31 | 62 | 81 | 44 | 34 | 10 | 0 |
| AR Clerk | Finance & Accounting | 2 | 15 | 50 | 115 | 12 | 63 | 38 | 21 | 4 |
| Logistics & Cost Finance Analyst | Finance & Accounting | 3 | 15 | 4 | 24 | 14 | 16 | 5 | 7 | 4 |
| FP&A Analyst | Finance & Accounting | 3 | 12 | 20 | 34 | 2 | 27 | 8 | 8 | 11 |
| FP&A Manager | Finance & Accounting | 1 | 9 | 9 | 26 | 9 | 16 | 5 | 9 | 2 |
| AP Supervisor | Finance & Accounting | 2 | 5 | 17 | 25 | 63 | 41 | 23 | 17 | 1 |
| AP Clerk | Finance & Accounting | 13 | 3 | 66 | 99 | 4 | 85 | 41 | 37 | 7 |
| Collections Specialist | Finance & Accounting | 2 | 2 | 5 | 3 | 0 | 5 | 1 | 4 | 0 |
| Revenue Assurance Analyst | Finance & Accounting | 1 | 1 | 0 | 6 | 2 | 2 | 1 | 1 | 0 |
| GL Accountant (one per entity) | Finance & Accounting | 5 | 0 | 3 | 2 | 0 | 4 | 2 | 2 | 0 |
| Category Manager | Merchandising & Buying | 5 | 101 | 600 | 557 | 544 | 714 | 116 | 474 | 124 |
| VP for Merchandising | Merchandising & Buying | 1 | 55 | 182 | 112 | 909 | 535 | 87 | 347 | 101 |
| Pricing Analyst | Merchandising & Buying | 4 | 31 | 68 | 126 | 9 | 96 | 14 | 74 | 8 |
| Merchandise Planner / Allocator | Merchandising & Buying | 6 | 31 | 69 | 129 | 10 | 79 | 11 | 57 | 11 |
| Buyer (incl. Senior Buyers) | Merchandising & Buying | 10 | 20 | 123 | 188 | 35 | 145 | 52 | 84 | 9 |
| Merchandising Operations & Master Data Manager | Merchandising & Buying | 1 | 16 | 4 | 18 | 61 | 32 | 14 | 17 | 1 |
| Pricing Manager | Merchandising & Buying | 1 | 5 | 4 | 10 | 10 | 14 | 4 | 9 | 1 |
| VP Supply Chain & Logistics (dual-hat GM, BuildRight Logistics, Inc.) | Supply Chain & Logistics | 1 | 39 | 126 | 96 | 508 | 325 | 83 | 174 | 68 |
| Procurement Manager | Supply Chain & Logistics | 1 | 32 | 25 | 72 | 90 | 83 | 31 | 37 | 15 |
| Logistics Coordinator | Supply Chain & Logistics | 2 | 22 | 17 | 54 | 23 | 44 | 8 | 35 | 1 |
| DC Operations Manager | Supply Chain & Logistics | 1 | 20 | 26 | 24 | 55 | 55 | 22 | 29 | 4 |
| Import Coordinator | Supply Chain & Logistics | 2 | 15 | 38 | 60 | 15 | 50 | 25 | 22 | 3 |
| S&OP/IBP Lead | Supply Chain & Logistics | 1 | 12 | 19 | 17 | 85 | 32 | 13 | 16 | 3 |
| Vendor Management Manager | Supply Chain & Logistics | 1 | 5 | 0 | 0 | 13 | 9 | 2 | 5 | 2 |
| Customs Broker | Supply Chain & Logistics | 2 | 2 | 24 | 12 | 6 | 25 | 18 | 5 | 2 |
| Demand Planner | Supply Chain & Logistics | 2 | 2 | 8 | 22 | 2 | 10 | 6 | 2 | 2 |
| Inventory Planner | Supply Chain & Logistics | 2 | 1 | 2 | 3 | 0 | 5 | 2 | 3 | 0 |
| Compensation & Benefits Manager | Human Resources | 1 | 22 | 0 | 0 | 0 | 22 | 3 | 16 | 3 |
| Labor Relations Director | Human Resources | 1 | 15 | 0 | 4 | 3 | 15 | 8 | 6 | 1 |
| Payroll Manager | Human Resources | 1 | 11 | 14 | 26 | 48 | 29 | 18 | 10 | 1 |
| HR Business Partner (one per region) | Human Resources | 6 | 7 | 23 | 47 | 15 | 32 | 21 | 9 | 2 |
| VP Human Resources | Human Resources | 1 | 2 | 7 | 17 | 37 | 20 | 7 | 13 | 0 |
| Payroll Specialist | Human Resources | 4 | 2 | 8 | 19 | 4 | 11 | 6 | 5 | 0 |
| Benefits Specialist | Human Resources | 2 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| Marketplace Manager | Marketing | 2 | 19 | 0 | 1 | 42 | 20 | 3 | 16 | 1 |
| Loyalty & CRM Manager | Marketing | 1 | 16 | 20 | 38 | 32 | 28 | 2 | 18 | 8 |
| Digital Marketing Manager | Marketing | 3 | 15 | 17 | 38 | 10 | 24 | 0 | 12 | 12 |
| VP Marketing | Marketing | 1 | 6 | 43 | 15 | 164 | 108 | 9 | 69 | 30 |
| Marketing Operations Manager | Marketing | 1 | 5 | 0 | 0 | 2 | 5 | 1 | 4 | 0 |
| CRM Manager | Marketing | 1 | 4 | 4 | 6 | 16 | 10 | 3 | 2 | 5 |
| CRM Data Steward | Marketing | 2 | 2 | 4 | 9 | 4 | 4 | 3 | 1 | 0 |
| Consumer Insights Manager | Marketing | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| Campaign Manager | Marketing | 2 | 0 | 2 | 18 | 1 | 3 | 0 | 1 | 2 |
| Brand Manager | Marketing | 1 | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| VP Store Operations (Director Field Retail Operations) | Store Operations | 1 | 54 | 162 | 140 | 441 | 329 | 60 | 214 | 55 |
| Regional Manager | Store Operations | 6 | 10 | 57 | 75 | 146 | 128 | 50 | 65 | 13 |
| District Manager | Store Operations | 13 | 1 | 2 | 5 | 1 | 3 | 2 | 0 | 1 |
| VP Legal & Compliance | Legal & Compliance | 1 | 63 | 130 | 111 | 997 | 570 | 180 | 346 | 44 |
| Government Affairs Manager | Legal & Compliance | 1 | 38 | 24 | 55 | 17 | 38 | 2 | 33 | 3 |
| Corporate Secretary | Legal & Compliance | 1 | 27 | 38 | 87 | 8 | 48 | 16 | 27 | 5 |
| Compliance Analyst | Legal & Compliance | 1 | 12 | 0 | 12 | 3 | 12 | 7 | 5 | 0 |
| Litigation & IP Counsel | Legal & Compliance | 2 | 9 | 15 | 33 | 19 | 27 | 13 | 14 | 0 |
| Data Privacy Officer (DPO) | Legal & Compliance | 1 | 5 | 74 | 108 | 97 | 92 | 47 | 41 | 4 |
| Head of Internal Audit & Risk | Internal Audit & Risk | 1 | 5 | 7 | 43 | 178 | 99 | 9 | 48 | 42 |
| Internal Auditor | Internal Audit & Risk | 2 | 5 | 8 | 17 | 6 | 12 | 3 | 8 | 1 |
| Senior Internal Auditor | Internal Audit & Risk | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Customer Service Representative | Customer Service | 22 | 23 | 81 | 214 | 27 | 102 | 33 | 59 | 10 |
| Head of Customer Service | Customer Service | 1 | 0 | 0 | 4 | 15 | 6 | 0 | 5 | 1 |
| LP Analytics Analyst | Regional Loss Prevention | 2 | 11 | 30 | 86 | 9 | 46 | 19 | 20 | 7 |
| Regional LP Officer | Regional Loss Prevention | 20 | 4 | 33 | 52 | 16 | 43 | 24 | 18 | 1 |
| LP Investigator | Regional Loss Prevention | 2 | 1 | 5 | 17 | 0 | 7 | 4 | 2 | 1 |
| Safety Officer (HSE Officer, DOLE-accredited SO2) | Health, Safety & Environment | 10 | 18 | 73 | 103 | 52 | 97 | 48 | 41 | 8 |
| Company Nurse | Health, Safety & Environment | 1 | 0 | 1 | 2 | 0 | 2 | 1 | 1 | 0 |
| Wellness Coordinator | Health, Safety & Environment | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Head of Quality Management | Quality Management | 1 | 20 | 23 | 72 | 117 | 77 | 23 | 48 | 6 |
| Quality Inspector (Incoming Inspection) | Quality Management | 2 | 1 | 14 | 19 | 0 | 19 | 4 | 13 | 2 |
| Surety Program Manager | Facilities & Real Estate | 1 | 21 | 24 | 46 | 1 | 24 | 4 | 16 | 4 |
| Energy Manager | Facilities & Real Estate | 1 | 17 | 26 | 40 | 26 | 26 | 2 | 19 | 5 |
| Facilities Manager | Facilities & Real Estate | 2 | 13 | 19 | 58 | 18 | 35 | 4 | 17 | 14 |
| Lease Administrator | Facilities & Real Estate | 1 | 7 | 14 | 19 | 4 | 16 | 2 | 13 | 1 |
| Facilities Coordinator | Facilities & Real Estate | 3 | 5 | 25 | 32 | 21 | 33 | 10 | 22 | 1 |
| Director, Facilities & Real Estate (dual-hat GM, BuildRight Property Mgmt, Inc.) | Facilities & Real Estate | 1 | 5 | 0 | 0 | 0 | 5 | 0 | 4 | 1 |
| Head of Sustainability / ESG (Sustainability/ESG Manager) | Sustainability / ESG | 1 | 35 | 40 | 95 | 117 | 95 | 14 | 52 | 29 |
| Sustainability Coordinator | Sustainability / ESG | 1 | 14 | 25 | 58 | 0 | 40 | 2 | 28 | 10 |
| Competitive Intelligence Manager | Strategy / Corporate Planning | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| Trade Account Manager | Trade / Account Management | 2 | 20 | 45 | 82 | 12 | 49 | 11 | 33 | 5 |
| Key Account Manager | Trade / Account Management | 2 | 3 | 8 | 13 | 4 | 9 | 4 | 4 | 1 |
| Shift Supervisor (DC roster) | Information Technology (product model) | — | 6 | 32 | 46 | 129 | 77 | 38 | 38 | 1 |

## Information Technology product-model seats (§5.3 by reference)

| Role | Dept / source | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|
| SEC Security Engineer | Information Technology (product model) | 18 | 14 | 21 | 17 | 32 | 9 | 19 | 4 |
| AAP AI-Governance Liaison | Information Technology (product model) | 18 | 25 | 42 | 56 | 27 | 13 | 10 | 4 |
| DP BI Platform | Information Technology (product model) | 17 | 141 | 135 | 60 | 153 | 24 | 47 | 82 |
| SEC OT Security Lead | Information Technology (product model) | 13 | 0 | 27 | 75 | 24 | 4 | 17 | 3 |
| FS ITAM Administrator | Information Technology (product model) | 12 | 4 | 2 | 37 | 20 | 5 | 14 | 1 |
| Head of Enterprise Architecture (CIO Office) | Information Technology (product model) | 10 | 11 | 22 | 39 | 26 | 0 | 23 | 3 |
| DP / Data & Analytics (VS-28) | Information Technology (product model) | 8 | 91 | 89 | 0 | 125 | 7 | 48 | 70 |
| IT Operations (FS/INFRA) | Information Technology (product model) | 5 | 23 | 13 | 11 | 37 | 11 | 22 | 4 |
| SEC (Cybersecurity, Privacy & OT Security) | Information Technology (product model) | 2 | 149 | 61 | 1 | 159 | 50 | 100 | 9 |
| DP Data & Reporting Analyst | Information Technology (product model) | 2 | 7 | 20 | 1 | 17 | 2 | 6 | 9 |
| DP Data Scientist / ML | Information Technology (product model) | 2 | 6 | 20 | 4 | 11 | 0 | 2 | 9 |
| DP Data Engineer | Information Technology (product model) | 2 | 6 | 17 | 2 | 8 | 2 | 2 | 4 |
| IT Product Manager (build squad) | Information Technology (product model) | 2 | 1 | 2 | 6 | 3 | 0 | 2 | 1 |
| IT Helpdesk Agent (FS) | Information Technology (product model) | 1 | 20 | 38 | 1 | 26 | 14 | 11 | 1 |
| INFRA DBA / SaaS Administrator | Information Technology (product model) | 1 | 7 | 10 | 2 | 8 | 4 | 4 | 0 |
| DP Customer Data Platform | Information Technology (product model) | 0 | 0 | 0 | 68 | 23 | 1 | 15 | 7 |
| Information Technology (department) | Information Technology (product model) | 0 | 1 | 20 | 1 | 15 | 8 | 6 | 1 |
| SEC Security Analyst | Information Technology (product model) | 0 | 9 | 22 | 2 | 12 | 4 | 6 | 2 |
| INFRA Network Engineer | Information Technology (product model) | 0 | 6 | 14 | 0 | 10 | 4 | 4 | 2 |
| INFRA System Administrator | Information Technology (product model) | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |

## Store field roles (§7.2 roster)

| Role | Dept / source | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|
| Store Manager | Store (field, per-store roster) | 157 | 669 | 787 | 1107 | 933 | 337 | 508 | 88 |
| Department Supervisors | Store (field, per-store roster) | 107 | 186 | 241 | 476 | 287 | 82 | 183 | 22 |
| Customer Service Rep | Store (field, per-store roster) | 21 | 27 | 39 | 0 | 49 | 16 | 30 | 3 |
| Cashiers | Store (field, per-store roster) | 20 | 104 | 258 | 11 | 160 | 68 | 76 | 16 |
| Sales Associate | Store (field, per-store roster) | 17 | 235 | 606 | 67 | 256 | 51 | 175 | 30 |
| Assistant Store Manager | Store (field, per-store roster) | 9 | 14 | 6 | 15 | 22 | 11 | 10 | 1 |
| Stock Associate | Store (field, per-store roster) | 3 | 84 | 218 | 2 | 130 | 47 | 73 | 10 |
| Department Supervisor | Store (field, per-store roster) | 0 | 0 | 40 | 66 | 41 | 23 | 17 | 1 |
| Maintenance | Store (field, per-store roster) | 0 | 18 | 21 | 3 | 30 | 4 | 16 | 10 |
| ASM | Store (field, per-store roster) | 0 | 0 | 5 | 2 | 1 | 1 | 0 | 0 |
| Receiving lead | Store (field, per-store roster) | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |

## DC field roles (§7.3 roster)

| Role | Dept / source | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|
| Receiving Clerks | DC (field, per-DC roster) | 14 | 72 | 150 | 9 | 107 | 33 | 68 | 6 |
| DC Manager | DC (field, per-DC roster) | 9 | 79 | 52 | 137 | 131 | 55 | 59 | 17 |
| Forklift Operators (inbound) | DC (field, per-DC roster) | 0 | 15 | 7 | 0 | 15 | 5 | 8 | 2 |
| Putaway Staff | DC (field, per-DC roster) | 0 | 4 | 4 | 0 | 4 | 2 | 0 | 2 |
| Receiving Supervisor | DC (field, per-DC roster) | 0 | 3 | 5 | 1 | 4 | 3 | 1 | 0 |
| Dispatch Coordinators | DC (field, per-DC roster) | 0 | 1 | 6 | 4 | 2 | 1 | 0 | 1 |
| Shift Supervisors | DC (field, per-DC roster) | 0 | 1 | 5 | 0 | 2 | 1 | 1 | 0 |
| Cycle Counters | DC (field, per-DC roster) | 0 | 1 | 2 | 0 | 1 | 0 | 1 | 0 |

## Department-level actors (department or generic form named as performer)

| Role | Dept / source | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|
| Finance | Finance & Accounting | 46 | 996 | 598 | 38 | 1110 | 226 | 680 | 204 |
| Finance Analyst | Finance & Accounting | 29 | 60 | 143 | 5 | 106 | 29 | 54 | 23 |
| Treasury | Finance & Accounting | 21 | 242 | 153 | 4 | 274 | 82 | 165 | 27 |
| Finance Manager | Finance & Accounting | 21 | 78 | 71 | 283 | 197 | 81 | 98 | 18 |
| Fixed Asset Accountant | Finance & Accounting | 21 | 29 | 55 | 18 | 34 | 9 | 24 | 1 |
| Accounting Manager | Finance & Accounting | 13 | 42 | 43 | 123 | 82 | 32 | 47 | 3 |
| Chief Accountant | Finance & Accounting | 5 | 20 | 45 | 14 | 24 | 17 | 7 | 0 |
| Cost Accountant | Finance & Accounting | 3 | 21 | 48 | 12 | 32 | 18 | 13 | 1 |
| Ap | Finance & Accounting | 2 | 48 | 36 | 1 | 56 | 34 | 21 | 1 |
| Ar | Finance & Accounting | 2 | 49 | 25 | 2 | 51 | 27 | 21 | 3 |
| Insurance | Finance & Accounting | 1 | 92 | 38 | 0 | 100 | 32 | 64 | 4 |
| Fraud Management Lead | Finance & Accounting | 0 | 1 | 0 | 64 | 23 | 15 | 8 | 0 |
| Revenue Assurance | Finance & Accounting | 0 | 17 | 11 | 0 | 19 | 3 | 14 | 2 |
| Credit | Finance & Accounting | 0 | 6 | 2 | 0 | 8 | 0 | 8 | 0 |
| Collections | Finance & Accounting | 0 | 5 | 1 | 0 | 5 | 2 | 3 | 0 |
| Accounting | Finance & Accounting | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Merchandising | Merchandising & Buying | 15 | 263 | 97 | 1 | 290 | 39 | 195 | 56 |
| Pricing | Merchandising & Buying | 6 | 58 | 58 | 0 | 68 | 8 | 46 | 14 |
| Master Data Analyst | Merchandising & Buying | 1 | 35 | 67 | 0 | 36 | 9 | 27 | 0 |
| Buyers | Merchandising & Buying | 1 | 26 | 17 | 0 | 30 | 4 | 21 | 5 |
| Category | Merchandising & Buying | 1 | 21 | 5 | 0 | 23 | 2 | 16 | 5 |
| Visual Merchandising | Merchandising & Buying | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Planogram | Merchandising & Buying | 0 | 3 | 0 | 0 | 3 | 0 | 3 | 0 |
| Logistics Manager | Supply Chain & Logistics | 35 | 53 | 103 | 171 | 137 | 25 | 89 | 23 |
| Logistics | Supply Chain & Logistics | 20 | 147 | 102 | 1 | 158 | 42 | 99 | 17 |
| Procurement | Supply Chain & Logistics | 17 | 308 | 222 | 6 | 346 | 48 | 244 | 54 |
| Supply Planning Manager | Supply Chain & Logistics | 12 | 21 | 44 | 49 | 42 | 19 | 17 | 6 |
| Procurement Director | Supply Chain & Logistics | 10 | 16 | 5 | 38 | 24 | 3 | 20 | 1 |
| Supply Planning | Supply Chain & Logistics | 9 | 82 | 65 | 0 | 91 | 14 | 56 | 21 |
| Fleet Manager | Supply Chain & Logistics | 8 | 18 | 42 | 34 | 27 | 10 | 9 | 8 |
| Procurement Specialist | Supply Chain & Logistics | 7 | 24 | 32 | 23 | 31 | 6 | 24 | 1 |
| Supply Planner | Supply Chain & Logistics | 6 | 37 | 57 | 5 | 47 | 19 | 24 | 4 |
| Import | Supply Chain & Logistics | 3 | 17 | 9 | 0 | 20 | 11 | 7 | 2 |
| Dc Operations | Supply Chain & Logistics | 2 | 45 | 11 | 3 | 49 | 19 | 28 | 2 |
| Fleet | Supply Chain & Logistics | 2 | 32 | 12 | 0 | 34 | 7 | 23 | 4 |
| Inventory | Supply Chain & Logistics | 1 | 46 | 20 | 0 | 47 | 17 | 28 | 2 |
| Dc Ops | Supply Chain & Logistics | 0 | 90 | 29 | 0 | 92 | 15 | 65 | 12 |
| Vendor Mgmt | Supply Chain & Logistics | 0 | 62 | 47 | 0 | 66 | 23 | 38 | 5 |
| Customs | Supply Chain & Logistics | 0 | 17 | 5 | 0 | 18 | 5 | 10 | 3 |
| Warehouse | Supply Chain & Logistics | 0 | 4 | 1 | 0 | 4 | 1 | 0 | 3 |
| Imports | Supply Chain & Logistics | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| It | Information Technology | 11 | 345 | 206 | 1 | 416 | 115 | 267 | 34 |
| Hr Manager | Human Resources | 24 | 41 | 83 | 110 | 89 | 36 | 43 | 10 |
| Hr | Human Resources | 15 | 359 | 172 | 10 | 393 | 89 | 256 | 48 |
| L&D | Human Resources | 5 | 65 | 27 | 0 | 70 | 4 | 59 | 7 |
| Recruiting | Human Resources | 0 | 12 | 2 | 0 | 12 | 0 | 12 | 0 |
| Training | Human Resources | 0 | 8 | 5 | 0 | 10 | 1 | 9 | 0 |
| Hris | Human Resources | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Sales Enablement | Marketing | 23 | 33 | 63 | 0 | 35 | 1 | 26 | 8 |
| Marketing Manager | Marketing | 18 | 27 | 47 | 50 | 48 | 5 | 25 | 18 |
| Market Research Analyst | Marketing | 16 | 23 | 43 | 4 | 23 | 1 | 12 | 10 |
| Marketing | Marketing | 2 | 225 | 115 | 3 | 254 | 18 | 184 | 52 |
| Insights | Marketing | 2 | 65 | 17 | 0 | 68 | 7 | 41 | 20 |
| Crm | Marketing | 1 | 25 | 9 | 1 | 27 | 4 | 16 | 7 |
| Event Marketing Mgr | Marketing | 0 | 0 | 34 | 53 | 24 | 1 | 22 | 1 |
| Sales Enablement Lead | Marketing | 0 | 0 | 0 | 60 | 22 | 0 | 14 | 8 |
| Retail Media | Marketing | 0 | 13 | 1 | 0 | 13 | 1 | 12 | 0 |
| Marketing Ops | Marketing | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 0 |
| Rental Fleet Manager | Store Operations | 9 | 10 | 32 | 24 | 16 | 4 | 8 | 4 |
| Store Ops | Store Operations | 5 | 362 | 103 | 0 | 375 | 65 | 265 | 45 |
| Stores | Store Operations | 5 | 17 | 14 | 0 | 26 | 4 | 22 | 0 |
| Services Manager | Store Operations | 3 | 10 | 13 | 45 | 22 | 9 | 9 | 4 |
| Store Operations | Store Operations | 1 | 40 | 11 | 2 | 45 | 10 | 29 | 6 |
| Store | Store Operations | 0 | 47 | 19 | 30 | 57 | 21 | 28 | 8 |
| Operations | Store Operations | 0 | 2 | 3 | 0 | 4 | 0 | 4 | 0 |
| Compliance Officer | Legal & Compliance | 30 | 27 | 79 | 102 | 86 | 41 | 39 | 6 |
| Legal | Legal & Compliance | 18 | 806 | 427 | 27 | 863 | 256 | 558 | 49 |
| Legal Counsel | Legal & Compliance | 14 | 96 | 94 | 49 | 139 | 59 | 67 | 13 |
| Ethics & Compliance Officer | Legal & Compliance | 14 | 24 | 41 | 58 | 24 | 7 | 13 | 4 |
| Compliance Specialist | Legal & Compliance | 13 | 9 | 54 | 42 | 24 | 15 | 9 | 0 |
| Compliance | Legal & Compliance | 9 | 313 | 215 | 9 | 342 | 102 | 215 | 25 |
| Trade Compliance Manager | Legal & Compliance | 8 | 1 | 1 | 45 | 23 | 13 | 10 | 0 |
| Privacy | Legal & Compliance | 3 | 106 | 22 | 2 | 108 | 34 | 69 | 5 |
| Records | Legal & Compliance | 1 | 52 | 18 | 0 | 53 | 26 | 27 | 0 |
| Internal Audit | Internal Audit & Risk | 32 | 152 | 74 | 18 | 190 | 53 | 91 | 46 |
| Risk | Internal Audit & Risk | 9 | 120 | 58 | 0 | 129 | 24 | 85 | 20 |
| Audit | Internal Audit & Risk | 5 | 122 | 57 | 0 | 135 | 38 | 78 | 19 |
| Auditor | Internal Audit & Risk | 0 | 3 | 125 | 0 | 31 | 0 | 3 | 28 |
| Customer Service Manager | Customer Service | 16 | 17 | 10 | 36 | 39 | 10 | 26 | 3 |
| Cs Manager | Customer Service | 1 | 9 | 35 | 34 | 14 | 2 | 11 | 1 |
| Cx | Customer Service | 0 | 95 | 28 | 0 | 98 | 14 | 64 | 20 |
| Customer Service | Customer Service | 0 | 80 | 36 | 1 | 86 | 34 | 45 | 7 |
| Lp Manager | Regional Loss Prevention | 12 | 30 | 58 | 106 | 73 | 30 | 35 | 8 |
| Loss Prevention | Regional Loss Prevention | 8 | 44 | 19 | 0 | 52 | 22 | 24 | 6 |
| Lp | Regional Loss Prevention | 0 | 114 | 60 | 2 | 128 | 41 | 77 | 10 |
| Occupational Health | Health, Safety & Environment | 8 | 37 | 23 | 0 | 37 | 11 | 24 | 2 |
| Hse | Health, Safety & Environment | 5 | 205 | 85 | 0 | 212 | 52 | 147 | 13 |
| Safety | Health, Safety & Environment | 0 | 10 | 2 | 0 | 11 | 2 | 8 | 1 |
| Product Compliance Manager | Quality Management | 19 | 24 | 51 | 61 | 24 | 19 | 3 | 2 |
| Quality | Quality Management | 7 | 170 | 57 | 0 | 174 | 42 | 116 | 16 |
| Real Estate | Facilities & Real Estate | 6 | 69 | 25 | 0 | 71 | 3 | 55 | 13 |
| Ifm | Facilities & Real Estate | 2 | 34 | 8 | 0 | 34 | 2 | 30 | 2 |
| Facilities | Facilities & Real Estate | 0 | 132 | 67 | 1 | 148 | 30 | 103 | 15 |
| Facilities & Real Estate | Facilities & Real Estate | 0 | 26 | 20 | 115 | 56 | 7 | 39 | 10 |
| Engineering | Facilities & Real Estate | 0 | 26 | 1 | 0 | 27 | 4 | 15 | 8 |
| Sustainability | Sustainability / ESG | 1 | 80 | 64 | 1 | 85 | 11 | 52 | 22 |
| Esg | Sustainability / ESG | 0 | 43 | 12 | 0 | 45 | 5 | 27 | 13 |
| Pmo | Strategy / Corporate Planning | 19 | 73 | 65 | 2 | 82 | 3 | 69 | 10 |
| Strategy | Strategy / Corporate Planning | 3 | 128 | 42 | 0 | 134 | 8 | 81 | 45 |
| Sponsor | Strategy / Corporate Planning | 0 | 20 | 14 | 39 | 34 | 0 | 30 | 4 |
| Account Manager | Trade / Account Management | 22 | 40 | 70 | 3 | 47 | 1 | 37 | 9 |
| Trade Sales Manager | Trade / Account Management | 16 | 16 | 43 | 29 | 42 | 9 | 28 | 5 |
| Head Of Strategic Accounts | Trade / Account Management | 8 | 8 | 13 | 45 | 23 | 0 | 17 | 6 |
| Trade Sales | Trade / Account Management | 2 | 52 | 18 | 0 | 56 | 12 | 40 | 4 |
| Head Of Trade / Account Management | Trade / Account Management | 2 | 24 | 1 | 66 | 55 | 4 | 39 | 12 |
| Trade | Trade / Account Management | 0 | 33 | 3 | 0 | 34 | 6 | 23 | 5 |
| Trade Capability Lead | Trade / Account Management | 0 | 0 | 0 | 60 | 22 | 4 | 15 | 3 |
| B2B | Trade / Account Management | 0 | 4 | 1 | 0 | 4 | 2 | 2 | 0 |
| Fp&A | Finance & Accounting (FP&A) | 31 | 145 | 156 | 13 | 172 | 11 | 105 | 56 |
| Data Protection Officer | Data Privacy Officer (DPO) | 26 | 9 | 3 | 5 | 38 | 22 | 16 | 0 |
| Ecommerce Operations Manager | Digital Commerce (IT-built platforms) | 24 | 4 | 3 | 41 | 33 | 12 | 19 | 2 |
| Project Manager | Strategy / Corporate Planning (PMO) | 16 | 36 | 57 | 11 | 46 | 2 | 36 | 8 |
| Global Sourcing | Merchandising & Buying (Direct Sourcing) | 13 | 31 | 53 | 0 | 33 | 5 | 25 | 3 |
| Digital Product Manager | Digital Commerce (IT-built platforms) | 13 | 11 | 36 | 5 | 24 | 3 | 14 | 7 |
| Ecommerce Manager | Digital Commerce (IT-built platforms) | 11 | 15 | 27 | 36 | 28 | 4 | 17 | 7 |
| Regulatory Officer | Regulatory Affairs Specialist | 8 | 24 | 74 | 11 | 34 | 19 | 14 | 1 |
| Tax | Finance & Accounting (Tax) | 4 | 79 | 34 | 0 | 88 | 29 | 56 | 3 |
| Data Science | DP Data Scientist / ML | 4 | 34 | 12 | 0 | 36 | 13 | 15 | 8 |
| Ecommerce | Digital Commerce (IT-built platforms) | 3 | 111 | 24 | 0 | 116 | 27 | 73 | 16 |
| Loyalty | Marketing (Loyalty) | 2 | 53 | 11 | 0 | 53 | 14 | 28 | 11 |
| Department Head | Generic / cross-department | 2 | 27 | 27 | 24 | 47 | 15 | 26 | 6 |
| Master Data | Merchandising & Buying (Master Data) | 2 | 39 | 16 | 0 | 43 | 14 | 28 | 1 |
| Department Heads | Generic / cross-department | 1 | 33 | 12 | 3 | 41 | 15 | 21 | 5 |
| Director | Generic / cross-department | 0 | 26 | 41 | 129 | 60 | 8 | 42 | 10 |
| Gm | Generic / cross-department | 0 | 6 | 7 | 71 | 51 | 7 | 32 | 12 |
| Digital Commerce Inc | Digital Commerce (IT-built platforms) | 0 | 5 | 7 | 72 | 50 | 7 | 31 | 12 |
| Payroll | Human Resources (Payroll) | 0 | 43 | 15 | 1 | 45 | 14 | 31 | 0 |
| Vp Merch | VP for Merchandising | 0 | 10 | 3 | 43 | 38 | 2 | 25 | 11 |
| Govt Affairs | Government Affairs Manager | 0 | 35 | 41 | 0 | 36 | 7 | 27 | 2 |
| Management | Generic / cross-department | 0 | 4 | 1 | 0 | 4 | 1 | 3 | 0 |

## System & automated actors

| Role | Dept / source | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|
| System | System & automated actors | 3 | 29 | 2078 | 5 | 1046 | 354 | 543 | 149 |
| Pos System | System & automated actors | 3 | 1 | 5 | 0 | 6 | 3 | 3 | 0 |
| Pos | System & automated actors | 2 | 24 | 9 | 0 | 28 | 16 | 8 | 4 |
| Wms | System & automated actors | 0 | 3 | 7 | 0 | 8 | 4 | 4 | 0 |
| Agent | System & automated actors | 0 | 0 | 3 | 0 | 3 | 1 | 2 | 0 |
| Erp System | System & automated actors | 0 | 0 | 4 | 0 | 3 | 2 | 1 | 0 |
| Iap | System & automated actors | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 |
| Platform | System & automated actors | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Automation | System & automated actors | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |

## Governance bodies

| Role | Dept / source | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|
| Board | Governance bodies | 1 | 54 | 18 | 148 | 156 | 26 | 97 | 33 |
| Audit Committee | Governance bodies | 0 | 6 | 1 | 70 | 56 | 8 | 35 | 13 |
| Board Audit Committee | Governance bodies | 0 | 11 | 1 | 31 | 34 | 11 | 17 | 6 |
| Board Of Directors | Governance bodies | 0 | 12 | 0 | 3 | 15 | 2 | 5 | 8 |
| Exco | Governance bodies | 0 | 9 | 0 | 0 | 9 | 0 | 2 | 7 |
| Executive Committee | Governance bodies | 0 | 8 | 0 | 0 | 8 | 2 | 4 | 2 |
| Board Risk Committee | Governance bodies | 0 | 3 | 0 | 4 | 6 | 0 | 5 | 1 |

## Generic workforce mentions

| Role | Dept / source | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|
| Employee | Workforce (generic) | 0 | 48 | 46 | 1 | 66 | 42 | 21 | 3 |
| Employees | Workforce (generic) | 0 | 13 | 0 | 0 | 13 | 2 | 11 | 0 |
| New Hire | Workforce (generic) | 0 | 1 | 2 | 0 | 3 | 1 | 2 | 0 |
| Staff | Workforce (generic) | 0 | 0 | 2 | 0 | 2 | 1 | 1 | 0 |

## External counterparties (not staff)

| Role | Dept / source | Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |
|---|---|---|---|---|---|---|---|---|---|
| Driver | External / counterparty | 2 | 29 | 60 | 2 | 56 | 17 | 32 | 7 |
| Customer | External / counterparty | 1 | 435 | 237 | 26 | 458 | 95 | 307 | 56 |
| Vendor | External / counterparty | 1 | 194 | 100 | 4 | 232 | 63 | 148 | 21 |
| Security Guard (contracted) | External / counterparty | 1 | 34 | 63 | 1 | 38 | 16 | 22 | 0 |
| Supplier | External / counterparty | 1 | 29 | 3 | 0 | 30 | 6 | 23 | 1 |
| External Auditor | External / counterparty | 0 | 61 | 23 | 5 | 69 | 26 | 38 | 5 |
| Contractor | External / counterparty | 0 | 41 | 29 | 0 | 55 | 4 | 44 | 7 |
| 3Pl | External / counterparty | 0 | 27 | 10 | 0 | 31 | 8 | 20 | 3 |
| Carrier | External / counterparty | 0 | 21 | 13 | 0 | 27 | 11 | 15 | 1 |
| Bank | External / counterparty | 0 | 21 | 11 | 1 | 26 | 13 | 11 | 2 |
| Vendors | External / counterparty | 0 | 23 | 2 | 0 | 24 | 1 | 20 | 3 |
| Dole | External / counterparty | 0 | 18 | 1 | 0 | 18 | 14 | 3 | 1 |
| Lgu | External / counterparty | 0 | 15 | 2 | 0 | 17 | 7 | 10 | 0 |
| Bir | External / counterparty | 0 | 11 | 2 | 0 | 12 | 8 | 4 | 0 |
| Delivery Partner | External / counterparty | 0 | 11 | 4 | 0 | 12 | 4 | 8 | 0 |
| Bfp | External / counterparty | 0 | 10 | 1 | 0 | 11 | 9 | 2 | 0 |
| 3Pl Carrier | External / counterparty | 0 | 10 | 1 | 0 | 10 | 9 | 0 | 1 |
| Vendor Representative | External / counterparty | 0 | 7 | 5 | 0 | 9 | 1 | 5 | 3 |
| Denr | External / counterparty | 0 | 8 | 0 | 0 | 8 | 5 | 2 | 1 |
| Financing Partner | External / counterparty | 0 | 5 | 3 | 0 | 7 | 2 | 3 | 2 |
| Contractors | External / counterparty | 0 | 6 | 0 | 0 | 6 | 0 | 6 | 0 |
| Sss | External / counterparty | 0 | 6 | 0 | 0 | 6 | 2 | 4 | 0 |
| Concessionaire | External / counterparty | 0 | 5 | 6 | 0 | 5 | 1 | 3 | 1 |
| Courier | External / counterparty | 0 | 2 | 6 | 0 | 5 | 2 | 2 | 1 |
| Landlord | External / counterparty | 0 | 4 | 1 | 0 | 5 | 1 | 4 | 0 |
| Suppliers | External / counterparty | 0 | 5 | 0 | 0 | 5 | 0 | 5 | 0 |
| Banks | External / counterparty | 0 | 4 | 0 | 0 | 4 | 1 | 2 | 1 |
| Customers | External / counterparty | 0 | 4 | 0 | 0 | 4 | 1 | 1 | 2 |
| Pag-Ibig | External / counterparty | 0 | 3 | 0 | 0 | 3 | 1 | 2 | 0 |
| Philhealth | External / counterparty | 0 | 3 | 0 | 0 | 3 | 2 | 1 | 0 |
| Shopper | External / counterparty | 0 | 1 | 5 | 0 | 3 | 0 | 3 | 0 |
| Acquirer | External / counterparty | 0 | 2 | 0 | 0 | 2 | 1 | 1 | 0 |
| Applicant | External / counterparty | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Erp Vendor | External / counterparty | 0 | 0 | 2 | 0 | 2 | 2 | 0 | 0 |
| Qsa | External / counterparty | 0 | 2 | 1 | 0 | 2 | 1 | 1 | 0 |
| Service Provider | External / counterparty | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 0 |
| Carriers | External / counterparty | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| Lender | External / counterparty | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| Software Vendor | External / counterparty | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Supplier Representative | External / counterparty | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |

## Uncharted titles (vocabulary-drift watchlist)

10829 distinct uncharted forms; the 60 with the widest workflow
coverage are listed — the remaining tail is aggregated below. This table
is the role-vocabulary drift watchlist: promote recurring forms into the
canonical vocabulary (or the alias tables) via the normal governance.

| Form | Touched | T1 | T2 | T3 |
|---|---|---|---|---|
| Cost Accounting Manager (Controller org) | 21 | 4 | 16 | 1 |
| Revenue Accounting Manager (Controller org) | 20 | 3 | 16 | 1 |
| Merchandising Planner | 28 | 1 | 23 | 4 |
| Analytics Manager | 26 | 1 | 8 | 17 |
| IT Infrastructure Manager | 19 | 6 | 12 | 1 |
| Dark Store Operations Manager | 17 | 4 | 10 | 3 |
| Sustainability Sourcing Manager | 13 | 2 | 11 | 0 |
| Payment Operations Manager (acquirer & card-brand liaison, W1205 PCI forensic engagement) | 19 | 5 | 12 | 2 |
| TPRM Program Manager | 15 | 3 | 12 | 0 |
| Lumber & Building Materials Department Supervisor | 12 | 2 | 10 | 0 |
| Merchandising Coordinator | 16 | 2 | 14 | 0 |
| MSME Sales Manager | 16 | 2 | 14 | 0 |
| Project Consultant | 19 | 0 | 19 | 0 |
| Quality Assurance Manager | 16 | 4 | 11 | 1 |
| Trade Compliance Specialist | 11 | 7 | 4 | 0 |
| Trade Sales Representative | 11 | 1 | 9 | 1 |
| Head of Internal Audit | 26 | 2 | 17 | 7 |
| Legal Compliance Officer | 16 | 7 | 8 | 1 |
| Inventory Control Manager | 13 | 6 | 7 | 0 |
| Sustainability/ESG Manager / VP Supply Chain | 10 | 2 | 6 | 2 |
| HR Shared Services Manager | 9 | 0 | 7 | 2 |
| Legal Operations Manager | 9 | 0 | 7 | 2 |
| B2B Sales Manager | 10 | 1 | 8 | 1 |
| Customer Experience Manager | 10 | 0 | 7 | 3 |
| Regulatory Compliance Officer | 10 | 9 | 1 | 0 |
| IT Integration Lead (VS-113) | 9 | 1 | 7 | 1 |
| Software Asset Manager | 9 | 2 | 6 | 1 |
| Dark Store Shift Supervisor | 8 | 5 | 2 | 1 |
| OH Nurse (VS-83) | 24 | 9 | 15 | 0 |
| CIT Operations Manager | 10 | 2 | 5 | 3 |
| Product Safety & Compliance Manager | 10 | 7 | 2 | 1 |
| Solar Sales Coordinator | 10 | 1 | 9 | 0 |
| Digital Commerce Manager | 9 | 0 | 5 | 4 |
| Risk & Insurance Manager | 9 | 1 | 8 | 0 |
| Corporate Controller | 8 | 6 | 2 | 0 |
| Loss Prevention Manager | 8 | 2 | 4 | 2 |
| Contingent Workforce Manager | 7 | 0 | 5 | 2 |
| Electrical Department Supervisor | 7 | 0 | 5 | 2 |
| Store Cashier Lead | 7 | 2 | 4 | 1 |
| Take-Back Counter Associate | 7 | 3 | 4 | 0 |
| OH Nurse Manager | 19 | 6 | 12 | 1 |
| Project Accountant | 12 | 3 | 9 | 0 |
| IP Counsel | 10 | 0 | 9 | 1 |
| Fleet Supervisor | 9 | 0 | 8 | 1 |
| Lease Operations Manager | 8 | 2 | 6 | 0 |
| TPRM Program Manager / Head of Internal Audit & Risk | 8 | 0 | 6 | 2 |
| EEO / Sustainability | 7 | 0 | 4 | 3 |
| Contingent Workforce Coordinator (VS-98) | 6 | 2 | 4 | 0 |
| Employee Experience Manager | 6 | 0 | 5 | 1 |
| Lease Origination Manager | 6 | 0 | 6 | 0 |
| People Analytics Manager | 6 | 0 | 2 | 4 |
| HSE Manager (sanitation decisions, VS-24) | 21 | 15 | 6 | 0 |
| Content Manager | 13 | 3 | 6 | 4 |
| DC Returns Coordinator | 12 | 4 | 8 | 0 |
| Legal & Compliance Officer | 11 | 3 | 8 | 0 |
| Training Manager (R for BuildRight training) | 11 | 2 | 9 | 0 |
| Customer Service Agent | 10 | 2 | 8 | 0 |
| Service Coordinator | 10 | 2 | 8 | 0 |
| AR Analyst | 9 | 3 | 6 | 0 |
| HR Compliance Manager | 9 | 4 | 5 | 0 |

Tail: 10769 further forms, 18399 aggregated touches (each form
touches fewer workflows than the last row above).

