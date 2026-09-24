#!/usr/bin/env python3
"""Step-level anchoring wave 1 — batch 39 (2026-09-23, by direction).

The weak-anchor verification (weak-anchor-demand-verification.md) found 58
weak-anchor roles with NO PARSED CADENCE: their anchored work is
Participant-level, so the gemba demand model cannot attribute step time to
them. This wave elevates the first nine roles into the Role (R) cells of the
steps their §5.3 mandates say they co-perform — no durations, frequencies,
step texts or ownership cells changed; only the R-cell performer lists gain
the chartered co-performer (comma-separated, both titles resolve).

  Payroll Supervisor                      → W10 register review (PA-19.2 step 6)
  Payroll & Statutory Remittance Officer  → statutory file generation (step 11)
  Timekeeping & Attendance Analyst        → weekly exception trend analysis (PA-19.3)
  Senior Demand Planner                   → S&OP demand review (PA-02.1)
  Purchasing / PO Specialist              → blanket-PO creation (PA-03.2)
  Tax Compliance & eFPS Specialist        → CAS/POS permit inventory (PA-79.1)
  TA Coordinator                          → pre-hire checks / offer advance (PA-121.2)
  Ecommerce Support Specialist            → online order-issue resolution (PA-10.1)
  Retail Media Operations Specialist      → campaign briefing/ops (PA-48.2)

Idempotent; every edit asserts its anchor. Regenerate the matrix, bpmn/ and
both gap/verification artifacts afterwards.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
WF = os.path.join(REPO, "01-model-company", "workflows")

# (relpath, unique step-text substring, old-R-cell-exact, role-to-add)
ELEVATIONS = [
    ("VS-19-hire-to-retire/PA-19.2-payroll-and-compensation.md",
     "Payroll Manager reviews and approves payroll register",
     "Payroll Manager", "Payroll Supervisor"),
    ("VS-19-hire-to-retire/PA-19.2-payroll-and-compensation.md",
     "SSS PRN, PhilHealth contribution, Pag-IBIG contribution files for remittance",
     "Payroll Officer", "Payroll & Statutory Remittance Officer"),
    ("VS-19-hire-to-retire/PA-19.3-workforce-management.md",
     "Weekly exception trend analysis: HR Supervisor generates exception trend report",
     "HR Supervisor", "Timekeeping & Attendance Analyst"),
    ("VS-02-supply-planning/PA-02.1-demand-forecasting-and-sandop.md",
     "presents statistical forecast by category with accuracy metrics",
     "Demand Planner", "Senior Demand Planner"),
    ("VS-03-vendor-management/PA-03.2-purchase-order-cycle.md",
     "creates Blanket PO in system: vendor, SKU lines with contract price",
     "Buyer", "Purchasing / PO Specialist"),
    ("VS-79-tax-management-bir-reporting/PA-79.1-indirect-tax-vat-and-einvoicing.md",
     "maintains BIR Computerized Accounting System (CAS)/POS permit inventory",
     "Tax Manager / IT", "Tax Compliance & eFPS Specialist"),
    ("VS-121-talent-acquisition-employer-brand-candidate-experience/PA-121.2-candidate-experience-sourcing-and-selection-operations.md",
     "advance selected candidates to offer",
     "Recruiting / Compliance", "TA Coordinator"),
    ("VS-10-ecommerce-digital/PA-10.1-ecommerce-platform-operations.md",
     "customer reports wrong item",
     "CSR / DC Dispatch", "Ecommerce Support Specialist"),
    ("VS-48-retail-media-network/PA-48.2-vendor-advertising-campaign-execution.md",
     "conducts campaign briefing with vendor",
     "Retail Media & Marketplace Manager", "Retail Media Operations Specialist"),
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
