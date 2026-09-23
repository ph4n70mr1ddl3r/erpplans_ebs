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
    (CANON, "*Document Version: 1.2 | Date: 2026-09-23", "DOC",
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
]

# --- retired forms: (file, banned substring, description) ---------------------------
RETIRED = [
    (P351, "(a) PO with asset category flag triggers asset creation workflow",
     "retired W1690 step 1(a) — capitalization now names the mass additions queue"),
    # §8 third pass — the retired bank-reconciliation preparer forms
    (P174, "spread across 2 Treasury Analysts",
     "retired W89 staffing attribution — reconciliation moved to the entity GL Accountants (OC-24)"),
    (P174, "| 9 | Bank reconciliation: Match bank statements to GL cash accounts (all bank accounts, all entities) | Treasury Analyst |",
     "retired W9A step 9 form — the close reconciliation names the independent preparer (OC-24)"),
    (ICTL, "| Treasury Analyst / Controller | W30.2, W30.9, W89 |",
     "retired CTL-19 owner form — the control seats the entity GL Accountant (OC-24)"),
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
