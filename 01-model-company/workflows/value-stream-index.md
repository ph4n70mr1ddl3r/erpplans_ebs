# BuildRight Depot Corp. — Value Stream Index

> Index of all operational workflows organized by **Value Stream** and **Process Area**.
> For the workflow format, conventions, and RACI key, see [WORKFLOW-FORMAT-GUIDE.md](./WORKFLOW-FORMAT-GUIDE.md).

---

## Value-Stream Blocks (origin)

The 188 active value streams were produced in four blocks. Use this to gauge content maturity
at a glance — all four blocks are now fully detailed; the *Expansion* block was templated but
was de-boilerplated on 2026-06-20 (the regression guard is `validate-repo.sh` Check 10).
Per-pass history: [workflow-gap-analysis.md](workflow-gap-analysis.md) §4.

| Block | VS range | Count | Maturity |
|---|---|---|---|
| Core | VS-01 – VS-48 | 48 | Fully detailed (original foundational model) |
| Expansion | VS-53 – VS-78 | 26 | Fully detailed (22 templated VSs de-boilerplated 2026-06-20; VS-69/70/71/73 were pre-detailed) |
| Statutory | VS-79 – VS-88 | 10 | Fully detailed (regulatory & finance deepening) |
| Gap analysis | VS-89 – VS-192 | 104 | Fully detailed (thirty gap-analysis passes, 2026-06-14/15/16/17/18/19/20/21) |
| — | VS-49 – VS-52 | — | Retired (placeholders removed 2026-06-14; numbers unused) |

---

## Value Stream Architecture

```
8 Families · 188 Value Streams · 569 Process Areas · 5,430 Workflows
```

> **Coverage note:** VS-49–VS-52 were retired after a 2026-06-14 review found their 96 workflow files contained only auto-generated placeholder content; the numbers remain unused. The resulting capability gaps — plus additional uncovered capabilities — were subsequently filled across thirty gap-analysis passes (2026-06-14 → 2026-06-21), growing the active inventory from 84 to 188 value streams (VS-89–VS-192; W2993–W5488). The canonical per-pass history — candidates considered and rejected-as-covered, workflow-ID allocation, and the family-subtotal impact — lives in [workflow-gap-analysis.md](workflow-gap-analysis.md) §3–§4 and [CHANGELOG.md](../../CHANGELOG.md).

| Family | VS | Value Stream | Block | Process Areas | Workflows |
|---|---|---|---|---|---|
| Plan & Source | [VS-01](VS-01-merchandise-strategy/README.md) | Merchandise Strategy | Core | 3 | 46 |
|  | [VS-02](VS-02-supply-planning/README.md) | Supply Planning | Core | 3 | 38 |
|  | [VS-03](VS-03-vendor-management/README.md) | Vendor Management & Procurement | Core | 4 | 82 |
|  | [VS-41](VS-41-private-label-brand/README.md) | Private Label & Exclusive Brand Management | Core | 3 | 24 |
|  | [VS-45](VS-45-consignment-vmi-operations/README.md) | Consignment & Vendor-Managed Inventory Operations | Core | 3 | 24 |
|  | [VS-57](VS-57-competitive-price-intelligence/README.md) | Competitive Price Intelligence & Monitoring | Expansion | 3 | 24 |
|  | [VS-64](VS-64-seasonal-merchandise-clearance/README.md) | Seasonal Merchandise Transition & Clearance | Expansion | 3 | 24 |
|  | [VS-67](VS-67-vendor-scorecard-analytics/README.md) | Vendor Scorecard & Performance Analytics | Expansion | 3 | 24 |
|  | [VS-94](VS-94-cooperative-community-enterprise-procurement/README.md) | Cooperative & Community Enterprise Procurement | Gap analysis | 3 | 24 |
|  | [VS-101](VS-101-merchandise-financial-planning-otb-margin-management/README.md) | Merchandise Financial Planning, OTB & Margin Management | Gap analysis | 3 | 24 |
|  | [VS-106](VS-106-commodity-input-cost-risk-management/README.md) | Commodity & Input-Cost Risk Management | Gap analysis | 3 | 24 |
|  | [VS-122](VS-122-global-sourcing-import-buying-sourcing-agent-management/README.md) | Global Sourcing, Import Buying & Sourcing Agent Management | Gap analysis | 3 | 24 |
|  | [VS-127](VS-127-sales-operations-planning-integrated-business-planning/README.md) | Sales & Operations Planning (S&OP) & Integrated Business Planning | Gap analysis | 4 | 32 |
|  | [VS-131](VS-131-human-rights-responsible-supply-chain-due-diligence/README.md) | Human Rights, Modern Slavery & Responsible Supply Chain Due Diligence | Gap analysis | 3 | 24 |
|  | [VS-182](VS-182-b2b-bulk-project-custom-import-indent-sourcing-and-brokerage/README.md) | B2B Bulk-Project Custom Import (Indent Sourcing & Brokerage Operations) | Gap analysis | 3 | 24 |
| | | | **Subtotal** | **47** | **462** |
| Make & Move | [VS-04](VS-04-dc-warehouse/README.md) | DC & Warehouse Operations | Core | 3 | 45 |
|  | [VS-05](VS-05-inventory-lifecycle/README.md) | Inventory Lifecycle | Core | 3 | 35 |
|  | [VS-06](VS-06-logistics-fleet/README.md) | Logistics & Fleet | Core | 3 | 37 |
|  | [VS-32](VS-32-returns-reverse-logistics/README.md) | Returns & Reverse Logistics | Core | 3 | 23 |
|  | [VS-56](VS-56-third-party-delivery-partner/README.md) | Third-Party Delivery Partner Management | Expansion | 3 | 24 |
|  | [VS-61](VS-61-fuel-fleet-cost-management/README.md) | Fuel & Fleet Cost Management | Expansion | 3 | 24 |
|  | [VS-74](VS-74-contractor-jobsite-delivery/README.md) | Professional Contractor Job Site Delivery | Expansion | 3 | 24 |
|  | [VS-81](VS-81-cash-in-transit-vault-armored/README.md) | Cash-in-Transit, Vault & Armored Car Operations | Statutory | 3 | 24 |
|  | [VS-90](VS-90-damage-claims-freight-recovery/README.md) | Damage, Claims & Freight Recovery Management | Gap analysis | 3 | 24 |
|  | [VS-92](VS-92-kitting-bundling-build-to-order-assembly/README.md) | Kitting, Bundling & Build-to-Order Assembly Operations | Gap analysis | 3 | 24 |
|  | [VS-93](VS-93-dark-store-micro-fulfillment/README.md) | Dark Store & Micro-Fulfillment Operations | Gap analysis | 3 | 24 |
|  | [VS-110](VS-110-freight-procurement-carrier-management-and-freight-audit/README.md) | Freight Procurement, Carrier Management & Freight Audit | Gap analysis | 3 | 24 |
|  | [VS-111](VS-111-packaging-pallet-and-returnable-transport-item-management/README.md) | Packaging, Pallet & Returnable Transport Item (RTI) Management | Gap analysis | 3 | 24 |
|  | [VS-136](VS-136-supply-chain-network-design-multi-echelon-inventory-optimization-flow-engineering/README.md) | Supply Chain Network Design, Multi-Echelon Inventory Optimization & Flow Engineering | Gap analysis | 3 | 24 |
|  | [VS-143](VS-143-bulky-white-goods-delivery-installation-haul-away-and-recycling/README.md) | Bulky & White-Goods Delivery, Installation, Haul-Away & Recycling Operations | Gap analysis | 3 | 24 |
|  | [VS-155](VS-155-trade-in-buy-back-and-certified-pre-owned-product-resale/README.md) | Trade-In, Buy-Back & Certified Pre-Owned Product Resale | Gap analysis | 3 | 24 |
|  | [VS-180](VS-180-disaster-relief-supply-chain-logistics-and-humanitarian-aid-coordination/README.md) | Disaster Relief Supply Chain Logistics & Humanitarian Aid Coordination | Gap analysis | 3 | 24 |
|  | [VS-191](VS-191-customer-construction-debris-demolition-waste-and-site-cleanup-operations/README.md) | Customer Construction Debris, Demolition Waste & Site Cleanup Operations | Gap analysis | 3 | 24 |
|  | [VS-192](VS-192-green-fleet-transition-electric-vehicle-fleet-operations-and-sustainable-transportation/README.md) | Green Fleet Transition, EV Fleet Operations & Sustainable Transportation | Gap analysis | 3 | 24 |
| | | | **Subtotal** | **57** | **500** |
| Sell & Serve | [VS-07](VS-07-store-operations/README.md) | Store Operations | Core | 4 | 151 |
|  | [VS-08](VS-08-pos-checkout/README.md) | POS & Checkout | Core | 3 | 61 |
|  | [VS-09](VS-09-in-store-services/README.md) | In-Store Customer Services | Core | 3 | 158 |
|  | [VS-10](VS-10-ecommerce-digital/README.md) | Ecommerce & Digital Channels | Core | 3 | 63 |
|  | [VS-11](VS-11-trade-project-wholesale/README.md) | Trade, Project & Wholesale | Core | 3 | 52 |
|  | [VS-12](VS-12-installation-services/README.md) | Installation & Services | Core | 3 | 40 |
|  | [VS-13](VS-13-customer-experience/README.md) | Customer Experience & Loyalty | Core | 3 | 64 |
|  | [VS-14](VS-14-marketing/README.md) | Marketing & Communications | Core | 3 | 42 |
|  | [VS-37](VS-37-store-opening-commissioning/README.md) | Store Opening & Commissioning | Core | 3 | 26 |
|  | [VS-43](VS-43-trade-professional-program/README.md) | Trade Professional Program & Contractor Services | Core | 3 | 24 |
|  | [VS-44](VS-44-consumer-insights-market-research/README.md) | Consumer Insights & Market Research | Core | 3 | 24 |
|  | [VS-46](VS-46-government-institutional-sales/README.md) | Government & Institutional B2G Sales | Core | 3 | 24 |
|  | [VS-47](VS-47-subscription-recurring-services/README.md) | Subscription & Recurring Home Services | Core | 3 | 24 |
|  | [VS-48](VS-48-retail-media-network/README.md) | Retail Media Network & Vendor Advertising | Core | 3 | 24 |
|  | [VS-53](VS-53-warranty-guarantee-management/README.md) | Warranty & Guarantee Management | Expansion | 3 | 24 |
|  | [VS-55](VS-55-store-planogram-space-optimization/README.md) | Store Planogram & Space Optimization | Expansion | 3 | 24 |
|  | [VS-58](VS-58-coupon-digital-promotions/README.md) | Coupon & Digital Promotions Management | Expansion | 3 | 24 |
|  | [VS-60](VS-60-omnichannel-order-routing/README.md) | Omnichannel Order Routing & Fulfillment Orchestration | Expansion | 3 | 24 |
|  | [VS-62](VS-62-product-sample-display-management/README.md) | Product Sample & Display Management | Expansion | 3 | 24 |
|  | [VS-63](VS-63-store-communication-task-management/README.md) | Store Communication & Task Management | Expansion | 3 | 24 |
|  | [VS-65](VS-65-ecommerce-marketplace-integration/README.md) | E-Commerce Marketplace Integration | Expansion | 3 | 24 |
|  | [VS-66](VS-66-customer-project-design-services/README.md) | Customer Project & Design Services | Expansion | 3 | 24 |
|  | [VS-70](VS-70-solar-renewable-energy/README.md) | Solar & Renewable Energy Product Operations | Expansion | 3 | 24 |
|  | [VS-75](VS-75-digital-engagement-app/README.md) | Customer Digital Engagement & Mobile App Operations | Expansion | 3 | 25 |
|  | [VS-77](VS-77-construction-material-staging/README.md) | Construction Project Material Staging & Phased Delivery | Expansion | 3 | 24 |
|  | [VS-78](VS-78-green-building-advisory/README.md) | Green Building & Sustainable Product Advisory | Expansion | 3 | 24 |
|  | [VS-82](VS-82-sari-sari-msme-micro-wholesale/README.md) | Sari-Sari Store & MSME Micro-Wholesale Program | Statutory | 3 | 24 |
|  | [VS-95](VS-95-marketplace-operator-third-party-seller/README.md) | Marketplace Operator & Third-Party Seller Management | Gap analysis | 3 | 24 |
|  | [VS-107](VS-107-strategic-key-account-enterprise-customer-management/README.md) | Strategic Key Account & Enterprise Customer Management | Gap analysis | 3 | 24 |
|  | [VS-124](VS-124-sales-enablement-product-knowledge-clienteling/README.md) | Sales Enablement, Product Knowledge Mastery & Clienteling | Gap analysis | 3 | 24 |
|  | [VS-139](VS-139-trade-show-exhibition-and-field-event-marketing/README.md) | Trade Show, Exhibition & Field Event Marketing | Gap analysis | 3 | 24 |
|  | [VS-140](VS-140-field-sales-outside-sales-and-route-to-market-force-management/README.md) | Field Sales, Outside Sales & Route-to-Market Force Management | Gap analysis | 3 | 24 |
|  | [VS-145](VS-145-garden-center-live-goods-and-plant-nursery/README.md) | Garden Center, Live Goods & Plant Nursery Operations | Gap analysis | 3 | 24 |
|  | [VS-149](VS-149-self-checkout-scan-and-go-and-unattended-retail-technology-operations/README.md) | Self-Checkout, Scan-&-Go & Unattended Retail Technology Operations | Gap analysis | 3 | 24 |
|  | [VS-156](VS-156-in-store-value-added-services-and-financial-agency-operations/README.md) | In-Store Value-Added Services & Financial Agency Operations | Gap analysis | 3 | 24 |
|  | [VS-162](VS-162-customer-pickup-truck-and-cargo-van-rental/README.md) | Customer Pickup Truck & Cargo Van Rental (Self-Haul) Operations | Gap analysis | 3 | 24 |
|  | [VS-164](VS-164-smart-locker-and-automated-parcel-collection-network/README.md) | Smart Locker & Automated Parcel Collection Network | Gap analysis | 3 | 24 |
|  | [VS-168](VS-168-in-store-audio-ambient-media-and-music-royalty-licensing/README.md) | In-Store Audio, Ambient Media & Music Royalty Licensing | Gap analysis | 3 | 24 |
|  | [VS-171](VS-171-customer-pickup-loading-zone-and-will-call-counter-operations/README.md) | Customer Pickup, Loading Zone & Will-Call Counter Operations | Gap analysis | 3 | 24 |
|  | [VS-172](VS-172-third-party-installer-and-contractor-network-pro-referral-management/README.md) | Third-Party Installer & Contractor Network (Pro-Referral) Management | Gap analysis | 3 | 24 |
|  | [VS-174](VS-174-self-storage-portable-container-and-mobile-storage-operations/README.md) | Self-Storage, Portable Container & Mobile-Storage Operations | Gap analysis | 3 | 24 |
|  | [VS-175](VS-175-propane-lpg-cylinder-exchange-and-gas-refill-operations/README.md) | Propane, LPG Cylinder Exchange & Gas Refill Operations | Gap analysis | 3 | 24 |
|  | [VS-176](VS-176-blueprint-reprographics-and-large-format-plan-printing-services/README.md) | Blueprint, Reprographics & Large-Format Plan Printing Services | Gap analysis | 3 | 24 |
|  | [VS-177](VS-177-field-retail-operations-regional-district-management-and-multi-store-execution/README.md) | Field Retail Operations, Regional/District Management & Multi-Store Retail Execution Network | Gap analysis | 3 | 24 |
|  | [VS-185](VS-185-b2b-cooperative-credit-and-procurement-partnerships/README.md) | B2B Cooperative Credit & Procurement Partnerships | Gap analysis | 3 | 24 |
|  | [VS-186](VS-186-compact-and-heavy-construction-equipment-rental-fleet-operations/README.md) | Compact & Heavy Construction Equipment Rental Fleet Operations | Gap analysis | 3 | 24 |
| | | | **Subtotal** | **139** | **1546** |
| Finance | [VS-15](VS-15-procure-to-pay/README.md) | Procure-to-Pay | Core | 2 | 43 |
|  | [VS-16](VS-16-order-to-cash/README.md) | Order-to-Cash | Core | 3 | 31 |
|  | [VS-17](VS-17-record-to-report/README.md) | Record-to-Report | Core | 4 | 70 |
|  | [VS-18](VS-18-treasury-cash/README.md) | Treasury & Cash | Core | 3 | 35 |
|  | [VS-34](VS-34-expense-procurement/README.md) | Expense & Non-Merchandise Procurement | Core | 3 | 22 |
|  | [VS-38](VS-38-consumer-credit-financing/README.md) | Consumer Credit & Financing | Core | 3 | 24 |
|  | [VS-39](VS-39-vendor-rebate-incentive/README.md) | Vendor Rebate & Incentive Management | Core | 3 | 24 |
|  | [VS-40](VS-40-capex-project-accounting/README.md) | Capex & Project Accounting | Core | 3 | 24 |
|  | [VS-54](VS-54-gift-card-stored-value/README.md) | Gift Card & Stored Value Management | Expansion | 3 | 26 |
|  | [VS-68](VS-68-trade-credit-risk-management/README.md) | Trade Credit Insurance & Risk Management | Expansion | 3 | 24 |
|  | [VS-72](VS-72-cross-entity-shared-services/README.md) | Cross-Entity Shared Services & Chargeback | Expansion | 3 | 24 |
|  | [VS-79](VS-79-tax-management-bir-reporting/README.md) | Tax Management & BIR Statutory Reporting | Statutory | 3 | 28 |
|  | [VS-80](VS-80-payment-operations-acquirer-settlement/README.md) | Payment Operations, Acquirer & Settlement Management | Statutory | 3 | 24 |
|  | [VS-96](VS-96-equipment-leasing-capital-equipment-finance/README.md) | Equipment Leasing & Capital Equipment Finance | Gap analysis | 3 | 24 |
|  | [VS-105](VS-105-supply-chain-finance-working-capital-management/README.md) | Supply Chain Finance & Working Capital Management | Gap analysis | 3 | 25 |
|  | [VS-116](VS-116-performance-bond-surety-and-bank-guarantee-management/README.md) | Performance Bond, Surety & Bank Guarantee Management | Gap analysis | 3 | 24 |
|  | [VS-118](VS-118-revenue-assurance-pricing-integrity-and-leakage-management/README.md) | Revenue Assurance, Pricing Integrity & Leakage Management | Gap analysis | 3 | 25 |
|  | [VS-125](VS-125-cross-channel-fraud-management-payment-fraud-protection/README.md) | Cross-Channel Fraud Management & Payment Fraud Protection | Gap analysis | 3 | 24 |
|  | [VS-142](VS-142-cash-on-delivery-operations-driver-cash-handling-and-reconciliation/README.md) | Cash-on-Delivery (COD) Operations, Driver Cash Handling & Reconciliation | Gap analysis | 3 | 24 |
|  | [VS-148](VS-148-lease-accounting-pfrs-16-and-right-of-use-asset-management/README.md) | Lease Accounting (PFRS 16/IFRS 16) & Right-of-Use Asset Management | Gap analysis | 3 | 24 |
|  | [VS-153](VS-153-captive-insurance-reinsurance-and-enterprise-risk-financing/README.md) | Captive Insurance, Reinsurance & Enterprise Risk Financing | Gap analysis | 3 | 24 |
|  | [VS-154](VS-154-home-construction-finance-loan-brokerage-and-mortgage-referral/README.md) | Home Construction Finance, Loan Brokerage & Mortgage Referral Services | Gap analysis | 3 | 24 |
|  | [VS-157](VS-157-revenue-recognition-pfrs-15-and-complex-contract-accounting/README.md) | Revenue Recognition (PFRS 15) & Complex Contract Accounting | Gap analysis | 3 | 24 |
|  | [VS-158](VS-158-product-costing-landed-cost-and-cost-accounting/README.md) | Product Costing, Landed-Cost & Cost Accounting | Gap analysis | 3 | 24 |
|  | [VS-170](VS-170-inventory-pledge-asset-based-lending-and-trust-receipt-financing/README.md) | Inventory Pledge, Asset-Based Lending & Trust-Receipt (Warehouse-Receipt) Financing | Gap analysis | 3 | 24 |
|  | [VS-173](VS-173-investor-relations-capital-markets-and-securities-disclosure/README.md) | Investor Relations, Capital Markets & Securities Disclosure | Gap analysis | 3 | 24 |
|  | [VS-181](VS-181-b2b-project-financing-escrow-account-orchestration-and-lien-release/README.md) | B2B Project Financing, Escrow Account Orchestration & Lien Release | Gap analysis | 3 | 24 |
|  | [VS-188](VS-188-trade-reseller-floor-plan-and-dealer-inventory-financing/README.md) | Trade Reseller Floor-Plan & Dealer Inventory Financing | Gap analysis | 3 | 24 |
|  | [VS-189](VS-189-trade-receivables-factoring-invoice-discounting-and-securitization/README.md) | Trade Accounts Receivable Factoring, Invoice Discounting & Receivables Securitization | Gap analysis | 3 | 24 |
| | | | **Subtotal** | **87** | **785** |
| People | [VS-19](VS-19-hire-to-retire/README.md) | Hire-to-Retire | Core | 5 | 81 |
|  | [VS-83](VS-83-occupational-health-clinic-wellness/README.md) | Occupational Health, Safety Clinic & Employee Wellness | Statutory | 3 | 25 |
|  | [VS-84](VS-84-labor-relations-collective-bargaining/README.md) | Labor Relations & Collective Bargaining Management | Statutory | 3 | 25 |
|  | [VS-98](VS-98-contingent-contract-outsourced-workforce/README.md) | Contingent, Contract & Outsourced Workforce Management | Gap analysis | 3 | 24 |
|  | [VS-102](VS-102-compensation-benefits-total-rewards/README.md) | Compensation, Benefits & Total Rewards Strategy | Gap analysis | 3 | 24 |
|  | [VS-103](VS-103-hr-shared-services-employee-experience-people-analytics/README.md) | HR Shared Services, Employee Experience & People Analytics | Gap analysis | 3 | 24 |
|  | [VS-121](VS-121-talent-acquisition-employer-brand-candidate-experience/README.md) | Talent Acquisition, Employer Brand & Candidate Experience | Gap analysis | 3 | 25 |
|  | [VS-123](VS-123-skilled-trade-apprenticeship-vocational-education-capability-pipeline/README.md) | Skilled-Trade Apprenticeship, Vocational Education & Capability Pipeline | Gap analysis | 3 | 24 |
|  | [VS-134](VS-134-organizational-change-management-digital-adoption-transformation-enablement/README.md) | Organizational Change Management, Digital Adoption & Transformation Enablement | Gap analysis | 3 | 24 |
|  | [VS-141](VS-141-employee-transport-shuttle-and-daily-commute-management/README.md) | Employee Transport, Shuttle & Daily Commute Management | Gap analysis | 3 | 25 |
|  | [VS-144](VS-144-employee-accommodation-dormitory-and-staff-housing/README.md) | Employee Accommodation, Dormitory & Staff Housing Operations | Gap analysis | 3 | 24 |
|  | [VS-150](VS-150-drug-free-workplace-and-substance-abuse-program/README.md) | Drug-Free Workplace & Substance Abuse Program | Gap analysis | 3 | 24 |
|  | [VS-160](VS-160-global-mobility-immigration-and-foreign-worker-compliance/README.md) | Global Mobility, Immigration & Foreign Worker Compliance | Gap analysis | 3 | 24 |
|  | [VS-167](VS-167-workforce-background-screening-credentialing-and-personnel-vetting/README.md) | Workforce Background Screening, Credentialing & Personnel Vetting | Gap analysis | 3 | 24 |
|  | [VS-169](VS-169-employee-uniform-workwear-and-ppe-issuance-program/README.md) | Employee Uniform, Workwear & PPE-Issuance Program | Gap analysis | 3 | 24 |
|  | [VS-183](VS-183-dual-training-system-dts-and-tesda-partnership-program/README.md) | Dual Training System (DTS) & TESDA Partnership Program | Gap analysis | 3 | 24 |
| | | | **Subtotal** | **50** | **445** |
| Asset & Infrastructure | [VS-20](VS-20-real-estate-construction/README.md) | Real Estate & Construction | Core | 3 | 33 |
|  | [VS-35](VS-35-fixed-asset-management/README.md) | Fixed Asset Management | Core | 3 | 24 |
|  | [VS-42](VS-42-property-lease-admin/README.md) | Property & Lease Administration | Core | 3 | 25 |
|  | [VS-59](VS-59-store-closure-decommissioning/README.md) | Store Closure & Decommissioning | Expansion | 3 | 24 |
|  | [VS-97](VS-97-corporate-real-estate-property-portfolio/README.md) | Corporate Real Estate & Property Portfolio Management | Gap analysis | 3 | 24 |
|  | [VS-108](VS-108-onsite-renewable-energy-prosumer-asset-operations/README.md) | On-Site Renewable Energy & Prosumer Asset Operations | Gap analysis | 3 | 24 |
|  | [VS-109](VS-109-store-remodel-renovation-lifecycle-refurbishment/README.md) | Store Remodel, Renovation & Lifecycle Refurbishment Program | Gap analysis | 3 | 24 |
|  | [VS-112](VS-112-corporate-project-and-program-management-office/README.md) | Corporate Project & Program Management Office (PMO) | Gap analysis | 3 | 24 |
|  | [VS-120](VS-120-energy-efficiency-conservation-and-ra-11285-compliance-program/README.md) | Energy Efficiency, Conservation & RA 11285 Compliance Program | Gap analysis | 3 | 24 |
|  | [VS-138](VS-138-integrated-facilities-management-workplace-services-and-building-automation/README.md) | Integrated Facilities Management, Workplace Services & Building Automation | Gap analysis | 3 | 24 |
|  | [VS-163](VS-163-electric-vehicle-ev-charging-station-host-network-operations/README.md) | Electric Vehicle (EV) Charging Station Host Network Operations | Gap analysis | 3 | 24 |
|  | [VS-178](VS-178-landbanking-site-acquisition-and-agrarian-lgu-zoning-conversion/README.md) | Landbanking, Site Acquisition & Agrarian/LGU Zoning Conversion Operations | Gap analysis | 3 | 25 |
|  | [VS-184](VS-184-post-disaster-store-infrastructure-reconstruction-and-rehabilitation/README.md) | Post-Disaster Store Infrastructure Reconstruction & Rehabilitation | Gap analysis | 3 | 24 |
| | | | **Subtotal** | **39** | **323** |
| Governance & Assurance | [VS-21](VS-21-internal-audit-risk/README.md) | Internal Audit & Risk | Core | 3 | 49 |
|  | [VS-22](VS-22-compliance-regulatory/README.md) | Compliance & Regulatory | Core | 3 | 57 |
|  | [VS-23](VS-23-loss-prevention/README.md) | Loss Prevention & Asset Protection | Core | 3 | 29 |
|  | [VS-24](VS-24-health-safety-environment/README.md) | Health, Safety & Environment | Core | 3 | 31 |
|  | [VS-25](VS-25-esg-sustainability/README.md) | ESG & Sustainability | Core | 3 | 31 |
|  | [VS-26](VS-26-business-continuity-insurance/README.md) | Business Continuity & Insurance | Core | 3 | 31 |
|  | [VS-31](VS-31-quality-management/README.md) | Quality Management & Product Compliance | Core | 3 | 23 |
|  | [VS-33](VS-33-strategic-planning/README.md) | Strategic Planning & Corporate Performance Management | Core | 3 | 23 |
|  | [VS-36](VS-36-corporate-governance/README.md) | Corporate Governance & Board Management | Core | 3 | 25 |
|  | [VS-69](VS-69-typhoon-disaster-response/README.md) | Typhoon & Natural Disaster Preparedness & Response | Expansion | 3 | 24 |
|  | [VS-71](VS-71-anti-counterfeit-authentication/README.md) | Anti-Counterfeit & Product Authentication | Expansion | 3 | 24 |
|  | [VS-73](VS-73-store-waste-circular-economy/README.md) | Store-Level Waste Management & Circular Economy | Expansion | 3 | 24 |
|  | [VS-76](VS-76-multi-region-lgu-compliance/README.md) | Philippine Multi-Region LGU & Local Regulatory Compliance | Expansion | 3 | 24 |
|  | [VS-85](VS-85-mandatory-discount-eligibility-tax-credit/README.md) | Mandatory Discount, Eligibility & Tax Credit Recovery | Statutory | 3 | 24 |
|  | [VS-86](VS-86-anti-financial-crime-aml-abc/README.md) | Anti-Financial Crime, AML/KYC & Anti-Corruption | Statutory | 3 | 24 |
|  | [VS-87](VS-87-customs-trade-compliance-tariff/README.md) | Customs Trade Compliance & Tariff Optimization | Statutory | 3 | 25 |
|  | [VS-88](VS-88-document-control-records-retention/README.md) | Document Control, Records Management & Retention | Statutory | 3 | 24 |
|  | [VS-89](VS-89-product-recall-safety-corrective-action/README.md) | Product Recall & Safety Corrective Action Management | Gap analysis | 3 | 25 |
|  | [VS-91](VS-91-consumer-data-privacy-protection/README.md) | Consumer Data Privacy & Data Protection Program | Gap analysis | 3 | 24 |
|  | [VS-100](VS-100-legal-operations-litigation-ip-management/README.md) | Legal Operations, Litigation & Intellectual Property Management | Gap analysis | 3 | 25 |
|  | [VS-104](VS-104-government-affairs-public-policy-industry-relations/README.md) | Government Affairs, Public Policy & Industry Relations | Gap analysis | 3 | 24 |
|  | [VS-114](VS-114-dangerous-goods-hazmat-transport-ecommerce-regulatory-compliance/README.md) | Dangerous Goods (DG) & Hazmat Transport, Ecommerce & Regulatory Compliance | Gap analysis | 3 | 24 |
|  | [VS-117](VS-117-dti-bps-product-standards-certification-ps-mark-icc-compliance/README.md) | DTI-BPS Product Standards Certification & PS Mark/ICC Compliance | Gap analysis | 3 | 24 |
|  | [VS-119](VS-119-whistleblower-ethics-and-corporate-integrity-speak-up-program/README.md) | Whistleblower, Ethics & Corporate Integrity (Speak-Up) Program | Gap analysis | 3 | 24 |
|  | [VS-129](VS-129-competition-and-antitrust-compliance/README.md) | Competition & Antitrust Compliance (RA 10667 / PCC) | Gap analysis | 3 | 24 |
|  | [VS-130](VS-130-corporate-development-ma-divestiture/README.md) | Corporate Development, Mergers, Acquisitions, Divestiture & Strategic Transactions | Gap analysis | 3 | 24 |
|  | [VS-132](VS-132-corporate-political-engagement-election-compliance/README.md) | Corporate Political Engagement, Election Compliance & Public Affairs Governance | Gap analysis | 3 | 24 |
|  | [VS-133](VS-133-operational-excellence-process-mining-continuous-improvement/README.md) | Operational Excellence, Process Mining & Continuous Improvement Program | Gap analysis | 3 | 24 |
|  | [VS-146](VS-146-customer-mystery-shopping-and-service-quality-assurance/README.md) | Customer Mystery Shopping & Service Quality Assurance Program | Gap analysis | 3 | 24 |
|  | [VS-147](VS-147-customer-safety-premises-liability-and-in-store-risk-management/README.md) | Customer Safety, Premises Liability & In-Store Risk Management | Gap analysis | 3 | 26 |
|  | [VS-152](VS-152-corporate-social-responsibility-foundation-and-community-investment/README.md) | Corporate Social Responsibility, Foundation & Community Investment | Gap analysis | 3 | 24 |
|  | [VS-159](VS-159-corporate-security-executive-protection-and-travel-risk-management/README.md) | Corporate Security, Executive Protection & Travel Risk Management | Gap analysis | 3 | 24 |
|  | [VS-161](VS-161-third-party-and-supplier-risk-management-tprm/README.md) | Third-Party & Supplier Risk Management (TPRM) | Gap analysis | 3 | 24 |
|  | [VS-165](VS-165-pcab-contractor-licensing-and-ra-4566-construction-contractor-compliance/README.md) | PCAB Contractor Licensing & RA 4566 Construction Contractor Compliance | Gap analysis | 3 | 24 |
|  | [VS-166](VS-166-regulatory-license-permit-and-accreditation-portfolio-management/README.md) | Regulatory License, Permit & Accreditation Portfolio Management | Gap analysis | 3 | 24 |
|  | [VS-179](VS-179-extended-producer-responsibility-compliance-and-plastic-recovery-network/README.md) | Extended Producer Responsibility (EPR) Compliance & Plastic Recovery Network | Gap analysis | 3 | 24 |
|  | [VS-187](VS-187-household-hazardous-waste-paint-and-product-stewardship-take-back/README.md) | Household Hazardous Waste, Paint & Used-Product Stewardship Take-Back Program | Gap analysis | 3 | 24 |
| | | | **Subtotal** | **111** | **976** |
| Technology & Data | [VS-27](VS-27-it-operations-security/README.md) | IT Operations & Security | Core | 3 | 71 |
|  | [VS-28](VS-28-data-analytics-bi/README.md) | Data, Analytics & BI | Core | 3 | 24 |
|  | [VS-29](VS-29-master-data/README.md) | Master Data Management | Core | 3 | 43 |
|  | [VS-30](VS-30-innovation-digital/README.md) | Innovation & Digital Transformation | Core | 3 | 29 |
|  | [VS-99](VS-99-it-asset-technology-lifecycle-management/README.md) | IT Asset & Technology Lifecycle Management | Gap analysis | 3 | 24 |
|  | [VS-113](VS-113-enterprise-architecture-application-portfolio-and-technology-strategy/README.md) | Enterprise Architecture, Application Portfolio & Technology Strategy | Gap analysis | 3 | 31 |
|  | [VS-115](VS-115-calibration-metrology-and-measurement-traceability-management/README.md) | Calibration, Metrology & Measurement Traceability Management | Gap analysis | 3 | 24 |
|  | [VS-126](VS-126-customer-data-platform-single-customer-view-identity-resolution/README.md) | Customer Data Platform, Single Customer View & Identity Resolution | Gap analysis | 3 | 24 |
|  | [VS-128](VS-128-ai-ml-governance-responsible-ai/README.md) | AI/ML Governance & Responsible AI | Gap analysis | 3 | 27 |
|  | [VS-135](VS-135-technology-business-management-it-financial-management-cloud-finops/README.md) | Technology Business Management, IT Financial Management & Cloud FinOps | Gap analysis | 3 | 24 |
|  | [VS-137](VS-137-product-information-management-and-digital-asset-management/README.md) | Product Information Management (PIM) & Digital Asset Management (DAM) | Gap analysis | 3 | 24 |
|  | [VS-151](VS-151-auto-id-barcode-rfid-labeling-and-eas-operations/README.md) | Auto-ID, Barcode, RFID, Price-Tag Labeling & EAS Operations | Gap analysis | 3 | 24 |
|  | [VS-190](VS-190-operational-technology-ot-ics-cybersecurity-and-retail-technology-asset-protection/README.md) | Operational Technology (OT) / ICS Cybersecurity & Retail Technology Asset Protection | Gap analysis | 3 | 24 |
| | | | **Subtotal** | **39** | **393** |
| | | | **Grand Total** | **569** | **5,430** |

---

## Detailed Value Stream Map

### Plan & Source

**[VS-01: Merchandise Strategy](./VS-01-merchandise-strategy/README.md)** (46 workflows)

- **PA-01.1** [Assortment Planning & Product Lifecycle](./VS-01-merchandise-strategy/PA-01.1-assortment-planning-and-product-lifecycle.md) — 22 workflows
- **PA-01.2** [Pricing & Promotions](./VS-01-merchandise-strategy/PA-01.2-pricing-and-promotions.md) — 16 workflows
- **PA-01.3** [Product Information & Content](./VS-01-merchandise-strategy/PA-01.3-product-information-and-content.md) — 8 workflows

**[VS-02: Supply Planning](./VS-02-supply-planning/README.md)** (38 workflows)

- **PA-02.1** [Demand Forecasting & S&OP](./VS-02-supply-planning/PA-02.1-demand-forecasting-and-sandop.md) — 14 workflows
- **PA-02.2** [Import & Customs Operations](./VS-02-supply-planning/PA-02.2-import-and-customs-operations.md) — 8 workflows
- **PA-02.3** [Supply Chain Orchestration & Risk](./VS-02-supply-planning/PA-02.3-supply-chain-orchestration-and-risk.md) — 16 workflows

**[VS-03: Vendor Management & Procurement](./VS-03-vendor-management/README.md)** (82 workflows)

- **PA-03.1** [Vendor Sourcing & Onboarding](./VS-03-vendor-management/PA-03.1-vendor-sourcing-and-onboarding.md) — 43 workflows
- **PA-03.2** [Purchase Order Cycle](./VS-03-vendor-management/PA-03.2-purchase-order-cycle.md) — 10 workflows
- **PA-03.3** [Vendor Performance & Contracts](./VS-03-vendor-management/PA-03.3-vendor-performance-and-contracts.md) — 12 workflows
- **PA-03.4** [Vendor Portal & Collaboration](./VS-03-vendor-management/PA-03.4-vendor-portal-and-collaboration.md) — 17 workflows

**[VS-41: Private Label & Exclusive Brand Management](./VS-41-private-label-brand/README.md)** (24 workflows)

- **PA-41.1** [Private Label Product Development & Sourcing](./VS-41-private-label-brand/PA-41.1-private-label-product-development.md) — 8 workflows
- **PA-41.2** [Private Label Quality Assurance & Compliance](./VS-41-private-label-brand/PA-41.2-private-label-quality-assurance.md) — 8 workflows
- **PA-41.3** [Private Label Brand, Packaging & Marketing](./VS-41-private-label-brand/PA-41.3-private-label-brand-marketing.md) — 8 workflows

**[VS-45: Consignment & Vendor-Managed Inventory Operations](./VS-45-consignment-vmi-operations/README.md)** (24 workflows)

- **PA-45.1** [Consignment Inventory Operations](./VS-45-consignment-vmi-operations/PA-45.1-consignment-inventory-operations.md) — 8 workflows
- **PA-45.2** [Vendor-Managed Inventory (VMI) Operations](./VS-45-consignment-vmi-operations/PA-45.2-vmi-operations.md) — 8 workflows
- **PA-45.3** [Consignment & VMI Settlement & Analytics](./VS-45-consignment-vmi-operations/PA-45.3-consignment-vmi-settlement-analytics.md) — 8 workflows

**[VS-57: Competitive Price Intelligence & Monitoring](./VS-57-competitive-price-intelligence/README.md)** (24 workflows)

- **PA-57.1** [Competitor Price Data Collection & Analysis](./VS-57-competitive-price-intelligence/PA-57.1-competitor-price-data-collection.md) — 8 workflows
- **PA-57.2** [Price Response Strategy & Execution](./VS-57-competitive-price-intelligence/PA-57.2-price-response-strategy.md) — 8 workflows
- **PA-57.3** [Pricing Analytics & Margin Optimization](./VS-57-competitive-price-intelligence/PA-57.3-pricing-analytics-margin-optimization.md) — 8 workflows

**[VS-64: Seasonal Merchandise Transition & Clearance](./VS-64-seasonal-merchandise-clearance/README.md)** (24 workflows)

- **PA-64.1** [Seasonal Planning & Phase-In Management](./VS-64-seasonal-merchandise-clearance/PA-64.1-seasonal-planning-phase-in.md) — 8 workflows
- **PA-64.2** [Markdown & Clearance Execution](./VS-64-seasonal-merchandise-clearance/PA-64.2-markdown-clearance-execution.md) — 8 workflows
- **PA-64.3** [Post-Season Analysis & Learning](./VS-64-seasonal-merchandise-clearance/PA-64.3-post-season-analysis-learning.md) — 8 workflows

**[VS-67: Vendor Scorecard & Performance Analytics](./VS-67-vendor-scorecard-analytics/README.md)** (24 workflows)

- **PA-67.1** [Vendor KPI Definition & Data Collection](./VS-67-vendor-scorecard-analytics/PA-67.1-vendor-kpi-data-collection.md) — 8 workflows
- **PA-67.2** [Vendor Performance Review & Rating](./VS-67-vendor-scorecard-analytics/PA-67.2-vendor-performance-review-rating.md) — 8 workflows
- **PA-67.3** [Vendor Development & Improvement Programs](./VS-67-vendor-scorecard-analytics/PA-67.3-vendor-development-improvement.md) — 8 workflows

**[VS-94: Cooperative & Community Enterprise Procurement](./VS-94-cooperative-community-enterprise-procurement/README.md)** (24 workflows)

- **PA-94.1** [Cooperative & Social Enterprise Sourcing Strategy & Onboarding](./VS-94-cooperative-community-enterprise-procurement/PA-94.1-cooperative-sourcing-strategy-onboarding.md) — 8 workflows
- **PA-94.2** [Cooperative Purchase Order, Logistics & Livelihood Settlement](./VS-94-cooperative-community-enterprise-procurement/PA-94.2-cooperative-po-logistics-settlement.md) — 8 workflows
- **PA-94.3** [Impact Measurement, Fair-Trade Compliance & Development Program](./VS-94-cooperative-community-enterprise-procurement/PA-94.3-impact-fairtrade-development-program.md) — 8 workflows

**[VS-101: Merchandise Financial Planning, OTB & Margin Management](./VS-101-merchandise-financial-planning-otb-margin-management/README.md)** (24 workflows)

- **PA-101.1** [Seasonal Merchandise Financial Planning & Open-to-Buy](./VS-101-merchandise-financial-planning-otb-margin-management/PA-101.1-seasonal-merchandise-financial-planning-and-open-to-buy.md) — 8 workflows
- **PA-101.2** [Inventory Investment, Turn & Productivity Planning](./VS-101-merchandise-financial-planning-otb-margin-management/PA-101.2-inventory-investment-turn-and-productivity-planning.md) — 8 workflows
- **PA-101.3** [Merchandise Performance Analytics & Margin Optimization](./VS-101-merchandise-financial-planning-otb-margin-management/PA-101.3-merchandise-performance-analytics-and-margin-optimization.md) — 8 workflows

**[VS-106: Commodity & Input-Cost Risk Management](./VS-106-commodity-input-cost-risk-management/README.md)** (24 workflows)

- **PA-106.1** [Commodity Exposure Identification & Market Intelligence](./VS-106-commodity-input-cost-risk-management/PA-106.1-commodity-exposure-identification-and-market-intelligence.md) — 8 workflows
- **PA-106.2** [Procurement Hedging, Forward Buying & Indexed-Pricing Strategy](./VS-106-commodity-input-cost-risk-management/PA-106.2-procurement-hedging-forward-buying-and-indexed-pricing.md) — 8 workflows
- **PA-106.3** [Input-Cost Pass-Through, Margin Protection & Risk Analytics](./VS-106-commodity-input-cost-risk-management/PA-106.3-input-cost-pass-through-margin-protection-and-risk-analytics.md) — 8 workflows

**[VS-122: Global Sourcing, Import Buying & Sourcing Agent Management](./VS-122-global-sourcing-import-buying-sourcing-agent-management/README.md)** (24 workflows)

- **PA-122.1** [Global Sourcing Strategy, Source-Market & Sourcing-Model Design](./VS-122-global-sourcing-import-buying-sourcing-agent-management/PA-122.1-global-sourcing-strategy-source-market-and-sourcing-model-design.md) — 8 workflows
- **PA-122.2** [Sourcing Agent, Overseas Buying Office & Import Vendor Management](./VS-122-global-sourcing-import-buying-sourcing-agent-management/PA-122.2-sourcing-agent-overseas-buying-office-and-import-vendor-management.md) — 8 workflows
- **PA-122.3** [Import Sourcing Performance, Consolidation & Total-Landed-Cost Analytics](./VS-122-global-sourcing-import-buying-sourcing-agent-management/PA-122.3-import-sourcing-performance-consolidation-and-total-landed-cost-analytics.md) — 8 workflows

**[VS-127: Sales & Operations Planning (S&OP) & Integrated Business Planning](./VS-127-sales-operations-planning-integrated-business-planning/README.md)** (32 workflows)

- **PA-127.1** [S&OP/IBP Framework, Demand Consensus & Forecasting](./VS-127-sales-operations-planning-integrated-business-planning/PA-127.1-sop-framework-demand-consensus-forecasting.md) — 8 workflows
- **PA-127.2** [Supply Reconciliation, Pre-S&OP & Scenario Planning](./VS-127-sales-operations-planning-integrated-business-planning/PA-127.2-supply-reconciliation-pre-sop-scenario-planning.md) — 8 workflows
- **PA-127.3** [IBP Financial Integration, Performance & Continuous Improvement](./VS-127-sales-operations-planning-integrated-business-planning/PA-127.3-ibp-financial-integration-performance-improvement.md) — 8 workflows
- **PA-127.4** [Calamity, Seasonality & Philippine-Retail Demand–Supply Dynamics](./VS-127-sales-operations-planning-integrated-business-planning/PA-127.4-calamity-seasonality-and-philippine-retail-demand-supply-dynamics.md) — 8 workflows

**[VS-131: Human Rights, Modern Slavery & Responsible Supply Chain Due Diligence](./VS-131-human-rights-responsible-supply-chain-due-diligence/README.md)** (24 workflows)

- **PA-131.1** [Human Rights Policy, Salient-Risk Identification & Due Diligence Framework](./VS-131-human-rights-responsible-supply-chain-due-diligence/PA-131.1-human-rights-policy-salient-risk-identification-and-due-diligence-framework.md) — 8 workflows
- **PA-131.2** [Supply Chain Human Rights Risk Assessment, Auditing & Remediation](./VS-131-human-rights-responsible-supply-chain-due-diligence/PA-131.2-supply-chain-human-rights-risk-assessment-auditing-and-remediation.md) — 8 workflows
- **PA-131.3** [Responsible Sourcing Governance, Reporting & Stakeholder Engagement](./VS-131-human-rights-responsible-supply-chain-due-diligence/PA-131.3-responsible-sourcing-governance-reporting-and-stakeholder-engagement.md) — 8 workflows

**[VS-182: B2B Bulk-Project Custom Import (Indent Sourcing & Brokerage Operations)](./VS-182-b2b-bulk-project-custom-import-indent-sourcing-and-brokerage/README.md)** (24 workflows)

- **PA-182.1** [Custom Project Sourcing Intake & Quotation](./VS-182-b2b-bulk-project-custom-import-indent-sourcing-and-brokerage/PA-182.1-custom-project-sourcing-intake-and-quotation.md) — 8 workflows
- **PA-182.2** [Indent Order Financing & LC Orchestration](./VS-182-b2b-bulk-project-custom-import-indent-sourcing-and-brokerage/PA-182.2-indent-order-financing-and-lc-orchestration.md) — 8 workflows
- **PA-182.3** [Direct Port-to-Jobsite Customs & Logistics](./VS-182-b2b-bulk-project-custom-import-indent-sourcing-and-brokerage/PA-182.3-direct-port-to-jobsite-customs-and-logistics.md) — 8 workflows

### Make & Move

**[VS-04: DC & Warehouse Operations](./VS-04-dc-warehouse/README.md)** (45 workflows)

- **PA-04.1** [DC Inbound Operations](./VS-04-dc-warehouse/PA-04.1-dc-inbound-operations.md) — 14 workflows
- **PA-04.2** [DC Outbound Operations](./VS-04-dc-warehouse/PA-04.2-dc-outbound-operations.md) — 10 workflows
- **PA-04.3** [DC Operations Management](./VS-04-dc-warehouse/PA-04.3-dc-operations-management.md) — 21 workflows

**[VS-05: Inventory Lifecycle](./VS-05-inventory-lifecycle/README.md)** (35 workflows)

- **PA-05.1** [Inventory Accuracy & Counting](./VS-05-inventory-lifecycle/PA-05.1-inventory-accuracy-and-counting.md) — 10 workflows
- **PA-05.2** [Stock Transfers & Rebalancing](./VS-05-inventory-lifecycle/PA-05.2-stock-transfers-and-rebalancing.md) — 10 workflows
- **PA-05.3** [Inventory Disposition & Optimization](./VS-05-inventory-lifecycle/PA-05.3-inventory-disposition-and-optimization.md) — 15 workflows

**[VS-06: Logistics & Fleet](./VS-06-logistics-fleet/README.md)** (37 workflows)

- **PA-06.1** [Outbound Distribution](./VS-06-logistics-fleet/PA-06.1-outbound-distribution.md) — 10 workflows
- **PA-06.2** [Fleet & Driver Management](./VS-06-logistics-fleet/PA-06.2-fleet-and-driver-management.md) — 15 workflows
- **PA-06.3** [Last-Mile & Delivery Partners](./VS-06-logistics-fleet/PA-06.3-last-mile-and-delivery-partners.md) — 12 workflows

**[VS-32: Returns & Reverse Logistics](./VS-32-returns-reverse-logistics/README.md)** (23 workflows)

- **PA-32.1** [Customer Returns Processing](./VS-32-returns-reverse-logistics/PA-32.1-customer-returns-processing.md) — 9 workflows
- **PA-32.2** [Vendor Returns & Recovery](./VS-32-returns-reverse-logistics/PA-32.2-vendor-returns-recovery.md) — 7 workflows
- **PA-32.3** [Reverse Logistics & Disposition](./VS-32-returns-reverse-logistics/PA-32.3-reverse-logistics-disposition.md) — 7 workflows

**[VS-56: Third-Party Delivery Partner Management](./VS-56-third-party-delivery-partner/README.md)** (24 workflows)

- **PA-56.1** [3PL Partner Onboarding & Qualification](./VS-56-third-party-delivery-partner/PA-56.1-3pl-partner-onboarding-qualification.md) — 8 workflows
- **PA-56.2** [Delivery Performance & SLA Management](./VS-56-third-party-delivery-partner/PA-56.2-delivery-performance-sla.md) — 8 workflows
- **PA-56.3** [3PL Settlement & Cost Optimization](./VS-56-third-party-delivery-partner/PA-56.3-3pl-settlement-cost-optimization.md) — 8 workflows

**[VS-61: Fuel & Fleet Cost Management](./VS-61-fuel-fleet-cost-management/README.md)** (24 workflows)

- **PA-61.1** [Fuel Procurement & Consumption Management](./VS-61-fuel-fleet-cost-management/PA-61.1-fuel-procurement-consumption.md) — 8 workflows
- **PA-61.2** [Toll, Parking & Route Cost Management](./VS-61-fuel-fleet-cost-management/PA-61.2-toll-route-cost.md) — 8 workflows
- **PA-61.3** [Fleet Total Cost of Ownership Analytics](./VS-61-fuel-fleet-cost-management/PA-61.3-fleet-total-cost-analytics.md) — 8 workflows

**[VS-74: Professional Contractor Job Site Delivery](./VS-74-contractor-jobsite-delivery/README.md)** (24 workflows)

- **PA-74.1** [Job Site Delivery Planning & Scheduling](./VS-74-contractor-jobsite-delivery/PA-74.1-jobsite-delivery-planning-scheduling.md) — 8 workflows
- **PA-74.2** [Job Site Delivery Execution & Material Handling](./VS-74-contractor-jobsite-delivery/PA-74.2-jobsite-delivery-execution-material-handling.md) — 8 workflows
- **PA-74.3** [Job Site Delivery Performance & Analytics](./VS-74-contractor-jobsite-delivery/PA-74.3-jobsite-delivery-performance-analytics.md) — 8 workflows

**[VS-81: Cash-in-Transit, Vault & Armored Car Operations](./VS-81-cash-in-transit-vault-armored/README.md)** (24 workflows)

- **PA-81.1** [Store Cash Office, Smart Safe & Pickup Planning](./VS-81-cash-in-transit-vault-armored/PA-81.1-store-cash-office-smart-safe-pickup.md) — 8 workflows
- **PA-81.2** [Armored Car, Vault & Cash Logistics Execution](./VS-81-cash-in-transit-vault-armored/PA-81.2-armored-car-vault-cash-execution.md) — 8 workflows
- **PA-81.3** [CIT Risk, Insurance & Cash Analytics](./VS-81-cash-in-transit-vault-armored/PA-81.3-cit-risk-insurance-analytics.md) — 8 workflows

**[VS-90: Damage, Claims & Freight Recovery Management](./VS-90-damage-claims-freight-recovery/README.md)** (24 workflows)

- **PA-90.1** [Damage Identification, Documentation & Disposition](./VS-90-damage-claims-freight-recovery/PA-90.1-damage-identification-documentation-disposition.md) — 8 workflows
- **PA-90.2** [Vendor, Carrier & Freight Claims Filing & Resolution](./VS-90-damage-claims-freight-recovery/PA-90.2-vendor-carrier-freight-claims-filing-resolution.md) — 8 workflows
- **PA-90.3** [Customer Damage/Shortage Claims & Recovery Analytics](./VS-90-damage-claims-freight-recovery/PA-90.3-customer-damage-claims-recovery-analytics.md) — 8 workflows

**[VS-92: Kitting, Bundling & Build-to-Order Assembly Operations](./VS-92-kitting-bundling-build-to-order-assembly/README.md)** (24 workflows)

- **PA-92.1** [Kit & Bundle Definition, BOM & Build Planning](./VS-92-kitting-bundling-build-to-order-assembly/PA-92.1-kit-bundle-definition-bom-build-planning.md) — 8 workflows
- **PA-92.2** [Kit Assembly, Build Execution & Inventory Management](./VS-92-kitting-bundling-build-to-order-assembly/PA-92.2-kit-assembly-build-execution-inventory.md) — 8 workflows
- **PA-92.3** [Bundle Pricing, Promotion & Performance Analytics](./VS-92-kitting-bundling-build-to-order-assembly/PA-92.3-bundle-pricing-promotion-performance-analytics.md) — 8 workflows

**[VS-93: Dark Store & Micro-Fulfillment Operations](./VS-93-dark-store-micro-fulfillment/README.md)** (24 workflows)

- **PA-93.1** [Dark Store Site Strategy, Design & Network Planning](./VS-93-dark-store-micro-fulfillment/PA-93.1-dark-store-site-strategy-design-network.md) — 8 workflows
- **PA-93.2** [Micro-Fulfillment Daily Pick / Pack / Dispatch Operations](./VS-93-dark-store-micro-fulfillment/PA-93.2-micro-fulfillment-daily-pick-pack-dispatch.md) — 8 workflows
- **PA-93.3** [Dark Store Inventory, Capacity & Performance Analytics](./VS-93-dark-store-micro-fulfillment/PA-93.3-dark-store-inventory-capacity-analytics.md) — 8 workflows

**[VS-110: Freight Procurement, Carrier Management & Freight Audit](./VS-110-freight-procurement-carrier-management-and-freight-audit/README.md)** (24 workflows)

- **PA-110.1** [Freight Sourcing, Carrier Contracting & Rate Management](./VS-110-freight-procurement-carrier-management-and-freight-audit/PA-110.1-freight-sourcing-carrier-contracting-and-rate-management.md) — 8 workflows
- **PA-110.2** [Freight Execution, Routing Guide & Visibility](./VS-110-freight-procurement-carrier-management-and-freight-audit/PA-110.2-freight-execution-routing-guide-and-visibility.md) — 8 workflows
- **PA-110.3** [Freight Audit, Payment & Freight Cost Analytics](./VS-110-freight-procurement-carrier-management-and-freight-audit/PA-110.3-freight-audit-payment-and-freight-cost-analytics.md) — 8 workflows

**[VS-111: Packaging, Pallet & Returnable Transport Item (RTI) Management](./VS-111-packaging-pallet-and-returnable-transport-item-management/README.md)** (24 workflows)

- **PA-111.1** [Packaging Engineering, Specification & Procurement](./VS-111-packaging-pallet-and-returnable-transport-item-management/PA-111.1-packaging-engineering-specification-and-procurement.md) — 8 workflows
- **PA-111.2** [Pallet & RTI Pool, Tracking & Reconciliation](./VS-111-packaging-pallet-and-returnable-transport-item-management/PA-111.2-pallet-and-rti-pool-tracking-and-reconciliation.md) — 8 workflows
- **PA-111.3** [Packaging Sustainability, Compliance & Cost Analytics](./VS-111-packaging-pallet-and-returnable-transport-item-management/PA-111.3-packaging-sustainability-compliance-and-cost-analytics.md) — 8 workflows

**[VS-136: Supply Chain Network Design, Multi-Echelon Inventory Optimization & Flow Engineering](./VS-136-supply-chain-network-design-multi-echelon-inventory-optimization-flow-engineering/README.md)** (24 workflows)

- **PA-136.1** [Supply Chain Network Strategy, Modeling & Design](./VS-136-supply-chain-network-design-multi-echelon-inventory-optimization-flow-engineering/PA-136.1-supply-chain-network-strategy-modeling-and-design.md) — 8 workflows
- **PA-136.2** [Multi-Echelon Inventory Optimization & Service-Level Engineering](./VS-136-supply-chain-network-design-multi-echelon-inventory-optimization-flow-engineering/PA-136.2-multi-echelon-inventory-optimization-and-service-level-engineering.md) — 8 workflows
- **PA-136.3** [Network & Inventory Performance Analytics, Simulation & Continuous Re-Optimization](./VS-136-supply-chain-network-design-multi-echelon-inventory-optimization-flow-engineering/PA-136.3-network-and-inventory-performance-analytics-and-re-optimization.md) — 8 workflows

**[VS-143: Bulky & White-Goods Delivery, Installation, Haul-Away & Recycling Operations](./VS-143-bulky-white-goods-delivery-installation-haul-away-and-recycling/README.md)** (24 workflows)

- **PA-143.1** [Bulky/White-Goods Delivery Network, Scheduling & Capacity](./VS-143-bulky-white-goods-delivery-installation-haul-away-and-recycling/PA-143.1-bulky-delivery-network-scheduling-and-capacity.md) — 8 workflows
- **PA-143.2** [Delivery Execution, Installation & In-Home Service Operations](./VS-143-bulky-white-goods-delivery-installation-haul-away-and-recycling/PA-143.2-delivery-execution-installation-and-in-home-service.md) — 8 workflows
- **PA-143.3** [Haul-Away, Old-Unit Recycling, Reverse Logistics & Analytics](./VS-143-bulky-white-goods-delivery-installation-haul-away-and-recycling/PA-143.3-haul-away-old-unit-recycling-reverse-logistics-and-analytics.md) — 8 workflows


**[VS-180: Disaster Relief Supply Chain Logistics & Humanitarian Aid Coordination](./VS-180-disaster-relief-supply-chain-logistics-and-humanitarian-aid-coordination/README.md)** (24 workflows)

- **PA-180.1** [Emergency Material Allocation, Disaster Kit Assembly & Staging Operations](./VS-180-disaster-relief-supply-chain-logistics-and-humanitarian-aid-coordination/PA-180.1-emergency-material-allocation-disaster-kit-assembly-staging-operations.md) — 8 workflows
- **PA-180.2** [Price Freeze Governance, State of Calamity Controls & Regulatory Reporting](./VS-180-disaster-relief-supply-chain-logistics-and-humanitarian-aid-coordination/PA-180.2-price-freeze-governance-state-of-calamity-controls-regulatory-reporting.md) — 8 workflows
- **PA-180.3** [Priority Relief Routing, LGU Coordination & Humanitarian Partner Logistics](./VS-180-disaster-relief-supply-chain-logistics-and-humanitarian-aid-coordination/PA-180.3-priority-relief-routing-lgu-coordination-humanitarian-partner-logistics.md) — 8 workflows

**[VS-191: Customer Construction Debris, Demolition Waste & Site Cleanup Operations](./VS-191-customer-construction-debris-demolition-waste-and-site-cleanup-operations/README.md)** (24 workflows)

- **PA-191.1** [Site Cleanup Service Design, Estimation & Crew Scheduling](./VS-191-customer-construction-debris-demolition-waste-and-site-cleanup-operations/PA-191.1-site-cleanup-service-design-estimation-and-crew-scheduling.md) — 8 workflows
- **PA-191.2** [Debris Collection, Segregation & DENR-Compliant Hauling Execution](./VS-191-customer-construction-debris-demolition-waste-and-site-cleanup-operations/PA-191.2-debris-collection-segregation-and-denr-compliant-hauling-execution.md) — 8 workflows
- **PA-191.3** [Diversion, Disposal, Settlement & Site Cleanup Analytics](./VS-191-customer-construction-debris-demolition-waste-and-site-cleanup-operations/PA-191.3-diversion-disposal-settlement-and-site-cleanup-analytics.md) — 8 workflows

**[VS-192: Green Fleet Transition, EV Fleet Operations & Sustainable Transportation](./VS-192-green-fleet-transition-electric-vehicle-fleet-operations-and-sustainable-transportation/README.md)** (24 workflows)

- **PA-192.1** [Green Fleet Strategy, Electrification Roadmap & Capital Planning](./VS-192-green-fleet-transition-electric-vehicle-fleet-operations-and-sustainable-transportation/PA-192.1-green-fleet-strategy-electrification-roadmap-and-capital-planning.md) — 8 workflows
- **PA-192.2** [EV / Alt-Fuel Fleet Operations, Charging & Energy Management](./VS-192-green-fleet-transition-electric-vehicle-fleet-operations-and-sustainable-transportation/PA-192.2-ev-alt-fuel-fleet-operations-charging-and-energy-management.md) — 8 workflows
- **PA-192.3** [Green Fleet Performance, Compliance, Safety & Analytics](./VS-192-green-fleet-transition-electric-vehicle-fleet-operations-and-sustainable-transportation/PA-192.3-green-fleet-performance-compliance-safety-and-analytics.md) — 8 workflows

**[VS-155: Trade-In, Buy-Back & Certified Pre-Owned Product Resale](./VS-155-trade-in-buy-back-and-certified-pre-owned-product-resale/README.md)** (24 workflows)

- **PA-155.1** [Trade-In/Buy-Back Program Design, Valuation & Pricing](./VS-155-trade-in-buy-back-and-certified-pre-owned-product-resale/PA-155.1-tradein-buyback-program-design-valuation-and-pricing.md) — 8 workflows
- **PA-155.2** [Take-Back, Inspection, Refurbishment & Certification](./VS-155-trade-in-buy-back-and-certified-pre-owned-product-resale/PA-155.2-takeback-inspection-refurbishment-and-certification.md) — 8 workflows
- **PA-155.3** [Resale Listing, Fulfillment, Warranty & Analytics](./VS-155-trade-in-buy-back-and-certified-pre-owned-product-resale/PA-155.3-resale-listing-fulfillment-warranty-and-analytics.md) — 8 workflows

### Sell & Serve

**[VS-07: Store Operations](./VS-07-store-operations/README.md)** (151 workflows)

- **PA-07.1** [Store Daily Management](./VS-07-store-operations/PA-07.1-store-daily-management.md) — 64 workflows
- **PA-07.2** [Store Facility & Safety](./VS-07-store-operations/PA-07.2-store-facility-and-safety.md) — 49 workflows
- **PA-07.3** [Store Receiving & Replenishment](./VS-07-store-operations/PA-07.3-store-receiving-and-replenishment.md) — 28 workflows
- **PA-07.4** [Store Staffing & People](./VS-07-store-operations/PA-07.4-store-staffing-and-people.md) — 10 workflows

**[VS-08: POS & Checkout](./VS-08-pos-checkout/README.md)** (61 workflows)

- **PA-08.1** [Transaction Processing](./VS-08-pos-checkout/PA-08.1-transaction-processing.md) — 38 workflows
- **PA-08.2** [Payment & Cash Management](./VS-08-pos-checkout/PA-08.2-payment-and-cash-management.md) — 11 workflows
- **PA-08.3** [POS Compliance & Controls](./VS-08-pos-checkout/PA-08.3-pos-compliance-and-controls.md) — 12 workflows

**[VS-09: In-Store Customer Services](./VS-09-in-store-services/README.md)** (158 workflows)

- **PA-09.1** [Custom Fabrication & Processing](./VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md) — 65 workflows
- **PA-09.2** [Project Estimation & Advisory](./VS-09-in-store-services/PA-09.2-project-estimation-and-advisory.md) — 75 workflows
- **PA-09.3** [Customer Amenities & Assistance](./VS-09-in-store-services/PA-09.3-customer-amenities-and-assistance.md) — 18 workflows

**[VS-10: Ecommerce & Digital Channels](./VS-10-ecommerce-digital/README.md)** (63 workflows)

- **PA-10.1** [Ecommerce Platform Operations](./VS-10-ecommerce-digital/PA-10.1-ecommerce-platform-operations.md) — 32 workflows
- **PA-10.2** [Order Fulfillment & Delivery](./VS-10-ecommerce-digital/PA-10.2-order-fulfillment-and-delivery.md) — 20 workflows
- **PA-10.3** [Marketplace & Social Commerce](./VS-10-ecommerce-digital/PA-10.3-marketplace-and-social-commerce.md) — 11 workflows

**[VS-11: Trade, Project & Wholesale](./VS-11-trade-project-wholesale/README.md)** (52 workflows)

- **PA-11.1** [Trade Account Management](./VS-11-trade-project-wholesale/PA-11.1-trade-account-management.md) — 10 workflows
- **PA-11.2** [Project Sales & B2B](./VS-11-trade-project-wholesale/PA-11.2-project-sales-and-b2b.md) — 32 workflows
- **PA-11.3** [Wholesale Operations](./VS-11-trade-project-wholesale/PA-11.3-wholesale-operations.md) — 10 workflows

**[VS-12: Installation & Services](./VS-12-installation-services/README.md)** (40 workflows)

- **PA-12.1** [Installation & Repair Services](./VS-12-installation-services/PA-12.1-installation-and-repair-services.md) — 20 workflows
- **PA-12.2** [Tool Rental & Equipment](./VS-12-installation-services/PA-12.2-tool-rental-and-equipment.md) — 10 workflows
- **PA-12.3** [Workshops & Events](./VS-12-installation-services/PA-12.3-workshops-and-events.md) — 10 workflows

**[VS-13: Customer Experience & Loyalty](./VS-13-customer-experience/README.md)** (64 workflows)

- **PA-13.1** [Customer Support & Complaints](./VS-13-customer-experience/PA-13.1-customer-support-and-complaints.md) — 32 workflows
- **PA-13.2** [Loyalty Program Operations](./VS-13-customer-experience/PA-13.2-loyalty-program-operations.md) — 19 workflows
- **PA-13.3** [Customer Data & CRM](./VS-13-customer-experience/PA-13.3-customer-data-and-crm.md) — 13 workflows

**[VS-14: Marketing & Communications](./VS-14-marketing/README.md)** (42 workflows)

- **PA-14.1** [Campaign Planning & Execution](./VS-14-marketing/PA-14.1-campaign-planning-and-execution.md) — 17 workflows
- **PA-14.2** [Digital Marketing & Social Media](./VS-14-marketing/PA-14.2-digital-marketing-and-social-media.md) — 13 workflows
- **PA-14.3** [Brand, PR & Corporate Communications](./VS-14-marketing/PA-14.3-brand-pr-and-corporate-communications.md) — 12 workflows

**[VS-37: Store Opening & Commissioning](./VS-37-store-opening-commissioning/README.md)** (26 workflows)

- **PA-37.1** [New Store Project Planning & Coordination](./VS-37-store-opening-commissioning/PA-37.1-new-store-project-planning.md) — 9 workflows
- **PA-37.2** [Store Staffing, Training & Systems Setup](./VS-37-store-opening-commissioning/PA-37.2-staffing-training-systems-setup.md) — 9 workflows
- **PA-37.3** [Grand Opening Execution & Post-Opening Stabilization](./VS-37-store-opening-commissioning/PA-37.3-grand-opening-post-opening.md) — 8 workflows

**[VS-43: Trade Professional Program & Contractor Services](./VS-43-trade-professional-program/README.md)** (24 workflows)

- **PA-43.1** [Trade Account Lifecycle & Relationship Management](./VS-43-trade-professional-program/PA-43.1-trade-account-lifecycle.md) — 8 workflows
- **PA-43.2** [Contractor Loyalty, Incentive & Volume Program](./VS-43-trade-professional-program/PA-43.2-contractor-loyalty-incentive.md) — 8 workflows
- **PA-43.3** [Trade Training, Certification & Community Engagement](./VS-43-trade-professional-program/PA-43.3-trade-training-community.md) — 8 workflows

**[VS-44: Consumer Insights & Market Research](./VS-44-consumer-insights-market-research/README.md)** (24 workflows)

- **PA-44.1** [Customer Satisfaction & Experience Research](./VS-44-consumer-insights-market-research/PA-44.1-customer-satisfaction-research.md) — 8 workflows
- **PA-44.2** [Market & Competitive Intelligence](./VS-44-consumer-insights-market-research/PA-44.2-market-competitive-intelligence.md) — 8 workflows
- **PA-44.3** [Product Category & Shopper Research](./VS-44-consumer-insights-market-research/PA-44.3-product-category-research.md) — 8 workflows

**[VS-46: Government & Institutional B2G Sales](./VS-46-government-institutional-sales/README.md)** (24 workflows)

- **PA-46.1** [Government Registration & Qualification](./VS-46-government-institutional-sales/PA-46.1-government-registration-qualification.md) — 8 workflows
- **PA-46.2** [Government Bid, Quotation & Order Processing](./VS-46-government-institutional-sales/PA-46.2-government-bid-order-processing.md) — 8 workflows
- **PA-46.3** [Government Billing, Collection & Compliance](./VS-46-government-institutional-sales/PA-46.3-government-billing-collection-compliance.md) — 8 workflows

**[VS-47: Subscription & Recurring Home Services](./VS-47-subscription-recurring-services/README.md)** (24 workflows)

- **PA-47.1** [Subscription Product Design & Setup](./VS-47-subscription-recurring-services/PA-47.1-subscription-product-design-setup.md) — 8 workflows
- **PA-47.2** [Subscription Billing, Renewal & Lifecycle](./VS-47-subscription-recurring-services/PA-47.2-subscription-billing-renewal-lifecycle.md) — 8 workflows
- **PA-47.3** [Service Fulfillment, Scheduling & Quality Assurance](./VS-47-subscription-recurring-services/PA-47.3-service-fulfillment-quality.md) — 8 workflows

**[VS-48: Retail Media Network & Vendor Advertising](./VS-48-retail-media-network/README.md)** (24 workflows)

- **PA-48.1** [Retail Media Platform & Inventory Management](./VS-48-retail-media-network/PA-48.1-retail-media-platform-inventory.md) — 8 workflows
- **PA-48.2** [Vendor Advertising Campaign Execution](./VS-48-retail-media-network/PA-48.2-vendor-advertising-campaign-execution.md) — 8 workflows
- **PA-48.3** [Retail Media Revenue & Analytics](./VS-48-retail-media-network/PA-48.3-retail-media-revenue-analytics.md) — 8 workflows

**[VS-53: Warranty & Guarantee Management](./VS-53-warranty-guarantee-management/README.md)** (24 workflows)

- **PA-53.1** [Product Warranty Registration & Activation](./VS-53-warranty-guarantee-management/PA-53.1-warranty-registration-activation.md) — 8 workflows
- **PA-53.2** [Warranty Claim Processing & Resolution](./VS-53-warranty-guarantee-management/PA-53.2-warranty-claim-processing.md) — 8 workflows
- **PA-53.3** [Extended Warranty & Service Contract Management](./VS-53-warranty-guarantee-management/PA-53.3-extended-warranty-service-contract.md) — 8 workflows

**[VS-55: Store Planogram & Space Optimization](./VS-55-store-planogram-space-optimization/README.md)** (24 workflows)

- **PA-55.1** [Planogram Design & Category Space Allocation](./VS-55-store-planogram-space-optimization/PA-55.1-planogram-design-space-allocation.md) — 8 workflows
- **PA-55.2** [Planogram Compliance & Audit](./VS-55-store-planogram-space-optimization/PA-55.2-planogram-compliance-audit.md) — 8 workflows
- **PA-55.3** [Space Productivity & Fixture Management](./VS-55-store-planogram-space-optimization/PA-55.3-space-productivity-fixture-mgmt.md) — 8 workflows

**[VS-58: Coupon & Digital Promotions Management](./VS-58-coupon-digital-promotions/README.md)** (24 workflows)

- **PA-58.1** [Coupon & Voucher Creation & Distribution](./VS-58-coupon-digital-promotions/PA-58.1-coupon-voucher-creation.md) — 8 workflows
- **PA-58.2** [Coupon Redemption & Fraud Prevention](./VS-58-coupon-digital-promotions/PA-58.2-coupon-redemption-fraud.md) — 8 workflows
- **PA-58.3** [Digital Promotion Performance Analytics](./VS-58-coupon-digital-promotions/PA-58.3-digital-promotion-analytics.md) — 8 workflows

**[VS-60: Omnichannel Order Routing & Fulfillment Orchestration](./VS-60-omnichannel-order-routing/README.md)** (24 workflows)

- **PA-60.1** [Intelligent Order Routing & Source Selection](./VS-60-omnichannel-order-routing/PA-60.1-intelligent-order-routing.md) — 8 workflows
- **PA-60.2** [Split-Order & Mixed-Basket Fulfillment](./VS-60-omnichannel-order-routing/PA-60.2-split-order-fulfillment.md) — 8 workflows
- **PA-60.3** [Fulfillment Performance & Optimization Analytics](./VS-60-omnichannel-order-routing/PA-60.3-fulfillment-performance-analytics.md) — 8 workflows

**[VS-62: Product Sample & Display Management](./VS-62-product-sample-display-management/README.md)** (24 workflows)

- **PA-62.1** [Sample Inventory Procurement & Distribution](./VS-62-product-sample-display-management/PA-62.1-sample-inventory-procurement.md) — 8 workflows
- **PA-62.2** [Display Maintenance & Sample Refresh](./VS-62-product-sample-display-management/PA-62.2-display-maintenance-sample-refresh.md) — 8 workflows
- **PA-62.3** [Sample & Display ROI Analytics](./VS-62-product-sample-display-management/PA-62.3-sample-display-roi-analytics.md) — 8 workflows

**[VS-63: Store Communication & Task Management](./VS-63-store-communication-task-management/README.md)** (24 workflows)

- **PA-63.1** [HQ-to-Store Communication & Broadcast](./VS-63-store-communication-task-management/PA-63.1-hq-store-communication.md) — 8 workflows
- **PA-63.2** [Store Task Assignment & Compliance Tracking](./VS-63-store-communication-task-management/PA-63.2-store-task-compliance.md) — 8 workflows
- **PA-63.3** [Communication Effectiveness & Feedback Analytics](./VS-63-store-communication-task-management/PA-63.3-communication-effectiveness-analytics.md) — 8 workflows

**[VS-65: E-Commerce Marketplace Integration](./VS-65-ecommerce-marketplace-integration/README.md)** (24 workflows)

- **PA-65.1** [Marketplace Channel Onboarding & Configuration](./VS-65-ecommerce-marketplace-integration/PA-65.1-marketplace-channel-onboarding.md) — 8 workflows
- **PA-65.2** [Marketplace Order & Inventory Sync](./VS-65-ecommerce-marketplace-integration/PA-65.2-marketplace-order-inventory-sync.md) — 8 workflows
- **PA-65.3** [Marketplace Performance & Settlement](./VS-65-ecommerce-marketplace-integration/PA-65.3-marketplace-performance-settlement.md) — 8 workflows

**[VS-66: Customer Project & Design Services](./VS-66-customer-project-design-services/README.md)** (24 workflows)

- **PA-66.1** [In-Home Measurement & Design Consultation](./VS-66-customer-project-design-services/PA-66.1-in-home-measurement-design.md) — 8 workflows
- **PA-66.2** [Project Quotation & Material Management](./VS-66-customer-project-design-services/PA-66.2-project-quotation-material-estimation.md) — 8 workflows
- **PA-66.3** [Project Tracking & Completion](./VS-66-customer-project-design-services/PA-66.3-project-tracking-completion.md) — 8 workflows

**[VS-70: Solar & Renewable Energy Product Operations](./VS-70-solar-renewable-energy/README.md)** (24 workflows)

- **PA-70.1** [Solar Product Merchandising & Consultation](./VS-70-solar-renewable-energy/PA-70.1-solar-product-merchandising-consultation.md) — 8 workflows
- **PA-70.2** [Solar Installation Coordination & Permitting](./VS-70-solar-renewable-energy/PA-70.2-solar-installation-coordination-permitting.md) — 8 workflows
- **PA-70.3** [Solar After-Sales Monitoring & Analytics](./VS-70-solar-renewable-energy/PA-70.3-solar-after-sales-monitoring-analytics.md) — 8 workflows

**[VS-75: Customer Digital Engagement & Mobile App Operations](./VS-75-digital-engagement-app/README.md)** (25 workflows)

- **PA-75.1** [Mobile App Product & Feature Management](./VS-75-digital-engagement-app/PA-75.1-mobile-app-product-feature-management.md) — 9 workflows
- **PA-75.2** [In-Store Digital Experience & Self-Service](./VS-75-digital-engagement-app/PA-75.2-in-store-digital-experience-self-service.md) — 8 workflows
- **PA-75.3** [Digital Engagement Analytics & Optimization](./VS-75-digital-engagement-app/PA-75.3-digital-engagement-analytics-optimization.md) — 8 workflows

**[VS-77: Construction Project Material Staging & Phased Delivery](./VS-77-construction-material-staging/README.md)** (24 workflows)

- **PA-77.1** [Project Material Planning & Phasing](./VS-77-construction-material-staging/PA-77.1-project-material-planning-phasing.md) — 8 workflows
- **PA-77.2** [Phased Delivery Execution & Site Coordination](./VS-77-construction-material-staging/PA-77.2-phased-delivery-execution-site-coordination.md) — 8 workflows
- **PA-77.3** [Project Material Reconciliation & Analytics](./VS-77-construction-material-staging/PA-77.3-project-material-reconciliation-analytics.md) — 8 workflows

**[VS-78: Green Building & Sustainable Product Advisory](./VS-78-green-building-advisory/README.md)** (24 workflows)

- **PA-78.1** [Green Product Curation & Certification](./VS-78-green-building-advisory/PA-78.1-green-product-curation-certification.md) — 8 workflows
- **PA-78.2** [Green Building Project Consultation](./VS-78-green-building-advisory/PA-78.2-green-building-project-consultation.md) — 8 workflows
- **PA-78.3** [Sustainability Compliance & Analytics](./VS-78-green-building-advisory/PA-78.3-sustainability-compliance-analytics.md) — 8 workflows

**[VS-82: Sari-Sari Store & MSME Micro-Wholesale Program](./VS-82-sari-sari-msme-micro-wholesale/README.md)** (24 workflows)

- **PA-82.1** [MSME/Sari-Sari Account Acquisition & Micro-Distribution](./VS-82-sari-sari-msme-micro-wholesale/PA-82.1-msme-acquisition-and-micro-distribution.md) — 8 workflows
- **PA-82.2** [Micro-Wholesale Ordering, Fulfillment & Delivery](./VS-82-sari-sari-msme-micro-wholesale/PA-82.2-micro-wholesale-order-fulfillment-delivery.md) — 8 workflows
- **PA-82.3** [MSME Growth, Credit & Digital Enablement](./VS-82-sari-sari-msme-micro-wholesale/PA-82.3-msme-growth-credit-and-digital-enablement.md) — 8 workflows

**[VS-95: Marketplace Operator & Third-Party Seller Management](./VS-95-marketplace-operator-third-party-seller/README.md)** (24 workflows)

- **PA-95.1** [Marketplace Platform Strategy & Seller Onboarding](./VS-95-marketplace-operator-third-party-seller/PA-95.1-marketplace-platform-strategy-seller-onboarding.md) — 8 workflows
- **PA-95.2** [Marketplace Catalog, Order Routing & Seller Fulfillment](./VS-95-marketplace-operator-third-party-seller/PA-95.2-marketplace-catalog-order-routing-fulfillment.md) — 8 workflows
- **PA-95.3** [Marketplace Settlement, Seller Performance & Governance](./VS-95-marketplace-operator-third-party-seller/PA-95.3-marketplace-settlement-performance-governance.md) — 8 workflows

**[VS-107: Strategic Key Account & Enterprise Customer Management](./VS-107-strategic-key-account-enterprise-customer-management/README.md)** (24 workflows)

- **PA-107.1** [Strategic Account Selection, Planning & Relationship Governance](./VS-107-strategic-key-account-enterprise-customer-management/PA-107.1-strategic-account-selection-planning-and-relationship-governance.md) — 8 workflows
- **PA-107.2** [Enterprise Account Growth, Contract & Executive Engagement](./VS-107-strategic-key-account-enterprise-customer-management/PA-107.2-enterprise-account-growth-contract-and-executive-engagement.md) — 8 workflows
- **PA-107.3** [Account Profitability, Retention & Strategic Analytics](./VS-107-strategic-key-account-enterprise-customer-management/PA-107.3-account-profitability-retention-and-strategic-analytics.md) — 8 workflows

**[VS-124: Sales Enablement, Product Knowledge Mastery & Clienteling](./VS-124-sales-enablement-product-knowledge-clienteling/README.md)** (24 workflows)

- **PA-124.1** [Sales Enablement Strategy, Content & Coaching Framework](./VS-124-sales-enablement-product-knowledge-clienteling/PA-124.1-sales-enablement-strategy-content-and-coaching-framework.md) — 8 workflows
- **PA-124.2** [Product Knowledge Mastery, Certification & Clienteling Tools](./VS-124-sales-enablement-product-knowledge-clienteling/PA-124.2-product-knowledge-mastery-certification-and-clienteling-tools.md) — 8 workflows
- **PA-124.3** [Selling Performance, Attachment & Clienteling Analytics](./VS-124-sales-enablement-product-knowledge-clienteling/PA-124.3-selling-performance-attachment-and-clienteling-analytics.md) — 8 workflows

**[VS-139: Trade Show, Exhibition & Field Event Marketing](./VS-139-trade-show-exhibition-and-field-event-marketing/README.md)** (24 workflows)

- **PA-139.1** [Event Marketing Strategy, Portfolio & Calendar Management](./VS-139-trade-show-exhibition-and-field-event-marketing/PA-139.1-event-marketing-strategy-portfolio-and-calendar-management.md) — 8 workflows
- **PA-139.2** [Exhibition & Trade-Show Operations](./VS-139-trade-show-exhibition-and-field-event-marketing/PA-139.2-exhibition-and-trade-show-operations.md) — 8 workflows
- **PA-139.3** [Field Events, Trade Days & Lead/ROI Analytics](./VS-139-trade-show-exhibition-and-field-event-marketing/PA-139.3-field-events-trade-days-and-lead-roi-analytics.md) — 8 workflows

**[VS-140: Field Sales, Outside Sales & Route-to-Market Force Management](./VS-140-field-sales-outside-sales-and-route-to-market-force-management/README.md)** (24 workflows)

- **PA-140.1** [Field Sales Strategy, Territory & Force Design](./VS-140-field-sales-outside-sales-and-route-to-market-force-management/PA-140.1-field-sales-strategy-territory-and-force-design.md) — 8 workflows
- **PA-140.2** [Field Sales Daily Operations, Account Coverage & Pipeline](./VS-140-field-sales-outside-sales-and-route-to-market-force-management/PA-140.2-field-sales-daily-operations-account-coverage-and-pipeline.md) — 8 workflows
- **PA-140.3** [Field Sales Performance, Compensation & Route Analytics](./VS-140-field-sales-outside-sales-and-route-to-market-force-management/PA-140.3-field-sales-performance-compensation-and-route-analytics.md) — 8 workflows

**[VS-145: Garden Center, Live Goods & Plant Nursery Operations](./VS-145-garden-center-live-goods-and-plant-nursery/README.md)** (24 workflows)

- **PA-145.1** [Live-Goods Assortment, Sourcing & Nursery Operations](./VS-145-garden-center-live-goods-and-plant-nursery/PA-145.1-live-goods-assortment-sourcing-and-nursery-operations.md) — 8 workflows
- **PA-145.2** [In-Store Garden Center Care, Merchandising & Sell-Through](./VS-145-garden-center-live-goods-and-plant-nursery/PA-145.2-in-store-garden-center-care-merchandising-and-sell-through.md) — 8 workflows
- **PA-145.3** [Live-Goods Shrink, Markdown, Compliance & Analytics](./VS-145-garden-center-live-goods-and-plant-nursery/PA-145.3-live-goods-shrink-markdown-compliance-and-analytics.md) — 8 workflows

**[VS-149: Self-Checkout, Scan-&-Go & Unattended Retail Technology Operations](./VS-149-self-checkout-scan-and-go-and-unattended-retail-technology-operations/README.md)** (24 workflows)

- **PA-149.1** [Self-Checkout & Scan-&-Go Strategy, Design & Technology](./VS-149-self-checkout-scan-and-go-and-unattended-retail-technology-operations/PA-149.1-self-checkout-and-scan-go-strategy-design-and-technology.md) — 8 workflows
- **PA-149.2** [SCO & Scan-&-Go Daily Operations & Customer Experience](./VS-149-self-checkout-scan-and-go-and-unattended-retail-technology-operations/PA-149.2-sco-and-scan-go-daily-operations-and-customer-experience.md) — 8 workflows
- **PA-149.3** [Loss Prevention, Cash, Compliance & Analytics](./VS-149-self-checkout-scan-and-go-and-unattended-retail-technology-operations/PA-149.3-loss-prevention-cash-compliance-and-analytics.md) — 8 workflows

**[VS-156: In-Store Value-Added Services & Financial Agency Operations](./VS-156-in-store-value-added-services-and-financial-agency-operations/README.md)** (24 workflows)

- **PA-156.1** [Value-Added Service & Financial Agency Product Setup & Partner Contracts](./VS-156-in-store-value-added-services-and-financial-agency-operations/PA-156.1-value-added-service-and-financial-agency-product-setup-and-partner-contracts.md) — 8 workflows
- **PA-156.2** [Counter Operations — Bills Payment, Remittance, E-Money & Mobile Load](./VS-156-in-store-value-added-services-and-financial-agency-operations/PA-156.2-counter-operations-bills-payment-remittance-e-money-and-mobile-load.md) — 8 workflows
- **PA-156.3** [Settlement, Reconciliation, Compliance (AML/BSP) & Analytics](./VS-156-in-store-value-added-services-and-financial-agency-operations/PA-156.3-settlement-reconciliation-compliance-and-analytics.md) — 8 workflows

**[VS-162: Customer Pickup Truck & Cargo Van Rental (Self-Haul) Operations](./VS-162-customer-pickup-truck-and-cargo-van-rental/README.md)** (24 workflows)

- **PA-162.1** [Rental Fleet Strategy, Acquisition & Lifecycle Management](./VS-162-customer-pickup-truck-and-cargo-van-rental/PA-162.1-rental-fleet-strategy-acquisition-and-lifecycle-management.md) — 8 workflows
- **PA-162.2** [Rental Transaction, Counter Operations & Customer Onboarding](./VS-162-customer-pickup-truck-and-cargo-van-rental/PA-162.2-rental-transaction-counter-operations-and-customer-onboarding.md) — 8 workflows
- **PA-162.3** [Incident, Damage, Compliance & Rental Analytics](./VS-162-customer-pickup-truck-and-cargo-van-rental/PA-162.3-incident-damage-compliance-and-rental-analytics.md) — 8 workflows

**[VS-164: Smart Locker & Automated Parcel Collection Network](./VS-164-smart-locker-and-automated-parcel-collection-network/README.md)** (24 workflows)

- **PA-164.1** [Locker Network Strategy, Siting & Deployment](./VS-164-smart-locker-and-automated-parcel-collection-network/PA-164.1-locker-network-strategy-siting-and-deployment.md) — 8 workflows
- **PA-164.2** [Collection Operations, Replenishment & Access Management](./VS-164-smart-locker-and-automated-parcel-collection-network/PA-164.2-collection-operations-replenishment-and-access-management.md) — 8 workflows
- **PA-164.3** [Maintenance, Integration, Compliance & Network Analytics](./VS-164-smart-locker-and-automated-parcel-collection-network/PA-164.3-maintenance-integration-compliance-and-network-analytics.md) — 8 workflows

**[VS-168: In-Store Audio, Ambient Media & Music Royalty Licensing](./VS-168-in-store-audio-ambient-media-and-music-royalty-licensing/README.md)** (24 workflows)

- **PA-168.1** [In-Store Audio, Ambient Media Strategy & Music Royalty Compliance](./VS-168-in-store-audio-ambient-media-and-music-royalty-licensing/PA-168.1-in-store-audio-ambient-media-strategy-and-music-royalty-compliance.md) — 8 workflows
- **PA-168.2** [In-Store Audio, PA & Media Daily Operations](./VS-168-in-store-audio-ambient-media-and-music-royalty-licensing/PA-168.2-in-store-audio-pa-and-media-daily-operations.md) — 8 workflows
- **PA-168.3** [Ambient Media Analytics, Technology & Program Assurance](./VS-168-in-store-audio-ambient-media-and-music-royalty-licensing/PA-168.3-ambient-media-analytics-technology-and-program-assurance.md) — 8 workflows

**[VS-171: Customer Pickup, Loading Zone & Will-Call Counter Operations](./VS-171-customer-pickup-loading-zone-and-will-call-counter-operations/README.md)** (24 workflows)

- **PA-171.1** [Customer Pickup & Will-Call Program Design, Capacity & Scheduling](./VS-171-customer-pickup-loading-zone-and-will-call-counter-operations/PA-171.1-customer-pickup-and-will-call-program-design-capacity-and-scheduling.md) — 8 workflows
- **PA-171.2** [Bulky-Goods Loading, Forklift-in-Customer-Area & Vehicle Coordination](./VS-171-customer-pickup-loading-zone-and-will-call-counter-operations/PA-171.2-bulky-goods-loading-forklift-in-customer-area-and-vehicle-coordination.md) — 8 workflows
- **PA-171.3** [Pickup Experience, Exceptions, Chargeback & Analytics](./VS-171-customer-pickup-loading-zone-and-will-call-counter-operations/PA-171.3-pickup-experience-exceptions-chargeback-and-analytics.md) — 8 workflows

**[VS-172: Third-Party Installer & Contractor Network (Pro-Referral) Management](./VS-172-third-party-installer-and-contractor-network-pro-referral-management/README.md)** (24 workflows)

- **PA-172.1** [Installer/Contractor Network Strategy, Recruitment & Vetting](./VS-172-third-party-installer-and-contractor-network-pro-referral-management/PA-172.1-installer-contractor-network-strategy-recruitment-and-vetting.md) — 8 workflows
- **PA-172.2** [Pro-Referral Matchmaking, Project Routing & Lead Management](./VS-172-third-party-installer-and-contractor-network-pro-referral-management/PA-172.2-pro-referral-matchmaking-project-routing-and-lead-management.md) — 8 workflows
- **PA-172.3** [Network Performance, Quality, Compliance & Analytics](./VS-172-third-party-installer-and-contractor-network-pro-referral-management/PA-172.3-network-performance-quality-compliance-and-analytics.md) — 8 workflows

**[VS-174: Self-Storage, Portable Container & Mobile-Storage Operations](./VS-174-self-storage-portable-container-and-mobile-storage-operations/README.md)** (24 workflows)

- **PA-174.1** [Storage Portfolio Strategy, Site Selection & Unit/Container Capacity Planning](./VS-174-self-storage-portable-container-and-mobile-storage-operations/PA-174.1-storage-portfolio-strategy-site-and-unit-capacity-planning.md) — 8 workflows
- **PA-174.2** [Customer Rental Lifecycle — Move-In, Access, Billing & Move-Out](./VS-174-self-storage-portable-container-and-mobile-storage-operations/PA-174.2-customer-rental-lifecycle-move-in-access-billing-and-move-out.md) — 8 workflows
- **PA-174.3** [Storage Operations, Maintenance, Safety & Analytics](./VS-174-self-storage-portable-container-and-mobile-storage-operations/PA-174.3-storage-operations-maintenance-safety-and-analytics.md) — 8 workflows

**[VS-175: Propane, LPG Cylinder Exchange & Gas Refill Operations](./VS-175-propane-lpg-cylinder-exchange-and-gas-refill-operations/README.md)** (24 workflows)

- **PA-175.1** [LPG Program Strategy, Bulk Supply, Cylinder Fleet & Regulatory Setup](./VS-175-propane-lpg-cylinder-exchange-and-gas-refill-operations/PA-175.1-lpg-program-strategy-supply-cylinder-fleet-and-compliance-setup.md) — 8 workflows
- **PA-175.2** [Cylinder Exchange & Refill Operations](./VS-175-propane-lpg-cylinder-exchange-and-gas-refill-operations/PA-175.2-cylinder-exchange-and-refill-operations.md) — 8 workflows
- **PA-175.3** [LPG Safety, Compliance, Cylinder Reconciliation & Analytics](./VS-175-propane-lpg-cylinder-exchange-and-gas-refill-operations/PA-175.3-safety-compliance-cylinder-reconciliation-and-analytics.md) — 8 workflows

**[VS-176: Blueprint, Reprographics & Large-Format Plan Printing Services](./VS-176-blueprint-reprographics-and-large-format-plan-printing-services/README.md)** (24 workflows)

- **PA-176.1** [Reprographics Service Strategy, Equipment & Catalog Setup](./VS-176-blueprint-reprographics-and-large-format-plan-printing-services/PA-176.1-reprographics-service-strategy-equipment-and-catalog-setup.md) — 8 workflows
- **PA-176.2** [Customer Reprographics Job Lifecycle](./VS-176-blueprint-reprographics-and-large-format-plan-printing-services/PA-176.2-customer-reprographics-job-lifecycle.md) — 8 workflows
- **PA-176.3** [Print Quality, Compliance, Document Security & Analytics](./VS-176-blueprint-reprographics-and-large-format-plan-printing-services/PA-176.3-quality-compliance-security-and-analytics.md) — 8 workflows

**[VS-177: Field Retail Operations, Regional/District Management & Multi-Store Retail Execution Network](./VS-177-field-retail-operations-regional-district-management-and-multi-store-execution/README.md)** (24 workflows)

- **PA-177.1** [Field Organization, Territory Design & Regional/District Store Management](./VS-177-field-retail-operations-regional-district-management-and-multi-store-execution/PA-177.1-field-organization-territory-design-and-regional-district-store-management.md) — 8 workflows
- **PA-177.2** [Store Visit, Field Coaching & Retail Standards Execution](./VS-177-field-retail-operations-regional-district-management-and-multi-store-execution/PA-177.2-store-visit-field-coaching-and-retail-standards-execution.md) — 8 workflows
- **PA-177.3** [Store Support Center, Escalation & Field Operations Analytics](./VS-177-field-retail-operations-regional-district-management-and-multi-store-execution/PA-177.3-store-support-center-escalation-and-field-operations-analytics.md) — 8 workflows

**[VS-185: B2B Cooperative Credit & Procurement Partnerships](./VS-185-b2b-cooperative-credit-and-procurement-partnerships/README.md)** (24 workflows)

- **PA-185.1** [Cooperative Account Onboarding & Credit Limits](./VS-185-b2b-cooperative-credit-and-procurement-partnerships/PA-185.1-cooperative-account-onboarding-and-credit-limits.md) — 8 workflows
- **PA-185.2** [Member Transaction Routing & Verification](./VS-185-b2b-cooperative-credit-and-procurement-partnerships/PA-185.2-member-transaction-routing-and-verification.md) — 8 workflows
- **PA-185.3** [Cooperative Rebate & Purchase Volume Reconciliation](./VS-185-b2b-cooperative-credit-and-procurement-partnerships/PA-185.3-cooperative-rebate-and-purchase-volume-reconciliation.md) — 8 workflows

**[VS-186: Compact & Heavy Construction Equipment Rental Fleet Operations](./VS-186-compact-and-heavy-construction-equipment-rental-fleet-operations/README.md)** (24 workflows)

- **PA-186.1** [Fleet Strategy, Acquisition & Yard Infrastructure](./VS-186-compact-and-heavy-construction-equipment-rental-fleet-operations/PA-186.1-equipment-rental-fleet-strategy-acquisition-and-yard-infrastructure.md) — 8 workflows
- **PA-186.2** [Rental Transaction Lifecycle — Booking, Handover, Operation & Return](./VS-186-compact-and-heavy-construction-equipment-rental-fleet-operations/PA-186.2-equipment-rental-transaction-lifecycle.md) — 8 workflows
- **PA-186.3** [Equipment Maintenance, Safety, Compliance & Fleet Utilization Analytics](./VS-186-compact-and-heavy-construction-equipment-rental-fleet-operations/PA-186.3-equipment-maintenance-safety-compliance-and-analytics.md) — 8 workflows

### Finance

**[VS-15: Procure-to-Pay](./VS-15-procure-to-pay/README.md)** (43 workflows)

- **PA-15.1** [Invoice Processing & Matching](./VS-15-procure-to-pay/PA-15.1-invoice-processing-and-matching.md) — 19 workflows
- **PA-15.2** [Vendor Payment & Reconciliation](./VS-15-procure-to-pay/PA-15.2-vendor-payment-and-reconciliation.md) — 24 workflows

**[VS-16: Order-to-Cash](./VS-16-order-to-cash/README.md)** (31 workflows)

- **PA-16.1** [Credit Application & Scoring](./VS-16-order-to-cash/PA-16.1-credit-application-and-scoring.md) — 12 workflows
- **PA-16.2** [AR & Collections](./VS-16-order-to-cash/PA-16.2-ar-and-collections.md) — 10 workflows
- **PA-16.3** [Customer Payment & Settlement](./VS-16-order-to-cash/PA-16.3-customer-payment-and-settlement.md) — 9 workflows

**[VS-17: Record-to-Report](./VS-17-record-to-report/README.md)** (70 workflows)

- **PA-17.1** [GL & Financial Close](./VS-17-record-to-report/PA-17.1-gl-and-financial-close.md) — 26 workflows
- **PA-17.2** [Consolidation & Intercompany](./VS-17-record-to-report/PA-17.2-consolidation-and-intercompany.md) — 10 workflows
- **PA-17.3** [Tax & Statutory](./VS-17-record-to-report/PA-17.3-tax-and-statutory.md) — 15 workflows
- **PA-17.4** [FP&A & Reporting](./VS-17-record-to-report/PA-17.4-fpanda-and-reporting.md) — 19 workflows

**[VS-18: Treasury & Cash](./VS-18-treasury-cash/README.md)** (35 workflows)

- **PA-18.1** [Cash Positioning & Forecasting](./VS-18-treasury-cash/PA-18.1-cash-positioning-and-forecasting.md) — 15 workflows
- **PA-18.2** [Banking & Payments](./VS-18-treasury-cash/PA-18.2-banking-and-payments.md) — 10 workflows
- **PA-18.3** [FX & Investments](./VS-18-treasury-cash/PA-18.3-fx-and-investments.md) — 10 workflows

**[VS-34: Expense & Non-Merchandise Procurement](./VS-34-expense-procurement/README.md)** (22 workflows)

- **PA-34.1** [Non-Merchandise Procurement Operations](./VS-34-expense-procurement/PA-34.1-non-merchandise-procurement.md) — 8 workflows
- **PA-34.2** [Service Provider & Contract Management](./VS-34-expense-procurement/PA-34.2-service-provider-management.md) — 7 workflows
- **PA-34.3** [Expense Monitoring & Control](./VS-34-expense-procurement/PA-34.3-expense-monitoring-control.md) — 7 workflows

**[VS-38: Consumer Credit & Financing](./VS-38-consumer-credit-financing/README.md)** (24 workflows)

- **PA-38.1** [Consumer Financing Program Management](./VS-38-consumer-credit-financing/PA-38.1-consumer-financing-program.md) — 8 workflows
- **PA-38.2** [Installment Sale Processing & Monitoring](./VS-38-consumer-credit-financing/PA-38.2-installment-sale-processing.md) — 8 workflows
- **PA-38.3** [Financing Reconciliation & Partner Settlement](./VS-38-consumer-credit-financing/PA-38.3-financing-reconciliation-settlement.md) — 8 workflows

**[VS-39: Vendor Rebate & Incentive Management](./VS-39-vendor-rebate-incentive/README.md)** (24 workflows)

- **PA-39.1** [Rebate Agreement & Accrual Management](./VS-39-vendor-rebate-incentive/PA-39.1-rebate-agreement-accrual.md) — 8 workflows
- **PA-39.2** [Co-Op Marketing & Promotional Fund Management](./VS-39-vendor-rebate-incentive/PA-39.2-coop-marketing-promotional-funds.md) — 8 workflows
- **PA-39.3** [Rebate Settlement & Analytics](./VS-39-vendor-rebate-incentive/PA-39.3-rebate-settlement-analytics.md) — 8 workflows

**[VS-40: Capex & Project Accounting](./VS-40-capex-project-accounting/README.md)** (24 workflows)

- **PA-40.1** [Capital Expenditure Request & Approval](./VS-40-capex-project-accounting/PA-40.1-capex-request-approval.md) — 8 workflows
- **PA-40.2** [Project Cost Tracking & Capitalization](./VS-40-capex-project-accounting/PA-40.2-project-cost-tracking.md) — 8 workflows
- **PA-40.3** [Construction-in-Progress & Asset Turnover](./VS-40-capex-project-accounting/PA-40.3-cip-asset-turnover.md) — 8 workflows

**[VS-54: Gift Card & Stored Value Management](./VS-54-gift-card-stored-value/README.md)** (26 workflows)

- **PA-54.1** [Gift Card Issuance & Distribution](./VS-54-gift-card-stored-value/PA-54.1-gift-card-issuance-distribution.md) — 8 workflows
- **PA-54.2** [Gift Card Redemption & Balance Management](./VS-54-gift-card-stored-value/PA-54.2-gift-card-redemption-balance.md) — 9 workflows
- **PA-54.3** [Gift Card Reconciliation & Analytics](./VS-54-gift-card-stored-value/PA-54.3-gift-card-reconciliation-analytics.md) — 9 workflows

**[VS-68: Trade Credit Insurance & Risk Management](./VS-68-trade-credit-risk-management/README.md)** (24 workflows)

- **PA-68.1** [Trade Credit Risk Assessment & Scoring](./VS-68-trade-credit-risk-management/PA-68.1-trade-credit-risk-assessment.md) — 8 workflows
- **PA-68.2** [Credit Limit Management & Monitoring](./VS-68-trade-credit-risk-management/PA-68.2-credit-limit-management-monitoring.md) — 8 workflows
- **PA-68.3** [Bad Debt Recovery & Write-Off Management](./VS-68-trade-credit-risk-management/PA-68.3-bad-debt-recovery-writeoff.md) — 8 workflows

**[VS-72: Cross-Entity Shared Services & Chargeback](./VS-72-cross-entity-shared-services/README.md)** (24 workflows)

- **PA-72.1** [Shared Services Cost Pool Management](./VS-72-cross-entity-shared-services/PA-72.1-shared-services-cost-pool-management.md) — 8 workflows
- **PA-72.2** [Inter-Entity Service Level & Billing](./VS-72-cross-entity-shared-services/PA-72.2-inter-entity-service-level-billing.md) — 8 workflows
- **PA-72.3** [Shared Services Performance & Analytics](./VS-72-cross-entity-shared-services/PA-72.3-shared-services-performance-analytics.md) — 8 workflows

**[VS-79: Tax Management & BIR Statutory Reporting](./VS-79-tax-management-bir-reporting/README.md)** (28 workflows)

- **PA-79.1** [Indirect Tax (VAT & Percentage Tax) & BIR E-Invoicing](./VS-79-tax-management-bir-reporting/PA-79.1-indirect-tax-vat-and-einvoicing.md) — 8 workflows
- **PA-79.2** [Withholding Tax (EWT/CWT) & Form 2307 Management](./VS-79-tax-management-bir-reporting/PA-79.2-withholding-tax-and-2307-management.md) — 10 workflows
- **PA-79.3** [Corporate Income Tax, Local Tax, DST & BIR Audit Defense](./VS-79-tax-management-bir-reporting/PA-79.3-income-tax-local-tax-and-audit-defense.md) — 10 workflows

**[VS-80: Payment Operations, Acquirer & Settlement Management](./VS-80-payment-operations-acquirer-settlement/README.md)** (24 workflows)

- **PA-80.1** [Acquirer, PSP & Payment Partner Lifecycle Management](./VS-80-payment-operations-acquirer-settlement/PA-80.1-acquirer-psp-and-partner-lifecycle.md) — 8 workflows
- **PA-80.2** [Settlement Reconciliation & Chargeback/Dispute Management](./VS-80-payment-operations-acquirer-settlement/PA-80.2-settlement-reconciliation-and-dispute.md) — 8 workflows
- **PA-80.3** [Payment Cost, Fraud & Tokenization Governance](./VS-80-payment-operations-acquirer-settlement/PA-80.3-payment-cost-fraud-and-tokenization.md) — 8 workflows

**[VS-96: Equipment Leasing & Capital Equipment Finance](./VS-96-equipment-leasing-capital-equipment-finance/README.md)** (24 workflows)

- **PA-96.1** [Lease Product Design, Credit Underwriting & Origination](./VS-96-equipment-leasing-capital-equipment-finance/PA-96.1-lease-product-design-underwriting-origination.md) — 8 workflows
- **PA-96.2** [Lease Booking, Billing & Asset Lifecycle Management](./VS-96-equipment-leasing-capital-equipment-finance/PA-96.2-lease-booking-billing-asset-lifecycle.md) — 8 workflows
- **PA-96.3** [Lease Portfolio Risk, Residual & Yield Analytics](./VS-96-equipment-leasing-capital-equipment-finance/PA-96.3-lease-portfolio-risk-residual-yield-analytics.md) — 8 workflows

**[VS-105: Supply Chain Finance & Working Capital Management](./VS-105-supply-chain-finance-working-capital-management/README.md)** (25 workflows)

- **PA-105.1** [Supplier Finance & Reverse-Factoring Program Management](./VS-105-supply-chain-finance-working-capital-management/PA-105.1-supplier-finance-and-reverse-factoring-program.md) — 8 workflows
- **PA-105.2** [Dynamic Discounting & Early-Payment Operations](./VS-105-supply-chain-finance-working-capital-management/PA-105.2-dynamic-discounting-and-early-payment-operations.md) — 8 workflows
- **PA-105.3** [Working Capital Analytics & Cash-Conversion-Cycle Governance](./VS-105-supply-chain-finance-working-capital-management/PA-105.3-working-capital-analytics-and-cash-conversion-governance.md) — 9 workflows

**[VS-116: Performance Bond, Surety & Bank Guarantee Management](./VS-116-performance-bond-surety-and-bank-guarantee-management/README.md)** (24 workflows)

- **PA-116.1** [Surety Facility Strategy, Provider Management & Program Governance](./VS-116-performance-bond-surety-and-bank-guarantee-management/PA-116.1-surety-facility-strategy-provider-management-and-governance.md) — 8 workflows
- **PA-116.2** [Bond/Guarantee Application, Issuance, Tracking & Encumbrance Management](./VS-116-performance-bond-surety-and-bank-guarantee-management/PA-116.2-bond-application-issuance-tracking-and-encumbrance-management.md) — 8 workflows
- **PA-116.3** [Bond Release, Claims, Recovery & Surety Analytics](./VS-116-performance-bond-surety-and-bank-guarantee-management/PA-116.3-bond-release-claims-recovery-and-surety-analytics.md) — 8 workflows

**[VS-118: Revenue Assurance, Pricing Integrity & Leakage Management](./VS-118-revenue-assurance-pricing-integrity-and-leakage-management/README.md)** (25 workflows)

- **PA-118.1** [Revenue Assurance Strategy, Governance & Leak Detection Framework](./VS-118-revenue-assurance-pricing-integrity-and-leakage-management/PA-118.1-revenue-assurance-strategy-governance-and-leak-detection-framework.md) — 8 workflows
- **PA-118.2** [Pricing, Promotion, Loyalty & Payment Integrity Monitoring](./VS-118-revenue-assurance-pricing-integrity-and-leakage-management/PA-118.2-pricing-promotion-loyalty-and-payment-integrity-monitoring.md) — 9 workflows
- **PA-118.3** [Leakage Recovery, Revenue Analytics & Continuous Assurance](./VS-118-revenue-assurance-pricing-integrity-and-leakage-management/PA-118.3-leakage-recovery-revenue-analytics-and-continuous-assurance.md) — 8 workflows

**[VS-125: Cross-Channel Fraud Management & Payment Fraud Protection](./VS-125-cross-channel-fraud-management-payment-fraud-protection/README.md)** (24 workflows)

- **PA-125.1** [Fraud Strategy, Governance & Detection Platform](./VS-125-cross-channel-fraud-management-payment-fraud-protection/PA-125.1-fraud-strategy-governance-detection-platform.md) — 8 workflows
- **PA-125.2** [Channel-Specific Fraud Prevention & Detection](./VS-125-cross-channel-fraud-management-payment-fraud-protection/PA-125.2-channel-fraud-prevention-detection.md) — 8 workflows
- **PA-125.3** [Investigation, Recovery, Compliance & Analytics](./VS-125-cross-channel-fraud-management-payment-fraud-protection/PA-125.3-investigation-recovery-compliance-analytics.md) — 8 workflows

**[VS-142: Cash-on-Delivery (COD) Operations, Driver Cash Handling & Reconciliation](./VS-142-cash-on-delivery-operations-driver-cash-handling-and-reconciliation/README.md)** (24 workflows)

- **PA-142.1** [COD Program Design, Policy & Risk Framework](./VS-142-cash-on-delivery-operations-driver-cash-handling-and-reconciliation/PA-142.1-cod-program-design-policy-and-risk-framework.md) — 8 workflows
- **PA-142.2** [COD Cash Collection, Custody & Driver/3PL Reconciliation](./VS-142-cash-on-delivery-operations-driver-cash-handling-and-reconciliation/PA-142.2-cod-cash-collection-custody-and-driver-3pl-reconciliation.md) — 8 workflows
- **PA-142.3** [COD Settlement, Working-Capital, Fraud & Analytics](./VS-142-cash-on-delivery-operations-driver-cash-handling-and-reconciliation/PA-142.3-cod-settlement-working-capital-fraud-and-analytics.md) — 8 workflows

**[VS-148: Lease Accounting (PFRS 16/IFRS 16) & Right-of-Use Asset Management](./VS-148-lease-accounting-pfrs-16-and-right-of-use-asset-management/README.md)** (24 workflows)

- **PA-148.1** [Lease Portfolio Identification, Recognition & PFRS 16 Transition](./VS-148-lease-accounting-pfrs-16-and-right-of-use-asset-management/PA-148.1-lease-portfolio-identification-recognition-and-pfrs-16-transition.md) — 8 workflows
- **PA-148.2** [ROU Asset & Lease Liability Measurement, Modification & Reporting](./VS-148-lease-accounting-pfrs-16-and-right-of-use-asset-management/PA-148.2-rou-asset-and-lease-liability-measurement-modification-and-reporting.md) — 8 workflows
- **PA-148.3** [Lease Administration, Compliance & Optimization Analytics](./VS-148-lease-accounting-pfrs-16-and-right-of-use-asset-management/PA-148.3-lease-administration-compliance-and-optimization-analytics.md) — 8 workflows

**[VS-153: Captive Insurance, Reinsurance & Enterprise Risk Financing](./VS-153-captive-insurance-reinsurance-and-enterprise-risk-financing/README.md)** (24 workflows)

- **PA-153.1** [Captive Feasibility, Formation & Domicile/Governance](./VS-153-captive-insurance-reinsurance-and-enterprise-risk-financing/PA-153.1-captive-feasibility-formation-and-domicile-governance.md) — 8 workflows
- **PA-153.2** [Captive Underwriting, Risk Transfer & Reinsurance Program](./VS-153-captive-insurance-reinsurance-and-enterprise-risk-financing/PA-153.2-captive-underwriting-risk-transfer-and-reinsurance-program.md) — 8 workflows
- **PA-153.3** [Captive Claims, Finance, Regulatory & Portfolio Analytics](./VS-153-captive-insurance-reinsurance-and-enterprise-risk-financing/PA-153.3-captive-claims-finance-regulatory-and-portfolio-analytics.md) — 8 workflows

**[VS-154: Home Construction Finance, Loan Brokerage & Mortgage Referral Services](./VS-154-home-construction-finance-loan-brokerage-and-mortgage-referral/README.md)** (24 workflows)

- **PA-154.1** [Construction Finance Product, Lender Network & Brokerage Setup](./VS-154-home-construction-finance-loan-brokerage-and-mortgage-referral/PA-154.1-construction-finance-product-lender-network-and-brokerage-setup.md) — 8 workflows
- **PA-154.2** [Customer Loan Origination, Underwriting & Closing](./VS-154-home-construction-finance-loan-brokerage-and-mortgage-referral/PA-154.2-customer-loan-origination-underwriting-and-closing.md) — 8 workflows
- **PA-154.3** [Loan Servicing, Referral Economics, Compliance & Analytics](./VS-154-home-construction-finance-loan-brokerage-and-mortgage-referral/PA-154.3-loan-servicing-referral-economics-compliance-and-analytics.md) — 8 workflows

**[VS-157: Revenue Recognition (PFRS 15) & Complex Contract Accounting](./VS-157-revenue-recognition-pfrs-15-and-complex-contract-accounting/README.md)** (24 workflows)

- **PA-157.1** [Multi-Element Arrangement Identification & Performance Obligation Assessment](./VS-157-revenue-recognition-pfrs-15-and-complex-contract-accounting/PA-157.1-multi-element-arrangement-identification-and-performance-obligation-assessment.md) — 8 workflows
- **PA-157.2** [Standalone Selling Price, Allocation & Deferred-Revenue Measurement](./VS-157-revenue-recognition-pfrs-15-and-complex-contract-accounting/PA-157.2-standalone-selling-price-allocation-and-deferred-revenue-measurement.md) — 8 workflows
- **PA-157.3** [Period Close, Disclosure, Audit & New-Revenue-Stream Onboarding](./VS-157-revenue-recognition-pfrs-15-and-complex-contract-accounting/PA-157.3-period-close-disclosure-audit-and-new-revenue-stream-onboarding.md) — 8 workflows

**[VS-158: Product Costing, Landed-Cost & Cost Accounting](./VS-158-product-costing-landed-cost-and-cost-accounting/README.md)** (24 workflows)

- **PA-158.1** [Standard-Cost Setup, Landed-Cost & Item Cost Roll](./VS-158-product-costing-landed-cost-and-cost-accounting/PA-158.1-standard-cost-setup-landed-cost-and-item-cost-roll.md) — 8 workflows
- **PA-158.2** [Cost Variance, Actual-vs-Standard & Margin Analytics](./VS-158-product-costing-landed-cost-and-cost-accounting/PA-158.2-cost-variance-actual-vs-standard-and-margin-analytics.md) — 8 workflows
- **PA-158.3** [Specialized Costing (Project, Service, Intercompany) & Cost Governance](./VS-158-product-costing-landed-cost-and-cost-accounting/PA-158.3-specialized-costing-project-service-intercompany-and-cost-governance.md) — 8 workflows

**[VS-170: Inventory Pledge, Asset-Based Lending & Trust-Receipt (Warehouse-Receipt) Financing](./VS-170-inventory-pledge-asset-based-lending-and-trust-receipt-financing/README.md)** (24 workflows)

- **PA-170.1** [Borrowing-Base, Collateral & Asset-Based Lending Facility Management](./VS-170-inventory-pledge-asset-based-lending-and-trust-receipt-financing/PA-170.1-borrowing-base-collateral-and-asset-based-lending-facility-management.md) — 8 workflows
- **PA-170.2** [Trust-Receipt, Warehouse-Receipt & Import Inventory Financing Operations](./VS-170-inventory-pledge-asset-based-lending-and-trust-receipt-financing/PA-170.2-trust-receipt-warehouse-receipt-and-import-inventory-financing-operations.md) — 8 workflows
- **PA-170.3** [Collateral Release, Reconciliation, Compliance & Analytics](./VS-170-inventory-pledge-asset-based-lending-and-trust-receipt-financing/PA-170.3-collateral-release-reconciliation-compliance-and-analytics.md) — 8 workflows


**[VS-181: B2B Project Financing, Escrow Account Orchestration & Lien Release](./VS-181-b2b-project-financing-escrow-account-orchestration-and-lien-release/README.md)** (24 workflows)

- **PA-181.1** [B2B Project Escrow Onboarding, Contract Matching & Credit Setup](./VS-181-b2b-project-financing-escrow-account-orchestration-and-lien-release/PA-181.1-b2b-project-escrow-onboarding-contract-matching-credit-setup.md) — 8 workflows
- **PA-181.2** [Milestone Inspection, Joint Quantity Survey & Escrow Draw Processing](./VS-181-b2b-project-financing-escrow-account-orchestration-and-lien-release/PA-181.2-milestone-inspection-joint-quantity-survey-escrow-draw-processing.md) — 8 workflows
- **PA-181.3** [Waiver of Lien, Progress Billing Reconciliation & Account Hold Management](./VS-181-b2b-project-financing-escrow-account-orchestration-and-lien-release/PA-181.3-waiver-of-lien-progress-billing-reconciliation-account-hold-management.md) — 8 workflows

**[VS-173: Investor Relations, Capital Markets & Securities Disclosure](./VS-173-investor-relations-capital-markets-and-securities-disclosure/README.md)** (24 workflows)

- **PA-173.1** [Investor Relations Program, Shareholder Communications & Capital-Markets Engagement](./VS-173-investor-relations-capital-markets-and-securities-disclosure/PA-173.1-investor-relations-program-shareholder-communications-and-capital-markets-engagement.md) — 8 workflows
- **PA-173.2** [Corporate Disclosure, Securities & SEC/Regulatory Compliance](./VS-173-investor-relations-capital-markets-and-securities-disclosure/PA-173.2-corporate-disclosure-securities-and-regulatory-compliance.md) — 8 workflows
- **PA-173.3** [Shareholder Services, Equity Records, Dividend & IR Analytics](./VS-173-investor-relations-capital-markets-and-securities-disclosure/PA-173.3-shareholder-services-equity-records-dividend-and-ir-analytics.md) — 8 workflows

**[VS-188: Trade Reseller Floor-Plan & Dealer Inventory Financing](./VS-188-trade-reseller-floor-plan-and-dealer-inventory-financing/README.md)** (24 workflows)

- **PA-188.1** [Program Strategy, Credit Framework & Dealer Onboarding](./VS-188-trade-reseller-floor-plan-and-dealer-inventory-financing/PA-188.1-floor-plan-program-strategy-credit-framework-and-onboarding.md) — 8 workflows
- **PA-188.2** [Loan Origination, Disbursement & Inventory Collateral Tracking](./VS-188-trade-reseller-floor-plan-and-dealer-inventory-financing/PA-188.2-floor-plan-origination-disbursement-and-collateral-tracking.md) — 8 workflows
- **PA-188.3** [Curtailment, Collections, Risk & Portfolio Analytics](./VS-188-trade-reseller-floor-plan-and-dealer-inventory-financing/PA-188.3-curtailment-collections-risk-and-portfolio-analytics.md) — 8 workflows

**[VS-189: Trade Accounts Receivable Factoring, Invoice Discounting & Receivables Securitization](./VS-189-trade-receivables-factoring-invoice-discounting-and-securitization/README.md)** (24 workflows)

- **PA-189.1** [Receivables Financing Strategy, Funder Relationships & Program Setup](./VS-189-trade-receivables-factoring-invoice-discounting-and-securitization/PA-189.1-receivables-financing-strategy-funder-relationships-and-setup.md) — 8 workflows
- **PA-189.2** [Invoice Sale, Factoring Drawdown, Notification & Cash Application](./VS-189-trade-receivables-factoring-invoice-discounting-and-securitization/PA-189.2-invoice-sale-factoring-drawdown-notification-and-cash-application.md) — 8 workflows
- **PA-189.3** [Collections, Recourse Management, Reconciliation & Portfolio Analytics](./VS-189-trade-receivables-factoring-invoice-discounting-and-securitization/PA-189.3-collections-recourse-reconciliation-and-portfolio-analytics.md) — 8 workflows

### People

**[VS-19: Hire-to-Retire](./VS-19-hire-to-retire/README.md)** (81 workflows)

- **PA-19.1** [Recruitment & Onboarding](./VS-19-hire-to-retire/PA-19.1-recruitment-and-onboarding.md) — 36 workflows
- **PA-19.2** [Payroll & Compensation](./VS-19-hire-to-retire/PA-19.2-payroll-and-compensation.md) — 11 workflows
- **PA-19.3** [Workforce Management](./VS-19-hire-to-retire/PA-19.3-workforce-management.md) — 12 workflows
- **PA-19.4** [Learning & Development](./VS-19-hire-to-retire/PA-19.4-learning-and-development.md) — 14 workflows
- **PA-19.5** [Separation & Benefits](./VS-19-hire-to-retire/PA-19.5-separation-and-benefits.md) — 8 workflows

**[VS-83: Occupational Health, Safety Clinic & Employee Wellness](./VS-83-occupational-health-clinic-wellness/README.md)** (25 workflows)

- **PA-83.1** [Occupational Health Clinic & Medical Case Management](./VS-83-occupational-health-clinic-wellness/PA-83.1-occupational-health-clinic-and-medical-case.md) — 8 workflows
- **PA-83.2** [Periodic Examination, DOLE Compliance & Disease Surveillance](./VS-83-occupational-health-clinic-wellness/PA-83.2-periodic-exam-dole-compliance-surveillance.md) — 8 workflows
- **PA-83.3** [Mental Health, Wellness & Employee Assistance Program](./VS-83-occupational-health-clinic-wellness/PA-83.3-mental-health-wellness-eap.md) — 9 workflows

**[VS-84: Labor Relations & Collective Bargaining Management](./VS-84-labor-relations-collective-bargaining/README.md)** (25 workflows)

- **PA-84.1** [Union Recognition, CBA Negotiation & Administration](./VS-84-labor-relations-collective-bargaining/PA-84.1-union-recognition-cba-negotiation-administration.md) — 8 workflows
- **PA-84.2** [Grievance Handling, Labor Dispute & DOLE Conciliation](./VS-84-labor-relations-collective-bargaining/PA-84.2-grievance-labor-dispute-dole-conciliation.md) — 9 workflows
- **PA-84.3** [Employee Voice, Engagement & Partnership Management](./VS-84-labor-relations-collective-bargaining/PA-84.3-employee-voice-engagement-partnership.md) — 8 workflows

**[VS-98: Contingent, Contract & Outsourced Workforce Management](./VS-98-contingent-contract-outsourced-workforce/README.md)** (24 workflows)

- **PA-98.1** [Contingent Workforce Strategy, Sourcing & Compliance](./VS-98-contingent-contract-outsourced-workforce/PA-98.1-contingent-workforce-strategy-sourcing-compliance.md) — 8 workflows
- **PA-98.2** [Contingent Worker Onboarding, Access & Time Operations](./VS-98-contingent-contract-outsourced-workforce/PA-98.2-contingent-worker-onboarding-access-time-operations.md) — 8 workflows
- **PA-98.3** [Contingent Workforce Performance, Risk & Spend Analytics](./VS-98-contingent-contract-outsourced-workforce/PA-98.3-contingent-workforce-performance-risk-spend-analytics.md) — 8 workflows

**[VS-102: Compensation, Benefits & Total Rewards Strategy](./VS-102-compensation-benefits-total-rewards/README.md)** (24 workflows)

- **PA-102.1** [Job Architecture, Pay Structure & Market Benchmarking](./VS-102-compensation-benefits-total-rewards/PA-102.1-job-architecture-pay-structure-and-market-benchmarking.md) — 8 workflows
- **PA-102.2** [Benefits, Wellness Programs & Statutory Administration](./VS-102-compensation-benefits-total-rewards/PA-102.2-benefits-wellness-programs-and-statutory-administration.md) — 8 workflows
- **PA-102.3** [Variable Pay, Incentives & Total Rewards Strategy](./VS-102-compensation-benefits-total-rewards/PA-102.3-variable-pay-incentives-and-total-rewards-strategy.md) — 8 workflows

**[VS-103: HR Shared Services, Employee Experience & People Analytics](./VS-103-hr-shared-services-employee-experience-people-analytics/README.md)** (24 workflows)

- **PA-103.1** [HR Shared Services & Employee/Manager Self-Service Operations](./VS-103-hr-shared-services-employee-experience-people-analytics/PA-103.1-hr-shared-services-and-employee-manager-self-service-operations.md) — 8 workflows
- **PA-103.2** [Employee Experience, Engagement & Internal Communications](./VS-103-hr-shared-services-employee-experience-people-analytics/PA-103.2-employee-experience-engagement-and-internal-communications.md) — 8 workflows
- **PA-103.3** [People Analytics, Workforce Planning & HR Technology](./VS-103-hr-shared-services-employee-experience-people-analytics/PA-103.3-people-analytics-workforce-planning-and-hr-technology.md) — 8 workflows

**[VS-121: Talent Acquisition, Employer Brand & Candidate Experience](./VS-121-talent-acquisition-employer-brand-candidate-experience/README.md)** (25 workflows)

- **PA-121.1** [Employer Brand, EVP & Talent Marketing Strategy](./VS-121-talent-acquisition-employer-brand-candidate-experience/PA-121.1-employer-brand-evp-and-talent-marketing-strategy.md) — 9 workflows
- **PA-121.2** [Candidate Experience, Sourcing & Selection Operations](./VS-121-talent-acquisition-employer-brand-candidate-experience/PA-121.2-candidate-experience-sourcing-and-selection-operations.md) — 8 workflows
- **PA-121.3** [Talent Community, Campus Pipeline & TA Analytics](./VS-121-talent-acquisition-employer-brand-candidate-experience/PA-121.3-talent-community-campus-pipeline-and-ta-analytics.md) — 8 workflows

**[VS-123: Skilled-Trade Apprenticeship, Vocational Education & Capability Pipeline](./VS-123-skilled-trade-apprenticeship-vocational-education-capability-pipeline/README.md)** (24 workflows)

- **PA-123.1** [Apprenticeship Program Design, TESDA Registration & Governance](./VS-123-skilled-trade-apprenticeship-vocational-education-capability-pipeline/PA-123.1-apprenticeship-program-design-tesda-registration-and-governance.md) — 8 workflows
- **PA-123.2** [Apprenticeship Cohort Operations, Mentorship & Competency Assessment](./VS-123-skilled-trade-apprenticeship-vocational-education-capability-pipeline/PA-123.2-apprenticeship-cohort-operations-mentorship-and-competency-assessment.md) — 8 workflows
- **PA-123.3** [Vocational Partnerships, Instructor Pipeline & Trade Capability Analytics](./VS-123-skilled-trade-apprenticeship-vocational-education-capability-pipeline/PA-123.3-vocational-partnerships-instructor-pipeline-and-trade-capability-analytics.md) — 8 workflows

**[VS-134: Organizational Change Management, Digital Adoption & Transformation Enablement](./VS-134-organizational-change-management-digital-adoption-transformation-enablement/README.md)** (24 workflows)

- **PA-134.1** [OCM Strategy, Governance & Change Readiness Assessment](./VS-134-organizational-change-management-digital-adoption-transformation-enablement/PA-134.1-ocm-strategy-governance-and-change-readiness.md) — 8 workflows
- **PA-134.2** [Change Delivery, Communications & Stakeholder Engagement](./VS-134-organizational-change-management-digital-adoption-transformation-enablement/PA-134.2-change-delivery-communications-and-stakeholder-engagement.md) — 8 workflows
- **PA-134.3** [Digital Adoption, Training & Sustainment Analytics](./VS-134-organizational-change-management-digital-adoption-transformation-enablement/PA-134.3-digital-adoption-training-and-sustainment-analytics.md) — 8 workflows

**[VS-141: Employee Transport, Shuttle & Daily Commute Management](./VS-141-employee-transport-shuttle-and-daily-commute-management/README.md)** (25 workflows)

- **PA-141.1** [Transport Strategy, Policy & Commute-Allowance Framework](./VS-141-employee-transport-shuttle-and-daily-commute-management/PA-141.1-transport-strategy-policy-and-commute-allowance-framework.md) — 8 workflows
- **PA-141.2** [Shuttle Service, Route & Daily Commute Operations](./VS-141-employee-transport-shuttle-and-daily-commute-management/PA-141.2-shuttle-service-route-and-daily-commute-operations.md) — 9 workflows
- **PA-141.3** [Transport Vendor, Safety, Cost & Commute Analytics](./VS-141-employee-transport-shuttle-and-daily-commute-management/PA-141.3-transport-vendor-safety-cost-and-commute-analytics.md) — 8 workflows

**[VS-144: Employee Accommodation, Dormitory & Staff Housing Operations](./VS-144-employee-accommodation-dormitory-and-staff-housing/README.md)** (24 workflows)

- **PA-144.1** [Housing Strategy, Portfolio & Policy Framework](./VS-144-employee-accommodation-dormitory-and-staff-housing/PA-144.1-housing-strategy-portfolio-and-policy-framework.md) — 8 workflows
- **PA-144.2** [Dormitory/Accommodation Operations, Occupancy & Resident Welfare](./VS-144-employee-accommodation-dormitory-and-staff-housing/PA-144.2-dormitory-operations-occupancy-and-resident-welfare.md) — 8 workflows
- **PA-144.3** [Housing Facility Maintenance, Vendor, Cost & Housing Analytics](./VS-144-employee-accommodation-dormitory-and-staff-housing/PA-144.3-housing-facility-maintenance-vendor-cost-and-analytics.md) — 8 workflows

**[VS-150: Drug-Free Workplace & Substance Abuse Program](./VS-150-drug-free-workplace-and-substance-abuse-program/README.md)** (24 workflows)

- **PA-150.1** [Drug-Free Workplace Policy, Framework & DOLE Compliance](./VS-150-drug-free-workplace-and-substance-abuse-program/PA-150.1-drug-free-workplace-policy-framework-and-dole-compliance.md) — 8 workflows
- **PA-150.2** [Drug Testing Operations, Results & Case Management](./VS-150-drug-free-workplace-and-substance-abuse-program/PA-150.2-drug-testing-operations-results-and-case-management.md) — 8 workflows
- **PA-150.3** [Rehabilitation, Return-to-Duty, Privacy & Program Analytics](./VS-150-drug-free-workplace-and-substance-abuse-program/PA-150.3-rehabilitation-return-to-duty-privacy-and-program-analytics.md) — 8 workflows

**[VS-160: Global Mobility, Immigration & Foreign Worker Compliance](./VS-160-global-mobility-immigration-and-foreign-worker-compliance/README.md)** (24 workflows)

- **PA-160.1** [Mobility Strategy, Policy & Assignment Framework](./VS-160-global-mobility-immigration-and-foreign-worker-compliance/PA-160.1-mobility-strategy-policy-and-assignment-framework.md) — 8 workflows
- **PA-160.2** [Immigration, Visa & Foreign-Worker Compliance Operations](./VS-160-global-mobility-immigration-and-foreign-worker-compliance/PA-160.2-immigration-visa-and-foreign-worker-compliance-operations.md) — 8 workflows
- **PA-160.3** [Assignment Administration, Tax/Payroll, Repatriation & Analytics](./VS-160-global-mobility-immigration-and-foreign-worker-compliance/PA-160.3-assignment-administration-tax-payroll-repatriation-and-analytics.md) — 8 workflows

**[VS-167: Workforce Background Screening, Credentialing & Personnel Vetting](./VS-167-workforce-background-screening-credentialing-and-personnel-vetting/README.md)** (24 workflows)

- **PA-167.1** [Screening Program Strategy, Policy & Governance](./VS-167-workforce-background-screening-credentialing-and-personnel-vetting/PA-167.1-screening-program-strategy-policy-and-governance.md) — 8 workflows
- **PA-167.2** [Vetting Operations Across Workforce Categories](./VS-167-workforce-background-screening-credentialing-and-personnel-vetting/PA-167.2-vetting-operations-across-workforce-categories.md) — 8 workflows
- **PA-167.3** [Screening Analytics, Risk & Program Assurance](./VS-167-workforce-background-screening-credentialing-and-personnel-vetting/PA-167.3-screening-analytics-risk-and-program-assurance.md) — 8 workflows

**[VS-169: Employee Uniform, Workwear & PPE-Issuance Program](./VS-169-employee-uniform-workwear-and-ppe-issuance-program/README.md)** (24 workflows)

- **PA-169.1** [Uniform & Workwear Program Strategy, Policy & Sourcing](./VS-169-employee-uniform-workwear-and-ppe-issuance-program/PA-169.1-uniform-workwear-program-strategy-policy-and-sourcing.md) — 8 workflows
- **PA-169.2** [Uniform, Workwear & PPE Issuance, Laundering & Lifecycle Operations](./VS-169-employee-uniform-workwear-and-ppe-issuance-program/PA-169.2-uniform-workwear-ppe-issuance-laundering-and-lifecycle-operations.md) — 8 workflows
- **PA-169.3** [Uniform/PPE Program Analytics, Compliance & Assurance](./VS-169-employee-uniform-workwear-and-ppe-issuance-program/PA-169.3-uniform-ppe-program-analytics-compliance-and-assurance.md) — 8 workflows

**[VS-183: Dual Training System (DTS) & TESDA Partnership Program](./VS-183-dual-training-system-dts-and-tesda-partnership-program/README.md)** (24 workflows)

- **PA-183.1** [DTS Accreditation & TVI Onboarding](./VS-183-dual-training-system-dts-and-tesda-partnership-program/PA-183.1-dts-accreditation-and-tvi-onboarding.md) — 8 workflows
- **PA-183.2** [Student-Trainee Lifecycle & Store Rotation](./VS-183-dual-training-system-dts-and-tesda-partnership-program/PA-183.2-student-trainee-lifecycle-and-store-rotation.md) — 8 workflows
- **PA-183.3** [DTS Tax-Incentive Compliance & Reporting](./VS-183-dual-training-system-dts-and-tesda-partnership-program/PA-183.3-dts-tax-incentive-compliance-and-reporting.md) — 8 workflows

### Asset & Infrastructure

**[VS-20: Real Estate & Construction](./VS-20-real-estate-construction/README.md)** (33 workflows)

- **PA-20.1** [Site Selection & Lease Management](./VS-20-real-estate-construction/PA-20.1-site-selection-and-lease-management.md) — 11 workflows
- **PA-20.2** [Engineering & Construction](./VS-20-real-estate-construction/PA-20.2-engineering-and-construction.md) — 10 workflows
- **PA-20.3** [Facility Maintenance & Equipment](./VS-20-real-estate-construction/PA-20.3-facility-maintenance-and-equipment.md) — 12 workflows

**[VS-35: Fixed Asset Management](./VS-35-fixed-asset-management/README.md)** (24 workflows)

- **PA-35.1** [Asset Registration & Lifecycle Tracking](./VS-35-fixed-asset-management/PA-35.1-asset-registration-lifecycle.md) — 8 workflows
- **PA-35.2** [Depreciation & Financial Reporting](./VS-35-fixed-asset-management/PA-35.2-depreciation-financial-reporting.md) — 8 workflows
- **PA-35.3** [Physical Verification & Disposal](./VS-35-fixed-asset-management/PA-35.3-physical-verification-disposal.md) — 8 workflows

**[VS-42: Property & Lease Administration](./VS-42-property-lease-admin/README.md)** (25 workflows)

- **PA-42.1** [Lease Negotiation & Administration](./VS-42-property-lease-admin/PA-42.1-lease-negotiation-administration.md) — 8 workflows
- **PA-42.2** [Rent Payment, Escalation & CAM Reconciliation](./VS-42-property-lease-admin/PA-42.2-rent-payment-escalation.md) — 8 workflows
- **PA-42.3** [Property Tax, LGU Compliance & Lease Accounting](./VS-42-property-lease-admin/PA-42.3-property-tax-compliance.md) — 9 workflows

**[VS-59: Store Closure & Decommissioning](./VS-59-store-closure-decommissioning/README.md)** (24 workflows)

- **PA-59.1** [Store Closure Decision & Planning](./VS-59-store-closure-decommissioning/PA-59.1-store-closure-decision-planning.md) — 8 workflows
- **PA-59.2** [Store Wind-Down & Asset Recovery](./VS-59-store-closure-decommissioning/PA-59.2-store-wind-down-asset-recovery.md) — 8 workflows
- **PA-59.3** [Staff Redeployment & Post-Closure Analytics](./VS-59-store-closure-decommissioning/PA-59.3-staff-redeployment-post-closure.md) — 8 workflows

**[VS-97: Corporate Real Estate & Property Portfolio Management](./VS-97-corporate-real-estate-property-portfolio/README.md)** (24 workflows)

- **PA-97.1** [Property Acquisition, Investment & Portfolio Strategy](./VS-97-corporate-real-estate-property-portfolio/PA-97.1-property-acquisition-investment-portfolio-strategy.md) — 8 workflows
- **PA-97.2** [Landlord Leasing Operations & Tenant Management](./VS-97-corporate-real-estate-property-portfolio/PA-97.2-landlord-leasing-tenant-management.md) — 8 workflows
- **PA-97.3** [Property Accounting, Compliance & Portfolio Analytics](./VS-97-corporate-real-estate-property-portfolio/PA-97.3-property-accounting-compliance-portfolio-analytics.md) — 8 workflows

**[VS-108: On-Site Renewable Energy & Prosumer Asset Operations](./VS-108-onsite-renewable-energy-prosumer-asset-operations/README.md)** (24 workflows)

- **PA-108.1** [Renewable Generation Investment, Capex & Project Development](./VS-108-onsite-renewable-energy-prosumer-asset-operations/PA-108.1-renewable-generation-investment-capex-and-project-development.md) — 8 workflows
- **PA-108.2** [Generation Operations, Grid Interaction & Net-Metering](./VS-108-onsite-renewable-energy-prosumer-asset-operations/PA-108.2-generation-operations-grid-interaction-and-net-metering.md) — 8 workflows
- **PA-108.3** [Renewable Asset Performance, REC & Decarbonization Analytics](./VS-108-onsite-renewable-energy-prosumer-asset-operations/PA-108.3-renewable-asset-performance-rec-and-decarbonization-analytics.md) — 8 workflows

**[VS-109: Store Remodel, Renovation & Lifecycle Refurbishment Program](./VS-109-store-remodel-renovation-lifecycle-refurbishment/README.md)** (24 workflows)

- **PA-109.1** [Remodel Strategy, Portfolio Planning & Scope Definition](./VS-109-store-remodel-renovation-lifecycle-refurbishment/PA-109.1-remodel-strategy-portfolio-planning-and-scope-definition.md) — 8 workflows
- **PA-109.2** [Remodel Design, Procurement & Construction Execution](./VS-109-store-remodel-renovation-lifecycle-refurbishment/PA-109.2-remodel-design-procurement-and-construction-execution.md) — 8 workflows
- **PA-109.3** [Re-merchandising, Re-opening & Remodel Performance Analytics](./VS-109-store-remodel-renovation-lifecycle-refurbishment/PA-109.3-re-merchandising-reopening-and-remodel-performance-analytics.md) — 8 workflows

**[VS-112: Corporate Project & Program Management Office (PMO)](./VS-112-corporate-project-and-program-management-office/README.md)** (24 workflows)

- **PA-112.1** [Project Portfolio Governance, Prioritization & Stage-Gate](./VS-112-corporate-project-and-program-management-office/PA-112.1-project-portfolio-governance-prioritization-and-stage-gate.md) — 8 workflows
- **PA-112.2** [Program & Project Delivery Management, Resource & Capacity](./VS-112-corporate-project-and-program-management-office/PA-112.2-program-and-project-delivery-resource-and-capacity.md) — 8 workflows
- **PA-112.3** [Project Benefits Realization, PMIS & PMO Analytics](./VS-112-corporate-project-and-program-management-office/PA-112.3-project-benefits-realization-pmis-and-pmo-analytics.md) — 8 workflows

**[VS-120: Energy Efficiency, Conservation & RA 11285 Compliance Program](./VS-120-energy-efficiency-conservation-and-ra-11285-compliance-program/README.md)** (24 workflows)

- **PA-120.1** [EEC Program Strategy, Designated-Establishment & Governance](./VS-120-energy-efficiency-conservation-and-ra-11285-compliance-program/PA-120.1-eec-program-strategy-designated-establishment-and-governance.md) — 8 workflows
- **PA-120.2** [Energy Audit, Measurement & Conservation Plan Management](./VS-120-energy-efficiency-conservation-and-ra-11285-compliance-program/PA-120.2-energy-audit-measurement-and-conservation-plan-management.md) — 8 workflows
- **PA-120.3** [ECM Delivery, Performance Optimization & Compliance Analytics](./VS-120-energy-efficiency-conservation-and-ra-11285-compliance-program/PA-120.3-ecm-delivery-performance-optimization-and-compliance-analytics.md) — 8 workflows

**[VS-138: Integrated Facilities Management, Workplace Services & Building Automation](./VS-138-integrated-facilities-management-workplace-services-and-building-automation/README.md)** (24 workflows)

- **PA-138.1** [Facilities Management Strategy, IFM Provider & SLA Governance](./VS-138-integrated-facilities-management-workplace-services-and-building-automation/PA-138.1-facilities-management-strategy-ifm-provider-and-sla-governance.md) — 8 workflows
- **PA-138.2** [Hard & Soft FM Service Operations (Cleaning, Pest, Security, Grounds, Workplace)](./VS-138-integrated-facilities-management-workplace-services-and-building-automation/PA-138.2-hard-and-soft-fm-service-operations.md) — 8 workflows
- **PA-138.3** [Building Automation, Energy Control & Facilities Analytics](./VS-138-integrated-facilities-management-workplace-services-and-building-automation/PA-138.3-building-automation-energy-control-and-facilities-analytics.md) — 8 workflows


**[VS-178: Landbanking, Site Acquisition & Agrarian/LGU Zoning Conversion Operations](./VS-178-landbanking-site-acquisition-and-agrarian-lgu-zoning-conversion/README.md)** (25 workflows)

- **PA-178.1** [Land Feasibility, Site Acquisition & Title Consolidation](./VS-178-landbanking-site-acquisition-and-agrarian-lgu-zoning-conversion/PA-178.1-land-feasibility-site-acquisition-title-consolidation.md) — 9 workflows
- **PA-178.2** [Agrarian Reform, NCIP Ancestral Domain & Land Use Conversion Operations](./VS-178-landbanking-site-acquisition-and-agrarian-lgu-zoning-conversion/PA-178.2-agrarian-reform-ncip-ancestral-domain-land-use-conversion-operations.md) — 8 workflows
- **PA-178.3** [Property Joint-Ventures, LGU Zoning Compliance & Site Development Governance](./VS-178-landbanking-site-acquisition-and-agrarian-lgu-zoning-conversion/PA-178.3-property-joint-ventures-lgu-zoning-compliance-site-development-governance.md) — 8 workflows

**[VS-184: Post-Disaster Store Infrastructure Reconstruction & Rehabilitation](./VS-184-post-disaster-store-infrastructure-reconstruction-and-rehabilitation/README.md)** (24 workflows)

- **PA-184.1** [Structural Damage & Insurance Appraisal Coordination](./VS-184-post-disaster-store-infrastructure-reconstruction-and-rehabilitation/PA-184.1-structural-damage-and-insurance-appraisal-coordination.md) — 8 workflows
- **PA-184.2** [Rebuilding Project Execution & Safety Clearance](./VS-184-post-disaster-store-infrastructure-reconstruction-and-rehabilitation/PA-184.2-rebuilding-project-execution-and-safety-clearance.md) — 8 workflows
- **PA-184.3** [Temporary Facility & Parking Lot Sales Mobilization](./VS-184-post-disaster-store-infrastructure-reconstruction-and-rehabilitation/PA-184.3-temporary-facility-and-parking-lot-sales-mobilization.md) — 8 workflows

**[VS-163: Electric Vehicle (EV) Charging Station Host Network Operations](./VS-163-electric-vehicle-ev-charging-station-host-network-operations/README.md)** (24 workflows)

- **PA-163.1** [Charging Network Strategy, Siting & Host Partnering](./VS-163-electric-vehicle-ev-charging-station-host-network-operations/PA-163.1-charging-network-strategy-siting-and-host-partnering.md) — 8 workflows
- **PA-163.2** [Station Deployment, Energy Integration & Roaming/Payment](./VS-163-electric-vehicle-ev-charging-station-host-network-operations/PA-163.2-station-deployment-energy-integration-and-roaming-payment.md) — 8 workflows
- **PA-163.3** [Operations, Maintenance, Compliance & Network Analytics](./VS-163-electric-vehicle-ev-charging-station-host-network-operations/PA-163.3-operations-maintenance-compliance-and-network-analytics.md) — 8 workflows

### Governance & Assurance

**[VS-21: Internal Audit & Risk](./VS-21-internal-audit-risk/README.md)** (49 workflows)

- **PA-21.1** [Audit Planning & Execution](./VS-21-internal-audit-risk/PA-21.1-audit-planning-and-execution.md) — 26 workflows
- **PA-21.2** [Enterprise Risk Management](./VS-21-internal-audit-risk/PA-21.2-enterprise-risk-management.md) — 10 workflows
- **PA-21.3** [Specialized Audit Domains](./VS-21-internal-audit-risk/PA-21.3-specialized-audit-domains.md) — 13 workflows

**[VS-22: Compliance & Regulatory](./VS-22-compliance-regulatory/README.md)** (57 workflows)

- **PA-22.1** [Regulatory Permits & Licenses](./VS-22-compliance-regulatory/PA-22.1-regulatory-permits-and-licenses.md) — 32 workflows
- **PA-22.2** [Government Audit & Inspection Response](./VS-22-compliance-regulatory/PA-22.2-government-audit-and-inspection-response.md) — 15 workflows
- **PA-22.3** [Regulatory Change Management](./VS-22-compliance-regulatory/PA-22.3-regulatory-change-management.md) — 10 workflows

**[VS-23: Loss Prevention & Asset Protection](./VS-23-loss-prevention/README.md)** (29 workflows)

- **PA-23.1** [Exception Monitoring & Investigation](./VS-23-loss-prevention/PA-23.1-exception-monitoring-and-investigation.md) — 10 workflows
- **PA-23.2** [Physical Security & Surveillance](./VS-23-loss-prevention/PA-23.2-physical-security-and-surveillance.md) — 10 workflows
- **PA-23.3** [Shrinkage Reduction](./VS-23-loss-prevention/PA-23.3-shrinkage-reduction.md) — 9 workflows

**[VS-24: Health, Safety & Environment](./VS-24-health-safety-environment/README.md)** (31 workflows)

- **PA-24.1** [Occupational Health & Safety](./VS-24-health-safety-environment/PA-24.1-occupational-health-and-safety.md) — 13 workflows
- **PA-24.2** [Emergency Preparedness](./VS-24-health-safety-environment/PA-24.2-emergency-preparedness.md) — 11 workflows
- **PA-24.3** [Hazmat Management](./VS-24-health-safety-environment/PA-24.3-hazmat-management.md) — 7 workflows

**[VS-25: ESG & Sustainability](./VS-25-esg-sustainability/README.md)** (31 workflows)

- **PA-25.1** [Environmental Monitoring](./VS-25-esg-sustainability/PA-25.1-environmental-monitoring.md) — 14 workflows
- **PA-25.2** [Social Impact & Governance](./VS-25-esg-sustainability/PA-25.2-social-impact-and-governance.md) — 9 workflows
- **PA-25.3** [ESG Reporting & Compliance](./VS-25-esg-sustainability/PA-25.3-esg-reporting-and-compliance.md) — 8 workflows

**[VS-26: Business Continuity & Insurance](./VS-26-business-continuity-insurance/README.md)** (31 workflows)

- **PA-26.1** [BCP Planning & Testing](./VS-26-business-continuity-insurance/PA-26.1-bcp-planning-and-testing.md) — 10 workflows
- **PA-26.2** [Crisis Response & Recovery](./VS-26-business-continuity-insurance/PA-26.2-crisis-response-and-recovery.md) — 11 workflows
- **PA-26.3** [Insurance Claims & Policy Management](./VS-26-business-continuity-insurance/PA-26.3-insurance-claims-and-policy-management.md) — 10 workflows

**[VS-31: Quality Management & Product Compliance](./VS-31-quality-management/README.md)** (23 workflows)

- **PA-31.1** [Incoming Quality Inspection & Control](./VS-31-quality-management/PA-31.1-incoming-quality-inspection.md) — 8 workflows
- **PA-31.2** [Vendor Quality Management & Audit](./VS-31-quality-management/PA-31.2-vendor-quality-audit.md) — 7 workflows
- **PA-31.3** [Product Recall & Safety Compliance](./VS-31-quality-management/PA-31.3-product-recall-safety-compliance.md) — 8 workflows

**[VS-33: Strategic Planning & Corporate Performance Management](./VS-33-strategic-planning/README.md)** (23 workflows)

- **PA-33.1** [Annual Business Planning & Budgeting](./VS-33-strategic-planning/PA-33.1-annual-business-planning.md) — 8 workflows
- **PA-33.2** [Corporate Performance Management](./VS-33-strategic-planning/PA-33.2-corporate-performance-management.md) — 8 workflows
- **PA-33.3** [Competitive Intelligence & Market Analysis](./VS-33-strategic-planning/PA-33.3-competitive-intelligence.md) — 7 workflows

**[VS-36: Corporate Governance & Board Management](./VS-36-corporate-governance/README.md)** (25 workflows)

- **PA-36.1** [Board Meeting Management & Corporate Records](./VS-36-corporate-governance/PA-36.1-board-meeting-corporate-records.md) — 10 workflows
- **PA-36.2** [Shareholder & Equity Management](./VS-36-corporate-governance/PA-36.2-shareholder-equity-management.md) — 7 workflows
- **PA-36.3** [Corporate Policy & Entity Governance](./VS-36-corporate-governance/PA-36.3-corporate-policy-entity-governance.md) — 8 workflows

**[VS-69: Typhoon & Natural Disaster Preparedness & Response](./VS-69-typhoon-disaster-response/README.md)** (24 workflows)

- **PA-69.1** [Typhoon Preparedness & Early Warning Operations](./VS-69-typhoon-disaster-response/PA-69.1-typhoon-preparedness-early-warning.md) — 8 workflows
- **PA-69.2** [Active Disaster Response & Emergency Operations](./VS-69-typhoon-disaster-response/PA-69.2-disaster-active-response-operations.md) — 8 workflows
- **PA-69.3** [Post-Disaster Recovery & Community Support](./VS-69-typhoon-disaster-response/PA-69.3-post-disaster-recovery-community-support.md) — 8 workflows

**[VS-71: Anti-Counterfeit & Product Authentication](./VS-71-anti-counterfeit-authentication/README.md)** (24 workflows)

- **PA-71.1** [Product Authentication & Serialization](./VS-71-anti-counterfeit-authentication/PA-71.1-product-authentication-serialization.md) — 8 workflows
- **PA-71.2** [Counterfeit Detection & Investigation](./VS-71-anti-counterfeit-authentication/PA-71.2-counterfeit-detection-investigation.md) — 8 workflows
- **PA-71.3** [Vendor Compliance & Anti-Counterfeit Analytics](./VS-71-anti-counterfeit-authentication/PA-71.3-vendor-compliance-anti-counterfeit-analytics.md) — 8 workflows

**[VS-73: Store-Level Waste Management & Circular Economy](./VS-73-store-waste-circular-economy/README.md)** (24 workflows)

- **PA-73.1** [Store Waste Segregation & Collection](./VS-73-store-waste-circular-economy/PA-73.1-store-waste-segregation-collection.md) — 8 workflows
- **PA-73.2** [Hazardous Waste & DENR Compliance](./VS-73-store-waste-circular-economy/PA-73.2-hazardous-waste-denr-compliance.md) — 8 workflows
- **PA-73.3** [Circular Economy & Recycling Analytics](./VS-73-store-waste-circular-economy/PA-73.3-circular-economy-recycling-analytics.md) — 8 workflows

**[VS-76: Philippine Multi-Region LGU & Local Regulatory Compliance](./VS-76-multi-region-lgu-compliance/README.md)** (24 workflows)

- **PA-76.1** [Multi-LGU Business Permit & License Management](./VS-76-multi-region-lgu-compliance/PA-76.1-multi-lgu-business-permit-license-management.md) — 8 workflows
- **PA-76.2** [Local Tax & Regulatory Variation Management](./VS-76-multi-region-lgu-compliance/PA-76.2-local-tax-regulatory-variation-management.md) — 8 workflows
- **PA-76.3** [LGU Relationship & Regulatory Analytics](./VS-76-multi-region-lgu-compliance/PA-76.3-lgu-relationship-regulatory-analytics.md) — 8 workflows

**[VS-85: Mandatory Discount, Eligibility & Tax Credit Recovery](./VS-85-mandatory-discount-eligibility-tax-credit/README.md)** (24 workflows)

- **PA-85.1** [SC/PWD/Solo Parent Eligibility & In-Store Discount Program](./VS-85-mandatory-discount-eligibility-tax-credit/PA-85.1-scpwd-soloparent-eligibility-indiscount.md) — 8 workflows
- **PA-85.2** [VAT-Exempt & Zero-Rated Customer Certification](./VS-85-mandatory-discount-eligibility-tax-credit/PA-85.2-vatexempt-zero-rated-certification.md) — 8 workflows
- **PA-85.3** [Tax Credit Recovery, Registry Reporting & Audit Defense](./VS-85-mandatory-discount-eligibility-tax-credit/PA-85.3-tax-credit-recovery-registry-audit.md) — 8 workflows

**[VS-86: Anti-Financial Crime, AML/KYC & Anti-Corruption](./VS-86-anti-financial-crime-aml-abc/README.md)** (24 workflows)

- **PA-86.1** [KYC, Customer Due Diligence & PEP/Sanctions Screening](./VS-86-anti-financial-crime-aml-abc/PA-86.1-kyc-cdd-pep-sanctions-screening.md) — 8 workflows
- **PA-86.2** [AML Transaction Monitoring & STR/CTR Reporting (AMLC)](./VS-86-anti-financial-crime-aml-abc/PA-86.2-aml-transaction-monitoring-strctr.md) — 8 workflows
- **PA-86.3** [Anti-Bribery, Gifts & Conflict of Interest Management](./VS-86-anti-financial-crime-aml-abc/PA-86.3-antibribery-gifts-conflict-of-interest.md) — 8 workflows

**[VS-87: Customs Trade Compliance & Tariff Optimization](./VS-87-customs-trade-compliance-tariff/README.md)** (25 workflows)

- **PA-87.1** [Tariff Classification, Origin & Valuation](./VS-87-customs-trade-compliance-tariff/PA-87.1-tariff-classification-origin-valuation.md) — 8 workflows
- **PA-87.2** [FTA Preference, Duty Drawback & Bonded Operations](./VS-87-customs-trade-compliance-tariff/PA-87.2-fta-preference-duty-drawback-bonded.md) — 8 workflows
- **PA-87.3** [Trade Compliance Audit, Broker Governance & ADC](./VS-87-customs-trade-compliance-tariff/PA-87.3-trade-compliance-audit-broker-governance.md) — 9 workflows

**[VS-88: Document Control, Records Management & Retention](./VS-88-document-control-records-retention/README.md)** (24 workflows)

- **PA-88.1** [Document Classification, Versioning & Taxonomy](./VS-88-document-control-records-retention/PA-88.1-document-classification-versioning-taxonomy.md) — 8 workflows
- **PA-88.2** [Retention, Legal Hold & Secure Disposition](./VS-88-document-control-records-retention/PA-88.2-retention-legal-hold-disposition.md) — 8 workflows
- **PA-88.3** [Records Compliance, e-Discovery & BIR/SEC/NPC Audit](./VS-88-document-control-records-retention/PA-88.3-records-compliance-ediscovery-audit.md) — 8 workflows

**[VS-89: Product Recall & Safety Corrective Action Management](./VS-89-product-recall-safety-corrective-action/README.md)** (25 workflows)

- **PA-89.1** [Recall Initiation, Risk Assessment & Regulatory Notification](./VS-89-product-recall-safety-corrective-action/PA-89.1-recall-initiation-risk-assessment-regulatory-notification.md) — 9 workflows
- **PA-89.2** [Recall Execution, Customer Notification & Product Retrieval](./VS-89-product-recall-safety-corrective-action/PA-89.2-recall-execution-customer-notification-retrieval.md) — 8 workflows
- **PA-89.3** [Recall Resolution, Reimbursement & Root Cause / CAPA](./VS-89-product-recall-safety-corrective-action/PA-89.3-recall-resolution-reimbursement-root-cause-capa.md) — 8 workflows

**[VS-91: Consumer Data Privacy & Data Protection Program](./VS-91-consumer-data-privacy-protection/README.md)** (24 workflows)

- **PA-91.1** [Privacy Governance, Consent & Data Subject Rights Fulfillment](./VS-91-consumer-data-privacy-protection/PA-91.1-privacy-governance-consent-data-subject-rights.md) — 8 workflows
- **PA-91.2** [Privacy Impact Assessment, Data Mapping & Vendor Privacy Due Diligence](./VS-91-consumer-data-privacy-protection/PA-91.2-privacy-impact-assessment-data-mapping-vendor-privacy.md) — 8 workflows
- **PA-91.3** [Breach Detection, Notification & NPC Regulatory Response](./VS-91-consumer-data-privacy-protection/PA-91.3-breach-detection-notification-npc-response.md) — 8 workflows

**[VS-100: Legal Operations, Litigation & Intellectual Property Management](./VS-100-legal-operations-litigation-ip-management/README.md)** (25 workflows)

- **PA-100.1** [Legal Matter, Case & Outside Counsel Management](./VS-100-legal-operations-litigation-ip-management/PA-100.1-legal-matter-case-outside-counsel-management.md) — 8 workflows
- **PA-100.2** [Intellectual Property Portfolio & Brand Protection](./VS-100-legal-operations-litigation-ip-management/PA-100.2-intellectual-property-portfolio-brand-protection.md) — 9 workflows
- **PA-100.3** [Corporate Legal Advisory, Contracts & Risk Governance](./VS-100-legal-operations-litigation-ip-management/PA-100.3-corporate-legal-advisory-contracts-risk-governance.md) — 8 workflows

**[VS-104: Government Affairs, Public Policy & Industry Relations](./VS-104-government-affairs-public-policy-industry-relations/README.md)** (24 workflows)

- **PA-104.1** [National Government Relations & Public Policy Advocacy](./VS-104-government-affairs-public-policy-industry-relations/PA-104.1-national-government-relations-and-public-policy-advocacy.md) — 8 workflows
- **PA-104.2** [Industry & Trade Association Relations](./VS-104-government-affairs-public-policy-industry-relations/PA-104.2-industry-and-trade-association-relations.md) — 8 workflows
- **PA-104.3** [Public Affairs, Community Relations & Reputation](./VS-104-government-affairs-public-policy-industry-relations/PA-104.3-public-affairs-community-relations-and-reputation.md) — 8 workflows

**[VS-114: Dangerous Goods (DG) & Hazmat Transport, Ecommerce & Regulatory Compliance](./VS-114-dangerous-goods-hazmat-transport-ecommerce-regulatory-compliance/README.md)** (24 workflows)

- **PA-114.1** [DG Classification, Inventory & Program Governance](./VS-114-dangerous-goods-hazmat-transport-ecommerce-regulatory-compliance/PA-114.1-dg-classification-inventory-and-program-governance.md) — 8 workflows
- **PA-114.2** [DG Transport, Carrier & Ecommerce Shipping Compliance](./VS-114-dangerous-goods-hazmat-transport-ecommerce-regulatory-compliance/PA-114.2-dg-transport-carrier-and-ecommerce-shipping-compliance.md) — 8 workflows
- **PA-114.3** [DG Storage/Handling Safety, Incident Response & Regulatory Compliance](./VS-114-dangerous-goods-hazmat-transport-ecommerce-regulatory-compliance/PA-114.3-dg-storage-handling-incident-and-regulatory-compliance.md) — 8 workflows

**[VS-117: DTI-BPS Product Standards Certification & PS Mark/ICC Compliance](./VS-117-dti-bps-product-standards-certification-ps-mark-icc-compliance/README.md)** (24 workflows)

- **PA-117.1** [PS Mark Licensing, Vendor Certification & Product Standards Governance](./VS-117-dti-bps-product-standards-certification-ps-mark-icc-compliance/PA-117.1-ps-mark-licensing-vendor-certification-and-product-standards-governance.md) — 8 workflows
- **PA-117.2** [Import ICC/SOC Clearance, Testing Lab & Sticker Management](./VS-117-dti-bps-product-standards-certification-ps-mark-icc-compliance/PA-117.2-import-icc-soc-clearance-testing-lab-and-sticker-management.md) — 8 workflows
- **PA-117.3** [Market Surveillance, Compliance Monitoring & Certification Analytics](./VS-117-dti-bps-product-standards-certification-ps-mark-icc-compliance/PA-117.3-market-surveillance-compliance-monitoring-and-certification-analytics.md) — 8 workflows

**[VS-119: Whistleblower, Ethics & Corporate Integrity (Speak-Up) Program](./VS-119-whistleblower-ethics-and-corporate-integrity-speak-up-program/README.md)** (24 workflows)

- **PA-119.1** [Ethics Governance, Speak-Up Channel & Intake Operations](./VS-119-whistleblower-ethics-and-corporate-integrity-speak-up-program/PA-119.1-ethics-governance-speak-up-channel-and-intake-operations.md) — 8 workflows
- **PA-119.2** [Investigation, Case Management & Retaliation Protection](./VS-119-whistleblower-ethics-and-corporate-integrity-speak-up-program/PA-119.2-investigation-case-management-and-retaliation-protection.md) — 8 workflows
- **PA-119.3** [Ethics Analytics, Culture & Program Assurance](./VS-119-whistleblower-ethics-and-corporate-integrity-speak-up-program/PA-119.3-ethics-analytics-culture-and-program-assurance.md) — 8 workflows

**[VS-129: Competition & Antitrust Compliance (RA 10667 / PCC)](./VS-129-competition-and-antitrust-compliance/README.md)** (24 workflows)

- **PA-129.1** [Competition Risk Assessment, Market Power & Exposure Analysis](./VS-129-competition-and-antitrust-compliance/PA-129.1-competition-risk-assessment-market-power-and-exposure-analysis.md) — 8 workflows
- **PA-129.2** [Anti-Competitive Conduct Prevention & Compliance Controls](./VS-129-competition-and-antitrust-compliance/PA-129.2-anticompetitive-conduct-prevention-and-compliance-controls.md) — 8 workflows
- **PA-129.3** [Competition Authority (PCC) Engagement, Investigation & Remediation](./VS-129-competition-and-antitrust-compliance/PA-129.3-pcc-engagement-investigation-and-remediation.md) — 8 workflows

**[VS-130: Corporate Development, Mergers, Acquisitions, Divestiture & Strategic Transactions](./VS-130-corporate-development-ma-divestiture/README.md)** (24 workflows)

- **PA-130.1** [Corporate Development Strategy, Pipeline & Target Identification](./VS-130-corporate-development-ma-divestiture/PA-130.1-corporate-development-strategy-pipeline-and-target-identification.md) — 8 workflows
- **PA-130.2** [Transaction Due Diligence, Valuation & Deal Structuring](./VS-130-corporate-development-ma-divestiture/PA-130.2-transaction-due-diligence-valuation-and-deal-structuring.md) — 8 workflows
- **PA-130.3** [Integration, Carve-Out, Divestiture & Post-Merger Performance](./VS-130-corporate-development-ma-divestiture/PA-130.3-integration-carveout-divestiture-and-postmerger-performance.md) — 8 workflows

**[VS-132: Corporate Political Engagement, Election Compliance & Public Affairs Governance](./VS-132-corporate-political-engagement-election-compliance/README.md)** (24 workflows)

- **PA-132.1** [Political Engagement Policy, Governance & Risk Assessment](./VS-132-corporate-political-engagement-election-compliance/PA-132.1-political-engagement-policy-governance-and-risk-assessment.md) — 8 workflows
- **PA-132.2** [Election-Period Compliance, Political Contributions & Lobbying Controls](./VS-132-corporate-political-engagement-election-compliance/PA-132.2-election-compliance-political-contributions-and-lobbying-controls.md) — 8 workflows
- **PA-132.3** [Stakeholder & Government Affairs Governance, Monitoring & Analytics](./VS-132-corporate-political-engagement-election-compliance/PA-132.3-stakeholder-and-government-affairs-governance-monitoring-and-analytics.md) — 8 workflows

**[VS-133: Operational Excellence, Process Mining & Continuous Improvement Program](./VS-133-operational-excellence-process-mining-continuous-improvement/README.md)** (24 workflows)

- **PA-133.1** [OpEx Strategy, Governance & Improvement Methodology](./VS-133-operational-excellence-process-mining-continuous-improvement/PA-133.1-opex-strategy-governance-and-improvement-methodology.md) — 8 workflows
- **PA-133.2** [Process Mining, Process Analysis & Improvement Project Execution](./VS-133-operational-excellence-process-mining-continuous-improvement/PA-133.2-process-mining-analysis-and-improvement-execution.md) — 8 workflows
- **PA-133.3** [Productivity, Benefit Realization & OpEx Analytics](./VS-133-operational-excellence-process-mining-continuous-improvement/PA-133.3-productivity-benefit-realization-and-opex-analytics.md) — 8 workflows

**[VS-146: Customer Mystery Shopping & Service Quality Assurance Program](./VS-146-customer-mystery-shopping-and-service-quality-assurance/README.md)** (24 workflows)

- **PA-146.1** [Service-Quality Assurance Strategy, Standards & Program Design](./VS-146-customer-mystery-shopping-and-service-quality-assurance/PA-146.1-service-quality-assurance-strategy-standards-and-design.md) — 8 workflows
- **PA-146.2** [Mystery Shopping, Service Audit & Measurement Operations](./VS-146-customer-mystery-shopping-and-service-quality-assurance/PA-146.2-mystery-shopping-service-audit-and-measurement-operations.md) — 8 workflows
- **PA-146.3** [Findings Remediation, Recognition & Service-Quality Analytics](./VS-146-customer-mystery-shopping-and-service-quality-assurance/PA-146.3-findings-remediation-recognition-and-service-quality-analytics.md) — 8 workflows

**[VS-147: Customer Safety, Premises Liability & In-Store Risk Management](./VS-147-customer-safety-premises-liability-and-in-store-risk-management/README.md)** (26 workflows)

- **PA-147.1** [Customer Safety Risk Strategy, Standards & Premises-Liability Framework](./VS-147-customer-safety-premises-liability-and-in-store-risk-management/PA-147.1-customer-safety-risk-strategy-standards-and-premises-liability-framework.md) — 8 workflows
- **PA-147.2** [In-Store Customer Safety Operations & Hazard Control](./VS-147-customer-safety-premises-liability-and-in-store-risk-management/PA-147.2-in-store-customer-safety-operations-and-hazard-control.md) — 9 workflows
- **PA-147.3** [Customer Incident Response, Claims & Safety Analytics](./VS-147-customer-safety-premises-liability-and-in-store-risk-management/PA-147.3-customer-incident-response-claims-and-safety-analytics.md) — 9 workflows

**[VS-152: Corporate Social Responsibility, Foundation & Community Investment](./VS-152-corporate-social-responsibility-foundation-and-community-investment/README.md)** (24 workflows)

- **PA-152.1** [CSR Strategy, Governance & Foundation Operations](./VS-152-corporate-social-responsibility-foundation-and-community-investment/PA-152.1-csr-strategy-governance-and-foundation-operations.md) — 8 workflows
- **PA-152.2** [Community Investment, Disaster Response & Volunteer Programs](./VS-152-corporate-social-responsibility-foundation-and-community-investment/PA-152.2-community-investment-disaster-response-and-volunteer-programs.md) — 8 workflows
- **PA-152.3** [CSR Impact Measurement, Reporting & Stakeholder Engagement](./VS-152-corporate-social-responsibility-foundation-and-community-investment/PA-152.3-csr-impact-measurement-reporting-and-stakeholder-engagement.md) — 8 workflows

**[VS-159: Corporate Security, Executive Protection & Travel Risk Management](./VS-159-corporate-security-executive-protection-and-travel-risk-management/README.md)** (24 workflows)

- **PA-159.1** [Corporate Security Strategy, Threat Intelligence & Risk Framework](./VS-159-corporate-security-executive-protection-and-travel-risk-management/PA-159.1-corporate-security-strategy-threat-intelligence-and-risk-framework.md) — 8 workflows
- **PA-159.2** [Executive Protection, Principal Travel & Event Security](./VS-159-corporate-security-executive-protection-and-travel-risk-management/PA-159.2-executive-protection-principal-travel-and-event-security.md) — 8 workflows
- **PA-159.3** [Investigations, Insider Threat, Workplace Violence & Crisis Response](./VS-159-corporate-security-executive-protection-and-travel-risk-management/PA-159.3-investigations-insider-threat-workplace-violence-and-crisis-response.md) — 8 workflows

**[VS-161: Third-Party & Supplier Risk Management (TPRM)](./VS-161-third-party-and-supplier-risk-management-tprm/README.md)** (24 workflows)

- **PA-161.1** [Third-Party Inventory, Tiering & Cross-Domain Risk Framework](./VS-161-third-party-and-supplier-risk-management-tprm/PA-161.1-third-party-inventory-tiering-and-cross-domain-risk-framework.md) — 8 workflows
- **PA-161.2** [Due Diligence, Continuous Monitoring & Evidence Lifecycle](./VS-161-third-party-and-supplier-risk-management-tprm/PA-161.2-due-diligence-continuous-monitoring-and-evidence-lifecycle.md) — 8 workflows
- **PA-161.3** [Concentration, Resilience, Exit & TPRM Governance/Analytics](./VS-161-third-party-and-supplier-risk-management-tprm/PA-161.3-concentration-resilience-exit-and-tprm-governance-analytics.md) — 8 workflows

**[VS-165: PCAB Contractor Licensing & RA 4566 Construction Contractor Compliance](./VS-165-pcab-contractor-licensing-and-ra-4566-construction-contractor-compliance/README.md)** (24 workflows)

- **PA-165.1** [PCAB Licensing Strategy, Entity Registration & Lifecycle](./VS-165-pcab-contractor-licensing-and-ra-4566-construction-contractor-compliance/PA-165.1-pcab-licensing-strategy-entity-registration-and-lifecycle.md) — 8 workflows
- **PA-165.2** [Project Registration, Bonding & Statutory Contractor Compliance](./VS-165-pcab-contractor-licensing-and-ra-4566-construction-contractor-compliance/PA-165.2-project-registration-bonding-and-statutory-contractor-compliance.md) — 8 workflows
- **PA-165.3** [Contractor Compliance, Inspection Response & Analytics](./VS-165-pcab-contractor-licensing-and-ra-4566-construction-contractor-compliance/PA-165.3-contractor-compliance-inspection-response-and-analytics.md) — 8 workflows


**[VS-179: Extended Producer Responsibility (EPR) Compliance & Plastic Recovery Network](./VS-179-extended-producer-responsibility-compliance-and-plastic-recovery-network/README.md)** (24 workflows)

- **PA-179.1** [Plastic Footprint Auditing, ERP Packaging Modeling & Registration](./VS-179-extended-producer-responsibility-compliance-and-plastic-recovery-network/PA-179.1-plastic-footprint-auditing-erp-packaging-modeling-registration.md) — 8 workflows
- **PA-179.2** [Outbound Plastic Recovery Partnerships & Waste-to-Energy Co-Processing](./VS-179-extended-producer-responsibility-compliance-and-plastic-recovery-network/PA-179.2-outbound-plastic-recovery-partnerships-waste-to-energy-co-processing.md) — 8 workflows
- **PA-179.3** [EPR Credit Trading, Compliance Auditing & Annual Reporting](./VS-179-extended-producer-responsibility-compliance-and-plastic-recovery-network/PA-179.3-epr-credit-trading-compliance-auditing-annual-reporting.md) — 8 workflows

**[VS-166: Regulatory License, Permit & Accreditation Portfolio Management](./VS-166-regulatory-license-permit-and-accreditation-portfolio-management/README.md)** (24 workflows)

- **PA-166.1** [Portfolio Strategy, Inventory, Governance & Regulatory Intelligence](./VS-166-regulatory-license-permit-and-accreditation-portfolio-management/PA-166.1-portfolio-strategy-inventory-governance-and-regulatory-intelligence.md) — 8 workflows
- **PA-166.2** [Renewal Execution, Inspection Coordination & Multi-Site Campaigns](./VS-166-regulatory-license-permit-and-accreditation-portfolio-management/PA-166.2-renewal-execution-inspection-coordination-and-multi-site-campaigns.md) — 8 workflows
- **PA-166.3** [Compliance Reporting, Analytics, Cost & Program Assurance](./VS-166-regulatory-license-permit-and-accreditation-portfolio-management/PA-166.3-compliance-reporting-analytics-cost-and-program-assurance.md) — 8 workflows

**[VS-187: Household Hazardous Waste, Paint & Used-Product Stewardship Take-Back Program](./VS-187-household-hazardous-waste-paint-and-product-stewardship-take-back/README.md)** (24 workflows)

- **PA-187.1** [Program Strategy, Regulatory Setup & Partner Network](./VS-187-household-hazardous-waste-paint-and-product-stewardship-take-back/PA-187.1-stewardship-program-strategy-regulatory-setup-and-partner-network.md) — 8 workflows
- **PA-187.2** [Customer Take-Back Operations — Collection, Handling & Reverse Logistics](./VS-187-household-hazardous-waste-paint-and-product-stewardship-take-back/PA-187.2-customer-take-back-operations-and-reverse-logistics.md) — 8 workflows
- **PA-187.3** [Recovery, Disposal, Compliance Reporting & Stewardship Analytics](./VS-187-household-hazardous-waste-paint-and-product-stewardship-take-back/PA-187.3-recovery-disposal-compliance-reporting-and-analytics.md) — 8 workflows

### Technology & Data

**[VS-27: IT Operations & Security](./VS-27-it-operations-security/README.md)** (71 workflows)

- **PA-27.1** [Service Management](./VS-27-it-operations-security/PA-27.1-service-management.md) — 30 workflows
- **PA-27.2** [Infrastructure & Platform](./VS-27-it-operations-security/PA-27.2-infrastructure-and-platform.md) — 24 workflows
- **PA-27.3** [Cybersecurity & Privacy](./VS-27-it-operations-security/PA-27.3-cybersecurity-and-privacy.md) — 17 workflows

**[VS-28: Data, Analytics & BI](./VS-28-data-analytics-bi/README.md)** (24 workflows)

- **PA-28.1** [BI Platform & Reporting](./VS-28-data-analytics-bi/PA-28.1-bi-platform-and-reporting.md) — 9 workflows
- **PA-28.2** [Data Engineering & Quality](./VS-28-data-analytics-bi/PA-28.2-data-engineering-and-quality.md) — 8 workflows
- **PA-28.3** [Advanced Analytics](./VS-28-data-analytics-bi/PA-28.3-advanced-analytics.md) — 7 workflows

**[VS-29: Master Data Management](./VS-29-master-data/README.md)** (43 workflows)

- **PA-29.1** [Foundational Masters](./VS-29-master-data/PA-29.1-foundational-masters.md) — 18 workflows
- **PA-29.2** [Financial & Operational Masters](./VS-29-master-data/PA-29.2-financial-and-operational-masters.md) — 12 workflows
- **PA-29.3** [Extended Masters](./VS-29-master-data/PA-29.3-extended-masters.md) — 13 workflows

**[VS-30: Innovation & Digital Transformation](./VS-30-innovation-digital/README.md)** (29 workflows)

- **PA-30.1** [Emerging Technology & PoC](./VS-30-innovation-digital/PA-30.1-emerging-technology-and-poc.md) — 9 workflows
- **PA-30.2** [AI/ML & Automation](./VS-30-innovation-digital/PA-30.2-ai-ml-and-automation.md) — 11 workflows
- **PA-30.3** [Document & Knowledge Management](./VS-30-innovation-digital/PA-30.3-document-and-knowledge-management.md) — 9 workflows

**[VS-99: IT Asset & Technology Lifecycle Management](./VS-99-it-asset-technology-lifecycle-management/README.md)** (24 workflows)

- **PA-99.1** [IT Hardware Asset Lifecycle & Deployment](./VS-99-it-asset-technology-lifecycle-management/PA-99.1-it-hardware-asset-lifecycle-deployment.md) — 8 workflows
- **PA-99.2** [Software Asset Management & License Compliance](./VS-99-it-asset-technology-lifecycle-management/PA-99.2-software-asset-management-license-compliance.md) — 8 workflows
- **PA-99.3** [Technology Asset Security, Cost & Governance Analytics](./VS-99-it-asset-technology-lifecycle-management/PA-99.3-technology-asset-security-cost-governance-analytics.md) — 8 workflows

**[VS-113: Enterprise Architecture, Application Portfolio & Technology Strategy](./VS-113-enterprise-architecture-application-portfolio-and-technology-strategy/README.md)** (31 workflows)

- **PA-113.1** [Enterprise Architecture Framework, Standards & Governance](./VS-113-enterprise-architecture-application-portfolio-and-technology-strategy/PA-113.1-enterprise-architecture-framework-standards-and-governance.md) — 12 workflows
- **PA-113.2** [Application Portfolio, Integration & Solution Architecture](./VS-113-enterprise-architecture-application-portfolio-and-technology-strategy/PA-113.2-application-portfolio-integration-and-solution-architecture.md) — 10 workflows
- **PA-113.3** [Technology Strategy, Innovation Governance & Architecture Analytics](./VS-113-enterprise-architecture-application-portfolio-and-technology-strategy/PA-113.3-technology-strategy-innovation-governance-and-architecture-analytics.md) — 9 workflows

**[VS-115: Calibration, Metrology & Measurement Traceability Management](./VS-115-calibration-metrology-and-measurement-traceability-management/README.md)** (24 workflows)

- **PA-115.1** [Calibration Program, Standards & Measurement Traceability](./VS-115-calibration-metrology-and-measurement-traceability-management/PA-115.1-calibration-program-standards-and-measurement-traceability.md) — 8 workflows
- **PA-115.2** [Device Calibration Operations](./VS-115-calibration-metrology-and-measurement-traceability-management/PA-115.2-device-calibration-operations.md) — 8 workflows
- **PA-115.3** [Weights & Measures Compliance, MRM & Measurement Analytics](./VS-115-calibration-metrology-and-measurement-traceability-management/PA-115.3-weights-and-measures-compliance-and-analytics.md) — 8 workflows

**[VS-126: Customer Data Platform, Single Customer View & Identity Resolution](./VS-126-customer-data-platform-single-customer-view-identity-resolution/README.md)** (24 workflows)

- **PA-126.1** [CDP Architecture, Ingestion & Identity Resolution](./VS-126-customer-data-platform-single-customer-view-identity-resolution/PA-126.1-cdp-architecture-ingestion-identity-resolution.md) — 8 workflows
- **PA-126.2** [Customer Segmentation, Activation & Personalization Foundation](./VS-126-customer-data-platform-single-customer-view-identity-resolution/PA-126.2-segmentation-activation-personalization.md) — 8 workflows
- **PA-126.3** [Customer 360 Consumption, Privacy & Governance Analytics](./VS-126-customer-data-platform-single-customer-view-identity-resolution/PA-126.3-customer-360-consumption-privacy-analytics.md) — 8 workflows

**[VS-128: AI/ML Governance & Responsible AI](./VS-128-ai-ml-governance-responsible-ai/README.md)** (27 workflows)

- **PA-128.1** [AI Strategy, Governance Framework & Model Risk Management](./VS-128-ai-ml-governance-responsible-ai/PA-128.1-ai-strategy-governance-framework-model-risk.md) — 8 workflows
- **PA-128.2** [Responsible AI — Fairness, Explainability, Privacy & Safety](./VS-128-ai-ml-governance-responsible-ai/PA-128.2-responsible-ai-fairness-explainability-privacy-safety.md) — 8 workflows
- **PA-128.3** [AI Lifecycle Operations, Assurance & Value Realization](./VS-128-ai-ml-governance-responsible-ai/PA-128.3-ai-lifecycle-operations-assurance-value-realization.md) — 11 workflows

**[VS-135: Technology Business Management, IT Financial Management & Cloud FinOps](./VS-135-technology-business-management-it-financial-management-cloud-finops/README.md)** (24 workflows)

- **PA-135.1** [Technology Investment Planning, Budgeting & TBM Framework](./VS-135-technology-business-management-it-financial-management-cloud-finops/PA-135.1-technology-investment-planning-budgeting-and-tbm-framework.md) — 8 workflows
- **PA-135.2** [Cloud FinOps, Cost Optimization & Spend Governance](./VS-135-technology-business-management-it-financial-management-cloud-finops/PA-135.2-cloud-finops-cost-optimization-and-spend-governance.md) — 8 workflows
- **PA-135.3** [Technology Value Realization & Financial Analytics](./VS-135-technology-business-management-it-financial-management-cloud-finops/PA-135.3-technology-value-realization-and-financial-analytics.md) — 8 workflows

**[VS-137: Product Information Management (PIM) & Digital Asset Management (DAM)](./VS-137-product-information-management-and-digital-asset-management/README.md)** (24 workflows)

- **PA-137.1** [Product Information Model, Attribute Taxonomy & Governance](./VS-137-product-information-management-and-digital-asset-management/PA-137.1-product-information-model-attribute-taxonomy-and-governance.md) — 8 workflows
- **PA-137.2** [Digital Asset Management, Rich Content & SDS/Certificate Lifecycle](./VS-137-product-information-management-and-digital-asset-management/PA-137.2-digital-asset-management-rich-content-and-sds-certificate-lifecycle.md) — 8 workflows
- **PA-137.3** [Content Syndication, Channel Publishing & PIM Analytics](./VS-137-product-information-management-and-digital-asset-management/PA-137.3-content-syndication-channel-publishing-and-pim-analytics.md) — 8 workflows

**[VS-151: Auto-ID, Barcode, RFID, Price-Tag Labeling & EAS Operations](./VS-151-auto-id-barcode-rfid-labeling-and-eas-operations/README.md)** (24 workflows)

- **PA-151.1** [Auto-ID Standards, GS1 Governance & Label/Tag Specification](./VS-151-auto-id-barcode-rfid-labeling-and-eas-operations/PA-151.1-auto-id-standards-gs1-governance-and-label-tag-specification.md) — 8 workflows
- **PA-151.2** [Label & Price-Tag Production, Printing & In-Store Application](./VS-151-auto-id-barcode-rfid-labeling-and-eas-operations/PA-151.2-label-and-price-tag-production-printing-and-application.md) — 8 workflows
- **PA-151.3** [EAS/RFID Tagging, Source-Tagging & Loss-Prevention Integration](./VS-151-auto-id-barcode-rfid-labeling-and-eas-operations/PA-151.3-eas-rfid-tagging-source-tagging-and-loss-prevention-integration.md) — 8 workflows

**[VS-190: Operational Technology (OT) / ICS Cybersecurity & Retail Technology Asset Protection](./VS-190-operational-technology-ot-ics-cybersecurity-and-retail-technology-asset-protection/README.md)** (24 workflows)

- **PA-190.1** [OT Asset Inventory, Architecture & IT/OT Segmentation Governance](./VS-190-operational-technology-ot-ics-cybersecurity-and-retail-technology-asset-protection/PA-190.1-ot-asset-inventory-architecture-and-it-ot-segmentation-governance.md) — 8 workflows
- **PA-190.2** [OT Threat Detection, Vulnerability & Incident Response Operations](./VS-190-operational-technology-ot-ics-cybersecurity-and-retail-technology-asset-protection/PA-190.2-ot-threat-detection-vulnerability-and-incident-response-operations.md) — 8 workflows
- **PA-190.3** [OT Compliance, Third-Party Access & Cyber Resilience Analytics](./VS-190-operational-technology-ot-ics-cybersecurity-and-retail-technology-asset-protection/PA-190.3-ot-compliance-third-party-access-and-cyber-resilience-analytics.md) — 8 workflows

---

## Cross-Reference Documents

| Document | Purpose |
|---|---|
| [WORKFLOW-FORMAT-GUIDE.md](./WORKFLOW-FORMAT-GUIDE.md) | Workflow format, RACI key & conventions |
| [workflow-criticality-classification.md](./workflow-criticality-classification.md) | Phase 1/2/3 implementation priorities |
| [workflow-dependency-map.md](./workflow-dependency-map.md) | Prerequisite relationships, critical path |
| [workflow-system-touchpoint-map.md](./workflow-system-touchpoint-map.md) | ERP module-to-workflow cross-reference |
| [workflow-gap-analysis.md](./workflow-gap-analysis.md) | Gap analysis methodology & results |
| [../requirement-workflow-matrix.md](../requirement-workflow-matrix.md) | Requirement-to-workflow traceability |

---

## Decision Tree: Where Does a New Workflow Go?

```
Does it involve a customer directly?     → Sell & Serve (VS-07 to VS-14, VS-37, VS-43–44, VS-46–48, VS-53, VS-55, VS-58, VS-60, VS-62–63, VS-65–66, VS-70, VS-75, VS-77–78, VS-82, VS-95, VS-107, VS-124, VS-139, VS-140, VS-145, VS-149, VS-156, VS-162, VS-164, VS-168, VS-171, VS-172, VS-174, VS-175, VS-176, VS-177)
Does it move physical goods?             → Make & Move (VS-04 to VS-06, VS-32, VS-56, VS-61, VS-74, VS-81, VS-90, VS-92, VS-93, VS-110, VS-111, VS-136, VS-143, VS-191)
Does it involve planning or sourcing?    → Plan & Source (VS-01 to VS-03, VS-41, VS-45, VS-57, VS-64, VS-67, VS-94, VS-101, VS-106, VS-122, VS-127, VS-131)
Does it involve money/financial flows?   → Finance (VS-15 to VS-18, VS-34, VS-38–40, VS-54, VS-68, VS-72, VS-79–80, VS-96, VS-105, VS-116, VS-118, VS-125, VS-142)
Does it involve people/HR?               → People (VS-19, VS-83, VS-84, VS-98, VS-102, VS-103, VS-121, VS-123, VS-134, VS-141, VS-144, VS-150, VS-160, VS-167, VS-169)
Does it involve buildings/fleet/assets?  → Asset & Infrastructure (VS-20, VS-35, VS-42, VS-59, VS-97, VS-108, VS-109, VS-112, VS-120, VS-138, VS-163)
Does it involve control/governance/risk?     → Governance & Assurance (VS-21 to VS-26, VS-31, VS-33, VS-36, VS-69, VS-71, VS-73, VS-76, VS-85–89, VS-91, VS-100, VS-104, VS-114, VS-117, VS-119, VS-129, VS-130, VS-132, VS-133, VS-146, VS-147, VS-152, VS-159, VS-161, VS-165, VS-166)
Is it about technology/data/platforms?   → Technology & Data (VS-27 to VS-30, VS-99, VS-113, VS-115, VS-126, VS-128, VS-135, VS-137, VS-190)
```

*Total: 5,430 workflows across 188 value streams · Date: 2026-09-21*
