# Universal Role-Demand Verification — Spec (batch 52 proposal)

> **Direction.** "I want consistency — if some roles can be properly known
> through workflows, can't we generalize that?" The Role-Anchoring Contract
> guarantees every chartered role ≥1 explicit RACI anchor (259/259/0, Check 71)
> — *measurability*. It does not yet guarantee every role a **verified demand
> verdict**: the time-and-motion verification loop currently runs only against
> the 53-role weak-anchor watchlist. This spec generalizes the instrument from
> the watchlist to **all 259 chartered roles**, adds the **named-residual**
> field, and emits the verdict into the role-coverage matrix — one evidence
> standard for every seat, regardless of work shape.

## 1. The doctrine being generalized

A role is **properly known** when three things hold — for throughput roles and
judgment/coverage roles alike:

1. **Anchor** — ≥1 explicit RACI cell in the catalog *(universal today)*
2. **Verified demand** — parsed anchor time × event cadence vs. chartered
   capacity, with a verdict *(today: 53 of 259 → make it 259)*
3. **Named residual** — the unanchored remainder of the seat's capacity is
>  declared, not hidden *(new field; authoring interface = the role charter)*

The uniformity is in the **evidence contract**, never in the anchor *texture*:
a Payroll Specialist foots via 13,430 payslips/month; the PEO Process
Architect foots via its recurring governance outputs (W3571 design reviews,
W3573 waivers, W5575–77 customization exceptions). Roles whose anchors read
ZERO-DURATION or unparseable cadence are **coverage-priced** (mandate + risk),
not workflow-priced — that is a verdict class, not a defect of the model.
No per-role workflow files are minted to fake texture (the demand-pattern
granularity rule stands).

## 2. Current state (verified against the code)

| Component | File | What it does today | What changes |
|---|---|---|---|
| Motion engine | `virtual-gemba-walk.py` `motion --full` | Dumps per-role annual demand h/yr, HC, util% for **every mapped role key** (not only weak anchors) | **Nothing.** Engine is already universal; its grammar lessons (plural units, per-occurrence symbolic rates, period-qualified totals) carry over untouched |
| Watchlist verifier | `verify-weak-anchor-demand.py` | Queue = `rows` where `0 < touched <= 2` (53 roles); verdict ladder; writes the byte-pinned `weak-anchor-demand-verification.md` (Check 80B) | Stands as batch-51 history until Phase 3 re-pin; its verdict ladder is lifted verbatim |
| Queue source | `generate-role-coverage.py` `build()` → `rows` | Every chartered role with `title / bucket / dept / touched / t1..t3 / hc` | Universal queue = the same rows with the `touched <= 2` filter dropped |
| IT-seat capacity | `IT_SEATS` dict (grc) mirroring ITOM §5.3/§9.1 | Seat titles + HC for the 32 product-model seats (incl. deferred-squad annotation in ITOM §9.1: 108 active / 122 design) | Pricing source for `bucket == "it"` rows (the engine's own cap map carries no IT HC — the TO defers IT by reference; this closes the MEASURED — CAPACITY UNMAPPED arm for IT seats) |
| Matrix | `generate-role-coverage.py` → `role-coverage-matrix.md` (Check 71 byte-pin) | Anchor census + per-role touch/tier tables | Phase 3: one new column **Demand verdict** + census extension |

## 3. Design

### 3.1 New tool — `verify-role-demand.py`

Same skeleton as the watchlist verifier (imports `grc` + `vgw`, shells
`motion --full`, parses the dump, `exercised_demand` fallback with a
pre-indexed step scan — index steps by normalized Role-cell text once, scan
matching cells per role; the O(wfs × roles) rescan is fine at 53 roles,
wasteful at 259). Deterministic, read-only over corpus and engine; `--check`
byte-compares the shipped register without writing.

**Queue:** all `rows` with `bucket in (hq, it, store, dc)` and `touched ≥ 1`
— the anchored chartered population (259). Sorted by `(touched, title)`.

**Capacity pricing:** `r["hc"] × 1,800` (HQ: register + IT seats) /
`× 1,900` (field: §7.2/§7.3 rosters) — the engine's standing assumptions.
IT seats priced from `r["hc"]` (the `IT_SEATS` mirror of ITOM §9.1); seats on
deferred squads (OMO/TPS, 7+7) carry the register note `design-of-record —
squad deferred (ad)/(ah)` so a hot verdict on a deferred seat reads as
design-load, not active-load.

### 3.2 Verdict ladder (lifted from batch 51, one addition)

| Verdict | Condition | Action |
|---|---|---|
| CONFIRMED | parsed demand 50–150% of capacity | stays as chartered |
| OVERLOAD | >150% | capacity decision — demand is real |
| UNDER-UTILIZED | <50% | merge/defer/resize candidate |
| EXERCISED-THROUGH (band) | own key empty; named cells land on broader seats | verify the via-group before any seat decision |
| MEASURED — HC UNPRICED | demand priced, `r["hc"]` missing (register defect) | register fix, not a workload verdict |
| ZERO-DURATION | anchored but every duration cell reads zero (days-based/cadence work) | cycle audit; **residual class COVERAGE-STANDBY by default** |
| UNPARSEABLE-FREQ | anchors ride unparseable cadence | adjudicate the frequency family |
| NO PARSED CADENCE | participant-level anchor only | step-level anchoring or gemba |

### 3.3 The named residual (new field)

For every role whose verdict parses to an hour band, residual =
`max(0, capacity − parsed demand)`. The residual must be **named** — one of:

| Residual class | Meaning | Authoring home |
|---|---|---|
| WORKFLOW-MEASURED | residual ≤ 20% of capacity (contingency/queue slack) | none needed |
| PARTIAL — NAMED | residual > 20%; declared as improvement slack, learning, peak buffers, cross-training, project time | charter §10 (authored) |
| COVERAGE-STANDBY | anchors zero/unparsed; seat priced by mandate + risk (on-call, DR, statutory) | charter §2/§11 (authored) |
| UNMEASURED | no anchors measurable and no named residual yet | **the worklist** — charter backlog |

The tool emits `residual` and `residual class`; where authoring is required
but absent it emits **`UNNAMED — charter worklist`** and counts it in the
census. The instrument deliberately does not invent residuals (Goodhart
guard): naming is a charter act, counting is an instrument act.

### 3.4 Census extension (Phase 3, Check 71 re-pin)

```
C71_CENSUS ... verified=259 verified_confirmed=N verified_overload=N
verified_under=N exercised=N coverage_standby=N unmeasured=N
residual_unnamed=N
```

Matrix gains the **Demand verdict** column on every chartered-role row, and
the Role-Anchoring Contract section's demand-verification paragraph re-points
from "the 53-role watchlist" to the universal register.

## 4. Phases

| Phase | Deliverable | Pins touched |
|---|---|---|
| **P0 — instrument** (this batch) | `verify-role-demand.py` + generated `role-demand-verification.md` (universal register); additive, no existing pin moves | none (new artifact unpinned until P3) |
| **P1 — charter layer** | `role-charters/` pilot consumes the register: §6 Demand status resolves from it; residual naming begins (the UNNAMED count is the charter backlog size) | none |
| **P2 — adjudication wave** | Read the universal verdicts; disposition the OVERLOAD/UNDER/UNMEASURED rows the same way batch 51 dispositioned its five (re-scope, re-anchor, or conscious accept — each with a named residual) | corpus edits per normal PA governance; register re-derived |
| **P3 — pin** | Matrix column + census extension in `generate-role-coverage.py`; Check 71 re-pin (conscious); Check 80 gains `verify-role-demand.py --check` (80E); the batch-51 weak-anchor report retires into its own history section or is subsumed — one re-adjudication note in TO §5.3 records the generalization | Check 71, Check 80 |

## 5. Guards carried over

- Verdicts are decision-support, never incumbent grading (the register prices
  *role design*, not timesheets).
- Narrow titles inherit department workload through the exercise-through
  contract — a hot narrow title is a department signal.
- Unparseable cadence reads low; the coverage note prints on every run.
- COVERAGE-STANDBY is a *first-class* verdict, not a euphemism for
  unmeasured: it requires the charter's mandate/risk citation to stand at P1.

## 6. Batch 52b — implementation record (2026-09-26)

`verify-role-demand.py` implements P0 + the §1/§2 improvements. Key records:

- **Engine patch (additive only):** `parse_workflows` now also emits
  `steps_raw` (verbatim duration cells); every priced figure unchanged — the
  batch-51 pin re-verified byte-identical post-patch.
- **Attribution architecture:** parts-based attribution first (mode_motion's
  distribution aggregated to chartered roles — the corpus's own resolver
  reconciliation, engine-parity confirmed by side-by-side), with surface
  matching (canonical + ROLE_ALIASES/W36/W38/W39 + IT_SEATS reverse map,
  blocklist-guarded) only as the zero-claim fallback — alias-claimed
  confidence. NO PARSED CADENCE fell 71 → 8.
- **Run-1 correction:** the first register's milder OVERLOAD (28) was a
  `parse_full_dump` merge artifact (per-bucket dump rows merged, last-row
  util). The engine itself prices e.g. Content & Creative Specialist's
  store-executed demand at 68,467% on HC 2 — the register now mirrors the
  engine faithfully: OVERLOAD active 82 is the honest corpus reading, the
  W2201-class store-multiplier artifacts dominating it are the P2 disposition
  queue, not instrument noise. (Superseded at 52c, see run-2 below: three of
  those 82 were the substring-claim phantoms — the honest active count is 79.)
- **Days-bridge:** the corpus's 2,869 day/week cells are elapsed-window
  style ('1–2 weeks' UAT, '2–5 days' signoff) with zero effort-worded cells —
  the batch-51 elapsed-vs-effort doctrine keeps them unpriced; the bridge is
  armed for explicit effort wording ('X days effort', 'man-days') and inert
  today (days-bridged rows: 0).
- **IT-seat HC:** no seat-level HC existed anywhere; added `IT_SEAT_HC` —
  explicit mirror of ITOM §9.1 + §5.3 rosters (26 seats priced; OMO/TPS
  deferred split carried by the State column). Vocabulary-umbrella seats
  (department/team grain: 'IT Operations (FS/INFRA)', 'DP / Data & Analytics
  (VS-28)', 'SEC (Cybersecurity…)' where unpriced, 'Information Technology
  (department)', 'Strategy / Corporate Planning (PMO)', DP CDP/scientist)
  stay MEASURED — HC UNPRICED deliberately: the ITOM seat-charter worklist,
  never a silent fold. Unpriced total: 7.
- **Register tallies (52c):** CONFIRMED 25 · OVERLOAD active 79 + design 3 ·
  UNDER 87 · EXERCISED-THROUGH 10 · ZERO-DURATION 39 · UNPARSEABLE 2 ·
  NO PARSED 8 · unpriced 6 · residual UNNAMED 41 / UNMEASURED 3 ·
  alias-claimed 2. All 259 census-joined.
- **Run-2 correction (52c, 2026-09-26 twelfth review-everything pass):** the
  52b fallback claimed demand by SUBSTRING while the corpus's own
  reconciliation (the resolver + ROLE_ALIASES tables) fires on whole-cell
  equality — bare generic alias tokens ('brand', 'energy', 'cloud', 'pmo')
  and suffix matches inside longer segments ('procurement compliance
  analyst' → Procurement Coordinator; 'data privacy officer' → the DPO
  seat; 'tax tech lead'; 'private label brand manager') priced OTHER
  roles' cells onto these seats: three phantom active-OVERLOAD verdicts
  (Brand Manager 1,200%, Compliance Analyst 347%, Energy Manager 168%)
  and inflated reads on seven more (incl. the DP umbrella's 125,955 h/yr).
  The guard: surface claims price a cell only at the corpus's own grain —
  whole-cell or comma/semicolon-segment equality of the paren-stripped
  cell, never substring, never slash-split (slash-compound titles resolve
  whole); substring matches count anchors only. Zero-claim rows whose
  named cells parse but fold to other seats read EXERCISED-THROUGH with
  the via-group named — §3.2's own ladder row, restored (the batch-51
  Privacy Officer precedent, which the 52b register had silently read as
  4 h/yr UNDER). The honest comma-segment claim survives (Tile &
  Heavy/Breakbulk Crew keeps its 684 h/yr — the cell names the crew
  verbatim as a co-performer). Companion repair: triage-role-demand.py
  (batch 54) joins the register's demand basis, so the disposition queue
  carries every active-OVERLOAD row (the 53 form silently dropped the 3
  phantom rows — 82 vs 79 — and its naming worklist dropped 5 of the 45
  PARTIAL — UNNAMED rows while asserting the class equation; the join
  makes both structural).

## 7. Artifact

`01-model-company/workflows/role-demand-verification.md` — universal
register: one row per chartered role
(`Role | Charter | Touched | Demand h/yr | HC | Util | Verdict | Residual`),
tally, census line, and the standing interpretation guardrails.
