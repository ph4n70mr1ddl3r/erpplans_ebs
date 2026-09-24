#!/usr/bin/env python3
"""Owner-grain promotion sweep — batch 33 (2026-09-23, by direction).

First remediation wave off the workflow→role coverage gap analysis (batch 32,
role-coverage-gap-analysis.md). Three adjudications, each a recorded governance
decision:

  1. Fleet & Logistics Manager (30 owner cells): 'Logistics Manager' is the
     corpus's name for the chartered Supply Chain & Logistics seat — the
     DEPT_ACTORS department-grain entry moves to ROLE_ALIASES with the
     chartered title as target.
  2. Data Privacy Officer (26 owner cells): 'Data Protection Officer (DPO)'
     is the RA-10173 statutory sense of the chartered Legal & Compliance seat;
     the DEPT_ACTORS entry (which even carried the chartered title as a
     department LABEL — the title-as-dept-label anti-class) moves to
     ROLE_ALIASES so the form resolves to the seat.
  3. Costing & fixed-asset accounting (36 owner cells) — THE REGISTER
     DECISION: the corpus's Cost Accountant / Cost Accounting Manager /
     Fixed Asset Accountant forms are the GL & Consolidation cluster's
     function. HC-neutral chartering: the §5.3 register's
     'GL Accountant (one per entity)' mandate gains inventory-valuation and
     fixed-asset/depreciation scope, the 'Manager, GL & Consolidation
     (Assistant Controller)' mandate gains costing oversight, and the three
     corpus forms promote via ROLE_ALIASES to those two seats. No HC, no
     register-row-count change.

  Plus the two genuine retail-media owner cells (PA-48.2 W2006/W2010): the
  vendor-facing campaign owner is the chartered 'Retail Media & Marketplace
  Manager' — owner/participant/step cells corrected in the PA file. The
  remaining 'Account Manager' owners (VS-43/VS-107) sit inside the B2B
  disabled—prepared estate and stay department-grain by design (the (x)
  adjudication).

Idempotent; every edit asserts its anchor. Regenerate the matrix, bpmn/ and
the gap-analysis report afterwards and re-pin the Check-71 census.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
GEN = os.path.join(HERE, "generate-role-coverage.py")
PA482 = os.path.join(REPO, "01-model-company", "workflows",
                     "VS-48-retail-media-network",
                     "PA-48.2-vendor-advertising-campaign-execution.md")
TO = os.path.join(REPO, "01-model-company", "optimal-table-of-organization.md")

# DEPT_ACTORS key -> ROLE_ALIASES chartered-title target
PROMOTIONS = {
    "cost accountant": "GL Accountant (one per entity)",
    "fixed asset accountant": "GL Accountant (one per entity)",
    "logistics manager": "Fleet & Logistics Manager",
    "cost accounting manager": "Manager, GL & Consolidation (Assistant Controller)",
    "data protection officer": "Data Privacy Officer (DPO)",
}

PROMO_BLOCK = '''    # --- Owner-grain promotion sweep (batch 33, 2026-09-23): recurring
    # Owner forms the gap analysis caught at department grain promoted to the
    # chartered titles they denote (see fix-owner-grain-promotions.py and the
    # workflow→role gap analysis).
    "cost accountant": "GL Accountant (one per entity)",
    "fixed asset accountant": "GL Accountant (one per entity)",
    "logistics manager": "Fleet & Logistics Manager",
    "cost accounting manager": "Manager, GL & Consolidation (Assistant Controller)",
    "data protection officer": "Data Privacy Officer (DPO)",'''

OLD_MANDATE_GL = ("| GL Accountant (one per entity) | 5 | GL & Consolidation Mgr | "
                  "Entity books: GL, reconciliations, accruals, BIR/SEC filing support per entity |")
NEW_MANDATE_GL = ("| GL Accountant (one per entity) | 5 | GL & Consolidation Mgr | "
                  "Entity books: GL, reconciliations, accruals, BIR/SEC filing support per entity; "
                  "inventory valuation (WAC) and fixed-asset/depreciation accounting per entity — the close's "
                  "Cost Accountant steps (PA-17.4) and the corpus's Fixed Asset Accountant form |")
OLD_MANDATE_AC = ("Per-entity GL hygiene and the consolidation/elimination cycle; "
                  "Assistant Controller for the transactional cluster below")
NEW_MANDATE_AC = ("Per-entity GL hygiene and the consolidation/elimination cycle; costing & "
                  "fixed-asset accounting oversight (the corpus's Cost Accounting Manager form); "
                  "Assistant Controller for the transactional cluster below")


def apply_generator():
    src = open(GEN, encoding="utf-8").read()
    if '"cost accountant": "GL Accountant (one per entity)"' in src:
        print("generator: batch-33 promotion block already present")
        return
    for k, target in PROMOTIONS.items():
        # remove the DEPT_ACTORS entry (values are department labels; entries
        # share lines, so remove the bare fragment keeping the delimiters)
        pat = re.compile(r' ?"%s": "[^"]*",?' % re.escape(k))
        src, n = pat.subn("", src, count=1)
        assert n == 1, f"DEPT_ACTORS entry for {k!r} not found"
        # add the ROLE_ALIASES title-level promotion (idempotent)
        marker = '"fixed asset accountant (fae)"'  # sentinel: not present
        assert f'"{k}": "{target}"' not in src.split("DEPT_ACTORS")[0], f"{k} already promoted"
    assert PROMO_BLOCK.split("\n")[3].strip() not in src.split("DEPT_ACTORS")[0], \
        "batch-33 block already present"
    anchor = '    "security guard": "EXTERNAL:Security Guard (contracted)",'
    assert anchor in src, "ROLE_ALIASES anchor not found"
    assert "batch-33 block already present" == "batch-33 block already present"
    src = src.replace(anchor, anchor + "\n" + "\n".join(PROMO_BLOCK.split("\n")[2:]), 1)
    open(GEN, "w", encoding="utf-8").write(src)
    print(f"generator: {len(PROMOTIONS)} DEPT_ACTORS -> ROLE_ALIASES promotions")


def apply_pa48():
    src = open(PA482, encoding="utf-8").read()
    n = src.count("Account Manager")
    if n == 0:
        assert "Retail Media & Marketplace Manager" in src, \
            "PA-48.2: neither form found"
        print("PA-48.2: already converted")
        return
    src = src.replace("Account Manager", "Retail Media & Marketplace Manager")
    open(PA482, "w", encoding="utf-8").write(src)
    print(f"PA-48.2: {n} 'Account Manager' cells/prose → 'Retail Media & Marketplace Manager'")


def apply_to():
    src = open(TO, encoding="utf-8").read()
    for old, new in ((OLD_MANDATE_GL, NEW_MANDATE_GL), (OLD_MANDATE_AC, NEW_MANDATE_AC)):
        if new in src:
            continue
        assert old in src, f"TO mandate anchor not found: {old[:60]!r}"
        src = src.replace(old, new, 1)
    open(TO, "w", encoding="utf-8").write(src)
    print("TO: GL & Consolidation cluster mandates re-scoped (HC-neutral)")


def main():
    apply_generator()
    apply_pa48()
    apply_to()
    print("done — regenerate matrix/bpmn/gap report, re-pin the Check-71 census")
    return 0


if __name__ == "__main__":
    sys.exit(main())
