#!/usr/bin/env python3
"""Timekeeping & Attendance Analyst re-anchor — batch 42 (2026-09-23, by direction).

Fixes the wave-1 elevation artifact the demand verification surfaced: the
batch-39 elevation placed the HQ Timekeeping & Attendance Analyst seat on a
STORE-SCALED weekly step (PA-19.3 W-trend, ×200 stores in the cadence ladder),
producing a bogus 182,500 h/yr / 10,139% OVERLOAD reading. The honest anchor
for this HQ data-quality seat is the W5532 platform-estate workflow itself:

  - REVERT: the store-scaled trend step returns to 'HR Supervisor' alone.
  - ELEVATE: 'HR Technology Manager / Payroll Specialist' R cell on the W5532
    downstream-integration-quality step gains the Timekeeping & Attendance
    Analyst (mandate: biometric/RFID feed integrity, shift/overtime data
    quality) as co-performer.

Idempotent; asserts both cells. Regenerate the matrix, bpmn/ and the
verification artefact afterwards.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PA193 = os.path.join(HERE, "..", "01-model-company", "workflows",
                     "VS-19-hire-to-retire", "PA-19.3-workforce-management.md")

REVERT_ANCHOR = "Weekly exception trend analysis: HR Supervisor generates exception trend report"
REVERT_OLD = "HR Supervisor, Timekeeping & Attendance Analyst"
REVERT_NEW = "HR Supervisor"

ELEV_ANCHOR = "Downstream integration quality"
ELEV_OLD = "HR Technology Manager / Payroll Specialist"
ELEV_ROLE = "Timekeeping & Attendance Analyst"


def main():
    lines = open(PA193, encoding="utf-8").read().splitlines(keepends=True)
    r_hits = [i for i, ln in enumerate(lines) if REVERT_ANCHOR in ln]
    assert len(r_hits) == 1, f"revert anchor matched {len(r_hits)}"
    i = r_hits[0]
    if REVERT_OLD in lines[i]:
        lines[i] = lines[i].replace(", " + ELEV_ROLE, "")
        print("reverted store-scaled elevation")
    e_hits = [i for i, ln in enumerate(lines) if ELEV_ANCHOR in ln]
    assert len(e_hits) == 1, f"elevate anchor matched {len(e_hits)}"
    j = e_hits[0]
    cells = [c.strip() for c in lines[j].strip().strip("|").split("|")]
    if ELEV_ROLE not in cells[2]:
        cells[2] = f"{cells[2]}, {ELEV_ROLE}"
        lines[j] = "| " + " | ".join(cells) + " |\n"
        print("elevated into W5532 downstream-integration-quality step")
    else:
        print("already elevated on W5532 step")
    open(PA193, "w", encoding="utf-8").write("".join(lines))
    print("done — regenerate matrix/bpmn/verification artefacts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
