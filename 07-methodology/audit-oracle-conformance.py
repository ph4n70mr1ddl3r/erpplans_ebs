#!/usr/bin/env python3
"""
audit-oracle-conformance.py — Oracle EBS best-practice conformance guard.

Companion to 02-oracle-ebs/oracle-ebs-conformance-standards.md (the canon, OC-01…OC-23).
Issued 2026-09-23 with the initial conformance review of the custody and treatment
chain (VS-35 fixed assets, VS-34 non-merchandise supplies, VS-40 capex turnover,
VS-15 invoice matching): eleven findings, all repaired in the same pass.
Extended 2026-09-23 with the corpus-wide second pass (canon §7 — all 569 process
areas swept across the canon's judgment classes): four findings repaired — the
W1695 eAM vehicle naming (closing the tracked triage item, the coverage-map eAM
row now carrying the VS-35 estate) and the W3234/W3235/W3238 IT-asset custody
chain (mass additions, custodian of record, tag-scan acceptance, release-and-
accept deployment and spare-pool re-custody).
Extended 2026-09-23 with the third pass (canon §8 — close and cash): two
findings repaired — W89's bank-reconciliation preparer re-seated to the entity
GL Accountant independent of payment execution (the Treasury/AP payment-file
seats never reconcile the accounts they pay from; W9A step 9 re-pointed, CTL-19
owner trued) and the GL close sequence codified on W9A step 17 (sub-ledgers
closed and reconciled before GL locks, GL last; new period opens sub-ledgers
first). New rules OC-24/OC-25.
Extended 2026-09-23 with the fourth pass (canon §9 — marketing & trade spend):
seven findings repaired across VS-14/VS-139/PA-39.2/W286 — W677 GL-budget-
organization commitment accounting (budgetary control + blanket PO releases)
and AME-routed spend thresholds; W83 AME budget gates and funds-checked
campaign requisitions (destination type Expense, campaign cost center); W833
ERES compliance sign-off with submitter/approver separation; W286 RMN billing
trued to OM/AR AutoInvoice on the TCA account + AR Revenue Management (A11);
the PA-39.2 co-op chain trued to Oracle Trade Management (B10) — fund setup
with purchase-based accrual, POP evidence on the claim record, claim settlement
and quarterly balance reconciliation; the W4201/W4207 booth estate through the
custody canon (Mass Additions, custodian of record, release-and-accept moves);
W288/W1545 cost-center governance trued to accounting-flexfield objects.

Extended 2026-09-23 with the fifth pass (canon §10 — payroll and people costing):
five findings repaired across PA-19.2/PA-19.5 — W10 step 9's payroll costing
journals routed through the GL journal-import chain (GL interface → unposted
batch under the Payroll PH source → GL validates and posts inside the W9A close;
OC-26, the ledger-of-record mass-additions analog, also pinned on W1416 step 1,
W1384 step 5 and the PA-19.5 resignation final-pay posting); the W644/W1416
13th-month double-posting ambiguity resolved with W638-routed corrections and
W644 re-scoped to verification (OC-27); the off-cycle/final-pay/13th-month
payment rails re-seated to Treasury transmission per CTL-13 with the W34
misdirected citation repaired (OC-28); and W1306's ~4×-overclaimed
statutory-contribution volume trued to the W1527 canon. New rules OC-26–OC-28
in family I; a payroll payment-file transmission census scan added.

Three rule families:

  * anchor rules   — the conformance clauses the review wrote into the repaired
                     workflows are required at their exact cells; stripping one
                     fires and forces a conscious re-point (house Check-71 pattern).
  * retired forms  — the replaced phrasings are banned in their files of scope so
                     the defect class cannot silently return.
  * corpus scans   — informational sweeps for the judgment classes the anchors
                     cannot reach (supplies capitalized inside PA-34, the Fixed
                     Asset Accountant appearing as the receiving Responsible role,
                     unattested count instructions). Reported as a census for
                     per-workflow triage; never guard-failing on their own.

Guard mode (--guard): anchor + retired-form rules only; exit 1 on any hit.
Default mode: everything, informational scans included; always exit 0 unless a
canon file itself is missing.
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WF = os.path.join(REPO, "01-model-company", "workflows")
CANON = os.path.join(REPO, "02-oracle-ebs", "oracle-ebs-conformance-standards.md")

# --- anchor rules: (file, required substring, rule id, description) -----------------
P351 = os.path.join(WF, "VS-35-fixed-asset-management", "PA-35.1-asset-registration-lifecycle.md")
P352 = os.path.join(WF, "VS-35-fixed-asset-management", "PA-35.2-depreciation-financial-reporting.md")
P353 = os.path.join(WF, "VS-35-fixed-asset-management", "PA-35.3-physical-verification-disposal.md")
P341 = os.path.join(WF, "VS-34-expense-procurement", "PA-34.1-non-merchandise-procurement.md")
P403 = os.path.join(WF, "VS-40-capex-project-accounting", "PA-40.3-cip-asset-turnover.md")
P991 = os.path.join(WF, "VS-99-it-asset-technology-lifecycle-management", "PA-99.1-it-hardware-asset-lifecycle-deployment.md")
P174 = os.path.join(WF, "VS-17-record-to-report", "PA-17.4-fpanda-and-reporting.md")
P082 = os.path.join(WF, "VS-08-pos-checkout", "PA-08.2-payment-and-cash-management.md")
P163 = os.path.join(WF, "VS-16-order-to-cash", "PA-16.3-customer-payment-and-settlement.md")
P142 = os.path.join(WF, "VS-14-marketing", "PA-14.2-digital-marketing-and-social-media.md")
P141 = os.path.join(WF, "VS-14-marketing", "PA-14.1-campaign-planning-and-execution.md")
P143 = os.path.join(WF, "VS-14-marketing", "PA-14.3-brand-pr-and-corporate-communications.md")
P1392 = os.path.join(WF, "VS-139-trade-show-exhibition-and-field-event-marketing", "PA-139.2-exhibition-and-trade-show-operations.md")
P392 = os.path.join(WF, "VS-39-vendor-rebate-incentive", "PA-39.2-coop-marketing-promotional-funds.md")
P292 = os.path.join(WF, "VS-29-master-data", "PA-29.2-financial-and-operational-masters.md")
P192 = os.path.join(WF, "VS-19-hire-to-retire", "PA-19.2-payroll-and-compensation.md")
P195 = os.path.join(WF, "VS-19-hire-to-retire", "PA-19.5-separation-and-benefits.md")
COVMAP = os.path.join(REPO, "02-oracle-ebs", "module-coverage-map.md")
ICTL = os.path.join(REPO, "01-model-company", "internal-controls-matrix.md")

ANCHORS = [
    # OC-05 custody of record — W1690 step 2(h) + touchpoint
    (P351, "assigns the asset custodian of record", "OC-05",
     "W1690 step 2 must assign the asset custodian of record"),
    (P351, "Assigned-To custodian field", "OC-05",
     "W1690 touchpoints must name the Assigned-To custodian field"),
    # OC-04 mass-additions queue gate — W1690 step 1(a) + touchpoint
    (P351, "mass additions queue", "OC-04",
     "W1690 step 1 must route capitalization through the mass additions queue"),
    (P351, "Mass Additions queue review", "OC-04",
     "W1690 touchpoints must name the Mass Additions queue review gate"),
    # OC-15 tractable-item pool — W1690 step 3
    (P351, "tractable items", "OC-15",
     "W1690 step 3 must declare the tractable-item pool"),
    # OC-06 tag scan = custody acceptance — W1692 step 4
    (P351, "custody-acceptance signature", "OC-06",
     "W1692 step 4 must record the custody-acceptance signature at tag scan"),
    # OC-07 transfer = release → accept — W1693 steps 1 and 4
    (P351, "releases the asset from custody", "OC-07",
     "W1693 step 1 must record the sending custodian's release"),
    (P351, "receiving custodian's custody acceptance", "OC-07",
     "W1693 step 4 must record the receiving custodian's acceptance"),
    # OC-08 corporate book / derived tax book — W1698 step 2
    (P352, "corporate book", "OC-08",
     "W1698 step 2 must name the corporate book as the depreciation book of record"),
    (P352, "derives from the corporate book", "OC-08",
     "W1698 step 2 must state the tax book derives from the corporate book"),
    # OC-10 custodian attestation — W1706 step 2
    (P353, "signs the count certification", "OC-10",
     "W1706 step 2 must require the custodian-of-record count attestation"),
    # OC-11 CIP custody handover — W1828 step 2
    (P403, "custody handover", "OC-11",
     "W1828 step 2 must include the custody handover to the operating custodian"),
    # OC-14 controlled-issue pool — W1670 step 4, W1673 step 3
    (P341, "from an expense subinventory per requisition", "OC-14",
     "W1670 step 4 must issue PPE/uniforms per requisition from an expense subinventory"),
    (P341, "counted quarterly", "OC-14",
     "W1670 step 4 must carry the recurring count of controlled-issue items"),
    (P341, "issued per requisition from the supplies storeroom custodian", "OC-14",
     "W1673 step 3 must issue controlled consumables per requisition under the storeroom custodian"),
    # canon document itself
    (CANON, "Every asset carries a **custodian of record**", "OC-05",
     "canon OC-05 custody-of-record rule"),
    (CANON, "*Document Version: 1.4 | Date: 2026-09-23", "DOC",
     "canon version footer"),
    # §7 second pass — W1695 eAM vehicle naming (canon-tracked triage closed)
    (P351, "eAM auto-generates the preventive maintenance schedule", "OC-EAM",
     "W1695 step 1 must name eAM PM scheduling as the vehicle"),
    (P351, "eAM work orders; records in the work order", "OC-EAM",
     "W1695 step 2 must record maintenance in the eAM work order"),
    (P351, "maintenance history available from the eAM work-order history", "OC-EAM",
     "W1695 step 5 must read history from the eAM work-order history"),
    (COVMAP, "W1695 category-rule PM work orders", "OC-EAM",
     "the adopted eAM coverage-map row must carry the VS-35 fixed-asset PM estate"),
    # §7 second pass — W3234 IT-asset registration custody chain
    (P991, "mass additions queue for Fixed Asset review", "OC-04",
     "W3234 step 3 must route capitalizable IT purchases through the mass additions queue"),
    (P991, "custodian of record into the Assigned-To field", "OC-05",
     "W3234 step 3 must assign the IT custodian of record into Assigned-To"),
    (P991, "tag-scan confirmation doubles as that custodian's custody acceptance", "OC-06",
     "W3234 step 3 must make the tag scan the custody acceptance"),
    # §7 second pass — W3235 deployment release-and-accept
    (P991, "custody transfers as a release-and-accept event", "OC-07",
     "W3235 step 2 must record deployment as a release-and-accept custody event"),
    (P991, "updates the asset register's Assigned-To field", "OC-07",
     "W3235 step 2 must update Assigned-To at deployment"),
    # §7 second pass — W3238 spare-pool re-custody
    (P991, "spare pool as a release-and-accept event", "OC-07",
     "W3238 step 2 must re-custody recovered devices into the spare pool by release-and-accept"),
    # §8 third pass — OC-24 bank-reconciliation independence (W89 re-owned to the entity GL Accountant)
    (P174, "**Owner** | GL Accountant |", "OC-24",
     "W89 must be owned by the entity GL Accountant (independent of payment execution)"),
    (P174, "independent of payment execution (the Treasury Analyst and AP Clerk roles that initiate, approve or release payment files", "OC-24",
     "W89 step 6 must name the payment-execution independence principle"),
    (P174, "executed by the entity GL Accountant independent of payment execution per W89", "OC-24",
     "W9A step 9 must re-point the close bank reconciliation to the independent preparer per W89"),
    (ICTL, "monthly full reconciliation per entity by the entity GL Accountant independent of payment execution", "OC-24",
     "CTL-19 must seat the bank-reconciliation control with the entity GL Accountant"),
    (CANON, "The bank-statement reconciliation is prepared by a role independent of payment execution", "OC-24",
     "canon OC-24 bank-reconciliation independence rule"),
    # §8 third pass — OC-25 GL close sequence (W9A step 17)
    (P174, "sub-ledger periods (Inventory, PO, AP, AR and Cash Management) are closed and fully transferred and reconciled to GL", "OC-25",
     "W9A step 17 must verify sub-ledgers closed and reconciled to GL before the GL period locks"),
    (P174, "the new period's sub-ledgers open first (Inventory → PO → AP → AR) and GL last", "OC-25",
     "W9A step 17 must state the new period's open order (sub-ledgers before GL)"),
    (CANON, "GL closes last", "OC-25",
     "canon OC-25 close-sequence rule"),
    # §8 third pass — scan-triage repairs (the bank-reconciliation census scan's findings)
    (P082, "GL Accountant reconciles all bank statements against ERP cash ledger weekly per W89, independent of payment execution", "OC-24",
     "W1468 step 5 must seat the weekly statement-to-ledger reconciliation with the GL Accountant"),
    (P163, "Monthly: GL Accountant reconciles electronic payment bank statements to GL cash postings per W89, independent of payment execution", "OC-24",
     "W1382 step 7 must seat the monthly statement-to-GL reconciliation with the GL Accountant"),
    (P163, "PDC clearance matching (feeds W89)", "OC-24",
     "W1380 step 7 must carry the PDC-clearance-matching sense, not the reconciliation-vehicle name"),
    # §9 fourth pass — W677 commitment accounting + AME routing
    (P142, "GL budget organization by marketing cost center × GL account × month with GL budgetary control enabled", "OC-13C",
     "W677 step 1 must load the approved budget into the GL budget organization with budgetary control enabled"),
    (P142, "routed by position hierarchy and AME rules, never an ad-hoc name chain", "OC-17",
     "W677 step 2 must route spend thresholds by position hierarchy and AME rules"),
    (P142, "release against blanket POs so the GL budgetary-control funds check fires at requisition and PO approval", "OC-13C",
     "W677 step 3 must commit agency/media spend through blanket PO releases funds-checked at commitment"),
    # §9 fourth pass — W83 budget gates + funds-checked requisitions
    (P141, "routed by position hierarchy and AME rules (CFO gate above PHP 1M, CEO gate above PHP 5M), never an ad-hoc name chain", "OC-17",
     "W83 step 4 must route campaign budget gates by position hierarchy and AME rules"),
    (P141, "destination type Expense charged to the campaign cost center and funds-check against the campaign envelope in GL budgetary control before approval", "OC-01",
     "W83 step 25 must carry destination-type-Expense campaign requisitions with a pre-approval funds check"),
    # §9 fourth pass — W833 ERES sign-off + submitter/approver separation
    (P143, "captured as ERES evidence on the compliance record and routed by position hierarchy", "OC-16",
     "W833 step 6 must capture the compliance sign-off as ERES evidence with submitter/approver separation"),
    # §9 fourth pass — W286 RMN billing on the AR spine
    (P143, "OM/AR AutoInvoice on the vendor's TCA account", "OC-AR",
     "W286 step 3 must generate RMN invoices via OM/AR AutoInvoice on the TCA account"),
    (P143, "AR Revenue Management — PFRS 15 revenue schedules for multi-element media contracts (the A11 vehicle)", "OC-AR",
     "W286 touchpoints must name AR Revenue Management for PFRS 15 schedules"),
    # §9 fourth pass — PA-39.2 co-op chain on Oracle Trade Management (B10)
    (P392, "System setup in Oracle Trade Management (fit-gap B10, the same agreements master the rebate estate rides per W27/PA-39.1)", "OC-OTM",
     "W1795 step 2 must set the co-op fund up in Oracle Trade Management with purchase-based accrual"),
    (P392, "attached to the vendor's Oracle Trade Management claim record (fit-gap B10)", "OC-OTM",
     "W1798 step 3 must attach POP evidence to the OTM claim record"),
    (P392, "against the Oracle Trade Management claim (fit-gap B10)", "OC-OTM",
     "W1799 step 2 must settle the reimbursement against the OTM claim"),
    (P392, "against the Oracle Trade Management fund balances (fit-gap B10)", "OC-OTM",
     "W1799 step 4 must reconcile quarterly fund balances to OTM"),
    # §9 fourth pass — booth estate custody chain
    (P1392, "flow PO → invoice → Mass Additions queue into Oracle Assets at first build, registered with the Event Marketing Manager as custodian of record in Assigned-To", "OC-04/OC-05",
     "W4201 step 2 must route capitalizable booth structures through Mass Additions with a custodian of record"),
    (P1392, "as a release-and-accept custody event — the storage custodian of record accepts", "OC-07",
     "W4207 step 2 must recover booth assets as a release-and-accept custody event moving Assigned-To"),
    # §9 fourth pass — cost-center governance on the accounting flexfield
    (P292, "accounting-flexfield cost-center segment value in the CoA, assigns it to its parent roll-up group", "OC-KFF",
     "W288 step 4 must create cost centers as accounting-flexfield segment values under roll-up groups"),
    (P292, "creates the value in the accounting flexfield — cost-center segment under the department roll-up group for HQ cost centers, the store hierarchy's profit-center segment for stores", "OC-KFF",
     "W1545 step 2 must name the flexfield segments for cost/profit-center creation"),
    # §10 fifth pass — OC-26 the payroll journal-import chain (the engine never posts directly)
    (P192, "imports them as unposted batches under the Payroll PH source", "OC-26",
     "W10 step 9 must import payroll costing journals as named-source unposted batches — the engine never posts directly to the ledger"),
    (P192, "GL posting from payroll: costing journals import to GL through the GL journal-import chain", "OC-26",
     "W10 touchpoints must name the GL journal-import chain"),
    (P192, "imported to GL through the W10.9 journal-import chain", "OC-26",
     "W1416 step 1 must import the per-run accrual journals through the W10.9 chain"),
    (P195, "System posts 13th month pay through the W10.9 journal-import chain", "OC-26",
     "W1384 step 5 must post through the W10.9 journal-import chain"),
    (P195, "system posts final pay through the W10.9 costing chain", "OC-26",
     "the PA-19.5 resignation final-pay posting must ride the W10.9 costing chain"),
    (COVMAP, "posts costing journals into GL via the GL journal-import chain", "OC-26",
     "the coverage-map HR & Payroll row must name the GL journal-import chain"),
    (CANON, "The payroll engine never posts directly to the ledger", "OC-26",
     "canon OC-26 payroll journal-import rule"),
    # §10 fifth pass — OC-27 manual payroll journals ride W638; no parallel accrual posting
    (P192, "no parallel manual accrual posting", "OC-27",
     "W644 step 3 must verify the W1416-imported accrual, not post a parallel manual JE"),
    (P192, "correction journals ride the W638 journal-entry review matrix", "OC-27",
     "W644 step 3 corrections must ride the W638 journal-entry review matrix"),
    (P192, "post adjustments as needed through the W638 journal-entry review matrix (preparer ≠ approver)", "OC-27",
     "W1416 step 2(c) must route accrual adjustments through the W638 matrix"),
    (CANON, "ride the journal-entry review workflow with tiered approval and preparer ≠ approver", "OC-27",
     "canon OC-27 payroll-journal review rule"),
    # §10 fifth pass — OC-28 Treasury transmits every payroll payment file
    (P192, "Treasury transmits the approved file per the W10 step-8 payroll bank-file chain — the payroll chain never transmits its own payment files", "OC-28",
     "W641 step 6 must seat bank-file transmission with Treasury"),
    (P192, "Treasury transmits the approved final-pay file per the W10 step-8 payroll bank-file chain", "OC-28",
     "W643 step 6 must seat final-pay transmission with Treasury"),
    (P192, "Treasury transmits the approved 13th month payment file per the W10 step-8 payroll bank-file chain", "OC-28",
     "W644 step 8 must seat 13th-month payment transmission with Treasury"),
    (P192, "Treasury transmits per the W10 step-8 payroll bank-file chain", "OC-28",
     "W1416 step 5(b) must seat the payment release on the W10 step-8 chain"),
    (CANON, "Payroll payment files are transmitted by the Treasury payment-execution seat", "OC-28",
     "canon OC-28 payroll-transmission rule"),
    # §10 fifth pass — W1306 volume canon
    (P192, "~PHP 25–30M/month in total statutory contributions (employee + employer share, per W1527)", "VOL",
     "W1306 Volume must carry the W1527 statutory-contribution canon"),
]

# --- retired forms: (file, banned substring, description) ---------------------------
RETIRED = [
    (P351, "(a) PO with asset category flag triggers asset creation workflow",
     "retired W1690 step 1(a) — capitalization now names the mass additions queue"),
    # §9 fourth pass — the retired generic RMN vehicle form
    (P143, "- Marketing Module (RMN) for impression aggregation, yield calculation, and vendor contract terms",
     "retired W286 touchpoint — generic 'Marketing Module' vehicle replaced by the in-house RMN platform feeding OM/AR AutoInvoice"),
    # §8 third pass — the retired bank-reconciliation preparer forms
    (P174, "spread across 2 Treasury Analysts",
     "retired W89 staffing attribution — reconciliation moved to the entity GL Accountants (OC-24)"),
    (P174, "| 9 | Bank reconciliation: Match bank statements to GL cash accounts (all bank accounts, all entities) | Treasury Analyst |",
     "retired W9A step 9 form — the close reconciliation names the independent preparer (OC-24)"),
    (ICTL, "| Treasury Analyst / Controller | W30.2, W30.9, W89 |",
     "retired CTL-19 owner form — the control seats the entity GL Accountant (OC-24)"),
    # §10 fifth pass — the retired payroll posting/transmission/volume forms
    (P192, "System posts payroll journal entries to GL (salary expense, payable, deductions)",
     "retired W10 step 9 — the unnamed direct-posting form replaced by the GL journal-import chain (OC-26)"),
    (P192, "Treasury releases payment per W34",
     "retired W1416 step 5(b) — the misdirected shift-scheduling citation replaced by the W10 step-8 chain (OC-28)"),
    (P192, "~PHP 100–120M/month",
     "retired W1306 volume — the ~4×-overclaimed statutory-contribution band replaced by the W1527 canon"),
    (P192, "Finance Analyst posts accrual journal entry (DR 13th Month Pay Expense",
     "retired W644 step 3 — the parallel manual accrual posting replaced by verification of the imported accrual (OC-27)"),
    (P192, "Finance Analyst executes payment via bank transfer",
     "retired W644 step 8 — payment execution re-seated to Treasury transmission (OC-28)"),
    (P192, "System reverses remaining accrual balance to actual payment",
     "retired W644 step 9 — the parallel reversal form replaced by zero-balance verification of the W1416 step-5 postings"),
    (P192, "routes for bank file approval |",
     "retired W641 step 6 — the unseated-transmission form (approval with no named transmitter) (OC-28)"),
    (P192, "prepares manual check |",
     "retired W643 step 6 — the unseated-transmission form (file prepared with no named transmitter) (OC-28)"),
    (P195, "system posts final pay: Dr. Salary Expense",
     "retired PA-19.5 step 7(c) — the unnamed final-pay posting form replaced by the W10.9 chain pin (OC-26)"),
]

# --- corpus scans (informational; per-workflow triage census) -----------------------
def corpus_scans():
    findings = []
    # scan 1: capitalization language inside the supplies process area (PA-34.*)
    for f in sorted(glob.glob(os.path.join(WF, "VS-34-*", "PA-*.md"))):
        text = open(f, encoding="utf-8").read()
        for m in re.finditer(r"[Cc]apitaliz\w*", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60].replace("\n", " ")
            # negated / prohibitive contexts are conformant uses
            if re.search(r"(never capitaliz|not capitaliz|no capitaliz|below the threshold|below the capitalization threshold)", ctx):
                continue
            findings.append(("scan-supplies-capitalization", os.path.relpath(f, REPO), ctx.strip()))
    # scan 2: segregation of duties — Fixed Asset Accountant as the receiving
    # Responsible role inside PA-35.1 (the register owner must not receive;
    # joint 'Fixed Asset Accountant / Receiving Clerk' tag/printing cells are
    # register-side work and exempt)
    p351_lines = open(P351, encoding="utf-8").read().splitlines()
    for line_no, line in enumerate(p351_lines, 1):
        if line.startswith("|") and re.search(r"\breceiv\w+\b", line.lower()):
            cells = [c.strip() for c in line.split("|")]
            if len(cells) > 4 and cells[3].startswith("Fixed Asset Accountant") and "Receiving Clerk" not in cells[3]:
                findings.append(("scan-sod-receiving", os.path.relpath(P351, REPO),
                                 f"line {line_no}: Fixed Asset Accountant is Responsible on a receiving step"))
    # scan 3: count instructions without an attestation clause in PA-35.3
    p353_text = open(P353, encoding="utf-8").read()
    if "signs the count certification" not in p353_text:
        findings.append(("scan-unattested-count", os.path.relpath(P353, REPO),
                         "physical-verification count carries no custodian attestation"))
    # scan 4 (canon §7 second pass): corpus-wide segregation-of-duties census —
    # the register owner (Fixed Asset Accountant) as the Responsible role on a
    # receiving or count-execution step in ANY process area (register-side joint
    # roles and review/reconcile/attest cells are exempt per the PA-35.1 rule;
    # the financial senses 'receivable', 'cash received' and the intercompany
    # 'receiving entity' are not goods receipt and are exempt)
    for f in sorted(glob.glob(os.path.join(WF, "VS-*", "PA-*.md"))):
        for line_no, line in enumerate(open(f, encoding="utf-8"), 1):
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.split("|")]
            if len(cells) <= 4 or not re.match(r"^\d+", cells[1] or ""):
                continue
            role = cells[3]
            act = cells[2].lower() if len(cells) > 2 else ""
            if not role.startswith("Fixed Asset Accountant") or "Receiving Clerk" in role:
                continue
            if re.search(r"receivable|cash received|receiving entity", act):
                continue
            if re.search(r"\breceiv(e|es|ed|ing)\b", act) or re.search(r"\b(perform|execut|conduct)[a-z]*\s+(the\s+)?(physical\s+)?count\b", act):
                findings.append(("scan-sod-register-owner", os.path.relpath(f, REPO),
                                 f"line {line_no}: Fixed Asset Accountant is Responsible on a receiving/count step"))
    # scan 5 (canon §8 third pass): bank-reconciliation steps carried by a
    # payment-execution role — the Treasury Analyst who initiates or releases
    # payment files (W320.1 maker, W1362 file generation/upload) must not be
    # Responsible for a bank-statement reconciliation step. PA-18.1 is exempt:
    # W30's daily auto-match is operational cash visibility (canon OC-24 keeps
    # the daily auto-match with Treasury and moves only the monthly control).
    for f in sorted(glob.glob(os.path.join(WF, "VS-*", "PA-*.md"))):
        if os.path.basename(f).startswith("PA-18.1"):
            continue
        for line_no, line in enumerate(open(f, encoding="utf-8"), 1):
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.split("|")]
            if len(cells) <= 4 or not re.match(r"^\d+", cells[1] or ""):
                continue
            role = cells[3]
            act = cells[2].lower() if len(cells) > 2 else ""
            if not role.startswith("Treasury Analyst"):
                continue
            if re.search(r"bank reconciliation|bank statement", act):
                # §8 adjudicated-exempt operations senses: the PA-15.2 monthly
                # payment-channel reconciliation (processor totals vs settlement —
                # a channel operations control) and the PA-18.2 bank-fee monitoring
                # (a bank-relationship duty). Neither is the statement-to-GL
                # accounting reconciliation.
                if re.search(r"payment channel|processor|fee monitor", act):
                    continue
                findings.append(("scan-sod-bank-recon", os.path.relpath(f, REPO),
                                 f"line {line_no}: Treasury Analyst (payment-execution seat) is Responsible on a bank-reconciliation step"))
    # scan 6 (canon §10 fifth pass): payroll payment-file transmission census —
    # a payroll/HR-responsible step that transmits, releases or sends a payroll
    # payment bank file reports for triage: the transmission seat is Treasury's
    # (CTL-13, canon OC-28); the payroll chain that computes and approves the run
    # never moves the money. File generation and approval routing by payroll
    # seats are the preparation side and are exempt.
    for f in sorted(glob.glob(os.path.join(WF, "VS-*", "PA-*.md"))):
        for line_no, line in enumerate(open(f, encoding="utf-8"), 1):
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.split("|")]
            if len(cells) <= 4 or not re.match(r"^\d+", cells[1] or ""):
                continue
            role = cells[3]
            act = cells[2].lower() if len(cells) > 2 else ""
            if not (role.startswith("Payroll") or role.startswith("HR")):
                continue
            if "bank file" not in act and "bank transfer file" not in act:
                continue
            if "treasury" in act:
                continue
            if re.search(r"\b(transmit|transmission|releas|send|sends|sent)\w*\b", act):
                findings.append(("scan-payroll-transmission", os.path.relpath(f, REPO),
                                 f"line {line_no}: payroll/HR seat transmits or releases a payment bank file (Treasury is the transmission seat, OC-28)"))
    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true",
                    help="exit 1 on any anchor/retired-form hit (corpus scans report only)")
    args = ap.parse_args()

    if not os.path.exists(CANON):
        print(f"canon-missing: {os.path.relpath(CANON, REPO)}")
        sys.exit(1)

    hits = []
    for path, needle, rid, desc in ANCHORS:
        text = open(path, encoding="utf-8").read()
        if needle not in text:
            hits.append(f"missing-anchor [{rid}]: {os.path.relpath(path, REPO)}: {desc}")
    for path, banned, desc in RETIRED:
        text = open(path, encoding="utf-8").read()
        if banned in text:
            line = text[:text.find(banned)].count("\n") + 1
            hits.append(f"retired-form: {os.path.relpath(path, REPO)}:{line}: {desc}")

    scans = corpus_scans()
    for kind, where, what in scans:
        print(f"{kind}: {where}: {what}")

    for h in hits:
        print(h)
    n_wf = len(glob.glob(os.path.join(WF, "VS-*", "PA-*.md")))
    print(f"audit-oracle-conformance: {len(hits)} conformance hit(s), {len(scans)} corpus-scan finding(s) across {n_wf} PA files")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
