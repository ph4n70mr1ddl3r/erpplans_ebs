# ERP Plans — Model Company & System Architecture

## Purpose

This repository contains the operational specifications, active workflows, and system architecture for **BuildRight Depot Corp.** (the **"Model Company"**), operating with all its capabilities and systems fully enabled on a modern **hybrid IT landscape**: a unified ERP **core** — selected as **Oracle E-Business Suite 12.2** and realized in [`02-oracle-ebs/`](02-oracle-ebs/) under the two-tier doctrine (*if it's in EBS we use it; otherwise we build* — customize only where gaps are proven, buy nothing) — in-house built and already-built differentiating platforms (sourcing governed by [`07-methodology/capability-sourcing-and-engineering-model.md`](07-methodology/capability-sourcing-and-engineering-model.md)). Each subfolder contains the configuration, design, and architecture for running the model company on specific ERP platforms. The whole model is synthesized into the portable, AI-first operating playbook — the ERP-agnostic doctrine, agent factory, knowledge-base-as-persistent-memory, and no-confusion decision system — in [`07-methodology/ai-first-operating-guide.md`](07-methodology/ai-first-operating-guide.md).

## Out of Scope

The following are **not** covered in this repository and would be addressed during implementation:

- **Comparative ERP vendor evaluation** — the requirements stay platform-agnostic; the platform selection itself is recorded as a decision (Oracle EBS 12.2, see [`02-oracle-ebs/`](02-oracle-ebs/) and CHANGELOG), not re-argued here
- **Warehouse robotics or automation hardware** — conveyor systems, AS/RS, autonomous mobile robots
- **Blockchain or cryptocurrency** — not applicable to current retail operations
- **IoT sensor networks** — beyond temperature monitoring and GPS telematics already specified
- **Custom mobile app development details** — strategy defined; UX/UI design and code are out of scope
- **Organizational change management plan** — training strategy is referenced but not detailed
- **Implementation project plan** — phase prioritization (Tier 1/2/3) is defined; Gantt charts and resourcing are not
- **Hardware procurement and vendor selection** — reference specifications provided; purchasing is out of scope
- **Network infrastructure detailed design** — bandwidth targets specified; network architecture diagrams are not

See [CHANGELOG.md](CHANGELOG.md) for revision history.

## Folder Structure

```
erpplans/
├── README.md                    ← You are here
├── 01-model-company/            ← Complete model company profile, requirements & workflows
│   ├── model-company-profile.md       Company profile, operations, financials
│   ├── erp-requirements.md            728 requirements across 38 categories
│   ├── data-volumes-and-integrations.md  Transaction volumes, integration map (canonical integration diagram)
│   ├── workflows/                      5,427 workflows organized by value stream
│   │   ├── README.md                           Navigation hub & quick stats
│   │   ├── value-stream-index.md              Master index (8 families · 188 value streams · 569 process areas)
│   │   ├── WORKFLOW-FORMAT-GUIDE.md            Workflow format, RACI key & conventions
│   │   ├── workflow-criticality-classification.md  Tier 1/2/3 confirmed priorities (5,450 rows)
│   │   ├── workflow-criticality-proposed.md    Keyword-driven tier proposal register for unclassified workflows (currently empty — 0 unclassified; regenerates via classify-workflows.py)
│   │   ├── workflow-dependency-map.md           Prerequisite relationships, critical path
│   │   ├── workflow-system-touchpoint-map.md    ERP module-to-workflow cross-reference
│   │   ├── workflow-gap-analysis.md            Gap-analysis methodology & 30-pass history
│   │   ├── event-custody-and-precedence-register.md  Cross-cutting event routing: accountable VS, PAGASA signal ladder, incident command, enforced overlap pairs
│   │   ├── VS-01-merchandise-strategy/         46 workflows (3 process areas)
│   │   ├── VS-02-supply-planning/               38 workflows (3 process areas)
│   │   ├── VS-03-vendor-management/             82 workflows (4 process areas)
│   │   ├── VS-04-dc-warehouse/                  45 workflows (3 process areas)
│   │   ├── VS-05-inventory-lifecycle/           35 workflows (3 process areas)
│   │   ├── VS-06-logistics-fleet/               37 workflows (3 process areas)
│   │   ├── VS-07-store-operations/              151 workflows (4 process areas)
│   │   ├── VS-08-pos-checkout/                  61 workflows (3 process areas)
│   │   ├── VS-09-in-store-services/             158 workflows (3 process areas)
│   │   ├── VS-10-ecommerce-digital/             63 workflows (3 process areas)
│   │   ├── VS-11-trade-project-wholesale/       52 workflows (3 process areas)
│   │   ├── VS-12-installation-services/         40 workflows (3 process areas)
│   │   ├── VS-13-customer-experience/           64 workflows (3 process areas)
│   │   ├── VS-14-marketing/                     42 workflows (3 process areas)
│   │   ├── VS-15-procure-to-pay/                43 workflows (2 process areas)
│   │   ├── VS-16-order-to-cash/                 31 workflows (3 process areas)
│   │   ├── VS-17-record-to-report/              70 workflows (4 process areas)
│   │   ├── VS-18-treasury-cash/                 35 workflows (3 process areas)
│   │   ├── VS-19-hire-to-retire/                81 workflows (5 process areas)
│   │   ├── VS-20-real-estate-construction/      33 workflows (3 process areas)
│   │   ├── VS-21-internal-audit-risk/           49 workflows (3 process areas)
│   │   ├── VS-22-compliance-regulatory/         57 workflows (3 process areas)
│   │   ├── VS-23-loss-prevention/               29 workflows (3 process areas)
│   │   ├── VS-24-health-safety-environment/     31 workflows (3 process areas)
│   │   ├── VS-25-esg-sustainability/            31 workflows (3 process areas)
│   │   ├── VS-26-business-continuity-insurance/ 31 workflows (3 process areas)
│   │   ├── VS-27-it-operations-security/        71 workflows (3 process areas)
│   │   ├── VS-28-data-analytics-bi/             24 workflows (3 process areas)
│   │   ├── VS-29-master-data/                   43 workflows (3 process areas)
│   │   ├── VS-30-innovation-digital/            29 workflows (3 process areas)
│   │   ├── VS-31-quality-management/            23 workflows (3 process areas)
│   │   ├── VS-32-returns-reverse-logistics/     23 workflows (3 process areas)
│   │   ├── VS-33-strategic-planning/            23 workflows (3 process areas)
│   │   ├── VS-34-expense-procurement/           22 workflows (3 process areas)
│   │   ├── VS-35-fixed-asset-management/        24 workflows (3 process areas)
│   │   ├── VS-36-corporate-governance/          25 workflows (3 process areas)
│   │   ├── VS-37-store-opening-commissioning/   26 workflows (3 process areas)
│   │   ├── VS-38-consumer-credit-financing/     24 workflows (3 process areas)
│   │   ├── VS-39-vendor-rebate-incentive/       24 workflows (3 process areas)
│   │   ├── VS-40-capex-project-accounting/      24 workflows (3 process areas)
│   │   ├── VS-41-private-label-brand/           24 workflows (3 process areas)
│   │   ├── VS-42-property-lease-admin/          25 workflows (3 process areas)
│   │   ├── VS-43-trade-professional-program/    24 workflows (3 process areas)
│   │   ├── VS-44-consumer-insights-market-research/ 24 workflows (3 process areas)
│   │   ├── VS-45-consignment-vmi-operations/    24 workflows (3 process areas)
│   │   ├── VS-46-government-institutional-sales/ 24 workflows (3 process areas)
│   │   ├── VS-47-subscription-recurring-services/ 24 workflows (3 process areas)
│   │   ├── VS-48-retail-media-network/          24 workflows (3 process areas)
│   │   ├── VS-53-warranty-guarantee-management/ 24 workflows (3 process areas)
│   │   ├── VS-54-gift-card-stored-value/        26 workflows (3 process areas)
│   │   ├── VS-55-store-planogram-space-optimization/ 24 workflows (3 process areas)
│   │   ├── VS-56-third-party-delivery-partner/  24 workflows (3 process areas)
│   │   ├── VS-57-competitive-price-intelligence/ 24 workflows (3 process areas)
│   │   ├── VS-58-coupon-digital-promotions/     24 workflows (3 process areas)
│   │   ├── VS-59-store-closure-decommissioning/ 24 workflows (3 process areas)
│   │   ├── VS-60-omnichannel-order-routing/     24 workflows (3 process areas)
│   │   ├── VS-61-fuel-fleet-cost-management/    24 workflows (3 process areas)
│   │   ├── VS-62-product-sample-display-management/ 24 workflows (3 process areas)
│   │   ├── VS-63-store-communication-task-management/ 24 workflows (3 process areas)
│   │   ├── VS-64-seasonal-merchandise-clearance/ 24 workflows (3 process areas)
│   │   ├── VS-65-ecommerce-marketplace-integration/ 24 workflows (3 process areas)
│   │   ├── VS-66-customer-project-design-services/ 24 workflows (3 process areas)
│   │   ├── VS-67-vendor-scorecard-analytics/    24 workflows (3 process areas)
│   │   ├── VS-68-trade-credit-risk-management/  24 workflows (3 process areas)
│   │   ├── VS-69-typhoon-disaster-response/      24 workflows (3 process areas)
│   │   ├── VS-70-solar-renewable-energy/          24 workflows (3 process areas)
│   │   ├── VS-71-anti-counterfeit-authentication/  24 workflows (3 process areas)
│   │   ├── VS-72-cross-entity-shared-services/    24 workflows (3 process areas)
│   │   ├── VS-73-store-waste-circular-economy/    24 workflows (3 process areas)
│   │   ├── VS-74-contractor-jobsite-delivery/     24 workflows (3 process areas)
│   │   ├── VS-75-digital-engagement-app/          25 workflows (3 process areas)
│   │   ├── VS-76-multi-region-lgu-compliance/     24 workflows (3 process areas)
│   │   ├── VS-77-construction-material-staging/   24 workflows (3 process areas)
│   │   ├── VS-78-green-building-advisory/          24 workflows (3 process areas)
│   │   ├── VS-79-tax-management-bir-reporting/     28 workflows (3 process areas)
│   │   ├── VS-80-payment-operations-acquirer-settlement/ 24 workflows (3 process areas)
│   │   ├── VS-81-cash-in-transit-vault-armored/    24 workflows (3 process areas)
│   │   ├── VS-82-sari-sari-msme-micro-wholesale/   24 workflows (3 process areas)
│   │   ├── VS-83-occupational-health-clinic-wellness/ 25 workflows (3 process areas)
│   │   ├── VS-84-labor-relations-collective-bargaining/ 25 workflows (3 process areas)
│   │   ├── VS-85-mandatory-discount-eligibility-tax-credit/ 24 workflows (3 process areas)
│   │   ├── VS-86-anti-financial-crime-aml-abc/     24 workflows (3 process areas)
│   │   ├── VS-87-customs-trade-compliance-tariff/  25 workflows (3 process areas)
│   │   ├── VS-88-document-control-records-retention/ 24 workflows (3 process areas)
│   │   ├── VS-89-product-recall-safety-corrective-action/ 25 workflows (3 process areas)
│   │   ├── VS-90-damage-claims-freight-recovery/ 24 workflows (3 process areas)
│   │   ├── VS-91-consumer-data-privacy-protection/ 24 workflows (3 process areas)
│   │   ├── VS-92-kitting-bundling-build-to-order-assembly/ 24 workflows (3 process areas)
│   │   ├── VS-93-dark-store-micro-fulfillment/ 24 workflows (3 process areas)
│   │   ├── VS-94-cooperative-community-enterprise-procurement/ 24 workflows (3 process areas)
│   │   ├── VS-95-marketplace-operator-third-party-seller/ 24 workflows (3 process areas)
│   │   ├── VS-96-equipment-leasing-capital-equipment-finance/ 24 workflows (3 process areas)
│   │   ├── VS-97-corporate-real-estate-property-portfolio/ 24 workflows (3 process areas)
│   │   ├── VS-98-contingent-contract-outsourced-workforce/ 24 workflows (3 process areas)
│   │   ├── VS-99-it-asset-technology-lifecycle-management/ 24 workflows (3 process areas)
│   │   ├── VS-100-legal-operations-litigation-ip-management/ 25 workflows (3 process areas)
│   │   ├── VS-101-merchandise-financial-planning-otb-margin-management/ 24 workflows (3 process areas)
│   │   ├── VS-102-compensation-benefits-total-rewards/ 24 workflows (3 process areas)
│   │   ├── VS-103-hr-shared-services-employee-experience-people-analytics/ 24 workflows (3 process areas)
│   │   ├── VS-104-government-affairs-public-policy-industry-relations/ 24 workflows (3 process areas)
│   │   ├── VS-105-supply-chain-finance-working-capital-management/ 25 workflows (3 process areas)
│   │   ├── VS-106-commodity-input-cost-risk-management/ 24 workflows (3 process areas)
│   │   ├── VS-107-strategic-key-account-enterprise-customer-management/ 24 workflows (3 process areas)
│   │   ├── VS-108-onsite-renewable-energy-prosumer-asset-operations/ 24 workflows (3 process areas)
│   │   ├── VS-109-store-remodel-renovation-lifecycle-refurbishment/ 24 workflows (3 process areas)
│   │   ├── VS-110-freight-procurement-carrier-management-and-freight-audit/ 24 workflows (3 process areas)
│   │   ├── VS-111-packaging-pallet-and-returnable-transport-item-management/ 24 workflows (3 process areas)
│   │   ├── VS-112-corporate-project-and-program-management-office/ 24 workflows (3 process areas)
│   │   ├── VS-113-enterprise-architecture-application-portfolio-and-technology-strategy/ 28 workflows (3 process areas)
│   │   ├── VS-114-dangerous-goods-hazmat-transport-ecommerce-regulatory-compliance/ 24 workflows (3 process areas)
│   │   ├── VS-115-calibration-metrology-and-measurement-traceability-management/ 24 workflows (3 process areas)
│   │   ├── VS-116-performance-bond-surety-and-bank-guarantee-management/ 24 workflows (3 process areas)
│   │   ├── VS-117-dti-bps-product-standards-certification-ps-mark-icc-compliance/ 24 workflows (3 process areas)
│   │   ├── VS-118-revenue-assurance-pricing-integrity-and-leakage-management/ 25 workflows (3 process areas)
│   │   ├── VS-119-whistleblower-ethics-and-corporate-integrity-speak-up-program/ 24 workflows (3 process areas)
│   │   ├── VS-120-energy-efficiency-conservation-and-ra-11285-compliance-program/ 24 workflows (3 process areas)
│   │   ├── VS-121-talent-acquisition-employer-brand-candidate-experience/ 25 workflows (3 process areas)
│   │   ├── VS-122-global-sourcing-import-buying-sourcing-agent-management/ 24 workflows (3 process areas)
│   │   ├── VS-123-skilled-trade-apprenticeship-vocational-education-capability-pipeline/ 24 workflows (3 process areas)
│   │   ├── VS-124-sales-enablement-product-knowledge-clienteling/ 24 workflows (3 process areas)
│   │   ├── VS-125-cross-channel-fraud-management-payment-fraud-protection/ 24 workflows (3 process areas)
│   │   ├── VS-126-customer-data-platform-single-customer-view-identity-resolution/ 24 workflows (3 process areas)
│   │   ├── VS-127-sales-operations-planning-integrated-business-planning/ 32 workflows (4 process areas)
│   │   ├── VS-128-ai-ml-governance-responsible-ai/ 27 workflows (3 process areas)
│   │   ├── VS-129-competition-and-antitrust-compliance/ 24 workflows (3 process areas)
│   │   ├── VS-130-corporate-development-ma-divestiture/ 24 workflows (3 process areas)
│   │   ├── VS-131-human-rights-responsible-supply-chain-due-diligence/ 24 workflows (3 process areas)
│   │   ├── VS-132-corporate-political-engagement-election-compliance/ 24 workflows (3 process areas)
│   │   ├── VS-133-operational-excellence-process-mining-continuous-improvement/ 24 workflows (3 process areas)
│   │   ├── VS-134-organizational-change-management-digital-adoption-transformation-enablement/ 24 workflows (3 process areas)
│   │   ├── VS-135-technology-business-management-it-financial-management-cloud-finops/ 24 workflows (3 process areas)
│   │   ├── VS-136-supply-chain-network-design-multi-echelon-inventory-optimization-flow-engineering/ 24 workflows (3 process areas)
│   │   ├── VS-137-product-information-management-and-digital-asset-management/ 24 workflows (3 process areas)
│   │   ├── VS-138-integrated-facilities-management-workplace-services-and-building-automation/ 24 workflows (3 process areas)
│   │   ├── VS-139-trade-show-exhibition-and-field-event-marketing/ 24 workflows (3 process areas)
│   │   ├── VS-140-field-sales-outside-sales-and-route-to-market-force-management/ 24 workflows (3 process areas)
│   │   ├── VS-141-employee-transport-shuttle-and-daily-commute-management/ 25 workflows (3 process areas)
│   │   ├── VS-142-cash-on-delivery-operations-driver-cash-handling-and-reconciliation/ 24 workflows (3 process areas)
│   │   ├── VS-143-bulky-white-goods-delivery-installation-haul-away-and-recycling/ 24 workflows (3 process areas)
│   │   ├── VS-144-employee-accommodation-dormitory-and-staff-housing/ 24 workflows (3 process areas)
│   │   ├── VS-145-garden-center-live-goods-and-plant-nursery/ 24 workflows (3 process areas)
│   │   ├── VS-146-customer-mystery-shopping-and-service-quality-assurance/ 24 workflows (3 process areas)
│   │   ├── VS-147-customer-safety-premises-liability-and-in-store-risk-management/ 26 workflows (3 process areas)
│   │   ├── VS-148-lease-accounting-pfrs-16-and-right-of-use-asset-management/ 24 workflows (3 process areas)
│   │   ├── VS-149-self-checkout-scan-and-go-and-unattended-retail-technology-operations/ 24 workflows (3 process areas)
│   │   ├── VS-150-drug-free-workplace-and-substance-abuse-program/ 24 workflows (3 process areas)
│   │   ├── VS-151-auto-id-barcode-rfid-labeling-and-eas-operations/ 24 workflows (3 process areas)
│   │   ├── VS-152-corporate-social-responsibility-foundation-and-community-investment/ 24 workflows (3 process areas)
│   │   ├── VS-153-captive-insurance-reinsurance-and-enterprise-risk-financing/ 24 workflows (3 process areas)
│   │   ├── VS-154-home-construction-finance-loan-brokerage-and-mortgage-referral/ 24 workflows (3 process areas)
│   │   ├── VS-155-trade-in-buy-back-and-certified-pre-owned-product-resale/ 24 workflows (3 process areas)
│   │   ├── VS-156-in-store-value-added-services-and-financial-agency-operations/ 24 workflows (3 process areas)
│   │   ├── VS-157-revenue-recognition-pfrs-15-and-complex-contract-accounting/ 24 workflows (3 process areas)
│   │   ├── VS-158-product-costing-landed-cost-and-cost-accounting/ 24 workflows (3 process areas)
│   │   ├── VS-159-corporate-security-executive-protection-and-travel-risk-management/ 24 workflows (3 process areas)
│   │   ├── VS-160-global-mobility-immigration-and-foreign-worker-compliance/ 24 workflows (3 process areas)
│   │   ├── VS-161-third-party-and-supplier-risk-management-tprm/ 24 workflows (3 process areas)
│   │   ├── VS-162-customer-pickup-truck-and-cargo-van-rental/ 24 workflows (3 process areas)
│   │   ├── VS-163-electric-vehicle-ev-charging-station-host-network-operations/ 24 workflows (3 process areas)
│   │   ├── VS-164-smart-locker-and-automated-parcel-collection-network/ 24 workflows (3 process areas)
│   │   ├── VS-165-pcab-contractor-licensing-and-ra-4566-construction-contractor-compliance/ 24 workflows (3 process areas)
│   │   ├── VS-166-regulatory-license-permit-and-accreditation-portfolio-management/ 24 workflows (3 process areas)
│   │   ├── VS-167-workforce-background-screening-credentialing-and-personnel-vetting/ 24 workflows (3 process areas)
│   │   ├── VS-168-in-store-audio-ambient-media-and-music-royalty-licensing/ 24 workflows (3 process areas)
│   │   ├── VS-169-employee-uniform-workwear-and-ppe-issuance-program/ 24 workflows (3 process areas)
│   │   ├── VS-170-inventory-pledge-asset-based-lending-and-trust-receipt-financing/ 24 workflows (3 process areas)
│   │   ├── VS-171-customer-pickup-loading-zone-and-will-call-counter-operations/ 24 workflows (3 process areas)
│   │   ├── VS-172-third-party-installer-and-contractor-network-pro-referral-management/ 24 workflows (3 process areas)
│   │   ├── VS-173-investor-relations-capital-markets-and-securities-disclosure/ 24 workflows (3 process areas)
│   │   ├── VS-174-self-storage-portable-container-and-mobile-storage-operations/ 24 workflows (3 process areas)
│   │   ├── VS-175-propane-lpg-cylinder-exchange-and-gas-refill-operations/ 24 workflows (3 process areas)
│   │   ├── VS-176-blueprint-reprographics-and-large-format-plan-printing-services/ 24 workflows (3 process areas)
│   │   ├── VS-177-field-retail-operations-regional-district-management-and-multi-store-execution/ 24 workflows (3 process areas)
│   │   ├── VS-178-landbanking-site-acquisition-and-agrarian-lgu-zoning-conversion/ 25 workflows (3 process areas)
│   │   ├── VS-179-extended-producer-responsibility-compliance-and-plastic-recovery-network/ 24 workflows (3 process areas)
│   │   ├── VS-180-disaster-relief-supply-chain-logistics-and-humanitarian-aid-coordination/ 24 workflows (3 process areas)
│   │   ├── VS-181-b2b-project-financing-escrow-account-orchestration-and-lien-release/ 24 workflows (3 process areas)
│   │   ├── VS-182-b2b-bulk-project-custom-import-indent-sourcing-and-brokerage/ 24 workflows (3 process areas)
│   │   ├── VS-183-dual-training-system-dts-and-tesda-partnership-program/ 24 workflows (3 process areas)
│   │   ├── VS-184-post-disaster-store-infrastructure-reconstruction-and-rehabilitation/ 24 workflows (3 process areas)
│   │   ├── VS-185-b2b-cooperative-credit-and-procurement-partnerships/ 24 workflows (3 process areas)
│   │   ├── VS-186-compact-and-heavy-construction-equipment-rental-fleet-operations/ 24 workflows (3 process areas)
│   │   ├── VS-187-household-hazardous-waste-paint-and-product-stewardship-take-back/ 24 workflows (3 process areas)
│   │   ├── VS-188-trade-reseller-floor-plan-and-dealer-inventory-financing/ 24 workflows (3 process areas)
│   │   ├── VS-189-trade-receivables-factoring-invoice-discounting-and-securitization/ 24 workflows (3 process areas)
│   │   ├── VS-190-operational-technology-ot-ics-cybersecurity-and-retail-technology-asset-protection/ 24 workflows (3 process areas)
│   │   ├── VS-191-customer-construction-debris-demolition-waste-and-site-cleanup-operations/ 24 workflows (3 process areas)
│   │   └── VS-192-green-fleet-transition-electric-vehicle-fleet-operations-and-sustainable-transportation/ 24 workflows (3 process areas)
│   ├── executive-summary.md            1-page C-suite overview
│   ├── assumptions-and-design-decisions.md  Consolidated assumptions & rationale
│   ├── headcount-reality-check.md     HQ headcount vs. workflow-coverage gap analysis
│   ├── optimal-table-of-organization.md  OFFICIAL table of organization of record — THE ACTUAL STRUCTURE (promoted 2026-09-14): HQ 511 / total 6,911, every HQ role defined in §5.3 (pre-optimization 362 / 6,762 retained as the §5.1 reference column; official elevation 2026-09-09; two-tier IT sourcing + agentic-AI model)
│   ├── requirement-workflow-matrix.md  Cross-reference: requirements ↔ workflows
│   ├── internal-controls-matrix.md     808 internal controls by objective
│   ├── role-coverage-matrix.md         GENERATED role ↔ workflow coverage matrix (per-role owned/participated/step/tier-mix; regenerate via 07-methodology/generate-role-coverage.py — do not hand-edit)
│   ├── mobile-app-strategy.md          Customer & employee mobile app strategy
│   └── data-migration-mapping.md       Data migration field mapping templates
├── 02-oracle-ebs/               ← Oracle E-Business Suite 12.2 platform blueprint (the ERP core of record)
│   ├── README.md                      Platform decision, fit-to-standard principles, document map, realization waves
│   ├── ebs-platform-architecture.md   Org/ledger model (5 legal entities · 205 inventory orgs), module footprint, tech stack, environments, integration & security
│   ├── module-coverage-map.md         Generic-module → EBS realization register, side-by-side with workflow-system-touchpoint-map.md
│   ├── fit-gap-analysis.md            97-row capability disposition register (74 standard / 2 PER / 1 EXT / 1 LOC / 5 INT / 14 BUILD incl. 5 already-built platforms / 0 EDGE / 0 OPEN), EBS-held vs payroll-built statutory split, two-tier resolution record + 2026-09-15/16 EBS-exhaustion audits (eight passes), standard-first KPIs
│   ├── customization-governance.md    CEMLI discipline: extension budget, CDR workflow, ADOP-safe coding standards, CEMLI register, de-customization triggers
│   ├── integrations.md                IAP-first integration patterns for every flow in the canonical integration matrix
│   ├── data-migration.md              Object → EBS load-path register (interfaces/APIs only), validation gates, cutover
│   ├── licensing-bom.md               License bill of materials — EBS perpetual + support vs Fusion Cloud scenarios, from the module footprint & user/volume drivers (negotiation baseline; totals re-derived by audit-model-docs)
│   └── ebs-vision-verification.md     Live verification of the documentation set against the Oracle EBS 12.2.12 Vision instance — footprint conformance, five transactional smoke tests, findings VF-1…VF-6 (regenerated per verification run)
├── dmn/                         ← Generated DMN 1.3 decision models (79 decisions across 40 process areas; rule tables + tiered PHP authorization thresholds; mirrors the workflows/ tree; regenerates via 07-methodology/generate-dmn.py)
├── bpmn/                        ← Generated BPMN 2.0 models (5,450 processes; mirrors the workflows/ tree; regenerates via 07-methodology/generate-bpmn.py)
├── CHANGELOG.md                 ← Revision history
└── 07-methodology/              ← Technical system architecture and guidelines
    ├── README.md                     Methodology index & future document plan
    ├── technical-guidelines.md       POS hardware, infrastructure, integration, security, two-tier sourcing architecture
    ├── capability-sourcing-and-engineering-model.md  Two-tier sourcing decision gate (in EBS → use it; otherwise build), sourcing register, build squads, SEP
    ├── it-product-operating-model.md IT product teams (two-tier: in-suite EBS core + in-house built & already-built platforms + AI agent platform), roles, RACI, governance, sizing (50 → 122 FTE)
    ├── ai-first-operating-guide.md   The AI-first operating guide — ERP-agnostic doctrine (ten laws, six layers, capability contracts), sourcing neutrality, autonomy ladder, agent factory, the EKB as persistent memory + consistency engine, the no-confusion decision system, and the seven-phase adoption path (v1.12)
    ├── validate-repo.sh              Cross-reference validation (77 checks)
    ├── generate-bpmn.py             BPMN 2.0 generator — converts every workflow block in 01-model-company/workflows into validated .bpmn files under bpmn/ (5,450 processes, lanes, DI)
    ├── generate-dmn.py             DMN 1.3 generator — extracts rule tables and tiered PHP authorization rules from workflow markdown into validated .dmn files under dmn/ (79 decisions, decision tables, DMNDI)
    ├── generate-role-coverage.py   Role–workflow coverage generator — parses PA RACI fields + tier register + the official TO into 01-model-company/role-coverage-matrix.md (per-role owned/participated/step/tier-mix, --check byte-verify)
    ├── classify-workflows.py         Keyword-driven criticality classifier
    ├── confirm-all-workflows.py      One-time full-coverage confirmation pass (2,596 → 0 unclassified)
    ├── confirm-postcatalog-14.py     One-time post-catalog confirmation pass (W5497–W5510: 14 → 0 unclassified, 2026-09-02)
    ├── add-automation-controls.py    Automation/Controls field adder
    ├── backfill-controls.py          CTL-XX backfiller for Controls sections
    ├── add-expansion-anchors.py      One-time expansion/legacy-block anchor-control adder (CTL-172–239)
    ├── add-pa-controls.py            Process-area operating-control adder (CTL-240–808; closes CTL mapping to 100%)
    ├── backfill-participants.py      Participants derivation from Steps roles
    ├── backfill-time-estimate.py     Time Estimate derivation from step durations
    ├── finalize-time-estimates.py    Draft Time Estimate finalizer (per-occurrence roll-up + Frequency-derived annualization; Check 49 companion)
    ├── audit-time-estimate-math.py    Inline-arithmetic audit of Time Estimate / Staffing paragraphs (unit-convention-aware chain re-derivation; Check 50 guard)
    ├── reconcile-staffing-claims.py  Headcount-anchor & Volume-product reconciliation vs canonical registers (Check 51 guard)
    ├── virtual-gemba-walk.py         Virtual gemba walk & time-and-motion analyzer — per-VS touch time / handoff / approval-gate walk + per-role annual demand vs chartered TO capacity (read-only; 39th wave)
    ├── audit-st-touchpoints.py       ST-vocabulary & duplicate-Trigger guard (Check 52)
    ├── fix-auto-keywords.py          Automation-keyword & RACI role-title repair/guard (Check 53)
    ├── audit-field-vocabulary.py    Risk-label / cadence / owner vocabulary guard (Check 54)
    ├── audit-participants-units.py  Participants hygiene & per-unit volume coherence guard (Check 55)
    ├── audit-operational-controls.py Operational-control prose variant guard (Check 56)
    ├── audit-risk-labels.py         Risk-label punctuation guard (Check 57)
    ├── audit-enrichment-completeness.py  Mitigation-clause & Trigger-richness guard (Check 58)
    ├── audit-model-docs.py           Root model-doc figure & cross-reference guard (Check 59)
    ├── audit-exec-ctl.py             Exec-summary anchors & CTL citation-scope guard (Check 60)
    ├── audit-matrix-refs.py          Matrix ghost-row & summary-doc anchor guard (Check 61)
    ├── audit-semantic-anchors.py    Semantic-sample anchor guard (Check 62)
    ├── audit-misdirected-ctl.py     Misdirected-CTL-citation family measurer (the batch-26/27 paste-family audits)
    ├── classify-isolated-ctl.py     Isolated colon-form CTL-citation classifier (gloss-vs-control overlap scoring, batch-27)
    ├── final-semantic-coverage.py    Final full-coverage semantic pass (review #71 — detector suite over the 3,122 unaudited workflows; closed the sampling loop to 5,363/5,363; the 2026-09-03 W5511 transition re-run extends the registry to 5,364/5,364; the agentic gap-fill transition extends it to 5,367/5,367; the sourcing-model gap-fill transition extends it to 5,370/5,370 — the current audited set; the 18 post-closure gap-fill workflows W5518–W5535 (the IT/people/finance/operations gap-fill passes, batches 8–11, plus the demand-intake gap fill, batch 15), are registry-pending, not audited)
    ├── semantic-audit-coverage.txt  Audited-W-id registry — LOOP CLOSED 2026-09-02 at 5,363 of 5,363; W5511 audited in full + detector-swept and admitted 2026-09-03 → 5,364 of 5,364; W5512–W5514 audited in full + detector-swept and admitted the same day → 5,367 of 5,367; W5515–W5517 (the capability-sourcing & engineering surface) admitted via the same path → 5,370 of 5,370, the current admitted set (2,241 stratified full-reads reviews #44–#67 + the review-#71 final-coverage detector pass; the fork-local batches 22–29 read their 832 post-fork W-ids in full — see the 2026-09-02 branch-reconciliation merge entry in CHANGELOG). The 18 post-closure workflows W5518–W5535 (the IT/people/finance/operations gap-fill passes, batches 8–11, plus the demand-intake gap fill, batch 15, 2026-09-03→04) carry the registry's transition-path-pending notes — NOT yet admitted; admission follows the documented W5511 transition path (full read + D1–D4 detector sweep), and Check 69 enforces live = admitted + pending
    ├── draw-batch26.py             Batch-26 semantic-audit sample drawer (seed 7070, 104 workflows, expansion-weighted)
    ├── draw-batch27.py             Batch-27 semantic-audit sample drawer (seed 7171)
    ├── draw-batch28.py             Batch-28 semantic-audit sample drawer (seed 7272)
    ├── draw-batch29.py             Batch-29 semantic-audit sample drawer (seed 7373)
    ├── placeholder-field-census.txt Completed missing-quantifier field census (173 spots repaired in review #57; now guarded structurally in Check 62)
    ├── unit-less-time-estimate-census.txt  Completed unit-less `per occurrence` Time Estimate census (131 spots repaired in review #62; now guarded structurally in Check 62)
    ├── batch18-deferred-candidates.txt  Batch-18 verified-but-deferred candidates — COMPLETED 2026-09-02 by review #70's re-audit + repair pass (~0 spots remain; all candidates repaired, closed with pointers, or dismissed)
    ├── batch17-deferred-candidates.txt  Batch-17 deferred candidates (~185 of ~190 spots repaired in review #62; both named residuals since closed — the W16.1 four-matrix conflict consolidated on W24's canonical ladder in review #64, and the W712 quote was not locatable with current text verified correct)
    ├── batch23-deferred-candidates.txt  Batch-23 deferred candidates — items 1–4 (VP Operations ghost family, W126 scope, the W239 move, the 204-vs-205 family) RESOLVED in the #69 successor adjudication pass; the role-charter/org residuals closed by the fork-local #72 ghost-role sweep and worklist closures (see CHANGELOG); item A ghost-title charter decisions closed by the batch-14 charter sweep and item B by batches 12–13
    ├── defragment-automation.py      One-time fragment-Automation-bullet repairer
    ├── fix-headcount-6757.py         Stale-headcount figure repairer (Check 24 companion)
    ├── fix-toc-anchors.py            Intra-file TOC anchor repairer (Check 23 companion)
    ├── fix-table-structure.py        One-time table delimiter/structure repairer (Check 29 companion)
    ├── fix-toc-completeness.py       PA TOC completeness/stray-fragment repairer (Check 30 companion)
    ├── fix-pa-names.py               PA-name 3-way aligner: H1 ↔ VS README ↔ index (Check 31 companion)
    ├── fix-pa-wrefs.py               Dangling/misdirected W- & CTL-reference repairer inside PA bodies (Check 33 companion)
    ├── fix-ctl-pa-names.py           PA-control objective canonicalizer: matrix ↔ index ↔ PA bodies (Check 34 companion)
    ├── fix-vs-wrefs.py               Workflow-reference-in-VS-namespace repairer inside the catalog (Check 35 companion)
    ├── fix-ctl-paste-families.py     One-time re-mapper of the 36 paste-family misdirected CTL citations (batch-26, review #72)
    ├── fix-ghost-roles-batch26.py    Ghost-role adjudication sweep for the batch-26 families (review #72; batch-24 precedent; sunset-guarded 2026-09-10 — refuses to run against the official TO's charted VP seats)
    ├── fix-ghost-titles-batch14.py   Ghost-title charter sweep closing item A — 25 uncharted-title families mapped to TO-charted seats (~1,090 spots, batch 14; sunset-guarded 2026-09-10 — refuses to run against its own frozen history note)
    ├── fix-pa211-order.py            One-time PA-21.1 scrambled-section-order canonicalizer (batch-27, review #73)
    ├── fix-controls-bullets.py       Controls-section list-hygiene/paren/bold repairer (Check 43 companion)
    ├── fix-controls-splice-artifacts.py         Forty-ninth-wave Controls-splice repairer, mechanical classes — 50 exact-match repairs (duplicated items, dangling '; .' tails)
    ├── fix-controls-splice-artifacts-2-context.py — Forty-ninth-wave Controls-splice repairer, context class — 49 exact-match repairs (risk-splices, vs.-truncations, re-grounded in each workflow's own Pain Points/Steps)
    ├── fix-ebs-vehicle-stragglers.py  Fifty-second-wave EBS-exhaustion straggler repairer — 87 exact-match vehicle re-points across 41 PA files (132 across 61 for the wave with part 2 + 23 inline context repairs) (eAM, Quality, Demantra, XTR/CE, AGIS, Procurement Contracts, Product Hub/SLM, Property Manager/A12 EXT, iRecruitment, Advanced Pricing, In-Memory Cost, DQM/SLM, OLA, Payroll PH, ROE/OTE, Oracle Alert); forms guarded by Check 46
    ├── fix-ebs-vehicle-stragglers-2.py — Fifty-second-wave part 2 — 22 further re-points from the whole-corpus scan (CMMS residuals, 'ERP loyalty module' conflicts, RM&I, Trade Management, Succession, ICM, Quality, WMS Yard, Sourcing, Install Base)
    ├── fix-pain-template-engine.py   Fiftieth-wave Pain-Points de-templating engine — corpus-wide template-pool derivation, keep-specific/replace-template semantics, balance+mitigation verification
    ├── fix-pain-template-vs65.py     Fiftieth-wave Pain de-templating, VS-65 — 24 workflow-specific Pain sections grounded in each workflow's own steps
    ├── fix-pain-template-vs66-68-74.py — Fiftieth-wave Pain de-templating, VS-66/68/74 — 72 workflow-specific Pain sections
    └── fix-pain-template-vs75-77-78.py — Fiftieth-wave Pain de-templating, VS-75/77/78 — 72 workflow-specific Pain sections
```

## The Model Company at a Glance

| Parameter | Value |
|---|---|
| Company Name | **BuildRight Depot Corp.** |
| Format | Hardware / DIY / Home Improvement Big Box |
| Stores | 200 |
| Distribution Centers | 4 |
| Corporate HQ | Davao City, Philippines |
| POS Machines per Store | 3 |
| Monthly POS Transactions per Store | 14,000 |
| Avg Lines per Transaction | 4 |
| Staff per Store | 29 |
| Active SKUs | 35,000 |
| Monthly Trade Purchase Orders | ~1,200 merchandise; ~1,400–1,600 total |
| Legal Entities | 5 |
| Total Headcount | 6,911 (200 stores × 29 + 600 DC + 511 HQ) |
| Ecommerce | Yes (with BOPIS) |
| Country | Philippines |

## Key Metrics

> **Single source of truth**: Counts below are derived from actual document content. All documents in this repository reference these figures.

| Metric | Value | Source |
|---|---|---|
| Requirements | **728** across 38 categories | `01-model-company/erp-requirements.md` |
| Workflows (total) | **5,427** across 188 value streams, 569 process areas | `01-model-company/workflows/value-stream-index.md` |
| Internal Controls | 808 (88 preventive, 720 detective) | `01-model-company/internal-controls-matrix.md` |
| Must Have Requirements | 429 | `01-model-company/erp-requirements.md` |
| Should Have Requirements | 293 | `01-model-company/erp-requirements.md` |
| Nice to Have Requirements | 6 | `01-model-company/erp-requirements.md` |

## Coverage & Known Gaps

| Coverage Area | Status | Source |
|---|---|---|
| Requirements | 728 fully specified (429 Must / 293 Should / 6 Nice) | `erp-requirements.md` |
| Workflows | 5,427 fully specified across 188 value streams (all 5,427 confirmed-classified — the 14 post-catalog additions W5497–W5510 were confirmed 2026-09-02; W5511 gift-card dormancy/escheat shipped confirmed 2026-09-03 in the event-custody pass; W5512–W5514 agentic-AI platform lifecycle shipped confirmed 2026-09-03 in the agentic gap-fill pass; W5515–W5517 capability-sourcing & engineering shipped confirmed 2026-09-03 in the sourcing-model gap-fill pass; W5518–W5524 the IT operating-model gap fill shipped confirmed 2026-09-03 (5 Tier 2 / 2 Tier 3) in the IT workflow gap-fill pass; W5525–W5528 the people-capability & reporting-policy gap fill shipped confirmed 2026-09-03 (4 Tier 2) in the people-workflow gap-fill pass; W5529–W5531 the finance-workflow gap fill shipped confirmed 2026-09-03 (2 Tier 1 / 1 Tier 2) in the finance-workflow gap-fill pass; W5532–W5534 the operations-workflow gap fill shipped confirmed 2026-09-04 (1 Tier 1 / 2 Tier 2) in the operations-workflow gap-fill pass; W5535 the capability demand-intake & backlog-triage gap fill shipped confirmed 2026-09-04 (1 Tier 2) in the demand-intake gap-fill pass; W5536–W5543 the emergency & continuity workflow gap fill shipped confirmed 2026-09-05 (3 Tier 1 / 5 Tier 2) in the emergency & continuity gap-fill pass; W5544–W5549 the regulatory-shock, platform-outage & governance-continuity gap fill shipped confirmed 2026-09-05 (2 Tier 1 / 4 Tier 2) in the batch-17 gap-fill pass; W5550–W5553 the channel-enforcement, employee-legal-status, OSH-enforcement & app-store-removal gap fill shipped confirmed 2026-09-05 (1 Tier 1 / 3 Tier 2) in the batch-18 gap-fill pass; W5554–W5557 the in-transit-security, fatality-scene, tampering-extortion & recruitment-fraud gap fill shipped confirmed 2026-09-05 (2 Tier 1 / 2 Tier 2) in the batch-19 gap-fill pass; W5558–W5561 the cyber-extortion, payment-diversion, land-occupation & water-continuity gap fill shipped confirmed 2026-09-05 (1 Tier 1 / 3 Tier 2) in the batch-20 gap-fill pass; W5562–W5565 the storefront-crash, brand-impersonation-scam, wallet-outage & adjacent-works gap fill shipped confirmed 2026-09-05 (1 Tier 1 / 3 Tier 2) in the batch-21 gap-fill pass; W5566–W5569 the terminal-tampering, procurement-impersonation, account-takeover & commute-disruption gap fill shipped confirmed 2026-09-05 (4 Tier 2) in the batch-22 gap-fill pass; W5570–W5573 the gas-leak, tsunami/storm-surge, media-exposé & server-room-environmental gap fill shipped confirmed 2026-09-05 (2 Tier 1 / 2 Tier 2) in the batch-23 gap-fill pass) | `workflows/value-stream-index.md` |
| Criticality classification | **5,427 of 5,427 workflows classified (full coverage)** — the confirmed register holds 5,450 rows incl. 23 `###` parent/summary sub-workflows; the 2026-06-28 Full-Coverage Confirmation Pass promoted the remaining keyword-proposed workflows (unclassified 2,596 → 0; 65 → Tier 1 statutory, 179 → Tier 3 analytics, 3 demoted to Tier 2, remainder adopted); the fourteen post-catalog workflows W5497–W5510 (added 2026-08-24/26) were confirmed 2026-09-02 (6 → Tier 1, 6 → Tier 2, 2 → Tier 3); W5511 (gift-card dormancy monitoring, escheat evaluation & expired-liability derecognition, VS-54.3) shipped confirmed Tier 2 in the 2026-09-03 event-custody pass; W5512–W5514 (the agentic-AI platform lifecycle, VS-128.3) shipped confirmed Tier 2 in the 2026-09-03 agentic gap-fill pass; W5515–W5517 (the capability-sourcing & engineering surface, VS-113) shipped confirmed Tier 2 in the 2026-09-03 sourcing-model gap-fill pass; W5518–W5524 (the IT operating-model surface, VS-27) shipped confirmed Tier 2 (5) / Tier 3 (2) in the 2026-09-03 IT workflow gap-fill pass; W5525–W5528 (the people-capability & reporting-policy surface, VS-19.4/VS-17.4) shipped confirmed Tier 2 (4) in the 2026-09-03 people-workflow gap-fill pass; W5529–W5531 (the finance-workflow surface, VS-42.3/VS-17.3/VS-17.4) shipped confirmed Tier 1 (2) / Tier 2 (1) in the 2026-09-03 finance-workflow gap-fill pass; W5532–W5534 (the operations-workflow surface, VS-19.3/VS-79.2/VS-23.2) shipped confirmed Tier 2 (2) / Tier 1 (1) in the 2026-09-04 operations-workflow gap-fill pass; W5535 (the capability demand-intake & backlog-triage surface, PA-113.2/VS-113) shipped confirmed Tier 2 (1) in the 2026-09-04 demand-intake gap-fill pass; W5536–W5543 (the emergency & continuity surface — missing-child/Code Adam, fire event, bomb threat, elevator entrapment, payroll run failure, bank failure, liquidity stress, price-file integrity event — VS-07.2/VS-24.2/VS-19.2/VS-18.3/VS-105.3/VS-118.2) shipped confirmed Tier 1 (3) / Tier 2 (5) in the 2026-09-05 emergency & continuity gap-fill pass; W5544–W5549 (the regulatory-shock, platform-outage & governance-continuity surface — emergency executive succession, BIR Oplan Kandado enforcement closure, eFPS outage filing contingency, card-network/acquirer outage, stored-value & loyalty platform outage, suicide/self-harm incident response — VS-36.1/VS-79.3/VS-08.1/VS-54.2/VS-24.1) shipped confirmed Tier 1 (2) / Tier 2 (4) in the 2026-09-05 batch-17 gap-fill pass; W5550–W5553 (the channel-enforcement, employee-legal-status, OSH-enforcement & app-store-removal surface — VS-10.3/VS-19.1/VS-24.1/VS-75.1) shipped confirmed Tier 1 (1) / Tier 2 (3) in the 2026-09-05 batch-18 gap-fill pass; W5554–W5557 (the in-transit-security, fatality-scene, tampering-extortion & recruitment-fraud surface — VS-06.2/VS-147.3/VS-89.1/VS-121.1) shipped confirmed Tier 1 (2) / Tier 2 (2) in the 2026-09-05 batch-19 gap-fill pass; W5558–W5561 (the cyber-extortion, payment-diversion, land-occupation & water-continuity surface — ransomware/destructive cyber-attack enterprise response, vendor payment-diversion/BEC fraud response, informal-settler invasion of banked land, sustained water-service interruption — VS-27.3/VS-18.2/VS-178.1/VS-07.2) shipped confirmed Tier 1 (1) / Tier 2 (3) in the 2026-09-05 batch-20 gap-fill pass; W5562–W5565 (the storefront-crash, brand-impersonation-scam, wallet-outage & adjacent-works surface — vehicle-impact & storefront-crash response, brand-impersonation commerce-scam response, mobile-wallet platform outage response, third-party construction damage & adjacent-works response — VS-147.2/VS-100.2/VS-08.1/VS-20.3) shipped confirmed Tier 1 (1) / Tier 2 (3) in the 2026-09-05 batch-21 gap-fill pass; W5566–W5569 (the terminal-tampering, procurement-impersonation, account-takeover & commute-disruption surface — payment-terminal tampering & card-skimmer response, procurement-impersonation & fake-PO goods-diversion response, official-channel account-takeover response, mass-commute disruption & transport-strike continuity — VS-08.2/VS-03.2/VS-14.2/VS-141.2) shipped confirmed Tier 2 (4) in the 2026-09-05 batch-22 gap-fill pass; W5570–W5573 (the gas-leak, tsunami/storm-surge, media-exposé & server-room-environmental surface — gas-leak event response, tsunami & storm-surge coastal-intrusion response, undercover-investigation & media-exposé response, server-room & data-center environmental event response — VS-24.2/VS-26.1/VS-14.3/VS-27.2) shipped confirmed Tier 1 (2) / Tier 2 (2) in the 2026-09-05 batch-23 gap-fill pass; W5574 (the concessionaire connectivity request, approval & independent-circuit governance surface, VS-07.1) shipped confirmed Tier 2 (1) in the 2026-09-10 batch-24 gap-fill pass; `workflow-criticality-proposed.md` is empty | `workflows/workflow-criticality-classification.md` |
| Internal controls | 808 controls mapped to workflows and requirements (67 core + 172 domain anchors CTL-68–239 + 569 process-area operating controls CTL-240–808) — CTL-XX citation coverage is 100% of workflows | `internal-controls-matrix.md` |
| Retired VS numbers | VS-49–VS-52 were retired after a 2026-06-14 review found their 96 workflow files contained only auto-generated placeholder content; the numbers remain unused. The resulting gaps — plus additional uncovered capabilities — were filled across thirty gap-analysis passes (2026-06-14 → 2026-06-21), growing the active inventory from 84 to 188 value streams (VS-89–VS-192; W2993–W5488). The canonical per-pass detail (candidates considered/rejected, workflow-ID allocation, family-subtotal impact) lives in [`workflows/workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md) §3–§4 and [CHANGELOG.md](CHANGELOG.md) | — |

## Document Relationships

```
                              ┌──────────────────────┐
                              │     README.md        │
                              │  (this file — index) │
                              └──────────┬───────────┘
                                         │
              ┌──────────────────────────┼──────────────────────────┐
              │                          │                          │
   ┌──────────▼──────────┐  ┌───────────▼───────────┐  ┌──────────▼──────────┐
   │  01-model-company/  │  │  07-methodology/      │  │ 02-oracle-ebs/      │
   │  Business context   │  │  Technical reference  │  │  Platform blueprint │
   └──────────┬──────────┘  └───────────┬───────────┘  └─────────────────────┘
              │                          │
   ┌──────────▼──────────────────────────▼───────────┐
   │              CROSS-REFERENCE LAYER               │
   │                                                   │
   │  erp-requirements.md ←→ workflows/ (5,427 WF)    │
   │       ↕                    ↕                      │
   │  internal-controls-   workflow-criticality-      │
   │  matrix.md (808 CTL)  classification.md          │
   │       ↕                    ↕                      │
   │  requirement-workflow- workflow-dependency-       │
   │  matrix.md              map.md                   │
   │       ↕                    ↕                      │
   │  assumptions-and-      workflow-system-           │
   │  design-decisions.md   touchpoint-map.md          │
   │                          ↕                        │
   │                value-stream-index.md              │
   │            (188 VS · 569 process areas)            │
   └───────────────────────────────────────────────────┘
```
