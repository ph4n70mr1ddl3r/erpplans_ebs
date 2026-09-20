# DMN 1.3 Models — Decisions Extracted from the Workflow Corpus

> **Generated artifacts — do not hand-edit.** Every `.dmn` file in this tree is
> generated from the markdown workflow corpus by
> [`07-methodology/generate-dmn.py`](../07-methodology/generate-dmn.py).
> Regenerate with:
>
> ```bash
> python3 07-methodology/generate-dmn.py
> ```

---

## Coverage

| Metric | Value |
|---|---|
| DMN files | 41 (one per process area that yields ≥ 1 decision) |
| Decisions | 80 |
| Decision-table rules | 343 |
| Deferred rule sets (not faked) | 197 step-row rule sets |

The directory structure mirrors the source: `dmn/VS-<NN>-<slug>/PA-<slug>.dmn`.
Each file is a DMN 1.3 `definitions` element carrying one `<decision>` per
extracted rule set, each with a full DRD-interchange `DMNDI` shape so the files
open directly in dmn-js / Camunda Modeler (table view and DRD).

## What gets extracted

Only content that **already exists as an explicit rule** in the markdown:

| Source (workflow markdown) | DMN target |
|---|---|
| Rule-shaped markdown tables — header with ≥ 1 criteria-like column (severity, tier, amount, scenario, category, priority, …) and outcome column(s) (action, approval, SLA, escalation, authority, …) | One decision table per table: every criteria column → `<input>`, every other column → `<output>` (no column is dropped); every row → one `<rule>` |
| Tiered money-threshold authorization rules in step prose — the recurring "(a) ≤ PHP X: Role A; (b) PHP X–Y: Role B; (c) > PHP Y: Role C" idiom, including the "> PHP 50K → Category Manager; > PHP 500K → VP; > PHP 2M → CFO" escalating form | One decision table over `Amount` (PHP, FEEL `number`) with `Approver` as output; each tier → one rule |

## Modeling conventions

- **Hit policy `U` (unique)** is published only after a mechanical disjointness
  check over the numeric bands (or full input-tuple uniqueness for string
  tables). Band sets that genuinely overlap are demoted to `C` (collect) or the
  whole set is deferred — never silently published as disjoint.
- **Ladder normalization** (documented per decision in its `<description>`):
  - `≤ PHP X` followed by `PHP X–Y` — the shared boundary point is assigned to
    the lower tier (standard tier-ladder reading).
  - Escalating open lower bounds only (`> PHP A → role 1; > PHP B → role 2`, with
    `A < B < …`) — rewritten to disjoint `(A..B]` bands: each band runs from its
    threshold to the next tier's threshold.
- **Non-monetary tiers** in an otherwise money-based marker list (e.g. a catch-all
  "Board + external appraiser" tier keyed on land value) are excluded from the
  amount-based table and flagged in the decision description.
- Every decision's `<description>` carries full provenance: source PA file,
  section / workflow + step, extraction notes, and the verbatim source text.
- FEEL rendering: comparison form (`<= 50000`, `> 2000000`) for one-sided bands,
  `(a..b]` ranges for two-sided bands, quoted string literals for enumerable
  cells; input expressions are sanitized FEEL identifiers of the source column
  title.

## What is deliberately NOT extracted

197 step-row rule sets reference money + approval language but are **deferred
rather than faked**:

- single-threshold rules with no complementary tier ("approvals above PHP 5,000
  required" — no ≤ tier stated, so a two-row table would be invented);
- multi-criteria sets (amount **and** another dimension — e.g. per-SKU vs
  aggregate-quarterly write-off matrices, NBV-vs-land-value disposal tiers);
- partially-structured lists where any money-bearing segment fails to yield a
  band + approver (a partial table would publish a wrong policy);
- percent-only or unit-based tiers (e.g. "markdown > 15%").

These remain documented in the markdown source; converting them is per-decision
authoring work, not mechanical extraction.

## Relationship to the corpus

- The markdown workflow corpus remains the **source of truth**; `dmn/` is a
  projection of it, exactly like `bpmn/`.
- The BPMN models render the *process* (sequence, roles, controls); the DMN
  models render the *decisions* those steps reference. Both are lossless for
  what they claim to represent — and nothing is claimed for what was deferred.

## Validation

The generator validates its own output before exiting:

- every file re-parsed as well-formed XML against the DMN 1.3 model namespace;
- ids unique per file; every decision has a `decisionTable` with ≥ 1 input,
  output and rule;
- every rule's entry counts match the table's inputs/outputs; no empty entries;
- every `DMNShape` `dmnElementRef` resolves, and every decision carries a
  `DMNShape` (so it renders in a DRD);
- numeric band sets published with hit policy `U` re-verified pairwise-disjoint.

A non-zero exit code means a file failed validation. The shipped tree is also
re-validated structurally on every `validate-repo.sh` run (Check 71), which
re-derives the canonical counts from the markdown corpus — so drift between a
stale `dmn/` and the corpus cannot ship silently.

---

*Generated by `07-methodology/generate-dmn.py` · source corpus: 80 decisions
extracted across 25 of 188 value streams (40 of 569 process areas)*
