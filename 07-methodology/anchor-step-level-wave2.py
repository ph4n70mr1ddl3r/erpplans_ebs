#!/usr/bin/env python3
"""Step-level anchoring wave 2 — batch 41 (2026-09-23, by direction).

Second elevation wave for the weak-anchor watchlist's NO PARSED CADENCE roles
(same co-performer pattern as batch 39 — Role (R) cells gain the chartered
co-performer; no durations, frequencies, step texts or ownership cells
changed):

  Technical Accounting Manager        → W5528 standards radar (PA-17.4)
  Accounting Policy Analyst           → W5528 policy manual maintenance (PA-17.4)
  Contracts & Commercial Manager      → W230 legal risk review (PA-17.1)
    (Senior Counsel)
  Audit Manager                       → audit execution (PA-21.1)
  Operations Compliance Lead          → store-audit cadence (PA-177.2)
  Field Compliance Auditor            → store-audit cadence (PA-177.2)
  Forensic / Fraud Investigator       → speak-up case investigation (PA-119.2)
  Compensation Analyst                → survey analysis / market position
                                        (PA-102.1)
  Strategy Analyst                    → quarterly competitive intelligence
                                        (PA-33.3)
  Field Communications Manager        → HQ-to-store announcement drafting
                                        (PA-63.1)

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
    ("VS-17-record-to-report/PA-17.4-fpanda-and-reporting.md",
     "Standards radar & adoption assessment",
     "Chief Accountant", "Technical Accounting Manager"),
    ("VS-17-record-to-report/PA-17.4-fpanda-and-reporting.md",
     "Policy manual maintenance",
     "Chief Accountant / Accounting Manager", "Accounting Policy Analyst"),
    ("VS-17-record-to-report/PA-17.1-gl-and-financial-close.md",
     "Legal reviews for risks, compliance, and alignment with company standards",
     "Legal Counsel", "Contracts & Commercial Manager (Senior Counsel)"),
    ("VS-21-internal-audit-risk/PA-21.1-audit-planning-and-execution.md",
     "Fieldwork: Test controls for POS (W5), Inventory (W4), Petty Cash (W25), LP (W37)",
     "Audit Team", "Audit Manager, Field Compliance Auditor"),
    ("VS-177-field-retail-operations-regional-district-management-and-multi-store-execution/PA-177.2-store-visit-field-coaching-and-retail-standards-execution.md",
     "share the cadence with Store Managers",
     "Regional/District Manager / Store Ops", "Operations Compliance Lead, Field Compliance Auditor"),
    ("VS-119-whistleblower-ethics-and-corporate-integrity-speak-up-program/PA-119.2-investigation-case-management-and-retaliation-protection.md",
     "Lead Investigator / Ethics & Compliance Officer / Legal",
     "Lead Investigator / Ethics & Compliance Officer / Legal",
     "Forensic / Fraud Investigator"),
    ("VS-102-compensation-benefits-total-rewards/PA-102.1-job-architecture-pay-structure-and-market-benchmarking.md",
     "analyze survey cuts (base, TCC, short-term incentive, benefits)",
     "C&B Manager", "Compensation Analyst"),
    ("VS-33-strategic-planning/PA-33.3-competitive-intelligence.md",
     "consolidates visit data into quarterly competitive intelligence report",
     "FP&A", "Strategy Analyst"),
    ("VS-63-store-communication-task-management/PA-63.1-hq-store-communication.md",
     "drafts announcement in store communication platform",
     "VP Corp Comms", "Field Communications Manager"),
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
