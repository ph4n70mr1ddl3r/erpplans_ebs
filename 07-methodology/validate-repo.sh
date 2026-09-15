#!/bin/bash
# validate-repo.sh — Cross-reference validation for BuildRight Depot ERP Plans
# Checks consistency of workflow counts, requirement IDs, cross-references, and table structure

set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ERRORS=0
WARNINGS=0

RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m'

error() { echo -e "${RED}ERROR${NC}: $1"; ERRORS=$((ERRORS + 1)); }
warn()  { echo -e "${YELLOW}WARN${NC}: $1"; WARNINGS=$((WARNINGS + 1)); }
ok()    { echo -e "${GREEN}OK${NC}: $1"; }

echo "=== BuildRight Depot ERP Plans — Validation ==="
echo ""

# --- Check 1: Workflow IDs in PA files that are NOT in criticality classification ---
echo "--- Check 1: Unclassified workflow headers ---"
# Primary workflows are ## (h2) headers; a small number of ### (h3) parent/summary
# sub-workflows (e.g. W9A) also receive their own classification row. The documented
# unclassified total = grand_total − classified table rows, used consistently repo-wide.
# We (a) report that documented figure and (b) verify every classified ID resolves to a
# real workflow header in a PA file (catching stale classification references).
CLASSIFIED=$(grep -oP '^\| (W\d+[A-Z]?) \|' "$REPO_ROOT"/01-model-company/workflows/workflow-criticality-classification.md | sed -E 's/^\| //;s/ \|$//' | sort -u)
CLASSIFIED_COUNT=$(echo "$CLASSIFIED" | grep -cP '^W' || true)
# Grand-total cell is comma-formatted (e.g. "4,596"); strip commas before arithmetic.
GRAND_TOTAL=$(grep 'Grand Total' "$REPO_ROOT"/01-model-company/workflows/value-stream-index.md | grep -oP '\d[\d,]*' | tail -1 | tr -d ',')
DOC_UNCLASS=$((GRAND_TOTAL - CLASSIFIED_COUNT))

ALL_HEADERS=$(grep -rohP '^#{2,3} W\d+[A-Z]?\.' "$REPO_ROOT"/01-model-company/workflows/VS-*/*.md 2>/dev/null | sed -E 's/^#{2,3} //;s/\.$//' | sort -u)
STALE_CLASSIFIED=$(comm -23 <(echo "$CLASSIFIED") <(echo "$ALL_HEADERS") | grep -cP '^W' || true)
SUB_CLASSIFIED=$(comm -12 <(grep -rohP '^### W\d+[A-Z]?\.' "$REPO_ROOT"/01-model-company/workflows/VS-*/*.md 2>/dev/null | sed -E 's/^### //;s/\.$//' | sort -u) <(echo "$CLASSIFIED") | grep -cP '^W' || true)

echo "  Classified register rows: $CLASSIFIED_COUNT (incl. $SUB_CLASSIFIED parent/summary sub-workflow rows → $((CLASSIFIED_COUNT - SUB_CLASSIFIED)) unique workflows classified) | Grand total (unique workflows): $GRAND_TOTAL"

if [ "$STALE_CLASSIFIED" -eq 0 ]; then
    ok "All $CLASSIFIED_COUNT classified workflow IDs resolve to a header in a PA file"
else
    error "$STALE_CLASSIFIED classified ID(s) do not match any workflow header in PA files"
fi

if [ "$DOC_UNCLASS" -gt 0 ]; then
  PROPOSED_FILE="$REPO_ROOT"/01-model-company/workflows/workflow-criticality-proposed.md
  # Real unclassified = ## headers not present in the confirmed register
  UNCLASSIFIED_IDS=$(comm -23 <(echo "$ALL_HEADERS") <(echo "$CLASSIFIED") | grep -P '^W' || true)
  UNCLASSIFIED_COUNT=$(echo "$UNCLASSIFIED_IDS" | grep -cP '^W' || true)
  if [ -f "$PROPOSED_FILE" ]; then
    PROPOSED_IDS=$(grep -oP '^\| W\d+[A-Z]? \|' "$PROPOSED_FILE" | sed -E 's/^\| //;s/ \|//' | sort -u)
    PROPOSED_COUNT=$(echo "$PROPOSED_IDS" | grep -cP '^W' || true)
    WITHOUT_PROPOSAL=$(comm -23 <(echo "$UNCLASSIFIED_IDS") <(echo "$PROPOSED_IDS") | grep -cP '^W' || true)
    warn "$UNCLASSIFIED_COUNT workflows remain unclassified in the confirmed register; $PROPOSED_COUNT have a keyword-driven proposed tier (workflow-criticality-proposed.md); $WITHOUT_PROPOSAL have no proposal yet"
    PROPOSED_DANGLING=$(comm -23 <(echo "$PROPOSED_IDS") <(echo "$ALL_HEADERS") | grep -cP '^W' || true)
    PROPOSED_DUP=$(comm -12 <(echo "$PROPOSED_IDS") <(echo "$CLASSIFIED") | grep -cP '^W' || true)
    if [ "$PROPOSED_DANGLING" -eq 0 ] && [ "$PROPOSED_DUP" -eq 0 ]; then
      ok "All $PROPOSED_COUNT proposed IDs resolve to headers and do not duplicate the confirmed register"
    else
      error "Proposed classification: $PROPOSED_DANGLING dangling, $PROPOSED_DUP duplicate(s) of confirmed register"
    fi
  else
    warn "$UNCLASSIFIED_COUNT workflows remain unclassified (pending criticality review)"
  fi
fi

# --- Check 2: Workflow counts per PA file match value-stream-index ---
echo "--- Check 2: PA workflow counts ---"
PA_FILES=$(find "$REPO_ROOT"/01-model-company/workflows -name "PA-*.md" -type f 2>/dev/null)
while IFS= read -r pafile; do
    HEADER_COUNT=$(grep -cP '^## W\d+[A-Z]?\.' "$pafile" 2>/dev/null || true)
    PA_NAME=$(basename "$pafile" .md)
    VS_NAME=$(basename "$(dirname "$pafile")")
    INDEX_COUNT=$(grep -P "\\Q$PA_NAME\\E" "$REPO_ROOT"/01-model-company/workflows/value-stream-index.md 2>/dev/null | grep -oP '\d+ workflows' | grep -oP '\d+' || echo "0")
    if [ "$HEADER_COUNT" != "$INDEX_COUNT" ] && [ "$INDEX_COUNT" != "0" ]; then
        warn "$VS_NAME/$PA_NAME: file has $HEADER_COUNT workflow headers, index says $INDEX_COUNT"
    fi
done <<< "$PA_FILES"
ok "PA workflow count checks complete"

# --- Check 3: Cross-reference key figures ---
echo "--- Check 3: Key figure consistency ---"
# Check total workflows in value-stream-index (cell is comma-formatted, e.g. "4,596")
TOTAL_VS=$(grep 'Grand Total' "$REPO_ROOT"/01-model-company/workflows/value-stream-index.md | grep -oP '\d[\d,]*' | tail -1 | tr -d ',')
README_TOTAL=$(grep -oP '1,\d{3}' "$REPO_ROOT"/README.md | head -1)
if [ -n "$TOTAL_VS" ]; then
    ok "Value stream index total: $TOTAL_VS workflows"
else
    error "Could not find grand total in value-stream-index.md"
fi

# Check requirement count
REQ_COUNT=$(grep -cP '^\| [A-Z]+-\d+' "$REPO_ROOT"/01-model-company/erp-requirements.md 2>/dev/null || true)
echo "  Requirements found in erp-requirements.md: $REQ_COUNT"

# Check controls count
CTL_COUNT=$(grep -cP '^\| CTL-' "$REPO_ROOT"/01-model-company/internal-controls-matrix.md 2>/dev/null || true)
echo "  Controls found in internal-controls-matrix.md: $CTL_COUNT"

# --- Check 4: Requirement IDs in matrix vs erp-requirements ---
echo "--- Check 4: Requirement-Workflow matrix consistency ---"
# Match only requirement IDs that begin a table row (|^REQ-XX |) so day-offset tokens
# like "T-7"/"T-14" or "VS-49" in footer prose are not mistaken for requirement IDs.
MATRIX_REQS=$(grep -ohP '^\| [A-Z]{2,}-\d+[a-z]? \|' "$REPO_ROOT"/01-model-company/requirement-workflow-matrix.md | sed -E 's/^\| //;s/ \|$//' | sort -u | wc -l)
REQ_DEFINED=$(grep -cP '^\| [A-Z]+-\d+' "$REPO_ROOT"/01-model-company/erp-requirements.md 2>/dev/null || true)
echo "  Requirement IDs in matrix table rows: $MATRIX_REQS | defined in erp-requirements.md: $REQ_DEFINED"

# --- Check 5: Empty process areas ---
echo "--- Check 5: Empty process areas ---"
EMPTY=$(grep -r "no workflows yet" "$REPO_ROOT"/01-model-company/workflows/ --include="*.md" 2>/dev/null || true)
if [ -z "$EMPTY" ]; then
    ok "No empty process areas found"
else
    warn "Empty process areas found:"
    echo "$EMPTY"
fi

# --- Check 6: W-numbers in requirement-workflow matrix that don't exist in PA files ---
echo "--- Check 6: Matrix workflow references ---"
# Include letter-suffixed sub-workflow IDs (W<number><letter>) via the [A-Z]? qualifier
MATRIX_WFS=$(grep -ohP '\bW\d{1,4}[A-Z]?\b' "$REPO_ROOT"/01-model-company/requirement-workflow-matrix.md | sort -u)
PA_ALL=$(grep -ohP '\bW\d{1,4}[A-Z]?\b' "$REPO_ROOT"/01-model-company/workflows/VS-*/*.md | sort -u)
MISSING=$(comm -23 <(echo "$MATRIX_WFS") <(echo "$PA_ALL") | head -20)
MISSING_COUNT=$(comm -23 <(echo "$MATRIX_WFS") <(echo "$PA_ALL") | wc -l)
if [ "$MISSING_COUNT" -le 5 ]; then
    ok "Only $MISSING_COUNT matrix W-references not found in PA files (parent/summary workflows)"
else
    warn "$MISSING_COUNT W-numbers in requirement-workflow matrix not found in PA file headers"
    echo "  First 10: $(echo "$MISSING" | head -10 | tr '\n' ' ')"
fi

# --- Check 7: Dangling workflow references in cross-reference docs ---
echo "--- Check 7: Dangling workflow references ---"
# All workflow IDs actually defined as a header (## or ###) in any PA file
DEFINED_WFS=$(grep -rohP '^#{2,3} W\d+[A-Z]?\.' "$REPO_ROOT"/01-model-company/workflows/VS-*/*.md 2>/dev/null | sed -E 's/^#{2,3} //;s/\.$//' | sort -u)
DANGLING_TOTAL=0
for doc in \
  "$REPO_ROOT"/01-model-company/workflows/workflow-dependency-map.md \
  "$REPO_ROOT"/01-model-company/workflows/workflow-system-touchpoint-map.md \
  "$REPO_ROOT"/01-model-company/requirement-workflow-matrix.md \
  "$REPO_ROOT"/01-model-company/internal-controls-matrix.md; do
  REFS=$(grep -ohP '\bW\d{1,4}[A-Z]?\b' "$doc" 2>/dev/null | sort -u)
  DANGLING=$(comm -23 <(echo "$REFS") <(echo "$DEFINED_WFS") | grep -P '^W' || true)
  DANGLING_COUNT=$(echo "$DANGLING" | grep -cP '^W' || true)
  DANGLING_TOTAL=$((DANGLING_TOTAL + DANGLING_COUNT))
  if [ "$DANGLING_COUNT" -eq 0 ]; then
    ok "$(basename "$doc"): no dangling workflow references"
  else
    error "$(basename "$doc"): $DANGLING_COUNT dangling workflow reference(s): $(echo "$DANGLING" | tr '\n' ' ')"
  fi
done

# --- Check 11: Dependency-map Tier-1 chain claims must be classified as Tier 1 ---
echo "--- Check 11: Dependency-map deepest-chain Tier-1 consistency ---"
# The dependency map declares a 'deepest dependency chain (all Tier 1)' with a stated
# total. Two reverse checks: (a) the count of unique workflow IDs in that block must
# equal the stated total; (b) every workflow in that block must be present in the
# Tier 1 section of the classification file. This catches drift like a Tier-1-claimed
# workflow that was never classified (regression that Check 1 cannot detect, because
# Check 1 only proves classified -> header, not dependency-claim -> classified).
DEPMAP="$REPO_ROOT"/01-model-company/workflows/workflow-dependency-map.md
TIER1_CHAIN=$(awk '/### Tier 1: Deepest Dependency Chain/{f=1;next} f&&/^### /{exit} f' "$DEPMAP" | grep -oP '\bW\d+[A-Z]?\b' | sort -u)
TIER1_CHAIN_COUNT=$(echo "$TIER1_CHAIN" | grep -cP '^W' || true)
STATED_TOTAL=$(grep -oP 'deepest dependency chain \(all Tier 1\)|Total\*\*: \K\d+(?= workflows in the deepest dependency chain)' "$DEPMAP" | head -1)
TIER1_SECTION=$(awk '/^## Tier 1: Core Operations/{f=1;next} f&&/^## Tier 2:/{f=0} f' "$REPO_ROOT"/01-model-company/workflows/workflow-criticality-classification.md)
TIER1_SECTION="$TIER1_SECTION\n$(awk '/^### Tier 1 Additions/{f=1;next} f&&/^### /{exit} f' "$REPO_ROOT"/01-model-company/workflows/workflow-criticality-classification.md)"
CHAIN_NOT_CLASSIFIED=$(echo "$TIER1_CHAIN" | while IFS= read -r w; do
  [ -n "$w" ] && grep -qP "^\| $w \|" <<< "$TIER1_SECTION" || echo "$w"
done)
CHAIN_NOT_CLASSIFIED_COUNT=$(echo "$CHAIN_NOT_CLASSIFIED" | grep -cP '^W' || true)
if [ -n "$STATED_TOTAL" ] && [ "$STATED_TOTAL" -eq "$TIER1_CHAIN_COUNT" ]; then
  ok "Deepest-chain total ($STATED_TOTAL) matches unique workflow count ($TIER1_CHAIN_COUNT)"
else
  error "Deepest-chain stated total ($STATED_TOTAL) != unique workflow count ($TIER1_CHAIN_COUNT)"
fi
if [ "$CHAIN_NOT_CLASSIFIED_COUNT" -eq 0 ]; then
  ok "All $TIER1_CHAIN_COUNT deepest-chain workflows are classified Tier 1"
else
  error "$CHAIN_NOT_CLASSIFIED_COUNT deepest-chain workflow(s) not classified Tier 1: $(echo "$CHAIN_NOT_CLASSIFIED" | tr '\n' ' ')"
fi

# --- Check 8: Placeholder/skeleton workflow content ---
echo "--- Check 8: Placeholder workflow content ---"
# Detect auto-generated placeholder workflows. Markers (any one indicates a stub):
#   - H1 header starting with "# PA-X.Y](..."  (broken markdown from a failed generator run)
#   - Generic workflow title pattern "Workflow NNNN — N Process N"
#   - Generic trigger "Process trigger"
#   - Generic 3-step body "Execute standard process step"
#   - Generic pain point "Standard operational risks mitigated by procedural controls"
PLACEHOLDER_FILES=$(grep -rlP '^# PA-\d+\.\d+\]\(|Workflow \d+ — \d+ Process \d|\*\*Trigger\*\* \| Process trigger \|Execute standard process step|Standard operational risks mitigated by procedural controls' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null || true)
PLACEHOLDER_COUNT=$(echo -n "$PLACEHOLDER_FILES" | grep -cP 'PA-' || true)

if [ "$PLACEHOLDER_COUNT" -eq 0 ]; then
    ok "No placeholder/skeleton workflow files detected"
else
    error "$PLACEHOLDER_COUNT PA file(s) contain placeholder workflow content:"
    echo "$PLACEHOLDER_FILES" | sed 's/^/    /' | head -20
fi

# --- Check 9: Grand total in value-stream-index matches actual PA file count ---
echo "--- Check 9: Grand total vs actual workflow count ---"
# Grand-total cell is comma-formatted (e.g. "4,596"); strip commas before comparison.
GRAND_TOTAL=$(grep 'Grand Total' "$REPO_ROOT"/01-model-company/workflows/value-stream-index.md | grep -oP '\d[\d,]*' | tail -1 | tr -d ',')
ACTUAL_WFS=$(grep -rhP '^## W\d+[A-Z]?\.' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l)
if [ "$GRAND_TOTAL" = "$ACTUAL_WFS" ]; then
    ok "Grand total ($GRAND_TOTAL) matches actual PA workflow header count ($ACTUAL_WFS)"
else
    error "Grand total ($GRAND_TOTAL) does NOT match actual PA workflow header count ($ACTUAL_WFS)"
fi

# --- Check 10: Boilerplate analysis fields (regression guard) ---
echo "--- Check 10: Boilerplate analysis fields ---"
# The Expansion block (VS-53..VS-78) was originally generated from a template whose three
# value-delivering analysis fields — Pain Points, System Touchpoints, and Time Estimate — were
# verbatim boilerplate copied across every workflow. A 2026-06-20 rework rewrote all 22
# templated value streams to workflow-specific content, so this check now passes; it is
# retained as a regression guard that surfaces any boilerplate reintroduced by a future
# generation artifact. See WORKFLOW-FORMAT-GUIDE.md "Quality bar for the three analysis fields".
BP_MARKER='Operational variability mitigated by standard procedures and system controls'
BP_FILES=$(grep -rlF "$BP_MARKER" "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null || true)
BP_INSTANCES=$(grep -rhF "$BP_MARKER" "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l | tr -d ' ' || true)
if [ "$BP_INSTANCES" -eq 0 ]; then
    ok "No boilerplate analysis fields detected"
else
    BP_FILE_COUNT=$(echo -n "$BP_FILES" | grep -cP 'PA-' || true)
    BP_VS_LIST=$(echo "$BP_FILES" | sed -E 's#.*/(VS-[0-9]+-[^/]+)/.*#\1#' | sort -u)
    BP_VS_COUNT=$(echo -n "$BP_VS_LIST" | grep -cP '^VS-' || true)
    warn "$BP_INSTANCES workflows across $BP_FILE_COUNT PA files in $BP_VS_COUNT value streams use verbatim boilerplate for Pain Points / System Touchpoints / Time Estimate (regression — the 2026-06-20 Expansion-block rework removed all known boilerplate; see WORKFLOW-FORMAT-GUIDE.md):"
    echo "$BP_VS_LIST" | sed 's/^/    /'
fi

# --- Check 12: Automation Opportunity + Controls field adoption ---
echo "--- Check 12: Automation Opportunity & Controls field adoption ---"
# Per WORKFLOW-FORMAT-GUIDE.md these are now standard analysis fields for any fully-detailed
# workflow. Each should appear as an ### subsection under its workflow. Adoption is tracked
# (not enforced as an error) so progress across the Core, Statutory, and early gap-analysis
# (VS-89–VS-132) blocks — which predate these fields — can be measured against the VS-73
# reference implementation.
TOTAL_WF=$(grep -rhP '^## W\d+[A-Z]?\.' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l | tr -d ' ')
AUTO_COUNT=$(grep -rohP '^### Automation Opportunity$' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l | tr -d ' ')
CTRL_COUNT=$(grep -rohP '^### Controls$' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l | tr -d ' ')
if [ "$AUTO_COUNT" -eq "$TOTAL_WF" ] && [ "$CTRL_COUNT" -eq "$TOTAL_WF" ]; then
    ok "Automation Opportunity and Controls headers are present on all $TOTAL_WF workflows (100% presence — content quality tracked by Check 21)"
else
    warn "Automation Opportunity present on $AUTO_COUNT / $TOTAL_WF workflows ($(awk "BEGIN{printf \"%.0f\", ($AUTO_COUNT/$TOTAL_WF)*100}")%); Controls present on $CTRL_COUNT / $TOTAL_WF workflows ($(awk "BEGIN{printf \"%.0f\", ($CTRL_COUNT/$TOTAL_WF)*100}")%). Target: 100% on all workflows (see WORKFLOW-FORMAT-GUIDE.md 'Standard analysis fields')"
    echo "  Note: Check W641–W647 formatting in VS-19 if any are missing or deviate from the standard '###' header structure."
fi

# --- Check 13: Markdown table structural integrity ---
echo "--- Check 13: Markdown table structural integrity ---"
# Two regressions that silently garble rendered tables without breaking any plain-text count
# elsewhere in this script:
#  (a) a table data row whose opening '|' is preceded by whitespace (e.g. '  | [VS-136]...')
#      shifts every column right by one — this corrupted 27 value-stream-index.md architecture
#      rows in the gap-analysis block before detection. Repo convention: every table row starts
#      at column 0 with '|'.
#  (b) within a table, a data row whose unescaped-pipe count differs from the header row
#      (missing/extra trailing pipe, a step number merged into the description cell, or an
#      unescaped '|' inside a cell). '\|' is treated as a literal escaped pipe, per CommonMark.
SUMMARY_DOCS="$REPO_ROOT/README.md $REPO_ROOT/01-model-company/*.md $REPO_ROOT/01-model-company/workflows/*.md $REPO_ROOT/07-methodology/*.md"
LEADING_WS=$(grep -rlP '^ +\|' $SUMMARY_DOCS 2>/dev/null || true)
LEADING_WS_COUNT=$(echo -n "$LEADING_WS" | grep -cP '\.md' || true)
if [ "$LEADING_WS_COUNT" -eq 0 ]; then
    ok "No table rows with leading whitespace before the opening '|' (column-shift risk)"
else
    error "$LEADING_WS_COUNT doc(s) have table rows with leading whitespace before '|' (column-shift risk):"
    echo "$LEADING_WS" | sed 's/^/    /'
fi
COL_MISMATCH=$(awk '
FNR==1{intable=0;hdr=0;prev=""}
function ncells(s){ t=s; gsub(/\\[|]/,"",t); return gsub(/[|]/,"",t)-1 }
{
  if ($0 ~ /^[|]/) {
    if ($0 ~ /^\|[[:space:]:|-]+\|$/) { hdr=ncells(prev); intable=1; next }
    if (intable) { c=ncells($0); if(hdr>0 && c!=hdr) printf "%s:%d header=%d row=%d: %.50s\n",FILENAME,FNR,hdr,c,$0 }
    prev=$0; next
  }
  intable=0; hdr=0; prev=""
}' $SUMMARY_DOCS 2>/dev/null)
COL_MISMATCH_COUNT=$(echo -n "$COL_MISMATCH" | grep -cP ':' || true)
if [ "$COL_MISMATCH_COUNT" -eq 0 ]; then
    ok "All summary-doc table rows match their header column count"
else
    error "$COL_MISMATCH_COUNT summary-doc table row(s) have a column count differing from their header:"
    echo "$COL_MISMATCH" | sed 's/^/    /' | head -20
fi

# --- Check 14: Templated doubled-word pain-point labels ("X-risk risk") ---
echo "--- Check 14: Templated doubled-word pain-point labels ---"
# A content-generation artifact left 12 Pain Points bullets of the form
#   - **<Word>-risk risk**: ...
# across the gap-analysis block (VS-99/107/114/116/121/123/130/135): the template appended
# the noun "risk" after a descriptor that already ended in "-risk". The sibling bullets in
# every affected file use the form "**<compound-modifier> risk**:" (e.g. "Strategy-misalignment
# risk"), so this regex catches the drift unambiguously with no false positives (proper nouns
# like the Philippine "Build Build Build" program are excluded by the required "-risk risk"
# / " risk risk" suffix). Scans every PA file's bold pain-point label.
DOUBLED_RISK=$(grep -rnP '\*\*[A-Za-z][A-Za-z-]*[- ]risk risk\b' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null || true)
DOUBLED_RISK_COUNT=$(echo -n "$DOUBLED_RISK" | grep -cP 'PA-' || true)
if [ "$DOUBLED_RISK_COUNT" -eq 0 ]; then
    ok "No templated '**X-risk risk**' pain-point labels detected"
else
    error "$DOUBLED_RISK_COUNT PA file(s) contain a templated '**<word>-risk risk**' pain-point label:"
    echo "$DOUBLED_RISK" | sed 's/^/    /' | head -20
fi

# --- Check 15: Analysis-field header canonicalization ---
echo "--- Check 15: Analysis-field header canonicalization ---"
# WORKFLOW-FORMAT-GUIDE.md canonicalizes the analysis subsection headers. This check guards the
# three that have NO legitimate variant form in the repo, so the Check 12 adoption counts stay
# trustworthy and the typo/synonym class cannot recur undetected:
#   '### Automation Opportunity'  — guarded (a 2026-06-20 review found 8 VS-161 '### Automation Option' typos)
#   '### Controls'                — guarded
#   '### Pain Points / Risks'     — guarded (a 2026-06-20 review found 2 VS-10 '### Risks & Exceptions' synonyms)
# NOT guarded: '### Steps', '### System Touchpoints', '### Time Estimate', '### Cross-references' — these have
# legitimate parenthetically-qualified sub-forms (e.g. '### System Touchpoints (Yard)') used as per-sub-area
# labels inside complex workflows; normalizing them would create duplicate headers and destroy semantics.
BAD_AUTO=$(grep -rnP '^### Automation(?! Opportunity$)' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null || true)
BAD_CTRL=$(grep -rnP '^### Control(?!s$)' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null || true)
BAD_RISK=$(grep -rnP '^### .*Risk' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | grep -vP '### Pain Points / Risks( \(|$)' || true)
BAD_COUNT=$(echo -n "$BAD_AUTO"$'\n'"$BAD_CTRL"$'\n'"$BAD_RISK" | grep -cP 'PA-' || true)
if [ "$BAD_COUNT" -eq 0 ]; then
    ok "All Automation/Controls/Pain-Points analysis-field headers use the canonical exact form"
else
    error "$BAD_COUNT non-canonical analysis-field header(s) (should be '### Automation Opportunity' / '### Controls' / '### Pain Points / Risks') — invisible to Check 12's adoption count:"
    echo "$BAD_AUTO" | sed 's/^/    /' | head -20
    echo "$BAD_CTRL" | sed 's/^/    /' | head -20
    echo "$BAD_RISK" | sed 's/^/    /' | head -20
fi

# --- Check 16: PA file footer format ---
echo "--- Check 16: PA file footer format ---"
# WORKFLOW-FORMAT-GUIDE.md and the established convention (493+ PA files) require every PA file to
# END with the standardized navigation footer:
#   *Workflow Count: N · Back to **[VS-NN: <Name>](./README.md)** · [Value Stream Index](../value-stream-index.md)*
# A 2026-06-20 review found 30 PA files in VS-168–VS-177 (Pass 21–25) that deviated — 18 had a
# simpler '*Back to [VS-NN README]*' footer and 12 had NO footer at all — and 50 Core-block files
# (VS-01–VS-31) with duplicate (2–3) mid-file footer lines from a generation artifact. This check
# flags any PA whose last non-empty line is not the standardized footer, so the format cannot drift.
BAD_FOOTER=$(for pafile in "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md; do
  last=$(grep -vE '^[[:space:]]*$' "$pafile" | tail -1)
  echo "$last" | grep -qP '^\*Workflow Count: \d+ · Back to \*\*\[VS-\d+: .+\]\(\./README\.md\)\*\* · \[Value Stream Index\]\(\.\./value-stream-index\.md\)\*$' || echo "$pafile"
done)
BAD_FOOTER_COUNT=$(echo -n "$BAD_FOOTER" | grep -cP 'PA-' || true)
if [ "$BAD_FOOTER_COUNT" -eq 0 ]; then
    ok "All PA files end with the standardized navigation footer (shape arm)"
else
    error "$BAD_FOOTER_COUNT PA file(s) do not end with the standardized footer (*Workflow Count: N · Back to... · Value Stream Index*):"
    echo "$BAD_FOOTER" | sed 's#.*/workflows/##' | sed 's/^/    /' | head -20
fi
# ---- Part B: the footer's figures are re-derived every run (2026-09-14 twenty-seventh-wave
# consistency review). The shape arm above matches the count and the VS label only positionally
# ('\d+' / '.+'), so a stale Workflow-Count number, a wrong VS-number or a drifted VS-name on the
# 569 footers was read by no check (Checks 2/24/31/44/67/68 re-derive the index, README, tree and
# VS-README surfaces; Check 20 resolves the footer's relative link targets — ./README.md always
# resolves — but nothing compared its printed figures). Verified before arming by synthetic
# injection: a footer count drift (22 → 21) and a VS-name drift ('Merchandise Strategy' →
# 'Merchandising Strategy') both passed the full validator 0/0 exit 0. Every figure is re-derived
# from the primary sources: the count against the file's own '## W' headers, the VS-number against
# the folder name, and the VS-name against the canonical value-stream-index row for that VS.
C16_FIG=$(python3 - "$REPO_ROOT" <<'PY'
import glob, os, re, sys
ROOT = sys.argv[1]
WF = os.path.join(ROOT, "01-model-company", "workflows")
canon = {}
for line in open(os.path.join(WF, "value-stream-index.md"), encoding="utf-8"):
    m = re.match(r"^\|\s*[^|]*\|\s*\[(VS-\d+)\]\((VS-\d+-[a-z0-9-]+)/README\.md\) \| ([^|]+) \|", line)
    if m:
        canon[m.group(2)] = m.group(3).strip()
bad = []
if len(canon) != 188:
    bad.append(f"value-stream-index parse: {len(canon)} summary-table rows carry a VS link (expected 188)")
for pafile in sorted(glob.glob(os.path.join(WF, "VS-*", "PA-*.md"))):
    folder = os.path.basename(os.path.dirname(pafile))
    txt = open(pafile, encoding="utf-8").read()
    lines = [l for l in txt.splitlines() if l.strip()]
    m = re.match(r"^\*Workflow Count: (\d+) · Back to \*\*\[VS-(\d+): ([^\]]+)\]\(\./README\.md\)\*\* · \[Value Stream Index\]\(\.\./value-stream-index\.md\)\*$", lines[-1]) if lines else None
    if not m:
        continue  # shape drift already flagged by the arm above
    n, vsnum, vsname = int(m.group(1)), "VS-" + m.group(2), m.group(3)
    rel = os.path.relpath(pafile, WF)
    n_hdr = len(re.findall(r"^## W\d+[A-Z]?\.", txt, re.M))
    if n != n_hdr:
        bad.append(f"{rel}: footer says Workflow Count: {n}, the file defines {n_hdr} '## W' headers")
    if not folder.startswith(vsnum + "-"):
        bad.append(f"{rel}: footer VS number {vsnum} disagrees with folder {folder}")
    elif folder in canon and vsname != canon[folder]:
        bad.append(f"{rel}: footer VS name {vsname!r} != canonical value-stream-index name {canon[folder]!r}")
print(f"HITS {len(bad)}")
for b in bad:
    print("BAD|" + b)
PY
)
C16_FIG_BAD=$(echo "$C16_FIG" | sed -n 's/^HITS \([0-9]*\)$/\1/p')
if [ "${C16_FIG_BAD:-1}" -eq 0 ]; then
    ok "All PA footers carry re-derived figures: Workflow Count equals the file's own '## W'-header count (569 files), every VS-number matches its folder and every VS-name matches the canonical value-stream-index row (figure arm added by the 2026-09-14 twenty-seventh-wave consistency review after synthetic injections proved a footer count drift and a VS-name drift both pass the full validator 0/0 — Check 16 validated the footer's shape only)"
else
    error "$C16_FIG_BAD PA footer figure drift(s) (count vs the file's own '## W' headers / VS-number vs folder / VS-name vs the canonical index row):"
    echo "$C16_FIG" | grep '^BAD|' | sed 's/^BAD|/    /' | head -20
fi

# --- Check 17: Orphan workflow bodies (ghost workflows) ---
echo "--- Check 17: Orphan workflow bodies (ghost workflows) ---"
# A ghost workflow is a complete workflow body (Trigger/Owner/Steps table) sitting inside a ## W
# block with NO introducing ### header — neither a '### W<num><letter>.' sub-workflow header nor
# a named narrative sub-process header (e.g. '### IC Invoice Dispute Resolution'). Legitimate
# multi-Trigger workflows always introduce each extra body with a ### header, so an orphan
# Trigger table (one whose nearest preceding header is a field-section header like '### Steps'
# or another field table) signals a workflow whose ## W header was lost in generation — making
# it invisible to every count, the index, the classification, and the dependency map.
# A 2026-06-20 scan found exactly one: VS-12 PA-12.2 W1376 (a 'Tool Rental Reservation, Waitlist
# & Scheduling' body). Reported as a WARN (not ERROR): the fix requires allocating a new W-number
# and updating the 4,980 grand total + index + classification + cross-reference docs — a
# substantive change with cascading impacts, not a mechanical normalization.
GHOST=$(python3 - "$REPO_ROOT" <<'PY'
import os,re,sys
ROOT=sys.argv[1]+"/01-model-company/workflows"
FIELD={'### Steps','### System Touchpoints','### Pain Points / Risks','### Time Estimate','### Cross-references','### Controls','### Automation Opportunity','### Staffing Implication','### Background'}
def is_field_section(h):
    return re.sub(r' \(.*$','',h) in FIELD
out=[]
for d in sorted(os.listdir(ROOT)):
    if not d.startswith("VS-"): continue
    for f in sorted(os.listdir(f"{ROOT}/{d}")):
        if not (f.startswith("PA-") and f.endswith(".md")): continue
        last=None; cur=None; tc=0
        for ln in open(f"{ROOT}/{d}/{f}").read().split("\n"):
            if re.match(r'^## W\d+[A-Z]?\. ', ln): cur=ln; tc=0; last=ln; continue
            if re.match(r'^### ', ln): last=ln; continue
            if '| **Trigger** |' in ln:
                tc+=1
                if tc==1: continue
                if last is None or is_field_section(last.strip()):
                    out.append(f"{d}/{f}: orphan Trigger table inside {cur[:55]}")
print("\n".join(out))
PY
)
GHOST_COUNT=$(echo -n "$GHOST" | grep -cP 'PA-' || true)
if [ "$GHOST_COUNT" -eq 0 ]; then
    ok "No orphan workflow bodies (ghost workflows) detected"
else
    warn "$GHOST_COUNT orphan workflow body/bodies (Trigger table with no introducing ### header — a workflow missing its ## W header; invisible to counts/index/classification; needs W-number allocation to fix):"
    echo "$GHOST" | sed 's/^/    /'
fi

# --- Check 18: Criticality-classification prose counts vs headings ---
echo "--- Check 18: Criticality-classification prose counts vs headings & canonical registers ---"
# validate-repo.sh's table-row checks (Check 1, 9) and the §Summary table proved trustworthy, but
# the file's free-prose counts drifted: across six 2026-06-20 classification batches (v7.19→v7.25)
# the per-tier body sentence 'These <N> workflows ...' under each '## Tier N: ... (M Workflows)'
# heading froze at the v7.19 counts (440/499/229 = 1,168) while the headings correctly advanced to
# 684/1,354/402 (= 2,440); the intro banner likewise held stale '2,684 unclassified (4,981 − 2,297)'
# against a correct 2,564. Both contradicted the file's own Summary table. A table-row check cannot
# see prose, so this check asserts the two stable prose invariants the Summary already encodes:
#   (a) each tier heading's '(M Workflows)' == that section's 'These <N> workflows' sentence, and
#   (b) the intro-banner arithmetic 'X unclassified = grand_total − classified' is self-consistent
# and matches the §Summary totals. Errors here mean a future classification batch updated the
# Summary table but forgot the surrounding prose — the exact v7.19→v7.25 regression.
# 2026-09-10 seventeenth-wave extension: internal consistency is not enough — the batch-24
# pass updated the Confirmed-Total row and the sub-workflow note while stranding four OTHER
# live spots quoting the retired totals (intro headline '5,426 unique … 5,449 rows', the
# Coverage table's 'Confirmed (hand-reviewed)' row, the Grand Total row, and the §Domain
# Breakdown prose), every one self-consistent with its neighbours and therefore invisible
# to (a)+(b). The unique/register-row canon is now re-derived from the PA files' own ##/###
# W headers every run and pinned on all six figure surfaces (intro headline ×2, Coverage
# row ×2, Grand Total row, Domain prose ×3, sub-workflow note, Confirmed Total row).
CLASS_FILE="$REPO_ROOT"/01-model-company/workflows/workflow-criticality-classification.md
PROSE_DRIFT=$(python3 - "$REPO_ROOT" <<'PY'
import os,re,sys
ROOT=sys.argv[1]
WFR=os.path.join(ROOT,"01-model-company","workflows")
f=open(os.path.join(WFR,"workflow-criticality-classification.md"),encoding="utf-8").read()
lines=f.split("\n")
errs=[]
# ---- (c) canon re-derivation from the PA corpus: unique ## W ids + ### sub-workflow rows ----
_ids=set(); _sub=0
for _d in os.listdir(WFR):
    if not _d.startswith("VS-"): continue
    _dd=os.path.join(WFR,_d)
    if not os.path.isdir(_dd): continue
    for _fn in os.listdir(_dd):
        if _fn.startswith("PA-") and _fn.endswith(".md"):
            _t=open(os.path.join(_dd,_fn),encoding="utf-8").read()
            _ids.update(re.findall(r"^## (W\d+[A-Z]?)\.",_t,re.M))
            _sub+=len(re.findall(r"^### W\d+[A-Z]?\.",_t,re.M))
CU=len(_ids); CR=CU+_sub
def _fig(pat,label,want,flags=re.M):
    m=re.search(pat,f,flags)
    if not m:
        errs.append("cannot find the classification "+label+" surface")
        return
    got=int(m.group(1).replace(",",""))
    if got!=want:
        errs.append(f"classification {label} says {got:,} but the PA corpus re-derives {want:,} (unique ## headers {CU:,} + {_sub} ### sub-workflow rows = {CR:,} register rows)")
_fig(r"^> Classifies all ([0-9,]+) unique operational workflows","intro headline unique-workflow figure",CU)
_fig(r"^> register holds ([0-9,]+) rows","intro headline register-row figure",CR)
_fig(r"^\| Confirmed \(hand-reviewed\) \| ([0-9,]+) rows","Coverage confirmed-row figure",CR)
_fig(r"^\| Confirmed \(hand-reviewed\) \| [0-9,]+ rows \(([0-9,]+) unique","Coverage confirmed-unique figure",CU)
_fig(r"^\| \*\*Confirmed Total\*\* \| \| \*\*([0-9,]+)\*\* \| 100% \|","Summary Confirmed-Total row",CR)
_fig(r"^\| \*\*Grand Total\*\* \| \*\*([0-9,]+)\*\* unique","Summary Grand-Total row",CU)
_fig(r"the remaining ([0-9,]+) are canonical `##` workflows","sub-workflow-note unique figure",CU)
_fig(r"breakdown of the ([0-9,]+) classified register rows","Domain-Breakdown register-row figure",CR)
_fig(r"breakdown of the [0-9,]+ classified register rows \(([0-9,]+) unique workflows\)","Domain-Breakdown unique figure",CU)
_fig(r"breakdown of all ([0-9,]+) workflows","Domain-Breakdown all-workflows figure",CU)
# (a) heading count vs 'These N workflows' body sentence
for i,ln in enumerate(lines):
    m=re.match(r'^## Tier [123]: .*\(([0-9,]+) Workflows\)', ln)
    if not m: continue
    head=int(m.group(1).replace(",",""))
    body=None
    for j in range(i+1, min(i+6,len(lines))):
        bm=re.match(r'^These ([0-9,]+) workflows', lines[j])
        if bm:
            body=int(bm.group(1).replace(",","")); break
        if lines[j].strip() and not lines[j].startswith('>'):
            # first non-blank non-quote prose line reached without a 'These N' sentence
            break
    if body is not None and body!=head:
        errs.append(f"Tier heading says {head:,} but following prose says {body:,}: {ln[:55]}")
# (b) intro-banner arithmetic self-consistency + match to the Grand Total row.
# The Grand Total row states all three UNIQUE-count figures in one cell
# ('4,981 unique ## workflows (2,417 confirmed + 2,564 unclassified)'); the intro banner uses
# the same unique-count frame, so it must agree with THAT row — not the 'Confirmed Total'
# (2,440) row, which counts register rows incl. 23 parent/summary sub-workflows.
intro_m=re.search(r'An additional ([0-9,]+) workflows \(([0-9,]+) total . ([0-9,]+) classified\)', f)
gt_m=re.search(r'\| \*\*Grand Total\*\* \| \*\*([0-9,]+)\*\* unique .##. workflows \(([0-9,]+) confirmed \+ ([0-9,]+) unclassified', f)
# Since the 2026-06-28 Full-Coverage Confirmation Pass the intro banner declares full
# coverage ('Classifies all 5,349 unique ... Zero workflows remain unclassified'). That
# form is accepted and cross-checked against the Grand Total row instead (confirmed ==
# unique, unclassified == 0).
full_m=re.search(r'^> Classifies all ([0-9,]+) unique operational workflows', f, re.M) and re.search(r'^> .*Zero workflows remain unclassified', f, re.M)
if full_m and not intro_m:
    if gt_m:
        g=int(gt_m.group(1).replace(",","")); c=int(gt_m.group(2).replace(",","")); u=int(gt_m.group(3).replace(",",""))
        if c!=g: errs.append(f"Grand Total confirmed-unique ({c:,}) != unique total ({g:,}) under full coverage")
        if u!=0: errs.append(f"Grand Total unclassified ({u:,}) must be 0 under the full-coverage banner")
    else:
        errs.append("cannot find Grand Total row to cross-check the full-coverage intro banner")
elif intro_m:
    unc=int(intro_m.group(1).replace(",","")); tot=int(intro_m.group(2).replace(",","")); cls=int(intro_m.group(3).replace(",",""))
    if tot-cls!=unc:
        errs.append(f"Intro banner arithmetic wrong: {tot:,} total − {cls:,} classified = {tot-cls:,}, but states {unc:,} unclassified")
    if gt_m:
        g=int(gt_m.group(1).replace(",","")); c=int(gt_m.group(2).replace(",","")); u=int(gt_m.group(3).replace(",",""))
        if tot!=g: errs.append(f"Intro banner grand total ({tot:,}) != Summary Grand Total unique ({g:,})")
        if cls!=c: errs.append(f"Intro banner classified ({cls:,}) != Summary Grand Total confirmed-unique ({c:,})")
        if unc!=u: errs.append(f"Intro banner unclassified ({unc:,}) != Summary Grand Total unclassified ({u:,})")
else:
    errs.append("Could not locate intro-banner (either the pre-2026-06-28 'An additional N workflows (M total − K classified)' form or the full-coverage 'Zero workflows remain unclassified' form)")
# ---- (d) register W-title mirror vs the PA canon (2026-09-15 thirtieth-wave) ----
# The register's W-title column is a navigation surface no rule read. Drift
# against the PA ##/###/#### W-header canon (the generator-read primary source
# and the bpmn process names) had accumulated 49 stranded forms: the NCSD/
# I-SEAL/PAS 39/Intercharge token errors the semantic batches repaired in the
# PA files but never re-pointed into the register, plus the abbreviation/
# prefix/spacing drifts (initial-commit short forms and retired spellings).
# Every register row's title must now equal the PA header title exactly, except
# the two v7.31-adjudicated treasury-companion annotated forms (W423/W425 —
# deliberate register-only retitles, self-documented in the register's own
# footer of 2026-08-24), whose exact literals are pinned here so a reversion
# to the bare PA title, or any new 'exception', fires.
_pa_title_re = re.compile(r"^(#{2,4}) (W\d+[A-Za-z]?)[.\s]\s*(.+?)\s*$")
_pa_titles = {}
for _d in os.listdir(WFR):
    if not _d.startswith("VS-"): continue
    _dd = os.path.join(WFR, _d)
    if not os.path.isdir(_dd): continue
    for _fn in os.listdir(_dd):
        if _fn.startswith("PA-") and _fn.endswith(".md"):
            for _ln in open(os.path.join(_dd, _fn), encoding="utf-8"):
                _m = _pa_title_re.match(_ln)
                if _m and _m.group(2) not in _pa_titles:
                    _pa_titles[_m.group(2)] = _m.group(3)
_STANDING_TITLES = {
    "W423": "AR Post-dated Check (PDC) Warehousing & Clearing — Treasury Execution (canonical lifecycle: W1380)",
    "W425": "Bounced Check (DAIF/DAUD) Recovery & Penalty — Treasury Reversal (canonical resolution: W1381)",
}
_reg_row_re = re.compile(r"^\|\s*(W\d+[A-Za-z]?)\s*\|\s*([^|]+?)\s*\|")
_reg_titles = {}
for _ln in lines:
    _m = _reg_row_re.match(_ln)
    if _m:
        _reg_titles.setdefault(_m.group(1), _m.group(2))
if len(_reg_titles) != CR:
    errs.append(f"register parses to {len(_reg_titles)} distinct W-id rows but the PA corpus re-derives {CR} register rows ({CU} unique + {_sub} sub-workflow headers)")
_missing = sorted(set(_reg_titles) - set(_pa_titles))[:5]
_extra = sorted(set(_pa_titles) - set(_reg_titles))[:5]
if _missing:
    errs.append(f"register rows for W-ids with no PA header: {_missing}")
if _extra:
    errs.append(f"PA headers with no register row: {_extra}")
for _w in sorted(_reg_titles):
    _want = _STANDING_TITLES.get(_w, _pa_titles.get(_w))
    if _want is not None and _reg_titles[_w] != _want:
        errs.append(f"register title for {_w} is '{_reg_titles[_w]}' but the PA canon is '{_want}'")
print("\n".join(errs))
PY
)
PROSE_DRIFT_COUNT=$(echo -n "$PROSE_DRIFT" | grep -cP '.' || true)
if [ "$PROSE_DRIFT_COUNT" -eq 0 ]; then
    ok "Criticality-classification prose counts (tier bodies + intro arithmetic) match headings/Summary, all six canonical figure surfaces (intro headline, Coverage row, Grand Total, Domain prose, sub-workflow note, Confirmed Total) match the PA corpus re-derivation (5,427 unique / 5,450 rows; canon-pin extension added by the 2026-09-10 seventeenth-wave review after the batch-24 pass stranded four live spots at the retired totals while every one stayed self-consistent), and all 5,450 register W-title cells equal the PA ##/### W-header canon exactly except the two v7.31-adjudicated W423/W425 treasury-companion annotated forms (title mirror added by the 2026-09-15 thirtieth-wave review after 49 stranded register titles — incl. the NCSD/I-SEAL/PAS 39/Intercharge token errors the semantic batches repaired in the PA files but never re-pointed into the register — were found on the surface no rule read)"
else
    error "$PROSE_DRIFT_COUNT criticality-classification prose count(s) disagree with their heading or the Summary table:"
    echo "$PROSE_DRIFT" | sed 's/^/    /'
fi

# --- Check 19: PA/VS link resolution in value-stream-index.md ---
echo "--- Check 19: PA/VS link resolution in value-stream-index.md ---"
# The index's 'Detailed Value Stream Map' lists every value stream and process area as a
# markdown link to its README / PA file (./VS-NN-.../(README|PA-NN.X-...).md). A 2026-06-21
# review found 12 such links stale for VS-178/179/180/181: the hrefs used slugs with an extra
# 'and' conjunction (e.g. ...-and-title-consolidation.md) while the files on disk omit it
# (...-title-consolidation.md) — a drift no other check sees (Check 2 compares header COUNTS,
# not link TARGETS; Check 7 validates workflow-ID references, not file paths). This check
# resolves every intra-repo markdown link in the index to its target file so the drift cannot
# recur. (Scope is the index; the cross-reference docs' W-references are covered by Checks 6/7.)
INDEX="$REPO_ROOT"/01-model-company/workflows/value-stream-index.md
BROKEN_INDEX_LINKS=""
TOTAL_INDEX_LINKS=$(grep -oP '\]\(\K\./VS-[^)]+\.md' "$INDEX" 2>/dev/null | wc -l | tr -d ' ')
while IFS= read -r link; do
    # link is relative to the index's own directory (workflows/)
    [ -f "$REPO_ROOT"/01-model-company/workflows/"$link" ] || BROKEN_INDEX_LINKS="$BROKEN_INDEX_LINKS$link"$'\n'
done < <(grep -oP '\]\(\K\./VS-[^)]+\.md' "$INDEX" 2>/dev/null || true)
BROKEN_INDEX_COUNT=$(echo -n "$BROKEN_INDEX_LINKS" | grep -cP '\.md' || true)
if [ "$BROKEN_INDEX_COUNT" -eq 0 ]; then
    ok "All $TOTAL_INDEX_LINKS PA/VS links in value-stream-index.md resolve to a file"
else
    error "$BROKEN_INDEX_COUNT link(s) in value-stream-index.md do not resolve to a file:"
    echo "$BROKEN_INDEX_LINKS" | sed 's/^/    /'
fi

# --- Check 20: PA-file relative-link resolution ---
echo "--- Check 20: PA-file relative-link resolution ---"
# Every PA file carries two navigation links (a 'Part of **[VS-NN: ...](./README.md)** ...'
# header line and a '*... · [Value Stream Index](../value-stream-index.md)*' footer) plus
# occasional in-body cross-reference links. A 2026-06-21 review found exactly one stale across
# all PA files (565 at the time of that review): VS-56 PA-56.1's header linked to '../value-stream.md' instead of
# '../value-stream-index.md'. No other check sees this — Check 2 compares header COUNTS, Check 7
# validates workflow-IDs, and Check 19 scopes only the index. This check resolves every
# relative (./ or ../) intra-repo .md link inside every PA file so the drift cannot recur.
PA_FILE_COUNT=$(find "$REPO_ROOT"/01-model-company/workflows -name 'PA-*.md' -type f | wc -l | tr -d ' ')
BROKEN_PA_LINKS=$(python3 - "$REPO_ROOT" <<'PY'
import os,re,sys,glob
ROOT=sys.argv[1]
out=[]
total=0
for f in sorted(glob.glob(f"{ROOT}/01-model-company/workflows/VS-*/PA-*.md")):
    dirn=os.path.dirname(f)
    txt=open(f,encoding='utf-8',errors='replace').read()
    for m in re.finditer(r'\]\((\./|\.\.\/)[^)]*?\.md(?:\s+"[^"]*")?\)', txt):
        target=m.group(0)[2:-1].split('"')[0].strip()  # strip ']( ... )' and any title attr
        # ignore fragment-only links (no file before '#')
        path_part=target.split('#')[0]
        if not path_part: continue
        total+=1
        resolved=os.path.normpath(os.path.join(dirn,path_part))
        if not os.path.exists(resolved):
            out.append(f"{f.replace(ROOT+'/','')}: -> {target}")
print(total, "\n".join(out), sep='\n')
PY
)
# First line of output is the total count; remainder are the broken links
PA_LINK_TOTAL=$(echo "$BROKEN_PA_LINKS" | head -1)
BROKEN_PA_BODY=$(echo "$BROKEN_PA_LINKS" | tail -n +2)
BROKEN_PA_COUNT=$(echo -n "$BROKEN_PA_BODY" | grep -cP 'PA-' || true)
if [ "$BROKEN_PA_COUNT" -eq 0 ]; then
    ok "All $PA_LINK_TOTAL relative links across all $PA_FILE_COUNT PA files resolve to a file"
else
    error "$BROKEN_PA_COUNT PA-file relative link(s) (of $PA_FILE_COUNT) do not resolve to a file:"
    echo "$BROKEN_PA_BODY" | sed 's/^/    /'
fi

# --- Check 21: Automation/Controls content quality (draft-field tracker) ---
echo "--- Check 21: Automation/Controls content quality ---"
# Checks 10/12/15 guard the analysis fields' PRESENCE and one legacy boilerplate string,
# but a 2026-06-21 review found the bulk of the machine-generated `### Automation Opportunity`
# and `### Controls` bodies (added repo-wide by add-automation-controls.py) are low-quality
# DRAFT content: Automation bullets were emitted as mid-phrase fragments like
#   '- auto-review (account manager reviews application: (a) verify)'
# and ~89% of Controls sections cited no CTL-XX from the internal-controls register.
# This check reports three live quality metrics. The backlog was fully closed on
# 2026-06-28: fragments were repaired by defragment-automation.py (2026-06-21), and CTL-XX
# citation coverage reached 100% when the register gained process-area operating controls
# (C26–C33, CTL-240–CTL-808 — one derived control per process area mapped to every workflow
# of that PA, via 07-methodology/add-pa-controls.py + backfill-controls.py). The check is
# retained as the regression guard: it WARNs (as before) if any metric slips off target —
# fragments > 0, CTL citation < 100%, or boilerplate > 0 — and prints a single OK otherwise.
# Metrics:
#   (a) Automation bullets that are broken fragments (auto-X (lowercase fragment, no period)
#   (b) Controls sections citing >=1 real CTL-XX  (coverage of the controls register)
#   (c) Controls sections that are pure boilerplate (no CTL-XX AND one of two known strings)
QUALITY=$(python3 - "$REPO_ROOT" <<'PY'
import glob, os, re, sys
ROOT = sys.argv[1]
files = glob.glob(f"{ROOT}/01-model-company/workflows/VS-*/PA-*.md")
BOILERPLATE = {
    "operational: standard operating procedures; system-enforced validation rules",
    "operational: periodic reconciliation against source documents",
}
frag = 0; auto_bullets = 0
ctrl_total = 0; ctrl_with_ctl = 0; ctrl_boiler = 0
# Broad fragment detector: any bullet emitted by add-automation-controls.py in its legacy
# fragment form. Matches every verb prefix in the generator's MANUAL_VERBS vocabulary
# ('auto-X', 'rule-based auto-X', 'workflow notification', 'continuous audit', etc.)
# followed by an opening paren — the signature of a mid-phrase snippet. The narrow regex
# used at Check 21's introduction under-counted (it missed 'rule-based'/'workflow'/'continuous'
# prefixes and nested parens); this broad form is aligned with defragment-automation.py and
# catches every generator-fragment form so the metric is an honest regression guard.
# Complete sentences (hand-written like VS-73, or regenerated '- System ...' drafts) never match.
frag_re = re.compile(r'^- (?:auto-\w+|rule-based auto-\w+|rule-based authorization|workflow (?:notification|orchestration)|continuous audit|auto-flag for investigation) [\(\)]')
for f in files:
    txt = open(f, encoding="utf-8", errors="replace").read()
    for m in re.finditer(r'^### Automation Opportunity\n(.*?)(?=^### |^---|^## |\Z)', txt, re.M | re.S):
        for line in m.group(1).split("\n"):
            line = line.strip()
            if line.startswith("- "):
                auto_bullets += 1
                if frag_re.match(line):
                    frag += 1
    for m in re.finditer(r'^### Controls\n(.*?)(?=^### |^---|^## |\Z)', txt, re.M | re.S):
        ctrl_total += 1
        body = m.group(1).strip()
        has_ctl = bool(re.search(r'\bCTL-\d+', body))
        if has_ctl:
            ctrl_with_ctl += 1
        elif any(b in body for b in BOILERPLATE) and '\n' not in body.strip():
            ctrl_boiler += 1
pct_ctl = (100 * ctrl_with_ctl // ctrl_total) if ctrl_total else 0
print(f"{frag}|{auto_bullets}|{ctrl_with_ctl}|{ctrl_total}|{pct_ctl}|{ctrl_boiler}")
PY
)
FRAG_BULLETS=$(echo "$QUALITY" | cut -d'|' -f1)
AUTO_TOTAL=$(echo "$QUALITY" | cut -d'|' -f2)
CTRL_WITH_CTL=$(echo "$QUALITY" | cut -d'|' -f3)
CTRL_TOTAL=$(echo "$QUALITY" | cut -d'|' -f4)
CTRL_PCT=$(echo "$QUALITY" | cut -d'|' -f5)
CTRL_BOILER=$(echo "$QUALITY" | cut -d'|' -f6)
if [ "$FRAG_BULLETS" -eq 0 ] && [ "$CTRL_WITH_CTL" -eq "$CTRL_TOTAL" ] && [ "$CTRL_BOILER" -eq 0 ]; then
    ok "Automation/Controls quality targets met: 0/$AUTO_TOTAL fragment bullets; $CTRL_WITH_CTL/$CTRL_TOTAL Controls sections cite a CTL-XX ($CTRL_PCT%); $CTRL_BOILER pure-boilerplate. (Register: 67 core + 172 domain anchors + 569 process-area operating controls = 808; PA controls are honest-draft derived mappings pending per-workflow review — see WORKFLOW-FORMAT-GUIDE.md 'Quality bar'. This check remains the regression guard for all three metrics.)"
else
    warn "Automation/Controls draft-field quality: $FRAG_BULLETS/$AUTO_TOTAL Automation bullets are mid-phrase fragments (target 0); $CTRL_WITH_CTL/$CTRL_TOTAL Controls sections cite a CTL-XX ($CTRL_PCT% — target 100%); $CTRL_BOILER are pure-boilerplate (target 0). See WORKFLOW-FORMAT-GUIDE.md 'Quality bar'; run defragment-automation.py / backfill-controls.py as appropriate."
fi

# --- Check 22: Required-field completeness (WORKFLOW-FORMAT-GUIDE 9 fields) ---
echo "--- Check 22: Required-field completeness ---"
# WORKFLOW-FORMAT-GUIDE.md lists 9 required fields per workflow. No prior check enforces them
# (Check 12 covers only Automation/Controls); a 2026-06-21 scan found ~1,105 missing-field
# instances across ~480 workflows (the affected set spans 27 value streams — chiefly
# VS-15..18/27/31..40/48 plus VS-53..63 and singletons — wider than first reported). The
# backlog was fully closed by the 2026-06-27 completeness pass: Participants rows were
# mechanically derived from each workflow's own Steps roles (backfill-participants.py),
# and System Touchpoints / Pain Points were authored per-workflow from step content.
# This check is retained as the regression guard so a future generation artifact that
# ships workflows missing required fields is caught. Reports any gap as a WARN (same
# treatment as Check 21's draft-quality tracker).
#   Five fields are table-row form ('| **Field** |'): Trigger, Frequency, Volume, Owner, Participants.
#   Three are ### sections: Steps, System Touchpoints, Pain Points / Risks.
#   Time Estimate accepts either form (all 5,349 workflows now use the ### form; 11 of
#   them also retain a legacy table row — the dual form is harmless and accepted).
# Each field is counted present if it appears in EITHER form within its workflow block.
FIELDS=$(python3 - "$REPO_ROOT" <<'PY'
import glob, os, re, sys
ROOT = sys.argv[1]
TABLE = ["Trigger", "Frequency", "Volume", "Owner", "Participants"]
HEADER = ["Steps", "System Touchpoints", "Time Estimate", "Pain Points / Risks"]
TIME_OK = True  # Time Estimate accepts either form
missing = {f: 0 for f in TABLE + HEADER}
worst_vs = {}
total = 0
for f in glob.glob(f"{ROOT}/01-model-company/workflows/VS-*/PA-*.md"):
    vs = re.search(r"VS-(\d+)", f).group(1)
    txt = open(f, encoding="utf-8", errors="replace").read()
    for m in re.finditer(r"^## (W\d+[A-Z]?)\..*?(?=^## W|\Z)", txt, re.M | re.S):
        block = m.group(0)
        total += 1
        for field in TABLE:
            if not re.search(r"^\| \*\*" + re.escape(field) + r"\*\*", block, re.M):
                missing[field] += 1
                worst_vs.setdefault(field, {}).setdefault(vs, 0)
                worst_vs[field][vs] += 1
        # Steps: present if '### Steps' (exact or qualified) header OR any table with the
        # '| # |' column header (every steps table uses it, regardless of whether the step
        # IDs are bare numbers, '1a', or alpha-prefixed 'CS-1'/'NR-1'). Catches all
        # legitimate forms: canonical flat table, multi-trigger '### Steps (...)',
        # phase-grouped '### <Phase>' tables, cadence-grouped '### Daily/Weekly' tables,
        # and non-numeric step-ID schemes. A strict 5-column-header or bare-number check
        # would false-flag the qualified/phase/cadence/alpha-prefix forms.
        if not (re.search(r"^### Steps(?: \([^)]*\))?\s*$", block, re.M) or
                re.search(r"^\| # \|", block, re.M)):
            missing["Steps"] += 1
            worst_vs.setdefault("Steps", {}).setdefault(vs, 0)
            worst_vs["Steps"][vs] += 1
        # System Touchpoints / Pain Points: accept exact OR '### Field (qualifier)'
        # (parenthetically-qualified sub-forms are legitimate per WORKFLOW-FORMAT-GUIDE.md).
        for field in ("System Touchpoints", "Pain Points / Risks"):
            if not re.search(r"^### " + re.escape(field) + r"(?: \([^)]*\))?\s*$", block, re.M):
                missing[field] += 1
                worst_vs.setdefault(field, {}).setdefault(vs, 0)
                worst_vs[field][vs] += 1
        # Time Estimate: accept either ### header (exact or qualified) or table row.
        if not (re.search(r"^### Time Estimate(?: \([^)]*\))?\s*$", block, re.M) or
                re.search(r"^\| \*\*Time Estimate\*\*", block, re.M)):
            missing["Time Estimate"] += 1
            worst_vs.setdefault("Time Estimate", {}).setdefault(vs, 0)
            worst_vs["Time Estimate"][vs] += 1
total_missing = sum(missing.values())
worst_vs_str = max(worst_vs, key=lambda k: sum(worst_vs[k].values())) if worst_vs else "-"
# Emit: total_missing|total|per-field counts|worst-vs
parts = [str(total_missing), str(total)]
for field in TABLE + HEADER:
    parts.append(f"{field}:{missing[field]}")
parts.append(f"worst:{worst_vs_str}")
print("|".join(parts))
PY
)
FIELD_TOTAL_MISSING=$(echo "$FIELDS" | cut -d'|' -f1)
FIELD_TOTAL_WF=$(echo "$FIELDS" | cut -d'|' -f2)
FIELD_DETAIL=$(echo "$FIELDS" | cut -d'|' -f3-)
if [ "$FIELD_TOTAL_MISSING" -eq 0 ]; then
    ok "All $FIELD_TOTAL_WF workflows have all 9 required fields"
else
    warn "$FIELD_TOTAL_MISSING missing required-field instance(s) across $FIELD_TOTAL_WF workflows (WORKFLOW-FORMAT-GUIDE.md 'Required fields'). Per-field: $(echo "$FIELD_DETAIL" | sed 's/|/, /g'). All 5,370 workflows carry all 9 fields (baseline: the 2026-06-27 completeness pass at 5,363 workflows; W5511 added 2026-09-03 with all fields; W5512–W5514 added 2026-09-03 with all fields; W5515–W5517 added 2026-09-03 with all fields) — any reading above zero is a regression from a new generation artifact."
fi

# --- Check 23: Intra-file TOC anchor resolution ---
echo "--- Check 23: Intra-file TOC anchor resolution ---"
# Every PA file opens with a '## Workflows in This Process Area' navigation list whose
# entries link to the workflow headings below via GitHub heading anchors (#slug). A
# gap-analysis generator bug left 1,926 such anchors malformed across 271 PA files —
# the slugger dropped hyphens ('Floor-Plan' -> 'floorplan') and stale W-numbers survived
# a renumber (display 'W4601' but anchor '#w4409-...') — so the TOC links resolved to
# nothing on GitHub. No prior check saw this: Checks 19/20 verify linked FILES resolve;
# none resolve anchors. This check computes each file's heading slugs (GitHub slugger)
# and reports any '(#anchor)' link that matches no heading. Treated as an ERROR (a
# broken navigational link), consistent with the file-resolution checks 19/20. Repaired
# by `07-methodology/fix-toc-anchors.py`; this check guards against regression.
ANCHORS=$(python3 - "$REPO_ROOT" <<'PY'
import glob, os, re, sys
ROOT = sys.argv[1]
def gh_slug(s):
    # github-slugger semantics (consistency review #11 correction): lowercase, remove
    # non-word/space/hyphen chars, then replace EACH space with '-' — do NOT collapse
    # runs. GitHub turns the two adjacent spaces left by removed spaced punctuation
    # (' & ', ' / ') into a DOUBLE hyphen; the previous collapsing rule wrongly accepted
    # single-hyphen anchors that are broken on GitHub (4,618 repo-wide, repaired by
    # fix-toc-anchors.py v2). Duplicates get '-1', '-2'… suffixes.
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s, flags=re.UNICODE)
    return s.replace(' ', '-')
files_bad = {}
for f in sorted(glob.glob(f"{ROOT}/01-model-company/workflows/VS-*/PA-*.md")):
    txt = open(f, encoding='utf-8', errors='replace').read()
    heads = set(); _seen = {}
    for h in re.findall(r'^#+\s+(.+?)\s*$', txt, re.M):
        s = gh_slug(h); n = _seen.get(s, 0); _seen[s] = n + 1
        heads.add(s if n == 0 else f"{s}-{n}")
    bad = sorted({anchor for _disp, anchor in re.findall(r'\[([^\]]+)\]\(#([^)]+)\)', txt)
                  if anchor not in heads})
    if bad:
        files_bad[f.replace(ROOT + '/', '')] = bad
print(f"{len(files_bad)}|{sum(len(v) for v in files_bad.values())}")
for f, bad in files_bad.items():
    sample = bad[0] + (f" (+{len(bad)-1} more)" if len(bad) > 1 else "")
    print(f"{f}: #{sample}")
PY
)
BAD_ANCHOR_FILES=$(echo "$ANCHORS" | head -1 | cut -d'|' -f1)
BAD_ANCHOR_TOTAL=$(echo "$ANCHORS" | head -1 | cut -d'|' -f2)
BAD_ANCHOR_SAMPLES=$(echo "$ANCHORS" | tail -n +2)
if [ "$BAD_ANCHOR_TOTAL" -eq 0 ]; then
    ok "All intra-file TOC anchors resolve to a heading"
else
    error "$BAD_ANCHOR_TOTAL intra-file TOC anchor(s) across $BAD_ANCHOR_FILES PA file(s) do not resolve to any heading (run 07-methodology/fix-toc-anchors.py to repair):"
    echo "$BAD_ANCHOR_SAMPLES" | sed 's/^/    /' | head -20
fi

# --- Check 24: workflows/README.md family reconciliation + stale canonical-figure guard ---
echo "--- Check 24: workflows/README.md family reconciliation & stale-figure guard ---"
# Two-part guard added 2026-06-26 after a review found (a) workflows/README.md family
# headers/rows had drifted out of sync with value-stream-index.md (a VS-127 row stuck at
# 24, a missing VS-192 row, and two stale family-header totals) and (b) a headcount
# change (6,757 -> 6,762) had been applied to summary docs but not propagated to ~97
# workflow files. No prior check saw either: Check 3 verifies the index GRAND total
# only; Check 18 covers criticality-classification prose only. Part A is a structural
# ERROR (count reconciliation, same class as Check 2/9); Part B is a WARN (editorial
# figure consistency) scoped to skip the labelled historical-record docs and any
# 'X -> Y' change-note. Repair scripts: fix-headcount-6757.py (Part B) + hand-edit (A).
CHECK24=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
errors, stale = [], []

# ---- Part A: workflows/README.md family sections reconcile with value-stream-index.md ----
idx = open(f"{ROOT}/01-model-company/workflows/value-stream-index.md", encoding='utf-8').read().splitlines()
readme = open(f"{ROOT}/01-model-company/workflows/README.md", encoding='utf-8').read().splitlines()

idx_sub, cur = {}, None
fam_row = re.compile(r'^\| ([A-Za-z][^|]*?) \| \[VS-')
for line in idx:
    m = fam_row.match(line)
    if m:
        cur = m.group(1).strip(); continue
    if '**Subtotal**' in line and cur:
        nums = re.findall(r'\*\*([\d,]+)\*\*', line)
        if nums:
            idx_sub[cur] = int(nums[-1].replace(',', ''))
        cur = None

hdr = re.compile(r'^### (.+?) \(([0-9,]+) workflows\)')
vs_row = re.compile(r'^\| \[VS-\d+\]\([^)]*\) \| .* \| (\d+) \|$')
readme_fam, cur = {}, None
for line in readme:
    m = hdr.match(line)
    if m:
        cur = m.group(1).strip(); readme_fam[cur] = {'header': int(m.group(2).replace(',', '')), 'sum': 0}; continue
    m = vs_row.match(line)
    if m and cur:
        readme_fam[cur]['sum'] += int(m.group(1))

idx_total = sum(idx_sub.values()); readme_total = sum(f['sum'] for f in readme_fam.values())
for fam, idx_n in idx_sub.items():
    if fam not in readme_fam:
        errors.append(f"family '{fam}' in value-stream-index.md but has no section in workflows/README.md"); continue
    h = readme_fam[fam]['header']; s = readme_fam[fam]['sum']
    if not (idx_n == h == s):
        errors.append(f"{fam}: index subtotal={idx_n}, README header={h}, README row-sum={s}")
if idx_total != readme_total:
    errors.append(f"grand total: index={idx_total}, README row-sum={readme_total}")

# ---- Part B: stale canonical total-headcount figure '6,757' in current-state prose ----
SKIP = {'CHANGELOG.md', 'workflow-gap-analysis.md', 'headcount-reality-check.md'}
pat = re.compile(r'(?<!\d)6,757(?!\d)')
for dirpath, _d, files in os.walk(ROOT):
    if os.sep + '.git' in dirpath: continue
    for fn in files:
        if not fn.endswith('.md') or fn in SKIP: continue
        path = os.path.join(dirpath, fn)
        txt = open(path, encoding='utf-8', errors='replace').read()
        for m in pat.finditer(txt):
            lo = max(0, m.start()-25); hi = min(len(txt), m.end()+25)
            if '->' in txt[lo:hi] or '\u2192' in txt[lo:hi]:
                continue  # legitimate historical 'X -> Y' change-note
            line_no = txt.count('\n', 0, m.start()) + 1
            stale.append(f"{os.path.relpath(path, ROOT)}:{line_no}")

# ---- Part C: workflows/README.md Quick-Stats table + family-subtotal reconciliation line
# vs the canonical registers. Added by the 2026-09-14 twenty-sixth-wave consistency review:
# the Quick-Stats table (188 / 569 / 5,427 / 1,396 / 3,296 / 758 / the 'Classified total'
# row-prefix triple) and the closing 'Family subtotal reconciliation: … = N' sentence were
# read by no check — Part A reconciles the family sections only, and Checks 70/74 pin other
# surfaces — so a batch that re-pointed every guarded surface could still strand the README's
# own headline block (verified by synthetic injection before arming: a 5,426 Quick-Stats row
# and a 5,426 reconciliation total both passed the full validator 0/0). Every figure is
# re-derived from the primary sources each run: VS-* directories, PA-*.md files, unique ##
# W-headers + ### sub-workflow headers in the PA corpus, and the classification register's
# per-tier rows (register_heading_hits attribution).
import glob
vs_dirs = [p for p in glob.glob(f"{ROOT}/01-model-company/workflows/VS-*") if os.path.isdir(p)]
pa_files = glob.glob(f"{ROOT}/01-model-company/workflows/VS-*/PA-*.md")
uniq_h, sub_h = set(), set()
for _f in pa_files:
    _t = open(_f, encoding='utf-8').read()
    uniq_h.update(m.group(1) for m in re.finditer(r'^## (W\d+[A-Z]?)\.', _t, re.M))
    sub_h.update(m.group(1) for m in re.finditer(r'^### (W\d+[A-Z]?)\.', _t, re.M))
cls_txt = open(f"{ROOT}/01-model-company/workflows/workflow-criticality-classification.md", encoding='utf-8').read()
# Per-tier row attribution ports audit-model-docs.register_heading_hits' derivation
# (the repo's canonical tier counter): '## Tier N:' / '### Tier N Additions' /
# '#### Tier N …' headings set the attribution context; any other level-≤2 heading
# clears it; every '| Wx | …' register row increments the active tier.
tiers, _cur = {1: 0, 2: 0, 3: 0}, None
for _line in cls_txt.splitlines():
    _hm = re.match(r'^(#{1,4}) (.*)', _line)
    if _hm:
        _level, _text = len(_hm.group(1)), _hm.group(2)
        _tm = re.match(r'^Tier (\d):', _text)
        _am = re.match(r'^Tier (\d) Additions', _text)
        _t4 = re.match(r'^Tier (\d)', _text)
        if _tm:
            _cur = int(_tm.group(1))
        elif _am:
            _cur = int(_am.group(1))
        elif _level == 4 and _t4:
            _cur = int(_t4.group(1))
        elif _level <= 2:
            _cur = None
        continue
    if _cur and re.match(r'^\| (W\d+[A-Z]?) \| ', _line):
        tiers[_cur] += 1
qs = {}
for _line in readme:
    _m = re.match(r'^\| ([A-Za-z][A-Za-z0-9 /()-]*?) \| ([0-9,]+) \|$', _line)
    if _m:
        qs[_m.group(1).strip()] = int(_m.group(2).replace(',', ''))
def _qeq(key, want, basis):
    got = qs.get(key)
    if got is None:
        errors.append(f"workflows/README.md Quick-Stats row '{key}' missing (guard re-derived {want:,} from the {basis})")
    elif got != want:
        errors.append(f"workflows/README.md Quick-Stats '{key}' says {got:,} but the canonical re-derivation is {want:,} ({basis})")
_qeq('Value Streams', len(vs_dirs), 'VS-* directory count')
_qeq('Process Areas', len(pa_files), 'PA-*.md file count')
_qeq('Workflows', len(uniq_h), 'unique ## W-headers')
_qeq('Classified (Tier 1)', tiers[1], 'register Tier-1 rows (register_heading_hits attribution)')
_qeq('Classified (Tier 2)', tiers[2], 'register Tier-2 rows (register_heading_hits attribution)')
_qeq('Classified (Tier 3)', tiers[3], 'register Tier-3 rows (register_heading_hits attribution)')
readme_whole = '\n'.join(readme)
_mtot = re.search(r'^\| Classified total \| ([0-9,]+) rows = ([0-9,]+) unique workflows \+ ([0-9,]+) parent/summary', readme_whole, re.M)
if not _mtot:
    errors.append("workflows/README.md Quick-Stats 'Classified total' row missing or reshaped (expected '| Classified total | N rows = U unique workflows + S parent/summary sub-workflow rows …')")
else:
    _n, _u, _s = (int(x.replace(',', '')) for x in _mtot.groups())
    if (_n, _u, _s) != (sum(tiers.values()), len(uniq_h), len(sub_h)) or sum(tiers.values()) != len(uniq_h) + len(sub_h):
        errors.append(f"workflows/README.md 'Classified total' triple {_n:,}/{_u:,}/{_s:,} disagrees with the re-derivation {sum(tiers.values()):,} register rows = {len(uniq_h):,} unique + {len(sub_h)} ### sub-workflow headers")
_exp_rec = 'Family subtotal reconciliation: ' + ' + '.join(f"{f['sum']:,}" for f in readme_fam.values()) + f" = {readme_total:,}"
if _exp_rec not in readme_whole:
    errors.append(f"workflows/README.md family-subtotal reconciliation line missing or stale (expected exactly: {_exp_rec})")
if f"all {len(vs_dirs)} value streams" not in readme_whole:
    errors.append(f"workflows/README.md index-row clause 'all N value streams' missing or stale (re-derives to {len(vs_dirs)})")

print(f"A_ERRS={len(errors)}")
for e in errors: print(f"A_ERR|{e}")
print(f"B_STALE={len(stale)}")
for s in stale[:12]: print(f"B_STALE|{s}")
print(f"GRAND={readme_total}")
PY
)
A_ERRS=$(echo "$CHECK24" | sed -n 's/^A_ERRS=//p')
B_STALE=$(echo "$CHECK24" | sed -n 's/^B_STALE=//p')
GRAND=$(echo "$CHECK24" | sed -n 's/^GRAND=//p')
if [ "$A_ERRS" -eq 0 ]; then
    ok "workflows/README.md family headers & per-VS row sums reconcile with value-stream-index.md subtotals (8 families, grand total $GRAND workflows); the Quick-Stats table and the family-subtotal reconciliation line match the canonical re-derivation ($GRAND unique ## headers, tier rows re-derived from the classification register; Part C added by the 2026-09-14 twenty-sixth-wave consistency review after synthetic injections proved the headline block invisible to every check)"
else
    error "workflows/README.md does not reconcile with value-stream-index.md or its own canonical-figure block ($A_ERRS mismatch(es)) — family header / row-sum / index-subtotal / Quick-Stats row / reconciliation line must all agree:"
    echo "$CHECK24" | grep '^A_ERR|' | sed 's/^A_ERR|/    /'
fi
if [ "$B_STALE" -eq 0 ]; then
    ok "No stale total-headcount figure '6,757' in current-state prose (canonical figure is 6,762; historical 'X -> Y' notes and CHANGELOG/workflow-gap-analysis/headcount-reality-check excluded)"
else
    warn "Stale total-headcount figure '6,757' appears $B_STALE time(s) in current-state prose (canonical figure is now 6,762 — run 07-methodology/fix-headcount-6757.py to repair):"
    echo "$CHECK24" | grep '^B_STALE|' | sed 's/^B_STALE|/    /'
fi

# --- Check 25: criticality proposed-register mirror + touchpoint-map reconciliation claims ---
echo "--- Check 25: proposed-register mirror & touchpoint-map reconciliation ---"
# Added 2026-06-26 after an independent review found the 2026-06-25 VS-127 PA-127.4 regeneration
# of workflow-criticality-proposed.md (unclassified 2,588 -> 2,596) had NOT been propagated into
# (a) workflow-criticality-classification.md's §Summary 'Proposed classification' mirror (still
#     2,564 / 507-1,912-145 — contradicting that same file's intro banner and Grand-Total row),
# (b) three further current-state prose spots citing the stale figure 2,564 (format-guide layout
#     line, touchpoint-map footer sentence), and
# (c) workflow-system-touchpoint-map.md, last fully reconciled at Pass 29: its footer still
#     declared 'Reconciled to 5,317 workflows across 187 value streams', its §summary section
#     stopped at VS-191 with no VS-192 row, and the Pass 26–29 rows (VS-178–VS-191) sat
#     header-less between the section heading and the intro note — a broken table invisible to
#     Check 13, whose parser anchors on a header row.
# No prior check saw any of these: Check 18 verifies tier-body counts only; Check 3 verifies the
# index grand total only; Check 24 Part B guards one hard-coded headcount figure. Parts:
#   A (ERROR): the classification doc's proposed-summary table (three tier rows, Proposed Total,
#      coverage row) must equal workflow-criticality-proposed.md's register header (itself
#      verified against PA headers by Check 1).
#   B (WARN): stale canonical unclassified figure '2,564' in current-state prose — same
#      SKIP-docs and 'X -> Y' exclusions as Check 24 Part B.
#   C (ERROR): touchpoint-map self-declared reconciliation must match canonical reality —
#      footer 'Reconciled to N workflows across M value streams' equals the index Grand Total
#      and active-VS count; the §summary heading range ends at the index's max VS; every
#      VS from 79 through max VS has a primary-module row.
CHECK25=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
errors, stale = [], []
WF = f"{ROOT}/01-model-company/workflows"

# ---- Part A: proposed-register mirror in workflow-criticality-classification.md ----
prop = open(f"{WF}/workflow-criticality-proposed.md", encoding='utf-8').read()
m = re.search(r'\*\*Workflow coverage:\*\* ([\d,]+) unclassified workflows · Tier 1: ([\d,]+) · Tier 2: ([\d,]+) · Tier 3: ([\d,]+)', prop)
if not m:
    errors.append("cannot parse '**Workflow coverage:**' register header in workflow-criticality-proposed.md")
else:
    reg_total = int(m.group(1).replace(',', ''))
    tiers = [int(m.group(i).replace(',', '')) for i in (2, 3, 4)]
    if sum(tiers) != reg_total:
        errors.append(f"register header inconsistent: T1+T2+T3={sum(tiers)} != total {reg_total}")
    cls = open(f"{WF}/workflow-criticality-classification.md", encoding='utf-8').read()
    def grab(pat, label):
        mm = re.search(pat, cls, re.M)
        if not mm:
            errors.append(f"classification doc: cannot find {label}")
            return None
        return int(mm.group(1).replace(',', ''))
    t1 = grab(r'^\| Phase 1 \| Go-Live Critical \(Tier 1\) \u2014 proposed \| ([\d,]+) \|$', 'proposed Tier-1 row')
    t2 = grab(r'^\| Phase 2 \| Operational Excellence \(Tier 2\) \u2014 proposed \| ([\d,]+) \|$', 'proposed Tier-2 row')
    t3 = grab(r'^\| Phase 3 \| Innovation & Optimization \(Tier 3\) \u2014 proposed \| ([\d,]+) \|$', 'proposed Tier-3 row')
    tot = grab(r'^\| \*\*Proposed Total\*\* \| \| \*\*([\d,]+)\*\* \|$', 'Proposed Total row')
    cov = grab(r'^\| Proposed \(keyword, pending review\) \| ([\d,]+) \|$', 'coverage-table Proposed row')
    for got, want, label in ((t1, tiers[0], 'Tier 1'), (t2, tiers[1], 'Tier 2'), (t3, tiers[2], 'Tier 3'), (tot, reg_total, 'Proposed Total'), (cov, reg_total, 'Coverage Proposed')):
        if got is not None and got != want:
            errors.append(f"classification proposed-summary {label} = {got:,} but register = {want:,}")

# ---- Part B: stale canonical unclassified figure in current-state prose ----
# '2,564' was the pre-Pass-26–29 figure; '2,596' became stale itself when the 2026-06-28
# Full-Coverage Confirmation Pass closed the backlog to zero. Both are guarded with the
# same SKIP-docs / 'X -> Y' change-note exclusions.
SKIP = {'CHANGELOG.md', 'workflow-gap-analysis.md', 'headcount-reality-check.md'}
for pat_src in (r'(?<!\d)2,564(?!\d)', r'(?<!\d)2,596(?!\d)'):
    pat = re.compile(pat_src)
    for dirpath, _d, files in os.walk(ROOT):
        if os.sep + '.git' in dirpath: continue
        for fn in files:
            if not fn.endswith('.md') or fn in SKIP: continue
            path = os.path.join(dirpath, fn)
            txt = open(path, encoding='utf-8', errors='replace').read()
            for m in pat.finditer(txt):
                lo = max(0, m.start()-25); hi = min(len(txt), m.end()+25)
                if '->' in txt[lo:hi] or '\u2192' in txt[lo:hi]:
                    continue  # legitimate historical 'X -> Y' change-note
                line_no = txt.count('\n', 0, m.start()) + 1
                stale.append(f"{os.path.relpath(path, ROOT)}:{line_no}")

# ---- Part C: touchpoint-map self-declared reconciliation vs canonical reality ----
idx = open(f"{WF}/value-stream-index.md", encoding='utf-8').read()
vs_nums = {int(n) for n in re.findall(r'\[VS-(\d+)\]\(', idx)}
max_vs = max(vs_nums) if vs_nums else 0
n_vs = len(vs_nums)
gm = re.search(r'^\|[^\n]*\*\*Grand Total\*\*[^\n]*$', idx, re.M)
if not gm:
    errors.append("cannot parse Grand Total row in value-stream-index.md")
else:
    nums = re.findall(r'\*\*([\d,]+)\*\*', gm.group(0))
    if len(nums) < 2:
        errors.append("Grand Total row does not carry two bold figures (PAs, workflows)")
    else:
        idx_pas, idx_wfs = int(nums[-2].replace(',', '')), int(nums[-1].replace(',', ''))
tmap_path = f"{WF}/workflow-system-touchpoint-map.md"
tmap = open(tmap_path, encoding='utf-8').read()
fm = re.search(r'Reconciled to ([\d,]+) workflows across (\d+) value streams', tmap)
if not fm:
    errors.append("touchpoint map: cannot find the self-declared 'Reconciled to N workflows across M value streams' footer claim")
elif 'idx_wfs' in dir():
    n_wfs, n_declared_vs = int(fm.group(1).replace(',', '')), int(fm.group(2))
    if n_wfs != idx_wfs or n_declared_vs != n_vs:
        errors.append(f"touchpoint map footer declares {n_wfs:,} workflows / {n_declared_vs} value streams but index says {idx_wfs:,} / {n_vs}")
hm = re.search(r'^## Statutory & Gap-Analysis Value Streams \(VS-\d+\u2013VS-(\d+)\)', tmap, re.M)
if not hm:
    errors.append("touchpoint map: cannot find the '## Statutory & Gap-Analysis Value Streams (VS-a\u2013VS-b)' section heading")
elif int(hm.group(1)) != max_vs:
    errors.append(f"touchpoint map section heading ends at VS-{hm.group(1)} but the index max is VS-{max_vs}")
rows = {int(n) for n in re.findall(r'^\| VS-(\d+) \| ', tmap, re.M)}
missing = [v for v in range(79, max_vs + 1) if v not in rows]
if missing:
    errors.append(f"touchpoint map primary-module rows missing for: {', '.join('VS-' + str(v) for v in missing)}")

# ---- D: per-VS title cells == index canon (2026-09-15 thirty-third-wave) ----
# The §Statutory & Gap-Analysis table's 114 '| VS-nn | Title |' cells are a VS-name
# label surface no rule read: 64 carried authoring-time compressed forms while 50 rows
# were already byte-exact — drift, not convention, by the file's own majority (the same
# retired-abbreviation family waves 27/28 trued off the PA footers/H1s/quote-lines and
# the detailed-map bullets). Every title cell must now equal the canonical
# value-stream-index summary-row name, with the 114-row population asserted so a
# restructure cannot void the arm.
_idx_names = {}
for _m in re.finditer(r'^\|(?:[^|]*)\|\s*\[VS-(\d+)\]\([^)]*\)\s*\|([^|]*)\|', idx, re.M):
    _idx_names[int(_m.group(1))] = _m.group(2).strip()
_tcells = re.findall(r'^\| VS-(\d+) \|([^|]+)\|', tmap, re.M)
if len(_tcells) != 114:
    errors.append(f"touchpoint map per-VS table parses to {len(_tcells)} title cells, expected 114 (title-arm population)")
for _vs, _name in _tcells:
    _want = _idx_names.get(int(_vs))
    if _want is None:
        errors.append(f"touchpoint map row VS-{_vs} has no index summary row")
    elif _name.strip() != _want:
        errors.append(f"touchpoint map VS-{_vs} title cell '{_name.strip()}' != canonical '{_want}'")

print(f"A_ERRS={len(errors)}")
for e in errors: print(f"A_ERR|{e}")
print(f"B_STALE={len(stale)}")
for s in stale[:12]: print(f"B_STALE|{s}")
print(f"MAX_VS={max_vs}")
PY
)
A_ERRS=$(echo "$CHECK25" | sed -n 's/^A_ERRS=//p')
B_STALE=$(echo "$CHECK25" | sed -n 's/^B_STALE=//p')
MAX_VS=$(echo "$CHECK25" | sed -n 's/^MAX_VS=//p')
if [ "$A_ERRS" -eq 0 ]; then
    ok "Proposed-register mirror & touchpoint-map reconciliation claims match canonical figures (register tiers/total; footer 'Reconciled to' == index grand totals; section range ends at VS-$MAX_VS with full VS-row coverage; and all 114 per-VS title cells equal the canonical value-stream-index summary-row names — title arm added by the 2026-09-15 thirty-third-wave review after 64 compressed authoring-time forms were found stranded on the surface no rule read while 50 sibling rows were already byte-exact)"
else
    error "Criticality proposed-register mirror / touchpoint-map reconciliation mismatch ($A_ERRS):
"
    echo "$CHECK25" | grep '^A_ERR|' | sed 's/^A_ERR|/    /'
fi
if [ "$B_STALE" -eq 0 ]; then
    ok "No stale unclassified-workflow figure '2,564'/'2,596' in current-state prose (register at full coverage — 0 unclassified — since 2026-06-28; historical 'X -> Y' notes and CHANGELOG/workflow-gap-analysis/headcount-reality-check excluded)"
else
    warn "Stale unclassified-workflow figure '2,564'/'2,596' appears $B_STALE time(s) in current-state prose (register at full coverage since 2026-06-28 — use an 'X -> Y' change-note or drop the figure):"
    echo "$CHECK25" | grep '^B_STALE|' | sed 's/^B_STALE|/    /'
fi

# --- Check 26: dependency-map §8 cross-cutting-block reconciliation ---
echo "--- Check 26: dependency-map §8 block reconciliation ---"
# The dependency map's §8 mines inline 'VS-NN' references across the Statutory + gap-analysis
# block's PA and README files and self-declares its coverage: the section heading range
# (VS-79–VS-NN), the intro's block size (N value streams / M workflows), the §8.1 anchor
# top-10 table, and §8.4's per-program anchor-edge rows. Consistency review #14 (2026-06-28)
# found this block frozen at the v4.4 snapshot — heading/§8.1/§8.4 all ended at VS-191, the
# intro still said 113 value streams / 2,712 workflows (excluding both VS-192's +24 and the
# PA-127.4 extension's +8), and the v4.4 footer itself flagged 'VS-192 incorporation pending
# the next consistency review' — a pending item three reviews (#10–#13) shipped without
# action because no check guarded §8; the §8.1 table had also drifted (v4.3 counts, and a
# top-10 that omitted VS-91 while listing VS-100). All parts ERROR (the doc's claims are
# machine-verifiable):
#   A: §8 heading range end == index max active VS.
#   B: §8.4's last '| VS-NN |' program row == max VS (full block coverage).
#   C: §8 intro's declared 'N value streams / M workflows' == actual block content on disk
#      (VS-79..max directories; ## W headers in their PA files).
#   D: §8.1's anchor table == the live top-10 recomputed from PA+README reference mining
#      (membership AND counts) — enforcing the table's own 'freshly recomputed' claim, so
#      any content change that shifts reference counts must refresh the table.
CHECK26=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
WF = f"{ROOT}/01-model-company/workflows"
errors = []
idx = open(f"{WF}/value-stream-index.md", encoding='utf-8').read()
vs_nums = {int(n) for n in re.findall(r'\[VS-(\d+)\]\(', idx)}
max_vs = max(vs_nums) if vs_nums else 0
dep = open(f"{WF}/workflow-dependency-map.md", encoding='utf-8').read()

# ---- E: intro coverage parenthetical vs the PA corpus (2026-09-10 seventeenth-wave) ----
# The batch-24 pass updated the intro's unique-workflow figure but stranded the adjacent
# parenthetical at the retired 5,449-row total — the §8 guards (A–D) read only the §8
# block, and no rule re-derived the intro's register canon. Re-derive unique ## W ids and
# ### sub-workflow rows from the PA files every run and pin the intro's three figures.
_ids = set(); _sub = 0
for _d in os.listdir(WF):
    if not _d.startswith('VS-'): continue
    _dd = os.path.join(WF, _d)
    if not os.path.isdir(_dd): continue
    for _fn in os.listdir(_dd):
        if _fn.startswith('PA-') and _fn.endswith('.md'):
            _t = open(os.path.join(_dd, _fn), encoding='utf-8', errors='replace').read()
            _ids.update(re.findall(r'^## (W\d+[A-Z]?)\.', _t, re.M))
            _sub += len(re.findall(r'^### W\d+[A-Z]?\.', _t, re.M))
CU, CR = len(_ids), len(_ids) + _sub
m = re.search(r'All ([\d,]+) workflows are classified', dep)
if not m:
    errors.append("cannot find the dependency-map intro 'All N workflows are classified' figure")
elif int(m.group(1).replace(',', '')) != CU:
    errors.append(f"dependency-map intro says {m.group(1)} workflows are classified but the PA corpus re-derives {CU:,} unique ## headers")
m = re.search(r'register holds ([\d,]+) rows, incl\. ([\d,]+) `###` parent/summary', dep)
if not m:
    errors.append("cannot find the dependency-map intro 'register holds N rows, incl. K ### parent/summary' parenthetical")
else:
    if int(m.group(1).replace(',', '')) != CR:
        errors.append(f"dependency-map intro parenthetical says {m.group(1)} register rows but the PA corpus re-derives {CR:,} ({CU:,} unique + {_sub} ### sub-workflow rows)")
    if int(m.group(2).replace(',', '')) != _sub:
        errors.append(f"dependency-map intro parenthetical says {m.group(2)} ### sub-workflow rows but the PA corpus re-derives {_sub}")

# ---- A: §8 heading range end == index max active VS ----
hm = re.search(r'^## 8\. Cross-Cutting Program Dependencies \(VS-79\u2013VS-(\d+)\)', dep, re.M)
if not hm:
    errors.append("cannot find the '## 8. Cross-Cutting Program Dependencies (VS-79\u2013VS-N)' heading")
elif int(hm.group(1)) != max_vs:
    errors.append(f"\u00a78 heading range ends at VS-{hm.group(1)} but the index max active VS is VS-{max_vs}")

# ---- B: §8.4's last program row == max VS ----
m84 = re.search(r'^### 8\.4 .*?\n(.*?)(?=^>|\Z)', dep, re.M | re.S)
if not m84:
    errors.append("cannot find the '### 8.4' program-anchor table section")
else:
    rows = [int(n) for n in re.findall(r'^\| VS-(\d+) \| ', m84.group(1), re.M)]
    if not rows:
        errors.append("\u00a78.4 has no '| VS-NN |' program rows")
    elif rows[-1] != max_vs:
        errors.append(f"\u00a78.4's last program row is VS-{rows[-1]} but the index max active VS is VS-{max_vs} (block coverage incomplete)")

# ---- C: §8 intro's declared block size == disk ----
# The intro is a wrapped markdown blockquote ('> ... \n> ...'), so normalize newlines and
# quote markers to single spaces before parsing the 'added N value streams / M workflows' claim.
intro_flat = re.sub(r'\s+', ' ', re.sub(r'[\n>]+', ' ', dep[hm.start():dep.find('### 8.1')] if hm else dep))
block_dirs = []
for d in sorted(os.listdir(WF)):
    m = re.match(r'VS-(\d+)-', d)
    if m and 79 <= int(m.group(1)) <= max_vs and os.path.isdir(os.path.join(WF, d)):
        block_dirs.append(d)
wf_disk = 0
for d in block_dirs:
    for fn in sorted(os.listdir(os.path.join(WF, d))):
        if fn.startswith("PA-") and fn.endswith(".md"):
            txt = open(os.path.join(WF, d, fn), encoding='utf-8', errors='replace').read()
            wf_disk += len(re.findall(r'^## W\d+[A-Z]?\.', txt, re.M))
im = re.search(r'added (\d+) value streams / ([\d,]+) workflows', intro_flat)
if not im:
    errors.append("cannot parse the §8 intro's 'added N value streams / M workflows' claim")
else:
    decl_vs, decl_wf = int(im.group(1)), int(im.group(2).replace(',', ''))
    if (decl_vs, decl_wf) != (len(block_dirs), wf_disk):
        errors.append(f"§8 intro declares {decl_vs} value streams / {decl_wf:,} workflows but the block on disk holds {len(block_dirs)} / {wf_disk:,}")

# ---- D: §8.1 anchor table == live top-10 recomputed from PA+README mining ----
counts = {}
for d in block_dirs:
    files = [os.path.join(WF, d, "README.md")] + [os.path.join(WF, d, fn) for fn in sorted(os.listdir(os.path.join(WF, d))) if fn.startswith("PA-") and fn.endswith(".md")]
    for fp in files:
        if not os.path.exists(fp):
            continue
        for mm in re.finditer(r'VS-(\d{1,3})(?![0-9])', open(fp, encoding='utf-8', errors='replace').read()):
            counts[mm.group(1)] = counts.get(mm.group(1), 0) + 1
want = sorted(counts.items(), key=lambda kv: (-kv[1], int(kv[0])))[:10]
m81 = re.search(r'^### 8\.1 .*?\n(.*?)(?=^### )', dep, re.M | re.S)
if not m81:
    errors.append("cannot find the '### 8.1' anchor table section")
else:
    got = [(k, int(v.replace(',', ''))) for k, v in re.findall(r'^\| VS-(\d+) \| [^|]+ \| ([\d,]+) \|$', m81.group(1), re.M)]
    if got != want:
        errors.append(f"§8.1 anchor table is not the live top-10 (freshly recomputed from VS-79\u2013VS-{max_vs} PA+README mining): table={[(('VS-'+k), v) for k, v in got]} live={[(('VS-'+k), v) for k, v in want]}")

# ---- F: §8 program-table VS-name cells == index canon + §1–§7 W-label guard (2026-09-15 thirty-third-wave) ----
# The §8.1/§8.2/§8.3 tables' VS-name cells and the §1–§7 dependency-tree 'Wnnn (Label)'
# labels were navigation surfaces no rule read: the §8 tables carried 32 compressed
# authoring-time name forms (incl. the retired VS-100 '…& IP' abbreviation waves 27/28
# retired from the PA footers/H1s/quote-lines), and §2.9's statutory tax chain named
# 'W140 (Corporate Income Tax)' — W140 is OHS Incident Management (VS-24), correctly
# labeled by the map's own §2.9/§4 since the initial commit while the chain line carried
# the wrong W-id from that same commit (PA-17.3's sibling-set prose — W90 monthly BIR
# filing, W260 eFPS filing, W407 corporate income tax computation, W475 CWT 2307
# collection — names the intended node). Every §8 VS-name cell must now equal the
# canonical value-stream-index summary-row name (populations asserted), and every
# §1–§7 'Wnnn (Label)' label must share a significant token with the PA ##/###/####
# W-header canon title for that W-id or appear on the adjudicated compressed-form
# allowlist — so a wrong-subject label (the defect class) can never ship silently.
_canon = {}
for _m in re.finditer(r'^\|(?:[^|]*)\|\s*\[VS-(\d+)\]\([^)]*\)\s*\|([^|]*)\|', idx, re.M):
    _canon[int(_m.group(1))] = _m.group(2).strip()
if len(_canon) != 188:
    errors.append(f"index summary rows parse to {len(_canon)} names, expected 188 (name-canon parse broken)")
_m81 = re.search(r'^### 8\.1 .*?\n(.*?)(?=^### )', dep, re.M | re.S)
if not _m81:
    errors.append("cannot find the '### 8.1' section for the name arm")
else:
    _rows81 = re.findall(r'^\| VS-(\d+) \| ([^|]+?) \|', _m81.group(1), re.M)
    if len(_rows81) != 10:
        errors.append(f"§8.1 anchor table parses to {len(_rows81)} name cells, expected 10 (name arm population)")
    for _vs, _name in _rows81:
        if _canon.get(int(_vs)) != _name.strip():
            errors.append(f"§8.1 VS-{_vs} name cell '{_name.strip()}' != canonical '{_canon.get(int(_vs))}'")
_i82 = dep.find('### 8.2')
_rows823 = re.findall(r'^\| VS-(\d+) ([^|]+?)\s*\|', dep[_i82:], re.M)
if len(_rows823) != 39:
    errors.append(f"§8.2–§8.3 program tables parse to {len(_rows823)} name cells, expected 39 (name arm population)")
for _vs, _name in _rows823:
    if _canon.get(int(_vs)) != _name.strip():
        errors.append(f"§8.2–8.3 VS-{_vs} name cell '{_name.strip()}' != canonical '{_canon.get(int(_vs))}'")
_pa_titles = {}
for _d in os.listdir(WF):
    if not _d.startswith('VS-'): continue
    _dd = os.path.join(WF, _d)
    if not os.path.isdir(_dd): continue
    for _fn in os.listdir(_dd):
        if _fn.startswith('PA-') and _fn.endswith('.md'):
            for _ln in open(os.path.join(_dd, _fn), encoding='utf-8', errors='replace'):
                _m = re.match(r'^(#{2,4}) (W\d+[A-Za-z]?)[.\s]\s*(.+?)\s*$', _ln)
                if _m and _m.group(2) not in _pa_titles:
                    _pa_titles[_m.group(2)] = _m.group(3)
_i1 = dep.find('## 1. Master Data Dependency Tree'); _i8 = dep.find('## 8. Cross-Cutting Program Dependencies')
_TREE = dep[_i1:_i8] if 0 <= _i1 < _i8 else ''
if not _TREE:
    errors.append("cannot slice the §1–§7 dependency-tree body for the W-label arm")
_STOP = {'the', 'and', 'of', 'for', 'with', 'per', 'via', 'in', 'on', 'to', 'at', 'by', 'a', 'an', 'vs'}
def _toks(s):
    s = re.sub(r'[^a-z0-9 &/\u2014-]', ' ', s.lower())
    return {w for w in re.split(r'[\s/&\u2014,()-]+', s) if w and w not in _STOP}
_ALLOW = {  # adjudicated compressed/jargon forms (2026-09-15 thirty-third-wave): the label
            # shares no token with the PA canon title by design (module shorthand, legacy
            # document names) — anything else zero-overlap is the wrong-subject defect class
    ('W14', 'IC'), ('W158', 'BC Drills'), ('W2', 'PO'), ('W27', 'Rebates'), ('W41', 'Complaints'),
    ('W56', 'Backorders'), ('W5B', 'Trade Account Sales'), ('W5F', 'EOD'), ('W65', 'CSAT'),
    ('W7', 'AP'), ('W8', 'AR'), ('W8', 'AR Invoicing'), ('W82', 'Hazmat')}
_seen_labels = 0
for _m in re.finditer(r'\b(W\d+[A-Z]?) \(([^()]*)\)', _TREE):
    _w, _label = _m.group(1), _m.group(2)
    _seen_labels += 1
    if _w not in _pa_titles:
        errors.append(f"§1–§7 tree label '{_w} ({_label})' names a W-id with no PA header")
        continue
    _base = re.split(r'\s+\u2014\s+', _label)[0]
    if _toks(_base) and not (_toks(_base) & _toks(_pa_titles[_w])) and (_w, _base) not in _ALLOW:
        errors.append(f"§1–§7 tree label '{_w} ({_base})' shares no token with the PA canon '{_pa_titles[_w]}' and is not on the adjudicated compressed-form allowlist")
if _seen_labels < 200:
    errors.append(f"§1–§7 W-label arm parsed only {_seen_labels} labels, expected >= 200 (parse broken)")


print(f"MAX_VS={max_vs}")

print(f"A_ERRS={len(errors)}")
for e in errors: print(f"A_ERR|{e}")
print(f"BLOCK_VS={len(block_dirs)}")
print(f"BLOCK_WF={wf_disk}")
PY
)
C26_ERRS=$(echo "$CHECK26" | sed -n 's/^A_ERRS=//p')
C26_MAXVS=$(echo "$CHECK26" | sed -n 's/^MAX_VS=//p')
C26_VS=$(echo "$CHECK26" | sed -n 's/^BLOCK_VS=//p')
C26_WF=$(echo "$CHECK26" | sed -n 's/^BLOCK_WF=//p')
if [ "$C26_ERRS" -eq 0 ]; then
    ok "Dependency-map §8 block reconciliation: heading/§8.4 end at VS-$C26_MAXVS, intro block size ($C26_VS value streams / $C26_WF workflows) matches disk, the §8.1 anchor table equals the live top-10 (freshly recomputed from PA+README reference mining), the intro coverage figures (5,427 unique / 5,450 rows / 23 sub-workflows) match the PA corpus re-derivation, and the §8.1/§8.2/§8.3 VS-name cells (10 + 39, populations asserted) equal the canonical value-stream-index summary-row names while all §1–§7 'Wnnn (Label)' tree labels token-overlap the PA W-header canon or sit on the adjudicated 13-entry compressed-form allowlist (intro pins added by the 2026-09-10 seventeenth-wave review; name + W-label arms added by the 2026-09-15 thirty-third-wave review after §2.9's tax chain was found carrying 'W140 (Corporate Income Tax)' — the wrong W-id, stranded since the initial commit — and 32 compressed §8 name forms were found stranded beside 17 byte-exact siblings)"
else
    error "Dependency-map §8 self-declared coverage does not reconcile ($C26_ERRS mismatch(es)) — the block tables must be re-mined/recomputed:"
    echo "$CHECK26" | grep '^A_ERR|' | sed 's/^A_ERR|/    /'
fi

# --- Check 27: stale register-row figures + unclassified-workflow claims ---
echo "--- Check 27: stale register-row figures & unclassified-workflow claims ---"
# Two guards closed by consistency review #15 (2026-06-28):
#   (A) the Full-Coverage Confirmation Pass updated the register's Summary table to 5,372 rows
#       (5,349 unique) but left three current-state prose figures frozen at the pre-pass state:
#       the root README's folder-tree '(2,776 rows)', the register's own Summary note 'the
#       remaining 2,753 are canonical ## workflows', and the §Domain Breakdown 'breakdown of
#       the 2,776 classified workflows'. '2,776' was the v7.26 register-row total; '2,753' its
#       unique-workflow complement (2,776 - 23 parents). Both are guarded with the same
#       SKIP-docs / 'X -> Y' change-note exclusions as Checks 24B and 25B (canonical: 5,372
#       rows / 5,349 unique).
#   (B) the dependency map's §8 coverage note still claimed 'VS-192 remains unclassified
#       pending criticality review' — true when v4.5 shipped, superseded the same day by the
#       Full-Coverage Confirmation Pass. With all 5,349 workflows classified, any
#       unclassified-workflow claim in workflow-dependency-map.md is stale by definition (the
#       register's own dated 2026-06-14 addition notes are the historical record and stay
#       exempt — this map carries no such dated-note convention).
CHECK27=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
stale = []
errs = []
# ---- Part A: stale register-row figures '2,776' / '2,753' in current-state prose ----
SKIP = {'CHANGELOG.md', 'workflow-gap-analysis.md', 'headcount-reality-check.md'}
for fig in ('2,776', '2,753'):
    pat = re.compile(r'(?<!\d)' + fig + r'(?!\d)')
    for dirpath, _d, files in os.walk(ROOT):
        if os.sep + '.git' in dirpath: continue
        for fn in files:
            if not fn.endswith('.md') or fn in SKIP: continue
            path = os.path.join(dirpath, fn)
            txt = open(path, encoding='utf-8', errors='replace').read()
            for m in pat.finditer(txt):
                lo = max(0, m.start()-25); hi = min(len(txt), m.end()+25)
                if '->' in txt[lo:hi] or '\u2192' in txt[lo:hi]:
                    continue  # legitimate historical 'X -> Y' change-note
                line_no = txt.count('\n', 0, m.start()) + 1
                stale.append(f"{os.path.relpath(path, ROOT)}:{line_no} ({fig})")
# ---- Part B: unclassified-workflow claims in workflow-dependency-map.md ----
DEP = os.path.join(ROOT, '01-model-company', 'workflows', 'workflow-dependency-map.md')
dep = open(DEP, encoding='utf-8', errors='replace').read()
for i, ln in enumerate(dep.split('\n'), 1):
    if 'remains unclassified' in ln or 'pending criticality review' in ln:
        errs.append(f"workflow-dependency-map.md:{i} asserts an unclassified/pending state, but all 5,427 workflows have been classified (2026-06-28 Full-Coverage Confirmation Pass; 2026-09-02 post-catalog confirmation of W5497–W5510; 2026-09-03 W5511; 2026-09-03 W5512–W5514; 2026-09-03 W5515–W5517; 2026-09-10 W5574)")
# ---- Part C: PA-corpus live-total guard (2026-09-09 fourteenth-wave review) ----
# The gap-fill batches re-pointed every navigation surface each time the unique total
# moved, but one surface family no check read was the PA files' own field rows: at ship
# time PA-128.3's W5512 Volume row still quoted the '5,370-workflow Automation Opportunity
# inventory' although batches 15–23 had since grown the corpus to 5,426. Every interim
# unique-workflow total must not appear workflow-adjacent in any PA file's live prose.
# 2026-09-10 seventeenth-wave extension: the static band (5,320–5,425) aged out the moment
# batch-24 made 5,427 canonical — PA-128.3's own Volume row stranded at the retired 5,426
# and nothing fired. The band now re-derives from the corpus every run: any integer in
# [5,320, canon-unique) that is workflow-adjacent in live PA prose is an error, so the
# guard re-arms itself at every future batch (the '*Date:' footer lines remain exempt as
# the historical record; the '~5,400 accounts' trade/corporate canon never matches — the
# rule requires workflow adjacency).
_idsC = set()
WFR = os.path.join(ROOT, '01-model-company', 'workflows')
for _d in os.listdir(WFR):
    if not _d.startswith('VS-'): continue
    _dd = os.path.join(WFR, _d)
    if not os.path.isdir(_dd): continue
    for _fn in os.listdir(_dd):
        if _fn.startswith('PA-') and _fn.endswith('.md'):
            _idsC.update(re.findall(r'^## (W\d+[A-Z]?)\.',
                open(os.path.join(_dd, _fn), encoding='utf-8', errors='replace').read(), re.M))
CANON = len(_idsC)
TOTAL_PAT = re.compile(r'\b([0-9][0-9,]*)\b(?=(?:-\s*|\s+)workflows?\b)', re.I)
for pa in sorted(os.path.join(ROOT, '01-model-company', 'workflows', d, f)
                 for d in os.listdir(os.path.join(ROOT, '01-model-company', 'workflows'))
                 if d.startswith('VS-')
                 for f in os.listdir(os.path.join(ROOT, '01-model-company', 'workflows', d))
                 if f.startswith('PA-') and f.endswith('.md')):
    for i, ln in enumerate(open(pa, encoding='utf-8', errors='replace'), 1):
        if ln.lstrip().startswith('*Date:'):
            continue
        for m in TOTAL_PAT.finditer(ln):
            n = int(m.group(1).replace(',', ''))
            if 5320 <= n < CANON:
                errs.append(f"{os.path.relpath(pa, ROOT)}:{i} quotes retired corpus total '{m.group(1)}' workflow-adjacent in live prose (canonical unique total: {CANON:,}; the [5,320, canon) band re-derives from the corpus every run)")
                break
print(f"A_STALE={len(stale)}")
for s in stale[:12]: print(f"A_STALE|{s}")
print(f"B_ERRS={len(errs)}")
for e in errs: print(f"B_ERR|{e}")
PY
)
C27_STALE=$(echo "$CHECK27" | sed -n 's/^A_STALE=//p')
C27_ERRS=$(echo "$CHECK27" | sed -n 's/^B_ERRS=//p')
if [ "$C27_STALE" -eq 0 ]; then
    ok "No stale register-row figure '2,776'/'2,753' in current-state prose (canonical figures are 5,393 rows / 5,370 unique since the 2026-09-03 sourcing-model gap-fill pass added W5515–W5517; historical 'X -> Y' notes and CHANGELOG/workflow-gap-analysis/headcount-reality-check excluded)"
else
    warn "Stale register-row figure '2,776'/'2,753' appears $C27_STALE time(s) in current-state prose (canonical figures are 5,393 rows / 5,370 unique — use an 'X -> Y' change-note or update the figure):"
    echo "$CHECK27" | grep '^A_STALE|' | sed 's/^A_STALE|/    /'
fi
if [ "$C27_ERRS" -eq 0 ]; then
    ok "No unclassified-workflow claims in workflow-dependency-map.md and no retired corpus-total literal (any workflow-adjacent integer in the self-re-arming [5,320, canon) band) in any PA file's live prose (canon: 5,427 unique; Part C added by the 2026-09-09 fourteenth-wave review after PA-128.3's W5512 Volume row shipped '5,370-workflow inventory' through batches 15–23 on a surface no check read; band made corpus-derived by the 2026-09-10 seventeenth-wave review after the same row stranded at the then-canonical 5,426 with the static band blind to it)"
else
    error "Stale unclassified-workflow claims / retired corpus-total literals in live prose ($C27_ERRS):"
    echo "$CHECK27" | grep '^B_ERR|' | sed 's/^B_ERR|/    /'
fi

# --- Check 28: requirements-TOC letter-suffixed-ID claims + proposed-register description staleness ---
echo "--- Check 28: requirements-TOC letter-suffixed IDs & proposed-register descriptions ---"
# Two guards closed by consistency review #16 (2026-06-28):
#   (A) the erp-requirements.md TOC's R5 row claimed '(incl. POS-014a, POS-022a)' but no
#       POS-022a exists anywhere — the four letter-suffixed IDs are NFR-022a, POS-014a,
#       PUR-025a/b. The TOC's 'incl.' claims must all exist as defined rows AND must cover
#       every letter-suffixed ID defined in the doc (phantom claims and omissions both fail).
#   (B) with the proposed register at 0 rows since the 2026-06-28 Full-Coverage Confirmation
#       Pass, navigation descriptions of workflow-criticality-proposed.md must not assert a
#       'remaining unclassified' population (stale current-state prose) and must carry the
#       'currently empty' marker; if the register ever repopulates (new workflows shipping
#       unclassified), the guard flips and demands the descriptions stop claiming emptiness.
CHECK28=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
errs = []
warns = []
# ---- Part A: TOC letter-suffixed-ID claims vs defined letter-suffixed IDs ----
REQ = os.path.join(ROOT, '01-model-company', 'erp-requirements.md')
txt = open(REQ, encoding='utf-8', errors='replace').read()
toc_end = txt.find('\n## R1.')
toc = txt[:toc_end] if toc_end != -1 else txt
claimed = set()
for m in re.finditer(r'\(incl\.\s+([^)]*)\)', toc):
    for tok in re.finditer(r'([A-Z]{2,4}-\d+)((?:[a-z])(?:/[a-z])*)', m.group(1)):
        base, suffixes = tok.group(1), tok.group(2)
        for suf in [s for s in suffixes.split('/') if s]:
            claimed.add(base + suf)
defined = set(m.group(1) for m in re.finditer(r'^\|\s*([A-Z]{2,4}-\d+[a-z])\s*\|', txt, re.M))
for phantom in sorted(claimed - defined):
    errs.append(f"erp-requirements.md TOC claims letter-suffixed ID {phantom}, but no such requirement row exists")
for missing in sorted(defined - claimed):
    errs.append(f"erp-requirements.md defines letter-suffixed ID {missing}, but the TOC's '(incl. ...)' claims omit it")
# ---- Part B: proposed-register description staleness in navigation docs ----
PROP = os.path.join(ROOT, '01-model-company', 'workflows', 'workflow-criticality-proposed.md')
prop = open(PROP, encoding='utf-8', errors='replace').read()
m = re.search(r'\*\*Workflow coverage:\*\*\s*(\d+) unclassified workflows', prop)
coverage = int(m.group(1)) if m else -1
if coverage == -1:
    warns.append("workflow-criticality-proposed.md: cannot parse the '**Workflow coverage:** N unclassified workflows' banner line")
else:
    spots = [
        ('README.md', 'tree'),
        (os.path.join('01-model-company', 'workflows', 'README.md'), 'nav table'),
        (os.path.join('01-model-company', 'workflows', 'WORKFLOW-FORMAT-GUIDE.md'), 'Related Documents table'),
    ]
    for rel, kind in spots:
        path = os.path.join(ROOT, rel)
        lines = open(path, encoding='utf-8', errors='replace').read().split('\n')
        for i, ln in enumerate(lines, 1):
            if 'workflow-criticality-proposed.md' not in ln:
                continue
            if 'validate-repo' in ln or ln.lstrip().startswith('#') or ln.lstrip().startswith('*'):
                continue  # tool rows, headings, and dated version-note footers are not current-state descriptions
            if coverage == 0:
                if re.search(r'remaining unclassified', ln, re.I):
                    warns.append(f"{rel}:{i} still describes workflow-criticality-proposed.md as holding 'the remaining unclassified workflows', but the register has stood at 0 rows since the 2026-06-28 Full-Coverage Confirmation Pass")
                elif 'empty' not in ln.lower():
                    warns.append(f"{rel}:{i} describes workflow-criticality-proposed.md without any emptiness marker while the register stands at 0 rows")
            else:
                if 'currently empty' in ln:
                    warns.append(f"{rel}:{i} claims workflow-criticality-proposed.md is 'currently empty', but the register holds {coverage} unclassified workflows")
print(f"A_ERRS={len(errs)}")
for e in errs: print(f"A_ERR|{e}")
print(f"B_WARNS={len(warns)}")
for w in warns: print(f"B_WARN|{w}")
PY
)
C28_ERRS=$(echo "$CHECK28" | sed -n 's/^A_ERRS=//p')
C28_WARNS=$(echo "$CHECK28" | sed -n 's/^B_WARNS=//p')
if [ "$C28_ERRS" -eq 0 ]; then
    ok "erp-requirements.md TOC '(incl. ...)' letter-suffixed-ID claims match the defined letter-suffixed requirement rows exactly (no phantom IDs, no omissions)"
else
    error "erp-requirements.md TOC letter-suffixed-ID claims do not match the defined letter-suffixed requirement rows ($C28_ERRS):"
    echo "$CHECK28" | grep '^A_ERR|' | sed 's/^A_ERR|/    /'
fi
if [ "$C28_WARNS" -eq 0 ]; then
    ok "Navigation descriptions of workflow-criticality-proposed.md (root README tree, workflows/README.md, WORKFLOW-FORMAT-GUIDE.md) match the register's current state (0 unclassified rows — descriptions carry the 'currently empty' marker)"
else
    warn "Navigation descriptions of workflow-criticality-proposed.md drifted from the register's current state ($C28_WARNS):"
    echo "$CHECK28" | grep '^B_WARN|' | sed 's/^B_WARN|/    /'
fi

# --- Check 29: repo-wide markdown table structural integrity (delimiter + data rows) ---
echo "--- Check 29: repo-wide table delimiter/data-row column integrity ---"
# Consistency review #17 (2026-06-28) found 18 table defects no prior check saw:
# Check 13 scans only the summary docs and only compares DATA rows to the header — the
# delimiter (separator) row was never validated, and the 569 PA files were never scanned
# for either. GFM requires the delimiter row to match the header cell count or the table
# is NOT RECOGNIZED AT ALL (the block renders as plain text on GitHub). Defect classes
# found & repaired by 07-methodology/fix-table-structure.py (companion script):
#   (a) 9 delimiter rows missing columns (5-col Steps tables with 4-cell delimiters;
#       a 2-col Field/Detail table with a 1-cell delimiter) — VS-09 x3, VS-11, VS-13,
#       VS-20, VS-28, VS-29 x2;
#   (b) 7 delimiter rows with excess columns (2-col Field/Detail tables carrying a
#       4/5-cell steps-delimiter) — VS-105 x5, VS-133, VS-170;
#   (c) a doubled delimiter line under one header — VS-29 PA-29.2;
#   (d) a stray 1-cell '| **Steps** |' data row inside a 2-col Field/Detail table —
#       VS-162 PA-162.3.
# This check re-scans ALL .md files (code-fence aware, escaped-pipe aware — '\|' is a
# literal, not a cell separator, per CommonMark) for delimiter-vs-header mismatches and
# data-row-vs-header mismatches, so neither class can ship silently again. It subsumes
# Check 13's second half over a wider scope (13 is retained for its leading-whitespace
# guard and its focused summary-doc reporting).
CHECK29=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
SEP = re.compile(r'^\|[\s:|-]+\|\s*$')
def ncells(s):
    return re.sub(r'\\\|', '', s).count('|') - 1
sep_bad, row_bad = [], []
for dirpath, _d, files in os.walk(ROOT):
    if os.sep + '.git' in dirpath or '__pycache__' in dirpath: continue
    for fn in sorted(files):
        if not fn.endswith('.md'): continue
        path = os.path.join(dirpath, fn)
        rel = os.path.relpath(path, ROOT)
        lines = open(path, encoding='utf-8', errors='replace').read().split('\n')
        fence = False; hdr = None
        for i, ln in enumerate(lines):
            if ln.startswith('```'): fence = not fence; hdr = None; continue
            if fence: continue
            if ln.startswith('|'):
                if SEP.match(ln):
                    if hdr is not None and ncells(ln) != hdr:
                        sep_bad.append(f"{rel}:{i+1} delimiter {ncells(ln)} cells vs header {hdr}: {ln[:50]}")
                    continue
                nxt = lines[i+1] if i+1 < len(lines) else ''
                if SEP.match(nxt):
                    hdr = ncells(ln); continue
                if hdr is not None and ncells(ln) != hdr:
                    row_bad.append(f"{rel}:{i+1} data row {ncells(ln)} cells vs header {hdr}: {ln[:50]}")
            else:
                hdr = None
print(f"SEP={len(sep_bad)} ROW={len(row_bad)}")
for x in sep_bad: print(f"SEP|{x}")
for x in row_bad: print(f"ROW|{x}")
PY
)
C29_SEP=$(echo "$CHECK29" | sed -n 's/^SEP=\([0-9]*\).*/\1/p')
C29_ROW=$(echo "$CHECK29" | sed -n 's/.*ROW=\([0-9]*\)$/\1/p')
if [ "${C29_SEP:-1}" -eq 0 ] && [ "${C29_ROW:-1}" -eq 0 ]; then
    ok "All markdown tables repo-wide (779 .md files incl. 569 PA files) have delimiter and data rows matching their header column count (code-fence & escaped-pipe aware)"
else
    error "Markdown table structural defects found (delimiter: $C29_SEP, data-row: $C29_ROW) — GFM will not recognize tables whose delimiter row mismatches the header; run 07-methodology/fix-table-structure.py:"
    echo "$CHECK29" | grep -E '^(SEP\||ROW\|)' | sed 's/^SEP|/    /; s/^ROW|/    /' | head -25
fi

# --- Check 30: PA TOC hygiene (completeness, duplicates, stray fragments) ---
echo "--- Check 30: PA-file TOC completeness & stray-fragment guard ---"
# Consistency review #18 (2026-06-28) found a defect class Check 23 cannot see: Check 23
# verifies every TOC ANCHOR resolves to a heading, but never asks whether the TOC is
# complete, de-duplicated, or free of debris. Found & repaired by
# 07-methodology/fix-toc-completeness.py (companion script):
#   (a) stray mid-file TOC fragments — nav lists left inside the workflow body when
#       appended workflows were merged (VS-04 PA-04.2: 6 lines; VS-06 PA-06.2: 2 lines);
#   (b) duplicate TOC entries (the ID-level symptom of (a));
#   (c) a shipped workflow heading with NO TOC entry (VS-12 PA-12.2: W1318 — invisible
#       in the file's navigation).
# Convention (WORKFLOW-FORMAT-GUIDE.md): the TOC indexes '## W…' (h2) workflows only —
# '### W…' parent/summary sub-workflows are deliberately not TOC-indexed.
CHECK30=$(python3 - "$REPO_ROOT" <<'PY'
import glob, os, re, sys
ROOT = sys.argv[1]
WF = os.path.join(ROOT, "01-model-company", "workflows")
TOC_LINE = re.compile(r"^- \[(W[^\]]+)\]\(#([^)]+)\)")
H2 = re.compile(r"^## (W\d+[A-Z]?(?:\.\d+[a-z]?)?)\. ")
stray = dup = missing = 0
for path in sorted(glob.glob(os.path.join(WF, "VS-*", "PA-*.md"))):
    rel = os.path.relpath(path, ROOT)
    lines = open(path, encoding="utf-8").read().split("\n")
    seen_first_wf = False
    toc, heads = [], []
    for i, ln in enumerate(lines, 1):
        if H2.match(ln):
            seen_first_wf = True
            heads.append(H2.match(ln).group(1))
        m = TOC_LINE.match(ln)
        if m:
            toc.append(re.match(r"(W\d+[A-Z]?(?:\.\d+[a-z]?)?)", m.group(1)).group(1))
            if seen_first_wf:
                stray += 1
                print(f"STRAY|{rel}:{i}: TOC line after first workflow heading")
    for w, c in __import__("collections").Counter(toc).items():
        if c > 1:
            dup += 1
            print(f"DUP|{rel}: TOC entry {w} listed {c}x")
    for w in heads:
        if w not in toc:
            missing += 1
            print(f"MISS|{rel}: workflow {w} has no TOC entry")
print(f"TOTALS stray={stray} dup={dup} missing={missing}")
PY
)
C30_TOTALS=$(echo "$CHECK30" | sed -n 's/^TOTALS stray=\([0-9]*\) dup=\([0-9]*\) missing=\([0-9]*\)$/\1 \2 \3/p')
C30_STRAY=$(echo "$C30_TOTALS" | cut -d' ' -f1); C30_DUP=$(echo "$C30_TOTALS" | cut -d' ' -f2); C30_MISS=$(echo "$C30_TOTALS" | cut -d' ' -f3)
if [ "${C30_STRAY:-1}" -eq 0 ] && [ "${C30_DUP:-1}" -eq 0 ] && [ "${C30_MISS:-1}" -eq 0 ]; then
    ok "All 569 PA-file TOCs are complete (every ## workflow indexed), duplicate-free, and free of stray mid-file fragments"
else
    error "PA TOC hygiene defects found (stray: $C30_STRAY, duplicate: $C30_DUP, missing: $C30_MISS) — run 07-methodology/fix-toc-completeness.py:"
    echo "$CHECK30" | grep -E '^(STRAY\||DUP\||MISS\|)' | sed 's/^[A-Z]*|/    /' | head -25
fi

# --- Check 31: PA-name 3-way consistency (H1 vs VS-README row vs index bullet) ---
echo "--- Check 31: PA-name 3-way consistency ---"
# Consistency review #18 (2026-06-28) found 38 name drifts across the three places a
# process-area name is stated (PA file H1, VS README 'Process Areas' row, value-stream-index
# bullet) — 37 H1s that had drifted from the canonical index/README name (mostly
# Expansion-block shortenings like 'Coupon & Voucher Creation' vs 'Coupon & Voucher
# Creation & Distribution', 'and'/'&' and ':'/'—' variants) plus one VS README outlier
# (PA-69.1). Repaired by 07-methodology/fix-pa-names.py; canonical source = index bullet.
CHECK31=$(python3 - "$REPO_ROOT" <<'PY'
import glob, os, re, sys
ROOT = sys.argv[1]
WF = os.path.join(ROOT, "01-model-company", "workflows")
idx = open(os.path.join(WF, "value-stream-index.md"), encoding="utf-8").read()
idx_pa = {m.group(1): (m.group(2), m.group(3)) for m in re.finditer(
    r"^- \*\*(PA-\d+\.\d+)\*\* \[([^\]]+)\]\(([^)]+)\) — (\d+) workflows", idx, re.M)}
# Canonical VS-name canon from the index summary rows (family cell may be empty), with the
# summary-row count asserted: the VS-README H1's 'VS-nn: Name' title is a fourth name surface
# no rule read — the 2026-09-14 twenty-seventh-wave review found 4 drifted H1s (VS-101/114/130/192)
# after the gap-fill batches renamed the index rows and re-pointed only Check 31's three surfaces.
bad = 0
vs_canon = {}
for m in re.finditer(r"^\|\s*[^|]*\|\s*\[(VS-\d+)\]\((VS-\d+-[a-z0-9-]+)/README\.md\) \| ([^|]+) \|", idx, re.M):
    vs_canon[m.group(2)] = m.group(3).strip()
if len(vs_canon) != 188:
    bad += 1
    print(f"BAD|value-stream-index summary rows: {len(vs_canon)} carry a VS link (expected 188)")
for vsdir in sorted(glob.glob(os.path.join(WF, "VS-*"))):
    vrd = open(os.path.join(vsdir, "README.md"), encoding="utf-8").read()
    vsname_m = re.match(r"^# (VS-\d+): (.+)$", vrd.split("\n", 1)[0])
    if vsname_m:
        vd = os.path.basename(vsdir)
        if vsname_m.group(1) != "VS-" + vd.split("-")[1]:
            bad += 1; print(f"BAD|{vd}/README.md: H1 VS-number {vsname_m.group(1)} disagrees with folder")
        elif vd in vs_canon and vsname_m.group(2).strip() != vs_canon[vd]:
            bad += 1; print(f"BAD|{vd}/README.md: H1 VS name {vsname_m.group(2).strip()!r} != canonical {vs_canon[vd]!r}")
    else:
        bad += 1; print(f"BAD|{os.path.relpath(vsdir, ROOT)}/README.md: H1 is not '# VS-nn: <Name>'")
    vr = {m.group(1): (m.group(3).strip(), m.group(2)) for m in re.finditer(
        r"^\| \[(PA-\d+\.\d+)\]\(([^)]+)\) \| ([^|]+) \| \d+ \|", vrd, re.M)}
    for p in sorted(glob.glob(os.path.join(vsdir, "PA-*.md"))):
        pid = re.match(r"(PA-\d+\.\d+)-", os.path.basename(p)).group(1)
        rel = os.path.relpath(p, ROOT)
        h1 = open(p, encoding="utf-8").read().split("\n", 1)[0]
        if pid not in idx_pa:
            bad += 1; print(f"BAD|{rel}: PA absent from value-stream-index bullets"); continue
        cname, clink = idx_pa[pid]
        if h1 != f"# {pid} — {cname}":
            bad += 1; print(f"BAD|{rel}: H1 {h1!r} != canonical '# {pid} — {cname}'")
        if pid in vr:
            rname, rlink = vr[pid]
            if rname != cname:
                bad += 1; print(f"BAD|{os.path.relpath(vsdir, ROOT)}/README.md: {pid} row name {rname!r} != canonical {cname!r}")
            if os.path.basename(p) != rlink:
                bad += 1; print(f"BAD|{os.path.relpath(vsdir, ROOT)}/README.md: {pid} links {rlink!r} != file {os.path.basename(p)!r}")
        else:
            bad += 1; print(f"BAD|{os.path.relpath(vsdir, ROOT)}/README.md: {pid} has no Process Areas row")
# (c) twenty-eighth wave: the PA header quote-line ('> Part of **[VS-nn: Name](./README.md)** ...')
# is the fifth VS-name label surface — and the value-stream-index detailed-map bullets carry the
# VS-name a sixth time. The 2026-09-14 twenty-eighth-wave review found 14 drifted quote-line VS
# names (VS-48.2/.3, VS-100/114/130/192 ×3 — twelve of them in the very files whose footers the
# twenty-seventh wave trued one paragraph away) and one drifted detailed-map VS bullet (VS-192,
# the class that wave adjudicated clean), all stranded by the same expansion-era index renames.
# The quote-line must be read JOINED over its wrapped '>' lines (the VS-190/191/192 quote-lines
# split across a line break — the twenty-second-wave line-split lesson), the VS-number must agree
# with the folder, the optional '(Family)' suffix must equal the workflows/README canonical family
# for that VS, and the '[Value Stream Index](../value-stream-index.md)' link is required.
rd = open(os.path.join(WF, "README.md"), encoding="utf-8").read()
fam_of = {}; curfam = None
for rl in rd.splitlines():
    fm = re.match(r"^### ([^()]+) \([\d,]+ workflows\)", rl)
    if fm:
        curfam = fm.group(1).strip(); continue
    rm = re.match(r"^\| \[(VS-\d+)\]\(VS-\d+-[a-z0-9-]+/README\.md\) \|", rl)
    if rm and curfam:
        fam_of[rm.group(1)] = curfam
if len(fam_of) != 188:
    bad += 1; print(f"BAD|workflows/README.md: family membership parsed for {len(fam_of)} VSs (expected 188)")
seen_quotes = 0
for vsdir in sorted(glob.glob(os.path.join(WF, "VS-*"))):
    vd = os.path.basename(vsdir)
    vsnum = "VS-" + vd.split("-")[1]
    for p in sorted(glob.glob(os.path.join(vsdir, "PA-*.md"))):
        rel = os.path.relpath(p, ROOT)
        lines = open(p, encoding="utf-8").read().splitlines()
        qblock = []; inq = False
        for ql in lines[:12]:
            if ql.startswith(">"):
                inq = True; qblock.append(ql[1:].strip())
            elif inq:
                break
        joined = " ".join(qblock)
        qm = re.search(r"Part of \*\*\[(VS-\d+):\s*([^]]+?)\]\(\./README\.md\)\*\*(?:\s*\(([^)]*)\))?", joined)
        if not qm:
            bad += 1; print(f"BAD|{rel}: header quote-line missing or malformed ('Part of **[VS-nn: <canonical VS-name>](./README.md)**')"); continue
        seen_quotes += 1
        if qm.group(1) != vsnum:
            bad += 1; print(f"BAD|{rel}: quote-line VS-number {qm.group(1)} disagrees with folder {vsnum}")
        elif qm.group(2).strip() != vs_canon.get(vd):
            bad += 1; print(f"BAD|{rel}: quote-line VS name {qm.group(2).strip()!r} != canonical {vs_canon.get(vd)!r}")
        if "[Value Stream Index](../value-stream-index.md)" not in joined:
            bad += 1; print(f"BAD|{rel}: quote-line missing the [Value Stream Index](../value-stream-index.md) link")
        suf = (qm.group(3) or "").strip()
        if suf and fam_of.get(vsnum) != suf:
            bad += 1; print(f"BAD|{rel}: quote-line family suffix ({suf}) != canonical family ({fam_of.get(vsnum)})")
if seen_quotes != 569:
    bad += 1; print(f"BAD|PA quote-lines found: {seen_quotes} (expected 569)")
# (d) twenty-eighth wave: the value-stream-index detailed-map '**[VS-nn: Name]**' bullets carry
# the VS-name — pinned to the same summary-row canon (slug + name; counts remain Check 68's).
seen_bullets = 0
for bm in re.finditer(r"^\*\*\[(VS-\d+):\s*([^]]+)\]\(\./([^)/]+)/README\.md\)\*\* \([\d,]+ workflows\)", idx, re.M):
    seen_bullets += 1
    bnum, bname, bslug = bm.group(1), bm.group(2).strip(), bm.group(3)
    if vs_canon.get(bslug) != bname:
        bad += 1; print(f"BAD|value-stream-index.md detailed map: {bnum} bullet VS name {bname!r} != canonical {vs_canon.get(bslug)!r}")
    if bnum != "VS-" + bslug.split("-")[1]:
        bad += 1; print(f"BAD|value-stream-index.md detailed map: {bnum} bullet links {bslug} (number disagrees)")
if seen_bullets != 188:
    bad += 1; print(f"BAD|value-stream-index.md detailed map: {seen_bullets} VS bullets (expected 188)")
print(f"TOTALS bad={bad}")
PY
)
C31_BAD=$(echo "$CHECK31" | sed -n 's/^TOTALS bad=\([0-9]*\)$/\1/p')
if [ "${C31_BAD:-1}" -eq 0 ]; then
    ok "All 569 process-area names agree 3-way (PA-file H1 == VS-README row == value-stream-index bullet, canonical = index), all 188 VS-README H1 titles carry the canonical index VS-name (H1 arm, twenty-seventh wave), all 569 PA header quote-lines carry the canonical VS-name over a line-break-proof joined read with VS-number, optional canonical family suffix and Value-Stream-Index link verified (quote-line arm, twenty-eighth wave), and all 188 detailed-map VS bullets carry the canonical summary-row name (bullet arm, twenty-eighth wave — fourteen drifted quote-lines across VS-48/100/114/130/192 and the VS-192 detailed bullet were found one layer out from the twenty-seventh wave's footer/H1 repairs)"
else
    error "PA/VS name drift found ($C31_BAD location(s)) — run 07-methodology/fix-pa-names.py (canonical source: value-stream-index.md):"
    echo "$CHECK31" | grep -E '^BAD\|' | sed 's/^BAD|/    /' | head -25 || true
fi

# --- Check 32: Dangling requirement-ID citations in workflow/PA and summary docs ---
echo "--- Check 32: Requirement-ID citation resolution (workflow catalog) ---"
CHECK32=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, glob, collections, sys
ROOT = os.path.join(sys.argv[1], "01-model-company")
# Canonical requirement IDs from erp-requirements.md table rows
defined = set()
for line in open(os.path.join(ROOT, "erp-requirements.md"), encoding="utf-8"):
    m = re.match(r"^\| ([A-Z]{2,5}-\d+[a-z]?) \|", line)
    if m:
        defined.add(m.group(1))
# Non-requirement tokens that match the ID shape: standards, laws, shift times,
# project codes, intra-file sub-step labels (NR-10/11), dependency-map row IDs (CIRC-xxx)
EXEMPT = {"ISPM-15", "EAN-13", "COVID-19", "DOLE-174", "ITF-14", "GTIN-13", "GTIN-14",
          "NR-10", "NR-11", "PM-10", "RG-59", "BRD-001", "PFRS-15"}
prefixes = ("VS-", "PA-", "CTL-", "CIRC-")
pat = re.compile(r"\b([A-Z]{2,5}-\d{2,3}[a-z]?)\b")
bad = collections.Counter()
where = collections.defaultdict(set)
files = [os.path.join(ROOT, "erp-requirements.md"), os.path.join(ROOT, "requirement-workflow-matrix.md")]
files = [f for f in files if os.path.exists(f)]
scan = set(glob.glob(os.path.join(ROOT, "workflows", "**", "*.md"), recursive=True)) - set(files)
# Review #23: also scan the surfaces outside the workflow catalog — the controls
# matrix (five shipped dangling citations of review #22-removed IDs lived in its
# Req Ref column) plus the summary/methodology docs and the root README.
scan |= {os.path.join(ROOT, f) for f in (
    "internal-controls-matrix.md", "model-company-profile.md", "executive-summary.md",
    "assumptions-and-design-decisions.md", "data-migration-mapping.md",
    "data-volumes-and-integrations.md", "mobile-app-strategy.md",
    "headcount-reality-check.md") if os.path.exists(os.path.join(ROOT, f))}
for extra in (os.path.join(sys.argv[1], "README.md"),
              os.path.join(sys.argv[1], "07-methodology", "technical-guidelines.md")):
    if os.path.exists(extra):
        scan.add(extra)
for f in sorted(scan):
    for m in pat.finditer(open(f, encoding="utf-8").read()):
        rid = m.group(1)
        if rid in defined or rid in EXEMPT or rid.startswith(prefixes):
            continue
        if re.fullmatch(r"W\d+[a-z]?", rid):
            continue
        bad[rid] += 1
        where[rid].add(os.path.relpath(f, ROOT))
for rid in sorted(bad):
    print(f"BAD|{rid} x{bad[rid]} in {sorted(where[rid])[:4]}")
print(f"TOTALS ids={len(bad)} refs={sum(bad.values())} defined={len(defined)}")
PY
)
C32_IDS=$(echo "$CHECK32" | sed -n 's/^TOTALS ids=\([0-9]*\) refs=.*/\1/p')
if [ "${C32_IDS:-1}" -eq 0 ]; then
    ok "All requirement-ID citations across the workflow catalog resolve to a defined erp-requirements.md row"
else
    error "Dangling requirement-ID citations found ($C32_IDS distinct ID(s)) — remap to the canonical requirement ID (see Check 4 for the matrix equivalent):"
    echo "$CHECK32" | grep -E '^BAD\|' | sed 's/^BAD|/    /' | head -25 || true
fi

# --- Check 33: Workflow-reference resolution inside PA bodies & VS READMEs ---
echo "--- Check 33: Workflow-reference resolution (PA bodies & VS READMEs) ---"
# Checks 6/7 validate W-references in the four cross-reference docs only; nothing
# previously verified the citations inside the 569 PA files themselves or the 188
# VS READMEs (review #20 found 19 dangling tokens there: zero-padded W01/W03/W05,
# a PA reference written in the W namespace (W03.4), phantom W413/W1593/W6796 and
# PA-file-slug citations W05.2). Every \bW\d{1,4}[A-Z]?\b token outside workflow
# headings must resolve to a '##'/'###' workflow header ID defined anywhere in the
# catalog (sub-step refs like W14.8 and sub-workflow refs like W13.9a reduce to their
# base id W14/W13 by the \b boundary).
CHECK33=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, glob, collections, sys
ROOT = os.path.join(sys.argv[1], "01-model-company")
defined = set()
pa_files = []
for f in glob.glob(os.path.join(ROOT, "workflows", "VS-*", "PA-*.md")):
    pa_files.append(f)
    for line in open(f, encoding="utf-8"):
        m = re.match(r"^#{2,3} (W\d+[A-Z]?)\.", line)
        if m:
            defined.add(m.group(1))
bad = collections.Counter()
where = collections.defaultdict(set)
scan = set(glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True))
for f in sorted(scan):
    for i, line in enumerate(open(f, encoding="utf-8"), 1):
        if re.match(r"^#{2,3} W\d", line):
            continue
        for m in re.finditer(r"\b(W\d{1,4}[A-Z]?)\b", line):
            w = m.group(1)
            if w not in defined:
                bad[w] += 1
                where[w].add(os.path.relpath(f, ROOT) + f":{i}")
for w in sorted(bad):
    print(f"BAD|{w} x{bad[w]} e.g. {sorted(where[w])[:3]}")
print(f"TOTALS ids={len(bad)} refs={sum(bad.values())} defined={len(defined)}")
PY
)
C33_IDS=$(echo "$CHECK33" | sed -n 's/^TOTALS ids=\([0-9]*\) refs=.*/\1/p')
if [ "${C33_IDS:-1}" -eq 0 ]; then
    ok "All workflow-ID citations across the model-company docs (PA bodies, VS READMEs, summary docs) resolve to a defined workflow header"
else
    error "Dangling workflow-ID citations found ($C33_IDS distinct ID(s)) — remap to the canonical workflow/VS id (see fix-pa-wrefs.py for the review #20 precedent):"
    echo "$CHECK33" | grep -E '^BAD\|' | sed 's/^BAD|/    /' | head -25 || true
fi

# --- Check 34: CTL-240–808 PA-control objective names match canonical PA names ---
echo "--- Check 34: PA-control objective canonical-name agreement ---"
# add-pa-controls.py derived objective names from PA file slugs (mangling proper nouns:
# S&OP->Sandop, DENR->Denr, ERP->Erp, DC->Dc, B2B->B2b) and backfill-controls.py
# truncated them to 90 chars mid-word; fix-ctl-pa-names.py (review #20) canonicalized
# both surfaces to the value-stream-index bullet names. This guard verifies:
#   (a) every matrix row 'Ensure controlled execution — <name> (PA-XX.Y)' carries the
#       canonical index name of its PA;
#   (b) every PA-body 'CTL-NNN (ensure controlled execution — ...)' parenthetical is
#       the exact canonical rendering of its register row.
CHECK34=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, glob, collections, sys
ROOT = os.path.join(sys.argv[1], "01-model-company")
canon = {}
for m in re.finditer(r"- \*\*(PA-\d{2,3}\.\d)\*\* \[([^\]]+)\]\(",
                     open(os.path.join(ROOT, "workflows", "value-stream-index.md"), encoding="utf-8").read()):
    canon[m.group(1)] = m.group(2)
row = re.compile(r"^\| (CTL-\d{3}) \| Ensure controlled execution — (.+?) \((PA-\d{2,3}\.\d)\) \|")
ctl2pa = {}
rows = 0
bad_matrix = []
for line in open(os.path.join(ROOT, "internal-controls-matrix.md"), encoding="utf-8"):
    m = row.match(line.rstrip("\n"))
    if not m:
        continue
    rows += 1
    ctl2pa[m.group(1)] = m.group(3)
    if m.group(2) != canon.get(m.group(3)):
        bad_matrix.append(f"{m.group(1)}: '{m.group(2)}' != canonical '{canon.get(m.group(3))}' (PA {m.group(3)})")
bad_body = collections.Counter()
where = collections.defaultdict(list)
bpat = re.compile(r"(CTL-\d{3}) \(ensure controlled execution — .*?\.\)")
for f in glob.glob(os.path.join(ROOT, "workflows", "VS-*", "PA-*.md")):
    text = open(f, encoding="utf-8").read()
    for m in bpat.finditer(text):
        ctl = m.group(1)
        pa = ctl2pa.get(ctl)
        want = f"{ctl} (ensure controlled execution — {canon[pa]} ({pa}).)" if pa else None
        if m.group(0) != want:
            key = f"{ctl}: '{m.group(0)[:70]}...' != canonical" if pa else f"{ctl}: not a register PA-control row"
            bad_body[key] += 1
            where[key].append(os.path.relpath(f, ROOT))
for k in sorted(bad_matrix):
    print(f"BAD-MATRIX|{k}")
for k in sorted(bad_body):
    print(f"BAD-BODY|{k} x{bad_body[k]} e.g. {where[k][0]}")
print(f"TOTALS matrix_rows={rows} matrix_bad={len(bad_matrix)} body_bad={sum(bad_body.values())} pa_controls={len(ctl2pa)}")
PY
)
C34_BAD=$(echo "$CHECK34" | sed -n 's/^TOTALS matrix_rows=[0-9]* matrix_bad=\([0-9]*\) body_bad=\([0-9]*\).*/\1 \2/p')
C34_MBAD=$(echo "$C34_BAD" | cut -d' ' -f1)
C34_BBAD=$(echo "$C34_BAD" | cut -d' ' -f2)
if [ "${C34_MBAD:-1}" -eq 0 ] && [ "${C34_BBAD:-1}" -eq 0 ]; then
    ok "All 569 PA-control objectives (matrix + PA-body parentheticals) carry their canonical process-area name from value-stream-index.md"
else
    error "PA-control objective-name drift (matrix: $C34_MBAD, PA bodies: $C34_BBAD) — re-run 07-methodology/fix-ctl-pa-names.py:"
    echo "$CHECK34" | grep -E '^BAD-' | sed 's/^BAD-MATRIX|/    /; s/^BAD-BODY|/    /' | head -25 || true
fi

# --- Check 35: VS-number citation resolution (catalog & summary docs) ---
echo "--- Check 35: Value-stream-number citation resolution ---"
# Checks 19/20 resolve link TARGETS and Checks 6/7/33 validate W… tokens, but nothing
# validated the VS… namespace itself. Consistency review #21 found 87 citations across
# 25 PA files of the form "(links to VS-469 DTI)" where 469 is not a value stream at
# all — it is workflow W469's number (Customer Complaint DTI Escalation), i.e. a
# workflow reference written in the VS namespace. Every phantom number matched an
# existing workflow whose title matched the surrounding gloss (VS-228→W228 sales
# commissions, VS-245→W245 vendor chargebacks, VS-289→W289 pricing master,
# VS-399→W399 asset register, VS-4398→W4398 wayfinding, …); all repaired by the new
# 07-methodology/fix-vs-wrefs.py. This check enforces the invariant that fixed:
# every `VS-<n>` token in every current-state doc must denote an ACTIVE value stream
# (or be a `VS-NN.M` process-area reference, or one of the two sanctioned retired-
# number forms — the 'VS-49–VS-52' range phrase and the 'former VS-49/VS-52' gap
# notes; CHANGELOG/workflow-gap-analysis are exempt as labelled historical records).
CHECK35=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, glob, collections, sys
ROOT = sys.argv[1]
WF = os.path.join(ROOT, "01-model-company", "workflows")
active = {int(re.match(r"VS-(\d+)-", d).group(1))
          for d in os.listdir(WF) if re.match(r"VS-\d+-", d)
          and os.path.isdir(os.path.join(WF, d))}
SKIP = {"CHANGELOG.md", "workflow-gap-analysis.md"}
bad = collections.Counter()
where = collections.defaultdict(list)
for dirpath, _d, files in os.walk(ROOT):
    if os.sep + ".git" in dirpath or "__pycache__" in dirpath: continue
    for fn in sorted(files):
        if not fn.endswith(".md") or fn in SKIP: continue
        path = os.path.join(dirpath, fn)
        rel = os.path.relpath(path, ROOT)
        txt = open(path, encoding="utf-8", errors="replace").read()
        txt = re.sub(r"`[^`]*`", "", txt)  # inline-code spans are illustrative examples, not citations
        for m in re.finditer(r"\bVS-(\d{1,4})\b(?!\.\d)", txt):
            n = int(m.group(1))
            if n in active: continue
            ctx = txt[max(0, m.start() - 24):m.end() + 24]
            if re.search(r"VS-49\s*[\u2013\u2014-]+\s*(VS-)?52", ctx): continue  # retirement range-note
            if re.search(r"former\s+VS-(?:49|52)\b", ctx): continue             # 'filled the former VS-n gap' note
            bad[f"VS-{n}"] += 1
            where[f"VS-{n}"].append(f"{rel}:{txt.count(chr(10), 0, m.start()) + 1}")
print(f"TOTALS ids={len(bad)} refs={sum(bad.values())}")
for k in sorted(bad, key=lambda x: int(x[3:])):
    print(f"BAD|{k} x{bad[k]} e.g. {sorted(where[k])[:3]}")
PY
)
C35_IDS=$(echo "$CHECK35" | sed -n 's/^TOTALS ids=\([0-9]*\) refs=.*/\1/p')
if [ "${C35_IDS:-1}" -eq 0 ]; then
    ok "All VS-number citations across the model-company docs resolve to an active value stream (no workflow references written in the VS namespace)"
else
    error "Dangling/misnamespaced VS-number citations found ($C35_IDS distinct id(s)) — remap to the canonical workflow id (see fix-vs-wrefs.py for the review #21 precedent):"
    echo "$CHECK35" | grep -E '^BAD\|' | sed 's/^BAD|/    /' | head -25 || true
fi

# --- Check 36: duplicate requirement titles in erp-requirements.md ---
echo "--- Check 36: Duplicate requirement titles (erp-requirements.md register) ---"
# Consistency review #22 (2026-08-24) found five exact-duplicate requirement rows no prior
# check saw: Checks 4/28/32 validate requirement ID *tokens* and TOC claims, but never the
# titles. PUR-015 duplicated FIN-019 (same title, same primary workflow W27), WSL-002
# duplicated CRM-012 + CRM-013 (W103; its extra scope is CRM-013), and WMS-009–011
# duplicated WHL-001–003 (same titles, same primary workflows W584/W585/W586). Two IDs for
# one capability is an ambiguity defect: any consumer citing the capability cannot tell
# which ID is canonical, and the duplicate rows drifted independently (priorities differed:
# WHL-001 S vs WMS-009 M, WMS-011 S vs WHL-003 M). All five rows were removed (total
# 733 -> 728; see erp-requirements.md v24.0 note); this check enforces title uniqueness so
# a future authoring round cannot re-register an existing capability under a new prefix.
CHECK36=$(python3 - "$REPO_ROOT" <<'PY'
import collections, re, sys
path = sys.argv[1] + "/01-model-company/erp-requirements.md"
titles = collections.defaultdict(list)
for line in open(path, encoding="utf-8"):
    m = re.match(r"^\| ([A-Z]{2,5}-\d+[ab]?) \| (.+?) \|", line)
    if m:
        titles[m.group(2).strip().lower()].append(m.group(1))
dups = {t: ids for t, ids in titles.items() if len(ids) > 1}
n = sum(len(v) for v in dups.values())
for t, ids in sorted(dups.items()):
    print(f"DUP|{' / '.join(sorted(ids))}: {t}")
print(f"TOTALS dup_titles={len(dups)} dup_rows={n}")
PY
)
C36_DUPS=$(echo "$CHECK36" | sed -n 's/^TOTALS dup_titles=\([0-9]*\) dup_rows=[0-9]*/\1/p')
if [ "${C36_DUPS:-1}" -eq 0 ]; then
    ok "All 728 erp-requirements.md requirement titles are unique across all 38 prefix categories (no capability registered twice under different IDs)"
else
    error "Duplicate requirement titles found ($C36_DUPS distinct title(s)) — merge into one canonical row and remap citations (see erp-requirements.md v24.0 note for the review #22 precedent):"
    echo "$CHECK36" | grep -E '^DUP\|' | sed 's/^DUP|/    /'
fi

# --- Check 37: Requirement priority-split figures vs the erp-requirements.md register ---
echo "--- Check 37: Priority-split figure agreement ---"
# Review #22 removed five requirement rows (733 -> 728; 429 Must / 293 Should / 6 Nice)
# but two prose surfaces kept quoting the pre-removal split (431/296): the classification
# doc's Classification Rules intro and the root-README Key Metrics table. No prior check
# compared quoted priority counts against the register itself, so this check derives the
# canonical split from the register rows and validates every quoted figure against it.
CHECK37=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, glob, sys
ROOT = sys.argv[1]
counts = {"Must Have": 0, "Should Have": 0, "Nice to Have": 0}
for line in open(os.path.join(ROOT, "01-model-company", "erp-requirements.md"), encoding="utf-8"):
    m = re.match(r"^\| [A-Z]{2,5}-\d+[ab]? \| .+? \| (Must Have|Should Have|Nice to Have) \|", line)
    if m:
        counts[m.group(1)] += 1
derived = (counts["Must Have"], counts["Should Have"], counts["Nice to Have"])
bad = []
def note(where, label, got):
    if tuple(got) != derived:
        bad.append(f"{where}: {label} figures {tuple(got)} != register {derived}")
def ints(m):
    return tuple(int(x.replace(",", "")) for x in m.groups())
tiers = ("Must Have", "Should Have", "Nice to Have")
# Surface 1: classification doc 'Classification Rules' '**X requirements** (N)' claims
text = open(os.path.join(ROOT, "01-model-company/workflows/workflow-criticality-classification.md"), encoding="utf-8").read()
got = []
for tier in tiers:
    m = re.search(r"\*\*" + tier + r" requirements\*\* \(([\d,]+)\)", text)
    got.append(int(m.group(1).replace(",", "")) if m else -1)
note("workflow-criticality-classification.md Classification Rules", "priority-split", got)
# Surface 2: root-README Key Metrics '| X Requirements | N |' rows
text = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
got = []
for tier in tiers:
    m = re.search(r"\| " + tier + r" Requirements \| ([\d,]+) \|", text)
    got.append(int(m.group(1).replace(",", "")) if m else -1)
note("root README Key Metrics", "priority-split", got)
# Surface 3: repo-wide 'A Must / B Should / C Nice' numeric triples (historical records excluded)
for f in glob.glob(ROOT + "/**/*.md", recursive=True):
    rel = os.path.relpath(f, ROOT)
    if rel.startswith("CHANGELOG") or "workflow-gap-analysis" in rel:
        continue
    for m in re.finditer(r"\b(\d[\d,]*) Must[^.\n]*?\b(\d[\d,]*) Should[^.\n]*?\b(\d[\d,]*) Nice\b", open(f, encoding="utf-8").read()):
        trip = ints(m)
        if trip != derived:
            note(rel, "'N Must / M Should / K Nice'", trip)
print(f"TOTALS derived={derived} mismatches={len(bad)}")
for b in bad:
    print("BAD|" + b)
PY
)
C37_BAD=$(echo "$CHECK37" | sed -n 's/^TOTALS derived=.* mismatches=\([0-9]*\)/\1/p')
if [ "${C37_BAD:-1}" -eq 0 ]; then
    ok "All quoted requirement priority-split figures match the erp-requirements.md register (429 Must / 293 Should / 6 Nice)"
else
    error "Quoted priority-split figures disagree with the erp-requirements.md register (see BAD lines for derived counts):"
    echo "$CHECK37" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 38: Requirements-TOC count-column agreement vs the register rows ---
echo "--- Check 38: Requirements-TOC count-column agreement ---"
# Review #22 updated R3 (45 -> 44) and R16 (8 -> 7) in the erp-requirements.md TOC
# when it removed five duplicate rows, but missed R4: retiring WMS-009–011 shrank
# R4's defined complement 26 -> 23 while its Count cell stayed at 26, so the Count
# column summed to 731 against the doc's own 'Total: 728' line. No prior check
# compared the TOC's per-section Counts against the register rows themselves.
CHECK38=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, sys
ROOT = sys.argv[1]
path = os.path.join(ROOT, "01-model-company", "erp-requirements.md")
lines = open(path, encoding="utf-8").read().splitlines()
# actual defined rows per prefix
cnt = {}
for line in lines:
    m = re.match(r"^\| ([A-Z]{2,5}-\d+[a-z]?) \|", line)
    if m:
        pre = m.group(1).split("-")[0]
        cnt[pre] = cnt.get(pre, 0) + 1
bad = []
sum_counts = 0
for line in lines:
    if not line.startswith("| [R") and not line.startswith("| — | Additional"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 4 or not cells[3].isdigit():
        continue
    claimed = int(cells[3])
    sum_counts += claimed
    # prefixes from the Req IDs cell (skip cells without ID tokens, e.g. 'Various')
    prefixes = sorted({t.split("-")[0] for t in re.findall(r"\b[A-Z]{2,5}-\d+", cells[2])})
    if not prefixes:
        continue
    actual = sum(cnt.get(p, 0) for p in prefixes)
    if actual != claimed:
        bad.append(f"{cells[1]} ({', '.join(prefixes)}): Count {claimed} != {actual} defined rows")
# Total line vs actual register size vs Count-column sum
mtot = re.search(r"\*\*Total: ([\d,]+) unique requirements\*\*", "\n".join(lines))
total_line = int(mtot.group(1).replace(",", "")) if mtot else -1
if total_line != len([k for k in cnt for _ in range(cnt[k])]):
    bad.append(f"Total line {total_line} != {sum(cnt.values())} defined register rows")
if sum_counts != total_line:
    bad.append(f"Count column sums to {sum_counts} != Total-line figure {total_line}")
print(f"TOTALS total_line={total_line} defined={sum(cnt.values())} count_col_sum={sum_counts} mismatches={len(bad)}")
for b in bad:
    print("BAD|" + b)
PY
)
C38_BAD=$(echo "$CHECK38" | sed -n 's/^TOTALS .* mismatches=\([0-9]*\)/\1/p')
if [ "${C38_BAD:-1}" -eq 0 ]; then
    ok "erp-requirements.md TOC Count column agrees with the register (per-row and 728-total)"
else
    error "Requirements-TOC Count column disagrees with the erp-requirements.md register:"
    echo "$CHECK38" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 39: Namespace & listing integrity (dup W headers, VS listings, CTL/PA citations, cross-file anchors) ---
echo "--- Check 39: Namespace & listing integrity ---"
# Regression guards for invariants verified manually in reviews #22/#23 but never
# codified: unique workflow headers across PA files (the 5,372-header / 5,349-unique
# register complement); repo-wide CTL-ID and PA-N.N citation resolution; cross-file
# markdown anchor links resolving to a heading. (VS READMEs aggregate workflows by
# process-area count rather than enumerating W-numbers — that count agreement is
# already guarded by Checks 2, 24 and 31.)
CHECK39=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, glob, collections, sys
ROOT = os.path.join(sys.argv[1], "01-model-company")
bad = []
# A. duplicate W headers across PA files
wdef = collections.Counter(); where = {}
hdr = re.compile(r"^#{2,4} (W\d+[A-Za-z]?)[\.\s]")
for f in glob.glob(os.path.join(ROOT, "workflows", "**", "PA-*.md"), recursive=True):
    for line in open(f, encoding="utf-8"):
        m = hdr.match(line)
        if m:
            wdef[m.group(1)] += 1; where.setdefault(m.group(1), f)
dups = {k: v for k, v in wdef.items() if v > 1}
if dups:
    bad.append(f"duplicate workflow headers: {dict(list(dups.items())[:5])}")
# B. CTL-ID citation resolution repo-wide
ctl = set()
for line in open(os.path.join(ROOT, "internal-controls-matrix.md"), encoding="utf-8"):
    m = re.match(r"^\| (CTL-\d+) \|", line)
    if m: ctl.add(m.group(1))
scan = glob.glob(ROOT + "/**/*.md", recursive=True) + [
    os.path.join(sys.argv[1], "README.md"),
    os.path.join(sys.argv[1], "07-methodology", "technical-guidelines.md")]
dang_ctl, dang_pa = [], []
padef = {re.match(r"(PA-\d+\.\d+)-", os.path.basename(f)).group(1)
         for f in glob.glob(os.path.join(ROOT, "workflows", "**", "*.md"), recursive=True)
         if re.match(r"(PA-\d+\.\d+)-", os.path.basename(f))}
for f in scan:
    txt = re.sub(r"```.*?```", "", open(f, encoding="utf-8").read(), flags=re.S)
    rel = os.path.relpath(f, ROOT)
    for m in re.finditer(r"\b(CTL-\d+)\b", txt):
        if m.group(1) not in ctl: dang_ctl.append(f"{rel}:{m.group(1)}")
    for m in re.finditer(r"\b(PA-\d+\.\d+)\b", txt):
        if m.group(1) not in padef: dang_pa.append(f"{rel}:{m.group(1)}")
if dang_ctl:
    bad.append(f"dangling CTL citations: {sorted(set(dang_ctl))[:5]} ({len(dang_ctl)} refs)")
if dang_pa:
    bad.append(f"dangling PA-number citations: {sorted(set(dang_pa))[:5]} ({len(dang_pa)} refs)")
# D. cross-file markdown anchor resolution
def slug(h):
    s = h.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s+", "-", s)
broke = 0; broke_ex = []
for f in glob.glob(sys.argv[1] + "/**/*.md", recursive=True):
    if os.sep + ".git" + os.sep in f: continue
    base = os.path.dirname(f)
    txt = re.sub(r"```.*?```", "", open(f, encoding="utf-8").read(), flags=re.S)
    for m in re.finditer(r"\]\(([^)#\s]+\.md)(#[^)\s]+)?\)", txt):
        tp = os.path.normpath(os.path.join(base, m.group(1)))
        if not os.path.exists(tp) or not m.group(2):
            continue
        heads = set()
        for line in open(tp, encoding="utf-8"):
            hm = re.match(r"^#+\s+(.*)", line)
            if hm: heads.add(slug(hm.group(1)))
            em = re.search(r'<a name="([^"]+)"', line)
            if em: heads.add(em.group(1).lower())
        if m.group(2)[1:].lower() not in heads:
            broke += 1
            if len(broke_ex) < 5:
                broke_ex.append(f"{os.path.relpath(f, ROOT)} -> {m.group(1)}{m.group(2)}")
if broke:
    bad.append(f"broken cross-file anchors: {broke} (e.g. {'; '.join(broke_ex)})")
print(f"TOTALS headers={len(wdef)} problems={len(bad)}")
for b in bad:
    print("BAD|" + b)
PY
)
# Part E (2026-09-10 eighteenth consistency review): the misdirected-CTL guard —
# audit-misdirected-ctl.py --guard. The paste-family class (one foreign core control
# pasted into every workflow block of a file with fabricated glosses) was re-mapped in
# batches 26/27; the residual isolated colon-form population was hand-adjudicated
# citation-by-citation at batch 13 as deliberate cross-references (verbatim-objective
# restatements / definition-matched paraphrases). The guard re-derives the census every
# run: zero paren-form citations naming a different PA (the unambiguous wrong-PA defect
# class), and the adjudicated colon-form population — total 170 with per-PA and
# per-cited-CTL distributions — unchanged, so any new paste, re-map or deletion forces a
# conscious re-adjudication with the baseline re-pointed (the Check-74 deferred-anchor
# pattern). The script itself had also been unrunnable outside its original author's
# machine since authoring (a hardcoded /home/riddler absolute path) — the eighteenth
# wave re-pointed it and its nine sibling tools to repo-relative resolution, which is how
# the guard could be armed at all.
C39_GUARD_OUT=$(python3 "$REPO_ROOT/07-methodology/audit-misdirected-ctl.py" --guard 2>&1) && C39_GUARD_RC=0 || C39_GUARD_RC=$?
C39_BAD=$(echo "$CHECK39" | sed -n 's/^TOTALS .* problems=\([0-9]*\)/\1/p')
if [ "${C39_BAD:-1}" -eq 0 ] && [ "$C39_GUARD_RC" -eq 0 ]; then
    C39_HDRS=$(echo "$CHECK39" | sed -n 's/^TOTALS headers=\([0-9]*\) .*/\1/p')
    ok "Namespace integrity: ${C39_HDRS} workflow headers unique; all CTL & PA-N.N citations resolve; all cross-file anchors resolve; misdirected-CTL guard clean (0 wrong-PA paren citations; batch-13-adjudicated 170-citation colon-form census exact per-PA and per-CTL — guard mode of audit-misdirected-ctl.py, armed by the 2026-09-10 eighteenth-wave review after the script was found unrunnable outside its original author's machine via a hardcoded absolute path, ten shipped tools re-pointed to repo-relative resolution; fix-ghost-titles-batch14 and fix-ghost-roles-batch26 additionally sunset-guarded after sandbox runs showed both would rewrite frozen/official records their aged-out rules still match)"
else
    error "Namespace/listing integrity violations found:"
    echo "$CHECK39" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
    if [ "$C39_GUARD_RC" -ne 0 ]; then
        echo "$C39_GUARD_OUT" | sed 's/^/    /'
    fi
fi

# --- Check 40: Validator self-description agreement (quoted check counts vs implemented checks) ---
echo "--- Check 40: Validator self-description agreement ---"
# Reviews #22–#24 grew the validator from 35 to 39 checks, but both canonical
# self-descriptions (the root-README folder-tree line and the 07-methodology
# README contents-table row) still said "35 checks". No prior check compared
# quoted check counts against the implemented checks, so every future check
# addition would silently strand the same two surfaces (exactly what happened
# between reviews #21 and #24). This check counts the '--- Check N:' markers
# in validate-repo.sh and validates every quoted check-count figure against it.
# Per-version history notes (footer '*Date: ...' lines carrying frozen
# 'across N checks' status records) and CHANGELOG/gap-analysis are exempt.
IMPLEMENTED_CHECKS=$(grep -c '^# --- Check ' "$REPO_ROOT/07-methodology/validate-repo.sh")
CHECK40=$(python3 - "$REPO_ROOT" "$IMPLEMENTED_CHECKS" <<'PY'
import re, os, glob, sys
ROOT, IMPL = sys.argv[1], int(sys.argv[2])
bad = []
forms = [re.compile(r"\((\d+) checks\)"),
         re.compile(r"\u2014 (\d+) checks covering"),
         re.compile(r"across (\d+) checks")]
for f in glob.glob(ROOT + "/**/*.md", recursive=True):
    rel = os.path.relpath(f, ROOT)
    if rel.startswith("CHANGELOG") or "workflow-gap-analysis" in rel:
        continue
    for i, line in enumerate(open(f, encoding="utf-8"), 1):
        if line.lstrip().startswith("*Date:") or "Prior v" in line:
            continue  # frozen per-version history notes
        # (a former '\u2192' line exemption was removed in review #30: it silently
        # exempted the 07-methodology README's own contents-table row — which quotes
        # an arrow inside its Check-46 description — letting that row drift to a
        # stale count; dated footers above are the only legitimate arrow carriers)
        for pat in forms:
            for m in pat.finditer(line):
                if int(m.group(1)) != IMPL:
                    bad.append(f"{rel}:{i}: '{m.group(0)}' != {IMPL} implemented checks")
print(f"TOTALS implemented={IMPL} mismatches={len(bad)}")
for b in bad:
    print("BAD|" + b)
PY
)
C40_BAD=$(echo "$CHECK40" | sed -n 's/^TOTALS .* mismatches=\([0-9]*\)/\1/p')
if [ "${C40_BAD:-1}" -eq 0 ]; then
    ok "All quoted validator check counts equal the ${IMPLEMENTED_CHECKS} checks implemented in validate-repo.sh"
else
    error "Quoted validator check counts disagree with the ${IMPLEMENTED_CHECKS} checks implemented in validate-repo.sh:"
    echo "$CHECK40" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 41: Quoted requirement-total & category-count figures vs the register ---
echo "--- Check 41: Requirement-total figure agreement ---"
# Review #22 shrank the register 733 -> 728, but the executive-summary footer's
# 'updated counts: 733 requirements' headline (written 2026-06-25, before the
# removal) kept quoting the pre-removal total. Check 37 guards only the
# priority split and Check 38 only the erp-requirements.md TOC; neither
# compares quoted *totals* (or 'across N categories' claims) against the
# register. This check derives both figures from the register rows and
# validates the total-claim surfaces: 'N requirements across', 'N unique
# requirements', 'Total requirements: N', 'updated counts: N requirements',
# the root-README Key Metrics '| Requirements | N |' row, and the anchored
# 'requirements across N categor…' category-count claims (anchored to the
# word 'requirements' so workflow-body phrases like 'across 13 categories'
# for product/vendor categories are not flagged). Historical records
# (CHANGELOG, gap-analysis, 'Prior v' notes, 'X → Y' transitions) are exempt.
CHECK41=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, glob, sys
ROOT = sys.argv[1]
req = {}
for line in open(os.path.join(ROOT, "01-model-company", "erp-requirements.md"), encoding="utf-8"):
    m = re.match(r"^\| ([A-Z]{2,5}-\d+[a-z]?) \|", line)
    if m:
        pre = m.group(1).split("-")[0]
        req[pre] = req.get(pre, 0) + 1
TOTAL, CATS = sum(req.values()), len(req)
bad = []
total_forms = [re.compile(r"\b([\d,]+)\s+requirements\s+across"),
               re.compile(r"\b([\d,]+)\s+unique\s+requirements"),
               re.compile(r"Total requirements\*?\*?:?\s*\**([\d,]+)"),
               re.compile(r"updated counts:\s*([\d,]+)\s+requirements"),
               re.compile(r"\| Requirements \| \**([\d,]+)\** \|")]
cat_forms = [re.compile(r"requirements\s+across\s+(\d+)\s+(?:distinct requirement-ID prefixes|prefix categor|categor)"),
             re.compile(r"\| Requirements \| \**[\d,]+\**\s+across\s+(\d+)\s+categor")]
for f in glob.glob(ROOT + "/**/*.md", recursive=True):
    rel = os.path.relpath(f, ROOT)
    if rel.startswith("CHANGELOG") or "workflow-gap-analysis" in rel:
        continue
    for i, line in enumerate(open(f, encoding="utf-8"), 1):
        if "Prior v" in line or "\u2192" in line:
            continue  # frozen version-history notes and 'X -> Y' transitions
        for pat in total_forms:
            for m in pat.finditer(line):
                if int(m.group(1).replace(",", "")) != TOTAL:
                    bad.append(f"{rel}:{i}: total-claim '{m.group(0)}' != register {TOTAL}")
        for pat in cat_forms:
            for m in pat.finditer(line):
                if int(m.group(1)) != CATS:
                    bad.append(f"{rel}:{i}: category-claim '{m.group(0)}' != register {CATS} prefixes")
print(f"TOTALS register={TOTAL} prefixes={CATS} mismatches={len(bad)}")
for b in bad:
    print("BAD|" + b)
PY
)
C41_BAD=$(echo "$CHECK41" | sed -n 's/^TOTALS .* mismatches=\([0-9]*\)/\1/p')
if [ "${C41_BAD:-1}" -eq 0 ]; then
    C41_T=$(echo "$CHECK41" | sed -n 's/^TOTALS register=\([0-9]*\) .*/\1/p')
    C41_C=$(echo "$CHECK41" | sed -n 's/^TOTALS .* prefixes=\([0-9]*\) .*/\1/p')
    ok "All quoted requirement-total and category-count figures match the erp-requirements.md register (${C41_T} requirements across ${C41_C} prefixes)"
else
    error "Quoted requirement-total/category-count figures disagree with the erp-requirements.md register:"
    echo "$CHECK41" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 42: Duplicate workflow titles (normalized) across the workflow catalog ---
echo "--- Check 42: Duplicate workflow-title guard ---"
# Consistency review #26 found same-title duplicate clusters no ID-based check could
# see: W1396/W1543 (identical titles, both VS-25 — a true duplicate authored in
# different passes), W1185/W1286/W1311 alongside canonical W510 (four same-scope
# review workflows in one PA with conflicting review volumes), and the cross-VS
# twins W1638/W176 and W1731/W2582 (conflicting cadence/agreement counts). Check 36
# guards requirement titles; nothing guarded workflow titles. Titles are normalized
# (case/punctuation-insensitive, so 'Store-to-DC Reverse Logistics (Consolidation)'
# equals 'Store-to-DC Reverse Logistics Consolidation') and grouped by normalized
# text; three ID groups are adjudicated intentional parallel program templates
# (same function, different asset domain) and sit on the allowlist below.
CHECK42=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, glob, collections, sys
ROOT = os.path.join(sys.argv[1], "01-model-company", "workflows")
# Adjudicated intentional parallel program templates (see check header):
ALLOWED = [frozenset(x) for x in (("W4776", "W4800"), ("W4786", "W4810"),
                                   ("W4888", "W4912", "W4936"))]
def norm(t):
    return " ".join(re.sub(r"[^a-z0-9]+", " ", t.lower()).split())
titles = collections.defaultdict(list)
for f in glob.glob(os.path.join(ROOT, "VS-*", "PA-*.md")):
    for line in open(f, encoding="utf-8"):
        m = re.match(r"^## (W\d+[A-Z]?)\. (.+)$", line.strip())
        if m:
            titles[norm(m.group(2))].append(m.group(1))
bad = 0
total = 0
for t, ids in sorted(titles.items()):
    total += len(ids)
    if len(ids) < 2:
        continue
    s = frozenset(ids)
    if any(a == s for a in ALLOWED):
        continue
    bad += 1
    print(f"BAD|{', '.join(sorted(ids))}: '{t[:80]}'")
print(f"TOTALS workflows={total} dup_groups={bad}")
PY
)
C42_BAD=$(echo "$CHECK42" | sed -n 's/^TOTALS workflows=[0-9]* dup_groups=\([0-9]*\)/\1/p')
C42_TOTAL=$(echo "$CHECK42" | sed -n 's/^TOTALS workflows=\([0-9]*\) dup_groups=[0-9]*/\1/p')
if [ "${C42_BAD:-1}" -eq 0 ]; then
    ok "All ${C42_TOTAL} workflow titles are unique after normalization (3 adjudicated parallel program-template groups allowlisted)"
else
    error "Duplicate workflow titles found (same normalized title on 2+ IDs) — designate a canonical workflow, retitle companions to their genuine slice, or add an adjudicated allowlist entry:"
    echo "$CHECK42" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 43: Analysis-section list hygiene, paren balance & bold balance ---
echo "--- Check 43: Controls-section list hygiene + bold/paren balance ---"
# Consistency review #27 found a rendering-defect cluster every prior check was blind to
# (they validate counts/IDs/anchors/tables — not list hygiene inside analysis sections):
# 3,349 Controls sections carried a dangling non-bulleted 'operational:' line (the
# add-automation-controls.py generator emitted CTL items bulleted but operational items
# bare, so markdown rendered the operational controls outside the list), 78 Controls
# lines had unbalanced parentheses (the generator's pain-point regex truncated captures
# at 'e.g.'/'vs.'/'No.' periods and swallowed ')' at '; operational:' joins), and 25
# paragraph blocks carried broken '**' bold markers (labels closed with a stray '"' or
# stray '**' leaked from Pain Points into Controls). This check guards all three:
#   A. every content line in a '### Controls' section is a bullet or indented continuation
#   B. Controls bullets have balanced parens and no '**' artifacts
#   C. every paragraph block in the model-company docs has an even '**' count
#      (code spans stripped first, so glob patterns like `workflows/**/*.md` are exempt)
# Companion repairer: 07-methodology/fix-controls-bullets.py
CHECK43=$(python3 - "$REPO_ROOT" <<'PY'
import glob, os, re, sys
ROOT = sys.argv[1]
bad = 0
# A + B: Controls-section hygiene across PA files
for f in glob.glob(os.path.join(ROOT, "01-model-company", "workflows", "VS-*", "PA-*.md")):
    rel = os.path.relpath(f, ROOT)
    in_c = False
    for i, line in enumerate(open(f, encoding="utf-8"), 1):
        s = line.rstrip("\n")
        if s == "### Controls":
            in_c = True
            continue
        if in_c and (s.startswith("#") or s.startswith("---") or s.strip() == ""):
            in_c = False
            continue
        if not in_c:
            continue
        if not s.startswith("- ") and not re.match(r"^  \S", s):
            bad += 1
            print(f"BAD|{rel}:{i}: non-bulleted Controls line: '{s[:80]}'")
        elif s.count("(") != s.count(")"):
            bad += 1
            print(f"BAD|{rel}:{i}: unbalanced parens: '{s[:80]}'")
        elif "**" in s:
            bad += 1
            print(f"BAD|{rel}:{i}: stray '**' in Controls bullet: '{s[:80]}'")
# C: bold balance per paragraph block, model-company docs + root README
files = glob.glob(os.path.join(ROOT, "01-model-company", "**", "*.md"), recursive=True)
files.append(os.path.join(ROOT, "README.md"))
for f in files:
    rel = os.path.relpath(f, ROOT)
    lines = open(f, encoding="utf-8").readlines()
    i = 0
    while i < len(lines):
        if "**" not in lines[i]:
            i += 1
            continue
        start = i
        while start > 0 and lines[start - 1].strip() and not lines[start - 1].lstrip().startswith(("#", "|", "---")):
            start -= 1
        end = i
        while end + 1 < len(lines) and lines[end + 1].strip() and not lines[end + 1].lstrip().startswith(("#", "|", "---")):
            end += 1
        block = "".join(lines[start:end + 1])
        block = re.sub(r"`[^`]*`", "", block)  # code spans may hold glob '**'
        if block.count("**") % 2 == 1:
            bad += 1
            print(f"BAD|{rel}:{i + 1}: odd '**' count in paragraph block: '{lines[i].strip()[:80]}'")
        i = end + 1
print(f"TOTALS bad={bad}")
PY
)
C43_BAD=$(echo "$CHECK43" | sed -n 's/^TOTALS bad=\([0-9]*\)/\1/p')
if [ "${C43_BAD:-1}" -eq 0 ]; then
    ok "Controls sections bullet-hygenic; all paragraph blocks bold-balanced and Controls parens balanced"
else
    error "Analysis-section hygiene violations (dangling Controls lines, unbalanced parens, broken '**' bold) — repair via 07-methodology/fix-controls-bullets.py + per-case review:"
    echo "$CHECK43" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 44: Root-README folder-tree agreement with value-stream-index.md ---
echo "--- Check 44: Root-README folder-tree agreement ---"
# Consistency review #28 found the root-README folder tree had drifted from the index
# after the post-catalog gap-fill batches: batch 1 (W5497–W5502) updated the tree's
# workflows/ total line but not the per-VS directory rows, so 6 rows sat at pre-batch
# counts (VS-10/19/21/36/83/84) and batch 2 (W5503/W5504) repeated the miss (VS-24/31)
# — batch 3 (W5505–W5507, VS-07) was reconciled only because it also touched the
# total line. The tree's proposed-register description row had drifted identically
# (8/W5497–W5504 vs 11/W5497–W5507). Checks 2/24 guard the index and workflows/README
# against the same drift but never scan the root README tree. This check derives the
# canonical per-VS PA/workflow counts and grand total from value-stream-index.md, the
# unclassified complement and ID range from workflow-criticality-proposed.md, and
# validates every tree row against them.
CHECK44=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, sys
ROOT = sys.argv[1]
bad = []
# canonical: index per-VS (PAs, workflows) + grand total
idx = {}
total = None
for line in open(os.path.join(ROOT, "01-model-company/workflows/value-stream-index.md"), encoding="utf-8"):
    m = re.match(r"^\|.*?\[VS-(\d+)\]\([^)]+\)\s*\|[^|]+\|[^|]+\|\s*(\d+)\s*\|\s*([\d,]+)\s*\|\s*$", line)
    if m:
        idx[int(m.group(1))] = (int(m.group(3).replace(",", "")), int(m.group(2)))  # (workflows, PAs)
    m = re.match(r"^\|\s*\|\s*\|\s*\|\s*\*\*Grand Total\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*([\d,]+)\*\*\s*\|\s*$", line)
    if m:
        total = int(m.group(2).replace(",", ""))
if total is None or sum(v[0] for v in idx.values()) != total:
    bad.append(f"index parse failed: grand_total={total} vs per-VS sum={sum(v[1] for v in idx.values())}")
# canonical: unclassified complement + ID range from the proposal register
prop = open(os.path.join(ROOT, "01-model-company/workflows/workflow-criticality-proposed.md"), encoding="utf-8").read()
m = re.search(r"\*\*Workflow coverage:\*\* (\d+) unclassified workflows", prop)
unclassified = int(m.group(1)) if m else -1
ids = [int(w[1:]) for w in re.findall(r"^\| (W\d+) \|", prop, re.M)]
lo, hi = (min(ids), max(ids)) if ids else (None, None)
if unclassified >= 0 and len(ids) != unclassified:
    bad.append(f"proposal register: coverage line says {unclassified}, table holds {len(ids)} rows")
# root README tree rows
tree = {}
tree_total = None
prop_rows = []
for i, line in enumerate(open(os.path.join(ROOT, "README.md"), encoding="utf-8"), 1):
    m = re.search(r"VS-(\d+)-[a-z0-9-]+/\s+([\d,]+) workflows \((\d+) process areas\)", line)
    if m:
        tree[int(m.group(1))] = (int(m.group(2).replace(",", "")), int(m.group(3)))
        continue
    m = re.search(r"workflows/\s+([\d,]+) workflows organized by value stream", line)
    if m:
        tree_total = int(m.group(1).replace(",", ""))
    if "├── workflow-criticality-proposed.md" in line and "post-catalog" in line:
        cm = re.search(r"\((\d+) post-catalog workflows (W\d+)–(W\d+) added", line)
        prop_rows.append((i, cm))
missing = sorted(set(idx) - set(tree))
extra = sorted(set(tree) - set(idx))
if missing:
    bad.append(f"tree omits index VS rows: {missing[:8]}")
if extra:
    bad.append(f"tree lists non-index VS rows: {extra[:8]}")
for v in sorted(set(idx) & set(tree)):
    if tree[v] != idx[v]:
        bad.append(f"VS-{v}: tree says {tree[v][0]} workflows / {tree[v][1]} PAs, index says {idx[v][0]} / {idx[v][1]}")
if tree_total != total:
    bad.append(f"tree 'workflows/ N workflows organized' line says {tree_total}, index grand total is {total}")
for i, cm in prop_rows:
    if unclassified > 0:
        if not cm:
            bad.append(f"README.md:{i}: proposed-register row lacks '(N post-catalog workflows Wxxx–Wyyy added…)' while {unclassified} are unclassified")
        else:
            cnt, a, b = int(cm.group(1)), int(cm.group(2)[1:]), int(cm.group(3)[1:])
            if cnt != unclassified:
                bad.append(f"README.md:{i}: proposed-register row says {cnt} post-catalog workflows, register holds {unclassified}")
            if lo is not None and (a, b) != (lo, hi):
                bad.append(f"README.md:{i}: proposed-register range W{a}–W{b} != register W{lo}–W{hi}")
    elif cm and int(cm.group(1)) != 0:
        bad.append(f"README.md:{i}: proposed-register row still quotes {cm.group(1)} post-catalog workflows while register is empty")
print(f"TOTALS vs={len(set(idx) & set(tree))} total={total} unclassified={unclassified} problems={len(bad)}")
for b in bad:
    print("BAD|" + b)
PY
)
C44_BAD=$(echo "$CHECK44" | sed -n 's/^TOTALS .* problems=\([0-9]*\)/\1/p')
if [ "${C44_BAD:-1}" -eq 0 ]; then
    C44_VS=$(echo "$CHECK44" | sed -n 's/^TOTALS vs=\([0-9]*\) .*/\1/p')
    C44_U=$(echo "$CHECK44" | sed -n 's/^TOTALS .* unclassified=\([0-9]*\) .*/\1/p')
    ok "Root-README folder tree agrees with value-stream-index.md (${C44_VS} VS rows, workflow/PA counts, total line) and workflow-criticality-proposed.md (${C44_U} unclassified)"
else
    error "Root-README folder-tree rows disagree with the canonical registers:"
    echo "$CHECK44" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 45: Current-state workflow-total figures on anchored self-description surfaces ---
echo "--- Check 45: Anchored current-state total-figure agreement ---"
# Consistency review #28 repaired 9 further current-state surfaces quoting the
# pre-batch-3 canonical total (5,357) or the pre-batch-3 unclassified complement
# (8 / W5497–W5504) that no prior check scanned: the format-guide required-fields
# completeness claim, its 100%-field-header-presence claim, and its Repository
# Layout / Related Documents proposed-register rows; the requirement-matrix closing
# 'The full N-workflow inventory' line; the VS-133 self-descriptions (README 'runs
# ~N documented workflows' + the PA-133.1/133.3 Volume rows); and the dependency-map
# VS-133 row. Blanket total-figure scans false-positive on frozen history
# (*Date: footers, 'Prior v' notes, gap-analysis pass tables), so this check
# instead validates the anchored claim forms on those exact surfaces against the
# index grand total, the classification confirmed-row count, and the proposal
# register's unclassified complement and ID range.
CHECK45=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, glob, sys
ROOT = sys.argv[1]
W = os.path.join(ROOT, "01-model-company", "workflows")
bad = []
# canonical figures
total = None
for line in open(os.path.join(W, "value-stream-index.md"), encoding="utf-8"):
    m = re.match(r"^\|\s*\|\s*\|\s*\|\s*\*\*Grand Total\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*([\d,]+)\*\*\s*\|\s*$", line)
    if m:
        total = int(m.group(2).replace(",", ""))
rows = None
for line in open(os.path.join(W, "workflow-criticality-classification.md"), encoding="utf-8"):
    m = re.match(r"^\| \*\*Confirmed Total\*\* \| \| \*\*([\d,]+)\*\* \|", line)
    if m:
        rows = int(m.group(1).replace(",", ""))
prop = open(os.path.join(W, "workflow-criticality-proposed.md"), encoding="utf-8").read()
m = re.search(r"\*\*Workflow coverage:\*\* (\d+) unclassified workflows", prop)
unclassified = int(m.group(1)) if m else -1
ids = [int(w[1:]) for w in re.findall(r"^\| (W\d+) \|", prop, re.M)]
lo, hi = (min(ids), max(ids)) if ids else (None, None)
def n(s):
    return int(s.replace(",", ""))
def want_total(label, got):
    if got != total:
        bad.append(f"{label}: total figure {got} != index grand total {total}")
# anchored surfaces (file glob, regex, validator fn); each regex must match exactly once
surfaces = [
    ("WORKFLOW-FORMAT-GUIDE.md", r"All ([\d,]+) workflows now carry all 9 required fields",
     lambda m: want_total("format-guide required-fields completeness claim", n(m.group(1))), 1),
    ("WORKFLOW-FORMAT-GUIDE.md", r"present on all \*\*([\d,]+) workflows \(100% presence\)\*\*",
     lambda m: want_total("format-guide 100%-presence claim", n(m.group(1))), 1),
    ("WORKFLOW-FORMAT-GUIDE.md", r"\(([\d,]+) confirmed rows; (\d+) post-catalog workflows keyword-proposed\)",
     lambda m: (n(m.group(1)) != rows and bad.append(f"format-guide layout row: confirmed-rows figure {n(m.group(1))} != classification {rows}"),
                int(m.group(2)) != unclassified and bad.append(f"format-guide layout row: post-catalog figure {m.group(2)} != register {unclassified}")), 1),
    ("WORKFLOW-FORMAT-GUIDE.md", r"currently empty — 0 unclassified",
     lambda m: (unclassified != 0 and bad.append(f"format-guide proposed-register rows claim 'currently empty — 0 unclassified' but the register holds {unclassified} unclassified workflows")), 2),
    (os.path.join("..", "requirement-workflow-matrix.md"), r"The full ([\d,]+)-workflow / 188-value-stream inventory",
     lambda m: want_total("requirement-matrix inventory line", n(m.group(1))), 1),
]
counts = {}
for fname, pat, fn, expect in surfaces:
    path = os.path.join(W, fname)
    txt = open(path, encoding="utf-8").read()
    ms = list(re.finditer(pat, txt))
    counts[fname + "|" + pat[:30]] = len(ms)
    if len(ms) != expect:
        bad.append(f"{fname}: anchored pattern '{pat[:40]}…' matched {len(ms)} times (expected exactly {expect}) — surface may have been rewritten; update Check 45's anchor")
        continue
    for m in ms:
        fn(m)
# VS-133 self-description sentences (README + both PA Volume rows)
p = os.path.join(W, "VS-133-operational-excellence-process-mining-continuous-improvement", "README.md")
ms = list(re.finditer(r"runs ~([\d,]+) documented workflows", open(p, encoding="utf-8").read()))
if len(ms) != 1:
    bad.append("VS-133 README: 'runs ~N documented workflows' anchor missing/duplicated")
else:
    want_total("VS-133 README self-description", n(ms[0].group(1)))
for pa in ("PA-133.1-opex-strategy-governance-and-improvement-methodology.md",
           "PA-133.3-productivity-benefit-realization-and-opex-analytics.md"):
    p = os.path.join(W, "VS-133-operational-excellence-process-mining-continuous-improvement", pa)
    ms = list(re.finditer(r"~([\d,]+) workflows across 188 value streams", open(p, encoding="utf-8").read()))
    if len(ms) != 1:
        bad.append(f"VS-133 {pa}: Volume-row anchor missing/duplicated")
    else:
        want_total(f"VS-133 {pa} Volume row", n(ms[0].group(1)))
# dependency-map VS-133 row
p = os.path.join(W, "workflow-dependency-map.md")
ms = [m for m in re.finditer(r"^\| VS-133 .*?over the ~([\d,]+) workflows", open(p, encoding="utf-8").read(), re.M)]
if len(ms) != 1:
    bad.append("workflow-dependency-map.md: VS-133 row 'over the ~N workflows' anchor missing/duplicated")
else:
    want_total("dependency-map VS-133 row", n(ms[0].group(1)))
print(f"TOTALS total={total} confirmed_rows={rows} unclassified={unclassified} problems={len(bad)}")
for b in bad:
    print("BAD|" + b)
PY
)
C45_BAD=$(echo "$CHECK45" | sed -n 's/^TOTALS .* problems=\([0-9]*\)/\1/p')
if [ "${C45_BAD:-1}" -eq 0 ]; then
    C45_T=$(echo "$CHECK45" | sed -n 's/^TOTALS total=\([0-9]*\) .*/\1/p')
    ok "Anchored current-state total figures agree with the canonical registers (grand total ${C45_T}; format-guide, requirement-matrix, VS-133 and dependency-map surfaces)"
else
    error "Anchored current-state total figures disagree with the canonical registers:"
    echo "$CHECK45" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 46: Stale tender-mix / fleet / SKU figures & superseded statutory citations ---
echo "--- Check 46: stale-figure & superseded-citation literal guard ---"
# Consistency review #29 repaired the semantic figure/statute drift no structural check
# could see: (1) W261's e-wallet Volume band quoted a 560,000-POS-transaction base × 30%
# share (canonical: 2.8M × ~15% = ~420,000/month per W1268) and a ~45,000 ecommerce
# order base (canonical ~42,900), leaving ~186,000/month totals in three spots; (2)
# W1268's background converted 420,000/month to '42,000 per day' (correct: ~14,000);
# (3) W265's maintenance fleet quoted '~1,000 terminals'/'4,000 PM events/quarter'/
# '~500 hours/quarter' against the canonical 3-per-store = 600-terminal fleet the
# same workflow's own Time Estimate derives (~300 hours/quarter); (4) W478's Volume
# quoted '~80,000 active SKUs' (canonical 35,000 active / ~55,000 incl. master);
# (5) statutory citations: 'RA 10862' for the LPG Industry Regulation Act (correct:
# RA 10617), 'RA 10691' for 13th-month pay (correct: PD 851), phantom BIR ATC codes
# WI 028/WI 160/WI 011 (correct: WC 010 professional services, WI 010 rent,
# WP 010 purchases of goods), and the DO 13-98 construction-OSH citation for store
# forklifts (correct: OSH Standards Rule 1160 series per D.O. 198-18). Consistency
# review #31 extended this guard with five more retired literals: 'RA 11592' is the
# actual LPG Industry Regulation Act (2021) so review #29's 'RA 10617' adjudication is
# itself retired (RA 10617 sits in the late-2013 numbering, predating the 17th/18th-
# Congress LPG bills; review #31 also mis-dated the act '(2020)' — corrected to 2021
# by review #33); review #31 also flipped the Philippine Competition Act number to
# RA 10677, which review #33 REVERSED: the Philippine Competition Act is RA 10667
# (signed 21 July 2015 — the act that creates the PCC; RA 10668 is the Right-of-Way
# Act and RA 10677 is not the Competition Act), so every RA 10677 spot (25 incl.
# VS-129 headings, index/dependency/touchpoint-map rows) went RA 10677 -> RA 10667 and
# the guard now retires the RA 10677 form instead of the correct number;
# hazardous-waste management under RA 6969 runs on DAO 2004-36 (Procedural Manual,
# 6-month storage limit) — DAO 2013-22 (mercury CCO) was mis-cited and a US-style
# 90-day accumulation limit had drifted into the DENR storage-limit machinery; RR
# 34-2022 does not exist as a BIR transfer-pricing regulation (correct: RR 02-2013);
# RA 9266 is the Architecture Act and cannot perfect collateral (correct: Act No.
# 1508 chattel mortgage / RA 11057 PPSA). Consistency review #32 found the sweep
# had missed sibling surfaces in the same hazardous-waste/chemical-safety family:
# one spelled-out 'DENR Administrative Order No. 2013-22' spot (PA-07.2) whose form
# dodged the literal guard plus a residual 90-day limit contradicting PA-22.1's own
# post-#31 180-day line; seven 'DAO 2015-09' spots doing the Procedural Manual's job
# or mandating SDS (PA-24.3 x6, PA-25.1); a phantom toxic-substances SDS order
# ('DENR Administrative Order 2015-08') paired with a dubious 'DOLE Department Order
# 1989-114' OSHS promulgation (PA-01.3); penalty attribution to 'DAO 2021-19'
# (PA-07.2); and septic-tank standards attributed to 'DAO 2005-10' instead of the
# Sanitation Code PD 856 Ch. XVII / National Plumbing Code (PA-09.2). Consistency
# review #33 (statutory-citation correctness sweep #4 + house-spelling normalization)
# found six more mis-citations: 'ADR Act RA 876' (PA-100.1) conflates the 1953
# Arbitration Law with the 2004 ADR Act (RA 9285); 'age-restricted items per RA 7610'
# (PA-08.1 x3, incl. the automation fragment) cites the child-protection act where the
# age-verification mandates run per RA 9211 Sec. 9 (tobacco) / PD 1619 (volatile
# solvents); 'DOLE DO 53-03' (erp-requirements.md) mistypes the drug-free-workplace
# guidelines, which are D.O. 53-04 (the catalog's own W4458) — [review #68 REVERSED:
# web-verified vs DOLE's own download page and the SC E-Library, the private-sector
# drug-free-workplace guidelines are D.O. 53-03, s. 2003; #33's '53-04' was a
# mis-verification that flipped only COM-001 + the VS-150 README against the corpus
# majority (53-03 in CTL-129, W4458, PA-150.1/2/3, PA-22.2, PA-167.2, gap-analysis)];
# 'RR 13-2018 (SAF-T)'
# (PA-17.3) is neither the e-invoicing regulation (RR 8-2020 under NIRC Sec. 237 as
# amended by TRAIN) nor a Philippine standard (SAF-T is an OECD format, not BIR);
# 'PD 1586, RA 6969' (PA-31.3) pairs the EIS/ECC law with hazardous-release
# notification, which runs under RA 6969 + its IRR alone; and the EVIDA IRR is cited
# as 'DAO 2023-05' (VS-192 README + PA-192.1) although EVIDA is DOE-administered — its
# IRR is a DOE department circular, while DENR DAO 2023-05 is the EPR Act (RA 11898)
# IRR. All repaired; the guard below now covers every retired form. This check guards the retired
# literals repo-wide so no surface regresses to them. CHANGELOG.md (frozen history + this
# repair's own description) and 'X -> Y' change-note contexts (e.g. the
# classification register's dated version footers) are exempt.
CHECK46=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
SKIP = {'CHANGELOG.md'}
bad_literals = [
    (r'RA\s?10862', 'LPG act citation (correct: RA 11592 — LPG Industry Regulation Act, 2020)'),
    (r'RA\s?10617', 'superseded LPG act citation from review #29 (correct: RA 11592)'),
    (r'RA\s?10677', 'superseded Philippine Competition Act citation from review #31 (correct: RA 10667 — the Philippine Competition Act of 21 July 2015 that creates the PCC)'),
    # review #64 REVERSAL of the #31 retirement: web-verified vs WTO notification/EMB's own
    # PDF/Japan-MOE — DAO 2013-22 IS the Revised Procedures and Standards for the
    # Management of Hazardous Wastes (RA 6969), revising DAO 2004-36; generators keep
    # on-site accumulation to 90 days. The old 'mercury CCO' claim was a mis-verification.
    (r'(?:DENR )?(?:DAO|AO)\s?2004-36(?! manual)', 'stale hazardous-waste-manual citation (correct: DAO 2013-22, which revised DAO 2004-36; 90-day on-site accumulation)'),
    (r'(?:180-day|6-month[/ ]180-day|180 day) (?:storage|accumulation) limit', 'stale 180-day storage limit (correct: 90-day on-site accumulation per DAO 2013-22)'),
    (r'storage to 6 months', 'stale 6-month storage limit (correct: 90-day per DAO 2013-22)'),
    # (the spelled-out 2013-22 retirement was removed in review #64 — see the DAO-2004-36 reversal note above)
    (r'DAO\s?2015-09', 'phantom/misapplied hazardous-waste order (correct: DENR DAO 2004-36 Procedural Manual under RA 6969)'),
    (r'(?:DAO\s?|DENR Administrative Order\s?)2015-08', 'mis-cited toxic-substances/SDS order (correct: RA 6969 and its implementing rules; workplace SDS also per OSH Standards / D.O. 198-18)'),
    (r'DAO\s?2021-19', 'mis-attributed hazardous-waste penalty citation (fines run under RA 6969 / DAO 2004-36)'),
    (r'(?:DA|A)O\s?2005-10', 'mis-cited septic-tank standards order (correct: Sanitation Code PD 856 Ch. XVII + National Plumbing Code; bare "AO 2005-10" caught too — the dodge class reviews #32/#71 documented)'),
    (r'DOLE Department Order\s?1989-114', 'dubious OSHS promulgation citation (correct: OSH Standards as amended, per DOLE D.O. 198-18)'),
    (r'DOLE Department Order\s?136-14', 'DO 136-14 governs construction-site OSH, not chemical/SDS duties (correct here: RA 6969 + implementing rules / OSH Standards per D.O. 198-18)'),
    (r'RR\s?34-2022', 'phantom BIR transfer-pricing regulation (correct: RR 02-2013)'),
    (r'ADR Act RA 876', 'mis-labeled arbitration citation (RA 876 is the 1953 Arbitration Law; the ADR Act is RA 9285)'),
    (r'age-restricted items per RA 7610', 'age-verification mis-citation (RA 7610 is child protection; age-restricted sale bans run per RA 9211 Sec. 9 tobacco / PD 1619 volatile solvents)'),
    # review #68 REVERSAL of the #33 adjudication: web-verified vs DOLE's own page and
    # the SC E-Library — the drug-free-workplace private-sector guidelines are
    # D.O. 53-03, s. 2003; '53-04' was the mis-verification.
    (r'D\.?\s?O\.?\s?53-04', 'the drug-free-workplace guidelines are DOLE D.O. 53-03, s. 2003, not 53-04'),
    (r'RR\s?13-2018 \(SAF-T\)', 'SAF-T is not a Philippine BIR standard; e-invoicing/e-receipts run per RR 8-2020 under NIRC Sec. 237 as amended by TRAIN'),
    (r'PD 1586, RA 6969', 'hazardous-release notification runs under RA 6969 + its IRR alone (PD 1586 is the EIS/ECC system)'),
    (r'IRR \(DAO 2023-05\)', 'the EVIDA (RA 11697) IRR is a DOE department circular (DENR DAO 2023-05 is the EPR Act RA 11898 IRR)'),
    (r'RA\s?10691', '13th-month-pay citation (correct: PD 851)'),
    (r'\bWI 028\b|\bWI 160\b|\bWI 011\b', 'phantom BIR ATC code (correct: WC 010 services / WI 010 rent / WP 010 goods)'),
    (r'560,000 POS transactions', 'stale e-wallet base (canonical: ~2.8M POS transactions × ~15% = ~420,000/month)'),
    (r'42,000 transactions per day', 'stale per-day conversion (canonical: ~14,000/day = 420,000/month ÷ 30)'),
    (r'~186,000 e-wallet', 'stale e-wallet total (canonical: ~437,000/month incl. ~17,000 ecommerce)'),
    (r'~?1,000 terminals', 'stale terminal-fleet figure (canonical: 600 POS terminals = 3/store × 200)'),
    (r'80,000 active SKUs', 'stale SKU figure (canonical: 35,000 active / ~55,000 item-master records)'),
]
stale = []
for dirpath, _d, files in os.walk(ROOT):
    if os.sep + '.git' in dirpath or os.sep + '__pycache__' in dirpath: continue
    for fn in files:
        if not fn.endswith('.md') or fn in SKIP: continue
        path = os.path.join(dirpath, fn)
        txt = open(path, encoding='utf-8', errors='replace').read()
        for pat, why in bad_literals:
            for m in re.finditer(pat, txt):
                lo = max(0, m.start()-40); hi = min(len(txt), m.end()+40)
                if '->' in txt[lo:hi] or '\u2192' in txt[lo:hi]:
                    continue  # legitimate historical 'X -> Y' change-note
                line_no = txt.count('\n', 0, m.start()) + 1
                stale.append(f"{os.path.relpath(path, ROOT)}:{line_no}: '{m.group(0)}' — {why}")
print(f"STALE={len(stale)}")
for s in stale: print(f"STALE|{s}")
PY
)
C46_BAD=$(echo "$CHECK46" | sed -n 's/^STALE=\([0-9]*\)$/\1/p')
if [ "${C46_BAD:-1}" -eq 0 ]; then
    ok "No stale tender-mix/fleet/SKU figures or superseded statutory citations (RA/ATC/DO literals) in current-state prose"
else
    error "Stale figures / superseded statutory citations found in current-state prose: (incl. RA 10617/RA 10677/DAO 2013-22/DAO 2015-09/RR 34-2022)"
    echo "$CHECK46" | grep -E '^STALE\|' | sed 's/^STALE|/    /'
fi

# --- Check 47: per-store rate ↔ chain-wide total unit coherence + explicit ×-math ---
echo "--- Check 47: per-store-rate/chain-total unit coherence & store-multiplication math ---"
# Consistency review #30 found a figure-drift family no structural check could see:
# Frequency/Volume fields pairing a per-store cadence with a chain-wide total whose
# unit does not cohere with the rate (e.g. '~600-800 bulk negotiation transactions/
# month across 200 stores (~3-4 per store per WEEK)' — 3-4/store/week is ~2,600-3,500/
# month, while the canonical total and Volume anchor ~700/month imply a per-MONTH
# rate; and '~4,000-8,000/year chain-wide' beside '~5-10 per store per week' where the
# Time Estimate's own chain-wide arithmetic was monthly). The same review repaired
# the store receiving-cadence cluster (W723/W745 quoted 600-1,000/2,000 truck &
# receiving events per DAY chain-wide vs the canonical 2-3 DC deliveries/store/WEEK
# + ~500-600 DSD receipts/month chain-wide per profile §7.1). Two guarded forms:
#   (a) same-line per-store rate ('N-M ... per store per week|month|day|year') vs
#       same-line chain total ('~A-B .../month|week|day|year chain-wide|across 200
#       stores'), normalized to events per month per 200-store chain (week=4.33,
#       day=30, year=1/12) with a 25% disjointness margin; multiple rates on one
#       line are summed before comparison; effort-denominated totals (hours/min/
#       staff-hours) are skipped — different dimension;
#   (b) explicit single-multiplier store math ('200 stores × ~N ... = ~M') verified
#       within 35% (multi-factor chains like '× ~7 ... × 6 promos' are skipped).
CHECK47=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = os.path.join(sys.argv[1], "01-model-company")
MONTHLY = {"week": 4.33, "month": 1.0, "day": 30.0, "year": 1/12}
SUFFIX = {"k": 1e3, "m": 1e6}
def nums(a, b=None):
    def val(s):
        s = s.strip().replace(",", "").replace("~", "")
        mult = 1.0
        if s and s[-1].lower() in SUFFIX:
            mult = SUFFIX[s[-1].lower()]; s = s[:-1]
        return float(s) * mult
    return val(a), val(b or a)
rate_re = re.compile(r"~?([\d,.]+[KkMm]?)\s*[\u2013-]\s*([\d,.]+[KkMm]?)?[^|;()]{0,60}?per store per (week|month|day|year)", re.I)
total_re = re.compile(r"~([\d,.]+[KkMm]?)\s*[\u2013-]\s*([\d,.]+[KkMm]?)?[^|;()]{0,60}?/(month|week|day|year)\s*(?:chain-?wide|across (?:the |all )?200\+? locations|across (?:the |all )?200 stores)", re.I)
effort_re = re.compile(r"(?:staff-)?(?:hours?|hrs?|min(?:ute)?s?|person-hours?|tons?|tonnes?)\s*/(?:month|week|day|year)", re.I)
prod_re = re.compile(r"200 stores?\s*[\u00d7x]\s*~?([\d,.]+)(\s*[\u2013-]\s*~?[\d,.]+)?([^=\n]{0,90})?=\s*~?([\d,.]+[KkMm]?)(\s*[\u2013-]\s*~?[\d,.]+[KkMm]?)?")
cad_re = re.compile(r"/(week|month|day|year)\b|per (week|month|day|year)\b", re.I)
bad = []
for dirpath, _d, files in os.walk(ROOT):
    if os.sep + ".git" in dirpath or os.sep + "__pycache__" in dirpath: continue
    for fn in sorted(files):
        if not fn.endswith(".md") or fn == "CHANGELOG.md": continue
        path = os.path.join(dirpath, fn)
        rel = os.path.relpath(path, ROOT)
        for i, line in enumerate(open(path, encoding="utf-8"), 1):
            rates = []
            for m in rate_re.finditer(line):
                lo, hi = nums(m.group(1), m.group(2))
                mult = MONTHLY[m.group(3).lower()]
                rates.append((lo * 200 * mult, hi * 200 * mult))
            if rates and not effort_re.search(line):
                rlo = sum(r[0] for r in rates); rhi = sum(r[1] for r in rates)
                tm = total_re.search(line)
                if tm:
                    tlo, thi = nums(tm.group(1), tm.group(2))
                    tmult = MONTHLY[tm.group(3).lower()]
                    tlo, thi = tlo * tmult, thi * tmult
                    if thi < rlo * 0.75 or tlo > rhi * 1.33:
                        bad.append(f"{rel}:{i}: per-store rate -> {rlo:,.0f}-{rhi:,.0f}/month/chain vs total {tlo:,.0f}-{thi:,.0f}: {line.strip()[:110]}")
            pm = prod_re.search(line)
            if pm:
                seg = pm.group(3) or ""
                if re.search(r"\b(?:min|minute|hour|hr)\b", seg, re.I) or " + " in seg or (line.count("\u00d7") + line.count(" x ")) > 1:
                    continue  # effort dimension, additive expression, or multi-factor chain
                cm = cad_re.search(seg)
                cad = MONTHLY[(cm.group(1) or cm.group(2)).lower()] if cm else 1.0
                plo, phi = nums(pm.group(1), (pm.group(2) or pm.group(1)).lstrip(" \u2013-").replace("~", ""))
                stated_unit_line = line[pm.end():pm.end() + 60]
                sm2 = cad_re.search(stated_unit_line)
                sunit = MONTHLY[(sm2.group(1) or sm2.group(2)).lower()] if sm2 else cad
                mlo, mhi = nums(pm.group(4), (pm.group(5) or pm.group(4)).lstrip(" \u2013-").replace("~", ""))
                # raw comparison first (handles period-count factors like '× 365 days = 73,000/year');
                # fall back to cadence-normalized comparison ('× 1 audit/week = ~800/month')
                raw_ok = not (mhi < plo * 200 * 0.65 or mlo > phi * 200 * 1.35)
                if not raw_ok:
                    plo_m, phi_m = plo * 200 * cad, phi * 200 * cad
                    mlo_m, mhi_m = mlo * sunit, mhi * sunit
                    if mhi_m < plo_m * 0.65 or mlo_m > phi_m * 1.35:
                        bad.append(f"{rel}:{i}: store math {plo:,.0f}-{phi:,.0f} x200 = {plo*200:,.0f}-{phi*200:,.0f} (cadence-normalized {plo_m:,.0f}-{phi_m:,.0f}/month) != stated {mlo:,.0f}-{mhi:,.0f}: {line.strip()[:110]}")
print(f"TOTALS bad={len(bad)}")
for b in bad: print(f"BAD|{b}")
PY
)
C47_BAD=$(echo "$CHECK47" | sed -n 's/^TOTALS bad=\([0-9]*\)$/\1/p')
if [ "${C47_BAD:-1}" -eq 0 ]; then
    ok "All per-store rates cohere with their same-line chain-wide totals (unit-normalized) and all explicit 200-store multiplications check out"
else
    error "Per-store-rate/chain-total unit mismatches or store-math errors found ($C47_BAD):"
    echo "$CHECK47" | grep -E '^BAD\|' | sed 's/^BAD|/    /' | head -20 || true
fi

# --- Check 48: steps-table row integrity (leading pipe, canonical header, ID ordering) ---
echo "--- Check 48: steps-table row integrity & step-ID ordering ---"
# Consistency review #30 found three step-table defects invisible to Check 29
# (which only validates rows that already start with '|') and to every ordering-
# blind structural check: (1) five rows missing their leading table pipe
# ('6a |', '16c |', '11 |', '12 |', '9a |' in PA-17.4/PA-17.1/PA-05.2 — the last
# also missing its trailing pipe), which rendered outside their tables; (2) two
# steps-table headers with typos ('Role (R))' in PA-57.2, 'Role(A)' in PA-170.3);
# (3) three mis-ordered step rows (W922's row 2 above row 1; W35's 14a above 14;
# W9's 16c above 16a/16b). House convention: step IDs ascend (num, letter) with
# letter variants AFTER their base row (4a/4b/4c per W47, 16a-16e per W9), and
# each ### section or sub-workflow may restart at 1. This check enforces all three.
CHECK48=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, glob, sys
ROOT = os.path.join(sys.argv[1], "01-model-company")
bad = []
CANON = re.compile(r"^\| # \| Activity \| Role \(R\) \| Role \(A\) \| (Duration|Frequency|Latency) \|$")
ROWID = re.compile(r"^(\d+)([a-z]?)\s*\|")
for f in sorted(glob.glob(os.path.join(ROOT, "workflows", "VS-*", "PA-*.md"))):
    rel = os.path.relpath(f, ROOT)
    lines = open(f, encoding="utf-8").readlines()
    wid = None
    seq = []
    def flush(seq, wid, lineno):
        prev = None
        for tok, ln in seq:
            n, letter = int(tok[:-1]) if tok[-1].isalpha() else int(tok), (tok[-1] if tok[-1].isalpha() else "")
            if prev is not None:
                pn, pl = prev
                if not ((n == pn and letter > pl) or n == pn + 1):
                    bad.append(f"{rel}:{ln}: step row {tok} out of order after {pn}{pl} (workflow {wid})")
            prev = (n, letter)
    in_steps = False
    for i, l in enumerate(lines, 1):
        m = re.match(r"## (W\d+[A-Z]?)\.", l)
        if m:
            flush(seq, wid, i); seq = []; wid = m.group(1); in_steps = False; continue
        if l.startswith("### "):
            flush(seq, wid, i); seq = []; in_steps = False; continue
        if l.startswith("| # | Activity |"):
            if not CANON.match(l.rstrip("\n")):
                bad.append(f"{rel}:{i}: non-canonical steps-table header: {l.strip()[:60]}")
            in_steps = True; continue
        bare = ROWID.match(l)
        if bare:
            ctx = next((lines[j] for j in range(i - 2, min(i + 1, len(lines))) if lines[j].strip()), "")
            if ctx.startswith("|"):
                bad.append(f"{rel}:{i}: step row missing leading table pipe: {l.strip()[:60]}")
        if in_steps:
            sm = re.match(r"^\| (\d+)([a-z]?) \|", l)
            if sm:
                seq.append((sm.group(1) + sm.group(2), i))
            elif l.strip() and not l.startswith("|"):
                flush(seq, wid, i); seq = []; in_steps = False
    flush(seq, wid, len(lines))
print(f"TOTALS bad={len(bad)}")
for b in bad: print(f"BAD|{b}")
PY
)
C48_BAD=$(echo "$CHECK48" | sed -n 's/^TOTALS bad=\([0-9]*\)$/\1/p')
if [ "${C48_BAD:-1}" -eq 0 ]; then
    ok "All 5,425 steps tables carry canonical headers, well-formed rows, and (num, letter)-ascending step IDs"
else
    error "Steps-table integrity violations found ($C48_BAD):"
    echo "$CHECK48" | grep -E '^BAD\|' | sed 's/^BAD|/    /' | head -25 || true
fi

# --- Check 49: Time Estimate finalization state (no mechanical drafts; full coverage) ---
echo "--- Check 49: Time Estimate finalization state ---"
# backfill-time-estimate.py (2026-06-21) shipped 410 honest-draft roll-ups labelled
# "Draft roll-up from per-step Durations"; finalize-time-estimates.py (2026-08-28)
# completed all 407 then remaining into the per-occurrence + annualization house style
# (W424's hand-authored finalization was the exemplar). Guards: (a) the retired draft
# literal must not reappear in any PA file; (b) every workflow block must carry at
# least one '### Time Estimate' header — stronger than Check 22's either-form presence
# test. Section COUNT may legitimately exceed the workflow count (variant-grouped
# workflows carry one Time Estimate per variant, like the 5,425 steps tables), so
# presence is asserted per workflow, not by aggregate equality.
C49_DRAFTS=$(grep -rlF "Draft roll-up from per-step Durations" "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null || true)
C49_DRAFT_N=$(echo -n "$C49_DRAFTS" | grep -cP 'PA-' || true)
C49_MISSING=$(python3 - "$REPO_ROOT" <<'PY'
import glob, os, re, sys
ROOT = sys.argv[1]
missing = []
total_wf = total_te = 0
for f in glob.glob(f"{ROOT}/01-model-company/workflows/VS-*/PA-*.md"):
    txt = open(f, encoding="utf-8", errors="replace").read()
    for m in re.finditer(r"^## (W\d+[A-Z]?)\..*?(?=^## W|\Z)", txt, re.M | re.S):
        block = m.group(0)
        total_wf += 1
        n = len(re.findall(r"^### Time Estimate\s*$", block, re.M))
        total_te += n
        if n == 0:
            missing.append(f"{os.path.relpath(f, ROOT)}: {m.group(1)}")
print(f"{total_wf}|{total_te}|{len(missing)}")
for x in missing:
    print("MISSING|" + x)
PY
)
C49_WF=$(echo "$C49_MISSING" | head -1 | cut -d'|' -f1)
C49_TE=$(echo "$C49_MISSING" | head -1 | cut -d'|' -f2)
C49_MN=$(echo "$C49_MISSING" | head -1 | cut -d'|' -f3)
if [ "$C49_DRAFT_N" -eq 0 ] && [ "$C49_MN" -eq 0 ]; then
    ok "No mechanical draft Time Estimates remain; all $C49_WF workflows carry a '### Time Estimate' section ($C49_TE sections incl. variant sub-sections; finalized 2026-08-28 per finalize-time-estimates.py)"
else
    if [ "$C49_DRAFT_N" -ne 0 ]; then
        error "$C49_DRAFT_N PA file(s) still carry the mechanical draft roll-up marker (run 07-methodology/finalize-time-estimates.py):"
        echo "$C49_DRAFTS" | sed 's/^/    /'
    fi
    if [ "$C49_MN" -ne 0 ]; then
        error "$C49_MN workflow(s) lack a '### Time Estimate' header:"
        echo "$C49_MISSING" | grep -E '^MISSING\|' | sed 's/^MISSING|/    /' | head -20
    fi
fi

# --- Check 50: Time-Estimate / Staffing inline arithmetic guard ---
echo "--- Check 50: Time-Estimate & Staffing inline arithmetic ---"
# audit-time-estimate-math.py (2026-08-29) re-derives every explicit
# "<A> × <B> (=|≈) <result>" chain written into the finalized Time Estimate and
# Staffing Implication paragraphs (5,382 sections), applying the unit
# conventions the house style licenses (min↔hours ÷/×60, sec→hours, workday/
# workweek/month-length alternates, per-cadence annualization ×12/×4/×52/×365/×6,
# noun/suffix cancellation, the canonical 200-store and 4-DC chain scalings,
# shared-factor inheritance, K/M endpoints, %-as-decimal). The full audit reports
# candidates for human adjudication (house-style range padding, elapsed-window
# weeks, hidden context factors are accepted classes); --guard is the strict
# zero-false-positive subset this check enforces: single-run effort-time product
# chains whose midpoint is off ≥1.6× under NO licensed convention, plus reversed
# numeric ranges. The 2026-08-29 pass adjudicated the complete hit list and
# repaired 25 workflows' arithmetic against their own steps/Frequency/Volume.
C50_OUT=$(python3 "$REPO_ROOT/07-methodology/audit-time-estimate-math.py" --guard 2>&1) && C50_RC=0 || C50_RC=$?
echo "$C50_OUT" | grep -E "^Guard:" | sed 's/^/    /'
if [ $C50_RC -eq 0 ]; then
    ok "No inline-arithmetic guard violations in Time Estimate / Staffing Implication sections (guard mode of audit-time-estimate-math.py; 25 defective chains repaired 2026-08-29)"
else
    C50_N=$(echo "$C50_OUT" | grep -c "^GUARD VIOLATION" || true)
    error "$C50_N inline-arithmetic guard violation(s) in Time Estimate / Staffing Implication sections (run 07-methodology/audit-time-estimate-math.py for the full audit trail):"
    echo "$C50_OUT" | grep -A1 "^GUARD VIOLATION" | sed 's/^/    /' | head -40
fi

# --- Check 51: headcount-anchor & Volume-product reconciliation ---
echo "--- Check 51: Staffing-claim & Volume-product reconciliation ---"
# reconcile-staffing-claims.py (2026-08-29, consistency review #34) reconciles the
# staffing-team / role-count claims in PA prose against the canonical registers
# (model-company-profile.md §3.3 eighteen-department 511-HQ register — the
# promoted structure of record, 2026-09-14; §4 store/DC/total figures; §13.1
# Merchandising 43 breakdown) and verifies every explicit A × B = C product in
# Volume/Frequency field rows (elementwise, K/M endpoints, week→month cadence
# allowance). Guards: (a) the retired literals from the review's repaired spots
# (pre-rebalance dept totals IT 28→50, Finance 37→46, Legal 9→14, Store Ops
# 23→24; stale role counts 3→4 Pricing Analysts, 10–12→10 Buyers, 6→5 Category
# Managers; the per-shift DC worker phrasing vs the canonical 4 × 150 = 600; the
# DSD per-store week→month cadence) plus — since the 2026-09-14 twenty-ninth-wave
# review — the pre-promotion HQ-subtotal family the promotion's 6,762-total sweep
# stranded (the '362 HQ' forms, the old §3.3 six-function enumeration, the
# 5-person trade register; PA files + a literal-only pass over the VS READMEs);
# (b) any '<Department> … team of N' claim must equal the §3.3 total (engagement
# crews 'team of 2–3'/'deploys a team of 2' exempt); (c) Volume-row products must
# compute ('+'-sum rows and cadence conversions out of scope).
C51_OUT=$(python3 "$REPO_ROOT/07-methodology/reconcile-staffing-claims.py" --guard 2>&1) && C51_RC=0 || C51_RC=$?
C51_N=$(echo -n "$C51_OUT" | tail -1)
echo "    $C51_N"
if [ $C51_RC -eq 0 ]; then
    ok "No stale headcount literals, dept-team mismatches, Volume-product defects, or DC-catchment drift (guard mode of reconcile-staffing-claims.py, --guard armed by the 2026-09-09 sixteenth-wave review after two latent checker false positives were found printing under the unarmed run; 21 claim spots + 3 Volume rows repaired 2026-08-29; DC-catchment average/range claims re-derived from the profile's §3.1/§3.2 tables and the retired 20–60-range / ~40-average / ~40–50 forms retired by the sixteenth wave; the register re-based to the promoted 511-HQ §3.3 and the pre-promotion 362-HQ-subtotal family — the '362 HQ' forms, the old six-function enumeration, the 5-person trade register — retired across PA files + VS READMEs by the 2026-09-14 twenty-ninth-wave review, the stragglers the promotion's 6,762-total sweep left behind)"
else
    C51_HITS=$(echo "$C51_OUT" | grep -cE "^(retired-literal|dept-team|volume-product|dc-catchment):" || true)
    error "$C51_HITS staffing-claim/Volume-product/DC-catchment violation(s) (run 07-methodology/reconcile-staffing-claims.py for detail):"
    echo "$C51_OUT" | grep -E "^(retired-literal|dept-team|volume-product|dc-catchment):" | sed 's/^/    /' | head -30
fi

# --- Check 52: System-Touchpoints vocabulary & Trigger-duplication guard ---
echo "--- Check 52: ST vocabulary & duplicate-Trigger guard ---"
# audit-st-touchpoints.py (2026-08-29, consistency review #35) audited the
# System Touchpoints module-name vocabulary (15,988 bullets spell-clean; the 36
# canonical touchpoint-map modules are families whose PA subsystem names
# cohere) and every same-PA byte-identical Trigger pair (20 clusters, all
# adjudicated legitimate shared-event/shared-cadence program triggers —
# parallel M&A diligence streams, annual-audit-plan children, month-close
# siblings, typhoon-signal preparedness streams — allowlisted). The review
# normalized eight rogue spelling/hyphenation variants to the dominant house
# forms (ageing→aging incl. the W995 title/TOC/register cascade; drilldown→
# drill-down; pick-up→pickup; put-away→putaway; time-stamp(ed)→timestamp(ed);
# charge-back(s)→chargeback(s); anti-counterfeiting→anti-counterfeit;
# self-serve→self-service) while deliberately preserving title-canonical forms
# (W258 Omni-channel, W1238/W1491 Material Take-Off, W3657 Closeout, the
# paired check-in/check-out noun).
C52_OUT=$(python3 "$REPO_ROOT/07-methodology/audit-st-touchpoints.py" --guard 2>&1) && C52_RC=0 || C52_RC=$?
C52_N=$(echo -n "$C52_OUT" | tail -1)
echo "    $C52_N"
if [ $C52_RC -eq 0 ]; then
    ok "No retired ST-vocabulary literals and no unallowlisted same-PA duplicate Triggers (guard mode of audit-st-touchpoints.py; ~35 variant spots normalized and 20 trigger clusters adjudicated 2026-08-29)"
else
    C52_HITS=$(echo "$C52_OUT" | grep -cE "^(retired-literal|duplicate-trigger):" || true)
    error "$C52_HITS ST-vocabulary/duplicate-Trigger violation(s) (run 07-methodology/audit-st-touchpoints.py for detail):"
    echo "$C52_OUT" | grep -E "^(retired-literal|duplicate-trigger):" | sed 's/^/    /' | head -30
fi

# --- Check 53: Automation-keyword & RACI role-title guard ---
echo "--- Check 53: Automation-keyword & RACI role-title guard ---"
# fix-auto-keywords.py --check (2026-08-29, consistency review #36) guards the two
# surfaces beyond Check 21's draft-marker scope: (a) the defragmented Automation
# Opportunity bullets' quoted keywords — the review repaired the extractor's glitch
# classes (mid-word clips like 'logy' re-quoted from their own step's full word,
# legal-entity captures like "Logistics Inc." re-quoted with the step's true object,
# trailing-space/punctuation fragments trimmed or extracted from nested quotes, and
# case-variant keywords lowercased) across ~250 bullets in 183 PA files; (b) the RACI
# role-title vocabulary in Steps tables — 124 cell-bounded normalizations to the
# dominant forms (plurals, abbreviation variants like Gov Affairs → Govt Affairs,
# OHS Officer → HSE Officer, External Adviser → External Advisor, and the org-chart
# ghost 'VP Communications' → Marketing Comms Manager, which §11.1 does not list);
# legitimately distinct look-alikes (Site Manager in VS-141, Property AR Manager in
# VS-97, Sourcing Manager, customer's site representative) were adjudicated and kept.
C53_OUT=$(python3 "$REPO_ROOT/07-methodology/fix-auto-keywords.py" --check 2>&1) && C53_RC=0 || C53_RC=$?
C53_N=$(echo -n "$C53_OUT" | tail -1)
echo "    $C53_N"
if [ $C53_RC -eq 0 ]; then
    ok "No glitched Automation keywords and no cell-bounded RACI role-title variants (guard mode of fix-auto-keywords.py; ~250 keyword repairs + 124 role normalizations on 2026-08-29)"
else
    C53_HITS=$(echo "$C53_OUT" | grep -cE "^(retired-keyword|glitched-keyword|role-variant):" || true)
    error "$C53_HITS Automation-keyword/RACI-role violation(s) (run 07-methodology/fix-auto-keywords.py for detail):"
    echo "$C53_OUT" | grep -E "^(retired-keyword|glitched-keyword|role-variant):" | sed 's/^/    /' | head -30
fi

# --- Check 54: risk-label / cadence / owner vocabulary guard ---
echo "--- Check 54: Pain-Points, Frequency & Owner vocabulary ---"
# audit-field-vocabulary.py (2026-08-29, consistency review #37) guards the three
# field vocabularies beyond Checks 14/15: (a) the Pain Points risk taxonomy — the
# 4,836-label vocabulary is domain-specific and clean; thirteen variant labels
# normalized (Blindspot → Blind-spot, Cannibalisation → Cannibalization, the
# hybrid Cannibalization-miss → Missed-cannibalization, Cost-leak → Cost-leakage,
# Metrics-gaming → Metric-gaming, Operations → Operational, Re-occurrence →
# Recurrence, Record-gap → Records-gap, Reputation → Reputational, unhyphenated
# "Scope creep risk", and three capitalized Risk tails → lowercase), with genuinely
# distinct concepts kept (Capability- vs Capacity-shortfall, Hidden-PL-cost,
# Reputational/ESG, Tax-mis-classification); (b) the Frequency cadence vocabulary —
# spell-clean, 17 unhyphenated 'ad hoc' → 'ad-hoc' (dominant 320x); (c) the Owner
# vocabulary vs the profile — HSE spelling enforced (EHS Manager → HSE Manager),
# PA-07.1 store-opening rows aligned to Compliance Officer in cell and prose; the
# bare 'Compliance Manager' adjudicated a plausible Legal & Compliance title and
# kept, as are the qualified Product/EPR/Trade/Tax/HR Compliance Manager roles.
C54_OUT=$(python3 "$REPO_ROOT/07-methodology/audit-field-vocabulary.py" --guard 2>&1) && C54_RC=0 || C54_RC=$?
C54_N=$(echo -n "$C54_OUT" | tail -1)
echo "    $C54_N"
if [ $C54_RC -eq 0 ]; then
    ok "No retired risk-label/cadence/owner vocabulary literals (guard mode of audit-field-vocabulary.py; 13 risk labels + 18 cadence spots + 3 owner spots normalized 2026-08-29)"
else
    C54_HITS=$(echo "$C54_OUT" | grep -cE "^(retired-literal|cadence-variant):" || true)
    error "$C54_HITS vocabulary violation(s) (run 07-methodology/audit-field-vocabulary.py for detail):"
    echo "$C54_OUT" | grep -E "^(retired-literal|cadence-variant):" | sed 's/^/    /' | head -30
fi

# --- Check 55: Participants hygiene & per-unit volume coherence ---
echo "--- Check 55: Participants hygiene & per-unit volume coherence ---"
# audit-participants-units.py (2026-08-29, consistency review #38) guards the three
# surfaces of that review: (a) the data-volumes §1.1 anchors vs PA Volume/Frequency
# at scale — agreement verified clean (subset/per-store figures and the W867 portal
# share of W7's merchandise invoices all cohere); the single defect repaired was
# W3's per-DC arithmetic (6,000 ÷ 4 = 1,500/DC, not ~1,200); the same-row per-unit
# coherence guard below is its generalization (units × per-unit within ±30% of the
# stated chain-wide total); (b) Participants hygiene — 35 rows carried stray RACI
# markers duplicating the Steps tables (stripped to the plain-name convention of the
# other 5,350 rows) and the 'Analytics Mgr' abbreviation was unified to 'Analytics
# Manager' (68 spots incl. VS READMEs); (c) steps-table Duration unit vocabulary —
# spell-clean (min/hours/days/weeks dominant; hrs/minutes/sec established variety;
# apparent 'hors'/'das' hits were substrings of Authors/horsepower/anchors).
C55_OUT=$(python3 "$REPO_ROOT/07-methodology/audit-participants-units.py" --guard 2>&1) && C55_RC=0 || C55_RC=$?
C55_N=$(echo -n "$C55_OUT" | tail -1)
echo "    $C55_N"
if [ $C55_RC -eq 0 ]; then
    ok "No RACI-marked Participants rows, no 'Analytics Mgr' abbreviation, and per-unit volume rows cohere with their chain-wide totals (guard mode of audit-participants-units.py; W3 per-DC arithmetic + 35 marker rows + 68 Mgr spots repaired 2026-08-29)"
else
    C55_HITS=$(echo "$C55_OUT" | grep -cE "^(raci-marker|retired-literal|per-unit-coherence):" || true)
    error "$C55_HITS Participants/per-unit violation(s) (run 07-methodology/audit-participants-units.py for detail):"
    echo "$C55_OUT" | grep -E "^(raci-marker|retired-literal|per-unit-coherence):" | sed 's/^/    /' | head -30
fi

# --- Check 56: operational-control prose variant guard ---
echo "--- Check 56: Operational-control prose variants ---"
# audit-operational-controls.py (2026-08-29, consistency review #39) guards the
# Controls-section 'operational:' prose vocabulary beyond Check 21's boilerplate
# strings: the review normalized ~20 variant spots (hyphenated
# 'review-and-approval gate', 'review & approval', 'review and approvals',
# 'VP for Merchandising/Store Operations', the '(CSR)' gloss and '(HQ)'
# qualifiers inside gate sentences) to the dominant '<Role> review and approval
# gate' template; role look-alikes in the near-miss tail are distinct roles and
# the 'Marketing — <role>' department-scoped composites are kept. The same
# review verified the ST module-family naming against the 36-module register
# (clean — the hyphenated hits are correct compound modifiers) and the VS-x
# citation density (44,041 citations across all 569 PAs, median 57, none
# isolated).
C56_OUT=$(python3 "$REPO_ROOT/07-methodology/audit-operational-controls.py" --guard 2>&1) && C56_RC=0 || C56_RC=$?
C56_N=$(echo -n "$C56_OUT" | tail -1)
echo "    $C56_N"
if [ $C56_RC -eq 0 ]; then
    ok "No retired operational-prose variant literals (guard mode of audit-operational-controls.py; ~20 gate-sentence variants normalized 2026-08-29)"
else
    C56_HITS=$(echo "$C56_OUT" | grep -c "^retired-literal:" || true)
    error "$C56_HITS operational-prose violation(s) (run 07-methodology/audit-operational-controls.py for detail):"
    echo "$C56_OUT" | grep "^retired-literal:" | sed 's/^/    /' | head -30
fi

# --- Check 57: risk-label punctuation guard ---
echo "--- Check 57: Risk-label punctuation ---"
# audit-risk-labels.py (2026-08-29, consistency review #40) guards the Pain-Points
# risk-label structure: 50 labels used the em-dash form '**X risk** — description'
# instead of the colon form used by the 6,800+ majority and the format guide's
# example; normalized. The same review quantified the enrichment backlogs it did
# NOT fabricate content for: 265 of 7,066 risk bullets (3.7%) state the risk
# without a mitigation clause (their mitigations live in the workflow's Controls
# sections), and 85 Trigger values outside the Check-52 allowlist are ultra-short
# cadence phrases — both documented for per-workflow review. The format guide's
# example anchors were verified against current state (W2599, VS-88, and the
# ~72,000 receipts/yr figure matching the canonical DC-only volume).
C57_OUT=$(python3 "$REPO_ROOT/07-methodology/audit-risk-labels.py" --guard 2>&1) && C57_RC=0 || C57_RC=$?
C57_N=$(echo -n "$C57_OUT" | tail -1)
echo "    $C57_N"
if [ $C57_RC -eq 0 ]; then
    ok "No em-dash risk labels (guard mode of audit-risk-labels.py; 50 labels converted to the colon form 2026-08-29)"
else
    C57_HITS=$(echo "$C57_OUT" | grep -c "^em-dash-risk-label:" || true)
    error "$C57_HITS em-dash risk label(s) (run 07-methodology/audit-risk-labels.py for detail):"
    echo "$C57_OUT" | grep "^em-dash-risk-label:" | sed 's/^/    /' | head -30
fi

# --- Check 58: mitigation-clause & Trigger-richness completeness ---
echo "--- Check 58: Mitigation-clause & Trigger-richness completeness ---"
# audit-enrichment-completeness.py (2026-08-29 enrichment pass) closes the two
# backlogs quantified by consistency review #40: (a) the 231 risk bullets that
# stated a risk without mitigation semantics now carry 'mitigated by …' clauses
# affinity-matched from their OWN workflow's Controls section (operational gates
# where they fit, else the PA-level CTL-XXX execution control — nothing cited
# that is not in that workflow's Controls); (b) the 38 cadence-only Trigger
# values outside the Check-52 allowlist are enriched with their workflow's own
# title subject ('Monthly analytics cycle — Sales Per Square Meter'). The
# remaining short triggers ('Breach confirmed', 'Retention expiry'…) were
# adjudicated already-specific event names.
C58_OUT=$(python3 "$REPO_ROOT/07-methodology/audit-enrichment-completeness.py" --guard 2>&1) && C58_RC=0 || C58_RC=$?
C58_N=$(echo -n "$C58_OUT" | tail -1)
echo "    $C58_N"
if [ $C58_RC -eq 0 ]; then
    ok "Every risk bullet carries mitigation content and no cadence-only Triggers remain outside the shared-event allowlist (231 mitigation clauses + 38 Trigger subjects enriched 2026-08-29)"
else
    C58_HITS=$(echo "$C58_OUT" | grep -cE "^(bare-mitigation|cadence-only-trigger):" || true)
    error "$C58_HITS enrichment-completeness violation(s) (run 07-methodology/audit-enrichment-completeness.py for detail):"
    echo "$C58_OUT" | grep -E "^(bare-mitigation|cadence-only-trigger):" | sed 's/^/    /' | head -30
fi

# --- Check 59: root-level model-company document integrity ---
echo "--- Check 59: Model-doc figures & cross-references ---"
# audit-model-docs.py (2026-08-29, consistency review #41) audits the root-level
# model-company documents against the canonical registers: every W/VS-/CTL-/PA-/
# requirement-ID token must resolve
# against the live registers (5,363 W / 190 VS / 569 PA / 808 CTL / 728 req),
# §-refs must resolve doc-scoped (profile / named target doc / the document's
# own sections; change-note footers exempt), and the retired stale totals
# (6,757 / 6,715 / 5,3xx / 80,000-SKU / 1,000-terminal) must not appear.
# Consistency review #68 (2026-09-02) extended the doc set from the three
# secondary root docs (mobile-app-strategy.md, data-migration-mapping.md,
# assumptions-and-design-decisions.md) to also cover the two organizational
# documents issued 2026-09-01/02 — optimal-table-of-organization.md and
# 07-methodology/it-product-operating-model.md — which had shipped with zero
# validator coverage; the review found and repaired three figure/citation
# defects between them (TO §7.3 'Outbound (51)' vs role-sum 50; IT-model
# '~11 external integration clusters' vs the canonical ten; a §13.3-for-§13.2
# seasonal-calendar §-ref) plus an unresolvable §2.4 self-reference, and added
# doc-scoped retired literals, required corrected anchors (the 171+17=188 /
# 4,864+499=5,363 reconciliation sums, the two-state 469/6,869 totals), and a
# structural rule re-deriving every §7.3 DC-roster group total from its own HC
# cells — so this check is the permanent regression guard.
C59_OUT=$(python3 "$REPO_ROOT/07-methodology/audit-model-docs.py" --guard 2>&1) && C59_RC=0 || C59_RC=$?
C59_N=$(echo -n "$C59_OUT" | tail -1)
echo "    $C59_N"
if [ $C59_RC -eq 0 ]; then
    ok "All model-doc tokens resolve, §-refs resolve doc-scoped, and no retired figures appear (guard mode of audit-model-docs.py, now 16 docs incl. the whole 02-oracle-ebs platform-blueprint folder; 3 secondary docs verified clean 2026-08-29; TO + IT operating model brought under the guard and verified clean 2026-09-02, review #68; sourcing model + technical guidelines brought under the guard with §12.1 tier-count and TO §11 phase-sum structural rules, 2026-09-03 post-AAP pass; methodology-index version pins and the two-state TO-anchor description pinned to the live docs, 2026-09-03 index-trueness pass; the OM 'Downstream:' pointer, the reality-check STATUS banner pins, and the executive-summary top-footer counts pinned to the live docs/registers, 2026-09-03 description-trueness pass; every register '(n Workflows)' heading claim and the Summary per-phase counts re-derived from the register's own rows via register_heading_hits, 2026-09-03 consistency review pass; the AI-first operating guide brought under the guard — verified clean on dry-run — with a guide_figure_hits structural rule re-deriving its catalog triple, Tier-ladder sentence and control/requirement canon-table citations from the primary registers, 2026-09-04 guard-extension pass; the OM reconciliation surfaces (§3.2 portfolio-table cross-foot, §4.9 Total row, live footer split) brought under the om_reconciliation_hits structural rule re-derived from the index Grand Total — 2026-09-05 sixth-wave review, after the batch-23 pass stranded the §4.9 Total row behind a self-satisfying stale ANCHOR; data-volumes-and-integrations.md brought under the guard with the dv_volume_hits §1.1/§1.2 arithmetic rule re-deriving every peak cell and the storage sums, the exec-summary Repository-Structure tree pinned to the on-disk top level (the bpmn/ + dmn/ rows the tree predated are now stated), and the reality-check §3.1 AP parenthetical repaired ~450/day → ~300/day — 2026-09-07 eighth-wave review; the reverse-direction companion-pin family (the sourcing model's header 'Companion to' OM pin stranded at v3.3 by the batch-20 cascade that re-pointed only its §13 sibling, the §13 OM row frozen at v3.4, the sourcing footer companion-pin chain broken by the sixth-wave OM v3.8 bump — sourcing bumped to v2.8 with its own re-point clause — and the OM §13 'this vN.M model' self-pin still at the 2026-09-03 v2.4) all re-pointed to the live footers and pinned every run by the new companion_pin_hits rule — 2026-09-07 ninth-wave review; the tenth-wave review adjudicated the sixth wave's flagged VS-151 residual (the §4.9 SSP row's enumeration claimed VS-151 while its 882 figure excluded it and DP's 213 included it — a mismatch traced to the v1.0 issuance itself) in favor of the unanimous mapping side — SSP 906 / DP 189 — and exposed the hand-maintained subtotal split ±3 off its own member rows (4,913 + 513 declared vs 4,910 + 516 derived), re-based to 4,934 + 492 with the OM bumped to v3.9 and the sourcing companion chain re-pointed (v2.9); om_reconciliation_hits extended to re-derive every §3.2 per-team cell, both subtotal cells and every §4.9 per-team workflow cell from the §4.1–4.8 mapping tables and the on-disk `##` headers each run — 2026-09-07 tenth-wave review; the 2026-09-09 thirteenth-wave review trued the v2.0 TO register issuance (the footer's '≈150 distinct roles' → the register's true 188 rows / 187 distinct titles; the §5.3 span note's 'Controller at 7 directs' → 7 sub-team lines / 8 register reporting rows in-band; the §5.2 GL & Consolidation mix cell conformed to its register rows — the same conformance class the v2.0 pass itself had applied to Store Operations and AR & Credit) and closed the guard gap with to_register_hits — §5.1's 18-department current/target columns and two-state total rows, the three §5.2 sub-team tables, every §5.3 department-table HC foot, the §5.1↔§5.3 per-department pairing, the register-total footer line, the quoted distinct-role-title count and the span-note Controller row-count re-derived every run); and the 2026-09-09 sixteenth-wave review trued three stranded-derived-figure classes — all 'the canonical table moved, the derived quote stayed' — and closed them with profile_derived_figure_hits (the revenue-per-employee quotient 9.22M → 9.21M on the profile §4 note, assumptions A2.6 and PA-133.3's Volume row after the v2.22 rebalance bumped the division's denominator 6,757 → 6,762 without re-deriving the quotient — the profile's own parenthetical division contradicted its quotient, and this module's #41 self-description had verified the stale figure; the §15.2 Master-Data trade-customer row 5,000 → 5,200 and PA-11.2's live '(5,000 accounts, ~30% of revenue)' → ~5,200 after the v2.23 canonicalization moved §9.2/§10.3 to 5,200/5,400; the rule re-derives the quotient and the account counts from the §9.4/§4/§9.2 rows, cross-foots §10.3 and §15.2 to them, and sweeps the live corpus — PA files, workflows support docs, root/methodology docs; CHANGELOG, generated trees, footers and the gap-analysis scenario table's authoring-time rows exempt — for disagreeing citations); and the 2026-09-14 nineteenth-wave review brought the whole 02-oracle-ebs platform-blueprint folder (7 documents, zero validator coverage since its same-day issues) under the guard — repairing six invented family names and two missing touchpoint-map module rows in the coverage map, the stale ASCP/Demantra 'evaluation' wording, the ~17,000-ecommerce subset-as-total NFR figure, an 'RPO/RPO' typo, the fit-gap Reading note's 6/4 BUILD-split inversion, the stale 4-component LOC budget row, the retired 'PAY-PH pack' wording, and a non-canonical CTL-1 citation — and closed the gap with ebs_blueprint_hits (fit-gap §2 register class counts re-derived onto the §3 table + intro + Reading-note split, the touchpoint-map module set and the canonical family names/counts mirrored one-for-one, the §7 ecommerce total re-derived from the profile canon, the README wave prose pinned to the classification tier ladder), with W0 exempted as a wave label and the sourcing-model + blueprint sections joining the §-resolution union; and the 2026-09-14 twenty-first-wave review closed the doctrine cascade's canonical-integration strand — the two-tier doctrine's Payroll PH → GL posting flow (fit-gap E8 INT) had never reached data-volumes §3's canonical Integration Detail Matrix, the EBS pattern register's Flow column claimed to 'quote the canonical matrix rows' while the gateway chargeback/fee row had no canonical counterpart and TWO canonical rows (Delivery Partners → ERP delivery status; Supplier Portal → ERP ASN/invoices) were silently folded into their outbound siblings, and the legacy mapping template still routed payroll YTD into the ERP against data-migration row 11 — repaired (canonical matrix row 20 + the statutory target named in full; the register's endpoints re-pointed verbatim with both folded rows split out and the chargeback row declared the register's single extension; the mapping template's §1 scope row and §2.4 YTD row re-pointed to the build) with integration_mirror_hits (the §3 matrix re-derived every run with the Payroll PH posting row required, the register's Flow sequence required equal to the canonical sequence after the one declared extension, endpoints verbatim) and migration_template_hits (corrected anchors required, the retired YTD-into-EBS routing forbidden, the 02 row-11 anchor required) inside this check); and the 2026-09-14 twenty-ninth-wave review closed the uncommitted structure-promotion session's own residue: the promotion re-based §3.3/§4/§11.1 but stranded the profile's three remaining live employee-count rows on the retired 6,762 (§11.2 Payroll-Parameters 'Total Employees', §15.2 Master-Data 'Employees', the §17 user-adoption bullet — §15.2's account rows were already cross-footed here, so the employees rows joined them, re-derived from the §4 canon every run), the same session left the OM header 'Companion to' sourcing-model pin at v3.1 when the same-day sourcing bump moved the footer to v3.2 (the ninth-wave rule pinned the sourcing→OM direction only — companion_pin_hits gains the mirror OM→sourcing arm, matched on the link-followed-by-(vN.M) form unique to the wrapped header), and the promotion's corpus sweep (which matched the ~6,762 total) never matched the HQ-subtotal family — PA-22.1's whole HQ-Departments table reconciled to the retired 362 while citing profile §3.3 as live, plus PA-72.3/PA-138.2/PA-19.3 Volume rows, PA-34.1's two laptop-refresh cells, PA-40.2's allocation step, PA-13.1's 362/5-person-trade-register note and VS-169's README intro parenthetical — all re-cut to the promoted 511 register, with the 362-class literals joining reconcile-staffing-claims' retired list (Check 51) and the CHANGELOG's own entry-letter collision (three prepended entries reusing committed letters (j)/(k)/(l)) joining Check 72; and the 2026-09-15 thirty-fifth-wave review pinned the fit-gap §7 standard-first KPI row's '(current N%)' figure to the register re-derivation — the 2026-09-15 EBS-maximization audit trued the §3 total row and the intro headline to 59/83 = 71.1% but stranded the KPI table at the retired 68.4% against its own 'This register, re-run per wave' enforcement cell, so the KPI figure now re-derives with the class counts every run"
else
    C59_HITS=$(echo "$C59_OUT" | grep -c "^model-doc:" || true)
    error "$C59_HITS model-doc violation(s) (run 07-methodology/audit-model-docs.py for detail):"
    echo "$C59_OUT" | grep "^model-doc:" | sed 's/^/    /' | head -30
fi

# --- Check 60: executive-summary anchors & CTL citation scope ---
echo "--- Check 60: Exec-summary anchors & CTL citation scope ---"
# audit-exec-ctl.py (2026-08-29, consistency review #42) guards the two surfaces
# of that review: (a) executive-summary.md's narrative claims — every anchor
# verified against the registers (6,762 employees, 35,000 SKUs, 200 stores, 4 DCs
# at Davao/Cebu/Laguna/Clark, 600 terminals, 2.8M transactions/month, PHP 62.3B,
# ~600,000 loyalty members, offline >= 8h, 300+ store scalability, 99.9% POS
# uptime, <= 5-working-day close, 728/5,363/188/6,762 footer counts) and retired
# totals must not appear outside change-notes; (b) the CTL register's citation
# scope — the 33 stretched spend-control citations (CTL-01 'Prevent unauthorized
# purchases' / CTL-02 '...capital expenditure' cited for non-spend governance
# notes like 'IR governance'/'exercise governance' in VS-184–191) were re-pointed
# to each workflow's own PA-level execution control in the Check-34 canonical
# form with the note preserved; spend-related notes remain on the spend controls.
C60_OUT=$(python3 "$REPO_ROOT/07-methodology/audit-exec-ctl.py" --guard 2>&1) && C60_RC=0 || C60_RC=$?
C60_N=$(echo -n "$C60_OUT" | tail -1)
echo "    $C60_N"
if [ $C60_RC -eq 0 ]; then
    ok "Executive-summary anchors agree with the registers and CTL-01/02 citations carry spend-scoped notes (33 stretched citations re-pointed 2026-08-29)"
else
    C60_HITS=$(echo "$C60_OUT" | grep -cE "^(exec-anchor|spend-ctl-scope):" || true)
    error "$C60_HITS exec-summary/CTL-scope violation(s) (run 07-methodology/audit-exec-ctl.py for detail):"
    echo "$C60_OUT" | grep -E "^(exec-anchor|spend-ctl-scope):" | sed 's/^/    /' | head -30
fi

# --- Check 61: matrix ghost-only rows, gap-analysis & tech-guidelines anchors ---
echo "--- Check 61: Matrix rows, gap-analysis & tech-guidelines anchors ---"
# audit-matrix-refs.py (2026-08-29, consistency review #43) guards the three
# surfaces of that review: (a) requirement-workflow-matrix.md — the letter-
# suffixed aliases (W5B, W9A, W2A… ~1,400 prose mentions) are the sanctioned
# POS-family shorthand, but no requirement row may map ONLY to ghost aliases;
# the 8 such rows found (POS-004/011/012/017/018, RPT-007, NFR-003, NFR-015)
# were re-pointed to the real workflows that exercise each requirement (W5,
# W463, W520, W528, W1282/W1485, W1425, W9, W14); (b) workflow-gap-analysis.md
# current-state line must quote the canonical 188/569/5,363 totals (per-pass
# historical totals exempt); (c) technical-guidelines.md must carry its verified
# anchor figures (~511 HQ staff ≈460 concurrent users, ~640 Mbps aggregate, >= 8h
# offline, 933 peak-day/store, 10-year retention — re-pointed by the 2026-09-14
# structure-promotion re-base).
C61_OUT=$(python3 "$REPO_ROOT/07-methodology/audit-matrix-refs.py" --guard 2>&1) && C61_RC=0 || C61_RC=$?
C61_N=$(echo -n "$C61_OUT" | tail -1)
echo "    $C61_N"
if [ $C61_RC -eq 0 ]; then
    ok "No ghost-only matrix rows; gap-analysis and technical-guidelines carry their canonical anchor figures (8 rows re-pointed 2026-08-29)"
else
    C61_HITS=$(echo "$C61_OUT" | grep -cE "^(ghost-only-row|gap-analysis-current-state|tg-anchor):" || true)
    error "$C61_HITS matrix/gap-analysis/tech-guidelines violation(s) (run 07-methodology/audit-matrix-refs.py for detail):"
    echo "$C61_OUT" | grep -E "^(ghost-only-row|gap-analysis-current-state|tg-anchor):" | sed 's/^/    /' | head -30
fi

# --- Check 62: semantic-sample anchor guard ---
echo "--- Check 62: Semantic-sample anchors ---"
# audit-semantic-anchors.py (2026-08-29, consistency review #44) guards the defects
# found by the bounded semantic-correctness sample: 40 workflows stratified 5-per-
# family across the 8 VS families (seed 44) audited in full — step logic, Duration
# plausibility, RACI feasibility, statutory statements — plus a 24-workflow
# statutory-heavy second batch (0 defects). 36+24 of 64 verified sound including
# every statutory base (DOLE 174, RA 4136, DENR CCO 2013-24, TRAIN, PFRS 15,
# BIR 2307 netting, RA 10173) and the volume chains. Four defects repaired:
# W264's stale Participants counts (6/8 -> 5/10 per section 13.1), W1777's
# in-house-interest VAT basis ('as a financial service' -> part of gross selling
# price; financial-service interest is NIRC-exempt), W253's impossible ~10,000
# loyalty enrollments/month vs the section 1.1 ~4,500/month anchor, and W449's
# mis-pasted operational-control line. The guard retires those literals and
# enforces register-equal Participants counts for the section 13.1 merchandising
# roles (CM 5, Buyers 10, Planners 5, Pricing Analysts 4) repo-wide.
# Review #50 (2026-08-29) extended it with the general keyword-quote integrity
# rules: every 'System ... of "QUOTE" (replaces manual Step N)' bullet must
# quote text that appears in the referenced step (containment) and at a word
# boundary (no mid-word clips) — repairing 884 clips (account/discount->count,
# profile->file, catalog->log, center->enter, analogous->logous, ...) and the
# 50 review #45/#47 '-logy' mis-repairs ('technology' where the step word was
# Metrology/methodology/typology/toxicology/genealogy/apology); 12 adjudicated
# noun-phrase summary bullets are allowlisted.
C62_OUT=$(python3 "$REPO_ROOT/07-methodology/audit-semantic-anchors.py" --guard 2>&1) && C62_RC=0 || C62_RC=$?
C62_N=$(echo -n "$C62_OUT" | tail -1)
echo "    $C62_N"
if [ $C62_RC -eq 0 ]; then
    ok "No retired semantic literals, register-equal Participants counts, and every step-quoting automation bullet passes containment + word-boundary (guard mode of audit-semantic-anchors.py; 64-workflow sample + review #50 quote-integrity sweep repaired 2026-08-29)"
else
    C62_HITS=$(echo "$C62_OUT" | grep -cE "^(retired-literal|participant-count|quote-integrity):" || true)
    error "$C62_HITS semantic-anchor violation(s) (run 07-methodology/audit-semantic-anchors.py for detail):"
    echo "$C62_OUT" | grep -E "^(retired-literal|participant-count|quote-integrity):" | sed 's/^/    /' | head -30
fi

# --- Check 63: Root-README worklist-row & methodology-tree guard ---
echo "--- Check 63: Root-README worklist rows & methodology-tree completeness ---"
# Consistency review #69 (2026-09-02) found a defect class no prior check could
# see: the root-README folder tree's PROSE rows for the 07-methodology worklists
# had drifted — the batch17 row still advertised 'residual: W712 phrasing,
# W16.1 approval-matrix design' although review #64 had already consolidated the
# W16.1 four-matrix conflict on W24's canonical ladder (W886/W1245 re-pointed)
# and the W712 quote was never locatable (current PA-17.3 text verified correct:
# 25% attaches to the surcharge per NIRC 248, compromise penalty listed
# separately). Check 44 guards the tree's per-VS counts/figures and the
# proposed-register description row, but no check guarded worklist prose or
# methodology-tree completeness. This check (a) retires the stale batch17-
# residual literal, (b) requires the batch17 row to carry the review-#64 closure
# anchor and to quote the worklist file's own '~N of ~M repaired' figures,
# (c) requires the batch18 row's '(~N spots' residual count to equal the
# 'residual ~N' figure in batch18-deferred-candidates.txt's header, and
# (d) requires every file in 07-methodology/ (pycache excluded) to appear in
# the root-README folder tree, so future worklists/scripts cannot ship
# unlisted.
C63_OUT=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
bad = []
readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
meth = os.path.join(ROOT, "07-methodology")
b17 = open(os.path.join(meth, "batch17-deferred-candidates.txt"), encoding="utf-8").read()
b18 = open(os.path.join(meth, "batch18-deferred-candidates.txt"), encoding="utf-8").read()

# (a) retired stale literal (repaired by review #69)
if "residual: W712 phrasing, W16.1 approval-matrix design" in readme:
    bad.append("retired-literal: stale batch17 residual form 'residual: W712 phrasing, W16.1 approval-matrix design' in README.md (both residuals closed by/until review #64)")

# (b) batch17 closure anchor + repaired-figures agreement with the worklist file
if "W24's canonical ladder in review #64" not in readme:
    bad.append("batch17-anchor: README tree must carry the review-#64 closure marker \"W24's canonical ladder in review #64\"")
m17 = re.search(r"~(\d+) of (?:the )?~(\d+) listed spots repaired", b17)
r17 = re.search(r"batch17-deferred-candidates\.txt.*?~(\d+) of ~(\d+) spots", readme, re.S)
if m17 and r17:
    if (r17.group(1), r17.group(2)) != (m17.group(1), m17.group(2)):
        bad.append("batch17-figures: README tree quotes ~%s of ~%s spots but the worklist says ~%s of ~%s" % (r17.group(1), r17.group(2), m17.group(1), m17.group(2)))
else:
    bad.append("batch17-figures: README tree batch17 row missing '~N of ~M spots repaired' agreement with the worklist file")

# (c) batch18 residual-count agreement with the worklist header
m18 = re.search(r"residual ~(\d+)", b18)
r18 = re.search(r"batch18-deferred-candidates\.txt.*?\(~(\d+) spots", readme, re.S)
if m18 and r18:
    if r18.group(1) != m18.group(1):
        bad.append("batch18-figures: README tree quotes ~%s spots but the worklist header says residual ~%s" % (r18.group(1), m18.group(1)))
else:
    bad.append("batch18-figures: README tree batch18 row missing '(~N spots' residual count")

# (d) methodology-tree completeness: every 07-methodology file listed in the root README
for name in sorted(os.listdir(meth)):
    if name == "__pycache__" or not os.path.isfile(os.path.join(meth, name)):
        continue
    if name not in readme:
        bad.append("tree-completeness: 07-methodology/%s not listed in the root-README folder tree" % name)
print("HITS %d" % len(bad))
for b in bad:
    print("BAD|" + b)
PY
)
C63_BAD=$(echo "$C63_OUT" | sed -n 's/^HITS \([0-9]*\)/\1/p')
if [ "${C63_BAD:-1}" -eq 0 ]; then
    ok "Root-README worklist rows agree with the worklist files and the methodology tree lists every 07-methodology file (stale batch17 residual repaired by review #69)"
else
    error "$C63_BAD root-README worklist/tree violation(s):"
    echo "$C63_OUT" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 64: event-custody register guards (dependency-map self-loops + overlap-pair bidirectional links) ---
echo "--- Check 64: Event-custody register guards ---"
# The 2026-09-03 event-custody pass closed the semantic-overlap blind spot: the gap
# methodology hunts capabilities appearing in ZERO PA files, and Check 35 verifies cited
# VS-numbers resolve — but nothing detected the same capability governed by MULTIPLE value
# streams with conflicting authority (the typhoon triple-collision VS-24/VS-26/VS-69: four
# workflows, four different closure triggers and commanders, zero cross-references between
# VS-26 and VS-69) or degenerate dependency-map self-loops (W54→W54, W288→W288 — 'W54 cannot
# function until W54 is operational'). Two guards:
#   Part A — the dependency map may carry no parent→itself edge (any `→|⇢|↔ Wxx` line whose
#            first target equals the enclosing parent block's W-id);
#   Part B — every overlap pair declared in event-custody-and-precedence-register.md §4
#            (`VS-A ↔ VS-B` rows) must cross-reference bidirectionally: at least one file of
#            VS-A's folder cites `\bVS-B\b` and vice versa, so a declared split can never ship
#            one-sided again.
CHECK64=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, glob, sys
ROOT = sys.argv[1]
errs = []

# ---- Part A: dependency-map self-loop edges ----
dep = os.path.join(ROOT, "01-model-company", "workflows", "workflow-dependency-map.md")
parent = None
for i, line in enumerate(open(dep, encoding="utf-8"), 1):
    pm = re.match(r"^\s*(W\d+[A-Z]?)\s*\(", line)
    if pm and not re.match(r"^\s*(\u2192|\u21e2|\u2194)", line):
        parent = pm.group(1)
        continue
    em = re.match(r"^\s*(\u2192|\u21e2|\u2194)\s*(W\d+[A-Z]?)", line)
    if em and parent and em.group(2) == parent:
        errs.append(f"workflow-dependency-map.md:{i}: self-loop edge {parent} {em.group(1)} {em.group(2)} (a block may not depend on itself; re-home the back-edge in \u00a76 CIRC like CIRC-005 or drop it)")

# ---- Part B: declared overlap pairs must cross-reference bidirectionally ----
reg = os.path.join(ROOT, "01-model-company", "workflows", "event-custody-and-precedence-register.md")
if not os.path.isfile(reg):
    errs.append("event-custody-and-precedence-register.md not found (workflows/ support file required since the 2026-09-03 event-custody pass)")
    pairs = []
else:
    pairs = sorted(set((int(a), int(b)) for a, b in
                       re.findall(r"\bVS-(\d+) \u2194 VS-(\d+)\b", open(reg, encoding="utf-8").read())))
folders = {}
for d in glob.glob(os.path.join(ROOT, "01-model-company", "workflows", "VS-*")):
    m = re.match(r"VS-(\d+)-", os.path.basename(d))
    if m:
        folders[int(m.group(1))] = d
for a, b in pairs:
    for x, y in ((a, b), (b, a)):
        if x not in folders:
            errs.append(f"OP pair VS-{a} \u2194 VS-{b}: VS-{x} has no workflow folder")
            continue
        hits = 0
        pat = re.compile(r"\bVS-0*%d\b" % y)  # citations may zero-pad (VS-07 for VS-7)
        for f in glob.glob(os.path.join(folders[x], "*.md")):
            if pat.search(open(f, encoding="utf-8").read()):
                hits += 1
        if hits == 0:
            errs.append(f"OP pair VS-{a} \u2194 VS-{b}: no file in VS-{x}/ cites VS-{y} (declared overlap pairs must cross-reference bidirectionally per the register \u00a74)")
print(f"TOTALS pairs={len(pairs)} problems={len(errs)}")
for e in errs:
    print("BAD|" + e)
PY
)
C64_BAD=$(echo "$CHECK64" | sed -n 's/^TOTALS .* problems=\([0-9]*\)/\1/p')
C64_PAIRS=$(echo "$CHECK64" | sed -n 's/^TOTALS pairs=\([0-9]*\) .*/\1/p')
if [ "${C64_BAD:-1}" -eq 0 ]; then
    ok "No dependency-map self-loop edges and all ${C64_PAIRS} declared event-custody overlap pairs cross-reference bidirectionally (guard added by the 2026-09-03 event-custody pass)"
else
    error "$C64_BAD event-custody violation(s) (dependency-map self-loop / one-sided overlap pair):"
    echo "$CHECK64" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 65: cross-VS duplicate-event guard (identical event Triggers / distinctive Frequency canons) ---
echo "--- Check 65: Cross-VS duplicate-event guard ---"
# The 2026-09-03 second custody wave found the copy/generator duplicate class the
# custody register cannot see mechanically: parallel full implementations of the same
# event living in different value streams (W12 'Returns & Exchanges' in VS-07 vs
# W1622/W1623 in VS-32 — same trigger semantics, same 56,000/month frequency canon,
# same owner, zero pointers between them until the register's E-09 scope note).
# Paraphrased duplicates (the W12/W1622 class itself) are caught only by semantic
# review; this guard catches the byte-identical class — future generator/copy-paste
# splits — via two signals, each with the adjudicated-legalitimate shared-cadence /
# shared-canon clusters allowlisted (same convention as Check 52's 20-cluster
# allowlist):
#   Part A — byte-identical event Triggers in different VS folders (pure-cadence
#            phrases like 'monthly reporting cycle' are auto-exempt via the cadence
#            vocabulary; 24 clusters adjudicated legitimate parallel programs);
#   Part B — byte-identical distinctive Frequency canons (containing a ≥3-digit figure
#            or %, length ≥ 12) in different VS folders (9 clusters adjudicated
#            legitimate shared enterprise canons: 200-store cadences, new-store
#            rates, TEU volumes, hire volumes).
CHECK65=$(python3 - "$REPO_ROOT" <<'PY'
import re, glob, os, collections, sys
ROOT = sys.argv[1]
CAD = set("monthly quarterly annual semiannual weekly daily review cycle reporting close monitoring analysis audit program strategy governance maturity ongoing continuous management financial period end event driven ad hoc scheduled per".split())
ALLOW_A = {
    "analytics cycle program review", "annual capital planning", "annual comprehensive review",
    "annual cycle strategic change", "annual planning cycle",
    "annual program review benchmark refresh maturity assessment vs133",
    "annual program review maturity assessment", "annual review strategic shift underperformance",
    "annual strategic review", "audit plan links to vs21 controls cycle", "delivery completion",
    "monthend close cycle w9a", "monthly analytics cycle", "monthly billing cycle",
    "monthly close margin review", "monthly cost analysis", "monthly ic settlement cycle",
    "monthlyquarterly programperformance review", "onboarding annual refresh",
    "quarterly competitive intelligence cycle", "quarterly planning cycle",
    "quarterly profitability review", "realtime monitoring",
    "risk assessment audit control remediation annual review",
}
ALLOW_B = {
    "1015 new storesyear", "400600 teusmonth", "6year 200 stores", "daily 200 stores",
    "daily all 200 stores", "monthly 200 stores", "monthly 200 stores 8 zones",
    "per hire 12001600 hiresyr", "quarterly 200 stores",
}
def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9% ]", "", s.lower())).strip()
trig, freq = collections.defaultdict(list), collections.defaultdict(list)
cur_w = cur_vs = None
for f in sorted(glob.glob(os.path.join(ROOT, "01-model-company", "workflows", "VS-*", "PA-*.md"))):
    vs = re.match(r"(VS-\d+)", os.path.basename(os.path.dirname(f))).group(1)
    for line in open(f, encoding="utf-8"):
        m = re.match(r"^#{2,3} (W\d+[A-Z]?)\.", line)
        if m:
            cur_w, cur_vs = m.group(1), vs
            continue
        m = re.match(r"^\|\s*\*\*Trigger\*\*\s*\|\s*(.+?)\s*\|\s*$", line)
        if m and cur_w:
            t = norm(m.group(1))
            if t and not all(w in CAD for w in t.split()):
                trig[t].append(f"{cur_w} ({cur_vs})")
        m = re.match(r"^\|\s*\*\*Frequency\*\*\s*\|\s*(.+?)\s*\|\s*$", line)
        if m and cur_w:
            t = norm(m.group(1))
            if t and len(t) >= 12 and (re.search(r"\d{3,}", t.replace(",", "")) or "%" in t):
                freq[t].append(f"{cur_w} ({cur_vs})")
errs = []
for label, table, allow in (("duplicate-event Trigger", trig, ALLOW_A),
                            ("shared distinctive Frequency canon", freq, ALLOW_B)):
    for t, ws in table.items():
        if len({w.split("(")[1] for w in ws}) > 1 and t not in allow:
            errs.append(f"{label} '{t}' shared by {len(ws)} workflows across value streams: {', '.join(ws[:5])} — parallel implementations of one event must be scoped via the event-custody register or reworded")
print(f"TOTALS problems={len(errs)}")
for e in errs:
    print("BAD|" + e)
PY
)
C65_BAD=$(echo "$CHECK65" | sed -n 's/^TOTALS problems=\([0-9]*\)/\1/p')
if [ "${C65_BAD:-1}" -eq 0 ]; then
    ok "No cross-VS byte-identical event Triggers or distinctive Frequency canons outside the 33 adjudicated shared-cadence/shared-canon clusters (guard added by the 2026-09-03 second custody wave; the paraphrase class is covered by the event-custody register's scope notes)"
else
    error "$C65_BAD cross-VS duplicate-event violation(s):"
    echo "$CHECK65" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 66: Repo-wide file-level relative-link resolution (non-PA files) ---
echo "--- Check 66: Relative-link target resolution outside PA files ---"
# Check 20 resolves every relative .md link inside PA files; Check 39(d) resolves the
# *anchor* half of cross-file links. Neither guards the file-level half in the other
# ~213 .md files (VS READMEs, workflows/ support docs, root docs, methodology docs) —
# a 2026-09-03 residual sweep found exactly this class: the VS-08 and VS-32 READMEs
# linked 'event-custody-and-precedence-register.md' without the '../' prefix (the
# register lives one directory up), invisible to both guards. This check resolves
# every relative markdown link target (file part; fragments and externals ignored)
# in every non-PA .md file so the drift cannot recur. Literal prose examples inside
# CHANGELOG change-notes ('file.md#anchor') are exempt.
CHECK66=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys, glob
ROOT = sys.argv[1]
bad = []
total = 0
files = [f for f in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)
         if ".git" not in f and not re.search(r"PA-\d+\.\d+-", os.path.basename(f))]
link = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
for f in files:
    txt = re.sub(r"```.*?```", "", open(f, encoding="utf-8", errors="replace").read(), flags=re.S)
    for m in link.finditer(txt):
        t = m.group(1).strip()
        if t.startswith(("http://", "https://", "mailto:")) or t.startswith("#"):
            continue
        path_part = t.split("#")[0].split()[0]
        if not path_part:
            continue
        if "CHANGELOG.md" in f and path_part == "file.md":  # literal prose example
            continue
        total += 1
        resolved = os.path.normpath(os.path.join(os.path.dirname(f), path_part))
        if not os.path.exists(resolved):
            bad.append(f"{os.path.relpath(f, ROOT)}: [{t}] -> missing target")
print(f"TOTALS links={total} problems={len(bad)}")
for b in bad:
    print("BAD|" + b)
PY
)
C66_BAD=$(echo "$CHECK66" | sed -n 's/^TOTALS links=[0-9]* problems=\([0-9]*\)/\1/p')
if [ "${C66_BAD:-1}" -eq 0 ]; then
    ok "All non-PA relative markdown links resolve to existing files (guard added by the 2026-09-03 residual sweep; PA files remain Check 20's surface)"
else
    error "$C66_BAD broken relative link(s) outside PA files:"
    echo "$CHECK66" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 67: VS-README Process-Areas tables cross-foot + extended-section guard ---
echo "--- Check 67: VS-README process-area counts & extended sections vs disk ---"
# The value-stream-index per-VS rows are re-derived by Check 68 (same pass), but
# each VS README carries its own Process-Areas table (one row per PA file with a
# workflow count, plus a **Total** row) that no check read. The 2026-09-03 worklist-adjudication
# pass moved W239 from PA-24.3 (8→7) to PA-87.3 (8→9), re-pointed the index, the root
# README tree and the dependency map — and missed exactly these two README tables
# (VS-24 stale 8/27, VS-87 stale 8/24). This check re-derives every VS README's
# per-PA row and Total row from the PA files' own '## W' headers.
# ---- Part B (2026-09-15 thirty-fourth wave): the 21 core-block READMEs (VS-01–VS-20
# + VS-73) also carry Overview / Why it matters / Owner & participants / Key dependencies
# / Key controls prose that NO check read — the thirty-fourth-wave review found four
# wrong-id control citations (CTL-229 glossed 'credit limit' in VS-11/VS-16 where the
# register objective is supplier quality/product-safety and the credit-limit control is
# CTL-05; CTL-337 'payroll audit' in VS-19 where CTL-337 is the PA-32.1 returns control
# and the payroll operating control is CTL-297; CTL-43 'lease/CAM audit' in VS-20 where
# CTL-43 is sales-rep credit self-approval and the facility/lease-cost control is
# CTL-218), two figure conflations vs the PA canon (VS-08's '~PHP 62.3B revenue flow
# through 600 terminals' — the terminal flow is the ~PHP 60.5B in-store subset, the
# PHP 1.8B ecommerce share rides the platform; VS-73's recycling split 1–2M/7–14M vs its
# own W2599 10–43K/store/yr and 5–10K/store/mo offcut canon → 2–8.6M/12–24M network),
# one TO reporting-line contradiction (VS-73's Coordinator '(reports to COO)' vs the
# org of record: reports to the Head of Sustainability / ESG), and five drifted/mangled
# owner seats (VS-08 'POS & IT' → IT Store Systems & POS (SSP); VS-09 'Service Managers'
# and VS-12 'Service Operations Managers' phantom seats → the PA owner canon; VS-13
# 'CRM & Loyalty' → the TO register's Loyalty & CRM Manager; VS-19 'CHRO / CHROs' →
# 'CHRO / HR & Payroll Managers'). Part B pins the 21 Owner lines, verifies every
# Key-controls CTL gloss against the register's own control objective (significant-token
# overlap, joined over wrapped lines), and anchors the repaired figures with the retired
# forms forbidden per file.
CHECK67=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
wf = os.path.join(ROOT, "01-model-company", "workflows")
bad = []
rows = 0
for d in sorted(os.listdir(wf)):
    if not d.startswith("VS-"):
        continue
    rd = os.path.join(wf, d, "README.md")
    if not os.path.exists(rd):
        continue
    disk = {}
    for f in os.listdir(os.path.join(wf, d)):
        if f.startswith("PA-") and f.endswith(".md"):
            txt = open(os.path.join(wf, d, f), encoding="utf-8").read()
            disk[f] = len(re.findall(r"^## W\d+[A-Z]?\.", txt, re.M))
    text = open(rd, encoding="utf-8").read()
    seen = {}
    total_claim = None
    for line in text.splitlines():
        m = re.match(r"^\|\s*\[?(PA-\d+\.\d+)[^|]*\]\((PA-[\w.-]+\.md)\)\s*\|[^|]+\|\s*(\d+)\s*\|", line)
        if m:
            fname = m.group(2)
            seen[fname] = int(m.group(3))
            rows += 1
            if fname not in disk:
                bad.append(f"{d}/README.md: row for {fname} but no such PA file on disk")
            elif seen[fname] != disk[fname]:
                bad.append(f"{d}/README.md: {fname} row says {seen[fname]} workflows, disk has {disk[fname]}")
            continue
        m = re.match(r"^\|\s*\|?\s*\*\*Total\*\*\s*\|\s*\*\*(\d[\d,]*)\*\*\s*\|", line)
        if m:
            total_claim = int(m.group(1).replace(",", ""))
    for f in disk:
        if f not in seen:
            bad.append(f"{d}/README.md: PA file {f} on disk has no Process-Areas table row")
    if total_claim is not None and total_claim != sum(disk.values()):
        bad.append(f"{d}/README.md: Total row says {total_claim}, disk sums to {sum(disk.values())}")

# ---- Part B: extended-section VS-README guard (2026-09-15 thirty-fourth wave) ----
OWNERS = {
    "VS-01-merchandise-strategy": "- **Owner**: VP Merchandising / Category Managers",
    "VS-02-supply-planning": "- **Owner**: VP Supply Chain / Demand & Supply Planners",
    "VS-03-vendor-management": "- **Owner**: VP Supply Chain / Category Managers",
    "VS-04-dc-warehouse": "- **Owner**: VP Supply Chain / DC Operations Managers",
    "VS-05-inventory-lifecycle": "- **Owner**: VP Supply Chain / Inventory Managers",
    "VS-06-logistics-fleet": "- **Owner**: VP Supply Chain / Fleet Manager",
    "VS-07-store-operations": "- **Owner**: VP Store Operations / Store Managers",
    "VS-08-pos-checkout": "- **Owner**: VP Store Operations / IT Store Systems & POS (SSP)",
    "VS-09-in-store-services": "- **Owner**: VP Store Operations / Store Managers & Department Supervisors",
    "VS-10-ecommerce-digital": "- **Owner**: GM, Digital Commerce Inc. / Digital",
    "VS-11-trade-project-wholesale": "- **Owner**: VP Trade Sales / B2B Sales Managers",
    "VS-12-installation-services": "- **Owner**: COO / Services Category Manager, Service Coordinators & Rental Fleet Manager",
    "VS-13-customer-experience": "- **Owner**: Head of Customer Service / Loyalty & CRM Manager",
    "VS-14-marketing": "- **Owner**: CMO / Marketing Managers",
    "VS-15-procure-to-pay": "- **Owner**: Controller / AP Manager",
    "VS-16-order-to-cash": "- **Owner**: Credit Manager / Controller",
    "VS-17-record-to-report": "- **Owner**: Controller / CFO",
    "VS-18-treasury-cash": "- **Owner**: Treasurer / CFO",
    "VS-19-hire-to-retire": "- **Owner**: CHRO / HR & Payroll Managers",
    "VS-20-real-estate-construction": "- **Owner**: COO / Facilities",
    "VS-73-store-waste-circular-economy": "- **Owner**: Sustainability Coordinator (reports to the Head of Sustainability / ESG)",
}
ANCHORS = {
    "VS-08-pos-checkout": ["~PHP 60.5B in-store revenue (of ~PHP 62.3B total company revenue)"],
    "VS-73-store-waste-circular-economy": [
        "~PHP 2–8.6M/yr cardboard recycling revenue",
        "~PHP 12–24M/yr lumber-offcut clearance revenue",
        "reports to the Head of Sustainability / ESG",
    ],
}
RETIRED = {
    "VS-08-pos-checkout": ["~PHP 62.3B revenue flow through 600 terminals", "/ POS & IT"],
    "VS-09-in-store-services": ["/ Service Managers"],
    "VS-11-trade-project-wholesale": ["CTL-229 (credit limit)"],
    "VS-12-installation-services": ["/ Service Operations Managers"],
    "VS-13-customer-experience": ["/ CRM & Loyalty"],
    "VS-16-order-to-cash": ["CTL-229 (credit limit)"],
    "VS-19-hire-to-retire": ["CHRO / CHROs", "CTL-337 payroll audit", "CTL-34 (statutory)"],
    "VS-20-real-estate-construction": ["CTL-43 (lease/CAM audit)"],
    "VS-73-store-waste-circular-economy": ["reports to COO", "~PHP 1–2M/yr cardboard", "~PHP 7–14M/yr"],
}
matrix_txt = open(os.path.join(ROOT, "01-model-company", "internal-controls-matrix.md"), encoding="utf-8").read()
ctl_obj = {}
for m in re.finditer(r"^\| CTL-(\d+) \| ([^|]+) \|", matrix_txt, re.M):
    ctl_obj[int(m.group(1))] = m.group(2)
STOP = {"ensure", "prevent", "detect", "and", "of", "the", "via", "per", "for", "a", "an",
        "to", "on", "in", "with", "control", "controls", "plus", "operational"}
def _toks(s):
    out = set()
    for t in re.split(r"[^a-z0-9]+", s.lower()):
        if not t or t in STOP:
            continue
        out.add(t[:-1] if len(t) > 3 and t.endswith("s") else t)
    return out
GLOSS_RE = re.compile(r"CTL-(\d{2,3})((?:/\d{2,3})*)\s*\(([^)]+)\)")
owner_dirs = set()
gloss_checked = 0
kc_sections = 0
for d in sorted(os.listdir(wf)):
    if not d.startswith("VS-"):
        continue
    rd = os.path.join(wf, d, "README.md")
    if not os.path.exists(rd):
        continue
    text = open(rd, encoding="utf-8").read()
    if "## Owner & participants" in text:
        owner_dirs.add(d)
    if d in OWNERS:
        want = OWNERS[d]
        if want not in text:
            bad.append(f"{d}/README.md: Owner line drifted — expected {want!r}")
    for lit in RETIRED.get(d, []):
        if lit in text:
            bad.append(f"{d}/README.md: retired literal present: {lit!r}")
    for anchor in ANCHORS.get(d, []):
        if anchor not in text:
            bad.append(f"{d}/README.md: repaired anchor missing: {anchor!r}")
    sec = re.search(r"^## Key controls\s*\n(.*?)(?=^## |\n---)", text, re.M | re.S)
    if not sec:
        continue
    kc_sections += 1
    joined = re.sub(r"\s*\n\s*", " ", sec.group(1))
    for g in GLOSS_RE.finditer(joined):
        ids = [int(g.group(1))] + [int(x) for x in g.group(2).split("/") if x]
        gt = _toks(g.group(3))
        for n in ids:
            gloss_checked += 1
            if n not in ctl_obj:
                bad.append(f"{d}/README.md: Key-controls cites CTL-{n} but no such register row")
            elif not (gt & _toks(ctl_obj[n])):
                bad.append(f"{d}/README.md: CTL-{n} gloss '{g.group(3)}' shares no token with register objective '{ctl_obj[n].strip()}'")
if owner_dirs != set(OWNERS):
    missing = sorted(set(OWNERS) - owner_dirs)
    extra = sorted(owner_dirs - set(OWNERS))
    bad.append(f"extended-section population drifted: missing={missing} extra={extra} (expected 21)")

print(f"TOTALS rows={rows} problems={len(bad)} glosses={gloss_checked} sections={kc_sections}")
for b in bad:
    print("BAD|" + b)
PY
)
C67_BAD=$(echo "$CHECK67" | sed -n 's/^TOTALS rows=[0-9]* problems=\([0-9]*\).*/\1/p')
if [ "${C67_BAD:-1}" -eq 0 ]; then
    C67_GLOSSES=$(echo "$CHECK67" | sed -n 's/^TOTALS rows=[0-9]* problems=[0-9]* glosses=\([0-9]*\) sections=[0-9]*/\1/p')
    C67_SECTIONS=$(echo "$CHECK67" | sed -n 's/^TOTALS rows=[0-9]* problems=[0-9]* glosses=[0-9]* sections=\([0-9]*\)/\1/p')
    ok "All 188 VS-README Process-Areas tables cross-foot against the PA files' own ## W headers, and the 21 extended-section READMEs (VS-01–VS-20 + VS-73) hold: every Owner line pinned to the org-of-record form, all ${C67_GLOSSES:-0} Key-controls CTL glosses across ${C67_SECTIONS:-0} sections token-overlapping the register's own control objective (joined over wrapped lines), and the thirty-fourth-wave repaired figure/reporting-line anchors present with the retired forms forbidden per file (Process-Areas cross-foot added by the 2026-09-03 consistency review pass after the W239 move left VS-24/VS-87 stale; extended-section arm added by the 2026-09-15 thirty-fourth-wave review after four wrong-id control citations (CTL-229 as 'credit limit' in VS-11/VS-16, CTL-337 as 'payroll audit' in VS-19, CTL-43 as 'lease/CAM audit' in VS-20), two subset/total and split-vs-canon figure conflations (VS-08's PHP 62.3B-through-terminals, VS-73's 1–2M/7–14M recycling split vs its own W2599/offcut canon), one TO reporting-line contradiction (VS-73's Coordinator 'reports to COO') and five drifted/mangled/phantom owner seats were found stranded on the prose sections no check read)"
else
    error "$C67_BAD VS-README process-area/extended-section problem(s):"
    echo "$CHECK67" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 68: Value-stream-index per-VS rows cross-foot vs disk ---
echo "--- Check 68: Value-stream-index per-VS rows vs disk ---"
# Check 2 compares each PA file's workflow count against its PA bullet in the
# index's detailed section and Check 9 guards the Grand Total, but two VS-level
# count surfaces read nothing: the 'Value Stream Architecture' summary-table
# rows (per-VS Process-Areas and Workflows cells) and the detailed section's
# per-VS headings ('(n workflows)'). The 2026-08-26 batch-4 gap-fill (W5508
# into VS-79.2, W5509 into VS-02.1) trued the summary-table cells, the VS
# READMEs, workflows/README and the Grand Total but left both headings stale
# (VS-02 '37 workflows' vs disk 38; VS-79 '24 workflows' vs disk 25) — drift
# invisible to every check, and to subsequent full re-derivations that read
# the summary table, until the 2026-09-03 second consistency review pass.
# This check re-derives both surfaces from the PA files' own '## W' headers:
# per-VS workflow counts on both surfaces and per-VS process-area counts on
# the summary table; missing rows for on-disk VSs and phantom rows for VSs
# with no directory both error. (The index-side sibling of Check 67.)
CHECK68=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
wf = os.path.join(ROOT, "01-model-company", "workflows")
idx = open(os.path.join(wf, "value-stream-index.md"), encoding="utf-8").read()
disk = {}
for d in sorted(os.listdir(wf)):
    m = re.match(r"VS-(\d+)-", d)
    if not m:
        continue
    vs = m.group(1)
    pas = 0
    wfs = 0
    for f in os.listdir(os.path.join(wf, d)):
        if re.match(r"PA-\d+\.\d+-", f) and f.endswith(".md"):
            pas += 1
            wfs += len(re.findall(r"^## W\d+[A-Z]?\.", open(os.path.join(wf, d, f), encoding="utf-8").read(), re.M))
    disk[vs] = (pas, wfs)
bad = []
sum_rows = 0
head_rows = 0
seen_sum = set()
seen_head = set()
for line in idx.splitlines():
    m = re.match(r"^\|[^|]*\|\s*\[VS-(\d+)\]\([^)]*\)\s*\|[^|]*\|[^|]*\|\s*(\d+)\s*\|\s*(\d[\d,]*)\s*\|", line)
    if m:
        vs, pa, n = m.group(1), int(m.group(2)), int(m.group(3).replace(",", ""))
        sum_rows += 1
        seen_sum.add(vs)
        if vs not in disk:
            bad.append(f"summary-table row for VS-{vs} but no such VS directory on disk")
        elif disk[vs] != (pa, n):
            bad.append(f"summary-table VS-{vs} cells say {pa} PAs / {n} workflows, disk has {disk[vs][0]} / {disk[vs][1]}")
        continue
    m = re.match(r"^\*\*\[VS-(\d+): [^\]]+\]\([^)]*\)\*\* \((\d[\d,]*) workflows\)", line)
    if m:
        vs, n = m.group(1), int(m.group(2).replace(",", ""))
        head_rows += 1
        seen_head.add(vs)
        if vs not in disk:
            bad.append(f"detailed heading for VS-{vs} but no such VS directory on disk")
        elif disk[vs][1] != n:
            bad.append(f"detailed heading VS-{vs} says {n} workflows, disk has {disk[vs][1]}")
for vs in disk:
    if vs not in seen_sum:
        bad.append(f"VS-{vs} on disk has no summary-table row")
    if vs not in seen_head:
        bad.append(f"VS-{vs} on disk has no detailed-section heading")
# ---- family Subtotal + Grand Total rows (2026-09-15 thirty-third-wave) ----
# Check 68 pins each per-VS row against disk, but the 8 family '**Subtotal**' cells and
# the '**Grand Total**' row themselves were read by no rule — a batch re-ordering rows or
# re-totaling a family cell could strand them while every per-VS row stayed exact. Each
# family subtotal must now equal the sum of its own per-VS rows (PA and workflow cells
# separately) and the Grand Total must equal the family-subtotal column sums.
_fam = None
_fams = {}
for line in idx.splitlines():
    m = re.match(r'^\| (Plan & Source|Make & Move|Sell & Serve|Finance|People|Asset & Infrastructure|Governance & Assurance|Technology & Data) \|', line)
    if m:
        _fam = m.group(1)
        _fams.setdefault(_fam, {'pa': 0, 'wf': 0, 'vs': 0, 'stated': None})
    m = re.match(r'^\|(?:[^|]*)\|\s*\[VS-(\d+)\]\([^)]*\)\s*\|[^|]*\|[^|]*\|\s*(\d+)\s*\|\s*([\d,]+)\s*\|', line)
    if m and _fam:
        _fams[_fam]['pa'] += int(m.group(2))
        _fams[_fam]['wf'] += int(m.group(3).replace(',', ''))
        _fams[_fam]['vs'] += 1
    else:
        m = re.match(r'^\|[^|]*\|[^|]*\|[^|]*\|\s*\*\*Subtotal\*\*\s*\|\s*\*\*([\d,]+)\*\*\s*\|\s*\*\*([\d,]+)\*\*\s*\|', line)
        if m and _fam:
            _fams[_fam]['stated'] = (int(m.group(1).replace(',', '')), int(m.group(2).replace(',', '')))
if len(_fams) != 8:
    bad.append(f"index family-subtotal arm parses to {len(_fams)} families, expected 8")
for _fname, _d in _fams.items():
    if _d['stated'] is None:
        bad.append(f"index family '{_fname}' has no **Subtotal** row")
    elif _d['stated'] != (_d['pa'], _d['wf']):
        bad.append(f"index family '{_fname}' Subtotal says {_d['stated'][0]} PAs / {_d['stated'][1]:,} workflows but its own rows sum to {_d['pa']} / {_d['wf']:,}")
m = re.search(r'^\|[^|]*\|[^|]*\|[^|]*\|\s*\*\*Grand Total\*\*\s*\|\s*\*\*([\d,]+)\*\*\s*\|\s*\*\*([\d,]+)\*\*\s*\|\s*$', idx, re.M)
if not m:
    bad.append("cannot find the index **Grand Total** row")
else:
    _gpa, _gwf = int(m.group(1).replace(',', '')), int(m.group(2).replace(',', ''))
    if (_gpa, _gwf) != (sum(_d['pa'] for _d in _fams.values()), sum(_d['wf'] for _d in _fams.values())):
        bad.append(f"index Grand Total says {_gpa} PAs / {_gwf:,} workflows but the family subtotals sum to {sum(_d['pa'] for _d in _fams.values())} / {sum(_d['wf'] for _d in _fams.values()):,}")
print(f"TOTALS summary_rows={sum_rows} headings={head_rows} problems={len(bad)}")
for b in bad:
    print("BAD|" + b)
PY
)
C68_BAD=$(echo "$CHECK68" | sed -n 's/^TOTALS .* problems=\([0-9]*\)/\1/p')
if [ "${C68_BAD:-1}" -eq 0 ]; then
    ok "All value-stream-index per-VS rows (summary table + detailed headings) cross-foot against disk, and the 8 family **Subtotal** rows plus the **Grand Total** row equal their own per-VS row sums (guard added by the 2026-09-03 second consistency review pass after the batch-4 additions left VS-02/VS-79 headings stale; subtotal arm added by the 2026-09-15 thirty-third-wave review)"
else
    error "$C68_BAD value-stream-index per-VS problem(s):"
    echo "$CHECK68" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 69: Semantic-audit registry integrity (admitted-set vs live workflows vs pending notes) ---
echo "--- Check 69: Semantic-audit registry integrity ---"
# final-semantic-coverage.py (Check 62 family) derives its audited set from the bare
# W-id lines in semantic-audit-coverage.txt, so the registry's line-list discipline IS
# the detector pass's coverage claim. The 2026-09-04 consistency review found the
# batch-9 pass (c56dc3c) had appended its four workflow ids W5525–W5528 as bare lines
# immediately above its own 'NOT yet in the audited registry' pending note — a
# self-contradiction no check read: the tool's audited-set silently read 5,374
# (matching neither the closed-loop 5,370 nor the live 5,387), four never-audited
# workflows were treated as detector-swept, and the tree rows describing the file had
# stranded at the 5,367/5,370 era. Repaired by deleting the stray lines and widening
# the second pending note to its real coverage (W5525–W5534, batches 9–11). Four
# invariants now guard the file so the class cannot recur:
#   (a) every bare W-id line is distinct;
#   (b) every bare W-id resolves to a live '## W' workflow header (no ghosts);
#   (c) no W-id may appear both as a bare line and inside a '(transition-path pending)'
#       note's declared range (the comment/bare-line contradiction class itself);
#   (d) the sets close: live workflows = admitted bare ids + ids named in the pending
#       notes' en-dash ranges (the file's naming convention) — so an admission that
#       forgets to retire its pending note, or a pending note that forgets its own
#       ids, both error. (Standalone prose mentions inside notes — e.g. 'the documented
#       W5511 transition path', which references the admitted exemplar — are not set
#       membership; the closure invariant is what pins the note to its real id set.)
CHECK69=$(python3 - "$REPO_ROOT" <<'PY'
import glob, os, re, sys
ROOT = sys.argv[1]
reg = os.path.join(ROOT, "07-methodology", "semantic-audit-coverage.txt")
lines = open(reg, encoding="utf-8").read().splitlines()
bare, pend = [], set()
in_pending = False
for i, l in enumerate(lines, 1):
    s = l.strip()
    if re.fullmatch(r"W\d+[A-Z]?", s):
        bare.append((s, i))
        continue
    if s.startswith("#") and "transition-path pending" in s:
        in_pending = True
    elif s and not s.startswith("#"):
        in_pending = False
    if in_pending:
        for a, b in re.findall(r"W(\d+)[A-Z]?\s*[\u2013\u2014-]\s*W(\d+)", s):
            pend.update(f"W{n}" for n in range(int(a), int(b) + 1))
errs = []
seen = {}
for w, i in bare:
    if w in seen:
        errs.append(f"duplicate bare id {w} (lines {seen[w]} and {i})")
    seen[w] = i
live = set()
for f in glob.glob(os.path.join(ROOT, "01-model-company", "workflows", "VS-*", "PA-*.md")):
    live |= set(re.findall(r"^## (W\d+[A-Z]?)\.", open(f, encoding="utf-8").read(), re.M))
def wk(x):
    return int(re.sub(r"\D", "", x))
for w in sorted(seen, key=wk):
    if w not in live:
        errs.append(f"bare id {w} resolves to no live '## W' workflow header (ghost)")
for w, i in bare:
    if w in pend:
        errs.append(f"line {i}: bare id {w} is also named in a '(transition-path pending)' note — a pending workflow must not be listed as audited")
admitted = set(seen)
if live - admitted != pend:
    only_live = sorted(live - admitted - pend, key=wk)
    only_pend = sorted(pend - (live - admitted), key=wk)
    if only_live:
        errs.append(f"closure: {len(only_live)} live workflow(s) neither admitted nor pending-named: {', '.join(only_live[:8])}")
    if only_pend:
        errs.append(f"closure: {len(only_pend)} pending-named id(s) already admitted or not live: {', '.join(only_pend[:8])}")
print(f"TOTALS admitted={len(admitted)} pending={len(pend)} live={len(live)} problems={len(errs)}")
for e in errs:
    print("BAD|" + e)
PY
)
C69_ADM=$(echo "$CHECK69" | sed -n 's/^TOTALS admitted=\([0-9]*\).*/\1/p')
C69_PEND=$(echo "$CHECK69" | sed -n 's/^TOTALS admitted=[0-9]* pending=\([0-9]*\).*/\1/p')
C69_LIVE=$(echo "$CHECK69" | sed -n 's/^TOTALS admitted=[0-9]* pending=[0-9]* live=\([0-9]*\).*/\1/p')
C69_BAD=$(echo "$CHECK69" | sed -n 's/^TOTALS .* problems=\([0-9]*\)/\1/p')
if [ "${C69_BAD:-1}" -eq 0 ]; then
    ok "Semantic-audit registry closes: $C69_ADM admitted + $C69_PEND pending = $C69_LIVE live workflows; no ghosts, duplicates, or pending/bare contradictions (guard added by the 2026-09-04 consistency review pass after the batch-9 pending-note contradiction left the detector audited-set at 5,374)"
else
    error "$C69_BAD semantic-audit-registry violation(s):"
    echo "$CHECK69" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 70: Root-README figure annotations vs canonical registers ---
echo "--- Check 70: Root-README figure annotations vs canonical registers ---"
# The batch-22→23 re-point cascades updated the root README's tree total, the
# Criticality-classification coverage row and the cross-reference diagram but
# stranded three sibling surfaces no check read: the Key-Metrics 'Workflows
# (total)' row, the Coverage 'Workflows' row's headline and '(all X confirmed-
# classified)' figures, and the classification tree row's '(N rows)' annotation —
# each frozen one batch behind (5,422/5,445 vs the 5,426/5,449 canon). This check
# re-derives the unique-workflow total and the confirmed-register row count from
# disk on every run and asserts all five README annotations against them, so the
# whole annotation family is guarded in one place. (The Key-Metrics requirement
# rows were already guarded by Checks 37/41; the workflows rows were not.)
README70="$REPO_ROOT/README.md"
ACTUAL_WF70=$(grep -rhP '^## W\d+[A-Z]?\.' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l | tr -d ' ')
REG_ROWS70=$(grep -cP '^\| W\d+[A-Z]? \|' "$REPO_ROOT"/01-model-company/workflows/workflow-criticality-classification.md)
C70_BAD=0
check70() { # $1 declared figure (comma-stripped), $2 expected, $3 label
    if [ "$1" != "$2" ]; then
        error "Root-README $3 declares $1 but the canonical figure is $2"
        C70_BAD=1
    fi
}
D70=$(grep -oP '├── workflows/ +\K[\d,]+(?= workflows organized by value stream)' "$README70" | tr -d ',')
if [ -n "$D70" ]; then check70 "$D70" "$ACTUAL_WF70" "'workflows/' tree-total line"; else error "Could not locate the workflows/ tree-total annotation in README.md"; C70_BAD=1; fi
KM70=$(grep -oP '\| Workflows \(total\) \| \*\*\K[\d,]+' "$README70" | tr -d ',')
if [ -n "$KM70" ]; then check70 "$KM70" "$ACTUAL_WF70" "Key-Metrics 'Workflows (total)' row"; else error "Could not locate the Key-Metrics 'Workflows (total)' row in README.md"; C70_BAD=1; fi
COV70=$(grep -oP '\| Workflows \| \K[\d,]+(?= fully specified)' "$README70" | tr -d ',')
if [ -n "$COV70" ]; then check70 "$COV70" "$ACTUAL_WF70" "Coverage-row 'Workflows' headline"; else error "Could not locate the Coverage-row 'Workflows' headline in README.md"; C70_BAD=1; fi
COVA70=$(grep -oP '\(all \K[\d,]+(?= confirmed-classified)' "$README70" | tr -d ',')
if [ -n "$COVA70" ]; then check70 "$COVA70" "$ACTUAL_WF70" "Coverage-row '(all X confirmed-classified)' figure"; else error "Could not locate the Coverage-row '(all X confirmed-classified)' figure in README.md"; C70_BAD=1; fi
TR70=$(grep -oP 'workflow-criticality-classification\.md  Tier 1/2/3 confirmed priorities \(\K[\d,]+(?= rows\))' "$README70" | tr -d ',')
if [ -n "$TR70" ]; then check70 "$TR70" "$REG_ROWS70" "classification tree-row '(N rows)' annotation"; else error "Could not locate the classification tree-row '(N rows)' annotation in README.md"; C70_BAD=1; fi
if [ "$C70_BAD" -eq 0 ]; then
    ok "All 5 root-README figure annotations match the canonical registers ($ACTUAL_WF70 unique workflows / $REG_ROWS70 confirmed-register rows; guard added by the 2026-09-05 sixth-wave review after the batch-23 pass stranded the Key-Metrics row, the Coverage-row headline figures and the classification tree-row annotation one batch behind)"
fi

# --- Check 71: Generated BPMN/DMN trees vs the markdown corpus ---
echo "--- Check 71: Generated BPMN/DMN trees vs the markdown corpus ---"
# The bpmn/ and dmn/ trees are generated artifacts whose only validation was
# the generators' built-in self-checks — i.e. they ran only when someone
# remembered to re-run the generators. No check in this script ever read the
# shipped trees, so a hand-edit or a partial regeneration could strand drift
# in exactly the defect class the 2026-09-05 seventh-wave consistency review's
# independent deep validation probed (and the same class as the bpmn/ wiring
# off-by-one that shipped before the same day's generator fix): well-formed
# XML, canonical counts (one .bpmn per PA file, one process per
# confirmed-register row, one decision per extracted rule set), per-process
# start/end cardinality, lane coverage with in-process lane refs, 1:1
# BPMNDiagram:BPMNPlane:process, DI shape/edge coverage with positive bounds
# and waypoints, decision-table structure, and a DRD shape per decision.
# This check re-derives the canonical counts from the markdown corpus on
# every run and structurally validates both trees. Since the 2026-09-15
# thirtieth-wave review it also byte-verifies the third generated artifact
# (01-model-company/role-coverage-matrix.md) via generate-role-coverage.py --check.
CHECK71=$(python3 - "$REPO_ROOT" <<'PY'
import re, sys, xml.etree.ElementTree as ET
from pathlib import Path
ROOT = Path(sys.argv[1])
bad = []
B = "{http://www.omg.org/spec/BPMN/20100524/MODEL}"
BD = "{http://www.omg.org/spec/BPMN/20100524/DI}"
D = "{https://www.omg.org/spec/DMN/20191111/MODEL/}"
DD = "{https://www.omg.org/spec/DMN/20191111/DMNDI/}"
# canonical counts from the markdown corpus
pa_files = sorted((ROOT / "01-model-company/workflows").glob("VS-*/PA-*.md"))
reg_rows = 0
for line in (ROOT / "01-model-company/workflows/workflow-criticality-classification.md").read_text().splitlines():
    if re.match(r"^\|\s*W\d+[A-Z]?\s*\|", line):
        reg_rows += 1
# ---- BPMN tree ----
files = sorted((ROOT / "bpmn").rglob("*.bpmn"))
if len(files) != len(pa_files):
    bad.append(f"bpmn/ holds {len(files)} .bpmn files but the corpus has {len(pa_files)} PA files")

# ---- 2026-09-10 seventeenth-wave extension: documentation-text mirror ----
# Structural validation cannot see CONTENT drift: the batch-24 pass edited the PA-133.1/.3
# Volume rows (5,426→5,427) but shipped the two generated .bpmn files stale at 5,426 — the
# commit's 'only PA-07.1's file moved' regeneration claim was false and no check noticed
# because the trees' processes/flows/counts were all still correct. This extension imports
# the generator's own parser, re-derives each process's <bpmn:documentation> text, start-
# event name and controls annotation exactly as generate-bpmn.py would emit them, and
# requires the shipped XML to match — i.e. any markdown field edit without a regeneration
# now fails the validator, and a hand-edit of the generated text fails it too.
import importlib.util
_spec = importlib.util.spec_from_file_location("_genbpmn", str(ROOT / "07-methodology" / "generate-bpmn.py"))
_gen = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_gen)

tot_procs = 0
for f in files:
    try:
        root = ET.parse(f).getroot()
    except ET.ParseError as e:
        bad.append(f"{f}: XML parse error: {e}"); continue
    procs = list(root.iter(B + "process"))
    tot_procs += len(procs)
    # ---- build the generator-equivalent expectations from the PA markdown ----
    exp_doc, exp_start, exp_anno = {}, {}, {}
    pa_md = ROOT / "01-model-company" / "workflows" / f.relative_to(ROOT / "bpmn").with_suffix(".md")
    if not pa_md.exists():
        bad.append(f"{f}: no corresponding PA markdown at {pa_md.relative_to(ROOT)}")
    else:
        for wf in _gen.parse_pa_file(pa_md):
            pid = "W_" + re.sub(r"[^A-Za-z0-9_.-]", "_", wf["id"])
            fld = wf["fields"]
            doc_lines = [f"{k}: {fld[k]}" for k in ("Trigger", "Frequency", "Volume", "Owner", "Participants") if k in fld]
            doc_lines.append(f"Source: workflow {wf['id']} — {wf['name']}")
            exp_doc[pid] = "\n".join(doc_lines)
            exp_start[pid] = _gen.truncate(_gen.strip_md(fld.get("Trigger", "Trigger")), 90)
            ctl = ("Controls: " + " | ".join(_gen.strip_md(b) for b in wf["sections"].get("Controls", []))) if wf["sections"].get("Controls") else "Controls: (none recorded)"
            if fld.get("Owner"):
                ctl += f"\nOwner: {fld['Owner']}"
            exp_anno[pid] = _gen.truncate(ctl, _gen.MAX_ANNOTATION)
    diags = list(root.iter(BD + "BPMNDiagram"))
    planes = list(root.iter(BD + "BPMNPlane"))
    if not (len(procs) == len(diags) == len(planes)):
        bad.append(f"{f}: {len(procs)} processes vs {len(diags)} diagrams / {len(planes)} planes (want 1:1:1)")
    proc_ids = {p.get("id") for p in procs}
    for pl in planes:
        if pl.get("bpmnElement") not in proc_ids:
            bad.append(f"{f}: plane {pl.get('id')} ref {pl.get('bpmnElement')} is not a process id")
    shapes = {s.get("bpmnElement") for s in root.iter(BD + "BPMNShape")}
    edges = {e.get("bpmnElement") for e in root.iter(BD + "BPMNEdge")}
    for p in procs:
        pid = p.get("id")
        if pid in exp_doc:
            de = p.find(B + "documentation")
            got = (de.text or "") if de is not None else None
            if got != exp_doc[pid]:
                bad.append(f"{f}: {pid} process documentation is stale vs its markdown source (generator re-derivation mismatch — regenerate the tree)")
            se = p.find(B + "startEvent")
            if se is not None and (se.get("name") or "") != exp_start[pid]:
                bad.append(f"{f}: {pid} start-event name is stale vs its markdown Trigger (generator re-derivation mismatch — regenerate the tree)")
            an = p.find(B + "textAnnotation")
            at = an.find(B + "text") if an is not None else None
            got_a = (at.text or "") if at is not None else None
            if got_a != exp_anno[pid]:
                bad.append(f"{f}: {pid} controls annotation is stale vs its markdown source (generator re-derivation mismatch — regenerate the tree)")
        else:
            bad.append(f"{f}: process {pid} has no markdown workflow block (id-derivation changed or PA content removed without regeneration)")
        nodes = [e for t in ("startEvent", "endEvent", "userTask", "serviceTask") for e in p.iter(B + t)]
        nid = {e.get("id") for e in nodes}
        if sum(1 for e in nodes if e.tag == B + "startEvent") != 1:
            bad.append(f"{f}: {p.get('id')} does not carry exactly one startEvent")
        if sum(1 for e in nodes if e.tag == B + "endEvent") != 1:
            bad.append(f"{f}: {p.get('id')} does not carry exactly one endEvent")
        covered = set()
        for lane in p.iter(B + "lane"):
            for r in lane.iter(B + "flowNodeRef"):
                rid = (r.text or "").strip()
                covered.add(rid)
                if rid not in nid:
                    bad.append(f"{f}: {p.get('id')} lane refs non-node {rid}")
        bare = nid - covered
        if bare:
            bad.append(f"{f}: {p.get('id')} nodes without a lane: {sorted(bare)[:3]}")
        need_s = nid | {e.get("id") for e in p.iter(B + "lane")} | {e.get("id") for e in p.iter(B + "textAnnotation")}
        miss = need_s - shapes
        if miss:
            bad.append(f"{f}: {p.get('id')} missing BPMNShape for {sorted(miss)[:3]}")
        need_e = {e.get("id") for e in p.iter(B + "sequenceFlow")} | {e.get("id") for e in p.iter(B + "association")}
        miss = need_e - edges
        if miss:
            bad.append(f"{f}: {p.get('id')} missing BPMNEdge for {sorted(miss)[:3]}")
    for s in root.iter(BD + "BPMNShape"):
        bnds = [c for c in s if c.tag.endswith("}Bounds")]
        if len(bnds) != 1 or float(bnds[0].get("width")) <= 0 or float(bnds[0].get("height")) <= 0:
            bad.append(f"{f}: shape {s.get('id')} missing/invalid Bounds")
    for e in root.iter(BD + "BPMNEdge"):
        if not [c for c in e if c.tag.endswith("}waypoint")]:
            bad.append(f"{f}: edge {e.get('id')} has no waypoint")
    if "PLACEHOLDER_" in f.read_text(encoding="utf-8"):
        bad.append(f"{f}: unreplaced PLACEHOLDER_ residue")
if tot_procs != reg_rows:
    bad.append(f"bpmn/ carries {tot_procs} processes but the register holds {reg_rows} rows")
print(f"BPMN_TOTALS files={len(files)} processes={tot_procs}")
# ---- DMN tree ----
dfiles = sorted((ROOT / "dmn").rglob("*.dmn"))
tot_dec = 0
for f in dfiles:
    try:
        root = ET.parse(f).getroot()
    except ET.ParseError as e:
        bad.append(f"{f}: XML parse error: {e}"); continue
    if root.tag != D + "definitions":
        bad.append(f"{f}: root element {root.tag}"); continue
    ids = {e.get("id") for e in root.iter() if e.get("id")}
    decs = list(root.iter(D + "decision"))
    tot_dec += len(decs)
    shape_refs = {s.get("dmnElementRef") for s in root.iter(DD + "DMNShape")}
    for dec in decs:
        dt = dec.find(D + "decisionTable")
        if dt is None:
            bad.append(f"{f}: {dec.get('id')} has no decisionTable"); continue
        ins = dt.findall(D + "input"); outs = dt.findall(D + "output"); rules = dt.findall(D + "rule")
        if not ins or not outs or not rules:
            bad.append(f"{f}: {dec.get('id')} degenerate decisionTable"); continue
        for r in rules:
            if len(r.findall(D + "inputEntry")) != len(ins) or len(r.findall(D + "outputEntry")) != len(outs):
                bad.append(f"{f}: {r.get('id')} entry-count mismatch")
        if dec.get("id") not in shape_refs:
            bad.append(f"{f}: decision {dec.get('id')} has no DMNShape (would not render in a DRD)")
    for s in root.iter(DD + "DMNShape"):
        if s.get("dmnElementRef") not in ids:
            bad.append(f"{f}: DMNShape dmnElementRef {s.get('dmnElementRef')} unresolved")
print(f"DMN_TOTALS files={len(dfiles)} decisions={tot_dec}")
print(f"TOTALS register_rows={reg_rows} pa_files={len(pa_files)} errors={len(bad)}")
for b in bad:
    print("BAD|" + b)
PY
)
C71_BAD=$(echo "$CHECK71" | sed -n 's/^TOTALS .* errors=\([0-9]*\)$/\1/p')
# Part C (2026-09-15 thirtieth-wave consistency review): the role-coverage
# matrix is a third generated artifact whose only regression harness was the
# generator's own --check mode — never invoked by this validator. A PA
# Owner/Participants/RACI edit that regenerates nothing could strand the
# shipped matrix stale at the retired role coverage — the exact staleness
# class this check exists to catch for bpmn/dmn. --check IS the generator's
# own byte-compare, so invoking it here gives the matrix the same shipped-tree
# currency guarantee; the check count is unchanged (the arm lives in Check 71).
C71_RC_OUT=$(python3 "$REPO_ROOT/07-methodology/generate-role-coverage.py" --check 2>&1) && C71_RC_RC=0 || C71_RC_RC=$?
# Part D (2026-09-15 thirty-first-wave consistency review): the role-vocabulary
# census pin. The matrix --check above proves the artifact is current, but a
# batch that edits PA Owner cells (or the alias tables / the §5.3 register) and
# regenerates consistently would still move the role↔org resolution population
# silently. The census — generate-role-coverage.py --census, under build()'s
# own touch semantics — re-derives that population every run and it is pinned
# here as the adjudicated baseline — re-pointed 2026-09-15 by the role-vocabulary
# reconciliation (thirty-second wave, completed same day by direction: every
# recurring uncharted Owner form, every systematic abbreviation across all RACI
# surfaces, AND the single-workflow deep tail — 495 alias mappings plus 17
# semantically-mangled Owner cells rewritten in their PA files): ALL 5,427
# Owner cells now resolve through the resolution order (owner_uncharted = 0 —
# full role↔org consistency on the accountability surface); 5,125 distinct
# uncharted forms remain across participant/step prose (down from 10,829),
# the watchlist for future vocabulary governance. Adjudicated standing:
# direction A — 94 of the §5.3 register's 186 ex-IT titles with zero workflow
# touches — is by design (workflow presence is contracted at function level,
# every department has ≥1 resolved role; recorded in the TO §5.3 note).
# Any movement of these numbers must be a conscious re-adjudication with the
# baseline re-pointed (the Check-74 deferred-anchor pattern).
C71_CENSUS_OUT=$(python3 "$REPO_ROOT/07-methodology/generate-role-coverage.py" --census 2>&1) && C71_CENSUS_RC=0 || C71_CENSUS_RC=$?
C71_CENSUS_OK=0
case "$C71_CENSUS_OUT" in
  *"CENSUS workflows=5427 owner_resolved=5427 owner_uncharted=0 owner_uncharted_forms=0 uncharted_forms=5125"*) C71_CENSUS_OK=1;;
esac
if [ "${C71_BAD:-1}" -eq 0 ] && [ "$C71_RC_RC" -eq 0 ] && [ "$C71_CENSUS_RC" -eq 0 ] && [ "$C71_CENSUS_OK" -eq 1 ]; then
    B71=$(echo "$CHECK71" | sed -n 's/^BPMN_TOTALS files=\([0-9]*\) processes=\([0-9]*\)$/\1 \2/p')
    D71=$(echo "$CHECK71" | sed -n 's/^DMN_TOTALS files=\([0-9]*\) decisions=\([0-9]*\)$/\1 \2/p')
    ok "Generated trees validate structurally against the markdown corpus AND mirror the generator's content derivation: bpmn/ $(echo $B71 | cut -d' ' -f1) files / $(echo $B71 | cut -d' ' -f2) processes (one per confirmed-register row) and dmn/ $(echo $D71 | cut -d' ' -f1) files / $(echo $D71 | cut -d' ' -f2) decisions — well-formed XML, 1 start/1 end per process, full lane coverage, 1:1 diagram:plane, complete DI shapes/edges/bounds/waypoints, decision-table structure, DRD shape per decision, and every process's documentation/start-event-name/controls-annotation byte-equal to the generator's re-derivation from its PA markdown (content mirror added by the 2026-09-10 seventeenth-wave review after batch-24 shipped PA-133.1/.3's generated files stale at the retired 5,426 — structural counts were all still correct, so nothing else could see it), and the shipped role-coverage matrix byte-identical to generate-role-coverage.py --check's re-derivation from the PA RACI fields + tier register + official TO (third-generated-artifact arm added by the 2026-09-15 thirtieth-wave review — the matrix's only harness had been the generator's own --check, which the validator never ran), and the role-vocabulary census pinned at the adjudicated baseline (owner cells 5,427 resolved / 0 uncharted — full accountability-surface consistency achieved by the thirty-second-wave reconciliation, 2026-09-15; 5,125 distinct uncharted forms remain across participant/step prose as the governed watchlist — census arm added by the 2026-09-15 thirty-first-wave review so a batch that edits owners, aliases or the register and regenerates consistently still cannot move the resolution population silently)"
else
    error "Generated BPMN/DMN trees failed structural validation:"
    echo "$CHECK71" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
    if [ "$C71_RC_RC" -ne 0 ]; then
        echo "role-coverage --check:" 
        echo "$C71_RC_OUT" | sed 's/^/    /'
    fi
    if [ "$C71_CENSUS_RC" -ne 0 ] || [ "$C71_CENSUS_OK" -eq 0 ]; then
        echo "role-vocabulary census (pinned baseline moved — re-adjudicate and re-point):"
        echo "$C71_CENSUS_OUT" | sed 's/^/    /'
    fi
fi

# --- Check 72: Document version-chain monotonicity (repo-wide) ---
echo "--- Check 72: Version-chain monotonicity ---"
# The eleventh-wave consistency review (2026-09-07) found the AI-first operating
# guide carrying all eight batch-16-23 re-point clauses labeled 'Prior v1.1'-
# 'Prior v1.8' BENEATH a version header that never left '1.0 | Initial issue' —
# a priors-newer-than-live inversion that no rule read: methodology_index_hits
# passed because the index row's own '(v1.0' pin satisfied itself off the same
# stale footer (the wave-6 'anchor satisfying itself off history' failure mode,
# in its version-pin form). Every other maintained doc keeps its newest clause
# leading under the live version with a strictly decreasing Prior chain. This
# check pins that invariant repo-wide: for every .md with a '*Document Version:'
# footer, every 'Prior vN.M' on the footer line must be strictly below the live
# version and the chain strictly decreasing in document order — so the class is
# caught at the first inverted clause, not eight batches later. CHANGELOG and the
# generated bpmn//dmn trees are exempt (no versioned footers; the CHANGELOG is a
# historical record). The footer line only is scanned, so body-narrative 'Prior'
# mentions can never false-trigger the order rule.
CHECK72=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, sys
ROOT = sys.argv[1]
bad, checked = [], 0
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in ('.git', 'bpmn', 'dmn', '__pycache__')]
    for fn in filenames:
        if not fn.endswith('.md') or fn.startswith('CHANGELOG'):
            continue
        f = os.path.join(dirpath, fn)
        rel = os.path.relpath(f, ROOT)
        lines = open(f, encoding='utf-8').read().split('\n')
        fi = next((i for i, l in enumerate(lines) if l.startswith('*Document Version: ')), None)
        if fi is None:
            continue
        m = re.match(r'\*Document Version: (\d+)\.(\d+)', lines[fi])
        if not m:
            bad.append(f"{rel}:{fi+1}: unparseable '*Document Version:' header")
            continue
        checked += 1
        live = int(m.group(1)) * 1000 + int(m.group(2))
        priors = [(int(a) * 1000 + int(b), f"{a}.{b}")
                  for a, b in re.findall(r'Prior v(\d+)\.(\d+)', lines[fi])]
        for val, txt in priors:
            if val >= live:
                bad.append(f"{rel}:{fi+1}: 'Prior v{txt}' is at/above the live version "
                           f"v{m.group(1)}.{m.group(2)} (priors-newer-than-live inversion)")
        for i in range(len(priors) - 1):
            if priors[i][0] <= priors[i + 1][0]:
                bad.append(f"{rel}:{fi+1}: version chain not strictly decreasing at "
                           f"'Prior v{priors[i][1]}' -> 'Prior v{priors[i+1][1]}'")
print(f"TOTALS versioned_docs={checked} errors={len(bad)}")
# 2026-09-14 twenty-ninth-wave addition — CHANGELOG entry-letter integrity: the
# uncommitted structure-promotion session prepended entries reusing the letters
# (j)/(k)/(l) already taken by the committed twenty-fourth–twenty-sixth waves
# (committed letters ran to (n)), shipping three double-lettered entries that no
# rule read. Within each date the entry letters must be unique AND strictly
# descending down the file (entries are stacked newest-first), so a collision,
# a re-used letter, or a misordered insert all fire.
cl_path = os.path.join(ROOT, 'CHANGELOG.md')
if os.path.exists(cl_path):
    order = []
    for i, l in enumerate(open(cl_path, encoding='utf-8').read().split('\n')):
        m2 = re.match(r'^## (\d{4}-\d{2}-\d{2}) \(([a-z])\)(?:\s|$)', l)
        if m2:
            order.append((i + 1, m2.group(1), m2.group(2), l[:90]))
    by_date = {}
    for ln, date, letter, head in order:
        by_date.setdefault(date, []).append((ln, letter, head))
    for date, entries in by_date.items():
        letters = [e[1] for e in entries]
        for ln, letter, head in entries:
            if letters.count(letter) > 1:
                bad.append(f"CHANGELOG.md:{ln}: entry letter '({letter})' used more than "
                           f"once under {date} (collision: {head}…)")
        for i in range(len(entries) - 1):
            if letters[i] <= letters[i + 1]:
                bad.append(f"CHANGELOG.md:{entries[i + 1][0]}: entry letters not strictly "
                           f"descending newest-first under {date} "
                           f"('({letters[i]})' above '({letters[i + 1]})')")
for b in bad:
    print("BAD|" + b)
PY
)
C72_BAD=$(echo "$CHECK72" | sed -n 's/^TOTALS .* errors=\([0-9]*\)$/\1/p')
if [ "${C72_BAD:-1}" -eq 0 ]; then
    V72=$(echo "$CHECK72" | sed -n 's/^TOTALS versioned_docs=\([0-9]*\) .*/\1/p')
    ok "All $V72 versioned document footers carry a strictly decreasing Prior chain below the live version (guard added by the 2026-09-07 eleventh-wave consistency review — the AI-first operating guide had shipped all eight batch-16\u201323 re-point clauses labeled v1.1\u2013v1.8 beneath a version header that never left '1.0 | Initial issue', an inversion invisible to the index-pin rule because the pin satisfied itself off the same stale footer)"
else
    error "Document version-chain monotonicity violated:"
    echo "$CHECK72" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 73: Canonical integration-diagram twin-copy byte-identity ---
echo "--- Check 73: Integration-diagram twin-copy identity ---"
# The integration-architecture ASCII diagram lives in exactly two maintained copies:
# the canonical fenced block in data-volumes-and-integrations.md and a declared
# convenience duplicate in technical-guidelines.md §3.2 (whose own blockquote says:
# update the canonical version first). Waves 7, 9 and 11 of the consistency reviews
# each re-verified the two copies byte-identical BY HAND — no check ever read them —
# so an edit to one copy (or a partial copy-through) would ship silently, exactly the
# sibling-surface class the eighth and ninth waves closed elsewhere. This check
# extracts each file's fenced block carrying the 'INTEGRATION ARCHITECTURE' banner,
# requires exactly one such block per file, and asserts byte-identity every run.
CHECK73=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
files = ["01-model-company/data-volumes-and-integrations.md",
         "07-methodology/technical-guidelines.md"]
blocks = {}
for rel in files:
    text = open(os.path.join(ROOT, rel), encoding='utf-8').read()
    fences = re.findall(r'^```[a-zA-Z]*\n(.*?)^```', text, re.S | re.M)
    hits = [b for b in fences if 'INTEGRATION ARCHITECTURE' in b]
    if len(hits) != 1:
        print(f"BAD|{rel}: expected exactly 1 fenced block carrying the 'INTEGRATION ARCHITECTURE' banner, found {len(hits)}")
    else:
        blocks[rel] = hits[0]
if len(blocks) == 2:
    a, b = (blocks[files[0]], blocks[files[1]])
    if a != b:
        import difflib
        diff = next(d for d in difflib.unified_diff(a.splitlines(), b.splitlines(), lineterm='') if d.startswith(('+', '-')) and not d.startswith(('+++', '---')))
        print(f"BAD|integration diagram drifted: canonical ({files[0]}) vs convenience copy ({files[1]}) differ, first differing line: {diff[:120]}")
    else:
        print(f"TOTALS lines={len(a.splitlines())} identical=true")
PY
)
C73_BAD=$(echo "$CHECK73" | grep -c '^BAD|' || true)
if [ "${C73_BAD:-1}" -eq 0 ] && echo "$CHECK73" | grep -q '^TOTALS'; then
    L73=$(echo "$CHECK73" | sed -n 's/^TOTALS lines=\([0-9]*\) identical=true/\1/p')
    ok "Canonical integration diagram byte-identical across its two copies (data-volumes §2 ↔ technical-guidelines §3.2, $L73 lines; guard added by the 2026-09-07 twelfth-wave consistency review — waves 7/9/11 each re-verified the twin copies by hand because no check read them)"
else
    error "Integration-diagram twin-copy check failed:"
    echo "$CHECK73" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 74: Generated-tree coverage surfaces (README quick-stats + quoted tree rows) ---
echo "--- Check 74: Generated-tree coverage surfaces ---"
# Check 71 validates the bpmn/ and dmn/ XML against the markdown corpus, but the
# three human-facing coverage surfaces stayed unguarded: the bpmn/README and
# dmn/README quick-stats tables (waves 8/9/11 each re-derived 569/5,449/23,008/28,457
# and 40/79/339 BY HAND), and the quoted generated-tree figures on the root-README
# tree rows (bpmn/ '5,449 processes', dmn/ '79 decisions'), the two generator rows in
# the methodology tree, and the exec-summary tree rows. This check re-derives the
# counts from the shipped trees by the generators' own definitions (processes =
# <bpmn:process elements; tasks = userTask+serviceTask, the generator's task tags;
# flows = sequenceFlow elements; diagrams = BPMNDiagram elements; decisions/rules =
# <decision>/<rule> elements) and asserts every quoted figure. The dmn/README's
# deferred-rule-set count (197) is an extraction-property of the source corpus, not
# derivable from the XML — it is pinned as a required anchor so any change forces a
# conscious regeneration re-point.
CHECK74=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
bad = []
# --- derive from the trees (generator definitions) ---
b_files = b_procs = b_tasks = b_flows = b_diags = 0
for dp, _, fns in os.walk(os.path.join(ROOT, 'bpmn')):
    for fn in fns:
        if not fn.endswith('.bpmn'):
            continue
        b_files += 1
        t = open(os.path.join(dp, fn), encoding='utf-8').read()
        b_procs += len(re.findall(r'<bpmn:process[ >]', t))
        b_tasks += len(re.findall(r'<bpmn:(?:user|service)Task id=', t))
        b_flows += len(re.findall(r'<bpmn:sequenceFlow[ >]', t))
        b_diags += len(re.findall(r'<bpmndi:BPMNDiagram[ >]', t))
d_files = d_dec = d_rules = 0
for dp, _, fns in os.walk(os.path.join(ROOT, 'dmn')):
    for fn in fns:
        if not fn.endswith('.dmn'):
            continue
        d_files += 1
        t = open(os.path.join(dp, fn), encoding='utf-8').read()
        d_dec += len(re.findall(r'<decision id=', t))
        d_rules += len(re.findall(r'<rule id=', t))
truth = {'BPMN files': b_files, 'BPMN processes': b_procs, 'Tasks': b_tasks,
         'Sequence flows': b_flows, 'Diagrams (DI)': b_diags,
         'DMN files': d_files, 'Decisions': d_dec, 'Decision-table rules': d_rules}
if b_flows != b_tasks + b_procs:
    bad.append(f"tree invariant broken: sequence flows {b_flows} != tasks {b_tasks} + one task→end flow per process {b_procs}")
# --- bpmn/README quick-stats rows ---
bpmn_readme = open(os.path.join(ROOT, 'bpmn/README.md'), encoding='utf-8').read()
for metric, want in truth.items():
    if metric not in ('BPMN files', 'BPMN processes', 'Tasks', 'Sequence flows', 'Diagrams (DI)'):
        continue
    m = re.search(r'^\| ' + re.escape(metric) + r' \| ([\d,]+)', bpmn_readme, re.M)
    if not m:
        bad.append(f"bpmn/README.md: quick-stats row for '{metric}' missing")
    elif int(m.group(1).replace(',', '')) != want:
        bad.append(f"bpmn/README.md: '{metric}' says {m.group(1)}, tree holds {want}")
# --- dmn/README quick-stats rows ---
dmn_readme = open(os.path.join(ROOT, 'dmn/README.md'), encoding='utf-8').read()
for metric, want in (('DMN files', d_files), ('Decisions', d_dec), ('Decision-table rules', d_rules)):
    m = re.search(r'^\| ' + re.escape(metric) + r' \| ([\d,]+)', dmn_readme, re.M)
    if not m:
        bad.append(f"dmn/README.md: quick-stats row for '{metric}' missing")
    elif int(m.group(1).replace(',', '')) != want:
        bad.append(f"dmn/README.md: '{metric}' says {m.group(1)}, tree holds {want}")
if not re.search(r'^\| Deferred rule sets \(not faked\) \| 197 step-row rule sets \|$', dmn_readme, re.M):
    bad.append("dmn/README.md: required deferred-rule-set anchor row '| Deferred rule sets (not faked) | 197 step-row rule sets |' missing or changed — regeneration is the only legitimate way this figure moves")
# --- quoted tree-row figures: root README, exec summary ---
root = open(os.path.join(ROOT, 'README.md'), encoding='utf-8').read()
execs = open(os.path.join(ROOT, '01-model-company/executive-summary.md'), encoding='utf-8').read()
# fourteenth wave: the methodology-index generator rows are a fourth sibling surface
# quoting the same tree figures (569 files / 5,449 processes; 40 files / 79 decisions /
# 339 rules; 197 deferred) — waves 8–12 re-derived the root/exec/README-tree spots by
# hand but no check read the index rows
meth = open(os.path.join(ROOT, '07-methodology/README.md'), encoding='utf-8').read()
rowchecks = [
    (root, r'├── dmn/[^\n]*?(\d[\d,]*) decisions', d_dec, 'README.md dmn/ tree row', 'decisions'),
    (root, r'├── bpmn/[^\n]*?(\d[\d,]*) processes', b_procs, 'README.md bpmn/ tree row', 'processes'),
    (root, r'generate-bpmn\.py +BPMN 2\.0 generator[^\n]*?(\d[\d,]*) processes', b_procs, 'README.md generator row', 'processes'),
    (root, r'generate-dmn\.py +DMN 1\.3 generator[^\n]*?(\d[\d,]*) decisions', d_dec, 'README.md generator row', 'decisions'),
    (execs, r'├── bpmn/[^\n]*?(\d[\d,]*) processes', b_procs, 'executive-summary.md bpmn/ tree row', 'processes'),
    (execs, r'├── dmn/[^\n]*?(\d[\d,]*) decisions', d_dec, 'executive-summary.md dmn/ tree row', 'decisions'),
    (meth, r'generate-bpmn\.py[^\n]*?\((\d[\d,]*) files / (\d[\d,]*) processes', (b_files, b_procs), 'methodology-index generate-bpmn row', 'files/processes'),
    (meth, r'generate-dmn\.py[^\n]*?\((\d[\d,]*) files / (\d[\d,]*) decisions / (\d[\d,]*) rules', (d_files, d_dec, d_rules), 'methodology-index generate-dmn row', 'files/decisions/rules'),
]
for rc in rowchecks:
    text, pat, want, label, unit = rc
    m = re.search(pat, text)
    if not m:
        bad.append(f"{label}: no '(N {unit})' figure found")
    else:
        wants = want if isinstance(want, tuple) else (want,)
        got = tuple(int(g.replace(',', '')) for g in m.groups())
        if got != wants:
            bad.append(f"{label}: says {'/'.join(str(g) for g in got)} {unit}, tree holds {'/'.join(str(w) for w in wants)}")
if not re.search(r'generate-dmn\.py[^\n]*?197 ambiguous rule sets deferred', meth):
    bad.append("methodology-index generate-dmn row: required deferred-rule-set anchor ('197 ambiguous rule sets deferred') missing or changed — regeneration is the only legitimate way this figure moves")
print(f"TOTALS bpmn={b_files}/{b_procs}/{b_tasks}/{b_flows}/{b_diags} dmn={d_files}/{d_dec}/{d_rules} errors={len(bad)}")
for b in bad:
    print('BAD|' + b)
PY
)
C74_BAD=$(echo "$CHECK74" | sed -n 's/^TOTALS .* errors=\([0-9]*\)$/\1/p')
if [ "${C74_BAD:-1}" -eq 0 ]; then
    B74=$(echo "$CHECK74" | sed -n 's/^TOTALS bpmn=\([^ ]*\) .*/\1/p')
    D74=$(echo "$CHECK74" | sed -n 's/^TOTALS .* dmn=\([^ ]*\) errors=.*/\1/p')
    ok "Generated-tree coverage surfaces match the shipped trees: bpmn/ $(echo $B74 | tr '/' ' / ') (files/processes/tasks/flows/diagrams) and dmn/ $(echo $D74 | tr '/' ' / ') (files/decisions/rules) re-derived and asserted on bpmn/README + dmn/README quick-stats and the root-README, generator-row and exec-summary tree rows and — since the 2026-09-09 fourteenth-wave review — the methodology-index generator rows (incl. the 197 deferred anchor); dmn/README deferred anchor (197) pinned (guard added by the 2026-09-07 twelfth-wave consistency review — Check 71 reads the XML, but waves 8/9/11 each re-derived the coverage tables and quoted tree-row figures by hand because no check read them)"
else
    error "Generated-tree coverage surfaces disagree with the shipped trees:"
    echo "$CHECK74" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 75: Methodology-index Contents completeness vs disk ---
echo "--- Check 75: Methodology-index Contents completeness ---"
# The twelfth wave completed the methodology index by hand (adding the generate-bpmn.py /
# generate-dmn.py rows the table had predated) and recorded on the record that no check
# read the table's completeness vs disk (Check 63 guards the root-README tree only).
# This check closes that gap: every tool (.py) and document (.md, the index itself
# excluded) on disk under 07-methodology/ must carry a Contents row in
# 07-methodology/README.md, and every Contents-row link must resolve to a file on disk.
# The six .txt data artifacts (batch17/18/23-deferred-candidates.txt,
# placeholder-field-census.txt, semantic-audit-coverage.txt,
# unit-less-time-estimate-census.txt) are deliberately out of scope: raw worklist/census
# data, not tools or docs — the root-README tree lists them (Check 63 enforces that).
# A future script or doc cannot ship unlisted (the twelfth-wave defect class), and a
# renamed/deleted file cannot strand its index row.
CHECK75=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
meth_dir = os.path.join(ROOT, '07-methodology')
disk = set()
for dirpath, dirs, files in os.walk(meth_dir):
    dirs[:] = [d for d in dirs if d != '__pycache__']
    for fn in files:
        if fn.endswith(('.py', '.md')) and fn != 'README.md':
            disk.add(fn)
readme_full = open(os.path.join(meth_dir, 'README.md'), encoding='utf-8').read()
# scope to the Contents table proper (links stop before the Future Additions section;
# the dated history footer below it is frozen narrative and must not satisfy completeness)
cut = readme_full.find('## Future Additions')
readme = readme_full[:cut] if cut != -1 else readme_full
# link targets in the Contents table (all file links in the table are same-dir relative)
linked = set()
for m in re.finditer(r'\[[^\]]+\]\(([^)]+)\)', readme):
    target = m.group(1).strip()
    if target.startswith(('http://', 'https://', '#')):
        continue
    linked.add(os.path.basename(target.split('#')[0]))
bad = []
for f in sorted(disk - linked):
    bad.append(f"on-disk file 07-methodology/{f} has no Contents row in 07-methodology/README.md (ship the row with the file — the twelfth-wave completeness-defect class)")
for f in sorted(linked - disk - {'CHANGELOG.md'})[:20]:
    tgt = os.path.join(meth_dir, f)
    if not os.path.exists(tgt):
        bad.append(f"Contents row links to 07-methodology/{f}, which does not exist on disk")
print(f"C75_BAD={len(bad)} disk={len(disk)} linked={len(linked)}")
for b in bad:
    print('BAD|' + b)
PY
)
C75_BAD=$(echo "$CHECK75" | sed -n 's/^C75_BAD=\([0-9]*\).*/\1/p')
if [ "${C75_BAD:-1}" -eq 0 ]; then
    D75=$(echo "$CHECK75" | sed -n 's/^C75_BAD=.* disk=\([0-9]*\).*/\1/p')
    ok "Methodology-index completeness: all $D75 on-disk 07-methodology/ tools (.py) and docs (.md) carry Contents rows in 07-methodology/README.md and every Contents-row link resolves (guard added by the 2026-09-09 fourteenth-wave consistency review, closing the gap the twelfth wave documented when it completed the table by hand — no check read its completeness vs disk; the six .txt worklist/census data artifacts are out of scope, listed only in the root-README tree per Check 63)"
else
    error "Methodology-index Contents table disagrees with disk ($C75_BAD):"
    echo "$CHECK75" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 76: Domain gap-analysis companion figures vs canonical registers ---
echo "--- Check 76: Domain gap-analysis companion figures ---"
# The four domain gap-analysis companions (workflow-gap-analysis-finance/it/operations/people.md,
# shipped with gap-fill batches 8–11) are live navigation surfaces — referenced from
# workflow-gap-analysis.md, the classification register, the touchpoint map, the executive
# summary, the IT operating model and the sourcing model — yet no check ever read them. The
# 2026-09-09 fifteenth-wave consistency review found the whole family stranded at their
# authoring-time snapshots: every later gap-fill batch re-pointed each guarded surface it moved
# but nothing read the companions, so the finance §1 roster carried the pre-batch-10 per-VS
# counts behind a '30 dedicated value streams / 775 workflows' header (canonical: 29 / 785) and
# listed dedicated members VS-72/VS-158 as 'adjacent' besides, the IT doc scoped 'the Technology
# & Data family' at 9 value streams / 284 workflows where the canonical family is 13 / 390
# (family member VS-151 called 'adjacent', VS-115/VS-126/VS-137 omitted outright), the operations
# doc's five family buckets sat 1–12 below canon behind a 'four workflow-level families' slip
# (its own §2 said five) with bucket rosters crossing canonical family boundaries, and every
# 'now stands at' clause quoted the batch-8/9/10/11 totals. This check re-derives every quoted
# family figure from the canonical family tables (workflows/README.md, the Check-24-guarded
# source), every 'now stands at' / per-PA figure from the PA files' own ## W headers, re-derives
# family membership in both directions (a dedicated roster must equal the canonical member set;
# an adjacent VS must not be a member), resolves every W-token against the live header universe
# (## and ###), and requires each expected clause shape to be present — a deleted clause fails
# loudly rather than silently unguarding the surface.
CHECK76=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys, glob
ROOT = sys.argv[1]
wf = os.path.join(ROOT, '01-model-company', 'workflows')
errs = []

# Canonical family tables from workflows/README.md (Check 24 guards these vs the register).
rtext = open(os.path.join(wf, 'README.md'), encoding='utf-8').read()
fams = {}
for m in re.finditer(r'### ([\w\'&\-, ]+?) \(([-\d,]+) workflows\)\n\| VS \| Value Stream \| Workflows \|\n\|---\|---\|---\|\n(.*?)(?=\n\n)', rtext, re.S):
    name, total, table = m.group(1), int(m.group(2).replace(',', '')), m.group(3)
    members = {int(v): int(c.replace(',', '')) for v, c in re.findall(r'\[VS-(\d+)\]\(VS-\d+[^)]*\)\s*\|[^|]+\|\s*([\d,]+)\s*\|', table)}
    fams[name] = {'total': total, 'members': members}
    if sum(members.values()) != total:
        errs.append(f"canonical family table '{name}' sums to {sum(members.values())} but declares {total}")
vs_total = {}
for f in fams.values():
    for v, c in f['members'].items():
        vs_total[v] = c

# Live header universe (## and ###) and per-PA distinct-## counts.
uni = set()
pa_counts = {}
for f in glob.glob(os.path.join(wf, 'VS-*', 'PA-*.md')):
    txt = open(f, encoding='utf-8').read()
    uni |= set(re.findall(r'^#{2,3} (W\d+[A-Z]?)\.', txt, re.M))
    pa_counts[re.search(r'(PA-[\d.]+)', os.path.basename(f)).group(1)] = len(set(re.findall(r'^## (W\d+[A-Z]?)\.', txt, re.M)))

def Wtok(doc, text):
    # \\bW\\d\\w* captures every W-prefixed word-token, well-formed or not — a token that
    # merely fails the strict pattern (e.g. a 5-digit W18777) must be flagged as malformed,
    # not silently skipped by the strict regex (the rule-caught-its-own-author lesson).
    for m in re.finditer(r'\bW\d\w*', text):
        tok = m.group(0)
        mm = re.fullmatch(r'W(\d{1,4}[A-Z]?)(?:\.\d+[a-z]?)?', tok)
        if not mm:
            errs.append(f"{doc}: malformed W-token '{tok}' (does not match the W<id>[.step] form)")
        elif f'W{mm.group(1)}' not in uni:
            errs.append(f"{doc}: W-token {tok} does not resolve to any ##/### workflow header")

def check_now_stands(doc, text):
    n = 0
    for pat in (r'VS-(\d+)\s+now\s+stands\s+at\s+\*\*([\d,]+) workflows\*\*\s*\(([^)]+)\)',
                r'VS-(\d+)\s+at\s+\*\*([\d,]+) workflows\*\*\s*\(([^)]+)\)',
                r'VS-(\d+)\s+at\s+\*\*([\d,]+)\*\*\s*\(([^)]+)\)'):
        for m in re.finditer(pat, text):
            vs, tot, paren = int(m.group(1)), int(m.group(2).replace(',', '')), m.group(3)
            if 'PA-' not in paren:
                continue
            n += 1
            if vs not in vs_total:
                errs.append(f"{doc}: 'now stands at' clause names VS-{vs}, which is not in any canonical family")
            elif tot != vs_total[vs]:
                errs.append(f"{doc}: VS-{vs} 'now stands at' {tot:,} but the canonical register holds {vs_total[vs]:,}")
            for pa, cnt in re.findall(r'(PA-[\d.]+): ([\d,]+)', paren):
                if pa not in pa_counts:
                    errs.append(f"{doc}: 'now stands at' clause cites {pa}, which is not an on-disk PA file")
                elif int(cnt.replace(',', '')) != pa_counts[pa]:
                    errs.append(f"{doc}: {pa} declared at {cnt} but its PA file holds {pa_counts[pa]} ## W headers")
    return n

def roster(doc, text, fam_name, clause_pat, entry_pat):
    m = re.search(clause_pat, text, re.S)
    if not m:
        errs.append(f"{doc}: family-scoping clause for '{fam_name}' not found (clause shape is guard-anchored; do not delete or reword it without re-pinning Check 76)")
        return
    decl_vs, decl_tot, body = int(m.group(1)), int(m.group(2).replace(',', '')), m.group(3)
    canon = fams[fam_name]
    if decl_vs != len(canon['members']):
        errs.append(f"{doc}: '{fam_name} family' declares {decl_vs} dedicated value streams but the canonical family has {len(canon['members'])}")
    if decl_tot != canon['total']:
        errs.append(f"{doc}: '{fam_name} family' declares {decl_tot:,} workflows but the canonical family total is {canon['total']:,}")
    quoted = {int(v): int(c) for v, c in re.findall(entry_pat, body)}
    if quoted != canon['members']:
        for v in sorted(set(quoted) - set(canon['members'])):
            errs.append(f"{doc}: roster lists VS-{v} as a '{fam_name}' member but it is not in the canonical family")
        for v in sorted(set(canon['members']) - set(quoted)):
            errs.append(f"{doc}: canonical '{fam_name}' member VS-{v} is missing from the roster")
        for v in sorted(set(quoted) & set(canon['members'])):
            if quoted[v] != canon['members'][v]:
                errs.append(f"{doc}: roster counts VS-{v} at {quoted[v]} but the canonical register holds {canon['members'][v]}")

def adjacent(doc, text, label, fam_name):
    m = re.search(r'\*\*Adjacent [^*]*\*\*: (.*?)(?=\n\n)', text, re.S)
    if not m:
        errs.append(f"{doc}: adjacent-value-streams clause not found (clause shape is guard-anchored)")
        return
    body = m.group(1)
    ids = {int(v) for v in re.findall(r'VS-(\d+)(?!\.\d)', body)}
    for v in sorted(ids & set(fams[fam_name]['members'])):
        errs.append(f"{doc}: adjacent list names VS-{v}, a dedicated '{fam_name}' family member (members cannot be adjacent)")
    for v, _g, cnt in re.findall(r'VS-(\d+)\s+\(([^)]+?),\s*([\d,]+)\)', body):
        v, cnt = int(v), int(cnt.replace(',', ''))
        if v not in vs_total:
            errs.append(f"{doc}: adjacent entry VS-{v} is not in any canonical family")
        elif cnt != vs_total[v]:
            errs.append(f"{doc}: adjacent entry counts VS-{v} at {cnt:,} but the canonical register holds {vs_total[v]:,}")

# --- Finance ---
doc = 'workflow-gap-analysis-finance.md'
text = open(os.path.join(wf, doc), encoding='utf-8').read()
roster(doc, text, 'Finance', r'The \*\*Finance family\*\* — (\d+) dedicated value streams, \*\*([\d,]+) workflows\*\*:\s*(.*?)(?=\n- \*\*Adjacent)', r'VS-(\d+) \((\d+)\)')
adjacent(doc, text, 'finance-facing', 'Finance')
m = re.search(r'in the (\d+) Finance value streams \(([,\d]+) workflows\)', text)
if not m:
    errs.append(f"{doc}: §2 inventory clause not found (guard-anchored)")
elif int(m.group(1)) != len(fams['Finance']['members']) or int(m.group(2).replace(',', '')) != fams['Finance']['total']:
    errs.append(f"{doc}: §2 inventory clause declares {m.group(1)} value streams / {m.group(2)} workflows; canonical: {len(fams['Finance']['members'])} / {fams['Finance']['total']:,}")
if check_now_stands(doc, text) < 2:
    errs.append(f"{doc}: expected ≥2 'stands at' clauses quoting VS totals, found fewer (guard-anchored)")
Wtok(doc, text)

# --- IT ---
doc = 'workflow-gap-analysis-it.md'
text = open(os.path.join(wf, doc), encoding='utf-8').read()
roster(doc, text, 'Technology & Data', r'The \*\*Technology & Data family\*\* — (\d+) dedicated value streams, \*\*([\d,]+) workflows\*\*:\s*(.*?)(?=\n- \*\*Adjacent)', r'VS-(\d+) \((\d+)\)')
adjacent(doc, text, 'IT-facing', 'Technology & Data')
m = re.search(r'in the (\d+) Technology & Data value streams \(([,\d]+) workflows\)', text)
if not m:
    errs.append(f"{doc}: §2 inventory clause not found (guard-anchored)")
elif int(m.group(1)) != len(fams['Technology & Data']['members']) or int(m.group(2).replace(',', '')) != fams['Technology & Data']['total']:
    errs.append(f"{doc}: §2 inventory clause declares {m.group(1)} value streams / {m.group(2)} workflows; canonical: {len(fams['Technology & Data']['members'])} / {fams['Technology & Data']['total']:,}")
m = re.search(r'With ([,\d]+) Technology & Data workflows', text)
if not m:
    errs.append(f"{doc}: G2 'With N Technology & Data workflows' clause not found (guard-anchored)")
elif int(m.group(1).replace(',', '')) != fams['Technology & Data']['total']:
    errs.append(f"{doc}: G2 quotes {m.group(1)} Technology & Data workflows; canonical family total is {fams['Technology & Data']['total']:,}")
if check_now_stands(doc, text) < 1:
    errs.append(f"{doc}: expected a 'stands at' clause quoting the VS-27 total, found none (guard-anchored)")
Wtok(doc, text)

# --- People ---
doc = 'workflow-gap-analysis-people.md'
text = open(os.path.join(wf, doc), encoding='utf-8').read()
roster(doc, text, 'People', r'The \*\*People family\*\* — (\d+) dedicated value streams, \*\*([\d,]+) workflows\*\*:\s*(.*?)(?=\n- \*\*Adjacent)', r'VS-(\d+) [^(\n]*\((\d+)\)')
adjacent(doc, text, 'people-capability', 'People')
m = re.search(r'in the People family \(([,\d]+) workflows\)', text)
if not m:
    errs.append(f"{doc}: §2 inventory clause not found (guard-anchored)")
elif int(m.group(1).replace(',', '')) != fams['People']['total']:
    errs.append(f"{doc}: §2 inventory clause declares {m.group(1)} workflows; canonical family total is {fams['People']['total']:,}")
if check_now_stands(doc, text) < 2:
    errs.append(f"{doc}: expected ≥2 'stands at' clauses quoting VS totals, found fewer (guard-anchored)")
Wtok(doc, text)

# --- Operations (five canonical buckets) ---
doc = 'workflow-gap-analysis-operations.md'
text = open(os.path.join(wf, doc), encoding='utf-8').read()
ops_fams = ['Plan & Source', 'Make & Move', 'Sell & Serve', 'Asset & Infrastructure', 'Governance & Assurance']
for fam in ops_fams:
    pat = (r'\*\*' + re.escape(fam) + r'\*\* — ([,\d]+) workflows in (\d+) value streams( incl\. \*\*VS-23 Loss Prevention & Asset Protection\*\*)? \(([^)]*)\)\.')
    m = re.search(pat, text)
    if not m:
        errs.append(f"{doc}: bucket clause for '{fam}' not found or reshaped (clause shape is guard-anchored)")
        continue
    tot, nv, body = int(m.group(1).replace(',', '')), int(m.group(2)), m.group(4)
    canon = fams[fam]
    if tot != canon['total']:
        errs.append(f"{doc}: '{fam}' bucket declares {tot:,} workflows but the canonical family total is {canon['total']:,}")
    if nv != len(canon['members']):
        errs.append(f"{doc}: '{fam}' bucket declares {nv} value streams but the canonical family has {len(canon['members'])}")
    quoted = set()
    for tok in re.findall(r'VS-(\d+(?:/\d+)*)', body):
        quoted |= {int(x) for x in tok.split('/')}
    if quoted != set(canon['members']):
        for v in sorted(quoted - set(canon['members'])):
            errs.append(f"{doc}: '{fam}' bucket lists VS-{v} but it is not a canonical family member")
        for v in sorted(set(canon['members']) - quoted):
            errs.append(f"{doc}: canonical '{fam}' member VS-{v} is missing from the bucket")
msum = re.search(r'in the five families \(≈([,\d]+) workflows\)', text)
canon_sum = sum(fams[f]['total'] for f in ops_fams)
if not msum:
    errs.append(f"{doc}: §2 five-families inventory clause not found (guard-anchored)")
elif int(msum.group(1).replace(',', '')) != canon_sum:
    errs.append(f"{doc}: §2 inventory clause declares ≈{msum.group(1)} workflows; the five canonical families sum to {canon_sum:,}")
if check_now_stands(doc, text) < 3:
    errs.append(f"{doc}: expected ≥3 'stands at' clauses quoting VS totals, found fewer (guard-anchored)")
Wtok(doc, text)

print(f"C76_BAD={len(errs)} fams={len(fams)} universe={len(uni)}")
for e in errs:
    print('BAD|' + e)
PY
)
C76_BAD=$(echo "$CHECK76" | sed -n 's/^C76_BAD=\([0-9]*\).*/\1/p')
if [ "${C76_BAD:-1}" -eq 0 ]; then
    U76=$(echo "$CHECK76" | sed -n 's/^C76_BAD=.* universe=\([0-9]*\).*/\1/p')
    ok "Domain gap-analysis companions (finance/IT/operations/people) re-derived clean: every family roster, bucket total, inventory clause and 'now stands at' figure matches the canonical registers (${U76}-header W universe; guard added by the 2026-09-09 fifteenth-wave consistency review — the four companions were live navigation surfaces no check read, and every gap-fill batch after their batches 8–11 had re-pointed the guarded surfaces while stranding the companions' authoring-time snapshots)"
else
    error "Domain gap-analysis companion figures disagree with the canonical registers ($C76_BAD):"
    echo "$CHECK76" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

# --- Check 77: Sourcing-doctrine posture guard (two-tier canon) ---
echo "--- Check 77: Sourcing-doctrine posture guard (two-tier canon) ---"
# The 2026-09-14 two-tier doctrine enactment (Oracle EBS 12.2 named the platform of
# record; the best-of-breed buy tier eliminated — commits 8256ab1 / 356afc5 / fe57b44)
# re-pointed every guarded surface but stranded the posture prose on live surfaces no
# rule read: the executive summary still introduced 'a unified cloud ERP core provided
# by a theoretical software vendor, surrounded by best-of-breed edge products' with a
# 'Bought Edges' landscape table, the AI-first operating guide's §4.2 systems-of-record
# reference assignment still assigned execution state to 'The bought edge systems
# (WMS/TMS/WFM/FSM)' and payroll to 'statutory-core', its L3 reference-architecture
# layer still drew 'bought best-of-breed edges', the root-README tree row still called
# the OM 'hybrid: ERP core + BoB edges', and the process layer (VS-113's sourcing
# machinery, the sourcing model's own §1 list) still taught the retired three-way
# 'configure → buy → build' gate alongside operational PA bodies describing a 'unified
# cloud ERP'. This check pins the two-tier canon: the retired 'cloud ERP' posture
# literal cannot reappear in live prose anywhere (the sourcing model's §1 history
# clause recording what the v1.x model assumed, dated change-notes and the gap-analysis
# scenario table's authoring-time rows are the exempt record), the VS-113 sourcing
# machinery and PA-128.3 cannot re-adopt lowercase 'best-of-breed' vocabulary (the
# W5516 registered title keeps its case), the executive summary must carry the
# two-tier landscape anchors and never the retired vendor/BoB forms, the guide's two
# repaired assignment phrases cannot regress, and the assumptions register's A6.3
# ecommerce row must state the already-built canon.
# 2026-09-14 on-premises canon correction (user direction): Oracle EBS is an on-premises
# suite, not a cloud-based ERP — the blueprint README's Deployment-model row still offered
# 'colocation or OCI compute' with the hedged 'on-premises-grade' rationale, the
# architecture's Data-residency row said 'hosted private deployment', and
# technical-guidelines §2.1 (pre-selection-era rows) said 'HR/payroll can be cloud-hosted'
# and 'Asia-Pacific hosting recommended'. All trued to on-premises and pinned (part g);
# the retired literals are scoped per document because 'OCI' elsewhere is legitimate
# (PFRS 9 OCI; cXML/OCI punchout) and 'Cloud FinOps' is VS-135's registered title.
# 2026-09-14 twenty-second-wave review: one stranded live surface found — the IT
# gap-analysis companion's §1 scope line still read 'hybrid cloud ERP + best-of-breed
# edge + 2 in-house built products', the retired three-tier posture — and it escaped
# BOTH sweep arms (the 'cloud ERP' literal was split across a line break, invisible to
# the line-based probe; the best-of-breed sweep was scoped to VS-113 + PA-128.3).
# Repaired in place and the class closed: the 'cloud ERP' probe is now joined-text
# (line-break-proof, offset→line mapping preserved), the lowercase-best-of-breed
# sweep extends to the four domain gap-analysis companions, and the companion's
# repaired scope anchor is required present (part f).
# 2026-09-14 twenty-third-wave review: the cascade's own teaching surfaces — the
# wave-20 re-points fixed W5515/PA-128.3's gate prose but left the documents that
# DEFINE the gate teaching the retired three-exit order: the sourcing model's §2
# heading still read 'Unified Core, Bought Edges, Built Differentiators' with a 'three
# tiers' intro over its own two-tier table (the v3.0 footer had collapsed §2 to
# in-suite/build), its §12.2 stage-2 still routed 'vendor agent products = buy', the
# guide's Law 4 statement still said 'in that default order', §3.3 still taught an
# 'exactly three sourcing postures' estate with a '**Bought edge**' row holding the
# retired BoB rows (WMS/TMS/WFM/FSM), §5.1 still taught 'configure → buy → build',
# §7.3 stage-1 routed 'buy = vendor agent', §9.2's decision-rights row still read
# '(configure/buy/build)', the operating model's §2 principle 7 still taught 'Configure
# by default; buy before build' with the four-item appendix list (the model's §3.3
# mandates five), its §8 SIB row still read 'Configure/buy/build routing', and
# PA-128.3's W5512 Step 3 still taught 'vendor agent product = buy' two paragraphs
# above its own use-EBS→build risk bullet and control — repaired in place and the
# class closed: the retired gate-order literal joins the joined-text probe (a), and
# part (h) anchor-pins the repaired §2 heading/intro, §12.2 routing, Law 4, §3.3,
# §5.1, §7.3, §9.2, OM principle 7, OM SIB row and W5512 Step 3 + Touchpoints.
CHECK77=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys, glob
ROOT = sys.argv[1]
errs = []

# (a) repo-wide live-prose retirement of the 'cloud ERP' posture literal.
# 2026-09-14 twenty-second-wave hardening: the probe is joined-text — live lines are
# collapsed to one string and matched with r'cloud\\s+ERP' case-insensitively — because
# the first draft was line-based and the IT gap-analysis companion's scope line shipped
# the literal split across a line break ('hybrid cloud<newline>ERP + best-of-breed edge'),
# which sailed through every run until the wave-22 review joined the lines. Offset→line
# mapping preserved so a firing guard still points at the exact line. The sourcing-model
# §1 history clause and the gap-analysis pass-record table keep their exemptions.
for f in glob.glob(ROOT + '/**/*.md', recursive=True):
    rel = os.path.relpath(f, ROOT)
    if rel.startswith('CHANGELOG'):
        continue
    if os.path.normpath(rel) == os.path.normpath('01-model-company/workflows/workflow-gap-analysis.md'):
        continue  # scenario table = authoring-time snapshot; batch notes = dated record
    live_lines = []
    for i, line in enumerate(open(f, encoding='utf-8'), 1):
        if line.lstrip().startswith('*Date:') or 'Prior v' in line:
            continue
        live_lines.append((i, line.rstrip('\n')))
    joined = ' '.join(text for _, text in live_lines)
    if 'single-vendor unified cloud ERP' in joined:
        joined = joined.replace('single-vendor unified cloud ERP', '')  # sourcing-model §1 history: what the v1.x model assumed (retained record)
    for m in re.finditer(r'cloud\s+ERP', joined, re.I):
        pos = m.start()
        lineno = live_lines[0][0] if live_lines else 0
        acc = 0
        for idx, (i, text) in enumerate(live_lines):
            end = acc + len(text) + 1
            if pos < end:
                lineno = i
                break
            acc = end
        errs.append(f"{rel}:{lineno}: retired 'cloud ERP' posture literal in live prose (canon: Oracle E-Business Suite 12.2, the ERP core of record; joined-text probe — the literal may span a line break)")
    # 2026-09-14 twenty-third-wave extension: the retired three-exit gate order joins the
    # joined-text probe. Arrow-form only — the sourcing model's §1 history narration of the
    # 2026-09-03 posture uses the slash form '(configure / buy / build)' and stays exempt as
    # the dated record; the workflow-gap-analysis batch records are already skipped above.
    for m in re.finditer(r'configure\s+→\s+buy\s+→\s+build', joined):
        pos = m.start()
        lineno = live_lines[0][0] if live_lines else 0
        acc = 0
        for idx, (i, text) in enumerate(live_lines):
            end = acc + len(text) + 1
            if pos < end:
                lineno = i
                break
            acc = end
        errs.append(f"{rel}:{lineno}: retired three-exit gate order 'configure → buy → build' in live prose (canon: the ordered two-exit test — in-EBS → build; joined-text probe)")
    # 2026-09-14 twenty-fifth-wave extension: the capability-product vendor seat joins the
    # joined-text probe — a 'WMS Vendor' seat cannot exist under the in-suite WMS adoption
    # (Oracle WMS/MSCA; no WMS vendor exists to seat). Zero legitimate live uses repo-wide
    # (the CHANGELOG, the gap-analysis scenario table and the dated lines keep their
    # exemptions); the PA-37.1 terminal-hardware 'POS vendor' is the exempt commodity sense
    # and is handled per-document below, never here.
    for m in re.finditer(r'WMS [Vv]endor', joined):
        pos = m.start()
        lineno = live_lines[0][0] if live_lines else 0
        acc = 0
        for idx, (i, text) in enumerate(live_lines):
            end = acc + len(text) + 1
            if pos < end:
                lineno = i
                break
            acc = end
        errs.append(f"{rel}:{lineno}: retired capability-vendor seat 'WMS Vendor' in live prose (the WMS is in-suite Oracle WMS/MSCA under the two-tier doctrine — no WMS vendor exists to seat; joined-text probe)")

# (b) VS-113 folder + PA-128.3 + the four domain gap-analysis companions: lowercase
# 'best-of-breed' retired (W5516's registered title keeps its canonical case — so the
# match is case-sensitive, and the TOC/intra-file anchor slugs forced by that registered
# title are stripped before matching). 2026-09-14 twenty-second-wave extension: the
# companions join the sweep — the IT companion's §1 scope line carried the retired
# 'best-of-breed edge' tier and only the VS-113/PA-128.3 folder scope kept it invisible.
# Adjudicated out of scope (do not extend blindly): PA-138.1's 'single-source IFM vs
# best-of-breed' is outsourced-facilities-SERVICES vendor strategy (commodity procurement
# under the doctrine), not capability-product sourcing; the classification's W5516
# registered title and the dated batch/blockquote records keep their exemptions.
vs113 = os.path.join(ROOT, '01-model-company', 'workflows', 'VS-113-enterprise-architecture-application-portfolio-and-technology-strategy')
targets = sorted(glob.glob(os.path.join(vs113, '*.md')))
targets.append(os.path.join(ROOT, '01-model-company', 'workflows', 'VS-128-ai-ml-governance-responsible-ai', 'PA-128.3-ai-lifecycle-operations-assurance-value-realization.md'))
for _comp in ('workflow-gap-analysis-it.md', 'workflow-gap-analysis-finance.md', 'workflow-gap-analysis-operations.md', 'workflow-gap-analysis-people.md'):
    targets.append(os.path.join(ROOT, '01-model-company', 'workflows', _comp))
for f in targets:
    rel = os.path.relpath(f, ROOT)
    for i, line in enumerate(open(f, encoding='utf-8'), 1):
        if line.lstrip().startswith('*Date:') or 'Prior v' in line:
            continue
        probe = re.sub(r'\(#[^)]*\)', '', line)  # anchor slugs inherit the registered title's case
        if 'best-of-breed' in probe:
            errs.append(f"{rel}:{i}: retired lowercase 'best-of-breed' posture vocabulary in live prose (two-tier doctrine: in-suite/build; the W5516 registered title keeps its case)")

# (c) executive-summary.md: two-tier landscape anchors required in live prose (a deleted
# landscape row fails loudly even while a change-note still mentions the phrase); retired
# forms forbidden in live prose (the *Date: change-notes are the exempt record).
ex = os.path.join(ROOT, '01-model-company', 'executive-summary.md')
xlines = open(ex, encoding='utf-8').readlines()
live_x = [l for l in xlines if not (l.lstrip().startswith('*Date:') or 'Prior v' in l)]
xtext = ''.join(live_x)
for anchor in ('Oracle E-Business Suite 12.2', 'two-tier', 'Oracle WMS/MSCA', 'already-built'):
    if anchor not in xtext:
        errs.append(f"01-model-company/executive-summary.md: required two-tier landscape anchor '{anchor}' not found (guard-anchored)")
for i, line in enumerate(xlines, 1):
    if line.lstrip().startswith('*Date:') or 'Prior v' in line:
        continue
    for retired in ('Theoretical Software Vendor', 'Best-of-breed WMS', 'Bought Edges', 'Specialist vendors', 'best-of-breed'):
        if retired in line:
            errs.append(f"01-model-company/executive-summary.md:{i}: retired posture literal '{retired}' in live prose")
# thirty-fifth-wave arm: the landscape builds row must carry the post-audit
# dispatch scoping — the 2026-09-15 EBS-maximization audit re-pointed fit-gap
# D13 (the Field Service dispatch core is in-suite) but the summary row still
# taught the unqualified pre-audit build scope.
if 'the dispatch experience layer (Field Service dispatch core in-suite)' not in xtext:
    errs.append("01-model-company/executive-summary.md: the landscape builds row must scope dispatch to the experience layer with the Field Service dispatch core in-suite (guard-anchored; fit-gap D13)")
for i, line in enumerate(xlines, 1):
    if line.lstrip().startswith('*Date:') or 'Prior v' in line:
        continue
    if 'store workforce scheduling · dispatch |' in line:
        errs.append(f"01-model-company/executive-summary.md:{i}: retired unqualified dispatch build row in live prose (canon: the Field Service dispatch core is in-suite, fit-gap D13 — the build is the experience layer)")

# (d) ai-first-operating-guide.md: the two repaired §4.2/L3 phrases cannot regress in
# live prose; the footer clause that documents the repair quotes them as frozen history.
ag = os.path.join(ROOT, '07-methodology', 'ai-first-operating-guide.md')
for i, line in enumerate(open(ag, encoding='utf-8'), 1):
    if line.lstrip().startswith('*Date:') or line.lstrip().startswith('*Document Version:') or 'Prior v' in line:
        continue
    for retired in ('bought best-of-breed edges', 'The bought edge systems', 'payroll stays statutory-core'):
        if retired in line:
            errs.append(f"07-methodology/ai-first-operating-guide.md:{i}: retired assignment phrase '{retired}' in live prose")

# (e) assumptions register: the A6.3 ecommerce row must state the already-built canon.
asm = os.path.join(ROOT, '01-model-company', 'assumptions-and-design-decisions.md')
if 'A6.3 | Ecommerce platform | Already-built in-house platform' not in open(asm, encoding='utf-8').read():
    errs.append("01-model-company/assumptions-and-design-decisions.md: A6.3 ecommerce row must read 'Already-built in-house platform' (guard-anchored)")

# (f) the IT gap-analysis companion's repaired §1 scope line cannot regress (corrected-form
# anchor, scanned over live lines joined — the same line-break-proof reading as (a)).
_it = os.path.join(ROOT, '01-model-company', 'workflows', 'workflow-gap-analysis-it.md')
_it_live = ' '.join(l.rstrip('\n') for l in open(_it, encoding='utf-8')
                    if not (l.lstrip().startswith('*Date:') or 'Prior v' in l))
if 'the in-suite ERP core of record — Oracle E-Business Suite 12.2 under the two-tier doctrine' not in _it_live:
    errs.append("01-model-company/workflows/workflow-gap-analysis-it.md: repaired §1 scope anchor 'the in-suite ERP core of record — Oracle E-Business Suite 12.2 under the two-tier doctrine' not found in live prose (guard-anchored; the retired 'hybrid cloud ERP + best-of-breed edge + 2 in-house built products' form may not return)")

# (g) deployment-posture guard (2026-09-14 on-premises canon): Oracle EBS is an
# on-premises suite, NOT a cloud/SaaS ERP — the platform of record runs in
# BuildRight-controlled facilities. The three deployment-decision surfaces are pinned:
# the blueprint README's Deployment-model row, the architecture's Data-residency row,
# and technical-guidelines §2.1 (whose pre-selection-era rows said 'HR/payroll can be
# cloud-hosted' and 'Asia-Pacific hosting recommended'). The retired literals are
# scoped per document — 'OCI' elsewhere in the corpus is legitimate (PFRS 9 Other
# Comprehensive Income; the cXML/OCI punchout protocol) and must never be swept
# repo-wide. VS-135's registered 'Cloud FinOps' title and the INFRA team names are
# commodity-estate vocabulary, not deployment claims — out of scope.
_ebs_readme = os.path.join(ROOT, '02-oracle-ebs', 'README.md')
_ebs_readme_live = ' '.join(l.rstrip('\n') for l in open(_ebs_readme, encoding='utf-8')
                            if not (l.lstrip().startswith('*Date:') or 'Prior v' in l))
if 'On-premises deployment' not in _ebs_readme_live:
    errs.append('02-oracle-ebs/README.md: Deployment-model row must state \'On-premises deployment\' (guard-anchored)')
if 'on-premises suite, not a cloud/SaaS ERP' not in _ebs_readme_live:
    errs.append('02-oracle-ebs/README.md: Deployment-model rationale must state \'on-premises suite, not a cloud/SaaS ERP\' (guard-anchored)')
for _retired in ('OCI compute', 'on-premises-grade', 'Hosted private deployment'):
    if _retired in _ebs_readme_live:
        errs.append(f'02-oracle-ebs/README.md: retired deployment literal \'{_retired}\' in live prose (canon: on-premises, BuildRight-controlled facilities)')
_arch = os.path.join(ROOT, '02-oracle-ebs', 'ebs-platform-architecture.md')
_arch_live = ' '.join(l.rstrip('\n') for l in open(_arch, encoding='utf-8')
                      if not (l.lstrip().startswith('*Date:') or 'Prior v' in l))
if 'Fully under BuildRight control (on-premises deployment)' not in _arch_live:
    errs.append('02-oracle-ebs/ebs-platform-architecture.md: Data-residency row must read \'Fully under BuildRight control (on-premises deployment)\' (guard-anchored)')
_tg = os.path.join(ROOT, '07-methodology', 'technical-guidelines.md')
_tg_live = ' '.join(l.rstrip('\n') for l in open(_tg, encoding='utf-8')
                    if not (l.lstrip().startswith('*Date:') or 'Prior v' in l))
for _anchor in ('Core HR lives in the on-premises EBS suite',
                'runs **on-premises** in BuildRight-controlled facilities per'):
    if _anchor not in _tg_live:
        errs.append(f'07-methodology/technical-guidelines.md: required on-premises §2.1 anchor not found: {_anchor!r} (guard-anchored)')
for _retired in ('can be cloud-hosted', 'Asia-Pacific hosting recommended', 'No strict PH data residency requirement'):
    if _retired in _tg_live:
        errs.append(f'07-methodology/technical-guidelines.md: retired deployment literal \'{_retired}\' in live prose (canon: EBS on-premises, BuildRight-controlled facilities)')
# thirty-fifth-wave arm: the assumptions register's A6.2 row still carried the
# retired pre-selection deployment posture ('No strict PH data residency /
# Asia-Pacific hosting recommended') while CITING technical-guidelines §2.1 —
# the very row the on-premises canon re-pointed to the opposite stance. The
# part-(g) literal ban was scoped per document, so the assumptions doc was
# invisible to it; the corrected row is now anchored and the retired forms
# forbidden in this document too (joined-text read, line-break-proof).
_asm_live = re.sub(r'\s+', ' ', ' '.join(l.rstrip('\n') for l in open(asm, encoding='utf-8')
                                         if not (l.lstrip().startswith('*Date:') or 'Prior v' in l)))
for _anchor in ('On-premises deployment — data residency under BuildRight control',
                'RA 10173 data residency fully under'):
    if _anchor not in _asm_live:
        errs.append(f'01-model-company/assumptions-and-design-decisions.md: required on-premises A6.2 anchor not found: {_anchor!r} (guard-anchored; the row must agree with its own cited source, technical-guidelines §2.1)')
for _retired in ('Asia-Pacific hosting recommended', 'No strict PH data residency'):
    if _retired in _asm_live:
        errs.append(f'01-model-company/assumptions-and-design-decisions.md: retired deployment literal {_retired!r} in live prose (canon: EBS on-premises in BuildRight-controlled facilities; RA 10173 data residency fully under BuildRight control)')

# (h) twenty-third-wave: the sourcing-gate teaching surfaces are anchor-pinned against
# the two-exit canon (in-EBS → build; vendor agent products are not a sourcing exit).
# Required anchors scanned over live lines joined (the same line-break-proof reading as
# (a)/(f)); retired literals forbidden per document — 'Bought Edges' appears legitimately
# in dated records elsewhere (change-notes, the sourcing-model §1 history), so it is
# scoped to the sourcing model's live prose.
_sm = os.path.join(ROOT, '07-methodology', 'capability-sourcing-and-engineering-model.md')
_sm_live = ' '.join(l.rstrip('\n') for l in open(_sm, encoding='utf-8')
                    if not (l.lstrip().startswith('*Date:') or 'Prior v' in l))
_sm_live = re.sub(r'\s+', ' ', _sm_live)  # collapse indentation/line breaks — anchors are line-break-proof
if '## 2. Landscape Principle — In-Suite Core, Built Differentiators' not in _sm_live:
    errs.append("07-methodology/capability-sourcing-and-engineering-model.md: §2 heading must read the two-tier form 'Landscape Principle — In-Suite Core, Built Differentiators' (guard-anchored; the v3.0 footer collapsed §2 to in-suite/build — the retired 'Unified Core, Bought Edges' heading contradicted its own two-tier table)")
if 'partitions the landscape into two' not in _sm_live:
    errs.append('07-methodology/capability-sourcing-and-engineering-model.md: §2 intro must say the landscape partitions into two tiers (guard-anchored)')
if 'Landscape Principle — Unified Core' in _sm_live or 'partitions the landscape into three' in _sm_live:
    errs.append('07-methodology/capability-sourcing-and-engineering-model.md: retired three-tier §2 heading/intro form in live prose (guard-anchored)')
if 'vendor agent products are not a sourcing' not in _sm_live:
    errs.append('07-methodology/capability-sourcing-and-engineering-model.md: §12.2 stage-2 must route per the two-exit §3 gate — vendor agent products are not a sourcing exit (guard-anchored)')
_ag = os.path.join(ROOT, '07-methodology', 'ai-first-operating-guide.md')
_ag_live = ' '.join(l.rstrip('\n') for l in open(_ag, encoding='utf-8')
                    if not (l.lstrip().startswith('*Date:') or l.lstrip().startswith('*Document Version:') or 'Prior v' in l))
_ag_live = re.sub(r'\s+', ' ', _ag_live)
for _anchor in ('one two-exit gate — use the core, else build',
                '**Commodity services**',
                'The test is ordered: **use the core → build**',
                'Capability sourcing (use-the-core/build)'):
    if _anchor not in _ag_live:
        errs.append(f'07-methodology/ai-first-operating-guide.md: required two-tier anchor not found in live prose: {_anchor!r} (guard-anchored)')
for _retired in ('**Bought edge**', 'exactly three sourcing postures', 'both alternatives are demonstrably inadequate', 'buy = vendor agent', 'Capability sourcing (configure/buy/build)'):
    if _retired in _ag_live:
        errs.append(f'07-methodology/ai-first-operating-guide.md: retired gate/posture literal {_retired!r} in live prose (canon: two-exit gate — use the core, else build)')
_om = os.path.join(ROOT, '07-methodology', 'it-product-operating-model.md')
_om_live = ' '.join(l.rstrip('\n') for l in open(_om, encoding='utf-8')
                    if not (l.lstrip().startswith('*Date:') or l.lstrip().startswith('*Document Version:') or 'Prior v' in l))
_om_live = re.sub(r'\s+', ' ', _om_live)
for _anchor in ('Use EBS by default; build where EBS ships nothing',
                'Use-EBS/build routing for every capability (the ordered test: in-EBS → build',
                'a run-cost & talent plan (build), and a re-evaluation trigger'):
    if _anchor not in _om_live:
        errs.append(f'07-methodology/it-product-operating-model.md: required two-tier anchor not found in live prose: {_anchor!r} (guard-anchored)')
for _retired in ('Configure by default; buy before build', 'Configure/buy/build routing', 'default order configure', 'in the order configure'):
    if _retired in _om_live:
        errs.append(f'07-methodology/it-product-operating-model.md: retired gate literal {_retired!r} in live prose (canon: in-EBS → build)')
_w5512 = os.path.join(ROOT, '01-model-company', 'workflows', 'VS-128-ai-ml-governance-responsible-ai', 'PA-128.3-ai-lifecycle-operations-assurance-value-realization.md')
_w5512_live = ' '.join(l.rstrip('\n') for l in open(_w5512, encoding='utf-8')
                       if not (l.lstrip().startswith('*Date:') or 'Prior v' in l))
_w5512_live = re.sub(r'\s+', ' ', _w5512_live)
if 'platform-native in-suite automation = use EBS' not in _w5512_live:
    errs.append('workflows/VS-128-.../PA-128.3-...md: W5512 Step 3 must route per the two-exit gate (anchor: platform-native in-suite automation = use EBS) (guard-anchored)')
if 'vendor agent product = buy' in _w5512_live or 'configure/buy/build decision record' in _w5512_live:
    errs.append('workflows/VS-128-.../PA-128.3-...md: retired W5512 Step-3/Touchpoints gate literals in live prose (vendor agent product = buy; configure/buy/build decision record)')

# (i) twenty-fourth-wave: the cascade's own portfolio/decision-rights/enumeration
# surfaces — the configure-and-integrate archetype rename (sourcing model v3.0 /
# OM v3.11) never reached the OM §3.2 portfolio-table Type cells (rows 2–4 still read
# 'Stream-aligned (buy & integrate)' against the same document's §5.1 'configure-and-
# integrate teams (WLI, SSP, CCP)'), the two-exit gate never reached the OM §6.1 RACI
# row ('Capability sourcing decision (configure/buy/build)'), the W5515 Controls bullet
# still enumerated the retired 'exit/run plan' appendix against §3.3's 'Run-cost &
# talent plan (build)' and the wave-20-trued Step 2, the sourcing model's §9
# TCO-per-product row still carried the retired BoB-product cost class ('BoB products
# carry license + integration run cost' — a v1.0 relic the v3.0 re-word claim never
# covered), and the guide's §5.1 five-appendix enumeration kept the retired
# 'exit/run-cost plan' name. Anchors required over whitespace-normalized joined live
# text (line-break-proof, the (a)/(f)/(h) reading); retired literals forbidden per
# document — the guide's §5 posture-neutral doctrine family (the v1.11/wave-23
# adjudication), the sourcing-model §1/§8 history clauses and the OM §6.2
# vendor-commodity incident row stay exempt (per their adjudications).
for _retired in ('Capability sourcing decision (configure/buy/build)',
                 'Stream-aligned (buy & integrate)'):
    if _retired in _om_live:
        errs.append(f'07-methodology/it-product-operating-model.md: retired gate/archetype literal {_retired!r} in live prose (canon: use-EBS/build decision routing; the configure-and-integrate archetype per §5.1)')
for _anchor in ('Capability sourcing decision (use-EBS/build)',
                'Stream-aligned (configure & integrate)'):
    if _anchor not in _om_live:
        errs.append(f'07-methodology/it-product-operating-model.md: required two-tier anchor not found in live prose: {_anchor!r} (guard-anchored)')
_w5515 = os.path.join(ROOT, '01-model-company', 'workflows', 'VS-113-enterprise-architecture-application-portfolio-and-technology-strategy', 'PA-113.3-technology-strategy-innovation-governance-and-architecture-analytics.md')
_w5515_live = re.sub(r'\s+', ' ', ' '.join(l.rstrip('\n') for l in open(_w5515, encoding='utf-8')
                                           if not (l.lstrip().startswith('*Date:') or 'Prior v' in l)))
if 'no sourcing decision without the five mandatory appendices (IAP estimate, control-mapping, TCO, run-cost & talent plan, re-evaluation trigger)' not in _w5515_live:
    errs.append('workflows/VS-113-.../PA-113.3-...md: W5515 Controls bullet must enumerate the §3.3 five with the run-cost & talent plan (build) (guard-anchored)')
if 'exit/run plan' in _w5515_live:
    errs.append('workflows/VS-113-.../PA-113.3-...md: retired \'exit/run plan\' appendix literal in live prose (the buy exit does not exist; §3.3 appendix 4 is the run-cost & talent plan)')
if 'BoB products carry license' in _sm_live:
    errs.append('07-methodology/capability-sourcing-and-engineering-model.md: retired BoB-product cost class in the §9 TCO row live prose (no BoB capability products exist under the two-tier doctrine)')
if 'in-suite and vendor-commodity licenses carry license/support + integration run cost' not in _sm_live:
    errs.append('07-methodology/capability-sourcing-and-engineering-model.md: §9 TCO-per-product row must carry the two-tier cost-shape anchor (guard-anchored)')
if 'exit/run-cost plan' in _ag_live:
    errs.append('07-methodology/ai-first-operating-guide.md: retired exit-appendix literal in the §5.1 enumeration live prose (canon: the run-cost & talent plan (build); the buy exit does not exist)')
if 'TCO sheet, the run-cost & talent plan (build), and a re-evaluation trigger' not in _ag_live:
    errs.append('07-methodology/ai-first-operating-guide.md: §5.1 five-appendix enumeration must carry the run-cost & talent plan (build) anchor (guard-anchored)')

# (j) twenty-fifth-wave: the doctrine cascade's vendor-seat/routing stragglers —
# the gate order and the capability-product vendor seats on surfaces no rule read:
# the official TO's §8 SIB cadence row still routed 'Configure/buy/build routing per
# the capability sourcing model' (the gate the sourcing model's own §3 collapsed to
# two exits; the same class the wave-23/24 trues closed in the OM's §8 SIB row and
# §6.1 RACI row), the OM's DP team row still read 'Under the hybrid landscape' (the
# sibling IAP row reads 'Under the two-tier landscape'), W3092 still carried a 'WMS
# Vendor' participant/step-R seat against the in-suite Oracle WMS/MSCA adoption (its
# own Step 1 has IT configuring the dark-store WMS extension on the enterprise WMS),
# and W1181/W1489/the financing-partner step still routed POS software changes to
# 'POS Vendor'/'POS Vendor Support' seats against the register's already-built
# in-house POS row and the workflows' own 'per IT change management' text (SSP —
# Store Systems & POS — owns the POS estate per sourcing model §4/§5). The PA-37.1
# terminal-hardware 'POS vendor' (equipment install parallel to 'CCTV vendor'/ISP)
# stays legitimate: commodity procurement, the PA-138.1/automation-vendor precedent —
# so the POS-vendor ban is scoped to the three software-context files, never
# repo-wide; the WMS-vendor seat alone joins the repo-wide joined-text probe (a).
_to = os.path.join(ROOT, '01-model-company', 'optimal-table-of-organization.md')
_to_live = re.sub(r'\s+', ' ', ' '.join(l.rstrip('\n') for l in open(_to, encoding='utf-8')
                                       if not (l.lstrip().startswith('*Date:') or 'Prior v' in l)))
if 'Use-EBS/build routing per the capability sourcing model' not in _to_live:
    errs.append('01-model-company/optimal-table-of-organization.md: §8 SIB row must route per the two-exit gate — use-EBS/build (guard-anchored)')
if 'Configure/buy/build routing' in _to_live:
    errs.append("01-model-company/optimal-table-of-organization.md: retired three-exit gate literal 'Configure/buy/build routing' in live prose (canon: use-EBS/build — the buy exit does not exist)")
if 'Under the hybrid landscape' in _om_live:
    errs.append('07-methodology/it-product-operating-model.md: retired hybrid-landscape literal in the DP team row live prose (canon: the two-tier landscape, per the sibling IAP row)')
if 'Under the two-tier landscape the second steward carries dual-record harmonization' not in _om_live:
    errs.append('07-methodology/it-product-operating-model.md: DP team row must carry the two-tier-landscape anchor (guard-anchored)')
_w3092 = os.path.join(ROOT, '01-model-company', 'workflows', 'VS-93-dark-store-micro-fulfillment', 'PA-93.1-dark-store-site-strategy-design-network.md')
_w3092_live = re.sub(r'\s+', ' ', ' '.join(l.rstrip('\n') for l in open(_w3092, encoding='utf-8')
                                          if not (l.lstrip().startswith('*Date:') or 'Prior v' in l)))
if 'Automation Vendor / IT (in-suite WMS' not in _w3092_live or 'IT Apps, IT Integration, Automation Vendor, Dark Store Ops Mgr, Quality' not in _w3092_live:
    errs.append('workflows/VS-93-.../PA-93.1-...md: W3092 must commission the in-suite WMS by IT with the automation vendor only (anchors: participants row + step-3 R cell) (guard-anchored)')
if 'WMS Vendor' in _w3092_live:
    errs.append('workflows/VS-93-.../PA-93.1-...md: retired capability-vendor seat "WMS Vendor" in live prose (the WMS is in-suite Oracle WMS/MSCA; no vendor exists to seat)')
for _posf, _posr in ((os.path.join(ROOT, '01-model-company', 'workflows', 'VS-17-record-to-report', 'PA-17.3-tax-and-statutory.md'), 'PA-17.3'),
                     (os.path.join(ROOT, '01-model-company', 'workflows', 'VS-22-compliance-regulatory', 'PA-22.1-regulatory-permits-and-licenses.md'), 'PA-22.1'),
                     (os.path.join(ROOT, '01-model-company', 'workflows', 'VS-38-consumer-credit-financing', 'PA-38.1-consumer-financing-program.md'), 'PA-38.1')):
    _plive = re.sub(r'\s+', ' ', ' '.join(l.rstrip('\n') for l in open(_posf, encoding='utf-8')
                                         if not (l.lstrip().startswith('*Date:') or 'Prior v' in l)))
    if 'POS Vendor' in _plive:
        errs.append(f'workflows/.../{_posr}: retired capability-vendor seat "POS Vendor" in live prose (the POS estate is the already-built in-house platform — software changes route to SSP, Store Systems & POS; the PA-37.1 terminal-hardware vendor is the exempt commodity sense)')
    if _posr != 'PA-38.1' and 'SSP (Store Systems & POS — the in-house POS platform)' not in _plive:
        errs.append(f'workflows/.../{_posr}: W1181/W1489 participants must seat the in-house POS owner SSP (Store Systems & POS) (guard-anchored)')
    if _posr == 'PA-38.1' and 'IT / SSP (the in-house POS platform team)' not in _plive:
        errs.append('workflows/.../PA-38.1: the financing-partner step must route POS integration to IT / SSP (the in-house POS platform team) (guard-anchored)')

# (k) thirty-fifth-wave: the EBS-maximization audit's (2026-09-15) own landscape
# cascade — the audit corrected the fit-gap register (D13's dispatch core is
# in-suite Oracle Field Service; E3's build scoped to the genuinely-absent
# shift-scheduling/optimization layer with timecards retiring to OTL) and
# re-pointed the doctrine docs, but the surfaces that ASSERT the disposition
# still taught the unqualified pre-audit build scope: the blueprint README's
# §1 in-house-builds row ('installation dispatch' + 'EBS offers no credible
# substitute for any of them'), the executive-summary builds row, the profile
# §14.1 note + Store-workforce/Dispatch rows (the technician mobile app is
# Field Service's, not the build's), and the guide's L3 built-differentiator
# cell + §4.2 execution-state row. Anchors required over joined live text
# (line-break-proof, the (a)/(f)/(h) reading); retired forms forbidden per
# document — the OM §5/§9 'dispatch build' seat-ownership shorthand and the
# sourcing model §5 squad row stay exempt (the audit's own adjudication: CCP
# keeps product management of the narrowed build). The fit-gap §7 KPI row's
# stranded 68.4% joined ebs_blueprint_hits as a register re-derivation
# (Check 59), not here — it is a figure the register re-derives.
for _anchor in ('the dispatch experience layer (consumer appointment/route-optimization/contractor portal',
                'store workforce scheduling & time capture (the genuinely-absent shift-scheduling/optimization layer'):
    if _anchor not in _ebs_readme_live:
        errs.append(f'02-oracle-ebs/README.md: required §1 build-scope anchor not found in live prose: {_anchor!r} (guard-anchored; fit-gap D13/E3 post-audit canon)')
if 'installation dispatch, space-planning' in _ebs_readme_live or \
        'EBS offers no credible substitute for any of them' in _ebs_readme_live:
    errs.append('02-oracle-ebs/README.md: retired pre-audit §1 build-scope/rationale literals in live prose (the dispatch core is in-suite per D13 and timecards ride OTL — each build row is scoped to what the suite genuinely does not ship)')
_prof_live = re.sub(r'\s+', ' ', ' '.join(l.rstrip('\n') for l in open(os.path.join(ROOT, '01-model-company', 'model-company-profile.md'), encoding='utf-8')
                                         if not (l.lstrip().startswith('*Date:') or 'Prior v' in l)).replace('>', ' '))  # the §14.1 note is a blockquote — '>' markers stripped so anchors survive the wrapping (the ebs_blueprint_hits intro-blockquote reading)
for _anchor in ('the installation-dispatch core is **in-suite** — Oracle Field Service, fit-gap D13',
                'Store shift scheduling/optimization (the genuinely-absent layer',
                'Dispatch (Field Service core + experience-layer build)'):
    if _anchor not in _prof_live:
        errs.append(f'01-model-company/model-company-profile.md: required §14.1 exhaustion-audit anchor not found in live prose: {_anchor!r} (guard-anchored)')
for _retired in ('Dispatch (build)', 'Installation & home-service dispatch, technician mobile app',
                 'Payroll PH, store workforce scheduling and dispatch are'):
    if _retired in _prof_live:
        errs.append(f'01-model-company/model-company-profile.md: retired pre-audit disposition literal {_retired!r} in live prose (canon: the Field Service dispatch core is in-suite, fit-gap D13; the builds own the genuinely-absent layers only)')
for _anchor in ('workforce scheduling & the field-service dispatch experience layer',
                'built platforms (workforce scheduling, the dispatch experience layer)'):
    if _anchor not in _ag_live:
        errs.append(f'07-methodology/ai-first-operating-guide.md: required exhaustion-audit anchor not found in live prose: {_anchor!r} (guard-anchored; fit-gap D13 post-audit canon)')
for _retired in ('workforce scheduling & field-service dispatch platforms',
                 'built platforms (workforce/dispatch)'):
    if _retired in _ag_live:
        errs.append(f'07-methodology/ai-first-operating-guide.md: retired pre-audit build-scope literal {_retired!r} in live prose (canon: the dispatch core rides the in-suite field-service module — the build is the experience layer, fit-gap D13)')

print(f"C77_BAD={len(errs)}")
for e in errs:
    print('BAD|' + e)
PY
)
C77_BAD=$(echo "$CHECK77" | sed -n 's/^C77_BAD=\([0-9]*\).*/\1/p')
if [ "${C77_BAD:-1}" -eq 0 ]; then
    ok "Sourcing-doctrine posture guard clean: no retired 'cloud ERP' / best-of-breed / bought-edge literals in live prose (joined-text probe — split literals caught), no retired 'configure → buy → build' gate order anywhere live (joined-text probe), the executive summary carries the two-tier landscape anchors, the guide's §4.2/L3 assignments and Law-4/§3.3/§5.1/§7.3/§9.2 two-exit forms hold, the sourcing model's §2 heading/intro and §12.2 routing hold the in-suite/build canon, the OM's principle 7 + SIB row hold, W5512's Step 3 routes use-EBS → build, the A6.3 already-built canon is pinned, the IT gap-analysis companion's §1 scope anchor holds, the deployment canon is on-premises (EBS is not a cloud/SaaS ERP; blueprint README + architecture data-residency + tech-guidelines §2.1 pinned), and the twenty-fourth-wave portfolio/enumeration surfaces hold — the OM's §3.2 configure-and-integrate Type cells + §6.1 use-EBS/build RACI row, the W5515 Controls five-appendix enumeration with the run-cost & talent plan (build), the sourcing model's §9 two-tier TCO cost shape, and the guide's §5.1 run-cost & talent-plan appendix (guard added by the 2026-09-14 twentieth-wave consistency review — the doctrine enactment re-pointed every guarded surface while stranding the posture prose on surfaces no rule read; twenty-second-wave review repaired the IT companion's line-split scope line and hardened the probe against line breaks; on-premises canon correction pinned the three deployment-decision surfaces; twenty-third-wave review closed the cascade's own teaching surfaces — the sourcing model §2 heading/'three tiers' intro + §12.2 vendor-agent-products routing, the guide's Law 4 'default order' / §3.3 three-posture estate / §5.1 configure→buy→build / §7.3 buy=vendor-agent / §9.2 row, the OM's principle 7 + SIB row, and W5512's Step 3 + Touchpoints, with the retired gate-order literal joining the joined-text probe and all repaired surfaces anchor-pinned; twenty-fourth-wave review closed the cascade's own portfolio/enumeration surfaces — the OM §3.2 Type cells + §6.1 RACI row, the W5515 Controls five-appendix enumeration, the sourcing model's §9 TCO cost-shape row, and the guide's §5.1 appendix enumeration, all anchor-pinned; twenty-fifth-wave review closed the cascade's own vendor-seat/routing stragglers — the official TO's §8 SIB row re-pointed to use-EBS/build routing, the OM's DP row trued to the two-tier landscape, W3092's 'WMS Vendor' seat retired for the in-suite WMS (automation vendor + IT only), and the W1181/W1489/financing-partner 'POS Vendor' seats re-seated to SSP (Store Systems & POS), the in-house POS owner — with the WMS-vendor seat joining the repo-wide joined-text probe and the POS-vendor ban scoped to the three software-context files (the PA-37.1 terminal-hardware sense staying exempt as commodity procurement); thirty-fifth-wave review closed the EBS-maximization audit's own landscape cascade — the surfaces that ASSERT the disposition still taught the unqualified pre-audit build scope after the audit re-pointed fit-gap D13: the blueprint README §1 in-house-builds row (the dispatch experience layer scoped in, the 'no credible substitute for any of them' rationale retired), the executive-summary builds row, the profile §14.1 note + Store-workforce/Dispatch rows (the technician mobile device is Field Service's), the guide's L3 built-differentiator cell + §4.2 execution-state row, and the assumptions register's A6.2 deployment row (still carrying the retired 'No strict PH data residency / Asia-Pacific hosting recommended' posture while citing the §2.1 row the on-premises canon had re-pointed — the part-(g) per-document scope made it invisible), all anchor-pinned over joined live text with the retired pre-audit forms forbidden per document; the OM §5/§9 'dispatch build' seat-ownership shorthand and the sourcing model §5 squad row stay exempt per the audit's own adjudication (CCP keeps product management of the narrowed build))"
else
    error "Sourcing-doctrine posture violations against the two-tier canon ($C77_BAD):"
    echo "$CHECK77" | grep -E '^BAD\|' | sed 's/^BAD|/    /' || true
fi

echo ""
echo "=== Validation Complete ==="
echo "Errors: $ERRORS, Warnings: $WARNINGS"
if [ "$ERRORS" -eq 0 ]; then
    echo -e "${GREEN}All checks passed (warnings are informational)${NC}"
else
    echo -e "${RED}Some checks failed — review errors above${NC}"
    exit 1
fi
