#!/usr/bin/env python3
"""Wave-50 repair, part 2: VS-66 / VS-68 / VS-74 Pain-Points template sections.

The 2026-06-20 Expansion-block rework (96a53dff) replaced the Check-10-detectable
boilerplate in the seven Python-assisted value streams with a *different* verbatim
paste: every workflow's '### Pain Points / Risks' section became one of a handful
of 2-bullet template combos (Integration-failure+Data-quality, Scope-creep,
Delivery-failure, Credit-default, Greenwashing, Execution, Metric-gaming,
Margin-erosion, ...), identical across up to 152 workflows — while the same
commit's message claimed '528/528 workflows de-boilerplated'. This script
rewrites each affected VS-66/68/74 section with workflow-specific bullets
grounded in the workflow's own steps and touchpoints, via the shared engine
(fix-pain-template-engine.py) that asserts every old bullet is a template-pool
member before writing.
"""
import importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "fix_pain_template_engine", os.path.join(HERE, "fix-pain-template-engine.py"))
_engine = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_engine)

R = []  # (vs-glob, filename, W-id) -> bullets appended below

# ---------------- VS-66 — Customer Project Design Services ----------------

# PA-66.1 — In-Home Measurement & Design
R += [
 ("VS-66-*", "PA-66.1-in-home-measurement-design.md", "W2430", [
  "- **Qualification-mismatch risk**: inquiries accepted outside the program's scope (below the PHP 50K referral threshold, or outside kitchen/bath/whole-house) consume consultant visits without converting; mitigated by the project-type/budget/timeline qualification gate (Step 1) routing sub-threshold projects back to store channels",
  "- **Visit-no-show risk**: in-home visits scheduled on unqualified demand strand consultant hours; mitigated by the confirmed date and the project intake form prepared before the visit (Step 2)",
 ]),
 ("VS-66-*", "PA-66.1-in-home-measurement-design.md", "W2431", [
  "- **Measurement-error risk**: a mis-measured room propagates into the design, the material take-off and the quotation, surfacing as site rework; mitigated by the photographed space and the dimensioned sketch (Step 2) giving the designer a verifiable record",
  "- **Concealed-condition risk**: plumbing relocation or structural issues invisible at the walkthrough emerge mid-installation as change orders; mitigated by the challenge identification at the visit (Step 2) and the 5-business-day proposal promise leaving review time before the design commitment",
 ]),
 ("VS-66-*", "PA-66.1-in-home-measurement-design.md", "W2432", [
  "- **Rendering-expectation risk**: a 3D rendering that outshines the specified materials sets expectations the installation cannot meet; mitigated by the physical design boards and material samples presented alongside the rendering (Step 2)",
  "- **Approval-limbo risk**: proposals neither approved, modified nor declined stall in the pipeline and expire unseen; mitigated by the explicit approve/modify/decline branch (Step 2) feeding W2435's revision loop",
 ]),
 ("VS-66-*", "PA-66.1-in-home-measurement-design.md", "W2433", [
  "- **Take-off error risk**: a missed tile-sqm or fixture count in the take-off shorts the delivery and stalls installation mid-project; mitigated by the system validation against standard waste factors (Step 2) over the consultant's line-item take-off (Step 1)",
  "- **Long-lead surprise risk**: special-order and import items discovered after quotation push the timeline past the customer's patience; mitigated by the lead-time item identification (Step 2) feeding W2439's procurement coordination",
 ]),
 ("VS-66-*", "PA-66.1-in-home-measurement-design.md", "W2434", [
  "- **Margin-threshold risk**: project pricing that wins on trade-price competitiveness can land below the minimum margin; mitigated by the Finance margin review (Step 2: material cost vs. project price) requiring approval or adjustment before the quotation issues",
  "- **Quotation-expiry risk**: a 30-day validity against volatile material prices quotes a project the purchase order cannot honor late; mitigated by the explicit validity window (Step 2) forcing re-quote and fresh approval on expiry",
 ]),
 ("VS-66-*", "PA-66.1-in-home-measurement-design.md", "W2435", [
  "- **Scope-approval gap risk**: verbal change requests proceed to procurement before the revised quotation and deposit are approved; mitigated by the approval-gated sales order and the 30–50% deposit collection (Step 2) preceding the execution phase",
  "- **Revision-cost drift risk**: successive small revisions re-price the project piecemeal and erode the approved margin; mitigated by the material-list and quotation update on every change (Step 1) under the W2434 Finance threshold",
 ]),
 ("VS-66-*", "PA-66.1-in-home-measurement-design.md", "W2436", [
  "- **Skill-decay risk**: uncertified consultants measuring and designing reproduce the error classes W2431/W2433 exist to catch; mitigated by the HR Training certification on design software and measurement accuracy (Step 1) with Category Manager product refreshers",
  "- **Trend-drift risk**: designs anchored to stale techniques and materials lose against competitors' current offerings; mitigated by the new-materials, installation-technique and design-trend training cadence (Step 1)",
 ]),
 ("VS-66-*", "PA-66.1-in-home-measurement-design.md", "W2437", [
  "- **License-lapse risk**: an expired design-software license idles every consultant's proposal pipeline at once; mitigated by the IT license-maintenance ownership (Step 1) ahead of renewal dates",
  "- **Catalog-drift risk**: a design tool carrying discontinued SKUs or stale prices generates take-offs the stores cannot fulfill; mitigated by the product-catalog updates in the design tool and the measurement-tool calibration (Step 1)",
 ]),
]

# PA-66.2 — Quotation, Procurement & Delivery
R += [
 ("VS-66-*", "PA-66.2-project-quotation-material-estimation.md", "W2438", [
  "- **Deposit-validation risk**: order processing on an unverified deposit reserves inventory against an unfunded project; mitigated by the Finance deposit validation (Step 2) gating the inventory reservation and the pick lists",
  "- **Order-quotation divergence risk**: SKU links or prices drifted between quotation and sales order bill a different project than the customer approved; mitigated by the SKU linking and pricing confirmation (Step 1) against the approved quotation",
 ]),
 ("VS-66-*", "PA-66.2-project-quotation-material-estimation.md", "W2439", [
  "- **Special-order delay risk**: a non-stock vendor item arriving after its installation window idles the crew and compresses every later milestone; mitigated by the project-linked PO with delivery tracked to store/DC (Step 1) coordinated against the project schedule",
  "- **Vendor-failure risk**: a special-order vendor missing the promised date strands the project timeline; mitigated by the W36 vendor PO terms and the VS-56 3PL alternatives for recovery",
 ]),
 ("VS-66-*", "PA-66.2-project-quotation-material-estimation.md", "W2440", [
  "- **Failed-receipt risk**: bulky deliveries arriving to no on-site customer are refused or left exposed, re-running a full truck for one signature; mitigated by the on-site receipt confirmation before dispatch (Step 1) and the 48-hour discrepancy resolution (Step 2)",
  "- **Transit-damage risk**: tile, lumber or cement damage signed for at the curb surfaces only when the installer opens the bundle; mitigated by the customer's quantity-and-condition verification at delivery (Step 2) before the goods-delivered status updates",
 ]),
 ("VS-66-*", "PA-66.2-project-quotation-material-estimation.md", "W2441", [
  "- **Installer-slot risk**: licensed contractor dates slipping against material-arrival dates idle the crew and extend customer disruption; mitigated by the scheduled dates with contractor confirmation (Step 1) per the VS-12 installer network",
  "- **Milestone-signoff risk**: installation proceeding past failed quality checkpoints compounds rework across milestones; mitigated by the key-milestone quality checks and customer milestone sign-offs (Step 2) gating contractor payment",
 ]),
 ("VS-66-*", "PA-66.2-project-quotation-material-estimation.md", "W2442", [
  "- **Unpriced-change risk**: scope changes executed on goodwill before the change-order quotation is approved recover no cost; mitigated by the impact evaluation and change-order quotation (Step 1) preceding procurement",
  "- **Timeline-cascade risk**: an approved change re-pricing materials but not the delivery/installation schedule misleads the customer; mitigated by the Finance payment-schedule adjustment and material-requirement update (Step 2) as a single re-baseline",
 ]),
 ("VS-66-*", "PA-66.2-project-quotation-material-estimation.md", "W2443", [
  "- **Milestone-billing lag risk**: invoices generated late against completed milestones convert finished work into aged receivable; mitigated by the sign-off-triggered invoice generation (Step 1) with Finance tracking deposit, progress and final payment status",
  "- **Final-payment leakage risk**: projects closing without the final payment collection write off the last milestone; mitigated by the payment-status tracking (Step 1) tied to the VS-17 financial close",
 ]),
 ("VS-66-*", "PA-66.2-project-quotation-material-estimation.md", "W2444", [
  "- **Registration-gap risk**: installed products left unregistered forfeit the manufacturer warranty the customer paid for; mitigated by the CRM warranty registration for every installed product (Step 2) per VS-53",
  "- **Handover-incompleteness risk**: a warranty package without the workmanship term or the care guide converts warranty calls into disputes; mitigated by the package compile list (Step 1: product warranties, 1-year workmanship, care and maintenance guide)",
 ]),
 ("VS-66-*", "PA-66.2-project-quotation-material-estimation.md", "W2445", [
  "- **Return-condition risk**: used or damaged materials accepted as saleable returns restock defects for the next customer; mitigated by the Receiving Clerk inspection (Step 1) with damaged returns routed per the vendor return policy (Step 2)",
  "- **Final-cost reconciliation risk**: returned materials credited to the customer but not to the project's final cost overstate the project's loss; mitigated by the Finance final-cost adjustment (Step 2)",
 ]),
]

# PA-66.3 — Tracking, Completion & Analytics
R += [
 ("VS-66-*", "PA-66.3-project-tracking-completion.md", "W2446", [
  "- **Stale-status risk**: a dashboard showing yesterday's milestone state dispatches decisions on dead data; mitigated by the Consultant's daily update ownership (Step 1) across status, milestones, payments and open issues",
  "- **Issue-burial risk**: open issues listed without ownership age until they stall the project; mitigated by the open-issues panel (Step 1) reviewed inside the daily cadence",
 ]),
 ("VS-66-*", "PA-66.3-project-tracking-completion.md", "W2447", [
  "- **Delay-communication risk**: slippage discovered but not communicated until the milestone date converts a recoverable delay into a customer complaint; mitigated by the delay identification and customer communication (Step 1) at tracking time",
  "- **Critical-path blindness risk**: adjusting one milestone date without its dependencies re-plans a schedule that cannot hold; mitigated by the timeline-vs-plan tracking across material dates, installation and milestones (Step 1)",
 ]),
 ("VS-66-*", "PA-66.3-project-tracking-completion.md", "W2448", [
  "- **Checkpoint-skipping risk**: installation milestones signed off un-inspected pass structural layout errors through to completion; mitigated by the four-stage inspection sequence (Step 1: delivery, start, mid-installation, completion punch list)",
  "- **Workmanship-drift risk**: deferring inspection to completion finds a whole room's workmanship below standard; mitigated by the mid-installation workmanship checkpoint (Step 1) catching drift while correction is cheap",
 ]),
 ("VS-66-*", "PA-66.3-project-tracking-completion.md", "W2449", [
  "- **Acceptance-without-punch risk**: customers signing acceptance before the punch list is agreed lose their leverage on the final fixes; mitigated by the punch-list documentation inside the walkthrough (Step 1) ahead of the acceptance signature",
  "- **Punch-list-aging risk**: minor fixes promised at completion aging past the 7-day window close the project with open items; mitigated by the 7-day resolution gate with contractor return and Consultant verification before final payment (Step 2)",
 ]),
 ("VS-66-*", "PA-66.3-project-tracking-completion.md", "W2450", [
  "- **Follow-up-latency risk**: satisfaction contact made only at the next purchase finds issues after warranty windows have closed; mitigated by the 30-day post-completion contact (Step 1) with the feedback logged in CRM",
  "- **Referral-omission risk**: satisfied customers never asked for referrals end the project's commercial value at final payment; mitigated by the referral request embedded in the follow-up call (Step 1)",
 ]),
 ("VS-66-*", "PA-66.3-project-tracking-completion.md", "W2451", [
  "- **Cost-attribution risk**: project margin computed without installation and delivery costs overstates the program's profitability by type; mitigated by the full-cost analysis (Step 1: material, installation, delivery) by project type and value range",
  "- **Type-mix blindness risk**: growing the lowest-margin project type because it books the most revenue; mitigated by the most-profitable-type identification (Step 1) feeding W2453's service strategy",
 ]),
 ("VS-66-*", "PA-66.3-project-tracking-completion.md", "W2452", [
  "- **Metric-gaming risk**: consultants chasing completion count over margin and satisfaction win incentives while the program loses; mitigated by the balanced scorecard (Step 1: revenue, margin, satisfaction, change-order rate, on-time completion) used for review and incentives together",
  "- **Change-order-penalty risk**: scorecarding the change-order rate as a standalone penalty drives honest re-scoping underground; mitigated by the rate read alongside margin achieved (Step 1) rather than in isolation",
 ]),
 ("VS-66-*", "PA-66.3-project-tracking-completion.md", "W2453", [
  "- **Expansion-without-evidence risk**: new service categories launched on enthusiasm rather than market-opportunity data strand training and inventory; mitigated by the market-opportunity and competitive-positioning evidence (Step 1) preceding the expansion recommendation",
  "- **Program-drift risk**: pricing left unadjusted against material inflation erodes program margin between reviews; mitigated by the annual pricing-adjustment recommendation (Step 1) on the reviewed margin data",
 ]),
]

# ---------------- VS-68 — Trade Credit Risk Management ----------------

# PA-68.1 — Assessment
R += [
 ("VS-68-*", "PA-68.1-trade-credit-risk-assessment.md", "W2478", [
  "- **Fraudulent-application risk**: falsified registration papers or fabricated trade references onboard credit the company later chases; mitigated by the document verification and background check (Step 1) before any risk assessment",
  "- **Risk-misgrading risk**: a misread financial ratio grades a risky account as creditworthy and sets its first limit too high; mitigated by the five-factor assessment (Step 2: viability, payment history, financial ratios, industry risk, relationship potential) feeding the W2486 approval matrix",
 ]),
 ("VS-68-*", "PA-68.1-trade-credit-risk-assessment.md", "W2479", [
  "- **Model-drift risk**: weightings calibrated on old default experience misrank today's applicants as the market moves; mitigated by the recalibration against actual default experience (Step 1) with backtesting before deployment",
  "- **Variable-selection risk**: predictors correlated with anything but credit behavior embed distortion into every downstream limit; mitigated by the new-variable review (Step 1: payment trend, order-frequency changes) confined to credit-relevant signals",
 ]),
 ("VS-68-*", "PA-68.1-trade-credit-risk-assessment.md", "W2480", [
  "- **Review-lag risk**: an annual-only cadence lets a deteriorating account keep its limit for months between reviews; mitigated by the quarterly high-risk deep reviews (Step 2: score decline, >15% late payments, >80% utilization) between the annual refreshes",
  "- **Limit-stickiness risk**: review recommendations arriving without action leave stale limits in force; mitigated by the auto-triggered recalculated score with its limit-adjustment recommendation (Step 1) routed into the W2486 approval matrix",
 ]),
 ("VS-68-*", "PA-68.1-trade-credit-risk-assessment.md", "W2481", [
  "- **Data-feed gap risk**: a missed monthly bureau pull blinds the portfolio to new legal filings and negative events; mitigated by the scheduled monthly pulls (Step 1) with the >20-point score-decline auto-flag routing to analyst review",
  "- **Signal-overreaction risk**: a single bureau event triggering limit action on an otherwise clean account; mitigated by the flag-for-review design (Step 1) keeping the decision with the Credit Analyst rather than auto-adjusting",
 ]),
 ("VS-68-*", "PA-68.1-trade-credit-risk-assessment.md", "W2482", [
  "- **Stale-financials risk**: statements years old score a customer whose current position has collapsed; mitigated by the industry-benchmark comparison (Step 1) and the review feeding the W2480 periodic refresh",
  "- **Window-dressing risk**: polished statements concealing cash-flow inadequacy pass the ratio checks; mitigated by the cash-flow-adequacy review (Step 1) alongside the profitability and leverage ratios",
 ]),
 ("VS-68-*", "PA-68.1-trade-credit-risk-assessment.md", "W2483", [
  "- **Macro-blindspot risk**: portfolio appetite set without the construction-cycle view concentrates exposure as the sector turns; mitigated by the macro-risk assessment (Step 1: sector outlook, interest rates, infrastructure spending) adjusting portfolio risk appetite",
  "- **Appetite-lag risk**: risk appetite revised slower than the interest-rate cycle reprices customer stress; mitigated by the Finance Controller ownership (Step 1) with the W2485 concentration analysis exposing the shifted mix",
 ]),
 ("VS-68-*", "PA-68.1-trade-credit-risk-assessment.md", "W2484", [
  "- **Coverage-adequacy risk**: insured limits below the portfolio's real exposure leave the uninsured gap to absorb a default; mitigated by the coverage-adequacy review (Step 1: deductible, exclusions, country limits) against actual concentrations",
  "- **Insurer-strength risk**: claims on a weakened insurer arrive unpaid precisely when defaults cluster; mitigated by the insurer financial-strength review (Step 1) at each policy assessment",
 ]),
 ("VS-68-*", "PA-68.1-trade-credit-risk-assessment.md", "W2485", [
  "- **Concentration breach risk**: a single customer above 5% of the portfolio turns one default into a capital event; mitigated by the policy-limit flags (Step 1) across customer tier, industry, region and account age",
  "- **Correlated-segment risk**: nominally diversified accounts sharing one industry or region default together; mitigated by the multi-dimension concentration cut (Step 1) feeding W2483's appetite adjustment",
 ]),
]

# PA-68.2 — Limit Management & Monitoring
R += [
 ("VS-68-*", "PA-68.2-credit-limit-management-monitoring.md", "W2486", [
  "- **Matrix-bypass risk**: a limit approved above the analyst's authority undercuts the control the matrix exists for; mitigated by the tiered approval matrix (Step 1: Analyst, Manager, Director bands) routing each limit to its right approver",
  "- **Insurance-mismatch risk**: limits set beyond the insured coverage shift default loss onto the balance sheet; mitigated by the credit-insurance coverage input (Step 1) bounded by the W2484 policy assessment",
 ]),
 ("VS-68-*", "PA-68.2-credit-limit-management-monitoring.md", "W2487", [
  "- **Block-evasion risk**: orders timed around the utilization check or split across accounts hide exposure past the limit; mitigated by the real-time outstanding-vs-limit monitor with auto-block (Step 1) applied at account level",
  "- **Alert-fatigue risk**: 80%-utilization alerts ignored in bulk train analysts to skip them; mitigated by each alert routed to the Trade Account Manager (Step 1) with the W2486 matrix governing any increase response",
 ]),
 ("VS-68-*", "PA-68.2-credit-limit-management-monitoring.md", "W2488", [
  "- **Growth-justified risk**: an increase justified by sales growth alone extends credit into a deteriorating payer; mitigated by the Credit Analyst evaluation (Step 1: justification, payment history) with counteroffer authority rather than binary approval",
  "- **Effective-date risk**: increases applied without effective-date control retroactively bless over-limit exposure; mitigated by the evaluation-to-application sequencing (Step 1) on the account",
 ]),
 ("VS-68-*", "PA-68.2-credit-limit-management-monitoring.md", "W2489", [
  "- **Relationship-shock risk**: a sudden suspension communicated poorly loses a salvageable account to a competitor; mitigated by the Trade Account Manager notification and customer management (Step 1) alongside the reduction",
  "- **Reduction-lag risk**: deterioration acted on only after the next default surrenders the protection the reduction exists for; mitigated by the deterioration triggers (Step 1: payment, bureau alert, financial weakness, industry downturn) acting before delinquency compounds",
 ]),
 ("VS-68-*", "PA-68.2-credit-limit-management-monitoring.md", "W2490", [
  "- **Escalation-skip risk**: accounts jumped straight to hold-shipment without the reminder ladder collect through conflict rather than process; mitigated by the 30/60/90-day ladder (Step 1: friendly reminder, formal demand, hold) applied in sequence",
  "- **Bucket-drift risk**: 60-day balances quietly aging into the 90-day hold band while untouched; mitigated by the daily past-due report (Step 1) with the Collections Specialist owning each bucket movement",
 ]),
 ("VS-68-*", "PA-68.2-credit-limit-management-monitoring.md", "W2491", [
  "- **Promise-credit risk**: customers skilled at promise-to-pay commitments score better than payers; mitigated by the promise-fulfillment-rate input (Step 1) discounting broken commitments inside the composite score",
  "- **Trend-blindness risk**: a scoring snapshot that hides an improving-or-deteriorating trajectory misprices the next limit action; mitigated by the payment-trend input (Step 1) feeding the W2480 review cycle",
 ]),
 ("VS-68-*", "PA-68.2-credit-limit-management-monitoring.md", "W2492", [
  "- **Hold-overreach risk**: full holds on partially-covered orders stop revenue the available credit still safely supports; mitigated by the partial and conditional release options (Step 1: up to available credit, with payment commitment) before full hold",
  "- **Release-without-commitment risk**: released orders without a documented payment commitment repeat the over-limit cycle next cycle; mitigated by the Analyst's evaluation record (Step 1) governing each release form",
 ]),
 ("VS-68-*", "PA-68.2-credit-limit-management-monitoring.md", "W2493", [
  "- **Provision-mismatch risk**: provisioning on stale aging understates expected loss after a deterioration burst; mitigated by the PFRS 9 expected-credit-loss calculation (Step 1) run on the current aging by account, region and segment",
  "- **Bucket-integrity risk**: mis-aged receivables flatter the 30-day bucket and understate the 120+ tail; mitigated by the system-generated aging across all buckets (Step 1) feeding the Finance Manager's provision",
 ]),
]

# PA-68.3 — Recovery & Write-Off
R += [
 ("VS-68-*", "PA-68.3-bad-debt-recovery-writeoff.md", "W2494", [
  "- **Negotiation-creep risk**: structured payment plans extended repeatedly become de facto credit without a limit decision; mitigated by the documented collection activity (Step 1) with plans bounded at 3–6 months",
  "- **Effort-misallocation risk**: intensive in-person collection spent evenly across accounts dilutes recovery on the balances that matter; mitigated by the high-value-account visit prioritization (Step 1) by the Collections Manager",
 ]),
 ("VS-68-*", "PA-68.3-bad-debt-recovery-writeoff.md", "W2495", [
  "- **Prescription risk**: collection cases filed beyond the prescriptive period forfeit otherwise winnable claims; mitigated by the escalation straight from pre-legal collection (W2494) with external counsel managing the judicial timeline (Step 1)",
  "- **Cost-bleed risk**: legal pursuit of uncollectible judgments spends fees exceeding any recovery; mitigated by the recovery-probability evidence carried from the W2496 decision framework",
 ]),
 ("VS-68-*", "PA-68.3-bad-debt-recovery-writeoff.md", "W2496", [
  "- **Approval-shortcut risk**: write-offs processed below the CFO/Board thresholds erode the provision without governance; mitigated by the tiered review (Step 1: Analyst recommendation, Finance Controller review, CFO approval, Board above threshold)",
  "- **Premature-writeoff risk**: accounts written off while collection avenues remain open abandon recoverable balances; mitigated by the collection-history, legal-status and recovery-probability evidence (Step 1) preceding the recommendation",
 ]),
 ("VS-68-*", "PA-68.3-bad-debt-recovery-writeoff.md", "W2497", [
  "- **Reinstatement-relapse risk**: a recovered account reinstated to full credit re-defaults within the cycle; mitigated by the reinstatement evaluation only after the sustained-payment condition (Step 1) with the COD-only flag carried from W2496",
  "- **Recovery-misposting risk**: recovered amounts posted as new receipts rather than bad-debt recovery income distort both revenue and the provision; mitigated by the recovery-income credit and account update (Step 1)",
 ]),
 ("VS-68-*", "PA-68.3-bad-debt-recovery-writeoff.md", "W2498", [
  "- **Late-claim risk**: claims filed past the policy's notification window forfeit insured recoveries; mitigated by the claim package (Step 1: customer details, outstanding amount, collection history, reason for non-payment) filed per the W2484 policy terms",
  "- **Underdocumentation risk**: claims missing collection evidence settle below entitlement; mitigated by the collection-history attachment (Step 1) proving pursuit before the non-payment",
 ]),
 ("VS-68-*", "PA-68.3-bad-debt-recovery-writeoff.md", "W2499", [
  "- **Lagging-indicator risk**: managing to the bad-debt rate reacts a quarter behind the leading signals; mitigated by the default-predictor analysis (Step 1) feeding tighter credit criteria before losses print",
  "- **Segment-blindness risk**: chain-wide criteria tightened against a problem concentrated in one segment or region; mitigated by the high-risk-segment, industry-concentration and geographic-pattern analysis (Step 1) targeting the recommendation",
 ]),
 ("VS-68-*", "PA-68.3-bad-debt-recovery-writeoff.md", "W2500", [
  "- **Policy-staleness risk**: approval matrices and thresholds unreviewed against the current market misprice risk a year at a time; mitigated by the annual review scope (Step 1: matrix, criteria, thresholds, escalation, write-off, insurance) with CFO approval",
  "- **Loosening-capture risk**: growth pressure tilting the review toward easier credit recreates the losses the policy prevents; mitigated by the review anchored on the W2499 trend evidence before any criteria change",
 ]),
 ("VS-68-*", "PA-68.3-bad-debt-recovery-writeoff.md", "W2501", [
  "- **Single-metric risk**: managing DSO alone rewards collections while limit and concentration risks compound unseen; mitigated by the composite dashboard (Step 1: AR, aging, DSO, bad-debt rate, collection effectiveness, utilization, insurance coverage)",
  "- **Alert-latency risk**: refresh cycles too slow to trigger same-day limit action on a breach; mitigated by the real-time alerts (Step 1) on risk-relevant movements",
 ]),
]

# ---------------- VS-74 — Contractor Jobsite Delivery ----------------

# PA-74.1 — Planning & Scheduling
R += [
 ("VS-74-*", "PA-74.1-jobsite-delivery-planning-scheduling.md", "W2622", [
  "- **Site-access surprise risk**: a truck dispatched to a job site it cannot enter (weight limits, no turning room) returns full and re-delivers another day; mitigated by the access-restriction capture and truck-accessibility verification (Steps 1–2) before dispatch",
  "- **Window-miss risk**: deliveries arriving outside the agreed window find no receiving crew and idle the vehicle; mitigated by the delivery-window agreement and the GPS-tagged delivery order with SMS confirmation (Step 3)",
 ]),
 ("VS-74-*", "PA-74.1-jobsite-delivery-planning-scheduling.md", "W2623", [
  "- **Capacity-overflow risk**: a multi-drop route loaded past vehicle capacity fails mid-sequence and re-sequences the day; mitigated by the total-weight check within vehicle capacity (Step 1) before the route plan issues",
  "- **Hours-of-service breach risk**: a route whose drive-plus-unload time exceeds driver hours stalls at the farthest drop; mitigated by the optimizer's hours-of-service compliance (Step 2) with the drop-sequence manifest loading (Step 3)",
 ]),
 ("VS-74-*", "PA-74.1-jobsite-delivery-planning-scheduling.md", "W2624", [
  "- **Crane-site-failure risk**: a crane arriving to a site without bearing capacity or overhead clearance lifts nothing and bills the full PHP 15K–30K; mitigated by the site-suitability confirmation (Step 1: positioning, ground bearing, overhead clearance) before booking",
  "- **Receiving-crew gap risk**: materials lifted to placement with no contractor personnel to receive them travel back down; mitigated by the receiving-personnel confirmation (Step 2) and the signed delivery receipt at execution (Step 3)",
 ]),
 ("VS-74-*", "PA-74.1-jobsite-delivery-planning-scheduling.md", "W2625", [
  "- **Phase-mismatch risk**: materials delivered for a phase the construction schedule has not reached sit exposed on site and degrade; mitigated by the phase-aligned delivery dates (Step 1) with the 3-day confirmation (Step 3) before each phase ships",
  "- **Reservation-strand risk**: inventory reserved for future phases starves near-term demand as schedules slip; mitigated by the Supply Planning reservation with ROP/safety-stock adjustment (Step 2) and the delay-adjustable calendar (Step 3)",
 ]),
 ("VS-74-*", "PA-74.1-jobsite-delivery-planning-scheduling.md", "W2626", [
  "- **Premium-fee erosion risk**: emergency dispatches waived freely for thin-margin accounts convert the premium into standard service; mitigated by the Store Manager approval gate (Step 1) with the PHP 2K–5K fee applied unless key-account waived (Step 2)",
  "- **Stock-diversion risk**: emergency loads pulled from store stock strand retail shelves to serve one site; mitigated by the availability verification (Step 1) and the per-contractor emergency-frequency tracking (Step 3) feeding W2642's root-cause analysis",
 ]),
 ("VS-74-*", "PA-74.1-jobsite-delivery-planning-scheduling.md", "W2627", [
  "- **Truck-ban risk**: Metro Manila deliveries scheduled inside the 6–9AM/4–8PM truck-ban windows are stopped at the city edge; mitigated by the LGU truck-ban hours check (Step 1) before scheduling and the special-access arrangements (Step 2)",
  "- **Turned-away blindness risk**: access denials resolved ad hoc repeat on the next delivery to the same site; mitigated by the denied-access documentation (Step 3) feeding future planning and the LGU permit/barangay clearance path (Step 2)",
 ]),
 ("VS-74-*", "PA-74.1-jobsite-delivery-planning-scheduling.md", "W2628", [
  "- **Night-safety risk**: off-hours unloading under inadequate lighting turns a routine delivery into an incident; mitigated by the Safety Officer review (Step 2: lighting, high-visibility vests, traffic management) before execution",
  "- **Overtime-cost creep risk**: off-hours premium costs left uncharged subsidize rush behavior; mitigated by the overtime tracking with the premium included in contractor billing (Step 3)",
 ]),
 ("VS-74-*", "PA-74.1-jobsite-delivery-planning-scheduling.md", "W2629", [
  "- **Spec-mismatch risk**: flatbeds or boom trucks arriving without site-compatible specifications cannot unload and still bill the 50–100% premium; mitigated by the equipment specs provided to the contractor for site compatibility (Step 2) before dispatch",
  "- **Rate-capture risk**: negotiated 3PL premiums left unbilled to the order hide the true delivery cost; mitigated by the cost-vs-benchmark tracking (Step 3) feeding proactive fleet planning",
 ]),
]

# PA-74.2 — Execution & Material Handling
R += [
 ("VS-74-*", "PA-74.2-jobsite-delivery-execution-material-handling.md", "W2630", [
  "- **Placement-chaos risk**: materials dumped unlabeled across the site bury the framing stock under finishing materials; mitigated by the designated staging area with separation by type and phase (Step 2) per contractor direction",
  "- **Shortage-at-site risk**: counts disputed after the truck departs have no evidence trail; mitigated by the foreman's manifest verification with damage/shortage notes and the driver's placement photographs (Step 3)",
 ]),
 ("VS-74-*", "PA-74.2-jobsite-delivery-execution-material-handling.md", "W2631", [
  "- **Responsibility-dispute risk**: damage blamed across BuildRight, 3PL and contractor stalls resolution past the 48-hour commitment; mitigated by the evidence-based responsibility determination (Step 2: driver photos, loading records) driving the Step 3 resolution paths",
  "- **Pattern-blindness risk**: repeated minor claims absorbed individually never surface the theft-or-abuse pattern; mitigated by the severity classification (Step 1: <PHP 5K, moderate, >PHP 50K) with LP investigation of patterns (Step 3)",
 ]),
 ("VS-74-*", "PA-74.2-jobsite-delivery-execution-material-handling.md", "W2632", [
  "- **Ineligible-return risk**: used or stale materials collected on site fail inspection and re-deliver at full logistics cost; mitigated by the eligibility verification (Step 1: within 30 days, unused condition) before authorization",
  "- **Dedicated-pickup cost risk**: return pickups dispatched as standalone trips carry full cost for one pallet; mitigated by the pickup combined with the next same-area delivery (Step 2)",
 ]),
 ("VS-74-*", "PA-74.2-jobsite-delivery-execution-material-handling.md", "W2633", [
  "- **POD-gap risk**: deliveries without complete proof of delivery (signature, photos, GPS, timestamp) unwind into billing disputes and BIR exposure; mitigated by the four-part POD capture (Step 1) matched to the delivery order in the system (Step 2)",
  "- **Billing-trigger failure risk**: invoicing triggered without confirmed delivery bills ahead of receipt or not at all; mitigated by the POD-gated invoicing and 3PL settlement (Step 3) with 10-year BIR archiving",
 ]),
 ("VS-74-*", "PA-74.2-jobsite-delivery-execution-material-handling.md", "W2634", [
  "- **PPE-noncompliance risk**: a driver refused at the gate for missing PPE re-delivers another day; mitigated by the full PPE and site safety-briefing requirement (Step 1) before site entry",
  "- **Hazard-blindness risk**: drivers operating near excavations or overhead work without the site's hazard picture create the incident the rules exist to prevent; mitigated by the site-specific rules and hazard identification (Steps 1–2) with random Safety Officer compliance checks (Step 3)",
 ]),
 ("VS-74-*", "PA-74.2-jobsite-delivery-execution-material-handling.md", "W2635", [
  "- **Catch-weight dispute risk**: visually estimated bulk quantities billed on estimated weight invite short-load claims; mitigated by the catch-weight recording with tipped-load photographs (Step 2) and delivered-weight billing (Step 3)",
  "- **Dump-area failure risk**: a tip executed without a designated dump area blocks the site or buries equipment; mitigated by the dump-area confirmation with the contractor (Step 1) before dispatch",
 ]),
 ("VS-74-*", "PA-74.2-jobsite-delivery-execution-material-handling.md", "W2636", [
  "- **Refusal-handling risk**: refused items trucked back without assessment re-deliver the same off-spec material; mitigated by the 24-hour Quality Inspector site assessment (Step 2) against the specification and order agreement",
  "- **Vendor-claim leakage risk**: valid quality failures absorbed as goodwill instead of vendor claims; mitigated by the resolution split (Step 3: replacement with vendor claim vs. specification clarification) and the product-description update",
 ]),
 ("VS-74-*", "PA-74.2-jobsite-delivery-execution-material-handling.md", "W2637", [
  "- **ETA-silence risk**: a delay communicated only on arrival strands the contractor's receiving crew; mitigated by the automated ETA notification at dispatch (Step 1) and the >30-minute exception notification (Step 3) against the ≥90% on-time target",
  "- **Status-gap risk**: tracking that drops mid-route hides the truck's true position from a waiting site; mitigated by the driver's in-app status updates (Step 2: departed, en route, arrived, unloading, complete)",
 ]),
]

# PA-74.3 — Performance Analytics
R += [
 ("VS-74-*", "PA-74.3-jobsite-delivery-performance-analytics.md", "W2638", [
  "- **Metric-gaming risk**: OTIF scored before site verification flatters the metric the customer already disputes; mitigated by the Damage-Free third leg (Step 1) and the trend/root-cause analysis (Step 2) over chronic late routes",
  "- **Segment-blindness risk**: a fleet-average score hiding one contractor segment's chronic failures; mitigated by the per-DC and per-segment scoring (Step 1) reviewed to VP Supply Chain (Step 3)",
 ]),
 ("VS-74-*", "PA-74.3-jobsite-delivery-performance-analytics.md", "W2639", [
  "- **Fee-cost inversion risk**: delivery fees set below true direct-plus-indirect cost quietly sell every contractor delivery at a loss; mitigated by the cost-vs-fee comparison (Step 1) with the Finance Controller profitability review and fee adjustments (Step 3)",
  "- **Optimization-churn risk**: consolidation changes made without modeling disrupt the service the fees fund; mitigated by the modeled levers (Step 2: route consolidation, 3PL rates, crane frequency, self-pickup) quantified before implementation",
 ]),
 ("VS-74-*", "PA-74.3-jobsite-delivery-performance-analytics.md", "W2640", [
  "- **Survey-fatigue risk**: response rates below the 30% target let the scores read only the happiest contractors; mitigated by the post-delivery survey cadence (Step 1) with the 48-hour detractor follow-up (Step 2) validating the signal",
  "- **Feedback-orphan risk**: findings logged but never returned to drivers or scheduling re-score the same complaints next quarter; mitigated by the Logistics Manager's retraining and improvement actions reported quarterly (Step 3)",
 ]),
 ("VS-74-*", "PA-74.3-jobsite-delivery-performance-analytics.md", "W2641", [
  "- **Empty-miles blindness risk**: overlapping routes and empty returns invisible without the GIS view keep paying for dead kilometers; mitigated by the GIS route mapping (Step 1) quantifying overlap, underutilization and empty return miles",
  "- **Change-shock risk**: schedule optimizations imposed without contractor communication read as service degradation; mitigated by the contractor communication and the 4-week monitored rollout (Step 3) with quarterly savings reporting",
 ]),
 ("VS-74-*", "PA-74.3-jobsite-delivery-performance-analytics.md", "W2642", [
  "- **Symptom-treatment risk**: emergency deliveries processed faster without touching their causes grow the premium-cost base; mitigated by the root-cause analysis (Step 1: poor planning, stockout, vendor late, scope change) and the preventive measures (Step 2)",
  "- **Chronic-customer blindness risk**: high-frequency emergency contractors subsidized silently inside standard service; mitigated by the per-contractor frequency analysis (Step 1) with the 20% YoY reduction target tracked (Step 3)",
 ]),
 ("VS-74-*", "PA-74.3-jobsite-delivery-performance-analytics.md", "W2643", [
  "- **Site-capability gap risk**: 3PL partners scored on general delivery metrics hide their failure at construction-site requirements; mitigated by the site-specific metrics (Step 1: on-time, damage, driver compliance, POD completeness, complaint rate) with corrective actions (Step 2)",
  "- **Portfolio-stickiness risk**: volume left with underperformers past the quarterly review for relationship reasons; mitigated by the quarterly allocation to better performers (Step 3) and specialized-partner sourcing for heavy equipment",
 ]),
 ("VS-74-*", "PA-74.3-jobsite-delivery-performance-analytics.md", "W2644", [
  "- **KPI-proliferation risk**: a dashboard reading everything highlights nothing; mitigated by the risk-and-opportunity commentary (Step 2) framing the metrics for the VP Supply Chain review",
  "- **Executive-echo risk**: ops-review presentations repeating the dashboard without decisions attached; mitigated by the COO monthly review carrying strategic initiatives and investment requests (Step 3)",
 ]),
 ("VS-74-*", "PA-74.3-jobsite-delivery-performance-analytics.md", "W2645", [
  "- **Benchmark-lag risk**: strategy set against year-old service and cost data targets a market that has moved; mitigated by the competitive benchmarking and trend review (Step 1) preceding target setting",
  "- **Unfunded-roadmap risk**: implementation roadmaps announced without milestones or resources; mitigated by the roadmap's quarterly milestones, resources and technology/3PL negotiations (Step 3) incorporated into the annual plan",
 ]),
]

REPLACEMENTS = {(vs, fs, wid): bullets for vs, fs, wid, bullets in R}

if __name__ == "__main__":
    pool = _engine.build_pool()
    _engine.apply(REPLACEMENTS, pool)
