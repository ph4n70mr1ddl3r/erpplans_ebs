# Role Charters — The Human-Facing Clarity Layer

> **What this layer is.** One page per chartered role that answers, for the
> person holding the seat and everyone who works with them: *what do I own,
> what do I do, what may I decide, what wins when things compete, where do I
> go when stuck, and what is explicitly not mine.* The goal is operational
> clarity — **no one stands still wondering what to do** — not documentation
> completeness.

## Position in the canon (the single-source rule)

| Layer | Artifact | Authority |
|---|---|---|
| Definition of record (roles) | `optimal-table-of-organization.md` §5.3 register · `it-product-operating-model.md` §5.3 seats · §7.2/§7.3 rosters | **Canon.** HC, reporting line, mandate. The charter never restates these with different numbers. |
| Definition of record (work) | Workflow catalog (5,433 PA workflows: Owner / Participants / Step R-A cells) | **Canon.** Ownership and participation surfaces. |
| Analytical layer | `role-coverage-matrix.md` (generated), `virtual-gemba-walk.py` demand verification | **Derived.** Anchors, tier mix, demand vs. capacity. |
| **This layer** | `role-charters/<ROLE>.md` | **Derived communication artifact.** Pulls from the layers above; authored only where human judgment is required. |

A charter field that contradicts the canon is a defect in the charter. When
canon moves (register change, workflow re-anchoring, batch regeneration), the
derived fields of the affected charters are refreshed in the same sitting.

## The two field classes

- **[D] Derived** — auto-fillable from canon today (and mechanically
  generatable later, `generate-role-charters.py`, following the
  `generate-role-coverage.py` pattern): identity block, workflow anchor table,
  owner/participant surfaces, priority matrix cells that mirror an SLA or
  severity canon, demand-verification status.
- **[A] Authored** — human judgment the registers deliberately do not carry:
  mission wording, decision-right limits, escalation wording, the *boundaries
  & handoffs* list, backup arrangements.

The pilot writes both by hand; the generator, if built later, emits [D] and
leaves [A] sections as fill-in slots.

## Why this layer exists (the confusion taxonomy it closes)

The Role-Anchoring Contract guarantees every chartered role is *measurable*
(≥1 RACI anchor). Measurability does not by itself produce clarity. The
charter closes the six residual confusion classes the catalog leaves open:

| Confusion class | Closed by charter section |
|---|---|
| Ownership — "is this mine?" | §3 Ownership |
| Priority — "which first?" | §7 Priority rules |
| Process — "how, exactly?" | §6 Workflow anchors (pointers, not restatement) |
| Decision rights — "can I approve this?" | §5 Decision rights |
| When stuck — "who do I ask?" | §8 Escalation path |
| Boundaries — "what is *not* my job?" | §9 Boundaries & handoffs |

**Charter discipline:** the charter points at workflows; it never re-documents
a workflow's steps (single-source). It is clarity for humans, not a
surveillance instrument — charter contents are not used to grade incumbents
(Goodhart guard), and coverage/judgment roles are chartered by *risk and
mandate*, not by utilization (a low-touch anchor table on a coverage role is
expected, and says nothing about justifiability — that question belongs to the
demand-verification instrument).

## Filling order (per role, ~60–90 min)

1. Copy `TEMPLATE.md`; fill §1 Identity from canon (cite sources).
2. Pull the role's row(s) from the role-coverage matrix → §6 anchor table.
3. Open each owned workflow's PA file: Owner cell → §3 bullet; SLA/severity
   matrices → §7; hand-off steps → §9 seed list.
4. Author §2 mission, §5 decision limits, §8 escalation, §9 boundaries, §10
   done-definition, §11 backup with the role's manager in one sitting.
5. Review by the role itself (does the incumbent recognize their job?), the
   manager, and one frequent counterparty.

## Pilot plan (one department, four weeks)

- **Week 1 — pick the pilot unit and the heat map.** Choose the department
  with the most "who does this?" friction. Build the confusion heat map from
  where questions actually land (chat threads, meeting agendas, escalation
  tickets): the top repeated questions name the charters and workflows to do
  first.
- **Week 2 — charter the department head + the 3–5 most-touched roles**
  (highest workflow-touch counts in the coverage matrix).
- **Week 3 — decision rights & escalation pass.** Cross-review all pilot
  charters together: every hand-off named in §9 must land on a role whose
  §3/§6 accepts it (symmetry check) — asymmetric hand-offs are the residual
  confusion list.
- **Week 4 — live test & retro.** New-hire test: can a person who has never
  worked here answer "what do I do when X happens?" from the charter alone?
  Fix gaps; publish v1.0; set review dates (quarterly, or on any canon batch
  that touches the role's anchors).

## Rollout order for the full population

259 chartered roles = 192 §5.3 register roles (the register's 194 rows ex the
by-reference IT-portfolio row, which the 32 seats carry, and the one
duplicated title — the coverage census's own decomposition) + 32 IT
product-model seats + 8 §7.2 store-roster + 27 §7.3 DC-roster roles.
Sequence by confusion exposure, not by
org chart: (1) Tier-1-owning roles, (2) weak-anchor watchlist roles (the 53 —
their charters make the mandate explicit while demand verification runs), (3)
shared-services and cross-department roles, (4) the long tail. Store/DC
roster roles use the same template with §6 collapsed to their process-area
anchors (the per-store/per-DC pattern means one charter per *role*, not per
site).

## Directory contents

- `TEMPLATE.md` — the one-page charter (field classes [D]/[A] marked).
- `EXAMPLE-it-helpdesk-lead.md` — worked example from real canon (W48 +
  Field & End-User Services team), demonstrating every derivation path.
