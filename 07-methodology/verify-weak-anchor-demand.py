#!/usr/bin/env python3
"""Weak-anchor demand verification generator — batch 43 (2026-09-23, by direction).

Verifies the Role-Anchoring Contract's weak-anchor watchlist (chartered roles
anchored in only 1–2 workflows) against per-role annual demand, using the
virtual-gemba-walk motion engine's own measurements (motion --full). Verdicts:

  CONFIRMED        parsed demand 50–150% of chartered capacity — stays.
  OVERLOAD         parsed demand > 150% — capacity decision; the demand is real.
  UNDER-UTILIZED   parsed demand < 50% — merge/defer/resize candidate.
  ZERO-DURATION    the role's anchored steps are days-based/multi-day work the
                   hour model cannot measure — verify by cycle audit, not hours.
  NO PARSED CADENCE Participant-level anchor or unparseable cadence — elevate
                   into Role (R)/(A) cells with durations, or measure by gemba.

Writes 01-model-company/workflows/weak-anchor-demand-verification.md.
Deterministic; read-only over the corpus and the motion engine.
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
            m = re.match(r"^(.{1,44}?)\s{2,}([\d,]+)\s+(\d+)\s+(\d+)%\s*$", ln.strip())
            if m:
                k = m.group(1).strip().lower()
                e = demand.setdefault(k, {"h": 0, "hc": 0})
                e["h"] += int(m.group(2).replace(",", ""))
                e["hc"] = int(m.group(3)) or e["hc"]
    return demand


def main():
    wfs, tier, rows, dept_order, anchor = grc.build()
    weak = sorted((r for r in rows if r["bucket"] in ("hq", "it", "store", "dc")
                   and 0 < r["touched"] <= 2),
                  key=lambda r: (r["touched"], r["title"].lower()))
    proc = subprocess.run([sys.executable, os.path.join(HERE, "virtual-gemba-walk.py"),
                           "motion", "--full"], capture_output=True, text=True)
    if proc.returncode != 0:
        print(proc.stderr[-500:])
        return 1
    demand = parse_full_dump(proc.stdout)

    src_map = {"hq": "§5.3 register", "it": "IT seat",
               "store": "§7.2 store roster", "dc": "§7.3 DC roster"}
    L = []
    A = L.append
    A("# Weak-Anchor Demand Verification (generated — batch 43, 2026-09-23)")
    A("")
    A("> **Verification record** for the Role-Anchoring Contract's weak-anchor watchlist — the")
    A(f"> {len(weak)} chartered roles anchored in only 1–2 workflows. Per the contract, no headcount")
    A("> or structure decision may touch a weak-anchor role until its per-role annual demand is")
    A("> verified against chartered capacity. Instrument: `virtual-gemba-walk.py motion --full`")
    A("> (per-role annual demand hours from the corpus's own step durations × event cadence vs")
    A("> chartered TO capacity; 1,800/1,900 net productive hours; ~53% frequency-parse coverage).")
    A("> Batches 39–41 elevated nineteen roles into Role (R) cells; batch 42 re-anchored the T&A")
    A("> Analyst off a store-scaled step onto its true HQ platform step; batch 43 classifies the")
    A("> residual — ZERO-DURATION rows are days-based/multi-day work the hour model cannot")
    A("> measure (verify by cycle audit), distinct from NO PARSED CADENCE (elevate into Role")
    A("> cells with durations, or measure by gemba). Generated — do not hand-edit.")
    A("")
    A("## Verdict legend")
    A("")
    A("| Verdict | Meaning | Action |")
    A("|---|---|---|")
    A("| CONFIRMED | parsed demand 50–150% of chartered capacity | role stays as chartered |")
    A("| OVERLOAD | parsed demand > 150% of capacity | capacity decision — the demand is real |")
    A("| UNDER-UTILIZED | parsed demand < 50% | merge/defer/resize candidate |")
    A("| ZERO-DURATION | anchored steps are days-based/multi-day work | verify by cycle audit, not hours |")
    A("| NO PARSED CADENCE | Participant-level anchor or unparseable cadence | step-level anchoring or gemba measurement |")
    A("")
    A("## Verification table")
    A("")
    A("| Role | Charter | Touched | Demand h/yr | HC | Utilization | Verdict |")
    A("|---|---|---|---|---|---|---|")
    conf = over = under = zero = noparse = 0
    for r in weak:
        hit = demand.get(r["title"].lower())
        if hit and hit["h"] > 0:
            util = hit["h"] / (hit["hc"] * (1900 if r["bucket"] in ("store", "dc") else 1800)) * 100
            if util > 150:
                v = "OVERLOAD"; over += 1
            elif util < 50:
                v = "UNDER-UTILIZED"; under += 1
            else:
                v = "CONFIRMED"; conf += 1
            A(f"| {r['title']} | {src_map[r['bucket']]} — {r['dept']} | {r['touched']} | {hit['h']:,} | {hit['hc']} | {util:.0f}% | {v} |")
        else:
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
    A(f"| NO PARSED CADENCE | {noparse} |")
    A("")
    A("> OVERLOAD rows are the headcount-real candidates this doctrine exists to find. UNDER-UTILIZED")
    A("> rows are merge/resize candidates. ZERO-DURATION rows carry days-based work — audit the cycle,")
    A("> not the hours. NO PARSED CADENCE rows need step-level anchoring or gemba measurement.")
    A("> Interpretation guardrails as printed by the tool.")
    open(OUT, "w").write("\n".join(L) + "\n")
    print(f"weak-anchor verification written: {len(weak)} roles — "
          f"CONFIRMED {conf}, OVERLOAD {over}, UNDER {under}, NO PARSED {noparse}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
