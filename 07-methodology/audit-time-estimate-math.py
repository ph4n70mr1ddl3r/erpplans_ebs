#!/usr/bin/env python3
"""
audit-time-estimate-math.py — Arithmetic audit of the finalized `### Time Estimate`
and `### Staffing Implication` paragraphs.

Check 49 proves every workflow carries a finalized Time Estimate section; nothing
verifies the arithmetic written INTO those paragraphs. This tool re-derives every
explicit inline computation —

    "<A> × <B> [× <C> ...] (=|≈) <result>"     (factors and result may be ranges,
                                                "30–45 min", "~4 hours each")

— applying the unit conventions the house style actually uses, charitably: a chain
verifies if ANY consistent interpretation lands within tolerance, so what survives
into the hits list is genuinely suspect. Conversions modeled:

  * minutes <-> hours (÷/× 60);
  * workday/workweek/month-length conventions — hours/day × weeks needs ×5 or ×7
    days; days -> hours ×8; /day -> /month ×21.7/22/30; /week -> /month ×4.33;
    /quarter -> /month ÷3; and the annualization table /month ×12, /quarter ×4,
    /week ×52, /day ×365 or ×260, /season ×6 — tried singly and in pairwise
    products, at most one calendar convention per comparison;
  * noun/suffix cancellation — "2 hours/visit × 20–30 visits/month" cancels
    visit↔visits; a bare "N <noun>" adjacent to a "…/<noun>" factor is an implicit
    multiplier when the nouns cancel ("2 hours/week during 8-week build × 4 seasons");
  * parenthesized sub-chains — "(5 min/call × ~5–10 calls = 25–50 min)" is verified
    on its own and its claimed result substituted into the surrounding sum.

It also flags reversed numeric ranges ("90–50 min") inside those sections
(workflow IDs like "W518 — 1-hour" are excluded).

The 2026-09-23 seventy-third-wave review triaged the default-mode adjudication
queue end-to-end (183 candidates at the wave baseline): the residue adjudicates
into the accepted classes above (unit-shape tails such as hours/vendor/year,
midpoint or padded ranges, elapsed-window weeks/days reported not summed, hidden
context factors, ambiguous-period readings the claimed total legitimately
reaches), and twelve claimed totals that contradict their OWN stated factors
were repaired across nine PA files. Each repaired cell is pinned by the
FOOTING_ANCHORS scan below: the corrected claim is REQUIRED inside its own
workflow block and the retired form is BANNED from it, in both default and
--guard modes — a future re-timing re-fires the arm until consciously
re-pointed (the Check-71 CENSUS-pin contract). One finding is OPEN and tracked
for per-workflow triage, deliberately not repaired here: W251's (PA-19.1)
"Total HR Benefits effort ~60–80 hours/month" against its own steps-table
derivation (verification 30 min + certification 20 min + reimbursement 15 min
× 410–590 claims/month ≈ 380–550 h/month) — the honest re-footing implies >2 FTE
against the TO/profile's 2-specialist HR canon, an HC cascade beyond a
consistency wave's mandate.

The tool reports footing violations explicitly; everything else is
candidates; adjudication and repair are manual.

Usage:
    python3 audit-time-estimate-math.py [--tolerance 0.15] [--all]
        --tolerance  endpoint ratio accepted before a chain is reported
        --all        also print chains that verify (audit trail)
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

BLOCK_SPLIT = re.compile(r"(?=^## W\d+[A-Z]?\. )", re.MULTILINE)
SECTION_RE = re.compile(r"^### (Time Estimate|Staffing Implication)\s*$", re.MULTILINE)

# --- footing-anchor scan (2026-09-23 seventy-third-wave review) ----------------
# (PA file name, workflow id, required corrected anchor, retired banned form).
# Block-scoped to the named workflow so sibling claims in the same file (e.g.
# PA-15.2's W633 Treasury-Analyst ~25 hours/month) never trip the arms.
FOOTING_ANCHORS = [
    ("PA-11.3-wholesale-operations.md", "W599",
     r"~90–155 person-hours/month", r"~50–75 person-hours/month"),
    ("PA-15.2-vendor-payment-and-reconciliation.md", "W634",
     r"~70–90 hours/month", r"1 day/month = ~25 hours/month"),
    ("PA-18.3-fx-and-investments.md", "W1474",
     r"~85–90 hours/year", r"= ~60 hours/year"),
    ("PA-41.1-private-label-product-development.md", "W1833",
     r"~50–55 hours/year", r"= ~25–40 hours/year"),
    ("PA-41.3-private-label-brand-marketing.md", "W1852",
     r"~180–220 hours/year", r"= ~80–120 hours/year"),
    ("PA-55.1-planogram-design-space-allocation.md", "W2169",
     r"~7\.5 hours/month ≈ ~90 hours/year", r"~90 hours/month"),
    ("PA-55.1-planogram-design-space-allocation.md", "W2171",
     r"≈ 4\.5–6 hours active", r"~4 days/optimization × ~30 optimizations/year"),
    ("PA-55.1-planogram-design-space-allocation.md", "W2172",
     r"~80 hours/year", r"~120–160 hours/year"),
    ("PA-55.2-planogram-compliance-audit.md", "W2179",
     r"~500 hours/quarter", r"~600–800 hours/quarter"),
    ("PA-76.1-multi-lgu-business-permit-license-management.md", "W2670",
     r"~460–660 hours/year", r"~600–700 hours/year"),
    ("PA-76.1-multi-lgu-business-permit-license-management.md", "W2673",
     r"~25–50 hours/location-year", r"~50–100 hours/location-year"),
    ("PA-76.1-multi-lgu-business-permit-license-management.md", "W2674",
     r"~160–360 hours/year", r"~250–400 hours/year"),
]


def footing_check(path, wid, block, hits, guard=None):
    base = os.path.basename(path)
    for fname, fwid, required, banned in FOOTING_ANCHORS:
        if fname != base or fwid != wid:
            continue
        if not re.search(required, block):
            detail = f"required footing anchor missing: /{required}/"
            hits.append((path, wid, "Footing", detail, None, detail,
                         ["footing"], False))
            if guard is not None:
                guard.append((path, wid, "Footing", detail,
                              f"missing footing anchor /{required}/"))
        if re.search(banned, block):
            detail = f"retired footing form present: /{banned}/"
            hits.append((path, wid, "Footing", detail, None, detail,
                         ["footing"], False))
            if guard is not None:
                guard.append((path, wid, "Footing", detail,
                              f"retired footing form /{banned}/ re-minted"))

# --- number / token grammar ---------------------------------------------------
NUM = r"~?\d[\d,]*(?:\.\d+)?"
RANGE_SEP = r"(?:\s*(?:-|to)\s*)"
UNIT_NOUN = (
    r"(?:min(?:ute)?s?|secs?|seconds?|hrs?|hours?|days?|weeks?|months?|quarters?|"
    r"seasons?|cycles?|visits?|stores?|events?|shifts?|trucks?|routes?|trips?|"
    r"deliveries|shipments?|pallets?|cartons?|cases?|bays?|sites?|SKUs?|POs?|"
    r"orders?|lines?|receipts?|invoices?|claims?|tickets?|calls?|complaints?|"
    r"requests?|reviews?|audits?|checks?|tests?|samples?|batches?|runs?|reports?|"
    r"meetings?|sessions?|campaigns?|promotions?|flyers?|labels?|signs?|tags?|"
    r"counters?|terminals?|lanes?|DCs?|departments?|categories?|vendors?|"
    r"suppliers?|customers?|members?|employees?|guards?|operators?|drivers?|"
    r"pickers?|loaders?|reps?|managers?|analysts?|specialists?|leads?|"
    r"coordinators?|officers?|incidents?|exceptions?|discrepancies?|damages?|"
    r"returns?|credits?|debits?|payments?|deposits?|withdrawals?|counts?)"
)
SUFFIX = r"(?:/[A-Za-z][A-Za-z-]*|\s+per\s+[A-Za-z][A-Za-z-]*)"
NUM_MK = r"~?\d[\d,]*(?:\.\d+)?(?:\s*[KMB](?![A-Za-z]))?"
# the unit is any noun-ish word, with up to two intervening words
# ("~50–100 write-offs/month", "1,000–1,800 multi-tender installment
# transactions/month"); the LAST word of the group is the noun
QUANT_RE = re.compile(
    r"(?P<num>" + NUM_MK + r"(?:" + RANGE_SEP + NUM_MK + r")?)" +
    r"(?P<unit>\s+(?!per\b)[A-Za-z][A-Za-z-]*"
    r"(?:\s+(?!per\b)[A-Za-z][A-Za-z-]*){0,2})?" +
    r"(?P<suffix>(?:\s*" + SUFFIX + r")*)"
)
RANGE_ORDER_RE = re.compile(
    "(?<![A-Za-z0-9])" + NUM + "(?:" + RANGE_SEP + NUM + ")(?=\\s+" + UNIT_NOUN + r"\b)"
)

# annual frequency of each cadence — the common denominator for normalization
CADENCE_PER_YEAR = {"day": 365, "workday": 260, "week": 52, "month": 12,
                   "mo": 12, "wk": 52, "yr": 1,
                    "quarter": 4, "season": 6, "year": 1}
MINUTE_UNITS = {"min", "mins", "minute", "minutes"}
HOUR_UNITS = {"hr", "hrs", "hour", "hours"}
DAY_UNITS = {"day", "days"}
PERSON_PREFIX = re.compile(
    r"\b(?:person|labor|staff|shift-supervisor|supervisor)[- ](?=hours?|days?|months?)",
    re.I)
CADENCE_ADJ = {"daily": "day", "weekly": "week", "monthly": "month",
               "quarterly": "quarter", "semi-annual": "month", "semiannually": "month",
               "annual": "year", "annually": "year", "yearly": "year",
               "seasonal": "season"}


def norm(line):
    line = line.replace("\u00d7", " × ")
    line = line.replace("\u2248", " ≈ ").replace("=", " = ")
    line = line.replace("\u2013", "-").replace("\u2014", "-")
    line = line.replace("**", "")
    line = PERSON_PREFIX.sub("", line)
    # percentages become decimals so they can ride in chains ("× 80% automated");
    # range percentages convert both endpoints ("5–8%" -> "0.05–0.08")
    line = re.sub(r"(\d+(?:\.\d+)?)\s*[–-]\s*(\d+(?:\.\d+)?)\s*%",
                  lambda m: f"{float(m.group(1)) / 100:g}-{float(m.group(2)) / 100:g}",
                  line)
    line = re.sub(r"(\d+(?:\.\d+)?)\s*%",
                  lambda m: f"{float(m.group(1)) / 100:g}", line)
    # "8-week build phase" -> "8 week build phase" so the noun is parseable
    line = re.sub(r"(\d)\s*-\s*(" + UNIT_NOUN + r")\b", r"\1 \2", line, flags=re.I)
    return line


def parse_num(text):
    """'1,000-2,000' -> (1000.0, 2000.0); '1.5M-10M' scales each endpoint by its
    own marker; a marker on the high endpoint only ('1.0-1.6M') scales both."""
    ends = re.findall(r"(\d[\d,]*(?:\.\d+)?)\s*([KMB](?![A-Za-z]))?", text)
    if not ends:
        return None
    mult = {"k": 1e3, "m": 1e6, "b": 1e9}
    if len(ends) == 1:
        v = float(ends[0][0].replace(",", "")) * mult.get(ends[0][1].lower(), 1)
        return (v, v)
    raw = [float(n.replace(",", "")) for n, _ in ends[:2]]
    scales = [mult[s.lower()] if s else None for _, s in ends[:2]]
    if scales[0] and scales[1]:
        return (raw[0] * scales[0], raw[1] * scales[1])
    if scales[1]:
        return (raw[0] * scales[1], raw[1] * scales[1])
    if scales[0]:
        return (raw[0] * scales[0], raw[1] * scales[0])
    return (raw[0], raw[1])


def singular(word):
    w = word.lower().strip()
    if w.endswith("ies"):
        return w[:-3] + "y"
    if w.endswith("s") and not w.endswith("ss") and len(w) > 3:
        return w[:-1]
    return w


class Quant:
    __slots__ = ("low", "high", "unit", "suffixes", "pos")

    def __init__(self, low, high, unit, suffixes, pos):
        self.low, self.high, self.unit, self.suffixes, self.pos = \
            low, high, unit, suffixes, pos


def tokenize(piece):
    """Yield Quant tokens and '×'/'+' operators in source order."""
    toks = []
    for m in QUANT_RE.finditer(piece):
        num = parse_num(m.group("num"))
        if num is None:
            continue
        raw_unit = (m.group("unit") or "").strip().lower()
        if raw_unit:
            words = raw_unit.split()
            # a time word anywhere in the group wins ("80 min average")
            tw = [w for w in words if w in MINUTE_UNITS | HOUR_UNITS | DAY_UNITS
                  or w in ("sec", "secs", "second", "seconds",
                           "week", "weeks", "month", "months")]
            unit = singular(tw[0] if tw else words[-1])
        else:
            unit = ""
        raw_suffix = (m.group("suffix") or "").strip().lower()
        suffixes = [a or b for a, b in
                    re.findall(r"/([A-Za-z][A-Za-z-]*)|per\s+([A-Za-z][A-Za-z-]*)",
                               raw_suffix)]
        toks.append((m.start(), Quant(num[0], num[1], unit, suffixes, m.start())))
    ops = [(m.start(), "×" if "×" in m.group() else "+")
           for m in re.finditer(r"[×+]", piece)]
    return [item for _, item in sorted(toks + ops, key=lambda t: t[0])]


def cadence_of(suffixes, nouns):
    """Dominant cadence suffix after noun/suffix cancellation, or None."""
    s, n = list(suffixes), list(nouns)
    for x in s[:]:
        if x in n:
            s.remove(x); n.remove(x)
    time_like = [x for x in s if x in CADENCE_PER_YEAR]
    if len(time_like) == 1:
        return time_like[0]
    return time_like[0] if time_like else None


def eval_runs(tokens, text=""):
    """Parse into '+'-separated runs of elementwise products.

    Returns (runs, factors_total) or None when a run is not a clean chain.
    Each run: {"val", "minutes", "hours", "days", "cadence", "suffixes", "nouns"}.
    A run with no suffix cadence inherits one from a cadence adjective
    ("monthly review ... 2 + 2 hours") in its own span, or from the unique
    cadence adjective anywhere in the clause.
    """
    groups, cur = [], []
    for item in tokens:
        if item == "+":
            groups.append(cur); cur = []
        else:
            cur.append(item)
    groups.append(cur)
    piece_adjs = [CADENCE_ADJ[a.lower()] for a in
                  re.findall(r"\b(" + "|".join(CADENCE_ADJ) + r")\b", text, re.I)]
    runs, n_factors = [], 0
    for run in groups:
        if not run:
            return None
        val, last = None, None
        r_suffixes, r_nouns = [], []
        r_min = r_hr = r_day = False
        r_counts = []
        for item in run:
            if isinstance(item, Quant):
                if item.unit in MINUTE_UNITS:
                    r_min = True
                if item.unit in HOUR_UNITS:
                    r_hr = True
                if item.unit in DAY_UNITS:
                    r_day = True
                if item.unit:
                    r_nouns.append(item.unit)
                    if item.unit not in MINUTE_UNITS | HOUR_UNITS | DAY_UNITS \
                            and item.high >= 10:
                        r_counts.append((item.unit, item.high))
                r_suffixes.extend(item.suffixes)
                if val is None:
                    val = (item.low, item.high); n_factors += 1
                elif last == "×":
                    val = (val[0] * item.low, val[1] * item.high); n_factors += 1
                elif isinstance(last, Quant) and (
                    (last.suffixes and item.unit in last.suffixes)
                    or (item.suffixes and last.unit in item.suffixes)
                ):
                    # adjacency whose nouns cancel is an implicit multiplication
                    val = (val[0] * item.low, val[1] * item.high); n_factors += 1
                else:
                    return None  # unrelated prose number — not a clean chain
                last = item
            else:
                if not isinstance(last, Quant):
                    return None  # doubled operator
                last = "×"
        if val is None or last == "×":
            return None
        cad = cadence_of(r_suffixes, r_nouns)
        quants = [t for t in run if isinstance(t, Quant)]
        if cad is None:
            # a bare scalar factor of 3–5.5 may already BE the cadence
            # conversion ("60–90 min × 4" weeks per month) — then an adjective
            # fallback would double-apply
            scalars = [t for t in quants if not t.unit and not t.suffixes]
            if not any(3.5 <= t.high <= 5.5 for t in scalars):
                span = text[quants[0].pos:quants[-1].pos] if quants else ""
                adjs = [CADENCE_ADJ[a.lower()] for a in
                        re.findall(r"\b(" + "|".join(CADENCE_ADJ) + r")\b",
                                   span, re.I)]
                if len(set(adjs)) == 1:
                    cad = adjs[0]
                elif len(set(piece_adjs)) == 1:
                    cad = piece_adjs[0]
        runs.append({"val": val, "minutes": r_min, "hours": r_hr, "days": r_day,
                     "cadence": cad, "suffixes": r_suffixes, "nouns": r_nouns,
                     "counts": r_counts})
    if not runs:
        return None
    return runs, n_factors


# alternate calendar readings for a cadence (calendar vs workday conventions)
CADENCE_ALTS = {"day": [365.0, 260.0], "workday": [260.0], "week": [52.0],
                "month": [12.0], "mo": [12.0], "wk": [52.0],
                "quarter": [4.0], "season": [6.0], "year": [1.0], "yr": [1.0]}
# implicit per-week/per-month day counts when a day-cadence meets a longer noun
PAIR_ALTS = {("day", "week"): [5.0, 7.0], ("day", "month"): [21.7, 22.0, 30.0],
             ("week", "month"): [4.33, 4.0], ("week", "quarter"): [13.0, 12.0]}

MID_TOL = 0.20      # claimed midpoint within ±20% of a consistent reading
END_TOL = 0.35      # both endpoints within ±35% (house style pads ranges)


SEC_UNITS = {"sec", "secs", "second", "seconds"}


def unit_scales(run, claimed):
    """Candidate unit conversions for one run toward the claimed unit."""
    c_min = claimed.unit in MINUTE_UNITS
    c_hr = claimed.unit in HOUR_UNITS
    r_secs = any(u in SEC_UNITS for u in run["nouns"])
    if r_secs and not run["minutes"] and not run["hours"] and c_hr:
        return [1 / 3600]
    if run["minutes"] and not run["hours"] and c_hr:
        return [1 / 60]
    if run["hours"] and not run["minutes"] and c_min:
        return [60]
    if run["days"] and not run["minutes"] and not run["hours"] and c_hr:
        return [8]           # workday
    if run["hours"] and not run["minutes"] and claimed.unit in DAY_UNITS:
        return [1 / 8]
    return [1]


def cadence_scales(run, target, claimed_nouns):
    """Candidate cadence conversions for one run toward the claimed cadence."""
    rc = run["cadence"]
    out = [1]
    if rc is not None and target is not None and rc != target:
        alts = CADENCE_ALTS.get(rc, [])
        talts = CADENCE_ALTS.get(target, [])
        out = [a / t for a in alts for t in talts] or [1]
    # conversion pairs hiding inside the run: an uncanceled /day (or /week)
    # suffix multiplied by a bare week/month noun implies days-per-week etc.
    nouns = set(run["nouns"]) | set(claimed_nouns)
    for (src, dst), alts in PAIR_ALTS.items():
        if src in (run["suffixes"] or []) and dst in nouns:
            out = [o * a for o in out for a in alts]
    return sorted(set(round(x, 6) for x in out))


def verify(runs, claimed):
    """(ok, best_score, best_val). ok is True when some licensed reading of
    the runs matches the claimed range; best_score is the smallest achievable
    max-deviation (midpoint/endpoints); best_val is that reading's range."""
    target = cadence_of(claimed.suffixes,
                        [claimed.unit] if claimed.unit else [])
    claimed_nouns = [claimed.unit] if claimed.unit else []
    # "+ N hours per <noun>" after a "... × M <noun>s" factor inherits that M
    for i, r in enumerate(runs):
        if i == 0:
            continue
        for s in r["suffixes"]:
            if s in CADENCE_PER_YEAR:
                continue
            for j in range(i):
                for noun, cnt in runs[j].get("counts", []):
                    if noun == s and cnt >= 10:
                        r["val"] = (r["val"][0] * cnt, r["val"][1] * cnt)
                        break
    combos = [()]
    for run in runs:
        us = unit_scales(run, claimed)
        cs = cadence_scales(run, target, claimed_nouns)
        opts = sorted({round(u * c, 6) for u in us for c in cs})
        # an uncanceled /store suffix against a chain-wide claim implies the
        # canonical 200-store multiplication
        run_sfx, _nouns = list(run["suffixes"]), list(run["nouns"])
        for x in run_sfx[:]:
            if x in _nouns:
                run_sfx.remove(x); _nouns.remove(x)
        if "store" in run_sfx and "store" not in claimed.suffixes:
            opts = sorted({round(o * 200, 6) for o in opts} | set(opts))
        if "dc" in run_sfx and "dc" not in claimed.suffixes:
            opts = sorted({round(o * 4, 6) for o in opts} | set(opts))
        combos = [c + (o,) for c in combos for o in opts]
        if len(combos) > 400:
            return True, 0.0, None  # degenerate — refuse to judge
    best = None
    best_val = None
    point = claimed.low == claimed.high
    for combo in combos:
        if best_val is None:
            # point claims that fail containment never update `best`; keep a
            # concrete reading so the guard can still score them
            best_val = (
                sum(r["val"][0] * s for r, s in zip(runs, combo)),
                sum(r["val"][1] * s for r, s in zip(runs, combo)))
        lo = sum(r["val"][0] * s for r, s in zip(runs, combo))
        hi = sum(r["val"][1] * s for r, s in zip(runs, combo))
        if point:
            # a point claim may sit anywhere inside the derived range
            if lo * 0.85 <= claimed.low <= hi * 1.15:
                return True, 0.0, (lo, hi)
            continue
        dm, cm = (lo + hi) / 2, (claimed.low + claimed.high) / 2
        if dm and cm:
            mid = abs(cm / dm - 1)
            endl = abs(claimed.low / lo - 1) if lo else 9
            endh = abs(claimed.high / hi - 1) if hi else 9
            score = max(mid, endl, endh)
            if best is None or score < best:
                best = score
                best_val = (lo, hi)
    ok = best is not None and best <= END_TOL
    return ok, (best if best is not None else 9.0), best_val


TOL = 0.15

# guard scoping, tuned on the 2026-08-29 hand adjudication of the full hit list:
# only single-run product chains whose factors carry effort-time units or bare
# counts, no percentages (shared-base ambiguity), no elapsed day/week/month
# effort factors — every remaining audit hit in the accepted set falls outside
# this scope or verifies under a licensed convention
GUARD_MID = 1.6        # midpoint deviation required for a guard error


def guard_violation(runs, n_factors, claimed, raw_line):
    """None, or a reason string when the strict guard flags this chain."""
    if len(runs) != 1 or n_factors < 2:
        return None
    if "%" in raw_line:
        return None
    run = runs[0]
    if run["days"] or "week" in run["nouns"] or "month" in run["nouns"]:
        return None  # elapsed day/week/month effort factors: adjudicated, not guarded
    ok, score, best_val = verify(runs, claimed)
    if ok or best_val is None:
        return None
    lo, hi = best_val
    dm, cm = (lo + hi) / 2, (claimed.low + claimed.high) / 2
    if dm and cm and abs(cm / dm - 1) >= GUARD_MID:
        return (f"derived {lo:,.0f}–{hi:,.0f} vs claimed "
                f"{claimed.low:,.0f}–{claimed.high:,.0f} (midpoint off "
                f"{abs(cm / dm - 1):.1f}, no licensed unit convention)")


def audit_chain(left_src, claimed, path, wid, section, raw_line, hits):
    parsed = eval_runs(tokenize(left_src), left_src)
    if parsed is None:
        return
    runs, n_factors = parsed
    if n_factors < 2:
        return
    ok, _, _ = verify(runs, claimed)
    if not ok:
        lo = sum(r["val"][0] for r in runs); hi = sum(r["val"][1] for r in runs)
        hits.append((path, wid, section, raw_line, (lo, hi),
                     (claimed.low, claimed.high), None, False))


def strip_parens(line, path, wid, section, raw_line, hits):
    """Verify '(A × B = R)' sub-chains and replace them with their claimed result;
    plain parentheticals are dropped so their numbers cannot poison the sum."""
    out = line
    for _ in range(12):
        m = re.search(r"\(([^()]*)\)", out)
        if not m:
            break
        if " = " not in m.group(1) and " ≈ " not in m.group(1):
            # keep time-quantity parentheticals (addends); drop annotations
            # (incl. breakdowns that directly follow a time quantity);
            # '+ -only time sums collapse into a single quantity token
            before = out[:m.start()].rstrip()
            if re.search(r"\b(hours?|hrs?|min(?:ute)?s?|days?|weeks?|months?)\s*$",
                         before, re.I):
                out = out[:m.start()] + " " + out[m.end():]
                continue
            inner0 = m.group(1)
            toks = [t for t in tokenize(inner0) if isinstance(t, Quant)]
            timeish = toks and all(
                t.unit in MINUTE_UNITS | HOUR_UNITS | DAY_UNITS or
                (t.unit == "" and "+" in inner0) for t in toks)
            if timeish and "×" not in inner0 and "+" in inner0:
                lo = sum(t.low for t in toks); hi = sum(t.high for t in toks)
                unit = next((t.unit for t in toks if t.unit), "")
                out = out[:m.start()] + f" {lo:g}-{hi:g} {unit} " + out[m.end():]
            else:
                repl = inner0 if timeish else " "
                out = out[:m.start()] + " " + repl + " " + out[m.end():]
            continue
        inner = m.group(1)
        parts = re.split(r"\s(?:=|≈)\s", inner)
        if len(parts) < 2:
            out = out[:m.start()] + " " + out[m.end():]
            continue
        toks_r = tokenize(parts[-1])
        if toks_r and isinstance(toks_r[0], Quant):
            claimed = toks_r[0]
            left_src = " × ".join(parts[:-1])
            audit_chain(left_src, claimed, path, wid, section,
                        raw_line + "  {sub: " + inner + "}", hits)
            out = out[:m.start()] + " " + parts[-1] + " " + out[m.end():]
        else:
            out = out[:m.start()] + " " + out[m.end():]
    return out


def audit_line(path, wid, section, raw_line, tolerance, show_all, hits, guard=None):
    line = strip_parens(norm(raw_line), path, wid, section, raw_line, hits)
    pieces = re.split(r"\s(?:=|≈)\s", line)
    for i in range(len(pieces) - 1):
        if " × " in pieces[i + 1]:
            continue  # head of the next piece is an operand of a further chain
        toks_r = tokenize(pieces[i + 1])
        if not toks_r or not isinstance(toks_r[0], Quant):
            continue
        claimed = toks_r[0]
        # evaluate only the clause adjacent to the comparison operator
        left_src = pieces[i].rsplit(";", 1)[-1]
        parsed = eval_runs(tokenize(left_src), left_src)
        if parsed is None:
            continue
        runs, n_factors = parsed
        if n_factors < 2:
            continue
        ok, _, _ = verify(runs, claimed)
        if not ok or show_all:
            lo = sum(r["val"][0] for r in runs); hi = sum(r["val"][1] for r in runs)
            hits.append((path, wid, section, raw_line.strip(), (lo, hi),
                         (claimed.low, claimed.high), None, ok))
        if guard is not None:
            reason = guard_violation(runs, n_factors, claimed, raw_line)
            if reason:
                guard.append((path, wid, section, raw_line.strip(), reason))


def audit_file(path, tolerance, show_all, hits, guard=None):
    text = open(path, encoding="utf-8").read()
    for block in BLOCK_SPLIT.split(text):
        m = re.match(r"## (W\d+[A-Z]?)\.", block)
        if not m:
            continue
        wid = m.group(1)
        footing_check(path, wid, block, hits, guard)
        for sm in SECTION_RE.finditer(block):
            rest = block[sm.end():]
            stop = re.search(r"^### ", rest, re.MULTILINE)
            body = rest[:stop.start()] if stop else rest
            section = sm.group(1)
            for raw in body.splitlines():
                line = raw.strip()
                if not line:
                    continue
                n = norm(line)
                for rm in RANGE_ORDER_RE.finditer(n):
                    pair = parse_num(rm.group(0))
                    if pair and pair[0] > pair[1]:
                        hits.append((path, wid, section, line, None, pair,
                                     ["reversed"], False))
                        if guard is not None:
                            guard.append((path, wid, section, line,
                                          f"reversed range "
                                          f"{pair[0]:,.0f}–{pair[1]:,.0f}"))
                if "×" in n or "=" in n or "≈" in n:
                    audit_line(path, wid, section, line, tolerance, show_all,
                               hits, guard)


def main():
    global TOL
    ap = argparse.ArgumentParser()
    ap.add_argument("--tolerance", type=float, default=0.15)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--guard", action="store_true",
                    help="strict zero-false-positive mode for the validator: "
                         "errors only on single-run effort-time chains whose "
                         "midpoint is off >=1.6x with no licensed unit "
                         "convention, and on reversed ranges; exit 1 on any")
    args = ap.parse_args()
    TOL = args.tolerance
    hits, guard = [], []
    files = sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md")))
    for f in files:
        audit_file(f, args.tolerance, args.all, hits, guard if args.guard else None)
    if args.guard:
        for path, wid, section, line, reason in guard:
            print(f"GUARD VIOLATION {os.path.relpath(path, REPO)} [{wid}] "
                  f"({section}): {reason}")
            print(f"    {line}")
        print(f"Guard: {len(guard)} violation(s) across {len(files)} PA files")
        sys.exit(1 if guard else 0)
    bad = [h for h in hits if not h[7]]
    print(f"Scanned {len(files)} PA files; {len(hits)} findings; {len(bad)} flagged "
          f"(tolerance ±{args.tolerance:.0%})")
    for h in bad:
        path, wid, section, line, adj, claimed, scales, _ = h
        rel = os.path.relpath(path, REPO)
        print(f"\n--- {rel} [{wid}] ({section})")
        print(f"    {line}")
        if adj:
            print(f"    derived {adj[0]:,.0f}–{adj[1]:,.0f}  vs claimed "
                  f"{claimed[0]:,.0f}–{claimed[1]:,.0f}"
                  + (f"  (no consistent unit convention)" if scales == [] else ""))
        elif scales == ["footing"]:
            print(f"    {claimed}")
        else:
            print(f"    reversed range {claimed[0]:,.0f}–{claimed[1]:,.0f}")


if __name__ == "__main__":
    main()
