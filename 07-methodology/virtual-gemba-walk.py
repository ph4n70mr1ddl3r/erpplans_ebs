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
                steps, periods, in_steps = [], [], False
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
                        dur_cell = cells[4] if len(cells) > 4 else ""
                        steps.append((parse_minutes(dur_cell),
                                      cells[2].strip(), cells[3].strip()))
                        periods.append(step_period_qualifier(dur_cell))
                out.append({"id": wid, "vs": vs, "title": title.strip(), "owner": owner,
                            "freq": freq, "steps": steps, "step_period": periods})
    return out


def parse_minutes(cell):
    """'5min'/'5–10min'/'2h'/'1.5 hours' → midpoint minutes; Automated/—/'' → 0.
    Batch 49 (2026-09-25): plural unit forms ('2 hours', '4 hrs', '30 mins',
    '24 hours/year') previously returned 0.0 — the unit alternation
    ('min|hour|hr|h') matched the singular stem and the trailing \b could not
    bind before the plural 's' (or the '/qualifier'), silently zeroing every
    plural-unit duration cell (3,775 corpus cells re-measured by the fix).
    Unit alternation is now plural-capable longest-first
    ('mins?|hours?|hrs?|h'), so qualifiers after the unit ('/year',
    '/item midpoint × ~30 items/year') no longer defeat the match.
    2026-09-25 (bu) tenth review-everything pass — per-occurrence rates are
    SYMBOLIC (the roll-up's per-unit discipline, mirrored here): a duration
    cell qualified by a subset-event unit ('/occurrence', '/exception',
    '/incident', '/case', 'per investigation', '/signup', …) prices the step
    per THAT subset, whose universe the workflow's Frequency clause does not
    carry — annualizing it against the workflow cadence multiplied subset
    work by the whole universe (W1365's '10–20 min/exception' read ×8,700
    ASN-events = 2,175 h/yr against its own ~105–150/exceptions-month
    estimate; W3's '15 min/occurrence' Buyer RTV cell read ×72,000
    store-events). Such cells return 0.0 here (counted, never summed — the
    roll-up's classification is authoritative for their volume). Period-
    qualified totals ('1 hour/week', '2 hours/month', '4 hours/year') are
    NOT zeroed: they are chain-wide periodic totals, bridged by the per-step
    step_period attachment (parse_workflows × step_period_qualifier) —
    '4 hours/year' on W942's DPO consent audit had been priced 240 min ×
    9,000 linking-events = 36,000 h/yr against a charter of 4 documented
    hours."""
    c = cell.strip().strip("*").lower()
    if not c or c in {"—", "-", "automated", "n/a", "system"}:
        return 0.0
    if re.search(r"(?:/\s*|\bper\s+)(occurrences?|exceptions?|incidents?|cases?|signups?|investigations?|claims?|requests?)\b", c):
        return 0.0
    m = re.search(r"(\d+(?:\.\d+)?)(?:\s*[–-]\s*(\d+(?:\.\d+)?))?\s*(mins?|hours?|hrs?|h)\b", c)
    if not m:
        return 0.0
    lo = float(m.group(1))
    hi = float(m.group(2)) if m.group(2) else lo
    mid = (lo + hi) / 2
    return mid * 60 if m.group(3).startswith(("h", "h")) else mid


PERIOD_DAYS = {"day": 1, "week": 7, "month": 30, "quarter": 91, "year": 365, "season": 91}
PERIOD_MULT = {"day": 365, "week": 52, "month": 12, "quarter": 4, "year": 1, "season": 4}
WORKDAYS = {"day": 250, "week": 50, "month": 12, "quarter": 4, "year": 1, "season": 4}

# Adjudicated nominal annual event volumes for the episodic program families
# (2026-09-25 (be) wave) — exact-form keys, chain-wide events/yr. These are
# DOCUMENTED ASSUMPTIONS (small-N episodic programs production does not
# measure), not derived figures; each is deliberately conservative and
# revisitable. Basis notes inline. Unmapped bespoke phrases stay unparsed.
NOMINAL_EVENTS = {
    "event-driven": 12,            # generic incident/escalation/case programs
    "event-driven; rare": 2,
    "event-driven × 200 stores": 2400,   # 12 exceptions/store/yr
    "per recall event": 2,         # product-safety recalls: rare by design
    "per project": 20,             # capex/EPC/construction program
    "per remodel": 15,             # store remodel program
    "per event": 24,               # marketing/event calendar (~2/month)
    "per transaction": 2,          # M&A/deal transactions, not POS
    "on event": 24,                # HR life-events + surveillance triggers
    "per case": 30,                # legal/investigation docket (W3258: ~30–80)
    "per closure": 2,              # store closures
    "per target": 12,              # M&A/screening funnel
    "periodic": 4,                 # quarterly review cycle
    "per rental": 4500,            # own-field sibling: ~3,000–6,000 rentals/yr
    "per site": 12,                # solar/site programs
    "per order": 6000,             # resale/pre-owned order volume (small)
    "per item": 1500,              # trade-in/take-back units
    "per opportunity": 30,
    "per shipment": 200,           # import containers/yr (consolidated)
    "per project completion": 20,
    "per initiative": 15,
    "per application": 300,        # housing-finance applications
    "per claim": 60,
    "per sourcing event + multi-year contract": 4,
    "ad hoc": 6,
    "ad-hoc": 6,
    "ad-hoc (rare)": 2,
    "ad hoc (lapse/breach events)": 2,
    "per cooperative onboarding": 10,
    "opportunity-driven": 30,
    "per dispute": 20,
    "per cycle": 4,
    "per incident": 20,
    "per program cycle": 4,
    "per loan": 150,
    "per assignment": 10,
    "per new store construction": 12,   # opening program ~10–15/yr (own-field)
    "per delivery": 2000,          # jobsite/bulky deliveries
    "per lease deal": 20,
    "per worker assignment": 500,  # contractor assignments (~10–20% of labor)
    "per matter": 15,
    "per engagement": 12,
    "per campaign": 12,
    "per bid": 30,
    "per milestone": 60,
    "per return": 400,
    "per season/promotion": 8,
    "per launch": 6,
    "per test": 12,
    "per finding": 12,
    "per cohort": 6,
    "per trip": 2000,
    "per issue": 12,
    "per candidate": 400,          # hiring pipeline (≈2x the hire volume)
    "per referral": 150,
    "per customer interaction": 20000,   # contact-center tier interactions
    "per visit": 2000,
    "per appointment": 300,
    "per consultation": 300,
    "per exception": 2400,
    "per need": 12,
    "per change": 250,             # per-workday change rate for register upkeep
    "per report": 50,
    "per lease": 20,
    "per asset": 100,
    "per instrument": 50,
    "per decision": 50,
    "per proposal": 30,
    "per exit": 1170,              # own-field sibling: ~1,000–1,340 exits/yr
    "per intake batch": 50,
    "per stage-gate": 80,
    "per movement": 500,
    "rare": 1,
    "occasional": 12,
    "moderate": 50,
    "seasonal": 4,
    "per tax year + per filing": 260,
    # batch 50 / 44c tranche (2026-09-25): paren-qualified and qualified-rare
    # whole forms — the qualifier IS the adjudication, so these are exact-form
    # entries rather than decomposition candidates (decomposition would price
    # 'per event (rare)' at the per-event rate and inflate a rare class 12×).
    "rare (preparedness continuous)": 1,     # continuity/evacuation preparedness programs
    "rare but high-impact": 1,               # DG transport incident, bond default class
    "per event (rare)": 2,                   # rare-event response with per-event triggers
    "as occurred": 2,                        # actual-occurrence reactive programs
    "per qualifying breach": 2,              # breach-of-contract / covenant class
    "per fault": 20,                         # equipment/fault dispatch queue (aligns per incident)
    "per procurement batch": 50,             # aligns per intake batch
    "exception-driven": 20,                  # vendor dispute/exception queue (aligns per dispute)
    "campaign-driven": 12,                   # marketing campaign calendar (~2/month)
    "seasonal + event-driven": 8,            # seasonal program + in-season events
    "event-driven per calamity": 4,          # PH calamity-season class
    "event-driven post-disaster": 4,         # post-disaster response cycles
    "statutory + usage-based": 12,           # statutory calibration/inspection + usage triggers
    "usage/time-based": 12,                  # usage-triggered calibration/maintenance
    "scheduled pm + reactive": 12,           # PM schedule + reactive service calls
    "per temporary office mobilization": 2,  # temporary-site program (rare)
    "ad-hoc; 5–10 per project": 20,          # 5–10 × the per-project rate
    "per seasonal event": 8,                 # garden/season program calendar
    "per dg shipment": 200,                  # aligns per shipment (import containers)
    "per dg last-mile shipment": 200,
    "per mode + per shipment": 200,
    "ad-hoc per project request": 20,         # aligns per project
}


PERIOD_QUALIFIER = re.compile(r"(?:/|per\s+)\s*(month|week|year|quarter)\b", re.I)

# Batch 50 / 44c (2026-09-25): clause-level nominal volumes for compound
# decomposition (rule 6a) — keyed on the clause text with a leading 'per '
# stripped, whitespace-normalized, parentheticals removed. Same discipline as
# NOMINAL_EVENTS: small-N documented assumptions, each deliberately
# conservative and revisitable. Deliberately ABSENT: high-volume or polysemous
# nouns (transaction, sku, pickup, load, employee, customer, store) — those
# clauses stay unparsed rather than risk a wrong-order annualization.
CLAUSE_EVENTS = {
    "contract": 40,        # ~40–60 active contracts, rolling renewals/reviews
    "project": 20,         # aligns per project
    "completed project": 20,
    "incident": 20,        # aligns per incident
    "case": 30,            # aligns per case
    "case event": 30,
    "event": 24,           # aligns per event
    "site": 12,            # aligns per site
    "lease": 20,           # aligns per lease
    "vendor": 40,          # certification/renewal subset of the vendor base
    "third party": 12,     # processor/partner due-diligence cycle
    "matter": 15,          # aligns per matter
    "engagement": 12,      # aligns per engagement
    "program": 12,
    "initiative": 15,      # aligns per initiative
    "model": 12,           # governed models (AI/pricing/risk), small-N
    "design": 12,
    "cycle": 4,            # aligns per cycle
    "season": 4,           # aligns seasonal
    "shipment": 200,       # aligns per shipment (import containers)
    "delivery": 2000,      # aligns per delivery (jobsite/bulky)
    "order": 6000,         # aligns per order (resale/pre-owned volume)
    "worker": 500,         # aligns per worker assignment
    "worker assignment": 500,
    "candidate": 400,      # aligns per candidate
    "device": 100,         # aligns per asset
    "asset": 100,
    "vehicle": 200,        # fleet ~200 trucks
    "category": 6,         # merch category reviews (~2/yr per category)
    "batch": 50,           # aligns per intake batch
    "claim": 60,           # aligns per claim
    "breach": 12,
    "dispute": 20,         # aligns per dispute
    "return": 400,         # aligns per return
    "move-out": 1170,      # aligns per exit (rental returns at maturity)
    "build": 12,           # quarterly-ish release/build cycles
    "build cycle": 12,
    "finding": 12,         # aligns per finding
    "milestone": 60,       # aligns per milestone
    "hedge": 12,           # rolling hedge program
    "carrier": 12,         # carrier re-qualification cycle
    "partner": 12,
    "supplier": 40,        # supplier review subset
    "permit cycle": 4,
    "audit cycle": 4,
    "onboarding": 300,     # onboarding pipeline (sub-per-candidate)
    "divestiture": 2,
    # second-clause family (the maintenance half of compounds)
    "periodic review": 4,
    "periodic refresh": 4,
    "periodic rebalance": 4,
    "periodic re-qualification": 2,
    "periodic re-vet": 2,
    "periodic re-verification": 2,
    "periodic revalidation": 2,
    "periodic recertification": 2,
    "periodic renewal": 2,
    "periodic review of template contracts": 4,
    "periodic tuning": 4,
    "periodic": 4,
    "refresh": 4,
    "launch": 6,           # aligns per launch
    "renewal": 40,         # aligns contract renewal cycles
    "on change": 250,      # aligns per change
    "on update": 250,
    "on regulation change": 4,
    "on standard change": 4,
    "on structural change": 4,
    "reactive": 20,        # aligns per incident class
    "portfolio": 12,
    "strategy refresh": 4,
    "portfolio review": 4,
    "portfolio capacity": 12,
    "per project request": 20,
}
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
    period_re = r"(day|week|month|quarter|year|season)"   # season: 4/yr (batch 50, 44c)
    core = re.sub(r"\([^)]*\)", " ", low)  # parentheticals are annotation, not cadence

    # 0. standing-coverage house forms: the work is per-workday coverage
    #    (system/platform monitoring, register maintenance), not a per-event
    #    count -> HQ/DC once per workday (250), store once per trading day
    #    (xSTORES). Judged on the paren-stripped text so annotation like
    #    'Continuous (~6,911 employees)' still matches; a bare cadence word in
    #    the core ('Continuous + monthly close') keeps rule 3 authoritative.
    if re.search(r"\b(continuous|ongoing|maintained|always[- ]on|real[- ]time|24/7)\b", core) \
            and not re.search(r"\b(daily|weekly|monthly|quarterly|annual|yearly)\b", core):
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
    # 5. self-stated volume: the field carries its own annual/monthly count in
    #    a parenthetical or tail clause ('Per hire (~1,200–1,600 hires/yr)',
    #    '~3,000–6,000 rentals/yr', '~100–200 loan/advance requests/month
    #    chain-wide') — the field's own numbers, not a synthetic cadence.
    m = re.search(r"~?\s*(\d[\d,]*)\s*[–-]\s*(\d[\d,]*)\s*[^();]*?/\s*(?:yr|year)\b", low) or \
        re.search(r"~?\s*(\d[\d,]*)\s*[–-]\s*(\d[\d,]*)\s*[^();]*?per\s+year\b", low)
    if m:
        return midpoint(m.group(1), m.group(2)), "self-stated-annual"
    m = re.search(r"~?\s*(\d[\d,]*)\s*[–-]\s*(\d[\d,]*)\s*[^();]*?/\s*month\b", low)
    if m:
        return midpoint(m.group(1), m.group(2)) * 12, "self-stated-monthly"

    # 6. adjudicated nominal families (exact-form map, 2026-09-25 (be)): the
    #    episodic program workflows whose volumes production does not measure
    #    (recalls, M&A deals, remodels, cases, rentals...) — small-N nominal
    #    events/yr, each an explicit documented assumption. Exact-form match
    #    (whitespace-normalized) so a polysemous noun can never hijack a real
    #    cadence. Unmapped bespoke one-off phrases stay honestly unparsed.
    nominal = NOMINAL_EVENTS.get(re.sub(r"\s+", " ", low).strip(" ;,."))
    if nominal:
        return float(nominal), "nominal-family"

    # 6a. compound decomposition (batch 50 / 44c, 2026-09-25): split the
    #     frequency on top-level '+' / ';' (paren-aware) and price each clause
    #     independently — clauses 1–5 of this ladder, then the exact-form map,
    #     then the clause-nominal table (leading 'per ' stripped). Take the
    #     MAXIMUM parsed clause: the binding (most frequent) cadence governs
    #     the annualization. Clauses that parse to nothing are ignored; if no
    #     clause parses the form stays honestly unparsed. Single-clause forms
    #     price through the same clause tables (a one-clause split).
    clauses = [c.strip(" ;,." ) for c in re.split(r"\s*\+\s*|\s*;\s*", core) if c.strip(" ;,.")]
    if clauses:
        best, best_rule = None, None
        for cl in clauses:
            cl_low = cl.strip().lower()
            ev2 = None
            m2 = re.search(r"(\d[\d,]*)\s*[–-]\s*(\d[\d,]*)\s*[^.;()]*?per\s+" + period_re + r"\b", cl_low) or \
                 re.search(r"(\d[\d,]*)\s*[^.;()]*?per\s+" + period_re + r"\b", cl_low)
            if m2:
                g2 = m2.groups()
                ev2 = midpoint(g2[0], g2[1] if len(g2) > 2 else None) * PERIOD_MULT[g2[-1]]
            else:
                for word, period in (("daily", "day"), ("weekly", "week"), ("monthly", "month"),
                                     ("quarterly", "quarter"), ("annual", "year"), ("yearly", "year")):
                    if re.search(r"\b" + word, cl_low):
                        ev2 = float(PERIOD_MULT[period])
                        break
            if ev2 is None:
                m2 = re.search(r"(\d[\d,]*)\s*[–-]\s*(\d[\d,]*)\s*[^.;()/]*?/\s*" + period_re + r"\b", cl_low) or \
                     re.search(r"(\d[\d,]*)\s*[^.;()/]*?/\s*" + period_re + r"\b", cl_low)
                if m2:
                    g2 = m2.groups()
                    ev2 = midpoint(g2[0], g2[1] if len(g2) == 3 else None) * PERIOD_MULT[g2[-1]]
            if ev2 is None:
                ev2 = NOMINAL_EVENTS.get(re.sub(r"\s+", " ", cl_low).strip(" ;,."))
            if ev2 is None:
                bare = re.sub(r"\([^)]*\)", " ", cl_low)
                bare = re.sub(r"\s+", " ", bare).strip(" ;,.")
                ev2 = NOMINAL_EVENTS.get(bare)
            if ev2 is None:
                # clause-nominal table: the leading 'per ' is optional
                # ('per incident' / 'incident' both price; 'ad-hoc per X'
                # forms stay out — they need their own exact entries)
                key = bare[4:].strip() if bare.startswith("per ") else bare
                ev2 = CLAUSE_EVENTS.get(key)
            if ev2 is not None and (best is None or ev2 > best):
                best, best_rule = float(ev2), f"compound:{cl_low[:24]}"
        if best is not None:
            return best, best_rule
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
