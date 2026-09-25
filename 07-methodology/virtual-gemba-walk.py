#!/usr/bin/env python3
"""
virtual-gemba-walk.py — virtual gemba walk & time-and-motion analyzer.

2026-09-16 (thirty-ninth-wave direction): "can we do a virtual gemba walk and a
virtual time and motion analysis so that we can check if the org structure and
headcount is optimal?" This tool is the read-only analyzer that answers it from
the corpus's own measurements — no corpus text is written by this script.

Two modes:

  walk    — walk every value stream's process chain the way a gemba walk walks
            a floor: for each VS, touch time per event (sum of human step
            durations), automated-step share, handoff density (adjacent-step
            Role (R) changes), approval-gate density (Role (A) ≠ '—'), distinct
            executing roles, and the busiest role→role handoff paths corpus-wide
            (the "motion" paths of the operation).

  motion  — time-and-motion against the org of record: per-role annual demand
            hours (step-duration share × annual events, events derived from the
            Frequency fields via a documented cadence ladder) vs chartered
            capacity (TO §5.3 register HC for HQ; §7.2/§7.3 roster complements
            ×200 stores / ×4 DCs for the field), with utilization bands.

Measurement assumptions (printed with every run):
  * step durations: '5min'/'5–10min' → midpoint minutes; 'Automated'/'—' → 0.
  * compound Role (R) cells: the step's duration is split evenly among the
    named roles (shared accountability, split capacity cost).
  * events/year cadence ladder: explicit 'N–M per <unit> per <period>' /
    'N–M ... per <period>' phrases first; bare 'Daily/Weekly/Monthly/Quarterly/
    Annual' mapped to 365 store-days (store-executed steps), 250 workdays
    (HQ/DC) × the unit's store/DC multiplier (200 / 4 / 1); unparseable
    frequencies are excluded from annualized figures and reported as coverage.
  * compound Frequencies of the calibration-era shape 'chain-wide N–M per
    period (n–m per store per period)' parse at the per-store parenthetical:
    the ladder's phrase bridges never cross parentheses ('[^.;()]*?'), so a
    chain-wide count is never multiplied by the store/DC scale (2026-09-23
    paren-blocking fix — W2201's '~1,800–2,400 drops/month (2–3 per store
    per week)' bridged across the parenthesis and read ~840x high, which is
    what showed receiving clerks at ~1,300% demand in the post-calibration
    time-and-motion re-run).
  * capacity: 1,800 net productive hours/FTE/year (HQ knowledge work) and
    1,900 (field shift roles) after PH holidays/leave — tool assumptions for
    decision support, not payroll actuals.
  * duration cells carrying an explicit period qualifier ('30 min/month',
    '2 hours/week', '8-12 h/month') mark regional/periodic steps: annual
    demand = duration x 12/52/4/1, NOT duration x the workflow's store-event
    count (fifty-sixth-wave store-scope review — the per-store ladder was
    multiplying such steps by store-day events).
  * demand keys fold onto their bucket-preferred capacity entry (exact form,
    then singular/plural variants) — the store and DC rosters carry same-noun
    titles ('Receiving Clerks'), and without bucket preference store
    receiving demand priced against the DC roster.
  * the wave-31 contract applies when reading narrow-title utilization:
    specialist/deputy titles are legitimately exercised through their
    department's broader titles, so a narrow title reading hot is a workload
    signal for its department, not a payroll defect.

Read-only: exits 0 on success; exits 1 with a diagnostic if the canonical
populations it asserts (5,433 workflows / HQ 532 / stores 5,800 / DCs 600 — HQ re-based 2026-09-18 actual-org gap-fill, workflow canon re-pointed 5,430 → 5,432 at the 2026-09-21 batch-26 gap fill) do
not hold, so a corpus that has moved invalidates the analysis loudly.
"""

import os
import re
import sys
import collections
import importlib.util
import statistics

TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(TOOL_DIR)
WF = os.path.join(REPO, "01-model-company", "workflows")
TO = os.path.join(REPO, "01-model-company", "optimal-table-of-organization.md")

CANON_WORKFLOWS = 5433
CANON_HQ_HC = 532
CANON_STORE_HC = 5800          # 200 stores x 29
CANON_DC_HC = 600              # 4 DCs x 150
HQ_NET_HOURS = 1800            # net productive hours/FTE/year (assumption)
FIELD_NET_HOURS = 1900         # field shift roles (assumption)
STORES, DCS = 200, 4


GRC_SPLIT_RE = None


def load_grc():
    """Import generate-role-coverage.py for its TO parse + role resolver."""
    global GRC_SPLIT_RE
    spec = importlib.util.spec_from_file_location(
        "grc", os.path.join(TOOL_DIR, "generate-role-coverage.py"))
    grc = importlib.util.module_from_spec(spec)
    sys.argv = ["generate-role-coverage.py"]
    spec.loader.exec_module(grc)
    GRC_SPLIT_RE = grc.SPLIT_RE
    return grc


# ---------------------------------------------------------------- parsing ---

def parse_workflows():
    """(id, vs, title, owner, r_roles, a_roles, steps[(dur_min, r, a)], freq_raw, exec_bucket)"""
    out = []
    for vd in sorted(d for d in os.listdir(WF) if d.startswith("VS-")):
        vs = int(re.match(r"VS-(\d+)", vd).group(1))
        for fn in sorted(f for f in os.listdir(os.path.join(WF, vd))
                         if f.startswith("PA-") and f.endswith(".md")):
            text = open(os.path.join(WF, vd, fn), encoding="utf-8").read()
            parts = re.split(r"^## (W\d+[A-Z]?)\. (.+)$", text, flags=re.M)
            for i in range(1, len(parts) - 2, 3):
                wid, title, body = parts[i], parts[i + 1], parts[i + 2]
                m = re.search(r"\| \*\*Owner\*\* \|(.*?)\|", body)
                owner = m.group(1).strip() if m else ""
                m = re.search(r"\| \*\*Frequency\*\* \|(.*?)\|", body)
                freq = m.group(1).strip() if m else ""
                steps, in_steps = [], False
                for ln in body.splitlines():
                    if re.match(r"^\|\s*#\s*\|", ln) and "Role (R)" in ln:
                        in_steps = True
                        continue
                    if in_steps:
                        if not ln.startswith("|"):
                            in_steps = False
                            continue
                        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
                        if len(cells) < 5 or set(cells[0]) <= set("- "):
                            continue
                        steps.append((parse_minutes(cells[4] if len(cells) > 4 else ""),
                                      cells[2].strip(), cells[3].strip()))
                out.append({"id": wid, "vs": vs, "title": title.strip(), "owner": owner,
                            "freq": freq, "steps": steps})
    return out


def parse_minutes(cell):
    """'5min'/'5–10min'/'2h'/'1.5 hours' → midpoint minutes; Automated/—/'' → 0."""
    c = cell.strip().strip("*").lower()
    if not c or c in {"—", "-", "automated", "n/a", "system"}:
        return 0.0
    m = re.search(r"(\d+(?:\.\d+)?)(?:\s*[–-]\s*(\d+(?:\.\d+)?))?\s*(min|hour|hr|h)\b", c)
    if not m:
        return 0.0
    lo = float(m.group(1))
    hi = float(m.group(2)) if m.group(2) else lo
    mid = (lo + hi) / 2
    return mid * 60 if m.group(3).startswith(("h", "h")) else mid


PERIOD_DAYS = {"day": 1, "week": 7, "month": 30, "quarter": 91, "year": 365}
PERIOD_MULT = {"day": 365, "week": 52, "month": 12, "quarter": 4, "year": 1}
WORKDAYS = {"day": 250, "week": 50, "month": 12, "quarter": 4, "year": 1}


PERIOD_QUALIFIER = re.compile(r"(?:/|per\s+)\s*(month|week|year|quarter)\b", re.I)
PERIOD_MULT_Q = {"month": 12.0, "week": 52.0, "quarter": 4.0, "year": 1.0}


def step_period_qualifier(cell):
    """Duration cells carrying an explicit period qualifier ('30 min/month',
    '2 hours/week', '8-12 h/month chain-wide') mark REGIONAL/PERIODIC steps:
    the step runs N times per period chain-wide (or per region), NOT once per
    workflow event. Fifty-sixth-wave store-scope review: the per-store ladder
    was multiplying such steps by the workflow's store-day events (W69's
    monthly 30-min regional price-audit review read as 30 min x 73,000
    store-events/yr). Returns the annual multiplier (12/52/4/1) or None."""
    m = PERIOD_QUALIFIER.search(cell or "")
    if not m:
        return None
    return PERIOD_MULT_Q[m.group(1).lower()]


def events_per_year(freq, field_exec):
    """Documented cadence ladder -> (events/year or None, rule).

    1. explicit 'N(-M) <units> per store|DC per <period>'  -> x STORES/DCS
    2. explicit 'N(-M) <units> per <period>' (chain scope)  -> as stated
    3. bare cadence word (Daily/Weekly/Monthly/Quarterly/Annual)
       - store-executed steps: daily=365xSTORES? No: a store-executed bare
         'Daily' workflow is a per-store daily event -> STORES x 365 is only
         right when the step is performed per store; the corpus's convention
         is that bare 'Daily' on a store-executed workflow means per store,
         so events/yr = 365 x STORES only for per-store steps. We cannot see
         'per store' here, so we take the corpus's own default: store-scoped
         cadence counts once per store per period (x STORES), HQ/DC scoped
         once per period at workday counts.
    Returns (events/year, rule-tag) — None events = excluded from annualized
    figures (reported as coverage).
    """
    f = freq.strip()
    if not f:
        return None, "no-frequency"
    low = f.lower()
    period_re = r"(day|week|month|quarter|year)"

    # 0. standing-coverage house forms (no digits, no bare cadence word): the
    #    work is per-workday coverage (system/platform monitoring, register
    #    maintenance), not a per-event count -> HQ/DC once per workday, store
    #    once per trading day (xSTORES). 'Continuous + periodic review' etc.
    #    with a bare cadence word fall through to rule 3 unchanged; genuinely
    #    event-driven forms ('Per case', 'Event-driven') are NOT matched here —
    #    they need measured volumes, not a synthetic cadence.
    if re.search(r"\b(continuous|ongoing|maintained|always[- ]on)\b", low) \
            and not re.search(r"\b(daily|weekly|monthly|quarterly|annual|yearly)\b", low) \
            and not re.search(r"\d", low):
        if field_exec == "store":
            return float(STORES * 365), "continuous-xSTORES"
        return float(WORKDAYS["day"]), "continuous-workdays"  # 250 workdays x 1/day

    def midpoint(lo_s, hi_s=None):
        lo = float(lo_s.replace(",", ""))
        hi = float(hi_s.replace(",", "")) if hi_s else lo
        return (lo + hi) / 2

    # 1. 'N-M ... per store per period' / 'per dc per period'. The bridges are
    #    paren-blocked ('[^.;()]*?'): in a compound Frequency of the
    #    calibration-era shape 'chain-wide N–M per period (n–m per store per
    #    period)' the chain-wide count must never bridge across '(' into the
    #    per-store tail (the 2026-09-23 fix — that bridge read W2201 ~840x
    #    high: 1,800–2,400 drops/month x 52 weeks x 200 stores instead of the
    #    parenthetical 2–3 per store per week the two clauses agree on).
    m = re.search(r"(\d[\d,]*)\s*[–-]\s*(\d[\d,]*)\s*[^.;()]*?per\s+(store|dc|stores|dcs)\s+per\s+" + period_re, low)
    if not m:
        m = re.search(r"(\d[\d,]*)\s*[^.;()]*?per\s+(store|dc|stores|dcs)\s+per\s+" + period_re, low)
        if m:
            g = m.groups()
            m = (g[0], None, g[1], g[2]) and m
    if m:
        g = m.groups()
        lo, hi, scope, period = g[0], g[1] if len(g) > 3 else None, g[-2], g[-1]
        per = midpoint(lo, hi if len(g) > 3 else None)
        scale = STORES if scope.startswith("store") else DCS
        return per * PERIOD_MULT[period] * scale, f"explicit-per-{scope}-{period}"

    # 2. 'N-M ... per period' (chain scope as stated) — paren-blocked bridges
    #    for the same reason as rule 1 (a '(...)' tail must not be crossed).
    m = re.search(r"(\d[\d,]*)\s*[–-]\s*(\d[\d,]*)\s*[^.;()]*?per\s+" + period_re, low) or \
        re.search(r"(\d[\d,]*)\s*[^.;()]*?per\s+" + period_re, low)
    if m:
        g = m.groups()
        per = midpoint(g[0], g[1] if len(g) > 2 else None)
        period = g[-1]
        return per * PERIOD_MULT[period], f"explicit-{period}"

    # 3. bare cadence words
    for word, period in (("daily", "day"), ("weekly", "week"), ("monthly", "month"),
                         ("quarterly", "quarter"), ("annual", "year"), ("yearly", "year")):
        if re.search(r"\b" + word, low):
            if field_exec == "store":
                events = float(STORES * PERIOD_MULT[period])
                return events, f"bare-{period}-xSTORES"
            events = float(WORKDAYS[period])
            return events, f"bare-{period}"

    # 4. 'N-M [/unit words] / period' slash form — including the calibration-era
    #    house shape '~13,000–15,000 transactions/month chain-wide (...)' where a
    #    unit word sits between the range and the slash (the 2026-09-25 (bd)
    #    extension: the bare 'N-M / period' form missed every v4.7-calibrated row).
    m = re.search(r"(\d[\d,]*)\s*[–-]\s*(\d[\d,]*)\s*[^.;()/]*?/\s*" + period_re, low) or \
        re.search(r"(\d[\d,]*)\s*[^.;()/]*?/\s*" + period_re, low)
    if m:
        g = m.groups()
        per = midpoint(g[0], g[1] if len(g) == 3 else None)
        return per * PERIOD_MULT[g[-1]], "slash-period"
    return None, "unparseable"


# --------------------------------------------------------- org of record ---

def parse_register(grc):
    """role-display-title → (HC, bucket). HQ from §5.3; field from roster canon."""
    hc = {}
    unmapped_rows = []
    in53 = False
    for line in open(TO, encoding="utf-8"):
        if line.startswith("### 5.3"):
            in53 = True
            continue
        if in53 and line.startswith("## "):
            break
        if in53:
            m = re.match(r"^\| ([^|]+?) \| (\d[\d,]*) \|", line)
            if m:
                title, n = m.group(1).strip(), int(m.group(2).replace(",", ""))
                t = re.sub(r"\s*\([^)]*\)", "", title).strip()
                if t in ("Role", "Reports-to") or set(title) <= set("- "):
                    continue
                if title.startswith("**") or "Total" in title:
                    continue
                if t in hc:
                    hc[t] = (hc[t][0] + n, "hq")
                else:
                    hc[t] = (n, "hq")
    hq_total = sum(n for n, b in hc.values() if b == "hq")
    # field complements: §7.2 store roster (29/store), §7.3 DC roster (150/DC)
    store = {
        "Store Manager": 1, "Assistant Store Manager": 1, "Department Supervisors": 4,
        "Sales Associate": 12, "Stock Associate": 4, "Cashiers": 3,
        "Customer Service Rep": 1, "Receiving lead": 1, "Receiving Clerk": 1,
        "Maintenance": 1,
    }
    dc = collections.Counter()
    in73 = False
    for line in open(TO, encoding="utf-8"):
        if line.startswith("### 7.3") or line.startswith("## 7.3"):
            in73 = True
            continue
        if in73 and (line.startswith("## ") or line.startswith("### ")) and "7.3" not in line:
            break
        if in73:
            # group-lead rows carry a bold group label in col 1; continuation
            # rows carry an empty col 1 — both list a role + HC in cols 2-3.
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 3 and re.fullmatch(r"\d[\d,]*", cells[2]):
                t = cells[1].strip().strip("*")
                n = int(cells[2].replace(",", ""))
                t = re.sub(r"\s*\([^)]*\)", "", t).strip()
                if t and not set(t) <= set("- ") and t not in ("Role", "Function", "Total"):
                    dc[t] += n
    dc_total = sum(dc.values())
    return hc, hq_total, store, dc, dc_total, unmapped_rows


def build_capacity(grc, res):
    hc, hq_total, store, dc, dc_total, _ = parse_register(grc)
    cap = {}

    def add(title, n, bucket):
        k = re.sub(r"\s+", " ", title).strip().lower()
        cap[k] = cap.get(k, 0) + n
        cap.setdefault("_bucket:" + k, bucket)

    for t, (n, b) in hc.items():
        add(t, n, "hq")
    for t, n in store.items():
        add(t, n * STORES, "store")
    for t, n in dc.items():
        add(t, n * DCS, "dc")
    return cap, hq_total, sum(store.values()) * STORES, dc_total * DCS


def lookup_capacity(cap, title):
    k = re.sub(r"\s+", " ", title).strip().lower()
    if k in cap:
        return cap[k]
    # plural/singular tolerance
    if k.endswith("s") and k[:-1] in cap:
        return cap[k[:-1]]
    if k + "s" in cap:
        return cap[k + "s"]
    return None


def fold_capacity_key(cap, k, bucket):
    """Fold a demand key onto its bucket-preferred capacity entry (exact form,
    then singular/plural variants). The store and DC rosters carry same-noun
    titles ('Receiving Clerks' x4 DCs vs the store receiving pair), and step
    cells mix singular/plural forms — without bucket preference, store
    receiving demand priced against the DC roster. Fifty-sixth-wave
    store-scope review."""
    variants = [k]
    if k.endswith("s"):
        variants.append(k[:-1])
    variants.append(k + "s")
    for c in variants:
        if c in cap and cap.get("_bucket:" + c) == bucket:
            return c
    for c in variants:
        if c in cap:
            return c
    return k


# --------------------------------------------------------------- walk mode --

def role_parts(cell, res):
    """[(part_text, bucket, canonical_title)] for the resolvable parts."""
    parts = grc_split(cell)
    out = []
    for p in parts:
        if p in {"—", "-", "", "System", "system"} or p.lower() in {"system"}:
            continue
        b, dept, title, _hc = res.resolve(p)
        if b == "unc":
            continue
        out.append((p, b, title if title else p))
    return out


def grc_split(raw):
    """Split a role cell into parts: commas (paren-aware, the generator's own
    SPLIT_RE so 'Manager, GL & Consolidation (Assistant Controller)' survives),
    then ';' and '/' within each comma-part. Batch 40: comma-splitting added —
    co-performer elevations (anchor-step-level-wave1.py) use comma-joined R
    cells, which previously stayed one unattributed key."""
    raw = re.sub(r"\([^)]*\)", "", raw)
    parts = []
    for chunk in GRC_SPLIT_RE.split(raw):
        parts.extend(p.strip() for p in re.split(r"\s*[;/]\s*", chunk) if p.strip())
    return [p for p in parts if p]


def mode_walk(grc, res, wfs):
    print("=" * 100)
    print("VIRTUAL GEMBA WALK — 188 value streams, process floor as designed")
    print("=" * 100)
    vs_data = collections.defaultdict(lambda: {
        "wf": 0, "steps": 0, "auto": 0, "touch": 0.0, "roles": set(),
        "handoffs": 0, "handoppairs": collections.Counter(), "gates": 0,
        "store_steps": 0, "dc_steps": 0, "hq_steps": 0})
    for w in wfs:
        d = vs_data[w["vs"]]
        d["wf"] += 1
        prev_roles = None
        for dur, r, a in w["steps"]:
            d["steps"] += 1
            roles = role_parts(r, res)
            human = dur > 0
            if not human:
                d["auto"] += 1
            d["touch"] += dur
            names = {p for p, _, _ in roles} if roles else set()
            d["roles"] |= names
            buckets = {b for _, b, _t in roles}
            if "store" in buckets:
                d["store_steps"] += 1
            elif "dc" in buckets:
                d["dc_steps"] += 1
            elif buckets:
                d["hq_steps"] += 1
            if human and prev_roles is not None and names and names != prev_roles:
                d["handoffs"] += 1
                for a_ in (names & prev_roles) or names:
                    pass
            if human and names and prev_roles is not None and prev_roles != names:
                for p in names:
                    for q in prev_roles:
                        if p != q:
                            d["handoppairs"][f"{q} → {p}"] += 1
            if human:
                prev_roles = names
            if a.strip() not in {"—", "-", ""}:
                d["gates"] += 1
    print(f"\n{'VS':>4} {'WFs':>5} {'steps':>6} {'auto%':>6} {'touch/ev*':>9} {'handoff%':>9} {'gate%':>6} {'roles':>6}  name")
    rows = []
    for vs in sorted(vs_data):
        d = vs_data[vs]
        name = vs_name(vs)
        human = d["steps"] - d["auto"]
        per_ev = d["touch"] / max(d["wf"], 1)
        hand = d["handoffs"] / max(human, 1) * 100
        gate = d["gates"] / max(d["steps"], 1) * 100
        rows.append((vs, d, per_ev, hand, gate, human, name))
        print(f"{vs:>4} {d['wf']:>5} {d['steps']:>6} {d['auto']/max(d['steps'],1)*100:>5.0f}% "
              f"{per_ev:>8.0f}m {hand:>8.0f}% {gate:>5.0f}% {len(d['roles']):>6}  {name}")
    tot_steps = sum(d["steps"] for d in vs_data.values())
    tot_auto = sum(d["auto"] for d in vs_data.values())
    tot_touch = sum(d["touch"] for d in vs_data.values())
    print(f"\nCorpus: {len(wfs)} workflows, {tot_steps} steps, {tot_auto/tot_steps*100:.0f}% automated, "
          f"total designed touch {tot_touch/60:,.0f} h/event-chain (~{tot_touch/len(wfs):,.0f} min/workflow).")
    print("\nTop role→role handoff paths (the operation's motion paths):")
    allpairs = collections.Counter()
    for d in vs_data.values():
        allpairs.update(d["handoppairs"])
    for pair, n in allpairs.most_common(15):
        print(f"  {n:5d}  {pair}")
    print("\n(* touch/ev = sum of human step durations across the VS's workflows, per workflow event; "
          "design-time measure.)")


_VS_NAMES = {}


def vs_name(vs):
    if not _VS_NAMES:
        idx = os.path.join(WF, "value-stream-index.md")
        for m in re.finditer(r"^## VS-(\d+): (.+)$", open(idx, encoding="utf-8").read(), re.M):
            _VS_NAMES[int(m.group(1))] = m.group(2).strip()
        if not _VS_NAMES:
            for d in sorted(os.listdir(WF)):
                mm = re.match(r"VS-(\d+)-(.+)", d)
                if mm:
                    _VS_NAMES[int(mm.group(1))] = mm.group(2).replace("-", " ").title()
    return _VS_NAMES.get(vs, f"VS-{vs}")


# ------------------------------------------------------------- motion mode --

def mode_motion(grc, res, wfs):
    print("=" * 100)
    print("VIRTUAL TIME & MOTION — annual role demand vs chartered capacity (org of record)")
    print("=" * 100)
    cap, hq_total, store_total, dc_total = build_capacity(grc, res)
    print(f"\nCapacity base: HQ {hq_total} (assert {CANON_HQ_HC}), stores {store_total} (assert {CANON_STORE_HC}), "
          f"DCs {dc_total} (assert {CANON_DC_HC}); net hours {HQ_NET_HOURS} HQ / {FIELD_NET_HOURS} field.")
    if hq_total != CANON_HQ_HC or store_total != CANON_STORE_HC or dc_total != CANON_DC_HC:
        print("ERROR: canonical headcount mismatch — analysis invalid for this corpus revision.")
        return 1
    demand = collections.defaultdict(float)       # (bucket, folded-key) → annual minutes
    events_cov = {"parsed": 0, "total": 0}
    touch_total = 0.0
    unattributed = 0.0
    for w in wfs:
        exec_bucket = "hq"
        for dur, r, a in w["steps"]:
            roles = role_parts(r, res)
            if roles and any(b == "store" for _, b, _t in roles):
                exec_bucket = "store"
                break
            if roles and any(b == "dc" for _, b, _t in roles):
                exec_bucket = "dc"
        ev, rule = events_per_year(w["freq"], exec_bucket)
        events_cov["total"] += 1
        if ev is None:
            continue
        events_cov["parsed"] += 1
        periods = w.get("step_period") or [None] * len(w["steps"])
        for si, (dur, r, a) in enumerate(w["steps"]):
            if dur <= 0:
                continue
            pm = periods[si] if si < len(periods) else None
            mult = pm if pm else ev
            roles = role_parts(r, res)
            if not roles:
                unattributed += dur * mult
                continue
            share = dur / len(roles)
            for _p, _b, t in roles:
                k = re.sub(r"\s+", " ", t).strip().lower()
                k = fold_capacity_key(cap, k, exec_bucket)
                demand[(exec_bucket, k)] += share * mult
    print(f"Annualization coverage: {events_cov['parsed']}/{events_cov['total']} workflows "
          f"({events_cov['parsed']/events_cov['total']*100:.0f}%) had a parseable frequency; "
          f"unattributed step time {unattributed/60:,.0f} h/yr.")
    rows = []
    for (_bucket, k), mins in demand.items():
        c = cap.get(k) or lookup_capacity(cap, k)
        if c is None:
            rows.append((k, mins, None, None))
        else:
            field = ("_bucket:" + k) in cap and cap["_bucket:" + k] in ("store", "dc")
            hours = FIELD_NET_HOURS if field else HQ_NET_HOURS
            cap_h = c * hours
            rows.append((k, mins, c, mins / 60 / cap_h * 100 if cap_h else None))
    mapped = [r for r in rows if r[2] is not None]
    unmapped = sorted(((r[0], r[1]) for r in rows if r[2] is None), key=lambda x: -x[1])
    print(f"\nDemand mapped to chartered roles: {len(mapped)}/{len(rows)} role keys "
          f"({sum(r[1] for r in mapped)/max(sum(r[1] for r in rows),1)*100:.0f}% of parsed annual minutes).")
    print("\nTop 25 roles by annual demand hours (with chartered HC and utilization):")
    print(f"{'role':<44} {'h/yr':>10} {'HC':>5} {'util%':>6}")
    for k, mins, c, util in sorted(mapped, key=lambda r: -r[1])[:25]:
        print(f"{k:<44} {mins/60:>10,.0f} {c:>5} {util:>5.0f}%")
    if MOTION_FULL:
        print(f"\nAll mapped roles by annual demand hours (--full; alphabetical):")
        for k, mins, c, util in sorted(mapped, key=lambda r: r[0]):
            print(f"{k:<44} {mins/60:>10,.0f} {c:>5} {util:>5.0f}%")
    hot = sorted((r for r in mapped if r[3] and r[3] > 85), key=lambda r: -r[3])
    cold = sorted((r for r in mapped if r[3] is not None and r[3] < 15 and r[1] > 0), key=lambda r: r[3])
    print(f"\nHot roles (>85% utilization): {len(hot)}")
    for k, mins, c, util in hot[:15]:
        print(f"  {k:<44} {util:>5.0f}%  HC={c}")
    print(f"\nCold roles (<15% utilization, >0 parsed demand): {len(cold)}")
    for k, mins, c, util in cold[:15]:
        print(f"  {k:<44} {util:>5.0f}%  HC={c}")
    if unmapped:
        print(f"\nUnmapped demand keys (title not found in register/roster HC — top 10):")
        for k, mins in unmapped[:10]:
            print(f"  {k:<44} {mins/60:>10,.0f} h/yr")
    print("\nInterpretation guardrails: (1) utilization is demand-on-role-design, not timesheet "
          "actuals; (2) narrow titles inherit department workload through the wave-31/32 exercise-"
          "through-broader-titles contract; (3) unparseable frequencies are excluded, so roles "
          "dominated by unparseable-cadence workflows read low here.")
    return 0


MOTION_FULL = False


def main():
    mode_arg = sys.argv[1] if len(sys.argv) > 1 else "walk"
    global MOTION_FULL
    MOTION_FULL = "--full" in sys.argv
    grc = load_grc()  # NOTE: rebinds sys.argv; mode captured above
    hq, dc, store, dept_order = grc.parse_toc()
    res = grc.Resolver(hq, dc, store, dept_order)
    wfs = parse_workflows()
    if len(wfs) != CANON_WORKFLOWS:
        print(f"ERROR: workflow population {len(wfs)} != canonical {CANON_WORKFLOWS}; "
              f"regenerate and re-run (analysis baselines are corpus-pinned).")
        return 1
    mode = mode_arg if mode_arg in ("walk", "motion") else "walk"
    if mode == "walk":
        return mode_walk(grc, res, wfs) or 0
    return mode_motion(grc, res, wfs)


if __name__ == "__main__":
    sys.exit(main())
