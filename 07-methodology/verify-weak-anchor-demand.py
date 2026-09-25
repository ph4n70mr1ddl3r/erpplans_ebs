#!/usr/bin/env python3
r"""Weak-anchor demand verification generator — batch 49 (2026-09-25, by direction).

Verifies the Role-Anchoring Contract's weak-anchor watchlist (chartered roles
anchored in only 1–2 workflows) against per-role annual demand, using the
virtual-gemba-walk motion engine's own measurements (motion --full). Verdicts:

  CONFIRMED        parsed demand 50–150% of chartered capacity — stays.
  OVERLOAD         parsed demand > 150% — capacity decision; the demand is real.
  UNDER-UTILIZED   parsed demand < 50% — merge/defer/resize candidate.
  EXERCISED-THROUGH
                   the role's own key carries no engine demand, but its named
                   step cells do (attributed to the broader/deputy seats the
                   cells resolve to, per the corpus's exercise-through-broader-
                   titles contract). Demand = the role's claimed share of its
                   named cells (engine share arithmetic), via = the folded keys
                   it lands on; band applied against the role's own charter.
  MEASURED — CAPACITY UNMAPPED
                   the role's own key carries engine-priced demand, but the
                   TO-based capacity map prices no HC for it (IT product-model
                   seats — the TO defers the department by reference — and the
                   §7.2 ASM roster-abbreviation alias gap). Demand is shown;
                   utilization needs a capacity-map decision, not a silent fold.
  ZERO-DURATION    the role's anchored steps are days-based/multi-day work the
                   hour model cannot measure — verify by cycle audit, not hours.
  NO PARSED CADENCE Participant-level anchor or unparseable cadence — elevate
                   into Role (R)/(A) cells with durations, or measure by gemba.

Batch 49 defects fixed (both found by the make-everything-measurable pass):
  1. ENGINE: virtual-gemba-walk.parse_minutes returned 0.0 for every plural
     unit form ('2 hours', '4 hrs', '30 mins', '24 hours/year') — the unit
     alternation bound the singular stem and the trailing \b could not bind
     before the 's'; 3,775 corpus duration cells (11%) silently measured zero,
     which had misclassified 20 batch-39–47 step-elevated roles as
     ZERO-DURATION/NO PARSED CADENCE. Fixed in the engine (plural-capable
     unit alternation); every figure in this report is re-derived post-fix.
  2. THIS TOOL: parse_full_dump's utilization group was (\d+)% — utilizations
     ≥ 100,000% print thousands-separated and were silently dropped from the
     parsed dump (e.g. store-floor roles at xSTORES cadence), reading as NO
     PARSED CADENCE. Group is now comma-tolerant.
  3. THIS TOOL: the exercised-through arm above — roles whose named cells
     attribute to broader seats are now measured instead of reported empty.

Writes 01-model-company/workflows/weak-anchor-demand-verification.md.
Deterministic; read-only over the corpus and the motion engine.
`--check` re-derives the report in memory and byte-compares it against the
shipped file (no write; exit 1 on drift) — wired into validate-repo.sh
Check 80 by the 2026-09-23 eighty-second-wave consistency review.
"""
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
OUT = os.path.join(REPO, "01-model-company", "workflows",
                   "weak-anchor-demand-verification.md")

# Capture BEFORE the imports: vgw.load_grc() rebinds sys.argv (the same
# lesson virtual-gemba-walk.py's MOTION_FULL flag records) — a flag read
# inside main() would always see the rebound argv and never fire.
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


def parse_full_dump(text):
    demand = {}
    started = False
    for ln in text.splitlines():
        if ln.startswith("All mapped roles"):
            started = True
            continue
        if started:
            # batch 49: utilization group is comma-tolerant — utilizations
            # ≥ 100,000% print thousands-separated and the old (\d+)% group
            # silently dropped every such row from the parsed dump.
            m = re.match(r"^(.{1,44}?)\s{2,}([\d,]+)\s+(\d+)\s+([\d,]+)%\s*$", ln.strip())
            if m:
                k = m.group(1).strip().lower()
                e = demand.setdefault(k, {"h": 0, "hc": 0})
                e["h"] += int(m.group(2).replace(",", ""))
                e["hc"] = int(m.group(3)) or e["hc"]
    return demand


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def exercised_demand(title, res, cap, wfs):
    """(own_minutes, via, anchors) — walks the steps that NAME the role
    (word-boundary surface match) with mode_motion's attribution arithmetic
    exactly (workflow exec-bucket detection with its early store-break, the
    events ladder, even share split across the cell's resolvable parts).
    own_minutes = the share of cells whose resolved parts include the role's
    own key (demand the engine also counts, but prices against no chartered
    HC — IT product-model seats the TO carries by reference, and the §7.2
    roster-abbreviation alias gap). via maps each OTHER folded demand key the
    named cells land on to the minutes routed there. anchors = (parsed, zero,
    unparsed) — named-cell counts by measurement state: on a parseable-
    frequency workflow with a parseable duration / on one with a zero or
    unparseable duration / on a workflow whose frequency fails the ladder."""
    pat = re.compile(r"(?<![a-z0-9])" + re.escape(norm(title)) + r"(?![a-z0-9])")
    own = 0.0
    via = {}
    anchors = {"parsed": 0, "zero": 0, "unparsed": 0}
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
        for si, (dur, r, a) in enumerate(w["steps"]):
            if not pat.search(norm(r)):
                continue
            roles = vgw.role_parts(r, res)
            if dur <= 0:
                anchors["zero"] += 1
                continue
            if ev is None:
                anchors["unparsed"] += 1
                continue
            anchors["parsed"] += 1
            if roles:
                periods = w.get("step_period") or [None] * len(w["steps"])
                pm = periods[si] if si < len(periods) else None
                mult = pm if pm else ev
                share = dur / len(roles) * mult
                for _p, _b, t in roles:
                    k = vgw.fold_capacity_key(cap, norm(t), exec_bucket)
                    if k == norm(title):
                        own += share
                    else:
                        via[k] = via.get(k, 0.0) + share
            else:
                # cell names the role but resolves to no org actor — the
                # engine counts it unattributed; credit the claim in full.
                own += dur * ev
    return own, via, anchors


def main():
    check = CHECK
    _wfs, tier, rows, dept_order, anchor = grc.build()
    weak = sorted((r for r in rows if r["bucket"] in ("hq", "it", "store", "dc")
                   and 0 < r["touched"] <= 2),
                  key=lambda r: (r["touched"], r["title"].lower()))
    wfs = vgw.parse_workflows()   # engine-shaped steps, for the exercised arm
    proc = subprocess.run([sys.executable, os.path.join(HERE, "virtual-gemba-walk.py"),
                           "motion", "--full"], capture_output=True, text=True)
    if proc.returncode != 0:
        print(proc.stderr[-500:])
        return 1
    demand = parse_full_dump(proc.stdout)

    # capacity map + resolver for the exercised-through arm (batch 49)
    hq_toc, dc_toc, store_toc, dept_toc = grc.parse_toc()
    res = grc.Resolver(hq_toc, dc_toc, store_toc, dept_toc)
    cap, _hq_total, _store_total, _dc_total = vgw.build_capacity(grc2, res)

    # coverage % re-derived from the same engine (was hardcoded '~53%' before the
    # (bd) parser extensions — a hardcoded figure contradicted the tool's own
    # coverage line on every motion re-run)
    cov = re.search(r"Annualization coverage: (\d[\d,]*)/(\d[\d,]*) workflows \((\d+)%\)",
                    proc.stdout)
    cov_pct = f"{cov.group(3)}%" if cov else "—"

    src_map = {"hq": "§5.3 register", "it": "IT seat",
               "store": "§7.2 store roster", "dc": "§7.3 DC roster"}
    L = []
    A = L.append
    A("# Weak-Anchor Demand Verification (generated — batch 51, 2026-09-25)")
    A("")
    A("> **Verification record** for the Role-Anchoring Contract's weak-anchor watchlist — the")
    A(f"> {len(weak)} chartered roles anchored in only 1–2 workflows. Per the contract, no headcount")
    A("> or structure decision may touch a weak-anchor role until its per-role annual demand is")
    A("> verified against chartered capacity. Instrument: `virtual-gemba-walk.py motion --full`")
    A("> (per-role annual demand hours from the corpus's own step durations × event cadence vs")
    A("> chartered TO capacity; 1,800/1,900 net productive hours; frequency-parse coverage "
      f"{cov_pct} at generation).")
    A("> Batches 39–41 elevated nineteen roles into Role (R) cells; batch 42 re-anchored the T&A")
    A("> Analyst off a store-scaled step onto its true HQ platform step; batch 43 classified the")
    A("> residual. **Batch 49 (2026-09-25) re-derived every figure after two measurement defects")
    A("> were fixed** — (1) the engine's parse_minutes read every plural unit form ('2 hours',")
    A("> '4 hrs', '24 hours/year') as zero minutes (3,775 corpus duration cells re-measured; 20")
    A("> batch-39–47 step-elevated roles had been misclassified as unmeasurable), and (2) this")
    A("> tool's dump parser silently dropped rows with thousands-separated utilizations — and")
    A("> added the EXERCISED-THROUGH arm: roles whose named cells attribute to the broader/deputy")
    A("> seats their cells resolve to (the corpus's exercise-through-broader-titles contract) are")
    A("> now measured at their claimed share instead of reported empty. **Batch 50 (2026-09-25, wave")
    A("> 7)** elevated the twelve participant-only roles that had a mandate-exact step (PA-04.1/.2/.3,")
    A("> PA-10.1, PA-27.2, PA-110.3, PA-113.1, PA-133.1, PA-138.2) and added the MEASURED — CAPACITY")
    A("> UNMAPPED arm for seats whose own-key demand prices against no mapped HC (the IT product-model")
    A("> seats the TO carries by reference; the ASM alias gap). Generated — do not hand-edit.")
    A("")
    A("## Verdict legend")
    A("")
    A("| Verdict | Meaning | Action |")
    A("|---|---|---|")
    A("| CONFIRMED | parsed demand 50–150% of chartered capacity | role stays as chartered |")
    A("| OVERLOAD | parsed demand > 150% of capacity | capacity decision — the demand is real |")
    A("| UNDER-UTILIZED | parsed demand < 50% | merge/defer/resize candidate |")
    A("| EXERCISED-THROUGH | the role's own key carries no engine demand, but its named step cells do — attributed to the broader/deputy seats the cells resolve to | demand shown is the role's claimed share of its named cells (band vs its own charter); verify the via-group before any seat decision |")
    A("| MEASURED — CAPACITY UNMAPPED | demand priced under the role's own key, but the TO-based capacity map carries no HC for it (IT product-model seats; §7.2 roster-abbreviation alias) | demand is real and shown; utilization needs a capacity-map decision — alias/adjudicate, then re-pin |")
    A("| ZERO-DURATION | step-anchored, but every named step's duration cell reads zero (days-based or cadence-only work) | verify by cycle audit, not hours |")
    A("| UNPARSEABLE-FREQ | step-anchored, but every anchor rides a workflow whose frequency fails the cadence ladder | adjudicate the frequency family, then re-derive |")
    A("| NO PARSED CADENCE | Participant-level anchor only | step-level anchoring or gemba measurement |")
    A("")
    A("## Verification table")
    A("")
    A("| Role | Charter | Touched | Demand h/yr | HC | Utilization | Verdict |")
    A("|---|---|---|---|---|---|---|")
    conf = over = under = exercised = measured = zero = unparsed = noparse = 0
    for r in weak:
        hit = demand.get(norm(r["title"]))
        if hit and hit["h"] > 0:
            util = hit["h"] / (hit["hc"] * (1900 if r["bucket"] in ("store", "dc") else 1800)) * 100
            if util > 150:
                v = "OVERLOAD"; over += 1
            elif util < 50:
                v = "UNDER-UTILIZED"; under += 1
            else:
                v = "CONFIRMED"; conf += 1
            A(f"| {r['title']} | {src_map[r['bucket']]} — {r['dept']} | {r['touched']} | {hit['h']:,} | {hit['hc']} | {util:.0f}% | {v} |")
            continue
        own, via, anchors = exercised_demand(r["title"], res, cap, wfs)
        if own > 0:
            # demand lands under the role's own key but the engine's capacity
            # map (parse_register) carries no HC for it — the TO defers the IT
            # department to the product model by reference (per-seat HC is a
            # team-sizing decision), and the §7.2 ASM roster abbreviation is
            # the standing alias gap. Measured, not priced.
            hc = r["hc"]
            measured += 1
            A(f"| {r['title']} | {src_map[r['bucket']]} — {r['dept']} | {r['touched']} | {own/60:,.0f} | {hc or '—'} | — | MEASURED — capacity unmapped |")
            continue
        if via:
            hc = r["hc"]
            via_total = sum(via.values())
            if hc:
                util = via_total / 60 / (hc * (1900 if r["bucket"] in ("store", "dc") else 1800)) * 100
                band = "OVERLOAD" if util > 150 else ("UNDER-UTILIZED" if util < 50 else "CONFIRMED")
                util_s = f"{util:.0f}%"
                label = f"EXERCISED-THROUGH ({band})"
            else:
                util_s, label = "—", "EXERCISED-THROUGH"
            via_s = "via " + ", ".join(sorted(via, key=via.get, reverse=True)[:3])
            exercised += 1
            A(f"| {r['title']} | {src_map[r['bucket']]} — {r['dept']} | {r['touched']} | {via_total/60:,.0f} | {hc or '—'} | {util_s} | {label} — {via_s} |")
            continue
        if anchors["parsed"] == 0 and anchors["zero"] > 0:
            # step-anchored, but every named step's duration reads zero —
            # days-based or cadence-only cells the hour model cannot price
            zero += 1
            A(f"| {r['title']} | {src_map[r['bucket']]} — {r['dept']} | {r['touched']} | — | {r['hc'] or '—'} | — | ZERO-DURATION |")
            continue
        if anchors["parsed"] == 0 and anchors["unparsed"] > 0:
            # step-anchored, but every anchor rides a workflow whose frequency
            # fails the cadence ladder
            unparsed += 1
            A(f"| {r['title']} | {src_map[r['bucket']]} — {r['dept']} | {r['touched']} | — | {r['hc'] or '—'} | — | UNPARSEABLE-FREQ |")
            continue
        noparse += 1
        A(f"| {r['title']} | {src_map[r['bucket']]} — {r['dept']} | {r['touched']} | — | {r['hc'] or '—'} | — | NO PARSED CADENCE |"
          .replace("| — |", "| — |", 1))
    A("")
    A("## Tally")
    A("")
    A("| Verdict | Roles |")
    A("|---|---|")
    A(f"| CONFIRMED | {conf} |")
    A(f"| OVERLOAD | {over} |")
    A(f"| UNDER-UTILIZED | {under} |")
    A(f"| EXERCISED-THROUGH | {exercised} |")
    A(f"| MEASURED — CAPACITY UNMAPPED | {measured} |")
    A(f"| ZERO-DURATION | {zero} |")
    A(f"| UNPARSEABLE-FREQ | {unparsed} |")
    A(f"| NO PARSED CADENCE | {noparse} |")
    A("")
    A("> OVERLOAD rows are the headcount-real candidates this doctrine exists to find. UNDER-UTILIZED")
    A("> rows are merge/resize candidates. EXERCISED-THROUGH rows are measured through the seats their")
    A("> cells resolve to — the via-group's aggregate utilization, not the row's, is the staffing signal;")
    A("> their demand column is the role's claimed share of its named cells. MEASURED — CAPACITY UNMAPPED")
    A("> rows carry real own-key demand against no mapped HC (IT product-model seats; the ASM alias gap).")
    A("> ZERO-DURATION rows are step-anchored on cells the hour model cannot price — audit the cycle,")
    A("> not the hours. UNPARSEABLE-FREQ rows await a cadence-family adjudication. NO PARSED CADENCE rows")
    A("> are participant-level only — the step-level anchoring backlog. Interpretation guardrails as printed by the tool.")
    out = "\n".join(L) + "\n"
    summary = (f"{len(weak)} roles — CONFIRMED {conf}, OVERLOAD {over}, "
               f"UNDER {under}, EXERCISED {exercised}, MEASURED-UNMAPPED {measured}, "
               f"ZERO-DUR {zero}, UNPARSEABLE-FREQ {unparsed}, NO PARSED {noparse}")
    if check:
        # Eighty-second-wave consistency review (2026-09-23): the shipped report
        # had no self-verification harness — every consistency wave verified it by
        # a manual no-op regeneration + diff (the CHANGELOG battery lines). --check
        # re-derives the report in memory and byte-compares it, the
        # role-coverage-gap-analysis.py --check pattern, so validate-repo.sh
        # Check 80 can gate the shipped artifact without writing.
        if not os.path.exists(OUT):
            print("report missing — run without --check to generate")
            return 1
        shipped = open(OUT, encoding="utf-8").read()
        if shipped == out:
            print(f"weak-anchor verification: byte-identical, OK — {summary}")
            return 0
        import difflib
        diff = list(difflib.unified_diff(shipped.splitlines(), out.splitlines(),
                                         "shipped", "re-derived", lineterm=""))
        print(f"weak-anchor verification DRIFT ({len(diff)} diff lines) — regenerate")
        for d in diff[:20]:
            print(d)
        return 1
    open(OUT, "w").write(out)
    print(f"weak-anchor verification written: {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
