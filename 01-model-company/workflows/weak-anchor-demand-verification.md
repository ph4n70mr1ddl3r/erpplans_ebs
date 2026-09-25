# Weak-Anchor Demand Verification (generated — batch 50, 2026-09-25)

> **Verification record** for the Role-Anchoring Contract's weak-anchor watchlist — the
> 53 chartered roles anchored in only 1–2 workflows. Per the contract, no headcount
> or structure decision may touch a weak-anchor role until its per-role annual demand is
> verified against chartered capacity. Instrument: `virtual-gemba-walk.py motion --full`
> (per-role annual demand hours from the corpus's own step durations × event cadence vs
> chartered TO capacity; 1,800/1,900 net productive hours; frequency-parse coverage 93% at generation).
> Batches 39–41 elevated nineteen roles into Role (R) cells; batch 42 re-anchored the T&A
> Analyst off a store-scaled step onto its true HQ platform step; batch 43 classified the
> residual. **Batch 49 (2026-09-25) re-derived every figure after two measurement defects
> were fixed** — (1) the engine's parse_minutes read every plural unit form ('2 hours',
> '4 hrs', '24 hours/year') as zero minutes (3,775 corpus duration cells re-measured; 20
> batch-39–47 step-elevated roles had been misclassified as unmeasurable), and (2) this
> tool's dump parser silently dropped rows with thousands-separated utilizations — and
> added the EXERCISED-THROUGH arm: roles whose named cells attribute to the broader/deputy
> seats their cells resolve to (the corpus's exercise-through-broader-titles contract) are
> now measured at their claimed share instead of reported empty. **Batch 50 (2026-09-25, wave
> 7)** elevated the twelve participant-only roles that had a mandate-exact step (PA-04.1/.2/.3,
> PA-10.1, PA-27.2, PA-110.3, PA-113.1, PA-133.1, PA-138.2) and added the MEASURED — CAPACITY
> UNMAPPED arm for seats whose own-key demand prices against no mapped HC (the IT product-model
> seats the TO carries by reference; the ASM alias gap). Generated — do not hand-edit.

## Verdict legend

| Verdict | Meaning | Action |
|---|---|---|
| CONFIRMED | parsed demand 50–150% of chartered capacity | role stays as chartered |
| OVERLOAD | parsed demand > 150% of capacity | capacity decision — the demand is real |
| UNDER-UTILIZED | parsed demand < 50% | merge/defer/resize candidate |
| EXERCISED-THROUGH | the role's own key carries no engine demand, but its named step cells do — attributed to the broader/deputy seats the cells resolve to | demand shown is the role's claimed share of its named cells (band vs its own charter); verify the via-group before any seat decision |
| MEASURED — CAPACITY UNMAPPED | demand priced under the role's own key, but the TO-based capacity map carries no HC for it (IT product-model seats; §7.2 roster-abbreviation alias) | demand is real and shown; utilization needs a capacity-map decision — alias/adjudicate, then re-pin |
| ZERO-DURATION | step-anchored, but every named step's duration cell reads zero (days-based or cadence-only work) | verify by cycle audit, not hours |
| UNPARSEABLE-FREQ | step-anchored, but every anchor rides a workflow whose frequency fails the cadence ladder | adjudicate the frequency family, then re-derive |
| NO PARSED CADENCE | Participant-level anchor only | step-level anchoring or gemba measurement |

## Verification table

| Role | Charter | Touched | Demand h/yr | HC | Utilization | Verdict |
|---|---|---|---|---|---|---|
| Accounting Policy Analyst | §5.3 register — Finance & Accounting | 1 | 8 | 1 | 0% | UNDER-UTILIZED |
| ASM | §7.2 store roster — Store (field, per-store roster) | 1 | 63,875 | — | — | MEASURED — capacity unmapped |
| Assistant DC Manager — Outbound | §7.3 DC roster — DC (field, per-DC roster) | 1 | 342 | 4 | 4% | UNDER-UTILIZED |
| Contracts & Commercial Manager (Senior Counsel) | §5.3 register — Legal & Compliance | 1 | — | 1 | — | ZERO-DURATION |
| Cycle Counters | §7.3 DC roster — DC (field, per-DC roster) | 1 | 1,375 | 36 | 2% | UNDER-UTILIZED |
| DC Office Administrator | §7.3 DC roster — DC (field, per-DC roster) | 1 | 28 | 4 | 0% | UNDER-UTILIZED |
| Discrepancy Analysts | §7.3 DC roster — DC (field, per-DC roster) | 1 | 3,000 | 8 | 20% | UNDER-UTILIZED |
| Ecommerce Marketing Specialist | §5.3 register — Marketing | 1 | 2,500 | 2 | 69% | CONFIRMED |
| Facilities/Utility | §7.3 DC roster — DC (field, per-DC roster) | 1 | — | — | — | NO PARSED CADENCE |
| Field Communications Manager | §5.3 register — Store Operations | 1 | 56 | 1 | 3% | UNDER-UTILIZED |
| IAP Integration Engineer | IT seat — Information Technology (product model) | 1 | 8 | — | — | MEASURED — capacity unmapped |
| Payroll & Statutory Remittance Officer | §5.3 register — Human Resources | 1 | 60 | 1 | 3% | UNDER-UTILIZED |
| Promotions & Vendor-Funding Coordinator | §5.3 register — Merchandising & Buying | 1 | 125 | 3 | 2% | UNDER-UTILIZED |
| Promotions Specialist | §5.3 register — Marketing | 1 | 62 | 2 | 2% | UNDER-UTILIZED |
| Quality & Workforce Analyst | §5.3 register — Customer Service | 1 | 7,500 | 2 | 208% | OVERLOAD |
| Senior LP Analytics Analyst | §5.3 register — Regional Loss Prevention | 1 | 18,250 | 1 | 1014% | OVERLOAD |
| Special Handling Lead | §7.3 DC roster — DC (field, per-DC roster) | 1 | 13,500 | 4 | 178% | OVERLOAD |
| TA Coordinator | §5.3 register — Human Resources | 1 | — | 1 | — | ZERO-DURATION |
| Technical Accounting Manager | §5.3 register — Finance & Accounting | 1 | 3 | 1 | 0% | UNDER-UTILIZED |
| Tile & Heavy/Breakbulk Crew | §7.3 DC roster — DC (field, per-DC roster) | 1 | 684 | — | — | EXERCISED-THROUGH — via loading crew |
| AAP Agent Engineer | IT seat — Information Technology (product model) | 2 | — | — | — | NO PARSED CADENCE |
| Assistant DC Manager — Inbound | §7.3 DC roster — DC (field, per-DC roster) | 2 | 65,340 | 4 | 860% | OVERLOAD |
| Audit Manager | §5.3 register — Internal Audit & Risk | 2 | — | 1 | — | ZERO-DURATION |
| Banking & Cash-Management Specialist | §5.3 register — Finance & Accounting | 2 | — | 2 | — | ZERO-DURATION |
| Build-Squad Tech Lead | IT seat — Information Technology (product model) | 2 | — | — | — | ZERO-DURATION |
| Business Process & IMS Lead | §5.3 register — Strategy / Corporate Planning | 2 | — | 1 | — | ZERO-DURATION |
| Corporate Secretary Analyst | §5.3 register — Legal & Compliance | 2 | — | 1 | — | ZERO-DURATION |
| CPM (Corporate Performance Management) Analyst | §5.3 register — Strategy / Corporate Planning | 2 | — | 1 | — | ZERO-DURATION |
| Cross-Dock Team | §7.3 DC roster — DC (field, per-DC roster) | 2 | 31 | 24 | 0% | UNDER-UTILIZED |
| DC Cost-to-Serve Analyst | §5.3 register — Finance & Accounting | 2 | — | 1 | — | ZERO-DURATION |
| DC Operations Analyst | §5.3 register — Supply Chain & Logistics | 2 | 62 | 1 | 3% | UNDER-UTILIZED |
| Ecommerce Support Specialist | §5.3 register — Customer Service | 2 | 5,000 | 3 | 93% | CONFIRMED |
| ESG Reporting & Data Analyst | §5.3 register — Sustainability / ESG | 2 | — | 1 | — | ZERO-DURATION |
| Facilities Coordination Specialist | §5.3 register — Store Operations | 2 | — | 1 | — | ZERO-DURATION |
| Forensic / Fraud Investigator | §5.3 register — Internal Audit & Risk | 2 | — | 1 | — | ZERO-DURATION |
| IAP Integration Support Engineer | IT seat — Information Technology (product model) | 2 | — | — | — | ZERO-DURATION |
| Import Documentation Specialist | §5.3 register — Supply Chain & Logistics | 2 | — | 1 | — | ZERO-DURATION |
| INFRA Site Reliability Engineer | IT seat — Information Technology (product model) | 2 | — | — | — | NO PARSED CADENCE |
| Legal Counsel — Contracts | §5.3 register — Legal & Compliance | 2 | — | 2 | — | ZERO-DURATION |
| Lumber / Long-Length Crew | §7.3 DC roster — DC (field, per-DC roster) | 2 | 30,542 | 32 | 50% | CONFIRMED |
| Maintenance & Projects Coordinator | §5.3 register — Facilities & Real Estate | 2 | — | 2 | — | ZERO-DURATION |
| Marketing Comms Specialist | §5.3 register — Marketing | 2 | 72 | 1 | 4% | UNDER-UTILIZED |
| Operations Compliance Lead | §5.3 register — Internal Audit & Risk | 2 | — | 1 | — | ZERO-DURATION |
| Paralegal / Contracts Specialist | §5.3 register — Legal & Compliance | 2 | 195 | 2 | 5% | UNDER-UTILIZED |
| Payroll Supervisor | §5.3 register — Human Resources | 2 | 30 | 1 | 2% | UNDER-UTILIZED |
| Privacy Officer | §5.3 register — Legal & Compliance | 2 | 36,000 | 1 | 2000% | EXERCISED-THROUGH (OVERLOAD) — via data privacy officer (dpo) |
| Purchasing / PO Specialist | §5.3 register — Supply Chain & Logistics | 2 | — | 6 | — | NO PARSED CADENCE |
| Replenishment & Allocation Analyst | §5.3 register — Supply Chain & Logistics | 2 | 3,042 | 2 | 84% | CONFIRMED |
| Retail Media Operations Specialist | §5.3 register — Marketing | 2 | 112 | 1 | 6% | UNDER-UTILIZED |
| Sourcing & Screening Coordinator | §5.3 register — Human Resources | 2 | — | 1 | — | ZERO-DURATION |
| Strategy Analyst | §5.3 register — Strategy / Corporate Planning | 2 | — | 1 | — | ZERO-DURATION |
| Vendor Portal & Collaboration Specialist | §5.3 register — Supply Chain & Logistics | 2 | 4,354 | 2 | 121% | CONFIRMED |
| Wellness Coordinator | §5.3 register — Health, Safety & Environment | 2 | — | 1 | — | ZERO-DURATION |

## Tally

| Verdict | Roles |
|---|---|
| CONFIRMED | 5 |
| OVERLOAD | 4 |
| UNDER-UTILIZED | 16 |
| EXERCISED-THROUGH | 2 |
| MEASURED — CAPACITY UNMAPPED | 2 |
| ZERO-DURATION | 20 |
| UNPARSEABLE-FREQ | 0 |
| NO PARSED CADENCE | 4 |

> OVERLOAD rows are the headcount-real candidates this doctrine exists to find. UNDER-UTILIZED
> rows are merge/resize candidates. EXERCISED-THROUGH rows are measured through the seats their
> cells resolve to — the via-group's aggregate utilization, not the row's, is the staffing signal;
> their demand column is the role's claimed share of its named cells. MEASURED — CAPACITY UNMAPPED
> rows carry real own-key demand against no mapped HC (IT product-model seats; the ASM alias gap).
> ZERO-DURATION rows are step-anchored on cells the hour model cannot price — audit the cycle,
> not the hours. UNPARSEABLE-FREQ rows await a cadence-family adjudication. NO PARSED CADENCE rows
> are participant-level only — the step-level anchoring backlog. Interpretation guardrails as printed by the tool.
