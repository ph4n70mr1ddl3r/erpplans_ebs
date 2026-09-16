#!/usr/bin/env python3
"""fix-controls-splice-artifacts-2-context.py — forty-ninth-wave repair, context class.

Repairs the context-grounded class of Controls `operational:`-bullet corruption
minted by the semantic-batch Controls enrichment: pain-point risk clauses and
mitigation-clause substrings minted as control items, and clauses truncated at
"vs." (the mint pass split item lists on sentence periods, so "vs. offered"
became the end of an item). Every replacement is grounded in the owning
workflow's own Pain Points / Steps, quoted from its own text.

Every repair is an exact-match assertion; the script fails loudly on drift.
(Class A duplicated-item and Class D dangling-tail repairs are in
fix-controls-splice-artifacts.py.)
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (file, 1-based line number, exact old line, exact new line)
REPAIRS = [
    # PA-03.1 W? early-payment discounting — split at "vs."; completed from the
    # workflow's own pain clause ("system must track actual discount realized vs. offered")
    ("01-model-company/workflows/VS-03-vendor-management/PA-03.1-vendor-sourcing-and-onboarding.md", 2519,
     "- operational: must track actual discount realized vs",
     "- operational: must track actual discount realized vs. offered"),
    # PA-03.2 W? SKU discontinuation — risk clause ("...ecosystem are stranded") minted as
    # the control; the pain point's own mitigation is the buy-back/trade-in program per W916
    ("01-model-company/workflows/VS-03-vendor-management/PA-03.2-purchase-order-cycle.md", 613,
     "- operational: are stranded",
     "- operational: vendor buy-back or trade-in program for orphaned accessories per W916"),
    # PA-04.3 W? shift handover — pain tail ("but not fully eliminated") minted into the
    # control, then duplicated; the control is the acknowledgment itself
    ("01-model-company/workflows/VS-04-dc-warehouse/PA-04.3-dc-operations-management.md", 201,
     "- operational: mandatory handover log acknowledgment but not fully eliminated; operational: handover log acknowledgment but not fully eliminated",
     "- operational: mandatory handover log acknowledgment"),
    # PA-07.1 W? recall execution — risk clause minted as the control; the workflow's own
    # traceability/blocking touchpoints are the control
    ("01-model-company/workflows/VS-07-store-operations/PA-07.1-store-daily-management.md", 731,
     "- operational: cannot identify which specific customers purchased affected items, limiting targeted notification",
     "- operational: lot/batch traceability with POS blocking (W29.3/W29.5) so targeted customer notification stays possible"),
    # PA-07.1 W? sample loan — mitigation-clause head dropped ("deposit system mitigates...")
    ("01-model-company/workflows/VS-07-store-operations/PA-07.1-store-daily-management.md", 2836,
     "- operational: mitigates financial loss; operational: must track deposits as a liability per W25",
     "- operational: refundable deposit system mitigates financial loss (repeat non-returners flagged); operational: must track deposits as a liability per W25"),
    # PA-07.3 W? customer pickup — split at "vs."; completed from the workflow's own pain clause
    ("01-model-company/workflows/VS-07-store-operations/PA-07.3-store-receiving-and-replenishment.md", 1660,
     "- operational: time slot management in Step 1 and separate pickup vs; operational: Stock Associate training on safe loading limits and willingness to refuse unsafe loads; operational: load securing assistance in Step 5 and electronic goods release form documenting customer's acceptance of responsibility in Step 6",
     "- operational: time slot management in Step 1 and separate pickup vs. delivery bay designation where space permits; operational: Stock Associate training on safe loading limits and willingness to refuse unsafe loads; operational: load securing assistance in Step 5 and electronic goods release form documenting customer's acceptance of responsibility in Step 6"),
    # PA-07.4 W? labor cost flash — split at "vs."; completed from the workflow's own pain clause
    ("01-model-company/workflows/VS-07-store-operations/PA-07.4-store-staffing-and-people.md", 245,
     "- operational: tracking absolute hours vs; operational: automated holiday calendar in payroll module per HR-011; operational: system requirement for same-day overtime entry in W601",
     "- operational: tracking absolute hours vs. budget in addition to percentage; operational: automated holiday calendar in payroll module per HR-011; operational: system requirement for same-day overtime entry in W601"),
    # PA-09.1 W274 third-party financing — two PAIN clauses minted as controls; the
    # workflow's own validation/reconciliation steps are the controls
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md", 260,
     "- operational: causing reconciliation failures; operational: outages halting the entire checkout flow for financed purchases",
     "- operational: POS reference-code validation at tender capture (Step 3); operational: T+3 batch reconciliation against partner remittance with suspense-account follow-up (Step 5, W261)"),
    # PA-09.1 W955 hiring facilitation — three mitigation-clause substrings minted as items;
    # re-grounded on the workflow's own governance steps
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md", 1502,
     "- operational: to purchase from BuildRight; operational: provides community self-regulation; operational: flags suspicious profiles",
     "- operational: facilitation-only terms with legal review per Step 5c (no co-employment); operational: government-ID verification at registration (Step 1b); operational: feedback-driven directory governance with Store Manager review (Steps 4d/5a)"),
    # PA-09.1 W? rebar fabrication — mitigation tails with the verb/prefix spliced off
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md", 1902,
     "- operational: PPE enforcement, equipment guard maintenance, and incident reporting per W140 mitigate; operational: must optimize cutting sequence to minimize waste (nesting algorithm); operational: with SMS notification when order is ready improves customer experience",
     "- operational: PPE enforcement, equipment guard maintenance, and incident reporting per W140; operational: must optimize cutting sequence to minimize waste (nesting algorithm); operational: queue management with SMS notification when the order is ready"),
    # PA-09.1 W1045 PVC cutting — mitigation heads dropped
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md", 2493,
     "- operational: for high-volume stores; operational: per W172",
     "- operational: weekly blade replacement schedule for high-volume stores; operational: PPE (gloves, safety glasses) required per W172"),
    # PA-09.1 W1054 wire spool — purpose infinitive minted; the reconciliation is the control
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md", 2616,
     "- operational: to maintain inventory accuracy per INV-001",
     "- operational: weekly spool reconciliation (physical remaining-length measurement) per INV-001"),
    # PA-09.1 W1114 stock lookup — risk clause minted; the workflow's own ATP deduction
    # and the accuracy target are the controls
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md", 3395,
     "- operational: stock (accuracy target ≥ 97%), customers will have a poor experience; operational: must prevent this through POS-level ATP deduction",
     "- operational: POS-level ATP deduction prevents sale of reserved stock to walk-in customers; operational: inventory record accuracy target ≥ 97%"),
    # PA-09.1 W1131 photo portal — tail fragment completed from the pain clause
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md", 3590,
     "- operational: should accept all uploads and let marketing team curate; operational: before marketing use",
     "- operational: system accepts all uploads and the marketing team curates; operational: consent and privacy review required before marketing use"),
    # PA-09.1 W1146 cement freshness — mitigation head dropped
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md", 3913,
     "- operational: for stock associates",
     "- operational: ergonomic training required for stock associates"),
    # PA-09.2 W? GI sheets — mitigation head dropped
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.2-project-estimation-and-advisory.md", 862,
     "- operational: must prioritize same-batch allocation; operational: for roofing orders",
     "- operational: must prioritize same-batch allocation; operational: vehicle loading assistance per W950 mandatory for roofing orders"),
    # PA-09.2 W? water systems — mitigation heads dropped / clause tail spliced
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.2-project-estimation-and-advisory.md", 927,
     "- operational: for tanks above 500L; operational: recommendation, and installation referral — not lowest price on individual items",
     "- operational: delivery scheduling per W5D mandatory for tanks above 500L; operational: professional sizing with complete system recommendation and installation referral — not lowest price on individual items"),
    # PA-09.2 W? plumbing takeoff — mitigation head dropped
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.2-project-estimation-and-advisory.md", 1126,
     "- operational: for building permit applications per LGU requirements per W54",
     "- operational: licensed plumber sign-off required for building permit applications per LGU requirements per W54"),
    # PA-09.2 W? filtration — mitigation head dropped
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.2-project-estimation-and-advisory.md", 1996,
     "- operational: purchase for >PHP 5,000 systems; operational: should send proactive replacement reminders",
     "- operational: recommend DIY water test before system purchase for >PHP 5,000 systems; operational: proactive filter-replacement reminders"),
    # PA-09.2 W? permit guide — risk clause minted; the workflow's own annual review is the control
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.2-project-estimation-and-advisory.md", 2051,
     "- operational: cannot guarantee accuracy for every LGU",
     "- operational: annual permit-requirement database review and update per W657 (regulatory change management)"),
    # PA-09.2 W? seismic — mitigation head dropped
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.2-project-estimation-and-advisory.md", 2536,
     "- operational: engineer referral; operational: must accurately classify store location and customer's project location",
     "- operational: mandatory engineer referral with recommendations framed per NSCP standards; operational: must accurately classify store location and customer's project location"),
    # PA-09.2 W? smart home — mid-clause splice ("...required by most smart switches")
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.2-project-estimation-and-advisory.md", 2662,
     "- operational: must assess Wi-Fi infrastructure first; operational: by most smart switches; operational: should recommend brands with strong privacy policies and recommend regular firmware updates",
     "- operational: must assess Wi-Fi infrastructure first; operational: must ask about neutral wires and recommend no-neutral-wire alternatives or professional rewiring where absent; operational: should recommend brands with strong privacy policies and recommend regular firmware updates"),
    # PA-09.2 W? home office — mitigation head dropped
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.2-project-estimation-and-advisory.md", 2846,
     "- operational: for specific ergonomic needs or medical conditions",
     "- operational: disclaimer required for specific ergonomic needs or medical conditions"),
    # PA-09.2 W? rainwater — mitigation head dropped
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.2-project-estimation-and-advisory.md", 3040,
     "- operational: for potable water, water quality depends on maintenance; operational: must specify tight-fitting tank covers and gutter maintenance per DOH advisory; operational: must manage customer expectations about seasonal variability",
     "- operational: potable-water disclaimer — customer responsible for regular testing; operational: must specify tight-fitting tank covers and gutter maintenance per DOH advisory; operational: must manage customer expectations about seasonal variability"),
    # PA-09.2 W? CCTV — risk clause minted; the workflow's own UPS rule is the control
    ("01-model-company/workflows/VS-09-in-store-services/PA-09.2-project-estimation-and-advisory.md", 3407,
     "- operational: is offline during outages — precisely when break-ins may occur; operational: must enforce surveillance-HDD-only recommendation",
     "- operational: UPS recommended in every system design so coverage survives outages; operational: must enforce surveillance-HDD-only recommendation"),
    # PA-10.1 W? feature flags — pain tail minted; the required cleanup is the control
    ("01-model-company/workflows/VS-10-ecommerce-digital/PA-10.1-ecommerce-platform-operations.md", 959,
     "- operational: but often deprioritized",
     "- operational: periodic feature-flag cleanup"),
    # PA-13.2 W? deceased-claim — mitigation head dropped
    ("01-model-company/workflows/VS-13-customer-experience/PA-13.2-loyalty-program-operations.md", 407,
     "- operational: for each case",
     "- operational: legal review required for each case"),
    # PA-13.2 W? partner program — mitigation head dropped (agreement review is Step 2, W62)
    ("01-model-company/workflows/VS-13-customer-experience/PA-13.2-loyalty-program-operations.md", 885,
     "- operational: for each partnership",
     "- operational: partnership agreement and integration review per W62 before build"),
    # PA-15.1 W? GRNI — mitigation head dropped
    ("01-model-company/workflows/VS-15-procure-to-pay/PA-15.1-invoice-processing-and-matching.md", 94,
     "- operational: for permanent accrual",
     "- operational: Controller intervention for GRNI items aged 90+ days with permanent accrual"),
    # PA-15.1 W? debit memo — mitigation tail spliced ("...CLM system is preventive")
    ("01-model-company/workflows/VS-15-procure-to-pay/PA-15.1-invoice-processing-and-matching.md", 1038,
     "- operational: must enforce one-to-one matching; operational: is preventive",
     "- operational: must enforce one-to-one matching; operational: clear contract language per W688 CLM (preventive)"),
    # PA-15.2 W? emergency cash — risk clause + verb fragment minted; the approval gate and
    # the seasonal adjustment are the controls
    ("01-model-company/workflows/VS-15-procure-to-pay/PA-15.2-vendor-payment-and-reconciliation.md", 1054,
     "- operational: for urgent requests may delay critical replenishment during peak hours; operational: should auto-adjust",
     "- operational: Finance Manager approval for urgent requests; operational: seasonal float auto-adjustment for Ber months and payday weekends"),
    # PA-16.1 W? demand letters — mitigation head dropped
    ("01-model-company/workflows/VS-16-order-to-cash/PA-16.1-credit-application-and-scoring.md", 145,
     "- operational: for BIR-compliant bad debt write-off (W81)",
     "- operational: registered-mail demand-letter documentation (Steps 4–5) required for BIR-compliant bad debt write-off (W81)"),
    # PA-16.1 W? credit hold — risk clause minted; the workflow's own Step 2 review is the control
    ("01-model-company/workflows/VS-16-order-to-cash/PA-16.1-credit-application-and-scoring.md", 575,
     "- operational: may block for disputed amount incorrectly",
     "- operational: Credit Analyst review and validation of holds with disputed-invoice exclusion before release (Step 2)"),
    # PA-17.4 W? margin — risk tail minted; the manual normalization is the control
    ("01-model-company/workflows/VS-17-record-to-report/PA-17.4-fpanda-and-reporting.md", 525,
     "- operational: may not handle automatically",
     "- operational: manual landed-cost normalization for import vs. domestic margin comparison"),
    # PA-18.2 W? bank signatories — sentence spliced at "system |and"; the control is the
    # separation alert + revocation the pain point demands
    ("01-model-company/workflows/VS-18-treasury-cash/PA-18.2-banking-and-payments.md", 126,
     "- operational: and bank portal access, creating a fraud and unauthorized transaction risk",
     "- operational: prompt HR-to-Treasury separation alerting with signatory and system-access revocation"),
    # PA-19.3 W? intercompany — purpose infinitive minted; the transfer gate is the control
    ("01-model-company/workflows/VS-19-hire-to-retire/PA-19.3-workforce-management.md", 468,
     "- operational: to maintain employee morale",
     "- operational: formal transfer handling per Step 4 to maintain employee morale"),
    # PA-19.4 W? APE/drug testing — mitigation heads dropped
    ("01-model-company/workflows/VS-19-hire-to-retire/PA-19.4-learning-and-development.md", 357,
     "- operational: for DOLE compliance per W436; operational: before action per W483",
     "- operational: 100% APE completion required for DOLE compliance per W436; operational: confirmatory testing (GC-MS) required before action per W483"),
    # PA-21.2 W? whistleblower — risk clause minted; the intake protections are the control
    ("01-model-company/workflows/VS-21-internal-audit-risk/PA-21.2-enterprise-risk-management.md", 181,
     "- operational: is perceived as insecure, the detected fraud rate will drop",
     "- operational: anonymous intake with authorized-access controls to preserve reporting confidence"),
    # PA-23.3 W? EAS tagging — risk clause minted; the custody protocol is the control
    ("01-model-company/workflows/VS-23-loss-prevention/PA-23.3-shrinkage-reduction.md", 523,
     "- operational: is compromised",
     "- operational: strict detacher-tool and key custody protocol"),
    # PA-24.1 W? OSH — mitigation head dropped
    ("01-model-company/workflows/VS-24-health-safety-environment/PA-24.1-occupational-health-and-safety.md", 73,
     "- operational: from Bureau of Fire Protection (BFP) per location",
     "- operational: current FSIC from Bureau of Fire Protection (BFP) per location, tracked to expiry"),
    # PA-24.2 W? fire safety — pain tail minted; the standardization clause is the control
    ("01-model-company/workflows/VS-24-health-safety-environment/PA-24.2-emergency-preparedness.md", 415,
     "- operational: by BFP for FSIC renewal",
     "- operational: internal inspection held to the highest BFP standard, with retrofit tracking where required for FSIC renewal"),
    # PA-24.3 W? hazmat regulatory — mitigation head dropped
    ("01-model-company/workflows/VS-24-health-safety-environment/PA-24.3-hazmat-management.md", 370,
     "- operational: to interpret applicability",
     "- operational: VP Legal guidance required to interpret applicability of new regulations"),
    # PA-25.1 W? solar — mid-word splice ("...25-year system life, reducing savings vs.");
    # the workflow's own monitoring/escalation is the control
    ("01-model-company/workflows/VS-25-esg-sustainability/PA-25.1-environmental-monitoring.md", 814,
     "- operational: life, reducing savings vs",
     "- operational: degradation-adjusted generation baseline with fault escalation when output drops > 20% below expected"),
    # PA-25.2 W? green building — mitigation head dropped
    ("01-model-company/workflows/VS-25-esg-sustainability/PA-25.2-social-impact-and-governance.md", 179,
     "- operational: to ensure compliance during construction",
     "- operational: additional contractor supervision to ensure green-building compliance during construction"),
    # PA-26.1 W? BCP exercises — split at "vs."; completed from the workflow's own pain clause
    ("01-model-company/workflows/VS-26-business-continuity-insurance/PA-26.1-bcp-planning-and-testing.md", 188,
     "- operational: BCP onboarding for new Store Managers (W16) and requiring BCP review as part of new SM orientation; operational: batch video conference sessions (10–15 stores at a time) and alternating detailed vs; operational: mandatory annual update in Step 2 and trigger-based updates (staff turnover, phone number changes)",
     "- operational: BCP onboarding for new Store Managers (W16) and requiring BCP review as part of new SM orientation; operational: batch video conference sessions (10–15 stores at a time) and alternating detailed vs. abbreviated exercises for low-risk locations; operational: mandatory annual update in Step 2 and trigger-based updates (staff turnover, phone number changes)"),
    # PA-26.2 W? DR failover — risk-clause fragments minted; the tier system and the legacy
    # reconnection procedure are the controls
    ("01-model-company/workflows/VS-26-business-continuity-insurance/PA-26.2-crisis-response-and-recovery.md", 128,
     "- operational: for affected transactions; operational: needed (POS > ecommerce > WMS > analytics)",
     "- operational: priority-tier DR peak-load allocation (POS > ecommerce > WMS > analytics); operational: manual POS reconnection runbook for affected transactions at legacy stores"),
    # PA-45.2 W? VMI — risk clause minted; the pain point's own parameter review is the control
    ("01-model-company/workflows/VS-45-consignment-vmi-operations/PA-45.2-vmi-operations.md", 134,
     "- operational: may auto-approve excessive replenishment",
     "- operational: periodic VMI parameter review with min/max and spending caps"),
    # PA-93.3 W? dark-store SLA — split at "vs."; completed from the workflow's own pain clause
    ("01-model-company/workflows/VS-93-dark-store-micro-fulfillment/PA-93.3-dark-store-inventory-capacity-analytics.md", 157,
     "- operational: segmenting internal vs",
     "- operational: segmenting internal vs. external SLA"),
    # PA-116.2 W? bid bonds — risk tail ("...required format is rejected") minted after the
    # two real controls; dropped
    ("01-model-company/workflows/VS-116-performance-bond-surety-and-bank-guarantee-management/PA-116.2-bond-application-issuance-tracking-and-encumbrance-management.md", 51,
     "- operational: lead-time and pre-arranged facility; operational: format review; operational: format is rejected",
     "- operational: lead-time and pre-arranged facility; operational: format review"),
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
