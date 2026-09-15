#!/usr/bin/env python3
"""
audit-model-docs.py — root-level model-company document integrity guard.

Consistency review #41 (2026-08-29) audited the three root-level model-company
documents never before swept — mobile-app-strategy.md, data-migration-mapping.md,
assumptions-and-design-decisions.md — for figure agreement with the canonical
registers and internal cross-reference integrity. Findings: fully clean —

  * figures: 6,762 employees, ~800–1,000 vendors (§6.5), 35,000 active + 20,000
    inactive items, ~600,000 loyalty members, 29 per store, 200 stores + 4 DCs,
    14,000 POS/store/month (2.8M ÷ 200), ~PHP 9.21M revenue/employee, and the
    5,200+200 trade/corporate price records all match the registers;
  * cross-references: every W/VS-/CTL-/PA-/requirement-ID token resolves
    (5,363 W, 190 VS, 569 PA, 808 CTL, 728 requirement registers); the §-refs
    resolve doc-scoped — unqualified to the profile's 61 sections, named-doc
    refs like 'Technical Guidelines §2.1' to 07-methodology/technical-
    guidelines.md, and bare §N.N inside data-migration-mapping.md to its own
    section headers; no retired stale totals (6,757/6,715/5,3xx) appear.

Guard mode (--guard, validator Check 59) re-runs the whole audit on every
invocation: token resolution against the live registers, doc-scoped §-ref
resolution, and the retired-figure literal list. Any hit exits 1.

Consistency review #68 (2026-09-02) extended the guard to the two
organizational documents issued 2026-09-01/02 — optimal-table-of-organization.md
and 07-methodology/it-product-operating-model.md — which had shipped with zero
validator coverage. The review repaired three defects between them (TO §7.3
'Outbound (51)' vs role-sum 50; IT-model '~11 external integration clusters' vs
the canonical ten; a §13.3-for-§13.2 seasonal-calendar §-ref) plus an
unresolvable §2.4 self-reference, and added: doc-scoped retired literals, the
required corrected anchors (incl. the 171+17=188 / 4,864+499=5,363 IT-model
reconciliation sums and the TO's two-state 469/6,869 totals), and a structural
rule that re-derives every §7.3 DC-roster group total from its own HC cells.

2026-09-03 hybrid capability-sourcing revision: anchors re-based to OM v2.0 (adds the
66+49=115 sizing sum) and TO v1.3 (HQ 504 / total 6,904; IT = 115 / 16 product teams),
with the v1.x sizing/shape literals retired doc-scoped. See the CHANGELOG entry for
2026-09-03 and 07-methodology/capability-sourcing-and-engineering-model.md.

2026-09-03 agentic-AI extension: OM v2.1 sizing anchor re-based 66+49=115 → 66+56=122
(AI & Agent Platform +7); TO v1.4 anchors re-based to HQ 511 / total 6,911 (~440–515
band row; 504+7=511) with the 115-era literals retired.

2026-09-03 post-AAP consistency pass: the two remaining uncovered methodology documents —
capability-sourcing-and-engineering-model.md and technical-guidelines.md — join DOCS (the
sourcing doc had quoted the stale pre-confirmation tier trio 1,375/3,243/754 in its §12.1
autonomy ladder precisely because it shipped outside this guard). Two structural rules are
added: (a) sourcing_tier_hits — the §12.1 autonomy-ladder tier counts are re-derived from
the criticality register's Summary table on every run; (b) to_phase_hits — the TO's §11
phase rows must have each HC-delta cell equal the sum of its own named from→to moves, the
three deltas sum to the stated total, and that total equal target-minus-current HQ (the
pass found the cells internally inconsistent since adoption: −7/−6/+13 against their rows,
with each IT re-base bumping only the Phase 3 cell). The change-note exemption is also
fixed to strip the whole version-history footer (from the first '*Date:' or
'*Document Version:' line to end-of-file) instead of only up to its first ')'.

2026-09-04 guard-extension pass: the AI-first operating guide (ai-first-operating-guide.md,
v1.0) joins DOCS — it shipped with zero guard coverage, the sourcing-model precedent (a
quantitative doc outside this guard is the one that drifts). Dry-run of the generic checks
against it was clean (tokens, §-refs, retired figures), so the extension is guard-side only,
plus a structural rule guide_figure_hits that re-derives the guide's canonical-figure
citations from the primary registers on every run (the §5 catalog triple in both its prose
and compressed forms, the Tier-wired autonomy-ladder sentence, and the control- and
requirement-register canon-table counts). The methodology-index version-pin rule now also
watches the guide's index row.

2026-09-03 index-trueness pass: the description surfaces OUTSIDE the 7 guarded docs can
also go stale, and 07-methodology/README.md had two such live defects — its OM row still
pinned '(v2.1' after the doc bumped to v2.2 (the §9.3 clarification pass), and its
validate-repo.sh row still described this guard's TO anchors as the superseded two-state
pair 469/6,869 after the v1.4 re-base to 511/6,911. New structural rule
methodology_index_hits: every '(vN.M' version pin on a row naming one of the versioned
methodology docs must equal that doc's own '*Document Version:' footer, and the retired
pair must not reappear. Teeth verified by synthetic injection (stale pin and retired pair
both caught, then restored clean). The root README's drifted 'merge note atop CHANGELOG'
pointer was also re-pointed to the 2026-09-02 branch-reconciliation entry — a
position-independent phrasing, so the class cannot recur there.

2026-09-03 description-trueness pass: three more live description-surface staleness spots
outside the 7 guarded docs — the executive summary's top footer still claimed
"updated counts: … 5,363 workflows" after the event-custody pass moved the canon to 5,364
(batch 5 had trued exactly this line; the W5511 re-point list missed it), the IT operating
model's footer 'Downstream:' pointer still pinned TO v1.4 / technical-guidelines v3.1 /
sourcing v1.1 after the post-AAP pass bumped all three (v1.5 / v3.2 / v1.2), and the
headcount reality-check STATUS banner still cited TO v1.4 / OM v2.1. All three trued, and
the new structural rule live_pin_hits pins every version pin on those surfaces to the
target docs' own '*Document Version:' footer and the executive-summary top footer to the
canonical register totals (index Grand Total; requirement row count). Teeth verified by
synthetic injection (stale OM pin, stale banner pin, and a regressed exec-summary count
all caught, then restored clean).

2026-09-03 consistency review pass: two more straggler classes found and trued, both
outside every previously-read surface. (a) The criticality register's '### Tier 2
Additions' sub-heading still claimed (495 Workflows) after the two 2026-09-03 gap-fill
passes appended six rows to that section (W5512–W5514 agentic, W5515–W5517 sourcing) —
the batch-7 pass had trued the top-level Tier-2 heading and Summary but not this
parenthetical. New structural rule register_heading_hits: every '(n Workflows)'
parenthetical in the register is re-derived from its data rows (direct rows for
family/Additions/history-pass/####-tier headings; the effective per-tier total for the
three '## Tier N' headings), and the effective per-tier totals must equal both the
heading claims and the ## Summary table's per-phase counts — closing the
rows → headings → Summary chain end-to-end. (b) The VS-24 and VS-87 README Process-Areas
tables still carried the pre-W239-move counts (PA-24.3 8/Total 27, PA-87.3 8/Total 24 —
the 03235a5 cascade re-pointed the index/root-README/dependency-map but missed both
README tables; now validator Check 67). Three stale live-body version pins in the
guarded docs also trued in place (sourcing-model header '(v2.0+)' and §13 row '(v2.1:'
re-pinned to OM v2.4; OM §13 row 'this v2.0 model' re-pinned to v2.4).
2026-09-07 eighth-wave consistency review: data-volumes-and-integrations.md joins DOCS
— it had shipped with zero validator coverage (not in this list, not read by any other
check), the sourcing-model/ai-guide precedent. Generic checks verified clean on dry-run
after two repairs: the §1.1 Customer-Registrations row carried a bare '—' peak factor
beside its ~450 peak (now stated as 3.0x sale-event basis; doc bumped to v4.5), and the
literal 6,715 needs a doc-scoped exemption — there it is the canonical AP
merchandise-invoice count (profile §10.2/§15.1), not the retired 6,715 HQ headcount
total. load_registers now also admits the 23 ###/#### sub-workflow ids (W7C is cited by
this doc). Three structural rules join the guard: dv_volume_hits (every §1.1 row
stating a peak must declare its factor and peak = daily × factor within 5%; the §1.2
size column must sum to the stated annual increment and the retention row to ~10× it),
exec_tree_hits (the executive summary's Repository Structure mini-tree must list
exactly the top-level directories on disk — the two-row tree predated the bpmn/ and
dmn/ trees, now added to the summary with a 2026-09-07 footer clause), and
reality_check_hits (the headcount reality-check §3.1 AP bullet's retired '~450/day'
parenthetical — 450/day implies ~13,500/month, matching no licensed convention; the
corrected '~300/day' form is anchored).

2026-09-10 eighteenth-wave consistency review: the shipped-tooling portability class
— ten 07-methodology scripts (audit-misdirected-ctl, classify-isolated-ctl,
fix-ctl-paste-families, fix-ghost-roles-batch26, fix-ghost-titles-batch14,
fix-pa211-order, draw-batch26–29)
carried a hardcoded '/home/riddler' absolute repo path and had therefore been
unrunnable on any other checkout since authoring; all re-pointed to
repo-relative resolution (dirname(dirname(abspath(__file__)))) and verified: the
four draw-batch samplers and both CTL-family measurers exit 0 against the live
corpus (the measurer's 170-citation isolated colon-form census re-derived exactly
as batch 13 hand-adjudicated it — no live defect), fix-ctl-paste-families re-runs
clean at 0 candidates, fix-pa211-order is idempotent (byte-identical output). One
genuine hazard surfaced by the sandbox runs: fix-ghost-roles-batch26 still rewrote
the official TO of record ('VP Finance & Accounting' / 'VP HR' → 'CFO' / 'CHRO') —
its rules predate the v2.0/v2.1 chart, which deliberately carries those strings as
sub-CFO / sub-CHRO seats — and its summary print carried a latent AttributeError
(per_rule is keyed by pattern strings; the loop unpacked them as compiled regexes).
The script now refuses to run while the TO charts those seats (documented sunset
guard; the eleven other rules are inert — the family is closed) and the summary bug
is fixed, and the same sweep caught fix-ghost-titles-batch14 (initially missed —
its '/home/alden' path happened to match this checkout) rewriting its own frozen
batch-14 closure note in workflow-gap-analysis.md on re-run; it now carries the same
documented sunset refusal. Guard armed: Check 39 Part E runs audit-misdirected-ctl.py --guard (zero
wrong-PA paren citations; the batch-13-adjudicated 170-citation colon-form census
pinned at total/per-PA/per-cited-CTL granularity, the Check-74 deferred-anchor
pattern), giving the repo its first automated read of the misdirected-CTL family.
Teeth: a synthetic foreign colon-form citation caught at all three violated surfaces
(total + per-PA + per-CTL), a synthetic wrong-PA paren citation caught at the paren
class, both fired through the full validator's Check 39 error branch, negative test
silent, fixtures restored byte-identical sha256-verified.

2026-09-10 seventeenth-wave consistency review: the batch-24 pass's own re-point
cascade audited — eight stranded spots found on five surface families, all of
them 'the canonical total moved 5,426 → 5,427, the derived quote stayed'. (1) The
generated bpmn tree shipped stale for PA-133.1/PA-133.3 (documentation Volume
'~5,426 workflows' vs the re-pointed markdown) — the batch's 'only PA-07.1's file
moved' regeneration claim was false, and no check could see it because Check 71
read only the trees' STRUCTURE. Validator-side closure: Check 71 now imports the
generator's own parser and requires every process's <bpmn:documentation> text,
start-event name and controls annotation to equal the generator's re-derivation
from its PA markdown — any field edit without regeneration, or any hand-edit of
the generated text, now fails. (2) classification.md stranded FOUR live spots at
the retired totals (intro headline 5,426/5,449; the Coverage 'Confirmed
(hand-reviewed)' row; the Summary Grand-Total row; the §Domain-Breakdown prose)
while Check 18 saw only self-consistency — every stale spot agreed with its stale
neighbours. Check 18 now re-derives the unique/register-row canon from the PA
corpus's ##/### headers every run and pins all six figure surfaces. (3)
workflow-dependency-map.md's intro parenthetical kept 5,449 while its own unique
figure moved — Check 26 extended with the intro pins (unique / rows / sub-workflow
count). (4) The sourcing model's §12.2 candidate-intake figure kept 5,426 while
the doc's own v2.10 footer CLAIMED 'the §12.2 intake figure reads 5,427' —
sourcing_tier_hits read only §12.1; extended to re-derive the canon and pin the
intake figure. (5) PA-128.3's W5512 Volume row kept the then-canonical 5,426 with
Check 27 Part C's static retired band (5,320–5,425) blind to it — the band now
re-derives from the corpus every run ([5,320, canon-unique)), so the guard
re-arms itself at every future batch instead of aging out one total at a time.
Same wave, armed: Check 51's sixteenth-wave '--guard' arming had fixed the
invisible-print class for reconcile-staffing-claims.py only — the validator's
thirteen guard-mode invocations (Checks 50–62) all captured the child's exit code
with 'OUT=$(...); RC=$?' under 'set -e', so any guard FIRING aborted the whole
script before its own error branch could print (verified live: a §12.2 injection
made the run die silently at Check 59 with zero output). All thirteen re-armed
with '&& RC=0 || RC=$?' — a firing guard now prints its violations and the
validation completes with the error count. Teeth verified by eight synthetic
injections each caught at the exact violated rule (classification intro/
Coverage/Grand-Total/Domain; dep-map parenthetical; sourcing §12.2; PA-128.3
Volume; a hand-corrupted PA-133.1 documentation block), fixtures restored
byte-identical sha256-verified — and the teeth caught their own author once
pre-ship (the Grand-Total pin was forgotten in the first draft: injection 2
passed with the row self-consistent at 5,426, the exact failure mode this wave
closes; the pin was added and re-verified firing).

2026-09-09 sixteenth-wave consistency review: three stranded-derived-figure classes
found live and closed — all of them 'the canonical table moved, the derived quote
stayed'. (1) Revenue-per-employee: the v2.22 rebalance bumped the §4 note's division
denominator 6,757 → 6,762 but the quotient stayed '~PHP 9.22M' (correct only at 6,757;
62.3B ÷ 6,762 = ~9.21M) — stranded on the profile's own §4 note (whose parenthetical
division contradicted its quotient), assumptions A2.6, PA-133.3's Volume row, and this
module's own #41 self-description above, which had verified the stale figure as
matching the registers. (2) The B2B account scheme: the v2.23 canonicalization moved
§9.2/§10.3 to trade ~5,200 / corporate ~200 / AR ~5,400 but §15.2's Master-Data row
kept the retired '5,000', and PA-11.2's live prose quoted '(5,000 accounts, ~30% of
revenue)'. (3) The DC-catchment range/average — closed over in
reconcile-staffing-claims.py (Check 51), which already owns profile-table-vs-PA-prose
claims. New structural rule profile_derived_figure_hits re-derives the quotient and
the account counts from the profile's own §9.4/§4/§9.2 rows every run, requires the
corrected anchors (the §4 quotient line and the §15.2 Master-Data rows), and sweeps
the live corpus (PA files, the workflows support docs, the root/methodology docs;
CHANGELOG, the generated trees, version-history footers, and the gap-analysis scenario
table's authoring-time rows exempt) for citations that disagree with the derivation.
2026-09-07 ninth-wave consistency review: the reverse-direction companion-pin family
— the mirror images of the live_pin_hits surfaces, read by no rule — found live and
closed: the sourcing model's header 'Companion to' OM pin stranded at v3.3 since
batch-19 (the batch-20 cascade's 'header/§13 OM pins re-pointed' claim re-pointed
only the §13 row), its §13 Related-Documents OM row frozen at v3.4, its footer
companion-pin chain broken by the sixth-wave OM v3.8 bump (the sourcing model stayed
at v2.7 — every batch-16→23 OM bump had produced a sourcing companion bump), and the
OM's own §13 doc-map self-pin 'this vN.M model' still at the v2.4 of the 2026-09-03
pin pass through six subsequent OM bumps. Repairs: the three sourcing pins re-pointed
to v3.8 and the sourcing model bumped to v2.8 so the newest footer clause reads true
(the OM Downstream pointer re-pointed v2.7 → v2.8; the OM self-pin trued in place per
the description-trueness convention — the OM itself stays v3.8). New structural rule
companion_pin_hits pins all four surfaces to the pinned doc's live footer every run.
2026-09-07 tenth-wave consistency review: adjudicated and closed the sixth wave's
'flagged for adjudication, not repaired' residual — the OM §4.9 SSP row's VS-151
enumeration vs its 882 workload figure. Found the mismatch as old as the document
(the v1.0 §3.2 carried SSP 873 / DP 210 with the same asymmetry) and the mapping
side unanimous (§4.3's SSP row, §4.9's explicit '+1 (VS-151)', the Sell & Serve
family partition): the workflow figures were the wrong side — SSP 882 → 906, DP
213 → 189, and the same re-derivation exposed a second latent drift, the
hand-maintained subtotal split sitting ±3 off its own member rows (4,913 + 513
declared vs 4,910 + 516 derived) — subtotals re-based to the member sums
4,934 + 492 (total unchanged 5,426); the OM bumped to v3.9 with the sourcing
companion chain re-pointed (sourcing v2.9) and the reality-check banner pin moved
to v3.9. om_reconciliation_hits extended to re-derive every §3.2 per-team cell and
subtotal and every §4.9 per-team workflow cell from the §4.1–4.8 mapping tables and
the on-disk `##` headers each run — the whole portfolio series, not just its
cross-foots; the ANCHOR re-pinned to the corrected literals.

2026-09-07 eleventh-wave consistency review: the AI-first operating guide's version
footer was found inverted — the header had stayed at '1.0 | Initial issue' while all
eight batch-16–23 re-point cascades appended 'Prior v1.1'–'Prior v1.8' clauses BELOW
it, each with a higher version number and a later date; methodology_index_hits could
not see it because the index row's own '(v1.0' pin satisfied itself off the same
stale footer (the anchor-satisfying-itself-off-history failure mode, in its pin
form). Footer re-based newest-first to live v1.9 with the initial issue demoted to
the chain's end; the index and root-README pins re-pointed; the class is now closed
repo-wide by validate-repo.sh Check 72 (every versioned footer's Prior chain must be
strictly decreasing below the live version), which this module deliberately does not
duplicate — the footer chain is a cross-document invariant, not a per-doc one.

2026-09-07 twelfth-wave consistency review: full re-verification clean (both
generators byte-identical; canonical registers re-derived exact — 188 VS / 569 PA /
5,426 ## headers + 23 ### sub-workflows = 5,449 register rows / 808 CTL / 728 Req /
6,762 HC; version chains, companion pins and retired-figure sweeps all clean; the
twin integration-diagram copies byte-identical and the bpmn//dmn coverage figures
correct on every quoted surface). Two guard gaps closed in validate-repo.sh, both
from surfaces this module's per-doc scope legitimately never read: Check 73 pins
the canonical integration diagram (data-volumes §2) byte-identical to its declared
convenience duplicate (technical-guidelines §3.2) — waves 7/9/11 had each re-verified
the twin copies by hand; Check 74 re-derives the generated-tree coverage figures
(bpmn 569/5,449/23,008/28,457/5,449 by the generator's own userTask+serviceTask
task definition; dmn 40/79/339) and asserts them on the bpmn/README and dmn/README
quick-stats tables and the root-README, generator-row and exec-summary tree rows,
with the dmn/README deferred-rule-set anchor (197) pinned. This module also gained
the methodology-README completeness repair — the two generators were the only .py
files on disk missing from that index's Contents table — and the check-count
self-descriptions re-pointed 72 → 74 across the guide §8.5 triple, the root-README
tree row and the methodology-index validate-repo row.

2026-09-09 thirteenth-wave consistency review: the official TO's v2.0 register issuance
(machine-verified at commit, but with no rule re-deriving it) trued and brought under
the guard. Three self-description defects repaired in optimal-table-of-organization.md:
the v2.0 footer's '≈150 distinct roles' (the register holds 188 rows / 187 distinct
titles); the §5.3 span note's 'the Controller's direct span at 7 and the Assistant
Controller's at 3' (7 is the §5.2 sub-team-line count — the register's two Logistics &
Cost Finance analyst rows give 8 reporting rows, in-band; and the 'at 3' counted only
the 3 administrative cluster lines, not the Assistant Controller's own 6-person GL &
consolidation team); and one §5.2 mix-cell conformance miss of the class the v2.0 pass
itself had repaired for Store Operations and AR & Credit — GL & Consolidation still
read the pre-register 'GL accountant per entity (5) + consolidation/elimination (2)'
blend with no head box where the register rows are the dual-hat manager + 5 GL
accountants + 1 consolidation & intercompany accountant. TO bumped to v2.1 with the
repairs described in a live clause; the v2.0 clause stands below as written, corrected
by this clause. New structural rule to_register_hits re-derives §5.1's 18-department
current/target columns and two-state total rows (incl. store/DC cross-foot to
6,762/6,911), the three §5.2 sub-team tables (headers may sit up to six prose lines
above their table — the Finance header's own '(3-way match,' parenthetical wraps — but
a following '**bold**' header terminates the scan so a header can never adopt the next
department's table), every §5.3 department-table HC foot (IT exempt as by-reference),
the §5.1↔§5.3 per-department pairing, the register-total footer line, the quoted
'N rows / M distinct role titles' and the span note's 'N register reporting rows'.
Teeth verified by twelve synthetic injections (HC cell, §5.1 target/current cell,
all three §5.2 tables, §5.3 declaration/pairing, both footer figures, span-note count,
register-total line; fixtures restored byte-identical sha256-verified) — and the
teeth suite caught its own author twice pre-ship (the §5.2 cell regex's '(?!Sub-team|
[- ])' lookahead rejected every normal '| ' row since rows begin with a space; the
first header→table adjacency pattern required the table to start on the line after a
header whose own parenthetical prose wraps). The twelfth wave's claim that the two
generators were the only .py files missing from the methodology README's Contents
table was itself wrong — fix-ghost-titles-batch14.py (the batch-14 ghost-title charter
sweep, listed in the root-README tree and cited by workflow-gap-analysis.md) was also
absent; a Contents row now ships with this wave.

2026-09-14 nineteenth-wave consistency review: the 02-oracle-ebs platform-blueprint
folder joins the doc set — seven documents issued 2026-09-14 that no check read (the
fifteenth-wave 'entire files' class one layer out), and the review found eight defects
across five of them: the coverage-map §2 roll-up carried six invented template family
names (Plan & Buy / Make & Improve / Move & Store / Count & Comply / People & Culture /
Finance & Growth) with headlines written to the invented names — warehouse text on the
785-workflow Finance row, statutory-filings text on the 445-workflow People row, payroll
text on the 323-workflow Asset & Infrastructure row, GL/AP/AR text on the 976-workflow
Governance & Assurance row — and §1 was missing two of the touchpoint map's 36 module
rows despite the one-for-one claim (Innovation & Digital Transformation; Document
Management); the architecture §2 planning paragraph kept the v1.0 'ASCP/Demantra
evaluation' wording after fit-gap C5/§4-2 resolved adoption the same day, its §7 NFR
row quoted the e-wallet SUBSET (~17,000/month, PA-15.2) as the ecommerce total against
the profile's ~42,900/month canon, and its §3 stack table carried an 'RPO/RPO' typo;
the fit-gap §3 Reading note's BUILD split ran 6 pre-date / 4 new-scope against the
register's true 4/6 (OMO D10 + DP H6 + IAP H7 + AAP H9 pre-date; the payroll trio E5–E7,
workforce E3, dispatch D13 and space-planning F4 are the doctrine's six new-scope rows;
TPS carries no register row); the customization-governance §2 budget kept the v1.0
'4 components' LOC-pack count against the register's single G4 row (its own footer
already said '2 EXT / 1 LOC row'); and the integrations §2 SSS row kept the retired
'PAY-PH pack' terminology for files the in-house Payroll PH build (E6) generates. All
repaired in place (no version bumps, the twelfth–seventeenth-wave no-bump precedent);
the guard gains ebs_blueprint_hits — the fit-gap §2 register's class column re-derived
every run and pinned on the §3 table, the intro headline and the Reading-note split
(counts must sum to the planned rows and name them), the touchpoint-map module set
mirrored exactly by coverage-map §1, the canonical family names/counts mirrored in
order by coverage-map §2, the §7 ecommerce total re-derived from the profile's
Total-Ecommerce-Orders row, and the README §4 wave prose pinned to the classification
register's re-derived tier ladder; doc-scoped retired literals hold the six invented
family names, the subset-as-total and evaluation wordings, 'RPO/RPO' and 'PAY-PH pack'
out of their documents. W0 joined the token scan's exemptions (the realization-wave
tables label their foundation wave 'W0 — Foundation'; the register's ids start at W1),
and the sourcing-model + folder sections joined the bare-§ fallback union (the
citations 'sourcing model §12.1' and 'architecture §4' are cross-doc).

2026-09-14 twenty-first-wave consistency review: the doctrine cascade's
 canonical-integration strand closed — the two-tier doctrine's payroll posting
 flow (fit-gap E8 INT; 02-oracle-ebs/data-migration row 11) had never reached
 data-volumes §3's canonical Integration Detail Matrix, the EBS pattern
 register's Flow column claimed to 'quote the canonical matrix rows' while the
 gateway chargeback/fee row had no canonical counterpart and the canonical
 delivery-status row was silently folded into the outbound 3PL row, and the
 legacy mapping template still routed payroll YTD into the ERP against
 data-migration row 11 — repaired in place and the whole class brought under
 guard with integration_mirror_hits (the §3 matrix re-derived every run with
 the Payroll PH posting row required; the register's Flow sequence required
 equal to the canonical sequence after the one declared extension, endpoints
 verbatim) and migration_template_hits (the corrected §1/§2.4 anchors
 required, the retired YTD-into-EBS routing forbidden, the 02 row-11 anchor
 required present).
"""

def _doc_versions():
    """Current '*Document Version:' footer of each versioned doc (basename -> 'N.M')."""
    versions = {}
    for rel in ["optimal-table-of-organization.md",
                "model-company-profile.md",
                "../07-methodology/it-product-operating-model.md",
                "../07-methodology/capability-sourcing-and-engineering-model.md",
                "../07-methodology/technical-guidelines.md"]:
        m = re.search(r"^\*Document Version: (\d+\.\d+)",
                      open(os.path.join(MC, rel), encoding="utf-8").read(), re.M)
        if m:
            versions[os.path.basename(rel)] = m.group(1)
    return versions


def _pin_hits(segment, base_line, where, versions, names):
    """The LAST 'name' occurrence in the segment carries the live pin (both surfaces
    append newest-at-the-end / newest-on-top respectively, so the newest pin is the
    one adjacent to the last mention); it must equal the target doc's footer version,
    and a bare mention with no 'vN.M' within the pin window is itself a defect."""
    hits = []
    for name in names:
        want = versions.get(name)
        if want is None:
            hits.append((where, 0, f"{name} has no parseable '*Document Version:' footer"))
            continue
        pos = segment.rfind(name)
        if pos < 0:
            hits.append((where, 0, f"{name} not referenced in {where}"))
            continue
        line = base_line + segment[:pos].count("\n")
        # pin window ends at the next '.md' boundary so an adjacent doc's pin
        # can never be attributed to this name
        nxt = segment.find(".md", pos + len(name))
        window = segment[pos + len(name): nxt + 3 if nxt >= 0 else pos + len(name) + 120]
        m = re.search(r"v(\d+\.\d+)", window)
        if not m:
            hits.append((where, line,
                         f"{name} mentioned in {where} without a version pin "
                         f"(doc footer says v{want})"))
        elif m.group(1) != want:
            hits.append((where, line,
                         f"{name} pinned at v{m.group(1)} in {where} but the doc "
                         f"footer says v{want}"))
    return hits


def live_pin_hits():
    """2026-09-03 description-trueness pass — pins the three live description surfaces
    outside the guarded docs (all three found stale in the same pass): the IT operating
    model's footer 'Downstream:' pointer, the headcount reality-check STATUS banner, and
    the executive summary's top footer count line (its only workflow/requirement-count
    claim). Version pins must equal the target docs' own '*Document Version:' footers,
    and the executive-summary counts must equal the canonical registers (index Grand
    Total row; requirement register row count)."""
    hits = []
    versions = _doc_versions()
    # (a) IT operating model footer 'Downstream:' pointer (last 'Downstream:' in the doc)
    om = open(os.path.join(MC, "..", "07-methodology", "it-product-operating-model.md"),
              encoding="utf-8").read()
    pos = om.rfind("Downstream:")
    if pos < 0:
        hits.append(("it-product-operating-model.md", 0,
                     "footer 'Downstream:' pointer not found"))
    else:
        hits.extend(_pin_hits(om[pos:], om[:pos].count("\n") + 1,
                              "it-product-operating-model.md (Downstream)",
                              versions,
                              ["optimal-table-of-organization.md",
                               "model-company-profile.md",
                               "technical-guidelines.md",
                               "capability-sourcing-and-engineering-model.md"]))
    # (b) headcount reality-check STATUS banner (first 10 lines — newest-last chain)
    rc = open(os.path.join(MC, "headcount-reality-check.md"), encoding="utf-8").read()
    banner_lines = rc.splitlines()[:10]
    banner = "\n".join(banner_lines)
    hits.extend(_pin_hits(banner, 1,
                          "headcount-reality-check.md (STATUS banner)", versions,
                          ["optimal-table-of-organization.md",
                           "it-product-operating-model.md"]))
    # (c) executive summary top footer counts vs the canonical registers
    ex = open(os.path.join(MC, "executive-summary.md"), encoding="utf-8").read()
    top = re.search(r"^\*Date: (.*)$", ex, re.M)
    if not top:
        hits.append(("executive-summary.md", 0, "no '*Date:' footer entry found"))
    else:
        ex_line = ex[:top.start()].count("\n") + 1
        idx = open(os.path.join(MC, "workflows", "value-stream-index.md"),
                   encoding="utf-8").read()
        mwf = re.search(r"\*\*Grand Total\*\* \| \*\*[\d,]+\*\* \| \*\*([\d,]+)\*\*", idx)
        reqs = open(os.path.join(MC, "erp-requirements.md"), encoding="utf-8").read()
        nreq = len(set(re.findall(r"^\| (?:\*\*)?[A-Z]+-\d+[a-z]?\b", reqs, re.M)))
        if not mwf:
            hits.append(("executive-summary.md", 0,
                         "value-stream-index Grand Total row not parseable"))
        elif f"{mwf.group(1)} workflows" not in top.group(0):
            hits.append(("executive-summary.md", ex_line,
                         f"top footer does not carry the canonical '{mwf.group(1)} workflows' "
                         f"(index Grand Total)"))
        if f"{nreq} requirements" not in top.group(0):
            hits.append(("executive-summary.md", ex_line,
                         f"top footer does not carry the canonical '{nreq} requirements' "
                         f"(requirement register row count)"))
    return hits


import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MC = os.path.join(REPO, "01-model-company")

# Paths relative to MC (".."-prefixed entries live in 07-methodology).
# Consistency review #68 (2026-09-02) brought the two organizational documents
# issued 2026-09-01/02 under this guard — both had shipped with zero validator
# coverage, and the review found three figure/citation defects between them.
DOCS = ["mobile-app-strategy.md", "data-migration-mapping.md",
        "assumptions-and-design-decisions.md",
        "optimal-table-of-organization.md",
        # 2026-09-07 eighth-wave consistency review: data-volumes-and-integrations.md
        # joins the doc set — it had shipped with zero validator coverage (not in this
        # list, not read by any other check), the sourcing-model/ai-guide precedent
        # that the quantitative doc outside the guard is the one that drifts. Generic
        # checks verified clean on dry-run (tokens W7/W7C, §10.2, no retired totals
        # beyond the scoped 6,715 exemption below); the guard gains the dv_volume_hits
        # structural rule for its §1.1/§1.2 arithmetic.
        "data-volumes-and-integrations.md",
        "../07-methodology/it-product-operating-model.md",
        "../07-methodology/capability-sourcing-and-engineering-model.md",
        "../07-methodology/technical-guidelines.md",
        # 2026-09-04 guard-extension pass: shipped v1.0 outside the guard (the
        # sourcing-model precedent); generic checks verified clean on dry-run.
        "../07-methodology/ai-first-operating-guide.md",
        # 2026-09-14 nineteenth-wave consistency review: the whole 02-oracle-ebs
        # platform-blueprint folder joins the doc set — seven documents issued
        # 2026-09-14 that no check read (the fifteenth-wave 'entire files' class one
        # layer out: the folder shipped with zero validator coverage through both
        # same-day issues, and the review found eight defects across five of the
        # seven — the coverage-map's six invented family names and its two missing
        # touchpoint-map module rows, the architecture's stale ASCP/Demantra
        # 'evaluation' wording, its ~17,000-ecommerce subset-as-total NFR figure and
        # the RPO/RPO typo, the fit-gap Reading note's 6/4 BUILD-split inversion,
        # the customization-governance budget's stale 4-component LOC row, and the
        # integrations SSS row's retired 'PAY-PH pack' terminology). Generic sweeps
        # verified clean after the repairs; the guard gains the ebs_blueprint_hits
        # structural rule (fit-gap §2→§3 class-count re-derivation + Reading-note
        # BUILD split, touchpoint-map module-set mirror, canonical family-name
        # mirror, ecommerce-total re-derivation, tier-ladder pin).
        "../02-oracle-ebs/README.md",
        "../02-oracle-ebs/ebs-platform-architecture.md",
        "../02-oracle-ebs/module-coverage-map.md",
        "../02-oracle-ebs/fit-gap-analysis.md",
        "../02-oracle-ebs/customization-governance.md",
        "../02-oracle-ebs/integrations.md",
        "../02-oracle-ebs/data-migration.md"]
RETIRED_FIGURES = ["6,757", "6,715", "5,357", "5,362", "5,349", "5,341",
                   "80,000 SKU", "1,000 POS terminal"]

# 2026-09-07 eighth-wave review — per-doc retired-figure exemptions. In
# data-volumes-and-integrations.md the literal 6,715 is the canonical AP
# merchandise-invoice count (~6,715/month, 3-way match per W7 — profile §10.2/§15.1),
# not the retired 6,715 HQ headcount total: the one surface where the digits
# legitimately recur.
RETIRED_FIGURE_EXEMPT = {"data-volumes-and-integrations.md": {"6,715"}}

# Consistency review #68 — doc-scoped retired literals (the exact defect forms
# the review repaired; matches on version-history footer lines are exempt) and
# required presence anchors (the corrected canonical forms must stay present).
RETIRED_LITERALS = {
    "it-product-operating-model.md": [
        # the canonical integration architecture (data-volumes-and-integrations.md
        # §2 diagram and §3 detail matrix) carries exactly ten external clusters
        "11 external integration clusters",
        # the profile's seasonal calendar is §13.2; §13.3 is Promotional Strategy
        "§13.3 seasonal calendar",
        # 2026-09-03 hybrid capability-sourcing revision (OM v2.0): the unified-model
        # sizing/shape literals are retired — 16 teams / 115 FTE is the canon
        "80-FTE steady-state sizing",
        "Phased build-up (50 → 80)",
        "80-FTE IT sizing",
        # 2026-09-03 agentic extension (OM v2.1): sizing 115 → 122 (AAP +7)
        "Steady-state design (115 IT FTE)",
        "Phased build-up (50 → 115)",
        "115-FTE IT sizing",
    ],
    "optimal-table-of-organization.md": [
        # §7.3 Outbound role HCs sum to 50 (the 150 grand total confirms)
        "Outbound (51)",
        # unresolvable subsection-style self-reference (§2 has no §2.4 heading)
        "three-lines model, §2.4",
        # 2026-09-03 hybrid revision (TO v1.3): target is HQ 504 / total 6,904 with
        # IT = 115 / 16 product teams — the v1.2 literals are retired
        "12 product teams per",
        "IT 50→80",
        "80 FTE, 12 product teams",
        # 2026-09-03 agentic extension (TO v1.4): target HQ 511 / total 6,911, IT = 122 / 17 teams
        "16 product teams per",
        "IT 50→115",
    ],
    # 2026-09-14 nineteenth-wave consistency review — the repaired defect forms of
    # the 02-oracle-ebs blueprint must not come back (per-doc scope: 'People &
    # Culture' legitimately appears in W3989's workflow title elsewhere, and the
    # ~17,000 e-wallet-subset figure legitimately appears in PA-15.2 — only these
    # documents misused them):
    "module-coverage-map.md": [
        # §2's roll-up table carried six invented template family names against the
        # workflow catalog's canonical eight (the canonical names/counts are
        # re-derived and pinned every run by ebs_blueprint_hits)
        "Plan & Buy",
        "Make & Improve",
        "Move & Store",
        "Count & Comply",
        "People & Culture",
        "Finance & Growth",
    ],
    "ebs-platform-architecture.md": [
        # the §7 NFR row quoted the e-wallet SUBSET volume (~17,000/month,
        # PA-15.2) as the ecommerce total; the canonical total is ~42,900/month
        # (re-derived from the profile's Total-Ecommerce-Orders row by
        # ebs_blueprint_hits)
        "+ ~17,000 ecommerce",
        "~17,000 ecommerce transactions/month",
        # the §2 planning paragraph kept the v1.0 'evaluation' wording after
        # fit-gap C5/§4-2 resolved adoption the same day
        "evaluation vs. the in-house ROP/forecast pipeline",
        # §3 tech-stack typo (the canon pairing is RPO/RTO)
        "RPO/RPO",
    ],
    "integrations.md": [
        # the §2 SSS/PhilHealth/Pag-IBIG row kept the v1.0 'PAY-PH pack'
        # terminology after the payroll localization pack was retired (the agency
        # files are generated by the in-house Payroll PH build, fit-gap E6;
        # Oracle Payroll unadopted)
        "PAY-PH pack",
    ],
}
ANCHORS = {
    "it-product-operating-model.md": [
        "10 external integration clusters",
        "§13.2 seasonal calendar",
        "**171 + 17 = 188**",
        # 2026-09-05 sixth-wave review: re-pinned from the stale '4,911 + 511 = 5,422'.
        # The batch-23 pass updated §4.9's per-team rows and the version footer but not
        # the Total row — and this anchor kept passing because the stale literal survived
        # verbatim inside the Prior-v3.6 footer text, i.e. the anchor was satisfying
        # itself off history. The Total row is now guarded structurally below by
        # om_reconciliation_hits (re-derived from the index Grand Total every run), so
        # this anchor can never again be the only line of defense.
        # 2026-09-07 tenth-wave review: re-pinned again after the VS-151 adjudication
        # (SSP 906 / DP 189) re-based the subtotals to their member sums 4,934 + 492.
        # 2026-09-10 batch-24 re-pin: W5574 (PA-07.1, VS-07 -> SSP) trues SSP 906 -> 907;
        # the subtotals re-foot to 4,935 + 492 and the total to 5,427.
        "**4,935 + 492 = 5,427**",
        # §3.2 portfolio-table subtotal/total rows (structurally re-derived from the
        # §4 mapping + disk by om_reconciliation_hits — these pin the corrected forms'
        # presence)
        "**171** | **4,935**",
        "**17** | **492**",
        "**188** | **5,427**",
        # v2.0 hybrid sizing anchor (66 domain + platform/CIO = 115 FTE); v2.1 agentic
        # re-bases it to 122 (66 + 56, AAP +7)
        "**66 + 56 = 122**",
    ],
    "optimal-table-of-organization.md": [
        "Outbound (50)",
        "**511** | **6,911**",
        "**Total HQ** | **362** | **~440–515** | **511**",
        "**504 + 7 = 511**",
        "× 4 DCs = **600**",
    ],
    # 2026-09-07 eighth-wave review — the corrected forms the data-volumes doc's own
    # v4.3/v4.4 repair chain produced must stay present (they are the anchors the new
    # dv_volume_hits rule reasons about).
    "data-volumes-and-integrations.md": [
        "10-Year Retention",
        "~300/day is the midpoint",
    ],
    # 2026-09-14 nineteenth-wave consistency review — the corrected forms the
    # 02-oracle-ebs repairs produced must stay present (ebs_blueprint_hits
    # re-derives their figures structurally; these pin the exact phrasings).
    "ebs-platform-architecture.md": [
        "RPO/RTO targets",
        "**adopted** as the planning stack",
        "~42,900 ecommerce orders/month",
    ],
    "customization-governance.md": [
        "1 register row (G4 — the EBS-held BIR indirect-tax pack",
    ],
    "fit-gap-analysis.md": [
        "of which 4 rows predate",
        "5 rows are new scope the doctrine creates",
    ],
    "module-coverage-map.md": [
        "| **Innovation & Digital Transformation** |",
        "| **Document Management** |",
    ],
}

# Consistency review #60: BIR Forms 1601-E/1601-F were discontinued by RR 11-2018
# (replaced by the quarterly 1601-EQ creditable / 1601-FQ final remittance
# returns). Guarded here in the two statutory-citation model docs (profile
# §10.5/§16 and erp-requirements FIN rows); the PA files are guarded by Check 62's
# legacy_form rule. Version-history footers are exempt — they legitimately name
# the retired form when describing the change.
LEGACY_FORM = re.compile(r"1601-[EF](?!Q)")
LEGACY_FORM_DOCS = ["model-company-profile.md", "erp-requirements.md"]


def legacy_form_hits(path):
    hits = []
    for i, line in enumerate(open(path, encoding="utf-8").read().splitlines(), 1):
        if line.startswith("*Document Version:"):
            continue
        for m in LEGACY_FORM.finditer(line):
            hits.append((os.path.basename(path), i,
                         f'retired BIR form "{m.group(0)}" '
                         f'(use 1601-EQ/1601-FQ per RR 11-2018)'))
    return hits


def load_registers():
    wids, vsids, paids, ctlids, reqids = set(), set(), set(), set(), set()
    for f in glob.glob(os.path.join(MC, "workflows", "VS-*", "PA-*.md")):
        text = open(f, encoding="utf-8").read()
        wids |= set(re.findall(r"^## (W\d+[A-Z]?)\.", text, re.M))
        # 2026-09-07 eighth-wave review: the 23 ###/#### sub-workflows (W7C, W5A, …)
        # are defined workflows — register rows 5,449 = 5,426 ## + 23 ###/#### — so
        # their ids belong in the token-resolution register (a strict superset; only
        # makes more tokens resolve, e.g. W7C cited by data-volumes-and-integrations.md).
        wids |= set(re.findall(r"^### (W\d+[A-Z]?)\.", text, re.M))
        wids |= set(re.findall(r"^#### (W\d+[A-Z]?)\.", text, re.M))
        m = re.match(r"(PA-\d+\.\d+)", os.path.basename(f))
        if m:
            paids.add(m.group(1))
    vsids |= set(re.findall(r"\bVS-\d+\b",
                            open(os.path.join(MC, "workflows", "value-stream-index.md"),
                                 encoding="utf-8").read()))
    ctlids |= set(re.findall(r"^\| (CTL-\d+) ",
                             open(os.path.join(MC, "internal-controls-matrix.md"),
                                  encoding="utf-8").read(), re.M))
    reqids |= set(re.findall(r"^\| ([A-Z]+-\d+) ",
                             open(os.path.join(MC, "erp-requirements.md"),
                                  encoding="utf-8").read(), re.M))
    return wids, vsids, paids, ctlids, reqids


def sections_of(path):
    return set(re.findall(r"^#{2,4} (\d+(?:\.\d+)*)[.\s]",
                          open(path, encoding="utf-8").read(), re.M))


def strip_footer(text):
    """Change-note exemption: everything from the first version-history footer line
    ('*Date: …' or '*Document Version: …') to end-of-file is a change-note and is
    exempt from the retired-literal / resolution checks. (The previous regex stripped
    only up to the footer's first ')' — which exempted almost nothing for the
    '*Document Version:'-style footers the 2026-09-03 org documents use.)"""
    m = re.search(r"^\*(?:Date|Document Version):", text, flags=re.M)
    return text[:m.start()] if m else text


def dc_roster_hits(path):
    """Consistency review #68 — structural guard for the target-state TO's §7.3
    DC roster: re-derives every group header's '(N)' from the HC cells beneath
    it, checks the group headers against the stated grand total, and checks the
    grand total against the '× 4 DCs = 600' chain-total anchor. (The review
    found the Outbound group labelled 51 while its roles sum to 50.)"""
    rel = "optimal-table-of-organization.md"
    hits = []
    lines = open(path, encoding="utf-8").read().splitlines()
    start = next((i for i, l in enumerate(lines)
                  if l.strip().startswith("| Function | Role | HC")), None)
    if start is None:
        return [(rel, 0, "DC roster table (§7.3) not found")]
    groups, cur, grand = [], None, None
    for ln, l in enumerate(lines[start + 1:], start + 2):
        if not l.strip().startswith("|"):
            break
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        m = re.fullmatch(r"\*\*(.+?) \((\d+)\)\*\*", cells[0])
        if m:
            cur = {"name": m.group(1), "declared": int(m.group(2)),
                   "sum": 0, "line": ln}
            groups.append(cur)
        if cur is not None and re.fullmatch(r"\d[\d,]*", cells[2]):
            cur["sum"] += int(cells[2].replace(",", ""))
        if cells[1] == "**Total**":
            mm = re.search(r"\d[\d,]*", cells[2])
            if mm:
                grand = int(mm.group(0).replace(",", ""))
    for g in groups:
        if g["sum"] != g["declared"]:
            hits.append((rel, g["line"],
                         f"DC roster group '{g['name']}' header says ({g['declared']}) "
                         f"but its HC cells sum to {g['sum']}"))
    declared_total = sum(g["declared"] for g in groups)
    if grand is None:
        hits.append((rel, 0, "DC roster grand-total row not found"))
    elif grand != declared_total:
        hits.append((rel, 0, f"DC roster grand total {grand} != sum of group "
                             f"headers {declared_total}"))
    if grand == 150 and not any("× 4 DCs = **600**" in l for l in lines):
        hits.append((rel, 0, "DC roster 150-grand-total anchor '× 4 DCs = **600**' missing"))
    return hits


def sourcing_tier_hits():
    """2026-09-03 post-AAP pass — structural guard for the sourcing model's §12.1
    autonomy ladder: its three tier counts are re-derived from the criticality
    register's Summary table on every run. (The pass found the ladder quoting the
    pre-confirmation trio 1,375/3,243/754 — the register as it stood before the
    2026-09-02 post-catalog confirmation — because the doc shipped outside this
    guard's doc set.)"""
    rel = "capability-sourcing-and-engineering-model.md"
    hits = []
    reg = open(os.path.join(MC, "workflows", "workflow-criticality-classification.md"),
               encoding="utf-8").read()
    canon = {}
    confirmed = re.search(r"### Confirmed classification.*?(?=^### |^## )", reg,
                          re.M | re.S)
    if confirmed:
        for m in re.finditer(r"^\| Phase (\d) \| [^|]+ \| ([\d,]+) \|", confirmed.group(0), re.M):
            canon[f"Tier {m.group(1)}"] = int(m.group(2).replace(",", ""))
    if len(canon) != 3:
        return [(rel, 0, "criticality register Summary table not parseable — "
                         "cannot derive canon tier counts")]
    src = open(os.path.normpath(os.path.join(MC, "..", "07-methodology", rel)),
               encoding="utf-8").read()
    body = strip_footer(src)
    quoted = {}
    for m in re.finditer(r"\*\*Tier (\d)\*\* \(([\d,]+)", body):
        quoted[f"Tier {m.group(1)}"] = int(m.group(2).replace(",", ""))
    if len(quoted) != 3:
        hits.append((rel, 0, f"autonomy-ladder tier counts incomplete: found "
                             f"{sorted(quoted)} — expected three '**Tier N** (n)' cells"))
    for tier, want in sorted(canon.items()):
        got = quoted.get(tier)
        if got != want:
            hits.append((rel, 0, f"autonomy ladder quotes {tier} = {got} but the "
                                 f"register Summary says {want}"))
    # 2026-09-10 seventeenth-wave extension — the §12.2 candidate-intake figure: the
    # batch-24 pass re-pointed the §12.1 ladder and this doc's own footer (whose clause
    # CLAIMS 'the §12.2 intake figure reads 5,427 workflows') while stranding the §12.2
    # body at the retired 5,426 — sourcing_tier_hits read only §12.1. Re-derive the
    # unique-workflow canon from the PA files' ## headers every run and pin the intake
    # figure, so the guard can never again satisfy itself off a footer beside a stale body.
    uniq = set()
    wf_dir = os.path.join(MC, "workflows")
    for d in os.listdir(wf_dir):
        if not d.startswith("VS-"):
            continue
        dd = os.path.join(wf_dir, d)
        if not os.path.isdir(dd):
            continue
        for fn in os.listdir(dd):
            if fn.startswith("PA-") and fn.endswith(".md"):
                uniq.update(re.findall(r"^## (W\d+[A-Z]?)\.",
                                       open(os.path.join(dd, fn), encoding="utf-8").read(), re.M))
    canon_unique = len(uniq)
    m_intake = re.search(r"Candidate intake.*?Automation Opportunity inventory "
                         r"\(([\d,]+) workflows\)", body, re.S)
    if not m_intake:
        hits.append((rel, 0, "§12.2 candidate-intake figure not found "
                             "(expected 'Candidate intake … Automation Opportunity inventory (N workflows)')"))
    else:
        got = int(m_intake.group(1).replace(",", ""))
        if got != canon_unique:
            line = body[:m_intake.start()].count("\n") + 1
            hits.append((rel, line, f"§12.2 candidate-intake figure says {got:,} workflows "
                                    f"but the PA corpus re-derives {canon_unique:,} unique ## headers"))
    return hits


def to_phase_hits():
    """2026-09-03 post-AAP pass — structural guard for the target-state TO's §11
    phasing table: each phase row's HC-delta cell must equal the sum of the
    from→to moves named in its own Moves cell; the three deltas must sum to the
    stated total; and that total must equal target-minus-current HQ. (The pass
    found the cells internally inconsistent since adoption — −7/−6/+13 against
    their rows — because each IT re-base bumped only the Phase 3 cell.)"""
    rel = "optimal-table-of-organization.md"
    hits = []
    lines = open(os.path.join(MC, rel), encoding="utf-8").read().splitlines()
    start = next((i for i, l in enumerate(lines) if "Sizing & Phasing" in l), None)
    if start is None:
        return [(rel, 0, "§11 Sizing & Phasing section not found")]
    pair_re = re.compile(r"([A-Za-z][A-Za-z/&\- ]*?)\s*(\d[\d,]*)\s*[→-]>?\s*(\d[\d,]*)")
    # (the doc uses the unspaced '14→20' form; a spaced '14 -> 20' form is accepted too)
    deltas = []
    total_declared = None
    total_range = None
    for l in lines[start:start + 40]:
        if not l.strip().startswith("|"):
            if deltas and total_declared is None:
                break
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        if cells[2] == "**Total**" or (cells[0] == "" and "**Total**" in cells):
            mm = re.search(r"\*\*(\d[\d,]*)\s*→\s*(\d[\d,]*)\s*\(\+([\d,]+)\)\*\*",
                           cells[3] or "")
            if mm:
                total_range = (int(mm.group(1).replace(",", "")),
                               int(mm.group(2).replace(",", "")))
                total_declared = int(mm.group(3).replace(",", ""))
            continue
        if not re.match(r"\*\*\d", cells[0] or ""):
            continue
        moves, declared = cells[2], cells[3]
        moves, declared = cells[2], cells[3]
        mm = re.search(r"\+([\d,]+)", declared)
        if not mm:
            continue
        declared_n = int(mm.group(1).replace(",", ""))
        named = 0
        for a, b, c in pair_re.findall(moves):
            named += int(c.replace(",", "")) - int(b.replace(",", ""))
        phase = re.search(r"\*\*(\d)", cells[0]).group(1)
        if named != declared_n:
            hits.append((rel, start + 1,
                         f"§11 Phase {phase} delta cell says +{declared_n} but its named "
                         f"moves sum to {named:+d}"))
        deltas.append((phase, declared_n))
    if total_declared is None:
        hits.append((rel, 0, "§11 total row ('362 → 511 (+149)') not found"))
    else:
        if sum(d for _, d in deltas) != total_declared:
            hits.append((rel, 0, f"§11 phase deltas {[d for _, d in deltas]} do not sum "
                                 f"to the stated total +{total_declared}"))
        if total_range and total_range[1] - total_range[0] != total_declared:
            hits.append((rel, 0, f"§11 total row range {total_range[0]} → {total_range[1]} "
                                 f"implies +{total_range[1] - total_range[0]}, not "
                                 f"+{total_declared}"))
    return hits


def to_register_hits():
    """2026-09-09 thirteenth-wave consistency review — structural guard for the official
    TO's §5.1 sizing summary, §5.2 sub-team tables and §5.3 Enterprise Role Register.
    The v2.0 'official TO of record' commit machine-verified the register foots at
    issuance, but no rule re-derived them: the wave found the register's own
    self-descriptions already drifting (footer claimed '≈150 distinct roles' vs the true
    188 rows / 187 distinct titles; the span note claimed 'the Controller's direct span
    at 7' vs the register's 8 reporting rows; the §5.2 GL & Consolidation mix cell still
    pre-register). Rules: (a) §5.1's 18 numbered department rows must sum to the stated
    current (362) and target (511) columns, with the Total-HQ / store / DC / Total-company
    rows present and cross-footing (6,762 = 362 + 5,800 + 600; 6,911 = 511 + 5,800 + 600);
    (b) each §5.2 sub-team table's HC column must foot to its own declared department
    total, which must be a §5.1 target cell; (c) every §5.3 '#### <Department> (N)' table
    must foot to its own N (the IT table is by-reference and exempt), the 18 declarations
    must pair one-to-one with §5.1's target cells, and the register-total footer line's
    numbers must equal the declarations and sum to 511; (d) the live footer clause's
    quoted 'N rows / M distinct role titles' and the span note's 'N register reporting
    rows' at the Controller must equal the register-derived values."""
    rel = "optimal-table-of-organization.md"
    path = os.path.join(MC, rel)
    hits = []
    text = open(path, encoding="utf-8").read()

    def region(a, b):
        i = text.index(a)
        return text[i:text.index(b, i)]

    # --- (a) §5.1 sizing summary ---
    s51 = region("### 5.1", "### 5.2")
    rows = re.findall(r"^\| \d+ \| (.+?) \| (\d+) \| [^|]* \| \*\*(\d+)\*\* \|", s51, re.M)
    if len(rows) != 18:
        hits.append((rel, 0, f"§5.1 expects 18 numbered department rows, found {len(rows)}"))
    cur = [int(r[1]) for r in rows]
    tgt = [int(r[2]) for r in rows]
    if sum(cur) != 362:
        hits.append((rel, 0, f"§5.1 current column sums to {sum(cur)}, canonical 362"))
    if sum(tgt) != 511:
        hits.append((rel, 0, f"§5.1 target column sums to {sum(tgt)}, canonical 511"))

    def total_row(label):
        m = re.search(rf"^\|\s*\|\s*\*\*{label}\*\*\s*\|\s*\*\*([\d,]+)\*\*\s*\|[^|]*\|\s*\*\*([\d,]+)\*\*\s*\|",
                      s51, re.M)
        if not m:
            hits.append((rel, 0, f"§5.1 '{label}' total row not found"))
            return None
        return (int(m.group(1).replace(",", "")), int(m.group(2).replace(",", "")))

    hq = total_row("Total HQ")
    if hq and hq != (362, 511):
        hits.append((rel, 0, f"§5.1 Total HQ row reads {hq}, canonical (362, 511)"))
    comp = total_row("Total company")
    if comp and comp != (6762, 6911):
        hits.append((rel, 0, f"§5.1 Total company row reads {comp}, canonical (6,762, 6,911)"))
    for label, want in (("Store personnel", 5800), ("DC personnel", 600)):
        m = re.search(rf"^\| \| {label} \| ([\d,]+) \| [^|]* \| \*\*([\d,]+)\*\* \|", s51, re.M)
        if not m or int(m.group(1).replace(",", "")) != want \
                or int(m.group(2).replace(",", "")) != want:
            hits.append((rel, 0, f"§5.1 '{label}' row must read {want} in both states"))
    if hq and comp:
        if comp[0] != hq[0] + 5800 + 600:
            hits.append((rel, 0, "§5.1 current company total ≠ HQ + store + DC rows"))
        if comp[1] != hq[1] + 5800 + 600:
            hits.append((rel, 0, "§5.1 target company total ≠ HQ + store + DC rows"))

    # --- (b) §5.2 sub-team tables (the three HC-column tables) ---
    s52 = region("### 5.2", "### 5.3")
    # a department header may be separated from its table by up to 6 prose/blank
    # lines (the Finance header's own '(3-way match,' parenthetical wraps) — but a
    # following '**bold**' header terminates the search so a header can never
    # adopt the next department's table
    for m in re.finditer(r"\*\*([^*\n]+?) \((\d+)[^)]*\)\*\*[^\n]*\n"
                         r"(?:[^\n*][^\n]*\n|\*[^\n*][^\n]*\n|\n){0,6}?"
                         r"((?:\|[^\n]*\n)+)", s52):
        name, claim, table = m.group(1).strip(), int(m.group(2)), m.group(3)
        vals = []
        for cells in re.findall(r"^\| (?!Sub-team)([^|]*)\|([^|]*)\|", table, re.M):
            hc = cells[1]
            nums = re.findall(r"(\d[\d,]*)\s*→\s*(\d[\d,]*)", hc)
            if nums:
                vals.append(int(nums[0][1].replace(",", "")))
            else:
                mm = re.match(r"\s*(\d[\d,]*)\s*$", hc)
                if mm:
                    vals.append(int(mm.group(1).replace(",", "")))
        if not vals:
            continue  # bold header followed by prose, not a sub-team table
        s = sum(vals)
        if s != claim:
            hits.append((rel, 0, f"§5.2 {name} sub-team table sums to {s}, declared {claim}"))
        if claim not in tgt:
            hits.append((rel, 0, f"§5.2 {name} declared total {claim} is not a §5.1 target cell"))

    # --- (c) §5.3 Enterprise Role Register ---
    s53 = region("### 5.3", "## 6.")
    secs = re.findall(r"^#### (.+?) \((\d+)[^)]*\)\n(.*?)(?=^#### |\Z)", s53, re.M | re.S)
    if len(secs) != 18:
        hits.append((rel, 0, f"§5.3 expects 18 department tables, found {len(secs)}"))
    declared = []
    all_titles = []
    ctrl_rows = 0
    for name, claim, body in secs:
        n = int(claim)
        declared.append((name.strip(), n))
        if "by reference" in name or "by reference" in body[:200]:
            continue  # IT: carried by the IT operating model (single-source rule)
        rws = re.findall(r"^\| ([^*\n][^|]*?) \| (\d+) \| ([^|]*) \|", body, re.M)
        all_titles.extend(t.strip() for t, _, _ in rws)
        s = sum(int(h) for _, h, _ in rws)
        if s != n:
            hits.append((rel, 0, f"§5.3 {name} table foots to {s}, declared {n}"))
        for _, _, rt in rws:
            if rt.strip() == "Controller":
                ctrl_rows += 1
    if len(rows) == len(secs) == 18:
        for (n51, _c, t), (n53name, d) in zip(rows, declared):
            w51 = re.sub(r"[^A-Za-z].*", "", n51).lower()
            w53 = re.sub(r"[^A-Za-z].*", "", n53name).lower()
            if w51 != w53 or int(t) != d:
                hits.append((rel, 0, f"§5.3 '{n53name}' ({d}) does not pair with "
                                     f"§5.1 '{n51}' ({t})"))
    m = re.search(r"Register total:(.*?)= \*\*(\d+)\*\*", text, re.S)
    if not m:
        hits.append((rel, 0, "register-total footer line not found"))
    else:
        nums = [int(x) for x in re.findall(r"\d+", m.group(1))]
        if nums != [d for _, d in declared]:
            hits.append((rel, 0, "register-total footer line does not match the "
                                 "§5.3 department declarations"))
        if sum(nums) != int(m.group(2)):
            hits.append((rel, 0, f"register-total footer sums to {sum(nums)}, "
                                 f"claims {m.group(2)}"))

    # --- (d) quoted self-description figures vs the register ---
    foot_i = text.index("*Document Version:")
    live = text[foot_i:text.index(" Prior ", foot_i)]
    norm = re.compile(r"\s+")
    distinct = {norm.sub(" ", re.sub(r"\(.*?\)", "", t)).strip().lower() for t in all_titles}
    mm = re.search(r"(\d+) rows / (\d+) distinct role titles", live)
    if not mm:
        hits.append((rel, 0, "live footer clause must quote 'N rows / M distinct role titles'"))
    else:
        if int(mm.group(1)) != len(all_titles):
            hits.append((rel, 0, f"live footer claims {mm.group(1)} register rows, "
                                 f"register holds {len(all_titles)}"))
        if int(mm.group(2)) != len(distinct):
            hits.append((rel, 0, f"live footer claims {mm.group(2)} distinct role titles, "
                                 f"register holds {len(distinct)}"))
    mm = re.search(r"(\d+) register reporting rows", s53)
    if not mm:
        hits.append((rel, 0, "§5.3 span note must quote its 'N register reporting rows' "
                             "at the Controller"))
    elif int(mm.group(1)) != ctrl_rows:
        hits.append((rel, 0, f"span note claims {mm.group(1)} Controller reporting rows, "
                             f"register holds {ctrl_rows}"))
    return hits


def methodology_index_hits():
    """2026-09-03 index-trueness pass — the description surfaces outside the 7 guarded
    docs can go stale in exactly two ways, both found live in 07-methodology/README.md:
    a '(vN.M' version pin left behind by a doc bump (OM row said v2.1 after v2.2
    shipped), and a description of this guard's TO anchors quoting the superseded
    two-state pair (469/6,869 after the 511/6,911 re-base). Rule: every '(vN.M' pin on a
    row naming one of the versioned methodology docs must equal that doc's own
    '*Document Version:' footer, and the retired pair must not reappear."""
    rel = "README.md"
    hits = []
    index_path = os.path.join(REPO, "07-methodology", rel)
    versioned = {"it-product-operating-model.md",
                 "capability-sourcing-and-engineering-model.md",
                 "technical-guidelines.md",
                 "ai-first-operating-guide.md"}
    current = {}
    for name in versioned:
        m = re.search(r"^\*Document Version: (\d+\.\d+)",
                      open(os.path.join(REPO, "07-methodology", name),
                           encoding="utf-8").read(), re.M)
        if m:
            current[name] = m.group(1)
    for ln, l in enumerate(open(index_path, encoding="utf-8").read().splitlines(), 1):
        if "469/6,869" in l:
            hits.append((rel, ln, 'retired TO-anchor pair "469/6,869" (the guard\'s '
                         'two-state anchors are 362/6,762 → 511/6,911)'))
        for name, ver in current.items():
            if name not in l:
                continue
            for m in re.finditer(r"\(v(\d+\.\d+)", l):
                if m.group(1) != ver:
                    hits.append((rel, ln, f"{name} pinned at v{m.group(1)} but the doc "
                                          f"footer says v{ver}"))
    return hits


def guide_figure_hits():
    """2026-09-04 guard-extension pass — structural guard for the AI-first operating
    guide's canonical-figure citations: the process-catalog triple (both its prose and
    compressed forms), the Tier-wired autonomy-ladder sentence, and the control- and
    requirement-register canon-table counts are re-derived from the primary registers
    on every run. (The guide shipped v1.0 outside this guard's doc set — the
    sourcing-model precedent: the quantitative claim quoted outside the guard is the
    one that drifts. Checks 40/41 already guard its check-count and the 'across N
    categories' requirement-total forms repo-wide; this rule covers the forms they
    cannot see.)"""
    rel = "ai-first-operating-guide.md"
    hits = []
    wf_dir = os.path.join(MC, "workflows")
    n_vs = sum(1 for n in os.listdir(wf_dir)
               if n.startswith("VS-") and os.path.isdir(os.path.join(wf_dir, n)))
    n_pa = len(glob.glob(os.path.join(wf_dir, "VS-*", "PA-*.md")))
    idx = open(os.path.join(wf_dir, "value-stream-index.md"), encoding="utf-8").read()
    m = re.search(r"\*\*Grand Total\*\* \| \*\*[\d,]+\*\* \| \*\*([\d,]+)\*\*", idx)
    if not m:
        return [(rel, 0, "value-stream-index Grand Total row not parseable")]
    n_wf = int(m.group(1).replace(",", ""))
    reg = open(os.path.join(wf_dir, "workflow-criticality-classification.md"),
               encoding="utf-8").read()
    tiers = {}
    confirmed = re.search(r"### Confirmed classification.*?(?=^### |^## )", reg,
                          re.M | re.S)
    if confirmed:
        for mm in re.finditer(r"^\| Phase (\d) \| [^|]+ \| ([\d,]+) \|",
                              confirmed.group(0), re.M):
            tiers[f"Tier {mm.group(1)}"] = int(mm.group(2).replace(",", ""))
    if len(tiers) != 3:
        return [(rel, 0, "criticality register Summary table not parseable — "
                         "cannot derive canon tier counts")]
    n_rows = sum(tiers.values())
    reqs = open(os.path.join(MC, "erp-requirements.md"), encoding="utf-8").read()
    n_req = len(set(re.findall(r"^\| ([A-Z]{2,5}-\d+[a-z]?) \|", reqs, re.M)))
    n_cats = len({pid.split("-")[0] for pid in
                  re.findall(r"^\| ([A-Z]{2,5}-\d+[a-z]?) \|", reqs, re.M)})
    ctl = open(os.path.join(MC, "internal-controls-matrix.md"), encoding="utf-8").read()
    n_ctl = len(set(re.findall(r"CTL-\d+", ctl)))
    body = strip_footer(open(os.path.normpath(os.path.join(MC, "..", "07-methodology",
                                                           rel)),
                             encoding="utf-8").read())

    def qint(s):
        return int(s.replace(",", ""))

    def line_of(pos):
        return body[:pos].count("\n") + 1

    # (a) prose catalog triple — 'the process catalog (188 value streams, 569
    # process areas, 5,388 workflows)'
    for mm in re.finditer(r"(\d[\d,]*) value streams, (\d[\d,]*) process areas,"
                          r" (\d[\d,]*) workflows", body):
        got = (qint(mm.group(1)), qint(mm.group(2)), qint(mm.group(3)))
        if got != (n_vs, n_pa, n_wf):
            hits.append((rel, line_of(mm.start()),
                         f"catalog triple {got} != disk canon ({n_vs}, {n_pa}, {n_wf})"))
    # (b) compressed catalog triple — '188 VS / 569 PA / 5,388 W'
    for mm in re.finditer(r"(\d[\d,]*) VS / (\d[\d,]*) PA / (\d[\d,]*) W\b", body):
        got = (qint(mm.group(1)), qint(mm.group(2)), qint(mm.group(3)))
        if got != (n_vs, n_pa, n_wf):
            hits.append((rel, line_of(mm.start()),
                         f"catalog triple {got} != disk canon ({n_vs}, {n_pa}, {n_wf})"))
    # (c) the Tier-wired autonomy-ladder sentence
    lad = re.search(r"Tier 1 = (\d[\d,]*) register rows, Tier 2 =\s*(\d[\d,]*),"
                    r" Tier 3 = (\d[\d,]*) of (\d[\d,]*) rows over"
                    r" (\d[\d,]*) unique workflows", body)
    if not lad:
        hits.append((rel, 0, "autonomy-ladder citation sentence not found (expected "
                             "'Tier 1 = … register rows, Tier 2 = …, Tier 3 = … of … rows "
                             "over … unique workflows')"))
    else:
        got = [qint(lad.group(i)) for i in (1, 2, 3, 4, 5)]
        want = [tiers["Tier 1"], tiers["Tier 2"], tiers["Tier 3"], n_rows, n_wf]
        if got != want:
            hits.append((rel, line_of(lad.start()),
                         f"autonomy ladder {got} != register canon {want}"))
    # (d) control-register citations
    for mm in re.finditer(r"control register \((\d[\d,]*) controls\)", body):
        if qint(mm.group(1)) != n_ctl:
            hits.append((rel, line_of(mm.start()),
                         f"control-register count {mm.group(1)} != matrix canon {n_ctl}"))
    for mm in re.finditer(r"(\d[\d,]*)-control", body):
        if qint(mm.group(1)) != n_ctl:
            hits.append((rel, line_of(mm.start()),
                         f"control-register count '{mm.group(0)}' != matrix canon {n_ctl}"))
    for mm in re.finditer(r"`internal-controls-matrix\.md` \((\d[\d,]*)\)", body):
        if qint(mm.group(1)) != n_ctl:
            hits.append((rel, line_of(mm.start()),
                         f"canon-table control count {mm.group(1)} != matrix canon {n_ctl}"))
    # (e) requirement-register citations (the 'in 38 categories' and '728 / 38'
    # forms Check 41's 'across' forms cannot see)
    for mm in re.finditer(r"(\d[\d,]*) requirements in (\d+) categories", body):
        got = (qint(mm.group(1)), int(mm.group(2)))
        if got != (n_req, n_cats):
            hits.append((rel, line_of(mm.start()),
                         f"requirement-total claim {got} != register canon "
                         f"({n_req}, {n_cats})"))
    for mm in re.finditer(r"`erp-requirements\.md` \((\d[\d,]*) / (\d+) categories\)",
                          body):
        got = (qint(mm.group(1)), int(mm.group(2)))
        if got != (n_req, n_cats):
            hits.append((rel, line_of(mm.start()),
                         f"canon-table requirement claim {got} != register canon "
                         f"({n_req}, {n_cats})"))
    return hits


def register_heading_hits():
    """2026-09-03 consistency review pass — structural guard for the criticality
    register's own section-heading counts. Every '(n Workflows)' parenthetical is
    re-derived from the data rows beneath it (nested sub-heading rows roll up):
    family/Additions/history-pass/####-tier headings hold their subtree rows; the
    three '## Tier N' headings (checked at end-of-file) must equal the effective
    per-tier total — original + Additions + history-pass '#### Tier N' blocks — and
    that total must also equal the ## Summary table's per-phase counts (the canon
    source that sourcing_tier_hits re-derives from — with this rule the
    rows -> headings -> Summary chain is closed end-to-end). The pass found
    '### Tier 2 Additions (495 Workflows)' holding 501 rows after the two 2026-09-03
    gap-fill passes appended six rows without bumping the parenthetical — exactly the
    straggler class that survived because the Summary table was trued while the
    intermediate heading was not."""
    rel = "workflow-criticality-classification.md"
    hits = []
    lines = open(os.path.join(MC, "workflows", rel), encoding="utf-8").read().splitlines()
    tier_rows = {1: 0, 2: 0, 3: 0}
    tier_heading_claim = {}
    summary_claim = {}
    cur = None                      # effective tier attribution context
    stack = []                      # [level, text, line_no, rows]

    def close_top():
        level, text, ln, rows = stack.pop()
        if re.match(r"^Tier \d:", text):
            return                  # '## Tier N' totals checked at end-of-file
        m = re.search(r"\(([\d,]+)\s*[Ww]orkflows?\)", text)
        if m and int(m.group(1).replace(",", "")) != rows:
            hits.append((rel, ln, f"heading '{text[:70]}' claims ({m.group(1)}) "
                                  f"but holds {rows} row(s)"))
        if stack:
            stack[-1][3] += rows    # roll up into the enclosing heading

    for ln, l in enumerate(lines, 1):
        m = re.match(r"^(#{1,4}) (.*)", l)
        if m:
            level = len(m.group(1))
            text = m.group(2)
            while stack and stack[-1][0] >= level:
                close_top()
            tm = re.match(r"^Tier (\d):", text)
            am = re.match(r"^Tier (\d) Additions", text)
            t4 = re.match(r"^Tier (\d)", text)
            if tm:
                cur = int(tm.group(1))
                tier_heading_claim[int(tm.group(1))] = (text, ln)
            elif am:
                cur = int(am.group(1))
            elif level == 4 and t4:
                cur = int(t4.group(1))
            elif level <= 2:
                cur = None
            stack.append([level, text, ln, 0])
            continue
        sm = re.match(r"^\| Phase (\d) \|[^|]+\|\s*([\d,]+)\s*\|", l)
        if sm and stack and stack[-1][1].startswith("Confirmed classification"):
            summary_claim[int(sm.group(1))] = int(sm.group(2).replace(",", ""))
            continue
        if re.match(r"^\| (W\d+[A-Z]?) \| ", l):
            if stack:
                stack[-1][3] += 1
            if cur:
                tier_rows[cur] += 1
    while stack:
        close_top()

    for n in (1, 2, 3):
        claim = tier_heading_claim.get(n)
        if claim is None:
            hits.append((rel, 0, f"## Tier {n} heading not found"))
            continue
        text, ln = claim
        m = re.search(r"\(([\d,]+)\s*[Ww]orkflows?\)", text)
        declared = int(m.group(1).replace(",", "")) if m else None
        if declared != tier_rows[n]:
            hits.append((rel, ln, f"## Tier {n} heading claims ({declared}) but the "
                                  f"register holds {tier_rows[n]} Tier-{n} row(s)"))
        want = summary_claim.get(n)
        if want is not None and want != tier_rows[n]:
            hits.append((rel, ln, f"## Summary Phase {n} count {want} != the register's "
                                  f"{tier_rows[n]} Tier-{n} row(s)"))
    return hits


def om_reconciliation_hits():
    """2026-09-05 sixth-wave consistency review — structural guard for the IT operating
    model's reconciliation surfaces, all found stale in the same pass: the batch re-point
    cascades trued §4.9's per-team rows and the version footer every pass but never the
    §3.2 portfolio table (stranded at the batch-18 state, total 5,406, for four passes),
    the batch-23 pass missed the §4.9 Total row while updating the footer beside it, and
    the v3.7 clause's split arithmetic put INFRA's +2 on the wrong side. No presence
    anchor can guard a Total row whose stale literal survives in the Prior-v footer
    history (the old ANCHOR was satisfying itself off exactly that), so the §3.2 Total
    row, the §4.9 Total row, and the LIVE (first/newest) footer 'making the
    reconciliation read **171 + 17 = 188 / X + Y = Z**' clause are re-derived here from
    the value-stream-index Grand Total on every run."""
    rel = "it-product-operating-model.md"
    hits = []
    idx = open(os.path.join(MC, "workflows", "value-stream-index.md"),
               encoding="utf-8").read()
    m = re.search(r"\*\*Grand Total\*\* \| \*\*[\d,]+\*\* \| \*\*([\d,]+)\*\*", idx)
    if not m:
        return [(rel, 0, "value-stream-index Grand Total row not parseable")]
    total = int(m.group(1).replace(",", ""))
    om = open(os.path.join(REPO, "07-methodology", rel), encoding="utf-8").read()
    # §3.2 portfolio table: Domain / Platform+CIO subtotal rows must cross-foot to the
    # Total row (both the VS split and the workflow split), and the Total row must equal
    # the canonical grand total
    sub = {}
    for pat, label in [
        (r"\|\s*\*\*Domain subtotal\*\*\s*\|\s*\|\s*\|\s*\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*([\d,]+)\*\*",
         "Domain"),
        (r"\|\s*\*\*Platform \+ CIO subtotal\*\*\s*\|\s*\|\s*\|\s*\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*([\d,]+)\*\*",
         "Platform + CIO"),
    ]:
        mm = re.search(pat, om)
        if not mm:
            hits.append((rel, 0, f"§3.2 {label} subtotal row not parseable"))
        else:
            sub[label] = (int(mm.group(1)), int(mm.group(2).replace(",", "")))
    mtot = re.search(r"\|\s*\*\*Total\*\*\s*\|\s*\|\s*\|\s*\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*([\d,]+)\*\*", om)
    if not mtot:
        hits.append((rel, 0, "§3.2 Total row not parseable"))
    else:
        vs_n, wf_n = int(mtot.group(1)), int(mtot.group(2).replace(",", ""))
        if wf_n != total:
            hits.append((rel, om[:mtot.start()].count("\n") + 1,
                         f"§3.2 Total row says {wf_n:,} workflows but the canonical total is {total:,}"))
        if len(sub) == 2:
            (d_vs, d_wf), (p_vs, p_wf) = sub["Domain"], sub["Platform + CIO"]
            if d_vs + p_vs != vs_n:
                hits.append((rel, om[:mtot.start()].count("\n") + 1,
                             f"§3.2 subtotal VS cells {d_vs} + {p_vs} != Total row {vs_n}"))
            if d_wf + p_wf != wf_n:
                hits.append((rel, om[:mtot.start()].count("\n") + 1,
                             f"§3.2 subtotal WF cells {d_wf:,} + {p_wf:,} != Total row {wf_n:,}"))
    # §4.9 mapping-reconciliation Total row
    m49 = re.search(r"\|\s*\*\*Total\*\*\s*\|\s*\*\*171 \+ 17 = 188\*\*\s*\|\s*\*\*([\d,]+) \+ ([\d,]+) = ([\d,]+)\*\*",
                    om)
    if not m49:
        hits.append((rel, 0, "§4.9 Total row not parseable"))
    else:
        x, y, z = (int(m49.group(i).replace(",", "")) for i in (1, 2, 3))
        if x + y != z or z != total:
            hits.append((rel, om[:m49.start()].count("\n") + 1,
                         f"§4.9 Total row declares {x:,} + {y:,} = {z:,} but the canonical total is {total:,}"))
    # live footer clause = the FIRST 'making the reconciliation read' occurrence
    # (the version footer is a newest-first Prior-v chain on a single line)
    mft = re.search(r"making the reconciliation read \*\*171 \+ 17 = 188 / ([\d,]+) \+ ([\d,]+) = ([\d,]+)\*\*",
                    om)
    if not mft:
        hits.append((rel, 0, "live footer reconciliation clause not found"))
    else:
        x, y, z = (int(mft.group(i).replace(",", "")) for i in (1, 2, 3))
        if x + y != z or z != total:
            hits.append((rel, om[:mft.start()].count("\n") + 1,
                         f"live footer reconciliation declares {x:,} + {y:,} = {z:,} but the canonical total is {total:,}"))
    # 2026-09-07 tenth-wave extension — re-derive the per-team workload cells, not
    # just their cross-foots. The sixth wave adjudicated the VS-151 residual (SSP 906
    # / DP 189, subtotals 4,937 + 489) and found the mismatch as old as the document:
    # twenty reconciliation passes trued the deltas correctly without ever re-deriving
    # the base, because the cross-foot checks here see only declared-vs-declared sums.
    # Derive team → VS from the §4.1–4.8 mapping tables, count each VS's `## W`
    # headers on disk, and assert §3.2's per-team rows and subtotals and §4.9's
    # per-team workflow cells against the derivation.
    team_vs = {}
    for ln, l in enumerate(om.splitlines(), 1):
        mr = re.match(r"^\| \[VS-(\d+)\]\([^)]*\) \| [^|]+ \| ([A-Za-z]+(?: Office)?) \|", l)
        if mr:
            team_vs.setdefault(mr.group(2).replace(" Office", ""), []).append(int(mr.group(1)))
    if sum(len(v) for v in team_vs.values()) != 188:
        hits.append((rel, 0, f"§4 mapping rows parse to "
                             f"{sum(len(v) for v in team_vs.values())} VSs across "
                             f"{len(team_vs)} teams — expected 188; mapping-table structure changed?"))
    else:
        disk = {}
        for d in os.listdir(os.path.join(MC, "workflows")):
            md = re.match(r"^VS-(\d+)-", d)
            if not md:
                continue
            n = 0
            for f in os.listdir(os.path.join(MC, "workflows", d)):
                if f.startswith("PA-") and f.endswith(".md"):
                    n += len(set(re.findall(r"^## (W\d+[A-Z]?)\.",
                        open(os.path.join(MC, "workflows", d, f), encoding="utf-8").read(), re.M)))
            disk[int(md.group(1))] = n
        wf = {t: sum(disk[v] for v in vs) for t, vs in team_vs.items()}
        # §3.2 per-team rows (CIO's row carries an empty leading cell); IAP/SEP/AAP
        # have no §4 mapping rows — legitimate only while they declare 0 VS / 0 WF.
        # Scoped to the §3.2 section — the §9.1 sizing table's | CODE | 1 | 1 | ...
        # rows share the leading-cell shape.
        m32s = re.search(r"### 3\.2 .*?(?=\n### 3\.3|\n## 4\.)", om, re.S)
        sec32 = m32s.group(0) if m32s else ""
        off32 = om[:m32s.start()].count("\n") + 1 if m32s else 1
        for ln, l in enumerate(sec32.splitlines(), off32):
            m32 = re.match(r"^\| (?:\d+)? \| [^|]+? \| ([A-Za-z]{2,5}) \|[^|]*\|[^|]*\| (\d+) \| ([\d,]+) \|", l)
            if not m32 or m32.group(1) in ("Total", "Domain", "Platform"):
                continue
            code, mvs, mwf = m32.group(1), int(m32.group(2)), int(m32.group(3).replace(",", ""))
            avs = len(team_vs.get(code, []))
            awf = wf.get(code, 0)
            if avs == 0 and awf == 0 and mvs == 0 and mwf == 0:
                continue
            if mvs != avs or mwf != awf:
                hits.append((rel, ln, f"§3.2 {code} row declares {mvs} VS / {mwf:,} workflows "
                                      f"but the §4 mapping + disk hold {avs} VS / {awf:,}"))
        # §3.2 subtotal cells must equal their member-row sums (domain = the 9
        # stream-aligned/enabling rows before the subtotal; platform = the rest)
        declared32 = {}
        for ln, l in enumerate(om.splitlines(), 1):
            ms = re.match(r"^\| \| \*\*(Domain subtotal|Platform \+ CIO subtotal)\*\* \| \| \| \| \| \*\*(\d+)\*\* \| \*\*([\d,]+)\*\*", l)
            if ms:
                declared32[ms.group(1)] = (int(ms.group(2)), int(ms.group(3).replace(",", "")), ln)
        dom = ["MSC", "WLI", "SSP", "CCP", "FIN", "CORP", "PEO", "OMO", "TPS"]
        if len(declared32) == 2:
            d_vs = sum(len(team_vs[t]) for t in dom if t in team_vs)
            d_wf = sum(wf.get(t, 0) for t in dom)
            p_vs = sum(len(v) for t, v in team_vs.items() if t not in dom)
            p_wf = sum(wf.get(t, 0) for t, v in team_vs.items() if t not in dom)
            if declared32["Domain subtotal"][0] != d_vs or declared32["Domain subtotal"][1] != d_wf:
                hits.append((rel, declared32["Domain subtotal"][2],
                             f"§3.2 Domain subtotal declares {declared32['Domain subtotal'][0]} VS / "
                             f"{declared32['Domain subtotal'][1]:,} workflows but its member rows derive "
                             f"{d_vs} VS / {d_wf:,}"))
            if declared32["Platform + CIO subtotal"][0] != p_vs or declared32["Platform + CIO subtotal"][1] != p_wf:
                hits.append((rel, declared32["Platform + CIO subtotal"][2],
                             f"§3.2 Platform+CIO subtotal declares {declared32['Platform + CIO subtotal'][0]} VS / "
                             f"{declared32['Platform + CIO subtotal'][1]:,} workflows but its member rows derive "
                             f"{p_vs} VS / {p_wf:,}"))
        # §4.9 per-team workflow cells: | CODE | VS enumeration | Workflows |
        m49s = re.search(r"### 4\.9 .*?(?=\n## 5\.|\n---)", om, re.S)
        sec49 = m49s.group(0) if m49s else ""
        off49 = om[:m49s.start()].count("\n") + 1 if m49s else 1
        for ln, l in enumerate(sec49.splitlines(), off49):
            m49r = re.match(r"^\| ([A-Za-z]{2,5}(?: Office)?) \| [^|]+ \| ([\d,]+) \|", l)
            if not m49r or m49r.group(1) == "Total":
                continue
            code = m49r.group(1).replace(" Office", "")
            if code not in team_vs:
                continue
            awf = wf[code]
            mwf49 = int(m49r.group(2).replace(",", ""))
            if mwf49 != awf:
                hits.append((rel, ln, f"§4.9 {m49r.group(1)} row declares {mwf49:,} workflows "
                                      f"but its mapped VSs hold {awf:,} on disk"))
    return hits


def dv_volume_hits():
    """2026-09-07 eighth-wave consistency review — structural guard for the
    data-volumes doc's volume arithmetic (the doc joined DOCS this pass after shipping
    with zero validator coverage — the sourcing-model/ai-guide precedent). (a) Every
    §1.1 row that states a peak-daily figure must declare its peak factor, and each
    numeric peak endpoint must equal daily × factor within 5% rounding tolerance (the
    review found the Customer-Registrations row carrying a bare '—' factor beside a
    ~450 peak — the implied 3.0x sale-event factor is now stated). (b) The §1.2 size
    column must sum to the stated annual increment, and the retention row to ~10× it."""
    rel = "data-volumes-and-integrations.md"
    hits = []
    text = open(os.path.join(MC, rel), encoding="utf-8").read()
    m11 = re.search(r"### 1\.1 .*?(?=### 1\.2)", text, re.S)
    m12 = re.search(r"### 1\.2 .*?(?=\n## )", text, re.S)
    if not m11 or not m12:
        return [(rel, 0, "§1.1/§1.2 volume tables not found")]

    def num(s):
        return float(s.replace("~", "").replace(",", "").strip())

    for ln, l in enumerate(m11.group(0).splitlines(),
                           text[:m11.start()].count("\n") + 1):
        if not l.strip().startswith("|"):
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cells) != 4 or not re.search(r"\d", cells[3]):
            continue
        name, daily, factor, peak = cells
        fm = re.match(r"~?(\d+(?:\.\d+)?)x", factor)
        if not fm:
            hits.append((rel, ln, f"§1.1 row '{name}' states a peak-daily figure "
                                  f"('{peak}') with no peak factor (cell '{factor}')"))
            continue
        f = float(fm.group(1))
        d_parts = [num(x) for x in re.split(r"[–-]", daily) if re.search(r"\d", x)]
        p_parts = [num(x) for x in re.split(r"[–-]", peak) if re.search(r"\d", x)]
        for d, p in zip(d_parts, p_parts):
            if abs(d * f - p) > max(1.0, 0.05 * p):
                hits.append((rel, ln, f"§1.1 row '{name}': peak {p:g} != daily {d:g} × "
                                      f"factor {f:g} (= {d * f:g})"))

    sizes, total_declared, retention_declared = [], None, None
    for l in m12.group(0).splitlines():
        if not l.strip().startswith("|"):
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        mm = re.search(r"([\d,]+(?:\.\d+)?)\s*GB", cells[2])
        if not mm:
            continue
        if cells[0].startswith("**Total Annual Increment**"):
            total_declared = float(mm.group(1).replace(",", ""))
        elif cells[0].startswith("**10-Year Retention**"):
            retention_declared = float(mm.group(1).replace(",", ""))
        else:
            sizes.append(float(mm.group(1).replace(",", "")))
    if not sizes or total_declared is None:
        hits.append((rel, 0, "§1.2 storage size rows / total row not parseable"))
    else:
        ssum = sum(sizes)
        if abs(ssum - total_declared) > max(2.0, 0.05 * total_declared):
            hits.append((rel, 0, f"§1.2 size column sums to {ssum:g} GB but the total "
                                 f"row says ~{total_declared:g} GB"))
        if retention_declared is not None and \
                abs(retention_declared - 10 * total_declared) > 0.05 * 10 * total_declared:
            hits.append((rel, 0, f"§1.2 retention row ~{retention_declared:g} GB != "
                                 f"10 × the ~{total_declared:g} GB annual increment"))
    return hits


def exec_tree_hits():
    """2026-09-07 eighth-wave consistency review — the executive summary's
    'Repository Structure' mini-tree must name exactly the top-level directories that
    exist on disk. (The two-row tree predated the generated bpmn/ and dmn/ trees,
    which shipped 2026-09-05 as first-class artifacts; the summary is the C-suite's
    map of the repo, so a missing top-level directory is exactly the sibling-surface
    drift class the batch re-point cascades keep repairing.)"""
    rel = "executive-summary.md"
    hits = []
    text = open(os.path.join(MC, rel), encoding="utf-8").read()
    m = re.search(r"## Repository Structure\s*```(.*?)```", text, re.S)
    if not m:
        return [(rel, 0, "Repository Structure block not found")]
    listed = set(re.findall(r"(?:├──|└──)\s*([A-Za-z0-9._-]+)/", m.group(1)))
    on_disk = {n for n in os.listdir(REPO)
               if os.path.isdir(os.path.join(REPO, n)) and not n.startswith(".")}
    if listed != on_disk:
        hits.append((rel, text[:m.start()].count("\n") + 1,
                     f"Repository Structure tree lists {sorted(listed)} but the repo "
                     f"top level holds {sorted(on_disk)}"))
    return hits


def companion_pin_hits():
    """2026-09-07 ninth-wave consistency review — the reverse-direction companion
    pins, the mirror images of the surfaces live_pin_hits already guards, which no
    rule read: (a) the sourcing model's header 'Companion to' pin, (b) its §13
    Related-Documents OM-row pin, (c) its footer's newest 'companion OM pin moves
    to' clause (the live end of the version-history chain — Prior clauses stand as
    written), and (d) the OM's own §13 doc-map self-pin 'this vN.M model'. All four
    must equal the pinned doc's current '*Document Version:' footer. Found live:
    the header pin stranded at v3.3 since batch-19 (the batch-20 cascade's
    'header/§13 OM pins re-pointed' claim re-pointed only the §13 row), the §13 row
    frozen at v3.4, the footer chain broken by the sixth-wave OM v3.8 bump (sourcing
    stayed at v2.7), and the OM self-pin still at the v2.4 of the 2026-09-03 pin
    pass through six subsequent OM bumps."""
    hits = []
    versions = _doc_versions()
    om_v = versions.get("it-product-operating-model.md")
    src_v = versions.get("capability-sourcing-and-engineering-model.md")
    om = open(os.path.join(REPO, "07-methodology",
                           "it-product-operating-model.md"), encoding="utf-8").read()
    src = open(os.path.join(REPO, "07-methodology",
                            "capability-sourcing-and-engineering-model.md"),
               encoding="utf-8").read()
    if om_v is None or src_v is None:
        return [("audit-model-docs", 0, "companion_pin_hits: unparseable doc footer")]
    # (a) sourcing header companion pin
    m = re.search(r"Companion to \[`it-product-operating-model\.md`\]\(it-product-"
                  r"operating-model\.md\) \(v(\d+\.\d+)\)", src)
    if not m:
        hits.append(("capability-sourcing-and-engineering-model.md", 0,
                     "header 'Companion to' OM pin not found"))
    elif m.group(1) != om_v:
        hits.append(("capability-sourcing-and-engineering-model.md",
                     src[:m.start()].count("\n") + 1,
                     f"header companion pin v{m.group(1)} but the OM footer says "
                     f"v{om_v}"))
    # (b) sourcing §13 Related-Documents OM-row pin
    for ln, l in enumerate(src.splitlines(), 1):
        if "it-product-operating-model.md" in l and "reshapes (v" in l:
            m = re.search(r"reshapes \(v(\d+\.\d+)", l)
            if not m:
                hits.append(("capability-sourcing-and-engineering-model.md", ln,
                             "§13 OM row carries no version pin"))
            elif m.group(1) != om_v:
                hits.append(("capability-sourcing-and-engineering-model.md", ln,
                             f"§13 OM-row pin v{m.group(1)} but the OM footer says "
                             f"v{om_v}"))
            break
    else:
        hits.append(("capability-sourcing-and-engineering-model.md", 0,
                     "§13 Related-Documents OM row not found"))
    # (c) sourcing footer: the NEWEST (first) 'companion OM pin moves to' clause
    m = re.search(r"companion OM pin moves to v(\d+\.\d+)", src)
    if not m:
        hits.append(("capability-sourcing-and-engineering-model.md", 0,
                     "footer 'companion OM pin moves to' clause not found"))
    elif m.group(1) != om_v:
        hits.append(("capability-sourcing-and-engineering-model.md",
                     src[:m.start()].count("\n") + 1,
                     f"newest footer OM-pin clause says v{m.group(1)} but the OM "
                     f"footer says v{om_v} (the companion-pin chain is broken — "
                     f"bump this model with a clause re-pointing it)"))
    # (d) OM §13 doc-map self-pin 'this vN.M model'
    for ln, l in enumerate(om.splitlines(), 1):
        if "capability-sourcing-and-engineering-model.md" in l and "this v" in l \
                and "model is built on" in l:
            m = re.search(r"this v(\d+\.\d+) model", l)
            if not m:
                hits.append(("it-product-operating-model.md", ln,
                             "§13 sourcing row self-pin unparsable"))
            elif m.group(1) != om_v:
                hits.append(("it-product-operating-model.md", ln,
                             f"§13 self-pin 'this v{m.group(1)} model' but the OM "
                             f"footer says v{om_v}"))
            break
    else:
        hits.append(("it-product-operating-model.md", 0,
                     "§13 sourcing doc-map row not found"))
    # (e) OM header 'Companion to' sourcing-model pin — the mirror of (a), added
    # by the 2026-09-14 twenty-ninth-wave review after the same-day promotion
    # bumped the sourcing model to v3.2 and stranded the OM header pin at v3.1
    # (the ninth-wave rule pinned the sourcing→OM direction only). The OM header
    # wraps 'companion' and the link across lines, so the match anchors on the
    # link-followed-by-(vN.M) form — unique to the header (the §13 row and the
    # footer cite the model without the ](…) (vN.M) shape)
    m = re.search(r"\[`capability-sourcing-and-engineering-model\.md`\]"
                  r"\(capability-sourcing-and-engineering-model\.md\) \(v(\d+\.\d+)\)", om)
    if not m:
        hits.append(("it-product-operating-model.md", 0,
                     "header 'Companion to' sourcing-model pin not found"))
    elif m.group(1) != src_v:
        hits.append(("it-product-operating-model.md",
                     om[:m.start()].count("\n") + 1,
                     f"header companion pin v{m.group(1)} but the sourcing-model "
                     f"footer says v{src_v}"))
    return hits


def reality_check_hits():
    """2026-09-07 eighth-wave consistency review — in-place arithmetic repair guard
    for the headcount reality-check §3.1 AP workload bullet: it carried '(~450/day)'
    beside the canonical '~8,500–9,500/month' — 450/day implies ~13,500/month and
    matches no licensed convention (the corpus-wide 30-operating-day convention gives
    ~300/day, the data-volumes v4.3+ / profile §15.1 reconciliation the repair
    followed). The corrected parenthetical is required present; the retired one must
    not reappear."""
    rel = "headcount-reality-check.md"
    hits = []
    text = open(os.path.join(MC, rel), encoding="utf-8").read()
    if "(~450/day)" in text:
        hits.append((rel, text[:text.find("(~450/day)")].count("\n") + 1,
                     'retired AP parenthetical "(~450/day)" (canonical midpoint is '
                     "~300/day at the 30-operating-days/month convention)"))
    anchor = "- **~8,500–9,500 AP invoices/month** (~300/day) — VS-17 / PA-17"
    if anchor not in text:
        hits.append((rel, 0, f'required corrected AP anchor missing: "{anchor}"'))
    return hits


def profile_derived_figure_hits():
    """2026-09-09 sixteenth-wave consistency review — derived-figure guard for the
    model-company profile's quotient/count claims and every live citation of them.
    Re-derives, from the profile's own canonical rows every run:
      * the revenue-per-employee quotient (§9.4 Annual Gross Revenue ÷ §4 Total
        Company Headcount) — the §4 note must quote the live division and the live
        2-dp quotient, and every live 'revenue per employee ~PHP N.NM' citation in
        the corpus must equal the derivation (found live: 9.22M stranded at the
        retired 6,757 denominator on the profile §4 note, assumptions A2.6 and
        PA-133.3's Volume row while the division read ÷ 6,762);
      * the B2B account counts (§9.2 trade/corporate) — the §10.3 AR row must
        cross-foot to them and the §15.2 Master-Data rows must equal them (found
        live: §15.2 trade stranded at the retired 5,000), and the retired
        '5,000-account' trade scheme must not reappear in live prose.
    Sweep scope: PA files, the workflows support docs, the root/methodology docs.
    Exempt: CHANGELOG, the generated trees, version-history footers (strip_footer),
    and the gap-analysis scenario table's authoring-time rows ('| N |' rows — the
    same dated-record status as the gap-history batch notes, whose own 6,757-era
    figures every wave has left standing)."""
    rel = "model-company-profile.md"
    hits = []
    prof_raw = open(os.path.join(MC, rel), encoding="utf-8").read()
    prof = strip_footer(prof_raw)

    m = re.search(r"\|\s*\*\*Total Company Headcount\*\*\s*\|\s*\*{0,2}~?([\d,]+)", prof)
    hc = int(m.group(1).replace(",", "")) if m else None
    m = re.search(r"\|\s*\*\*Annual Gross Revenue\*\*\s*\|\s*~PHP\s*([\d.]+)\s*Billion", prof)
    rev_b = float(m.group(1)) if m else None
    m = re.search(r"\|\s*\*\*Trade Account Customers\*\*\s*\|\s*~?([\d,]+)", prof)
    trade = int(m.group(1).replace(",", "")) if m else None
    m = re.search(r"\|\s*\*\*Corporate Account Customers\*\*\s*\|\s*~?([\d,]+)", prof)
    corp = int(m.group(1).replace(",", "")) if m else None
    if None in (hc, rev_b, trade, corp):
        return [(rel, 0, f"profile_derived_figure_hits: canonical inputs unparseable "
                         f"(HC={hc}, revenue={rev_b}, trade={trade}, corporate={corp})")]

    # (1) revenue-per-employee quotient, re-derived
    quot = round(rev_b * 1e9 / hc / 1e6, 2)
    quot_s = f"{quot:.2f}"
    anchor = f"~PHP {quot_s}M/year (~PHP {rev_b:g}B \u00f7 {hc:,})"
    if anchor not in prof:
        hits.append((rel, 0, f'required corrected revenue-per-employee anchor missing: '
                             f'"{anchor}" (re-derived: PHP {rev_b:g}B \u00f7 {hc:,} = '
                             f'~PHP {quot_s}M)'))

    # (2) B2B account counts: §15.2 Master-Data rows and the §10.3 AR row must
    # equal the §9.2 canon
    m = re.search(r"\|\s*Customers \(B2B Trade\)\s*\|\s*~?([\d,]+)\s*\|", prof)
    md_trade = int(m.group(1).replace(",", "")) if m else None
    m = re.search(r"\|\s*Customers \(B2B Corporate\)\s*\|\s*~?([\d,]+)\s*\|", prof)
    md_corp = int(m.group(1).replace(",", "")) if m else None
    if md_trade != trade:
        hits.append((rel, 0, f"\u00a715.2 Master-Data trade-customer row ({md_trade}) "
                             f"disagrees with the \u00a79.2 canon (~{trade:,})"))
    if md_corp != corp:
        hits.append((rel, 0, f"\u00a715.2 Master-Data corporate-customer row ({md_corp}) "
                             f"disagrees with the \u00a79.2 canon (~{corp:,})"))
    m = re.search(r"\|\s*\*\*Active AR Accounts\*\*\s*\|\s*~?([\d,]+)\s*"
                  r"\(([\d,]+) trade \+ ([\d,]+) corporate\)", prof)
    if not m:
        hits.append((rel, 0, "\u00a710.3 Active-AR-accounts row not in the "
                             "'~N (T trade + C corporate)' form"))
    else:
        ar, t2, c2 = (int(x.replace(",", "")) for x in m.groups())
        if ar != t2 + c2 or t2 != trade or c2 != corp:
            hits.append((rel, 0, f"\u00a710.3 AR row ({ar} = {t2} + {c2}) does not "
                                 f"cross-foot to the \u00a79.2 canon "
                                 f"({trade} + {corp} = {trade + corp})"))

    # (2b) the three live employee-count rows must equal the §4 canon — added by
    # the 2026-09-14 twenty-ninth-wave review after the promotion re-based
    # §3.3/§4/§11.1 but stranded §11.2's Payroll-Parameters 'Total Employees' row,
    # §15.2's Master-Data 'Employees' row and the §17 user-adoption bullet on the
    # retired 6,762 (no rule read them; profile_derived_figure_hits already
    # cross-foots §15.2's account rows, so the employees rows belong here)
    for label, pat in (
        ("\u00a711.2 Payroll-Parameters 'Total Employees' row",
         r"\|\s*\*\*Total Employees\*\*\s*\|\s*([\d,]+)\s*\|"),
        ("\u00a715.2 Master-Data 'Employees' row",
         r"\|\s*Employees\s*\|\s*([\d,]+)\s*\|"),
        ("\u00a717 user-adoption bullet",
         r"~([\d,]+)\s*users across varying tech literacy"),
    ):
        m = re.search(pat, prof)
        if not m:
            hits.append((rel, 0, f"{label} not found (required to carry the "
                                 f"\u00a74 total {hc:,})"))
        elif int(m.group(1).replace(",", "")) != hc:
            hits.append((rel, 0, f"{label} reads {m.group(1)} but the \u00a74 canon "
                                 f"is {hc:,}"))

    # (3) live-corpus citation sweep
    paths = sorted(glob.glob(os.path.join(MC, "workflows", "VS-*", "PA-*.md")))
    paths += sorted(glob.glob(os.path.join(MC, "workflows", "VS-*", "README.md")))
    paths += sorted(glob.glob(os.path.join(MC, "workflows", "*.md")))
    paths += sorted(glob.glob(os.path.join(MC, "*.md")))
    paths += sorted(glob.glob(os.path.join(REPO, "07-methodology", "*.md")))
    paths.append(os.path.join(REPO, "README.md"))
    rev_re = re.compile(r"[Rr]evenue[\s/\-]*(?:per[\s/\-]*)?"
                        r"employee[^\n]{0,120}?"
                        r"([\u2265>]?\s*)PHP\s*~?(\d+(?:\.\d+)?)\s*M")
    # the TO's §5.1 two-state total row carries the target denominator (6,911);
    # its 'Revenue/employee ≈ PHP 9.01M' note and the sizing row's '≥ PHP 9M
    # preserved' are target-state claims, both derived from rev ÷ target-HC
    to_raw = open(os.path.join(MC, "optimal-table-of-organization.md"),
                  encoding="utf-8").read()
    m = re.search(r"\*\*Total company\*\*\s*\|\s*\*\*~?([\d,]+)\*\*\s*\|\s*\|?\s*\*\*~?([\d,]+)\*\*", to_raw)
    target_hc = int(m.group(2).replace(",", "")) if m else None
    target_quot = round(rev_b * 1e9 / target_hc / 1e6, 2) if target_hc else None
    retired_acct = [
        # the census-complete retired-scheme forms: the trade base is the only
        # 5,000-account population in the corpus, so the bare adjacency is
        # unambiguous ('5,000 trade-relevant SKUs' does not match)
        "5,000 accounts", "5,000-account", "accounts (~5,000",
    ]
    for path in paths:
        raw = open(path, encoding="utf-8").read()
        body = strip_footer(raw)
        prel = os.path.relpath(path, REPO)
        if os.path.basename(path) == "workflow-gap-analysis.md":
            # scenario-table rows are the authoring-time record (dated by their
            # Pass number, like the batch notes) — exempt
            body = "\n".join(l for l in body.splitlines()
                             if not re.match(r"\|\s*\d+\s*\|", l))
        for m in rev_re.finditer(body):
            cited = float(m.group(2))
            threshold = bool(m.group(1).strip())
            if threshold:
                # '≥ PHP 9M' — a floor claim: it must be satisfiable at the
                # target denominator (9.0117… ≥ 9 ✓); an unsatisfiable floor
                # (> target quotient) is the drift
                if target_quot is None:
                    hits.append((prel, body[:m.start()].count("\n") + 1,
                                 f"revenue-per-employee floor '≥ PHP {m.group(2)}M' but "
                                 f"the TO two-state total row is unparseable"))
                elif cited > target_quot + 0.005:
                    hits.append((prel, body[:m.start()].count("\n") + 1,
                                 f"revenue-per-employee floor '≥ PHP {m.group(2)}M' is "
                                 f"unsatisfiable at the target denominator "
                                 f"(PHP {rev_b:g}B \u00f7 {target_hc:,} = ~PHP "
                                 f"{target_quot}M)"))
            elif abs(cited - quot) <= 0.005:
                pass  # current-state citation — canonical
            elif target_quot is not None and abs(cited - target_quot) <= 0.005:
                pass  # target-state citation (~9.01M at 6,911) — canonical
            else:
                bases = f"~PHP {quot_s}M (PHP {rev_b:g}B \u00f7 {hc:,})"
                if target_quot is not None:
                    bases += f" or ~PHP {target_quot}M at target (\u00f7 {target_hc:,})"
                hits.append((prel, body[:m.start()].count("\n") + 1,
                             f"revenue-per-employee citation ~PHP {m.group(2)}M matches "
                             f"neither derived canon: {bases}"))
        for lit in retired_acct:
            for m in re.finditer(re.escape(lit), body, re.I):
                hits.append((prel, body[:m.start()].count("\n") + 1,
                             f"retired B2B account-count literal \"{lit}\" "
                             f"(canonical scheme: trade ~{trade:,} + corporate ~{corp:,} "
                             f"= AR ~{trade + corp:,})"))
    return hits


def ebs_blueprint_hits():
    """2026-09-14 nineteenth-wave consistency review — structural guard for the
    02-oracle-ebs platform blueprint (seven documents that no check read; the review
    found eight defects across five of them). Re-derives every pinned figure from
    the primary sources on every run:
      (a) the fit-gap §2 register's class column → §3's pinned class-count table,
          the intro headline figures, and the §3 Reading note's BUILD split
          (5 already-built platforms vs the planned-build rows; the note's
          pre-doctrine/new-scope counts must sum to the planned rows and name them);
      (b) the touchpoint map's module set ↔ module-coverage-map §1's column-1 set —
          exact equality in both directions (the doc's 'one-for-one' claim — the
          review found two module rows missing);
      (c) the workflows/README canonical family names/counts ↔ coverage-map §2's
          eight roll-up rows in order (the review found six invented names with
          headlines describing the wrong families);
      (d) the architecture §7 NFR row's ecommerce total ↔ the profile's
          Total-Ecommerce-Orders canon (the review found the e-wallet subset
          quoted as the total);
      (e) the README §4 realization-wave prose ↔ the classification register's
          re-derived tier ladder."""
    hits = []

    def ebs(name):
        return os.path.normpath(os.path.join(MC, "..", "02-oracle-ebs", name))

    def add(doc, ln, msg):
        hits.append((doc, ln, msg))

    # ---- (a) fit-gap register class counts → §3 table + intro + Reading note
    fg = open(ebs("fit-gap-analysis.md"), encoding="utf-8").read()
    fg_body = strip_footer(fg)
    reg = fg_body.split("## 2. Capability Disposition Register")[1].split("## 3.")[0]
    counts, build_existing, build_planned = {}, [], []
    for ln in reg.splitlines():
        if not ln.startswith("| "):
            continue
        cells = [c.strip() for c in ln.split("|")]
        if len(cells) < 6 or not re.fullmatch(r"[A-H]\d+", cells[1] or ""):
            continue
        m = re.match(r"[A-Z][A-Z-]*", cells[4])
        if not m:
            add("fit-gap-analysis.md", 0,
                f"register row {cells[1]} has an unparseable class cell '{cells[4]}'")
            continue
        cls = m.group(0)
        counts[cls] = counts.get(cls, 0) + 1
        if cls == "BUILD":
            (build_existing if "*(existing)*" in cells[4] else build_planned).append(cells[1])
    total = sum(counts.values())
    std = counts.get("FIT-STD", 0) + counts.get("FIT-CFG", 0)
    expect = {"FIT-STD": 31, "FIT-CFG": 28, "PER": 2, "EXT": 2, "LOC": 1,
              "INT": 5, "BUILD": 14, "EDGE": 0, "OPEN": 0}
    for cls, want in expect.items():
        got = counts.get(cls, 0)
        if got != want:
            add("fit-gap-analysis.md", 0,
                f"register re-derives {got} {cls} rows but §3 pins {want} — the "
                f"class-count table no longer foots against the §2 register")
    if total != 83:
        add("fit-gap-analysis.md", 0,
            f"register re-derives {total} disposition rows but the pinned register "
            f"total is 83")
    # every §3 class-count cell must equal the §2 re-derivation (the rule's first
    # draft pinned only the standard-total and grand-total rows; a corrupted single
    # class cell sailed through — caught by this wave's own teeth suite, T4)
    sec3 = fg_body.split("## 3. Register Counts")[1].split("## 4.")[0]
    for cls, want in expect.items():
        m3 = re.search(rf"^\| \*{{0,2}}{cls}\*{{0,2}} \| \*{{0,2}}(\d+)", sec3, re.M)
        if not m3:
            add("fit-gap-analysis.md", 0, f"cannot find the §3 pinned row for {cls}")
        elif int(m3.group(1)) != counts.get(cls, 0):
            add("fit-gap-analysis.md", 0,
                f"§3 pins {m3.group(1)} {cls} rows but the §2 register re-derives "
                f"{counts.get(cls, 0)}")
    m = re.search(r"\*\*Standard total \(STD \+ CFG\)\*\* \| \*\*(\d+)\*\* \| \*\*([\d.]+)%\*\*", fg_body)
    if m:
        if (int(m.group(1)), float(m.group(2))) != (std, round(std / total * 100, 1)):
            add("fit-gap-analysis.md", 0,
                f"§3 standard-total row says {m.group(1)} rows / {m.group(2)}% but the "
                f"register re-derives {std} / {round(std / total * 100, 1)}%")
    else:
        add("fit-gap-analysis.md", 0, "cannot find the §3 standard-total row")
    m = re.search(r"\*\*Total register rows\*\* \| \*\*(\d+)\*\*", fg_body)
    if m and int(m.group(1)) != total:
        add("fit-gap-analysis.md", 0,
            f"§3 total row says {m.group(1)} but the register re-derives {total}")
    if f"{total}-row register" not in fg_body:
        add("fit-gap-analysis.md", 0,
            f"intro headline does not carry the re-derived '{total}-row register' figure")
    norm = " ".join(fg_body.replace(">", " ").split())  # the intro blockquote wraps mid-clause
    if f"**{std} rows ({round(std / total * 100, 1)}%) run on standard or configured EBS**" not in norm:
        add("fit-gap-analysis.md", 0,
            f"intro headline does not carry the re-derived '{std} rows "
            f"({round(std / total * 100, 1)}%)' standard-share figure")
    if len(build_existing) != 5:
        add("fit-gap-analysis.md", 0,
            f"register re-derives {len(build_existing)} already-built BUILD rows "
            f"({', '.join(build_existing)}) but 5 are pinned")
    else:
        m = re.search(r"of which (\d+) already-built platforms: ([^|*]+)", fg_body)
        if not m or int(m.group(1)) != len(build_existing) or \
                any(rid not in m.group(2) for rid in build_existing):
            add("fit-gap-analysis.md", 0,
                f"§3 BUILD row's already-built list does not match the register's "
                f"re-derived BUILD*(existing)* rows: {', '.join(build_existing)}")
    m = re.search(r"of which (\d+) rows predate", fg_body)
    n_new = re.search(r"and (\d+) rows are new scope", fg_body)
    if not m or not n_new:
        add("fit-gap-analysis.md", 0,
            "§3 Reading note lost its pre-doctrine/new-scope BUILD-split clauses "
            "(expected 'of which N rows predate' and 'and M rows are new scope')")
    elif int(m.group(1)) + int(n_new.group(1)) != len(build_planned):
        add("fit-gap-analysis.md", 0,
            f"Reading note's BUILD split ({m.group(1)} predate + {n_new.group(1)} "
            f"new scope) does not sum to the register's {len(build_planned)} planned "
            f"BUILD rows ({', '.join(build_planned)})")
    else:
        note = fg_body.split("Reading:")[1]
        ids_named = set(re.findall(r"\b[A-H]\d+\b", note))
        # expand 'E5–E7'-style row ranges (the note summarizes the payroll trio as a range)
        for a1, n1, a2, n2 in re.findall(r"\b([A-H])(\d+)–([A-H])(\d+)\b", note):
            if a1 == a2:
                ids_named |= {f"{a1}{i}" for i in range(int(n1), int(n2) + 1)}
        missing = [rid for rid in build_planned if rid not in ids_named]
        if missing:
            add("fit-gap-analysis.md", 0,
                f"Reading note's BUILD split does not name planned-build row(s) "
                f"{', '.join(missing)}")

    # ---- (a.1) §7 standard-first KPI row tracks the register — the 2026-09-15
    # exhaustion audit trued the §3 total row and the intro headline but stranded
    # the KPI table's '(current 68.4%)' against the re-derived 71.1% (59/83) — a
    # row whose own enforcement cell says 'This register, re-run per wave'
    # (thirty-fifth-wave consistency review).
    kpi_sec = (fg_body.split("## 7. Standard-First KPIs")[1]
               if "## 7. Standard-First KPIs" in fg_body else "")
    mk = re.search(r"\(current ([\d.]+)%\)", kpi_sec)
    if not mk:
        add("fit-gap-analysis.md", 0,
            "cannot find the §7 standard-share KPI row's '(current N%)' figure")
    elif float(mk.group(1)) != round(std / total * 100, 1):
        add("fit-gap-analysis.md", 0,
            f"§7 KPI row says 'current {mk.group(1)}%' but the register re-derives "
            f"{std}/{total} = {round(std / total * 100, 1)}%")

    # ---- (b) touchpoint-map module set ↔ coverage-map §1 (one-for-one)
    tm = open(os.path.join(MC, "workflows", "workflow-system-touchpoint-map.md"),
              encoding="utf-8").read()
    tm_rows = re.findall(r"^\| \*\*(.+?)\*\* \|", tm, re.M)
    cm = strip_footer(open(ebs("module-coverage-map.md"), encoding="utf-8").read())
    cm_sec1 = cm.split("## 1. Generic Module")[1].split("## 2.")[0]
    cm_rows = re.findall(r"^\| \*\*(.+?)\*\* \|", cm_sec1, re.M)
    if sorted(tm_rows) != sorted(cm_rows):
        missing = [r for r in tm_rows if r not in cm_rows]
        extra = [r for r in cm_rows if r not in tm_rows]
        add("module-coverage-map.md", 0,
            f"§1 module set is not one-for-one with the touchpoint map "
            f"({len(tm_rows)} rows there, {len(cm_rows)} here"
            f"{' — missing: ' + '; '.join(missing) if missing else ''}"
            f"{' — not in the touchpoint map: ' + '; '.join(extra) if extra else ''})")

    # ---- (c) canonical family names/counts ↔ coverage-map §2 roll-up
    wf = open(os.path.join(MC, "workflows", "README.md"), encoding="utf-8").read()
    canon = re.findall(r"^### (.+?) \(([\d,]+) workflows\)", wf, re.M)
    cm_sec2 = cm.split("## 2. Family Coverage Summary")[1].split("## 3.")[0]
    cm_fam = re.findall(r"^\| \*\*(.+?)\*\* \(([\d,]+) WF\)", cm_sec2, re.M)
    canon_named = [(n, int(c.replace(",", ""))) for n, c in canon]
    cm_named = [(n, int(c.replace(",", ""))) for n, c in cm_fam]
    if canon_named != cm_named:
        add("module-coverage-map.md", 0,
            f"§2 family roll-up does not match the workflow catalog's canonical "
            f"families (catalog: "
            f"{' / '.join(f'{n} {c}' for n, c in canon_named)}; coverage map: "
            f"{' / '.join(f'{n} {c}' for n, c in cm_named) or 'none parsed'})")

    # ---- (d) architecture §7 ecommerce total ↔ the profile's canon
    prof = open(os.path.join(MC, "model-company-profile.md"), encoding="utf-8").read()
    m = re.search(r"\| Total Ecommerce Orders \| ~([\d,]+) \|", prof)
    arch = strip_footer(open(ebs("ebs-platform-architecture.md"), encoding="utf-8").read())
    if m:
        if f"~{m.group(1)} ecommerce" not in arch:
            add("ebs-platform-architecture.md", 0,
                f"§7 NFR row does not carry the profile's Total-Ecommerce-Orders "
                f"canon (~{m.group(1)}/month) — the e-wallet subset must not stand "
                f"in for the total")
    else:
        hits.append(("model-company-profile.md", 0,
                     "cannot find the '| Total Ecommerce Orders |' canon row "
                     "(ebs_blueprint_hits re-derivation source)"))

    # ---- (e) README realization-wave prose ↔ the classification tier ladder
    cls = open(os.path.join(MC, "workflows", "workflow-criticality-classification.md"),
               encoding="utf-8").read()
    tiers = dict(re.findall(r"^## Tier (\d): [^\n]*\(([\d,]+) Workflows\)", cls, re.M))
    rd = strip_footer(open(ebs("README.md"), encoding="utf-8").read())
    for t in sorted(tiers):
        if f"Tier {t} ({tiers[t]}" not in rd:
            add("README.md (02-oracle-ebs)", 0,
                f"realization-wave prose does not carry the classification "
                f"register's re-derived Tier-{t} figure ({tiers[t]})")
    return hits


def integration_mirror_hits():
    """2026-09-14 twenty-first-wave consistency review — the doctrine cascade
    extended the integration estate (fit-gap E8: the in-house Payroll PH build
    posts period costing to the GL) but never reached the canonical integration
    map, and 02-oracle-ebs/integrations.md §2's header claims its Flow column
    'quotes the canonical matrix rows' — a claim that was false at the edges
    (the gateway chargeback/fee row had no canonical counterpart; the canonical
    delivery-status row was silently folded into the outbound 3PL row). Re-derived
    every run: (a) data-volumes §3's Integration Detail Matrix must carry exactly
    one Payroll PH → ERP posting row (the E8 INT canon); (b) the register's Flow
    column must quote the canonical matrix one-for-one, in the matrix's own order,
    with exactly one declared register extension (the gateway chargeback/fee row)
    — a missing, folded, extra, reordered or re-endpointed row fires."""
    hits = []

    def norm(s):
        return re.sub(r"[^a-z0-9]", "", s.lower())

    # ---- (a) the canonical matrix's own integrity + the payroll posting row
    dv = strip_footer(open(os.path.join(MC, "data-volumes-and-integrations.md"),
                           encoding="utf-8").read())
    if "## 3. Integration Detail Matrix" not in dv:
        return [("data-volumes-and-integrations.md", 0,
                 "cannot find §3 Integration Detail Matrix "
                 "(integration_mirror_hits re-derivation source)")]
    sec3 = dv.split("## 3. Integration Detail Matrix")[1].split("## 4.")[0]
    canon = []
    for ln in sec3.splitlines():
        if not ln.startswith("| "):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) != 5 or cells[0] == "Source":
            continue
        canon.append((cells[0], cells[1]))
    if not canon:
        return [("data-volumes-and-integrations.md", 0,
                 "cannot parse the §3 Integration Detail Matrix rows "
                 "(integration_mirror_hits re-derivation source)")]
    payroll = [r for r in canon if "payroll" in r[0].lower()]
    if len(payroll) != 1 or "erp" not in payroll[0][1].lower():
        hits.append(("data-volumes-and-integrations.md", 0,
                     f"§3 canonical matrix must carry exactly one Payroll PH → ERP "
                     f"posting row (the fit-gap E8 INT canon the EBS pattern register "
                     f"quotes) — found {payroll or 'none'}"))

    # ---- (b) the EBS pattern register must quote the canonical rows 1:1, in order
    reg_path = os.path.normpath(os.path.join(MC, "..", "02-oracle-ebs", "integrations.md"))
    reg = strip_footer(open(reg_path, encoding="utf-8").read())
    if "## 2. Pattern Register" not in reg:
        return hits + [("integrations.md (02-oracle-ebs)", 0,
                        "cannot find §2 Pattern Register")]
    sec2 = reg.split("## 2. Pattern Register")[1].split("## 3.")[0]
    flows = []
    for ln in sec2.splitlines():
        if not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) != 4:
            continue
        m = re.match(r"^(.+?)\s*→\s*(.+?):", cells[0])
        if m:
            flows.append((m.group(1), m.group(2), cells[0]))
    quoted = [f for f in flows if "chargebacks/fees" not in f[2].lower()]
    extensions = [f for f in flows if "chargebacks/fees" in f[2].lower()]
    if len(extensions) != 1:
        hits.append(("integrations.md (02-oracle-ebs)", 0,
                     f"the §2 register must declare exactly one extension row (the "
                     f"gateway chargeback/fee row, marked as beyond the canonical "
                     f"matrix) — found {len(extensions)}"))
    if len(quoted) != len(canon):
        hits.append(("integrations.md (02-oracle-ebs)", 0,
                     f"§2 register quotes {len(quoted)} canonical-matrix flows but the "
                     f"§3 matrix re-derives {len(canon)} — every canonical flow needs "
                     f"exactly one register row (no folding, no additions beyond the "
                     f"declared extension)"))
    else:
        for i, ((cs, ct), (rs, rt, raw)) in enumerate(zip(canon, quoted)):
            if norm(cs) != norm(rs) or norm(ct) != norm(rt):
                hits.append(("integrations.md (02-oracle-ebs)", 0,
                             f"register row {i + 1} '{raw}' does not quote canonical "
                             f"matrix row {i + 1} '{cs} → {ct}' — the Flow column must "
                             f"quote the canonical endpoints verbatim, in the matrix's "
                             f"own order"))
    return hits


def migration_template_hits():
    """2026-09-14 twenty-first-wave consistency review — the two-tier doctrine
    moved payroll balances (02-oracle-ebs/data-migration.md v1.1 row 11: payroll
    YTD loads into the in-house Payroll PH build; EBS receives postings, not
    balances) but the legacy mapping template (data-migration-mapping.md) still
    routed YTD earnings & deductions into the ERP — the same-day sibling
    contradiction the (b)-commit cascade class keeps producing. The corrected
    §1 scope-row and §2.4 YTD-row forms are required present, the retired
    YTD-into-EBS routing is forbidden in live prose, and the 02 row-11 anchor
    this template must not contradict is required present."""
    hits = []
    rel = "data-migration-mapping.md"
    body = strip_footer(open(os.path.join(MC, rel), encoding="utf-8").read())
    for anc in (
            "year-to-date earnings & deductions to the in-house Payroll PH build",
            "EBS receives postings, not balances",
            "Load into the in-house Payroll PH build — not EBS",
    ):
        if anc not in body:
            hits.append((rel, 0, f'missing required anchor "{anc}"'))
    for lit in (
            "Full employee master + year-to-date for BIR reconciliation",
            "Migrate year-to-date for BIR annual reconciliation",
    ):
        for m in re.finditer(re.escape(lit), body):
            hits.append((rel, body[:m.start()].count("\n") + 1,
                         f'retired payroll-YTD-into-EBS routing "{lit}"'))
    dm = strip_footer(open(os.path.normpath(
        os.path.join(MC, "..", "02-oracle-ebs", "data-migration.md")),
        encoding="utf-8").read())
    if "Loaded into the **in-house payroll build** (Payroll PH)" not in dm:
        hits.append(("data-migration.md (02-oracle-ebs)", 0,
                     "row 11's in-house-payroll-build anchor is missing — the mapping "
                     "template's YTD routing must not contradict it"))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true",
                    help="exit 1 on any unresolved reference or retired figure")
    args = ap.parse_args()
    wids, vsids, paids, ctlids, reqids = load_registers()
    prof_secs = sections_of(os.path.join(MC, "model-company-profile.md"))
    tg_secs = sections_of(os.path.join(REPO, "07-methodology", "technical-guidelines.md"))
    dv_secs = sections_of(os.path.join(MC, "data-volumes-and-integrations.md"))
    # review #68: the two organizational docs also cite the headcount reality
    # check and the IT operating model — both join the bare-§ fallback union
    rc_secs = sections_of(os.path.join(MC, "headcount-reality-check.md"))
    it_secs = sections_of(os.path.join(REPO, "07-methodology",
                                       "it-product-operating-model.md"))
    # 2026-09-14 nineteenth-wave consistency review: the blueprint docs cite the
    # sourcing model ('sourcing model §12.1', 'sourcing model §7 rule 7') and their
    # own siblings ('architecture §4', 'fit-gap §6', 'customization-governance §5',
    # 'integrations §1') — both join the bare-§ fallback union (the rc/it precedent).
    src_secs = sections_of(os.path.join(REPO, "07-methodology",
                                        "capability-sourcing-and-engineering-model.md"))
    # data-migration.md cites its mapping companion's subsections ('per mapping §2.1')
    dmm_secs = sections_of(os.path.join(MC, "data-migration-mapping.md"))
    ebs_secs = set()
    for rel in DOCS:
        if rel.startswith("../02-oracle-ebs/"):
            ebs_secs |= sections_of(os.path.normpath(os.path.join(MC, rel)))
    hits = []
    for rel in DOCS:
        doc = os.path.basename(rel)
        path = os.path.normpath(os.path.join(MC, rel))
        text = open(path, encoding="utf-8").read()
        body = strip_footer(text)
        for m in re.finditer(r"\b(W\d+[A-Z]?|VS-\d+|CTL-\d+|PA-\d+\.\d+|[A-Z]{2,4}-\d{3})\b", body):
            tok = m.group(1)
            line = body[:m.start()].count("\n") + 1
            # review #68: dispatch prefixed namespaces FIRST — the generic
            # requirement pattern would otherwise swallow 3-digit VS-1xx/CTL-1xx
            # tokens (e.g. VS-101 fullmatches [A-Z]{2,4}-\d{3})
            if re.fullmatch(r"W\d+[A-Z]?", tok):
                if tok == "W0":
                    continue  # 2026-09-14 nineteenth-wave review: the 02-oracle-ebs
                    # realization-wave tables label their foundation wave 'W0 —
                    # Foundation' (data-migration §2 sequence likewise); W0 is a wave
                    # label, not a workflow id — the register's ids start at W1.
                if tok not in wids:
                    hits.append((doc, line, f"unresolved {tok}"))
            elif tok.startswith("VS") and tok not in vsids:
                hits.append((doc, line, f"unresolved {tok}"))
            elif tok.startswith("CTL") and tok not in ctlids:
                hits.append((doc, line, f"unresolved {tok}"))
            elif tok.startswith("PA") and tok not in paids:
                hits.append((doc, line, f"unresolved {tok}"))
            elif re.fullmatch(r"[A-Z]{2,4}-\d{3}", tok) and not re.match(r"(?:VS|CTL|PA)-", tok):
                # (namespace-prefixed tokens that RESOLVED above must not
                # fall through into the requirement register check —
                # VS-177 fullmatches the generic requirement shape)
                if tok not in reqids:
                    hits.append((doc, line, f"unresolved requirement {tok}"))
        for m in re.finditer(r"(Technical Guidelines|technical-guidelines)\s*§(\d+(?:\.\d+)?)", body):
            if m.group(2) not in tg_secs:
                hits.append((doc, body[:m.start()].count("\n") + 1,
                             f"unresolved technical-guidelines §{m.group(2)}"))
        for m in re.finditer(r"(?<!Guidelines )(?<!guidelines )§(\d+(?:\.\d+)?)", body):
            sec = m.group(1)
            own = sections_of(path)
            if sec not in prof_secs and sec not in own and sec not in dv_secs \
                    and sec not in rc_secs and sec not in it_secs \
                    and sec not in src_secs and sec not in ebs_secs \
                    and sec not in dmm_secs:
                hits.append((doc, body[:m.start()].count("\n") + 1,
                             f"unresolved §{sec}"))
        for lit in RETIRED_LITERALS.get(doc, []):
            for m in re.finditer(re.escape(lit), body):
                line_start = body.rfind("\n", 0, m.start()) + 1
                if body[line_start:line_start + 20].startswith(("*Date:", "*Document Version:")):
                    continue  # version-history footer
                hits.append((doc, body[:m.start()].count("\n") + 1,
                             f'retired literal "{lit}"'))
        for anc in ANCHORS.get(doc, []):
            if anc not in body:
                hits.append((doc, 0, f'missing required anchor "{anc}"'))
        for lit in RETIRED_FIGURES:
            if lit in RETIRED_FIGURE_EXEMPT.get(doc, set()):
                continue
            for m in re.finditer(re.escape(lit), body):
                hits.append((doc, body[:m.start()].count("\n") + 1,
                             f"retired figure {lit}"))
    for doc in LEGACY_FORM_DOCS:
        for d, line, detail in legacy_form_hits(os.path.join(MC, doc)):
            hits.append((d, line, detail))
    hits.extend(dc_roster_hits(os.path.join(MC, "optimal-table-of-organization.md")))
    hits.extend(to_phase_hits())
    # 2026-09-09 thirteenth-wave consistency review addition
    hits.extend(to_register_hits())
    hits.extend(sourcing_tier_hits())
    hits.extend(guide_figure_hits())
    hits.extend(om_reconciliation_hits())
    hits.extend(register_heading_hits())
    hits.extend(methodology_index_hits())
    hits.extend(live_pin_hits())
    # 2026-09-07 eighth-wave consistency review additions
    hits.extend(dv_volume_hits())
    hits.extend(exec_tree_hits())
    hits.extend(reality_check_hits())
    # 2026-09-07 ninth-wave consistency review addition
    hits.extend(companion_pin_hits())
    # 2026-09-09 sixteenth-wave consistency review addition
    hits.extend(profile_derived_figure_hits())
    # 2026-09-14 nineteenth-wave consistency review addition
    hits.extend(ebs_blueprint_hits())
    # 2026-09-14 twenty-first-wave consistency review additions
    hits.extend(integration_mirror_hits())
    hits.extend(migration_template_hits())
    for doc, line, detail in hits:
        print(f"model-doc: {doc}:{line}: {detail}")
    print(f"audit-model-docs: {len(hits)} hit(s) across {len(DOCS)} documents")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
