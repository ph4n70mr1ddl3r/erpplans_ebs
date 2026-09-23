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
COVMAP = os.path.join(REPO, "02-oracle-ebs", "module-coverage-map.md")

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
    (CANON, "*Document Version: 1.1 | Date: 2026-09-23", "DOC",
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
]

# --- retired forms: (file, banned substring, description) ---------------------------
RETIRED = [
    (P351, "(a) PO with asset category flag triggers asset creation workflow",
     "retired W1690 step 1(a) — capitalization now names the mass additions queue"),
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
