#!/usr/bin/env python3
"""
reconcile-staffing-claims.py — Headcount-anchor & Volume-product reconciliation.

Consistency review #34 (2026-08-29) reconciled the staffing-team and role-count
claims scattered through the PA files' Staffing Implication / Time Estimate /
Volume prose against the canonical headcount registers —

  * `model-company-profile.md` §3.3 (18 HQ departments summing to 532 — the promoted structure of record, gap-filled 2026-09-18 by the actual-org benchmark; the 2026-09-14 promotion figure was 511),
    §4 (stores 200 × 29 = 5,800; DCs 4 × 150 = 600; total 6,932),
    §13.1 (Merchandising 43: 5 Category Managers, 10 Buyers, 6 Merchandise
    Planners/Allocators, 1 Pricing Manager, 4 Pricing Analysts, …);
  * `headcount-reality-check.md` (the historical gap record the rebalances
    closed — its pre-rebalance figures are NOT current state).

Three guards, all tuned to zero false positives on the adjudicated repo:

  1. retired literals — the superseded staffing figures the review repaired
     (pre-rebalance department totals, the stale role counts, the per-shift DC
     worker phrasing, the DSD per-store week/month slip) must not reappear;
  2. department-team equality — any "<Department> … team of N" claim for a
     canonical HQ department must quote that department's §3.3 total;
  3. Volume-row products — every explicit "A × B = C" (or "× D = E") product
     inside a `| **Volume** |` / `| **Frequency** |` field row must compute
     elementwise (ranges low×low / high×high);
  4. DC-catchment claims (2026-09-09 sixteenth-wave consistency review) — the
     per-DC catchment average is re-derived from the profile's §3.1 Total-Stores
     and §3.2 DC-table rows (200 ÷ 4 = 50) and every 'each DC serves ~N stores
     on average' / 'DCs each serving ~N stores' claim must equal it; the range
     canon is 20–80 (the §3.2 region/DC-role tables: Mindanao 60, Visayas 40,
     South-Luzon+NCR 80, North/Central 20) and the retired '~40 on average' /
     '(range: 20–60)' / '~40–50 stores' forms must not reappear. The review
     found the profile's own §3.2 operations bullet contradicting its DC3 row
     ('~40 on average (range: 20–60)' vs South-Luzon+NCR = 80), PA-26.1 citing
     the profile with the correct range but the stale ~40 average, and PA-04.2
     carrying '~40' and '~40–50' forms.

The same review armed the validator's use of this script (Check 51 now passes
--guard; previously the error branch was dead code, which is how two latent
volume-product checker false positives printed invisibly for months) and fixed
both false-positive classes: '+'-sum rows are now skipped by whole-row scan (the
PA-08.2 row carried its '+' before the product span), and parenthetical unit
annotations are stripped before factor extraction (the PA-28.3 row's 200 × 13 =
2,600 had been read as × 40 = 104,000).

Usage:  python3 reconcile-staffing-claims.py [--guard]     (exit 1 on any hit)

2026-09-23 eighty-sixth-wave review: the (ah) cascade's own switchboard/PA
residue — (a) the guard's own hit-messages still taught the retired (ad)-era
canon as current (the retired-HQ-active and retired-single-deferral messages
said 6,918/HQ 518 and 'two-deferral required'; re-pointed to 6,911/HQ 511 and
the three-deferral form); (b) PA-22.1's functions-table reconciliation recital
labeled the (x)-disablement endpoint 'active HQ 518' where the (x) canon is
525 (518 is the (ad) value; 'active HQ 518' joins the retired-HQ-active bans
and the corrected '— active HQ 525' anchor is required); (c) PA-30.3's bold
Annual-estimate summary line kept the retired ~13,836 beside its own re-based
~13,822 derivation — hours, not headcount, invisible to the headcount arms —
so the retired derived-figure arm bans '~13,836' on live PA/README lines and
requires the '~13,822 hours (annual reassessment)' anchor (the Check-71
CENSUS-pin contract).

2026-09-23 eighty-seventh-wave review: the guard's own dead pair-check — the
PA-34.1 laptop-refresh special case compared its anchor against the retired
'518 active HQ + DC office staff' form while the (ah) re-point had moved the
REQ_HQ_ACTIVE_ANCHORS entry itself to the 511 form, so the count-both-cells
arm (the step-1 + touchpoint pair the eighty-fifth wave added) could never
fire — proven by injection (stripping the touchpoint anchor left the guard
silent at 0 hits). The comparison re-pointed to the live '511 active HQ + DC
office staff' form; the same injection now fires 'found 1 of 2' at the exact
arm and the clean tree is silent.

2026-09-23 eighty-eighth-wave review: the pre-promotion sizing family the
(canon-digit) sweeps could not see — three live cells sizing their populations
at figures two or more IT/HQ generations retired, each invisible to the
retired-canon arms because the retired digits (360/50/30/5,800) are not in any
ban list (only the 6,9xx/5xx headcount forms are): (a) PA-19.4's W-training
delivery step still decomposed the training audience 'Store staff (5,800) /
DC staff (600) / HQ staff (~360)' — the HQ component at the pre-promotion
362-era figure beside store/DC cells already at canon, footing ~6,760 against
its own file's ~6,911 Volume rows (the sibling decompositions PA-40.2/VS-169
carry the annotated ~511 form); (b) PA-27.2's W55 DR staffing line still read
'part of the planned ~50 IT staff in W48' — the review-#34-era sizing (the
canon since moved 50 → 80 → 115 → the 122-FTE 17-team design, 108 active
post-(ad)/(ah)); (c) PA-27.3's W394 Volume still read '~30 IT staff' — the
2026-06-09 authoring figure, pre-dating every sizing generation. Repaired to
the annotated canon forms; the retired joined forms banned ('HQ staff (~360)',
'planned ~50 IT staff', '~30 IT staff') with the repaired-cell anchors
required (new retired-it-sizing arm). PA-19.5's W1383 resignation-volume
cell — the derived-band class one scope layer deeper: '~60–80 resignations/
month across all entities (based on ~15% annual turnover rate × ~5,800
employees ÷ 12)' derived the band from the STORE population under an
all-entities scope (5,800 was store-only even at the 2026-06-10 authoring,
when the company total was 6,757 — the cell escaped every sweep because its
digits are canon digits), and its 720–960/year volume echoed into W1384's
prorated-computations cell; re-derived at the active canon (15% × 6,911 ÷ 12
≈ 86.4 → ~85–90/month; ~1,020–1,080/year) with W1384's echo re-pointed to
the separations canon its own words name (1,200–1,600, matching W43); hours
and staffing tails re-footed. The retired forms banned and the corrected
anchors required (new retired-derived-volume arm).
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")
PROFILE = os.path.join(REPO, "01-model-company", "model-company-profile.md")

# canonical §3.3 HQ department totals (spot anchors used by prose claims)
# Re-based 2026-09-14 to the PROMOTED structure of record (TO v2.3 / profile
# v3.1 §3.3: HQ 532 (2026-09-18 actual-org gap-fill; the 2026-09-14 promotion figure was 511); IT 122 per the 17-team product model, OM v3.13).
RETIRED_HC_CANON = "6,932|6,925|6,918"   # 6,932 retired 2026-09-23 (x): Trade / Account Management
# disabled — prepared (registry CAP-B01); 6,925 retired 2026-09-23 (ad) and 6,918 retired
# 2026-09-23 (ah): the IT estate's TPS and OMO build squads deferred — prepared (sourcing
# register §4 amendments — routing is deterministic BOPIS, every sale a regular POS sale).
# The ACTIVE employee canon is 6,911 (HQ 511 active of the 532-role design). Version footers
# and dated history lines are exempt.

# 2026-09-23 seventy-ninth-wave review: the (x) sweep's own residue — live
# population cells still sizing off the RETIRED HQ-ACTIVE canon (532) after the
# same sweep had re-based their neighbors' 6,932 totals (the half-repaired-cell
# class, the seventy-seventh-wave precedent): PA-19.3's W5498 eligible-population
# cell, PA-40.2's allocation-methodology HQ component, PA-138.2's W4182 canteen
# Volume, PA-72.3's W2593 shared-services Volume, PA-34.1's laptop-refresh
# step/touchpoint pair, PA-22.1's functions-table preamble + reconciliation
# recital, PA-13.1's trade-desk staffing bullet and VS-169's README population
# decomposition. The banned joined forms name the retired active sense; the
# required anchors pin the repaired cells so a future census move re-fires the
# arm until consciously re-pointed (the Check-71 CENSUS-pin contract). The TO's
# design-register citations ('the 532/6,932 design', '532-role design') are the
# settlement's own vocabulary and do not match the joined forms.
RETIRED_HQ_ACTIVE_FORMS = [
    "~532 staff",
    "532 HQ staff",
    "532 HQ +",
    "+ ~532 HQ",
    "total HQ = 532",
    "532 HQ total",
    "532 HQ headcount",
    "~518 staff",
    "518 HQ staff",
    "518 HQ +",
    "+ ~518 HQ",
    "total HQ = 518",
    "518 HQ total",
    "518 HQ headcount",
    # 2026-09-23 eighty-sixth wave: the reversed-order form — PA-22.1's
    # functions-table reconciliation recital labeled the (x)-disablement
    # endpoint 'active HQ 518' where the (x) canon is 525 (518 is the (ad)
    # endpoint; the recital's own final clause correctly ends at 511).
    "active HQ 518",
    # 2026-09-23 eighty-eighth wave: the pre-promotion HQ family — PA-19.4's
    # training-audience decomposition sized the HQ component at the 362-era
    # figure beside store/DC cells already at canon (the sibling
    # decompositions PA-40.2/VS-169 carry the annotated ~511 form). Joined
    # forms only — bare '~360' is legitimate hour/day arithmetic elsewhere.
    "HQ staff (~360)",
    "~360 HQ staff",
]
REQ_HQ_ACTIVE_ANCHORS = [
    ("PA-19.3-workforce-management.md",
     "HQ corporate functions (~511 active staff, profile §3.3/§11.1"),
    ("PA-19.3-workforce-management.md",
     "Trade / Account Management disabled — prepared 2026-09-23 (x), the "
     "TPS build squad deferred — prepared (ad) and the OMO build squad "
     "deferred — prepared (ah), sourcing register §4 amendments, "
     "registry CAP-B01"),
    ("PA-40.2-project-cost-tracking.md",
     "Holdings/HQ: ~511 active per profile §3.3/§11.1"),
    ("PA-40.2-project-cost-tracking.md",
     "the TO's 532-role design retains the disabled—prepared Trade "
     "department — 2026-09-23 (x) — and the deferred—prepared TPS and OMO "
     "build squads — 2026-09-23 (ad)/(ah)"),
    ("PA-138.2-hard-and-soft-fm-service-operations.md",
     "HQ (~511 active staff, profile §3.3"),
    ("PA-138.2-hard-and-soft-fm-service-operations.md",
     "the TO's 532-role design retains the disabled—prepared Trade "
     "department and the deferred—prepared TPS and OMO build squads"),
    ("PA-72.3-shared-services-performance-analytics.md",
     "~511 active HQ staff across shared services"),
    ("PA-72.3-shared-services-performance-analytics.md",
     "Trade / Account Management disabled — prepared 2026-09-23 (x), the "
     "TPS build squad deferred — prepared (ad) and the OMO build squad "
     "deferred — prepared (ah), sourcing register §4 amendments, "
     "registry CAP-B01"),
    ("PA-34.1-non-merchandise-procurement.md",
     "511 active HQ + DC office staff"),
    ("PA-34.1-non-merchandise-procurement.md",
     "the TO's 532-role design retains the disabled—prepared Trade "
     "department and the deferred—prepared TPS and OMO build squads"),
    ("PA-22.1-regulatory-permits-and-licenses.md",
     "the active org is **HQ 511**"),
    ("PA-22.1-regulatory-permits-and-licenses.md",
     "the 2026-09-23 (ah) direction deferred the OMO build squad (7) — "
     "prepared with every sale completing as a regular POS sale"),
    # 2026-09-23 eighty-sixth wave: the functions-table reconciliation recital
    # pinned at the corrected (x)-endpoint value (the mislabeled 518 was the
    # (ad) canon — the CENSUS-pin contract, a future census move re-fires).
    ("PA-22.1-regulatory-permits-and-licenses.md",
     "re-cut to the 2026-09-23 (x) disablement — active HQ 525"),
    ("PA-13.1-customer-support-and-complaints.md",
     "511 active of the 532-role design"),
    ("PA-13.1-customer-support-and-complaints.md",
     "the disabled—prepared Trade department's 7, the deferred—prepared "
     "TPS build squad's 7 and the deferred—prepared OMO build squad's 7 "
     "all retained in the design"),
    # 2026-09-23 eighty-eighth wave: the training-audience decomposition's
    # HQ component pinned at the annotated two-canon form (the sibling
    # decompositions PA-40.2/VS-169 convention).
    ("PA-19.4-learning-and-development.md",
     "HQ staff (~511 active of the TO's 532-role design)"),
]
# 2026-09-23 eighty-fifth-wave review: the (ad) sweep's own annotation residue —
# seven live cells pair the 518/6,918 active canon with a design annotation
# naming ONLY the Trade department, explaining 7 of the 14 gap (6,932 − 6,918 =
# 7 trade + 7 TPS) — the (ad) pass extended PA-22.1's preamble but missed these
# (the half-repaired-cell class one clause deeper). The repaired cells' anchors
# above require the two-deferral form; the retired single-deferral suffixes are
# banned on live PA/README lines (line-scoped probes — the two-canon clauses the
# TO/registry/VS-169 settlement surfaces carry do not match).
RETIRED_SINGLE_DEFERRAL_FORMS = [
    "retains the disabled—prepared Trade department)",
    "Trade department — 2026-09-23 (x); promoted",
    "disabled — prepared 2026-09-23, registry CAP-B01",
    "and the deferred—prepared TPS build squad)",
    "and the deferred—prepared TPS build squad — 2026-09-23 (ad)",
]
REQ_HQ_ACTIVE_README_ANCHORS = [
    ("VS-169-employee-uniform-workwear-and-ppe-issuance-program/README.md",
     "~511 HQ active"),
    ("VS-169-employee-uniform-workwear-and-ppe-issuance-program/README.md",
     "the deferred—prepared TPS and OMO build squads (ad)/(ah)"),
]

# 2026-09-23 eighty-sixth wave: the retired DERIVED-hour figures — the (ah)
# sweep re-based PA-30.3's reassessment derivation line (×6,911 = ~13,822)
# but left the bold Annual-estimate summary line one line below at the
# retired ~13,836 (the literal half-repaired-cell class; the figure is
# hours, not headcount, so the retired-headcount arms cannot see it). The
# corrected anchor is required at the summary cell — a future census move
# re-fires the arm until consciously re-pointed (the Check-71 CENSUS-pin
# contract).
RETIRED_DERIVED_TE_FIGURES = ["~13,836"]
REQ_DERIVED_TE_ANCHORS = [
    ("PA-30.3-document-and-knowledge-management.md",
     "~13,822 hours (annual reassessment)"),
]

# 2026-09-23 eighty-eighth wave: the pre-promotion IT-sizing family — live
# cells sizing the IT department at figures two or more sizing generations
# retired (the canon: 122-FTE 17-team design, 108 active post-(ad)/(ah);
# 50 was the review-#34-era cell PA-27.2's W55 staffing line still quoted,
# 30 the 2026-06-09 authoring figure PA-27.3's W394 Volume still carried).
# The retired-canon arms cannot see these — the retired digits are not
# headcount-canon forms — so the class gets its own arm; the repaired cells'
# annotated-canon anchors are required (the Check-71 CENSUS-pin contract).
RETIRED_IT_SIZING_FORMS = [
    "planned ~50 IT staff",
    "~30 IT staff",
]
REQ_IT_SIZING_ANCHORS = [
    ("PA-27.2-infrastructure-and-platform.md",
     "part of the IT department's ~108 active of the 122-FTE 17-team design"),
    ("PA-27.3-cybersecurity-and-privacy.md",
     "~108 IT staff active (122-design"),
]

# 2026-09-23 eighty-eighth wave: the resignation-volume family — W1383's
# Frequency derived its band from the STORE population (~5,800) under an
# all-entities scope (store-only even at authoring; the company total was
# 6,757 then), and the 720–960/year volume echoed into W1384's
# prorated-computations cell. Re-derived at the active canon (15% × 6,911
# ÷ 12 ≈ 86.4/month); W1384's echo re-pointed to the separations canon its
# own words name (1,200–1,600, matching W43). The retired forms banned on
# live PA/README lines, the corrected anchors required.
RETIRED_DERIVED_VOLUME_FORMS = [
    "~5,800 employees ÷ 12",
    "60–80 resignations",
    "adds ~60–80 hours/month",
    "720–960 resignations",
    "720–960 prorated",
]
REQ_DERIVED_VOLUME_ANCHORS = [
    ("PA-19.5-separation-and-benefits.md",
     "~15% annual turnover rate × ~6,911 active employees ÷ 12"),
    ("PA-19.5-separation-and-benefits.md",
     "~1,020–1,080 resignations/year"),
    ("PA-19.5-separation-and-benefits.md",
     "~1,200–1,600 prorated computations for separations"),
]

DEPT_TOTALS = {
    "executive office": 7, "merchandising": 43, "finance & accounting": 62,
    "finance and accounting": 62, "finance": 62, "supply chain & logistics": 46,
    "supply chain and logistics": 46, "supply chain": 46,
    "information technology": 122, "it": 122, "human resources": 55, "hr": 55,
    "marketing": 30, "store operations": 24, "legal & compliance": 20,
    "legal and compliance": 20, "legal": 20, "internal audit & risk": 14,
    "internal audit and risk": 14, "internal audit": 14,
    "customer service / call center": 35, "call center": 35,
    "regional loss prevention": 27, "loss prevention": 27,
    "health, safety & environment": 13, "hse": 13,
    "quality management": 5, "facilities & real estate": 12,
    "sustainability / esg": 4, "strategy / corporate planning": 6,
    "trade / account management": 7,
}

# §13.1 merchandising role counts + other profile-anchored role sizes
ROLE_TOTALS = {
    "category managers": 5, "buyers": 10, "merchandise planners": 6,
    "pricing analysts": 4,
}

RETIRED_LITERALS = [
    # pre-rebalance department totals quoted in PA prose
    "IT team of ~28", "~28–30 IT headcount", "the recommended ~28–30 IT staff",
    "planned expansion to ~28–30", "IT staff of ~28",
    "Finance & Accounting team of 37", "team of 37 staff",
    "Legal & Compliance team of ~9", "Store Operations team of ~23",
    # stale merchandising role counts (§13.1: 4 analysts, 10 buyers, 5 CMs)
    "3 Pricing Analysts", "3 Pricing Analyst roles", "spread across 3 analysts",
    "10–12 Buyers", "10–12 buyers", "~10 Category Managers",
    "With 6 Category Managers", "÷ ~4 Category Managers",
    "existing 2 Merchandise Planners",
    # HSE: safety officers sit inside the 10-person team with nurse/wellness
    "~10–12 Safety Officers",
    # DC headcount is 600 (4 × 150) — no per-shift roster claims
    "workers per DC per shift",
    # DSD cadence is per store per MONTH (~500–600 receipts/month chain-wide)
    "DSD deliveries per store per week", "DSD deliveries/store/week",
    "DSD deliveries/week",
    # 2026-09-14 structure promotion (profile v3.0 / TO v2.3): the pre-promotion
    # HQ subtotal 362 retired in live PA/README prose — the promotion's corpus
    # sweep matched the ~6,762 total but stranded the 362 HQ-subtotal family
    # (PA-22.1's HQ-Departments table, PA-72.3/PA-138.2/PA-19.3 Volume rows,
    # PA-34.1 laptop-refresh cells, PA-13.1's trade register, VS-169's README).
    # The 362 canon survives ONLY in dated records (profile §3.3 history note,
    # TO §5.1 reference column, reality-check banner, *Date: footers) — none of
    # them PA files or VS READMEs.
    "362 HQ", "HQ = 362", "362 staff",
    "5-person Trade/Account Management register",
    "HSE 10, Quality 4",
]

DEPT_TEAM_RE = re.compile(
    r"\b(" + "|".join(re.escape(d) for d in
                      sorted(DEPT_TOTALS, key=len, reverse=True)) +
    r")\b[^.|\n]{0,40}?\bteam of ~?(\d+)", re.I)
TEAM_IN_RE = re.compile(
    r"\bteam of ~?(\d+)\s*(?:staff|people|personnel)?\s*(?:at HQ|in (?:the )?)?"
    r"[\s(]*(?:the )?\b(" + "|".join(re.escape(d) for d in
                                     sorted(DEPT_TOTALS, key=len, reverse=True)) +
    r")\b", re.I)

NUM = r"~?\d[\d,]*(?:\.\d+)?"
RANGE = r"(?:[–—-]\s*" + NUM + r")?"
QUANT = re.compile("(" + NUM + RANGE + r"\s*[KMB]?(?![A-Za-z]))")
PRODUCT_RE = re.compile(
    NUM + r"\s*" + RANGE + r"\s*(?:[A-Za-z-]+/)*(?:[A-Za-z-]+\s+){0,2}[A-Za-z-]+\s*×\s*" +
    NUM + r"\s*" + RANGE + r"(?:[^\n=+×]{0,60}?×\s*" + NUM + r"\s*" + RANGE +
    r")?\s*(?:[^\n=+×]{0,30}?)=\s*~?" + NUM + r"\s*" + RANGE +
    r"\s*[KMB]?(?![A-Za-z])")


def parse_range(text):
    ends = re.findall(r"(\d[\d,]*(?:\.\d+)?)\s*([KMB](?![A-Za-z]))?", text)
    if not ends:
        return None
    mult = {"k": 1e3, "m": 1e6, "b": 1e9}
    vals = [float(n.replace(",", "")) * mult.get(suf.lower(), 1)
            for n, suf in ends]
    return (vals[0], vals[-1])


def check_file(path, hits):
    text = open(path, encoding="utf-8").read()
    rel = os.path.relpath(path, REPO)
    for lit in RETIRED_LITERALS:
        for m in re.finditer(re.escape(lit), text, re.I):
            line = text[:m.start()].count("\n") + 1
            hits.append(("retired-literal", rel, line, lit))
    for m in DEPT_TEAM_RE.finditer(text):
        dept, n = m.group(1).lower(), int(m.group(2))
        canon = DEPT_TOTALS.get(dept)
        after = text[m.end():m.end() + 4]
        if canon and n != canon and not re.match(r"\s*[–-]\s*\d", after) \
                and not re.search(r"deploy|send|assign|field|audit crew",
                                  m.group(0), re.I):
            line = text[:m.start()].count("\n") + 1
            hits.append(("dept-team", rel, line,
                         f"'{m.group(0)}' — canonical §3.3 {dept} = {canon}"))
    for m in TEAM_IN_RE.finditer(text):
        n, dept = int(m.group(1)), m.group(2).lower()
        canon = DEPT_TOTALS.get(dept)
        after = text[m.end():m.end() + 4]
        if canon and n != canon and not re.match(r"\s*[–-]\s*\d", after) \
                and not re.search(r"deploy|send|assign|field|audit crew",
                                  m.group(0), re.I):
            line = text[:m.start()].count("\n") + 1
            hits.append(("dept-team", rel, line,
                         f"'{m.group(0)}' — canonical §3.3 {dept} = {canon}"))
    for m in re.finditer(r"^\| \*\*(?:Volume|Frequency)\*\* \|(.+)\|$", text, re.M):
        row = m.group(1)
        line = text[:m.start()].count("\n") + 1
        for pm in PRODUCT_RE.finditer(row):
            span = pm.group(0)
            if "+" in row:
                continue  # '+'-sum rows are outside the product checker's scope
                          # (whole-row skip per the sixteenth wave: the PA-08.2
                          # class carried its '+' BEFORE the product span, so the
                          # span-windowed skip missed it and read the sum's total
                          # as the product's claimed value)
            quants = [parse_range(q) for q in QUANT.findall(
                re.sub(r"\([^)]*\)", "", span))]  # parentheticals are unit
            # annotations ('(~40 categories)'), not factors — sixteenth-wave fix,
            # the PA-28.3 class had 200 × 13 = 2,600 read as × 40 = 104,000
            factors, claimed = quants[:-1], quants[-1]
            if not factors or any(q is None for q in quants):
                continue
            lo = hi = 1.0
            for flo, fhi in factors:
                lo *= flo
                hi *= fhi
            clo, chi = claimed
            scales = [1.0]
            if "week" in span and ("month" in row or "/mo" in row):
                scales += [4.0, 52 / 12]   # weekly factor, monthly claim
            if not any(0.95 * lo * sc <= clo <= 1.05 * hi * sc and
                       0.95 * hi * sc <= chi <= 1.05 * hi * sc
                       for sc in scales) \
                    and not (lo * 0.8 <= clo <= hi * 1.2):
                hits.append(("volume-product", rel, line,
                             f"'{pm.group(0)}' — elementwise {lo:g}–{hi:g} "
                             f"vs claimed {clo:g}–{chi:g}"))


def dc_catchment_hits():
    """2026-09-09 sixteenth-wave consistency review — the DC-catchment claims.
    The profile's own §3.2 tables give the catchments (Mindanao 60, Visayas 40,
    South-Luzon+NCR 80, North/Central 20 — the five region rows foot to the
    §3.1 store total), so the true average is stores ÷ DCs and the true range is
    20–80; the operations bullet nonetheless said '~40 stores on average
    (range: 20–60)', contradicting its own DC3 row, and PA-26.1 cited the profile
    with the correct range but the same stale ~40 average while PA-04.2 carried
    '~40' and '~40–50' forms. Re-derives the average from the §3.1 Total-Stores
    and §3.2 DC-table rows every run, requires the corrected anchor (average
    derived; the 20–80 range pinned as the hand-derived region-table truth),
    re-derives every 'each DC serves ~N stores on average' / 'DCs each serving
    ~N stores' claim in the profile and the PA files, and retires the stale
    range/average literals."""
    hits = []
    prof = open(PROFILE, encoding="utf-8").read()
    m = re.search(r"\|\s*\*\*Total Stores\*\*\s*\|\s*\*{0,2}~?([\d,]+)", prof)
    stores = int(m.group(1).replace(",", "")) if m else None
    dcs = len(re.findall(r"^\|\s*\*\*DC\d\s*[—-]", prof, re.M))
    if stores is None or dcs == 0:
        return [("dc-catchment", "model-company-profile.md", 0,
                 f"canonical inputs unparseable (stores={stores}, DCs={dcs})")]
    avg = stores // dcs
    anchor = f"Each DC serves ~{avg} stores on average (range: 20\u201380)"
    if anchor not in prof:
        hits.append(("dc-catchment", "model-company-profile.md", 0,
                     f'required corrected DC-catchment anchor missing: "{anchor}" '
                     f'(re-derived: {stores} stores \u00f7 {dcs} DCs = ~{avg}; range '
                     f'20\u201380 per the \u00a73.2 region/DC-role tables)'))
    retired = [
        "(range: 20\u201360)", "range: 20\u201360", "range 20\u201360",
        "~40 stores on average", "each serving ~40 stores",
        "serves ~40\u201350 stores",
    ]
    avg_re = re.compile(r"each DC serves ~(\d+) stores on average"
                        r"|DCs each serving ~(\d+) stores", re.I)
    for path in [PROFILE] + sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md"))):
        text = open(path, encoding="utf-8").read()
        rel = os.path.relpath(path, REPO)
        for lit in retired:
            for m in re.finditer(re.escape(lit), text, re.I):
                hits.append(("dc-catchment", rel, text[:m.start()].count("\n") + 1,
                             f"retired catchment literal \"{lit}\" (canonical: "
                             f"~{avg} average, range 20\u201380)"))
        for m in avg_re.finditer(text):
            n = int(m.group(1) or m.group(2))
            if n != avg:
                hits.append(("dc-catchment", rel, text[:m.start()].count("\n") + 1,
                             f"'{m.group(0)}' — derived {stores} stores \u00f7 {dcs} "
                             f"DCs = ~{avg} (range 20\u201380)"))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true",
                    help="exit 1 on any hit (validator mode)")
    args = ap.parse_args()
    hits = []
    files = sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md")))
    for f in files:
        check_file(f, hits)
    # 2026-09-14 structure-promotion wave: the VS READMEs join the guard with a
    # literal-only pass (VS-169's intro carried the pre-promotion
    # '~5,800 store + ~600 DC + ~362 HQ' cut after the sweep re-based its
    # totals; the full dept-team/volume arms stay PA-scoped — README prose
    # carries no Volume/Frequency field rows)
    readme_files = sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "README.md")))
    for f in readme_files:
        text = open(f, encoding="utf-8").read()
        rel = os.path.relpath(f, REPO)
        for lit in RETIRED_LITERALS:
            for m in re.finditer(re.escape(lit), text, re.I):
                line = text[:m.start()].count("\n") + 1
                hits.append(("retired-literal", rel, line, lit))
    # 2026-09-23 (x) trade-desk disablement: the retired 6,932 active-headcount
    # canon is banned on live PA lines (version-footed PA files are none, so the
    # whole file is live); the Sweep protocol restored it in 252 cells across 98
    # PA/README files — a future headcount move re-fires this arm until
    # consciously re-pointed (the Check-71 CENSUS-pin contract).
    for f in files:
        text = open(f, encoding="utf-8").read()
        rel = os.path.relpath(f, REPO)
        for m in re.finditer(RETIRED_HC_CANON, text):
            line = text[:m.start()].count("\n") + 1
            hits.append(("retired-headcount", rel, line,
                         "retired active canon — 6,918 since the TPS-squad "
                         "deferral, 2026-09-23 (ad); 6,932 retired at (x))"))
    for f in readme_files:
        text = open(f, encoding="utf-8").read()
        rel = os.path.relpath(f, REPO)
        for m in re.finditer(RETIRED_HC_CANON, text):
            line = text[:m.start()].count("\n") + 1
            hits.append(("retired-headcount", rel, line,
                         "retired active canon — 6,918 since the TPS-squad "
                         "deferral, 2026-09-23 (ad); 6,932 retired at (x))"))
    # 2026-09-23 seventy-ninth wave: the retired HQ-ACTIVE forms (532) banned on
    # live PA/README lines, and the repaired cells' two-canon anchors required —
    # the (x) sweep's own residue (see the module-head notes).
    for f in files + readme_files:
        text = open(f, encoding="utf-8").read()
        rel = os.path.relpath(f, REPO)
        for lit in RETIRED_HQ_ACTIVE_FORMS:
            for m in re.finditer(re.escape(lit), text, re.I):
                line = text[:m.start()].count("\n") + 1
                hits.append(("retired-hq-active", rel, line,
                             f"{lit} (retired HQ-active canon — HQ 511 active of the "
                             "532-role design since the OMO-squad deferral (ah); "
                             "518 retired at (ad), 532 at (x))"))
    text_by_base = {os.path.basename(f): open(f, encoding="utf-8").read()
                    for f in files}
    # 2026-09-23 eighty-fifth wave: the (ad) sweep's annotation residue — the
    # retired single-deferral design annotations banned on live PA/README lines
    # (each explained 7 of the 14 gap; the repaired cells carry the two-deferral
    # form the anchors above require).
    for f in files + readme_files:
        text = open(f, encoding="utf-8").read()
        rel = os.path.relpath(f, REPO)
        for lit in RETIRED_SINGLE_DEFERRAL_FORMS:
            for m in re.finditer(re.escape(lit), text):
                line = text[:m.start()].count("\n") + 1
                hits.append(("retired-single-deferral", rel, line,
                             f"{lit} (retired (x)-era annotation — the active "
                             "canon is 6,911/HQ 511 since the OMO build squad's "
                             "deferral (ah); the three-deferral design annotation "
                             "is required)"))
    for base, anchor in REQ_HQ_ACTIVE_ANCHORS:
        text = text_by_base.get(base)
        if text is None:
            hits.append(("missing-hq-active-anchor", base, 0,
                         f"anchor file not found: {base}"))
        elif anchor not in text:
            hits.append(("missing-hq-active-anchor", base, 0,
                         f'required two-canon anchor missing: "{anchor}"'))
        elif base == "PA-34.1-non-merchandise-procurement.md" and \
                anchor == "511 active HQ + DC office staff" and \
                text.count(anchor) < 2:
            hits.append(("missing-hq-active-anchor", base, 0,
                         "the laptop-refresh pair (step 1 + touchpoint) must both "
                         f"carry the anchor: \"{anchor}\" (found "
                         f"{text.count(anchor)} of 2)"))
    for relpath, anchor in REQ_HQ_ACTIVE_README_ANCHORS:
        f = os.path.join(WORKFLOWS, relpath)
        text = open(f, encoding="utf-8").read() if os.path.exists(f) else None
        if text is None:
            hits.append(("missing-hq-active-anchor", relpath, 0,
                         f"anchor file not found: {relpath}"))
        elif anchor not in text:
            hits.append(("missing-hq-active-anchor", relpath, 0,
                         f'required two-canon anchor missing: "{anchor}"'))
    # 2026-09-23 eighty-sixth wave: the retired derived-hour figures banned on
    # live PA/README lines, the corrected summary anchors required (the arm's
    # module-head note has the class).
    for f in files + readme_files:
        text = open(f, encoding="utf-8").read()
        rel = os.path.relpath(f, REPO)
        for lit in RETIRED_DERIVED_TE_FIGURES:
            for m in re.finditer(re.escape(lit), text):
                line = text[:m.start()].count("\n") + 1
                hits.append(("retired-derived-figure", rel, line,
                             f"{lit} (retired derived reassessment-hours figure "
                             "— ~13,822 at the 6,911 active canon, retired "
                             "2026-09-23 (ah))"))
    for base, anchor in REQ_DERIVED_TE_ANCHORS:
        text = text_by_base.get(base)
        if text is None:
            hits.append(("missing-derived-anchor", base, 0,
                         f"anchor file not found: {base}"))
        elif anchor not in text:
            hits.append(("missing-derived-anchor", base, 0,
                         f'required derived-figure anchor missing: "{anchor}"'))
    # 2026-09-23 eighty-eighth wave: the pre-promotion IT-sizing family banned
    # on live PA/README lines, the repaired cells' annotated-canon anchors
    # required (the arm's module-head note has the class).
    for f in files + readme_files:
        text = open(f, encoding="utf-8").read()
        rel = os.path.relpath(f, REPO)
        for lit in RETIRED_IT_SIZING_FORMS:
            for m in re.finditer(re.escape(lit), text, re.I):
                line = text[:m.start()].count("\n") + 1
                hits.append(("retired-it-sizing", rel, line,
                             f"{lit} (retired IT-sizing figure — the IT department "
                             "runs the 122-FTE 17-team product model at ~108 active "
                             "since the TPS (ad) and OMO (ah) build-squad deferrals, "
                             "OM v3.28)"))
    for base, anchor in REQ_IT_SIZING_ANCHORS:
        text = text_by_base.get(base)
        if text is None:
            hits.append(("missing-it-sizing-anchor", base, 0,
                         f"anchor file not found: {base}"))
        elif anchor not in text:
            hits.append(("missing-it-sizing-anchor", base, 0,
                         f'required annotated-canon anchor missing: "{anchor}"'))
    # 2026-09-23 eighty-eighth wave: the resignation-volume family (the
    # store-only base under the all-entities scope, and its W1384 echo)
    # banned on live PA/README lines, the corrected anchors required.
    for f in files + readme_files:
        text = open(f, encoding="utf-8").read()
        rel = os.path.relpath(f, REPO)
        for lit in RETIRED_DERIVED_VOLUME_FORMS:
            for m in re.finditer(re.escape(lit), text, re.I):
                line = text[:m.start()].count("\n") + 1
                hits.append(("retired-derived-volume", rel, line,
                             f"{lit} (retired resignation-volume family — W1383's "
                             "band derives at the 6,911 active canon: ~85–90/month, "
                             "~1,020–1,080/year; W1384's echo follows the W43 churn "
                             "canon 1,200–1,600)"))
    for base, anchor in REQ_DERIVED_VOLUME_ANCHORS:
        text = text_by_base.get(base)
        if text is None:
            hits.append(("missing-derived-volume-anchor", base, 0,
                         f"anchor file not found: {base}"))
        elif anchor not in text:
            hits.append(("missing-derived-volume-anchor", base, 0,
                         f'required derived-volume anchor missing: "{anchor}"'))
    # 2026-09-09 sixteenth-wave addition: the DC-catchment class (profile + PAs)
    hits.extend(dc_catchment_hits())
    for kind, rel, line, detail in hits:
        print(f"{kind}: {rel}:{line}: {detail}")
    print(f"reconcile-staffing-claims: {len(hits)} hit(s) across {len(files)} PA files "
          f"+ {len(readme_files)} VS READMEs")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
