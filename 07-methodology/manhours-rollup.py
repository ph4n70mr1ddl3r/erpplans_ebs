#!/usr/bin/env python3
"""
manhours-rollup.py — Derive workflow man-hours from the Steps tables' Duration column.

The corpus guarantees every workflow a Steps table whose rows carry
`| # | Activity | Role (R) | Role (A) | Duration |` (validator-enforced, and the
single source of truth for the generated BPMN). What it has never had is a LIVING
derivation of man-hours from that column: the `### Time Estimate` sections were
hand-finalized once (backfill-time-estimate.py -> finalize-time-estimates.py,
2026-08-28) and are audited only where their inline math is written out
(audit-time-estimate-math.py). This tool re-derives the roll-up from the steps on
every run, honestly classifying every Duration cell instead of guessing:

  effort            — "~30 min", "5–10 min", "2 hours", "~1–2 hours/day",
                      "4 hours/week", "1 day/month", "3 days/quarter" … hours
                      normalized to monthly-equivalents under the house conventions
                      (below); non-cadence denominators ("15 min/transfer") stay
                      SYMBOLIC per-unit rates and are never summed into hours
  elapsed           — bare "2–3 days" / "4–6 weeks": elapsed windows, reported in
                      days, NOT converted to hours (house rule: elapsed timelines
                      reported not summed — finalize-time-estimates.py)
  automated         — system steps ("Automated", "(automated)" annotations,
                      "N–N min (automated)"): 0 human hours
  cadence-only      — "monthly", "quarterly", "per event", "per cycle", "per W15":
                      the cell carries WHEN, not HOW LONG — no effort figure exists
  qualitative       — "continuous", "ongoing", "maintained", "periodic",
                      "real-time", "immediate", "event-driven", "as needed", …
  empty / non-duration-header / unparseable — counted and listed for triage

Conventions (from audit-time-estimate-math.py's licensed set, primary alternates):
  1 workday = 8 h; month = 21.7 business days; week = 4.33 months-month; month = 1;
  quarter -> /3; year -> /12; season -> /6.  Ranges sum low+low / high+high.
  Compound cells split on top-level " + " ("Automated + 15 min/run review") and
  every informative segment is classified; the workflow carries the union.
  Bare cadence words are NOT annualized by workflow Frequency (mixed-cadence
  workflows may carry per-step cadences — the finalize-time-estimates rule).

Role attribution: the Role (R) cell, split on " / " (house rule: compound roles
attribute to EACH named role; the workflow keeps the raw string too).

Outputs are honest by construction: totals cover ONLY the effort steps that carry
a cadence denominator; per-unit rates and elapsed windows are listed, never added
into hour totals; every unparseable cell is reported with file, workflow, step.

Usage:
    python3 07-methodology/manhours-rollup.py                    # stdout summary
    python3 07-methodology/manhours-rollup.py --report PATH      # markdown report
    python3 07-methodology/manhours-rollup.py --json PATH        # full detail
    python3 07-methodology/manhours-rollup.py --csv PATH         # workflow x role rows
    python3 07-methodology/manhours-rollup.py --ranking PATH     # per-workflow ranking by derived hours
    python3 07-methodology/manhours-rollup.py --workflow W30     # one-workflow detail
    python3 07-methodology/manhours-rollup.py --unparseable N    # show N unparseable cells
    python3 07-methodology/manhours-rollup.py --check            # byte-verify the four
                                                                 # shipped artifacts, exit 1 on drift
"""
import argparse, collections, csv, glob, io, json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

# ---------------------------------------------------------------- house constants
HOURS_PER_WORKDAY = 8.0
BUSINESS_DAYS_PER_MONTH = 21.7
WEEKS_PER_MONTH = 4.33
# cadence denominator -> multiplier to monthly hours
CADENCE_TO_MONTH = {
    "day": BUSINESS_DAYS_PER_MONTH,
    "week": WEEKS_PER_MONTH,
    "month": 1.0,
    "quarter": 1.0 / 3.0,
    "year": 1.0 / 12.0,
    "season": 1.0 / 6.0,
}

# ---------------------------------------------------------------- parsing
BLOCK_SPLIT = re.compile(r"(?=^#{2,4} W\d+[A-Z]?\. )", re.MULTILINE)
WF_HEADER = re.compile(r"^#{2,4} (W\d+[A-Z]?)\. (.+?)\s*$", re.MULTILINE)
STEPS_SECTION = re.compile(
    r"^### Steps\s*\n(.*?)(?=^### |^---|^## |\Z)", re.MULTILINE | re.DOTALL
)
STEPS_HEADER = re.compile(
    r"^\|\s*#\s*\|\s*Activity\s*\|\s*Role \(R\)\s*\|\s*Role \(A\)\s*\|\s*"
    r"(Duration|Frequency|Latency)\s*\|\s*$", re.I,
)
STEP_ROW = re.compile(
    r"^\|\s*(\d+[a-z]?(?:\.\d+)?)\s*\|\s*(.+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|"
)
FREQ_FIELD = re.compile(r"^\| \*\*Frequency\*\* \| (.+?) \|", re.MULTILINE)
VOL_FIELD = re.compile(r"^\| \*\*Volume\*\* \| (.+?) \|", re.MULTILINE)

NUM = r"(\d[\d,]*(?:\.\d+)?)"
RNG = r"(?:–|—|-|to)\s*"

def _n(s):
    return float(s.replace(",", ""))

# number [range] unit, optional trailing context
DUR_NUM_RE = re.compile(
    r"^~?\s*" + NUM + r"(?:\s*" + RNG + NUM + r")?\s*"
    r"(hours?|hrs?|h|minutes?|mins?|seconds?|secs?|days?|weeks?|months?|years?)\b(.*)$",
    re.I,
)

def _to_hours(lo, hi, unit):
    """Convert a numeric pair in the given unit to hours."""
    if unit.startswith(("hour", "hr")) or unit == "h":
        return (lo, hi)
    if unit.startswith("min") or unit == "m":
        return (lo / 60.0, hi / 60.0)
    if unit.startswith("sec") or unit == "s":
        return (lo / 3600.0, hi / 3600.0)
    return (lo, hi)  # days/weeks/months handled by caller
MIXED_RANGE_RE = re.compile(  # "30 min–1 hour", "45 min - 2 hours"
    r"^~?\s*" + NUM + r"\s*(?:minutes?|mins?)\s*" + RNG + NUM + r"\s*(?:hours?|hrs?)\b(.*)$",
    re.I,
)
TIMES_RE = re.compile(r"^~?\s*" + NUM + r"\s*x?\s*(?:/|per\b)\s*(\w+)", re.I)  # "3x/week"
PAREN_AUTOMATED = re.compile(r"\(automated\)", re.I)
DENOM_RE = re.compile(r"(?:/|per\s+)\s*([A-Za-z]+)", re.I)

CADENCE_WORDS = {"day", "days", "daily", "week", "weeks", "weekly", "month", "months",
                 "monthly", "quarter", "quarters", "quarterly", "year", "years",
                 "annual", "annually", "yearly", "season", "semi-annual",
                 "semi-annual", "semiannually", "semi-annually", "biannual", "biannually"}
QUAL_WORDS = {"continuous", "continuously", "ongoing", "maintained", "periodic",
              "periodically", "immediate", "immediately", "real-time", "realtime",
              "event-driven", "as-needed", "as", "needed", "variable", "varies",
              "24/7", "always-on", "on-demand", "recurring", "watch", "setup",
              "external", "standard", "self-service", "instant", "instantly",
              "same", "reactive", "ad-hoc", "adhoc", "one-time", "nonce"}
AUTOMATED_WORDS = {"automated", "auto", "system", "automatic"}
HALF_FULL_DAY = {"half": HOURS_PER_WORKDAY / 2, "full": HOURS_PER_WORKDAY}

def _split_top(cell):
    """Split a compound cell on top-level ' + ' / '；' / ' ; ' outside parens."""
    parts, depth, cur, i = [], 0, [], 0
    while i < len(cell):
        ch = cell[i]
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if depth == 0 and cell[i:i + 3] == " + ":
            parts.append("".join(cur)); cur = []; i += 3; continue
        if depth == 0 and cell[i] == ";":
            parts.append("".join(cur)); cur = []; i += 1; continue
        cur.append(ch); i += 1
    parts.append("".join(cur))
    return [p.strip() for p in parts if p.strip()]

def _denominators(rest):
    """Return (cadence_den|None, [multiplier units]) from trailing context text."""
    cad, mults = None, []
    for m in DENOM_RE.finditer(rest or ""):
        w = m.group(1).lower()
        if w in ("day", "days", "daily"): cad = "day"
        elif w in ("week", "weeks", "weekly"): cad = "week"
        elif w in ("month", "months", "monthly"): cad = "month"
        elif w in ("quarter", "quarters", "quarterly"): cad = "quarter"
        elif w in ("year", "years", "annual", "annually", "yearly"): cad = "year"
        elif w in ("season", "seasons"): cad = "season"
        elif w in ("hour", "hours", "min", "minute", "minutes"): pass  # "per hour" rate talk
        else: mults.append(w)
    return cad, mults

def classify_duration(cell):
    """Classify one Duration cell. Returns a dict:
       klass, hours=(low,high) per-occurrence-or-per-cadence, cadence (denominator
       or None for per-occurrence), monthly=(low,high)|None, unit (for per-unit),
       mults, elapsed_days=(low,high)|None, notes=[...]"""
    raw = cell.strip()
    raw = re.sub(r"^[~≈]\s*", "", raw)
    c = raw.strip()
    out = {"klass": "unparseable", "hours": None, "cadence": None, "monthly": None,
           "unit": None, "mults": [], "elapsed_days": None, "notes": []}
    if c in ("", "—", "–", "-", "—", "–", "TBD", "tbd"):
        out["klass"] = "empty"; return out

    segments = _split_top(c)
    if len(segments) > 1:
        out["klass"] = "compound"
    klasses = []
    out["_m_low"] = 0.0; out["_m_high"] = 0.0; out["_has_monthly"] = False
    out["_o_low"] = 0.0; out["_o_high"] = 0.0; out["_has_occ"] = False
    out["_has_unit"] = False
    for seg in segments:
        s = seg.strip()
        sl = s.lower().rstrip(".").strip()
        # --- pure-word classes -------------------------------------------------
        first = re.split(r"[\s(,;/-]", sl, 1)[0]
        if PAREN_AUTOMATED.search(s) or sl in AUTOMATED_WORDS or first in AUTOMATED_WORDS and len(sl.split()) <= 2:
            klasses.append("automated"); continue
        # "Automated (< 30 sec)" — system step, parenthetical is machine time
        if re.match(r"^(?:automated|auto|automatic)\b", sl):
            klasses.append("automated")
            if re.search(r"\d", s): out["notes"].append("machine time detail: " + s)
            continue
        # cross-references — the step is performed inside another workflow
        if (re.match(r"^(?:part of|during|absorbed (?:into|in|within)|integrated into|"
                     r"rides (?:the )?|folded into|handled (?:by|in) W|same as|per W|see W|within W)", sl)
                and not re.search(r"\d+\s*(?:min|hour|sec|\bh\b)", sl)):
            klasses.append("cross-ref")
            out["notes"].append("cross-reference: " + s)
            continue
        # digit-less cells are never effort: qualitative or cadence-only
        if not re.search(r"\d", s):
            toks = set(re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", sl))
            if toks & QUAL_WORDS:
                klasses.append("qualitative")
            elif sl in ("half day", "full day"):
                klasses.append("effort")
                _acc(out, HALF_FULL_DAY[sl.split()[0]], HALF_FULL_DAY[sl.split()[0]], None, [])
            else:
                klasses.append("cadence-only")
            continue
        # "Day 1–2" post-incident style labels -> elapsed
        mday = re.match(r"^days?\s+" + NUM + r"(?:\s*" + RNG + NUM + r")?\s*$", s, re.I)
        if mday:
            lo = _n(mday.group(1)); hi = _n(mday.group(2)) if mday.group(2) else lo
            ed = out["elapsed_days"] or (0.0, 0.0)
            out["elapsed_days"] = (ed[0] + lo, ed[1] + hi)
            if len(segments) == 1: out["klass"] = "elapsed"
            out["notes"].append("day-label elapsed: " + s)
            klasses.append("elapsed"); continue
        # "annual (6 hours)" — qualifier with parenthesized effort
        pq = re.match(r"^([^()]+)\(\s*~?" + NUM + r"(?:\s*" + RNG + NUM + r")?\s*"
                      r"(hours?|hrs?|minutes?|mins?|days?|weeks?)\s*\)\s*$", s, re.I)
        if pq:
            a = _n(pq.group(2)); b = _n(pq.group(3)) if pq.group(3) else None
            lo, hi = (a, b) if b is not None else (a, a)
            unit = pq.group(4).lower()
            hrs = _to_hours(lo, hi, unit)
            if unit.startswith("day"):
                hrs = (lo * HOURS_PER_WORKDAY, hi * HOURS_PER_WORKDAY)
            elif unit.startswith("week"):
                hrs = (lo * HOURS_PER_WORKDAY * 5, hi * HOURS_PER_WORKDAY * 5)
            outer = pq.group(1).lower()
            cad = None
            for w, c in (("quarter", "quarter"), ("annual", "year"), ("year", "year"),
                         ("month", "month"), ("week", "week"), ("day", "day"), ("season", "season")):
                if w in outer: cad = c; break
            klasses.append("effort")
            _acc(out, hrs[0], hrs[1], cad, [])
            out["notes"].append("parenthesized effort: " + s)
            continue
        # "Full shift × 5 days" — shift-count effort (8 h per shift-day)
        msh = re.match(r"^(?:full |half )?shifts?\s*[×x*]\s*~?" + NUM + r"(?:\s*" + RNG + NUM + r")?\s*"
                       r"(?:days?|shifts?)?\s*$", s, re.I)
        if msh:
            a = _n(msh.group(1)); b = _n(msh.group(2)) if msh.group(2) else None
            lo, hi = (a, b) if b is not None else (a, a)
            klasses.append("effort")
            _acc(out, lo * HOURS_PER_WORKDAY, hi * HOURS_PER_WORKDAY, None, [])
            out["notes"].append("shift-count: " + s)
            continue
        # "As needed (15–30 min/occurrence)" — event-driven per-unit effort
        ma = re.match(r"^as[- ]needed\b[^()]*\((.+?)\)\s*$", s, re.I)
        if ma:
            dm3 = DUR_NUM_RE.match(ma.group(1).strip())
            if dm3:
                a = _n(dm3.group(1)); b = _n(dm3.group(2)) if dm3.group(2) else None
                lo, hi = (a, b) if b is not None else (a, a)
                hrs = _to_hours(lo, hi, dm3.group(3).lower())
                cad, mults = _denominators(dm3.group(4) or "")
                klasses.append("effort")
                _acc(out, hrs[0], hrs[1], cad, mults or ["occurrence"])
                out["notes"].append("event-driven: " + s)
                continue
        # labeled prefix ("Scheduling: 15 min") — retry numeric after the colon
        if ":" in s and not re.search(r"\d", s.split(":", 1)[0]):
            s2 = s.split(":", 1)[1].strip()
            dm4 = DUR_NUM_RE.match(s2)
            if dm4:
                a = _n(dm4.group(1)); b = _n(dm4.group(2)) if dm4.group(2) else None
                lo, hi = (a, b) if b is not None else (a, a)
                hrs = _to_hours(lo, hi, dm4.group(3).lower())
                cad, mults = _denominators(dm4.group(4) or "")
                klasses.append("effort")
                _acc(out, hrs[0], hrs[1], cad, mults)
                out["notes"].append("labeled: " + s)
                continue
        # "Within 24 hours" / "First 24–72 hours" — elapsed windows
        mw = re.match(r"^(?:within|first)\s+~?" + NUM + r"(?:\s*" + RNG + NUM + r")?\s*"
                      r"(hours?|hrs?|days?|weeks?)\b\s*$", s, re.I)
        if mw:
            a = _n(mw.group(1)); b = _n(mw.group(2)) if mw.group(2) else None
            lo, hi = (a, b) if b is not None else (a, a)
            unit = mw.group(3).lower()
            sc = 1.0
            if unit.startswith(("hour", "hr")): sc = 1.0 / 24.0
            elif unit.startswith("week"): sc = 7.0
            ed = out["elapsed_days"] or (0.0, 0.0)
            out["elapsed_days"] = (ed[0] + lo * sc, ed[1] + hi * sc)
            if len(segments) == 1: out["klass"] = "elapsed"
            out["notes"].append("elapsed window: " + s)
            klasses.append("elapsed"); continue
        # "1–3 business days" / "5–10 working days" / "2–3 simulated days" — elapsed
        mb = re.match(r"^~?" + NUM + r"(?:\s*" + RNG + NUM + r")?\s*"
                      r"(?:business |working |simulated )?(days?|weeks?)\b\s*$", s, re.I)
        if mb:
            a = _n(mb.group(1)); b = _n(mb.group(2)) if mb.group(2) else None
            lo, hi = (a, b) if b is not None else (a, a)
            ed = out["elapsed_days"] or (0.0, 0.0)
            out["elapsed_days"] = (ed[0] + lo, ed[1] + hi)
            if len(segments) == 1: out["klass"] = "elapsed"
            out["notes"].append("elapsed window: " + s)
            klasses.append("elapsed"); continue
        # "< 5 min" upper-bound effort (label prefix tolerated)
        if "<" in s:
            s_lb = s[s.index("<"):]
            dm2 = DUR_NUM_RE.match(s_lb[1:].strip())
            if dm2:
                a = _n(dm2.group(1)); unit = dm2.group(3).lower()
                cad, mults = _denominators(dm2.group(4) or "")
                if unit.startswith(("day", "week", "month")):
                    sc = {"d": 1.0, "w": 7.0, "m": 30.0}[unit[0]]
                    ed = out["elapsed_days"] or (0.0, 0.0)
                    out["elapsed_days"] = (ed[0], ed[1] + _to_hours(a, a, unit)[1] * sc)
                    if len(segments) == 1: out["klass"] = "elapsed"
                    out["notes"].append("upper-bound elapsed: " + s)
                    klasses.append("elapsed"); continue
                klasses.append("effort")
                _acc(out, 0.0, _to_hours(a, a, unit)[1], cad, mults)
                out["notes"].append("upper bound: " + s)
                continue
        if sl in QUAL_WORDS or first in QUAL_WORDS:
            klasses.append("qualitative")
            if re.search(r"\d", s): out["notes"].append("qualitative with figures: " + s)
            continue
        # bare cadence word(s) — tolerate slashes/commas ('monthly/quarterly')
        words = [w.strip("()") for w in re.split(r"[\s,/]+", sl) if w.strip("()")]
        if words and all(w in CADENCE_WORDS for w in words):
            klasses.append("cadence-only"); continue
        if sl.startswith("per "):
            klasses.append("cadence-only"); continue
        # "3x/week" / "3 times per month"
        tm = TIMES_RE.match(s)
        if tm:
            klasses.append("cadence-only"); out["notes"].append("count-only: " + s); continue
        # --- numeric -----------------------------------------------------------
        mm = MIXED_RANGE_RE.match(s)
        if mm:
            lo = _n(mm.group(1)) / 60.0; hi = _n(mm.group(2))
            rest = mm.group(3)
            cad, mults = _denominators(rest)
            klasses.append("effort")
            _acc(out, lo, hi, cad, mults)
            continue
        dm = DUR_NUM_RE.match(s)
        if dm:
            a = _n(dm.group(1))
            b = _n(dm.group(2)) if dm.group(2) else None
            unit = dm.group(3).lower()
            rest = dm.group(4) or ""
            lo, hi = (a, b) if b is not None else (a, a)
            if unit.startswith(("hour", "hr")) or unit == "h":
                hrs = (lo, hi)
            elif unit.startswith("min") or unit == "m":
                hrs = (lo / 60.0, hi / 60.0)
            elif unit.startswith("sec") or unit == "s":
                hrs = (lo / 3600.0, hi / 3600.0)
            else:  # days / weeks / months
                cad, mults = _denominators(rest)
                if cad:  # "1 day/month" — recurring effort, x8 h/workday
                    scale = {"day": HOURS_PER_WORKDAY, "days": HOURS_PER_WORKDAY,
                             "week": HOURS_PER_WORKDAY * 5.0,
                             "weeks": HOURS_PER_WORKDAY * 5.0,
                             "month": HOURS_PER_WORKDAY * BUSINESS_DAYS_PER_MONTH,
                             "months": HOURS_PER_WORKDAY * BUSINESS_DAYS_PER_MONTH}[unit]
                    klasses.append("effort")
                    _acc(out, lo * scale, hi * scale, cad, mults)
                    continue
                # bare days/weeks/months -> elapsed window, reported not summed
                scale = {"day": 1.0, "days": 1.0, "week": 7.0, "weeks": 7.0,
                         "month": 30.0, "months": 30.0, "year": 365.0, "years": 365.0}[unit]
                if len(segments) == 1:
                    out["klass"] = "elapsed"
                elif not out["klass"] == "elapsed":
                    pass
                ed = out["elapsed_days"] or (0.0, 0.0)
                out["elapsed_days"] = (ed[0] + lo * scale, ed[1] + hi * scale)
                out["notes"].append("elapsed window: " + s)
                klasses.append("elapsed"); continue
            cad, mults = _denominators(rest)
            klasses.append("effort")
            _acc(out, hrs[0], hrs[1], cad, mults)
            continue
        # inline-figure rescue: '~8,000 training hours/year across all employees',
        # 'inside the 1.5-hour quarterly cycle'
        mr = re.search(r"~?" + NUM + r"(?:\s*" + RNG + NUM + r")?\s*-?\s*"
                       r"(hours?|hrs?|h|minutes?|mins?|seconds?|secs?)\b"
                       r"((?:\s*(?:/|per\b)\s*(?:day|week|month|quarter|year|season)\w*)?)",
                       s, re.I)
        if mr:
            a = _n(mr.group(1)); b = _n(mr.group(2)) if mr.group(2) else None
            lo, hi = (a, b) if b is not None else (a, a)
            hrs = _to_hours(lo, hi, mr.group(3).lower())
            cad = None
            if mr.group(4):
                cw = re.search(r"(day|week|month|quarter|year|season)", mr.group(4), re.I)
                cad = cw.group(1).lower()
            klasses.append("effort")
            _acc(out, hrs[0], hrs[1], cad, [])
            out["notes"].append("inline figure: " + s)
            continue
        # trailing "(automated)" after numbers etc.
        if PAREN_AUTOMATED.search(s):
            klasses.append("automated"); continue
        klasses.append("unparseable")

    if not klasses:
        return out
    # --- fold segment verdicts ----------------------------------------------
    if "cross-ref" in klasses and len(klasses) == 1:
        out["klass"] = "cross-ref"
        out.pop("_m_low", None); out.pop("_o_low", None)
        return out
    if "unparseable" in klasses and "effort" not in klasses and "elapsed" not in klasses:
        out["klass"] = "unparseable"
        out.pop("_m_low", None); out.pop("_o_low", None)
        return out
    if len(segments) == 1:
        if out["klass"] not in ("elapsed",):
            out["klass"] = klasses[0]
    elif len(set(klasses)) == 1:
        out["klass"] = klasses[0]          # e.g. 'annual + on change' -> cadence-only
    else:
        out["klass"] = "compound"
    # monthly wins over per-occurrence (mixed cadences are each monthly-normalized)
    if out["_has_monthly"]:
        out["monthly"] = (out["_m_low"], out["_m_high"])
        out["hours"] = (out["_o_low"], out["_o_high"]) if out["_has_occ"] else None
        if out["_has_unit"]:
            out["notes"].append("includes per-unit segment")
    elif out["_has_unit"]:
        out["klass"] = "per-unit"
        out["hours"] = (out["_o_low"], out["_o_high"])
    elif out["_has_occ"]:
        out["hours"] = (out["_o_low"], out["_o_high"])
    if out["klass"] == "compound":
        if "automated" in klasses: out["notes"].append("includes automated segment")
        if "cadence-only" in klasses: out["notes"].append("includes cadence-only segment")
        if "qualitative" in klasses: out["notes"].append("includes qualitative segment")
        if "elapsed" in klasses: out["notes"].append("includes elapsed segment")
    for k in ("_m_low", "_m_high", "_has_monthly", "_o_low", "_o_high", "_has_occ", "_has_unit"):
        out.pop(k, None)
    return out

def _acc(out, lo, hi, cad, mults):
    """Accumulate one effort segment (hours lo–hi) into the running totals.
    Cadenced segments normalize to monthly; uncadenced-with-multipliers go to the
    symbolic per-unit bucket; plain per-occurrence hours accumulate as hours."""
    if cad is None and mults:
        out["mults"] = sorted(set(out["mults"] + mults))
        out["unit"] = "+".join(out["mults"])
        out["_o_low"] += lo; out["_o_high"] += hi
        out["_has_unit"] = True
        return
    if cad is None:
        out["cadence"] = out["cadence"] or "occurrence"
        out["_o_low"] += lo; out["_o_high"] += hi; out["_has_occ"] = True
        return
    out["cadence"] = cad
    m = CADENCE_TO_MONTH[cad]
    out["_m_low"] += lo * m; out["_m_high"] += hi * m; out["_has_monthly"] = True
    if mults:
        out["notes"].append("multiplier NOT applied (symbolic): per " + ", ".join(mults))



# ---------------------------------------------------------------- corpus walk
def walk():
    """Yield (relpath, wf_id, wf_name, wf_dict) for every workflow block."""
    for path in sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md"))):
        rel = os.path.relpath(path, REPO)
        text = open(path).read()
        for block in BLOCK_SPLIT.split(text):
            hm = WF_HEADER.search(block)
            if not hm:
                continue
            sm = STEPS_SECTION.search(block)
            header = None
            rows = []
            irregular = 0
            if sm:
                lines = sm.group(1).split("\n")
                for line in lines:
                    if STEPS_HEADER.match(line):
                        header = STEPS_HEADER.match(line).group(1)
                    rm = STEP_ROW.match(line)
                    if rm:
                        if rm.group(2).lower() in ("activity", "---") or set(rm.group(2)) <= {"-"}:
                            continue
                        rows.append(rm.groups())
                    elif line.strip().startswith("|") and re.match(r"^\|\s*\d", line):
                        irregular += 1
            fm = FREQ_FIELD.search(block)
            vm = VOL_FIELD.search(block)
            yield rel, hm.group(1), hm.group(2).strip(), {
                "header": header, "rows": rows, "irregular_rows": irregular,
                "frequency": fm.group(1).strip() if fm else None,
                "volume": vm.group(1).strip() if vm else None,
                "block": block,
            }

def split_roles(role_cell):
    """'A / B' -> [A, B]; singletons stay singletons."""
    parts = [p.strip() for p in role_cell.split("/")]
    return [p for p in parts if p and p.lower() != "system"] or ["System"]

# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--report", metavar="PATH", help="write markdown report")
    ap.add_argument("--json", metavar="PATH", help="write full JSON detail")
    ap.add_argument("--csv", metavar="PATH", help="write workflow x role CSV")
    ap.add_argument("--ranking", metavar="PATH",
                    help="write per-workflow ranking CSV (all workflows by "
                         "derived monthly hours, high then low desc)")
    ap.add_argument("--workflow", metavar="WID", help="show detail for one workflow")
    ap.add_argument("--unparseable", type=int, default=0, metavar="N",
                    help="print up to N unparseable cells for triage")
    ap.add_argument("--check", action="store_true",
                    help="re-derive the four shipped artifacts in memory and "
                         "byte-compare them; exit 1 on drift or missing file")
    args = ap.parse_args()

    class_counts = collections.Counter()
    workflows = []
    role_month = collections.defaultdict(lambda: [0.0, 0.0, 0, 0])  # low, high, wf_steps, auto
    for rel, wid, wname, w in walk():
        rec = {"file": rel, "id": wid, "name": wname, "header": w["header"],
               "frequency": w["frequency"], "steps": [], "irregular_rows": w["irregular_rows"]}
        monthly = [0.0, 0.0]; effort_n = 0
        elapsed = [0.0, 0.0]; per_unit = []
        nauto = ncad = nqual = nempty = 0
        for (num, activity, r, a, dur) in w["rows"]:
            cls = classify_duration(dur)
            cls["step"] = num; cls["role_r"] = r.strip(); cls["role_a"] = a.strip()
            cls["duration"] = dur.strip()
            rec["steps"].append(cls)
            k = cls["klass"]
            class_counts[k if k != "compound" else "compound"] += 1
            if k in ("effort", "compound") and cls.get("monthly"):
                monthly[0] += cls["monthly"][0]; monthly[1] += cls["monthly"][1]; effort_n += 1
                for role in split_roles(cls["role_r"]):
                    rm_ = role_month[role]
                    rm_[0] += cls["monthly"][0]; rm_[1] += cls["monthly"][1]
                    rm_[2] += 1
            elif k == "per-unit":
                per_unit.append({"unit": cls["unit"], "hours": cls["hours"]})
            elif k == "elapsed" and cls["elapsed_days"]:
                elapsed[0] += cls["elapsed_days"][0]; elapsed[1] += cls["elapsed_days"][1]
            elif k == "automated": nauto += 1
            elif k == "cadence-only": ncad += 1
            elif k == "qualitative": nqual += 1
            elif k == "empty": nempty += 1
            if k == "automated":
                for role in split_roles(cls["role_r"]):
                    role_month[role][3] += 1
        rec.update({
            "monthly_hours": tuple(monthly), "effort_steps": effort_n,
            "automated_steps": nauto, "cadence_only_steps": ncad,
            "qualitative_steps": nqual, "empty_steps": nempty,
            "elapsed_days": tuple(elapsed), "per_unit_rates": per_unit,
        })
        workflows.append(rec)

    # ---- detail mode
    if args.workflow:
        want = args.workflow.lower()
        hits = [w for w in workflows if w["id"].lower() == want]
        if not hits:
            sys.exit(f"workflow {args.workflow} not found")
        w = hits[0]
        print(f"{w['id']}. {w['name']}   ({w['file']})")
        print(f"header: {w['header']}   frequency: {w['frequency']}")
        for s in w["steps"]:
            mon = f" -> {s['monthly'][0]:.2f}–{s['monthly'][1]:.2f} h/month" if s.get("monthly") else ""
            print(f"  step {s['step']:>4} [{s['klass']:<13}] {s['duration'][:70]}{mon}")
            if s["mults"]: print(f"           multipliers: {s['mults']}")
            for n in s["notes"]: print(f"           note: {n}")
        print(f"monthly total (effort, cadenced): {w['monthly_hours'][0]:.1f}–{w['monthly_hours'][1]:.1f} h"
              f"  over {w['effort_steps']} effort steps"
              f"; elapsed {w['elapsed_days'][0]:.1f}–{w['elapsed_days'][1]:.1f} d;"
              f" per-unit rates {len(w['per_unit_rates'])};"
              f" automated {w['automated_steps']}; cadence-only {w['cadence_only_steps']};"
              f" qualitative {w['qualitative_steps']}")
        return

    total_steps = sum(class_counts.values())
    lines = []
    P = lines.append
    P("# Workflow man-hours roll-up (mechanically derived)")
    P("")
    P(f"Corpus: {len(workflows)} workflow blocks with Steps tables across "
      f"`01-model-company/workflows/`. Every Duration cell is classified; totals cover")
    P("ONLY cadence-denominated effort steps. Per-unit rates (`15 min/transfer`),")
    P("elapsed windows (`2–3 days`) and cadence-only cells are counted, never summed")
    P("into hours. This file is GENERATED by `07-methodology/manhours-rollup.py`.")
    P("")
    P("## Classification coverage")
    P("")
    P("| class | cells | share | meaning |")
    P("|---|---:|---:|---|")
    desc = {
        "effort": "hours normalized to monthly equivalents (cadence denominators)",
        "per-unit": "hours per non-cadence unit (transfer/case/store) — symbolic",
        "elapsed": "elapsed windows (bare days/weeks/months) — reported in days",
        "automated": "system steps — zero human hours",
        "cadence-only": "cell says WHEN (monthly / per event), not HOW LONG",
        "qualitative": "continuous / ongoing / as needed / periodic …",
        "compound": "mixed segments ('Automated + 15 min/run review')",
        "empty": "empty / dash cell",
        "cross-ref": "step performed inside another workflow ('Part of W89')",
        "unparseable": "did not match any grammar — needs manual triage",
        "non-duration-header": "steps table under a Frequency/Latency header column",
    }
    for k in ("effort", "per-unit", "elapsed", "automated", "cadence-only",
              "qualitative", "compound", "cross-ref", "empty", "unparseable"):
        n = class_counts.get(k, 0)
        P(f"| {k} | {n} | {n / total_steps * 100:.1f}% | {desc[k]} |")
    P(f"| **total** | **{total_steps}** | 100% | |")
    hdr_variants = collections.Counter(w["header"] for w in workflows)
    for hv, n in hdr_variants.items():
        if hv and hv.lower() != "duration":
            P("")
            P(f"NOTE: {n} workflow(s) use a `{hv}`-headed last column (carries "
              f"cadence/latency semantics, not effort) — their cells are excluded.")
    P("")
    # corpus totals
    tot = [sum(w["monthly_hours"][0] for w in workflows),
           sum(w["monthly_hours"][1] for w in workflows)]
    P("## Corpus totals (cadence-denominated effort only)")
    P("")
    P(f"- Derived human effort: **{tot[0]:,.0f}–{tot[1]:,.0f} hours/month** "
      f"(≈ {tot[0]/BUSINESS_DAYS_PER_MONTH/HOURS_PER_WORKDAY:,.0f}–{tot[1]/BUSINESS_DAYS_PER_MONTH/HOURS_PER_WORKDAY:,.0f} FTE "
      f"at 173.6 h/FTE-month)")
    el = [sum(w["elapsed_days"][0] for w in workflows), sum(w["elapsed_days"][1] for w in workflows)]
    P(f"- Elapsed windows: {el[0]:,.0f}–{el[1]:,.0f} person-days reported (not converted)")
    pu = sum(len(w["per_unit_rates"]) for w in workflows)
    P(f"- Per-unit rates held symbolic: {pu}")
    P("")
    P("## Top roles by derived monthly hours")
    P("")
    P("| role | h/month (derived) | effort steps | automated steps |")
    P("|---|---:|---:|---:|")
    for role, (lo, hi, nst, nau) in sorted(role_month.items(), key=lambda kv: -kv[1][1])[:30]:
        P(f"| {role} | {lo:,.0f}–{hi:,.0f} | {nst} | {nau} |")
    P("")
    P("## Top workflows by derived monthly hours")
    P("")
    P("| workflow | h/month | steps (effort/auto/cad-only/qual) |")
    P("|---|---:|---|")
    for w in sorted(workflows, key=lambda w: -w["monthly_hours"][1])[:30]:
        P(f"| {w['id']}. {w['name'][:60]} | {w['monthly_hours'][0]:,.0f}–{w['monthly_hours'][1]:,.0f} | "
          f"{w['effort_steps']}/{w['automated_steps']}/{w['cadence_only_steps']}/{w['qualitative_steps']} |")
    P("")

    unparse = [(w["file"], w["id"], s["step"], s["duration"])
               for w in workflows for s in w["steps"] if s["klass"] == "unparseable"]
    if unparse:
        P(f"## Unparseable cells ({len(unparse)}) — manual triage list")
        P("")
        for f, wid, st, d in unparse[: args.unparseable or 40]:
            P(f"- `{f}` {wid} step {st}: `{d}`")
        if len(unparse) > (args.unparseable or 40):
            P(f"- … and {len(unparse) - (args.unparseable or 40)} more (use --unparseable N)")
        P("")

    report = "\n".join(lines)

    def json_str():
        jd = []
        for w in workflows:
            jd.append({k: (list(v) if isinstance(v, tuple) else v) for k, v in w.items()})
        return json.dumps(jd, indent=1) + "\n"

    def csv_str():
        buf = io.StringIO(newline="")
        wr = csv.writer(buf)
        wr.writerow(["file", "workflow", "role", "monthly_hours_low",
                     "monthly_hours_high", "effort_steps", "automated_steps",
                     "cadence_only_steps", "qualitative_steps",
                     "elapsed_days_low", "elapsed_days_high", "per_unit_rates"])
        # per workflow x role rows
        by_wr = collections.defaultdict(lambda: [0.0, 0.0, 0, 0, 0, 0, 0.0, 0.0, []])
        for w in workflows:
            for s in w["steps"]:
                if s["klass"] in ("effort",) and s.get("monthly"):
                    for role in split_roles(s["role_r"]):
                        cell = by_wr[(w["file"], w["id"], role)]
                        cell[0] += s["monthly"][0]; cell[1] += s["monthly"][1]; cell[2] += 1
                elif s["klass"] == "automated":
                    for role in split_roles(s["role_r"]):
                        by_wr[(w["file"], w["id"], role)][3] += 1
                elif s["klass"] == "cadence-only":
                    for role in split_roles(s["role_r"]):
                        by_wr[(w["file"], w["id"], role)][4] += 1
                elif s["klass"] == "qualitative":
                    for role in split_roles(s["role_r"]):
                        by_wr[(w["file"], w["id"], role)][5] += 1
                elif s["klass"] == "elapsed" and s.get("elapsed_days"):
                    for role in split_roles(s["role_r"]):
                        by_wr[(w["file"], w["id"], role)][6] += s["elapsed_days"][0]
                        by_wr[(w["file"], w["id"], role)][7] += s["elapsed_days"][1]
                elif s["klass"] == "per-unit":
                    for role in split_roles(s["role_r"]):
                        by_wr[(w["file"], w["id"], role)][8].append(
                            f"{s['hours'][0]:.2f}-{s['hours'][1]:.2f}h/{s['unit']}")
        for (f, wid, role), c in sorted(by_wr.items()):
            wr.writerow([f, wid, role, f"{c[0]:.2f}", f"{c[1]:.2f}", c[2], c[3],
                         c[4], c[5], f"{c[6]:.1f}", f"{c[7]:.1f}",
                         "; ".join(c[8])])
        return buf.getvalue()

    def ranking_str():
        # the headcount-optimization priority list: every workflow ranked by
        # derived monthly hours (high desc, then low desc; stable over corpus
        # order on full ties). fte_high = high / (8 h x 21.7 d) — the same
        # 173.6 h/FTE-month convention the report's corpus-total line uses.
        recs = sorted(workflows, key=lambda w: (-w["monthly_hours"][1],
                                                -w["monthly_hours"][0]))
        buf = io.StringIO(newline="")
        wr = csv.writer(buf)
        wr.writerow(["rank", "workflow_id", "title", "process_area", "file",
                     "monthly_hours_low", "monthly_hours_high", "fte_high",
                     "effort_steps", "automated_steps", "cadence_only_steps",
                     "qualitative_steps", "elapsed_days_low",
                     "elapsed_days_high", "per_unit_rates"])
        for i, w in enumerate(recs, 1):
            area = w["file"].split("/")[2]
            wr.writerow([i, w["id"], w["name"], area, w["file"],
                         f"{w['monthly_hours'][0]:.2f}",
                         f"{w['monthly_hours'][1]:.2f}",
                         f"{w['monthly_hours'][1] / (HOURS_PER_WORKDAY * BUSINESS_DAYS_PER_MONTH):.3f}",
                         w["effort_steps"], w["automated_steps"],
                         w["cadence_only_steps"], w["qualitative_steps"],
                         f"{w['elapsed_days'][0]:.1f}",
                         f"{w['elapsed_days'][1]:.1f}",
                         len(w["per_unit_rates"])])
        return buf.getvalue()

    here = os.path.dirname(os.path.abspath(__file__))
    artifacts = [
        ("report", os.path.join(here, "manhours-rollup-report.md"), (report + "\n").encode("utf-8")),
        ("json", os.path.join(here, "manhours-rollup.json"), json_str().encode("utf-8")),
        ("csv", os.path.join(here, "manhours-rollup.csv"), csv_str().encode("utf-8")),
        ("ranking", os.path.join(here, "manhours-workflow-ranking.csv"), ranking_str().encode("utf-8")),
    ]

    if args.check:
        bad = 0
        for name, path, derived in artifacts:
            if not os.path.exists(path):
                print(f"manhours-rollup: {name} missing ({os.path.basename(path)}) "
                      f"— run without --check to generate")
                bad = 1
                continue
            if open(path, "rb").read() == derived:
                print(f"manhours-rollup: {name} byte-identical, OK")
            else:
                print(f"manhours-rollup: {name} DRIFT — regenerate "
                      f"(a Steps-table or grammar change moved the derivation)")
                bad = 1
        sys.exit(bad)

    print(report)
    if args.report:
        open(args.report, "w").write(report + "\n")
        print(f"[written] {args.report}", file=sys.stderr)
    if args.json:
        open(args.json, "w").write(json_str())
        print(f"[written] {args.json}", file=sys.stderr)
    if args.csv:
        with open(args.csv, "w", newline="") as fh:
            fh.write(csv_str())
        print(f"[written] {args.csv}", file=sys.stderr)
    if args.ranking:
        with open(args.ranking, "w", newline="") as fh:
            fh.write(ranking_str())
        print(f"[written] {args.ranking}", file=sys.stderr)

if __name__ == "__main__":
    main()
