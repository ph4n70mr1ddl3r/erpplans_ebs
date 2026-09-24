#!/usr/bin/env python3
"""Workflow→role coverage gap analyzer — 01-model-company/workflows/role-coverage-gap-analysis.md.

The reverse arm of the role-anchoring contract: the contract's matrix proves
every chartered role carries ≥1 explicit RACI anchor (role → workflow); this
analyzer measures how well the WORKFLOW CATALOG names its roles (workflow →
role) — where work is still owned or performed under department-grain,
generic or unchartered forms instead of the org of record's chartered titles.

Gap classes, measured over all 5,433 workflows under generate-role-coverage
build()'s own resolution semantics (whole-cell first, then the slash/dash
part fallback — compound owners resolve part-by-part):

  Class A — ROLE-LESS WORKFLOWS: no chartered role in any RACI cell (Owner,
     Participants, Step Role (R)/(A)). The hard accountability gaps; every
     one is listed in full. Workflows inside a registered dormancy estate
     (the (x) B2B disabled—prepared VS-11/43/107/68, the (ad) TPS VS-74/77,
     the (ah) OMO VS-60) are annotated as by-design retained-design scope,
     not defects — their owner cells cite the disabled department per the
     disable-not-delete doctrine.
  Class B — OWNER-GRAIN GAPS: the owner resolves to no chartered role while
     chartered roles are touched elsewhere in the workflow. Aggregated by the
     literal Owner-cell form (the vocabulary the catalog actually uses) with
     workflow and value-stream counts; the full per-workflow appendix follows.
  Class C — HEALTHY: ≥1 chartered owner. Count only.
  Register-coverage backlog — recurring owner forms that resolve only to
     department grain (no §5.3 register row charters them): the chartering /
     alias-promotion candidates for role-vocabulary governance (the wave-32
     precedent: promote via ROLE_ALIASES when the corpus form denotes an
     existing chartered title; charter the role when the function is real and
     unseated).
  Ownership-span view — top chartered owners by workflow count, and the
     participate-only chartered roles (anchored, own nothing) whose
     accountability may be understated.

Adjudication policy (recorded so the classes are governed, not just counted):
department-grain ownership is acceptable only where the work is genuinely
department-wide; a recurring owner form that denotes one seat's function is a
gap — remediate through the wave-32/36 role-vocabulary governance (alias
promotion to the chartered title, or chartering the seat) with the anchor
census re-pinned; the numbers only legitimately move downward for Classes
A/B (any increase forces conscious re-adjudication).

Deterministic, read-only over the corpus: no timestamps, sorted outputs.
`--check` re-derives and byte-compares the shipped report. The workflow
population is pinned (mismatch exits 1 — a corpus change intentionally moves
these numbers and must re-point this pin, the Check-71 CENSUS-pin contract).
"""
import importlib.util
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
OUT = os.path.join(REPO, "01-model-company", "workflows", "role-coverage-gap-analysis.md")

spec = importlib.util.spec_from_file_location(
    "grc", os.path.join(HERE, "generate-role-coverage.py"))
grc = importlib.util.module_from_spec(spec)
sys.modules["grc"] = grc
spec.loader.exec_module(grc)

POPULATION_PIN = 5433
CHARTERED = {"hq", "it", "store", "dc"}
# Registered dormancy estates (capability-sourcing register §4 / channel-
# capability registry): workflows here are retained design, not gaps.
ESTATES = {
    frozenset({11, 43, 107, 68}): "B2B estate disabled—prepared (x), registry CAP-B01–B04",
    frozenset({74, 77}): "TPS build squad deferred—prepared (ad), sourcing register §4",
    frozenset({60}): "OMO build squad deferred—prepared (ah), sourcing register §4",
}


def estate(vs):
    for vs_set, label in ESTATES.items():
        if vs in vs_set:
            return label
    return None


def resolve_all(res, raw):
    """build()'s touch semantics: whole-cell first, then the part fallback."""
    b, d, t, h = res.resolve(raw)
    if b != "unc":
        return [(b, t)]
    for sp in (grc.split_owner_parts, grc.split_owner_parts_w36):
        parts = sp(raw)
        if len(parts) > 1:
            rs = [res.resolve(p) for p in parts]
            if all(r[0] != "unc" for r in rs):
                return [(r[0], r[2]) for r in rs]
    return [(b, t)]


def esc(s):
    return s.replace("|", "\\|")


def analyze():
    wfs, tier, rows, dept_order, anchor = grc.build()
    res = grc.Resolver(*grc.parse_toc())

    class_a, class_b = [], []
    b_forms = defaultdict(lambda: {"n": 0, "vs": set(), "form": ""})
    span = defaultdict(int)
    for w in wfs:
        own = resolve_all(res, w["owner"])
        if w["owner"]:
            span[(own[0][0], own[0][1])] += 1
        touched = set(b for b, _ in own)
        for p in w["participants"]:
            touched |= {b for b, _ in resolve_all(res, p)}
        for r in w["step_r"] + w["step_a"]:
            touched |= {b for b, _ in resolve_all(res, r)}
        est = estate(w["vs"])
        if not touched & CHARTERED:
            class_a.append({"wid": w["id"], "title": w["title"], "vs": w["vs"],
                            "pa": w["pa"], "owner": grc.norm(w["owner"]) if w["owner"] else "—",
                            "est": est or ""})
        elif own[0][0] not in CHARTERED and not any(b in CHARTERED for b, _ in own):
            key = grc.norm(w["owner"])
            e = b_forms[key]
            e["n"] += 1
            e["vs"].add(w["vs"])
            e["form"] = " / ".join(t for _, t in own)
            class_b.append({"wid": w["id"], "title": w["title"], "vs": w["vs"],
                            "pa": w["pa"], "form": e["form"], "raw": key, "est": est or ""})

    class_a.sort(key=lambda r: (r["vs"], r["pa"], r["wid"]))
    class_b.sort(key=lambda r: (r["raw"], r["vs"], r["pa"], r["wid"]))
    part_only = sorted((r for r in rows if r["bucket"] in CHARTERED
                        and r["touched"] > 0 and r["own"] == 0),
                       key=lambda r: (r["touched"], r["title"].lower()))
    return wfs, class_a, class_b, span, part_only, anchor


def render(wfs, class_a, class_b, span, part_only, anchor):
    L = []
    a = L.append
    a("# Workflow→Role Coverage Gap Analysis (generated)")
    a("")
    a("> **Generated artifact — do not hand-edit.** Produced by")
    a("> [`../../07-methodology/role-coverage-gap-analysis.py`](../../07-methodology/role-coverage-gap-analysis.py)")
    a("> under [`generate-role-coverage.py`](../../07-methodology/generate-role-coverage.py) build()'s")
    a("> own resolution semantics (whole Owner/Participants/Step cell first, then")
    a("> the slash/dash part fallback), over the same canonical registers. This is")
    a("> the reverse arm of the Role-Anchoring Contract: the contract's matrix")
    a("> proves every chartered role is explicitly in the catalog (role →")
    a("> workflow); this report measures where workflows still do their work")
    a("> without a chartered role (workflow → role). Regenerate after any PA,")
    a("> alias or register change; `--check` byte-verifies this file. The")
    a("> workflow population is pinned — a corpus change intentionally moves")
    a("> these numbers and must re-point this report (the Check-71 CENSUS-pin")
    a("> contract).")
    a("")
    a("## Baseline")
    a("")
    a("| Measure | Value |")
    a("|---|---|")
    a(f"| Workflows analyzed | {len(wfs)} (population-pinned) |")
    a(f"| Class C — healthy (≥1 chartered owner) | {len(wfs) - len(class_a) - len(class_b)} |")
    a(f"| Class B — owner-grain gap (chartered roles touched, owner not chartered) | {len(class_b)} |")
    a(f"| Class A — role-less (no chartered role in any RACI cell) | {len(class_a)} |")
    a(f"| Anchoring census (role → workflow arm, pinned by Check 71) | {len(anchor['chartered'])} chartered / {anchor['anchored']} anchored / {len(anchor['zero'])} zero-anchor / {len(anchor['weak'])} weak |")
    a("")
    a("> **Adjudication policy.** Department-grain ownership ('Finance', 'Legal',")
    a("> 'HR' as performer) is acceptable only where the work is genuinely")
    a("> department-wide; a recurring Owner form that denotes one seat's function")
    a("> is a gap. Remediation runs through the wave-32/36 role-vocabulary")
    a("> governance — alias-promote the form to the chartered title it denotes,")
    a("> or charter the seat in the §5.3 register — with the Check-71 census")
    a("> re-pinned. Workflows inside a registered dormancy estate carry their")
    a("> estate annotation and are retained design, not defects (the")
    a("> disable-not-delete doctrine). Classes A/B only legitimately move")
    a("> downward; any increase forces conscious re-adjudication.")
    a("")

    a(f"## Class A — Role-less workflows ({len(class_a)})")
    a("")
    a("No chartered role appears in Owner, Participants, or either Steps Role")
    a("cell. Estate-annotated rows are retained design under a registered")
    a("dormancy posture; the remainder are the hard remediation queue (anchor a")
    a("chartered role, or adjudicate the vocabulary, or record the dormancy")
    a("estate).")
    a("")
    a("| Workflow | Title | VS | PA | Owner form | Estate |")
    a("|---|---|---|---|---|---|")
    for r in class_a:
        a(f"| {r['wid']} | {esc(r['title'])} | VS-{r['vs']} | {r['pa'].split('-')[0]}-{r['pa'].split('-')[1]} | {esc(r['owner'])} | {r['est']} |")
    a("")

    est_a = sum(1 for r in class_a if r["est"])
    a(f"> {est_a} of the {len(class_a)} Class-A rows sit inside registered dormancy")
    a(f"> estates (by-design retained design); {len(class_a) - est_a} are open gaps.")
    a("")

    forms = defaultdict(lambda: {"n": 0, "vs": set()})
    for r in class_b:
        forms[r["raw"]]["n"] += 1
        forms[r["raw"]]["vs"].add(r["vs"])
    a(f"## Class B — Owner-grain gaps ({len(class_b)})")
    a("")
    a("The Owner cell resolves to no chartered role while chartered roles are")
    a("touched elsewhere in the workflow. Aggregated by the literal Owner-cell")
    a("form — the full per-workflow appendix follows the aggregate.")
    a("")
    a("| Owner form (literal) | Workflows | Distinct VSs | Resolved grain |")
    a("|---|---|---|---|")
    for k in sorted(forms, key=lambda k: (-forms[k]["n"], k)):
        e = forms[k]
        grain = class_b and next((r["form"] for r in class_b if r["raw"] == k), "")
        a(f"| {esc(k)} | {e['n']} | {len(e['vs'])} | {esc(grain or '')} |")
    a("")
    a(f"### Class B appendix — all {len(class_b)} workflows")
    a("")
    a("| Workflow | Title | VS | Owner form (resolved) | Estate |")
    a("|---|---|---|---|---|")
    for r in class_b:
        a(f"| {r['wid']} | {esc(r['title'])} | VS-{r['vs']} | {esc(r['form'])} | {r['est']} |")
    a("")

    a(f"## Class C — Healthy ({len(wfs) - len(class_a) - len(class_b)})")
    a("")
    a("At least one chartered role owns the workflow. No action.")
    a("")

    top = sorted(span.items(), key=lambda kv: (-kv[1], kv[0][1].lower()))[:15]
    a("## Ownership-span view (top 15 chartered and department-grain owners)")
    a("")
    a("| Owner | Bucket | Workflows owned |")
    a("|---|---|---|")
    for (b, t), n in top:
        a(f"| {esc(t)} | {b} | {n} |")
    a("")
    a(f"## Participate-only chartered roles ({len(part_only)})")
    a("")
    a("Chartered roles anchored in the catalog (the role-anchoring contract is")
    a("satisfied) that own no workflow — their accountability may be understated;")
    a("each is either a genuine supporting seat or an ownership-understatement")
    a("candidate for the same governance path.")
    a("")
    a("| Role | Charter | Workflows touched | Owns |")
    a("|---|---|---|---|")
    for r in part_only:
        a(f"| {esc(r['title'])} | {esc(r['dept'])} | {r['touched']} | 0 |")
    a("")
    return "\n".join(L) + "\n"


def main():
    wfs, class_a, class_b, span, part_only, anchor = analyze()
    if len(wfs) != POPULATION_PIN:
        print(f"role-coverage-gap-analysis: population {len(wfs)} != pinned "
              f"{POPULATION_PIN} — a corpus change moved the baseline; re-point "
              f"POPULATION_PIN and the report consciously")
        return 1
    out = render(wfs, class_a, class_b, span, part_only, anchor)
    if "--check" in sys.argv:
        if os.path.exists(OUT):
            shipped = open(OUT, encoding="utf-8").read()
            if shipped == out:
                print("role-coverage-gap-analysis: byte-identical, OK")
                return 0
            import difflib
            diff = list(difflib.unified_diff(shipped.splitlines(), out.splitlines(),
                                             "shipped", "re-derived", lineterm=""))
            print(f"role-coverage-gap-analysis DRIFT ({len(diff)} diff lines) — regenerate")
            for d in diff[:20]:
                print(d)
            return 1
        print("report missing — run without --check to generate")
        return 1
    open(OUT, "w", encoding="utf-8").write(out)
    est_a = sum(1 for r in class_a if r["est"])
    print(f"role-coverage-gap-analysis written: {len(wfs)} workflows — "
          f"class A {len(class_a)} ({est_a} estate-annotated), class B {len(class_b)}, "
          f"class C {len(wfs) - len(class_a) - len(class_b)}; "
          f"participate-only chartered roles {len(part_only)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
