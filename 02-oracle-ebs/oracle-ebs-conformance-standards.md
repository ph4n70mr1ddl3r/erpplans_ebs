# Oracle EBS Conformance Standards — the Best-Practice Canon for Transactional Workflows

> Codifies how the model company's workflows must behave so the [workflow corpus](../01-model-company/workflows/README.md) runs the way Oracle E-Business Suite 12.2 is designed to be run — destination-type routing, mass-additions capitalization, custody-of-record, derived tax books, controlled-issue consumables — rather than fighting the suite's grain. Every rule names its Oracle mechanism, its workflow surface, and how conformance is checked. Companion tool: [`audit-oracle-conformance.py`](../07-methodology/audit-oracle-conformance.py).

---

## 1. Why this document exists

The workflow corpus (5,433 workflows across 569 process areas) was authored business-first and
platform-aligned through the [fit-gap register](fit-gap-analysis.md) at the *vehicle* level — which
EBS product serves which capability. This canon goes one level deeper: the *behavioral* standards
Oracle's own implementation methodology (AIM/OUIM) expects transactions to follow. A workflow can
name the right module and still behave in a way that produces audit findings, ghost assets, or
unreconcilable sub-ledgers. These rules close that gap; the audit tool enforces them mechanically.

## 2. The routing principle — one decision drives everything

Every purchased good in EBS is routed by the purchase-order line **destination type** — the master
switch that separates the model company's three non-merchandise worlds:

| Destination type | Meaning | Lands in | Model-company category |
|---|---|---|---|
| **Inventory** | Item for resale or controlled internal stock; item-master record, valued on-hand | Oracle Inventory org / subinventory | Trade items |
| **Expense** | Consumed on receipt; charged directly to a cost-center expense account, never capitalized | Oracle GL via the AP invoice | Office supplies and consumables |
| **Asset** or a CIP project | Capitalized item at or above the capitalization threshold with a useful life over one year | Oracle Payables → Mass Additions → Oracle Assets | Fixed assets |

The requisitioner never chooses an accounting treatment. Classification happens at master-data
level — item templates, asset categories, non-catalog request templates — so the transaction
cannot be misrouted by judgment at the point of entry. This is the core Oracle design standard.

## 3. The standards

### A. Routing and classification

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-01 | The destination type on the PO line — Inventory, Expense, or Asset — decides the accounting treatment; no transaction-level overrides | PO line destination type; receiving routing | All PA-15, PA-34 workflows |
| OC-02 | Classification lives in master data, not user judgment: item templates and iProcurement stores pre-flag asset vs expense vs inventory before requisition | Item templates, iProcurement stores, non-catalog request templates | PA-29 master data; PA-34.1 catalogs |
| OC-03 | The capitalization threshold is enforced as a category-driven default plus PO flag, never as requester discretion; threshold gaming is detected by repeat-purchase flags | Asset category defaults; purchasing category flags | W1690 step 3 |

### B. Fixed-asset lifecycle and custody

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-04 | Every capitalizable purchase flows PO → receipt → AP invoice → **Mass Additions**, and nothing posts to the register without the queue review — the Fixed Asset Accountant posts as addition, charges to expense, splits, merges, or rejects | Mass Additions Create; the FA mass-additions review queue | W1690, W1690.1 touchpoints |
| OC-05 | Every asset carries a **custodian of record** — populated in the asset record's Assigned-To field at registration. Named individual for IT equipment, tools and vehicles; role-level of record for fixtures. Custody is never blank and never a department alone | Oracle Assets Assigned-To and Location fields | W1690 step 2; the custody table in §4 |
| OC-06 | **Tag before use, scan as acceptance**: no asset goes productive without a tag tied to the asset number, and the location's tag-scan confirmation doubles as the custodian of record's custody acceptance | Barcode/QR tag generation; mobile scan confirmation writing to the asset record | W1692 |
| OC-07 | **Transfers are custody events, not moves**: the sending custodian of record releases the asset and the receiving custodian accepts it — custody is in transit, never unassigned; the register update is the evidence of transfer | Oracle Assets transfer; location and Assigned-To update | W1693 steps 1 and 4 |
| OC-08 | Depreciation calculates in each entity's **corporate book**; tax books **derive from** the corporate book — tax schedules are never maintained independently of the corporate register | Corporate book per ledger; tax books derived from corporate | W1698 step 2; W1704 |
| OC-09 | Retirements are approval-gated before the register is touched: location-initiated request, Finance review, disposal evidence attached, then system retirement with proceeds and gain/loss | Oracle Assets retirement with proceed-of-sale; AME approval above threshold | W1708, W1711 |
| OC-10 | Physical verification is executed by the location's custodian of record and attested by signature, counted down by a party independent of the book owner — the Fixed Asset Accountant never counts their own register alone | Register extract by location; mobile scan reconciliation | W1706 |
| OC-11 | CIP assets are owned by the project until a formal **custody handover**: the completion certificate includes the operating custodian of record's acceptance, and registration assigns the custodian so no asset turns over unowned | CIP-to-asset conversion; Projects handover | W1828 step 2; W1829 |

### C. Supplies, consumables and non-trade items

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-12 | Supplies are never capitalized regardless of local opinion — below the threshold or under one year of life means expense, full stop | Destination type Expense | PA-34.1 |
| OC-13 | Treatment is chosen per class of spend, not one size for all: direct expense for fast-consumed low-value items; **expense subinventory** where issues must be counted; blanket PO releases for predictable recurring volume | iProcurement non-catalog requests; expense subinventories; blanket releases | W1668, W1673 |
| OC-14 | **Controlled-issue items** — PPE, uniforms, toner-class consumables, company-grade equipment below the threshold — are issued per requisition from a custodied storeroom or expense subinventory with a named custodian, and counted on a recurring cycle: expensed in the books, accountable in custody | Expense subinventory issues; cycle count program | W1670, W1673 |
| OC-15 | A **tractable-item pool** catches what the capitalization threshold would otherwise lose: items below the threshold but accountable by nature — power tools, measuring instruments, cameras — are expensed yet carried on a countable minor-asset register so the physical count covers them | Descriptive flexfield or minor-asset register alongside Oracle Assets | W1690 step 3 |

### D. Approvals and segregation of duties

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-16 | No single person records the asset, receives it, holds it, and disposes of it: the Fixed Asset Accountant owns the register, receiving owns the receipt, the custodian of record holds the asset, Finance leadership approves disposal | EBS responsibility design; SoD role queries | PA-35 RACI columns |
| OC-17 | Approvals ride position hierarchies and AME rules above value thresholds — not ad-hoc name chains | Position hierarchy; AME | PA-15, PA-40.1 |
| OC-18 | High-value capitalization and retirement carry a second gate: capitalization approval for assets at or above the executive threshold, and CFO-visible disposal review with gain/loss reporting | AME rules; FA approval workflows | W1690 step 4; W1708 |

### D2. Cash and banking

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-24 | The bank-statement reconciliation is prepared by a role independent of payment execution: the people who initiate, approve or release payment files never reconcile the accounts they pay from — Treasury owns daily cash visibility (the operational auto-match), the entity GL Accountant owns the monthly statement reconciliation and its sign-off | EBS responsibility design; Cash Management (CE) reconciliation responsibility held apart from the Payables/Treasury payment seats | W89 steps 1–6; W9A step 9; CTL-19 |

### E. Receiving and matching

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-19 | Asset lines require receipt — the three-way match of PO, receipt and invoice is mandatory for capitalized purchases; two-way matching is reserved for true expense consumables | Purchasing receiving options; AP matching | PA-15.1 steps 2–4 |

### F. Master data

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-20 | The asset category key flexfield — major and minor segments — defaults the asset and clearing GL accounts, book, depreciation method and useful life; accounts are never keyed per asset | Asset Category KFF defaults | W1691 category tree |
| OC-21 | Asset Key carries the cost-center dimension and Location carries the physical place; together with Assigned-To they form the custody triangle that every custody report reads | Asset Key and Location KFFs; Assigned-To | W1690, W1693, W1706 |

### G. Assurance

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-22 | The sub-ledger reconciles to the GL every period — gross, accumulated depreciation and net book value, per entity, before close | FA-to-GL reconciliation report | W1705 reconciliation |
| OC-23 | Counting is a program, not an event: the annual wall-to-wall count for fixed assets, cycle counts for controlled-issue supplies, and the tractable pool inside the annual count | Physical inventory and cycle count; the W1706 program | W1706, W1707; OC-14 |

### H. Period close

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-25 | The close runs in the suite's sequence: sub-ledger periods (Inventory, PO, AP, AR, CE) are closed and fully transferred and reconciled to GL before the GL period locks — GL closes last; the new period opens its sub-ledgers first (Inventory → PO → AP → AR) and GL last, so no transaction posts to a closed period | Accounting periods (sub-ledger and GL close/open order); the close calendar | W9A step 17 |

### I. Payroll and people costing

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-26 | The payroll engine never posts directly to the ledger: in-house payroll costing journals land in the GL interface and import as named-source unposted journal batches (source Payroll PH), which GL validates and posts inside the close discipline — every peso of payroll cost reaches the ledger through Journal Import's audit trail, never as a direct write and never re-keyed by hand (the OC-04 mass-additions gate's ledger-of-record analog) | GL Journal Import (GL interface → import → validate → post) under the payroll source | W10 step 9; W1416 step 1; W1384 step 5 |
| OC-27 | Manual payroll-side GL journals — accrual true-ups, corrections, reversals — ride the journal-entry review workflow with tiered approval and preparer ≠ approver; no payroll adjustment posts as an unreviewed direct entry, and no two workflows book the same payroll accrual in parallel | GL journal approval; the W638 approval matrix | W644 step 3; W1416 step 2; W816 step 6 |
| OC-28 | Payroll payment files are transmitted by the Treasury payment-execution seat under approved release — the same separation CTL-13 seats for the regular run — never by the payroll chain that computes and approves the run; the W10 step-8 convention carries into every payroll disbursement rail: regular, off-cycle, final pay and 13th month (the execution-side twin of OC-24) | EBS responsibility design; payment-file transmission held apart from payroll computation | W10 step 8 (conformant anchor); W641 step 6; W643 step 6; W644 step 8; W1416 step 5 |

## 4. Custody of record — the operating model

Oracle's implicit standard, reflected in the Assigned-To field and in audit methodology, is a
three-way split of record ownership, physical custody and custody at birth:

| Function | Owner | What they hold | Where it lives |
|---|---|---|---|
| Record ownership | Fixed Asset Accountant — Finance | The register truth: cost, book, depreciation | Oracle Assets |
| Physical custody | The custodian of record — the location manager, DC supervisor or department head of record | The physical asset; answerable for its existence and condition | Assigned-To plus Location on the asset record |
| Custody at birth | Receiving Clerk, then the first custodian of record after the acceptance scan | From dock to tag to acceptance — brief, documented, signed | Receipt plus the W1692 acceptance scan |

The five rules of custody, each testable at audit:

1. Every asset has exactly one custodian of record — never blank, never a department alone.
2. Custody transfers are events with a release and an acceptance — never conventions.
3. Record owner, receiver, custodian and disposal approver are four different people.
4. The custodian attests at the count; Internal Audit verifies independently.
5. No asset goes productive without a tag, and the acceptance scan is the signature.

## 5. Enforcement

The companion tool [`audit-oracle-conformance.py`](../07-methodology/audit-oracle-conformance.py)
implements this canon as machine-checkable rules over the workflow corpus:

- **Anchor rules** — the repaired workflows must carry their conformance clauses; stripping one
  fires and forces a conscious re-point. Enforced in `--guard` mode per the house convention.
- **Retired-form rules** — the replaced phrasings are banned in their files of scope so the
  defect class cannot silently return.
- **Corpus scans** — informational sweeps for the judgment classes the anchors cannot reach
  (supplies capitalized in PA-34, Fixed Asset Accountant receiving steps, unattested counts),
  reported as a findings census for per-workflow triage.

## 6. Initial conformance review — 2026-09-23

The review audited the custody and treatment chain — the highest-risk class under this canon —
across VS-35, VS-34, VS-40 and VS-15. Eleven findings; all repaired in the same pass:

| # | Finding | Rule | Disposition |
|---|---|---|---|
| 1 | W1690 registered assets without a custodian of record — the responsible department was recorded, no Assigned-To | OC-05 | Fixed — step 2(h) |
| 2 | W1690's capitalization pipeline did not name the mass-additions queue as the AP-to-Assets gate | OC-04 | Fixed — step 1(a) + touchpoint |
| 3 | W1690 had no below-threshold accountable pool — countable items fell out of the estate at the threshold | OC-15 | Fixed — step 3 |
| 4 | W1692 tag confirmation was not custody acceptance — assets went productive unsigned | OC-06 | Fixed — step 4 |
| 5 | W1693 transfers moved assets without a release step — custody was unassigned in transit | OC-07 | Fixed — steps 1, 4 |
| 6 | W1698 depreciation did not name corporate-book derivation of the tax book | OC-08 | Fixed — step 2(f) |
| 7 | W1706 count lacked the custodian attestation signature | OC-10 | Fixed — step 2(e) |
| 8 | W1828 turnover certificate omitted the custody handover to the operating custodian | OC-11 | Fixed — step 2(e) |
| 9 | W1670 PPE and uniforms issued without requisition control from a custodied storeroom | OC-14 | Fixed — step 4 |
| 10 | W1673 office supplies lacked the controlled-issue treatment for accountable consumables | OC-14 | Fixed — step 3 |
| 11 | W1708 retirement approvals, W1706 audit independence, PA-15.1 three-way match, W1711 gain/loss — verified conformant | OC-09, OC-10, OC-19 | None — recorded conformant |

Tracked for per-workflow triage via the tool's corpus scans: the corpus-wide segregation-of-duties
role-pair sweep, and the W1695 maintenance-history vehicle naming against the adopted eAM row —
both closed by the corpus-wide review in §7.

---

## 7. Corpus-wide conformance review — 2026-09-23 (second pass)

The second pass extended the review from the four custody-chain process areas to the whole corpus
(all 569 process areas), sweeping the canon's judgment classes mechanically: ad-hoc name-chain
approvals, self-approval rows, register-owner-as-receiver and register-owner-as-counter role
pairs, tax-book independence, mass-additions bypasses, two-way matching on capital, unattested
counts and requester-chosen accounting treatment. The routing, book-derivation, matching and
treatment classes came back clean corpus-wide. Four findings — all repaired in the same pass:

| # | Finding | Rule | Disposition |
|---|---|---|---|
| 1 | W1695's PM-schedule, maintenance-recording and history rows rode generic 'system' naming — the adopted eAM row (module-coverage-map Facility Maintenance) carried every estate except the fixed-asset PM estate the workflow itself describes | OC-08 companion — vehicle true | Fixed — steps 1, 2, 5 name eAM PM scheduling, work-order costing and the eAM work-order history; the eAM coverage-map row now carries the VS-35 estate (W1695 PM work orders, history feeding the W1706 condition assessment) |
| 2 | W3234 registered and tagged IT hardware without the mass-additions gate and without a custodian of record — IT equipment is the canon's named-individual custody class, and the register entry could not say who held the device | OC-04, OC-05, OC-06 | Fixed — step 3 routes capitalizable lines through the mass additions queue, assigns the named-individual custodian into Assigned-To, and makes the tag-scan confirmation the custody acceptance |
| 3 | W3235 deployed devices to sites with a CMDB confirmation only — custody moved with no release-and-accept event, leaving Assigned-To stale at the staging custodian | OC-07 | Fixed — steps 2–3 record the staging release and site acceptance, update Assigned-To at deployment, and name the acceptance scan as the custody acceptance on the register |
| 4 | W3238 refresh waves recovered devices into the spare pool with no custody event — pool inventory drifted unowned between waves | OC-07 | Fixed — step 2 names the release-and-accept into the IT Asset Manager's spare-pool custody on the Assigned-To field |

Recorded conformant at corpus level: position-hierarchy approval routing with tiered value gates
(the R==A rows in steps tables are escalation phrasing — preparer and approver are different
roles), the OT asset register as a security view reconciled to the financial register (VS-190),
calibration devices as eAM maintainable assets under role-of-record custody (VS-115), and the
IT/OT retirement chains gating derecognition through the VS-35.3 approval workflows (OC-09).

---

## 8. Corpus-wide conformance review — 2026-09-23 (third pass: close and cash)

The third pass extended the review to the close-and-cash classes the first two passes did not
sweep: the bank-reconciliation preparer's independence from payment execution, the GL close
sequence, the receipt-application/credit-memo pair, the count-executor/adjustment-approver pair,
and credit checking before order release. Two findings — both repaired in the same pass:

| # | Finding | Rule | Disposition |
|---|---|---|---|
| 1 | W89's reconciliation preparer and sign-off was the Treasury Analyst — the same role that initiates and releases payment files (the W320.1 maker seat, W1362 steps 3–6) — so the payment maker reconciled the very accounts they paid from; the classic disbursement-fraud window the maker-checker design of W320 never closed on the accounting-control side | OC-24 | Fixed — W89 steps 1–6 and the aging follow-up re-seated to the entity GL Accountant (register mandate 'Entity books: GL, reconciliations, accruals', no payment-execution seat); the Background and touchpoints name the independence principle; W9A step 9 re-pointed to the same convention; CTL-19's owner and activity cells trued (v14) |
| 2 | W9A step 17 locked the period with no close-order discipline — the corpus never stated which periods close first, and the new period's open order was undefined, so a sub-ledger could stay open while GL locked (or a transaction post to a closed period at month-open) | OC-25 | Fixed — step 17 now verifies the suite's sequence: sub-ledgers (Inventory, PO, AP, AR, CE) closed and fully transferred and reconciled to GL before GL locks (bank per W89, fixed assets per W1705, payroll per W10); GL closes last; the new period opens Inventory → PO → AP → AR before GL |

Recorded conformant at corpus level: W1362 step 8's next-day bank debit-confirmation against the
payment batch (a payment-completeness check by the executor — distinct from the accounting
reconciliation, which is W89's and now independent); the daily W30 treasury auto-match
(operational cash visibility, not the monthly control); the W1468 weekly sweep/deposit
statement matching and the W1382 monthly electronic-payment statement reconciliation (both
re-seated to the GL Accountant as finding-class repairs above); the W1380 PDC-clearance
matching step (a Treasury operations status feed into W89, relabeled to its true sense); the
PA-15.2 monthly payment-channel reconciliation (processor totals vs settlement — a channel
operations control, not the statement-to-GL reconciliation) and the PA-18.2 bank-fee
monitoring (a bank-relationship duty) — both adjudicated exempt from OC-24; AR receipt
application beside approver-gated credit memos (W8.9/W8.11 — the §7 adjudication stands); the
DC cycle-count chain (blind recount by the Inventory Control Clerk, adjustment approval by the
DC Operations Manager — count executor never approves their own count, W1413.3/W1413.8);
credit checking before order release (the W164.3 validation engine and the W229
exception-and-escalation workflow). The third pass also adds the bank-reconciliation census
scan to the companion tool: PA-18.1's daily-visibility steps exempt, every other
bank-reconciliation step naming a payment-execution seat reports for triage.

---

## 9. Corpus-wide conformance review — 2026-09-23 (fourth pass: marketing & trade spend)

The fourth pass scoped the review to the marketing estate the first three passes had not
examined: VS-14 (campaign, digital, brand/PR), VS-139 (trade-show & event marketing),
PA-39.2 (co-op marketing funds) and the RMN billing chain. The strategic posture is unchanged
(marketing execution stays in-house per the coverage map's non-adoption boundary) — the pass
trues the EBS-facing mechanics: spend commitment, approval routing, trade-spend vehicles,
billing, and the booth custody chain. Seven findings — all repaired in the same pass:

| # | Finding | Rule | Disposition |
|---|---|---|---|
| 1 | W677 tracked marketing budget after the fact — media spend is committed on platform dashboards outside EBS and arrived as mostly non-PO invoices, with no funds check at commitment time | OC-13 companion — commitment accounting | Fixed — step 1 loads the approved budget into the GL budget organization (marketing cost center × GL account × month) with budgetary control enabled; step 3 releases agency retainers and media buys against blanket POs so the funds check fires at requisition/PO approval |
| 2 | W677's spend thresholds (agency POs > PHP 500K, media buys > PHP 1M) named approvers but no routing mechanism — approval could ride an ad-hoc name chain | OC-17 | Fixed — step 2 routes the thresholds by position hierarchy and AME rules |
| 3 | W83's campaign budget gates (CFO > PHP 1M, CEO > PHP 5M) named approvers but no routing mechanism; W83 step 25 requisitions tagged the campaign cost center but funds-checked nothing before approval | OC-17, OC-01 | Fixed — step 4 routes the gates by position hierarchy + AME; step 25 requisition lines carry destination type Expense charged to the campaign cost center with a GL budgetary-control funds check before approval |
| 4 | W833's compliance sign-off recorded a digital approval with no evidence class and no submitter/approver separation | OC-16 companion; ERES | Fixed — step 6 captures the sign-off as ERES evidence on the compliance record, routed by position hierarchy so the submitting Marketing Manager can never approve their own submission |
| 5 | W286's RMN billing named a generic 'Marketing Module (RMN)' vehicle and invoiced without a revenue-schedule treatment | Vehicle true; A11 | Fixed — step 3 and the touchpoints name OM/AR AutoInvoice on the vendor TCA account (AP debit-memo offset where the vendor is also a supplier) and AR Revenue Management (the A11 vehicle) for multi-element media contracts |
| 6 | PA-39.2's co-op chain (W1795 fund agreement, W1798 proof-of-performance, W1799 claim & settlement) ran a manual negotiate→execute→proof→reimburse cycle while the coverage map and the sibling rebate flows resolve vendor-funded trade spend in Oracle Trade Management (B10) — the co-op funds lived on a manual side-register | Vehicle true — OTM (B10) | Fixed — W1795 step 2 sets the fund up in OTM with purchase-based accrual; W1798 step 3 attaches the POP evidence to the OTM claim record; W1799 steps 2 and 4 settle claims and reconcile quarterly balances against the OTM fund |
| 7 | W4201/W4207 tracked the modular-booth estate as generic 'asset tracking' — no mass-additions gate at first build, no custodian of record, and show-to-show moves with no custody event (the W3235/W3238 drift class) | OC-04, OC-05, OC-07 | Fixed — W4201 step 2 routes capitalizable booth structures PO → invoice → Mass Additions queue into Oracle Assets with the Event Marketing Manager as custodian of record in Assigned-To; W4207 steps 1–2 record the show release and the storage release-and-accept with the Assigned-To move |

Recorded conformant at pass level: marketing execution, loyalty/CRM, CDP and campaign
attribution remaining on the in-house stack (the documented non-adoption boundary — no Oracle
Marketing/iStore adoption implied); W677's GL reconciliation and 80% threshold alerting; the
W4207 sample/return reconciliation to inventory (VS-05). The pass also trues the W288/W1545
cost-center governance language to the accounting-flexfield objects the hierarchy actually
manages (cost-center segment values, roll-up groups, cross-validation rules) — PA-29.2 steps
edited in the same pass.

---

## 10. Corpus-wide conformance review — 2026-09-23 (fifth pass: payroll and people costing)

The fifth pass scoped the review to the payroll estate the first four passes had not examined: the
in-house Payroll PH engine's path into the ledger of record, the 13th-month accrual family, and the
payroll disbursement rails. Five findings — all repaired in the same pass:

| # | Finding | Rule | Disposition |
|---|---|---|---|
| 1 | W10 step 9 posted payroll journals to GL through an unnamed mechanism — the in-house engine could write outside journal validation, approval and the W9A close discipline (the ledger-of-record analog of the mass-additions bypass) | OC-26 | Fixed — step 9 and the W10.9 touchpoint name the GL interface → Journal Import chain under the Payroll PH source, validated and posted inside the W9A close; W1416 step 1's per-run accrual journals, W1384 step 5 and the PA-19.5 resignation final-pay posting ride the same chain |
| 2 | W644 step 3 posted a parallel manual monthly accrual journal (Finance Analyst) while W1416 step 1 booked the accrual automatically per payroll run — two owners, two cadences, one liability, with a double-posting ambiguity; W1416 step 2(c) posted quarterly adjustments with no review rails | OC-27 | Fixed — W644 step 3 re-scoped to verifying the W1416-imported accrual and reconciling to the payroll register (no parallel manual posting), corrections routed through the W638 matrix; W1416 step 2(c) names W638 (preparer ≠ approver) |
| 3 | The off-cycle, final-pay and 13th-month payment rails unseated or mis-seated transmission: W641 step 6 approved its own bank file with no named transmitter; W643 step 6 and W644 step 8 executed payment inside the payroll/Finance chain; W1416 step 5(b) cited W34 — the store shift-scheduling workflow — for the payment release; CTL-13 of record already seats Treasury as transmitter, so the workflows drifted from the control | OC-28 | Fixed — all four rails trued to the W10 step-8 convention (Treasury transmits under approved release, CTL-13 cited); W641/W643/W644/W1416 Participants gain the Treasury seat; W644 step 9's parallel reversal form re-scoped to zero-balance verification of the W1416 step-5 postings |
| 4 | W1306's Volume row carried ~PHP 100–120M/month in total statutory contributions against W1527's ~PHP 25–30M canon on the same 6,932-employee population — a ~4× intra-estate conflict (the calibrated-volume class; ~PHP 100–120M would exceed the SSS/PhilHealth/Pag-IBIG cap arithmetic for the estate) | Volume canon | Fixed — W1306 Volume trued to the W1527 canon (~PHP 25–30M/month, employee + employer share) |
| 5 | W644 steps 3, 8 and 9 as a set made W644 a shadow 13th-month engine beside W1416 (its own accrual posting, its own payment execution, its own reversal) — the two-workflow-one-process ambiguity the corpus resolved for W12/W1622 by scoping, here resolved by re-seating W644 as the verification/reconciliation slice | OC-26, OC-27, OC-28 | Fixed — W644 step 3 verifies the W1416 accrual, step 8 monitors Treasury's transmission, step 9 verifies the zero balance; W1416 remains the computation/accrual/payment engine of record |

Recorded conformant at pass level: W816's intercompany payroll allocations (dual-entry journals per
W638 with balanced intercompany positions per W235 — the §7 position-hierarchy adjudication class);
W5540's failure canon (CTL-13 preservation under time pressure, the Treasury funding seat, the W641
advance-recovery rails); W1527's deduction-to-remittance reconciliation and W1306 step 4's GL
liability reconciliation (sub-ledger owners reconciling their own ledger to GL — reading GL, not the
bank statement; OC-24 untouched); W280's deduction prioritization with the AP liability booking;
W9A step 18's close-side 13th-month accrual reconciliation (complementary to W1416 step 2's quarterly
deep reconciliation); and the W638 tiered journal-approval matrix itself (the OC-27 mechanism of
record). The pass also adds the payroll payment-file transmission census scan to the companion tool:
a payroll/HR-responsible step transmitting or releasing a bank file with no Treasury seat reports
for triage.

---

*Document Version: 1.5 | Date: 2026-09-23 | **Seventy-sixth-wave consistency review (census re-point).** §1's live framing sentence re-pointed 5,432 → 5,433 workflows — the batch-30 census straggler on this document (the corpus moved under the fifth pass and no conformance arm read the canon's own §1 census cell); no rule, family, finding or §-content change. Prior v1.4 | Date: 2026-09-23 | **Payroll & people-costing conformance review.** §10 fifth pass — five findings across PA-19.2/PA-19.5, all repaired same-pass: W10 step 9's payroll costing journals routed through the GL journal-import chain (OC-26, the ledger-of-record mass-additions analog); the W644/W1416 13th-month double-posting ambiguity resolved with W638-routed corrections (OC-27); the off-cycle/final-pay/13th-month transmission seats trued to Treasury per CTL-13 and the W34 misdirected citation repaired (OC-28); W1306's ~4×-overclaimed statutory-contribution volume trued to the W1527 canon. New rules OC-26–OC-28 in family I. Prior v1.3 | Date: 2026-09-23 | **Marketing & trade-spend conformance review.** §9 fourth pass — seven findings across VS-14/VS-139/PA-39.2/W286, all repaired same-pass: W677 GL-budget-organization commitment accounting + AME routing, W83 AME budget gates + funds-checked requisitions, W833 ERES sign-off with submitter/approver separation, W286 OM/AR AutoInvoice + AR Revenue Management (A11) billing, PA-39.2 co-op chain trued to Oracle Trade Management (B10), W4201/W4207 booth estate through the custody canon (Mass Additions, custodian of record, release-and-accept), W288/W1545 cost-center governance trued to accounting-flexfield objects. Prior v1.2 | Date: 2026-09-23 | **Close-and-cash conformance review.** §8 third pass — the bank-reconciliation preparer seated independent of payment execution (OC-24: W89 re-owned to the entity GL Accountant, W9A step 9 re-pointed, CTL-19 trued) and the GL close sequence codified (OC-25: W9A step 17 sub-ledgers-before-GL); new rules OC-24/OC-25 in families D2/H; two findings, all repaired same-pass. Prior v1.1 | Date: 2026-09-23 | **Corpus-wide conformance review.** §7 second pass — all 569 process areas swept across the canon's judgment classes; four findings (eAM vehicle naming on W1695 closing the tracked triage item; custody-of-record chain on W3234/W3235/W3238), all repaired same-pass; corpus-wide SoD census added to the companion tool. Prior v1.0 (2026-09-23): initial canon — OC-01–OC-23 in seven families; §4 custody-of-record operating model; §5 enforcement contract; §6 initial conformance review — eleven findings, all repaired same-pass.*
