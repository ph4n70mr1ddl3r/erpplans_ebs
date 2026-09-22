#!/usr/bin/env python3
"""
audit-semantic-anchors.py — semantic-sample anchor guard (validator Check 62).

Consistency review #44 (2026-08-29) performed the bounded semantic-correctness
sample audit: 40 workflows randomly drawn (seed 44), stratified 5-per-family
across the 8 value-stream families, audited in full — step-sequence logic,
per-step Duration plausibility vs the described activity, RACI role
feasibility vs the org chart, and statutory statements inside step prose.
36 of 40 verified semantically sound, including every statutory base checked
(DOLE 174 labor-only-contracting, RA 4136 PDL/restriction codes, DENR CCO
2013-24 lead-in-paint at 90 ppm, TRAIN-law payroll tables, point-of-sale VAT
recognition) and the volume chains (W1627's 280/store × 200 = 56,000/month and
2 min × 56,000 ≈ 22,400 h/yr; W31's 35,000 × 204 = 7.2M SKU-locations and
140,000 SKU-DC; W614's §1.1-anchored feed volumes). Four defects repaired:

  * W264 — Participants counts 'Category Manager (6), Buyer (8)' were stale
    vs the §13.1 register (5 Category Managers, 10 Buyers incl. Senior);
  * W1777 — the in-house-installment interest VAT basis 'as a financial
    service' was wrong (financial-service interest is VAT-exempt under the
    NIRC; the 12% holds because the interest forms part of the gross selling
    price);
  * W253 — '~10,000 new loyalty enrollments/month' was impossible against
    the data-volumes §1.1 customer-registration anchor (~150/day ≈ 4,500/
    month, of which loyalty sign-ups are the bulk);
  * W449 — the Controls section's operational line was a mis-paste of the
    regularization-risk prose, not a control; replaced with the actual
    DOLE-174 audit control.

Guard mode (--guard): the four repaired literals must not reappear, and any
Participants-field parenthetical count for a §13.1-anchored merchandising
role must equal the register (Category Managers 5, Buyers 10, Merchandise
Planners 5, Pricing Analysts 4).

Consistency review #49 (2026-08-29) lifted coverage toward the corpus-wide
bar: a corpus-wide statutory-citation census (110 distinct forms) plus a
200-workflow stratified batch (seed 5050, excluding the 481 already
audited; see semantic-audit-coverage.txt) brought full-read coverage to
681 of 5,363 workflows. Repairs: 4 "RR No./Revenue Regulation(s) No.
19-2020" spelling variants and 17 bare "RR 19-2020" transfer-pricing
mis-citations → RR 02-2013 (house TP canon); "RA 9160 as amended by
RA 10121" → RA 10365 and RA 11521 (AMLA amendments; RA 10121 is the
DRRM Act, whose two live DRRM usages are correct); W269's RACI R-column
realigned to the prose actors (five steps); W2141's quarterly
warranty-partner review given an internal Accountable (CFO, not the
external Insurance Partner); 11 "BFS"/"BFSR" spots → BPS / DTI-BPS (the
Bureau of Philippine Standards' acronym is and was BPS — including the
inverted "(BFS, formerly BPS)" note — and "DOE Bureau of Fire Standards
and Regulations" does not exist; VS-175 anchors cylinder re-qualification
to DTI-BPS per RA 11592). Each retired literal above is teeth-verified.

Consistency review #50 (2026-08-29) added the general keyword-quote integrity
rules after the 104-workflow batch-7 read exposed the clip family at its true
extent: every `System … of "QUOTE" (replaces manual Step N)` bullet must quote
text that (a) actually appears in the referenced step's Activity cell
(containment — catches the 50 review #45/#47 '-logy' mis-repairs that wrote
"technology" where the step word was Metrology/methodology/typology/toxicology/
genealogy/apology) and (b) appears at a word boundary in at least one
occurrence (catches the 884 mid-word clips: account(s)/discount(s)→count(s),
profile→file, catalog→log, center→enter, analogous→logous, … — the class the
exact-literal clip regexes had only piecemeal covered). Hand-authored
noun-phrase summary bullets (adjudicated, semantically sound vintage style)
are allowlisted per (file, workflow).
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

RETIRED_LITERALS = [
    "Category Manager (6), Buyer (8)",
    "subject to VAT (12%) as a financial service",
    "~10,000 new loyalty enrollments/month",
    "operational: regularization of thousands of workers",
    "| Participants (field) |",
    "200 stores × ~5,000 replenishment orders/month",
    "**Absb-erosion risk**",
    "(DOLE DO 174 Compliance)",
    "DTI DAO 2",
    # "RR 19-2020" re-scoped in #66 — it is a real TP-documentation issuance legitimately
    # supplementing RR 02-2013; only the bare "per RR 19-2020" mis-citation (without the
    # RR 02-2013 anchor) is retired
    "per RR 19-2020)",
    "per RR 19-2020.",
    "No. 19-2020",
    # review #74 (batch 28) REVERSED review #49's own adjudication per the #22/#68
    # precedent: #49 retired "RA 11199" and swept SSS cites to "RA 11111" — backwards.
    # RA 11199 IS the Social Security Act of 2018 (signed 2019-02-07; LawPhil + SSS
    # official site, web-verified 2026-08-30); RA 11111 is the Farm Tourism Development
    # Act. The two #49-era spots were re-trued to RA 11199 and the literal flipped.
    "RA 11111",
    "per DAO 198",
    "amended by RA 10121",
    "DTI/BFS",
    "BFS/DTI",
    "DENR/BFS",
    "(BFS, formerly BPS)",
    "PS Mark from BFS",
    "BFS may cite",
    "/BFSR",
    "Bureau of Fire Standards",
    "to HR. | Store Manager | HR Admin |",
    "in the system. | Security Guard |",
    "attendance profile. | Vendor Account Mgr |",
    "their payroll. | Store Manager | HR Admin |",
    "upon offboarding. | HR Admin | HR Director |",
    "| VP Merchandising | Insurance Partner |",
    # review #50 batch-7 repairs
    "1 LP analyst per region (~10–12 LP analysts chain-wide)",
    "Supply Chain team (31 at HQ)",
    "(personnel safety logs)",
    "~20–30 RFQs per month",
    "× 10 groups = 5 hours/day",
    "~5–10 tonnes of recyclable material per store/month",
    # review #51 batch-8 repairs
    "- operational: as evidence",
    "- operational: (eFPS) experiences frequent downtime",
    "- operational: is not always accessible or up-to-date",
    "NOLCO carryforward period is 3 years for small taxpayers",
    "Labor Code Article 294",
    "130% for rest days and holidays",
    "PHP 500K–20M; represents ~5–8% of total revenue",
    "SALSBAC",
    "archived accounting data (W15.3)",
    "~100–150 new hires",
    "~200 new hires/month",
    "~15–25 new hires/month",
    "1.5 hours × 4,500 employees",
    "- **Total: ~140–160 hours/year**",
    "(18 regular holidays",
    # review #52 batch-9 repairs
    "Store staff (6,000)",
    "~35-person Finance team",
    "instead of 0.00236, a small rounding error",
    "- operational: and physical reality",
    "| IT Auditor | BPO | 2 days |",
    "~500–800 qualifying transactions/day",
    "(10th and 25th of following month)",
    "per W1324 (DOLE DO 174 compliance)",
    "notice per DO 174 requirements",
    "~1.2–1.5 GWh/store",
    "175,000–220,000 tonnes",
    "~1M loyalty members",
    "~1–2 per store/month",
    "D.O. 53-04",
    # review #53 batch-10 repairs
    "General Affiliate Notice",
    "(GIS, AFS, GAN",
    "10-20 per store per day",
    "2,000-4,000 orders/day",
    "- operational: to file public financial statements",
    "~150–250 exceptions/week",
    "30-person Supply Chain team",
    "~84,000 returns/month",
    "~84,000 product returns per month",
    "(double the chain average)",
    "~55 license expirations/year",
    "55% of revenue from ~600,000 loyalty members",
    "per RA 9275",
    "RA 9275 refrigerant",
    "ODS/RA 9275",
    "transfer-prricing",
    # review #54 batch-11 repairs
    "30 staff × 200 stores",
    "~600–800 separations/year",
    "~50–70 separations/month",
    "≈ 550–730 hours/year",
    "~200–300 new vendor assessments/year",
    "DIY segment (55% of revenue)",
    "~60 stores in typhoon-prone Visayas",
    # review #55 batch-12 repairs
    "~200–400 customer complaints per store per month",
    "~2,800 in-store return refunds",
    "~5,000–6,000 refund transactions/month",
    "~50–80 off-cycle payments/month",
    "~800–1,000 active contracts",
    "~5–10 active sabbaticals",
    "assuming 5-10 active programs",
    "~15–20 active 3PL contracts",
    "(15–20 providers × 2–3 hours",
    "15–20 × 3–5 hours = 45–100 hours",
    "~3,000–4,400 SKU-location",
    "~PHP 3–5M in fixtures/equipment",
    "~12 categories × tens of attributes",
    # review #56 batch-13 repairs
    "~20–40/DC/month",
    "~1,825 hazmat receiving events",
    "= ~304 hours/year",
    "= ~520 hours/year",
    # "1601-E," retired in #56, superseded by the structural LEGACY_FORM rule (#60)
    "(~25,000–50,000 total)",
    "per DOLE 174",
    "(DOLE Department Order 174) distinguishes",
    "~150 DC staff on duty per shift",
    "~2–3 hours/day at 30–40 selections",
    "= ~2,000 store-hours/month",
    "~5 hours/month on daily reconciliation",
    "~12,000–15,000 store-hours/year",
    "5-day standard onboarding",
    "~250–450 hours/year",
    "~15 min/day per store on pallet sorting",
    "~250–350 component structures/year",
    "~20–30 component structures/month",
    "× 3 hours = ~60 hours/quarter",
    "~15–20 days/quarter",
    "~400–500 deliveries/day",
    "**~360 hours/year**",
    "revertion",
    "ERB",
    # review #58 batch-14 repairs
    "~90–110 hours/week",
    "3–4 orders/store/day",
    "~115 home deliveries/DC/day",
    "~500–800 new barcodes/month",
    "~230 person-hours/month",
    "~15–20 per store per day",
    "~40–50 rent escalations/year",
    "~1,500–2,500 hours/month",
    "~400–500 empty return trips",
    "Monthly; ~20 vehicles",
    # "~1,000 dealer grades" withdrawn in review #62 — W5385's ~1,000-active-dealer anchor
    # supports one-grade-per-dealer; the #58 300–800 basis is superseded
    # review #59 batch-15 repairs
    "All store staff (30/store)",
    "PHP 150,000–300,000/month in penalties",
    "~5,000–10,000 catalog updates per year",
    "= 6,000 person-hours/year",
    "catalog review is 30% of role",
    # "~8,500–9,500 invoices" withdrawn in review #67 — superseded by the corpus-wide total-AP canon
    # (profile §10.2; W556 payments aligned to the 8,500–9,500/month inflow in #66; W1362 2 runs/week)
    "(PHP 5,800 employees",
    "~5,800 employees with average basic salary",
    "200 stores × 35 departments",
    "~50–80 active VMI vendor partners",
    "~6,000 employees across 5 legal entities",
    "contributions reach PHP 8–12M",
    "**~1,400 hours/month**",
    "DTI: within 24 hours of recall decision",
    "DTI 24-hour reporting deadline",
    "PMBTI",
    "NMIC)",
    "Amillaramento",
    # review #60 batch-15-successor repairs (RR 11-2018 EWT regime straggler sweep:
    # the #56 batch-13 repair retired only the comma-form "1601-E,", leaving ~24
    # non-comma citations live; superseded here by the structural LEGACY_FORM rule)
    "Monthly EWT Remittance",
    "Monthly EWT payment run",
    "~800–1,000 vendor EWT certificates per month",
    "monthly batch issuance is essential",
    "within 20 days of month-end",
    "subject to 15–20% withholding tax",
    # review #60 batch-16 repairs (statutory + canon stragglers; the 1601-E/F
    # class is additionally guarded structurally by LEGACY_FORM)
    "Input VAT Spread (120-Month Amortization)",
    "DOLE Department Order No. 197-18",
    "48 hours for serious injuries",
    "PHP 10K-500K",
    "Fair Lending Act",
    "mandatory per RA 7641",
    "Calampa",
    "top 50 = 45% of COGS",
    "DUERC",
    "PASER",
    "NCSD",
    "PFRS 37",
    "~2,800 active vendors",
    "16 Sales Associates",
    "Revenue Regulation No. 11-2024",
    "Regulations No. 5-2022",
    "8%/12% VAT-on-imports",
    "(23 FTE)",
    "37 Finance & Accounting",
    "3 Stock Associates per store",
    "209 locations",
    "PHP 2–4B in forward-buy",
    "8,000–12,000 ship-from-store",
    "~115 orders/DC/day",
    "Foriklift",
    "50kg cement",
    "(BIR Form 1601-F)",
    "hundreds of inquiries/day group-wide",
    # review #61 batch-17 repairs
    "superseding DO 252-25",
    "each employ 150-250 workers",
    "~150 DC employees per shift per DC",
    "~80–100 delivery vehicles",
    "IT team expanded to ~33",
    "~200 terminal replacements/year",
    "(30/store)",
    "(PHP 1 per 10 points)",
    "high turnover rate (30–40%)",
    "~500–800 new SKUs created/month",
    "~650 new employee records/year",
    "~15% of transactions |",
    "~20 high-velocity VMI vendors",
    "~20–40 new vendors/month per W36",
    "~2,000–3,000 POs per month across ~800 active vendors",
    "Holdings: ~315)",
    "For a hardware retailer adding 3,000–5,000 new SKUs annually",
    "12 product categories across 200 stores",
    "across 12 product categories",
    "checks the Booklet for the monthly purchase limit",
    "~47,000–57,000 monthly shipments",
    "~50,000 monthly intercompany movements",
    "80% by Year 5 per RA 11898",
    "from 120+ delivery vehicles",
    "<72 hr for mandatory",
    # review #61 g2-attribution repairs
    "penalties (40–100% of duties)",
    "≤ PHP 5B total assets",
    "IPAPTA",
    "Bureau of Weights and Measures",
    "fleet of ~20 trucks",
    "5,200 trade accounts per store",
    # review #63 batch-18 repairs
    "NPCA",
    "(NPCA) & Data Sharing",
    "\"Red\" or \"Gold\" membership",
    "I-SEAL",
    "RR No. 10-2021 and related CAS",
    "No. 11-2018 and Revenue Memorandum Order (RMO) No. 29-2002",
    "1601E (monthly)",
    "1601F/1601FF monthly",
    "dividends 10/20%",
    "fines up to PHP 200,000 per day",
    "DAO 2015-09",
    "SOGO",
    "PFRS 136",
    "PAS 39 / Contingent-Liability",
    "DTO consumer protection",
    "per BIR and SEC guidelines",
    "1.4 in-store returns",
    "across all 50 assigned stores",
    "with 50 stores",
    "10–15 store completions/year + ~10–15 other project completions ≈ 10–15",
    "600–800 inbound deliveries/month",
    "~130,000 daily",
    "5,000–6,000 refund/credit",
    # "1601E" withdrawn — substring of the legitimate 1601EQ; hyphenated forms covered structurally
    # review #65 batch-19 repairs
    "PNS 48",
    "(top 4 with",
    "COBAC",
    # "opose" withdrawn — substring of propose/proposed; the W3355 spot is repaired
    "stakeaker",
    "PSA/Nikcert",
    "SSS Form B-302",
    "ECC-1.1",
    "controlled/nserialized",
    "RCOR",
    "30% corporate tax rate",
    "34(D)(2)",
    "≤ 100 employees",
    # "Permit to Operate (PTO) for standby generators" withdrawn — the DOE attribution is repaired;
    # the remaining literal matches the correct DENR-EMB text
    "within 5 days of document execution",
    # review #66 batch-20 repairs
    "MARPA",
    "AO 2016-0015",
    "1604E/1604C with Alpha List attachments via eFPS BIR system before January 31",
    "coorporate",
    "deliquent",
    "DTI/NMIS",
    "PSA certification for aircon technicians",
    "RR 19-2017",
    "USD 50,000 require BSP reporting",
    # "(3 per store)" withdrawn — matches the correct 3-POS-terminals-per-store canon;
    # the Stock-Associate mis-count is repaired
    "23-person Marketing team",
    "10–12 Sales Reps",
    "~5,000 active vendors",
    # "100 points = PHP 10" re-scoped — substring of the correct "PHP 100" form;
    # only bounded mis-citation variants are retired
    "100 points = PHP 10 for",
    "100 points = PHP 10)",
    "PHP 5,000 per terminal",
    "2–10% of contract value",
    "~28,000 monthly special-order",
    "~600–960 new listings",
    "~15,000–20,000 partner reward redemptions",
    # review #67 batch-21 repairs
    "CAO 4-2016 (Customs Modernization and Tariff Act)",
    "RR 19-2017",
    "USD 50,000 require BSP reporting",
    "Intercharge",
    "引入",
    "mimifies",
    "ERC-licensed electrician",
    "RA 7160 §199",
    "theARTA",
    "Staffing Impiction",
    "BIR Form 2552",
    "DOLE Department Order No. 16",
    "CAO 4-2016",
    "DOTC road hazmat",
    "BuildRight Retail",
    "PGBI",
    "RMC 044-2022",
    "loan PHP 2 per PHP 200",
    "~1 days per occurrence",
    "~1 weeks per occurrence",
    # review #68 batch-22 repairs (scoped after collision testing: "~20 mins per waiver"
    # is the repaired W5218 estimate, the bare "~2,800–4,200"/"~1,400–1,800 hours/year"/
    # CTL-65 and "annual refresh" forms were withdrawn as over-broad — legitimate
    # sibling derivations exist in PA-09.2/PA-76.3/PA-18.3/PA-187.1)
    "BIR Form 2307 requirements for 150% expense deduction claims",
    "Certificate of Tax Savings",
    "~40–50 stores per manager",
    "~600–1,000 visits/yr per manager",
    "~14–16 managers",
    "~40–50 store managers per regional/district manager",
    "~10–20 active CIP accounts",
    "~20–30 turnovers/year",
    "~20–30 conversions/year",
    "~20–30 closeouts/year",
    "~20–30 post-implementation reviews/year",
    "across ~200 LGUs",
    "across 200 LGU jurisdictions",
    "Affects all 6,762 users",
    "3–6 hours target within RTO",
    "NBI/PBI",
    "1–10% per BIR table",
    "~2,800–4,200 active private label",
    "~2,800–4,200 private label SKU",
    "~2,800–4,200 existing SKUs",
    "targeting 8–12% of active SKUs",
    "reasonable-suspision",
    "stale-dated check escheatment after 6 months",
    "10 Regional Managers",
    "1 hour/store × 200 stores = 150 hours",
    "~150 hours/week ≈ ~7,500 hours/year",
    "~30 min/store setup × 200 stores × 12 promos = **~1,400–1,800 hours/year**",
    "5.5-9.5 hours",
    "~15–25 hours/DC/month",
    "~200–500 entering the manual queue",
    "~16 mega-sale events",
    "12 monthly payday sales",
    "8–10 events × 80–100 hours",
    "5-15% depending on category",
    "commissions (5-15%)",
    "- operational: backlog means",
    "- operational: fields and photo prompts",
    "- operational: for reliable aging data",
    "- operational: VP or CEO sign-off",
    "- operational: changes triggered by regulation",
    "- operational: auto-revert helps",
    "- operational: means the same error",
    "~10–15 hours/month on Consumer Act",
    "~20–25 category strategies",
    "~8–12 hours for all consignment vendors",
    "**Frequency** | Weekly; ~200–300 quality failures",
    "4–6 items per store per week with reconditionable",
    "~50M–250M/year in recovered revenue",
    "~31,200 hours/year",
    "~3,000 exceptions/month = ~150 hours/month",
    "~6,000–8,000 DC delivery receipts",
    "RTPWB",
    "LTFRB/DOTC",
    "~2,000 hours (200 stores × 10 hours average)",
    "~24,000 person-hours/year",
    "~100–140 hours/year each",
    "~5–10% develop into formal insurer-notified claims",
    "~8–16 weeks per transaction",
    "8–13 hours across steps 1–6",
    "~1,000–1,500 person-hours/year for major rollouts",
    "the 1,750–2,500/year canon",
    "~120,000 hours/year",
    "~300–400 hours for BI analysis",
    "~10–15 store completions/year + ~10–15 other project completions",
    "11–19 weeks elapsed per occurrence",
    "~200 hours/closure",
    "~50–200 carton sizes/day",
    "effectively a full-time workload for 1 FTE",
    "insurance W3261",
    "~260 person-hours/year",
    "1 BI Analyst dedicated to foot traffic",
    "480 requests × 30 min",
    "2–3 hours/day on moderation",
    "~30 min/day on negative review responses",
    "~4 days/evaluation × ~2.5/year = ~80 hours/year",
    "~3–4 hours/week on fuel monitoring",
    "~15–20 min per backorder communication",
    "~5 weeks elapsed per annual refresh; ~100 person-hours",
    # review #69 batch-23 repairs (withdrawn after collision testing: bare "204 locations"
    # — 25 live uses, a 204-vs-205 family worklisted for a dedicated sweep — and the
    # generic "~10–15 hours/month" and "~30 min per occurrence"/"1-2 hours" forms)
    "~5–10 transfers/month across 4 DCs",
    "Demand forecasting despite (W2)",
    "(W1423.1)",
    "100K new serials/month",
    "across 5+ acquiring banks",
    "With 5+ bank partners",
    "straightcharge",
    "BDO, BPI, Citibank, Metrobank, HSBC",
    "~15–20 active bank accounts",
    "~50 store deposit account linkages/year",
    "DAU filings are mandatory every 5 years",
    "with no grace period",
    "~100+ different LGUs",
    "no standardization across ~100 LGUs",
    "100+ LGU jurisdictions",
    "~400–500 hours/month",
    "~800–1,000 hours total",
    "~25,000–35,000 follow-ups/month",
    "≈ 100 cases/day",
    "12–18 month rolling horizon",
    "~12–18 month rolling horizon",
    "digital by 2025",
    "~20 vehicles",
    "20 vehicles + growth",
    "Semiannually per trainee",
    "~200-300 time punches daily",
    "~1,000–1,500 standing order management actions",
    "~8,000–12,000 installment transactions/month",
    "~250–400 person-days/yr",
    "~80–100 trucks",
    "helpdesk ~5–10 FTE national",
    "Per monthly package: 25–30 person-hours",
    "~65 person-hours/year (per the itemization)",
    "Total monthly: ~15 hours",
    "4–6 hours/activation",
    "Daily per store: ~1 hour for 4 holds",
    "~4 hours/day on issue resolution follow-ups",
    "~4–6 hours/month on SDS management",
    "approaching 5-year validity expiry",
    "RA 6969 … and DOLE DO 252-25",
    "whereBuildRight",
    "rate/sLA",
    "Per request (<immediate)",
    "Per item submission: 45 min",
    "landfill/ recycler",
    "16 hours per lease",
    "~15–20 active bank accounts",
    "~100+ different LGUs",
    "straightcharge",
    "~20 vehicles/month",
    "Annual; ~20 vehicles",
    "BDO, BPI, Citibank, Metrobank, HSBC",
    # review #69 successor — the VP-Operations ghost-role adjudication (2026-08-30):
    # web/corpus-verified decision — the corpus's own PA-69.2 gloss "VP Operations (COO
    # designate)" and profile §11.1's closed 7-exec C-suite (ops under the COO) settle
    # the 519 bare-title spots as the COO; "VP Store Operations" (canonical) untouched.
    "| VP Operations |",
    # review #70 batch-24 repairs ("13 departments [,/]-~40 categories" literals WITHDRAWN after
    # the repair — #66 had canonicalized that very form as the per-department planning convention;
    # the batch-24 flag was the over-correction, caught by the guard's own first run)
    "~320–600 hours across 4 DCs",
    # "4 DCs × ~15–20 loads/day" WITHDRAWN 2026-09-23 (sixty-seventh wave): the batch-24
    # ban predates the production-volume calibration, which re-declared the chain-wide
    # load canon at ~60–80 loads/day (= ~15–20/DC/day — the batch's own 1,800–2,400/month
    # tail already said so); the batch's ×~10=~40 correction is the retired form now
    # (calibrated_volume_hits bans "= ~40 loads/day"). Same lesson as the withdrawn
    # '13 departments/~40 categories' flags below: a guard literal outlives its canon.
    "Primarily with top 50 vendors (by spend)",
    "(PHP 50–200 value)",
    "store/DC staff (98%+ of headcount)",
    "management resolutions: ~10–20/year",
    "funded projects ~120–200/month",
    "~1,750–2,800/yr",
    "~50 critical categories requiring diversification",
    "typically 5–30% per RA 9184",
    "~60–90 min per wholesale return",
    "adds ~4–6 hours/month centralized",
    "fabrication activity consumes ~20–40 min/day",
    "~1–2 days/month on vehicle registration compliance",
    "200 stores × ~20 extinguishers per store",
    "regional operations directors",
    "VP Store Ops",
    "Chief Audit Executive",
    "the restocking fee (5–10%)",
    "Pay the registration fees; download and archive the NPC",
    # review #70 successor — the ghost-role adjudication sweep (2026-08-30): ten families
    # (1,108 spots) unified on charted/majority owners per profile §11.1 — CRO -> Head of
    # Internal Audit & Risk (the W122 "acting as Risk Officer" gloss), General Counsel -> VP
    # Legal & Compliance, Store Ops Director -> VP Store Operations (715-use majority), VP
    # Procurement -> VP Supply Chain (charted), VP Quality -> Quality Manager, VP Sustainability
    # -> Sustainability/ESG Manager, CDAIO -> CIO, VP Services/VP Real Estate/VP Asset & Infra -> COO
    # (the §11.1 COO row owns Store Ops, Supply Chain, Facilities & Real Estate, Quality, Trade).
    "| CRO |",
    "General Counsel",
    "Store Ops Director",
    "VP Procurement",
    "VP Quality",
    "VP Sustainability",
    "CDAIO",
    "VP Services",
    "VP Real Estate",
    "VP Asset & Infra",
    # review #72 batch-26 ghost-role adjudication: the finance-exec seat family
    # ("VP Finance" ~148 + "Finance VP" ~71) unified on CFO per the corpus's own
    # approval ladders (INS-008/CCR-001 "≤PHP 500K Finance Controller, ≤PHP 5M
    # Finance VP, >PHP 5M CEO" — the seat between Controller and CEO is the CFO's
    # in §11.1's closed 7-exec chart); "Finance Director" (~100) -> Finance
    # Controller (the §3.3 department head; 478-use majority form; the external
    # "Developer Finance Director" is legitimately live and NOT retired);
    # "VP HR" (~42) -> CHRO; "VP Internal Audit" (~31) -> Head of Internal Audit
    # (batch-24 target); "Merchandising VP"/"Marketing VP"/"Supply Chain VP" ->
    # the charted VP-majority forms; "Regional Ops Director" (9) -> Regional
    # Manager (PA-26.2's own step text already names Regional Manager);
    # "Store Ops Dir" (16) -> VP Store Operations (batch-24 decision's abbreviation
    # form); "Supply Chain Mgr" (8) -> VP Supply Chain (approval/escalation
    # A-columns = the department-head seat charted at profile §3.3).
    "VP Finance",
    "Finance VP",
    "| Finance Director |",
    "the Finance Director",
    "| VP HR |",
    "| VP Internal Audit |",
    "Merchandising VP",
    "Regional Ops Director",
    "Store Ops Dir",
    "Supply Chain Mgr",
    # review #72 batch-26 second wave: role families swept after the five audit passes
    # (VP Customer Service 11 spots -> COO per §11.1's CS-under-COO row, VP-Services
    # precedent; Head of Sustainability 33 -> Sustainability/ESG Manager, the CSO/
    # VP-Sustainability adjudicated owner; Chief Risk Officer remnant -> Head of
    # Internal Audit & Risk), statutory forms from the web-verified RA 9481/D.O. 40-03
    # and BIR-2306 repairs, the solar-fleet stale figure, and the CTL-51 paste-template
    # leading form (PA-67.2's deliberate topical cross-reference is a different string).
    "VP Customer Service",
    "Head of Sustainability",
    "Chief Risk Officer",
    "2306 on Imports",
    "20% representation support",
    "DOLE-BLRF",
    "8 pilot stores installed",
    "- CTL-51: master-data quality \u2014 links to VS-29 / W291",
    # review #73 batch-27 repairs: role variants swept on canon targets (Merchandising
    # Director -> VP Merchandising per §13.1; Financial Controller -> Finance Controller;
    # Logistics Director/VP Logistics -> VP Supply Chain; VS-183's HR L&D Director /
    # L&D VP -> the PA's charted HR-L&D Manager; executive-seat CCO forms -> VP Legal &
    # Compliance — the DENR "CCO 2013-24" Chemical Control Order references are
    # legitimately live and NOT retired), statutory forms (the phantom BOC "CAB-CBP"
    # accreditation -> AMO per CMO 04-2014 + RA 9280; the last PSIAB remnant -> PNP-SOSIA
    # per RA 5487; the AMLA covered-person mis-claim — general retail is not an RA 9160
    # covered person, the group's financing subsidiaries are; RA 8556-only lending-company
    # framing -> RA 9474 alongside RA 8556), and the CSO disambiguation literal form.
    "Merchandising Director",
    "Financial Controller",
    "Logistics Director",
    "VP Logistics",
    "HR L&D Director",
    "L&D VP",
    "VP Legal/CCO",
    "VP Legal / CCO",
    "CAB-CBP",
    "PSIAB",
    "which includes businesses accepting cash payments",
    "under RA 8556 / SEC oversight",
    # review #74 batch-28 repairs: the Pag-IBIG remittance deadline trued to the 10th
    # of the following month (three spots incl. the W1306 trigger and PA-17.3), the
    # stale "~16-person HR team" figure (26 per §3.3), the 12-24x data-warehouse
    # growth claim trued to the §1.2 canon, the "standard 15%" receiving-sampling
    # figure trued to the corpus 10% canon (W1600), and the deprecated W5c sub-step
    # ids renumbered to W5F.
    "Pag-IBIG: every 14th",
    "Pag-IBIG by every 14th",
    "~16-person HR team",
    "100\u2013200 GB/month",
    "(vs. standard 15%)",
    # review #75 batch-29 sweeps: two systemic wrong-VS pointer boilerplates
    # (W113 "Business Intelligence & Data Governance" lives in VS-27, not VS-28;
    # W52 "Fleet Management" lives in VS-04, not VS-06; 60 files / ~258 spots
    # swept, plus 40 "VS-63 / W571" -> VS-07 spots), role families completed
    # (Store Operations Director -> VP Store Operations incl. 5 ICM owner rows;
    # Land Liaison Specialist -> Officer; ITAM Manager -> IT Asset Manager;
    # Safety & PPE Department Supervisor -> Department Supervisor (Tools/Hardware)
    # per §12.1's closed 4-supervisor set; Lease Accounting Controller -> Finance
    # Controller (Lease Accounting); CHRO/CHRO doubled cells), and the W1278
    # price-approval threshold (PHP 50 -> PHP 50,000 per the PA's own tiers).
    "VS-28 / W113",
    "VS-06 / W52",
    "VS-63 / W571",
    "51 daily workflows",
    "above PHP 50 impact",
    "CHRO / CHRO",
    "downtime exceeds 99.9%",
    # review #71 batch-25 repairs (withdrawn after collision testing: bare "~8K–12K/month"
    # — legitimate coupon/gift-card volumes share the form; "CSO /" and "| CDO |" match
    # un-swept non-sustainability contexts — the CSO/CDO flips were scoped to the
    # sustainability/AI files where the org-canon conflict was verified)
    "Commission on Ruling",
    "(Type-A/B/C",
    "EICC (energy conservation) registration",
    "Alpha list Tax Code",
    "quarterly 1604E",
    "~PHP 1.0B+ monthly cash sales",
    "Per closure; ~15–20 redeployments",
    "Store Operations Director (HQ-side)",
    "distinct from W838 (yard dispatch",
    "Type-A/B/C",
    "~29 Store Managers viewing daily",
    "PSIAB — Philippine Private Investigation",
    "VP Audit |",
    "Layout fails BP 344/ADA",
    "signing a tripartite JQS statement",
    "~40–70 hours/month for HR Assistant",
    "adds ~15 hours/month",
    "Total: ~100–140 days/year",
    "110 person-hours/year",
    "Per vendor onboarding: 45 min",
    "~12–16 hours/week across Pricing Analysts",
    '~500–1,000 "KVIs"',
    "~20–30 consignment vendors",
    "Quarterly forward-buy planning cycles",
    "Buyer: ~20 hours/quarter",
    "CTL-44: re-route integrity",
    "| VP Audit |",
    "1,224 hours/year",
    "60–90 min per store per day",
    "15–30 min (10–20 communications",
    "fails BP 344/ADA",
    "Internal Audit Director",
    "Real Estate Legal Counsel",
    "VP Communications",
    "Bi-weekly payroll cycle",
    "| VP Audit |",
]
CLIP_RE = re.compile(r'auto-\w+ of "(logies|logy[^"s/]|countant)')
FOOTPRINT_CLIP_RE = re.compile(r'auto-\w+ of "print([^"]*)" \(replaces manual Step (\d+)\)')
ROLE_COUNTS = [("Category Manager", 5), ("Buyers", 10), ("Buyer", 10),
               ("Merchandise Planners", 5), ("Pricing Analysts", 4)]

BULLET_RE = re.compile(r'- System [^"]*?of "([^"]+)" \(replaces manual Step (\d+)([a-z]?)\)\.')
STEP_RE = re.compile(r"^\|\s*(\d+)([a-z]?)\s*\|")

# Hand-authored noun-phrase summary bullets (vintage generator style): the quote
# is a descriptive noun phrase, not a verbatim step span — adjudicated sound.
QUOTE_STYLE_ALLOWLIST = {
    ("PA-116.2-bond-application-issuance-tracking-and-encumbrance-management.md", "W3655"),
    ("PA-117.3-market-surveillance-compliance-monitoring-and-certification-analytics.md", "W3687"),
    ("PA-17.3-tax-and-statutory.md", "W590"),
    ("PA-17.3-tax-and-statutory.md", "W1503"),
    ("PA-18.1-cash-positioning-and-forecasting.md", "W234"),
    ("PA-18.1-cash-positioning-and-forecasting.md", "W323"),
    ("PA-15.1-invoice-processing-and-matching.md", "W461"),
    ("PA-38.3-financing-reconciliation-settlement.md", "W1785"),
    ("PA-40.2-project-cost-tracking.md", "W1826"),
    ("PA-46.1-government-registration-qualification.md", "W1950"),
    ("PA-26.3-insurance-claims-and-policy-management.md", "W860"),
    ("PA-10.1-ecommerce-platform-operations.md", "W1185"),
}


def steps_header_hits(lines):
    """Structural rule (review #51): a steps table header row must not directly
    follow a field-table row — the W4762 signature (missing '### Steps' or any
    phase header between the field table and the steps table)."""
    out = []
    for i, l in enumerate(lines):
        if re.match(r"^\| # \| Activity \|", l):
            prev = next((x for x in lines[:i][::-1] if x.strip()), "")
            if prev.startswith("| **") and "**" in prev:
                out.append((i + 1, "steps table follows field row with no section header"))
    return out


def quote_integrity_hits(fname, lines):
    """Containment + word-boundary check for step-quoting automation bullets."""
    out = []
    cur = None
    steps = {}
    in_steps = False
    for i, l in enumerate(lines, 1):
        if re.match(r"^### Steps\b", l):
            in_steps = True
            continue
        m = re.match(r"^#{2,3} (W\d+[A-Z]?)[. ]", l)
        if m:
            cur = m.group(1)
            in_steps = False
            continue
        if l.startswith("#"):
            # named h3 sub-sections (e.g. '### Vendor Rebate Dispute Resolution')
            # end the current workflow's step scope
            cur = None
            in_steps = False
            continue
        if in_steps:
            sm = STEP_RE.match(l)
            if sm and cur:
                steps[(cur, sm.group(1), sm.group(2))] = l
        bm = BULLET_RE.search(l)
        if bm and cur:
            if (fname, cur) in QUOTE_STYLE_ALLOWLIST:
                continue
            quote, snum, sltr = bm.group(1), bm.group(2), bm.group(3)
            st = steps.get((cur, snum, sltr), "")
            if not st:
                continue
            stn = re.sub(r"\*\*", "", st)
            stw = re.sub(r"\s+", " ", stn)
            q = quote.rstrip("…").rstrip()

            def contained(s):
                s2 = re.sub(r"\s+", " ", s)
                return bool(s) and (s in stn or s.lower() in stn.lower()
                                    or s2 in stw or s2.lower() in stw.lower())

            if not contained(q):
                if not ("…" in quote and contained(quote.split("…")[0].rstrip())):
                    out.append((i, f'quote not in Step {snum}{sltr}: "{q[:60]}"'))
                    continue
            # word-boundary: at least one occurrence must not sit inside a word
            hay, needle = (stn, q) if q in stn else (stn.lower(), q.lower())
            ok = False
            for mm in re.finditer(re.escape(needle), hay):
                s, e = mm.start(), mm.end()
                if (s == 0 or not hay[s - 1].isalnum()) and (e >= len(hay) or not hay[e].isalnum()):
                    ok = True
                    break
            if not ok:
                out.append((i, f'mid-word clip in Step {snum}{sltr}: "{q[:60]}"'))
    return out


# review #56/#57 missing-quantifier Volume/Frequency rule: a register cell that
# starts "~ <noun>" (no count word) and carries no digit/% of its own — ignoring
# digits that are part of codes (VS-122, 3PL, 9G, B2B) — is a placeholder.
QUANT_WORDS = {"all", "most", "every", "each", "tens", "hundreds", "thousands",
               "dozens", "majority", "half", "one", "two", "three", "few",
               "several", "annual", "continuous", "rare", "event-driven",
               "event", "daily", "weekly", "monthly", "quarterly", "per",
               "hopefully", "variable", "negligible", "minimal", "low", "high",
               "medium", "top"}
CODE_TOKENS = re.compile(r'(?:VS|PA|W|CTL|RA|DO|DAO|RR|SEC|MC|GIS|D\.O\.|DTS)'
                         r'-?\d+(?:\.\d+)*|\dPL|9[GD]|B2B|B2C|C2C'
                         r'|10-wheeler|6-wheel')
PLACEHOLDER_CELL = re.compile(r'^\| \*\*(Volume|Frequency)\*\* \| ~\s?([^|]*)\|')

# Legacy BIR withholding forms discontinued by RR 11-2018 (filed their last
# returns in 2018): 1601-E -> 1601-EQ (quarterly, creditable/EWT) and
# 1601-F -> 1601-FQ (quarterly, final). Any non-Q sighting is a defect.
LEGACY_FORM = re.compile(r"1601-E(?!Q)|1601-F(?!F|Q)")

# Review #61: a Time Estimate line `~N(-N)? per occurrence` with no time unit is a
# defect (131 spots censused and repaired across 20 files; units restored from each
# workflow's own step durations).
UNITLESS_OCCURRENCE = re.compile(r"^- ~\d+(?:–\d+)? per occurrence", re.M)


def placeholder_cell_hits(lines):
    out = []
    for i, l in enumerate(lines, 1):
        m = PLACEHOLDER_CELL.match(l)
        if not m:
            continue
        txt = m.group(2)
        first = re.split(r'[\s/–-]', txt.strip())[0].lower()
        if first in QUANT_WORDS:
            continue
        if re.search(r'[\d%]', CODE_TOKENS.sub('', txt)):
            continue
        out.append((i, f'missing-quantifier {m.group(1)} cell: "{txt.strip()[:60]}"'))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true")
    args = ap.parse_args()
    hits = []
    files = sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md")))
    for f in files:
        text = open(f, encoding="utf-8").read()
        rel = os.path.relpath(f, REPO)
        fname = os.path.basename(f)
        for lit in RETIRED_LITERALS:
            if lit in text:
                hits.append(("retired-literal", rel,
                             text[:text.find(lit)].count("\n") + 1, lit))
        for m in CLIP_RE.finditer(text):
            hits.append(("clipped-keyword", rel,
                         text[:m.start()].count("\n") + 1,
                         f'automation keyword clip "{m.group(1)}"'))
        for m in FOOTPRINT_CLIP_RE.finditer(text):
            stepn = m.group(2)
            blk = text[text.rfind("## W", 0, m.start()):]
            sm = re.search(r"^\| " + stepn + r" \| (.+?) \|", blk, re.M)
            if sm and "footprint" in sm.group(1).lower():
                hits.append(("clipped-keyword", rel,
                             text[:m.start()].count("\n") + 1,
                             f'footprint clip "print{m.group(1)[:30]}"'))
        for m in re.finditer(r"^\| \*\*Participants\*\* \| (.+?) \|$", text, re.M):
            row = m.group(1)
            for role, n in ROLE_COUNTS:
                pm = re.search(re.escape(role) + r"\s*\((\d+)\)", row)
                if pm and int(pm.group(1)) != n:
                    hits.append(("participant-count", rel,
                                 text[:m.start()].count("\n") + 1,
                                 f"{role} count {pm.group(1)} != register {n}"))
        for line, detail in quote_integrity_hits(fname, text.splitlines()):
            hits.append(("quote-integrity", rel, line, detail))
        for line, detail in steps_header_hits(text.splitlines()):
            hits.append(("steps-header", rel, line, detail))
        for line, detail in placeholder_cell_hits(text.splitlines()):
            hits.append(("placeholder-cell", rel, line, detail))
        for m in LEGACY_FORM.finditer(text):
            hits.append(("legacy-bir-form", rel,
                         text[:m.start()].count("\n") + 1,
                         f'retired BIR form "{m.group(0)}" (use 1601-EQ / 1601-FQ per RR 11-2018)'))
        for m in UNITLESS_OCCURRENCE.finditer(text):
            hits.append(("unitless-occurrence", rel,
                         text[:m.start()].count("\n") + 1,
                         'unit-less "per occurrence" Time Estimate line (restore the unit from the workflow step durations)'))
    for kind, rel, line, detail in hits:
        print(f"{kind}: {rel}:{line}: {detail}")
    print(f"audit-semantic-anchors: {len(hits)} hit(s) across {len(files)} PA files")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
