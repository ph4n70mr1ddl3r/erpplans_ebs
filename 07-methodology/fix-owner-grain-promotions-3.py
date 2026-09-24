#!/usr/bin/env python3
"""Class-A cluster promotion sweep — batch 35 (2026-09-23, by direction).

Third remediation wave off the workflow→role coverage gap analysis: the three
largest open Class-A (role-less) clusters promoted via ROLE_ALIASES so their
compound owner cells resolve to chartered seats:

  1. 'EEO' (the RA-11285 Energy Efficiency Officer, ~13 owner cells across
     VS-120's renewable-energy program) → the chartered Energy Manager
     (Facilities & Real Estate) — the EEO IS the site's energy manager under
     the DOE program.
  2. 'Event Marketing Manager' (~9 owner cells, VS-139 events) → Promotions &
     Campaigns Manager — whose chartered mandate already carries 'event P&L
     (6 events/yr)'.
  3. 'Trade Capability' (~9 owner cells, VS-123 apprenticeship) → Learning &
     Development Manager — the chartered L&D seat that runs the trade
     capability program.

  Plus two single-form alignments: 'Store HR Administrator' → Store HR
  Coordinator (one per district) (the v2.6 gap-fill's re-pointed seat) and
  'Dark Store Shift Supervisor' → DC:Shift Supervisors (dark stores are
  DC-model nodes; the DC roster's shift-supervisor complement covers them).

The analyzer (role-coverage-gap-analysis.py) now also annotates system-owned
Class-A workflows as 'Automated (system-owned)' — by design, not gaps.

Idempotent; regenerating the matrix and gap report afterwards is required.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, "generate-role-coverage.py")

PROMOTIONS = {
    "eeo": "Energy Manager",
    "event marketing manager": "Promotions & Campaigns Manager",
    "trade capability": "Learning & Development Manager",
    "store hr administrator": "Store HR Coordinator (one per district)",
    "dark store shift supervisor": "DC:Shift Supervisors",
}

PROMO_BLOCK = """
    # --- Owner-grain promotion sweep III (batch 35, 2026-09-23): the largest
    # open Class-A (role-less) clusters promoted to the chartered seats they
    # denote — EEO (the RA-11285 Energy Efficiency Officer, VS-120) -> Energy
    # Manager; Event Marketing Manager (VS-139) -> Promotions & Campaigns
    # Manager (whose mandate carries event P&L); Trade Capability (VS-123
    # apprenticeship) -> Learning & Development Manager; plus Store HR
    # Administrator -> Store HR Coordinator (one per district) and Dark Store
    # Shift Supervisor -> DC:Shift Supervisors (dark stores are DC-model nodes).
    "eeo": "Energy Manager",
    "event marketing manager": "Promotions & Campaigns Manager",
    "trade capability": "Learning & Development Manager",
    "store hr administrator": "Store HR Coordinator (one per district)",
    "dark store shift supervisor": "DC:Shift Supervisors",
"""


ANCHOR = '"market research analyst": "Insights Analyst",'


def apply_generator():
    src = open(GEN, encoding="utf-8").read()
    if '"market research analyst": "Insights Analyst",' in src and '"eeo": "Energy Manager"' in src:
        print("generator: batch-35 promotion block already present")
        return
    for k in PROMOTIONS:
        pat = re.compile(r' ?"%s": "[^"]*",?' % re.escape(k))
        src, n = pat.subn("", src, count=1)
        assert n == 1, f"competing entry for {k!r} not found (or absent — remove from PROMOTIONS if intentionally absent)"
    block = "\n".join(PROMO_BLOCK.split("\n")[2:])
    idx = src.index(ANCHOR) + len(ANCHOR)
    src = src[:idx] + "\n" + block + src[idx:]
    open(GEN, "w", encoding="utf-8").write(src)
    print(f"generator: {len(PROMOTIONS)} Class-A cluster promotions")


def main():
    apply_generator()
    print("done — regenerate the matrix and gap report, re-pin the Check-71 census")
    return 0


if __name__ == "__main__":
    sys.exit(main())
