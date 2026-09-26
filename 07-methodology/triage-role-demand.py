#!/usr/bin/env python3
r"""P2 disposition triage for the universal role-demand register (batch 53).

Reads the same machinery as verify-role-demand.py (census join, parts
attribution, capacity pricing, state) and adds SOURCE TRACKING — for every
chartered role, the per-cell contributions behind its demand — so the
register's OVERLOAD/UNDER rows can be triaged into disposition classes before
any corpus or capacity decision (the batch-51 disposition discipline: no
decision before the evidence is read).

Classes (auto-assigned, evidence shown — a class is a hypothesis until the
disposition note says otherwise):

  SCALE-ARTIFACT (field-exec × HQ charter)
      ≥60% of the role's demand arises from store/DC-executed step cells
      (event ladders ×200 stores / ×4 DCs) while its capacity is priced
      against HQ register HC — the W2201 class. Disposition path: per-cell
      adjudication (whose work is it at store grain? re-point to the field
      seat, or re-scope the frequency parenthetical), then re-derive.
  CELL-AUDIT (concentration)
      One cell carries ≥50% of the role's demand — a per-occurrence subset
      rate, a misparsed cadence, or a genuinely oversized cell. Disposition
      path: read the cell (batch-51's W837/W1365 precedents), fix or confirm.
  FIELD-SIGNAL (chain vs roster pricing)
      Field-roster role, demand chain-wide vs the roster multiplier — verify
      per-site arithmetic before any roster decision.
  DISTRIBUTED (real-signal candidate)
      Demand spread across cells/workflows with aligned buckets — a capacity
      decision candidate on the evidence as it stands.

Also emits the charter naming worklist (P1 interface): priced roles whose
residual is PARTIAL — UNNAMED plus the UNMEASURED rows, ranked by unnamed
hours (capacity h/yr minus measured demand h/yr) — the charter layer's
prioritized queue (naming is a charter act; the instrument counts).

Writes 01-model-company/workflows/role-demand-disposition-queue.md.
Deterministic; read-only over the corpus and the engine. --check byte-compares.
Unpinned — a Phase-3 candidate after the P2 dispositions settle.
"""
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
OUT = os.path.join(REPO, "01-model-company", "workflows",
                   "role-demand-disposition-queue.md")
CHECK = "--check" in sys.argv


def load(n, f):
    s = importlib.util.spec_from_file_location(n, os.path.join(HERE, f))
    m = importlib.util.module_from_spec(s)
    sys.modules[n] = m
    s.loader.exec_module(m)
    return m


grc = load("grc", "generate-role-coverage.py")
sys.argv = ["vrd"] + sys.argv[1:]
vrd = load("vrd", "verify-role-demand.py")
vgw = vrd.vgw
norm = vrd.norm


PER_UNIT_RE = re.compile(
    r"/(guide|campaign|event|delivery|audit|review|incident|case|exception|"
    r"investigation|signup|occurrence|item|sku|request|claim|batch|file|report|"
    r"terminal|store|vendor|partner|appraisal)s?\b|"
    r"\bper (guide|campaign|event|delivery|audit|review|incident|case|exception|"
    r"investigation|signup|occurrence|item|sku|request|claim|batch|file|report|"
    r"terminal|store|vendor|partner)\b", re.I)
PERIOD_MIN_RE = re.compile(
    r"\d+(?:[.,]\d+)?\s*(?:min(?:s)?|hours?|hrs?|h)\s*/\s*(day|week|month|year)",
    re.I)


def grammar_gap(raw):
    """Evidence marker for the two engine grammar-gap families behind the
    worst OVERLOADs (batch-53 observation): per-unit qualifier forms outside
    the batch-51 symbolic family ('8–12 hours/guide', '2–4 hours per
    campaign', '1-2 hours' × per-delivery) and min/day-style period cells the
    step-period ladder misses ('30 min/day')."""
    if PER_UNIT_RE.search(raw):
        return "PER-UNIT?"
    if PERIOD_MIN_RE.search(raw):
        return "PERIOD?"
    return ""


def main():
    _wfs, tier, rows, dept_order, anchor = grc.build()
    row_by = {}
    for r in rows:
        row_by.setdefault((grc.key(r["title"]), r["bucket"]), r)
    queue = []
    for k, c in anchor["chartered"].items():
        r = row_by.get((k, c["bucket"]))
        if r:
            queue.append({"title": c["title"], "bucket": c["bucket"], "dept": c["dept"],
                          "hc": c["hc"] or r["hc"], "touched": r["touched"]})
    queue.sort(key=lambda r: (r["touched"], r["title"].lower()))

    hq_toc, dc_toc, store_toc, dept_toc = grc.parse_toc()
    res = grc.Resolver(hq_toc, dc_toc, store_toc, dept_toc)
    cap, _h, _s, _d = vgw.build_capacity(vrd.grc2, res)
    wfs = vgw.parse_workflows()
    idx, cov = vrd.build_index(res, wfs)

    # ---- attribution with source tracking (mirrors parts_attribution) ----
    fold_of = {}
    for q in queue:
        b = q["bucket"] if q["bucket"] in ("store", "dc") else "hq"
        fold_of.setdefault(vgw.fold_capacity_key(cap, norm(q["title"]), b), []).append(q)
    claim = {norm(q["title"]): 0.0 for q in queue}
    by_bucket_min = {norm(q["title"]): {"hq": 0.0, "store": 0.0, "dc": 0.0} for q in queue}
    contrib = {norm(q["title"]): {} for q in queue}   # role -> {(wfid, step, act, raw, freq, bucket): minutes}
    hit = set()
    wf_by_id = {w["id"]: w for w in wfs}
    # (source tracking needs occurrence granularity — walk wfs directly)
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
        if ev is None:
            continue
        raws = w.get("steps_raw") or [""] * len(w["steps"])
        acts = w.get("steps_act") or [""] * len(w["steps"])
        periods = w.get("step_period") or [None] * len(w["steps"])
        for si, (dur, r, a) in enumerate(w["steps"]):
            if dur <= 0:
                continue
            roles = vgw.role_parts(r, res)
            if not roles:
                continue
            pm = periods[si] if si < len(periods) else None
            mult = pm if pm else ev
            share = dur / len(roles) * mult
            for _p, _b, t in roles:
                fk = vgw.fold_capacity_key(cap, norm(t), exec_bucket)
                for q in fold_of.get(fk, ()):
                    k = norm(q["title"])
                    claim[k] += share
                    by_bucket_min[k][exec_bucket] += share
                    hit.add(k)
                    key = (w["id"], si + 1, acts[si][:60] if si < len(acts) else "",
                           raws[si] if si < len(raws) else "", w["freq"][:60], exec_bucket)
                    contrib[k][key] = contrib[k].get(key, 0.0) + share

    # ---- verdicts (mirror the register's ladder) ----
    over_rows, under_rows, naming = [], [], []
    for q in queue:
        k = norm(q["title"])
        state = vrd.state_of(q)
        if k not in hit or claim[k] <= 0:
            continue
        ch, hours = vrd.capacity_for(q, cap)
        if not ch:
            continue
        cap_h = ch * hours
        dem_h = claim[k] / 60
        util = dem_h / cap_h * 100
        if util > 150 and state == "active":
            tb = by_bucket_min[k]
            tot = max(claim[k], 1e-9)
            field_share = (tb["store"] + tb["dc"]) / tot
            top = sorted(contrib[k].items(), key=lambda x: -x[1])
            top1_share = top[0][1] / tot if top else 0
            if q["bucket"] == "hq" and field_share >= 0.6:
                cls = "SCALE-ARTIFACT (field-exec × HQ charter)"
            elif top1_share >= 0.5:
                cls = "CELL-AUDIT (concentration)"
            elif q["bucket"] in ("store", "dc"):
                cls = "FIELD-SIGNAL (chain vs roster pricing)"
            else:
                cls = "DISTRIBUTED (real-signal candidate)"
            over_rows.append((q, dem_h, util, field_share, top, cls))
        elif util < 80:
            naming.append((q, dem_h, cap_h, util))

    over_rows.sort(key=lambda x: -x[2])
    naming_unnamed = [n for n in naming if n[3] < 5]
    naming.sort(key=lambda n: -(n[2] - n[1]))

    L = []
    A = L.append
    gap_rows = 0
    A("# Role-Demand Disposition Queue — P2 triage (generated — batch 53, 2026-09-26)")
    A("")
    A("> **P2 worklist** for the universal register")
    A("> ([role-demand-verification.md](role-demand-verification.md), batch 52b): every")
    A(f"> active-state OVERLOAD row ({len(over_rows)}) with its evidence — the per-cell")
    A("> contributions behind the demand — auto-classified for disposition, plus the")
    A("> charter naming worklist ranked by unnamed hours. A class is a hypothesis until")
    A("> the disposition note says otherwise; no headcount or corpus decision rides a")
    A("> class label alone (the batch-51 discipline: read the cell, then re-point,")
    A("> re-scope, or confirm — and re-derive). Cadence-parse coverage")
    A(f"> {cov['parsed']}/{cov['total']} workflows at generation. Generated — do not hand-edit.")
    A("")
    A("## P2-A — OVERLOAD (active) triage")
    A("")
    A("| Role | Dept | Demand h/yr | Util | Field-exec share | Top contributing cell | Class |")
    A("|---|---|---|---|---|---|---|")
    for q, dem_h, util, fs, top, cls in over_rows:
        if top:
            (wfid, step_no, act, raw, freq, bucket) = top[0][0]
            mins = top[0][1] / 60
            gm = grammar_gap(raw)
            if gm:
                gap_rows += 1
            act = act.replace("**", "'").replace("|", "/")[:44]
            raw = raw.replace("|", "/")
            cell = (f"{wfid} s{step_no} “{act}” {raw} · {freq[:36]} · "
                    f"{bucket}-exec · {mins:,.0f} h/yr"
                    + (f" · {gm}" if gm else ""))
        else:
            cell = "—"
        A(f"| {q['title']} | {q['dept']} | {dem_h:,.0f} | {util:.0f}% | {fs*100:.0f}% | "
          f"{cell} | {cls} |")
    A("")
    A("## P2-B — class tally & disposition paths")
    A("")
    cls_count = {}
    for *_x, cls in over_rows:
        cls_count[cls] = cls_count.get(cls, 0) + 1
    A("| Class | Roles | Disposition path |")
    A("|---|---|---|")
    paths = {
        "SCALE-ARTIFACT (field-exec × HQ charter)":
            "Per-cell adjudication: whose work is it at store/DC grain? Re-point to the field seat (the W837 precedent) or fix the frequency parenthetical (the W2201 precedent); re-derive.",
        "CELL-AUDIT (concentration)":
            "Read the top cell: per-occurrence subset rate, misparsed cadence, or genuinely oversized cell (the W1365 / W942 precedents); fix or confirm, then re-derive.",
        "FIELD-SIGNAL (chain vs roster pricing)":
            "Verify per-site arithmetic (events ladder × site multiplier vs roster complement) before any roster decision; the §7.2/§7.3 rosters price per-site.",
        "DISTRIBUTED (real-signal candidate)":
            "Capacity decision on the evidence as it stands — resize, split, or accept with a named residual; the demand is spread, not an artifact.",
    }
    for cls in ("SCALE-ARTIFACT (field-exec × HQ charter)", "CELL-AUDIT (concentration)",
                "FIELD-SIGNAL (chain vs roster pricing)", "DISTRIBUTED (real-signal candidate)"):
        A(f"| {cls} | {cls_count.get(cls, 0)} | {paths[cls]} |")
    A("")
    A(f"**Engine grammar-gap sensitivity:** {gap_rows} of {len(over_rows)} OVERLOAD rows")
    A("have a `PER-UNIT?` / `PERIOD?` top cell — per-unit qualifier forms outside")
    A("the batch-51 symbolic family ('8–12 hours/guide', '2–4 hours per campaign',")
    A("'1-2 hours' × per-delivery) and min/day-style period cells ('30 min/day').")
    A("These are engine-grammar candidates first (batch-49/51 precedent): extend the")
    A("symbolic family and the period ladder, re-derive, and re-adjudicate the pin —")
    A("the OVERLOAD population is expected to shrink materially before any capacity")
    A("decision is taken. Not fixed in this batch: engine grammar changes move the")
    A("batch-51 pin and are a conscious re-adjudication by direction.")
    A("")
    A("## P2-C — charter naming worklist (P1 interface), ranked by unnamed hours")
    A("")
    A("> Priced roles under 80% utilization: `unnamed hours = capacity − measured")
    A("> demand`. Naming is a charter act (§10 definition-of-done / §2 mission / §11")
    A("> coverage) — this queue ranks where naming buys the most explained capacity.")
    A("> Top 30 shown; util < 5% rows are the PARTIAL — UNNAMED register class.")
    A("")
    A("| Role | Dept | Util | Unnamed h/yr | HC |")
    A("|---|---|---|---|---|")
    for q, dem_h, cap_h, util in naming[:30]:
        A(f"| {q['title']} | {q['dept']} | {util:.0f}% | {max(0.0, cap_h - dem_h):,.0f} | {q['hc'] or '—'} |")
    A("")
    A(f"(Full naming queue: {len(naming)} priced roles under 80%; of these")
    A(f"{len(naming_unnamed)} sit under 5% — the register's PARTIAL — UNNAMED class.)")
    A("")
    A("> Guardrails: verdicts price role design, never incumbents; classes are")
    A("> hypotheses with evidence attached; every disposition re-derives the register")
    A("> (movement is conscious re-adjudication, never silent).")

    text = "\n".join(L) + "\n"
    if CHECK:
        if not os.path.exists(OUT) or open(OUT, encoding="utf-8").read() != text:
            print("queue drift or missing: regenerate (python3 triage-role-demand.py)")
            return 1
        print("queue verified (byte-identical)")
        return 0
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(text)
    cc = ", ".join(f"{c.split(' ')[0]} {n}" for c, n in cls_count.items())
    print(f"wrote {OUT} — {len(over_rows)} OVERLOAD triaged ({cc}); "
          f"naming queue {len(naming)} (top unnamed hours shown)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
