# Finance Workflow Gap Analysis — BuildRight Depot Corp.

> Focused gap analysis of **finance-related workflows**, performed per the methodology in
> [workflow-gap-analysis.md](workflow-gap-analysis.md) §2 (defining-term keyword search across all
> PA files to distinguish *dedicated* coverage — a `## W` header that owns the capability — from
> *incidental* single-step references). Companion to the canonical thirty-pass gap history; this
> document does **not** amend that record. **Status (2026-09-03): adopted.** All three gaps were
> confirmed and filled as workflows **W5529–W5531**, allocated in
> [workflow-gap-analysis.md](workflow-gap-analysis.md) batch 10 and confirmed into the criticality
> register (2 × Tier 1, 1 × Tier 2).

---

## 1. Scope

All workflows governing the **finance function** of the model company (PHP 62.3B revenue, 5 legal
entities, ~210 bank accounts, ~800–1,000 vendors, ~5,400 trade accounts, ~450–700 utility/telecom
deposit accounts), across:

- The **Finance family** — 29 dedicated value streams, **786 workflows**: VS-15 (43), VS-16 (32),
  VS-17 (70), VS-18 (35), VS-34 (22), VS-38 (24), VS-39 (24), VS-40 (24), VS-54 (26), VS-68 (24),
  VS-72 (24), VS-79 (28), VS-80 (24), VS-96 (24), VS-105 (25), VS-116 (24), VS-118 (25),
  VS-125 (24), VS-142 (24), VS-148 (24), VS-153 (24), VS-154 (24), VS-157 (24), VS-158 (24),
  VS-170 (24), VS-173 (24), VS-181 (24), VS-188 (24), VS-189 (24).
- **Adjacent value streams with finance-facing scope**: VS-19 (payroll processing & consolidation),
  VS-42 (property & lease administration — landlord deposits, utility accounts, PFRS 16), VS-97
  (corporate property portfolio), VS-21 (internal audit), VS-22 (BIR/regulatory response),
  VS-29 (financial master data), VS-33 (strategic planning & budgeting), VS-120 (energy program).

## 2. Method

1. **Inventory** every `## W` header in the 29 Finance value streams (786 workflows) plus
   finance-scoped workflows hosted elsewhere (payroll accounting in VS-19.2, landlord deposits in
   VS-42.2, BIR response in VS-22.2).
2. **Map** each capability of a reference corporate-finance operating model for a Philippine
   multi-entity retailer — transactional finance (P2P/O2C/expense/payroll accounting), accounting
   operations (close, reconciliation, intercompany, technical accounting), treasury (cash, banking,
   FX, debt, deposits), tax (direct/indirect/statutory regimes), FP&A, cost & margin, risk &
   insurance, controls & audit, finance systems & data — to the owning workflow(s).
3. **Flag** capabilities with no owning workflow, thin-partial coverage, or scattered ownership.
4. **Validate** each candidate gap by keyword search across all PA files; discard false positives
   and near-misses (e.g., 'corporate card' has zero exact-title hits but W713/W1685 own the
   program; 'insurance broker' appears in 16 PA files but W59 owns the broking interface;
   'bank relationship' has 8 incidental hits but W317 owns the annual relationship review and the
   monthly fee review inside its lifecycle).

## 3. Current-State Coverage Map (confirmed covered — no gap)

| Finance Capability | Owner workflow(s) | VS / PA |
|---|---|---|
| AP: 3-way match, payment runs, debit memos, duplicate detection, aging | W7, W556, W770, W813, W662 | VS-15.1/.2 |
| Vendor statement reconciliation, advances, price-discrepancy debits | W100, W498, W1504 | VS-15.1 |
| AR: payment application, disputes, statements, overpayments, unapplied cash | W2745, W2746, W892, W769 | VS-16.2/.3 |
| Credit: applications, limits, scoring, collections, agency placement, legal escalation | W24, W886–W893, W108, W812, W1200 | VS-16.1/.2 |
| Bad-debt provisioning (PFRS 9) & write-off; customer deposits; PDC lifecycle | W81, W891, W94, W1380–W1382, W423–W425 | VS-16.3, VS-18.1 |
| Close: month-end/year-end checklist, JE review, BS reconciliations, period lock | W9 (W9A/W9B), W636, W638 | VS-17.1/.4 |
| Intercompany: transactions, netting, service fees, transfer pricing, profit elimination | W14, W234, W1201, W1277, W1293, W1299, W612 | VS-17.2, VS-18.1, VS-72 |
| CIT computation & deferred tax (PAS 12); monthly tax filings; VAT reconciliations; provision | W407, W90, W260, W1418, W590 | VS-17.3 |
| SEC reportorial (GIS/AFS/MC 28); external audit coordination; BIR audit response | W481, W95, W351, W77 | VS-17.3, VS-22.2 |
| Accounting policy & technical accounting (PFRS positions, new standards) | W5528, W1875 | VS-17.4, VS-42.3 |
| FP&A: budget, rolling forecast, store P&L, flash, QBR, KPI framework | W26, W639, W1405, W1406, W231, W1659 | VS-17.4, VS-33 |
| Treasury: daily position, forecasting, concentration/sweeping, RTGS, investments, debt & covenants | W30, W233, W589, W664, W1361, W1342, W318, W1474, W319 | VS-18 |
| Banking: account lifecycle/signatories, e-banking security, multi-bank aggregation, fee review (step) | W317, W320, W1361 | VS-18.2 |
| FX: hedging, exposure & BSP reporting, hedge accounting, IC FX settlement | W80, W321, W1473, W1456 | VS-18.3 |
| Guarantees & contingent liabilities (outgoing bonds/guarantees); LC lifecycle | W232, W325, W1199, W1294, W1455 | VS-18.2/.3, VS-15.2 |
| SCF & working capital; inventory-pledge/ABL financing; receivables factoring | W324, VS-105, VS-170, VS-189 | Finance family |
| Expense: reimbursement, corporate cards (×2 owners), T&E, utilities monitoring, policy audit | W74-analog W1686, W713, W1685, W1687, W1689 | VS-34.3, VS-15.2 |
| Payroll accounting: multi-entity payroll consolidation & GL reconciliation; 13th-month accrual | W816, W1416, W1527, W1306 | VS-19.2 |
| Fixed assets: capitalization, depreciation, verification, disposal, AUC | VS-35 (W661, W184, W39, W276), W1431 | VS-35, VS-17.1 |
| Inventory accounting: obsolescence write-offs, NRV write-downs & reversals, adjustments | W587, W4660, W9A.16b/.16d | VS-05.3, VS-158.2, VS-17.4 |
| Costing & margin: landed cost, standard vs actual, cost-to-serve | VS-158, W85 | VS-158, VS-17.4 |
| Revenue recognition (PFRS 15 complex contracts); loyalty-points liability; lease accounting (PFRS 16) | VS-157, W1274, W1316, VS-148 (W635, W1872) | VS-157, VS-13, VS-148 |
| Revenue assurance & merchant-fee optimization | VS-118 (W348 successors), W640 | VS-118, VS-15.2 |
| Payment operations: acquirer/PSP settlement, chargebacks, BSP scheme compliance | VS-80 (W2785–W2800) | VS-80 |
| Insurance: policy lifecycle & broker market-comparison, claims, captive | W59, W610, VS-153 | VS-17.1, VS-26.3, VS-153 |
| Financial master data: COA & cost centers, fiscal calendar, FX rates, payment terms | W288, W308, W307, W295, W1545 | VS-29.2 |
| Treasury month-end close: interest accruals, FX revaluation, fee verification | W326 | VS-18.1 |
| Tax incentives (BOI/PEZA), percentage-tax regime, EIS, CAS/PTU, ATP registration | W472, W1503, W473, W1525, W1181 | VS-17.3 |
| Capital returns: dividends (external & intercompany), IR/capital-markets disclosure | W327, W137, VS-173 | VS-18.3, VS-17.2 |
| Financial restatement & prior-year adjustment | W712 | VS-16.1 |

## 4. Gaps Identified

### G1 — Utility, telecommunications & site deposits paid (deposit-asset lifecycle) — **MEDIUM**

~450–700 deposit-bearing utility/water/telecom accounts across ~205 locations lock **PHP 10M–40M**
of cash — a figure the corpus itself quantifies in W1877's Pain Points ("Electric cooperatives may
require deposits of PHP 50K–200K per store; total utility deposits across ~205 locations =
PHP 10M–40M in locked capital") — with **no owning workflow anywhere**.

- **Evidence (dedicated-header hits / defining terms):** 'utility deposit' **0** dedicated headers
  (2 incidental PA files: a store-closure *recovery sub-step* in PA-20.3 and the W1877 pain-point
  line); 'deposit accounting' **0**; 'billing deposit' **0**. The owned sibling patterns exist:
  W1867 owns *landlord* security deposits end-to-end (register, adequacy, return, dispute),
  W3532 owns pallet/RTI deposit exchange, W94 owns *customer* deposits — nobody owns BuildRight's
  deposits **paid** to utilities/telecom providers.
- **Why it matters:** PHP 10M–40M of cash earns deposit-rate interest well below the W318
  investment yield; EPIRA IRR interest entitlements on distribution-utility deposits are missed
  when untracked; closure refunds lapse past provider claim windows and are forfeited outright;
  several providers accept surety/bank-guarantee replacement (W232/W325 machinery exists) —
  releasing the cash entirely.
- **Proposed disposition:** 1 workflow in **PA-42.3** — *"Utility, Telecommunications & Site
  Deposits Paid — Register, Interest Reconciliation, Surety Replacement & Recovery-on-Closure"*
  (hosted next to the pain point and the W1877 utility-account sibling).

### G2 — Minimum corporate income tax (MCIT) computation & carry-forward — **HIGH** (statutory)

The 2% MCIT gross-income floor of NIRC §27(E)/§28(A)(e) — applicable from an entity's 4th taxable
year, payable when it exceeds normal income tax, with the excess creditable against normal tax for
the 3 immediately following years — is **absent from the entire corpus**.

- **Evidence:** 'MCIT' **0** corpus-wide; 'minimum corporate income' **0**; 'gross income tax'
  **0**. W407 computes normal corporate income tax and deferred tax (PAS 12) per entity; W590
  runs the monthly provision; neither references the MCIT floor, the regime evaluation, or the
  excess-credit register. For 5 entities past their 4th year, a low-margin quarter silently
  under-declares the 1702Q/1702RT and accrues BIR penalties — the exact exposure W77 defends.
- **Why it matters:** statutory filing dependency (the W5508 precedent — FBT computation feeding
  the BIR 1605 shipped Tier 1); the excess-credit carry-forward is real money that lapses silently
  after 3 years when untracked.
- **Proposed disposition:** 1 workflow in **PA-17.3** — *"Minimum Corporate Income Tax (MCIT)
  Computation, Regime Evaluation & 3-Year Excess-Credit Carry-Forward"* (per-entity quarterly
  MCIT-vs-normal-tax comparison, annual return integration, carry-forward register, relief
  evaluation, W77 examination evidence).

### G3 — PFRS 8 operating-segment reporting & CODM disclosure package — **MEDIUM** (statutory)

The audited financial statements require a PFRS 8 operating-segment note derived from the CODM's
*actual* internal review structure — and while every ingredient exists (the CODM review packages
in W1653/W231/W102/W1657, the consolidation machinery in W9B/W234, the AFS filing in W481), the
segment-note production that binds them is **absent from the entire corpus**.

- **Evidence:** 'segment reporting' **0** corpus-wide; 'operating segment' **0**; 'group
  reporting' **0** dedicated headers (3 incidental hits). W481 files the AFS and quotes
  "Controller provides audited financial statements (after W9B year-end close...)" — but no
  workflow produces the segment disclosures, the CODM-measure consistency evidence, the
  entity-wide (product/geographic/major-customer) disclosures, or the PFRS 8 reconciliation of
  segment to consolidated totals.
- **Why it matters:** the segment note is not optional disclosure — an AFS filed without it (or
  with segments inconsistent with the CODM's review package) is defective for SEC purposes and
  exposes the W481 filing to deficiency action; the audit walkthrough (W95/W351) tests exactly
  this consistency.
- **Proposed disposition:** 1 workflow in **PA-17.4** — *"PFRS 8 Operating-Segment Reporting, CODM
  Disclosure Package & Segment-Note Production"* (CODM designation & segment-structure
  confirmation against the W1653 package, segment data assembly & reconciliation, aggregation and
  restatement criteria, entity-wide disclosures, audit walkthrough, AFS note production on the
  W481 calendar).

## 5. Thin-Partial Coverage (monitor; no immediate new workflow required)

| Topic | State | Note |
|---|---|---|
| Bank-relationship & fee governance layer | 'bank relationship' 8 incidental hits, 0 dedicated headers | W317 owns the annual relationship review and monthly fee review inside the account lifecycle; W320 step 9 and W1468 step 6 supplement — adequately owned |
| Electricity supply / retail-competition (RCOA) sourcing | PA-120.1 step 1 owns the contestable-account RES program; W4775 demand-charge management | Tariff-structure optimization rides the EEO workflow; monitor at the next VS-120 review |
| Insurance broking & renewal marketing | W59 step 3 owns broker market-comparison; broker named as external partner | Owned interface; no separate workflow warranted |
| Collection-agency placement & performance | W108 steps 6–7 own agency engagement, contingency terms and monitoring | Owned |
| Check-stock & stale-check custody | 'check stock'/'positive pay' ≈ 0 | Payments are predominantly electronic (W556/W320/W1362); PDC issuance is owned by W424; revisit only if check volume grows |
| Vendor credit-balance aging | W9A.16e reconciles unapplied AP/AR credit notes monthly; W662 ages AP | Owned at close |
| Suspense/clearing-account governance | W9A.2a GR/IR clearing; W2792 aged settlement & suspense clearing | Owned |
| Segment-level planning platform (EPM) | W1646 names the budgeting/planning module; consolidation system mentioned in W9 | The ERP-module layer is named and owned inside the budget/close workflows; watch for a standalone EPM need at multi-entity scale |
| Interest income on corporate deposits | W326 accrues investment/loan interest at close; W1474 yield optimization | Owned |

## 6. Summary

| ID | Gap | Priority | Proposed home | Proposed workflows | Status (2026-09-03) |
|---|---|---|---|---|---|
| G1 | Utility/telecom/site deposits paid (deposit-asset lifecycle) | Medium | PA-42.3 | 1 | **Adopted — W5529** (Tier 2) |
| G2 | MCIT computation, regime evaluation & carry-forward | High (statutory) | PA-17.3 | 1 | **Adopted — W5530** (Tier 1) |
| G3 | PFRS 8 segment reporting & CODM disclosure package | Medium (statutory) | PA-17.4 | 1 | **Adopted — W5531** (Tier 1) |
| | **Total** | | | **3 workflows** | **3 shipped: W5529–W5531** |

**Overall verdict:** the finance workflow inventory is the deepest in the corpus — transactional
finance, close/consolidation, intercompany, treasury, tax, FP&A, cost, insurance and finance
master data are owned at workflow granularity with explicit boundaries (VS-15 vs VS-34 vs VS-72;
VS-16 vs VS-68 vs VS-189; VS-17 vs VS-79 vs VS-158). The residual exposure sat in exactly three
places: the **deposit-asset lifecycle** that every adjacent owner assumed was somebody else's job
(G1), and two **statutory layers** the corpus computes and files around but never names (G2 — the
MCIT floor; G3 — the PFRS 8 note). Filling the three gaps added **3 workflows (~0.4% growth to
the Finance family)** and closed every unowned capability surfaced by this analysis. VS-17 now
stands at **70 workflows** (PA-17.1: 26 · PA-17.2: 10 · PA-17.3: 15 · PA-17.4: 19) and VS-42 at
**25 workflows** (PA-42.3: 9).

---

*Methodology note: candidate gaps surviving keyword validation follow §2 step 4 of
[workflow-gap-analysis.md](workflow-gap-analysis.md). The adoption was recorded there as batch 10
(workflow-ID allocation W5529–W5531), with criticality tiers confirmed (2 × Tier 1, 1 × Tier 2)
in [workflow-criticality-classification.md](workflow-criticality-classification.md).*
