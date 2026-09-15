#!/usr/bin/env python3
"""
audit-matrix-refs.py — matrix ghost-only rows, gap-analysis current-state figures,
and technical-guidelines anchor guard.

Consistency review #43 (2026-08-29) audited the three surfaces:

  * requirement-workflow-matrix.md cell-by-cell — all 724 rows' W tokens
    resolve (Checks 4/6 green); the letter-suffixed aliases (W5B, W9A, W2A…
    ~1,400 prose mentions) are the sanctioned POS-family sub-workflow
    shorthand resolved via prose. The defect class repaired: **8 rows were
    mapped ONLY to ghost aliases** (POS-004/011/012/017/018, RPT-007,
    NFR-003, NFR-015 — e.g. FIN-054/055's W9A) leaving the requirement
    untraceable to any real workflow header; each re-pointed to the real
    workflows that exercise it (W5, W463, W520, W528, W1282/W1485, W1425,
    W9, W14).
  * workflow-gap-analysis.md summary figures — the current-state declaration
    quotes 188 VS / 569 PA / 5,364 workflows and the fourteen post-catalog
    workflows plus the W5511 event-custody addition; the smaller totals (5,349…5,363)
    and the 6,757 headcount live
    inside per-pass historical notes, exempt per the change-note convention.
  * technical-guidelines.md quantitative claims — verified against current
    state: offline capacity 933 peak-day (= 467 avg × 2.0), event latency
    < 30 sec, price push ≤ 60 sec, offline ≥ 8 hours, bandwidth table
    (200 × 2 Mbps + 4 × 10 + 200 HQ = 640 Mbps aggregate, ~511 HQ staff,
    ~80 RF guns/DC, 205 sites — re-based 2026-09-14 to the promoted
    HQ 511 / total 6,911 canon), RTO ≤ 4 hours, 10-year retention.

Guard mode (--guard, validator Check 61):
  1. no requirement-matrix row may map only to ghost (non-header) W tokens;
  2. the gap-analysis current-state line must quote the canonical totals;
  3. technical-guidelines must carry its verified anchor figures.
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MC = os.path.join(REPO, "01-model-company")

TG_ANCHORS = ["~511 HQ staff (≈460 concurrent users)", "~640 Mbps aggregate",
              "≥ 8 hours", "933 peak-day transactions per store",
              "10 years"]
GA_ANCHOR = "**188 value streams · 569 process areas · 5,370 workflows**"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true")
    args = ap.parse_args()
    hits = []
    headers = set()
    for f in glob.glob(os.path.join(MC, "workflows", "VS-*", "PA-*.md")):
        headers |= set(re.findall(r"^## (W\d+[A-Z]?)\.",
                                  open(f, encoding="utf-8").read(), re.M))
    matrix = open(os.path.join(MC, "requirement-workflow-matrix.md"),
                  encoding="utf-8").read()
    for line in matrix.splitlines():
        m = re.match(r"^\| ([A-Z]{2,4}-\d{3}) \|", line)
        if not m:
            continue
        ws = re.findall(r"\b(W\d+[A-Z]?)(?:\.\d+[a-z]?)?\b", line)
        real = [w for w in ws if w in headers]
        ghosts = sorted({w for w in ws
                         if w not in headers and re.fullmatch(r"W\d+[A-Z]", w)})
        if ghosts and not real:
            hits.append(("ghost-only-row", "requirement-workflow-matrix.md", 0,
                         f"{m.group(1)} maps only to ghost aliases {ghosts}"))
    ga = open(os.path.join(MC, "workflows", "workflow-gap-analysis.md"),
              encoding="utf-8").read()
    if GA_ANCHOR not in ga:
        hits.append(("gap-analysis-current-state", "workflow-gap-analysis.md", 0,
                     f"missing canonical totals line '{GA_ANCHOR}'"))
    tg = open(os.path.join(REPO, "07-methodology", "technical-guidelines.md"),
              encoding="utf-8").read()
    for a in TG_ANCHORS:
        if a not in tg:
            hits.append(("tg-anchor", "technical-guidelines.md", 0,
                         f"missing anchor '{a}'"))
    for kind, rel, line, detail in hits:
        print(f"{kind}: {rel}:{line}: {detail}")
    print(f"audit-matrix-refs: {len(hits)} hit(s)")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
