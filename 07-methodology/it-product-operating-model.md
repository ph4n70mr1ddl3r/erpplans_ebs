# BuildRight Depot Corp. — IT Product Operating Model & Product-Team Design

> How the Information Technology department organizes as long-lived, business-paired **product
> teams** to run and continuously improve the IT landscape across all 188 value streams —
> team structure, membership, roles, RACI, governance, and sizing. Since v2.0 the landscape
> has been governed by capability sourcing; since **v3.11 the doctrine is two-tier**
> (2026-09-14): *if it's in Oracle EBS we use it — otherwise we build* — warehouse/transport
> execution runs **in-suite** (Oracle WMS/MSCA, Shipping/Transportation Execution), the POS
> estate, the ecommerce platform and the loyalty stack are **already-built in-house
> platforms** (integration is the program), **Payroll PH** is an **in-house build** posting
> journals to EBS, and the best-of-breed buy tier is eliminated. Sourcing decisions remain
> governed by the companion
> [`capability-sourcing-and-engineering-model.md`](capability-sourcing-and-engineering-model.md) (v3.2).
> Since **v3.12 the team shape conforms to the doctrine**: each configure-and-integrate team
> carries one **Platform Product Manager** (WLI's seat chartered as the chain-wide **Oracle
> Relationship & In-Suite Currency Manager**), WLI's second vendor seat is converted to
> in-suite WMS/OTE functional-analyst depth, and commercial ownership of the vendor-commodity
> line consolidates in the CIO Office — 122 FTE / 17 teams unchanged.
> Since v2.1 an **AI & Agent Platform (AAP)** gives every product team the capability to
> automate manual tasks with governed AI agents (VS-128 discipline; autonomy ladder wired to
> the workflow Tier register).

---

## 1. Purpose & Scope

This document defines the target **IT operating model** for BuildRight Depot Corp.: the product
taxonomy, product-team membership, role definitions, RACI, governance bodies, cadence, and
headcount. It is the organizational counterpart to the system landscape defined in
[`technical-guidelines.md`](technical-guidelines.md) and the business process catalog in
[`workflows/value-stream-index.md`](../01-model-company/workflows/value-stream-index.md)
(188 value streams, 569 process areas, 5,427 workflows).

Scope covers the steady state **after** the unified ERP go-live under the two-tier sourcing
doctrine adopted 2026-09-14 (the in-suite EBS core + in-house/already-built products of
`model-company-profile.md` §14.1; supersedes the 2026-09-03 hybrid posture). **Since
2026-09-14 this model is the IT department's structure of record** — promoted with the
org's structure promotion (profile v3.0 §3.3; TO v2.4 §5.2: "Actual = 122"). Implementation-phase structures (SI governance,
cutover command centers) are out of scope; see §10 for the transition.

---

## 2. Design Principles

1. **Products, not projects.** A product is a long-lived business capability delivered through
   the ERP (e.g., "Store Systems & POS"). Teams are stable, own outcomes (uptime, adoption,
   value-stream KPIs), and absorb enhancement, defect, regulatory, and tech-debt work into one
   backlog — no temporary project teams that disband at go-live.
2. **Business–IT pairing.** Every product team is co-owned by an **IT Product Owner** and a
   **Business Product Owner (BPO)** — the actual process owner from the department that runs the
   value stream (`model-company-profile.md` §3.3/§11.1). This prevents the "unowned program"
   failure mode previously caught in the S&OP/IBP gap (VS-127).
3. **Value streams map to products; teams own systems.** A value stream is a business process;
   a product team owns the *systems and configuration* that enable it. Every one of the 188 value
   streams has exactly **one primary product team** (gap-free, overlap-free ownership — §4),
   while controls embedded in those workflows remain jointly governed (§6.3).
4. **Capability-sourced talent model.** The landscape is two-tier: the **in-suite EBS
   core** (used, configured — never rebuilt or bought around) and **in-house built
   products**, including the already-built POS/ecommerce/loyalty platforms
   (`model-company-profile.md` §14.1; decisions per the
   [`capability-sourcing-and-engineering-model.md`](capability-sourcing-and-engineering-model.md)
   register). Team shape follows the sourcing archetype: **configure** teams are built around
   ERP functional analysts and process architects; **configure-and-integrate** teams add
   product/vendor management (the Oracle relationship, in-suite currency, the already-built
   platforms); **build** products are delivered by software squads on the SEP paved
   road. Dedicated engineers live in the build squads and the platform layer (integration,
   data, engineering enablement).
5. **Tier-aware service levels.** The workflow criticality register
   ([`workflow-criticality-classification.md`](../01-model-company/workflows/workflow-criticality-classification.md):
   1,375 Tier-1 / 3,243 Tier-2 / 754 Tier-3) drives each team's regression coverage, incident
   SLAs, and roadmap prioritization. Every Tier-1 workflow in a team's domain maps to at least
   one automated regression test.
6. **Platform thinking.** Domain ("stream-aligned") teams build on shared **platform teams**
   (integration, infrastructure, security, data, engineering enablement, field services) that
   treat domain teams as their customers, following Team-Topologies-style separation:
   stream-aligned, platform, and enabling (GRC) team types.
7. **Use EBS by default; build where EBS ships nothing.** Every capability decision routes
   through the Sourcing & Investment Board gate in the order in-EBS → build — build is
   admitted only when the EBS-standard answer demonstrably does not exist — with the
   in-suite core protected by a CEO-noted waiver rule. No capability may be re-sourced
   without a registered decision carrying an IAP integration estimate, a control-mapping
   appendix against the 808-control register, a TCO sheet, a run-cost & talent plan (build),
   and a re-evaluation trigger.
8. **Agents are products, not side effects.** Agentic automation runs on the AI & Agent
   Platform (AAP) paved road: every agent is registered under VS-128, acts only through
   IAP-contract tools, obeys the Tier-based autonomy ladder (Tier-1 human-approval-gated,
   Tier-2 bounded, Tier-3 autonomous-in-bounds), and ships with evaluation evidence, a
   kill-switch, and an audit trail that counts as control evidence. Every agent has exactly
   one accountable product team — the same gap-free ownership rule as any capability.

---

## 3. Product Taxonomy — From 188 Value Streams to 17 IT Products

### 3.1 The mapping rule

The 8 value-stream families do not translate 1:1 into teams (188 teams is absurd; 8 teams is too
coarse for the selling side). The taxonomy below groups by **system domain and business
partner**, then assigns every value stream to exactly one primary product team — **17 teams in
all**: 9 stream-aligned domain products (including the two in-house **build** products OMO and
TPS, created by sourcing decisions rather than value-stream families), 7 platform teams, and
the CIO Office. Two consequences worth stating explicitly:

- The **Governance & Assurance family (37 VS)** gets **no dedicated team**: those workflows are
  controls *embedded in* other products' configurations, with a small GRC/controls cell (§5.3)
  and Internal Audit/Legal & Compliance as demand-side owners. The mapping in §4 shows which
  product carries each governance VS's system enablement.
- The **Technology & Data family (13 VS)** is IT itself: these value streams are owned directly
  by the platform teams and the CIO Office.

### 3.2 IT product portfolio

| # | Product Team | Code | Type | Primary Business Partner(s) | VS | Workflows |
|---|---|---|---|---|---|---|
| 1 | Merchandising & Supply Chain Systems | MSC | Stream-aligned (configure) | VP Supply Chain; VP Merchandising | 16 | 486 |
| 2 | Warehouse, Logistics & Inventory Systems | WLI | Stream-aligned (configure & integrate) | VP Supply Chain (DC Ops, Fleet & Logistics) | 20 | 526 |
| 3 | Store Systems & POS | SSP | Stream-aligned (configure & integrate) | VP Store Operations | 25 | 907 |
| 4 | Commerce & Customer Platforms | CCP | Stream-aligned (configure & integrate) | CMO; Digital Commerce Inc. GM; Trade/Account Mgmt | 25 | 742 |
| 5 | Finance & Treasury Systems | FIN | Stream-aligned (configure) | CFO (Controller, Treasurer, Tax) | 30 | 809 |
| 6 | Corporate, Governance & Asset Systems | CORP | Stream-aligned (configure) | VP Legal & Compliance; Facilities & Real Estate; Quality; Internal Audit & Risk | 35 | 924 |
| 7 | People Systems | PEO | Stream-aligned (configure) | CHRO | 16 | 445 |
| 8 | Order Orchestration | OMO | Stream-aligned (build) | Digital Commerce with Supply Chain | 1 | 24 |
| 9 | Trade & Project Services Platform | TPS | Stream-aligned (build) | VP Supply Chain (Fleet & Logistics) with Trade/Account Mgmt | 3 | 72 |
| | **Domain subtotal** | | | | **171** | **4,935** |
| 10 | Integration & API Platform | IAP | Platform | All product teams | 0 | 0 |
| 11 | Cloud Infrastructure & SRE | INFRA | Platform | All product teams | 3 | 126 |
| 12 | Cybersecurity, Privacy & OT Security | SEC | Platform + enabling | All product teams; DPO; Internal Audit | 3 | 72 |
| 13 | Data Platform & MDM | DP | Platform | All product teams; Strategy/CPM; Marketing | 7 | 189 |
| 14 | Software Engineering Platform | SEP | Platform | Build squads (OMO, TPS); all product teams | 0 | 0 |
| 15 | AI & Agent Platform | AAP | Platform | All product teams (agent enablement); VS-128 governance | 0 | 0 |
| 16 | Field & End-User Services | FS | Platform | All 205 locations; 6,911 users | 1 | 24 |
| | CIO Office (EA, Portfolio Governance, FinOps, Vendor Portfolio) | CIO | Enabling | CIO; CEO; Finance | 3 | 81 |
| | **Platform + CIO subtotal** | | | | **17** | **492** |
| | **Total** | | | | **188** | **5,427** |

> Team **workload is weighted by Tier-1 density and transaction volume, not raw VS count** —
> CORP's 35 VS are mostly registers and GRC tooling with modest system complexity, while SSP's
> 25 VS include the 600-terminal POS estate with a 99.9% uptime target. Sizing (§9) reflects
> this.

---

## 4. Full Value-Stream → Product-Team Mapping (188 VS)

> Primary team = the product team accountable for the systems enabling the value stream. The
> business process owner is the department that runs the process (§3.3/§11.1 departments).
> Business-side BPO/SME participation per team is defined in §5.2.

### 4.1 Plan & Source (15 VS → all MSC)

| VS | Value Stream | Team | Business Process Owner |
|---|---|---|---|
| [VS-01](../01-model-company/workflows/VS-01-merchandise-strategy/README.md) | Merchandise Strategy | MSC | Merchandising |
| [VS-02](../01-model-company/workflows/VS-02-supply-planning/README.md) | Supply Planning | MSC | Supply Chain (Demand Planning) |
| [VS-03](../01-model-company/workflows/VS-03-vendor-management/README.md) | Vendor Management & Procurement | MSC | Supply Chain (Procurement) with Merchandising (Buying) |
| [VS-41](../01-model-company/workflows/VS-41-private-label-brand/README.md) | Private Label & Exclusive Brand Management | MSC | Merchandising (Private Brand) |
| [VS-45](../01-model-company/workflows/VS-45-consignment-vmi-operations/README.md) | Consignment & Vendor-Managed Inventory Operations | MSC | Merchandising with Supply Chain |
| [VS-57](../01-model-company/workflows/VS-57-competitive-price-intelligence/README.md) | Competitive Price Intelligence & Monitoring | MSC | Merchandising (Pricing) |
| [VS-64](../01-model-company/workflows/VS-64-seasonal-merchandise-clearance/README.md) | Seasonal Merchandise Transition & Clearance | MSC | Merchandising |
| [VS-67](../01-model-company/workflows/VS-67-vendor-scorecard-analytics/README.md) | Vendor Scorecard & Performance Analytics | MSC | Supply Chain (Vendor Management) |
| [VS-94](../01-model-company/workflows/VS-94-cooperative-community-enterprise-procurement/README.md) | Cooperative & Community Enterprise Procurement | MSC | Supply Chain (Procurement) |
| [VS-101](../01-model-company/workflows/VS-101-merchandise-financial-planning-otb-margin-management/README.md) | Merchandise Financial Planning, OTB & Margin Management | MSC | Merchandising with Finance (FP&A) |
| [VS-106](../01-model-company/workflows/VS-106-commodity-input-cost-risk-management/README.md) | Commodity & Input-Cost Risk Management | MSC | Merchandising with Finance |
| [VS-122](../01-model-company/workflows/VS-122-global-sourcing-import-buying-sourcing-agent-management/README.md) | Global Sourcing, Import Buying & Sourcing Agent Management | MSC | Merchandising (Import Buying) with Supply Chain (Imports) |
| [VS-127](../01-model-company/workflows/VS-127-sales-operations-planning-integrated-business-planning/README.md) | Sales & Operations Planning (S&OP) & Integrated Business Planning | MSC | S&OP/IBP sub-team |
| [VS-131](../01-model-company/workflows/VS-131-human-rights-responsible-supply-chain-due-diligence/README.md) | Human Rights, Modern Slavery & Responsible Supply Chain Due Diligence | MSC | Supply Chain (Vendor Management) with Legal & Compliance |
| [VS-182](../01-model-company/workflows/VS-182-b2b-bulk-project-custom-import-indent-sourcing-and-brokerage/README.md) | B2B Bulk-Project Custom Import (Indent Sourcing & Brokerage Operations) | MSC | Merchandising with Trade/Account Management |

### 4.2 Make & Move (19 VS → 17 WLI, 2 TPS)

| VS | Value Stream | Team | Business Process Owner |
|---|---|---|---|
| [VS-04](../01-model-company/workflows/VS-04-dc-warehouse/README.md) | DC & Warehouse Operations | WLI | DC Operations |
| [VS-05](../01-model-company/workflows/VS-05-inventory-lifecycle/README.md) | Inventory Lifecycle | WLI | Inventory Planning |
| [VS-06](../01-model-company/workflows/VS-06-logistics-fleet/README.md) | Logistics & Fleet | WLI | Fleet & Logistics |
| [VS-32](../01-model-company/workflows/VS-32-returns-reverse-logistics/README.md) | Returns & Reverse Logistics | WLI | DC Operations with Store Operations |
| [VS-56](../01-model-company/workflows/VS-56-third-party-delivery-partner/README.md) | Third-Party Delivery Partner Management | WLI | Fleet & Logistics |
| [VS-61](../01-model-company/workflows/VS-61-fuel-fleet-cost-management/README.md) | Fuel & Fleet Cost Management | WLI | Fleet & Logistics |
| [VS-74](../01-model-company/workflows/VS-74-contractor-jobsite-delivery/README.md) | Professional Contractor Job Site Delivery | TPS | Fleet & Logistics |
| [VS-81](../01-model-company/workflows/VS-81-cash-in-transit-vault-armored/README.md) | Cash-in-Transit, Vault & Armored Car Operations | WLI | Treasury with Loss Prevention |
| [VS-90](../01-model-company/workflows/VS-90-damage-claims-freight-recovery/README.md) | Damage, Claims & Freight Recovery Management | WLI | Fleet & Logistics |
| [VS-92](../01-model-company/workflows/VS-92-kitting-bundling-build-to-order-assembly/README.md) | Kitting, Bundling & Build-to-Order Assembly Operations | WLI | DC Operations |
| [VS-93](../01-model-company/workflows/VS-93-dark-store-micro-fulfillment/README.md) | Dark Store & Micro-Fulfillment Operations | WLI | Store Operations with Supply Chain |
| [VS-110](../01-model-company/workflows/VS-110-freight-procurement-carrier-management-and-freight-audit/README.md) | Freight Procurement, Carrier Management & Freight Audit | WLI | Fleet & Logistics |
| [VS-111](../01-model-company/workflows/VS-111-packaging-pallet-and-returnable-transport-item-management/README.md) | Packaging, Pallet & Returnable Transport Item (RTI) Management | WLI | DC Operations |
| [VS-136](../01-model-company/workflows/VS-136-supply-chain-network-design-multi-echelon-inventory-optimization-flow-engineering/README.md) | Supply Chain Network Design, Multi-Echelon Inventory Optimization & Flow Engineering | WLI | VP Supply Chain |
| [VS-143](../01-model-company/workflows/VS-143-bulky-white-goods-delivery-installation-haul-away-and-recycling/README.md) | Bulky & White-Goods Delivery, Installation, Haul-Away & Recycling Operations | TPS | Fleet & Logistics |
| [VS-155](../01-model-company/workflows/VS-155-trade-in-buy-back-and-certified-pre-owned-product-resale/README.md) | Trade-In, Buy-Back & Certified Pre-Owned Product Resale | WLI | Store Operations |
| [VS-180](../01-model-company/workflows/VS-180-disaster-relief-supply-chain-logistics-and-humanitarian-aid-coordination/README.md) | Disaster Relief Supply Chain Logistics & Humanitarian Aid Coordination | WLI | VP Supply Chain |
| [VS-191](../01-model-company/workflows/VS-191-customer-construction-debris-demolition-waste-and-site-cleanup-operations/README.md) | Customer Construction Debris, Demolition Waste & Site Cleanup Operations | WLI | Fleet & Logistics |
| [VS-192](../01-model-company/workflows/VS-192-green-fleet-transition-electric-vehicle-fleet-operations-and-sustainable-transportation/README.md) | Green Fleet Transition, EV Fleet Operations & Sustainable Transportation | WLI | Fleet & Logistics |

### 4.3 Sell & Serve (46 VS → 20 SSP, 24 CCP, 1 OMO, 1 TPS)

| VS | Value Stream | Team | Business Process Owner |
|---|---|---|---|
| [VS-07](../01-model-company/workflows/VS-07-store-operations/README.md) | Store Operations | SSP | Store Operations |
| [VS-08](../01-model-company/workflows/VS-08-pos-checkout/README.md) | POS & Checkout | SSP | Store Operations |
| [VS-09](../01-model-company/workflows/VS-09-in-store-services/README.md) | In-Store Customer Services | SSP | Store Operations with Customer Service |
| [VS-10](../01-model-company/workflows/VS-10-ecommerce-digital/README.md) | Ecommerce & Digital Channels | CCP | Digital Commerce |
| [VS-11](../01-model-company/workflows/VS-11-trade-project-wholesale/README.md) | Trade, Project & Wholesale | CCP | Trade/Account Management |
| [VS-12](../01-model-company/workflows/VS-12-installation-services/README.md) | Installation & Services | CCP | Store Operations (Services) |
| [VS-13](../01-model-company/workflows/VS-13-customer-experience/README.md) | Customer Experience & Loyalty | CCP | Marketing (Loyalty) |
| [VS-14](../01-model-company/workflows/VS-14-marketing/README.md) | Marketing & Communications | CCP | Marketing |
| [VS-37](../01-model-company/workflows/VS-37-store-opening-commissioning/README.md) | Store Opening & Commissioning | SSP | Store Operations with Facilities |
| [VS-43](../01-model-company/workflows/VS-43-trade-professional-program/README.md) | Trade Professional Program & Contractor Services | CCP | Trade/Account Management |
| [VS-44](../01-model-company/workflows/VS-44-consumer-insights-market-research/README.md) | Consumer Insights & Market Research | CCP | Marketing (Insights) |
| [VS-46](../01-model-company/workflows/VS-46-government-institutional-sales/README.md) | Government & Institutional B2G Sales | CCP | Trade/Account Management |
| [VS-47](../01-model-company/workflows/VS-47-subscription-recurring-services/README.md) | Subscription & Recurring Home Services | CCP | Store Operations (Services) |
| [VS-48](../01-model-company/workflows/VS-48-retail-media-network/README.md) | Retail Media Network & Vendor Advertising | CCP | Marketing |
| [VS-53](../01-model-company/workflows/VS-53-warranty-guarantee-management/README.md) | Warranty & Guarantee Management | CCP | Customer Service |
| [VS-55](../01-model-company/workflows/VS-55-store-planogram-space-optimization/README.md) | Store Planogram & Space Optimization | SSP | Merchandising (Assortment & Space) |
| [VS-58](../01-model-company/workflows/VS-58-coupon-digital-promotions/README.md) | Coupon & Digital Promotions Management | CCP | Marketing |
| [VS-60](../01-model-company/workflows/VS-60-omnichannel-order-routing/README.md) | Omnichannel Order Routing & Fulfillment Orchestration | OMO | Digital Commerce with Supply Chain |
| [VS-62](../01-model-company/workflows/VS-62-product-sample-display-management/README.md) | Product Sample & Display Management | SSP | Merchandising |
| [VS-63](../01-model-company/workflows/VS-63-store-communication-task-management/README.md) | Store Communication & Task Management | SSP | Store Operations |
| [VS-65](../01-model-company/workflows/VS-65-ecommerce-marketplace-integration/README.md) | E-Commerce Marketplace Integration | CCP | Digital Commerce |
| [VS-66](../01-model-company/workflows/VS-66-customer-project-design-services/README.md) | Customer Project & Design Services | CCP | Trade/Account Management |
| [VS-70](../01-model-company/workflows/VS-70-solar-renewable-energy/README.md) | Solar & Renewable Energy Product Operations | CCP | Merchandising |
| [VS-75](../01-model-company/workflows/VS-75-digital-engagement-app/README.md) | Digital Engagement & Mobile App Operations | CCP | Digital Commerce |
| [VS-77](../01-model-company/workflows/VS-77-construction-material-staging/README.md) | Construction Project Material Staging & Phased Delivery | TPS | Trade/Account Management |
| [VS-78](../01-model-company/workflows/VS-78-green-building-advisory/README.md) | Green Building & Sustainable Product Advisory | CCP | Merchandising |
| [VS-82](../01-model-company/workflows/VS-82-sari-sari-msme-micro-wholesale/README.md) | Sari-Sari Store & MSME Micro-Wholesale Program | CCP | Trade/Account Management |
| [VS-95](../01-model-company/workflows/VS-95-marketplace-operator-third-party-seller/README.md) | Marketplace Operator & Third-Party Seller Management | CCP | Digital Commerce |
| [VS-107](../01-model-company/workflows/VS-107-strategic-key-account-enterprise-customer-management/README.md) | Strategic Key Account & Enterprise Customer Management | CCP | Trade/Account Management |
| [VS-124](../01-model-company/workflows/VS-124-sales-enablement-product-knowledge-clienteling/README.md) | Sales Enablement, Product Knowledge Mastery & Clienteling | CCP | Marketing with Trade/Account Management |
| [VS-139](../01-model-company/workflows/VS-139-trade-show-exhibition-and-field-event-marketing/README.md) | Trade Show, Exhibition & Field Event Marketing | CCP | Marketing |
| [VS-140](../01-model-company/workflows/VS-140-field-sales-outside-sales-and-route-to-market-force-management/README.md) | Field Sales, Outside Sales & Route-to-Market Force Management | CCP | Trade/Account Management |
| [VS-145](../01-model-company/workflows/VS-145-garden-center-live-goods-and-plant-nursery/README.md) | Garden Center, Live Goods & Plant Nursery Operations | SSP | Store Operations |
| [VS-149](../01-model-company/workflows/VS-149-self-checkout-scan-and-go-and-unattended-retail-technology-operations/README.md) | Self-Checkout, Scan-&-Go & Unattended Retail Technology Operations | SSP | Store Operations |
| [VS-156](../01-model-company/workflows/VS-156-in-store-value-added-services-and-financial-agency-operations/README.md) | In-Store Value-Added Services & Financial Agency Operations | SSP | Store Operations |
| [VS-162](../01-model-company/workflows/VS-162-customer-pickup-truck-and-cargo-van-rental/README.md) | Customer Pickup Truck & Cargo Van Rental (Self-Haul) Operations | SSP | Store Operations |
| [VS-164](../01-model-company/workflows/VS-164-smart-locker-and-automated-parcel-collection-network/README.md) | Smart Locker & Automated Parcel Collection Network | SSP | Digital Commerce with Store Operations |
| [VS-168](../01-model-company/workflows/VS-168-in-store-audio-ambient-media-and-music-royalty-licensing/README.md) | In-Store Audio, Ambient Media & Music Royalty Licensing | SSP | Marketing |
| [VS-171](../01-model-company/workflows/VS-171-customer-pickup-loading-zone-and-will-call-counter-operations/README.md) | Customer Pickup, Loading Zone & Will-Call Counter Operations | SSP | Store Operations |
| [VS-172](../01-model-company/workflows/VS-172-third-party-installer-and-contractor-network-pro-referral-management/README.md) | Third-Party Installer & Contractor Network (Pro-Referral) Management | SSP | Store Operations with Trade/Account Management |
| [VS-174](../01-model-company/workflows/VS-174-self-storage-portable-container-and-mobile-storage-operations/README.md) | Self-Storage, Portable Container & Mobile-Storage Operations | SSP | Store Operations |
| [VS-175](../01-model-company/workflows/VS-175-propane-lpg-cylinder-exchange-and-gas-refill-operations/README.md) | Propane, LPG Cylinder Exchange & Gas Refill Operations | SSP | Store Operations |
| [VS-176](../01-model-company/workflows/VS-176-blueprint-reprographics-and-large-format-plan-printing-services/README.md) | Blueprint, Reprographics & Large-Format Plan Printing Services | SSP | Store Operations |
| [VS-177](../01-model-company/workflows/VS-177-field-retail-operations-regional-district-management-and-multi-store-execution/README.md) | Field Retail Operations, Regional/District Management & Multi-Store Retail Execution Network | SSP | Store Operations (Field Management) |
| [VS-185](../01-model-company/workflows/VS-185-b2b-cooperative-credit-and-procurement-partnerships/README.md) | B2B Cooperative Credit & Procurement Partnerships | CCP | Trade/Account Management |
| [VS-186](../01-model-company/workflows/VS-186-compact-and-heavy-construction-equipment-rental-fleet-operations/README.md) | Compact & Heavy Construction Equipment Rental Fleet Operations | SSP | Store Operations |

### 4.4 Finance (29 VS → all FIN)

| VS | Value Stream | Team | Business Process Owner |
|---|---|---|---|
| [VS-15](../01-model-company/workflows/VS-15-procure-to-pay/README.md) | Procure-to-Pay | FIN | Finance (AP) with Supply Chain (Procurement) |
| [VS-16](../01-model-company/workflows/VS-16-order-to-cash/README.md) | Order-to-Cash | FIN | Finance (AR) |
| [VS-17](../01-model-company/workflows/VS-17-record-to-report/README.md) | Record-to-Report | FIN | Finance (Controller) |
| [VS-18](../01-model-company/workflows/VS-18-treasury-cash/README.md) | Treasury & Cash | FIN | Treasury |
| [VS-34](../01-model-company/workflows/VS-34-expense-procurement/README.md) | Expense & Non-Merchandise Procurement | FIN | Finance with Supply Chain (Procurement) |
| [VS-38](../01-model-company/workflows/VS-38-consumer-credit-financing/README.md) | Consumer Credit & Financing | FIN | Finance with Store Operations |
| [VS-39](../01-model-company/workflows/VS-39-vendor-rebate-incentive/README.md) | Vendor Rebate & Incentive Management | FIN | Finance with Merchandising |
| [VS-40](../01-model-company/workflows/VS-40-capex-project-accounting/README.md) | Capex & Project Accounting | FIN | Finance (Controller) |
| [VS-54](../01-model-company/workflows/VS-54-gift-card-stored-value/README.md) | Gift Card & Stored Value Management | FIN | Finance with Marketing |
| [VS-68](../01-model-company/workflows/VS-68-trade-credit-risk-management/README.md) | Trade Credit Insurance & Risk Management | FIN | Finance (AR) with Trade/Account Management |
| [VS-72](../01-model-company/workflows/VS-72-cross-entity-shared-services/README.md) | Cross-Entity Shared Services & Chargeback | FIN | Finance (Controller) |
| [VS-79](../01-model-company/workflows/VS-79-tax-management-bir-reporting/README.md) | Tax Management & BIR Statutory Reporting | FIN | Tax |
| [VS-80](../01-model-company/workflows/VS-80-payment-operations-acquirer-settlement/README.md) | Payment Operations, Acquirer & Settlement Management | FIN | Finance with Treasury |
| [VS-96](../01-model-company/workflows/VS-96-equipment-leasing-capital-equipment-finance/README.md) | Equipment Leasing & Capital Equipment Finance | FIN | Finance |
| [VS-105](../01-model-company/workflows/VS-105-supply-chain-finance-working-capital-management/README.md) | Supply Chain Finance & Working Capital Management | FIN | Treasury |
| [VS-116](../01-model-company/workflows/VS-116-performance-bond-surety-and-bank-guarantee-management/README.md) | Performance Bond, Surety & Bank Guarantee Management | FIN | Finance with Legal & Compliance |
| [VS-118](../01-model-company/workflows/VS-118-revenue-assurance-pricing-integrity-and-leakage-management/README.md) | Revenue Assurance, Pricing Integrity & Leakage Management | FIN | Finance with Merchandising (Pricing) |
| [VS-125](../01-model-company/workflows/VS-125-cross-channel-fraud-management-payment-fraud-protection/README.md) | Cross-Channel Fraud Management & Payment Fraud Protection | FIN | Finance with Loss Prevention |
| [VS-142](../01-model-company/workflows/VS-142-cash-on-delivery-operations-driver-cash-handling-and-reconciliation/README.md) | Cash-on-Delivery (COD) Operations, Driver Cash Handling & Reconciliation | FIN | Finance with Digital Commerce |
| [VS-148](../01-model-company/workflows/VS-148-lease-accounting-pfrs-16-and-right-of-use-asset-management/README.md) | Lease Accounting (PFRS 16/IFRS 16) & Right-of-Use Asset Management | FIN | Finance (Controller) |
| [VS-153](../01-model-company/workflows/VS-153-captive-insurance-reinsurance-and-enterprise-risk-financing/README.md) | Captive Insurance, Reinsurance & Enterprise Risk Financing | FIN | Finance with Internal Audit & Risk |
| [VS-154](../01-model-company/workflows/VS-154-home-construction-finance-loan-brokerage-and-mortgage-referral/README.md) | Home Construction Finance, Loan Brokerage & Mortgage Referral Services | FIN | Finance with Store Operations |
| [VS-157](../01-model-company/workflows/VS-157-revenue-recognition-pfrs-15-and-complex-contract-accounting/README.md) | Revenue Recognition (PFRS 15) & Complex Contract Accounting | FIN | Finance (Controller) |
| [VS-158](../01-model-company/workflows/VS-158-product-costing-landed-cost-and-cost-accounting/README.md) | Product Costing, Landed-Cost & Cost Accounting | FIN | Finance with Merchandising |
| [VS-170](../01-model-company/workflows/VS-170-inventory-pledge-asset-based-lending-and-trust-receipt-financing/README.md) | Inventory Pledge, Asset-Based Lending & Trust-Receipt (Warehouse-Receipt) Financing | FIN | Treasury |
| [VS-173](../01-model-company/workflows/VS-173-investor-relations-capital-markets-and-securities-disclosure/README.md) | Investor Relations, Capital Markets & Securities Disclosure | FIN | Finance (Controller) with Legal & Compliance |
| [VS-181](../01-model-company/workflows/VS-181-b2b-project-financing-escrow-account-orchestration-and-lien-release/README.md) | B2B Project Financing, Escrow Account Orchestration & Lien Release | FIN | Finance with Trade/Account Management |
| [VS-188](../01-model-company/workflows/VS-188-trade-reseller-floor-plan-and-dealer-inventory-financing/README.md) | Trade Reseller Floor-Plan & Dealer Inventory Financing | FIN | Finance |
| [VS-189](../01-model-company/workflows/VS-189-trade-receivables-factoring-invoice-discounting-and-securitization/README.md) | Trade Accounts Receivable Factoring, Invoice Discounting & Receivables Securitization | FIN | Finance (AR) |

### 4.5 People (16 VS → all PEO)

| VS | Value Stream | Team | Business Process Owner |
|---|---|---|---|
| [VS-19](../01-model-company/workflows/VS-19-hire-to-retire/README.md) | Hire-to-Retire | PEO | HR |
| [VS-83](../01-model-company/workflows/VS-83-occupational-health-clinic-wellness/README.md) | Occupational Health, Safety Clinic & Employee Wellness | PEO | HR with HSE |
| [VS-84](../01-model-company/workflows/VS-84-labor-relations-collective-bargaining/README.md) | Labor Relations & Collective Bargaining Management | PEO | HR (Labor Relations) |
| [VS-98](../01-model-company/workflows/VS-98-contingent-contract-outsourced-workforce/README.md) | Contingent, Contract & Outsourced Workforce Management | PEO | HR |
| [VS-102](../01-model-company/workflows/VS-102-compensation-benefits-total-rewards/README.md) | Compensation, Benefits & Total Rewards Strategy | PEO | HR (Compensation & Benefits) |
| [VS-103](../01-model-company/workflows/VS-103-hr-shared-services-employee-experience-people-analytics/README.md) | HR Shared Services, Employee Experience & People Analytics | PEO | HR (Shared Services) |
| [VS-121](../01-model-company/workflows/VS-121-talent-acquisition-employer-brand-candidate-experience/README.md) | Talent Acquisition, Employer Brand & Candidate Experience | PEO | HR (Recruitment) |
| [VS-123](../01-model-company/workflows/VS-123-skilled-trade-apprenticeship-vocational-education-capability-pipeline/README.md) | Skilled-Trade Apprenticeship, Vocational Education & Capability Pipeline | PEO | HR (Training) |
| [VS-134](../01-model-company/workflows/VS-134-organizational-change-management-digital-adoption-transformation-enablement/README.md) | Organizational Change Management, Digital Adoption & Transformation Enablement | PEO | HR with Strategy/Corporate Planning |
| [VS-141](../01-model-company/workflows/VS-141-employee-transport-shuttle-and-daily-commute-management/README.md) | Employee Transport, Shuttle & Daily Commute Management | PEO | HR with Facilities |
| [VS-144](../01-model-company/workflows/VS-144-employee-accommodation-dormitory-and-staff-housing/README.md) | Employee Accommodation, Dormitory & Staff Housing Operations | PEO | HR with Facilities |
| [VS-150](../01-model-company/workflows/VS-150-drug-free-workplace-and-substance-abuse-program/README.md) | Drug-Free Workplace & Substance Abuse Program | PEO | HR with HSE |
| [VS-160](../01-model-company/workflows/VS-160-global-mobility-immigration-and-foreign-worker-compliance/README.md) | Global Mobility, Immigration & Foreign Worker Compliance | PEO | HR with Legal & Compliance |
| [VS-167](../01-model-company/workflows/VS-167-workforce-background-screening-credentialing-and-personnel-vetting/README.md) | Workforce Background Screening, Credentialing & Personnel Vetting | PEO | HR |
| [VS-169](../01-model-company/workflows/VS-169-employee-uniform-workwear-and-ppe-issuance-program/README.md) | Employee Uniform, Workwear & PPE-Issuance Program | PEO | HR with HSE |
| [VS-183](../01-model-company/workflows/VS-183-dual-training-system-dts-and-tesda-partnership-program/README.md) | Dual Training System (DTS) & TESDA Partnership Program | PEO | HR (Training) |

### 4.6 Asset & Infrastructure (13 VS → 12 CORP, 1 SSP)

| VS | Value Stream | Team | Business Process Owner |
|---|---|---|---|
| [VS-20](../01-model-company/workflows/VS-20-real-estate-construction/README.md) | Real Estate & Construction | CORP | Facilities & Real Estate |
| [VS-35](../01-model-company/workflows/VS-35-fixed-asset-management/README.md) | Fixed Asset Management | CORP | Finance (Controller) with Facilities |
| [VS-42](../01-model-company/workflows/VS-42-property-lease-admin/README.md) | Property & Lease Administration | CORP | Facilities (Lease Admin) |
| [VS-59](../01-model-company/workflows/VS-59-store-closure-decommissioning/README.md) | Store Closure & Decommissioning | SSP | Store Operations with Facilities |
| [VS-97](../01-model-company/workflows/VS-97-corporate-real-estate-property-portfolio/README.md) | Corporate Real Estate & Property Portfolio Management | CORP | Facilities & Real Estate |
| [VS-108](../01-model-company/workflows/VS-108-onsite-renewable-energy-prosumer-asset-operations/README.md) | On-Site Renewable Energy & Prosumer Asset Operations | CORP | Facilities with Sustainability/ESG |
| [VS-109](../01-model-company/workflows/VS-109-store-remodel-renovation-lifecycle-refurbishment/README.md) | Store Remodel, Renovation & Lifecycle Refurbishment Program | CORP | Store Operations with Facilities |
| [VS-112](../01-model-company/workflows/VS-112-corporate-project-and-program-management-office/README.md) | Corporate Project & Program Management Office (PMO) | CORP | Strategy/Corporate Planning (PMO) |
| [VS-120](../01-model-company/workflows/VS-120-energy-efficiency-conservation-and-ra-11285-compliance-program/README.md) | Energy Efficiency, Conservation & RA 11285 Compliance Program | CORP | Facilities with Sustainability/ESG |
| [VS-138](../01-model-company/workflows/VS-138-integrated-facilities-management-workplace-services-and-building-automation/README.md) | Integrated Facilities Management, Workplace Services & Building Automation | CORP | Facilities |
| [VS-163](../01-model-company/workflows/VS-163-electric-vehicle-ev-charging-station-host-network-operations/README.md) | Electric Vehicle (EV) Charging Station Host Network Operations | CORP | Facilities with Digital Commerce |
| [VS-178](../01-model-company/workflows/VS-178-landbanking-site-acquisition-and-agrarian-lgu-zoning-conversion/README.md) | Landbanking, Site Acquisition & Agrarian/LGU Zoning Conversion Operations | CORP | Facilities & Real Estate with Strategy |
| [VS-184](../01-model-company/workflows/VS-184-post-disaster-store-infrastructure-reconstruction-and-rehabilitation/README.md) | Post-Disaster Store Infrastructure Reconstruction & Rehabilitation | CORP | Facilities with Store Operations |

### 4.7 Governance & Assurance (37 VS → no dedicated team; embedded controls)

> These value streams are enabled by the product teams that own the systems the controls run
> in. Demand-side owners are Internal Audit & Risk, Legal & Compliance, and the respective
> program owners named below; the SEC GRC/controls cell (§5.3) coordinates control design and
> test coverage against the 808-control register in
> [`internal-controls-matrix.md`](../01-model-company/internal-controls-matrix.md).

| VS | Value Stream | Team | Business Process Owner |
|---|---|---|---|
| [VS-21](../01-model-company/workflows/VS-21-internal-audit-risk/README.md) | Internal Audit & Risk | CORP | Internal Audit & Risk (Board Audit Committee) |
| [VS-22](../01-model-company/workflows/VS-22-compliance-regulatory/README.md) | Compliance & Regulatory | CORP | Legal & Compliance |
| [VS-23](../01-model-company/workflows/VS-23-loss-prevention/README.md) | Loss Prevention & Asset Protection | SSP | Regional Loss Prevention |
| [VS-24](../01-model-company/workflows/VS-24-health-safety-environment/README.md) | Health, Safety & Environment | CORP | HSE |
| [VS-25](../01-model-company/workflows/VS-25-esg-sustainability/README.md) | ESG & Sustainability | CORP | Sustainability/ESG |
| [VS-26](../01-model-company/workflows/VS-26-business-continuity-insurance/README.md) | Business Continuity & Insurance | INFRA | Internal Audit & Risk with CIO Office (DR owner) |
| [VS-31](../01-model-company/workflows/VS-31-quality-management/README.md) | Quality Management & Product Compliance | CORP | Quality Management |
| [VS-33](../01-model-company/workflows/VS-33-strategic-planning/README.md) | Strategic Planning & Corporate Performance Management | DP | Strategy/Corporate Planning |
| [VS-36](../01-model-company/workflows/VS-36-corporate-governance/README.md) | Corporate Governance & Board Management | CORP | Corporate Secretary |
| [VS-69](../01-model-company/workflows/VS-69-typhoon-disaster-response/README.md) | Typhoon & Natural Disaster Preparedness & Response | INFRA | HSE with Store Operations and CIO Office |
| [VS-71](../01-model-company/workflows/VS-71-anti-counterfeit-authentication/README.md) | Anti-Counterfeit & Product Authentication | CORP | Quality Management with Loss Prevention |
| [VS-73](../01-model-company/workflows/VS-73-store-waste-circular-economy/README.md) | Store-Level Waste Management & Circular Economy | CORP | Sustainability/ESG with Store Operations |
| [VS-76](../01-model-company/workflows/VS-76-multi-region-lgu-compliance/README.md) | Philippine Multi-Region LGU & Local Regulatory Compliance | CORP | Legal & Compliance (Regulatory) |
| [VS-85](../01-model-company/workflows/VS-85-mandatory-discount-eligibility-tax-credit/README.md) | Mandatory Discount, Eligibility & Tax Credit Recovery | SSP | Store Operations with Tax |
| [VS-86](../01-model-company/workflows/VS-86-anti-financial-crime-aml-abc/README.md) | Anti-Financial Crime, AML/KYC & Anti-Corruption | FIN | Legal & Compliance (AML/MLRO) with Finance |
| [VS-87](../01-model-company/workflows/VS-87-customs-trade-compliance-tariff/README.md) | Customs Trade Compliance & Tariff Optimization | WLI | Supply Chain (Imports & Customs) |
| [VS-88](../01-model-company/workflows/VS-88-document-control-records-retention/README.md) | Document Control, Records Management & Retention | CORP | Legal & Compliance with Finance |
| [VS-89](../01-model-company/workflows/VS-89-product-recall-safety-corrective-action/README.md) | Product Recall & Safety Corrective Action Management | WLI | Quality Management with Store Operations |
| [VS-91](../01-model-company/workflows/VS-91-consumer-data-privacy-protection/README.md) | Consumer Data Privacy & Data Protection Program | SEC | Legal & Compliance (DPO) |
| [VS-100](../01-model-company/workflows/VS-100-legal-operations-litigation-ip-management/README.md) | Legal Operations, Litigation & Intellectual Property Management | CORP | Legal & Compliance |
| [VS-104](../01-model-company/workflows/VS-104-government-affairs-public-policy-industry-relations/README.md) | Government Affairs, Public Policy & Industry Relations | CORP | Legal & Compliance (Government Affairs) |
| [VS-114](../01-model-company/workflows/VS-114-dangerous-goods-hazmat-transport-ecommerce-regulatory-compliance/README.md) | Dangerous Goods (DG) & Hazmat Transport, Ecommerce & Regulatory Compliance | WLI | Fleet & Logistics with HSE |
| [VS-117](../01-model-company/workflows/VS-117-dti-bps-product-standards-certification-ps-mark-icc-compliance/README.md) | DTI-BPS Product Standards Certification & PS Mark/ICC Compliance | MSC | Quality Management with Merchandising |
| [VS-119](../01-model-company/workflows/VS-119-whistleblower-ethics-and-corporate-integrity-speak-up-program/README.md) | Whistleblower, Ethics & Corporate Integrity (Speak-Up) Program | CORP | Legal & Compliance |
| [VS-129](../01-model-company/workflows/VS-129-competition-and-antitrust-compliance/README.md) | Competition & Antitrust Compliance (RA 10667 / PCC) | CORP | Legal & Compliance |
| [VS-130](../01-model-company/workflows/VS-130-corporate-development-ma-divestiture/README.md) | Corporate Development, Mergers, Acquisitions, Divestiture & Strategic Transactions | CORP | Strategy with Legal & Compliance |
| [VS-132](../01-model-company/workflows/VS-132-corporate-political-engagement-election-compliance/README.md) | Corporate Political Engagement, Election Compliance & Public Affairs Governance | CORP | Legal & Compliance |
| [VS-133](../01-model-company/workflows/VS-133-operational-excellence-process-mining-continuous-improvement/README.md) | Operational Excellence, Process Mining & Continuous Improvement Program | DP | Strategy with COO Office |
| [VS-146](../01-model-company/workflows/VS-146-customer-mystery-shopping-and-service-quality-assurance/README.md) | Customer Mystery Shopping & Service Quality Assurance Program | CCP | Customer Service with Marketing |
| [VS-147](../01-model-company/workflows/VS-147-customer-safety-premises-liability-and-in-store-risk-management/README.md) | Customer Safety, Premises Liability & In-Store Risk Management | SSP | Store Operations with HSE |
| [VS-152](../01-model-company/workflows/VS-152-corporate-social-responsibility-foundation-and-community-investment/README.md) | Corporate Social Responsibility, Foundation & Community Investment | CORP | Sustainability/ESG |
| [VS-159](../01-model-company/workflows/VS-159-corporate-security-executive-protection-and-travel-risk-management/README.md) | Corporate Security, Executive Protection & Travel Risk Management | CORP | Loss Prevention (Corporate Security) with Legal & Compliance |
| [VS-161](../01-model-company/workflows/VS-161-third-party-and-supplier-risk-management-tprm/README.md) | Third-Party & Supplier Risk Management (TPRM) | SEC | Internal Audit & Risk with Legal & Compliance |
| [VS-165](../01-model-company/workflows/VS-165-pcab-contractor-licensing-and-ra-4566-construction-contractor-compliance/README.md) | PCAB Contractor Licensing & RA 4566 Construction Contractor Compliance | CORP | Legal & Compliance (Regulatory) |
| [VS-166](../01-model-company/workflows/VS-166-regulatory-license-permit-and-accreditation-portfolio-management/README.md) | Regulatory License, Permit & Accreditation Portfolio Management | CORP | Legal & Compliance (Regulatory) |
| [VS-179](../01-model-company/workflows/VS-179-extended-producer-responsibility-compliance-and-plastic-recovery-network/README.md) | Extended Producer Responsibility (EPR) Compliance & Plastic Recovery Network | CORP | Sustainability/ESG |
| [VS-187](../01-model-company/workflows/VS-187-household-hazardous-waste-paint-and-product-stewardship-take-back/README.md) | Household Hazardous Waste, Paint & Used-Product Stewardship Take-Back Program | CORP | Sustainability/ESG with Store Operations |

### 4.8 Technology & Data (13 VS → owned by platform teams and CIO Office)

| VS | Value Stream | Team | Business Process Owner |
|---|---|---|---|
| [VS-27](../01-model-company/workflows/VS-27-it-operations-security/README.md) | IT Operations & Security | INFRA | CIO Office (co-owned with SEC) |
| [VS-28](../01-model-company/workflows/VS-28-data-analytics-bi/README.md) | Data, Analytics & BI | DP | CIO Office with Strategy |
| [VS-29](../01-model-company/workflows/VS-29-master-data/README.md) | Master Data Management | DP | CIO Office with Merchandising Operations & Master Data |
| [VS-30](../01-model-company/workflows/VS-30-innovation-digital/README.md) | Innovation & Digital Transformation | CIO Office | CEO with CIO |
| [VS-99](../01-model-company/workflows/VS-99-it-asset-technology-lifecycle-management/README.md) | IT Asset & Technology Lifecycle Management | FS | CIO Office |
| [VS-113](../01-model-company/workflows/VS-113-enterprise-architecture-application-portfolio-and-technology-strategy/README.md) | Enterprise Architecture, Application Portfolio & Technology Strategy | CIO Office | CIO |
| [VS-115](../01-model-company/workflows/VS-115-calibration-metrology-and-measurement-traceability-management/README.md) | Calibration, Metrology & Measurement Traceability Management | CORP | Quality Management (Metrology) with Facilities |
| [VS-126](../01-model-company/workflows/VS-126-customer-data-platform-single-customer-view-identity-resolution/README.md) | Customer Data Platform, Single Customer View & Identity Resolution | DP | Marketing with CIO Office |
| [VS-128](../01-model-company/workflows/VS-128-ai-ml-governance-responsible-ai/README.md) | AI/ML Governance & Responsible AI | DP | CIO Office with Legal & Compliance (AI Governance) |
| [VS-135](../01-model-company/workflows/VS-135-technology-business-management-it-financial-management-cloud-finops/README.md) | Technology Business Management, IT Financial Management & Cloud FinOps | CIO Office | CIO with Finance |
| [VS-137](../01-model-company/workflows/VS-137-product-information-management-and-digital-asset-management/README.md) | Product Information Management (PIM) & Digital Asset Management (DAM) | DP | Merchandising (Master Data) with Digital Commerce |
| [VS-151](../01-model-company/workflows/VS-151-auto-id-barcode-rfid-labeling-and-eas-operations/README.md) | Auto-ID, Barcode, RFID, Price-Tag Labeling & EAS Operations | SSP | Store Operations with Loss Prevention |
| [VS-190](../01-model-company/workflows/VS-190-operational-technology-ot-ics-cybersecurity-and-retail-technology-asset-protection/README.md) | Operational Technology (OT) / ICS Cybersecurity & Retail Technology Asset Protection | SEC | IT Security with Loss Prevention |

### 4.9 Mapping reconciliation

| Team | VS | Workflows |
|---|---|---|
| MSC | 15 (§4.1) + 1 (VS-117) | 486 |
| WLI | 17 (§4.2) + 3 (VS-87, VS-89, VS-114) | 526 |
| SSP | 20 (§4.3) + 1 (VS-59) + 3 (VS-23, VS-85, VS-147) + 1 (VS-151) | 907 |
| CCP | 24 (§4.3) + 1 (VS-146) + 1 (VS-14, batch 23) | 742 |
| FIN | 29 (§4.4) + 1 (VS-86) | 809 |
| CORP | 12 (§4.6) + 22 (§4.7) + 1 (VS-115) + 1 (VS-24, batch 23) | 924 |
| PEO | 16 (§4.5) | 445 |
| OMO | 1 (VS-60, from §4.3) | 24 |
| TPS | 2 (§4.2: VS-74, VS-143) + 1 (§4.3: VS-77) | 72 |
| INFRA | 2 (VS-26, VS-69) + 1 (VS-27, incl. the W5518–W5524 IT gap fill) + 2 (batch 23: the VS-26 coastal-intrusion canon and the VS-27 server-room environmental canon) | 126 |
| SEC | 2 (VS-91, VS-161) + 1 (VS-190) | 72 |
| DP | 2 (VS-33, VS-133) + 5 (VS-28, VS-29, VS-126, VS-128, VS-137) | 189 |
| FS | 1 (VS-99) | 24 |
| SEP | 0 (build-enablement platform for OMO/TPS) | 0 |
| AAP | 0 (agentic-automation enablement platform) | 0 |
| CIO Office | 3 (VS-30, VS-113, VS-135) | 81 |
| **Total** | **171 + 17 = 188** | **4,935 + 492 = 5,427** |

---

## 5. Product-Team Membership & Roles

### 5.1 Domain-team shapes — three archetypes

Sourcing decisions shape domain teams into three archetypes
([`capability-sourcing-and-engineering-model.md`](capability-sourcing-and-engineering-model.md) §5):
**configure** teams (MSC, FIN, PEO, CORP), **configure-and-integrate** teams (WLI, SSP, CCP), and
**build** squads (OMO, TPS, plus the doctrine's new build scope — Payroll PH, store workforce,
dispatch). All three start from the same 6-role core below; the
configure-and-integrate teams add the product/vendor management role, and build squads are staffed
per the squad table at the end of this section. IT headcount figures below are FTE; §9 sizes
each team.

| Member | IT HC | Reports to | Role & Responsibilities |
|---|---|---|---|
| **IT Product Owner (PO)** | 1 | CIO (solid); product-domain exec (dotted) | Single accountable owner of the product backlog, roadmap, and budget. Prioritizes enhancements, defects, regulatory changes, and tech debt. Owns product KPIs (§8.3). Represents the product at the Product Council. Manages the vendor relationship for the product's ERP modules (escalations, roadmap influence, release intake). |
| **Product/Process Architect** | 1 | Head of EA (solid); team PO (dotted) | Owns end-to-end process design across the team's process areas; enforces fit-to-standard; maintains the team's portion of the enterprise architecture (VS-113); chairs the team's design reviews; prepares customization-exception requests for the Architecture Review Board. |
| **ERP Functional Analysts / Configurators** | 2–4 | Team PO | Day-to-day configuration of the ERP core (and, in configure-and-integrate teams, the integration surfaces of the already-built platforms and the in-suite add-ons): approval matrices, pricing rules, warehouse/transport parameters (Oracle WMS/MSCA, Shipping/OTE), tax setups, workflow conditions. Analyze incidents that are configuration defects. Write functional specifications for integrations and reports. Each analyst owns named sub-domains (e.g., AP vs AR vs tax inside FIN). |
| **Commerce/App Engineer** (CCP only) | 1 | Team PO | Builds and maintains the custom edge on top of the SaaS ecommerce engine — storefront theming, mobile-app releases, marketplace connectors — under platform standards (IAP APIs, CI/CD). |
| **Data & Reporting Analyst** | 1 | Team PO (solid); DP lead (dotted) | Product-specific dashboards and reports on the DP semantic layer; data-quality checks on the product's master-data domains; close-cycle reporting (e.g., FIN's 5-working-day close pack). |
| **QA & Release Analyst** | 1 | Team PO | Owns the regression suite (every Tier-1 workflow in the domain covered), UAT coordination with business SMEs, release notes, cutover checklists, and post-release verification. |

> **Configure-and-integrate teams (WLI, SSP, CCP) add:** one **Platform Product Manager**
> each (v3.12), re-pointed by the two-tier doctrine — WLI: the **chain-wide Oracle
> relationship and in-suite currency** (one account-team interface for all EBS modules:
> license/support position, RUP/CPU calendar, ADOP rehearsal discipline, escalations; the
> in-suite currency KPI owner) plus supply-chain in-suite currency for Oracle WMS/MSCA +
> Shipping/OTE — with module-level release/roadmap intake staying with every PO; SSP: the
> already-built POS platform and the store-workforce build; CCP: the already-built
> ecommerce/loyalty platforms and the dispatch build — release intake, roadmap intelligence,
> upgrade currency, and the TPRM (VS-161) operational liaison. Commercial ownership of the
> vendor-commodity line (LLM APIs, managed services, hardware/licenses) consolidates in the
> CIO Office vendor-portfolio analyst (§5.3), the teams keeping operational SLA ownership;
> plus added functional-analyst depth for the in-suite add-ons' configuration surface
> (WLI's second vendor seat converts to a fifth analyst — §9.1).

**Build-squad shape (OMO, TPS).** The two in-house products are delivered by stable software
squads on the SEP paved road (sourcing model §5–§7):

| Member | IT HC | Reports to | Role & Responsibilities |
|---|---|---|---|
| **Product Manager (PM)** | 1 | CIO (solid); product-domain exec (dotted) | The build-side equivalent of the IT PO: outcomes, discovery, roadmap, and budget; pairs with the BPO like any domain PO; owns product KPIs (§8.3) and delivery trade-offs. |
| **Tech Lead** | 1 | Head of Engineering (solid); squad PM (dotted) | Technical design authority for the product; chairs squad design reviews; holds the product's seat in the architect community; prepares ARB records for the product. |
| **Software Engineers** | 3–4 | Tech Lead | Build and run the product: implementation, code review, P1/P2 on-call, telemetry, and the FinOps-tagged cost of the services they own. |
| **QA Automation Engineer** | 1 | Squad PM | Automated acceptance and contract tests, regression harness, ring-release verification — the build twin of the configure teams' QA & release analyst. |
| **UX / Product Designer** | 0.5 (SEP pool) | Head of Engineering | Flows, screens, and usability for the product's internal and customer-facing surfaces. |
| *Dotted:* IAP engineer (0.4) + DP data analyst | — | — | Matrixed integration-touchpoint owner and data-contract steward, same matrix rules as configure teams (§5.4). |

### 5.2 Business-side membership (not IT headcount)

| Member | Source | Commitment | Role & Responsibilities |
|---|---|---|---|
| **Business Product Owner (BPO)** | The department named "Business Process Owner" in §4 | ~30–50% | Owns requirements and business value; accepts releases into the business; drives user adoption; decides process-change vs configuration-change trade-offs; co-signs the roadmap. Named individuals, e.g., the S&OP/IBP Lead is the standing BPO for MSC's VS-127 scope; the Controller for FIN. |
| **Business SMEs** | Named per sub-domain (a buyer, a DC manager, a store manager, an AP clerk, a payroll officer) | ~5–10% each, 2–4 people per team | Consulted continuously on design; participate in UAT as first users; validate training content; feed pain points into the backlog. |
| **Change & Training Lead** | Shared pool under HR (Training) with CIO Office funding | ~0.25–0.5 FTE per team | Training curriculum and materials per release, adoption metrics, floor-walking for major rollouts — essential for 6,911 users of varying tech literacy across the archipelago. |

> These roles sit in their own §3.3 departments and are **not** counted in the 122-FTE IT
> sizing (§9). Their time commitments are agreed in each BPO's objectives, reviewed at the
> Quarterly Business Review.

### 5.3 Platform teams

| Platform Team | Members (§9) | Role & Responsibilities |
|---|---|---|
| **Integration & API Platform (IAP)** | Platform lead; 5 integration engineers; 1 events/monitoring engineer; 1 API-contract engineer; 1 integration-support engineer | Owns the integration backbone all product teams consume: middleware/iPaaS, event streaming (near-real-time POS-to-ERP inventory sync), API standards and contracts, error handling and replay, integration monitoring dashboards. Under the two-tier landscape IAP additionally owns the **canonical event/API contract catalog** with consumer-driven contract testing for every product-to-product flow (the in-suite WMS, the already-built POS/ecommerce platforms and in-house OMO/TPS included) — the single-integration-path rule of the sourcing model. Owns the ~10 external integration clusters of `data-volumes-and-integrations.md` (payment gateways, banks, BIR eFPS, SSS/PhilHealth/Pag-IBIG, delivery partners, loyalty engine, WMS RF, supplier portal). Most engineering-heavy team. |
| **Cloud Infrastructure & SRE (INFRA)** | Lead; 2 cloud engineers; 1 network engineer; 1 SRE; 1 DBA/SaaS administrator | Uptime (POS 99.9%, back-office 99.5%), performance (POS transaction < 3s; standard reports < 30s), environment management, patch intake, DR/BCP execution (typhoon resilience, VS-26/VS-69), capacity planning for the 1,000–1,500 peak concurrent users (§15.3). |
| **Cybersecurity, Privacy & OT Security (SEC)** | Lead; 2 security engineers; 1 security analyst; 2 GRC/controls analysts; 1 TPRM analyst | SOC liaison and monitoring (with managed-SOC partner), vulnerability management, penetration-test remediation, access reviews and SOD enforcement, RA 10173 privacy program support with the DPO (VS-91), OT/retail-tech security for POS terminals, RF guns, CCTV (VS-190), third-party risk assessments (VS-161). The second security engineer pairs with SEP's AppSec engineer on SDLC gates for built products; the TPRM analyst carries vendor tiering and annual reassessments (commodity vendors — LLM APIs, managed services — under the two-tier doctrine). The GRC/controls analysts form the **enabling cell** that coordinates control design, test evidence, and audit responses across all product teams against the 808-control register. |
| **Data Platform & MDM (DP)** | Lead; 3 data engineers; 2 MDM stewardship leads; 1 BI platform administrator | Data warehouse and semantic layer; the item/customer/vendor/employee master-data platforms (55,000-SKU item master; ~600,000 loyalty members); CDP/identity resolution (VS-126); PIM/DAM (VS-137); AI/ML governance tooling (VS-128); process-mining platform (VS-133). Under the two-tier landscape the second steward carries dual-record harmonization (e.g., execution-state data from the in-suite WMS and the built platforms vs the ERP ledger) and the data-contract tests built products publish against (§6.3; sourcing model §7). Domain data analysts build on DP's certified layer; DP enforces the shared-object change process (§6.3). |
| **Software Engineering Platform (SEP)** | Head of Engineering; 2 DevEx engineers; 1 AppSec engineer; 1 QA automation lead; 1 UX/product designer; 1 build SRE | The paved road for in-house products (OMO, TPS): golden-path templates, CI/CD, feature flags and telemetry, SAST/DAST/dependency/SBOM security gates, the shared test and contract-testing harness, ring-deployment infrastructure, production-readiness reviews, and the engineering career track. Full definition in [`capability-sourcing-and-engineering-model.md`](capability-sourcing-and-engineering-model.md) §6. Treats build squads as customers; nothing ships off the paved road without an ARB-recorded exception. |
| **AI & Agent Platform (AAP)** | Platform lead; 3 agent engineers; 1 evaluation/AI-QA engineer; 1 agent-ops SRE; 1 AI-governance liaison (dotted to the VS-128 program and SEC) | The paved road for **agentic automation**: the agent runtime and tool registry (agents may only call IAP-published contracts — never a database directly), guardrails and human-in-the-loop gates, the evaluation harness (offline evals → shadow → canary), agent observability and cost telemetry, non-human identity management, and the kill-switch infrastructure. Agents are delivered by the owning domain product teams on this platform; AAP enables and governs the runtime (full program definition in the sourcing model §12). VS-128 retains the governance discipline — registry, risk tiering, ethics review, AI incident management. |
| **Field & End-User Services (FS)** | Supervisor; 2 helpdesk L2 analysts; 1 ITAM administrator; 5 regional field technicians (one per major island region: Mindanao, Visayas, South Luzon, Metro Manila, North/Central Luzon) | L1 (outsourced contact center) and L2 support for 200 stores, 4 DCs, and HQ; hardware lifecycle for the 600-terminal POS estate, RF guns, biometric devices, and printers (VS-99); store-visit SLAs and storm-season readiness stock. This team closes the archipelago field-support gap flagged in `headcount-reality-check.md` §3.2. |
| **CIO Office** | Head of Enterprise Architecture; 1 portfolio-governance lead; 1 FinOps/TBM analyst; 1 vendor-portfolio analyst | Chairs the Architecture Review Board (VS-113); runs the Product Council secretariat and portfolio kanban; IT financial management and cloud FinOps (VS-135); innovation pipeline governance (VS-30). The vendor-portfolio analyst maintains the Capability Sourcing Register and the vendor-contract/sourcing-reserve records (sourcing model §4, §8), and — since v3.12 — holds the **commercial ownership of the vendor-commodity line** (contracts, price-escalation caps, renewal/exit clauses, tier-1 TPRM interface) across all teams, so the doctrine's commodity-only vendor estate is managed with one register and one negotiating posture. The CIO is counted in the Executive Office (§11.1), not in IT headcount. |

### 5.4 Role definitions (cross-team reference)

| Role | Definition |
|---|---|
| **Accountable (single-wielder) roles** | Each product has exactly one IT PO and one BPO. Each platform has exactly one lead. Single-point accountability mirrors the "single accountable owner" fix applied to VS-127. |
| **Matrixed integration analyst** | IAP integration engineers are matrixed ~0.4 FTE to each domain team as its touchpoint owner; they sit in domain ceremonies and hold the domain's integration health. Build squads get the same matrixed touchpoint owner. |
| **Platform Product Manager** (v3.12; formerly Product/Vendor Manager) | One seat per configure-and-integrate team (WLI, SSP, CCP). WLI's seat is the **Oracle Relationship & In-Suite Currency Manager** — the single chain-wide interface to the Oracle account team (license/support position, RUP/CPU calendar, escalation path) and the in-suite currency KPI owner (sourcing model §8); SSP's and CCP's seats product-manage the already-built in-house platforms (POS estate; ecommerce/loyalty/gift-card) and liaise their in-house builds (store workforce; dispatch). Release-intake owner, roadmap intelligence, TPRM operational liaison per team; commercial contract ownership for the vendor-commodity line sits with the CIO Office vendor-portfolio analyst (§5.3). |
| **Engineering career track** | All software engineers, tech leads, DevEx, AppSec, build-SRE and the UX pool sit on one track under the Head of Engineering (SEP) — hired centrally, staffed to squads, never squad-owned. Bus-factor ≥ 2 per service is a standing rule (sourcing model §11). |
| **Architect community** | The domain architects (the MSC/WLI/SSP/CCP/FIN/PEO product architects — FIN's covering CORP — plus the OMO/TPS tech leads) and the IAP/INFRA/SEC/DP/SEP/AAP leads form the Architecture Review Board quorum, chaired by the Head of EA. |
| **Escalation path** | L1 (outsourced) → FS L2 → domain functional analyst (config defects) or IAP (integration) or INFRA (platform) → PO → Product Council for prioritization conflicts. |

---

## 6. RACI

RACI key per [`WORKFLOW-FORMAT-GUIDE.md`](../01-model-company/workflows/WORKFLOW-FORMAT-GUIDE.md): **R** = Responsible, **A** = Accountable (exactly one per activity), **C** = Consulted, **I** = Informed.

### 6.1 Delivery activities (per domain team)

| Activity | IT PO | BPO | Architect | Functional Analyst | QA/Release | ARB |
|---|---|---|---|---|---|---|
| Product roadmap & backlog prioritization | A/R | C | C | C | I | I |
| Annual funding ask & capacity plan | A/R | C | C | I | I | I |
| Process design & fit-to-standard decision | C | A | R | R | I | C |
| Configuration change (within own domain) | A | C | C | R | C | I |
| Customization-exception request | R | C | R | C | I | A |
| Capability sourcing decision (use-EBS/build) | R | C | R | C | I | C (SIB gate; Council ratifies >PHP 25M TCO) |
| UAT execution | R | A | I | C | R | I |
| Regression-pack maintenance | I | I | C | C | A/R | I |
| Production release (monthly train) | A | C | I | C | R | I |
| Post-release verification & adoption tracking | A | R | I | C | R | I |

### 6.2 Run & operate

| Activity | FS (L1/L2) | Domain Team | INFRA/SRE | SEC | BPO |
|---|---|---|---|---|---|
| P1 incident (e.g., store POS down) | R | A | R | C | I |
| P2/P3 incident & configuration defect | R | A | C | I | C |
| Root-cause analysis & problem record | C | A/R | C | C | I |
| Access request processing & SOD review | R | C | I | A | C |
| Vendor ERP release intake & regression | I | A/R | R | C | C |
| DR exercise (annual, pre-typhoon season) | R | C | A/R | C | I |
| New-store technology commissioning | R | A (SSP) | C | C | I |
| P1 on a bought product (vendor-side defect) | R | A | C | I | I |
| P1 on a built product (code defect; squad on-call) | R | A | R | C | I |

### 6.3 Shared-object changes & controls

| Activity | Requesting Team | Owning Team | Platform (DP or IAP) | ARB |
|---|---|---|---|---|
| Item master / pricing object change | R | C | A (DP) | C |
| Chart-of-accounts segment change | R | C (FIN owns) | A (DP) | C |
| Customer master model change | R | C (CCP owns) | A (DP) | C |
| Integration contract change | R | C | A (IAP) | C |
| Control change touching Tier-1 workflows | R | A | C (SEC GRC cell) | I |

> For control changes, the SEC GRC cell validates design, the owning team's QA analyst
> validates test evidence, and Internal Audit is informed through the monthly Tier & Control
> Board (§7).

### 6.4 Build-squad delivery (OMO, TPS)

| Activity | Squad PM | Tech Lead | Engineers | QA Automation | SEP | ARB |
|---|---|---|---|---|---|---|
| Discovery & outcome roadmap | A/R | C | C | C | I | I |
| Technical design & architecture record | C | A/R | R | C | C | C |
| Code, peer review & merge to trunk | I | A | R | C | C (golden path) | I |
| Security gate before ring expansion | I | R | R | R | A (AppSec may block) | I |
| Ring deployment (internal → canary → fleet) | C | A | R | R | C | I |
| Production on-call, incident & rollback | C | A | R | C | C | I |

---

## 7. Governance Bodies

| Body | Cadence | Chair | Members | Decision Rights |
|---|---|---|---|---|
| **Product Council** | Monthly | CIO | 9 domain POs/PMs; BPOs or executive delegates (CFO/COO/CMO/CHRO offices); Head of EA; FinOps analyst with vendor-portfolio analyst (secretariat) | Capacity allocation between products (funding runs, not projects); roadmap approval above PHP 5M; cross-product priority conflicts; product KPI review; new-product creation or team split/merge recommendations; ratifies Sourcing & Investment Board recommendations above PHP 25M 3-year TCO |
| **Sourcing & Investment Board (SIB)** | Monthly + on demand | CIO | Head of EA (assessment lead); affected IT PO/PM and BPO; FinOps analyst; CFO delegate; SEC lead (TPRM); Head of Engineering (build decisions); AAP lead (agentic decisions) | Use-EBS/build routing for every capability (the ordered test: in-EBS → build; the fit-gap register is the standing evidence base); agent-automation decisions incl. the Tier-based autonomy ladder; maintains the Capability Sourcing Register; recommends >PHP 25M-TCO decisions to the Product Council; core-tier waiver recommendations to the CEO (sourcing model §3) |
| **Architecture Review Board (ARB)** | Bi-weekly | Head of EA | Domain architects (incl. the OMO/TPS tech leads); IAP, INFRA, SEC, DP, SEP leads | Customization exceptions; new applications, integrations, or data pipelines; architecture opinions on sourcing proposals; retirement of capabilities; waivers removing a capability from the ERP core (rare, CEO-noted; core guardrail per the sourcing model §2) |
| **Product Sync** | Weekly | Rotating PO | Domain POs/PMs; platform leads (IAP, INFRA, SEC, DP, SEP); FS supervisor | Dependency sequencing; release-window and contract-change coordination across the ERP train, vendor release intake, and build-squad rings; matrixed-resource booking; incident-trend review |
| **Tier & Control Board** | Monthly | SEC GRC lead (senior analyst) | Domain QA/release analysts; Internal Audit liaison; Legal & Compliance liaison | Sign-off on changes touching Tier-1 workflows; audit-finding remediation tracking; annual control-test calendar against the 808-control register |
| **Quarterly Business Review (QBR)** | Quarterly | CIO with CEO/CFO/COO | Executive team; POs presenting their products | Outcome review against KPIs; funding continuation; BPO time-commitment health; structural adjustments (headcount reallocation between products) |

**Internal-audit independence:** the Tier & Control Board coordinates with Internal Audit &
Risk, which retains its Board Audit Committee reporting line per `model-company-profile.md`
§11.1 note 1 — the Board does not sit under the CIO.

---

## 8. Operating Cadence, Releases, KPIs & Funding

### 8.1 Cadence

| Rhythm | Activity |
|---|---|
| Continuous | Backlog refinement with BPO; incident and problem management; P2/P3 fixes |
| 2-week | Team build cycles: configuration, integration, and report work items; demo to BPO/SMEs |
| Monthly | ERP-core release train (RUP/CPU) + in-suite adoption + build/platform release intake (see §8.2); Product Council; Sourcing & Investment Board; Tier & Control Board |
| Quarterly | Roadmap re-plan fed by S&OP/IBP outputs and seasonal calendar; QBR; funding reallocation |
| Annual | IT plan aligned to corporate budget; DR exercise before typhoon season; penetration test; control-test calendar refresh |

### 8.2 Release cadences by archetype

The single monthly cross-product train of v1.x is replaced by per-archetype cadences, still
sequenced by Product Sync and **avoiding the bi-monthly sale-event windows and the December
peak** (§13.2 seasonal calendar):

- **Configure (ERP core):** the monthly release train as in v1.x, executed by the QA/release
  analysts. Each release carries: regression evidence (Tier-1 coverage mandatory), release
  notes for BPOs, updated training content, and a rollback plan. Vendor ERP releases are
  intake-tested by INFRA and domain teams in a staging ring before the train.
- **Vendor commodities (LLM APIs, managed services):** vendor changes are intake-checked by
  the team's Platform Product Manager against contract and TPRM terms, with contract,
  renewal and exit-clause actions executed by the CIO Office vendor-portfolio analyst
  (§5.3). No capability products are bought under the two-tier doctrine, so no BoB release
  train exists; the already-built platforms (POS, ecommerce, loyalty) release on the build
  cadence below, owned by their teams.
- **Build (OMO, TPS):** continuous delivery on the SEP ring model (internal → canary
  stores/DCs → fleet) behind feature flags, with SLO-burn rollback gates (sourcing model §7),
  independent of the monthly train.

### 8.3 Product KPIs (headline set)

| Team | KPIs (targets per `model-company-profile.md` §12.3/§15.3) |
|---|---|
| SSP | POS uptime ≥ 99.9%; transaction processing < 3s; offline continuity ≥ 8h; store-critical incident MTTR; price-label sync accuracy |
| MSC | Forecast accuracy and bias (S&OP); automated ROP release adoption; vendor-scorecard data freshness |
| WLI | Inventory accuracy ≥ 97%; RF transaction success rate; DC throughput report freshness; transfer-order cycle time; in-suite supply-chain currency (Oracle WMS/MSCA + Shipping/OTE current within one RUP) |
| CCP | BOPIS 4-hour pick SLA; order-routing success rate; ecommerce uptime; catalog data completeness |
| FIN | Month-end close ≤ 5 working days; 3-way-match automation rate; BIR filing timeliness (zero penalties) |
| PEO | Payroll accuracy and on-time runs (semi-monthly, 5 entities); statutory remittance accuracy |
| CORP | Permit/renewal tracking completeness; GRC platform adoption; audit-finding closure rate |
| OMO | Routing decision latency; split-order/mixed-basket success rate; order-event end-to-end latency; DORA four (deployment frequency, lead time, MTTR, change-failure rate) |
| TPS | On-time job-site/phased delivery; staging schedule adherence; technician-app adoption; DORA four |
| IAP | Integration availability; event-streaming latency (inventory sync near-real-time, < 30s per POS-013); contract coverage; contract-test pass rate across the product-to-product catalog |
| INFRA | POS 99.9% / back-office 99.5%; report generation < 30s; DR RTO/RPO met in exercises |
| SEC | Vulnerability SLA compliance; access-review completion; privacy DSAR turnaround; zero material incidents |
| DP | Master-data quality scores (item/customer/vendor); dashboard freshness; AI-model governance coverage |
| FS | First-contact resolution; regional store-visit SLA; POS terminal MTTR; asset-register accuracy |
| SEP | Paved-road adoption (share of build traffic on the golden path = 100% minus ARB-recorded exceptions); pipeline availability; AppSec gate pass rate; squad DORA attainment (enablement) |
| AAP | Hours of manual work automated per month; agent task success rate; human-takeover/escalation rate; agent incident MTTR; cost-per-task vs human baseline; agents registered & current in the VS-128 registry (100%) |

### 8.4 Funding model

- **Persistent capacity funding**: each product receives an annual envelope sized at Product
  Council and re-allocatable quarterly at the QBR — no project-based funding for steady-state
  work.
- **Central surge pool** (CIO Office): a small bucket for statutory mandates that land on any
  team (e.g., BIR e-invoicing readiness, eFPS form changes), protecting team capacity plans.
- **Innovation fund** (VS-30): competitive bids presented at the Product Council; prototypes
  run through the ARB before production.
- **Sourcing & exit reserves (CIO Office):** a central sourcing reserve funds transitions
  (evaluations, migrations, exits) so no team's steady-state capacity is cannibalized by a
  sourcing move; replaceable vendor dependencies accrue funded exit reserves — the
  already-built in-house platforms are forever by doctrine (sourcing model §9).
- **Capitalization of built products:** qualifying in-house development costs are assessed
  for PFRS/IAS 38 capitalization quarterly with FIN (Controller) — FIN owns the accounting
  policy, the squads own the evidence trail.
- **FinOps discipline** (VS-135): the FinOps analyst reports cloud/SaaS spend per product at
  every QBR, tagging 100% of spend to products.

---

## 9. Sizing & Headcount Reconciliation

### 9.1 Steady-state design (122 IT FTE)

| Team | PO/PM | Architect/TL | Functional Analysts | Engineers | Data Analyst | QA/Release | Platform PM | Platform Roles | Total |
|---|---|---|---|---|---|---|---|---|---|
| MSC | 1 | 1 | 3 | — | 1 | 1 | — | — | 7 |
| WLI | 1 | 1 | 5 | — | 1 | 1 | 1 | — | 10 |
| SSP | 1 | 1 | 4 | — | 1 | 1 | 1 | — | 9 |
| CCP | 1 | 1 | 2 | 1 | 1 | 1 | 1 | — | 8 |
| FIN | 1 | 1 | 4 | — | 1 | 1 | — | — | 8 |
| CORP | 1 | — (¹) | 2 | — | — (¹) | 1 | — | — | 4 |
| PEO | 1 | 1 | 2 | — | 1 | 1 | — | — | 6 |
| OMO | 1 | 1 (TL) | — | 4 | — (²) | 1 | — | — | 7 |
| TPS | 1 | 1 (TL) | — | 4 | — (²) | 1 | — | — | 7 |
| **Domain subtotal** | 9 | 8 | 22 | 9 | 6 | 9 | 3 | — | **66** |
| IAP | — | — | — | — | — | — | — | lead 1 + integration 5 + events 1 + API-contract 1 + support 1 | 9 |
| INFRA | — | — | — | — | — | — | — | lead 1 + cloud 2 + network 1 + SRE 1 + DBA 1 | 6 |
| SEC | — | — | — | — | — | — | — | lead 1 + security eng 2 + analyst 1 + GRC 2 + TPRM 1 | 7 |
| DP | — | — | — | — | — | — | — | lead 1 + data eng 3 + MDM stewardship 2 + BI admin 1 | 7 |
| SEP | — | — | — | — | — | — | — | Head of Eng 1 + DevEx 2 + AppSec 1 + QA-auto lead 1 + designer 1 + build-SRE 1 | 7 |
| AAP | — | — | — | — | — | — | — | lead 1 + agent eng 3 + eval/AI-QA 1 + agent-ops 1 + AI-governance liaison 1 | 7 |
| FS | — | — | — | — | — | — | — | supervisor 1 + L2 2 + ITAM 1 + field techs 5 | 9 |
| CIO Office | — | — | — | — | — | — | — | Head of EA 1 + portfolio 1 + FinOps 1 + vendor-portfolio 1 | 4 |
| **Platform + CIO subtotal** | | | | | | | | | **56** |
| **Total** | | | | | | | | | **122** |

> (¹) CORP is covered by the FIN architect (dotted line) and uses FIN/DP analysts for its
> reporting needs; its GRC-tooling work is co-delivered with the SEC GRC cell. (²) OMO and
> TPS are staffed as build squads (§5.1); their data analysts are matrixed from DP and their
> integration touchpoints from IAP. Steady state under the two-tier capability-sourcing
> doctrine with the agentic platform: domain **66** + platform/CIO **56** = **66 + 56 = 122** IT FTE
> — v1.x unified 80 → v2.0 hybrid 115 → v2.1 agentic 122, the final +7 being the AAP
> platform team. The v3.12 mix re-point (§5.1/§5.4) converts WLI's second product/vendor
> seat into the fifth functional analyst — the in-suite Oracle WMS/MSCA + Shipping/OTE
> configuration depth the doctrine pays for — and retitles the remaining seat Platform
> Product Manager (WLI's doubling as the chain-wide Oracle Relationship & In-Suite Currency
> Manager); team totals, the 66/56 split and 122 are untouched.

### 9.2 Reconciliation to the current state and benchmarks

| Reference | Figure | Source |
|---|---|---|
| Pre-promotion IT department | 50 | `model-company-profile.md` §3.3 (superseded 2026-09-14 — the promotion is §9.1's 122) |
| Gap-record need band (pre-hybrid, single-vendor model) | 65–80 | `headcount-reality-check.md` §3.2 (table row "Information Technology") |
| Two-tier-model need band (in-suite EBS + in-house builds; issued 2026-09-03 as the 'hybrid' amendment, collapsed to two tiers 2026-09-14) | 65–130 | `headcount-reality-check.md` §3.2 amendment (2026-09-03) |
| Industry benchmark | 100–168 (1.5–2.5% of 6,911 headcount); lean outsourced floor ~60–70 | `headcount-reality-check.md` §3.2 |
| This design, v1.x (unified model) | 80 | OM v1.x §9 |
| This design, v2.0 (hybrid) | 115 | OM v2.0 §9 |
| This design, v2.1 (hybrid + agentic) | 122 | §9.1 |

The two-tier design lands mid-benchmark. The +35 over the unified-model 80 (v2.0) is deliberate and
concentrated exactly where the sourcing strategy creates permanent work: two build squads
(+14), the SEP platform (+7), the integration backbone for a multi-product landscape
(IAP +4), security engineering and TPRM for the vendor/software estate (SEC +2), data
contracts and dual-record MDM stewardship (DP +2), and product/vendor management in the
integrate domains (+4, net of configure-side relief — re-pointed by the two-tier doctrine to
the Oracle relationship, in-suite currency and the already-built platforms). The v2.1 agentic extension adds the AAP platform
(+7) — still mid-band (65–130), because agents substitute for task hours across the 6,911-user
base rather than adding transaction-processing headcount. The v1.x argument that single-vendor SaaS
transfers DBA, OS, and availability operations away still holds for the ERP core — which is
why the design sits mid-benchmark and below the 130 ceiling of the two-tier band rather than
at its top. L1 support and the 24/7 SOC remain partner-operated.

### 9.3 Phased build-up (50 → 122)

| Phase | Focus | Net adds | End state |
|---|---|---|---|
| **Phase 0 — Reorganize & decide (next 2 quarters)** | Stand up the first 16 of the 17 teams (9 domain incl. the OMO/TPS squads, 6 platform incl. SEP, CIO Office — the AAP platform team follows in Phase 2), name POs/PMs/BPOs, adopt single backlogs, SIB/ARB/Product Council cadence; issue the first Capability Sourcing Register; SEP nucleus (Head of Engineering + 2 DevEx engineers); CIO Office vendor-portfolio analyst; first senior IAP integration engineer | +5 | ~55 |
| **Phase 1 — Field, backbone & first build** | FS regional field technicians and L2 (the archipelago gap); INFRA to full strength; IAP build-out toward 9; SEC security engineering + TPRM analyst; DP data-contract steward; SEP completed (AppSec, QA-automation lead, designer, build-SRE); **OMO squad #1** — the order-orchestration MVP on the paved road | +35 | ~90 |
| **Phase 2 — In-suite adoption, second build, agentic platform & depth** | Oracle WMS/MSCA + Shipping/OTE adoption (WLI analyst depth); Payroll PH and store-workforce builds (SSP with PEO) and the dispatch build (CCP) — per the two-tier doctrine; **TPS squad #2**; **AAP stand-up** (lead, agent engineers, evaluation engineer — the crawl-phase read-only agents); remaining domain functional-analyst depth (MSC/SSP/FIN); IAP final engineer; FinOps analyst | +32 | 122 |

---

## 10. Adoption Notes

- **Day-1 artifacts per team**: product charter (mission, KPIs, VS coverage from §4), current
  backlog seeded from the workflow gap analysis
  ([`workflow-gap-analysis.md`](../01-model-company/workflows/workflow-gap-analysis.md)),
  named BPO/SME roster, regression inventory mapped to Tier-1 workflows. For build squads
  additionally: architecture record, paved-road onboarding, SLOs and on-call runbook with a
  scheduled production-readiness review. For vendor dependencies additionally: vendor dossier
  (contract, SLA, release calendar, TPRM tier, exit clause).
- **Anti-patterns to avoid**: project-style exception lanes around the backlog; BPO delegated
  to a junior analyst (the BPO must be the process owner); customization approved outside the
  ARB; domain teams building private integrations outside IAP; per-team data marts outside DP
  (the DP rule now extends to built products); buying a capability product at all (the
  two-tier doctrine: in EBS → use it, otherwise build); building what EBS already does
  well; squads shipping
  off the SEP paved road; **unregistered agents, agents acting outside the IAP tool registry,
  or agent autonomy beyond the Tier-based ladder** (sourcing model §12.1).
- **Split/merge triggers** (reviewed at QBR): a team sustaining > 25% overflow demand for two
  consecutive quarters is a split candidate (first candidate if growth continues: SSP store
  execution vs store-adjacent services); a team below 60% utilization for two quarters is a
  merge candidate.

## 11. Related Documents

| Document | Relationship |
|---|---|
| [`model-company-profile.md`](../01-model-company/model-company-profile.md) | Departments (§3.3), org chart (§11.1), performance targets (§12.3/§15.3), ERP landscape (§14) |
| [`workflows/value-stream-index.md`](../01-model-company/workflows/value-stream-index.md) | The 188-VS / 569-PA / 5,427-WF catalog this model assigns to products |
| [`workflows/workflow-criticality-classification.md`](../01-model-company/workflows/workflow-criticality-classification.md) | Tier 1/2/3 register driving regression coverage and SLAs |
| [`internal-controls-matrix.md`](../01-model-company/internal-controls-matrix.md) | 808-control register governed via the Tier & Control Board |
| [`headcount-reality-check.md`](../01-model-company/headcount-reality-check.md) | §3.2 IT staffing gap record this sizing resolves |
| [`erp-requirements.md`](../01-model-company/erp-requirements.md) | Capability requirements the products deliver |
| [`technical-guidelines.md`](technical-guidelines.md) | Infrastructure, integration, and security reference underpinning the platform teams; §5 multi-vendor sourcing-architecture reference; §6 agentic-runtime reference |
| [`capability-sourcing-and-engineering-model.md`](capability-sourcing-and-engineering-model.md) | The sourcing decision gate, Capability Sourcing Register, build-squad engineering standard, and SEP definition this v3.13 model is built on |
| [`data-volumes-and-integrations.md`](../01-model-company/data-volumes-and-integrations.md) | Transaction volumes and integration touchpoints owned by IAP/INFRA |

---

*Document Version: 3.13 | Date: 2026-09-14 | **Promotion — this model is the IT department's structure of record.** With the org's structure promotion (TO v2.3; profile v3.0 §3.3/§4/§11.1 re-based to HQ 511 / total 6,911) the 17-team product-centric model is the **actual** IT department structure, no longer a steady-state target: §1 scope declares it, §3.2's FS row and §5.2/§9.2 user-base references re-based 6,762 → 6,911 (the promoted headcount), §9.2's 'Current IT department 50' row relabeled **pre-promotion** (superseded by §9.1's 122), and §9.3's build-up ladder (50 → ~55 → ~90 → 122) is the hiring-execution record. No team, seat, or sizing change — 122 FTE / 17 teams; 66 domain + 56 platform/CIO; 171 + 17 = 188 / 4,935 + 492 = 5,427. Prior v3.12 (2026-09-14): **Two-tier shape optimization — the org follows the doctrine:** the configure-and-integrate teams carry one **Platform Product Manager** each (§5.1 blockquote, §5.4 role definition, §9.1 column retitled 'Vendor PM' → 'Platform PM'); WLI's second vendor seat — sized for the retired best-of-breed WMS/TMS vendor estate — **converts to a fifth functional analyst** carrying the in-suite Oracle WMS/MSCA + Shipping/OTE configuration surface (§9.1: WLI analysts 4 → 5, platform PM 2 → 1; team total 10, domain 66 unchanged), and WLI's remaining seat is chartered as the **chain-wide Oracle Relationship & In-Suite Currency Manager** (one account-team interface, one RUP/CPU calendar, in-suite currency KPI owner — with module-level release/roadmap intake staying with every PO); **commercial ownership of the vendor-commodity line consolidates in the CIO Office vendor-portfolio analyst** (§5.3; sourcing model v3.1 §8), teams keeping operational SLA ownership (§8.2); WLI's §8.3 KPI row gains the in-suite currency KPI. **Seats, teams, sizing and the reconciliation unchanged** (122 FTE / 17 teams; 66 domain + 56 platform/CIO; 171 + 17 = 188 / 4,935 + 492 = 5,427). Prior v3.11 (2026-09-14): **Two-tier sourcing doctrine alignment (sourcing model v3.0):** the archetype 'Buy-and-integrate' is renamed **'Configure-and-integrate'** (§2 principle 4, §5.1); product/vendor management remit re-pointed (§5.1/§5.3/§5.4) from BoB products to the Oracle relationship, in-suite currency (RUP/CPU), the already-built POS/ecommerce/loyalty platforms and the commodity vendor line — **seats, teams, sizing and the reconciliation unchanged** (122 FTE / 17 teams; 171 + 17 = 188 / 4,935 + 492 = 5,427); §8.1/§8.2 release cadences re-worded (no BoB release train exists under the doctrine; vendor commodities intake-checked; already-built platforms release on the build cadence); §8.4 exit-reserve wording re-pointed; §9.2 need-band label + prose re-pointed to the two-tier band; §9.3 Phase 2 re-scoped (in-suite Oracle WMS/MSCA + Shipping/OTE adoption; Payroll PH + store-workforce builds; dispatch build); §10 anti-patterns updated (buying a capability product at all is the anti-pattern; building what EBS already does well). Catalog triple in §1/§11 trued **5,388 → 5,427** — a live-straggler derived quote the reconciliation waves never covered (§1/§11 sit outside om_reconciliation_hits' §3.2/§4.9 scope and outside the guide-scoped catalog-triple rule); the sixteenth-wave derived-quote class. Prior v3.10 (2026-09-10): Batch-24 gap-fill reconciliation: W5574 Concessionaire Connectivity Request, Approval & Independent-Circuit Governance (PA-07.1, VS-07 — workflow-gap-analysis.md batch 24; confirmed directly Tier 2) adds one workflow to SSP's mapped estate, so SSP's workflow load is trued 906 → 907 (§3.2 and §4.9), the domain subtotal re-foots 4,934 → 4,935, making the reconciliation read **171 + 17 = 188 / 4,935 + 492 = 5,427**. No team, sizing, phase, or VS-assignment changes — the workflow is absorbed within the sized SSP (store-operations governance) team, matching its absorbed staffing statement. Prior v3.9 (2026-09-07) | Tenth-wave consistency-review repair (the sixth-wave adjudication-pending residual, now adjudicated and closed): the sixth wave had flagged that §4.9's SSP row enumerates VS-151 while its workflow figure (882) only reconciles excluding it, and DP's 213 only including it (DP's own seven listed VSs hold 189 on disk) — a mismatch now traced to the document's issuance itself (the v1.0 §3.2 carried SSP 873 / DP 210 with the same asymmetry, and twenty reconciliation passes each trued the deltas correctly without ever re-deriving the base). Adjudication: the mapping side is unanimous — §4.3 lists VS-151 (Auto-ID, Barcode, RFID, Price-Tag Labeling & EAS Operations) under SSP with business owner 'Store Operations with Loss Prevention', §4.9's SSP row names '+1 (VS-151)' explicitly, VS-151 sits in the Sell & Serve family while DP's seven VSs are all drawn from the Technology & Data / Governance families — so the workflow figures are the wrong side: SSP trued 882 → 906 (VS-151's 24 workflows return to the team its mapping assigns), DP trued 213 → 189. The same re-derivation exposed a second, independent latent drift: the hand-maintained subtotal split itself sat ±3 off its own member rows (4,913 + 513 against member sums 4,910 + 516 pre-repair) — the split series had been carried by deltas since before v3.8 and never cross-footed to the rows — so the subtotals are re-based to the member sums **4,913 + 513 → 4,934 + 492** (total unchanged 5,426), making the reconciliation read **171 + 17 = 188 / 4,934 + 492 = 5,426**. No team, sizing, phase, or VS-assignment changes — VS-151 was always mapped to SSP; only its workload count followed. Guard extension: om_reconciliation_hits now re-derives every §3.2 per-team workflow cell and both subtotal cells, and every §4.9 per-team workflow cell, from the §4.1–4.8 mapping tables and the on-disk `##` headers each run — the whole portfolio series, not just its cross-foots. Prior v3.8 (2026-09-05): Sixth-wave consistency-review repair (post-batch-23): the batch-16→23 re-point cascades trued §4.9's per-team rows and this footer each pass but never §3.2, the batch-23 pass missed the §4.9 Total row, and the v3.7 clause's split arithmetic put INFRA's batch-23 +2 on the domain side against the chain's own v3.4 convention (INFRA = platform side) — all repaired in one pass: §3.2's per-team rows trued to the §4.9 values (MSC 485 → 486, WLI 523 → 526, SSP 877 → 882, CCP 740 → 742, FIN 808 → 809, CORP 920 → 924, PEO 443 → 445, INFRA 123 → 126) with the subtotals re-based **4,896 + 510 → 4,913 + 513** and the total **5,406 → 5,426**; §4.9's WLI row trued 525 → 526 (VS-87's 25th workflow predates the row's last true-up — the batch-16 stale-row repair reached the index/README but not the OM) and the §4.9 Total row re-pointed **4,911 + 511 = 5,422 → 4,913 + 513 = 5,426**, making the reconciliation read **171 + 17 = 188 / 4,913 + 513 = 5,426**; the v3.7 clause's '4,915 + 511' stands below as written and is corrected by this clause. Canonical totals unchanged 188 VS / 569 PA / 5,426 WF / 5,449 register rows / 808 CTL. Prior v3.7 (2026-09-05): Gas-leak, tsunami/storm-surge, media-exposé & server-room-environmental gap-fill reconciliation (batch 23): four workflow-level owners added — W5570 Gas-Leak Event Response (LPG/Natural-Gas Odor on Premises) in PA-24.2, W5571 Tsunami & Storm-Surge Coastal-Intrusion Response Protocol (PHIVOLCS Advisory / PAGASA Storm-Surge Warning) in PA-26.1, W5572 Undercover-Investigation & Media-Exposé Response Protocol (Investigative-Newsroom Event) in PA-14.3, and W5573 Server-Room & Data-Center Environmental Event Response (Cooling Failure, Water Intrusion, Fire-Suppression Discharge) in PA-27.2 (workflow-gap-analysis.md batch 23; the same analysis produced the custody register's tenth wave, events E-46–E-49) — so CORP's workflow load is trued 923 → 924 (VS-24), CCP's 741 → 742 (VS-14) and INFRA's 124 → 126 (VS-26 coastal-intrusion + VS-27 server-room environmental), making the reconciliation read **171 + 17 = 188 / 4,915 + 511 = 5,426**. No team, sizing, or phase changes — the four are absorbed within the sized CORP (HSE/safety posts), CCP (brand/PR bench) and INFRA (DR/facilities desk and IT infrastructure bench) teams, matching the absorbed staffing statements in each workflow. Prior v3.6 (2026-09-05): Terminal-tampering, procurement-impersonation, account-takeover & commute-disruption gap-fill reconciliation (batch 22): four workflow-level owners added outside the IT estate — W5566 Payment-Terminal Tampering & Card-Skimmer Response (PIN-Pad Compromise Event) in PA-08.2, W5567 Procurement-Impersonation & Fake-PO Goods-Diversion Response in PA-03.2, W5568 Official-Channel Account-Takeover Response (Brand-Account Hijack) in PA-14.2, and W5569 Mass-Commute Disruption & Transport-Strike Continuity Protocol in PA-141.2 (workflow-gap-analysis.md batch 22; the same analysis produced the custody register's ninth wave, events E-42–E-45) — so SSP's workflow load is trued 881 → 882 (VS-08), MSC's 485 → 486 (VS-03), CCP's 740 → 741 (VS-14) and PEO's 444 → 445 (VS-141), making the reconciliation read **171 + 17 = 188 / 4,911 + 511 = 5,422**. No team, sizing, or phase changes — the four are absorbed within the sized SSP (store front-end and payment-operations desks), MSC (procurement team), CCP (social/digital-marketing bench) and PEO (transport-program seat) teams, matching the absorbed staffing statements in each workflow. Prior v3.5 (2026-09-05): Storefront-crash, brand-impersonation-scam, wallet-outage & adjacent-works gap-fill reconciliation (batch 21): four workflow-level owners added outside the IT estate — W5562 Vehicle-Impact & Storefront-Crash Response Protocol in PA-147.2, W5563 Brand-Impersonation Commerce-Scam Response (Fake Sellers & Fraudulent Pickup Offers) in PA-100.2, W5564 Mobile-Wallet Platform Outage Response (E-Wallet Tender Downtime) in PA-08.1, and W5565 Third-Party Construction Damage & Adjacent-Works Response Protocol in PA-20.3 (workflow-gap-analysis.md batch 21; the same analysis produced the custody register's eighth wave, events E-38–E-41) — so SSP's workflow load is trued 879 → 881 (VS-08 + VS-147) and CORP's 921 → 923 (VS-20 + VS-100), making the reconciliation read **171 + 17 = 188 / 4,907 + 511 = 5,418**. No team, sizing, or phase changes — the four are absorbed within the sized SSP (store front-end and customer-safety benches) and CORP (IP/legal bench, facilities team) teams, matching the absorbed staffing statements in each workflow. Prior v3.4 (2026-09-05): Cyber-extortion four workflow-level owners added — W5558 Ransomware & Destructive Cyber-Attack Enterprise Response Protocol in PA-27.3 (inside the IT estate), W5559 Vendor Payment-Diversion & Business Email Compromise (BEC) Fraud Event Response & Recovery Protocol in PA-18.2, W5560 Informal-Settler Invasion & Illegal Occupation of Banked Land — Detection, Relocation & Ejection Protocol in PA-178.1, and W5561 Sustained Water-Service Interruption Response & Store Continuity Protocol in PA-07.2 (workflow-gap-analysis.md batch 20; the same analysis produced the custody register's seventh wave, events E-34–E-37) — so INFRA's workflow load is trued 123 → 124 (VS-27, the first in-estate gap-fill workflow since the batch-8 IT pass), SSP's 878 → 879 (VS-07), FIN's 808 → 809 (VS-18) and CORP's 920 → 921 (VS-178), making the reconciliation read **171 + 17 = 188 / 4,903 + 511 = 5,414**. No team, sizing, or phase changes — the four are absorbed within the sized INFRA (IT security bench + IR retainer), SSP (store facility/safety posts), FIN (treasury desk) and CORP (landbanking team) teams, matching the absorbed staffing statements in each workflow. Prior v3.3 (2026-09-05): In-transit-security, fatality-scene, tampering-extortion & recruitment-fraud gap-fill reconciliation: four workflow-level owners added outside the IT estate — W5554 In-Transit Cargo Hijacking, Armed Truck Robbery & Driver-Safety First Response Protocol in PA-06.2, W5555 Customer or Visitor Death on Premises — Scene Protocol, Family Liaison & Trading-Continuity Decision in PA-147.3, W5556 Product-Tampering Threat, Extortion Demand & Merchandise-Integrity Sweep Protocol in PA-89.1, and W5557 Recruitment Fraud & Fake Job-Offer Scam Response, Takedown & Victim-Guidance Protocol in PA-121.1 (workflow-gap-analysis.md batch 19; the same analysis produced the custody register's sixth wave, events E-30–E-33) — so WLI's workflow load is trued 523 → 525 (VS-06 + VS-89), SSP's 877 → 878 (VS-147) and PEO's 443 → 444 (VS-121), making the reconciliation read **171 + 17 = 188 / 4,900 + 510 = 5,410**. No team, sizing, or phase changes — the four are absorbed within the sized WLI (fleet safety posts), SSP (store-ops/customer-safety bench) and PEO (TA marketing bench) teams, matching the absorbed staffing statements in each workflow. Prior v3.2 (2026-09-05): Channel-enforcement, employee-legal-status, OSH-enforcement & app-store-removal gap-fill reconciliation: four workflow-level owners added outside the IT estate — W5550 Marketplace Account Suspension, Enforcement Freeze & Appeal Recovery Protocol in PA-10.3, W5551 Employee Arrest, Detention & Criminal-Case Employment-Status Response Protocol in PA-19.1, W5552 DOLE Imminent-Danger Work-Stoppage Order Response, Abatement & Reinstatement Gate in PA-24.1, and W5553 Mobile App Store Removal, Policy-Violation Response & Re-Listing Recovery Protocol in PA-75.1 (workflow-gap-analysis.md batch 18; the same analysis produced the custody register's fifth wave, events E-27–E-29) — so CCP's workflow load is trued 738 → 740 (VS-10 + VS-75), CORP's 919 → 920 (VS-24) and PEO's 442 → 443 (VS-19), making the reconciliation read **171 + 17 = 188 / 4,896 + 510 = 5,406**. No team, sizing, or phase changes — the four are absorbed within the sized CCP, CORP and PEO teams, matching the absorbed staffing statements in each workflow. Prior v3.1 (2026-09-05): Regulatory-shock, platform-outage & governance-continuity gap-fill reconciliation: six workflow-level owners added outside the IT estate — W5544 Emergency Executive Succession & Decision-Rights Continuity Protocol in PA-36.1, W5545 BIR Tax-Enforcement Suspension & Closure-Order Response (Oplan Kandado) and W5546 BIR eFPS & Government-Portal Outage Filing Contingency in PA-79.3, W5547 Payment-Network & Acquirer Outage Response in PA-08.1, W5548 Stored-Value & Loyalty Platform Outage Protocol in PA-54.2, and W5549 Suicide/Self-Harm Incident Response & Psychosocial-Aftermath Protocol in PA-24.1 (workflow-gap-analysis.md batch 17; the same analysis produced the custody register's fourth wave, events E-23–E-26) — so SSP's workflow load is trued 876 → 877 (VS-08), FIN's 805 → 808 (VS-79 ×2 + VS-54), and CORP's 917 → 919 (VS-24 + VS-36), making the reconciliation read **171 + 17 = 188 / 4,892 + 510 = 5,402**. No team, sizing, or phase changes — the six are absorbed within the sized SSP, FIN and CORP teams, matching the absorbed staffing statements in each workflow. Prior v3.0 (2026-09-05): Emergency & continuity gap-fill reconciliation: eight workflow-level owners added outside the IT estate — W5536 Missing-Child / Code Adam In-Store Response Protocol and W5539 Elevator & Escalator Entrapment Response Protocol in PA-07.2, W5537 Fire Event Response & Post-Fire BFP Clearance and W5538 Bomb Threat Response in PA-24.2, W5540 Payroll Run Failure, Correction & Emergency Off-Cycle Payment in PA-19.2, W5541 Bank-Failure & Frozen-Deposit Contingency in PA-18.3, W5542 Liquidity Stress, Covenant-Breach & Payment-Prioritization Escalation in PA-105.3, and W5543 Price-File Integrity Event Response & Mass-Mispricing Rollback in PA-118.2 ([workflow-gap-analysis.md](../01-model-company/workflows/workflow-gap-analysis.md) batch 16; the same analysis produced the custody register's third wave, events E-19–E-22) — so SSP's workflow load is trued 874 → 876 (VS-07), FIN's 802 → 805 (VS-18/VS-105/VS-118), CORP's 915 → 917 (VS-24) and PEO's 441 → 442 (VS-19), making the reconciliation read **171 + 17 = 188 / 4,886 + 510 = 5,396**; the same pass trued the §4.9 CIO Office straggler (80 — a v2.9 edit miss — → 81, matching §3.2). No team, sizing, or phase changes — the eight are absorbed within the sized SSP (store facility/safety posts), FIN (treasury desk, revenue-assurance desk), CORP (HSE posts) and PEO (payroll team) teams, matching the absorbed staffing statements in each workflow. Prior v2.9 (2026-09-04): VS-113 gains one workflow-level owner for the stakeholder capability-demand front door — W5535 Capability Demand Intake & Backlog Triage in PA-113.2 (raise → log & triage → route to team backlog / workflow-catalog gap-admission / the W5515 sourcing gate → Product-Council capacity funding; workflow-gap-analysis.md batch 15) — so the CIO Office's workflow load is trued 80 → 81 and the reconciliation reads **171 + 17 = 188 / 4,878 + 510 = 5,388**. No team, sizing, or phase changes — the workflow is absorbed within the sized CIO Office (Head of EA + vendor-portfolio analyst), matching its staffing statement. Prior v2.8 (2026-09-04): Operations-workflow gap-fill reconciliation: three workflow-level owners added outside the IT estate — W5532 Workforce Time & Attendance (Biometric/Time-Clock) Platform Estate & Punch-Data Operations in PA-19.3, W5533 BIR Form 2316 Annual Issuance, Employee Acknowledgment & Certificate Lifecycle in PA-79.2, and W5534 Company-Property Gate Pass & Asset-Exit Control (Stores, DCs & HQ) in PA-23.2 ([workflow-gap-analysis-operations.md](../01-model-company/workflows/workflow-gap-analysis-operations.md)) — so PEO's workflow load is trued 440 → 441, FIN's 801 → 802 and SSP's (hosting VS-23, the Governance & Assurance loss-prevention stream) 873 → 874, making the reconciliation read **171 + 17 = 188 / 4,878 + 509 = 5,387**; the same pass trued the §4.9 FIN straggler (799 — a batch-10 leftover — → 802, matching §3.2). No team, sizing, or phase changes — the three are absorbed within the sized PEO (HR technology seat, W3351 class), FIN (tax sub-team, W2764/W2765 class) and SSP (loss-prevention posts, W1477/W1478 class) teams, matching the absorbed staffing statements in each workflow. Prior v2.7 (2026-09-03): Finance-workflow gap-fill reconciliation: three workflow-level owners added outside the IT estate — W5529 Utility, Telecommunications & Site Deposits Paid — Register, Interest Reconciliation, Surety Replacement & Recovery-on-Closure in PA-42.3, W5530 Minimum Corporate Income Tax (MCIT) Computation, Regime Evaluation & 3-Year Excess-Credit Carry-Forward in PA-17.3, and W5531 PFRS 8 Operating-Segment Reporting, CODM Disclosure Package & Segment-Note Production in PA-17.4 ([workflow-gap-analysis-finance.md](../01-model-company/workflows/workflow-gap-analysis-finance.md)) — so FIN's workflow load is trued 799 → 801 (and Asset & Infrastructure, the other non-IT family touched, rises 320 → 321), making the reconciliation read **171 + 17 = 188 / 4,875 + 509 = 5,384**. No team, sizing, or phase changes — the three are absorbed within the sized FIN stream-aligned team (treasury desk, tax sub-team, corporate accounting/consolidation), matching the absorbed staffing statements in each workflow. Prior v2.6 (2026-09-03): People-capability & reporting-policy gap-fill reconciliation: four workflow-level owners added outside the IT estate — W5525 Learning Platform (LMS) Administration, Integration & Learning-Records Operations, W5526 Learning-Content Development, Course-Catalog & Certification-Program Lifecycle and W5527 Leadership Development & Management-Capability Program (HiPo Development) in PA-19.4, and W5528 Accounting Policy, Technical Accounting (PFRS) Position & New-Standard Adoption Governance in PA-17.4 ([workflow-gap-analysis-people.md](../01-model-company/workflows/workflow-gap-analysis-people.md)) — so PEO's workflow load is trued 437 → 440 and FIN's 798 → 799, and the reconciliation reads **171 + 17 = 188 / 4,872 + 509 = 5,381**. No team, sizing, or phase changes — the four are absorbed within the sized PEO (HR technology + L&D seats) and FIN (corporate accounting) stream-aligned teams, matching the absorbed staffing statements in each workflow. Prior v2.5 (2026-09-03): IT gap-fill reconciliation: VS-27 gains seven workflow-level owners for the IT operating-model surfaces ([workflow-gap-analysis-it.md](../01-model-company/workflows/workflow-gap-analysis-it.md) — W5518 collaboration/productivity tenant ops, W5519 store telephony/UCC lifecycle, W5520 core network services & IPAM in PA-27.2; W5521 release calendar & peak-season change freeze in PA-27.1; W5522 ISMS/security certification, W5523 enterprise pentest/red-team, W5524 DLP & insider-risk in PA-27.3), so INFRA's workflow load is trued 116 → 123 and the reconciliation reads **171 + 17 = 188 / 4,868 + 509 = 5,377**. No team, sizing, or phase changes — the seven are absorbed within the sized INFRA stream-aligned + SEC/FS platform teams (end-user services, network engineering, security analysis, IT compliance), matching the absorbed staffing statements in each workflow. Prior v2.4 (2026-09-03): Sourcing-model gap-fill reconciliation: VS-113 gains three workflow-level owners for the hybrid sourcing machinery (W5515 Sourcing Decision Gate Operation & Capability Sourcing Register in PA-113.3, W5516 Best-of-Breed Product Lifecycle Management, Vendor Release Intake & Exit Reserves in PA-113.2, W5517 SEP Paved Road & Engineering Standard Governance for Built Products in PA-113.1; sourcing model §3–§9), so the CIO Office's workflow load is trued 77 → 80 and the reconciliation reads **171 + 17 = 188 / 4,868 + 502 = 5,370**. No team, sizing, or phase changes — the three are absorbed within the sized CIO Office and buy-archetype Vendor PM seats, and the SEP engineering standard remains enforced by the paved road. Prior v2.3 (2026-09-03): Agentic gap-fill reconciliation: VS-128 gains three workflow-level agentic-platform lifecycle owners (W5512–W5514 in PA-128.3 — intake/sourcing/registration, shadow & canary evaluation with autonomy-tier ratification, runtime/guardrail/kill-switch telemetry with quarterly re-registration & sunset; sourcing model §12), so DP's workflow load is trued 210 → 213 and the reconciliation reads **171 + 17 = 188 / 4,868 + 499 = 5,367**. No team, sizing, or phase changes — the three are absorbed within the sized AAP enablement + DP portfolio. Prior v2.2 (2026-09-03): §9.3 Phase-0 row clarified (no figure changes): it stands up the first **16 of the 17** teams — the AAP platform team follows in Phase 2, matching the sizing ladder 50 → ~55 → ~90 → 122. Prior v2.1 (2026-09-03): **Agentic-AI extension.** The AI & Agent Platform
(AAP) joins as platform team #15/17 — the paved road for governed AI agents that automate
manual tasks: tool registry (IAP contracts only), guardrails and human-in-the-loop gates,
evaluation harness (offline → shadow → canary), non-human identity, kill-switch, cost
telemetry. Design principle 8 added ("agents are products"); the autonomy ladder is wired to
the workflow Tier register (Tier-1 human-approval-gated / Tier-2 bounded / Tier-3
autonomous-in-bounds) with hard boundaries — no agent owns a statutory filing, touches the
POS/OT estate, or holds SoD-conflicting duties; agents are registered under VS-128 and
routed through the SIB like any sourcing decision; agents are delivered by their owning
product teams on the AAP runtime. Sizing re-based 115 → 122 FTE (platform/CIO 49 → 56 with
AAP +7); phased build-up now 50 → 122; AAP KPI row (§8.3); SIB gains the AAP seat and agent
autonomy ratification (§7). Program definition: sourcing model §12; runtime rules:
technical-guidelines §6. Prior v2.0 (2026-09-03): hybrid capability-sourcing revision —
three-tier landscape (unified ERP core, BoB WMS/TMS/WFM/FSM edges, in-house OMO/TPS builds),
16 teams (reconciliation unchanged 171 + 17 = 188 VS / 4,865 + 499 = 5,364 workflows),
archetypes + Vendor PM + build squads, SIB governance, per-archetype release cadences,
sizing 80 → 115. Prior v1.1 (2026-09-02, review #68) and v1.0 (2026-09-01): unified-model
12-team design at 80 FTE. Downstream: `optimal-table-of-organization.md` v2.4 (HQ 511 /
total 6,911 — the actual structure of record), `model-company-profile.md` v3.0,
`technical-guidelines.md` v3.4,
`capability-sourcing-and-engineering-model.md` v3.2.*
