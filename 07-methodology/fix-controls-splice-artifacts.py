#!/usr/bin/env python3
"""fix-controls-splice-artifacts.py — forty-ninth-wave repair, mechanical classes.

Repairs the two mechanically-detectable classes of Controls `operational:`-bullet
corruption minted by the semantic-batch Controls enrichment:

  Class A (duplicated item): the semicolon item list repeats an item with its
  leading modifier(s) dropped ("mandatory X; operational: X") — the later,
  shorter copy is dropped, keeping the fuller first form.

  Class D (dangling tail): the item list ends with an empty final item
  ("...; .") — the dangling "; ." is dropped to the terminal period.

Every repair is an exact-match assertion: the script fails loudly if any target
line is not exactly as recorded, so re-runs and partial states are safe.

The splice/fragment classes (pain-point substrings minted as control items,
mid-clause truncations) are context-grounded and repaired by hand in the same
wave; they are guarded — not repaired — here (see validate-repo.sh Check 21).
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (file, 1-based line number, exact old line, exact new line)
REPAIRS = [
    # --- Class A: duplicated item (later copy drops the leading modifier) ---
    ("01-model-company/workflows/VS-01-merchandise-strategy/PA-01.3-product-information-and-content.md", 401,
     "- operational: public notification channels (in-store, social media, press); operational: empowering POS System Administrator to execute emergency blocks without IT manager approval for safety recalls; operational: Administrator to execute emergency blocks without IT manager approval for safety recalls",
     "- operational: public notification channels (in-store, social media, press); operational: empowering POS System Administrator to execute emergency blocks without IT manager approval for safety recalls"),
    ("01-model-company/workflows/VS-03-vendor-management/PA-03.4-vendor-portal-and-collaboration.md", 210,
     "- operational: mobile-responsive portal design, Filipino-language support, in-person training at DCs, and phased feature rollout (start with PO acknowledgment, then invoices, then advanced features); operational: portal invoice template with mandatory field validation, inline error messages, and vendor training; operational: field validation, inline error messages, and vendor training",
     "- operational: mobile-responsive portal design, Filipino-language support, in-person training at DCs, and phased feature rollout (start with PO acknowledgment, then invoices, then advanced features); operational: portal invoice template with mandatory field validation, inline error messages, and vendor training"),
    ("01-model-company/workflows/VS-05-inventory-lifecycle/PA-05.1-inventory-accuracy-and-counting.md", 466,
     "- operational: mandatory investigation documentation for variances >PHP 5K and quarterly unknown-rate target (<15%); operational: investigation documentation for variances >PHP 5K and quarterly unknown-rate target (<15%); operational: tiered approach (A-items prioritized, C-items batch-processed monthly)",
     "- operational: mandatory investigation documentation for variances >PHP 5K and quarterly unknown-rate target (<15%); operational: tiered approach (A-items prioritized, C-items batch-processed monthly)"),
    ("01-model-company/workflows/VS-06-logistics-fleet/PA-06.3-last-mile-and-delivery-partners.md", 295,
     "- operational: re-confirming access 24 hours before delivery; operational: mandatory PPE, site safety briefing from foreman, and company insurance coverage for delivery personnel; operational: PPE, site safety briefing from foreman, and company insurance coverage for delivery personnel",
     "- operational: re-confirming access 24 hours before delivery; operational: mandatory PPE, site safety briefing from foreman, and company insurance coverage for delivery personnel"),
    ("01-model-company/workflows/VS-07-store-operations/PA-07.1-store-daily-management.md", 1793,
     "- operational: strict categorization (only genuinely urgent items marked Urgent), mandatory reading confirmation checkbox, and HQ communication guidelines limiting daily volume; operational: reading confirmation checkbox, and HQ communication guidelines limiting daily volume; operational: periodic spot-checks by Regional Manager and supervisor cascade documentation requirement for policy and task-type communications",
     "- operational: strict categorization (only genuinely urgent items marked Urgent), mandatory reading confirmation checkbox, and HQ communication guidelines limiting daily volume; operational: periodic spot-checks by Regional Manager and supervisor cascade documentation requirement for policy and task-type communications"),
    ("01-model-company/workflows/VS-07-store-operations/PA-07.4-store-staffing-and-people.md", 303,
     "- operational: system-enforced workflow with mandatory NTE issuance before NOD; operational: NTE issuance before NOD; operational: policy matrix with offense severity classification and HR Coordinator review in Steps 5 and 7",
     "- operational: system-enforced workflow with mandatory NTE issuance before NOD; operational: policy matrix with offense severity classification and HR Coordinator review in Steps 5 and 7"),
    ("01-model-company/workflows/VS-07-store-operations/PA-07.4-store-staffing-and-people.md", 361,
     "- operational: mandatory Buddy training module and Store Manager selection oversight; operational: Buddy training module and Store Manager selection oversight; operational: assigning backup Buddy and cross-training multiple eligible buddies per department",
     "- operational: mandatory Buddy training module and Store Manager selection oversight; operational: assigning backup Buddy and cross-training multiple eligible buddies per department"),
    ("01-model-company/workflows/VS-08-pos-checkout/PA-08.2-payment-and-cash-management.md", 130,
     "- operational: automatic retry and terminal memory buffer; operational: retry and terminal memory buffer; operational: next-day settlement file matching per W99",
     "- operational: automatic retry and terminal memory buffer; operational: next-day settlement file matching per W99"),
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md", 427,
     "- operational: mandatory safety briefing, safety equipment provision, and customer trial waiver; operational: safety briefing, safety equipment provision, and customer trial waiver; operational: scheduled preventive maintenance and quarterly demo unit replacement program",
     "- operational: mandatory safety briefing, safety equipment provision, and customer trial waiver; operational: scheduled preventive maintenance and quarterly demo unit replacement program"),
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.2-project-estimation-and-advisory.md", 4721,
     "- operational: mandatory engineering referral for projects exceeding advisory scope; operational: engineering referral for projects exceeding advisory scope",
     "- operational: mandatory engineering referral for projects exceeding advisory scope"),
    ("01-model-company/workflows/VS-11-trade-project-wholesale/PA-11.2-project-sales-and-b2b.md", 468,
     "- operational: mandatory CO logging before any delivery change; operational: CO logging before any delivery change",
     "- operational: mandatory CO logging before any delivery change"),
    ("01-model-company/workflows/VS-110-freight-procurement-carrier-management-and-freight-audit/PA-110.1-freight-sourcing-carrier-contracting-and-rate-management.md", 164,
     "- operational: system enforcement and exception approval; operational: enforcement and exception approval; operational: maintenance discipline",
     "- operational: system enforcement and exception approval; operational: maintenance discipline"),
    ("01-model-company/workflows/VS-112-corporate-project-and-program-management-office/PA-112.3-project-benefits-realization-pmis-and-pmo-analytics.md", 88,
     "- operational: training, integration, and mandate; operational: integration",
     "- operational: training, integration, and mandate"),
    ("01-model-company/workflows/VS-114-dangerous-goods-hazmat-transport-ecommerce-regulatory-compliance/PA-114.1-dg-classification-inventory-and-program-governance.md", 89,
     "- operational: expert classification and validation; operational: mandatory DG attributes at SKU setup; operational: DG attributes at SKU setup",
     "- operational: expert classification and validation; operational: mandatory DG attributes at SKU setup"),
    ("01-model-company/workflows/VS-118-revenue-assurance-pricing-integrity-and-leakage-management/PA-118.1-revenue-assurance-strategy-governance-and-leak-detection-framework.md", 278,
     "- operational: system gating and audit; operational: gating and audit; operational: annual review",
     "- operational: system gating and audit; operational: annual review"),
    ("01-model-company/workflows/VS-12-installation-services/PA-12.1-installation-and-repair-services.md", 510,
     "- operational: conditional accreditation pathway (step 2c) for experienced but uncertified applicants, combined with mandatory BuildRight training (step 6) and supervised trial period (step 8); operational: BuildRight training (step 6) and supervised trial period (step 8); operational: establishing 3–4 regional assessment hubs (Metro Manila, Cebu, Davao, and one Northern Luzon location), conducting quarterly assessment batches rather than individual assessments, and using senior accredited contractors as regional assessors",
     "- operational: conditional accreditation pathway (step 2c) for experienced but uncertified applicants, combined with mandatory BuildRight training (step 6) and supervised trial period (step 8); operational: establishing 3–4 regional assessment hubs (Metro Manila, Cebu, Davao, and one Northern Luzon location), conducting quarterly assessment batches rather than individual assessments, and using senior accredited contractors as regional assessors"),
    ("01-model-company/workflows/VS-128-ai-ml-governance-responsible-ai/PA-128.2-responsible-ai-fairness-explainability-privacy-safety.md", 203,
     "- operational: mandatory human-review for tier-1; operational: human-review for tier-1; operational: override-rate tracking and SLA",
     "- operational: mandatory human-review for tier-1; operational: override-rate tracking and SLA"),
    ("01-model-company/workflows/VS-13-customer-experience/PA-13.1-customer-support-and-complaints.md", 750,
     "- operational: structured complaint intake with mandatory categorization; operational: categorization; operational: management review and accountability in QBR (W231)",
     "- operational: structured complaint intake with mandatory categorization; operational: management review and accountability in QBR (W231)"),
    ("01-model-company/workflows/VS-15-procure-to-pay/PA-15.1-invoice-processing-and-matching.md", 1171,
     "- operational: 7-day clearing SLA with daily aging report and Store Manager escalation for GIT > 14 days; operational: automated reconciliation system that matches WMS quantities to ERP balances daily, flagging exceptions for manual review; operational: that matches WMS quantities to ERP balances daily, flagging exceptions for manual review",
     "- operational: 7-day clearing SLA with daily aging report and Store Manager escalation for GIT > 14 days; operational: automated reconciliation system that matches WMS quantities to ERP balances daily, flagging exceptions for manual review"),
    ("01-model-company/workflows/VS-17-record-to-report/PA-17.2-consolidation-and-intercompany.md", 283,
     "- operational: annual TP documentation in Step 7; operational: quarterly review cadence and automatic escalation trigger if cost variance > 10%; operational: escalation trigger if cost variance > 10%",
     "- operational: annual TP documentation in Step 7; operational: quarterly review cadence and automatic escalation trigger if cost variance > 10%"),
    ("01-model-company/workflows/VS-19-hire-to-retire/PA-19.1-recruitment-and-onboarding.md", 971,
     "- operational: system attendance tracking and Regional Safety Coordinator quarterly review; operational: attendance tracking and Regional Safety Coordinator quarterly review; operational: automated reminders and Store Manager escalation",
     "- operational: system attendance tracking and Regional Safety Coordinator quarterly review; operational: automated reminders and Store Manager escalation"),
    ("01-model-company/workflows/VS-22-compliance-regulatory/PA-22.2-government-audit-and-inspection-response.md", 620,
     "- operational: ensuring payroll records are accurate and complete before inspection; operational: system deadline tracking and escalation; operational: deadline tracking and escalation",
     "- operational: ensuring payroll records are accurate and complete before inspection; operational: system deadline tracking and escalation"),
    ("01-model-company/workflows/VS-76-multi-region-lgu-compliance/PA-76.1-multi-lgu-business-permit-license-management.md", 274,
     "- operational: local-tax accrual reviewed by Tax Manager quarterly (per VS-79 / W90 indirect-tax); operational: Finance Controller sign-off on the annual store-P&L local-tax line; operational: Finance Controller sign-off on the annual store-P&L local-tax line",
     "- operational: local-tax accrual reviewed by Tax Manager quarterly (per VS-79 / W90 indirect-tax); operational: Finance Controller sign-off on the annual store-P&L local-tax line"),
    ("01-model-company/workflows/VS-85-mandatory-discount-eligibility-tax-credit/PA-85.1-scpwd-soloparent-eligibility-indiscount.md", 50,
     "- operational: mandatory ID capture in POS; operational: ID capture in POS",
     "- operational: mandatory ID capture in POS"),
    ("01-model-company/workflows/VS-86-anti-financial-crime-aml-abc/PA-86.1-kyc-cdd-pep-sanctions-screening.md", 122,
     "- operational: mandatory screening and senior approval; operational: screening and senior approval",
     "- operational: mandatory screening and senior approval"),
    ("01-model-company/workflows/VS-86-anti-financial-crime-aml-abc/PA-86.3-antibribery-gifts-conflict-of-interest.md", 87,
     "- operational: mandatory register and threshold rules; operational: register and threshold rules",
     "- operational: mandatory register and threshold rules"),
    ("01-model-company/workflows/VS-88-document-control-records-retention/PA-88.1-document-classification-versioning-taxonomy.md", 87,
     "- operational: mandatory fields and validation; operational: fields and validation",
     "- operational: mandatory fields and validation"),
    ("01-model-company/workflows/VS-89-product-recall-safety-corrective-action/PA-89.1-recall-initiation-risk-assessment-regulatory-notification.md", 51,
     "- operational: mandatory hazard-classification field and dedicated triage queue; operational: hazard-classification field and dedicated triage queue",
     "- operational: mandatory hazard-classification field and dedicated triage queue"),
    ("01-model-company/workflows/VS-90-damage-claims-freight-recovery/PA-90.1-damage-identification-documentation-disposition.md", 124,
     "- operational: mandatory damage-case logging; operational: damage-case logging",
     "- operational: mandatory damage-case logging"),
    ("01-model-company/workflows/VS-90-damage-claims-freight-recovery/PA-90.3-customer-damage-claims-recovery-analytics.md", 235,
     "- operational: mandatory liability-flag at resolution; operational: liability-flag at resolution",
     "- operational: mandatory liability-flag at resolution"),
    ("01-model-company/workflows/VS-91-consumer-data-privacy-protection/PA-91.1-privacy-governance-consent-data-subject-rights.md", 159,
     "- operational: case tracking and cross-system retrieval runbooks; operational: retrieval runbooks",
     "- operational: case tracking and cross-system retrieval runbooks"),
    ("01-model-company/workflows/VS-94-cooperative-community-enterprise-procurement/PA-94.2-cooperative-po-logistics-settlement.md", 233,
     "- operational: mandatory direct-to-bank and expedited terms; operational: direct-to-bank and expedited terms",
     "- operational: mandatory direct-to-bank and expedited terms"),
    ("01-model-company/workflows/VS-95-marketplace-operator-third-party-seller/PA-95.1-marketplace-platform-strategy-seller-onboarding.md", 159,
     "- operational: mandatory attributes and quality score; operational: attributes and quality score",
     "- operational: mandatory attributes and quality score"),
    ("01-model-company/workflows/VS-96-equipment-leasing-capital-equipment-finance/PA-96.1-lease-product-design-underwriting-origination.md", 302,
     "- operational: mandatory perfection checklist; operational: perfection checklist",
     "- operational: mandatory perfection checklist"),
    ("01-model-company/workflows/VS-96-equipment-leasing-capital-equipment-finance/PA-96.2-lease-booking-billing-asset-lifecycle.md", 198,
     "- operational: mandatory insurance verification (W3168) and annual check (W3171); operational: insurance verification (W3168) and annual check (W3171)",
     "- operational: mandatory insurance verification (W3168) and annual check (W3171)"),
    ("01-model-company/workflows/VS-98-contingent-contract-outsourced-workforce/PA-98.2-contingent-worker-onboarding-access-time-operations.md", 278,
     "- operational: mandatory screening and re-screening; operational: screening and re-screening; operational: documented process and legal review",
     "- operational: mandatory screening and re-screening; operational: documented process and legal review"),
    # --- Class D: dangling "; ." tail ---
    ("01-model-company/workflows/VS-186-compact-and-heavy-construction-equipment-rental-fleet-operations/PA-186.3-equipment-maintenance-safety-compliance-and-analytics.md", 246,
     "- operational: performance vs. business-case hurdle; utilization-data accuracy; .",
     "- operational: performance vs. business-case hurdle; utilization-data accuracy."),
    ("01-model-company/workflows/VS-187-household-hazardous-waste-paint-and-product-stewardship-take-back/PA-187.1-stewardship-program-strategy-regulatory-setup-and-partner-network.md", 50,
     "- operational: regulatory compliance scope; program budget adherence; .",
     "- operational: regulatory compliance scope; program budget adherence."),
    ("01-model-company/workflows/VS-187-household-hazardous-waste-paint-and-product-stewardship-take-back/PA-187.1-stewardship-program-strategy-regulatory-setup-and-partner-network.md", 285,
     "- operational: hazardous-waste manifest/DENR compliance; manifest quantity accuracy; .",
     "- operational: hazardous-waste manifest/DENR compliance; manifest quantity accuracy."),
    ("01-model-company/workflows/VS-187-household-hazardous-waste-paint-and-product-stewardship-take-back/PA-187.3-recovery-disposal-compliance-reporting-and-analytics.md", 169,
     "- operational: statutory environmental reporting; reporting accuracy/reconciliation; .",
     "- operational: statutory environmental reporting; reporting accuracy/reconciliation."),
    ("01-model-company/workflows/VS-187-household-hazardous-waste-paint-and-product-stewardship-take-back/PA-187.3-recovery-disposal-compliance-reporting-and-analytics.md", 328,
     "- operational: ESG-claim substantiation; metric-data accuracy; .",
     "- operational: ESG-claim substantiation; metric-data accuracy."),
    ("01-model-company/workflows/VS-188-trade-reseller-floor-plan-and-dealer-inventory-financing/PA-188.1-floor-plan-program-strategy-credit-framework-and-onboarding.md", 250,
     "- operational: account/feed accuracy; dealer data safeguards; .",
     "- operational: account/feed accuracy; dealer data safeguards."),
    ("01-model-company/workflows/VS-188-trade-reseller-floor-plan-and-dealer-inventory-financing/PA-188.3-curtailment-collections-risk-and-portfolio-analytics.md", 167,
     "- operational: grading accuracy; limit-approval authority; concentration-limit adherence; .",
     "- operational: grading accuracy; limit-approval authority; concentration-limit adherence."),
    ("01-model-company/workflows/VS-188-trade-reseller-floor-plan-and-dealer-inventory-financing/PA-188.3-curtailment-collections-risk-and-portfolio-analytics.md", 246,
     "- operational: performance-data accuracy; program-growth tracking; .",
     "- operational: performance-data accuracy; program-growth tracking."),
    ("01-model-company/workflows/VS-188-trade-reseller-floor-plan-and-dealer-inventory-financing/PA-188.3-curtailment-collections-risk-and-portfolio-analytics.md", 286,
     "- operational: profitability-data accuracy; vs. business case; treasury reconciliation; .",
     "- operational: profitability-data accuracy; vs. business case; treasury reconciliation."),
    ("01-model-company/workflows/VS-188-trade-reseller-floor-plan-and-dealer-inventory-financing/PA-188.3-curtailment-collections-risk-and-portfolio-analytics.md", 326,
     "- operational: statutory reporting; regulatory compliance; internal-audit independence (VS-21); accuracy; .",
     "- operational: statutory reporting; regulatory compliance; internal-audit independence (VS-21); accuracy."),
    ("01-model-company/workflows/VS-189-trade-receivables-factoring-invoice-discounting-and-securitization/PA-189.1-receivables-financing-strategy-funder-relationships-and-setup.md", 128,
     "- operational: eligibility accuracy; fraud detection on fabricated invoices; concentration-limit adherence; .",
     "- operational: eligibility accuracy; fraud detection on fabricated invoices; concentration-limit adherence."),
    ("01-model-company/workflows/VS-189-trade-receivables-factoring-invoice-discounting-and-securitization/PA-189.1-receivables-financing-strategy-funder-relationships-and-setup.md", 285,
     "- operational: dilution accuracy; adequate reserve; coverage; .",
     "- operational: dilution accuracy; adequate reserve; coverage."),
    ("01-model-company/workflows/VS-189-trade-receivables-factoring-invoice-discounting-and-securitization/PA-189.3-collections-recourse-reconciliation-and-portfolio-analytics.md", 288,
     "- operational: statutory compliance; regulatory; internal-audit independence (VS-21); accuracy; consolidated reporting; .",
     "- operational: statutory compliance; regulatory; internal-audit independence (VS-21); accuracy; consolidated reporting."),
    # --- Class D variant: the CTL-802 gloss spliced mid-bullet, then the dangling tail
    # (the gloss duplicates the CTL-802 line above it; the operational items are the
    #  three noun phrases with the spliced gloss removed) ---
    ("01-model-company/workflows/VS-190-operational-technology-ot-ics-cybersecurity-and-retail-technology-asset-protection/PA-190.3-ot-compliance-third-party-access-and-cyber-resilience-analytics.md", 290,
     "- operational: cross-channel segregation consistency; ensure controlled execution — OT Compliance, Third-Party Access & Cyber Resilience Analytics (PA-190.3; .) — coordination governance; channel posture evidence; .",
     "- operational: cross-channel segregation consistency; coordination governance; channel posture evidence."),
]


def main() -> int:
    by_file = {}
    for path, ln, old, new in REPAIRS:
        by_file.setdefault(path, []).append((ln, old, new))
    applied = 0
    for path, reps in sorted(by_file.items()):
        p = ROOT / path
        lines = p.read_text(encoding="utf-8").split("\n")
        for ln, old, new in reps:
            if lines[ln - 1] != old:
                print(f"MISMATCH {path}:{ln}\n  expected: {old!r}\n  found:    {lines[ln - 1]!r}")
                return 1
            lines[ln - 1] = new
            applied += 1
        p.write_text("\n".join(lines), encoding="utf-8")
    print(f"applied {applied} exact-match repairs across {len(by_file)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
