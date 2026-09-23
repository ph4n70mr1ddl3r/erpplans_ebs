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

2026-09-23 Component-GPL sellable-SKU sweep: gpl_sku_sweep_hits joins the guard for the
 coverage register's new §7 — the price-list direction (the third artifact after the
 workflow corpus and the documentation library): the §7 result sentence re-derived
 against the part-number universe of applications-price-list-070574.pdf itself
 (pdftotext every run), every backtick-cited part number existence-checked, the four
 entitlement-flag pins (L11496, L72211, L31659, L42175) and the L72189 collision pin
 required, and the UPK band count re-derived from the band-priced lines.

2026-09-23 sixty-sixth-wave consistency review: calibrated_volume_hits joins the guard
 for the production-volume calibration's (data-volumes v4.7) derived-surface stragglers
 — 46 volume-citing cells across 30 documents kept the retired canons after the §1.1/§1.2
 rows moved: ~5,000 replenishment orders/month (new canon ~50,000/month, ~1,700/day,
 ~415–425/DC/day; physical deliveries deliberately unchanged — 2–3 drops/store/week,
 ~20–30 orders consolidated per drop, ~60–80 loads/day chain-wide), the ~18,000 PO
 lines/month and ~15-lines-per-PO basis (new canon ~12,000 all types at ~7 lines/PO;
 the profile's own §6.5 band had been left against its restated §15.1), the ~100 GB/year
 and ~1,000 GB storage sizing (new canon ~123 GB/year, ~1,230 GB over 10 years), and the
 pre-ecommerce-canon ~10,000 home deliveries/month family (the W19 canon: 17,200/month
 = ~573/day). The retired forms are banned on live PA/README surfaces (whole files —
 no history blocks), footer-stripped bodies and the classification register's live cells;
 the calibrated anchors are required at the repaired cells; the gap-analysis scenario
 tables and version footers stay exempt as frozen history (the sixteenth-wave
 convention). Teeth: five synthetic injections through the FULL audit, each caught at
 its exact arm, fixtures restored byte-identical.

 2026-09-23 sixty-seventh-wave consistency review: calibrated_volume_hits extended for
 the sibling-cell stragglers the calibration and the sixty-sixth-wave sweep both left
 inside the very files they repaired — W4's own Volume row + four staffing sentences
 (~167/day, ~42/DC/day, ~50 lines/order under a Frequency row the wave itself re-pointed),
 PA-04.2's other six volume-citing workflows (W1352 Frequency vs its own re-based Volume;
 W1353 ~33+~115; W1369 ~148; W1370 ~5,000/month vs its own re-based Background; W836's
 4×~10=~40 loads/day vs its own ~1,800–2,400/month clause), PA-04.3's dock-appointment
 cells (30 outbound loads/DC/day vs the 60–80/day chain-wide canon), W1256's Volume
 (~5,000 RTP shipments vs its own re-based Background), W277/W461's freight-billable
 family (~10,000–17,000 home deliveries; ~12,000–20,000 sum), W919's Background tail
 (~5,000+ movements vs its own repaired Frequency), W784's ~60,000/year annual form,
 W1415's ~500–800 SKUs/delivery lines-per-drop and PA-10.2's staffing sentence. The
 repaired cells state the load/drop canon (load = consolidated drop; 60–80 loads/day
 chain-wide = 15–20/DC/day; W4 at ~1,700 orders/day, ~3 lines/order → ~1,250 pick
 lines/DC/day) and are anchor-pinned; the PA-15.1 sum form is file-scoped banned.
 Teeth: three synthetic injections through the FULL audit, each caught at its exact arm,
 fixtures restored byte-identical.

 2026-09-23 sixty-eighth-wave consistency review: calibrated_volume_hits extended for
 the calibration's own written-cell drift and the new canon rows' unread derived cells —
 W1352's Time Estimate (PA-04.2, written by the calibration itself at ~5,300/~1,060/~265
 chain-wide pick lines against the file's own ~1,250/DC/day Frequency anchor → ~5,000
 chain-wide; hours re-footed ~7–14/~6–8/~13–21), W92's adjustment cells (PA-05.3 —
 ~1,700–2,600/month at 200×8–12 + 4×30–50 against the calibration's new §1.1 IAD row
 ~30/day ≈ ~900/month, measured 3,508–11,652/yr; re-based to 200×~3–5 + 4×~20–30 =
 ~680–1,120/month, ~1–2 h/store/month), W270's RTP cell (PA-04.3 — ~40 receipts/day/DC
 against PA-04.1's canon-citing ~50 ×4 cells and §1.1's 200/day row; ~2.5 hours/day),
 W3962's Volume (PA-129.2 — the retired ~1,400–1,600 POs/month band; trued to ~1,200
 merchandise POs/month, all types ~1,600–1,900), PA-28.2's two remaining 1,000 GB cells
 (W881 risk bullet + W1481 backup step) against its own ~1,230 GB anchor and A6.5/§1.2,
 and W109/W666's 20–50-lines-per-delivery cells (PA-07.3) against the 60–90-line
 consolidated-drop canon. The wave-66 banned form '5,000 replenishment' narrowed to
 '5,000 replenishment orders' — the loose form fired on the corrected ~5,000
 replenishment pick lines/day anchor (the wave-67 withdrawal convention).
 Teeth: four synthetic injections through the FULL audit, each caught at its exact arm
 (banned form + missing anchor), fixtures restored sha256-verified byte-identical.

 2026-09-23 sixty-ninth-wave consistency review: the calibration straggler one layer
 further out, plus the GPL sweep's misdirected flag — two repairs and two guard
 extensions. (1) The root README's at-a-glance PO row ('~1,200 merchandise;
 ~1,400–1,600 total') still carried the retired total-PO band the sixty-sixth wave
 retired on profile §6.5/TO/W2 and the sixty-eighth wave retired on W3962 — the one
 volume-citing surface neither the (b) cascade nor waves 66–68 swept (the README sits
 outside the PA/README glob in calibrated_volume_hits and outside the versioned-doc
 list; no check read the row at PO-band grain). Trued to the §15.1 canon (~1,200
 merchandise; ~1,600–1,900 total production-calibrated); calibrated_volume_hits gains
 the root-README arm (swept whole — un-versioned), the retired '~1,400–1,600 total'
 form banned and the calibrated anchor required; the loose numeral pair is deliberately
 NOT banned repo-wide (PA-79.2's separated-employee cells legitimately use it).
 (2) The §4-resolution-37 Asset-Tracking entitlement flag (L11496 verify-at-RFQ) was
 appended to the fit-gap register's D6 POS row — a paste-family misdirection: the flag
 qualifies F7's own 'rides the Install Base/Inventory bases (BOM decision 6)' clause
 and has no bearing on D6's in-house-checkout disposition, while F7 carried none and
 resolution 37's own record declares the flags 'carried on the F7/B10 note cells'.
 The flag sentence moved D6 → F7 verbatim (fit-gap v2.9 footer segment); ebs_blueprint_hits
 gains the flag-placement arm (the entitlement-flag/L11496 forms banned on the D6 row,
 the flag anchor required on the F7 row).
 Teeth: four synthetic injections through the FULL guard, each caught at its exact arm
 with file and line named (D6 re-mint → both retired-form arms at :156; F7 flag strip →
 the missing-anchor arm at :197; README band re-mint → the retired-form arm at :342 plus
 the missing-anchor arm; README anchor-only strip → the missing-anchor arm), fixtures
 restored sha256-verified byte-identical, clean tree silent at 0 hits.

 2026-09-23 seventieth-wave consistency review: the receipt/ASN/container sibling
 family, one derivation step out from the pinned cells — four PA-file clusters plus the
 rule docstring's own duplicated sixty-eighth-wave paragraph (a paste-family artifact
 of that wave's commit) removed. (1) W3's Volume (PA-04.1) still read '~15 lines per
 receipt' — the retired ~15-lines-per-PO basis the sixty-sixth wave retired on the PO
 surfaces — which × the ~6,000 receipts/month canon implied ~90,000 receipt lines/month
 against the ~12,000 PO-lines/month all-types canon; trued to ~2 lines per receipt
 (bulk POs arrive as multiple partial truck receipts). (2) W3C's Volume (same file)
 read '~20–30 import containers per DC per month' against W1271's own '~100–150
 containers/DC/month' and W1169's '~20–30 per DC per week', both deriving from the
 ~400–600 TEUs/month §7.1 import canon at ~1 TEU/container (the receipt-mix cell still
 foots ~1,410–1,640 vs the ~1,500/DC/month Frequency); trued to ~100–150, file-scoped
 banned on PA-04.1 (PA-01.1's per-seasonal-event forward-buy cells are a different,
 legitimate population). (3) W1365's ASN universe (same file) read '~4,800 ASN
 submissions/month' = 80% × the 6,000-receipt canon — but 1 ASN per PO (W1006's own
 Volume model) caps the ASN spine at the ~1,200-merchandise-PO universe: W1006's
 ~700–750/month and PA-03.4's combined ~5,000–10,000 portal-document band (PO acks +
 ASNs + invoices ≈ 8,700 inside the band; 4,800 ASNs would blow it to ~12,700) both
 adjudicate the PO-spine reading, and W1365's own 15–20% exceptions of 4,800 = 720–960
 equaled W1006's ENTIRE ASN universe — nearly every ASN discrepant, against its own
 <70%-accuracy flagging threshold; trued to ~700–750 ASNs with ~105–150 exceptions, the
 Time Estimate re-footed (~18–50 h/month chain-wide, ~4–13 h/DC; total ~40–75 h/month)
 and the Staffing cells re-derived (DC Inbound Supervisor ~4–13 h/DC/month; Buyer
 ~6–9 h/month total, <1 h/buyer) — both roles still absorbed, no HC change. (4) W1006's
 Volume (PA-03.2) read 'average 15 lines per ASN' under its own '1 ASN per PO' model —
 the ASN mirrors its PO; trued to ~7 lines per ASN at the 6.9–7.4 lines/PO canon.
 (5) W1169's Volume (PA-06.1) read '~15–25 container drayage moves per DC per week',
 below its own Frequency row's '~20–30 containers per DC per week' arrival canon;
 trued to ~20–30 round-trip moves (one per container, port ↔ DC with the empty
 return). Guard: calibrated_volume_hits gains the seventieth-wave arms — the four
 retired forms banned repo-wide ('~15 lines per receipt', '15 lines per ASN',
 '4,800 ASN', '~15–25 container drayage moves'), the container form file-scoped banned
 on PA-04.1, and the corrected anchors required at the six repaired cells (a future
 calibration moves the canon → these re-fire until consciously re-pointed — the
 Check-71 CENSUS-pin contract).
 Teeth: five synthetic injections through the FULL audit, each caught at its exact arm
 with file and line named (W3 re-mint → banned-form at :30 + missing-anchor; W3C
 re-mint → file-scoped arm + missing-anchor, with PA-01.1's seasonal form verified
 exempt; W1365 re-mint → banned-form at :874 + missing-anchor; W1006 re-mint →
 banned-form at :504 + missing-anchor; W1169 re-mint → banned-form at :257 +
 missing-anchor), fixtures restored sha256-verified byte-identical, clean tree silent
 at 0 hits.

 2026-09-23 seventy-first-wave consistency review: the returns canon — the one §1.1
 row the production calibration grounded but whose workflow family it never
 re-derived. The calibration's Customer-Returns row (measured 14,744/13,584 AR
 credit memos/year at ~1.05 lines/doc → ~40/day ≈ ~1,200/month ≈ ~14,500/year;
 profile §15.1's AR-Credit-Memos row) sits 47x below the returns workflows'
 pre-calibration assumption of ~56,000 returns/month (2% × 2.8M transactions),
 and the ecommerce sub-canon of ~4,000–5,000 return requests/month at ~10–12%
 of ~42,900 orders is untenable inside a ~1,200/month all-channel universe (the
 W12B cell even miscited '≈110–140/day per the corpus returns canon' for a SUBSET
 of a 40/day canon). ~50 cells trued across 16 documents: PA-32.1's W1622 master
 (~950–1,050 counter returns/month = the canon less W1629's ~100–150 B2B credit
 notes and W215's ~50–100 courier pickups; ~5/store/month; hours re-footed
 ~0.8 h/store/month), W1623 (~250–350 requests at ~0.6–0.8%; drop-off subset
 ~200–250 at ~0.5–0.6%; courier ≈ 50–100), W1624 (~325 exchanges, 27%), W1625
 (~180–215 no-receipt, 15–18%), W1626 (~180–215 quality, 15–18%), W1627 (~875
 refunds = the canon less exchanges; ~4–5/store/month), W1628, W1629 (~100–150
 B2B returns at ~2–4% of the ~3,200–5,200 B2B order universe, one credit note per
 return at the ~1.05-lines/doc profile); PA-07.1's W12A/W12B/W12C (W12C
 ~120–240/month at the unchanged 10–20% share); PA-08.3's W540 (~1,200 BIR credit
 notes/month) and W605 (~36–60 fraudulent at 3–5%); PA-23.3's W1336 (~60–95 at
 5–8%; the 'per W1627' miscite trued to W1622); PA-32.3 (~360 disposition
 exceptions, ~720 h/yr); PA-10.1's W509 (~500–1,000 returned items; 1–2 Returns
 Inspectors, absorbed); PA-10.2's W215 (~0.3–0.6% of home deliveries, ~50–100/
 month; staffing re-footed ~17–33/~8–17/~8–17 h/month) and W1273 (~1 drop-off/
 store/month; ~50–104 h/month chain-wide); PA-13.1's W707 (~40 total returns/day
 across all channels); PA-60.3's W2308; PA-125.2 (~14,500 returns/yr); PA-118.2;
 PA-15.2's W101 (~950–1,050 + ~200–250 + ~50–100 + ~100–150 = ~1,300–1,550
 refund/credit transactions/month; hours re-footed ~76–93); PA-30.2's IDP row
 (~1,200 return receipts/month beside its already-true receipt canon); the
 profile's §5 POS transaction-mix bullet (~0.04%, bumped v3.4); the custody
 register's live E-09 row (bumped v1.11); and erp-requirements GOV-051 (bumped
 v24.4). Category-level return-rate prose (PA-09.2's 10–15%/8–12% bathroom-
 fixture/electrical rates) and PA-30.3's training-hours '~56,000 hours' are
 different, legitimate populations, exempt. Guard: calibrated_volume_hits gains
 the seventy-first-wave arms — the retired forms banned on live surfaces, the
 corrected anchors required at the repaired cells, and the custody register's
 live body (before its dated footer) swept with the E-09 anchor required.
 Teeth: four synthetic injections through the FULL audit, each caught at its exact
 arm, fixtures restored sha256-verified byte-identical, clean tree silent at 0 hits.

 2026-09-23 seventy-second-wave consistency review: the dodging-variant stragglers —
 three families the prior sweeps' banned forms read past at the glyph level: (1) the
 hyphenated replenishment form '~5,000 store-replenishment orders/month'
 (PA-136.1's W4126 Volume + the VS-136 README framing sentence — both wave-66 forms
 '5,000 store replenishment'/'5,000 replenishment orders' are space-form), with
 W4126 step 2's 'replenishment grouping 2–3 orders/truck' a surviving copy of the
 retired consolidation mechanic (canon: each store drop consolidates the ~20–30
 orders since the previous drop, 2–3 drops per truck trip); (2) the returns-canon
 sibling stragglers INSIDE the files the seventy-first wave repaired — PA-32.3's
 W1641 ('~56,000 return dispositions/month' Frequency + '~70% of ~56,000 monthly
 returns' touchpoint + 'mis-routes thousands of returns' pain point, against the
 same workflow's own wave-71-trued ~1,200/month Time Estimate) and W1640's refurb
 pool (~500–800 items/month = 42–67% of ALL returns, untenable when only ~180–215
 returns/month are quality-assessed; re-based to ~180–300 eligible = the
 damaged-packaging-functional share, ~45–75/DC, hours re-footed ~900–1,500 h/yr)
 and PA-23.3's W1336 Background ('~56,000 product returns per month per W12/W1627'
 with 'PHP 60–100M in annual losses' derived from the retired 2,800–4,500/month
 fraud universe; trued to the ~1,200 canon with ~PHP 3–6M/yr at 720–1,140
 fraudulent returns × ~PHP 3,500–5,000 avg) and W1336 step 1(f)'s '>5% of
 transactions (~2.5x the chain average)' — the retired ~2% basis; the chain canon
 is ~0.04%; (3) the AP business-day family review #60 left behind: #60 trued W7's
 staffing headline to 395–440 but W7's own Time Estimate still derived from the
 retired 305–370 band (~25–31 h scanning, '~70 invoices × 25 min' = ~25–30 h
 exceptions, total ~60–70 h) with its staffing tail still summing to '~53–67 h /
 ~5–6 hours each', and PA-22.1's copy of the band survived verbatim; all trued
 (scanning ~33–37 h, exceptions ~33–37 h at 79–88 invoices, total ~68–76 h,
 10 clerks ~7 h each). Guard: calibrated_volume_hits gains the seventy-second-wave
 arms — the hyphenated form, the 56,000-dispositions/monthly-returns/
 product-returns forms, the consolidation-mechanic form, the refurb-pool and
 W1336 forms, and the 305–370 band with its derived hour cells banned; the
 corrected anchors required at the repaired cells. Teeth: four synthetic
 injections through the FULL audit, each caught at its exact arm with file and
 line named, fixtures restored sha256-verified byte-identical, clean tree silent
 at 0 hits.

2026-09-23 directed cadence-ladder fix (virtual-gemba-walk.py, by direction:
implement the recommended permanent fix from the post-calibration gemba/time-
and-motion re-run): the production-volume calibration minted compound
Frequency forms of the shape 'chain-wide N–M per period (n–m per store per
period)' (6 cells corpus-wide, e.g. PA-56.2's W2201), and the time-and-motion
tool's rule-1/rule-2 phrase bridges crossed the parenthesis, multiplying the
chain-wide count by the store scale — W2201 read 21.84M events/yr (840x its
true ~26,000; the two clauses agree arithmetically, the parser did not), and
the re-run's receiving-clerk ×12.9 / store-manager ×2 demand jumps were this
artifact, not workload (corrected: receiving clerk 101% → 102%, hot/cold
membership unchanged pre/post calibration — the calibration itself
demand-neutral). Guard: gap_fill_straggler_hits gains the cadence-ladder arm
— the paren-crossing bridge class banned in the tool source, the
paren-blocked class required exactly 4× (ladder rules 1–2), and the docstring
measurement-assumption bullet pinned. Teeth: synthetic injection re-minting
the retired bridge caught at the arm, fixture restored sha256-verified
byte-identical, clean audit silent at 0 hits.

2026-09-23 seventy-fifth-wave consistency review: the A6.6 Atlassian incorporation's
own completeness (the incorporation pass, assumptions v4, had named the four suite
products but stopped there). (1) Atlassian Guard — the suite's centralized identity
plane (SAML SSO, enforced MFA, SCIM provisioning, organization audit logs) that
guardrails 5 and 7 already assumed — was never named; added to the A6.6 row, the
Design-Decisions row and guardrails 5/7 (assumptions bumped v5). (2) Guardrails 2/4
phrased 'every production change'/'only path to production' universally over an estate
(EBS) whose path to production is ADOP online patching (customization-governance §6,
the W495 monthly train), not Bitbucket Pipelines; scoped to the built-product estate
with the EBS chain named, and Bitbucket branch permissions (no direct pushes; the
reviewer rule as a merge check) pinned. (3) The two EBS-adjacent flows the workflows
assert joined the canonical integration matrix (data-volumes §3 v4.8: rows 21–22 — the
W616.1 → Jira Software enhancement-request sync and the Atlassian Guard → SIEM audit-
log stream) with the EBS pattern register mirroring one-for-one (02-oracle-ebs
integrations.md v1.3; integration_mirror_hits checks endpoint order, this rule pins
row content). (4) The sourcing model's §8 vendor-commodity estate named the suite
(v3.9) with §12.2's 'sole vendor product line' parenthetical trued to 'in capability
sourcing' (OM companion v3.19; headcount banner pin re-pointed). (5) The A6.6 Source
cell completed to all 16 PA-27.1 workflows (W495/W5521 joined). Guard:
atlassian_suite_hits joins the guard — anchors required at every repaired surface,
the retired universal-chain/Guard-less-SIEM forms banned doc-scoped on the assumptions
doc, and the incorporation pass's retired hedges ('Jira/ServiceNow', 'TestRail',
'(Confluence, SharePoint, or ITSM built-in KB)') banned repo-wide across the authored
trees (the methodology-index row exempt where it quotes the literals in its own guard
description — the Check-46/wave-9 convention). The rule's first live run caught the
methodology-index OM row still at v3.18 pre-ship.

2026-09-23 seventy-sixth-wave consistency review: domain_companion_hits joins the
guard — the batch-30 (W5580, 5,432 → 5,433) census stragglers on the surfaces no
arm read: the value-stream-index H1 banner and closing Total footer (both
maintained live at batch 26, both stranded at 5,432), the conformance canon's own
§1 framing sentence (canon bumped v1.5, guard DOC anchor re-pointed), the IT
domain companion's Technology-&-Data roster (393 → 394 / VS-113 (31) → (32) —
Check 76's own class one derivation step outside its four quoted cells), and the
retired 6,762 employee canon on the IT/operations/people companions' §1 scope
lines and evidence cells (the twenty-ninth-wave headcount sweep never opened
these four navigation surfaces). Retired forms banned doc-scoped, the corrected
anchors required at the repaired cells — the Check-71 CENSUS-pin contract.
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


import argparse, glob, os, re, subprocess, sys, tempfile

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
        "../02-oracle-ebs/data-migration.md",
        # 2026-09-17 fifty-third-wave consistency review: the licensing BOM joins
        # the doc set — it shipped with the fifty-second-wave session but was left
        # untracked, unmapped and unintegrated (the nineteenth-wave 'entire files'
        # class one layer out: a folder document no check read). Generic sweeps
        # verified clean on dry-run; the guard gains the licensing_bom_hits
        # structural rule (every scenario total re-derived from the doc's own
        # line items, per the dv_volume_hits arithmetic precedent).
        "../02-oracle-ebs/licensing-bom.md",
        "../02-oracle-ebs/ebs-vision-verification.md",
        # 2026-09-18 fifty-fifth-wave consistency review: the cross-repo
        # quote-coverage review joins the doc set — it shipped mapped but unguarded
        # (the licensing_bom_hits precedent), and its quoted RFQ figures had already
        # drifted once against the RFQ's own v2.0.1/v2.0.2 revisions. The guard
        # gains the quote_coverage_hits structural rule (register skeletons + the
        # canon/anchors + the supersession note).
        "../02-oracle-ebs/quote-coverage-review.md",
        # 2026-09-21 oratest capability verification: the CitiHardware R12.2.4
        # PROD-clone rig becomes the second installation of record and the
        # capability of record for 'what can be executed today' — the doc ships
        # with its own structural rule (oratest_hits) re-deriving the section
        # skeleton, the 39-row FP x rig re-map, the 10-row VT x rig matrix and
        # its GREEN/PARTIAL tally, the OR findings register and the rig-marker
        # anchors, per the vision_verification_hits precedent.
        "../02-oracle-ebs/ebs-oratest-verification.md",
        # 2026-09-21: the inward-direction reconciliation of the official R12.2
        # documentation library (ebs_docs/) against this model joins the doc set at
        # issue, not a wave later -- the licensing_bom/oratest precedent.
        "../02-oracle-ebs/ebs-documentation-coverage.md"]
RETIRED_FIGURES = ["6,757", "6,715", "5,357", "5,362", "5,349", "5,341",
                   "80,000 SKU", "1,000 POS terminal"]

# 2026-09-07 eighth-wave review — per-doc retired-figure exemptions. In
# data-volumes-and-integrations.md the literal 6,715 is the canonical AP
# merchandise-invoice count (~6,715/month, 3-way match per W7 — profile §10.2/§15.1),
# not the retired 6,715 HQ headcount total: the one surface where the digits
# legitimately recur.
RETIRED_FIGURE_EXEMPT = {"data-volumes-and-integrations.md": {"6,715"},
                         # 2026-09-22: the BOM's 22%-support derivation states $10,716,715
                         # (48,712,340 × 0.22 = 10,716,714.8) — the retired 6,715 HQ-headcount
                         # literal occurs only as an incidental substring of that larger
                         # figure (the data-volumes precedent, where 6,715 is the canonical
                         # AP merchandise-invoice count). A standalone 6,715 in the BOM
                         # remains impossible by construction (all cells are 6-7 figure sums).
                         "licensing-bom.md": {"6,715"}}

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
        # the subtotals re-foot to 4,935 + 492 and the total to 5,427; the
        # 2026-09-21 batch-25 re-pin: W5575-W5577 (PA-113.1, VS-113 -> CIO Office)
        # true CIO 81 -> 84, so the subtotals re-foot to 4,935 + 495 and the total
        # to 5,430.
        "**4,937 + 496 = 5,433**",
        # §3.2 portfolio-table subtotal/total rows (structurally re-derived from the
        # §4 mapping + disk by om_reconciliation_hits — these pin the corrected forms'
        # presence)
        "**171** | **4,937**",
        "**17** | **496**",
        "**188** | **5,433**",
        # v2.0 hybrid sizing anchor (66 domain + platform/CIO = 115 FTE); v2.1 agentic
        # re-bases it to 122 (66 + 56, AAP +7)
        "**66 + 56 = 122**",
    ],
    "optimal-table-of-organization.md": [
        "Outbound (50)",
        "**532** | **6,932**",
        "**Total HQ** | **362** | **~440–515** | **532**",
        "**518 + 7 = 525**",
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
        "6 rows are new scope the doctrine creates",
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
    rows present and cross-footing (6,762 = 362 + 5,800 + 600; 6,932 = 532 + 5,800 + 600);
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
    if sum(tgt) != 532:
        hits.append((rel, 0, f"§5.1 target column sums to {sum(tgt)}, canonical 532 (re-based 2026-09-18 actual-org gap-fill; the 2026-09-14 promotion figure was 511)"))

    def total_row(label):
        m = re.search(rf"^\|\s*\|\s*\*\*{label}\*\*\s*\|\s*\*\*([\d,]+)\*\*\s*\|[^|]*\|\s*\*\*([\d,]+)\*\*\s*\|",
                      s51, re.M)
        if not m:
            hits.append((rel, 0, f"§5.1 '{label}' total row not found"))
            return None
        return (int(m.group(1).replace(",", "")), int(m.group(2).replace(",", "")))

    hq = total_row("Total HQ")
    if hq and hq != (362, 532):
        hits.append((rel, 0, f"§5.1 Total HQ row reads {hq}, canonical (362, 532)"))
    comp = total_row("Total company")
    if comp and comp != (6762, 6932):
        hits.append((rel, 0, f"§5.1 Total company row reads {comp}, canonical (6,762, 6,932)"))
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
                         'two-state anchors are 362/6,762 → 532/6,932)'))
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
          re-derived tier ladder; and, since the 2026-09-16 forty-third-wave
          consistency review, (f) every README document-map row is paren-balanced
          (the eighth pass's append to the fit-gap row shipped a doubled
          close-paren — the doubled-join genre on the document the forty-first
          wave's fit-gap-scoped join-hygiene arm did not read); and, since the
          2026-09-21 sixty-first-wave consistency review, (g) the two README
          navigation rows quoting the fit-gap register — the root-README tree row
          and this document map's fit-gap row — carry the §2-re-derived register
          total and, on the root row, the standard-total class cell, with the
          retired 97/74 forms forbidden (batch 26's cascade re-pointed both
          READMEs' workflow-count surfaces but stranded the fit-gap counts on the
          two rows no check read at register-count grain); and, since the
          2026-09-21 sixty-first-wave manuals sweep, (h) the two disposition
          POS rows (fit-gap D6, coverage-map POS/Retail) carry the checkout
          qualifier ('No EBS POS checkout product') — the library's POS-named
          Channel Rebate & POS guides make the bare absence form false — and
          the retired bare 'No EBS POS exists' form is banned on both; and,
          since the 2026-09-22 sixty-fifth-wave review, (j) data-migration's
          §2 W0 sequence-tree line names the platform of record (the VF-2
          re-point stranded 'into ICM (24)' one section below its own re-pointed
          row 24; the retired form banned, the corrected anchor required); and,
          since the 2026-09-23 sixty-ninth-wave review, (k) the §4-resolution-37
          entitlement flags ride their own disposition rows — the Asset-Tracking
          `L11496` flag (a §4-resolution-37/GPL-sweep paste-family misdirection)
          sat on the D6 POS row, whose in-house-checkout disposition it has no
          bearing on, while F7 (the Asset-Tracking row whose own note the flag
          qualifies) carried none, contradicting resolution 37's own 'carried on
          the F7/B10 note cells' record: the entitlement-flag/L11496 forms are
          banned on the D6 row and the flag anchor required on the F7 row."""
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
    # 2026-09-16 second-pass EBS-exhaustion audit: register 83 → 90 rows — A11
    # re-dispositioned EXT → FIT-CFG (Revenue Management and Invoicing found
    # in-suite; the planned PFRS 15 build retired through its de-customization
    # trigger) and seven native vehicles added (F5 eAM, B12 Procurement
    # Contracts, D15 Global Order Promising, C16 Configurator in-store, C15
    # In-Memory Cost Management, F6 GL budgets + budgetary control, G9 Oracle
    # Alert); EXT 2 → 1, BUILD unchanged at 14. The pins below re-based to the
    # re-derived arithmetic (67 standard = 74.4% of 90).
    # 2026-09-16 third-pass EBS-exhaustion audit: register 90 → 96 rows — six
    # native vehicles adopted where the workflows invoked capabilities without
    # naming them (A14 AR Lockbox + Balance Forward Billing + iReceivables,
    # B13 Purchasing Contingent Labor, C17 Engineering ECO/ECN, D16 Install
    # Base + Service Contracts, D17 Depot Repair, E10 Compensation Workbench)
    # plus five realization-note trues (A3 Bills Receivable, A13 rental family,
    # C1 Product Hub, C3 Site Hub, H6 GoldenGate); BUILD unchanged at 14.
    # Pins re-based to the re-derived arithmetic (73 standard = 76.0% of 96).
    # 2026-09-16 sixth-pass EBS-exhaustion audit: register 96 → 97 rows — H11
    # Oracle Internal Controls Manager adopted as the VS-21 audit-management/GRC
    # surface (the workflows' 'Audit Management portal / GRC Tool' touchpoints
    # named the suite's own GRC module); H8's environment lifecycle trued to
    # Rapid Clone + Oracle iSetup. Pins re-based to the re-derived arithmetic
    # (74 standard = 76.3% of 97). 2026-09-21 batch-26 re-base: the
    # ebs-documentation-coverage register closed its six highest-confidence
    # rows as H12-H17 (Price Protection, Environmental Accounting & Reporting,
    # Incentive Compensation, Bill Presentment Architecture, E-Business Tax
    # Reporting, Copy Inventory Organization) -- register 97 -> 103 rows,
    # FIT-STD/FIT-CFG 37 -> 40 each, 80 standard = 77.7% of 103.
    # 2026-09-21 batch-27 re-base: the coverage register's remaining 19 rows
    # dispositioned (fit-gap §4 resolution 35) -- six native vehicles adopted
    # (B14 e-Commerce Gateway, D18 Sales Contracts, D19 Knowledge Management,
    # D20 Customer Data Librarian + Customers Online, F7 Asset Tracking +
    # iAssets, H18 Report Manager) and six realization trues (A10/B10/C5/C10/
    # D14/H5) -- register 103 -> 109 rows, FIT-STD 40 -> 44, FIT-CFG 40 -> 42,
    # 86 standard = 78.9% of 109.
    # 2026-09-22 Vision-findings re-disposition (fit-gap §4 resolution 36):
    # VF-2 -- H11 Oracle Internal Controls Manager re-dispositioned FIT-CFG ->
    # BUILD (AMW registered '(Obsolete)', no installation record on either
    # installation of record); VF-1 -- A11's vehicle naming trued to
    # Receivables Revenue Management (in-suite AR). Register stays 109 rows;
    # FIT-CFG 42 -> 41, BUILD 14 -> 15, 85 standard = 78.0% of 109.
    expect = {"FIT-STD": 44, "FIT-CFG": 41, "PER": 2, "EXT": 1, "LOC": 1,
              "INT": 5, "BUILD": 15, "EDGE": 0, "OPEN": 0}
    for cls, want in expect.items():
        got = counts.get(cls, 0)
        if got != want:
            add("fit-gap-analysis.md", 0,
                f"register re-derives {got} {cls} rows but §3 pins {want} — the "
                f"class-count table no longer foots against the §2 register")
    if total != 109:
        add("fit-gap-analysis.md", 0,
            f"register re-derives {total} disposition rows but the pinned register "
            f"total is 109")
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

    # ---- (a.2) register-note join hygiene — the 2026-09-16 forty-first-wave
    # consistency review: the seventh pass appended its eleven register-row
    # clauses and the intro's seventh-pass sentence without their join
    # punctuation — eight register notes read '…feeds The 2026-09-16…'-style
    # unseparated runs and the intro carried a ').;' doubled join against the
    # '; and the' segment convention — and the B13 note's PA-98.2 file
    # reference sat lowercase ('pa-98.2'). The general rule: an appended audit
    # clause must be sentence- or semicolon-separated (a lowercase letter or
    # digit directly followed by ' The <date>' can only be a missing
    # separator — the forty-fifth-wave review widened the arm after the
    # eighth pass's F3/F5 appends dodged it with digit-ended joins, 'A12 The'
    # and 'C14 The'); the ').;' join and the lowercase file reference are
    # retired per document; the corrected anchor is required.
    for jm in re.finditer(r"[a-z0-9] The 2026-", fg_body):
        ctx = fg_body[max(0, jm.start() - 40):jm.end() + 30]
        add("fit-gap-analysis.md", 0,
            f"register/intro prose carries an appended audit clause with its join "
            f"punctuation missing (…{ctx}… — appended pass clauses must be "
            f"sentence- or semicolon-separated)")
    if ").;" in fg_body:
        add("fit-gap-analysis.md", 0,
            "intro carries a ').;' doubled sentence join (the segment convention "
            "is '); and the' — no period before the joining semicolon)")
    if "pa-98.2" in fg_body:
        add("fit-gap-analysis.md", 0,
            "register note carries the lowercase 'pa-98.2' file reference (the "
            "canon form is 'PA-98.2')")
    if "PA-98.2 ST row names it" not in fg_body:
        add("fit-gap-analysis.md", 0,
            "required corrected anchor 'PA-98.2 ST row names it' not found in the "
            "B13 register note")

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

    # ---- (f) README document-map rows are paren-balanced — 2026-09-16
    # forty-third-wave consistency review: the eighth pass's append to the fit-gap
    # document-map row shipped its segment-final parenthetical double-closed
    # ('§4 resolution 32))') against the row's own balanced-nesting convention — the
    # same doubled-join genre the forty-first wave retired in the fit-gap intro, on
    # the sibling document the join-hygiene arm's fit-gap scope did not read. Every
    # document-map row must carry balanced parentheses so a future append that
    # drifts the row's paren nesting fires here.
    for ln_i, ln in enumerate(rd.splitlines(), 1):
        if ln.startswith("| [`") and ln.count("(") != ln.count(")"):
            add("README.md (02-oracle-ebs)", ln_i,
                f"document-map row is not paren-balanced "
                f"({ln.count('(')} open / {ln.count(')')} close) — appended clauses "
                f"must preserve the row's nesting (forty-third-wave arm)")

    # ---- (g) the two README navigation rows quoting the fit-gap register carry
    # the re-derived register counts — 2026-09-21 sixty-first-wave consistency
    # review: batch 26's re-point cascade moved the root-README's workflow-count
    # rows and this README's Tier-2 census line but stranded the fit-gap counts
    # on both READMEs' own rows — the root tree row read '97-row capability
    # disposition register (74 standard ...' and the document-map row read 'the
    # capability disposition register (97 rows incl.' against the register's 103
    # (80 standard): no check read either row at register-count grain (Check 70
    # pins the five workflow-figure annotations; arm (f) pins this row's paren
    # balance, not its numbers). Rule: each row naming fit-gap-analysis.md and a
    # 'disposition register' must state the re-derived total ('{total}-row' /
    # '({total} rows') and, on the root tree row, the '({std} standard' class
    # cell; the retired 97/74 forms are banned on both.
    root_rd = strip_footer(open(os.path.join(REPO, "README.md"), encoding="utf-8").read())
    for row_doc, row_body in (("README.md (root)", root_rd),
                              ("README.md (02-oracle-ebs)", rd)):
        for ln_i, ln in enumerate(row_body.splitlines(), 1):
            if "fit-gap-analysis.md" not in ln or "disposition register" not in ln:
                continue
            for retired in ("97-row", "(97 rows", "(74 standard"):
                if retired in ln:
                    add(row_doc, ln_i,
                        f"fit-gap navigation row carries the retired '{retired}' "
                        f"form — the register-count cascade must reach the README "
                        f"tree/document-map rows (sixty-first-wave arm)")
            if f"{total}-row" not in ln and f"({total} rows" not in ln:
                add(row_doc, ln_i,
                    f"fit-gap navigation row does not state the re-derived register "
                    f"total ({total} rows)")
            if row_doc == "README.md (root)" and f"({std} standard" not in ln:
                add(row_doc, ln_i,
                    f"root-README fit-gap tree row does not state the re-derived "
                    f"standard total ({std} standard)")

    # ---- (h) the disposition POS rows carry the checkout qualifier — 2026-09-21
    # sixty-first-wave manuals sweep: the library ships a POS-named product
    # (Oracle Channel Rebate and Point-of-Sale Management, supplier-side,
    # recorded not-needed in the coverage register §5), so the bare 'No EBS POS
    # exists' form is false and retired on the two disposition surfaces; each
    # must state the checkout sense the D6 decision actually rests on.
    cm = strip_footer(open(ebs("module-coverage-map.md"), encoding="utf-8").read())
    for row_doc, txt, marker in (("fit-gap-analysis.md", fg_body, "| D6 |"),
                                 ("module-coverage-map.md", cm, "| **POS / Retail** |")):
        row_i = next((i for i, l in enumerate(txt.splitlines(), 1)
                      if l.startswith(marker)), 0)
        if not row_i:
            add(row_doc, 0, f"POS disposition row starting '{marker.strip()}' not found")
            continue
        row = txt.splitlines()[row_i - 1]
        if "No EBS POS checkout product" not in row:
            add(row_doc, row_i,
                "POS row does not carry the checkout qualifier ('No EBS POS checkout "
                "product') — the library's POS-named Channel Rebate & POS guides "
                "make the bare absence form false")
        if "No EBS POS exists" in row:
            add(row_doc, row_i,
                "retired bare 'No EBS POS exists' form is back on the POS row")
    # ---- (i) manuals-vocabulary arm — 2026-09-21 sixty-second-wave capability
    # sweep: two product-mechanics vocabularies the shipped R12.2 manuals do not
    # document were live on the realization surfaces. L&FM: 122oklug documents lease
    # contracts with rental periods, rent streams and evergreen rentals — 'rental
    # contract' as a construct name and 'reservations' appear zero times in it. AP
    # Bills Payable: 122apug's own phrase for the outstanding-instrument state is
    # 'issued but not matured' (the Future Dated Payments balance definition and the
    # Maturity Date Report) — 'issued-but-unreleased' is retired on the blueprint
    # realization surfaces (the two PA-file instances of the same class ride the
    # Check 46 workflow-corpus literal probe).
    vocab_docs = {
        "module-coverage-map.md": cm,
        "fit-gap-analysis.md": fg_body,
        "ebs-platform-architecture.md": strip_footer(open(
            ebs("ebs-platform-architecture.md"), encoding="utf-8").read()),
    }
    for row_doc, txt in vocab_docs.items():
        # fit-gap §4's resolution-record rows are dated records of what each pass
        # resolved — their own-date wording stands, the same adjudication as their
        # own-date counts (waves 31–34 keep '74 = 76.3%')
        scan_lines = [(i + 1, l) for i, l in enumerate(txt.splitlines(), 1)
                      if not (row_doc == "fit-gap-analysis.md"
                              and re.match(r"^\| \d+ \|", l))]
        for bad in ("rental contracts/reservations", "rental contracts & reservations",
                    "issued-but-unreleased"):
            hit_ln = next((ln for ln, l in scan_lines if bad in l), None)
            if hit_ln:
                add(row_doc, hit_ln,
                    f"retired manuals-vocabulary form '{bad}' (122oklug documents "
                    f"lease contracts with rental-period billing — rent streams and "
                    f"evergreen rentals; 122apug's phrase is 'issued but not matured')")
        if "issued-but-unmatured" not in txt:
            add(row_doc, 0,
                "missing AP Bills Payable manuals-vocabulary anchor "
                "'issued-but-unmatured'")
    if "evergreen rentals" not in cm:
        add("module-coverage-map.md", 0,
            "Services/Rental row must state the manual-documented L&FM mechanics "
            "(rental-period billing — rent streams and evergreen rentals)")
    # ---- (j) data-migration's §2 W0 sequence-tree line names the load target
    # of record — 2026-09-22 sixty-fifth-wave review: the VF-2 re-point (v1.7)
    # trued row 24's load target to the in-house Audit & GRC platform but
    # stranded the §2 'Sequence & Dependencies' tree one section below
    # ('the control register into ICM (24)') — the unguarded summary-surface
    # class the fifty-fifth wave swept.
    dm = strip_footer(open(ebs("data-migration.md"), encoding="utf-8").read())
    if "the control register into ICM (24)" in dm:
        add("data-migration.md", 0,
            "retired load target 'into ICM (24)' in the §2 sequence tree (row 24's "
            "target is the in-house Audit & GRC platform control-library load — "
            "Vision VF-2)")
    if "the control register into the Audit & GRC platform (24)" not in dm:
        add("data-migration.md", 0,
            "missing the corrected W0 sequence-tree anchor 'the control register "
            "into the Audit & GRC platform (24)'")
    # ---- (k) the §4-resolution-37 entitlement flags ride their own disposition
    # rows — 2026-09-23 sixty-ninth-wave review: the Asset-Tracking L11496 flag
    # was appended to the D6 POS row (a paste-family misdirection — D6's
    # in-house-checkout disposition has no Asset-Tracking bearing) while F7, the
    # Asset-Tracking row whose own 'rides the Install Base/Inventory bases (BOM
    # decision 6)' clause the flag qualifies, carried none — contradicting
    # resolution 37's own record ('carried on the F7/B10 note cells'). The flag
    # sentence moved D6 → F7 verbatim; this arm keeps it there.
    d6_i = next((i for i, l in enumerate(fg_body.splitlines(), 1)
                 if l.startswith("| D6 |")), 0)
    f7_i = next((i for i, l in enumerate(fg_body.splitlines(), 1)
                 if l.startswith("| F7 |")), 0)
    if not d6_i or not f7_i:
        add("fit-gap-analysis.md", 0,
            "disposition rows D6/F7 not found (register structure changed — "
            "re-point the flag-placement arm)")
    else:
        d6_row = fg_body.splitlines()[d6_i - 1]
        f7_row = fg_body.splitlines()[f7_i - 1]
        for bad in ("entitlement flag (2026-09-23", "L11496"):
            if bad in d6_row:
                add("fit-gap-analysis.md", d6_i,
                    f"retired form '{bad}' on the D6 POS row (the Asset-Tracking "
                    f"entitlement flag is misdirected here — its carrier is the "
                    f"F7 row, per §4 resolution 37's own F7/B10 record)")
        if "entitlement flag (2026-09-23, coverage register §7)" not in f7_row or \
                "L11496" not in f7_row:
            add("fit-gap-analysis.md", f7_i,
                "missing the Asset-Tracking entitlement-flag anchor on the F7 row "
                "('entitlement flag (2026-09-23, coverage register §7)' + L11496 "
                "— the §4-resolution-37 record declares the flags carried on the "
                "F7/B10 note cells)")
    return hits


def licensing_bom_hits():
    """2026-09-17 fifty-third-wave consistency review — structural guard for the
    02-oracle-ebs licensing BOM (the quantitative doc joined the DOCS set after
    shipping untracked and unintegrated; the dv_volume_hits precedent: the
    doc whose arithmetic no rule re-derives is the one that drifts). Re-derives
    every stated total from the doc's own line items on every run:
      (a) Scenario A: every 6-column line item's price × quantity must equal its
          license-$ cell, and every §2.8 Employee-metric HRMS row must equal
          list × 6,911; the line items must sum to the §2.10 perpetual total,
          with support (22%), 3-yr and 5-yr TCO following;
      (b) Scenario B1/B2: each option's monthly column must sum to its stated
          **Total**, and the stated /yr · 3-yr · 5-yr bold line must follow;
      (c) §4's comparison table must quote the re-derived totals at their
          stated rounding;
      (d) fifty-fourth-wave footing arm: the §2 build-up notes must carry their
          explicit footing clauses and §1's ecommerce driver its derived
          order-line basis (the unqualified/contradictory forms retired);
      (e) fifty-fifth-wave driver arm: the §1 Total-employees row's store/DC/HQ
          parenthetical must foot to its own leading figure;
      (f) sixtieth-wave Fusion employee-metric arm: in §3.1/§3.2 every
          Employee-metric quantity must equal the §1 canon, and the Suite
          Employee tier — the one cell that DERIVES the headcount rather than
          stating it — must equal canon − the professional tier and state that
          footing in prose (it had survived the 2026-09-18 literal re-base at
          3,311 = 6,911 − 3,600, arithmetically consistent with its own totals
          and therefore invisible to arms (a)–(c));
      (g) 2026-09-22 Component-GPL true-up arm: the in-repo price-list PDF
          (applications-price-list-070574.pdf, the September 10, 2026 EBS
          Component Global Price List) resolved every † placeholder on the EBS
          side — Scenario A must carry no 'TBD †' form (the Fusion † rows in
          §3.1/§3.2 stay; the Fusion Cloud GPL is not in-repo), the eight
          GPL-verified part numbers are required on the footer-stripped body,
          the register clause ('no Component-GPL SKU') is required, and the
          five no-SKU products (Credit Management, Oracle Quality, Engineering,
          Project Management, Environmental Accounting & Reporting) must stay
          recorded in the §2.11 custom-quote register; and, since the 2026-09-22
          sixty-fifth-wave review, (h) the Fusion Risk Management parity tags
          (B1 §3.1, the B2 add-on and the §3 parity note) are anchored on the
          H11 capability naming, not the retired ICM product name ('ICM
          parity'/'ICM eq.' banned on the footer-stripped body; the §1/§2.11
          dated change-record mentions exempt by form)."""
    rel = "licensing-bom.md"
    hits = []
    path = os.path.normpath(os.path.join(MC, "..", "02-oracle-ebs", rel))
    text = open(path, encoding="utf-8").read()

    def num(s):
        return float(s.replace(",", ""))

    def section(start_pat, end_pat):
        m1 = re.search(start_pat, text)
        if not m1:
            return None
        m2 = re.search(end_pat, text[m1.end():])
        return text[m1.end(): m1.end() + m2.start()] if m2 else text[m1.end():]

    def add(doc, ln, msg):
        hits.append((doc, ln, msg))

    # ---- (a) Scenario A line items → §2.10 stated totals
    stated = sup = t3 = t5 = None
    livetot = 0.0
    sec_a = section(r"## 2\. Scenario A", r"## 3\. Scenario B")
    if sec_a is None:
        hits.append((rel, 0, "Scenario A section not found"))
    else:
        total = 0.0
        for m in re.finditer(
                r"\| ([^|]+) \| ([^|]+) \| [^|]+ \| ([\d,]+(?:\.\d+)?) \| "
                r"([\d,]+)[^|]*\| ([\d,]+) \|", sec_a):
            name = m.group(1).strip()
            price, qty, lic = num(m.group(3)), int(num(m.group(4))), num(m.group(5))
            if abs(price * qty - lic) > 0.5:
                add(rel, text[:m.start()].count("\n") + 1,
                    f"Scenario A line item '{name}': {price} × {qty} != {lic}")
            total += lic
        for m in re.finditer(
                r"\| ([^|]+) \| ([A-Z][A-Z0-9]+) \| ([\d,]+) \| ([\d,]+) \|", sec_a):
            name = m.group(1).strip()
            if name.startswith("~~") or "Total" in name:
                continue
            price, lic = num(m.group(3)), num(m.group(4))
            if abs(price * 6925 - lic) > 0.5:
                add(rel, text[:m.start()].count("\n") + 1,
                    f"Employee-metric HRMS row '{name}': {price} × 6,925 != {lic}")
            total += lic
        stated = re.search(r"\*\*Perpetual license total\*\* \| \*\*\$([\d,]+)\*\*", sec_a)
        if not stated:
            hits.append((rel, 0, "§2.10 perpetual-license-total row not found"))
        elif abs(total - num(stated.group(1))) > 0.5:
            hits.append((rel, 0,
                         f"Scenario A line items sum to {total:,.0f} but §2.10 states "
                         f"{stated.group(1)}"))
        livetot = num(stated.group(1)) if stated else total
        sup = re.search(r"Annual SUL&S \(22%\) \| \$([\d,]+)/yr", sec_a)
        t3 = re.search(r"3-yr TCO \(license \+ 3× support\) \| \$([\d,]+)", sec_a)
        t5 = re.search(r"5-yr TCO \(license \+ 5× support\) \| \*\*\$([\d,]+)\*\*", sec_a)
        for pat, name, want in ((sup, "support", livetot * 0.22),
                                (t3, "3-yr TCO", livetot * 1.66),
                                (t5, "5-yr TCO", livetot * 2.1)):
            if not pat:
                hits.append((rel, 0, f"§2.10 {name} row not found"))
            elif abs(num(pat.group(1)) - want) > 1.5:
                hits.append((rel, 0, f"§2.10 {name} states {pat.group(1)} but the "
                                     f"re-derivation is {want:,.0f}"))
        # 2026-09-21 sixty-second-wave tightening: once the support row parses, the
        # 3-yr/5-yr cells derive from the section's own stated components (license +
        # N × the STATED support, tolerance ±0.5) — the ×1.66/×2.1 approximations at
        # ±1.5 above had let the batch-26 restatement ship a 5-yr TCO of 102,504,244
        # whose own components give 102,504,245 (the approximation product 102,504,244.5
        # straddled both integers, so the tolerance ate the off-by-one).
        if sup:
            sup_v = num(sup.group(1))
            chain = [(t3, "3-yr TCO", livetot + 3 * sup_v, 0.5),
                     (t5, "5-yr TCO", livetot + 5 * sup_v, 0.5)]
        else:
            chain = [(t3, "3-yr TCO", livetot * 1.66, 1.5),
                     (t5, "5-yr TCO", livetot * 2.1, 1.5)]
        for pat, name, want, tol in chain:
            if not pat:
                hits.append((rel, 0, f"§2.10 {name} row not found"))
            elif abs(num(pat.group(1)) - want) > tol:
                hits.append((rel, 0, f"§2.10 {name} states {pat.group(1)} but the "
                                     f"re-derivation is {want:,.0f}"))

    # ---- (b) Scenario B1/B2 monthly columns → stated totals
    for opt, sec_pat, total_pat, bold_pat in (
            ("B1", r"### 3\.1 ", r"### 3\.2 ",
             r"\*\*B1 totals: \$([\d,]+)/yr · \$([\d,]+) \(3-yr\) · \$([\d,]+) \(5-yr\)\*\*"),
            ("B2", r"### 3\.2 ", r"## 4\.",
             r"\*\*B2 totals: \$([\d,]+)/yr · \$([\d,]+) \(3-yr\) · \$([\d,]+) \(5-yr\)\*\*")):
        sec = section(sec_pat + r"[^\n]*\n", total_pat)
        if sec is None:
            hits.append((rel, 0, f"Scenario {opt} section not found"))
            continue
        monthly = 0.0
        for m in re.finditer(
                r"\| ([^|]+) \| [^|]+ \| [^|]+ \| ([\d,]+(?:\.\d+)?) \| "
                r"([\d,]+)[^|]*\| ([\d,]+) \|", sec):
            name = m.group(1).strip()
            if name.startswith("**Total**"):
                continue
            price, qty, mo = num(m.group(2)), int(num(m.group(3))), num(m.group(4))
            if abs(price * qty - mo) > 0.5:
                add(rel, text[:m.start()].count("\n") + 1,
                    f"Scenario {opt} line item '{name}': {price} × {qty} != {mo}")
            monthly += mo
        stated = re.search(r"\*\*Total\*\* \|(?:[^|]*\|){4}\s*\*\*\$([\d,]+)/mo\*\*", sec)
        if not stated:
            hits.append((rel, 0, f"Scenario {opt} monthly-total row not found"))
        elif abs(monthly - num(stated.group(1))) > 0.5:
            hits.append((rel, 0,
                         f"Scenario {opt} line items sum to {monthly:,.0f}/mo but the "
                         f"stated total is {stated.group(1)}/mo"))
        bold = re.search(bold_pat, text)
        if not stated:
            continue
        mo = num(stated.group(1))
        if not bold:
            hits.append((rel, 0, f"Scenario {opt} bold totals line not found"))
        else:
            yr, t3v, t5v = (num(bold.group(i)) for i in (1, 2, 3))
            if abs(mo * 12 - yr) > 2 or abs(mo * 36 - t3v) > 3 or abs(mo * 60 - t5v) > 3:
                hits.append((rel, 0,
                             f"Scenario {opt} bold totals ({yr:,.0f}/yr, {t3v:,.0f}, "
                             f"{t5v:,.0f}) do not follow from the monthly total "
                             f"{mo:,.0f}"))

    # ---- (c) §4 comparison table at the stated cells' own rounding
    sec4 = text.split("## 4. Comparison", 1)[-1]

    def roundcmp(row_name, quoted, wants):
        if quoted is None:
            hits.append((rel, 0, f"§4 comparison row for scenario {row_name!r} not found"))
            return
        strs = re.findall(r"\$([\d.]+)M", quoted)
        if len(strs) != len(wants):
            hits.append((rel, 0,
                         f"§4 comparison row for {row_name!r} quotes {strs} — expected "
                         f"{len(wants)} figures (the re-derived cells)"))
            return
        for fs, w in zip(strs, wants):
            dec = len(fs.split(".")[1]) if "." in fs else 0
            if abs(float(fs) - round(w, dec)) > 0.005:
                hits.append((rel, 0,
                             f"§4 comparison row for {row_name!r} quotes ${fs}M — the "
                             f"re-derived cell is {w:,.4f}M (not equal at the quoted "
                             f"precision)"))

    if stated and sup and t3 and t5:
        roundcmp("A — EBS 12.2 perpetual",
                 next((l for l in sec4.splitlines() if "A — EBS 12.2 perpetual" in l), None),
                 (livetot / 1e6, num(sup.group(1)) / 1e6,
                  num(t3.group(1)) / 1e6, num(t5.group(1)) / 1e6))
    b1_bold = re.search(r"\*\*B1 totals: \$([\d,]+)/yr · \$([\d,]+) \(3-yr\) · \$([\d,]+) \(5-yr\)\*\*", text)
    b2_bold = re.search(r"\*\*B2 totals: \$([\d,]+)/yr · \$([\d,]+) \(3-yr\) · \$([\d,]+) \(5-yr\)\*\*", text)
    if b1_bold:
        roundcmp("B1 — Fusion Cloud",
                 next((l for l in sec4.splitlines() if "B1 — Fusion Cloud" in l), None),
                 (num(b1_bold.group(1)) / 1e6, num(b1_bold.group(2)) / 1e6,
                  num(b1_bold.group(3)) / 1e6))
    if b2_bold:
        roundcmp("B2 — Fusion Suite bundle",
                 next((l for l in sec4.splitlines() if "B2 — Fusion Suite bundle" in l), None),
                 (num(b2_bold.group(1)) / 1e6, num(b2_bold.group(2)) / 1e6,
                  num(b2_bold.group(3)) / 1e6))

    # ---- (d) fifty-fourth-wave footing arm — the explanatory build-up surfaces the
    # line-item re-derivations above cannot read: the §2 user build-up notes must
    # carry their explicit footing clauses (the document's own iExpenses 'rounded
    # to' convention — the fifty-fourth wave found the Financials note silently
    # 58 seats short of its 650 qty and the MSCA note silently 100 short of its
    # 2,700 qty with a DC figure contradicting the §1 driver), and §1's ecommerce
    # driver must keep stating the derived basis its order-line pricing rides
    # (~4.5 lines/order — no lines-per-order canon exists anywhere; the EOL and
    # Pooled-line quantities price off it). Anchors and retired forms are checked
    # against the footer-stripped body — the wave's own first draft satisfied the
    # anchors off its own change-note quoting them (the sixth-wave
    # anchor-satisfying-itself-off-history failure, caught by the synthetic
    # injection before shipping).
    body = strip_footer(text)
    for anc in ("= 597, rounded to 650",
                "= 2,650, rounded to 2,700",
                "~4.5 lines/order"):
        if anc not in body:
            hits.append((rel, 0, f'missing required footing anchor "{anc}"'))
    for lit in ("DC 550", "(≈2.3M OM order lines) |", "+ 511 HQ"):
        if lit in body:
            hits.append((rel, body[:body.index(lit)].count("\n") + 1,
                         f'retired unqualified build-up form "{lit}"'))

    # ---- (e) fifty-fifth-wave driver-row arm — the §1 Total-employees driver row
    # must carry its store/DC/HQ breakdown parenthetical and the breakdown must
    # foot to the row's own leading figure. The 2026-09-18 gap-fill re-based the
    # leading figure to 6,932 but left the parenthetical at the retired
    # '+ 511 HQ' — a 21-seat contradiction inside the one row every employee-
    # derived quantity prices off, invisible to the line-item arms above.
    m = re.search(r"\| Total employees \| \*\*([\d,]+)\*\* \(([\d,]+) store \+ ([\d,]+) DC \+ ([\d,]+) HQ\)",
                  body)
    if not m:
        hits.append((rel, 0, '§1 Total-employees driver row: breakdown form not found '
                             '(expected "**N** (S store + D DC + H HQ)")'))
    else:
        tot, store, dc, hq = (int(num(g)) for g in m.groups())
        if store + dc + hq != tot:
            hits.append((rel, 0, f"§1 driver breakdown {store} + {dc} + {hq} "
                                 f"!= stated total {tot}"))

    # ---- (f) sixtieth-wave Fusion employee-metric arm — the §2.8 HRMS rows are
    # anchored to the employee canon by arm (a) (list × 6,932), but nothing
    # anchored the Fusion side's employee-metric quantities, so a headcount
    # re-base that swept literals left the one DERIVED cell behind: §3.2's
    # 'Fusion Suite Employee (self-service tier)' quantity is the complement of
    # the professional tier, and it still read 3,311 = 6,911 − 3,600 under the
    # retired canon long after every literal 6,911 had become 6,932 — arithmetically
    # self-consistent with its own totals, so arms (a)–(c) could not see it
    # (the '+ 511 HQ' straggler of arm (e), one level further down).
    # Rule: in §3.1/§3.2 every Employee-metric row carries the §1 canon, except
    # the Suite Employee tier, which must equal canon − the Suite Professional
    # quantity and must state that footing in prose (the §2 build-up convention).
    canon = int(num(m.group(1))) if m else 6932
    for opt, sec_pat, end_pat in (("B1", r"### 3\.1 ", r"### 3\.2 "),
                                  ("B2", r"### 3\.2 ", r"### 3\.3 ")):
        sec = section(sec_pat + r"[^\n]*\n", end_pat)
        if sec is None:
            continue
        prof = None
        rows = []
        for mm in re.finditer(
                r"\| ([^|]+) \| [^|]+ \| ([^|]+) \| ([\d,]+(?:\.\d+)?) \| "
                r"([\d,]+)[^|]*\| ([\d,]+) \|", sec):
            name, metric, qty = mm.group(1).strip(), mm.group(2).strip(), int(num(mm.group(4)))
            if name.startswith("Fusion Suite Professional"):
                prof = qty
            rows.append((name, metric, qty, sec[:mm.start()].count("\n")))
        base = text[:text.index(sec)].count("\n") + 1 if sec in text else 0
        for name, metric, qty, off in rows:
            if "Employee" not in metric and "Comp. Individual" not in metric:
                continue
            if name.startswith("Fusion Suite Employee"):
                if prof is None:
                    hits.append((rel, base + off,
                                 f"Scenario {opt} Suite Employee tier present but the "
                                 f"Suite Professional row it complements was not found"))
                elif qty != canon - prof:
                    hits.append((rel, base + off,
                                 f"Scenario {opt} '{name}' quantity {qty:,} != the §1 "
                                 f"employee canon less the professional tier "
                                 f"({canon:,} − {prof:,} = {canon - prof:,}) — the derived "
                                 f"employee cell is stranded on a retired headcount"))
                continue
            if qty != canon:
                hits.append((rel, base + off,
                             f"Scenario {opt} Employee-metric row '{name}' quantity "
                             f"{qty:,} != the §1 employee canon {canon:,}"))
    fm = re.search(r"Suite Employee tier = the employee population outside the "
                   r"professional tier: ([\d,]+) − ([\d,]+) =\s*([\d,]+)", body)
    if not fm:
        hits.append((rel, 0, "§3.2 Suite Employee footing clause not found "
                             "(expected 'Suite Employee tier = the employee population "
                             "outside the professional tier: C − P = Q')"))
    else:
        fc, fp_, fq = (int(num(g)) for g in fm.groups())
        if fc != canon or fc - fp_ != fq:
            hits.append((rel, body[:fm.start()].count("\n") + 1,
                         f"§3.2 Suite Employee footing clause states {fc:,} − {fp_:,} = "
                         f"{fq:,} — does not foot against the §1 employee canon {canon:,}"))

    # ---- (g) 2026-09-22 Component-GPL true-up arm — the in-repo price list
    # (applications-price-list-070574.pdf, the September 10, 2026 EBS Component
    # Global Price List) resolved every † placeholder on the EBS side: §2 must
    # carry no 'TBD †' form (the Fusion † rows in §3.1/§3.2 stay — the Fusion
    # Cloud GPL is not in-repo), the eight GPL-verified part numbers are
    # required in their §2 line-table cell form ('| PN |' — a prose mention
    # alone no longer satisfies the anchor), the register clause is required
    # and the five no-SKU products must stay recorded in §2.11's custom-quote
    # register (the retired placeholder lines banned with their section).
    if sec_a is not None:
        base_off = text.index(sec_a)
        for mm in re.finditer(r"TBD †", sec_a):
            add(rel, text[:base_off + mm.start()].count("\n") + 1,
                "Scenario A still carries a 'TBD †' placeholder line — the 2026-09-22 "
                "GPL true-up verified every EBS-side line against the in-repo "
                "Component GPL (the † rows belong to Fusion §3.1/§3.2 only)")
        for anc in ("| L72200 |", "| A92469 |", "| A81412 |", "| L98184 |", "| L10090 |",
                    "| A85655 |", "| L42119 |", "| A80531 |"):
            if anc not in body:
                hits.append((rel, 0,
                             f'missing GPL-verified part-number anchor "{anc}" — the '
                             f'2026-09-22 true-up pinned every EBS-side part number to '
                             f'the in-repo Component GPL'))
        if "no Component-GPL SKU** to the same register" not in body:
            hits.append((rel, 0,
                         'missing the custom-quote register clause ("no Component-GPL '
                         'SKU** to the same register") — the no-SKU record is required'))
        for prod in ("Credit Management", "Oracle Quality", "Engineering",
                     "Project Management", "Environmental Accounting & Reporting"):
            if prod not in body:
                hits.append((rel, 0,
                             f'"{prod}" vanished from the BOM — the five no-SKU products '
                             f'must stay recorded in §2.11\'s custom-quote register'))
    # ---- (h) the Fusion parity tags' retired ICM anchor — 2026-09-22
    # sixty-fifth-wave review: the VF-2 re-disposition retired ICM/AMW as a
    # vehicle, and the same-day VF-1 pass had already re-worded the sibling
    # Fusion Revenue Management tag to its surviving vehicle — but the two
    # Fusion Risk Management line tags (B1 §3.1 and the B2 add-on) and the §3
    # parity note still anchored on the retired product name. The §1 decision-5
    # note and the §2.11 delta note keep their own-date ICM mentions as dated
    # change-records — the banned forms are the parity-anchor idioms only.
    for bad in ("ICM parity", "ICM eq."):
        if bad in body:
            hits.append((rel, body[:body.index(bad)].count("\n") + 1,
                         f"retired Fusion parity anchor '{bad}' (the H11 vehicle of "
                         f"record is the in-house Audit & GRC platform per Vision "
                         f"VF-2 — anchor the tags on the H11 capability)"))
    for anc in ("the H11 audit/GRC surface's Fusion-side equivalent",
                "Fusion Risk Management add-on (the H11 audit/GRC eq.)"):
        if anc not in body:
            hits.append((rel, 0, f'missing the H11-anchored Fusion tag "{anc}"'))
    return hits


def vision_verification_hits():
    """2026-09-17 fifty-fourth-wave consistency review — structural guard for the
    live EBS Vision instance verification report (02-oracle-ebs/ebs-vision-verification.md;
    the licensing_bom_hits precedent: a quantitative doc joins the DOCS set with a rule
    that re-derives its own stated counts). Re-derives, every run:
      (a) the section skeleton (environment / FP footprint / VT transactional / VF
          findings / artifacts) must be complete;
      (b) the FP table must hold exactly the pinned 39 conformance rows (unique ids)
          and the VT table exactly 10 test rows (v2.0 round-2 extension: 5 → 10);
      (c) the §2 tally sentence must equal the count of FP rows whose verdict cell
          begins CONFIRMED (the licensing_bom_hits arithmetic rule's self-consistency
          principle applied to the doc's own verdict tally);
      (d) the required instance-evidence anchors must stay present (release 12.2.12,
          the AR 'Revenue Management Super User' responsibility evidence, the AMW
          '(Obsolete)' registry status, and the Order Import wrapper name)."""
    rel = "ebs-vision-verification.md"
    hits = []
    path = os.path.normpath(os.path.join(MC, "..", "02-oracle-ebs", rel))
    text = open(path, encoding="utf-8").read()
    body = strip_footer(text)
    for sec in ("## 1. Environment of record", "## 2. Footprint conformance (FP rows)",
                "## 3. Transactional verification (VT rows)", "## 4. Findings (VF)",
                "## 5. Verification artifacts"):
        if sec not in body:
            hits.append((rel, 0, f"missing section '{sec}'"))
    fp = re.findall(r"^\| (FP-\d+) ", body, flags=re.M)
    vt = re.findall(r"^\| (VT-\d+) ", body, flags=re.M)
    if len(fp) != 39 or len(set(fp)) != len(fp):
        hits.append((rel, 0, f"FP table holds {len(fp)} rows "
                             f"({len(set(fp))} unique) but the doc pins 39 unique rows"))
    if len(vt) != 10:
        hits.append((rel, 0, f"VT table holds {len(vt)} rows but the doc pins 10"))
    confirmed = len(re.findall(r"^\| FP-\d+ \|.*\| CONFIRMED", body, flags=re.M))
    m = re.search(r"Tally: \*\*(\d+) of the 39 FP rows CONFIRMED", body)
    if not m:
        hits.append((rel, 0, "§2 tally sentence ('Tally: **N of the 39 FP rows "
                             "CONFIRMED ...**') not found"))
    elif int(m.group(1)) != confirmed:
        hits.append((rel, 0, f"§2 tally claims {m.group(1)} CONFIRMED rows but the "
                             f"FP table holds {confirmed}"))
    for anc in ("12.2.12", "'Revenue Management Super User'",
                "marked **(Obsolete)**", "ORDER_IMPORT_CONC_PGM"):
        if anc not in body:
            hits.append((rel, 0, f'missing required verification anchor "{anc}"'))
    for vf in range(1, 7):
        if f"VF-{vf}" not in body:
            hits.append((rel, 0, f"missing finding VF-{vf}"))
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


def gap_fill_straggler_hits():
    """2026-09-18 fifty-fifth-wave consistency review — the actual-org gap-fill's
    own live-surface stragglers, the class its 294-replacement corpus sweep
    missed: (a) the classification register's live table cells — the W10
    Payroll-Processing 'Operational Significance' cell still carried the retired
    6,911 employee total after the sweep (the file's dated batch-note blockquotes
    and version footer are the frozen-history surfaces and stay exempt); (b) the
    official TO's §1 design stance — still reading 'lands at HQ 511' two lines
    under a states table the gap-fill had re-pointed (the promoted-structure
    rationale the gap-fill superseded; no rule read the stance prose); and
    (c) 2026-09-21 sixtieth-wave — the requirement register, whose own v24.2
    footer names seven employee/user-count rows but whose sweep re-based only
    two of them, leaving five live rows at 6,911 beside two siblings at 6,932."""
    hits = []
    # (a) classification register — live (non-blockquote, pre-footer) lines only
    cpath = os.path.join(REPO, "01-model-company", "workflows",
                         "workflow-criticality-classification.md")
    lines = open(cpath, encoding="utf-8").read().split("\n")
    fi = next((i for i, l in enumerate(lines)
               if l.startswith("*Document Version:") or l.startswith("*Date:")),
              len(lines))
    for i, l in enumerate(lines[:fi]):
        if l.startswith(">"):
            continue
        if "6,911" in l:
            hits.append(("workflow-criticality-classification.md", i + 1,
                         'retired 6,911 employee total on a live line (the dated '
                         'batch-note blockquotes are the frozen-history surfaces)'))
    if not any("6,925 employees" in l for l in lines[:fi]):
        hits.append(("workflow-criticality-classification.md", 0,
                     'missing live "6,925 employees" W10 significance cell'))
    # (b) TO §1 design stance — footer-stripped body
    tpath = os.path.join(REPO, "01-model-company", "optimal-table-of-organization.md")
    tbody = open(tpath, encoding="utf-8").read().split("*Document Version:")[0]
    if "lands at **HQ 511**" in tbody:
        hits.append(("optimal-table-of-organization.md",
                     tbody[:tbody.index("lands at **HQ 511**")].count("\n") + 1,
                     'retired §1 design stance "lands at **HQ 511**" (the 2026-09-18 '
                     'gap-fill raised the promoted 511 to HQ 532)'))
    if "raised it to **HQ 532**" not in tbody:
        hits.append(("optimal-table-of-organization.md", 0,
                     'missing §1 design-stance gap-fill anchor "raised it to **HQ 532**"'))
    # (c) 2026-09-21 sixtieth-wave arm — the requirement register. Its own v24.2
    # footer names SEVEN rows as the employee/user-count family, but the gap-fill
    # sweep re-based only two of them (MDM-011, HR-036), leaving five live
    # requirement rows (HR-039, HSE-004, HR-041, HR-045, NFR-041) stating 6,911
    # employees beside two siblings stating 6,932 — one register, two headcounts.
    # Rule: no retired 6,911 anywhere in the live body, and all seven declared
    # rows carry the canon.
    # (the register interleaves per-round '*Document Version:' footers mid-file,
    # so the frozen-history surface is those lines themselves, not a tail slice)
    rpath = os.path.join(REPO, "01-model-company", "erp-requirements.md")
    rlines = open(rpath, encoding="utf-8").read().split("\n")
    live = [(i + 1, l) for i, l in enumerate(rlines)
            if not l.startswith("*Document Version:")]
    for ln, l in live:
        if "6,911" in l:
            hits.append(("erp-requirements.md", ln,
                         'retired 6,911 employee/user total on a live requirement row '
                         '(the version-footer lines are the frozen-history surface)'))
    for rid in ("MDM-011", "HR-036", "HR-039", "HSE-004", "HR-041", "HR-045", "NFR-041"):
        row = next(((ln, l) for ln, l in live if l.startswith(f"| {rid} |")), None)
        if row is None:
            hits.append(("erp-requirements.md", 0,
                         f"employee-count requirement row {rid} not found"))
        elif "6,925" not in row[1]:
            hits.append(("erp-requirements.md", row[0],
                         f"requirement row {rid} is in the v24.2-declared "
                         f"employee/user-count family but does not carry the 6,925 canon"))
    # (d) 2026-09-21 sixty-second-wave arm — the live workflow-census canon. Batch 26
    # moved the corpus 5,430 → 5,432 and its cascade trued each document's headline
    # figures, but the present-tense count cells no rule read at that grain kept the
    # retired totals: the fit-gap intro's two census mentions, the coverage register's
    # framing sentence, the blueprint README's §1/§5 corpus cells, the AI-first guide's
    # Law-2/D1 rows, the OM's §11 companion-artifacts quote, the methodology index's
    # two tool rows, the TO's §5.3 census parenthetical and the virtual-gemba population
    # pin (the tool exited 1 on every run). Rule: the retired totals (5,426/5,427/5,430)
    # are banned on the footer-stripped live bodies of the census documents, the current
    # canon is required at the repaired cells, the TO parenthetical must read
    # '5,432 of 5,432 owner cells' across its wrapped lines, and the tool pin must equal
    # the corpus re-derivation. (When a future batch moves the canon, these anchors
    # re-fire until consciously re-pointed — the Check-71 CENSUS-pin contract.)
    census_docs = [
        "02-oracle-ebs/fit-gap-analysis.md",
        "02-oracle-ebs/ebs-documentation-coverage.md",
        "02-oracle-ebs/README.md",
        "02-oracle-ebs/module-coverage-map.md",
        "07-methodology/ai-first-operating-guide.md",
        "07-methodology/it-product-operating-model.md",
        "07-methodology/README.md",
        "01-model-company/optimal-table-of-organization.md",
    ]
    bodies = {}
    # contextual retired-count forms - bare historical integers in wave-narration
    # rows (the methodology index quotes each wave's then-canonical totals) stay legal
    retired_forms = [f"{bad} workflows" for bad in ("5,426", "5,427", "5,430")]
    retired_forms += [f"{bad}-workflow" for bad in ("5,426", "5,427", "5,430")]
    retired_forms += [f"{bad}-WF" for bad in ("5,426", "5,427", "5,430")]
    retired_forms += ["5,427 of 5,427", "5,426 of 5,426", "5,430 of 5,430"]
    for relp in census_docs:
        body = re.split(r"(?m)^\*Document Version:", open(
            os.path.join(REPO, relp), encoding="utf-8").read())[0]
        bodies[relp] = body
        for bad in retired_forms:
            if bad in body:
                hits.append((os.path.basename(relp), body[:body.index(bad)].count("\n") + 1,
                             f"retired workflow-census form '{bad}' on a live line (the "
                             f"canon is 5,433 workflows since batch 30; the version "
                             f"footers are the frozen-history surfaces)"))
    fit_b = bodies["02-oracle-ebs/fit-gap-analysis.md"]
    if "5,433 workflows demand" not in fit_b:
        hits.append(("fit-gap-analysis.md", 0,
                     'missing intro census anchor "5,433 workflows demand"'))
    if "5,433 workflows invoke without naming" not in fit_b:
        hits.append(("fit-gap-analysis.md", 0,
                     'missing intro census anchor "5,433 workflows invoke without naming"'))
    if ("Executed 2026-09-22 (the re-disposition pass" not in fit_b
            or "109 rows" not in fit_b):
        hits.append(("fit-gap-analysis.md", 0,
                     'missing §7 charter-note execution anchor (the charter note '
                     'must record the 2026-09-22 execution and the live register '
                     'state)'))
    if "5,433 workflows" not in bodies["02-oracle-ebs/ebs-documentation-coverage.md"]:
        hits.append(("ebs-documentation-coverage.md", 0,
                     'missing §1 framing census anchor "5,433 workflows"'))
    br_b = bodies["02-oracle-ebs/README.md"]
    for anchor in ("188 value streams · 5,433 workflows · 808 controls",
                   "workflows (5,433)"):
        if anchor not in br_b:
            hits.append(("README.md (02-oracle-ebs)", 0,
                         f'missing live corpus cell anchor "{anchor}"'))
    guide_b = bodies["07-methodology/ai-first-operating-guide.md"]
    for anchor in ("on all 5,433 workflows", "100% of 5,433 workflows"):
        if anchor not in guide_b:
            hits.append(("ai-first-operating-guide.md", 0,
                         f'missing guide census anchor "{anchor}"'))
    if "5,433-WF catalog" not in bodies["07-methodology/it-product-operating-model.md"]:
        hits.append(("it-product-operating-model.md", 0,
                     'missing §11 companion-artifacts census anchor "5,433-WF catalog"'))
    idx_b = bodies["07-methodology/README.md"]
    for anchor in ("5,433-workflow corpus", "Population-pinned (5,433 workflows"):
        if anchor not in idx_b:
            hits.append(("README.md (07-methodology)", 0,
                         f'missing tool-row census anchor "{anchor}"'))
    to_joined = " ".join(re.sub(r"(?m)^>\s?", "", bodies[
        "01-model-company/optimal-table-of-organization.md"]).split())
    if "5,433 of 5,433 owner cells resolved" not in to_joined:
        hits.append(("optimal-table-of-organization.md", 0,
                     '§5.3 census parenthetical must read "5,433 of 5,433 owner cells '
                     'resolved" across its wrapped lines (the retired form is '
                     '"5,427 of 5,427")'))
    vg = open(os.path.join(REPO, "07-methodology", "virtual-gemba-walk.py"),
              encoding="utf-8").read()
    if "CANON_WORKFLOWS = 5433" not in vg:
        hits.append(("virtual-gemba-walk.py", 0,
                     'population pin must read CANON_WORKFLOWS = 5433 (the tool '
                     'exits 1 on every run while it disagrees with the corpus)'))
    if "CANON_WORKFLOWS = 5432" in vg:
        hits.append(("virtual-gemba-walk.py", 0,
                     "retired population pin CANON_WORKFLOWS = 5432"))
    if "5,433 workflows" not in vg:
        hits.append(("virtual-gemba-walk.py", 0,
                     'docstring population line must state "5,432 workflows"'))
    # (e) 2026-09-23 directed cadence-ladder fix — the virtual-gemba frequency
    # bridges. The production-volume calibration minted compound Frequency
    # forms of the shape 'chain-wide N–M per period (n–m per store per
    # period)' (6 cells corpus-wide, e.g. PA-56.2's W2201), and the
    # time-and-motion tool's rule-1/rule-2 phrase bridges crossed the
    # parenthesis, multiplying the chain-wide count by the store scale —
    # W2201 read 21.84M events/yr (840x its true ~26,000; the two clauses
    # agree arithmetically, the parser did not), and the post-calibration
    # gemba/time-and-motion re-run's receiving-clerk x12.9 / store-manager x2
    # demand jumps were this artifact, not workload (corrected: receiving
    # clerk 101% -> 102%, hot/cold membership unchanged pre/post calibration).
    # Rule: the paren-crossing bridge class is banned in the tool source, the
    # paren-blocked class must appear exactly 4 times (ladder rules 1–2, the
    # dash-form and single-number alternatives), and the docstring
    # measurement-assumption bullet documenting the rule must stay.
    if "[^.;]*?per" in vg:
        hits.append(("virtual-gemba-walk.py", 0,
                     "retired paren-crossing frequency bridge class "
                     "'[^.;]*?per' (compound 'chain-wide (per-store)' "
                     "Frequencies parse 840x high across it — the bridge "
                     "must be paren-blocked)"))
    _nb = vg.count("[^.;()]*?per")
    if _nb != 4:
        hits.append(("virtual-gemba-walk.py", 0,
                     f"paren-blocked frequency bridge class '[^.;()]*?per' must "
                     f"appear exactly 4 times (found {_nb}) — ladder rules 1–2, "
                     f"dash-form + single-number alternatives"))
    if "bridges never cross parentheses" not in vg:
        hits.append(("virtual-gemba-walk.py", 0,
                     'missing docstring measurement-assumption anchor "bridges '
                     'never cross parentheses" (the paren-blocking rule must '
                     'stay documented where the cadence ladder is described)'))
    return hits


def calibrated_volume_hits():
    """2026-09-23 sixty-sixth-wave consistency review — the production-volume
    calibration's (data-volumes v4.7, cascade 2026-09-22) derived-surface
    stragglers: the §1.1 canon moved the replenishment row to 1,700/day
    (~50,000/month, ~250/store, on the measured STROO run-rate; physical
    deliveries deliberately unchanged at 2–3 drops/store/week, ~20–30 orders
    consolidated per drop, ~60–80 loads/day chain-wide) and the PO row to
    55–65/day at the production-measured ~7 lines/PO (~12,000 PO lines/month
    all types), the §1.2 storage rows to ~123 GB/year (~1,230 GB over 10
    years), while the volume-citing cells no rule read at that grain kept the
    retired figures: ~5,000 replenishment orders/month (25 live surfaces across
    21 PA files/READMEs and the classification register), the ~18,000 PO
    lines/month and ~15-lines-per-PO basis (6 surfaces incl. the TO's two
    sizing-basis cells and the profile's own §6.5 band against its restated
    §15.1), the ~100 GB/year and ~1,000 GB storage sizing (2), and the
    pre-ecommerce-canon ~10,000 home deliveries/month family (8; the W19 canon
    is 17,200/month = 573/day).

    2026-09-23 sixty-seventh-wave extension — the sibling-cell stragglers the (b) pass and
    the sixty-sixth-wave sweep both left inside the very files they repaired: W4's own
    Volume row + four staffing sentences (PA-05.1 — ~167/day, ~42/DC/day, ~50 lines/order,
    directly under a Frequency row the wave itself re-pointed), PA-04.2's other six
    volume-citing workflows (W1352 Frequency ~1,300+~115 against its own re-based Volume;
    W1353 ~33+~115; W1369 ~148; W1370 ~5,000/month against its own re-based Background;
    W836's 4×~10=~40 loads/day against its own ~1,800–2,400/month clause), PA-04.3's
    appointment/dock cells (30 outbound loads/DC/day = 120/day chain-wide against the
    60–80/day canon), W1256's Volume (~5,000 DC-to-store shipments against its own re-based
    Background), W277/W461's freight-billable family (~10,000–17,000 home deliveries;
    ~12,000–20,000 sum), W919's Background tail (~5,000+ monthly movements against its own
    repaired Frequency), W784's annual form (~60,000 orders/year), W1415's lines-per-drop
    (~500–800 SKUs/delivery) and PA-10.2's staffing sentence (~42 orders/day, ~50 lines).
    The load/drop canon these repairs state: one store-delivery load = one consolidated
    drop (2–3 drops/store/week → ~60–80 loads/day chain-wide = ~1,800–2,400/month =
    ~15–20/DC/day; 6–10 truck trips/DC/day at 2–3 drops/trip; W4 at ~1,700 orders/day
    chain-wide, ~3 lines/order → ~1,250 replenishment pick lines/DC/day).

    2026-09-23 sixty-eighth-wave extension — the calibration's own written-cell drift and
    the new canon rows' unread derived cells: W1352's Time Estimate (written by the
    calibration itself at ~5,300/~1,060/~265 chain-wide pick lines against the file's own
    ~1,250/DC/day Frequency anchor → ~5,000 chain-wide; hours re-footed ~7–14/~6–8/~13–21),
    W92's adjustment cells (PA-05.3 — ~1,700–2,600/month at 200×8–12 + 4×30–50 against the
    calibration's new §1.1 IAD row ~30/day ≈ ~900/month, measured 3,508–11,652/yr; re-based
    to 200×~3–5 + 4×~20–30 = ~680–1,120/month, ~1–2 h/store/month), W270's RTP cell
    (PA-04.3 — ~40 receipts/day/DC against PA-04.1's canon-citing ~50 ×4 cells + §1.1's
    200/day row; ~2.5 hours/day re-footed), W3962's Volume (PA-129.2 — the retired
    ~1,400–1,600 POs/month band the sixty-sixth wave retired on profile §6.5/TO/W2; trued
    to ~1,200 merchandise POs/month, all types ~1,600–1,900), PA-28.2's two remaining
    1,000 GB cells (W881 risk bullet + W1481 backup step) against its own ~1,230 GB anchor
    and A6.5/§1.2, and W109/W666's 20–50-lines-per-delivery cells (PA-07.3) against the
    60–90-line consolidated-drop canon (the form is "5,000 replenishment" narrowed to
    "5,000 replenishment orders" — the loose form fired on the corrected ~5,000
    replenishment pick lines/day anchor).

    2026-09-23 sixty-ninth-wave extension — the calibration straggler one layer further
    out: the root README's at-a-glance PO row (the one volume-citing surface neither the
    (b) cascade nor waves 66–68 swept — the README is outside the PA/README-glob and outside
    the versioned-doc list, and no check read the row at PO-band grain) still carried the
    retired ~1,400–1,600 total-PO band the sixty-sixth wave retired on profile §6.5/TO/W2
    and the sixty-eighth wave retired on W3962. Trued to the §15.1 canon; the retired
    '~1,400–1,600 total' form banned on the README and the calibrated anchor required (the
    loose '1,400–1,600' numeral pair is NOT banned repo-wide — PA-79.2's separated-employee
    cells legitimately use it).

    2026-09-23 seventieth-wave extension — the receipt/ASN/container sibling family, one
    derivation step out from the pinned cells: W3's Volume (PA-04.1 — '~15 lines per
    receipt' still carried the retired ~15-lines-per-PO basis the sixty-sixth wave retired
    on the PO surfaces; × the ~6,000 receipts/month canon it implied ~90,000 receipt
    lines/month against the ~12,000 PO-lines/month all-types canon — trued to ~2 lines per
    receipt, bulk POs arriving as multiple partial truck receipts), W3C's Volume (same
    file — '~20–30 import containers per DC per month' against W1271's own
    '~100–150 containers/DC/month' and W1169's '~20–30 per DC per week', both deriving
    from the ~400–600 TEUs/month §7.1 import canon at ~1 TEU/container; trued to
    ~100–150, PA-04.1-file-scoped banned — PA-01.1's per-seasonal-event forward-buy cells
    are a different, legitimate population), W1365's ASN universe (same file —
    '~4,800 ASN submissions/month' was 80% × the 6,000-receipt canon, but 1 ASN per PO
    caps the ASN spine at the ~1,200-merchandise-PO universe: W1006's ~700–750/month and
    PA-03.4's combined ~5,000–10,000 portal-document band (PO acks + ASNs + invoices)
    both adjudicate the PO-spine reading, and W1365's own 15–20% exceptions of 4,800
    = 720–960 equaled W1006's ENTIRE ASN universe — nearly every ASN discrepant, against
    its own <70%-accuracy flagging threshold; trued to ~700–750 ASNs with ~105–150
    exceptions and the hours/staffing re-footed ~18–50 h/month chain-wide, ~4–13 h/DC),
    W1006's Volume (PA-03.2 — 'average 15 lines per ASN' under a '1 ASN per PO' model:
    the ASN mirrors its PO at the 6.9–7.4 lines/PO canon; trued to ~7 lines per ASN), and
    W1169's Volume (PA-06.1 — '~15–25 container drayage moves per DC per week' below its
    own Frequency row's ~20–30 containers/DC/week arrival canon; trued to ~20–30
    round-trip moves, one per container).
    Rule: the retired forms are banned on live
    surfaces (whole PA/README files — they carry no history blocks;
    footer-stripped bodies for the versioned docs; the gap-analysis scenario
    tables stay exempt as dated authoring-time records, the sixteenth-wave
    convention; the classification register's dated batch-note segments
    exempt), and the calibrated anchors are required at the repaired cells
    (when a future calibration moves the canon these anchors re-fire until
    consciously re-pointed — the Check-71 CENSUS-pin contract)."""
    hits = []

    def _sweep(relp, body, label):
        banned = [
            "5,000 store replenishment", "5,000 replenishment orders",
            "~33 replenishment orders", "~1,250 replenishment orders",
            "18,000 PO lines", "~15 lines per PO",
            "carries 2\u20133 orders consolidated",
            "fulfills 2\u20133 replenishment orders",
            "grows ~100 GB/year", "~1,000 GB data warehouse",
            "~10,000 deliveries", "~330\u2013350 deliveries/day",
            "~400\u2013500/day", "~80\u201390 home deliveries",
            "~55\u201360 store replenishments", "~40\u201350 per DC per day",
            # sixty-seventh-wave extension: sibling-cell stragglers of the same canon
            "~167 orders/day", "(~42 per DC/day)", "~42 orders/day",
            "with ~50 lines each", "~50 lines per order",
            "~1,300 store-replenishment pick lines",
            "~33 store replenishment shipments", "~148 shipments",
            "~5,000 shipments/month chain-wide", "~40\u201350 shipments/DC/day",
            "~5,000 DC-to-store shipments",
            "~60,000 store replenishment orders annually",
            "~10,000\u201317,000 home delivery", "~5,000+ monthly movements",
            "= ~40 loads/day", "~30 outbound loads/day",
            "~900 outbound load slots", "~70 appointment slots",
            "~500\u2013800 SKUs per delivery",
            # sixty-eighth-wave extension: the calibration's own written-cell drift and
            # the new canon rows' unread derived cells
            "~5,300 replenishment pick lines", "~1,060 high-value pick lines",
            "~265 issues/day", "~40 receipts/day/DC",
            "~1,400\u20131,600 POs/month",
            "20\u201350 lines per DC delivery", "~20\u201350 lines/SKUs per delivery",
            "1,700\u20132,600 adjustments", "1,000 GB",
            # sixty-ninth-wave extension: the root-README at-a-glance PO row (the
            # loose numeral pair is NOT banned — PA-79.2's separated-employee cells
            # legitimately use it; only the 'total' form is the retired PO band)
            "~1,400\u20131,600 total",
            # seventieth-wave extension: the receipt/ASN/container sibling family
            # (the '~20–30 import containers' form is PA-04.1-file-scoped — see the
            # (g) block: PA-01.1's '~20–30 import containers per seasonal event'
            # forward-buy cells are a different, legitimate population)
            "~15 lines per receipt", "15 lines per ASN",
            "4,800 ASN", "~15\u201325 container drayage moves",
            # seventy-first-wave extension: the returns canon — the §1.1
            # AR-credit-memo row (~40/day = ~1,200/month at ~1.05 lines/doc)
            # that the calibration grounded but the returns workflows never
            # re-derived (the '~56,000/month at ~2%' family and its
            # 10–12%-of-ecommerce-orders sub-canon; the training-hours
            # '~56,000 hours' population of PA-30.3 is a different, legitimate
            # number and stays untouched; PA-09.2's per-category return-rate
            # prose and PA-08.1's split-tender share are different populations)
            "~56,000 returns", "56,000 credit notes", "56,000 return receipts",
            "48,000\u201356,000", "50,000\u201358,000 refund", "~1,867 returns/day",
            "~280 returns/store", "~2% return rate", "~2% of POS transactions",
            "~2% of transactions (returns)", "~56K/month", "~670K+ returns/yr",
            "4,000\u20135,000 ecommerce return", "4,000\u20135,000/month per W1623",
            "4,000\u20135,000/mo", "4,000\u20135,000 total requests",
            "10\u201312% ecommerce return", "~10\u201312% return-request rate",
            "(~10\u201312% return rate)", "8\u201310% of ecommerce orders",
            "\u2248 8\u201310% subset", "3,300\u20134,200",
            "8,000\u201315,000 returned items", "800\u20131,700 returns",
            "800\u20131,700/month", "~41,000 refund transactions",
            "~15,000 exchanges", "~75 exchanges/store",
            "~8,000\u201310,000 no-receipt", "~45\u201350 per store/month",
            "~40\u201350 per store/month", "~205 per store/month",
            "~17,000 exceptions", "~2,800\u20134,500 fraudulent",
            "~1,700\u20132,800/month", "~9 per store/day",
            "~17\u201321 drop-offs/store", "~17\u201321 returns",
            "~11,500 items/month", "~130\u2013170 ecommerce",
            "~1,860 POS returns/day", "~2,000 total returns/day",
            "5,600\u201311,200 returns/month", "~28\u201356 per store per month",
            "6\u201314 Returns Inspectors", "~500\u2013700 B2B returns",
            # seventy-second-wave extension: the dodging-variant stragglers —
            # the hyphenated replenishment form (both wave-66 forms are
            # space-form), the returns-canon sibling stragglers inside the
            # very files the seventy-first wave repaired (W1641's
            # dispositions Frequency/touchpoint, W1640's refurb pool,
            # W1336's Background + loss derivation + step-1(f) rate basis),
            # and the AP business-day band review #60 left behind in W7's
            # own Time Estimate and PA-22.1's copy
            "5,000 store-replenishment",
            "56,000 return dispositions", "56,000 monthly returns",
            "56,000 product returns per month", "grouping 2\u20133 orders/truck",
            "mis-routes thousands of returns",
            "500\u2013800 items/month eligible for refurbishment",
            "125\u2013200 per DC/month",
            "PHP 60\u2013100M in annual losses", "~2.5x the chain average",
            "305\u2013370 invoices", "~70 invoices \u00d7 25 min",
            "60\u201370 hours/business-day", "53\u201367 hours/business-day",
        ]
        for bad in banned:
            if bad in body:
                hits.append((label, body[:body.index(bad)].count("\n") + 1,
                             f"retired calibration form '{bad}' on a live surface "
                             f"(the canon is ~50,000 replenishment orders/month, "
                             f"~12,000 PO lines/month at ~7 lines/PO, ~123 GB/year, "
                             f"~17,200 home deliveries/month, ~1,200 returns/month "
                             f"at the ~40/day AR-credit-memo basis; version footers "
                             f"and the gap-analysis scenario tables are the "
                             f"frozen-history surfaces)"))

    # (a) every PA file + VS README — live in full (no history blocks)
    for pa in sorted(glob.glob(os.path.join(REPO, "01-model-company", "workflows",
                                            "VS-*", "*.md"))):
        txt = open(pa, encoding="utf-8").read()
        _sweep(pa, txt, os.path.basename(pa))
    for rd in sorted(glob.glob(os.path.join(REPO, "01-model-company", "workflows",
                                           "VS-*", "README.md"))):
        txt = open(rd, encoding="utf-8").read()
        _sweep(rd, txt, "VS README " + os.path.basename(os.path.dirname(rd)))

    # (b) the classification register — live cells only (dated segments exempt)
    cpath = os.path.join(REPO, "01-model-company", "workflows",
                         "workflow-criticality-classification.md")
    clines = open(cpath, encoding="utf-8").read().split("\n")
    fi = next((i for i, l in enumerate(clines)
               if l.startswith("*Document Version:") or l.startswith("*Date:")),
              len(clines))
    cbody = "\n".join(l for l in clines[:fi] if not l.startswith(" >"))
    _sweep(cpath, cbody, "workflow-criticality-classification.md")
    if "~50,000 replenishment orders/month (production-calibrated)" not in cbody:
        hits.append(("workflow-criticality-classification.md", 0,
                     'missing W4 significance anchor "~50,000 replenishment '
                     'orders/month (production-calibrated)"'))

    # (c) versioned docs — footer-stripped live bodies
    for relp, label in [
        ("01-model-company/model-company-profile.md", "model-company-profile.md"),
        ("01-model-company/optimal-table-of-organization.md",
         "optimal-table-of-organization.md"),
        ("01-model-company/data-volumes-and-integrations.md",
         "data-volumes-and-integrations.md"),
        ("01-model-company/headcount-reality-check.md",
         "headcount-reality-check.md"),
        ("07-methodology/it-product-operating-model.md",
         "it-product-operating-model.md"),
    ]:
        body = re.split(r"(?m)^\*Document Version:", open(
            os.path.join(REPO, relp), encoding="utf-8").read())[0]
        _sweep(relp, body, label)
    prof = re.split(r"(?m)^\*Document Version:", open(
        os.path.join(REPO, "01-model-company", "model-company-profile.md"),
        encoding="utf-8").read())[0]
    if "~1,600\u20131,900 total POs (production-calibrated" not in prof:
        hits.append(("model-company-profile.md", 0,
                     'missing §6.5 anchor "~1,600–1,900 total POs '
                     '(production-calibrated" (the §15.1 all-types canon)'))
    to_body = re.split(r"(?m)^\*Document Version:", open(
        os.path.join(REPO, "01-model-company",
                     "optimal-table-of-organization.md"),
        encoding="utf-8").read())[0]
    if "~12,000 PO lines/mo" not in to_body:
        hits.append(("optimal-table-of-organization.md", 0,
                     'missing procurement sizing-basis anchor "~12,000 PO lines/mo"'))

    # (c2) the root README — the at-a-glance row the cascade never reached
    # (sixty-ninth wave): un-versioned, so swept whole.
    root_readme = open(os.path.join(REPO, "README.md"), encoding="utf-8").read()
    _sweep(relp="README.md", body=root_readme, label="README.md")
    if "~1,600\u20131,900 total (production-calibrated)" not in root_readme:
        hits.append(("README.md", 0,
                     'missing at-a-glance PO anchor "~1,600–1,900 total '
                     '(production-calibrated)" (the §15.1 all-types canon)'))

    # (d) calibrated storage/PO anchors in the IT PA surfaces
    it27 = open(os.path.join(REPO, "01-model-company", "workflows", "VS-27-"
                 "it-operations-security", "PA-27.2-infrastructure-and-platform.md"),
                encoding="utf-8").read()
    if "~123 GB/year per the §1.2 canon" not in it27:
        hits.append(("PA-27.2-infrastructure-and-platform.md", 0,
                     'missing storage-growth anchor "~123 GB/year per the §1.2 canon"'))
    it28 = open(os.path.join(REPO, "01-model-company", "workflows", "VS-28-"
                 "data-analytics-bi", "PA-28.2-data-engineering-and-quality.md"),
                encoding="utf-8").read()
    if "~1,230 GB data warehouse" not in it28:
        hits.append(("PA-28.2-data-engineering-and-quality.md", 0,
                     'missing DW-size anchor "~1,230 GB data warehouse"'))

    # (e) sixty-seventh-wave anchors — the sibling-cell repairs' corrected forms
    # required at their cells (a future calibration moves the canon → these re-fire)
    def _pa(vs_dir, name):
        return open(os.path.join(REPO, "01-model-company", "workflows", vs_dir,
                                 name), encoding="utf-8").read()

    pa051 = _pa("VS-05-inventory-lifecycle",
                "PA-05.1-inventory-accuracy-and-counting.md")
    for anc in ("~1,700 orders/day across all DCs (~415\u2013425 per DC/day)",
                "avg ~3 lines per order (the production-measured order profile, "
                "per data-volumes \u00a71.1)",
                "handle ~415\u2013425 orders/day with ~3 lines each"):
        if anc not in pa051:
            hits.append(("PA-05.1-inventory-accuracy-and-counting.md", 0,
                         f'missing W4 calibrated anchor "{anc}"'))
    pa042 = _pa("VS-04-dc-warehouse", "PA-04.2-dc-outbound-operations.md")
    for anc in ("~1,250 store-replenishment pick lines + ~140\u2013145 ecommerce picks",
                "~15\u201320 store-replenishment delivery loads + ~140\u2013145 ecommerce parcels",
                "~1,800\u20132,400 store-delivery loads/month chain-wide",
                "~15\u201320 store-delivery loads/DC/day",
                "4 DCs \u00d7 ~15\u201320 loads/day = ~60\u201380 loads/day",
                "~600,000 store replenishment orders annually",
                "~155\u2013165 shipments/DC/day",
                "60\u201390 order lines at the production-measured ~3 lines/order"):
        if anc not in pa042:
            hits.append(("PA-04.2-dc-outbound-operations.md", 0,
                         f'missing calibrated anchor "{anc}"'))
    pa151 = _pa("VS-15-procure-to-pay",
                "PA-15.1-invoice-processing-and-matching.md")
    for anc in ("~17,200 home delivery shipments/month (the W19 canon)",
                "~18,900\u201319,900 freight-billable movements",
                "~50,630\u201350,640 monthly IC inventory movements"):
        if anc not in pa151:
            hits.append(("PA-15.1-invoice-processing-and-matching.md", 0,
                         f'missing calibrated anchor "{anc}"'))
    if "~12,000\u201320,000" in pa151:
        hits.append(("PA-15.1-invoice-processing-and-matching.md", 0,
                     "retired calibration form '~12,000–20,000' on a live "
                     "surface (the W277/W461 freight-billable sum re-foots to "
                     "~18,900–19,900 with the 17,200/month W19 home-delivery "
                     "canon)"))
    pa062 = _pa("VS-06-logistics-fleet", "PA-06.2-fleet-and-driver-management.md")
    if "~1,800\u20132,400 DC-to-store delivery loads/month using RTP" not in pa062:
        hits.append(("PA-06.2-fleet-and-driver-management.md", 0,
                     'missing W1256 RTP anchor "~1,800–2,400 DC-to-store '
                     'delivery loads/month using RTP"'))
    pa043 = _pa("VS-04-dc-warehouse", "PA-04.3-dc-operations-management.md")
    for anc in ("~15\u201320 outbound loads/day per DC",
                "~450\u2013600 outbound load slots/month per DC",
                "~55\u201360 appointment slots"):
        if anc not in pa043:
            hits.append(("PA-04.3-dc-operations-management.md", 0,
                         f'missing calibrated anchor "{anc}"'))
    pa102 = _pa("VS-10-ecommerce-digital",
                "PA-10.2-order-fulfillment-and-delivery.md")
    if "~415\u2013425 orders/day \u2248 ~1,250 pick lines/DC/day" not in pa102:
        hits.append(("PA-10.2-order-fulfillment-and-delivery.md", 0,
                     'missing staffing anchor "~415–425 orders/day '
                     '≈ ~1,250 pick lines/DC/day"'))

    # (f) sixty-eighth-wave anchors — the calibration's own written-cell drift and
    # the new canon rows' unread derived cells, corrected
    if "~5,000 replenishment pick lines/day chain-wide" not in pa042 or \
            "~1,000 high-value pick lines/day chain-wide" not in pa042 or \
            "(~250 issues/day chain-wide)" not in pa042:
        hits.append(("PA-04.2-dc-outbound-operations.md", 0,
                     'missing W1352 Time-Estimate anchor "~5,000 replenishment '
                     'pick lines/day chain-wide" / "~1,000 high-value pick lines '
                     'day chain-wide" / "(~250 issues/day chain-wide)"'))
    if "~50 receipts/day/DC" not in pa043:
        hits.append(("PA-04.3-dc-operations-management.md", 0,
                     'missing W270 RTP anchor "~50 receipts/day/DC" (the '
                     '~6,000/month DC goods-receipt canon, per PA-04.1/§1.1)'))
    pa053 = _pa("VS-05-inventory-lifecycle",
                "PA-05.3-inventory-disposition-and-optimization.md")
    if "200 stores \u00d7 ~3\u20135 + 4 DCs \u00d7 ~20\u201330" not in pa053 or \
            "~3\u20135 adjustments per store per month" not in pa053:
        hits.append(("PA-05.3-inventory-disposition-and-optimization.md", 0,
                     'missing W92 calibrated anchor "200 stores × ~3–5 + 4 DCs '
                     '× ~20–30" / "~3–5 adjustments per store per month" (the '
                     '~30/day §1.1 IAD canon)'))
    pa073 = _pa("VS-07-store-operations",
                "PA-07.3-store-receiving-and-replenishment.md")
    if "60\u201390 order lines per DC delivery" not in pa073 or \
            "~60\u201390 order lines per delivery" not in pa073:
        hits.append(("PA-07.3-store-receiving-and-replenishment.md", 0,
                     'missing consolidated-drop anchor "60–90 order lines per '
                     'DC delivery" (W109) / "~60–90 order lines per delivery" '
                     '(W666)'))
    pa1292 = _pa("VS-129-competition-and-antitrust-compliance",
                 "PA-129.2-anticompetitive-conduct-prevention-and-compliance-"
                 "controls.md")
    if "~1,200 merchandise POs/month" not in pa1292:
        hits.append(("PA-129.2-anticompetitive-conduct-prevention-and-"
                     "compliance-controls.md", 0,
                     'missing W3962 PO-canon anchor "~1,200 merchandise '
                     'POs/month" (all types ~1,600–1,900/month '
                     'production-calibrated)'))

    # (g) seventieth-wave anchors — the receipt/ASN/container sibling family the
    # calibration and waves 66–69 left one derivation step out from the pinned
    # cells (a future calibration moves the canon → these re-fire until
    # consciously re-pointed — the Check-71 CENSUS-pin contract)
    pa041 = _pa("VS-04-dc-warehouse", "PA-04.1-dc-inbound-operations.md")
    for anc in ("~2 lines per receipt on average",
                "~100\u2013150 import containers",
                "~700\u2013750 ASN submissions/month",
                "~105\u2013150 exceptions/month"):
        if anc not in pa041:
            hits.append(("PA-04.1-dc-inbound-operations.md", 0,
                         f'missing calibrated anchor "{anc}"'))
    if "20\u201330 import containers" in pa041:
        hits.append(("PA-04.1-dc-inbound-operations.md", 0,
                     "retired calibration form '20–30 import containers' on a "
                     "live surface (the container canon is the ~400–600 TEUs/month "
                     "§7.1 import universe — ~100–150 containers/DC/month at "
                     "~1 TEU/container, per W1271/W1169; PA-01.1's seasonal-event "
                     "forward-buy cells are the legitimate '~20–30 per seasonal "
                     "event' population and stay exempt — the wave-67 "
                     "file-scoped-ban convention)"))
    pa032 = _pa("VS-03-vendor-management", "PA-03.2-purchase-order-cycle.md")
    if "~7 lines per ASN" not in pa032:
        hits.append(("PA-03.2-purchase-order-cycle.md", 0,
                     'missing W1006 ASN anchor "~7 lines per ASN" (1 ASN per PO '
                     'at the production-measured 6.9–7.4 lines/PO canon)'))
    pa061 = _pa("VS-06-logistics-fleet", "PA-06.1-outbound-distribution.md")
    if "~20\u201330 container drayage round-trip moves per DC per week" not in pa061:
        hits.append(("PA-06.1-outbound-distribution.md", 0,
                     'missing W1169 drayage anchor "~20–30 container drayage '
                     'round-trip moves per DC per week" (per its own '
                     '~20–30 containers/DC/week Frequency canon)'))

    # (h) seventy-first-wave anchors — the returns canon the calibration grounded
    # (§1.1 AR credit memos ~40/day = ~1,200/month at ~1.05 lines/doc) but whose
    # workflow family it never re-derived: the master counter slice, the
    # ecommerce sub-canon, the B2B slice, the derived shares and the fraud/
    # disposition/refund/IDP/P2P dependents (a future calibration moves the
    # canon → these re-fire until consciously re-pointed — the Check-71
    # CENSUS-pin contract)
    pa321 = _pa("VS-32-returns-reverse-logistics",
                "PA-32.1-customer-returns-processing.md")
    for anc in ("~950\u20131,050 counter returns/month",
                "~250\u2013350 ecommerce return requests/month",
                "~325 exchanges/month",
                "~180\u2013215 no-receipt returns/month",
                "~180\u2013215 returns/month require quality assessment",
                "~875 refund transactions/month",
                "~100\u2013150 B2B returns/month",
                "~1,200 returns/month across 200 stores (the AR-credit-memo "
                "returns canon)"):
        if anc not in pa321:
            hits.append(("PA-32.1-customer-returns-processing.md", 0,
                         f'missing returns-canon anchor "{anc}"'))
    pa071 = _pa("VS-07-store-operations", "PA-07.1-store-daily-management.md")
    for anc in ("~950\u20131,050 returns/month chain-wide",
                "~200\u2013250 online returns/month chain-wide",
                "\u2248120\u2013240/month chain-wide"):
        if anc not in pa071:
            hits.append(("PA-07.1-store-daily-management.md", 0,
                         f'missing W12 returns-canon anchor "{anc}"'))
    pa083 = _pa("VS-08-pos-checkout", "PA-08.3-pos-compliance-and-controls.md")
    for anc in ("~1,200 credit notes/month", "~36\u201360/month"):
        if anc not in pa083:
            hits.append(("PA-08.3-pos-compliance-and-controls.md", 0,
                         f'missing W540/W605 returns-canon anchor "{anc}"'))
    pa233 = _pa("VS-23-loss-prevention", "PA-23.3-shrinkage-reduction.md")
    if "~60\u201395 fraudulent returns/month" not in pa233:
        hits.append(("PA-23.3-shrinkage-reduction.md", 0,
                     'missing W1336 returns-canon anchor "~60–95 fraudulent '
                     'returns/month"'))
    pa323 = _pa("VS-32-returns-reverse-logistics",
                "PA-32.3-reverse-logistics-disposition.md")
    if "~360 exceptions/month" not in pa323:
        hits.append(("PA-32.3-reverse-logistics-disposition.md", 0,
                     'missing disposition anchor "~360 exceptions/month"'))
    pa101 = _pa("VS-10-ecommerce-digital",
                "PA-10.1-ecommerce-platform-operations.md")
    for anc in ("~500\u20131,000 returned items/month",
                "~750 items/month average"):
        if anc not in pa101:
            hits.append(("PA-10.1-ecommerce-platform-operations.md", 0,
                         f'missing W509 returns-canon anchor "{anc}"'))
    for anc in ("~50\u2013100 returns/month at steady state",
                "~200\u2013250 ecommerce store drop-offs/month"):
        if anc not in pa102:
            hits.append(("PA-10.2-order-fulfillment-and-delivery.md", 0,
                         f'missing W215/W1273 returns-canon anchor "{anc}"'))
    pa131 = _pa("VS-13-customer-experience",
                "PA-13.1-customer-support-and-complaints.md")
    for anc in ("~32\u201335 in-store/POS counter returns/day",
                "~40 total returns/day across all channels"):
        if anc not in pa131:
            hits.append(("PA-13.1-customer-support-and-complaints.md", 0,
                         f'missing W707 returns-canon anchor "{anc}"'))
    pa603 = _pa("VS-60-omnichannel-order-routing",
                "PA-60.3-fulfillment-performance-analytics.md")
    if "return-request rate ~0.6\u20130.8%" not in pa603:
        hits.append(("PA-60.3-fulfillment-performance-analytics.md", 0,
                     'missing W2308 anchor "return-request rate ~0.6–0.8%"'))
    pa1252 = _pa("VS-125-cross-channel-fraud-management-payment-fraud-"
                 "protection",
                 "PA-125.2-channel-fraud-prevention-detection.md")
    if "~14,500 returns/yr" not in pa1252:
        hits.append(("PA-125.2-channel-fraud-prevention-detection.md", 0,
                     'missing returns-canon anchor "~14,500 returns/yr"'))
    pa1182 = _pa("VS-118-revenue-assurance-pricing-integrity-and-leakage-"
                 "management",
                 "PA-118.2-pricing-promotion-loyalty-and-payment-integrity-"
                 "monitoring.md")
    if "~0.04% return rate (profile \u00a75 \u2014 the ~40/day AR-credit-memo canon)" \
            not in pa1182:
        hits.append(("PA-118.2-pricing-promotion-loyalty-and-payment-integrity-"
                     "monitoring.md", 0,
                     'missing returns-canon anchor "~0.04% return rate '
                     '(profile §5 — the ~40/day AR-credit-memo canon)"'))
    pa152 = _pa("VS-15-procure-to-pay",
                "PA-15.2-vendor-payment-and-reconciliation.md")
    for anc in ("~950\u20131,050 in-store return refunds/credits",
                "~1,300\u20131,550 refund/credit transactions/month"):
        if anc not in pa152:
            hits.append(("PA-15.2-vendor-payment-and-reconciliation.md", 0,
                         f'missing W101 returns-canon anchor "{anc}"'))
    pa802 = _pa("VS-80-payment-operations-acquirer-settlement",
                "PA-80.2-settlement-reconciliation-and-dispute.md")
    if "~1,200 refund/void events/month" not in pa802:
        hits.append(("PA-80.2-settlement-reconciliation-and-dispute.md", 0,
                     'missing W2790 returns-canon anchor "~1,200 refund/void '
                     'events/month"'))
    pa302 = _pa("VS-30-innovation-digital", "PA-30.2-ai-ml-and-automation.md")
    if "~1,200 return receipts/month" not in pa302:
        hits.append(("PA-30.2-ai-ml-and-automation.md", 0,
                     'missing IDP returns-canon anchor "~1,200 return '
                     'receipts/month"'))
    if "(~0.04% return rate \u2014 ~40 AR credit memos/day, per data-volumes \u00a71.1)" \
            not in prof:
        hits.append(("model-company-profile.md", 0,
                     'missing §5 POS-mix returns anchor "(~0.04% return rate — '
                     '~40 AR credit memos/day, per data-volumes §1.1)"'))
    # the custody register's E-09 row — a live navigation surface outside the
    # PA/README glob (swept live-body only; the dated custody-wave footer
    # segments are frozen history)
    custody = os.path.join(REPO, "01-model-company", "workflows",
                           "event-custody-and-precedence-register.md")
    clines2 = open(custody, encoding="utf-8").read().split("\n")
    fi2 = next((i for i, l in enumerate(clines2)
                if l.startswith("*Date:") and "(v" in l), len(clines2))
    cbody2 = "\n".join(clines2[:fi2])
    for bad in ("3,300\u20134,200", "4,000\u20135,000/mo", "8\u201310% subset"):
        if bad in cbody2:
            hits.append(("event-custody-and-precedence-register.md",
                         cbody2[:cbody2.index(bad)].count("\n") + 1,
                         f"retired returns-canon form '{bad}' on the live "
                         f"E-09 row"))
    if "\u2248 250\u2013350/mo, ~0.6\u20130.8% of ~42,900 orders" not in cbody2:
        hits.append(("event-custody-and-precedence-register.md", 0,
                     'missing E-09 returns-canon anchor "≈ 250–350/mo, '
                     '~0.6–0.8% of ~42,900 orders"'))

    # (i) seventy-second-wave anchors — the dodging-variant stragglers'
    # corrected forms required at their cells (a future calibration moves
    # the canon → these re-fire until consciously re-pointed — the
    # Check-71 CENSUS-pin contract)
    pa1361 = _pa("VS-136-supply-chain-network-design-multi-echelon-inventory-"
                 "optimization-flow-engineering",
                 "PA-136.1-supply-chain-network-strategy-modeling-and-design.md")
    for anc in ("~50,000 store-replenishment orders/month (production-calibrated, "
                "per data-volumes \u00a71.1)",
                "each store drop consolidates the ~20\u201330 replenishment orders "
                "since the previous drop, 2\u20133 drops per truck trip"):
        if anc not in pa1361:
            hits.append(("PA-136.1-supply-chain-network-strategy-modeling-and-"
                         "design.md", 0, f'missing calibrated anchor "{anc}"'))
    pa136r = _pa("VS-136-supply-chain-network-design-multi-echelon-inventory-"
                 "optimization-flow-engineering", "README.md")
    if ("~50,000 monthly store-replenishment orders (production-calibrated, "
            "per data-volumes \u00a71.1)") not in pa136r:
        hits.append(("VS-136 README", 0,
                     'missing calibrated anchor "~50,000 monthly '
                     'store-replenishment orders (production-calibrated, '
                     'per data-volumes §1.1)"'))
    for anc in ("~1,200 return dispositions/month (one per return",
                "~180\u2013300 items/month eligible for refurbishment",
                "~45\u201375 per DC/month (180\u2013300 \u00f7 4 DCs)"):
        if anc not in pa323:
            hits.append(("PA-32.3-reverse-logistics-disposition.md", 0,
                         f'missing returns-canon anchor "{anc}"'))
    for anc in ("~1,200 product returns per month per W12/W1622",
                "~PHP 3\u20136M in annual losses",
                "materially above the ~0.04%-of-transactions chain canon"):
        if anc not in pa233:
            hits.append(("PA-23.3-shrinkage-reduction.md", 0,
                         f'missing W1336 returns-canon anchor "{anc}"'))
    pa221 = _pa("VS-22-compliance-regulatory",
                "PA-22.1-regulatory-permits-and-licenses.md")
    for anc in ("~33\u201337 hours/business-day (395\u2013440 invoices \u00d7 5 min)",
                "~79\u201388 invoices \u00d7 25 min avg",
                "~68\u201376 hours/business-day"):
        if anc not in pa151:
            hits.append(("PA-15.1-invoice-processing-and-matching.md", 0,
                         f'missing W7 AP-band anchor "{anc}"'))
    for anc in ("~395\u2013440 invoices/business-day",
                "requiring 10 clerks at ~7 hrs each/day"):
        if anc not in pa221:
            hits.append(("PA-22.1-regulatory-permits-and-licenses.md", 0,
                         f'missing AP-band anchor "{anc}"'))
    return hits


def atlassian_suite_hits():
    """2026-09-23 seventy-fifth-wave consistency review — the A6.6 Atlassian
    canon's own completeness guard. The 2026-09-23 incorporation pass
    (assumptions v4) put the IT toolchain on the Atlassian Cloud suite but (a)
    never named **Atlassian Guard** — the suite's centralized identity plane
    (SAML SSO, enforced MFA, SCIM provisioning, organization audit logs) that
    guardrails 5 and 7 already assumed — (b) left the two EBS-adjacent flows the
    workflows assert out of the canonical integration matrix (data-volumes §3:
    the W616.1 self-service portal → Jira Software enhancement-request sync and
    the Guard organization audit-log stream into the SIEM), (c) left the sourcing
    model's §8 vendor-commodity estate un-named while §12.2's 'sole vendor
    product line' parenthetical could be misread against A6.6, and (d) phrased
    guardrails 2/4 universally over an estate (EBS) whose path to production is
    ADOP online patching, not Bitbucket Pipelines. This pass trued all four; the
    rule re-derives the repaired surfaces every run.

    Anchors required (a future Atlassian re-architecture moves the canon → these
    re-fire until consciously re-pointed — the Check-71 CENSUS-pin contract):
    the Guard forms at the A6.6 row, the Design-Decisions row, guardrail 5 and
    guardrail 7; the completed A6.6 Source cell (all 16 PA-27.1 workflows); the
    built-product scoping + EBS ADOP boundary in guardrails 2/4; the Bitbucket
    branch-permission form; the two canonical matrix rows and their pattern-
    register mirrors (02-oracle-ebs integrations §2 — endpoint order is checked
    by integration_mirror_hits, content pinned here); the W152
    Guard-provisioning and W132 branch-permission touchpoints (PA-27.1); the
    W367 Guard audit-log touchpoint (PA-27.3); the sourcing model's §8 Atlassian
    line and §12.2 'in capability sourcing' true-up.

    Retired forms banned (footer-stripped, doc-scoped unless noted): the
    universal 'every production change carries the chain' form (the built-product
    scoping is the canon), the unqualified 'cloud audit logs streamed to the
    SIEM' form (Guard is the vehicle), the 'IT-staff seats provisioned via
    directory groups with SSO/MFA' Guard-less form, and — repo-wide across the
    authored trees — the incorporation pass's retired hedges 'Jira/ServiceNow',
    'TestRail' and '(Confluence, SharePoint, or ITSM built-in KB)' (the
    assumptions doc's Design-Decisions alternative legitimately names ServiceNow
    without the slash form — the slash hedge is the banned signature)."""
    hits = []

    def _body(relp):
        return re.split(r"(?m)^\*Date: |^\*Document Version:", open(
            os.path.join(REPO, relp), encoding="utf-8").read())[0]

    # ---- (a) the assumptions doc: Guard anchors + completed Source cell +
    # the guardrail 2/4 estate scoping
    asm = _body("01-model-company/assumptions-and-design-decisions.md")
    for anc in (
            "administered under Atlassian Guard (centralized identity: SAML SSO, "
            "enforced MFA, SCIM provisioning, organization audit logs)",
            "W152/W615/W372/W495/W5521",
            "administered under Atlassian Guard (SAML SSO, enforced MFA, SCIM "
            "provisioning, organization audit logs)",
            "**End-to-end traceability (built-product estate)**",
            "JSM change ticket \u2194 Confluence runbook \u2194 ADOP online-patching "
            "execution",
            "**Bitbucket is the only path to production for the built-product "
            "estate**",
            "branch permissions on the production branches (no direct pushes \u2014 "
            "merges only through PR with the reviewer rule enforced as a merge "
            "check",
            "SSO with MFA enforced through Atlassian Guard",
            "Atlassian Guard organization audit logs streamed to the SIEM"):
        if anc not in asm:
            hits.append(("assumptions-and-design-decisions.md", 0,
                         f'missing A6.6 anchor "{anc[:72]}..."'))
    for lit in ("every production change carries the chain",
                "cloud audit logs streamed to the SIEM"):
        if lit in asm:
            hits.append(("assumptions-and-design-decisions.md", 0,
                         f'retired A6.6 form "{lit}" on a live surface'))

    # ---- (b) the canonical matrix rows + their EBS pattern-register mirrors
    dv = _body("01-model-company/data-volumes-and-integrations.md")
    for anc in ("| ERP | Jira Software | Approved ERP enhancement requests "
                "(the W616.1 self-service portal) synced to the delivery backlog "
                "| ERP \u2192 Jira | Near real-time (on approval) |",
                "| Atlassian Cloud | SIEM | Organization audit logs (JSM, Jira, "
                "Confluence, Bitbucket \u2014 via Atlassian Guard) | Atlassian \u2192 "
                "SIEM | Continuous (streaming) |"):
        if anc not in dv:
            hits.append(("data-volumes-and-integrations.md", 0,
                         f'missing \u00a73 canonical matrix row "{anc[:60]}..." '
                         f'(the A6.6 flow canon; the EBS pattern register mirrors '
                         f'it one-for-one)'))
    reg = _body("02-oracle-ebs/integrations.md")
    for anc in ("| ERP \u2192 Jira Software: enhancement-request sync |",
                "| Atlassian Cloud \u2192 SIEM: organization audit-log stream |"):
        if anc not in reg:
            hits.append(("integrations.md (02-oracle-ebs)", 0,
                         f'missing pattern-register row "{anc[:60]}..." (must '
                         f'quote the canonical \u00a73 matrix row verbatim)'))

    # ---- (c) the sourcing model's vendor-commodity estate + the \u00a712.2 true-up
    src = _body("07-methodology/capability-sourcing-and-engineering-model.md")
    for anc in ("the Atlassian Cloud IT-tooling suite \u2014 JSM/Jira/Confluence/"
                "Bitbucket under Atlassian Guard, per A6.6",
                "the doctrine's sole vendor product line in capability sourcing"):
        if anc not in src:
            hits.append(("capability-sourcing-and-engineering-model.md", 0,
                         f'missing sourcing-model anchor "{anc[:64]}..."'))

    # ---- (d) the workflow touchpoints (W152/W132 in PA-27.1; W367 in PA-27.3)
    pa271 = _body("01-model-company/workflows/VS-27-it-operations-security/"
                  "PA-27.1-service-management.md")
    for anc in ("provisioned via Atlassian Guard (SCIM provisioning from the "
                "corporate directory groups, enforced SSO/MFA policies)",
                "branch permissions on the production branches (no direct pushes "
                "\u2014 merges only through PR with the two-reviewer rule enforced "
                "as a merge check)"):
        if anc not in pa271:
            hits.append(("PA-27.1-service-management.md", 0,
                         f'missing A6.6 touchpoint anchor "{anc[:64]}..."'))
    pa273 = _body("01-model-company/workflows/VS-27-it-operations-security/"
                  "PA-27.3-cybersecurity-and-privacy.md")
    if "the Atlassian Guard organization audit-log stream into the SIEM" not in pa273:
        hits.append(("PA-27.3-cybersecurity-and-privacy.md", 0,
                     'missing W367 anchor "the Atlassian Guard organization '
                     'audit-log stream into the SIEM"'))

    # ---- (e) the retired hedge forms, banned repo-wide across the authored
    # trees (01-model-company, 02-oracle-ebs, 07-methodology; CHANGELOG exempt
    # as frozen history; the generated bpmn/dmn trees re-derive from the corpus).
    # 07-methodology/README.md is exempt: its audit-model-docs Contents row
    # quotes the retired literals in its own guard description (the Check-46
    # doctrine-scope adjudication — the arm caught its own author there
    # pre-ship, the wave-9 precedent; same exemption Check 78 records).
    hedges = ("Jira/ServiceNow", "TestRail",
              "(Confluence, SharePoint, or ITSM built-in KB)")
    for root in ("01-model-company", "02-oracle-ebs", "07-methodology"):
        for dirpath, _, files in os.walk(os.path.join(REPO, root)):
            if "__pycache__" in dirpath:
                continue
            for fn in files:
                if not fn.endswith(".md") or fn == "CHANGELOG.md":
                    continue
                if os.path.join(dirpath, fn) == os.path.join(
                        REPO, "07-methodology", "README.md"):
                    continue
                relp = os.path.relpath(os.path.join(dirpath, fn), REPO)
                txt = open(os.path.join(dirpath, fn), encoding="utf-8").read()
                for h in hedges:
                    for m in re.finditer(re.escape(h), txt):
                        hits.append((fn, txt[:m.start()].count("\n") + 1,
                                     f'retired A6.6 hedge "{h}" on a live '
                                     f'surface ({relp})'))
    return hits


def domain_companion_hits():
    """2026-09-23 seventy-sixth-wave consistency review — the batch-30 census
    stragglers on the surfaces no arm read. The (v) capability-switchboard pass
    (W5580, corpus 5,432 → 5,433) re-pointed every guarded census surface but
    stranded six unguarded classes: the value-stream-index H1 banner and its
    closing Total footer (both maintained live at batch 26 — the batch-30
    cascade moved the Grand Total cell between them and missed both), the
    conformance canon's own §1 framing sentence, the IT domain companion's
    Technology-&-Data roster (393 → 394 / VS-113 (31) → (32) — the exact class
    Check 76 guards, one derivation step outside its four quoted cells), and
    the retired **6,762** employee canon still sitting on the §1 scope lines
    and evidence cells of the IT/operations/people domain companions (the
    twenty-ninth-wave headcount sweep covered the PA files and VS READMEs but
    never opened these four navigation surfaces, which the fifteenth wave had
    established as live by re-pointing their family rosters to canon). This
    rule pins all six: retired forms banned doc-scoped on the live bodies, the
    corrected anchors required at the repaired cells — a future census move
    re-fires these until consciously re-pointed (the Check-71 CENSUS-pin
    contract)."""
    hits = []

    def _plain(relp):
        text = open(os.path.join(REPO, relp), encoding="utf-8").read()
        return text, text.split("*Document Version:")[0]

    # ---- (a) value-stream-index: banner + Total footer are maintained live
    # (batch 26 updated both; the footer is NOT a frozen-history surface)
    vsi_text, vsi = _plain("01-model-company/workflows/value-stream-index.md")
    for bad in ("5,432 Workflows", "5,432 workflows across 188 value streams"):
        if bad in vsi:
            hits.append(("value-stream-index.md",
                         vsi[:vsi.index(bad)].count("\n") + 1,
                         f"retired census form '{bad}' on a live line (the "
                         f"banner and Total footer are maintained live — the "
                         f"canon is 5,433 workflows since batch 30)"))
    for anc in ("569 Process Areas · 5,433 Workflows",
                "Total: 5,433 workflows across 188 value streams"):
        if anc not in vsi:
            hits.append(("value-stream-index.md", 0,
                         f'missing live census anchor "{anc}"'))

    # ---- (b) the conformance canon's own §1 framing sentence
    canon_text, canon = _plain(
        "02-oracle-ebs/oracle-ebs-conformance-standards.md")
    if "5,432 workflows across 569 process areas" in canon:
        hits.append(("oracle-ebs-conformance-standards.md",
                     canon[:canon.index("5,432 workflows across 569 process")
                           ].count("\n") + 1,
                     "retired §1 census form '5,432 workflows across 569 "
                     "process areas' (the canon is 5,433 since batch 30)"))
    if "(5,433 workflows across 569 process areas)" not in canon:
        hits.append(("oracle-ebs-conformance-standards.md", 0,
                     'missing §1 census anchor "(5,433 workflows across 569 '
                     'process areas)"'))

    # ---- (c) the four domain gap-analysis companions (live navigation
    # surfaces per Check 76's own preamble): retired census + headcount forms
    companions = {
        "01-model-company/workflows/workflow-gap-analysis-finance.md",
        "01-model-company/workflows/workflow-gap-analysis-it.md",
        "01-model-company/workflows/workflow-gap-analysis-operations.md",
        "01-model-company/workflows/workflow-gap-analysis-people.md",
    }
    for relp in sorted(companions):
        _t, body = _plain(relp)
        name = os.path.basename(relp)
        for bad in ("6,762", "6,911", "5,426", "5,427", "5,430"):
            if bad in body:
                hits.append((name, body[:body.index(bad)].count("\n") + 1,
                             f"retired canon figure '{bad}' on a live line of "
                             f"a domain companion (the active canon is 6,925 "
                             f"employees / 5,433 workflows; these surfaces "
                             f"carry no version footer, so the whole file is "
                             f"live)"))
    _t, it = _plain("01-model-company/workflows/workflow-gap-analysis-it.md")
    for bad in ("393 workflows", "VS-113 (31)"):
        if bad in it:
            hits.append(("workflow-gap-analysis-it.md",
                         it[:it.index(bad)].count("\n") + 1,
                         f"retired family-roster form '{bad}' (VS-113 is 32 "
                         f"workflows and the Technology & Data family is 394 "
                         f"since batch 30)"))
    for anc in ("**394 workflows**", "VS-113 (32)",
                "~6,925 M365/email users"):
        if anc not in it:
            hits.append(("workflow-gap-analysis-it.md", 0,
                         f'missing corrected roster anchor "{anc}"'))
    _t, ops = _plain(
        "01-model-company/workflows/workflow-gap-analysis-operations.md")
    for anc in ("payroll of 6,925 employees",
                "furnishing campaign to ~6,925 employees"):
        if anc not in ops:
            hits.append(("workflow-gap-analysis-operations.md", 0,
                         f'missing corrected headcount anchor "{anc}"'))
    _t, people = _plain(
        "01-model-company/workflows/workflow-gap-analysis-people.md")
    if "~6,925 employees (active); ~1,200–1,600 new hires/year" not in people:
        hits.append(("workflow-gap-analysis-people.md", 0,
                     'missing §1 scope anchor "~6,925 employees (active); '
                     '~1,200–1,600 new hires/year"'))

    # ---- (d) the 2026-09-23 (x) trade-desk disablement estate — the CAP-B01–B04
    # canon's completeness: the registry §3.4 rows, the assumptions Design-Decision
    # row, the TO's disabled annotations and the profile §3.3 bullet. A future
    # re-enablement moves the canon → these re-fire until consciously re-pointed.
    reg = open(os.path.join(REPO, "01-model-company",
                            "channel-capability-registry.md"),
               encoding="utf-8").read()
    for anc in ("| CAP-B01 | **Trade & Account Management department**",
                "**DISABLED — PREPARED** (2026-09-23 (x)) | TO §5.2/§5.3",
                "| CAP-B02 | Trade credit accounts (B2B AR)",
                "| CAP-B03 | Trade volume rebates",
                "| CAP-B04 | Trade Professional membership program",
                "Trade customers without the trade desk"):
        if anc not in reg:
            hits.append(("channel-capability-registry.md", 0,
                         f'missing §3.4 trade-estate anchor "{anc[:56]}..."'))
    assum = open(os.path.join(REPO, "01-model-company",
                              "assumptions-and-design-decisions.md"),
                 encoding="utf-8").read()
    if "| Trade & Account Management capability | **DISABLED — PREPARED (2026-09-23 (x))" not in assum:
        hits.append(("assumptions-and-design-decisions.md", 0,
                     "missing the trade-desk Design-Decision row"))
    to_t = open(os.path.join(REPO, "01-model-company",
                             "optimal-table-of-organization.md"),
                encoding="utf-8").read()
    for anc in ("**DISABLED — PREPARED (2026-09-23 (x))** — not staffed; design retained. 5,200 trade accounts",
                "active HQ **525** (Trade's 7 disabled — prepared)",
                "Design total; active **6,925**",
                "#### Trade / Account Management (7 — DISABLED — PREPARED 2026-09-23 per registry CAP-B01"):
        if anc not in to_t:
            hits.append(("optimal-table-of-organization.md", 0,
                         f'missing trade-desk annotation anchor "{anc[:56]}..."'))
    prof_raw = open(os.path.join(REPO, "01-model-company",
                                 "model-company-profile.md"),
                    encoding="utf-8").read()
    if "**DISABLED — PREPARED (2026-09-23 (x))** — not staffed; the 7-role design" not in prof_raw:
        hits.append(("model-company-profile.md", 0,
                     "missing §3.3 Trade disabled—prepared bullet"))
    return hits


def quote_coverage_hits():
    """2026-09-18 fifty-fifth-wave consistency review — structural guard for the
    cross-repo quote-coverage review (02-oracle-ebs/quote-coverage-review.md; it
    joined the DOCS set one wave after shipping, the licensing_bom_hits precedent
    — and its quoted RFQ figures had already drifted once against the RFQ's own
    v2.0.1/v2.0.2 revisions). Re-derives, every run: the G1–G17 coverage register
    (17 unique ids, no gaps), the PD decision register D-1–D-9, the §4
    quantity-reconciliation canon row (RFQ go-live 7,247 employees vs the 6,932
    repo canon), and the v1.1 post-review status note's supersession anchors."""
    rel = "quote-coverage-review.md"
    hits = []
    path = os.path.normpath(os.path.join(MC, "..", "02-oracle-ebs", rel))
    text = open(path, encoding="utf-8").read()
    body = text.split("*Document Version:")[0]
    ids = [int(m) for m in re.findall(r"\| \*\*G(\d+)\*\* \|", body)]
    if ids != list(range(1, 18)):
        hits.append((rel, 0, f"G-register ids {ids} != 1..17"))
    dids = sorted(int(m.group(1)) for m in re.finditer(r"\| D-(\d) \|", body))
    if dids != list(range(1, 10)):
        hits.append((rel, 0, f"PD decision register ids {dids} != D-1..D-9"))
    for anc in ("Post-review RFQ movement (recorded 2026-09-18",
                "**$20,273,515**",
                "coverage dispositions stand unchanged",
                "7,247 | 9,271 | 6,925"):
        if anc not in body:
            hits.append((rel, 0, f'missing required anchor "{anc}"'))
    return hits



def ebs_doc_coverage_hits():
    """2026-09-21 -- structural guard for the EBS documentation coverage register
    (02-oracle-ebs/ebs-documentation-coverage.md). The register is the only surface
    that reads the official R12.2 library (ebs_docs/) against this model, so its
    own figures must re-derive from disk rather than from its authoring snapshot
    (the licensing_bom_hits principle: the quantitative doc no rule re-derives is
    the one that drifts). Re-derived every run:
      (a) the §1 inventory's guide total and page total equal the PDFs on disk;
      (b) the §1 class rows sum to those totals;
      (c) the §4 EDC ids are contiguous 1..N with no duplicates, and the §2
          outcome arithmetic (adjudicated + recorded + open = products) holds
          with `open` equal to the EDC row count;
      (d) every backtick-quoted guide basename in the register exists in
          ebs_docs/current/acrobat/ -- a citation to a file that is not in the
          library is the register's own dangling-reference class; and, since the
          2026-09-21 sixty-first-wave manuals sweep, (e) the §3 POS-confirmation
          row states the library truthfully -- it must cite the one POS-named
          product the library actually ships (`122crposig`/`122crposug`, the
          supplier-side Channel Rebate & POS engine, recorded not-needed in §5),
          must carry the checkout-sense anchor, and the retired bare
          'No EBS POS product exists in the library' form is banned."""
    rel = "ebs-documentation-coverage.md"
    hits = []
    path = os.path.normpath(os.path.join(MC, "..", "02-oracle-ebs", rel))
    lib = os.path.normpath(os.path.join(MC, "..", "ebs_docs", "current", "acrobat"))
    text = open(path, encoding="utf-8").read()
    body = text.split("*Document Version:")[0]

    def num(s):
        return int(s.replace(",", ""))

    # ---- (a)/(b) inventory vs disk
    pdfs = [f for f in os.listdir(lib) if f.endswith(".pdf")] if os.path.isdir(lib) else []
    if not pdfs:
        hits.append((rel, 0, "ebs_docs/current/acrobat/ holds no PDFs -- the register's "
                             "source of record is missing"))
    rows = re.findall(r"^\| (?!Class\b)(?!\*\*Total)[^|]+\| (\*\*)?([\d,]+)(?:\*\*)? \| "
                      r"(\*\*)?([\d,]+)(?:\*\*)? \|", body, flags=re.M)
    tot = re.search(r"\| \*\*Total\*\* \| \*\*([\d,]+)\*\* \| \*\*([\d,]+)\*\* \|", body)
    if not tot:
        hits.append((rel, 0, "§1 inventory Total row not found"))
    else:
        g, pg = num(tot.group(1)), num(tot.group(2))
        if pdfs and g != len(pdfs):
            hits.append((rel, 0, f"§1 Total declares {g:,} guides but "
                                 f"ebs_docs/current/acrobat/ holds {len(pdfs):,} PDFs"))
        sg = sum(num(r[1]) for r in rows)
        sp = sum(num(r[3]) for r in rows)
        if sg != g or sp != pg:
            hits.append((rel, 0, f"§1 class rows sum to {sg:,} guides / {sp:,} pages but the "
                                 f"Total row declares {g:,} / {pg:,}"))
    # ---- (c) EDC contiguity + outcome arithmetic
    ids = [int(m) for m in re.findall(r"\*\*EDC-(\d+)\*\*", body)]
    if ids != list(range(1, len(ids) + 1)):
        hits.append((rel, 0, f"§4 EDC ids are not contiguous 1..N: {ids}"))
    adj_notadj_rec_opn = None
    m = re.search(r"\*\*Result: (\d+) of (\d+) products already adjudicated; (\d+) were not\.\*\* "
                  r"Of the \d+, (\d+) are\s+recorded not-needed in §5, and \*\*(\d+) are open gap rows",
                  re.sub(r"\s+", " ", body))
    if not m:
        hits.append((rel, 0, "§2 outcome sentence not found or not parseable"))
    else:
        adj, prod, notadj, rec, opn = (int(m.group(i)) for i in range(1, 6))
        adj_notadj_rec_opn = (adj, prod, notadj, rec, opn)
        if adj + notadj != prod:
            hits.append((rel, 0, f"§2 outcome: {adj} adjudicated + {notadj} not "
                                 f"!= {prod} products"))
        if rec + opn != notadj:
            hits.append((rel, 0, f"§2 outcome: {rec} recorded + {opn} open != {notadj} "
                                 f"un-adjudicated"))
        if opn != len(ids):
            hits.append((rel, 0, f"§2 declares {opn} open gap rows but §4 holds "
                                 f"{len(ids)} EDC rows"))
    # ---- (d) cited guide basenames must exist in the library
    have = {os.path.splitext(f)[0] for f in pdfs}
    for mm in re.finditer(r"`(122[a-z0-9]+|12[a-z0-9]{3,})`", body):
        stem = mm.group(1)
        if have and stem not in have:
            hits.append((rel, body[:mm.start()].count("\n") + 1,
                         f"cites guide `{stem}` -- no such PDF in "
                         f"ebs_docs/current/acrobat/"))
    # ---- (f) per-row page-count re-derivation — 2026-09-21 sixty-third-wave
    # review: every basename-cited '/ Np' form must equal the pdfinfo page sum of
    # the cited guides (the register's convention is combined per-product sums),
    # and an 'across k files' suffix must equal the cited-guide count. The defect
    # class: EDC-21's '(3 guides / 474p)' against a library that ships two HRMSi
    # Strategic Reporting guides (94p + 286p = 380p — 94 + 286 + 94 = 474, the
    # Deploy guide double-counted). The titleless per-row citations (EDC-15/16/18/
    # 19/21/22/24's guide names without basenames) stay outside the pdfinfo arm —
    # re-deriving those needs a page-1 title scan of all 376 PDFs per run — and
    # are pinned instead where defective (EDC-21, arm (g)).
    pcache = {}

    def pdf_pages(stem):
        if stem not in pcache:
            out = subprocess.run(["pdfinfo", os.path.join(lib, stem + ".pdf")],
                                 capture_output=True, text=True).stdout
            mm2 = re.search(r"Pages:\s+(\d+)", out)
            pcache[stem] = int(mm2.group(1)) if mm2 else None
        return pcache[stem]

    for mm in re.finditer(r"`(122[a-z0-9]+(?:`, `122[a-z0-9]+)*)` / ([\d,]+)p"
                          r"(?: across (\d+) files)?", body):
        gs = re.findall(r"122[a-z0-9]+", mm.group(1))
        cited = num(mm.group(2))
        try:
            actual = sum(pdf_pages(g) for g in gs)
        except Exception:
            continue  # a missing PDF is arm (d)'s finding
        if actual != cited:
            hits.append((rel, body[:mm.start()].count("\n") + 1,
                         f"cited {cited}p for {gs} but pdfinfo sums {actual}p "
                         f"(the register's convention is the combined per-product "
                         f"sum)"))
        if mm.group(3) and int(mm.group(3)) != len(gs):
            hits.append((rel, body[:mm.start()].count("\n") + 1,
                         f"cited 'across {mm.group(3)} files' for {gs}"))
    # ---- (g) the EDC-21 HRMSi citation — 2026-09-21 sixty-third-wave review:
    # the library ships exactly two HRMSi Strategic Reporting guides
    # (`122hrdsrig` 94p Deploy guide + `122hrdsrug` 286p user guide = 380p);
    # pin the corrected form and ban the double-counted one.
    edc21 = next((l for l in body.splitlines() if l.startswith("| **EDC-21** |")), "")
    if "2 guides / 380p" not in edc21:
        hits.append((rel, 0,
                     "EDC-21 must cite the library truth 'HRMSi Strategic Reporting "
                     "(2 guides / 380p)' (122hrdsrig 94p + 122hrdsrug 286p)"))
    if "3 guides / 474p" in body:
        hits.append((rel, body[:body.index("3 guides / 474p")].count("\n") + 1,
                     "retired EDC-21 citation '3 guides / 474p' (the Deploy guide "
                     "was double-counted: 94 + 286 + 94 = 474)"))
    # ---- (e) the §3 POS-confirmation row must state the library truthfully --
    # 2026-09-21 sixty-first-wave manuals sweep: the v1.0 confirmation 'No EBS
    # POS product exists in the library' was false as stated (Oracle Channel
    # Rebate and Point-of-Sale Management ships in the library), so the corrected
    # row must cite both crpos guides (arm (d) verifies they exist), must carry
    # the checkout-sense anchor, and the retired bare form is banned; the §5
    # not-needed record for the product must stay.
    pos_rows = [ln for ln in body.splitlines() if "No EBS POS" in ln]
    if len(pos_rows) != 1:
        hits.append((rel, 0, f"§3 holds {len(pos_rows)} POS-confirmation rows, "
                             f"expected exactly 1"))
    else:
        ln_i = body[:body.index(pos_rows[0])].count("\n") + 1
        if "`122crposig`" not in pos_rows[0] or "`122crposug`" not in pos_rows[0]:
            hits.append((rel, ln_i,
                         "POS-confirmation row does not cite the library's POS-named "
                         "guides (`122crposig`/`122crposug`)"))
        if "Channel Rebate" not in pos_rows[0]:
            hits.append((rel, ln_i,
                         "POS-confirmation row does not name the Channel Rebate & POS "
                         "product the library actually ships"))
        if "checkout" not in pos_rows[0]:
            hits.append((rel, ln_i,
                         "POS-confirmation row lost the checkout-sense anchor"))
    if "No EBS POS product exists in the library" in body:
        hits.append((rel, 0, "retired bare POS-absence form 'No EBS POS product "
                             "exists in the library' is back (the library ships "
                             "122crposig/122crposug — state the checkout sense)"))
    if not any(ln.startswith("| Oracle Channel Rebate and Point-of-Sale Management")
               for ln in body.splitlines()):
        hits.append((rel, 0, "§5 lost the Channel Rebate and Point-of-Sale "
                             "Management not-needed record"))
    # ---- (h) the §6 guard-note's arithmetic quote must track §2 — 2026-09-22
    # sixty-fifth-wave review: the §6 re-running note quoted the outcome
    # arithmetic as '(107 adjudicated + 33 recorded + 25 open = 165)' while §2's
    # own sentence had been restated at batch 27 (90 of 165; 50 recorded; 25
    # opened rows) — the derived-quote class; the parenthetical is re-derived
    # from §2's numbers every run so a future §2 re-statement re-fires until
    # the note is re-pointed.
    flat = re.sub(r"\s+", " ", body)
    m6 = re.search(r"\((\d+) adjudicated \+ (\d+) recorded \+ (\d+) opened EDC rows"
                   r" = ([\d,]+), all \d+ since closed\)", flat)
    if m6 and adj_notadj_rec_opn:
        adj, prod, notadj, rec, opn = adj_notadj_rec_opn
        q_adj, q_rec, q_opn, q_prod = (int(m6.group(i)) for i in range(1, 5))
        if (q_adj, q_rec, q_opn, q_prod) != (adj, rec, opn, prod):
            hits.append((rel, 0,
                         f"§6 guard-note arithmetic ({q_adj} + {q_rec} + {q_opn} = "
                         f"{q_prod}) disagrees with §2's own sentence ({adj} "
                         f"adjudicated + {notadj} un-adjudicated of {prod}, of which "
                         f"{rec} recorded + {opn} opened EDC rows) — re-point the "
                         f"derived quote"))
    elif not m6:
        hits.append((rel, 0,
                     "missing the §6 outcome-arithmetic anchor '(N adjudicated + "
                     "M recorded + K opened EDC rows = P, all K since closed)' — "
                     "the guard-note quote is required to track §2's own sentence"))
    return hits

def oratest_hits():
    """2026-09-21 oratest capability verification — structural guard for the
    rig capability report (02-oracle-ebs/ebs-oratest-verification.md; the
    vision_verification_hits precedent — a verification report joins the DOCS
    set with a rule that re-derives its own stated counts). Re-derives, every
    run:
      (a) the section skeleton (rig environment / FP x rig footprint / VT x rig
          transactional / OR findings / artifacts) must be complete;
      (b) the FP x rig table must hold exactly the pinned 39 conformance rows
          (unique ids, mirroring the Vision report's FP set) and the VT x rig
          table exactly 10 rows (unique ids);
      (c) the section-3 rig tally sentence must equal the count of VT rows whose
          verdict cell begins GREEN / PARTIAL (the vision_verification_hits
          self-consistency principle applied to the rig verdicts);
      (d) the required rig-evidence anchors must stay present (release 12.2.4,
          business group 81, the VT-9 employee marker 10029015, the VT-10 asset
          marker E2E-ERP-F-001 and posting request 76976818, the APXIIMPT
          history anchor); and the OR-1..OR-6 findings register must be
          complete."""
    rel = "ebs-oratest-verification.md"
    hits = []
    path = os.path.normpath(os.path.join(MC, "..", "02-oracle-ebs", rel))
    text = open(path, encoding="utf-8").read()
    body = strip_footer(text)
    for sec in ("## 1. Environment of record (rig)",
                "## 2. Footprint conformance on the rig (FP \u00d7 rig)",
                "## 3. Transactional cross-verification (VT \u00d7 rig)",
                "## 4. Findings and consistency dispositions",
                "## 5. Verification artifacts"):
        if sec not in body:
            hits.append((rel, 0, f"missing section '{sec}'"))
    fp = re.findall(r"^\| (FP-\d+) ", body, flags=re.M)
    vt = re.findall(r"^\| (VT-\d+) ", body, flags=re.M)
    if len(fp) != 39 or len(set(fp)) != len(fp):
        hits.append((rel, 0, f"FP x rig table holds {len(fp)} rows "
                             f"({len(set(fp))} unique) but the doc pins 39 unique rows"))
    if len(vt) != 10 or len(set(vt)) != len(vt):
        hits.append((rel, 0, f"VT x rig table holds {len(vt)} rows "
                             f"({len(set(vt))} unique) but the doc pins 10 unique rows"))
    green = len(re.findall(r"^\| VT-\d+ \|.*\| GREEN", body, flags=re.M))
    partial = len(re.findall(r"^\| VT-\d+ \|.*\| PARTIAL", body, flags=re.M))
    m = re.search(r"Rig tally: (\d+) GREEN \+ (\d+) PARTIAL of the 10 paths", body)
    if not m:
        hits.append((rel, 0, "section-3 tally sentence ('Rig tally: **N GREEN + M "
                             "PARTIAL of the 10 paths**') not found"))
    elif (int(m.group(1)), int(m.group(2))) != (green, partial):
        hits.append((rel, 0, f"section-3 tally claims {m.group(1)} GREEN + "
                             f"{m.group(2)} PARTIAL but the VT table holds "
                             f"{green} GREEN / {partial} PARTIAL"))
    for anc in ("12.2.4", "81 — CITIHARDWARE INC", "10029015", "E2E-ERP-F-001",
                "76976818", "APXIIMPT"):
        if anc not in body:
            hits.append((rel, 0, f'missing required rig-evidence anchor "{anc}"'))
    for i in range(1, 7):
        if f"OR-{i}" not in body:
            hits.append((rel, 0, f"missing finding OR-{i}"))
    return hits


def store_scope_hits():
    """2026-09-18 fifty-sixth-wave consistency review — guard for the
    store-layer role-scope true-up (the wave that made the store time-and-
    motion attribution honest):
      (a) the 9 unambiguous store-execution PA files carry the store roster
          title 'Customer Service Rep' everywhere — the HQ
          'Customer Service Representative' form (the 22-HC HQ register row)
          is retired there; store counter/desk cells resolving to the HQ
          bucket mispriced 1.65M h/yr of store demand;
      (b) 'Floor Associate' step role cells are retired repo-wide (uncharted
          vocabulary; the duties are Sales Associate work per the §12.1
          roster) — prose mentions stand per the sweep's own adjudication;
      (c) W562's store-daily LP routine executes as the Store Manager per the
          workflow's own no-dedicated-officer Owner clause — the 9 pure
          'LP Officer' Role (R) cells are retired (compound steps 1/9/12
          keep the officer);
      (d) the four dual-scope Frequency fields lead with the per-store figure
          the analyzer's documented cadence ladder parses — the retired
          network-total-first forms are forbidden."""
    hits = []
    wf = os.path.join(REPO, "01-model-company", "workflows")

    # (a) store-file CSR title form
    for rel in ("VS-07-store-operations/PA-07.1-store-daily-management.md",
                "VS-07-store-operations/PA-07.3-store-receiving-and-replenishment.md",
                "VS-08-pos-checkout/PA-08.1-transaction-processing.md",
                "VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md",
                "VS-09-in-store-services/PA-09.2-project-estimation-and-advisory.md",
                "VS-09-in-store-services/PA-09.3-customer-amenities-and-assistance.md",
                "VS-12-installation-services/PA-12.1-installation-and-repair-services.md",
                "VS-32-returns-reverse-logistics/PA-32.1-customer-returns-processing.md",
                "VS-78-green-building-advisory/PA-78.2-green-building-project-consultation.md"):
        text = open(os.path.join(wf, rel), encoding="utf-8").read()
        if "Customer Service Representative" in text:
            hits.append((rel, text[:text.index("Customer Service Representative")].count("\n") + 1,
                         'retired HQ title form "Customer Service Representative" in a '
                         'store-execution file (store roster title: "Customer Service Rep")'))
        if "Customer Service Rep" not in text:
            hits.append((rel, 0, 'missing store roster title "Customer Service Rep"'))

    # (b) Floor Associate role cells repo-wide (step-table rows only)
    step_row = re.compile(r"^\| \d+ \|")
    for vd in sorted(os.listdir(wf)):
        if not vd.startswith("VS-"):
            continue
        vd_path = os.path.join(wf, vd)
        for fn in sorted(os.listdir(vd_path)):
            if not (fn.startswith("PA-") and fn.endswith(".md")):
                continue
            for ln_no, ln in enumerate(open(os.path.join(vd_path, fn), encoding="utf-8"), 1):
                if step_row.match(ln) and "Floor Associate" in ln:
                    hits.append((fn, ln_no, 'retired "Floor Associate" step role cell '
                                             '(Sales Associate per the §12.1 roster)'))

    # (c) W562 pure LP Officer cells
    c1 = os.path.join(wf, "VS-07-store-operations/PA-07.1-store-daily-management.md")
    text = open(c1, encoding="utf-8").read()
    m = re.search(r"^## W562\..*$", text, flags=re.M)
    if not m:
        hits.append(("PA-07.1-store-daily-management.md", 0, "W562 block not found"))
    else:
        body = text[m.start():]
        block = body.split("\n## W")[0]
        pure = 0
        sm_cells = 0
        for ln in block.splitlines():
            sm = re.match(r"^\| (\d+) \|", ln)
            if not sm:
                continue
            if int(sm.group(1)) not in (2, 3, 4, 5, 6, 7, 8, 10, 11):
                continue
            # exact-cell match: descriptions may carry literal '|' characters,
            # so positional indexing is not row-safe here
            if re.search(r"\| LP Officer \|", ln):
                pure += 1
            elif re.search(r"\| Store Manager \|", ln):
                sm_cells += 1
        if pure:
            hits.append(("PA-07.1-store-daily-management.md", 0,
                         f"W562 store-daily LP routine: {pure} pure 'LP Officer' Role (R) "
                         f"cells (retired — Store Manager per the Owner's "
                         f"no-dedicated-officer clause)"))
        if sm_cells != 9:
            hits.append(("PA-07.1-store-daily-management.md", 0,
                         f"W562 expects 9 Store Manager routine cells, found {sm_cells}"))

    # (d) retired dual-scope frequency fragments
    retired_freq = [
        ("VS-07-store-operations/PA-07.2-store-facility-and-safety.md",
         "~400–600 incidents per month across 200 stores (~2–3 per store per month)"),
        ("VS-06-logistics-fleet/PA-06.1-outbound-distribution.md",
         "~500–600 DSD receipts/month across all stores (~2–3 DSD deliveries per store per month)"),
        ("VS-13-customer-experience/PA-13.3-customer-data-and-crm.md",
         "~400–600 visits per month (~2–3 visits per store per month)"),
        ("VS-07-store-operations/PA-07.4-store-staffing-and-people.md",
         "~1,200–1,600 new hires/year across 200 stores (~6–8 per store per year per profile §11.4)"),
    ]
    for rel, frag in retired_freq:
        text = open(os.path.join(wf, rel), encoding="utf-8").read()
        if frag in text:
            hits.append((rel, text[:text.index(frag)].count("\n") + 1,
                         'retired dual-scope Frequency form (lead with the per-store figure): '
                         '"' + frag[:50] + '…"'))
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


def gpl_sku_sweep_hits():
    """2026-09-23 -- structural guard for the Component-GPL sellable-SKU sweep
    (02-oracle-ebs/ebs-documentation-coverage.md §7). The §7 annex claims 'every priced
    part number on the GPL carries a recorded disposition' — the one quantitative claim
    no other rule re-derives — so it re-derives from the price-list PDF itself every run:
      (a) the part-number universe (every [A-Z][0-9]{4,6} token in the pdftotext text of
          applications-price-list-070574.pdf) — a missing PDF or extractor is a hit;
      (b) the §7 arithmetic sentence must state a total equal to that universe and must
          foot across its components (licensed + read-only-annotation + prior + annexed);
      (c) every backtick-quoted part number in §7 must exist on the GPL;
      (d) the flag pins: the four ⚠ rows (L11496, L72211, L31659, L42175) and the
          L72189 naming-collision item must be present in §7; and
      (e) the UPK band count stated in the annex must equal the band-priced part-number
          lines re-derived from the price list.
    """
    rel = "ebs-documentation-coverage.md"
    hits = []
    path = os.path.normpath(os.path.join(MC, "..", "02-oracle-ebs", rel))
    pdf = os.path.normpath(os.path.join(MC, "..", "applications-price-list-070574.pdf"))
    text = open(path, encoding="utf-8").read()
    body = text.split("*Document Version:")[0]
    if "## 7. The Component Global Price List sweep" not in body:
        hits.append((rel, 0, "§7 GPL sellable-SKU sweep section missing"))
        return hits
    sec7 = body.split("## 7. The Component Global Price List sweep", 1)[1]
    if not os.path.isfile(pdf):
        hits.append((rel, 0, "price-list PDF missing — the §7 sweep's source of record is gone"))
        return hits
    try:
        with tempfile.TemporaryDirectory() as td:
            out_txt = os.path.join(td, "gpl.txt")
            r = subprocess.run(["pdftotext", "-layout", pdf, out_txt],
                               capture_output=True, text=True, timeout=120)
            if r.returncode != 0:
                hits.append((rel, 0, "pdftotext failed over the price-list PDF"))
                return hits
            gpl = open(out_txt, encoding="utf-8", errors="replace").read()
    except (OSError, subprocess.SubprocessError):
        hits.append((rel, 0, "could not run pdftotext over the price-list PDF"))
        return hits
    universe = set(re.findall(r"\b[A-Z][0-9]{4,6}\b", gpl))
    if not universe:
        hits.append((rel, 0, "part-number universe empty — the price-list text parsed to nothing"))
        return hits
    flat = re.sub(r"\s+", " ", sec7)
    m = re.search(r"Result: the sweep accounts for all ([\d,]+) priced part numbers on the GPL: "
                  r"([\d,]+) licensed lines, ([\d,]+) "
                  r"Applications-Read-Only-User annotation parts, ([\d,]+) recorded at prior passes, "
                  r"([\d,]+) recorded in the table below \((\d+) named \+ (\d+) band-priced UPK modules\)"
                  r" — 0 unexamined", flat)
    if not m:
        hits.append((rel, 0, "§7 result sentence not found in its pinned form"))
    else:
        total, lic, ann, prior, tab, named, bands = (int(x.replace(",", "")) for x in m.groups())
        if total != len(universe):
            hits.append((rel, 0, f"§7 declares {total} priced part numbers but the GPL text "
                                 f"holds {len(universe)}"))
        if lic + ann + prior + tab != total or named + bands != tab:
            hits.append((rel, 0, f"§7 arithmetic does not foot: {lic}+{ann}+{prior}+{tab} "
                                 f"(!= {total}) or {named}+{bands} (!= {tab})"))
        m2 = re.search(r"(\d[\d,]*) band-priced UPK Module part numbers", flat)
        if not m2 or int(m2.group(1).replace(",", "")) != bands:
            hits.append((rel, 0, "§7 UPK-module row must restate the band count its arithmetic uses"))
        band_lines = [l for l in gpl.splitlines()
                      if re.search(r"\(over 4K|up to 4K", l)
                      and re.search(r"[A-Z][0-9]{4,6}\s*$", l.rstrip())]
        derived_bands = {re.findall(r"[A-Z][0-9]{4,6}\s*$", l.rstrip())[0] for l in band_lines}
        if bands != len(derived_bands):
            hits.append((rel, 0, f"§7 states {bands} band-priced UPK modules but the price list "
                                 f"holds {len(derived_bands)}"))
    have = universe
    for mm in re.finditer(r"`([A-Z][0-9]{4,6})`", sec7):
        stem = mm.group(1)
        if stem not in have:
            hits.append((rel, body[:mm.start()].count("\n") + 1,
                         f"§7 cites part `{stem}` — no such part number on the price list"))
    for pin in ("L11496", "L72211", "L31659", "L42175", "L72189"):
        if f"`{pin}`" not in sec7:
            hits.append((rel, 0, f"§7 flag pin `{pin}` missing — the sweep's ⚠/collision items "
                                 f"must stay on the record"))
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
    # 2026-09-17 fifty-third-wave consistency review addition (licensing BOM)
    hits.extend(licensing_bom_hits())
    # 2026-09-17 fifty-fourth-wave consistency review addition (Vision verification report)
    hits.extend(vision_verification_hits())
    # 2026-09-18 fifty-fifth-wave consistency review additions
    hits.extend(gap_fill_straggler_hits())
    hits.extend(quote_coverage_hits())
    # 2026-09-18 fifty-sixth-wave consistency review addition (store role scope)
    hits.extend(store_scope_hits())
    # 2026-09-21 oratest capability verification addition (rig capability report)
    hits.extend(oratest_hits())
    hits.extend(ebs_doc_coverage_hits())
    # 2026-09-23 Component-GPL sellable-SKU sweep addition (coverage register §7)
    hits.extend(gpl_sku_sweep_hits())
    # 2026-09-23 sixty-sixth-wave consistency review addition (calibration volumes)
    hits.extend(calibrated_volume_hits())
    # 2026-09-23 seventy-fifth-wave consistency review addition (the A6.6 Atlassian canon)
    hits.extend(atlassian_suite_hits())
    # 2026-09-23 seventy-sixth-wave consistency review addition (batch-30 census
    # stragglers: VS-index banner/footer, canon §1, domain companions)
    hits.extend(domain_companion_hits())
    for doc, line, detail in hits:
        print(f"model-doc: {doc}:{line}: {detail}")
    print(f"audit-model-docs: {len(hits)} hit(s) across {len(DOCS)} documents")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
