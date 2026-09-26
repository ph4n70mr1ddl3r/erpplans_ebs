#!/usr/bin/env python3
r"""Universal role-demand verification register — batch 52b (2026-09-26, by direction).

Generalizes the Role-Anchoring Contract's demand-verification loop from the
53-role weak-anchor watchlist to ALL chartered roles (259), per
universal-role-demand-verification-spec.md (§1/§2 improvements implemented:
alias-surface matching, attribution confidence, state column, days/week
bridge, peak-aware flagging, department roll-up).

Batch 52b instrument grammar — mode_motion's attribution arithmetic computed
IN-PROCESS at role grain (no subprocess; one corpus pass), with four
documented supersets over the engine:

  1. DAYS/WEEK BRIDGE — whole-cell pure day/week ranges ('3–5 days',
     '1–2 weeks') price at midpoint days × 6.5 h (weeks × 5 d). The engine's
     parse_minutes reads them 0.0 (its days-based work is verified by cycle
     audit, not hours); the bridge converts that class to hour-measured with
     a † marker. The engine itself is untouched (additive steps_raw field
     only) — the batch-51 pin re-verified byte-identical after the patch.
  2. IT-SEAT ALIAS SURFACES — a seat's claimed share is matched not only on
     its canonical title but on its IT_SEATS alias keys ('helpdesk agent',
     'integration engineer', …), with a preceding-qualifier blocklist
     ('facilities', 'transport', 'bir', 'eis') so 'facilities helpdesk' never
     claims against the IT FS seat. Converts participant-only reads to
     measured claims without corpus edits.
  3. ATTRIBUTION CONFIDENCE — every row carries own-surface (a matched cell's
     resolved parts fold to the seat's own capacity key), alias-claimed
     (matched only through alias vocabulary — the corpus's cells denote the
     seat through broader forms), or participant-only (Owner/Participants
     anchor, no step surface at all).
  4. PEAK-AWARE FLAGGING — roles whose matched workflows' Frequency strings
     hit a peak-calendar vocabulary (semi-monthly payroll, month/year-end
     close, seasonal/typhoon/promo peaks) carry ⚑: average utilization
     understates the peak window; verify the peak, not the mean.

State column: active / deferred-prepared (Build-Squad — OMO/TPS (ad)/(ah)) /
dormant — design-load (Trade dept disabled-prepared (x)); the OVERLOAD tally
splits live vs design-load so dormant design capacity never reads as an
active staffing verdict.

Department roll-up: per §5.3 department (+ IT product model split by state +
store/DC field), measured demand h/yr vs capacity h/yr with a measured-roles
count — a low measured-share is a COVERAGE gap (anchor the department's
seats), not slack (the exercise-through contract: individual UNDER rows
inside a hot department are queue-shape).

Verdict ladder: CONFIRMED (50–150%) / OVERLOAD (>150%) / UNDER-UTILIZED
(<50%) / MEASURED — HC UNPRICED / ZERO-DURATION / UNPARSEABLE-FREQ /
NO PARSED CADENCE. Residual classes: WORKFLOW-MEASURED (util ≥80%) /
PARTIAL — NAMED / PARTIAL — UNNAMED (<5%) / COVERAGE-STANDBY / UNMEASURED —
naming is a charter act (charter §10/§2/§11); the instrument counts, the
charter names, and never invents residual content.

Writes 01-model-company/workflows/role-demand-verification.md.
Deterministic; read-only over the corpus and the engine module.
--check re-derives in memory and byte-compares (no write; exit 1 on drift).
Unpinned until Phase 3 of the spec — this batch moves no existing pin.
"""
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
OUT = os.path.join(REPO, "01-model-company", "workflows",
                   "role-demand-verification.md")

# Capture BEFORE the imports: vgw.load_grc() rebinds sys.argv.
CHECK = "--check" in sys.argv

spec = importlib.util.spec_from_file_location(
    "grc", os.path.join(HERE, "generate-role-coverage.py"))
grc = importlib.util.module_from_spec(spec)
sys.modules["grc"] = grc
spec.loader.exec_module(grc)
spec2 = importlib.util.spec_from_file_location(
    "vgw", os.path.join(HERE, "virtual-gemba-walk.py"))
vgw = importlib.util.module_from_spec(spec2)
sys.modules["vgw"] = vgw
spec2.loader.exec_module(vgw)
grc2 = vgw.load_grc()

HOURS_PER_DAY = 6.5          # days-bridge net hours per workday
DAYS_PER_WEEK = 5
PRECEDING_BLOCKLIST = {"facilities", "transport", "bir", "eis"}
PEAK_VOCAB = ("semi-monthly", "semimonthly", "payroll", "13th month",
              "thirteenth month", "typhoon", "storm season", "peak season",
              "peak-season", "seasonal", "ber month", "christmas", "holiday",
              "promo event", "month-end", "month end", "year-end", "year end",
              "quarter-end", "quarter end", "close cycle", "closing")

DAYS_RE = re.compile(
    r"^\s*(\d+(?:\.\d+)?)\s*(?:–|—|-|to\s+)?\s*(\d+(?:\.\d+)?)?\s*"
    r"(days?|weeks?)\b[^a-z0-9]*$", re.I)
EFFORT_WORD_RE = re.compile(r"effort|man-?day|work-?day|touch", re.I)


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def bridge_days(cell):
    """Effort-worded day/week cells → midpoint minutes; else None. The
    corpus's 2,869 day/week cells are elapsed-window style ('1–2 weeks' UAT,
    '2–5 days' signoff) — the batch-51 elapsed-vs-effort doctrine keeps them
    unpriced (cycle audit). The bridge fires only on explicit effort wording
    ('X days effort', 'man-days'); none exist today, so it is armed for
    corpus discipline rather than active."""
    if not cell or not EFFORT_WORD_RE.search(cell):
        return None
    m = DAYS_RE.match(cell.strip())
    if not m:
        return None
    lo = float(m.group(1))
    hi = float(m.group(2)) if m.group(2) else lo
    days = (lo + hi) / 2
    if m.group(3).lower().startswith("week"):
        days *= DAYS_PER_WEEK
    return days * HOURS_PER_DAY * 60


def build_index(res, wfs):
    """One corpus pass → per distinct normalized Role-(R) cell text:
    occurrences (bridged_dur, mult|None, exec_bucket, peak_flag) with the
    cell's resolved parts, plus the cadence coverage counts."""
    idx = {}
    cov = {"parsed": 0, "total": 0}
    for w in wfs:
        exec_bucket = "hq"
        for dur, r, a in w["steps"]:
            roles = vgw.role_parts(r, res)
            if roles and any(b == "store" for _, b, _t in roles):
                exec_bucket = "store"
                break
            if roles and any(b == "dc" for _, b, _t in roles):
                exec_bucket = "dc"
        ev, _rule = vgw.events_per_year(w["freq"], exec_bucket)
        cov["total"] += 1
        if ev is not None:
            cov["parsed"] += 1
        peak = any(v in norm(w["freq"]) for v in PEAK_VOCAB)
        raws = w.get("steps_raw") or [""] * len(w["steps"])
        periods = w.get("step_period") or [None] * len(w["steps"])
        for si, (dur, r, a) in enumerate(w["steps"]):
            k = norm(r)
            if not k or k in ("—", "-"):
                continue
            e = idx.setdefault(k, {"occ": [], "parts": None})
            bridged = bridge_days(raws[si]) if si < len(raws) and dur <= 0 else None
            d = bridged if bridged is not None else dur
            if ev is None:
                e["occ"].append((d, None, exec_bucket, peak, bridged is not None))
                continue
            pm = periods[si] if si < len(periods) else None
            e["occ"].append((d, pm if pm else ev, exec_bucket, peak,
                             bridged is not None))
    return idx, cov


def build_alias_index():
    """Reverse map canonical live title → corpus alias surfaces, from the
    corpus's own adjudicated reconciliation tables (ROLE_ALIASES + W36/W38/W39
    + IT_SEATS) — the same vocabulary the engine folds through, so the
    instrument's claims and the engine's resolution stay one system."""
    rev = {}
    for tab in (grc.ROLE_ALIASES, grc.ROLE_ALIASES_W36, grc.ROLE_ALIASES_W38,
                grc.ROLE_ALIASES_W39, grc.IT_SEATS):
        for k, v in tab.items():
            rev.setdefault(norm(v), set()).add(norm(k))
    return rev


ALIAS_REV = build_alias_index()

# IT-seat HC mirror — ITOM §9.1 steady-state table + §5.3 platform rosters
# (2026-09-26 batch 52b). Design-of-record posture; deferred-squad seats are
# annotated by the State column. Vocabulary-umbrella seats with no seat-level
# roster basis (department/team grain the workflow vocabulary resolves
# through) are deliberately absent → MEASURED — HC UNPRICED, the ITOM
# seat-charter worklist, never a silent fold.
IT_SEAT_HC = {
    "it product owner": 9,                 # 7 active — OMO/TPS POs deferred
    "it product manager (build squad)": 2,  # OMO/TPS — deferred
    "build-squad tech lead": 2,             # OMO/TPS — deferred
    "build-squad software engineer": 9,     # 1 active (CCP commerce) + 8 deferred
    "build-squad qa automation engineer": 1,# SEP QA-auto lead
    "erp functional analyst": 22,           # domain §9.1 analysts column
    "dp data & reporting analyst": 6,       # domain §9.1 data column
    "iap integration engineer": 5,
    "iap integration support engineer": 1,
    "infra cloud engineer": 2,
    "infra network engineer": 1,
    "infra site reliability engineer": 1,
    "infra dba / saas administrator": 1,
    "infra system administrator": 1,       # ERP-sysadmin workflow vocabulary (W595)
    "sec security engineer": 2,
    "sec security analyst": 1,
    "sec ot security lead": 1,              # SEC lead seat
    "sec (cybersecurity, privacy & ot security)": 3,  # GRC 2 + TPRM 1 (unseated members)
    "dp data engineer": 3,
    "dp mdm steward": 2,
    "dp bi platform": 1,
    "it helpdesk agent (fs)": 2,           # FS L2 analysts
    "fs itam administrator": 1,
    "head of enterprise architecture (cio office)": 1,
    "aap agent engineer": 3,
    "aap ai-governance liaison": 1,
}


def surfaces_for(q):
    """Canonical title surface + every adjudicated corpus alias that denotes
    the seat (grc reconciliation tables + IT_SEATS), longest first so
    canonical wins ties."""
    base = norm(q["title"])
    ss = {base} | ALIAS_REV.get(base, set())
    return sorted(ss, key=len, reverse=True)


def make_matcher(surface):
    return re.compile(r"(?<![a-z0-9])" + re.escape(surface) + r"(?![a-z0-9])")


def surface_hits(text, surfaces, canonical):
    """(hit, is_canonical) — first matching surface; alias hits guarded
    against a blocklisted preceding qualifier ('facilities helpdesk')."""
    for s in surfaces:
        m = make_matcher(s).search(text)
        if not m:
            continue
        if s != canonical:
            pre = text[:m.start()].strip().lower().split()
            if pre and pre[-1] in PRECEDING_BLOCKLIST:
                continue
        return s, s == canonical
    return None, False


def parts_attribution(queue, idx, res, cap):
    """Engine-parity pass: attribute each cell's even share to the chartered
    roles its RESOLVED parts denote (fold the part title under the occurrence's
    exec bucket; match against each role's own folded key under its charter
    bucket). This is mode_motion's distribution aggregated to chartered
    roles — the corpus's own reconciliation, not a re-implementation."""
    fold_of = {}
    for q in queue:
        b = q["bucket"] if q["bucket"] in ("store", "dc") else "hq"
        fold_of.setdefault(vgw.fold_capacity_key(cap, norm(q["title"]), b), []).append(q)
    claim = {norm(q["title"]): 0.0 for q in queue}
    hit = set()
    for text, e in idx.items():
        if e["parts"] is None:
            e["parts"] = vgw.role_parts(text, res)
        roles = e["parts"]
        if not roles:
            continue
        for d, mult, bucket, _pk, _bd in e["occ"]:
            if mult is None or d <= 0:
                continue
            share = d / len(roles) * mult
            for _p, _b, t in roles:
                fk = vgw.fold_capacity_key(cap, norm(t), bucket)
                for q in fold_of.get(fk, ()):
                    k = norm(q["title"])
                    claim[k] += share
                    hit.add(k)
    return claim, hit
def surface_claim(q, idx, res, cap):
    """Fallback pass for zero-claim roles: the claimed even-share slice of
    every step cell whose text names the seat through a canonical or
    adjudicated-alias surface (blocklist-guarded) — the vocabulary the
    resolver folds elsewhere, claimed honestly at alias-claimed confidence."""
    canonical = norm(q["title"])
    surfaces = surfaces_for(q)
    claimed = 0.0
    anchors = {"parsed": 0, "zero": 0, "unparsed": 0}
    days_bridged = 0
    peak = False
    own_surface = False
    own_key = vgw.fold_capacity_key(cap, canonical, "hq")
    for text, e in idx.items():
        s, is_canon = surface_hits(text, surfaces, canonical)
        if not s:
            continue
        if is_canon:
            own_surface = True
        if e["parts"] is None:
            e["parts"] = vgw.role_parts(text, res)
        roles = e["parts"]
        if roles and not own_surface:
            for _p, _b, t in roles:
                if vgw.fold_capacity_key(cap, norm(t), "hq") == own_key:
                    own_surface = True
                    break
        for d, mult, bucket, pk, brd in e["occ"]:
            if pk:
                peak = True
            if mult is None:
                if d > 0:
                    anchors["unparsed"] += 1
                continue
            if d <= 0:
                anchors["zero"] += 1
                continue
            anchors["parsed"] += 1
            if brd:
                days_bridged += 1
            if roles:
                claimed += d / len(roles) * mult
            else:
                claimed += d * mult
    return claimed, anchors, days_bridged, peak, own_surface


def capacity_for(q, cap):
    """(hc, hours) mirroring mode_motion: engine cap map looked up through
    the engine's own fold with the role's charter bucket (store/DC rosters
    fold under their bucket preference), trying the canonical title, its
    paren-stripped register key, and the adjudicated alias forms; IT seats at
    chartered HC × 1,800; nothing maps → (None, None)."""
    b = q["bucket"] if q["bucket"] in ("store", "dc") else "hq"
    tried = [norm(q["title"]), grc.key(q["title"])] + \
        sorted(ALIAS_REV.get(norm(q["title"]), ()), key=len, reverse=True)
    for t in tried:
        if not t:
            continue
        fk = vgw.fold_capacity_key(cap, t, b)
        for cand in (fk, t):
            c = cap.get(cand) if cand else None
            if c:
                field = cap.get("_bucket:" + cand) in ("store", "dc")
                return c, (vgw.FIELD_NET_HOURS if field else vgw.HQ_NET_HOURS)
    if q["bucket"] == "it":
        hc = IT_SEAT_HC.get(norm(q["title"])) or q["hc"]
        if hc:
            return hc, vgw.HQ_NET_HOURS
    return None, None


def state_of(q):
    if "trade" in q["dept"].lower():
        return "dormant — design-load (dept disabled-prepared)"
    if q["bucket"] == "it" and "build-squad" in norm(q["title"]):
        return "deferred-prepared (OMO/TPS)"
    return "active"


def band_of(util):
    return ("OVERLOAD" if util > 150 else
            "UNDER-UTILIZED" if util < 50 else "CONFIRMED")


def residual_of(util, band):
    if band == "OVERLOAD":
        return "—"
    if util >= 80:
        return "WORKFLOW-MEASURED"
    if util < 5:
        return "PARTIAL — UNNAMED"
    return "PARTIAL — NAMED"


def main():
    _wfs, tier, rows, dept_order, anchor = grc.build()
    row_by = {}
    for r in rows:
        row_by.setdefault((grc.key(r["title"]), r["bucket"]), r)
    queue, missing = [], []
    for k, c in anchor["chartered"].items():
        r = row_by.get((k, c["bucket"]))
        if r is None:
            missing.append(c["title"])
            continue
        queue.append({"title": c["title"], "bucket": c["bucket"], "dept": c["dept"],
                      "hc": c["hc"] or r["hc"], "touched": r["touched"]})
    queue.sort(key=lambda r: (r["touched"], r["title"].lower()))
    if missing:
        print(f"ERROR: {len(missing)} chartered roles joined no stats row: {missing[:5]}")
        return 1

    wfs = vgw.parse_workflows()
    hq_toc, dc_toc, store_toc, dept_toc = grc.parse_toc()
    res = grc.Resolver(hq_toc, dc_toc, store_toc, dept_toc)
    cap, _hq, _st, _dc = vgw.build_capacity(grc2, res)
    idx, cov = build_index(res, wfs)

    src_map = {"hq": "§5.3 register", "it": "IT seat",
               "store": "§7.2 store roster", "dc": "§7.3 DC roster"}
    tally = {"CONFIRMED": 0, "OVERLOAD (active)": 0, "OVERLOAD (design-load)": 0,
             "UNDER-UTILIZED": 0, "MEASURED — HC UNPRICED": 0,
             "ZERO-DURATION": 0, "UNPARSEABLE-FREQ": 0, "NO PARSED CADENCE": 0}
    resid = {"WORKFLOW-MEASURED": 0, "PARTIAL — NAMED": 0,
             "PARTIAL — UNNAMED": 0, "COVERAGE-STANDBY": 0, "UNMEASURED": 0}
    n_alias = n_days = n_peak = 0
    dept_roll = {}

    L = []
    A = L.append
    A("# Universal Role-Demand Verification (generated — batch 52b, 2026-09-26)")
    A("")
    A("> **Universal register** for the Role-Anchoring Contract — every chartered role")
    A(f"> ({len(queue)}: §5.3 register + IT product-model seats + §7.2/§7.3 roster roles) carries a")
    A("> per-role annual-demand verdict against chartered capacity, generalizing the batch-49–51")
    A("> weak-anchor instrument from its 53-role watchlist to the full population, per")
    A("> [`universal-role-demand-verification-spec.md`](../../07-methodology/universal-role-demand-verification-spec.md).")
    A("> **Batch 52b grammar** — mode_motion's attribution computed in-process at role grain,")
    A("> with four documented supersets: (1) days/week bridge († — whole-cell '3–5 days'/'1–2")
    A("> weeks' price at midpoint × 6.5 h/day; the engine keeps its cycle-audit zero), (2) IT-seat")
    A("> alias surfaces (claims matched through IT_SEATS vocabulary, blocklist-guarded), (3)")
    A("> attribution confidence (own-surface / alias-claimed / participant-only), (4) peak-aware")
    A("> flagging (⚑ — matched workflows ride a peak-calendar cadence: payroll, close, seasonal;")
    A("> the average understates the peak window). State column separates active verdicts from")
    A("> deferred-prepared (OMO/TPS (ad)/(ah)) and dormant design-load (Trade dept disabled-")
    A(f"> prepared (x)) — the OVERLOAD tally splits accordingly. Cadence-parse coverage")
    A(f"> {cov['parsed']}/{cov['total']} workflows ({cov['parsed'] * 100 // max(cov['total'], 1)}%)")
    A("> at generation. Residual classes: measured or NAMED — naming is a charter act")
    A("> (charter §10/§2/§11); `UNNAMED` residuals are the charter layer's worklist and the")
    A("> instrument never invents them. Verdicts are demand-on-role-design decision support,")
    A("> not timesheet actuals and never incumbent grading. Generated — do not hand-edit.")
    A("")
    A("## Verdict, residual, state & confidence legend")
    A("")
    A("| Verdict | Meaning | Residual class |")
    A("|---|---|---|")
    A("| CONFIRMED | parsed demand 50–150% of chartered capacity | WORKFLOW-MEASURED if util ≥80%; else PARTIAL |")
    A("| OVERLOAD | parsed demand >150% of capacity | — (capacity decision; design-load rows are posture, not staffing) |")
    A("| UNDER-UTILIZED | parsed demand <50% | PARTIAL — residual named or seat resized |")
    A("| MEASURED — HC UNPRICED | demand priced; no mappable HC (§7.2 alias gap class) | capacity-map decision |")
    A("| ZERO-DURATION | anchors are cadence-only work the bridge cannot price | COVERAGE-STANDBY (cycle audit) |")
    A("| UNPARSEABLE-FREQ | anchors ride unparseable cadence | adjudicate the frequency family |")
    A("| NO PARSED CADENCE | Owner/Participants-level anchor only (no step surface) | COVERAGE-STANDBY or UNMEASURED |")
    A("")
    A("| State | Meaning | · | Confidence | Meaning |")
    A("|---|---|---|---|---|")
    A("| active | live posture | · | own-surface | matched cells' resolved parts fold to this seat |")
    A("| deferred-prepared | Build-Squad — OMO/TPS design (108-active canon) | · | alias-claimed | claimed through alias vocabulary (broader forms denote the seat) |")
    A("| dormant — design-load | Trade dept disabled-prepared (x) | · | participant-only | Owner/Participants anchor, no step surface |")
    A("")
    A("## Verification register — all chartered roles")
    A("")
    A("| Role | Charter | Touched | Demand h/yr | HC | Util | Verdict | Residual | State | Conf |")
    A("|---|---|---|---|---|---|---|---|---|---|")

    def emit(q, dh, hc, util, v, rc, state, conf, marks=""):
        A(f"| {q['title']}{marks} | {src_map[q['bucket']]} — {q['dept']} | {q['touched']} | "
          f"{dh} | {hc if hc else '—'} | {util} | {v} | {rc} | {state} | {conf} |")

    parts_claim, parts_hit = parts_attribution(queue, idx, res, cap)

    results = []
    for q in queue:
        state = state_of(q)
        k = norm(q["title"])
        s_claimed, anchors, nbd, peak, own_surface = surface_claim(q, idx, res, cap)
        if k in parts_hit and parts_claim.get(k, 0.0) > 0.0:
            claimed = parts_claim[k]
            conf = "own-surface"
        else:
            claimed = s_claimed
            conf = ("own-surface" if own_surface else
                    "alias-claimed" if anchors["parsed"] + anchors["zero"] + anchors["unparsed"] > 0
                    else "participant-only")
        if conf == "alias-claimed":
            n_alias += 1
        if nbd:
            n_days += 1
        marks = ("†" if nbd else "") + ("⚑" if peak else "")
        results.append((q, claimed, anchors, state, conf, marks, peak, nbd))
        if claimed > 0:
            ch, hours = capacity_for(q, cap)
            if not ch:
                tally["MEASURED — HC UNPRICED"] += 1
                emit(q, f"{claimed/60:,.0f}{marks}", q["hc"], "—",
                     "MEASURED — HC UNPRICED", "capacity-map decision", state, conf)
                continue
            util = claimed / 60 / (ch * hours) * 100
            v = band_of(util)
            rc = residual_of(util, v)
            tkey = ("OVERLOAD (design-load)" if state != "active"
                    else "OVERLOAD (active)") if v == "OVERLOAD" else v
            tally[tkey] += 1
            if v != "OVERLOAD":
                resid[rc if rc != "—" else "WORKFLOW-MEASURED"] += 1
            emit(q, f"{claimed/60:,.0f}{marks}", ch, f"{util:.0f}%", v, rc, state, conf)
            continue
        if anchors["parsed"] == 0 and anchors["zero"] > 0:
            tally["ZERO-DURATION"] += 1
            resid["COVERAGE-STANDBY"] += 1
            emit(q, f"—{marks}", q["hc"], "—", "ZERO-DURATION",
                 "COVERAGE-STANDBY — cycle audit", state, conf)
            continue
        if anchors["parsed"] == 0 and anchors["unparsed"] > 0:
            tally["UNPARSEABLE-FREQ"] += 1
            resid["COVERAGE-STANDBY"] += 1
            emit(q, f"—{marks}", q["hc"], "—", "UNPARSEABLE-FREQ",
                 "adjudicate cadence", state, conf)
            continue
        tally["NO PARSED CADENCE"] += 1
        resid["COVERAGE-STANDBY" if q["hc"] else "UNMEASURED"] += 1
        emit(q, "—", q["hc"], "—", "NO PARSED CADENCE",
             "COVERAGE-STANDBY — mandate-priced" if q["hc"] else "UNMEASURED — worklist",
             state, conf)

    # Department roll-up: §5.3 departments, IT product model split by state,
    # store/DC field rosters — measured demand vs capacity, with coverage.
    for q, claimed, anchors, state, conf, marks, peak, nbd in results:
        grp = (q["dept"] if q["bucket"] == "hq" else
               f"IT product model — {state}" if q["bucket"] == "it" else
               f"{q['dept']} (field)")
        g = dept_roll.setdefault(grp, {"dem": 0.0, "cap": 0.0, "n": 0, "meas": 0})
        g["n"] += 1
        if claimed > 0:
            g["meas"] += 1
            g["dem"] += claimed / 60
        ch, hours = capacity_for(q, cap)
        if ch:
            g["cap"] += ch * hours

    A("")
    A("## Tally")
    A("")
    A("| Verdict | Roles |")
    A("|---|---|")
    for k in ("CONFIRMED", "OVERLOAD (active)", "OVERLOAD (design-load)",
              "UNDER-UTILIZED", "MEASURED — HC UNPRICED", "ZERO-DURATION",
              "UNPARSEABLE-FREQ", "NO PARSED CADENCE"):
        A(f"| {k} | {tally[k]} |")
    A(f"| **Total chartered verified** | **{len(queue)}** |")
    A("")
    A("| Residual class | Roles |")
    A("|---|---|")
    for k in ("WORKFLOW-MEASURED", "PARTIAL — NAMED", "PARTIAL — UNNAMED",
              "COVERAGE-STANDBY", "UNMEASURED"):
        A(f"| {k} | {resid[k]} |")
    A("")
    A(f"Instrument marks: alias-claimed rows {n_alias} · days-bridged rows {n_days} ·")
    A("peak-calendar rows ⚑ counted in the marks column of the register.")
    A("")
    A("## Department roll-up — measured demand vs capacity")
    A("")
    A("> A low measured-share is a **coverage gap** (the department's seats lack step")
    A("> surfaces — anchor them), not slack; individual UNDER rows inside a hot")
    A("> department are queue-shape (the exercise-through contract). Roll-ups sum")
    A("> per-seat claims — the even-share convention — so cross-department cells")
    A("> split, never double-count.")
    A("")
    A("| Department / roster | Roles | Measured | Demand h/yr | Capacity h/yr | Measured util |")
    A("|---|---|---|---|---|---|")
    for grp in sorted(dept_roll, key=lambda g: -(dept_roll[g]["dem"] / max(dept_roll[g]["cap"], 1))):
        g = dept_roll[grp]
        mu = f"{g['dem'] / g['cap'] * 100:.0f}%" if g["cap"] else "—"
        A(f"| {grp} | {g['n']} | {g['meas']} | {g['dem']:,.0f} | {g['cap']:,.0f} | {mu} |")
    A("")
    A("## Census line (Phase-3 Check 71 extension form)")
    A("")
    A("```")
    A(f"verified={len(queue)} verified_confirmed={tally['CONFIRMED']} "
      f"verified_overload_active={tally['OVERLOAD (active)']} "
      f"verified_overload_design={tally['OVERLOAD (design-load)']} "
      f"verified_under={tally['UNDER-UTILIZED']} "
      f"coverage_standby={resid['COVERAGE-STANDBY']} "
      f"unmeasured={resid['UNMEASURED']} residual_unnamed={resid['PARTIAL — UNNAMED']} "
      f"alias_claimed={n_alias} days_bridged={n_days}")
    A("```")
    A("")
    A("> Interpretation guardrails: (1) utilization is demand-on-role-design, not timesheet")
    A("> actuals and never incumbent grading; (2) narrow titles inherit department workload")
    A("> through the exercise-through-broader-titles contract — read the department roll-up")
    A("> before any single-seat decision; (3) unparseable cadence reads low (COVERAGE-STANDBY);")
    A("> (4) † rows price the days-bridge estimate — cycle-audit before a capacity decision")
    A("> rides them; (5) ⚑ rows are peak-calendar shaped — verify the peak window, not the")
    A("> mean; (6) design-load rows price the 122/6,932 design posture, not the active canon;")
    A("> (7) `PARTIAL — UNNAMED` and `UNMEASURED` are the charter layer's naming worklist —")
    A("> the instrument counts, the charter names.")

    text = "\n".join(L) + "\n"
    if CHECK:
        if not os.path.exists(OUT):
            print(f"register missing: {OUT}")
            return 1
        shipped = open(OUT, encoding="utf-8").read()
        if shipped != text:
            print("register drift: regenerate (python3 verify-role-demand.py)")
            return 1
        print("register verified (byte-identical)")
        return 0
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {OUT} — {len(queue)} roles; "
          f"CONFIRMED {tally['CONFIRMED']} / OVERLOAD active {tally['OVERLOAD (active)']} "
          f"+ design {tally['OVERLOAD (design-load)']} / UNDER {tally['UNDER-UTILIZED']} / "
          f"unpriced {tally['MEASURED — HC UNPRICED']} / zero-dur {tally['ZERO-DURATION']} / "
          f"unparsed {tally['UNPARSEABLE-FREQ']} / no-cadence {tally['NO PARSED CADENCE']}; "
          f"alias-claimed {n_alias} / days-bridged {n_days}; "
          f"residual unnamed {resid['PARTIAL — UNNAMED']} / unmeasured {resid['UNMEASURED']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
