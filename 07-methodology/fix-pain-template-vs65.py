#!/usr/bin/env python3
"""Wave-50 repair, part 1: VS-65 marketplace Pain-Points template sections.

The 2026-06-20 Expansion-block rework (96a53dff) replaced the Check-10-detectable
boilerplate in the seven Python-assisted value streams with a *different* verbatim
paste: every workflow's '### Pain Points / Risks' section became one of three
2-bullet template combos (Integration-failure+Data-quality / +Inventory-desync /
+Reconciliation-error), identical across up to 152 workflows. This script rewrites
each affected VS-65 section with workflow-specific bullets grounded in the
workflow's own steps and touchpoints. Every replacement asserts the old bullets
are pool members before writing (exact-match repair discipline).
"""
import importlib.util, os

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "fix_pain_template_engine", os.path.join(HERE, "fix-pain-template-engine.py"))
_engine = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_engine)


# (file-suffix, W-id) -> new bullets
REPLACEMENTS = {
 ("PA-65.1-marketplace-channel-onboarding.md", "W2406"): [
  "- **Commission-drift risk**: the 5–15% commission evaluated at platform selection is re-tierable by the marketplace after onboarding, silently degrading channel margin; mitigated by the seller-agreement change-notice terms secured in the legal review (Step 2) and the W2423 monthly effective-commission recomputation",
  "- **Channel-exit risk**: seller-agreement terms on data sharing, IP and dispute resolution accepted at registration constrain a later sunset; mitigated by the legal and finance review gating signature (Step 2) and the W2429 annual review's expand/maintain/sunset decision",
 ],
 ("PA-65.1-marketplace-channel-onboarding.md", "W2407"): [
  "- **Guideline-takedown risk**: storefront content violating marketplace guidelines (branding misuse, category misplacement) risks listing suppression or store takedown after launch; mitigated by the launch gated on marketplace-guideline compliance (Step 1) with Brand Manager review of banner and category assets",
  "- **Content-staleness risk**: store policies, shipping options and service info published at setup drift from current operations; mitigated by Digital Marketing owning storefront content and the W2419 monthly listing audit extended to the policy fields",
 ],
 ("PA-65.1-marketplace-channel-onboarding.md", "W2408"): [
  "- **Commission-math risk**: marketplace prices must carry the commission adjustment on top of BuildRight price; publishing the unadjusted price shifts the commission onto margin on every order; mitigated by the commission-adjusted price build (Step 2) and the CTL-200 marketplace order & settlement reconciliation flagging net-realized-vs-listed gaps",
  "- **Assortment-leakage risk**: excluded categories (consignment, heavy/bulky, low-margin) re-enter the marketplace assortment through bulk listing uploads; mitigated by the SKU-selection exclusion filters (Step 1) and the W2419 listing-quality audit",
 ],
 ("PA-65.1-marketplace-channel-onboarding.md", "W2409"): [
  "- **Sync-latency risk**: inventory lag between the scheduled pushes oversells marketplace stock another channel already sold; mitigated by the integration-health monitor (Step 2: sync latency, error rate, data accuracy) and issue resolution inside the marketplace's 24-hour SLA",
  "- **Certification-regression risk**: a marketplace API version change after certification silently breaks field mappings (order download, shipment push, return status); mitigated by sandbox testing before certification (Step 1) and the IT Integration Lead's ownership of the error-rate monitor",
 ],
 ("PA-65.1-marketplace-channel-onboarding.md", "W2410"): [
  "- **Margin-blind-flash-sale risk**: flash-deal discount levels stack with marketplace commission and co-op spend, driving event contribution negative at velocity; mitigated by the real-time campaign monitor (Step 2: sales velocity, conversion, reviews) triggering mid-event price and allocation adjustments",
  "- **Campaign-stockout risk**: campaign velocity outruns the reserved allocation and the listing stocks out mid-event, wasting the co-op budget; mitigated by the inventory-allocation adjustment lever (Step 2) fed by W2420's stock-out monitoring",
 ],
 ("PA-65.1-marketplace-channel-onboarding.md", "W2411"): [
  "- **Auto-reply-mismatch risk**: marketplace chat auto-replies answering with BuildRight's own policies (return window, shipping fees) rather than the platform's create dispute losses; mitigated by the CS-agent training on marketplace-specific policies (Step 1) before the chat tools go live",
  "- **Response-SLA risk**: marketplace response-time requirements are stricter than own-channel queues and go unnoticed at peak; mitigated by the CS Supervisor's configuration ownership with escalation to the CS Director per the marketplace SLA",
 ],
 ("PA-65.1-marketplace-channel-onboarding.md", "W2412"): [
  "- **Allocation-starvation risk**: marketplace share set too low strands sellable stock in stores while the listing stocks out; set too high it starves own-channel availability; mitigated by the weekly sell-through rebalance (Step 1) and W2420's delist-before-stock-out trigger",
  "- **Double-promise risk**: an allocation reservation not honored by the fulfilling source promises the same unit to two channels; mitigated by the W2414 routing reserving inventory at order download and the weekly allocation review",
 ],
 ("PA-65.1-marketplace-channel-onboarding.md", "W2413"): [
  "- **Baseline-drift risk**: acquisition costs and fees measured at launch harden into standing targets that no longer reflect the channel; mitigated by the baseline owned by GM, Digital Commerce Inc. and the W2425 dashboard re-benchmarking the same metrics daily",
  "- **Fee-stack omission risk**: marketplace net margin computed without the commission/shipping/fee stack overstates the channel against own ecommerce; mitigated by the baseline explicitly carrying marketplace fees and net margin (Step 1) per the W2424 channel-P&L convention",
 ],
 ("PA-65.2-marketplace-order-inventory-sync.md", "W2414"): [
  "- **Routing-misroute risk**: an order routed to a source whose stated availability was stale cancels after the customer has waited; mitigated by the VS-60 routing logic reserving inventory at download (Step 1) and W2415's 15-minute availability pushes",
  "- **Field-mapping risk**: marketplace order attributes (SKU codes, buyer names, addresses) mapped incorrectly at conversion produce unfulfillable BuildRight orders; mitigated by the conversion validation in Step 1 with exceptions flagged to the Ecommerce Operations Manager",
 ],
 ("PA-65.2-marketplace-order-inventory-sync.md", "W2415"): [
  "- **Oversell-window risk**: the 15-minute push cadence leaves a window in which two channels sell the last unit; mitigated by the availability push deducting the marketplace allocation before publish (Step 1) and W2420's delist-before-stock-out trigger",
  "- **Sync-divergence risk**: a failed push leaves marketplace quantities at stale values until the next cycle; mitigated by the sync-error handling and discrepancy reconciliation in Step 1 backed by the IT Integration Lead's weekly monitor",
 ],
 ("PA-65.2-marketplace-order-inventory-sync.md", "W2416"): [
  "- **Tracking-push failure risk**: a shipment updated in the warehouse but not pushed to the marketplace shows as unshipped, prompting customer disputes and platform penalties; mitigated by the tracking-number push (Step 2) with the order-status auto-update as the completion proof",
  "- **Suboptimal-source risk**: seller-managed orders routed to a wrong DC or an unstocked store inflate split shipments and delivery cost; mitigated by the VS-60 routing to the optimal source (Step 1b) under the VP Supply Chain accountability",
 ],
 ("PA-65.2-marketplace-order-inventory-sync.md", "W2417"): [
  "- **Return-abuse risk**: a marketplace return refunded on the platform's timeline can ship back a used or wrong item; mitigated by the refund processed upon physical receipt (Step 1) and the CSA approve/contest review at notification",
  "- **Contest-window risk**: contesting an invalid return only at goods receipt misses the platform's dispute window and forfeits the claim; mitigated by the CSA review at the return notification (Step 1) rather than after transit",
 ],
 ("PA-65.2-marketplace-order-inventory-sync.md", "W2418"): [
  "- **Price-war risk**: matching every marketplace competitor move ratchets prices below floor with no margin check; mitigated by the commission-adjusted sync baseline (Step 1) and adjustment recommendations owned by GM, Digital Commerce Inc.",
  "- **Stale-price sale risk**: a BuildRight price change not yet synced sells at the outdated marketplace price; mitigated by the daily sync cycle (Step 1) and the W9 financial close reconciling realized vs. listed prices",
 ],
 ("PA-65.2-marketplace-order-inventory-sync.md", "W2419"): [
  "- **Search-rank decay risk**: stale images, thin titles and unanswered reviews sink listings below marketplace search thresholds, hiding live stock; mitigated by the monthly audit (Step 1: image quality, title optimization, keyword relevance, review response) updating underperformers",
  "- **Description-accuracy risk**: listing copy overstating specs drives returns and review damage; mitigated by the description-accuracy check in the monthly audit with product issues escalated to the Category Manager per W2421",
 ],
 ("PA-65.2-marketplace-order-inventory-sync.md", "W2420"): [
  "- **Delist-lag risk**: a fast seller stocks out before the delist lands, cancelling marketplace orders and consuming the platform's seller metrics; mitigated by the continuous sell-through monitor flagging approaching stock-outs (Step 1) with pre-emptive delisting",
  "- **Allocation-miss risk**: replenishment generated for store demand ignores the marketplace allocation and keeps the listing dark; mitigated by the allocation-adjustment lever (Step 1) operating on the W105 multi-channel allocation base",
 ],
 ("PA-65.2-marketplace-order-inventory-sync.md", "W2421"): [
  "- **Review-latency risk**: unanswered negative reviews on the marketplace storefront depress conversion for the whole assortment; mitigated by the daily monitoring cadence (Step 1) with resolution offers on every negative",
  "- **Quality-issue-blindness risk**: defect reviews handled as service cases never reach the owning category; mitigated by the escalation-to-Category-Manager routing (Step 1) feeding W2419's listing optimization",
 ],
 ("PA-65.3-marketplace-performance-settlement.md", "W2422"): [
  "- **Deduction-acceptance risk**: settlement deductions (commissions, subsidies, refunds) accepted without a line-level match quietly become the channel's standing cost; mitigated by the line-level verification (Step 1: gross sales, commission, shipping, subsidies, refunds, net) and Step 2's dispute inside the 30-day window",
  "- **Dispute-expiry risk**: discrepancies raised late miss the marketplace dispute window and are written off; mitigated by the monthly reconciliation cadence (Step 1) keeping every dispute inside the window",
 ],
 ("PA-65.3-marketplace-performance-settlement.md", "W2423"): [
  "- **Cost-to-serve opacity risk**: effective commission computed on the headline rate alone misses shipping subsidies, promotional co-op and return fees; mitigated by the total-cost-as-%-of-revenue computation across all fee classes (Step 1) benchmarked against own-ecommerce cost-to-serve",
  "- **Rate-drift blindness risk**: platform re-tiering between quarters passes unnoticed inside a blended average; mitigated by the monthly analysis cadence (Step 1) and the W2428 QBR negotiating commission rates from this evidence",
 ],
 ("PA-65.3-marketplace-performance-settlement.md", "W2424"): [
  "- **Allocation-distortion risk**: shared marketing and fulfillment costs allocated unevenly flatter one channel's contribution; mitigated by the like-for-like cost lines across channels (Step 1: revenue, COGS, commissions, shipping, marketing, returns) with CFO accountability",
  "- **Snapshot-reaction risk**: one month's contribution swing triggering channel investment swings; mitigated by the monthly trend view (Step 1) and the W2429 annual review as the expand/maintain/sunset decision point",
 ],
 ("PA-65.3-marketplace-performance-settlement.md", "W2425"): [
  "- **Metric-normalization risk**: a dashboard consumed as daily routine stops flagging anomalies once they normalize into the numbers; mitigated by the daily anomaly review plus the monthly deep analysis with optimization recommendations (Step 1)",
  "- **Definition-drift risk**: AOV or conversion computed differently from the W2413 baseline makes trends unreadable; mitigated by the dashboard carrying the baseline's own metric set (orders, AOV, conversion, ratings, return rate, stock-out rate)",
 ],
 ("PA-65.3-marketplace-performance-settlement.md", "W2426"): [
  "- **Survivorship bias risk**: comparing only surviving marketplace SKUs against own-site averages overstates marketplace performance; mitigated by the by-product/by-category comparison (Step 1) including delisted items' history",
  "- **Attribution-gap risk**: marketplace-acquired customers credited fully to the channel ignore their later own-site migration; mitigated by the W2427 acquisition analysis carrying the migration and lifetime-value view alongside this comparison",
 ],
 ("PA-65.3-marketplace-performance-settlement.md", "W2427"): [
  "- **First-order-horizon risk**: acquisition judged on first-order contribution kills channels whose value is the loyalty conversion; mitigated by the analysis explicitly carrying loyalty conversion, repeat purchase and lifetime value (Step 1)",
  "- **Migration-measurement risk**: marketplace-to-own-site migration left untracked reads as channel leakage rather than funnel success; mitigated by the repeat-purchase vs. migration comparison (Step 1) feeding W2426's channel recommendations",
 ],
 ("PA-65.3-marketplace-performance-settlement.md", "W2428"): [
  "- **QBR-theater risk**: quarterly reviews held without the cost analysis behind them become relationship visits that concede rate increases; mitigated by the QBR armed with W2423's fee analysis and the W2424 channel P&L (Step 1)",
  "- **Concession-creep risk**: featured-placement and growth commitments accepted across QBRs accumulate unfunded obligations; mitigated by GM, Digital Commerce Inc. ownership with VP Marketing accountability under the W2406 agreement terms",
 ],
 ("PA-65.3-marketplace-performance-settlement.md", "W2429"): [
  "- **Sunk-channel risk**: a legacy marketplace kept for relationship reasons consumes operating cost while contribution decays; mitigated by the expand/maintain/sunset discipline (Step 1) presented to the Executive Committee on channel-contribution data",
  "- **Exit-friction risk**: sunsetting a channel without wind-down sequencing strands listings, inventory and customer expectations; mitigated by the review's recommendation routed through W2428's platform relationship management for orderly exit",
 ],
}



REPLACEMENTS = {("VS-65-*", fs, wid): bullets for (fs, wid), bullets in REPLACEMENTS.items()}

if __name__ == "__main__":
    _engine.apply(REPLACEMENTS, _engine.build_pool())
