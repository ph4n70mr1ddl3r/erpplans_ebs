#!/usr/bin/env python3
"""Owner-grain promotion sweep III (Class-B folds) — batch 36 (2026-09-23, by direction).

Third remediation wave off the workflow→role coverage gap analysis. Four
further department-grain owner forms promoted to the chartered seats they
denote (same mechanics as batches 33-35 — DEPT_ACTORS department-grain entries
move to ROLE_ALIASES title-level targets):

  1. Dark Store Operations Manager (13 owner cells, VS-93) → DC Operations
     Manager (chartered HQ Supply Chain seat) — dark stores are DC-model
     micro-fulfillment nodes (the batch-35 Shift Supervisors → DC roster
     adjudication, at the manager grain).
  2. Marketing Manager (15 owner cells, 4 VSs) → Marketing Operations Manager
     (chartered Marketing seat) — the department's operations seat owns the
     campaign-operations workflows.
  3. Accounting Manager (12 owner cells, 6 VSs) → Manager, GL & Consolidation
     (Assistant Controller) — the batch-33 costing adjudication's cluster
     manager, same fold.
  4. IT Infrastructure Manager (13 owner cells, 3 VSs) → IT Operations
     (FS/INFRA) — the chartered IT product-model seat for infrastructure
     operations (IT_SEATS target, the §5.3-by-reference IT row).

Adjudicated NOT this batch (remaining backlog): Ecommerce Operations Manager
(22) and Digital Product Manager (12) — the wave-36 adjudication deliberately
assigned the ecommerce-operations grain to the 'Digital Commerce (IT-built
platforms)' department label and a sizing decision is needed to charter the
seat; Customer Service Manager (13) — ambiguous between Head of Customer
Service and Services Manager; Finance Analyst (22), HR Manager (19), Internal
Audit (17), Trade Sales Manager (13) — genuinely department-wide or
disabled-estate grain.

Idempotent; every edit asserts its anchor. Regenerate the matrix and the gap
analysis report afterwards and re-pin the Check-71 census.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, "generate-role-coverage.py")

PROMOTIONS = {
    "dark store operations manager": "DC Operations Manager",
    "marketing manager": "Marketing Operations Manager",
    "accounting manager": "Manager, GL & Consolidation (Assistant Controller)",
    "it infrastructure manager": "IT Operations (FS/INFRA)",
}

ANCHOR = '"data protection officer": "Data Privacy Officer (DPO)",'


def apply_generator():
    src = open(GEN, encoding="utf-8").read()
    if '"dark store operations manager": "DC Operations Manager"' in src:
        print("generator: batch-36 promotion block already present")
        return
    for k in PROMOTIONS:
        pat = re.compile(r' ?"%s": "[^"]*",?' % re.escape(k))
        src, n = pat.subn("", src, count=1)
        assert n == 1, f"DEPT_ACTORS entry for {k!r} not found"
    block_lines = [
        '    # --- Owner-grain promotion sweep III (batch 36, 2026-09-23): four',
        '    # further recurring Owner forms the gap analysis caught at department',
        '    # grain promoted to the chartered titles they denote (see',
        '    # fix-owner-grain-promotions-4.py and the workflow-to-role gap analysis).',
        '    "dark store operations manager": "DC Operations Manager",',
        '    "marketing manager": "Marketing Operations Manager",',
        '    "accounting manager": "Manager, GL & Consolidation (Assistant Controller)",',
        '    "it infrastructure manager": "IT Operations (FS/INFRA)",',
    ]
    idx = src.index(ANCHOR) + len(ANCHOR)
    src = src[:idx] + "\n" + "\n".join(block_lines) + src[idx:]
    open(GEN, "w", encoding="utf-8").write(src)
    print(f"generator: {len(PROMOTIONS)} DEPT_ACTORS -> ROLE_ALIASES promotions")


def main():
    apply_generator()
    print("done — regenerate the matrix and gap report, re-pin the Check-71 census")
    return 0


if __name__ == "__main__":
    sys.exit(main())
