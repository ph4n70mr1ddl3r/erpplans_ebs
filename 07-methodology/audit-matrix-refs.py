#!/usr/bin/env python3
"""
audit-matrix-refs.py — matrix ghost-only rows, matrix R-section headings,
gap-analysis current-state declarations, and technical-guidelines anchor guard.

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

Thirty-seventh wave (2026-09-15): the matrix's own section-numbering layer
joins the guard after the BCP section was found carrying '## R25.' against
the canonical register's R26 (the same number as the matrix's own Loss-
Prevention section, and against the matrix's own Coverage-Validation claim
of '32 sections (R1–R32)') — a duplicate/wrong-subject heading no rule read.
And the gap-analysis totals check is promoted from a frozen literal (which,
by the sixth-wave OM-Total precedent, had come to satisfy itself off a
retired batch-6 note quoting 5,370 — the anchor survived verbatim in history
while the live declaration moved on) to a structural re-derivation.

Guard mode (--guard, validator Check 61):
  1. no requirement-matrix row may map only to ghost (non-header) W tokens;
  2. every matrix '## R<N>.' heading must resolve to the canonical
     erp-requirements.md section scheme: the number exists, no two matrix
     sections claim the same number, and the title shares a significant
     token with the canonical title (compression allowed, wrong-subject not);
  3. every matrix section numbered R25+ (the canonical tail sections) must
     mirror the canonical section's requirement population exactly (both
     directions); range headings (R19–R24) must hold only rows that
     canonically sit inside the range;
  4. every 'Canonical totals are now **N VS · M PA · K WF**' declaration in
     workflow-gap-analysis.md must carry the canonical 188/569, and the
     maximum K across the declarations (totals are add-only across batches,
     so the max is the live declaration) must equal the value-stream-index
     Grand Total;
  5. technical-guidelines must carry its verified anchor figures.
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MC = os.path.join(REPO, "01-model-company")

TG_ANCHORS = ["~511 HQ staff (≈460 concurrent users)", "~640 Mbps aggregate",
              "≥ 8 hours", "933 peak-day transactions per store",
              "10 years"]
# Canonical VS/PA figures carried by every gap-analysis per-batch declaration.
GA_CANON_VS = "188"
GA_CANON_PA = "569"
GA_DECLARATION_RE = re.compile(
    r"Canonical totals are now \*\*(\d+) value streams\s*·\s*(\d+) process areas\s*·\s*([\d,]+) workflows\*\*")

STOPWORDS = {"the", "and", "for", "of", "in", "a", "an", "to"}


def _tokens(title):
    t = title.replace("&", " ").replace("(", " ").replace(")", "").lower()
    return {w for w in re.split(r"[^a-z0-9]+", t) if len(w) >= 3 and w not in STOPWORDS}


def _canonical_sections():
    """erp-requirements.md: section number -> title, and requirement id -> section number."""
    titles, row_section = {}, {}
    cur = None
    for line in open(os.path.join(MC, "erp-requirements.md"), encoding="utf-8"):
        m = re.match(r"^## R(\d+)\.\s+(.+?)\s*$", line)
        if m:
            cur = int(m.group(1))
            titles[cur] = m.group(2)
            continue
        m = re.match(r"^\|\s*([A-Z]{2,}-\d+[a-z]?)\s*\|", line)
        if m and cur is not None:
            row_section[m.group(1)] = cur
    return titles, row_section


def _matrix_sections():
    """requirement-workflow-matrix.md: the numbered/range R-sections and their
    requirement-row populations. Unnumbered 'Additional …' sections make no
    numbered claim and are skipped."""
    head = re.compile(r"^## R(\d+)(?:–R?(\d+))?\.?\s+(.+?)\s*$")
    row = re.compile(r"^\|\s*([A-Z]{2,}-\d+[a-z]?)\s*\|")
    sections, cur = [], None
    for line in open(os.path.join(MC, "requirement-workflow-matrix.md"), encoding="utf-8"):
        m = head.match(line)
        if m:
            cur = {"start": int(m.group(1)),
                   "end": int(m.group(2)) if m.group(2) else None,
                   "title": m.group(3), "rows": set()}
            sections.append(cur)
            continue
        if line.startswith("## "):
            cur = None
            continue
        if cur is not None:
            m = row.match(line)
            if m:
                cur["rows"].add(m.group(1))
    return sections


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

    # --- thirty-seventh wave: the matrix's R-section numbering vs the canonical
    # register (the duplicate-R25/wrong-subject class)
    canon_titles, canon_rows = _canonical_sections()
    seen = {}
    for sec in _matrix_sections():
        s, e, title = sec["start"], sec["end"], sec["title"]
        nums = [s] if e is None else list(range(s, e + 1))
        for n in nums:
            if n in seen:
                hits.append(("matrix-r-heading", "requirement-workflow-matrix.md", 0,
                             f"R{n} claimed twice: '{seen[n]}' and '{title}' — "
                             f"duplicate section number against the canonical R1–R32 scheme"))
            seen[n] = title
        if e is not None:
            for rid in sec["rows"]:
                cs = canon_rows.get(rid)
                if cs is None or not (s <= cs <= e):
                    hits.append(("matrix-tail-population", "requirement-workflow-matrix.md", 0,
                                 f"{rid} under range heading R{s}–R{e} '{title}' but "
                                 f"canonically in R{cs} "
                                 f"({canon_titles.get(cs, 'unknown') if cs else 'not in register'})"))
            continue
        if s not in canon_titles:
            hits.append(("matrix-r-heading", "requirement-workflow-matrix.md", 0,
                         f"R{s} '{title}' has no canonical erp-requirements.md section"))
        elif not (_tokens(title) & _tokens(canon_titles[s])):
            hits.append(("matrix-r-heading", "requirement-workflow-matrix.md", 0,
                         f"R{s} '{title}' shares no significant token with the canonical "
                         f"R{s} '{canon_titles[s]}' — wrong-subject heading"))
        if s >= 25:
            canon_pop = {rid for rid, cs in canon_rows.items() if cs == s}
            missing = sorted(canon_pop - sec["rows"])
            extra = sorted(sec["rows"] - canon_pop)
            if missing or extra:
                hits.append(("matrix-tail-population", "requirement-workflow-matrix.md", 0,
                             f"R{s} '{title}' must mirror canonical R{s} exactly — "
                             f"missing {missing}, extra {extra}"))

    # --- thirty-seventh wave: the gap-analysis current-state declarations,
    # re-derived structurally (the frozen 5,370 literal had come to satisfy
    # itself off a retired batch-6 note — the sixth-wave OM-Total precedent)
    ga = open(os.path.join(MC, "workflows", "workflow-gap-analysis.md"),
              encoding="utf-8").read()
    ga_joined = re.sub(r"[>\n\r]+", " ", ga)
    decls = GA_DECLARATION_RE.findall(ga_joined)
    if not decls:
        hits.append(("gap-analysis-declaration", "workflow-gap-analysis.md", 0,
                     "no 'Canonical totals are now **N VS · M PA · K WF**' declarations found"))
    else:
        bad = [(vs, pa, wf) for vs, pa, wf in decls
               if vs != GA_CANON_VS or pa != GA_CANON_PA]
        if bad:
            hits.append(("gap-analysis-declaration", "workflow-gap-analysis.md", 0,
                         f"declaration(s) {bad} carry non-canonical VS/PA figures "
                         f"(canonical {GA_CANON_VS}/{GA_CANON_PA})"))
        index = open(os.path.join(MC, "workflows", "value-stream-index.md"),
                     encoding="utf-8").read()
        m = re.search(r"\*\*Grand Total\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*([\d,]+)\*\*", index)
        if not m:
            hits.append(("gap-analysis-declaration", "workflow-gap-analysis.md", 0,
                         "value-stream-index.md Grand Total row not found for the re-derivation"))
        else:
            total = int(m.group(2).replace(",", ""))
            max_wf = max(int(wf.replace(",", "")) for _, _, wf in decls)
            if max_wf != total:
                hits.append(("gap-analysis-declaration", "workflow-gap-analysis.md", 0,
                             f"the newest declaration's workflow total {max_wf} != the index "
                             f"Grand Total {total} — a batch stranded its declaration"))

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
