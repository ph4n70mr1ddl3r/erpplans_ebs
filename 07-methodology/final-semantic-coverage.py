#!/usr/bin/env python3
"""
final-semantic-coverage.py — Final full-coverage semantic pass (review #71).

Closes the Check 62 sampling loop by extending coverage from the 2,241 stratified
full-read workflows to ALL 5,363. The remaining 3,122 workflows are covered by a
programmatic detector suite implementing the highest-yield defect classes of the
prior full-read batches (#44–#67), with every flagged spot then read and adjudicated
by hand (repairs applied; adjudicated-legitimate patterns on the documented allowlist
below). This is honestly labelled: detector coverage + targeted reads, not a claim of
30×104 stratified full reads.

Detectors (scoped to the unaudited W-blocks only — the audited 2,241 are excluded
because their classes were already swept; the mechanical Check 46–63 guards already
cover the corpus-wide literal/arithmetic classes and are green):

  D1  per-store-rate vs chain-total coherence — the review-#65 class: any block
      pairing a '~N–M per store per day|week|month' rate with a chain-wide
      '/month chain|chain-wide|across (all )?(200|205)' total must cohere once
      normalized to events/month/200 stores (factor-3 tolerance on midpoints,
      mirroring Check 55's ±scale convention widened for band padding).
      Known limitation: decimal-suffixed chain magnitudes ('2.8M …/month across')
      are invisible to the gap class (no '.' allowed between number and '/month')
      — currency/PHT figures are therefore out of D1's scope.
  D2  unseen statutory citations — every RA/PD/DO/DAO/RR/RMC/PNS/BP/CA citation in
      an unaudited block must appear somewhere in the already-audited corpus or on
      the KNOWN_GOOD canon list (the web-verified adjudications of reviews #29–#67);
      anything else is NEW and requires adjudication before the loop can close.
  D3  staffing-cadence contradiction — a Staffing/TE 'N hours/week' claim alongside
      an hours/month figure for the same block whose implied weekly equivalents
      differ by >4x (the review-#65 day-vs-month family, block-local form).
  D4  unit-suspect totals — a chain-wide '/day' total in a Volume/Frequency row for
      an activity whose per-store basis is per-week or per-month (cadence-class
      mismatch), flagged for read.

Usage:
    python3 07-methodology/final-semantic-coverage.py            # report (unaudited set)
    python3 07-methodology/final-semantic-coverage.py --all      # regression net: D1/D3/D4 over ALL workflows
    python3 07-methodology/final-semantic-coverage.py --quiet    # exit code only

Post-closure note: the registry is complete (5,432/5,432 since the 2026-09-23
 seventy-fourth-wave admission; the 62 workflows W5518–W5579 that shipped after the
 closure were admitted in one pass via this exact transition path — full read of
 every block + D1–D4 over the unaudited set (0 flags beyond D2) + the five D2
 citation hits adjudicated legitimate in context and added to KNOWN_GOOD
 (RA 10175/RA 7279/RA 10821), with four in-read defects repaired the same pass
 (W5529's W336 misdirected citation, W5578's W327 misdirected citation, the
 '~99,000 customers' population mislabel against the W330 people canon on three
 surfaces, W5522's doubled fit-gap clause), bringing the registry to 5,432/5,432), so the
 default run is vacuous (no unaudited blocks) — it exists for re-running the
 transition if workflows ever ship outside the registry again. The --all mode is
 the standing regression net (D2 is skipped there: with no unaudited set there is
 no baseline to diff against).
"""
import argparse
import collections
import os
import re
import sys

REPO = __file__.rsplit("/07-methodology/", 1)[0]
WF = f"{REPO}/01-model-company/workflows"
REGISTRY = f"{REPO}/07-methodology/semantic-audit-coverage.txt"

# ---------------------------------------------------------------- allowlist
# Adjudicated-legitimate hits (detector, workflow, reason). Each entry documents
# why the flagged pairing was verified sound on a targeted read.
ALLOWLIST = {
    # D1 false-positive constructions (adjudicated legitimate on targeted reads):
    ("D1", "W205"): "time-denominated rates — '~1 min/store/day of POS time' vs '~80 hours/month chain-wide' derive exactly (1,000 × ~5 min ≈ 83 h); the detector multiplies minutes as events",
    ("D1", "W1516"): "'~2.8M POS transactions/month across 200 stores (~467/store/day)' — 2.8M/200/30.4 = 460 ✓ coherent; the same row's '~8/month' figure is a different activity (exception filings)",
    ("D1", "W897"): "'~100–150 hours/month chain-wide (~30–45 min/store/month)' — 6,000–9,000 min ÷ 200 = 30–45 ✓ exactly coherent, time-denominated",
    ("D1", "W922"): "'~600–800 bulk negotiation transactions/month across 200 stores (~3–4 per store per month)' — 600–800/200 = 3–4 ✓ coherent; the detector grabbed the '200' of 'across 200 stores'",
    ("D1", "W1375"): "'~5 min per overdue call × ~150–300/month = ~12–25 hours/month chain-wide (~4–8 min per store per month)' — all three figures derive; per-store figure is minutes",
    ("D1", "W1555"): "'~15–20 min per damage assessment × ~150–250/month = ~40–80 hours/month chain-wide (~12 min/store/month)' — derives; per-store figure is minutes",
    ("D1", "W1039"): "'500–800 registries/month across 200 stores, ~2–4 registries per store per month' — coherent (detector gap grabbed '200 stores,')",
    ("D1", "W1212"): "'~200–500 kg per store per month; ~40–100 tons/month chain-wide' — exact kg→ton ×200 conversion (handled by the unit-aware tolerance since review #71)",
    # D3 false positives — same-line component lists (different activities, different cadences):
    ("D3", "W107"): "'~3 hours/week for conflict log and override review + ~6 hours/quarter for shelf-tag…' — component list, not one activity in two cadences",
    ("D3", "W7"): "'AP Clerks … ~90–160 hours/month averaged across the team' vs the per-clerk ~1–2.5 h/week — different bases (team-month vs clerk-week), coherent at 8–10 clerks",
    ("D3", "W70"): "'~5–6 hours/week + ~1.5 hours/month cyclical' — explicit component sum",
    ("D3", "W614"): "'~60 min/day on monitoring + ~1 hour/week … + ~2 hours/month on reports' — explicit component sum",
    # seventy-fourth-wave addition: the seventy-third wave's W634 footing repair
    # ('~2–3 hours/day + 4 hours/week + 1 day/month = ~70–90 hours/month') is a
    # same-line component list — the written arithmetic foots (≈ 55–75 + 17 + 8–12);
    # the detector's implied-weekly reading of the 4 h/week component is the documented
    # component-sum false-positive class (W107/W70/W614 precedents). Adjudicated accepted.
    ("D3", "W634"): "'~2–3 hours/day + 4 hours/week + 1 day/month = ~70–90 hours/month' — explicit component sum summing TO the claimed monthly total (the seventy-third wave's footing repair); the 4 h/week component is one input, not the same activity in a second cadence",
    # full-corpus (--all) mode additions (spots inside the previously-audited set):
    ("D1", "W22"): "'~50–80 store-to-store transfers/month … = ~17–27 hours/month across 200 stores (~5–8 min per store per month)' — derives exactly; the per-store figure is MINUTES (time-denominated class)",
    ("D1", "W1202"): "'~PHP 2.1B cash collected/month across all stores; ~PHP 10.6M/store/month' — 2.1B/200 = 10.5M ✓ coherent; the detector grabbed currency magnitudes as event counts",
    ("D3", "W5509"): "'~10–20 sec × ~15,000–35,000 events/month ≈ 40–190 staff-hours/month' on the same bullet as the separate ~4–6 h/week review cadence — component list, both derive",
    ("D3", "W591"): "'~30 min/day on corrective action assignment + ~1 hour/week on weekly review + ~2 hours/month on reports' — explicit component sum",
}

# Statutory citations established as canon by the web-verified adjudications of
# reviews #29–#67 (independent of whether they appear in the audited sample).
KNOWN_GOOD = {
    "RA 7394", "RA 7277", "BP 344", "RA 11058", "RA 11165", "RA 11313", "RA 7877",
    "RA 9285", "RA 876", "RA 6969", "RA 8749", "RA 9275", "RA 10173", "RA 9184",
    "RA 10667", "RA 11592", "RA 11057", "Act 1508", "Act 3936", "RA 4146", "RA 7160",
    "RA 11961", "RA 11036", "RA 11285", "RA 11210", "RA 10771", "RA 10911", "RA 8980",
    "RA 10361", "RA 9501", "RA 10644", "RA 6939", "RA 7610", "RA 9211", "PD 1619",
    "RA 9160", "RA 9136", "RA 7920", "RA 544", "RA 4566", "RA 9266", "RA 9255",
    "RA 9474", "RA 3765", "RA 7581", "RA 11898", "RA 11861", "RA 11534", "RA 11697",
    "RA 3844", "RA 6425", "RA 6713", "RA 3019", "RA 6713", "RA 9236", "RA 9520",
    "RA 7526", "RA 9261", "RA 9288", "RA 7611", "RA 10028", "RA 9995", "RA 8552",
    "PD 851", "PD 1096", "PD 856", "PD 1586", "PD 626", "PD 442", "PD 957", "PD 1517",
    "PD 1344", "PD 904-A", "BP 22", "BP 881", "BP 129",
    "D.O. 174-17", "D.O. 198-18", "D.O. 252-25", "D.O. 53-03", "D.O. 53-04",
    "D.O. 147-15", "D.O. 136-14", "D.O. 13-98", "D.O. 197-18", "D.O. 11", "D.O. 62-09",
    "DAO 2013-22", "DAO 2004-36", "DAO 92-29", "DAO 2000-38", "DAO 2016-08",
    "RR 02-2013", "RR 8-2020", "RR 11-2018", "RR 7-2010", "RR 19-2020", "RR 14-2002",
    "RR 16-2018", "RR 5-2021", "RMC 7-2015", "RMC 57-2015", "RMC 21-2022", "RMC 27-2018",
    "PNS 49", "PNS 48", "CA 496", "CA 141", "EO 647", "EO 406",
    # added by review #71's citation adjudication (each verified in context):
    "RR 1-2023", "RR 8-2022", "RR 9-2022", "RR 3-98", "RR 5-2018",
    "RA 8792", "RA 9710", "RA 6727", "RA 10951", "RA 10623", "RA 9006",
    "PNS 63", "PNS 67", "PNS 35", "PNS 90", "DAO 29",
    # added by the 2026-09-23 seventy-fourth-wave admission (the 62 post-closure
    # workflows W5518–W5579; each verified in context before registering):
    "RA 10175",  # Cybercrime Prevention Act 2012 — PNP Anti-Cybercrime Group is its referral authority (W5558 ransomware step 3; W5559 BEC step 4)
    "RA 7279",   # Urban Development and Housing Act — professional-squatter syndicates / the UDHA relocation track (W5560 background + step 2)
    "RA 10821",  # Children's Emergency Relief and Protection — the duty-of-care framing beside RA 7610 (W5536 background)
}

CITE_RE = re.compile(
    r"\b(?:RA|P\.D\.|PD|D\.O\.|DO|DAO|DENR AO|RR|RMC|PNS|BP|CA|Act No\.|Act|EO)\s?"
    r"(?:No\.?\s)?(\d{1,5}(?:-[0-9]{1,4})?)\b", re.I)

CITE_NORMALIZE = [
    (re.compile(r"^P\.?D\.?\s?(\d+)$", re.I), r"PD \1"),
    (re.compile(r"^D\.?O\.?\s?(\d+-\d+)$", re.I), r"D.O. \1"),
    (re.compile(r"^DENR\s?AO\s?(\d+-\d+)$", re.I), r"DAO \1"),
    (re.compile(r"^Act\s?(?:No\.?)?\s?(\d+)$", re.I), r"Act \1"),
]


def normalize_cit(kind, num):
    s = f"{kind} {num}"
    for pat, rep in CITE_NORMALIZE:
        m = pat.match(s)
        if m:
            return rep if isinstance(rep, str) else s
    return s


def parse_blocks():
    """Yield (vs, file, wid, startline, text) for every workflow block."""
    for d in sorted(os.listdir(WF)):
        if not d.startswith("VS-"):
            continue
        v = int(d.split("-")[1])
        for f in sorted(os.listdir(f"{WF}/{d}")):
            if not (f.startswith("PA-") and f.endswith(".md")):
                continue
            path = f"{WF}/{d}/{f}"
            lines = open(path, encoding="utf-8").read().split("\n")
            cur, start = None, 0
            for i, ln in enumerate(lines):
                m = re.match(r"^## (W\d+[A-Z]?)\.", ln)
                if m:
                    if cur:
                        yield v, f"{d}/{f}", cur, start, "\n".join(lines[start:i])
                    cur, start = m.group(1), i
            if cur:
                yield v, f"{d}/{f}", cur, start, "\n".join(lines[start:])


def num(s):
    s = (s or "").replace(",", "").replace("~", "").strip()
    return float(s) if s else 0.0


def mid(lo, hi):
    return (num(lo) + num(hi)) / 2 if hi else num(lo)


PER_STORE = re.compile(
    r"~?([\d,]+(?:\.\d+)?)(?:\s?[–-]\s?([\d,]+(?:\.\d+)?))?\s*[^.,;|\d×]{0,40}?"
    r"(?:per|/)\s*store\s*(?:per|/)\s*(day|week|month)", re.I)
CHAIN_M = re.compile(
    r"~?([\d,]+)(?:\s?[–-]\s?([\d,]+))?\s*[^.,;|]{0,60}?"
    r"(?:/|per)\s*month\s*(?:chain(?:-wide|\s*wide)?|network-wide|company-wide|across\s*(?:all\s*)?(?:200|205|the\s*chain|all\s*stores)[^.,;|]{0,20})",
    re.I)
HOUR_WEEK = re.compile(r"~?([\d,]+(?:\.\d+)?)(?:\s?[–-]\s?([\d,]+(?:\.\d+)?))?\s*(?:staff-)?hours?\s*/\s*week", re.I)
HOUR_MONTH = re.compile(r"~?([\d,]+(?:\.\d+)?)(?:\s?[–-]\s?([\d,]+(?:\.\d+)?))?\s*(?:staff-)?hours?\s*/\s*month", re.I)
PER_DAY_CHAIN = re.compile(r"~?([\d,]+)(?:\s?[–-]\s?([\d,]+))?\s*[^.,;|]{0,40}?/day[^.,;|]{0,30}?(?:chain|across)", re.I)

CAD = {"day": 30.4, "week": 4.33, "month": 1}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--all", action="store_true",
                    help="regression net: run D1/D3/D4 over ALL workflows (D2 skipped — no unaudited baseline post-closure)")
    args = ap.parse_args()

    audited = set(l.strip() for l in open(REGISTRY) if re.match(r"^W\d+[A-Z]?$", l.strip()))
    scan_all = bool(args.all)
    audited_cites = set()
    # citation baseline from the audited corpus (used by D2 in transition mode)
    if not scan_all:
        for _v, _f, wid, _s, text in parse_blocks():
            if wid in audited:
                for m in CITE_RE.finditer(text):
                    kind = m.group(0).split()[0].upper().rstrip(".")
                    audited_cites.add(normalize_cit(kind, m.group(1)))

    hits = []
    for v, f, wid, s, text in parse_blocks():
        if not scan_all and wid in audited:
            continue
        fields = "\n".join(ln for ln in text.split("\n")
                           if ln.startswith("| **") or ln.startswith("- "))
        # D1: per-store rate vs chain-wide monthly total — SAME FIELD ROW only
        # (the review-#65 class was per-row contradictions). Skips the two benign
        # constructions: (a) the identical figure matched twice (per-store number
        # restated with a chain-scope marker), and (b) the "monthly" figure that is
        # itself per-store scoped (within 3x of the UN-multiplied rate).
        for row in fields.split("\n"):
            ps = PER_STORE.findall(row)
            cm = CHAIN_M.findall(row)
            if ps and cm:
                for a, b, cad in ps:
                    per_store_mo = mid(a, b) * CAD[cad.lower()]
                    rate = per_store_mo * 200
                    for c, d in cm:
                        tot = mid(c, d)
                        if tot <= 0:
                            continue
                        if (a, b) == (c, d):
                            continue  # same figure matched twice
                        if per_store_mo / 3 <= tot <= per_store_mo * 3:
                            continue  # the monthly figure is per-store scoped
                        if rate / 3 <= tot <= rate * 3:
                            continue  # coherent chain total
                        if re.search(r"\bkg\b", row, re.I) and re.search(r"\btons?\b", row, re.I) \
                                and rate / 3000 <= tot <= rate * 3:
                            continue  # kg-per-store vs tons-chain-wide (÷1000 unit conversion)
                        hits.append(("D1", f, wid, s + 1,
                                     f"per-store {a}{'–' + b if b else ''}/{cad} ⇒ {rate:,.0f}/mo chain vs same-row {c}{'–' + d if d else ''}/mo chain-marked ({tot / max(rate, 1):.2f}×)"))
        # D2: unseen statutory citations (transition mode only — no baseline in --all)
        if not scan_all:
            for m in CITE_RE.finditer(text):
                raw = m.group(0)
                kind = raw.split()[0].upper().rstrip(".")
                cit = normalize_cit(kind, m.group(1))
                if cit in audited_cites or cit.upper() in KNOWN_GOOD or cit in KNOWN_GOOD:
                    continue
                # generic 'RA nnnn' numbers: only flag if the SAME number is not used
                # anywhere in the audited corpus under any prefix variant
                variants = {cit, cit.replace("D.O.", "DO"), cit.replace("DO", "D.O."),
                            cit.replace("Act ", "Act No. ")}
                if variants & audited_cites or variants & KNOWN_GOOD:
                    continue
                hits.append(("D2", f, wid, s + 1, f"citation '{raw}' not in audited corpus or canon list"))
        # D3: hours/week vs hours/month contradiction — SAME LINE only (the
        # block-level form false-positives on different activities carrying
        # different cadences in one workflow)
        for row in fields.split("\n"):
            hw = HOUR_WEEK.findall(row)
            hm = HOUR_MONTH.findall(row)
            if hw and hm:
                for a, b in hw:
                    wk = mid(a, b)
                    for c, d in hm:
                        mo = mid(c, d)
                        implied_wk = mo / 4.33
                        if wk > 0 and implied_wk > 0 and (
                                implied_wk / wk > 4 or wk / implied_wk > 4):
                            hits.append(("D3", f, wid, s + 1,
                                         f"same line: ~{a}{'–' + b if b else ''} h/week vs ~{c}{'–' + d if d else ''} h/month (implied {implied_wk:,.0f} h/wk; {max(implied_wk / wk, wk / implied_wk):.1f}× apart): {row.strip()[:110]}"))
        # D4: chain-wide /day total for a per-store per-week/month activity
        if ps and PER_DAY_CHAIN.search(fields):
            for a, b, cad in ps:
                if cad.lower() in ("week", "month"):
                    hits.append(("D4", f, wid, s + 1,
                                 f"per-store cadence /{cad} alongside a chain-wide /day total"))

    live = [h for h in hits if (h[0], h[2]) not in ALLOWLIST]
    if not args.all and not live and audited == set():
        pass
    byd = collections.Counter(h[0] for h in live)
    if not args.quiet:
        print(f"audited-set: {len(audited)} | audited-citation baseline: {len(audited_cites)}"
              + (" | MODE: full corpus (D2 skipped)" if args.all else ""))
        print(f"flags: {len(live)} (D1 per-store/chain {byd['D1']}, D2 unseen citations "
              f"{byd['D2']}, D3 cadence {byd['D3']}, D4 chain-/day {byd['D4']})")
        for h in live:
            print(f"{h[0]}|{h[1]}:{h[3]}|{h[2]}|{h[4]}")
    print(f"TOTALS live={len(live)}")
    sys.exit(1 if live else 0)


if __name__ == "__main__":
    main()
