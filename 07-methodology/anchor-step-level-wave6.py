#!/usr/bin/env python3
"""Step-level anchoring wave 6 — batch 48 (2026-09-23, by direction).

DC-floor elevations for the weak-anchor watchlist (the batch-39 co-performer
pattern):

  Discrepancy Analysts → GR/IR discrepancy resolution (PA-04.1; mandate:
                         'GR/IR variances < 24h resolution')
  Cross-Dock Team      → cross-dock operations (PA-04.3)

Idempotent; regenerating the matrix, bpmn/ and the gap/verification artefacts
afterwards is required.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PA041 = os.path.join(HERE, "..", "01-model-company", "workflows", "VS-04-dc-warehouse",
                     "PA-04.1-dc-inbound-operations.md")
PA043 = os.path.join(HERE, "..", "01-model-company", "workflows", "VS-04-dc-warehouse",
                     "PA-04.3-dc-operations-management.md")

EDITS = [
    (PA041, "If discrepancy (shortage, damage, wrong item): flag in system; notify Buyer", "Receiving Clerk", "Discrepancy Analysts"),
    (PA043, "Labor allocation and task assignment", "DC Shift Supervisor", "Cross-Dock Team"),
]


def main():
    for path, anchor, oldr, role in EDITS:
        lines = open(path, encoding="utf-8").read().splitlines(keepends=True)
        hits = [i for i, ln in enumerate(lines)
                if anchor in ln and ln.startswith("| ") and ln.split("|")[3].strip() == oldr]
        assert len(hits) == 1, f"{os.path.basename(path)}: anchor {anchor!r} matched {len(hits)}"
        i = hits[0]
        if role in lines[i]:
            print(f"  {os.path.basename(path)}: already elevated")
            continue
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        cells[2] = f"{cells[2]}, {role}"
        lines[i] = "| " + " | ".join(cells) + " |\n"
        open(path, "w", encoding="utf-8").write("".join(lines))
        print(f"  {os.path.basename(path)}: {role} elevated on '{anchor[:40]}...' step")
    print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
