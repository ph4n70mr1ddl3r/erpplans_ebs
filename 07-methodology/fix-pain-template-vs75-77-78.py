#!/usr/bin/env python3
"""Wave-50 repair, part 3: VS-75 / VS-77 / VS-78 Pain-Points template sections.

Same class and method as fix-pain-template-vs66-68-74.py: rewrites the pasted
template Pain sections of the digital-engagement (75), construction-staging (77)
and green-building (78) Python-assisted expansion streams with bullets grounded
in each workflow's own steps, via fix-pain-template-engine.py (which replaces
only template-pool bullets, preserves any specific bullet, and skips sections
that are already fully specific).
"""
import importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "fix_pain_template_engine", os.path.join(HERE, "fix-pain-template-engine.py"))
_engine = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_engine)

R = []

# ---------------- VS-75 — Digital Engagement App ----------------

# PA-75.1
R += [
 ("VS-75-*", "PA-75.1-mobile-app-product-feature-management.md", "W2646", [
  "- **Roadmap-shelfware risk**: features shipped on stakeholder volume rather than RICE score crowd the releases with unadopted builds; mitigated by the RICE prioritization and the CIO/CMO-approved quarterly roadmap (Step 2) with post-launch adoption monitoring (Step 3)",
  "- **Staged-rollout stall risk**: a feature failing at the 10% cohort rolls to nobody but lingers half-shipped; mitigated by the 10% → 50% → 100% staged rollout (Step 3) catching defects before full exposure",
 ]),
 ("VS-75-*", "PA-75.1-mobile-app-product-feature-management.md", "W2647", [
  "- **Review-deterioration risk**: negatives unanswered past 24 hours compound into a sub-4.5 rating that suppresses downloads; mitigated by the daily review monitoring with 24-hour response (Step 1) against the 4.5+ star target",
  "- **Stale-listing risk**: screenshots and descriptions lagging the release understate new features and depress conversion; mitigated by the per-release listing refresh with A/B-tested conversion optimization (Step 2)",
 ]),
 ("VS-75-*", "PA-75.1-mobile-app-product-feature-management.md", "W2648", [
  "- **Opt-out spiral risk**: promotional pushes past the frequency cap train users to disable notifications, killing the transactional channel too; mitigated by the frequency cap (max 2/day, Step 2) and the opt-out monitor (<1%/month, Step 3)",
  "- **Timing-blindness risk**: pushes sent outside the optimized windows underperform and burn the audience; mitigated by the timing optimization with A/B-tested messaging (Steps 2–3) against the open-rate (>15%) and CTR (>5%) targets",
 ]),
 ("VS-75-*", "PA-75.1-mobile-app-product-feature-management.md", "W2649", [
  "- **Points-divergence risk**: an app balance disagreeing with the POS-earned total at checkout breaks trust in the digital card; mitigated by the real-time points balance and redemption sync (Step 1) with the digital barcode scanning at POS",
  "- **Expiry-silence risk**: points expiring without reminder forfeit member value and generate service contacts; mitigated by the expiry reminders and tier-upgrade celebrations (Step 2) configured by the Loyalty Program Manager",
 ]),
 ("VS-75-*", "PA-75.1-mobile-app-product-feature-management.md", "W2650", [
  "- **Crash-threshold drift risk**: a crash rate creeping past 0.5% between reviews bleeds DAU before anyone is paged; mitigated by the Firebase/Crashlytics degradation alerts (Step 1) with 24-hour hotfixes for critical issues (Step 2)",
  "- **Bottleneck-accumulation risk**: slow image loads and API timeouts accepted individually degrade the aggregate session experience; mitigated by the weekly bottleneck prioritization (Step 2) reviewed against the DAU/MAU (>20%) and session (>3 min) targets (Step 3)",
 ]),
 ("VS-75-*", "PA-75.1-mobile-app-product-feature-management.md", "W2651", [
  "- **Catalog-divergence risk**: app content lagging the website past the 5-minute window sells wrong prices or unavailable items; mitigated by the real-time sync (Step 2: prices, per-store inventory, launches, removals) with the sync-health monitor (Step 3) resolving failures within 4 hours",
  "- **Feed-quality risk**: enriched content published without data-quality checks propagates bad images or specs to every customer screen; mitigated by the PIM data-quality gate before feeding (Step 1)",
 ]),
 ("VS-75-*", "PA-75.1-mobile-app-product-feature-management.md", "W2652", [
  "- **Compliance-debt risk**: a new SDK or data flow introduced outside the controls breaks the RA 10173 posture the certification relies on; mitigated by the quarterly penetration testing (Step 1) and the DPO's consent, deletion-request and breach discipline (Step 2)",
  "- **Anomaly-latency risk**: unauthorized-access patterns detected only at the quarterly report; mitigated by the continuous security-event monitoring (Step 3) with escalation to the CIO",
 ]),
 ("VS-75-*", "PA-75.1-mobile-app-product-feature-management.md", "W2653", [
  "- **Peeking-error risk**: tests called early on interim results ship noise as winners; mitigated by the required statistical significance with pre-set sample size and duration (Step 1) before the all-user rollout (Step 3)",
  "- **Guardrail-blindness risk**: a winning variant degrading a guardrail metric nets negative overall; mitigated by the guardrail metrics tracked during the test (Step 2) and the documented learnings (Step 3)",
 ]),
]

# PA-75.2
R += [
 ("VS-75-*", "PA-75.2-in-store-digital-experience-self-service.md", "W2654", [
  "- **Kiosk-downtime risk**: a faulty unit beyond the 48-hour replacement window dead-ends the in-store digital journey it anchors; mitigated by the 99% uptime monitor with the 48-hour replacement commitment (Step 1)",
  "- **Kiosk-content-staleness risk**: kiosk screens promoting last month's promo mislead customers at the shelf; mitigated by the monthly refresh with weekly promo updates (Step 2) and the usage-analytics placement optimization (Step 3)",
 ]),
 ("VS-75-*", "PA-75.2-in-store-digital-experience-self-service.md", "W2655", [
  "- **Dead-link risk**: a QR pointing at a delisted product dead-ends the customer mid-aisle; mitigated by the product-page linkage (Step 1) with scan analytics surfacing failing journeys (Step 3)",
  "- **Content-thinness risk**: scans landing on sparse pages train customers to stop scanning; mitigated by the enriched mobile page (Step 2: specs, reviews, how-to, availability) and the enhanced-content opportunities (Step 3)",
 ]),
 ("VS-75-*", "PA-75.2-in-store-digital-experience-self-service.md", "W2656", [
  "- **Shrink-leakage risk**: weight-mismatch and barcode-override exceptions left unworked become the shrink the pilot is judged on; mitigated by the LP Officer's exception-alert response (Step 2) feeding the shrinkage-rate evaluation (Step 3)",
  "- **Intervention-latency risk**: customers queued behind unworked intervention alerts abandon the lane; mitigated by the staffed assist requirement with age-restricted authorization available (Step 2)",
 ]),
 ("VS-75-*", "PA-75.2-in-store-digital-experience-self-service.md", "W2657", [
  "- **Geofence-misdetection risk**: activations firing outside the store, or failing inside it, waste the feature's one first impression; mitigated by the GPS-geofence plus Bluetooth-beacon dual detection (Step 1)",
  "- **Feature-ghost-town risk**: in-store features activated but unused deliver no basket lift; mitigated by the usage-frequency and basket-correlation analysis (Step 3) optimizing the feature set",
 ]),
 ("VS-75-*", "PA-75.2-in-store-digital-experience-self-service.md", "W2658", [
  "- **Delivery-failure risk**: digital receipts silently failing to arrive forfeit the paper saving and the warranty touchpoint; mitigated by the delivery-success-rate monitoring (Step 3) alongside the >50% adoption target",
  "- **Preference-ignoring risk**: receipts pushed against the customer's channel choice train opt-outs; mitigated by the app-and/or-email preference honoring (Step 1)",
 ]),
 ("VS-75-*", "PA-75.2-in-store-digital-experience-self-service.md", "W2659", [
  "- **Adoption-decay risk**: low-adoption stores quietly revert to paper task lists and unverified counts; mitigated by the >95% task-completion tracking (Step 3) with targeted training for low-adoption stores",
  "- **Task-verification gap risk**: tasks marked complete without evidence hide failed planogram execution; mitigated by the completion verification with photo documentation (Step 2)",
 ]),
 ("VS-75-*", "PA-75.2-in-store-digital-experience-self-service.md", "W2660", [
  "- **Bandwidth-starvation risk**: customer Wi-Fi crowding the POS network risks the transaction path for the engagement benefit; mitigated by the adequate-bandwidth requirement for customers and POS (Step 1) with quality monitoring",
  "- **Portal-abandonment risk**: a clunky captive portal loses the customer before the loyalty CTA renders; mitigated by the A/B-tested messaging and engagement tracking (Step 2) with the opt-in-rate analysis (Step 3)",
 ]),
 ("VS-75-*", "PA-75.2-in-store-digital-experience-self-service.md", "W2661", [
  "- **Price-sync failure risk**: an ESL showing yesterday's price at the shelf against a different POS price is the classic overcharge complaint; mitigated by the daily 20–30-label spot-check vs. POS (Step 2) against the 99.9% sync-accuracy target (Step 3)",
  "- **Battery-death risk**: labels dying silently on the shelf revert to frozen prices; mitigated by the low-battery alerts (Step 2) and battery-life management (Step 3)",
 ]),
]

# PA-75.3
R += [
 ("VS-75-*", "PA-75.3-digital-engagement-analytics-optimization.md", "W2662", [
  "- **Attribution-myth risk**: last-click attribution crediting the final touch starves the app's assist channels of credit; mitigated by the cross-channel journey mapping (Step 1) with the CFO's ROI review adjusting investment (Step 3)",
  "- **Journey-fragment risk**: identities unresolved across web, app and store build three customers out of one; mitigated by the unified customer view build (Step 1)",
 ]),
 ("VS-75-*", "PA-75.3-digital-engagement-analytics-optimization.md", "W2663", [
  "- **CPI-illusion risk**: acquisition cost read without retention quality buys downloads that churn within a week; mitigated by the Day 1/7/30 retention comparison by source (Step 2) weighting the per-channel CPI/CPA (Step 1)",
  "- **Churn-signal-ignore risk**: churn signals identified but never wired into campaigns; mitigated by the retention campaigns (Step 3: re-engagement push, personalized recommendations, points acceleration) with measured impact",
 ]),
 ("VS-75-*", "PA-75.3-digital-engagement-analytics-optimization.md", "W2664", [
  "- **Correlation-causation risk**: high QR-scan stores celebrated when the scans merely mark busy stores; mitigated by the correlation-with-performance analysis (Step 2) before the kiosk reallocations (Step 3)",
  "- **Adoption-asymmetry risk**: a chain-wide rollout judged on Tier-1 store usage; mitigated by the per-store promotion identification (Step 3) for lagging locations",
 ]),
 ("VS-75-*", "PA-75.3-digital-engagement-analytics-optimization.md", "W2665", [
  "- **Drop-off-blindness risk**: checkout funnel stages monitored without fix prioritization bleed the >3% conversion target; mitigated by the drop-off identification (Step 1) with the conversion-rate optimizations A/B-tested individually (Step 2)",
  "- **Novelty-decay risk**: one-time optimization wins assumed permanent as traffic mix shifts; mitigated by the monthly impact tracking (Step 3) on conversion, abandonment, AOV and payment mix",
 ]),
 ("VS-75-*", "PA-75.3-digital-engagement-analytics-optimization.md", "W2666", [
  "- **Survey-bias risk**: an in-app NPS reading only the engaged random 10% misses the churned silent majority; mitigated by the random sampling with segmented results (Steps 1–2) surfacing detractor themes by platform and region",
  "- **Detractor-theater risk**: detractor themes reported quarter after quarter without prioritized fixes; mitigated by the CMO's quarterly review approving detractor-fixing features (Step 3)",
 ]),
 ("VS-75-*", "PA-75.3-digital-engagement-analytics-optimization.md", "W2667", [
  "- **Filter-bubble risk**: recommendations narrowing to past purchases shrink discovery baskets; mitigated by the diversity monitoring inside the iteration loop (Step 3) with new data signals incorporated",
  "- **Model-drift risk**: recommendation performance decaying as the catalog shifts under a stale model; mitigated by the CTR (>5%), conversion (>1%) and revenue-contribution (>10%) monitors (Step 1) with quarterly CIO reporting",
 ]),
 ("VS-75-*", "PA-75.3-digital-engagement-analytics-optimization.md", "W2668", [
  "- **Silent-degradation risk**: an integration failing below alert thresholds (stale prices, delayed BOPIS transmission) erodes trust before it pages anyone; mitigated by the failure alerting (Step 1) with the monthly uptime (99.5%), freshness and error-rate review (Step 3)",
  "- **Repeat-incident risk**: incidents patched without preventive measures recur; mitigated by the root-cause analysis with retry-logic and circuit-breaker implementation (Step 2)",
 ]),
 ("VS-75-*", "PA-75.3-digital-engagement-analytics-optimization.md", "W2669", [
  "- **Tech-debt deferral risk**: growth targets set while platform debt compounds under the roadmap; mitigated by the tech-debt line in the review (Step 1) with the CIO's infrastructure-upgrade plan (Step 3)",
  "- **Adoption-plan vacuum risk**: platform investments approved without the adoption plan that fills them; mitigated by the CMO adoption plan combined with the CIO implementation plan to the CEO (Step 3)",
 ]),
]

# ---------------- VS-77 — Construction Material Staging ----------------

# PA-77.1
R += [
 ("VS-77-*", "PA-77.1-project-material-planning-phasing.md", "W2694", [
  "- **Long-lead blindside risk**: imported tiles needed at 60–90 days discovered after the construction clock starts; mitigated by the long-lead identification with advance POs (Step 2) before the phased schedule locks (Step 3)",
  "- **Quantity-basis risk**: quantities estimated off the blueprint without the bill-of-quantities cross-check over- and under-buy whole phases; mitigated by the blueprint review with per-phase estimates (Step 1) and the contractor sign-off (Step 3)",
 ]),
 ("VS-77-*", "PA-77.1-project-material-planning-phasing.md", "W2695", [
  "- **Reservation-cannibalization risk**: ROP replenishment consuming stock a project PO already reserved strands the phase; mitigated by the reservation logic preventing ROP consumption (Step 1) with ATP showing uncommitted availability only",
  "- **Retail-starvation risk**: project reservations sized without the retail floor's needs turn one big project into chain stockouts; mitigated by the Category Manager's stockout monitoring and allocation adjustments (Step 2)",
 ]),
 ("VS-77-*", "PA-77.1-project-material-planning-phasing.md", "W2696", [
  "- **Visual-equivalence risk**: a technically-equivalent tile substituted without the contractor's eye fails approval on site and re-trucks the delivery; mitigated by the visual-equivalence evaluation with contractor approval (Steps 2–3) before any reservation update",
  "- **Undocumented-substitution risk**: swaps agreed verbally during site calls vanish from the project record; mitigated by the documented rationale (Step 2) with the project file carrying every approval (Step 3)",
 ]),
 ("VS-77-*", "PA-77.1-project-material-planning-phasing.md", "W2697", [
  "- **Escalation-cap breach risk**: market movements past the formula's cap turn the locked price into BuildRight's loss; mitigated by the maximum-cap term (Step 1) with the Pricing Analyst's margin-erosion escalation below 15% (Step 2)",
  "- **Lock-duration risk**: a 3–12 month lock set against a project that runs longer reprices the tail at market; mitigated by the duration-matched lock terms (Step 1) and the Finance monthly margin tracking including holding cost (Step 3)",
 ]),
 ("VS-77-*", "PA-77.1-project-material-planning-phasing.md", "W2698", [
  "- **Project-retail collision risk**: project demand exceeding 30% of an item's total silently starves retail; mitigated by the >30% flag with allocation rules (Step 3) and the forecast-adjusted procurement (Step 2)",
  "- **Spike-overreaction risk**: one project's quantities read as a demand trend and over-ordered chain-wide; mitigated by the check against the retail forecast (Step 1) separating project spikes from base demand",
 ]),
 ("VS-77-*", "PA-77.1-project-material-planning-phasing.md", "W2699", [
  "- **Unconfirmed-change risk**: change orders discussed but never written confirmed leave procurement and reservations stale; mitigated by the written confirmation requirement (Step 3) before the PO and reservation updates",
  "- **Restockability-miss risk**: deletions accepted without the restocking-feasibility check strand unsaleable returns; mitigated by the Supply Planning assessment (Step 2: availability, restocking, schedule, cost impact)",
 ]),
 ("VS-77-*", "PA-77.1-project-material-planning-phasing.md", "W2700", [
  "- **Spec-availability gap risk**: specs documented for products no vendor can certify stall the project at procurement; mitigated by the availability verification with certification documents (Step 2: PS mark, ASTM, ISO)",
  "- **Certificate-missing risk**: project documentation submitted without the test certificates fails the contractor's QA audit; mitigated by the Quality-provided certificates (Step 3: cement compressive, steel tensile, tile breaking strength) in the project package",
 ]),
 ("VS-77-*", "PA-77.1-project-material-planning-phasing.md", "W2701", [
  "- **Terms-creep risk**: Net 60 with 10% retention negotiated per project without approval authority compounds receivable risk; mitigated by the Credit Manager's authorization-matrix approval (Step 1) over the milestone, progress-billing and retention terms",
  "- **Retention-release leakage risk**: completed projects never releasing retention strand the contractor's final margin and the relationship; mitigated by the payment-health monitoring ensuring retention release upon completion (Step 3)",
 ]),
]

# PA-77.2
R += [
 ("VS-77-*", "PA-77.2-phased-delivery-execution-site-coordination.md", "W2702", [
  "- **Premature-trigger risk**: phases shipped on early notification arrive to an unready site and weather in the mud; mitigated by the 3–5-day advance notice (Step 1) with the scheduled ETA confirmation (Step 3)",
  "- **Outbound-quality risk**: a phase picked short or damaged discovered at site restarts the whole delivery cycle; mitigated by the quantity verification against the phase list with Quality's outbound inspection (Step 2)",
 ]),
 ("VS-77-*", "PA-77.2-phased-delivery-execution-site-coordination.md", "W2703", [
  "- **Blanket-signature risk**: receipts signed unverified convert shortages into disputed billing milestones; mitigated by the item-by-item manifest check with photographed exceptions (Steps 1–2) before the Rep's billing trigger (Step 3)",
  "- **Exception-drift risk**: noted exceptions logged but never resolved hang over the project file; mitigated by the exception processing (Step 3: replacement, shortage investigation, reservation adjustment)",
 ]),
 ("VS-77-*", "PA-77.2-phased-delivery-execution-site-coordination.md", "W2704", [
  "- **Improper-storage damage risk**: cement left on wet ground or lumber stacked tight ruins materials BuildRight supplied but cannot reclaim; mitigated by the storage advisory (Step 1: cement off-ground, tiles flat, lumber spaced, paint cool) with periodic site assessments (Step 2)",
  "- **Liability-blur risk**: post-delivery damage blamed on product quality instead of storage; mitigated by the documented assessments (Step 2) and the contractor-expense replacement rule post-delivery (Step 3)",
 ]),
 ("VS-77-*", "PA-77.2-phased-delivery-execution-site-coordination.md", "W2705", [
  "- **Cascading-shortage risk**: reallocating materials to an ahead-of-schedule phase stockouts the later phase it fed; mitigated by the future-stockout check with additional procurement (Step 2) and the cascading-impact monitoring (Step 3)",
  "- **Verbal-reallocation risk**: site-level agreement to move materials without the ERP update corrupts every downstream reservation; mitigated by the documented request (Step 1) and the ERP update (Step 3)",
 ]),
 ("VS-77-*", "PA-77.2-phased-delivery-execution-site-coordination.md", "W2706", [
  "- **Surplus-eligibility risk**: used or weathered materials collected as returns fail inspection at cost to both sides; mitigated by the eligibility verification (Step 1: unused condition, return window) before pickup",
  "- **Credit-friction risk**: restocking-fee surprises at close-out poison an otherwise clean project; mitigated by the disclosed 5–10% restocking fee credited against billing (Step 3)",
 ]),
 ("VS-77-*", "PA-77.2-phased-delivery-execution-site-coordination.md", "W2707", [
  "- **Lead-time mismatch risk**: local 7–21-day and import 45–90-day items sequenced without their offsets arrive phase-misaligned; mitigated by the lead-time mapping with sequenced POs (Step 1) for on-time phase delivery",
  "- **Consolidation-gap risk**: multi-vendor materials arriving unconsolidated force partial deliveries; mitigated by the DC staging coordination before the delivery date (Step 3) with the vendor-performance escalation (Step 2)",
 ]),
 ("VS-77-*", "PA-77.2-phased-delivery-execution-site-coordination.md", "W2708", [
  "- **Penalty-spiral risk**: 1%/day penalties accruing on an unmanaged delay compound past the project's margin; mitigated by the early delay report with revised ETA (Step 1) and the negotiated resolution (Step 2: waiver, expedited replacement)",
  "- **Root-cause recurrence risk**: delays root-caused to weather repeatedly without prevention; mitigated by the prevention implementation (Step 3: earlier staging, backup trucks, weather planning) against the ≥95% on-time target",
 ]),
 ("VS-77-*", "PA-77.2-phased-delivery-execution-site-coordination.md", "W2709", [
  "- **Reconciliation-gap risk**: projects closing with ordered-vs-delivered-vs-returned unreconciled strand open reservations and unbilled items; mitigated by the three-way reconciliation (Step 1) before Finance completes billing and closes the account (Step 2)",
  "- **Reservation-remnant risk**: unused reservations left open after close-out ghost-lock inventory for the next project; mitigated by the reservation release with staging-area closure and PO cancellation (Step 3)",
 ]),
]

# PA-77.3
R += [
 ("VS-77-*", "PA-77.3-project-material-reconciliation-analytics.md", "W2710", [
  "- **Estimate-drift risk**: the same over-estimation pattern repeating across projects because nobody closes the loop; mitigated by the improved estimation templates (Step 2) feeding the pricing-model factors (Step 3)",
  "- **Variance-noise risk**: per-item noise burying the category-level biases worth managing; mitigated by the per-category and total-PHP variance view (Step 1) with significant-variance investigation",
 ]),
 ("VS-77-*", "PA-77.3-project-material-reconciliation-analytics.md", "W2711", [
  "- **Metric-isolation risk**: project delivery KPIs tracked apart from retail metrics hide the program's true service cost; mitigated by the comparison vs. standard retail metrics (Step 1)",
  "- **Pattern-without-action risk**: damage-prone categories identified but shipped the same way; mitigated by the contractor-facing quarterly reviews setting delivery expectations (Step 3)",
 ]),
 ("VS-77-*", "PA-77.3-project-material-reconciliation-analytics.md", "W2712", [
  "- **Mix-drift risk**: portfolio margin read without the project-mix shift blames pricing for what is mix; mitigated by the margin-driver analysis (Step 2: size, category mix, delivery cost, price lock, change orders)",
  "- **Pipeline-hope risk**: revenue targets carried on pipeline probability nobody re-reviews; mitigated by the CFO-reviewed pricing strategy and targets (Step 3) on the compiled pipeline (Step 1)",
 ]),
 ("VS-77-*", "PA-77.3-project-material-reconciliation-analytics.md", "W2713", [
  "- **Carrying-cost invisibility risk**: quotes priced without the 15–20% annual carrying rate on PHP 200M–500M reserved stock subsidize long projects; mitigated by the carrying-cost calculation (Step 1) incorporated into pricing (Step 3)",
  "- **Early-reservation incentive risk**: contractors reserving whole-project quantities at award because waiting costs them nothing; mitigated by the high-cost project identification (Step 2: long duration, early reservation, slow phases) with just-in-phase recommendations",
 ]),
 ("VS-77-*", "PA-77.3-project-material-reconciliation-analytics.md", "W2714", [
  "- **Survey-silence risk**: a <60% response reading only the angriest and the happiest; mitigated by the >60% response target (Step 1) with the satisfaction-driver analysis (Step 2)",
  "- **Repeat-assumption risk**: repeat rate celebrated without the retention trend underneath; mitigated by the annual portfolio review (Step 3: top-20 customers, retention trend, lifetime value, account strategies)",
 ]),
 ("VS-77-*", "PA-77.3-project-material-reconciliation-analytics.md", "W2715", [
  "- **Waste-normalization risk**: returns near the 10% target accepted as the cost of doing projects; mitigated by the waste-reduction levers (Step 2: estimation, packaging, on-site advisory, phased delivery) against the <10% target",
  "- **Disposal-compliance risk**: damaged materials disposed outside the requirements create the environmental exposure the program exists to avoid; mitigated by the disposal-requirements tracking (Step 1) per project",
 ]),
 ("VS-77-*", "PA-77.3-project-material-reconciliation-analytics.md", "W2716", [
  "- **Concentration-blindspot risk**: vendor or import dependency assessed chain-wide but not per project; mitigated by the per-project risk assessment (Step 1: vendor concentration, import dependency, DC capacity, weather, geopolitical)",
  "- **Unquantified-mitigation risk**: resilience investments approved without the exposure they protect; mitigated by the PHP-quantified risk exposure per project (Step 2) with the VP-reviewed mitigation investments (Step 3)",
 ]),
 ("VS-77-*", "PA-77.3-project-material-reconciliation-analytics.md", "W2717", [
  "- **Target-inheritance risk**: growth targets set from last year's numbers without the market view; mitigated by the 3-year trend, market-share and competitive-positioning review (Step 1)",
  "- **Roadmap-without-budget risk**: a strategy roadmap presented outside the annual operating plan; mitigated by the CEO presentation incorporated into the annual plan and budget (Step 3)",
 ]),
]

# ---------------- VS-78 — Green Building Advisory ----------------

# PA-78.1
R += [
 ("VS-78-*", "PA-78.1-green-product-curation-certification.md", "W2718", [
  "- **Certificate-forge risk**: a supplier's lapsed or fabricated certification riding on the Green Choice designation; mitigated by the validity confirmation with the issuing body (Step 2) before the ERP designation (Step 3)",
  "- **Criteria-drift risk**: green criteria widening without the standards' updates dilute what the designation promises; mitigated by the documented criteria (Step 1) behind the filterable 'BuildRight Green Choice' designation (Step 3)",
 ]),
 ("VS-78-*", "PA-78.1-green-product-curation-certification.md", "W2719", [
  "- **Score-washing risk**: sustainability scores assigned without supplier engagement become unimprovable labels; mitigated by the development work with suppliers (Step 2: certification support, carbon measurement) alongside the scored evaluation (Step 1)",
  "- **Threshold-erosion risk**: the Green Choice minimum slipping to keep a favored supplier; mitigated by the minimum threshold applied in selection (Step 3) with the reported supplier distribution",
 ]),
 ("VS-78-*", "PA-78.1-green-product-curation-certification.md", "W2720", [
  "- **Knowledge-staleness risk**: BERDE/LEED guidance aged against code updates misadvises certification-targeted projects; mitigated by the maintained knowledge base (Step 1: BERDE, LEED, PH Green Building Code, LGU ordinances)",
  "- **Product-credit mismatch risk**: products mapped to credits they no longer earn break a customer's submission; mitigated by the product-to-credit mapping with documentation requirements (Step 2) trained into staff (Step 3)",
 ]),
 ("VS-78-*", "PA-78.1-green-product-curation-certification.md", "W2721", [
  "- **Premium-erosion risk**: green premiums discounted toward conventional prices without recovering certification cost; mitigated by the premium-vs-cost validation (Step 1) with the 30–35% margin guard (Step 2)",
  "- **Adoption-margin tension risk**: driving adoption through price cuts that gut the program's own economics; mitigated by the sell-through and price-sensitivity monitoring (Step 2) with Finance tracking green revenue share (Step 3)",
 ]),
 ("VS-78-*", "PA-78.1-green-product-curation-certification.md", "W2722", [
  "- **Display-decay risk**: the green section's markers and labels aging into floor-level inaccuracy; mitigated by the quarterly display rotation with current-label checks (Step 2)",
  "- **Demo-evidence risk**: live comparisons (LED vs. incandescent) run without measurement make claims customers can discount; mitigated by the sales-lift and engagement measurement (Step 3) on the designed experience (Step 1)",
 ]),
 ("VS-78-*", "PA-78.1-green-product-curation-certification.md", "W2723", [
  "- **Claim-overreach risk**: content overstating savings invites the greenwashing challenge the program fears; mitigated by the case-study and comparison format (Step 1) with the engagement and conversion measurement (Step 3)",
  "- **Channel-orphan risk**: strong hub content invisible in the channels customers actually use; mitigated by the multi-channel distribution (Step 2: hub, social, kiosk, newsletter, YouTube, workshops)",
 ]),
 ("VS-78-*", "PA-78.1-green-product-curation-certification.md", "W2724", [
  "- **Stale-document risk**: certifications or declarations compiled past their currency fail the project's submission review; mitigated by the currency verification (Step 2) against the BERDE/LEED credit requirements",
  "- **Credit-mapping error risk**: products mapped to the wrong credits shift the project's scorecard and its certification target; mitigated by the product-credit mapping summary delivered with the package (Step 3)",
 ]),
 ("VS-78-*", "PA-78.1-green-product-curation-certification.md", "W2725", [
  "- **Badge-inflation risk**: sustainability badges applied broadly dilute the filter customers pay attention to; mitigated by the PIM enrichment criteria (Step 1) behind the category-wide sustainability filter (Step 2)",
  "- **Calculator-credibility risk**: a savings calculator overstating payback undermines the program's core claim; mitigated by the savings-calculator and comparison-tool monitoring (Step 3) against filter usage and conversion",
 ]),
]

# PA-78.2
R += [
 ("VS-78-*", "PA-78.2-green-building-project-consultation.md", "W2726", [
  "- **Overselling risk**: consultation recommendations drifting past the project's stated green target into premium upselling; mitigated by the target/budget-based recommendation (Steps 1–2) with the escalated advanced-support path (Step 3)",
  "- **Savings-defensibility risk**: energy/water savings quoted without a calculation basis collapse under the customer's bill comparison; mitigated by the savings calculations with payback periods (Step 2) in the quotation's benefit summary (Step 3)",
 ]),
 ("VS-78-*", "PA-78.2-green-building-project-consultation.md", "W2727", [
  "- **Auditor-quality risk**: partner auditors recommending off-brand products break the referral's trusted-adviser premise; mitigated by the BuildRight-product recommendations with savings basis (Step 2) and the conversion tracking (Step 3)",
  "- **Referral-leak risk**: audit leads dispatched without follow-up convert for the partner, not BuildRight; mitigated by the Sales Associate follow-up with bundled pricing (Step 3)",
 ]),
 ("VS-78-*", "PA-78.2-green-building-project-consultation.md", "W2728", [
  "- **Partnership-drift risk**: architect/engineer partnerships signed and left unmanaged decay into price-only relationships; mitigated by the quarterly updates with pipeline visibility and the feedback loop (Step 3)",
  "- **Knowledge-gap risk**: partner sessions aging against the new-product pipeline misalign specifications; mitigated by the product-knowledge sessions covering specs and BERDE/LEED contributions (Step 2)",
 ]),
 ("VS-78-*", "PA-78.2-green-building-project-consultation.md", "W2729", [
  "- **Attendance-vanity risk**: workshops measured on heads rather than the conversion the program needs; mitigated by the sales-lift and workshop-to-project conversion measurement (Step 3)",
  "- **Stock-miss risk**: featured products out of stock at the workshop squander the demand the event creates; mitigated by the Category Manager's in-stock and display assurance (Step 2)",
 ]),
 ("VS-78-*", "PA-78.2-green-building-project-consultation.md", "W2730", [
  "- **Stream-contamination risk**: LED, paint and fixtures mixed into the wrong disposal stream create the liability the program avoids; mitigated by the recyclability assessment with per-stream routing (Step 1: recycling partner, hazwaste vendor, manufacturer take-back)",
  "- **Event-dependency risk**: customer recycling waiting on quarterly events accumulates in garages and erodes trust; mitigated by the quarterly collection events with LGU partnership and loyalty incentives (Step 2) and the end-of-life metrics (Step 3)",
 ]),
 ("VS-78-*", "PA-78.2-green-building-project-consultation.md", "W2731", [
  "- **Probability-inflation risk**: pipeline forecasts weighted by optimism rather than stage; mitigated by the probability-weighted forecast across stages (Step 1) with FP&A's actual-vs-forecast tracking (Step 2)",
  "- **ESG-claim gap risk**: green contributions reported without the project evidence behind them; mitigated by the Coordinator's ESG reporting on supplied BERDE/LEED projects (Step 3)",
 ]),
 ("VS-78-*", "PA-78.2-green-building-project-consultation.md", "W2732", [
  "- **Score-gaming risk**: suppliers polishing disclosures without operational change to hold the 70/100 threshold; mitigated by the multi-dimension scorecard (Step 1: certifications, carbon, sourcing, packaging, labor, end-of-life) with development plans below threshold (Step 2)",
  "- **Opportunity-paralysis risk**: excellent sustainability stories left unco-marketed; mitigated by the opportunity identification (Step 3: increase, improve-or-replace, co-market)",
 ]),
 ("VS-78-*", "PA-78.2-green-building-project-consultation.md", "W2733", [
  "- **NPS-vanity risk**: consultation NPS tracked without the knowledge-gap fixes that move it; mitigated by the gap and issue analysis (Step 2) with the implemented improvements tracked next quarter (Step 3)",
  "- **Pricing-perception blindspot risk**: green pricing objections read as product objections; mitigated by the pricing-perception dimension in the survey (Step 1)",
 ]),
]

# PA-78.3
R += [
 ("VS-78-*", "PA-78.3-sustainability-compliance-analytics.md", "W2734", [
  "- **Growth-attribution risk**: green growth credited to the program when the 15–20% market CAGR drives it; mitigated by the market-growth and competitor context (Step 2) around the category analytics (Step 1)",
  "- **Forecast-theater risk**: 3-year projections built to the investment answer already chosen; mitigated by the CFO/CEO strategic-planning review (Step 3) on the stated assumptions",
 ]),
 ("VS-78-*", "PA-78.3-sustainability-compliance-analytics.md", "W2735", [
  "- **Methodology-fragility risk**: impact numbers built on assumptions collapse under ESG-report scrutiny; mitigated by the validated, documented methodology (Step 2: DOE baselines, utility data, FSC records) before the ESG summary (Step 3)",
  "- **Unit-confusion risk**: energy, water, carbon and VOC metrics mixed without per-category discipline; mitigated by the per-benefit-category calculation (Step 1)",
 ]),
 ("VS-78-*", "PA-78.3-sustainability-compliance-analytics.md", "W2736", [
  "- **Ordinance-lag risk**: LGU green ordinances adopted before the assortment and training respond; mitigated by the impact assessment with the accelerated-assortment and staff-training response (Step 3)",
  "- **Compliance-myopia risk**: monitoring the code but missing the customer-advisory opportunity it creates; mitigated by the customer-advisory assessment (Step 2) alongside own-construction compliance",
 ]),
 ("VS-78-*", "PA-78.3-sustainability-compliance-analytics.md", "W2737", [
  "- **Claim-verification risk**: vendor-supplied lifecycle data taken at face value into customer-facing claims; mitigated by the cross-checks with third-party LCA verification for key categories (Step 2)",
  "- **Scope-3 leakage risk**: LCA data gathered but not fed to the emissions accounting it exists for; mitigated by the Scope 3 contribution (Step 3) from the sustainability database (Step 1)",
 ]),
 ("VS-78-*", "PA-78.3-sustainability-compliance-analytics.md", "W2738", [
  "- **Greenwashing exposure risk**: green revenue disclosed without defensible definitions invites regulator and NGO challenge; mitigated by the CFO's definition review against GRI/SASB (Step 2) before external reporting (Step 3)",
  "- **Category-mixing risk**: revenue classified green by loose attribution inflates the 5–8% target metric; mitigated by the benefit-category breakdown (Step 1) under the approved definitions",
 ]),
 ("VS-78-*", "PA-78.3-sustainability-compliance-analytics.md", "W2739", [
  "- **Award-without-substance risk**: nominations built on marketing claims rather than project evidence; mitigated by the case-study evidence with project data and testimonials (Step 2) behind the nominations (Step 1)",
  "- **Recognition-silo risk**: awards won but never leveraged in trade communications; mitigated by the press, social, in-store and trade leverage (Step 3)",
 ]),
 ("VS-78-*", "PA-78.3-sustainability-compliance-analytics.md", "W2740", [
  "- **Benchmark-echo risk**: benchmarking the same competitor set annually misses the new entrants; mitigated by the multi-dimension benchmark (Step 1: assortment, certification, pricing, experience, digital, ESG disclosure) refreshed with the roadmap",
  "- **Strength-lag risk**: differentiation messaging aging against the closed gaps; mitigated by the messaging incorporating the improvement roadmap (Step 3) on the identified advantages and gaps (Step 2)",
 ]),
 ("VS-78-*", "PA-78.3-sustainability-compliance-analytics.md", "W2741", [
  "- **Target-stretch risk**: green revenue targets set without the product-count and pipeline capacity to carry them; mitigated by the cross-functional target setting (Step 2: revenue %, product count, pipeline) on the 3-year trend review (Step 1)",
  "- **Roadmap-drift risk**: quarterly milestones announced without the launch calendar and rollout to carry them; mitigated by the roadmap's milestones, category-launch calendar, store rollout and digital upgrade (Step 3)",
 ]),
]

REPLACEMENTS = {(vs, fs, wid): bullets for vs, fs, wid, bullets in R}

if __name__ == "__main__":
    pool = _engine.build_pool()
    _engine.apply(REPLACEMENTS, pool)
