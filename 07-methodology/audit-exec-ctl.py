#!/usr/bin/env python3
"""
audit-exec-ctl.py — executive-summary anchor & CTL citation-scope guard.

Consistency review #42 (2026-08-29) audited the two remaining never-swept
surfaces:

  * executive-summary.md narrative beyond its guarded figure anchors — every
    quantitative and descriptive claim verified against the canonical
    registers: the company table (200 stores, 4 DCs at Davao/Cebu/Laguna/
    Clark per profile §3.2, 5 entities per §2, PHP 62.3B, 6,762 employees,
    35,000 SKUs, 600 terminals = 3/store, 2.8M monthly transactions,
    ~600,000 loyalty members matching the W1217 base), the critical
    requirements (offline ≥ 8 hours, 300+ store scalability per profile §10),
    the operational metrics (POS uptime 99.9% = NFR-001, month-end close
    ≤ 5 working days = FIN-015, inventory accuracy ≥ 97%), and the footer
    counts (728 requirements / 5,387 workflows / 188 VS / 6,762 HC [re-based
    5,384 → 5,387 by the 2026-09-04 operations-workflow gap-fill pass
    (batch 11, W5532–W5534); previously re-based 5,381 → 5,384 by the
    2026-09-03 finance-workflow gap-fill pass (batch 10, W5529–W5531)
    2026-09-03 people-capability & reporting-policy gap-fill pass
    (batch 9, W5525–W5528); previously re-based 5,363 → 5,364
    by the description-trueness pass when the event-custody pass's W5511
    re-point list was found to have missed both this anchor and the doc line
    it pins], the
    14-workflow post-catalog set, and the 733 → 728 dedup note). CLEAN.
  * the internal-controls-matrix CTL register's descriptive text vs the PA
    files that cite each CTL — CTL-240–808 citations already carry canonical
    PA names (Check 34); the CTL-001–239 citations carry free-form application
    notes by convention. The defect class found and repaired: 33 citations of
    the SPEND controls (CTL-01 'Prevent unauthorized purchases', CTL-02
    'Prevent unauthorized capital expenditure') in VS-184–191 carried
    non-spend application notes ('IR governance', 'test governance/safety
    sign-off', 'subordination approval', 'exercise governance'…) — stretched
    semantic reuse of spend-authorization controls for generic approval
    governance. Each was re-pointed to the workflow's OWN PA-level execution
    control in the Check-34 canonical form with the application note preserved
    as an em-dash suffix. One genuinely spend-related citation
    ('capital/program approval') was kept.

Guard mode (--guard, validator Check 60):
  1. executive-summary.md must carry the canonical anchor figures and must
     not carry retired ones (6,757/6,715/5,3xx);
  2. CTL-01/CTL-02 citations anywhere in the PA files must contain spend
     vocabulary in their parenthetical (purchase/procurement/capex/capital/
     spend/expenditure/vendor/supplier/PO/order).
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MC = os.path.join(REPO, "01-model-company")

ANCHORS = ["| Employees | 6,932 |", "| Active SKUs | 35,000 |",
           "| Stores | 200 (nationwide: Luzon, Visayas, Mindanao) |",
           "| POS Terminals | 600 (3 per store) |",
           "| Monthly Transactions | 2.8 million |",
           "| Annual Revenue | ~PHP 62.3 Billion |",
           "| Loyalty Members | ~600,000 |",
           "728 requirements, 5,427 workflows across 188 value streams, 6,762 employees"]
RETIRED = ["6,757", "6,715", "5,357", "5,362", "5,349", "5,341", "5,364", "5,367", "5,384"]
SPEND = ("purchase", "purchasing", "procurement", "capex", "capital", "spend",
         "expenditure", "buying", "vendor", "supplier", "po ", "order")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true",
                    help="exit 1 on any anchor/citation-scope violation")
    args = ap.parse_args()
    hits = []
    text = open(os.path.join(MC, "executive-summary.md"), encoding="utf-8").read()
    for anchor in ANCHORS:
        if anchor not in text:
            hits.append(("exec-anchor", "executive-summary.md", 0,
                         f"missing canonical anchor: '{anchor[:60]}'"))
    # retired-figure scan: italic footers and 'X -> Y' change-notes exempt
    for i, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("*") or "\u2192" in line or "->" in line:
            continue
        for lit in RETIRED:
            if lit in line:
                hits.append(("exec-anchor", "executive-summary.md", i,
                             f"retired figure {lit}"))
    for f in sorted(glob.glob(os.path.join(MC, "workflows", "VS-*", "PA-*.md"))):
        t = open(f, encoding="utf-8").read()
        for m in re.finditer(r"\b(CTL-0[12])\s*\(([^)]+)\)", t):
            if not any(s in m.group(2).lower() for s in SPEND):
                hits.append(("spend-ctl-scope", os.path.relpath(f, REPO),
                             t[:m.start()].count("\n") + 1,
                             f"{m.group(1)} cited for non-spend note '{m.group(2)[:50]}'"))
    for kind, rel, line, detail in hits:
        print(f"{kind}: {rel}:{line}: {detail}")
    print(f"audit-exec-ctl: {len(hits)} hit(s)")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
