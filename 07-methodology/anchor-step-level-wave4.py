#!/usr/bin/env python3
"""Step-level anchoring wave 4 — batch 45 (2026-09-23, by direction).

Fourth elevation wave for the weak-anchor watchlist's NO PARSED CADENCE roles
(the batch-39/41 co-performer pattern — Role (R) cells gain the chartered
co-performer; no durations, frequencies, step texts or ownership cells
changed):

  Real-Estate & Site-Selection Analyst  → market screening + candidate-site
                                          identification (PA-20.1 ×2)
  Maintenance & Projects Coordinator    → PM schedule build (PA-138.1)
  Sourcing & Screening Coordinator      → consistent screening (PA-121.2)
  3PL & Freight Specialist              → freight-spend baseline & category
                                          strategy (PA-110.1)
  IAP Integration Engineer +            → integration platform step (PA-27.2)
  IAP Integration Support Engineer
  Senior LP Analytics Analyst           → exception rule engine (PA-23.1)
  Marketing Comms Specialist            → official statement / FAQ messaging
                                          (PA-14.3)
  ESG Reporting & Data Analyst          → ESG data validation (PA-25.3)
  Wellness Coordinator                  → EAP utilization review (PA-83.3)

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
    ("VS-20-real-estate-construction/PA-20.1-site-selection-and-lease-management.md",
     "Market opportunity screening",
     "Real Estate Manager", "Real-Estate & Site-Selection Analyst"),
    ("VS-20-real-estate-construction/PA-20.1-site-selection-and-lease-management.md",
     "Candidate site identification and traffic analysis",
     "Real Estate Manager / External Broker", "Real-Estate & Site-Selection Analyst"),
    ("VS-138-integrated-facilities-management-workplace-services-and-building-automation/PA-138.1-facilities-management-strategy-ifm-provider-and-sla-governance.md",
     "preventive-maintenance (PM) schedule per asset/system",
     "Facilities Maintenance Lead / Provider", "Maintenance & Projects Coordinator"),
    ("VS-121-talent-acquisition-employer-brand-candidate-experience/PA-121.2-candidate-experience-sourcing-and-selection-operations.md",
     "run consistent screening: application review",
     "Recruiting / Hiring Managers", "Sourcing & Screening Coordinator"),
    ("VS-110-freight-procurement-carrier-management-and-freight-audit/PA-110.1-freight-sourcing-carrier-contracting-and-rate-management.md",
     "freight-spend baseline and category strategy",
     "Logistics / Procurement / FP&A", "3PL & Freight Specialist"),
    ("VS-23-loss-prevention/PA-23.1-exception-monitoring-and-investigation.md",
     "exception rule engine execution",
     "LP Analyst", "Senior LP Analytics Analyst"),
    ("VS-14-marketing/PA-14.3-brand-pr-and-corporate-communications.md",
     "Develop official statement and FAQ for press/social media",
     "PR Manager", "Marketing Comms Specialist"),
    ("VS-25-esg-sustainability/PA-25.3-esg-reporting-and-compliance.md",
     "validates all submitted data",
     "Sustainability Lead", "ESG Reporting & Data Analyst"),
    ("VS-83-occupational-health-clinic-wellness/PA-83.3-mental-health-wellness-eap.md",
     "aggregate utilization and trend themes",
     "EAP Provider / EAP Manager", "Wellness Coordinator"),
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
                    if anchor in ln and ln.startswith("| ")
                    and not ln.split("|")[1].strip().startswith("**")
                    and len(ln.strip().strip("|").split("|")) >= 5]
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
