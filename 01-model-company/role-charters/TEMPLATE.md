# Role Charter — `<ROLE TITLE>`

> **One page. If it needs a second page, the role is unclear or two roles.**
> Field classes: **[D]** derived from canon (cite the source; refresh when
> canon moves) · **[A]** authored (the registers deliberately do not carry
> this). Delete the gray instruction lines when filled.

---

## 1. Identity [D]

| Field | Value | Source |
|---|---|---|
| Role title | *(exact canonical title)* | TO §5.3 register / ITOM §5.3 seat / §7.2–7.3 roster |
| Team / department | — | same row |
| Reports to | — | same row |
| Headcount (seats with this charter) | — | same row |
| Charter ID / version / review date | `RC-<DEPT>-<nn>` · v0.1 · *(quarterly or on anchor-touching batch)* | this layer |

## 2. Mission [A]

One sentence: why this seat exists, in outcome terms. Test: if the mission
were already true without this role, the role is mis-scoped.
> *Example shape: "Every user in every location gets their issue resolved
> within the published SLA, and the company sees why incidents happen."*

## 3. Ownership — what this role is accountable for [D→A]

Derived from the **Owner cells** of this role's anchored workflows; each
bullet states the *outcome*, not the steps. Every bullet must trace to a W#.

- Owns `<outcome>` — W#… *(PA file link)*
- …

**Not the owner of:** anything listed in §9. (If a recurring decision has no
owner at all, that is a register/anchoring gap — raise it, don't absorb it.)

## 4. Contribution — where this role executes but does not own [D]

Derived from **Participants / Step Role (R)** cells where another role is
Owner. Kept as a summary count + notable entries, not an exhaustive list
(the coverage matrix is the exhaustive list).

- `<n>` contributor anchors; principal surfaces: W#… (as `<what the role does
  there>`), W#…

## 5. Decision rights [A]

Three rows, concrete limits, no "as appropriate":

| May decide alone | Recommends, others approve | Must escalate (to whom) |
|---|---|---|
| …(with limits, e.g. spend ≤ X, standard changes, access grants per matrix) | …(names the approver role) | …(names the role, cites the trigger) |

If a decision type is not in the table, §8 decides where it goes.

## 6. Workflow anchors — the demand signal [D]

| W# | Workflow | This role | Tier | Cadence/volume | Demand status |
|---|---|---|---|---|---|
| … | *(PA link)* | Owner / R / A | 1–3 | *(from PA Frequency/Volume)* | verified / watchlist-53 / n-a |

Rules: Tier from the confirmed register; "Demand status" carries the
virtual-gemba verdict for weak-anchor roles. A short anchor table on a
coverage role is **expected** — mandate, not utilization, justifies the seat
(see layer README).

## 7. Priority rules — what wins when things compete [D where canon exists]

Mirror the governing canon (severity/SLA matrices, tier register); author
only what no matrix covers. State as an ordered list, tie-breaker included:

1. …(e.g. P1 per W48 severity matrix: response 15 min / resolution 4 h)
2. …
Tie-breaker: *(e.g. tier register, then Owner's call, then §8 escalation)*

## 8. Escalation — when stuck [A]

| Situation | First ask | If unresolved, decides |
|---|---|---|
| … | *(role, not person)* | *(role)* |

Every row names roles, never incumbents' names. Include one "novel situation"
row: anything not covered here goes to `<manager>` within `<timebox>` —
standing still is the only wrong move.

## 9. Boundaries & handoffs — what this role explicitly does NOT do [A]

The biggest confusion killer. Left column must be work this role is *asked to
do but shouldn't*; right column names the receiving role (whose charter §3/§6
must accept it — symmetry check in pilot week 3).

| Not this role's job | Belongs to |
|---|---|
| … | *(role / W#)* |

## 10. Definition of done — what "good" looks like [D/A]

3–5 measures already governed by canon (SLA compliance, cycle time, audit
findings), stated as targets. Not a surveillance instrument: measures serve
the role's own steering and the §2 mission, not individual grading.

- …(e.g. ≥ target on `<SLA>`; `<n>`-day turnaround on `<artifact>`)

## 11. Coverage & backup [A]

| Duty | Covered by | Activation |
|---|---|---|
| …(incl. on-call/peak-season duties if any) | *(role)* | *(automatic / explicit delegation)* |

A role with a P1 obligation must name its backup here; a P1 obligation with
no backup row is an org defect, not a charter omission.

## 12. Provenance & change log [D]

| Field | Value |
|---|---|
| Canon sources | *(register row + PA files + coverage-matrix row, with versions/dates)* |
| Derived-fields refresh trigger | *(any batch touching this role's anchors — regenerate, don't hand-reconcile)* |
| Authored by / reviewed with | *(author · incumbent · manager · counterparty)* |
| Changes | *(v0.1 draft — …)* |

---

**Fill-order reminder:** §1 identity from canon → §6 anchors from the
coverage matrix → §3/§4/§7 from the PA files → §2/§5/§8/§9/§10/§11 authored
with the manager in one sitting → incumbent recognition test → v1.0.
