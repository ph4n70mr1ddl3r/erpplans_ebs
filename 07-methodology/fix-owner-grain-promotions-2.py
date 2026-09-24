#!/usr/bin/env python3
"""Owner-grain promotion sweep II — batch 34 (2026-09-23, by direction).

Second remediation wave off the workflow→role coverage gap analysis. Three
further department-grain owner forms promoted to the chartered seats they
denote (same mechanics as batch 33 — DEPT_ACTORS department-grain entries move
to ROLE_ALIASES title-level targets):

  1. FP&A (25 owner cells, 10 VSs) → FP&A Manager — the department's chartered
     manager owns its workflows (the 'fp&a director' → FP&A Manager precedent).
  2. Compliance Officer (22 owner cells, 7 VSs) → Compliance Manager / MLRO —
     the chartered compliance seat; the ABC/regulatory programs it already owns
     (PA-21.1) are this seat's mandate.
  3. Market Research Analyst (16 owner cells, 1 VS) → Insights Analyst — the
     chartered insights seat (HC 2); market research is the insights function's
     research arm (VS-44).

Adjudicated NOT this batch (remaining backlog, needs sub-function judgment or a
sizing decision): Finance Analyst (22, genuinely cross-department), HR Manager
(19), Internal Audit (17 — bare department name, department-wide work),
Ecommerce Operations Manager (22) / Dark Store Operations Manager (13) /
Digital Product Manager (12) (register-coverage candidates needing a sizing
decision), Marketing Manager (15) / Customer Service Manager (13) / Accounting
Manager (12) / IT Infrastructure Manager (13) / Trade Sales Manager (13),
Account Manager (12 — VS-43/107 estate by design).

Idempotent; every edit asserts its anchor. Regenerate the matrix and the gap
analysis report afterwards and re-pin the Check-71 census.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, "generate-role-coverage.py")

PROMOTIONS = {
    "fp&a": "FP&A Manager",
    "compliance officer": "Compliance Manager / MLRO",
    "market research analyst": "Insights Analyst",
}

PROMO_BLOCK = '''    # --- Owner-grain promotion sweep II (batch 34, 2026-09-23): further
    # recurring Owner forms the gap analysis caught at department grain
    # promoted to the chartered titles they denote (see
    # fix-owner-grain-promotions-2.py and the workflow→role gap analysis).
    "fp&a": "FP&A Manager",
    "compliance officer": "Compliance Manager / MLRO",
    "market research analyst": "Insights Analyst",'''

ANCHOR = '"data protection officer": "Data Privacy Officer (DPO)",'


def apply_generator():
    src = open(GEN, encoding="utf-8").read()
    if '"market research analyst": "Insights Analyst"' in src:
        print("generator: batch-34 promotion block already present")
        return
    for k in PROMOTIONS:
        pat = re.compile(r' ?"%s": "[^"]*",?' % re.escape(k))
        src, n = pat.subn("", src, count=1)
        assert n == 1, f"DEPT_ACTORS entry for {k!r} not found"
    idx = src.index(ANCHOR) + len(ANCHOR)
    src = src[:idx] + "\n" + "\n".join(PROMO_BLOCK.split("\n")[2:]) + src[idx:]
    open(GEN, "w", encoding="utf-8").write(src)
    print(f"generator: {len(PROMOTIONS)} DEPT_ACTORS -> ROLE_ALIASES promotions")


def main():
    apply_generator()
    print("done — regenerate the matrix and gap report, re-pin the Check-71 census")
    return 0


if __name__ == "__main__":
    sys.exit(main())
