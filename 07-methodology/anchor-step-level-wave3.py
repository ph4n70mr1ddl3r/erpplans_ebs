#!/usr/bin/env python3
"""Step-level anchoring wave 3 — batch 44 (2026-09-23, by direction).

Third elevation wave for the weak-anchor watchlist's NO PARSED CADENCE roles
(the batch-39/41 co-performer pattern — Role (R) cells gain the chartered
co-performer; no durations, frequencies, step texts or ownership cells
changed):

  Banking & Cash-Management Specialist  → petty-cash custodian control
                                          (PA-18.2)
  Corporate Secretary Analyst           → disclosure-controls operation
                                          (PA-173.2)
  Import Documentation Specialist       → customs brokerage filing (PA-02.2)
  B2B Support Representative            → wholesale SO entry (PA-11.3)
  Replenishment & Allocation Analyst    → end-of-replenishment cycle
                                          confirmation (PA-07.3)
  CPM Analyst                           → corporate scorecard production
                                          (PA-33.2)

Idempotent; every edit asserts its anchor. Regenerate the matrix, bpmn/ and
both gap/verification artifacts afterwards.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
WF = os.path.join(REPO, "01-model-company", "workflows")

# (relpath, unique step-text substring, old-R-cell-exact, role-to-add)
ELEVATIONS = [
    ("VS-18-treasury-cash/PA-18.2-banking-and-payments.md",
     "Store Manager / Finance Controller",
     "Store Manager / Finance Controller", "Banking & Cash-Management Specialist"),
    ("VS-173-investor-relations-capital-markets-and-securities-disclosure/PA-173.2-corporate-disclosure-securities-and-regulatory-compliance.md",
     "Operate the disclosure-controls framework",
     "VP IR / Legal / Compliance", "Corporate Secretary Analyst"),
    ("VS-02-supply-planning/PA-02.2-import-and-customs-operations.md",
     "Shipping Documents**: Receive set of documents: Bill of Lading (B/L)",
     "Import Coordinator", "Import Documentation Specialist"),
    ("VS-11-trade-project-wholesale/PA-11.3-wholesale-operations.md",
     "SO Entry",
     "Sales Rep", "B2B Support Representative"),
    ("VS-07-store-operations/PA-07.3-store-receiving-and-replenishment.md",
     "End-of-replenishment cycle confirmation",
     "Stock Associate", "Replenishment & Allocation Analyst"),
    ("VS-33-strategic-planning/PA-33.2-corporate-performance-management.md",
     "CFO / C-Suite",
     "CFO / C-Suite", "CPM (Corporate Performance Management) Analyst"),
]


def main():
    by_file = {}
    for rel, anchor, oldr, role in ELEVATIONS:
        by_file.setdefault(rel, []).append((anchor, oldr, role))
    for rel, items in sorted(by_file.items()):
        path = os.path.join(WF, rel)
        lines = open(path, encoding="utf-8").read().splitlines(keepends=True)
        changed = 0
        for anchor, oldr, role in items:
            hits = [i for i, ln in enumerate(lines) if anchor in ln and ln.startswith("| ")]
            assert len(hits) == 1, f"{rel}: step anchor {anchor[:50]!r} matched {len(hits)}"
            i = hits[0]
            cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            if role in cells[2]:
                continue
            assert cells[2] == oldr, f"{rel}: step {anchor[:40]!r} R cell is {cells[2]!r}, expected {oldr!r}"
            cells[2] = f"{cells[2]}, {role}"
            lines[i] = "| " + " | ".join(cells) + " |\n"
            changed += 1
        if changed:
            open(path, "w", encoding="utf-8").write("".join(lines))
        print(f"  {rel}: {changed} step Role (R) cell(s) elevated")
    print("done — regenerate matrix/bpmn/gap/verification artifacts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
