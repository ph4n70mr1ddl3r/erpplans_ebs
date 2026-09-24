#!/usr/bin/env python3
"""Step-level anchoring wave 5 — batch 46 (2026-09-23, by direction).

Fifth elevation wave for the weak-anchor watchlist's NO PARSED CADENCE roles
(the batch-39/41 co-performer pattern — Role (R) cells gain the chartered
co-performer; no durations, frequencies, step texts or ownership cells
changed):

  Senior FP&A Analyst               → capex validation / ROI check (PA-17.4)
  Quality & Workforce Analyst       → Tier-2 resolution QA (PA-13.1)
  Sourcing & Screening Coordinator  → pre-hire background checks (PA-121.2)
  Legal Counsel — Contracts         → contract negotiation (W230, PA-17.1)
  Privacy Officer                   → consent & privacy governance (PA-91.1)
  Promotions Specialist             → markdown monitoring (PA-64.2)
  Promotions & Vendor-Funding       → markdown approval (PA-64.2)
    Coordinator

Idempotent; every edit asserts its anchor. Regenerate the matrix, bpmn/ and
the verification artifact afterwards.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
WF = os.path.join(REPO, "01-model-company", "workflows")

ELEVATIONS = [
    ("VS-17-record-to-report/PA-17.4-fpanda-and-reporting.md",
     "checks ROI calculation",
     "Capex Analyst", "Senior FP&A Analyst"),
    ("VS-13-customer-experience/PA-13.1-customer-support-and-complaints.md",
     "investigates root cause; coordinates with relevant department",
     "CS Manager / Store Manager", "Quality & Workforce Analyst"),
    ("VS-121-talent-acquisition-employer-brand-candidate-experience/PA-121.2-candidate-experience-sourcing-and-selection-operations.md",
     "run compliant pre-hire checks where role-appropriate",
     "Recruiting / Compliance, TA Coordinator", "Sourcing & Screening Coordinator"),
    ("VS-17-record-to-report/PA-17.1-gl-and-financial-close.md",
     "Legal reviews for risks, compliance, and alignment with company standards",
     "Legal Counsel, Contracts & Commercial Manager (Senior Counsel)", "Legal Counsel — Contracts"),
    ("VS-91-consumer-data-privacy-protection/PA-91.1-privacy-governance-consent-data-subject-rights.md",
     "Marketing Tech / Loyalty",
     "Marketing Tech / Loyalty", "Privacy Officer"),
    ("VS-64-seasonal-merchandise-clearance/PA-64.2-markdown-clearance-execution.md",
     "recommends markdown level based on residual inventory",
     "System / Pricing Analyst", "Promotions Specialist"),
    ("VS-64-seasonal-merchandise-clearance/PA-64.2-markdown-clearance-execution.md",
     "approves markdown; system updates price",
     "Category Manager / IT", "Promotions & Vendor-Funding Coordinator"),
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
            hits = [i for i, ln in enumerate(lines)
                    if ln.startswith("| ") and re.search(anchor, ln)
                    and not ln.split("|")[1].strip().startswith("**")
                    and len(ln.strip().strip("|").split("|")) >= 5]
            assert len(hits) == 1, f"{rel}: anchor {anchor[:45]!r} matched {len(hits)}"
            i = hits[0]
            cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            if role in cells[2]:
                continue
            assert cells[2] == oldr, f"{rel}: R cell is {cells[2]!r}, expected {oldr!r}"
            cells[2] = f"{cells[2]}, {role}"
            lines[i] = "| " + " | ".join(cells) + " |\n"
            changed += 1
        if changed:
            open(path, "w", encoding="utf-8").write("".join(lines))
        print(f"  {rel}: {changed} step Role (R) cell(s) elevated")
    print("done — regenerate matrix/bpmn/verification artifacts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
