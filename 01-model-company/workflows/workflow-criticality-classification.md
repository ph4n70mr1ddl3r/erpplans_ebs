# Workflow Criticality Classification

> Classifies all 5,433 unique operational workflows into criticality tiers (the confirmed
> register holds 5,456 rows, of which 23 are `###` parent/summary sub-workflows double-counted
> against a `##` parent). Zero workflows remain unclassified: the 2026-06-28 Full-Coverage
> Confirmation Pass promoted every then-existing keyword-proposed workflow (unclassified
> 2,596 → 0), the fourteen post-catalog workflows W5497–W5510 (added 2026-08-24/26) were
> confirmed on 2026-09-02 by the post-catalog confirmation pass
> (`07-methodology/confirm-postcatalog-14.py`; 6 → Tier 1, 6 → Tier 2, 2 → Tier 3),
> W5511 (VS-54.3 gift-card dormancy/escheat) shipped directly confirmed Tier 2 in the
> 2026-09-03 event-custody pass, W5512–W5514 (the agentic-AI platform lifecycle gap fill
> in VS-128.3) shipped directly confirmed Tier 2 in the 2026-09-03 agentic gap-fill pass,
> W5515–W5517 (the capability-sourcing & engineering gap fill in VS-113) shipped
> directly confirmed Tier 2 in the 2026-09-03 sourcing-model gap-fill pass, and
> W5518–W5524 (the IT operating-model gap fill in VS-27) shipped directly confirmed
> Tier 2 (5) / Tier 3 (2) in the 2026-09-03 IT workflow gap-fill pass, W5525–W5528
> (the people-capability & reporting-policy gap fill in VS-19.4/VS-17.4) shipped directly
> confirmed Tier 2 (4) in the 2026-09-03 people-workflow gap-fill pass, and W5529–W5531
> (the finance-workflow gap fill in VS-42.3/VS-17.3/VS-17.4) shipped directly confirmed
> Tier 1 (2) / Tier 2 (1) in the 2026-09-03 finance-workflow gap-fill pass, and W5532–W5534
> (the operations-workflow gap fill in VS-19.3/VS-79.2/VS-23.2) shipped directly confirmed
> Tier 2 (2) / Tier 1 (1) in the 2026-09-04 operations-workflow gap-fill pass, and W5535
> (the capability demand-intake & backlog-triage gap fill in PA-113.2, VS-113) shipped
> directly confirmed Tier 2 in the 2026-09-04 demand-intake gap-fill pass, and W5536–W5543
> (the emergency & continuity workflow gap fill in VS-07.2/VS-24.2/VS-19.2/VS-18.3/VS-105.3/
> VS-118.2) shipped directly confirmed Tier 1 (3) / Tier 2 (5) in the 2026-09-05 emergency
> & continuity gap-fill pass, and W5544–W5549
> (the regulatory-shock, platform-outage & governance-continuity workflow gap fill in
> VS-36.1/VS-79.3/VS-08.1/VS-54.2/VS-24.1) shipped directly confirmed Tier 1 (2) / Tier 2 (4)
> in the 2026-09-05 batch-17 gap-fill pass, and W5550–W5553
> (the channel-enforcement, employee-legal-status, OSH-enforcement & app-store-removal gap
> fill in VS-10.3/VS-19.1/VS-24.1/VS-75.1) shipped directly confirmed Tier 1 (1) / Tier 2 (3)
> in the 2026-09-05 batch-18 gap-fill pass, and W5554–W5557 (the in-transit-security,
> fatality-scene, tampering-extortion & recruitment-fraud gap fill in VS-06.2/VS-147.3/
> VS-89.1/VS-121.1) shipped directly confirmed Tier 1 (2) / Tier 2 (2) in the 2026-09-05
> batch-19 gap-fill pass, and W5558–W5561 (the cyber-extortion, payment-diversion,
> land-occupation & water-continuity gap fill in VS-27.3/VS-18.2/VS-178.1/VS-07.2) shipped
> directly confirmed Tier 1 (1) / Tier 2 (3) in the 2026-09-05 batch-20 gap-fill pass, and
> W5562–W5565 (the storefront-crash, brand-impersonation-scam, wallet-outage &
> adjacent-works gap fill in VS-147.2/VS-100.2/VS-08.1/VS-20.3) shipped directly
> confirmed Tier 1 (1) / Tier 2 (3) in the 2026-09-05 batch-21 gap-fill pass, and W5566–W5569
> (the terminal-tampering, procurement-impersonation, account-takeover & commute-disruption gap
> fill in VS-08.2/VS-03.2/VS-14.2/VS-141.2) shipped directly confirmed Tier 2 (4) in the
> 2026-09-05 batch-22 gap-fill pass, and W5570–W5573 (the gas-leak, tsunami/storm-surge,
> media-exposé & server-room-environmental gap fill in VS-24.2/VS-26.1/VS-14.3/VS-27.2) shipped
> directly confirmed Tier 1 (2) / Tier 2 (2) in the 2026-09-05 batch-23 gap-fill pass.
> [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) is empty and is
> re-derived from the register on every run of
> `07-methodology/classify-workflows.py` whenever new workflows ship unclassified.
>
> **Layout note:** each tier's workflows are split into the original register (`## Tier N`) and a
> later `### Tier N Additions` batch added in subsequent review passes; the per-tier counts in the
> section headings and the [`## Summary`](#summary) table include both batches.
>
> Back to [Workflow Index](README.md)

---

### Operational Criticality Tiers

| Criticality Tier | Label | Description | Operational Dependency |
|---|---|---|---|
| **Tier 1** | Core Operations | Revenue-critical, core operations, legal compliance | Hard dependency (business cannot function without) |
| **Tier 2** | Standard Support | Standard support workflows, cost controls | Soft dependency (business experiences operational friction without) |
| **Tier 3** | Advanced Optimization | Advanced analytics, optimization, automation | Enhancement only (improves efficiency) |

### Classification Rules

1. **Must Have requirements** (429) are overwhelmingly Tier 1, with exceptions for requirements that only apply at scale (e.g., across all 200 stores rather than pilot 5)
2. **Should Have requirements** (293) are split between Tier 1 (operational necessities) and Tier 2
3. **Nice to Have requirements** (6) are Tier 3
4. Domain-specific workflows (governance, audit, ESG, innovation) are classified by their operational impact
5. Master data governance workflows are classified by dependency — foundational masters (item, customer, vendor, location) are Tier 1; advanced masters (planogram, loyalty config, digital assets) are Tier 2
6. Store-level daily operational workflows (safety checks, compliance, cash management, closings) are Tier 1
7. Customer-facing estimation/advisory services (material calculators, design consultations) are Tier 2 or Tier 3 based on revenue criticality

---

## Tier 1: Core Operations (1,396 Workflows)

These 1,396 workflows are foundational to daily store and supply chain operations.
Failure in any of these workflows would disrupt store operations or legal compliance.

### Core Finance (30 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W7 | Accounts Payable — Vendor Invoice Processing | 6,715+ invoices/month; 3-way match is a must-have |
| W7C | Non-PO / Recurring Expense Invoice Processing | Recurring vendor payments must continue |
| W7D | AP Vendor Statement Reconciliation | Month-end AP integrity |
| W8 | Accounts Receivable — Trade & Corporate Accounts | 5,200 AR accounts; B2B revenue collection |
| W9 | Financial Close & Reporting | Under CREATE Law / PFRS requirements |
| W9A | Month-End Close | 5-day close SLA |
| W9B | Year-End Close | Statutory auditing dependency |
| W21 | Capital Expenditure (Capex) Request & Approval | Capital budgeting & controls |
| W24 | Trade & Corporate Credit Application | Credit risk mitigation |
| W25 | Petty Cash Management | Controls cash across 205 locations |
| W26 | Annual Budget Preparation & Monthly Variance Review | Cost controls |
| W30 | Daily Treasury & Cash Position Management | Sweep cash; ensure liquidity |
| W59 | Insurance Policy Lifecycle Management | Risk mitigation |
| W74 | Employee Expense Reimbursement | Expense processing |
| W76 | Employee Loans & Advances | Loan management |
| W89 | Bank Reconciliation | Daily/weekly bank matching |
| W90 | Monthly Tax Filing & Statutory Remittance | BIR compliance |
| W94 | Customer Deposit & Advance Payment Management | Deposit tracking |
| W99 | Payment Settlement Reconciliation (Card / E-Wallet / Online) | Payment integrity |
| W100 | Vendor Statement Reconciliation | Vendor relationship |
| W101 | Customer Refund & Credit Processing | BIR-compliant credit notes |
| W108 | Customer Credit Collection & Escalation | Collection for 5,200 accounts |
| W260 | BIR eFPS Filing & Electronic Payment Submission | Mandatory BIR filing |
| W261 | E-Wallet & Digital Payment Settlement Reconciliation | GCash/Maya reconciliation |
| W423 | AR Post-dated Check (PDC) Warehousing & Clearing — Treasury Execution (canonical lifecycle: W1380) | Critical for B2B revenue collection in PH |
| W424 | AP Post-dated Check (PDC) Issuance & Monitoring | Critical for lease/rent payments to PH malls |
| W425 | Bounced Check (DAIF/DAUD) Recovery & Penalty — Treasury Reversal (canonical resolution: W1381) | Financial/legal risk management in PH |
| W473 | BIR Electronic Invoicing System (EIS) API Transmission & Reconciliation | Mandatory real-time e-invoicing transmission to BIR for large taxpayers |
| W475 | Customer Creditable Withholding Tax (CWT) Certificate (BIR 2307) Collection & Reconciliation | B2B cash clearing and BIR corporate income tax credit reconciliation |
| W478 | BIR Annual Inventory List Submission (RMC 57-2015) | Mandatory annual inventory list reporting to BIR |

### Core Inventory (14 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W4 | Store Replenishment (DC → Store) | ~50,000 replenishment orders/month (production-calibrated) |
| W4B | Store-Initiated Replenishment Request | Store-level demand signal |
| W6 | Cycle Counting & Inventory Accuracy | Weekly counts; ≥97% accuracy target |
| W22 | Stock Transfers (Store-to-Store & Inter-DC) | Multi-location transfers |
| W22A | Store-Level Outbound Transfer Fulfillment | Transfer execution |
| W22B | Store-to-DC Return (Excess / Damaged Inventory) | Reverse logistics |
| W42 | Annual Physical Inventory Execution | Annual wall-to-wall count |
| W56 | Customer Backorder Management | Customer order fulfillment |
| W91 | Damaged & Defective Goods Disposition | Inventory quality |
| W92 | Inventory Adjustment & Shrinkage Authorization | Shrinkage control |
| W105 | Multi-Channel Inventory Allocation & Priority Governance | Channel reservation rules |
| W204 | Regional Stock Rebalancing & Inter-Store Expedited Transfers | Regional optimization |
| W214 | Store-to-Store Expedited Transfers (Customer-Initiated) | Customer service |
| W219 | Store Inventory Quarantine & Recertification | Quality control |

### Core Procurement (13 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W2 | Procurement — Purchase Order Cycle | Parent workflow |
| W2A | Auto-Replenishment (Stocking Items) | 1,200+ POs/month auto-generated |
| W2B | Import Purchase Orders | 40% of COGS; LC, customs, landed cost |
| W2C | Blanket Purchase Orders | Annual supply agreements |
| W36 | Vendor Onboarding | 800–1,000 active vendors |
| W38 | Special Order / Non-Stock Item Fulfillment | Customer special orders |
| W44 | Vendor Performance Review | Vendor management |
| W60 | Emergency Procurement | Urgent purchasing |
| W62 | Vendor Contract Lifecycle (Non-PO Contracts) | Contract management |
| W88 | Return to Vendor (RTV) Processing | Defective/wrong item returns |
| W136 | Indirect / Non-Merchandise Procurement | Non-merch POs |
| W244 | Vendor Invoice Dispute & Discrepancy Resolution | AP dispute resolution |
| W328 | Customer Credit Limit Periodic Review | Annual credit risk reassessment |

### Core Warehouse (7 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W3 | Warehouse Receiving & Putaway | DC core operation |
| W3B | Yard & Outdoor Inventory Management | Lumber/building materials |
| W3C | DC Inbound Delivery Scheduling | Inbound coordination |
| W46 | Kit / Bundle Assembly & Disassembly | Kit operations |
| W106 | DC Outbound Dispatch & Load Planning | Outbound coordination |
| W188 | Fleet Spare Parts & Preventive Maintenance (PM) Management | Fleet readiness |
| W270 | Pallet & Returnable Transport Packaging (RTP) Tracking | Pallet management |

### Core POS & Store Operations (23 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W5 | Daily Store Operations | Parent workflow |
| W5A | Store Opening | Daily opening procedure |
| W5B | In-Store Selling | 2.8M transactions/month |
| W5D | In-Store Customer Delivery Scheduling | Bulky item delivery |
| W5E | Store Opening Delay Procedure | System-down protocol |
| W5F | Store Closing & End-of-Day | Cash reconciliation for 200 stores |
| W5G | Offline POS Recovery & Reconciliation | Must sell during outages |
| W12 | Returns & Exchanges | Parent workflow |
| W12A | In-Store Returns | Customer-facing returns |
| W12B | Online-Initiated Returns | Omnichannel returns |
| W12C | Cross-Store Returns (Purchased at Store A, Returned at Store B) | Cross-store return processing |
| W18 | Direct Store Delivery (DSD) Receiving | 30% of goods by value |
| W18B | DSD Vendor Delivery Scheduling | DSD coordination |
| W33 | Warranty Claim Processing | Customer warranty |
| W109 | Store-Level Inventory Receiving & Putaway | Store receiving |
| W330 | In-Store Emergency Response Protocol | Safety compliance (RA 11058) |
| W432 | Solo Parent Discount Compliance (RA 11861) | PH Legal requirement for checkout |
| W438 | Yard Dispatch & Customer Vehicle Loading Operations | Critical for bulky material pickup |
| W537 | POS Card Terminal & Acquirer Settlement Operations | Card settlement — 36% of POS transactions; financial integrity |
| W538 | POS Real-Time Loss Prevention Exception Monitoring & Alert Response | Real-time LP monitoring; fraud/theft prevention |
| W540 | POS BIR Invoice Reprint, Adjustment & Credit Note Issuance | BIR-compliant credit note issuance; statutory requirement |
| W541 | POS Cash Office Operations & Bank Deposit Preparation | Cash office close; bank deposit accuracy for 200 stores |
| W553 | POS Pricing Error Detection & Immediate Correction at Checkout | DTI compliance; price accuracy enforcement at checkout |

### Core Merchandising & Pricing (2 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W13 | Promotions & Pricing Execution | Must Have POS-014 (promo auto-apply), ECOM-002 (price sync); without it POS cannot auto-apply promotions |
| W40 | Regular Price Change Execution | Must Have POS-010 (quantity breaks), ECOM-002 (price sync); stores cannot adjust prices post-go-live |

### Core Ecommerce (7 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W11 | Ecommerce — BOPIS Order Fulfillment | ~42,900 orders/month |
| W19 | Ecommerce — Home Delivery Fulfillment | ~17,200 orders/month |
| W19B | Ship from Store (Store-Fulfilled Home Delivery) | Omnichannel fulfillment |
| W98 | Ecommerce Order Exception & Cancellation Management | Order exceptions |
| W215 | Customer Home Delivery Reverse Logistics (Returns) | Delivery returns |
| W246 | Drop-Ship Vendor (DSV) Order Fulfillment | Drop-ship orders |
| W247 | BOPIS Smart Locker & Queue Management | Smart locker pickup |

### Core HR & Payroll (6 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W10 | Payroll Processing | 6,918 employees; 5 entities × 2 runs/month |
| W15 | Recruitment & Employee Onboarding | ~1,200–1,600 hires/year |
| W34 | Store Shift Scheduling | Store workforce management |
| W43 | Employee Separation & Offboarding | Offboarding compliance |
| W251 | Philippine Statutory Benefits & Claims Administration (SSS, PhilHealth, Pag-IBIG) | SSS, PhilHealth, Pag-IBIG |
| W280 | Court-Ordered Wage Garnishment & Third-Party Deductions | Legal compliance |

### Core Supply Chain (5 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W31 | Demand Forecasting Cycle | Drives replenishment |
| W32 | Seasonal Buy Planning | Seasonal procurement |
| W133 | Sales & Operations Planning (S&OP) Cycle | Sales & operations planning |
| W144 | International Logistics & Import Operations | Import operations |
| W250 | Supply Chain Control Tower & Real-Time Shipment Visibility | Shipment visibility |

### Core Compliance & IT (29 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W37 | Loss Prevention & Exception Reporting | POS fraud detection |
| W48 | IT Operations & Helpdesk Support | IT support |
| W53 | Data Privacy Breach Response | RA 10173 compliance |
| W54 | LGU Business Permit Renewal per Location | 200+ local permits |
| W55 | IT Disaster Recovery & System Failover | Failover preparedness |
| W131 | IT Asset Lifecycle Management | Asset tracking |
| W132 | Software Development & Change Management | ERP change management |
| W152 | Employee IT Provisioning & Access Lifecycle Management | Identity & access management |
| W158 | Business Continuity Drill & Disaster Recovery Testing | DR drills |
| W257 | Enterprise API & Systems Integration Lifecycle Management | Integrations management |
| W265 | POS Terminal Hardware Maintenance & Peripheral Management | POS terminal uptime |
| W266 | Ecommerce Online Fraud Detection & Prevention | Fraud block |
| W267 | Ecommerce Digital Payment Reconciliation & Dispute Handling | payment integrity |
| W271 | Data Subject Access & Deletion Requests (DPA Compliance) | RA 10173 DSAR |
| W366 | Network Infrastructure & Connectivity Management | Connectivity for 200+ sites |
| W368 | Database & Cloud Infrastructure Management | ERP performance & integrity |
| W375 | Privileged Access Management (PAM) Operations | Admin access security |
| W377 | Domain, SSL & Digital Certificate Management | Web & API uptime |
| W380 | IT Alert & Event Management | Proactive ops monitoring |
| W460 | Corporate & Trade Account Onboarding | B2B onboarding is revenue-critical for trade/corporate segment |
| W461 | Intercompany Fulfillment & Logistics Fee Settlement | IC settlement between 5 entities |
| W463 | Catch-Weight & Cut-to-Length Processing | Must Have POS-016; critical for hardware retail (lumber, wire, bulk) |
| W464 | In-House Customs Brokerage & Port Operations | Import operations (40% of COGS) |
| W467 | Specialized Hardware Permits (DENR, FPA) | Mandatory regulatory compliance for chemical/fertilizer products |
| W476 | LGU / BFP Fire Safety Inspection Certificate (FSIC) Management | Mandatory for business permit renewal and fire safety compliance |
| W477 | DENR Permit to Operate (PTO) & Wastewater Discharge Permit (WDP) Compliance | Mandatory for standby generator sets and wastewater discharge compliance |
| W479 | FDA License to Operate (LTO) for Household Hazardous Substances Compliance | Mandatory for selling paint, chemical-based goods, and solvents in PH |
| W480 | CAAP Height Clearance Permit Compliance | Mandatory CAAP clearances for store structures/signage near aerodromes |
| W54A | BIR Computerized Accounting System (CAS) Registration | Mandatory BIR CAS permit per entity/location; legal prerequisite for POS invoice/receipt numbering and books-of-accounts generation |

### Core Master Data Governance (16 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W252 | Centralized Item Master Creation & Governance | 55K SKUs; single source of truth |
| W253 | Customer Master Data Governance & Deduplication | 600K+ customer records |
| W254 | Location Master Lifecycle & Hierarchy Management | 200 stores + 4 DCs + HQ |
| W287 | Vendor Master Data Governance & Deduplication | 800–1,000 vendors |
| W288 | Financial Master Data Governance (COA & Cost Centers) | GL and cost center governance |
| W289 | Pricing Master Governance (Base Prices & Matrices) | Pricing control |
| W291 | Master Data Quality Monitoring & Reporting | Data quality |
| W293 | Tax & Regulatory Master Data Governance | BIR tax codes |
| W294 | Unit of Measure (UOM) Master & Conversion Management | Critical for catch-weight |
| W308 | Fiscal Calendar & Posting Period Master Governance | Period control |
| W309 | Bank & Banking Partner Master Governance | Bank master records |
| W311 | Barcode, GTIN & Item Identification Master Governance | Must Have POS-003, ECOM-009, MDM-020; barcode assignment at SKU creation is go-live critical |
| W312 | Replenishment & Planning Parameter Master Governance | Must Have MDM-021; direct dependency for Phase 1 W2A (auto-replenishment) and W4 (store replenishment) |
| W399 | Fixed Asset Master Data Governance | Asset categorization and tracking rules |
| W404 | Point-of-Sale (POS) System & Hardware Master Governance | POS terminal and peripheral metadata rules |
| W405 | Data Privacy & Consent Preferences Master Governance | Customer privacy preferences master records |

### Core Reporting (4 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W35 | Management Reporting Rhythm | Daily/weekly/monthly reporting |
| W113 | Business Intelligence & Data Governance | BI platform |
| W231 | Management Performance Reporting (QBR) | Executive reporting |
| W326 | Treasury Month-End Close & Reconciliation | Treasury operations |

---

## Tier 2: Standard Support (3,302 Workflows)

These 3,302 workflows are needed for standard operational support, cost controls, and category management.

### Merchandising & Pricing (15 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W1 | Merchandise Planning & Assortment Review | Strategic planning; not Day 1 |
| W27 | Vendor Rebate Accrual & Settlement | Vendor negotiation outcome |
| W50 | Product Information Management (PIM) | Content richness post-go-live |
| W63 | Shelf Label & Price Tag Distribution | Operational efficiency |
| W64 | New Product Pilot / Store Test | Innovation |
| W68 | Product Lifecycle & Discontinuation | Lifecycle management |
| W93 | Markdown & Clearance Pricing Execution | Seasonal clearance |
| W97 | Sample & Demo Inventory Management | Separate tracking |
| W102 | Category Performance Review & P&L Ownership | Category analytics |
| W107 | Pricing Hierarchy Governance & Compliance Audit | Pricing governance |
| W129 | Private Label / In-house Brand Development | PL lifecycle |
| W130 | Competitor Price Intelligence Gathering | Market intelligence |
| W181 | Store-Level Price Tag Printing & Verification | Store execution |
| W262 | Store Promotional Setup & Visual Merchandising Execution | Promotional execution |
| W329 | Competitive Price Tactical Response | Tactical pricing |

### Extended Inventory (6 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W23 | Consignment Inventory Operations | Vendor-owned stock management |
| W57 | Promotional Stock Allocation & Pre-Positioning | Promo stock allocation |
| W154 | Proactive Store Inventory Rebalancing (Stock Push) | System-suggested rebalancing |
| W218 | Inter-DC Stock Rebalancing (Stock Push) | DC-to-DC rebalancing |
| W220 | Slow-Moving & Obsolete Inventory (SLOB) Provisioning & Liquidation | SLOB management |
| W439 | In-Store Bulk-to-Retail Repackaging Operations | Bulk-to-retail conversion for hardware items |

### Extended Procurement (10 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W20 | Vendor Managed Inventory (VMI) | VMI for 12 key vendors |
| W62B | 3PL / Delivery Partner Onboarding & Offboarding | 3PL management |
| W110 | Supplier Quality & CAPA (Corrective and Preventive Action) | Quality management |
| W115 | Supplier Diversity & MSME Development Program | MSME program |
| W150 | Product Quality Testing & Certification | Quality testing |
| W155 | Vendor Strategic Collaboration & Joint Business Planning (JBP) | JBP |
| W160 | Private Label Factory Audit & Social Compliance | PL factory audit |
| W161 | Vendor Price Protection & Market Markdown Claims | Price protection |
| W245 | Vendor Performance Chargebacks & Penalties Management | Penalty management |
| W422 | VMI Collaborative Data Sharing & Replenishment Execution | VMI data collaboration |

### Extended Warehouse (3 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W52 | Fleet Management | Fleet admin |
| W66 | Inter-Island Logistics & Freight Management | Inter-island coordination |
| W221 | Cross-Docking Operations for Fast-Moving Bulky Items | Cross-dock optimization |

### Extended Store Operations (32 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W16 | New Store Opening | Store expansion (10–15/year) |
| W17 | Customer Loyalty Program Operations | Loyalty at POS |
| W28 | Gift Card & Store Credit Lifecycle | Gift card operations |
| W29 | Product Recall Execution | Recall management |
| W45 | Store Closure / Relocation | Store lifecycle |
| W47 | Store Facility Maintenance & Work Orders | Maintenance management |
| W67 | Monthly Store Performance Review | Store analytics |
| W69 | Price Compliance Audit | Price compliance |
| W71 | Store Physical Security & Access Control | Security management |
| W75 | Layaway / Installment Sales | Layaway operations |
| W86 | Planogram Compliance & Store Layout Verification | Planogram compliance |
| W96 | Store Renovation & Remodel Project | Renovation management |
| W111 | Store Energy & Utility Consumption Management | Energy monitoring |
| W470 | Store-Level Rotational Brownout / Power Outage Management Protocol | Power outage operational readiness |
| W471 | Store-Level Security Incident & Police/Barangay Reporting Protocol | Store-level security & legal incident reporting |
| W170 | Senior Citizen & PWD Discount Compliance (PH Legal) | SC/PWD compliance |
| W171 | Store Physical Security & Yard Patrol Routine | Security routine |
| W176 | Store-to-DC Reverse Logistics (Consolidation) | Reverse logistics |
| W205 | Employee Purchase Program & Internal Staff Sales | Employee purchases |
| W248 | Store Inventory Variance & LP Investigation | Variance investigation |
| W278 | Mid-Day Cash Skimming / Till Sweeps | Cash management |
| W428 | Community Disaster Relief & Emergency Response | "Critical Infrastructure" role during PH disasters |
| W445 | Display & Demo Infrastructure Maintenance | Store display maintenance |
| W539 | POS Promotional Coupon, Voucher & Manufacturer Coupon Processing | Coupon/voucher acceptance and reconciliation |
| W542 | POS Quotation & Estimate Generation with Sales Conversion | Quotation-to-order conversion for trade customers |
| W543 | POS Consignment Sell-Through Transaction Processing & Vendor Settlement Trigger | Consignment sell-through processing and vendor settlement |
| W544 | POS Service Work Order Creation & Scheduling | Service work order management at POS |
| W545 | POS Special Order & Customer Order Processing | Special/customer order intake and tracking |
| W546 | POS Deposit & Progress Payment Collection for Project Orders | Project deposit collection and milestone payment tracking |
| W549 | POS Damaged & Open-Box Item Discount Processing | Damaged/open-box item markdown at POS |
| W550 | POS Loyalty Points as Payment Tender | Loyalty point redemption as payment method |
| W551 | POS Customer On-the-Spot Loyalty Enrollment & Account Lookup | Real-time loyalty enrollment during checkout |

### Extended Finance & Treasury (21 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W137 | Intercompany Dividend & Loan Management | IC financial management |
| W174 | Store-Level Cash-in-Transit (CIT) & Armored Car Management | CIT operations |
| W175 | Employee Gratuity & Retirement Fund Management (RA 7641) | Retirement management |
| W184 | Fixed Asset Physical Verification (Audit) | Asset verification |
| W217 | Senior Citizen & PWD VAT-Exemption Audit & Reporting | SC/PWD reporting |
| W232 | Letter of Credit (LC) & Bank Guarantee Lifecycle | LC management |
| W233 | Cash Flow Forecasting & Liquidity Management | Cash forecasting |
| W234 | Intercompany Profit Elimination & Consolidation | IC consolidation |
| W235 | Transfer Pricing Compliance & Documentation | TP compliance |
| W275 | IFRS 16 / PFRS 16 Lease Accounting & Modifications | Lease accounting |
| W276 | Asset Under Construction (AUC) & Mass Capitalization | AUC management |
| W277 | Freight Bill Audit & Payment (FBAP) Reconciliation | Freight cost control |
| W317 | Bank Account Lifecycle & Signatory Management | Bank account management |
| W472 | BOI/PEZA/LGU Tax Incentive Monitoring & Compliance | Tax incentive compliance and optimization |
| W319 | Debt Facility & Covenant Compliance Management | Debt management |
| W320 | Electronic Banking Security & Payment Control | Banking security |
| W321 | FX Exposure Analysis & BSP Regulatory Reporting | FX reporting |
| W322 | Treasury Policy, Governance & Risk Appetite Framework | Treasury governance |
| W323 | Cash Concentration & Inter-Entity Pooling Operations | Cash pooling |
| W327 | External Shareholder Dividend Declaration & Payment | Dividend management |
| W435 | Intercompany Service Level Agreement (SLA) Fee Billing | IC service fee governance |

### Extended HR (8 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W51 | Employee Training & Skills Development | Training programs |
| W72 | Employee Performance Management | Performance reviews |
| W172 | Employee PPE & Uniform Lifecycle | PPE management |
| W178 | Employee Succession & Internal Mobility | Succession planning |
| W179 | Management Trainee (Cadetship) Program | Trainee program |
| W269 | Vendor Promodizer & Third-Party Staff Management | Third-party staff |
| W429 | Vendor-Funded Promodizer Incentive Management | Conflict of interest & labor cost control |
| W449 | Promodizer Labor Compliance & DOLE 174 Governance | Co-employment risk management |

### Extended Supply Chain (5 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W183 | Supply Chain Network Optimization Review | Network optimization |
| W191 | Global Supply Chain — Incoterm & Marine Insurance Tracking | Incoterm management |
| W249 | Import Port Demurrage & Detention Management | Demurrage control |
| W268 | Last-Mile Home Delivery Tracking & Proof-of-Delivery | Last-mile tracking |
| W284 | Customs Bonded Warehouse (CBW) Operations & Duty Deferral | Bonded warehouse |

### Extended Ecommerce (2 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W180 | E-commerce Marketplace Integration (Lazada/Shopee) | Marketplace expansion |
| W210 | E-commerce Fulfillment Hub (Dark Store) Operations | Dark store |
### Customer Experience (11 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W41 | Customer Complaint Resolution | Complaint management |
| W58 | Corporate / Project Account Management | Project accounts |
| W61 | Competitor Price Match Process | Price matching |
| W65 | Customer Satisfaction Measurement | CSAT/NPS |
| W84 | Customer Account Reactivation | Dormant accounts |
| W87 | Customer Feedback-to-Action Loop | Feedback loop |
| W103 | Trade Sales Pipeline & Territory Management | Trade sales |
| W112 | Trade Counter / Pro Desk Operations | Trade counter |
| W156 | Customer Data Platform (CDP) & Hyper-Personalization | CDP |
| W258 | Omni-channel Customer Ticketing & Support Management | Customer ticketing |
| W259 | Call Center Daily Operations & Queue Management | Call center ops |

### Extended IT (23 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W367 | Cybersecurity Operations & Vulnerability Management | Proactive security posture |
| W369 | IT Vendor SLA Governance & Performance Management | Vendor service quality |
| W370 | Software License & SaaS Subscription Management | Compliance & cost control |
| W371 | Mobile Device Management (MDM) Operations | RF device readiness |
| W372 | IT Policy, Security Awareness & User Training | Human-factor security |
| W373 | IT FinOps & Cloud Cost Management | Cloud spend governance |
| W374 | IT Project Intake & Demand Management | IT resource alignment |
| W376 | IT Capacity & Performance Planning | Proactive scaling |
| W378 | IT Problem Management & Root Cause Analysis | Systemic issue elimination |
| W379 | IT Service Request Fulfillment & Service Catalog | Standard IT requests |
| W381 | IT Knowledge Management | Operational continuity |
| W384 | ERP Environment Management & Data Masking | Non-prod data security |
| W391 | Software Quality Assurance (QA) & Testing Lifecycle | Release quality & defect management |
| W392 | IT Service Level Management (SLM) & Business Relationship Management (BRM) | Business alignment & service uptime governance |
| W394 | IT Technical Skills, Training & Certification Lifecycle | IT team competency & succession |
| W395 | Mobile App Store Management (Public & Enterprise) | App release & mobility governance |
| W396 | ERP Data Archiving & Database Tiering Operational Execution | ERP performance & storage cost control |
| W434 | NPC Annual DPO & System Registration | Mandatory data privacy compliance |
| W386 | IT Strategy & Annual Roadmap Development | IT strategic alignment |
| W387 | IT Compliance & Control Self-Assessment (CSA) | IT control validation |
| W388 | Shadow IT Discovery & Governance | Unauthorized IT risk mitigation |
| W389 | Data Privacy Impact Assessment (DPIA) Lifecycle | RA 10173 DPIA requirement |
| W390 | IT Service Continuity & Business Impact Analysis (BIA) Refresh | Business continuity foundation |

### Compliance & Governance (19 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W49 | Natural Disaster / Typhoon Business Continuity | BC planning |
| W77 | BIR Tax Audit Response | BIR audit |
| W78 | Government / Institutional Procurement Participation | Government procurement |
| W79 | Employee Grievance & Whistleblower Process | Grievance management |
| W82 | Hazardous Waste Disposal Tracking & DENR Compliance | Hazmat compliance |
| W95 | External Audit Coordination & Support | External audit |
| W114 | Sustainability & Environmental Compliance Reporting | ESG reporting |
| W185 | Product Liability & Consumer Safety Incident Management | Product safety |
| W207 | Store-Level Security Camera (CCTV) Audit & LP Integration | CCTV audit |
| W209 | Barangay & Local Community Relationship Management | Community relations |
| W216 | BIR CAS (Computerized Accounting System) Compliance Audit | BIR CAS audit |
| W469 | Customer Complaint DTI Escalation & Consumer Adjudication Management | DTI complaint adjudication case management |
| W285 | Public Liability & Customer Incident Claims Management | Liability claims |
| W426 | Annual Conflict of Interest (COI) & Gift Policy Disclosure | Corporate governance & fraud prevention |
| W427 | DTI Sales Promotion Permit Monitoring & In-Store Compliance | Regulatory fine avoidance |
| W433 | DENR Self-Monitoring (SMR) & Compliance (CMR) Reporting | Mandatory environmental reporting |
| W437 | Regulatory Branch De-registration & Permit Cancellation | Final regulatory closure procedure |
| W444 | Community Solicitation & Donation Processing | Community relations governance |
| W446 | Temporary LGU Permits for Outdoor Sales & Events | LGU compliance for promotional events |

### Facility & Asset Maintenance (3 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W240 | DC Facility & Warehouse Equipment Maintenance | DC maintenance |
| W241 | HQ Office Facility & Executive Asset Maintenance | HQ maintenance |
| W242 | 3PL & Logistics Partner Performance Review | 3PL performance |

### Extended Health & Safety (1 workflow)

| ID | Workflow | Operational Significance |
|---|---|---|
| W436 | Annual OHS Statutory Reporting (WAIR/AMR) | Mandatory safety compliance reporting |

### Extended Master Data (25 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W290 | Hierarchical Category Structure Management | Category management |
| W292 | Employee Master Data Governance & Cross-Entity Lifecycle | Employee master |
| W295 | Payment Terms & Settlement Rule Master Governance | Payment terms |
| W296 | Service & Non-Stock Item Master Governance | Service items |
| W297 | Warehouse Location & Bin Master Governance | Bin management |
| W298 | Product Attribute Template Master Governance | Attribute templates |
| W299 | Assortment & Store Cluster Master Governance | Assortment matrix |
| W300 | Promotional Rule & Campaign Master Governance | Promo rules |
| W301 | Reason Code & Disposition Master Governance | Reason codes |
| W302 | Kit/BOM & Bundle Structure Master Governance | Kit structures |
| W303 | Manufacturer/Brand Master Governance | Brand management |
| W304 | Routing, Carrier & Transit Time Master Governance | Routing |
| W305 | Intercompany Transfer Pricing Rule Master Governance | IC pricing |
| W306 | Seasonal Calendar & Event Master Governance | Seasonal calendar |
| W307 | Currency & Exchange Rate Master Governance | FX rate governance |
| W310 | Address & Geographic Hierarchy Master Governance (Philippine-Specific) | PSGC codes |
| W313 | Loyalty Program Configuration & Rule Master Governance | Initial config pre-loaded; ongoing governance matures in Phase 2 |
| W314 | Planogram Template & Space Planning Master Governance | Planogram master |
| W315 | Product Lifecycle Status & Transition Rule Master Governance | Lifecycle master |
| W316 | Digital Asset & Product Content Master Governance | Digital asset master |
| W400 | Equipment & Asset Maintenance (EAM) Master Governance | EAM equipment classification and tagging metadata |
| W401 | Fleet & Vehicle Master Governance | Logistics fleet registration and specifications metadata |
| W402 | Contract & Agreement Master Governance | Legal contract classification and metadata fields |
| W403 | Competitor & Market Intelligence Master Governance | Competitor profiles and pricing category structures |
| W406 | ESG & Sustainability Metrics Master Governance | Carbon emission factor and environmental indicators metadata |

### Other Phase 2 (22 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W116 | Site Selection & Feasibility Analysis | Real estate expansion |
| W117 | Lease Administration & Renewal | Lease management |
| W118 | Rent & CAM Payment Processing | Rent payments |
| W119 | Real Property Tax (Amillaramiento) Management | Property tax |
| W162 | Project Quotation & Bid Management | Trade/project sales |
| W163 | Contract Pricing & Project Price Books | Project pricing |
| W164 | Staged Project Delivery & Call-Off Orders | Staged deliveries |
| W165 | Project Retention & Milestone Billing | Milestone billing |
| W166 | Corporate / Institutional Tendering | Tendering |
| W169 | Lumber & Board Cutting Services | Daily revenue-generating service; system-supported during wave rollout |
| W228 | Sales Commission Calculation (Trade & Project Sales) | Commission management |
| W229 | B2B Customer Credit Limit Exception & Escalation | Credit exceptions |
| W421 | Batch/Shade Reconciliation for Large Project Sales | Shade consistency |
| W239 | Customs Duty & Tax Reconciliation (BOC) | Customs reconciliation |
| W255 | Electronic Document Storage & Retrieval (ERP-wide) | Document storage |
| W256 | Enterprise Document Retention & Archiving Policy | Document retention |
| W264 | Seasonal Merchandise Transition & Display Rotation | Seasonal transition |
| W279 | Product Substitution Rules & Governance | Substitution rules |
| W441 | Corporate Staff Housing & Billeting Management | Staff housing management |
| W238 | Hazmat Spill Response & Incident Management | Hazmat spill response |
| W430 | LGU Business Permit & "Amillaramiento" (RPT) On-Site Inspection | Regulatory compliance for 200 sites |
| W431 | LGU-Specific "Truck Ban" & Route Governance | Delivery window & fine management |

---

## Tier 3: Advanced Optimization (758 Workflows)

These 758 workflows deliver advanced capabilities for competitive differentiation, AI-driven automation, and deep business analytics.

### Innovation & Digital Transformation (8 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W200 | AI-Driven Personalization & Recommendation Engine | AI capability |
| W201 | Robotic Process Automation (RPA) Lifecycle | RPA automation |
| W202 | Predictive Maintenance for Industrial Assets | Predictive capability |
| W203 | Computer Vision for Inventory & Planogram Audit | Computer vision |
| W208 | Retail Analytics & AI-Driven Inventory Optimization | Advanced analytics |
| W420 | AI Shelf Monitoring & Real-time Replenishment Alerting | AI shelf monitoring |
| W397 | Cyber Threat Intelligence & Proactive Threat Hunting | Advanced threat detection maturity |
| W398 | IT Innovation, Emerging Tech & Proof of Concept (PoC) Lifecycle | Structured technology innovation |

### ESG & Sustainability (4 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W192 | Greenhouse Gas (GHG) Emissions Tracking | Carbon tracking |
| W193 | Waste Management & Circular Economy | Waste management |
| W194 | Social Impact & Community Development (CSR) | Social impact |
| W195 | Sustainable Sourcing & Ethical Vendor Audit | Ethical sourcing |

### Marketing & Campaigns (13 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W83 | Marketing Campaign Planning, Execution & Performance Measurement | Full campaign lifecycle |
| W104 | Loyalty Program Financial Governance & Periodic Review | Loyalty financials |
| W134 | Crisis Communication & Brand Reputation Management | Crisis management |
| W135 | CSR Program Execution | CSR execution |
| W142 | Social Media & Influencer Management | Social media |
| W143 | Public Relations & Corporate Communications | PR management |
| W149 | Bank & Credit Card Partnership Management | Bank partnerships |
| W151 | Corporate Social Responsibility (CSR) Impact Measurement & Reporting | CSR measurement |
| W153 | Retail Media Network (RMN) Operations | RMN operations |
| W189 | Referral Program & Brand Ambassador Management | Referral program |
| W190 | In-house Design & Creative Production Management | Creative production |
| W263 | Loyalty Member Enrollment & Onboarding Journey | Enrollment journey |
| W286 | Retail Media Network (RMN) Vendor Billing & Yield Management | RMN billing |

### Corporate Governance & Strategy (8 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W124 | Corporate Secretarial & Entity Management | Corporate secretarial |
| W125 | Legal Case & Litigation Management | Litigation |
| W126 | Intellectual Property (IP) Portfolio Management | IP management |
| W127 | Annual Strategic Planning & OKRs | Strategic planning |
| W128 | Enterprise Project Management (EPM) Lifecycle | EPM |
| W186 | Internal SOP & Policy Governance Lifecycle | SOP governance |
| W230 | Legal Contract Review & Approval | Legal review |
| W474 | Enterprise Data Governance Council Operations | Data quality policy ratification and dispute arbitration |

### Internal Audit (42 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W120 | Internal Audit Planning & Risk Assessment | Audit planning |
| W121 | Operational Audit Execution (Store/DC/HQ) | Operational audit |
| W122 | Enterprise Risk Management (ERM) Review | ERM |
| W123 | Fraud Investigation Protocol | Fraud investigation |
| W159 | Anti-Bribery & Corruption (ABC) Monitoring & Audit | ABC monitoring |
| W243 | Power of Attorney (POA) & Board Resolution Lifecycle | POA management |
| W331 | IT General Controls (ITGC) & Cybersecurity Audit | ITGC compliance |
| W332 | Continuous Control Monitoring (CCM) & Exception Management | Real-time controls |
| W333 | Audit Issue Remediation & CAP Tracking | Findings lifecycle |
| W334 | Third-Party Vendor Risk & Compliance Audit | External risk |
| W335 | Major Capex & Post-Implementation Project Audit | Investment control |
| W336 | Quality Assurance & Improvement Program (QAIP) | IA quality |
| W337 | Payroll & Statutory Compliance Audit | Payroll integrity |
| W338 | Segregation of Duties (SOD) Review & Remediation | Access governance |
| W339 | Regulatory Compliance Audit (DPA, Labor, Consumer Act) | Legal risk management |
| W340 | Unannounced Store Cash & Vault Audit | Retail cash control |
| W341 | ESG Assurance & Sustainability Compliance Audit | ESG audit |
| W342 | Inventory Observation & Cycle Count Audit | Inventory audit |
| W343 | Lease & CAM (Common Area Maintenance) Compliance Audit | Lease audit |
| W344 | Trade Promotion, Rebate & Marketing Spend Audit | Trade spend audit |
| W345 | Logistics, Fleet & Fuel Management Audit | Logistics audit |
| W346 | Capex Construction & Store Build-out Audit | Construction audit |
| W347 | E-commerce & Omni-channel Operations Audit | E-commerce audit |
| W348 | Revenue Assurance & Payment Gateway Audit | Revenue audit |
| W349 | Corporate Tax & Statutory Reporting Audit | Tax audit |
| W350 | BC/DR Readiness & Crisis Management Audit | BC/DR audit |
| W351 | External Audit Coordination & Statutory Filing Support | External audit support |
| W352 | Fixed Asset Verification & Audit | Fixed asset audit |
| W353 | Ethical Sourcing & Social Compliance Audit | Ethical sourcing audit |
| W354 | AML & Sanctions Screening (Wholesale/B2B) Audit | AML audit |
| W355 | Intellectual Property (IP) & Brand Protection Audit | IP audit |
| W356 | Whistleblower System & Non-Retaliation Audit | Whistleblower audit |
| W357 | Board Governance & Manual on Corporate Governance (MCG) Compliance Audit | Governance audit |
| W358 | Physical Security, CCTV & Guard Force Audit | Physical security audit |
| W359 | AI Governance, Algorithmic Bias & Data Ethics Audit | AI governance audit |
| W360 | Crisis Response & Incident Management Audit | Crisis audit |
| W361 | Corporate Treasury, Cash Management & Investment Audit | Treasury audit |
| W362 | Master Data Governance & Data Quality Audit | MDM audit |
| W363 | Insurance Program & Claims Audit | Insurance audit |
| W364 | Marketing Agency & Media Spend Audit | Media spend audit |
| W365 | Strategic Workforce Planning & Succession Audit | Workforce audit |
| W466 | Loss Prevention & Asset Protection (LPAP) | LP operations audit |

### Advanced Store Operations (10 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W173 | Store-Level Solar Energy Monitoring | Solar monitoring |
| W177 | Vending & Concessionaire Management | Concessionaire |
| W182 | Gift / Home Registry Lifecycle | Gift registry |
| W206 | Mobile POS (mPOS) & Queue-Busting Operations | mPOS |
| W212 | Automated Store Cash Management & Smart Safe Integration | Smart Safe |
| W272 | Cashier Over/Short Dispute & Deduction Resolution | Cashier disputes |
| W281 | Self-Checkout (SCO) Exception & Intervention Management | SCO |
| W547 | POS Scan & Go / Mobile Self-Scan Checkout | Mobile self-scan checkout experience |
| W548 | POS Third-Party On-Demand Delivery Integration | On-demand delivery partner integration |
| W552 | POS Donation & Charity Round-Up Processing | Charity round-up at checkout |

### Services & Value-Added (6 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W138 | Home Installation Services Management | Installation services |
| W139 | Tool & Equipment Rental Operations | Tool rental |
| W147 | DIY Workshop & In-Store Event Management | Workshops |
| W148 | Home Design & Consultancy Services | Design consultancy |
| W168 | Custom Paint Mixing & Tinting Operations | Paint mixing |
| W211 | In-Store 3D Kitchen/Bathroom Design Rendering | 3D rendering |

### Wholesale & B2B (3 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W145 | Wholesale Reseller Onboarding & Credit Management | Wholesale channel |
| W146 | Bulk Fulfillment & Cross-Docking for Wholesale | Bulk fulfillment |
| W283 | B2B Punchout Catalog Integration (cXML) | B2B integration |

### Engineering & Construction (5 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W223 | New Store Design & Engineering Standards | Store design |
| W224 | Construction Bidding & Contractor Selection | Construction bidding |
| W225 | Store Construction Management & Supervision | Construction management |
| W226 | Store Renovation & Retrofitting (CAPEX) | Store renovation |
| W227 | Commissioning & Operational Handover | Commissioning |

### Fleet & Logistics (8 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W196 | Route Planning & Dispatch Optimization | Route optimization |
| W197 | Driver Performance & Safety Management | Driver management |
| W198 | Fuel Management & Consumption Monitoring | Fuel management |
| W199 | Fleet Telematics & Real-Time Tracking | Telematics |
| W1163 | 3PL & Delivery Partner Daily Operations Management | 3PL partner coordination |
| W1164 | Inter-Island Logistics Coordination & Shipping Management | Inter-island shipping |
| W1165 | Last-Mile Delivery Dispatch, Tracking & SLA Management | Last-mile delivery SLA |
| W1166 | Carrier Rate Management, Freight Audit & Cost Optimization | Freight cost management |

### Hazmat & Safety (4 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W141 | Workplace Safety Inspection & Audit | Safety inspection |
| W187 | Contractor & Third-Party On-site Safety Orientation | Contractor safety |
| W236 | Hazmat Storage & Segregation Compliance (DC) | Hazmat storage |
| W237 | Hazmat Handling & Safety Training (Store) | Hazmat training |

### Advanced Treasury (3 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W318 | Short-Term Investment & Surplus Cash Placement | Investment management |
| W324 | Supply Chain Finance & Dynamic Discounting Program | SCF program |
| W325 | Corporate Guarantee & Contingent Liability Management | Guarantee management |

### Advanced Master Data (7 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W222 | DC Container Yard & Chassis Management | Container yard |
| W273 | In-Store Endless Aisle & Vendor Direct-to-Customer Delivery | Endless aisle |
| W274 | Third-Party Customer Financing / Equipment Leasing | Customer financing |
| W440 | Power Tool Service & Repair Center Operations | Power tool service |
| W442 | Site Technical Survey & Measurement Services | Site survey service |
| W443 | Salvage & Scrap Material Disposition (Waste-to-Cash) | Salvage monetization |
| W465 | Network-Wide Disaster Recovery & BCP | Enterprise BCP governance |

### Advanced MDM, Services, and Other (4 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W157 | E-waste Collection & Circular Economy Operations | E-waste |
| W167 | Store & DC Recycling Program (Circular Economy) | Recycling |
| W213 | Installation Service Partner Quality Audit | Partner audit |
| W282 | Subscription Billing for Recurring Home Services | Subscription billing |

---

## Summary

### Confirmed classification (hand-reviewed)

| Phase | Label | Workflow Count | % of Classified |
|---|---|---|---|
| Phase 1 | Go-Live Critical (Tier 1) | 1,396 | 25.6% |
| Phase 2 | Operational Excellence (Tier 2) | 3,302 | 60.5% |
| Phase 3 | Innovation & Optimization (Tier 3) | 758 | 13.9% |
| **Confirmed Total** | | **5,456** | 100% |

> Counts include 23 `###` parent/summary sub-workflows (e.g. W5A/W9A/W54A) that receive their
> own classification row; the remaining 5,433 are canonical `##` workflows.

### Proposed classification (keyword-driven, pending human review)

The register reached full coverage on 2026-06-28 (every then-existing keyword-proposed workflow
promoted by the Full-Coverage Confirmation Pass) and holds full coverage again since 2026-09-02,
when the fourteen post-catalog workflow-level gap fills (W5497–W5510, added 2026-08-24/26) were
confirmed by the post-catalog confirmation pass — 6 → Tier 1, 6 → Tier 2, 2 → Tier 3, with three
statutory-execution promotions (W5498/W5503/W5504), one analytics promotion (W5501), two analytics/
billing-core demotions to Tier 3 (W5509) and Tier 2 (W5507/W5510), and eight adoptions at the
keyword-proposed tier. [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) is
empty and is regenerated by
[`07-methodology/classify-workflows.py`](../../07-methodology/classify-workflows.py)
whenever new workflows ship unclassified.

| Phase | Label | Proposed Count |
|---|---|---|
| Phase 1 | Go-Live Critical (Tier 1) — proposed | 0 |
| Phase 2 | Operational Excellence (Tier 2) — proposed | 0 |
| Phase 3 | Innovation & Optimization (Tier 3) — proposed | 0 |
| **Proposed Total** | | **0** |

| Coverage | Workflows |
|---|---|
| Confirmed (hand-reviewed) | 5,456 rows (5,433 unique `##` workflows) |
| Proposed (keyword, pending review) | 0 |
| Without even a proposal | 0 |
| **Grand Total** | **5,433** unique `##` workflows (5,433 confirmed + 0 unclassified) |

### Domain Breakdown

The per-tier subsection headings above (Core Finance, Extended Store Operations, Internal Audit, etc.) provide the authoritative domain-and-phase breakdown of the 5,456 classified register rows (5,433 unique workflows), and the [value-stream-index.md](./value-stream-index.md) provides the authoritative value-stream/process-area breakdown of all 5,433 workflows. A rolled-up "by domain" summary table was removed during consistency review because it could not be reconciled with the tier totals and presented stale partial counts.

> **2026-09-05 addition (cyber-extortion, payment-diversion, land-occupation & water-continuity gap fill, batch 20):** Four workflow-level gap fills — W5558 (Ransomware & Destructive Cyber-Attack Enterprise Response Protocol; PA-27.3), W5559 (Vendor Payment-Diversion & Business Email Compromise (BEC) Fraud Event Response & Recovery Protocol; PA-18.2), W5560 (Informal-Settler Invasion & Illegal Occupation of Banked Land — Detection, Relocation & Ejection Protocol; PA-178.1), and W5561 (Sustained Water-Service Interruption Response & Store Continuity Protocol; PA-07.2) — were added after the batch-16/17/18/19 edge-case sweeps were re-run across scenario families not yet probed (destructive cyber attack with extortion, disbursement-diversion fraud, vacant-land occupation, utility-service failure beyond power): the ransomware/destructive-attack event ('ransomware'/'extortion demand'/'data-destruction' in zero dedicated headers — only PA-27.2's DR pain point naming the isolate-DR-before-failover trap, W1330's exercise inject, W5529's OT drill; nobody owned the extortion-decision law, the DR-isolation sequencing, chain-wide manual trading mode, the privileged forensics clock, or the insurance/disclosure chain), the payment-diversion/BEC event (BEC named only in PA-18.2 pain points with a one-bullet callback mitigation, and VS-125.2 watching only the customer-side diversion class — nobody owned the after-prevention-fails event: the same-day recall race, the honest-ledger treatment, the insider-vs-mailbox forensics, or the cooling-off retrofit), the informal-settler invasion event ('informal settler'/'squatter'/'illegal occupation'/'adverse possession' in zero PA files — nobody owned the prescription-interruption evidence discipline, the RA 7279 syndicate-vs-settler classification, the no-self-help eviction rule, or the caretaker-fraud variant on parcels held vacant for years), and the sustained water-interruption event ('water interruption'/'water rationing' only as product-selling context in PA-09.2 — nobody owned the sanitation decision law, the live-goods watering priority, emergency trucked-water sourcing, or the flush-and-confirm recovery gate). The same analysis produced the custody register's seventh wave (event-custody-and-precedence-register.md v1.7, events E-34–E-37). W5558 ships **directly confirmed Tier 1** (the enterprise-trading-halt & statutory-continuity class of the W5545/W5546 precedent — the data-privacy core rides the Tier-1 W53 chain, the OT variant rides W5529); W5559/W5560/W5561 ship **directly confirmed Tier 2** (the financial-crime contingency class of W5541/W2814, the landbanking asset-protection class of W5133/W5143, and the facility-continuity class of the W470 power analog).
>
> **2026-09-05 addition (storefront-crash, brand-impersonation-scam, wallet-outage & adjacent-works gap fill, batch 21):** Four workflow-level gap fills — W5562 (Vehicle-Impact & Storefront-Crash Response Protocol; PA-147.2), W5563 (Brand-Impersonation Commerce-Scam Response (Fake Sellers & Fraudulent Pickup Offers); PA-100.2), W5564 (Mobile-Wallet Platform Outage Response (E-Wallet Tender Downtime); PA-08.1), and W5565 (Third-Party Construction Damage & Adjacent-Works Response Protocol; PA-20.3) — were added after the batch-16/17/18/19/20 edge-case sweeps were re-run across scenario families not yet probed (vehicle impact into an operating store, brand-impersonation commerce scams whose victims arrive at stores, mobile-wallet provider outages, adjacent construction damaging occupied property): the vehicle-impact event ('vehicle into building'/'storefront crash' in zero PA files — nobody owned the crash-scene safety law, the driver's-CTPL-first liability ordering with subrogation, the red-tag structural discipline before any zone reopens, or the bollard/barrier retrofit feedback), the brand-impersonation commerce-scam event ('fake seller'/'scam listing' in zero PA files — nobody owned the victims-arrive-at-our-stores protocol, the same-day advisory with a single verification source of truth, the simultaneous takedown wave, or the data-harvesting variant's W53 routing), the mobile-wallet platform-outage event (one tender-outage canon per rail — W5547 owns cards, W535 store connectivity; nobody owned the wallet rail's rail-diagnosis protocol, tender-type directive flag, no-manual-receipt double-charge rule, or stranded-authorization settlement sweep), and the adjacent-works damage event ('adjacent construction'/'excavation damage' in zero dedicated headers — nobody owned the evidence-before-repair rule, the red-tag safety gate, the CAR/TPD-first claim ordering, or the LGU permit-leverage track). The same analysis produced the custody register's eighth wave (event-custody-and-precedence-register.md v1.8, events E-38–E-41). W5562 ships **directly confirmed Tier 1** (the life-safety structural-clearance class of the W5537/W5555 precedent — gating zone reopening on documented external assessment); W5563/W5564/W5565 ship **directly confirmed Tier 2** (the brand-integrity event class of W5557/W5550, the payment-platform contingency class of W5547/W5548, and the asset-protection contingency class of W5560/W5133).
>
> **2026-09-05 addition (terminal-tampering, procurement-impersonation, account-takeover & commute-disruption gap fill, batch 22):** Four workflow-level gap fills — W5566 (Payment-Terminal Tampering & Card-Skimmer Response (PIN-Pad Compromise Event); PA-08.2), W5567 (Procurement-Impersonation & Fake-PO Goods-Diversion Response; PA-03.2), W5568 (Official-Channel Account-Takeover Response (Brand-Account Hijack); PA-14.2), and W5569 (Mass-Commute Disruption & Transport-Strike Continuity Protocol; PA-141.2) — were added after the batch-16/17/18/19/20/21 edge-case sweeps were re-run across scenario families not yet probed (payment-device compromise at the lane, fraudsters impersonating BuildRight as the buyer, takeover of BuildRight's own verified accounts, and commute interruptions that strand crews while sites stay undamaged): the device-compromise event ('card skimmer'/'tampered terminal' in zero PA files — W537 owns terminal operations, W1205 the PCI program, VS-125.2 transaction-level fraud; nobody owned the freeze-in-place evidence rule, the fleet sweep, the acquirer notification clock, or the seal retrofit), the procurement-impersonation event ('fake PO'/'fraudulent purchase order' in zero PA files — the mirror image of W5559's diverted payments and W5563's fake sellers; nobody owned the void-order posture, the supplier wave, the receiving holds, or the order-code retrofit), the brand-account hijack event (W5563 covers pages that pretend to be BuildRight; nobody covered the real accounts turned against their followers — the credential kill-chain, the platform appeal, the unaffected-channel advisory, or the W53 clock on exposed follower data), and the mass-commute disruption event ('transport strike'/'commute disruption' in zero PA files — W4255 is vehicle-level and the closure canon is site-level; nobody owned the attendance-forecast call, the critical-role matrix, the W4253-gated surge, or the no-penalty coding). The same analysis produced the custody register's ninth wave (event-custody-and-precedence-register.md v1.9, events E-42–E-45). All four ship **directly confirmed Tier 2** (W5566 the payment-device security class of W1205/W5547, W5567 the procurement-fraud contingency class of W5559/W5563, W5568 the brand-integrity channel-contingency class of W5563/W5550, and W5569 the workforce-continuity class of W5561/W4255).
>
> **2026-09-05 addition (gas-leak, tsunami/storm-surge, media-exposé & server-room-environmental gap fill, batch 23):** Four workflow-level gap fills — W5570 (Gas-Leak Event Response (LPG/Natural-Gas Odor on Premises); PA-24.2), W5571 (Tsunami & Storm-Surge Coastal-Intrusion Response Protocol (PHIVOLCS Advisory / PAGASA Storm-Surge Warning); PA-26.1), W5572 (Undercover-Investigation & Media-Exposé Response Protocol (Investigative-Newsroom Event); PA-14.3), and W5573 (Server-Room & Data-Center Environmental Event Response (Cooling Failure, Water Intrusion, Fire-Suppression Discharge); PA-27.2) — were added after the batch-16/17/18/19/20/21/22 edge-case sweeps were re-run across scenario families not yet probed (pre-ignition gas events at sites with LPG exchange cages, coastal water intrusion by tsunami or storm surge, genuine-fault investigative journalism, and physical-room failures inside the IT estate): the gas-leak event ('gas leak'/'gas odor'/'smell of gas' in zero PA files — W5069 owns cylinder leak inspection/quarantine as intake QC and W5537 the fire event after ignition; nobody owned the pre-ignition odor event: the odor-is-real law, the ignition-source ban, the heavier-than-air evacuation, the trained-only isolation boundary, or the detector-clear reopen gate), the coastal-intrusion event ('tsunami' in zero PA files, 'storm surge' only as PA-09.2 product-advisory context — W1450's quake canon ends at structural assessment and W1387 owns rainfall/riverine flooding; nobody owned the quake-is-the-warning law, vertical move-up, the no-return rule until PHIVOLCS cancellation, the surge-forecast closure ladder, or the salt-intrusion desalination gate), the media-exposé event ('undercover'/'hidden camera'/'investigative report'/'right of reply' in zero PA files — W1562 owns recall/safety media response and W3271/W3272 the fake-content class; nobody owned genuine-fault journalism: the authentication-before-response law, the no-obstruction rule, the right-of-reply discipline, the self-report calculus, or the remediation track), and the server-room environmental event ('server room'/'cooling failure'/'fire-suppression discharge' in zero PA files — W55 owns failover execution once declared and W380 alert triage; nobody owned the thermal-runaway clock, the power-before-water rule, the suppression re-arm discipline, the RTO-bounded failover boundary, or the staged repower). The same analysis produced the custody register's tenth wave (event-custody-and-precedence-register.md v1.10, events E-46–E-49). W5570/W5571 ship **directly confirmed Tier 1** (the pre-ignition life-safety class of the W5537/W5538 precedent and the coastal-water evacuation-and-clearance class of the W1449/W5562 precedent — each gates a physical-state transition on documented external assessment); W5572/W5573 ship **directly confirmed Tier 2** (the brand-integrity comms-contingency class of W5563/W5568 and the IT-facility-contingency class of W5547/W5564).
>
> **2026-09-21 addition (batch 25) — ERP customization governance (the CDR/customization-register loop).**
> The EBS blueprint layer issued from 2026-09-14 defines a set of recurring post-go-live processes that no gap pass had yet read:
> the customization decision record and its eight-gate admissibility test, the hard extension budget with its retire-one-to-add-one
> rule, the customization register and its quarterly object-inventory audit against the databases, and the de-customization
> programme with its five retirement triggers. Keyword verification: 'CEMLI', 'de-customization', 'extension budget' and
> 'customization governance' appear in zero PA files, and 'customization' in eight with no dedicated `## W` header (all incidental —
> product/bundle customization, the software-capitalization gray area, an over-customization risk bullet). The adjacent owners each
> govern a different boundary: W5515 decides use-EBS versus build, W3571 reviews initiative architectures and W3573 their
> deviations, W132/W1409 deliver a change, and W495 checks custom-code compatibility during a patch cycle — nothing owned the gate
> between configure and extend inside the suite. **W5575** Customization Decision Record (CDR) Intake, Admissibility Gate & ARB
> Approval, **W5576** CEMLI Register Maintenance & Quarterly Object-Inventory Audit and **W5577** Extension De-Customization,
> Retirement & Budget Reclamation (all VS-113.1) fill the surface and ship **directly confirmed Tier 2** (the architecture-governance
> class of the W5515–W5517 siblings; the ARB, change-management and patch rails they invoke are already in place, so nothing here is
> go-live blocking). All absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 532 / 6,932). Canonical totals are now
> **188 value streams · 569 process areas · 5,430 workflows** (5,453 confirmed register rows; Tier 1 1,396 unchanged, Tier 2
> 3,296 → 3,299).
>
> **2026-09-10 addition (batch 24) — concessionaire connectivity request, approval & independent-circuit governance.**
> A concessionaire operating-model review (the batch-3 concession-catalog lineage) found the connectivity question unowned: W177
> bundles internet into the monthly 'Rent + Utilities + Commission' invoice and W111 benchmarks internet as a store utility, but no
> workflow owned the case where a concessionaire wants its own internet connection — neither the policy answer (allowed only as a
> contract-governed exception to the BuildRight-provided-utility default, with the segmented Wi-Fi offering on BuildRight's own link
> evaluated first) nor the machinery (the eligibility gate, the W5520/W5418-class isolation envelope, the W47 works approval with
> landlord and LGU consent for exterior terminations, the W117 addendum with incident demarcation and insurance per VS-147, the
> commission-integrity clause keeping all sales on the BuildRight throughput SKU, and the restoration holdback at exit).
> **W5574** Concessionaire Connectivity Request, Approval & Independent-Circuit Governance (VS-07.1) fills the surface and ships
> **directly confirmed Tier 2** (the concession-operations governance class of the W5505–W5507 siblings; the network-boundary
> machinery it invokes — W366, W5520, W5418/W5421, W1409 — is already in place, so nothing here is go-live blocking). All absorbed
> within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Canonical totals are now **188 value streams · 569
> process areas · 5,427 workflows** (5,450 confirmed register rows; Tier 1 1,396 unchanged, Tier 2 3,295 → 3,296).
>
> **2026-09-05 addition (in-transit-security, fatality-scene, tampering-extortion & recruitment-fraud gap fill, batch 19):** Four workflow-level gap fills — W5554 (In-Transit Cargo Hijacking, Armed Truck Robbery & Driver-Safety First Response Protocol; PA-06.2), W5555 (Customer or Visitor Death on Premises — Scene Protocol, Family Liaison & Trading-Continuity Decision; PA-147.3), W5556 (Product-Tampering Threat, Extortion Demand & Merchandise-Integrity Sweep Protocol; PA-89.1), and W5557 (Recruitment Fraud & Fake Job-Offer Scam Response, Takedown & Victim-Guidance Protocol; PA-121.1) — were added after the batch-16/17/18 edge-case sweeps were re-run across scenario families not yet probed (in-transit cargo crime, on-premises death events, merchandise-integrity extortion, employment-brand impersonation): the in-transit hijacking event (cargo theft appears only inside W1337's ORC intelligence background and VS-180's relief-convoy escort note; W653 owns accidents/cargo damage, W2814 the CIT-vendor robbery, E-21 armed violence on premises — nobody owned the roadside armed-robbery event, whose first rule is the opposite of loss prevention: comply, surrender the load, protect the crew), the death-on-premises event (W4401 owns injuries and names fatality only as W4405's notification trigger; 'death on premises'/'died in store' in zero PA files as protocol content — nobody owned the potential-crime-scene discipline until PNP/SOCO documented clearance, the family-liaison sequencing that prevents social-media-first discovery, the dignity-first trading-continuity decision, or the witnessing-staff stand-down), the product-tampering threat/extortion event (VS-89 owns every found-defect trigger — W2993 intake, W2994 recall decision, W2995 notification, W3000 stop-sale — but 'tampering threat'/'contamination threat'/'extortion' appear in zero dedicated headers; nobody owned the never-pay rule, the specificity-gated sweep-or-monitor decision, or the law-enforcement assessment that must precede any W3000 stop-sale), and the recruitment-fraud event ('recruitment scam'/'fake job'/'job scam' in zero PA files; PA-100.2's W3272 digital-IP machinery watches impersonating sites/accounts through the customer-phishing lens, W3764 the review-site reputation — nobody owned the event whose victims arrive at BuildRight's own door: the same-day never-charges-fees advisory, the multi-surface takedown wave, the empathy-first victim-guidance desk, and the PNP Anti-Cybercrime referral). The same analysis produced the sixth custody wave (event-custody-and-precedence-register.md v1.6, events E-30–E-33: in-transit cargo hijacking, death on premises, product-tampering threat, recruitment fraud). W5555/W5556 ship **directly confirmed Tier 1** (the life-safety scene-and-clearance class of the W5536/W5537/W5538 precedent — each gates a physical-state transition on documented external assessment: PNP/SOCO scene release, and the law-enforcement-assessed sweep/stop-sale decision); W5554/W5557 ship **directly confirmed Tier 2** (the contingency-operations class of W653/W2814 with the crew-safety dimension riding the Tier-1 W501/W717 chains, and the brand-integrity channel-contingency class of the W5550/W5553 precedent).

> **2026-09-05 addition (channel-enforcement, employee-legal-status, OSH-enforcement & app-store-removal gap fill, batch 18):** Four workflow-level gap fills — W5550 (Marketplace Account Suspension, Enforcement Freeze & Appeal Recovery Protocol; PA-10.3), W5551 (Employee Arrest, Detention & Criminal-Case Employment-Status Response Protocol; PA-19.1), W5552 (DOLE Imminent-Danger Work-Stoppage Order Response, Abatement & Reinstatement Gate; PA-24.1), and W5553 (Mobile App Store Removal, Policy-Violation Response & Re-Listing Recovery Protocol; PA-75.1) — were added after the batch-16/17 edge-case sweeps were re-run across scenario families not yet probed (platform-side channel enforcement, employee criminal-case events, OSH enforcement orders, store-distribution takedowns): the marketplace account-suspension event ('account suspension'/'account health'/'delisting' in zero PA files — W1470 owns the preventive seller-metrics layer ending at "escalates … to avoid platform penalties" and W659 the own-platform incidents, but nobody owns the enforcement event itself: freeze-scope containment, demand re-routing, the appeal pack, the settlement-freeze accounting and the reinstatement gate), the employee arrest/detention event ('arrest' only as a VS-167 re-screening trigger and an LP case-closure outcome; nobody owns the employment-status mechanics — the involuntary-absence leave placement, the work-relatedness/legal-support decision with the employer's Arts. 2176/2180 exposure, family liaison, acquittal-reinstatement, and the W2883/W2884 two-notice gate on verified facts), the DOLE imminent-danger stop-work order (RA 11058 cited in ~15 PA files only as the duties/penalties context of W505 — 'work stoppage'/'stoppage order'/'imminent danger' in zero dedicated headers; the OSH analog of the W5545 closure-order class: comply-first abatement, the no-wage-loss rule, and reopening only on the written DOLE lifting), and the app-store removal event ('app store removal'/'policy violation'/'app takedown' in zero files — W2647 owns listing upkeep and W2650 monitoring, not the removal: class-specific fix paths, the appeal with remediation in hand, interim-channel comms and the release-checklist gate). The same analysis produced the fifth custody wave (event-custody-and-precedence-register.md v1.5, events E-27–E-29: marketplace account suspension, DOLE work-stoppage order, employee arrest/detention). W5552 ships **directly confirmed Tier 1** (the OSH statutory-enforcement class of the W5545 closure-order precedent — a regulator-ordered halt gated on life safety with a written-lifting reopen gate); W5550/W5551/W5553 ship **directly confirmed Tier 2** (the channel-contingency class of the W5547/W5548 precedent and the specialized employee-relations event class; the OSH inspection layer rides the Tier-1 W505/W140 canons).

> **2026-09-05 addition (regulatory-shock, platform-outage & governance-continuity gap fill, batch 17):** Six workflow-level gap fills — W5544 (Emergency Executive Succession & Decision-Rights Continuity Protocol; PA-36.1), W5545 (BIR Tax-Enforcement Suspension & Closure-Order Response (Oplan Kandado); PA-79.3), W5546 (BIR eFPS & Government-Portal Outage Filing Contingency, AAB Fallback & Penalty-Relief Documentation; PA-79.3), W5547 (Payment-Network & Acquirer Outage Response (Card Scheme / Acquirer Downtime); PA-08.1), W5548 (Stored-Value & Loyalty Platform Outage, Downtime-Acceptance & Manual-Redemption Protocol; PA-54.2), and W5549 (Suicide Attempt / Self-Harm Incident Response & Psychosocial-Aftermath Protocol; PA-24.1) — were added after the batch-16 edge-case sweep was re-run across scenario families not yet probed (governance continuity, regulatory enforcement, payment-platform failure, tender-program failure, and sensitive psychosocial incidents): the emergency executive succession ('emergency succession'/'incapacity'/'board continuity' appeared only as PA-36.2's records-update trigger "(d) death or incapacity" — no owner of the first-24-hour board mechanics, the delegation-of-authority bridge, bank/BIR signatory continuity or the disclosure clock; W178 owns only planned succession), the BIR enforcement closure event ('Oplan Kandado'/'tax suspension'/'closure order' in zero PA files — W2773 owns audit defense and W658 inspection response, neither owns the closure order that halts trading at a site), the eFPS-outage filing contingency (downtime cited as a pain point in four PA files — W590-class, PA-17.3 twice, PA-79.1 — with only a one-bullet AAB mitigation and no owner of the filing-day decision tree, evidence pack or penalty-relief documentation), the card-network/acquirer outage ('card network outage'/'card scheme outage' in zero files — W535 owns store-side offline POS and W537 the settlement cycle, but the network-side outage is a chain-wide tender-policy event with no owner), the stored-value/loyalty platform outage ('gift card system outage'/'loyalty system failure' in zero files — W2150–W2157 own the lifecycle and W3699 integrity monitoring, but the downtime-acceptance decision, manual-redemption mode and liability true-up had no owner), and the suicide/self-harm incident protocol ('suicide'/'self-harm' in zero files — W140/W1266 own the incident frameworks but not the crime-scene/witness-care/no-speculation/aftermath disciplines specific to this event class). The same analysis produced the fourth custody wave (event-custody-and-precedence-register.md v1.4, events E-23–E-26: stored-value & loyalty outage, card-network/acquirer outage, regulator-ordered suspension/closure, and key-executive incapacitation). W5545/W5546 ship **directly confirmed Tier 1** (the statutory-deadline-protection class of the W2764/W2765/W5508 filing siblings — enforcement response and filing-failure protection); W5544/W5547/W5548/W5549 ship **directly confirmed Tier 2** (the governance-continuity and platform-contingency classes of their PA siblings; the life-safety medical dimension of W5549 rides the Tier-1 W501 chain).

> **2026-09-05 addition (emergency & continuity workflow gap fill, batch 16):** Eight workflow-level gap fills — W5536 (Missing-Child / Code Adam In-Store Response Protocol; PA-07.2), W5537 (Fire Event Response, Suppression & Post-Fire BFP Clearance (Store & DC); PA-24.2), W5538 (Bomb Threat Response & Search-or-Evacuation Decision Protocol; PA-24.2), W5539 (Elevator & Escalator Entrapment Response Protocol; PA-07.2), W5540 (Payroll Run Failure, Correction & Emergency Off-Cycle Payment; PA-19.2), W5541 (Bank-Failure & Frozen-Deposit Contingency; PA-18.3), W5542 (Liquidity Stress, Covenant-Breach & Payment-Prioritization Escalation; PA-105.3), and W5543 (Price-File Integrity Event Response & Mass-Mispricing Rollback; PA-118.2) — were added after a dedicated emergency/edge-case gap analysis re-ran the §2 gap methodology at *scenario* granularity (failure modes and rare events rather than capabilities): the missing-child response (only corpus hits for 'missing child' were cart straps), the fire *event* (prevention/testing owned by W806/W1296 and the generic W330 protocol, but no suppression/BFP-clearance/reopen-gate owner), the bomb threat (a W330 classification row and a plan-template bullet only), elevator entrapment (maintenance/inspection owned, rescue not), the payroll run failure (W10/W641 own the run and planned off-cycle, not the failed run), the bank-failure event (W1474 owns steady-state counterparty limits, not the freeze event), liquidity-stress escalation (W319/W3400 own routine covenant/policy governance, not the stressed state), and the mass-mispricing event (W13/W3697/W1622 own fragments, no event owner). The same analysis produced the third custody-register wave (event-custody-and-precedence-register.md v1.3, events E-19–E-22) — fire, earthquake (W1450 named as the canon the register had never routed), armed violence (W717 vs W330 during-event command), and the mispricing event. W5536/W5537/W5538 ship **directly confirmed Tier 1** (the life-safety in-store emergency class of W330/W501/W576, each gating reopening/reunification on verified external clearance); W5539–W5543 ship **directly confirmed Tier 2** (the contingency-operations and integrity-event classes of W470/W641/W319/W3697).

> **2026-09-04 addition (demand-intake gap fill, batch 15):** One workflow-level gap fill — W5535 (Capability Demand Intake & Backlog Triage; PA-113.2, VS-113) — was added after re-running the gap methodology at workflow granularity against the end-to-end stakeholder demand cycle described in the IT operating model (OM §5.1/§7 governance) and the sourcing model (§3 gate): a BPO/executive raises a new software-capability need → the paired IT PO/PM logs it → EA triages (existing coverage vs. missing workflows vs. genuinely new value stream vs. sourcing candidate) → routing (team backlog, workflow-catalog gap-admission, or the W5515 SIB gate) → Product-Council capacity funding — the front door had no dedicated owner in any PA file ('capability demand intake'/'backlog triage'/'accepted or routed or declined' appear in zero dedicated `## W` headers — the adjacent VS-113 slices are each post-intake: W3577 portfolio rationalization, W3580 solution architecture for approved initiatives, W3588 investment-governance ROI, and the batch-7 machinery W5515–W5517 all start after intake). Ships **directly confirmed Tier 2** — the governance/lifecycle-operations class of its W5515/W5516 siblings; no statutory dimension (the front door routes and never executes statutory filings), matching the batch-7 governance precedent.

> **2026-09-04 addition (operations-workflow gap fill, batch 11):** Three workflow-level gap fills — W5532 (Workforce Time & Attendance (Biometric/Time-Clock) Platform Estate & Punch-Data Operations; PA-19.3), W5533 (BIR Form 2316 Annual Issuance, Employee Acknowledgment & Certificate Lifecycle; PA-79.2), and W5534 (Company-Property Gate Pass & Asset-Exit Control (Stores, DCs & HQ); PA-23.2) — were added after a dedicated operations-domain gap analysis (workflow-gap-analysis-operations.md) re-ran the §2 gap methodology across the four workflow-level families not yet covered by a domain pass (Plan & Source, Make & Move, Sell & Serve, Asset & Infrastructure, Governance & Assurance): the workforce time-&-attendance (biometric/time-clock) platform estate cited only as infrastructure (W561's trigger source, W586/W796's labor-metrics feed, new-store readiness's "biometric system installed"), the BIR Form 2316 annual furnishing layer generated only as W90.8/W1384.7 sub-steps, and the company-property gate-pass/asset-exit control PA-09.1 expects as a "Gate Pass Integration (Security exit clearance)" system integration each had no dedicated owner in any PA file ('time and attendance'/'timekeeping'/'biometric' = 38 PA files with zero dedicated headers, '2316' = 10 PA files / 0 dedicated headers, 'gate pass'/'property pass' = 5 PA files / 0 dedicated headers). W5533 ships **directly confirmed Tier 1** (the statutory furnishing layer of the withholding regime — the W2764/W2765 sibling class, W5508 precedent); W5532/W5534 ship **directly confirmed Tier 2** (the platform-operations class of W5525/W3351 and the physical-security control class of W1477/W1478).

> **2026-09-03 addition (IT operating-model gap fill, batch 8):** Seven workflow-level gap fills — W5518 (Collaboration & Productivity Platform (M365/Email/Teams) Operations & Tenant Governance; PA-27.2), W5519 (Enterprise Messaging & Store Telephony Services (UCC) Lifecycle; PA-27.2), W5520 (Core Network Services & IPAM (DNS/DHCP/IP-Schema) Management; PA-27.2), W5521 (Enterprise Release Calendar & Peak-Season Change-Freeze Governance; PA-27.1), W5522 (ISMS Program, Security Certification & Security-Policy Lifecycle (ISO/IEC 27001); PA-27.3), W5523 (Enterprise Pentest, Red/Purple-Team & Attack-Surface Management Program; PA-27.3), and W5524 (Enterprise DLP & Insider-Risk Monitoring (Endpoint/Email/Cloud); PA-27.3) — were added after a dedicated IT-domain gap analysis (workflow-gap-analysis-it.md) re-ran the gap methodology across all 9 Technology & Data value streams: the ~6,911-user M365/email/telephony collaboration estate, the internal core network services, the cross-estate change freeze, and the ISMS/adversarial-validation/insider-risk assurance layer each had no dedicated owner in any PA file ('Microsoft 365', 'tenant administration', 'digital workplace', 'email security', 'DMARC', 'IPAM', 'DHCP', 'change freeze', and a true-word 'ISMS' each appeared in zero dedicated `## W` headers — the adjacent VS-27 slices are each operations-generic: W366 owns WAN/ISP/Wi-Fi, W367 vulnerability ops, W387 quarterly ITGC CSA sampling, W1205 the PCI QSA cycle, W1409 the weekly CAB). Five ship **directly confirmed Tier 2** (W5518/W5520/W5521/W5522/W5524 — the infrastructure-operations and governance class of their VS-27 siblings), two ship **Tier 3** (W5519 store telephony/UCC — support-layer communications; W5523 pentest/red-team — periodic assurance), matching the batch-7 governance precedent.

> **2026-09-03 addition (sourcing-model gap fill, batch 7):** Three workflow-level gap fills — W5515 (Sourcing Decision Gate Operation & Capability Sourcing Register; PA-113.3), W5516 (Best-of-Breed Product Lifecycle Management, Vendor Release Intake & Exit Reserves; PA-113.2), and W5517 (SEP Paved Road & Engineering Standard Governance for Built Products; PA-113.1) — were added after re-running the gap methodology at workflow granularity against the rest of the 2026-09-03 hybrid capability-sourcing extension (capability-sourcing-and-engineering-model.md §3–§9, the surface the batch-6 pass's §12 scope deliberately left unexamined): the sourcing gate + Register machinery, the bought-edge lifecycle, and the build-side paved road/standard each had no dedicated owner in any PA file ('sourcing gate', 'golden path', 'paved road', 'ring deployment', 'upgrade currency', 'exit reserve', 'release intake', 'DORA', 'best-of-breed', and 'configure' each appeared in zero dedicated `## W` headers — the adjacent VS-113 slices are each strategy/portfolio-generic: W3588 owns investment-governance ROI, W3589 vendor/platform strategy direction, W3577 portfolio rationalization, W3573 architecture exceptions). All three ship **directly confirmed Tier 2** — the governance/lifecycle-operations class of their VS-113 siblings (W3588/W3589) and the batch-6 W5512–W5514 precedent; the contract-clause dimension (RA 10173 data-residency terms, statutory-readiness warranties) rides W5516's Step-3 verification gate, not a standalone statutory register, matching the W5513/W5511 sibling pattern.

> **2026-09-03 addition (agentic-AI platform gap fill, batch 6):** Three workflow-level gap fills — W5512 (Agentic Candidate Intake, Sourcing Routing & Agent Registry Registration), W5513 (Agent Shadow & Canary Evaluation, Graduation & Autonomy-Tier Ratification), and W5514 (Agent Runtime Operations, Guardrail & Kill-Switch Telemetry, Quarterly Re-Registration & Portfolio Sunset; all VS-128.3) — were added after re-running the gap methodology at workflow granularity against the 2026-09-03 Agentic-AI extension (capability-sourcing-and-engineering-model.md §12, OM v2.1 AAP team #15): the agent lifecycle (intake → SIB sourcing routing → VS-128 registration → shadow/canary evaluation → runtime operation → QBR sunset) had no dedicated owner in any PA file ('agentic', 'agent runtime', 'shadow mode', 'canary', 'kill-switch', and 'non-human identity' each appeared in zero dedicated `## W` headers — the adjacent slices are each model-generic: W3931 owns the model registry, W3946 model pre-deployment assurance, W3947 model monitoring, W3948 model retirement). All three ship **directly confirmed Tier 2** — the lifecycle-operations class of their PA-128.3 siblings (W3945–W3948), with the statutory/boundary dimension carried inside W5513's ratification gate (the hard boundaries — no statutory filings, no POS/OT, no SoD conflicts — are verification steps, not standalone statutory registers, matching the W5511 sibling pattern).

> **2026-08-26 addition (batch 5):** One further post-catalog workflow-level gap fill — W5510 (Supplier Service-Fee Billing & Account Deduction for Store-Rendered Services (Barcode Labels & Promotional Collaterals); VS-15.1) — was added after a supplier-expense-model review found the two existing recovery paths each own a different money flow (co-op funds W513/W1799 = pre-agreed campaign reimbursement; compliance chargebacks W245 = penalties for non-performance) while per-event, store-rendered services billed to the supplier's account — barcode/price-label printing, promotional-collateral production, source-tag re-application — had no owner ('service fee'/'supplier billing' appeared in zero merchandise-supplier PA files as dedicated headers; only the concessionaire analog W5507 existed, in VS-07.1); it ships **unclassified** with a keyword-driven proposed Tier 1 tier (the `barcode` core-transactional keyword, same precedent as W5507), joining W5497–W5509 in the pending-confirmation register (its settlement rides W770/W556, which are already Tier 1, so the Tier 1 proposal is recovery-integrity driven rather than go-live blocking — warrants explicit confirmation review).

> **2026-09-02 confirmation (post-catalog pass):** The fourteen post-catalog workflows W5497–W5510 were confirmed by the post-catalog confirmation pass (`07-methodology/confirm-postcatalog-14.py`), applying the calibrated rules workflow-by-workflow: **6 → Tier 1** (W5497 CODI statutory machinery; W5498 *promoted* on the RA 11165 written-agreement mandate, no-less-favorable-treatment duty and DOLE labor-standards inspection readiness; W5503 *promoted* on the DENR CCO 2013-24 90-ppm lead-cap item/goods-receipt gates, DENR EMB market-surveillance response deadlines and stop-sale machinery; W5504 *promoted* on the RA 11058/DO 252-25 foreseeable-risk duty executed as a threshold work-interruption protocol — the W576/W140 Tier-1 sibling precedent; W5505 core-transactional barcode/price-label integrity under the RA 7394 posted-tag regime; W5508 quarterly BIR 1605 FBT filing), **6 → Tier 2** (W5499/W5500/W5502/W5506 adopted at the proposed tier; W5507/W5510 *demoted* — service-fee billing and account-deduction recovery operations where the `barcode` keyword is incidental to the fee schedule), and **2 → Tier 3** (W5501 *promoted* — scenario analysis/modeling feeding W122; W5509 *demoted* — substitution-analytics core). Register 5,372 → 5,386 rows (5,349 → 5,363 unique); the proposal register is regenerated empty.

> **2026-08-26 addition (batch 4):** Two further post-catalog workflow-level gap fills — W5508 (Fringe Benefits Tax (FBT) Determination, Valuation & Quarterly BIR Form 1605 Filing; VS-79.2) and W5509 (Unfulfilled-Demand & Lost-Sales Capture, Substitution Analytics & Replenishment Feedback; VS-02.1) — were added after re-running the gap methodology at workflow granularity ('fringe benefit'/'FBT'/'1605' appeared in zero PA files as dedicated headers — only PA-144.1 flags 'BIR (fringe benefit)' as a dormitory-housing obligation with no downstream owner — and 'lost sales' appeared across 37 PA files only as a consequence/estimate, never as a captured event with an owner); both ship **unclassified** with keyword-driven proposed Tier 1 tiers (W5508 on the statutory `BIR` keyword, W5509 on the core-transactional `POS` keyword), joining W5497–W5507 in the pending-confirmation register (W5509's Tier 1 proposal in particular warrants explicit confirmation review — the capture program is an analytics-overlay capability, not a go-live transactional blocker).

> **2026-08-25 addition (batch 3):** Three further post-catalog workflow-level gap fills — W5505 (Concession Item Catalog, Barcode & Price-Label Onboarding & Governance; VS-07.1), W5506 (Concessionaire Self-Service Price Change Request, Approval & Store-Level Propagation; VS-07.1), and W5507 (Concession Service-Fee Billing & Cost Recovery for Labels, Barcode Changes & Admin Services; VS-07.1) — were added after a concessionaire-model review found W177 modeled only agreement admin and a single throughput SKU ('concession item'/'concessionaire price'/'concessionaire portal' in zero PA files as dedicated headers); all three ship **unclassified** with keyword-driven proposed tiers (W5505/W5507 Tier 1 on the `barcode` core-transactional keyword, W5506 Tier 2), joining W5497–W5504 in the pending-confirmation register (W5506's RA 7394 label-first propagation and W5507's BIR service-fee invoicing warrant explicit confirmation review).

> **2026-08-25 addition:** Two further post-catalog workflow-level gap fills — W5503 (Restricted-Substance & Chemical-Content Product Compliance — lead-in-paint per DENR CCO 2013-24, formaldehyde emission classes, VOC limits; VS-31.3) and W5504 (Extreme-Heat Work Interruption & Occupational Heat-Stress Management — DOLE heat-index advisory response; VS-24.1) — were added after re-running the gap methodology at workflow granularity ('restricted substance'/'lead in paint'/'formaldehyde' and 'heat stress'/'heat index' each appeared in zero PA files as dedicated headers); both ship **unclassified** with keyword-driven proposed Tier 2 tiers, joining W5497–W5502 in the pending-confirmation register.

> **2026-08-24 addition:** Six post-catalog workflow-level gap fills — W5497 (POSH / Safe Spaces CODI program, VS-84.2), W5498 (Telecommuting / RA 11165, VS-19.3), W5499 (Director induction & board education, VS-36.1), W5500 (Customer digital accessibility / WCAG 2.1 AA, VS-10.1), W5501 (Climate physical & transition risk assessment, VS-21.2), and W5502 (Employee financial wellness, VS-83.3) — were added after re-running the gap methodology at workflow granularity; they are currently **unclassified** with keyword-driven proposed tiers (1 Tier 1 / 5 Tier 2). Several warrant Tier 1 confirmation (statutory CODI investigation/reporting under RA 7877/RA 11313; RA 11165 written-agreement and equal-treatment execution) and will be assigned in a follow-up confirmation pass.

> **2026-06-14 addition:** Value streams VS-79 through VS-88 (240 workflows, W2753–W2992) were added covering Tax Management & BIR Statutory Reporting, Payment Operations & Acquirer Settlement, Cash-in-Transit & Armored Car Operations, Sari-Sari Store & MSME Micro-Wholesale, Occupational Health & Employee Wellness, Labor Relations & Collective Bargaining, Mandatory Discount & Tax Credit Recovery, Anti-Financial Crime (AML/KYC/ABC), Customs Trade Compliance & Tariff Optimization, and Document Control & Records Retention. These 240 workflows are currently **unclassified** (counted in the unclassified total) pending criticality review; many warrant Tier 1 classification (BIR tax filing, AML/STR reporting, CBA administration, mandatory-discount tax credit recovery, CIT operations) and will be assigned in a follow-up classification pass.
>
> **2026-06-14 addition (gap analysis Pass 1):** Value streams VS-89 through VS-92 (96 workflows, W2993–W3088) were added to fill capability gaps identified in a workflow gap analysis: VS-89 Product Recall & Safety Corrective Action Management, VS-90 Damage, Claims & Freight Recovery Management, VS-91 Consumer Data Privacy & Data Protection Program, and VS-92 Kitting, Bundling & Build-to-Order Assembly Operations. These 96 workflows are currently **unclassified** (counted in the unclassified total) pending criticality review; several warrant Tier 1 classification (product recall regulatory notification/stop-sale, DPA breach NPC 72-hour notification, freight/vendor claim notice windows, DSAR statutory fulfillment) and will be assigned in a follow-up classification pass.
>
> **2026-06-14 addition (gap analysis Pass 2):** Value streams VS-93 through VS-96 (96 workflows, W3089–W3184) were added to fill the remaining retired-number gaps and two new capability gaps: VS-93 Dark Store & Micro-Fulfillment Operations (former VS-49 gap), VS-94 Cooperative & Community Enterprise Procurement (former VS-52 gap), VS-95 Marketplace Operator & Third-Party Seller Management, and VS-96 Equipment Leasing & Capital Equipment Finance. These 96 workflows are currently **unclassified** (counted in the unclassified total) pending criticality review; several warrant Tier 1 classification (marketplace seller KYB/payout, lease credit underwriting and Truth-in-Lending disclosure, dark-store dispatch SLA for ecommerce promise, cooperative fair-trade pricing) and will be assigned in a follow-up classification pass.
>
> **2026-06-14 addition (gap analysis Pass 3):** Value streams VS-97 through VS-100 (96 workflows, W3185–W3280) were added to strengthen the previously-thinnest operating families: VS-97 Corporate Real Estate & Property Portfolio Management, VS-98 Contingent, Contract & Outsourced Workforce Management, VS-99 IT Asset & Technology Lifecycle Management, and VS-100 Legal Operations, Litigation & IP Management. These 96 workflows are currently **unclassified** (counted in the unclassified total) pending criticality review; several warrant Tier 1 classification (intercompany rent transfer-pricing benchmarking, DOLE D.O. 174 labor-only-contracting compliance, software license compliance-audit response, litigation loss-contingency accrual under PFRS/IAS 37) and will be assigned in a follow-up classification pass.
>
> **2026-06-14 addition (gap analysis Pass 4):** Value streams VS-101 through VS-104 (96 workflows, W3281–W3376) were added to strengthen the three thinnest operating families (People +2; Plan & Source +1; Governance & Assurance +1): VS-101 Merchandise Financial Planning, OTB & Margin Management, VS-102 Compensation, Benefits & Total Rewards Strategy, VS-103 HR Shared Services, Employee Experience & People Analytics, and VS-104 Government Affairs, Public Policy & Industry Relations. These 96 workflows are currently **unclassified** (counted in the unclassified total) pending criticality review; several warrant Tier 1 classification (open-to-buy/markdown-budget governance, pay-equity analysis and minimum-wage compliance, multi-entity statutory-benefits remittance governance, political-activity/anti-bribery compliance in government affairs) and will be assigned in a follow-up classification pass.

---

## Previously Unclassified Workflows — Now Classified

> The following 681 workflows (previously listed as "additional batch workflows unclassified")
> have been classified by value stream context, process area, and operational criticality.
> Classification: **284 Tier 1** (core) · **293 Tier 2** (support) · **104 Tier 3** (optimization).

### Tier 1 Additions (422 Workflows)

#### Plan & Source

| ID | Workflow | Value Stream |
|---|---|---|
| W558 | Supplier Risk Assessment & Supply Disruption Contingency Planning | Supply Planning |
| W596 | Store-Level Replenishment Exception Management & Auto-Override | Supply Planning |
| W680 | Supply Chain Cost Analysis & Logistics Optimization Review | Supply Planning |
| W727 | Carrier & Freight Forwarder Daily Performance Monitoring | Supply Planning |
| W729 | Supply Chain Disruption Rapid Response & Escalation Protocol | Supply Planning |
| W762 | Carrier Performance Weekly Review & Freight Rate Benchmarking | Supply Planning |
| W763 | Supply Chain Vendor Diversification & Alternative Sourcing Maintenance | Supply Planning |
| W835 | Store-Level Replenishment Forecast Accuracy Review & Parameter Tuning | Supply Planning |
| W921 | Store-Level Emergency Local Sourcing & Alternative Vendor Activation | Supply Planning |
| W1006 | Vendor Purchase Order ASN Reconciliation & Discrepancy Resolution | Vendor Management & Procurement |
| W1020 | Vendor Consignment Inventory Physical Count & Periodic Reconciliation | Vendor Management & Procurement |
| W1026 | Vendor Product Discontinuation Notification & Last-Time Buy Management | Vendor Management & Procurement |
| W1038 | Vendor Catalog Synchronization & Product Information Quality Audit | Vendor Management & Procurement |
| W1137 | Vendor Purchase Order Line-Level Partial Shipment Acceptance & Backorder Management | Vendor Management & Procurement |
| W593 | Vendor Portal Content Management & Self-Service Operations | Vendor Management & Procurement |
| W620 | Vendor Due Diligence & Onboarding Site Visit Management | Vendor Management & Procurement |
| W632 | Competitive Bidding & Tender Management | Vendor Management & Procurement |
| W633 | Purchase Price Variance (PPV) Analysis & Cost Management | Vendor Management & Procurement |
| W669 | Vendor Contract Compliance Monitoring & Enforcement | Vendor Management & Procurement |
| W670 | Supplier Emergency Onboarding & Rapid Activation | Vendor Management & Procurement |
| W671 | Commodity Price Monitoring & Procurement Strategy | Vendor Management & Procurement |
| W760 | Vendor-Specific Commodity Price Index Tracking & Procurement Trigger Management | Vendor Management & Procurement |
| W818 | Vendor Insurance Certificate & Compliance Documentation Tracking | Vendor Management & Procurement |
| W819 | Vendor Quality Incoming Inspection Failure & Material Review Board (MRB) | Vendor Management & Procurement |
| W866 | Vendor Self-Service Purchase Order Acknowledgment & Confirmation | Vendor Management & Procurement |
| W867 | Vendor Self-Service Invoice Submission & Payment Status Inquiry | Vendor Management & Procurement |
| W870 | Vendor Compliance Document Upload & Expiration Tracking | Vendor Management & Procurement |
| W915 | Vendor Product Packaging Sustainability Assessment & Compliance Management | Vendor Management & Procurement |
| W938 | Vendor Managed Inventory (VMI) Periodic Data Accuracy Audit & Reconciliation | Vendor Management & Procurement |
| W959 | Vendor Rebate Volume Tier Compliance Reconciliation & Shortfall Processing | Vendor Management & Procurement |
| W962 | Vendor-Sponsored In-Store Display Compliance Audit & Chargeback | Vendor Management & Procurement |
| W5229 | Custom Order Pro-Forma Invoice Generation and Downpayment Collection | B2B Bulk-Project Custom Import |
| W5235 | Shipping Document Receipt Discrepancy Auditing and Bank Release | B2B Bulk-Project Custom Import |
| W5236 | Bank Trust Receipt Financing Execution for Indent Orders | B2B Bulk-Project Custom Import |
| W5238 | Import Duties Excise Tax and 12 Percent VAT Payment Processing | B2B Bulk-Project Custom Import |
| W5239 | Bureau of Customs Formal Entry Filing and Single Administrative Document Release | B2B Bulk-Project Custom Import |
| W5240 | Port Drayage Scheduling and Direct Container Delivery Mobilization | B2B Bulk-Project Custom Import |
| W5243 | Direct Delivery Container Devanning and Joint Quantity Survey at Jobsite | B2B Bulk-Project Custom Import |
| W5245 | Progressive Project Billing and Milestone Payment Collection | B2B Bulk-Project Custom Import |
| W5246 | Landed Cost Reconciliation and Arm's-Length Transfer Price Accounting | B2B Bulk-Project Custom Import |

#### Make & Move

| ID | Workflow | Value Stream |
|---|---|---|
| W1029 | DC-Level Temperature, Humidity & Environmental Monitoring for Sensitive Goods | DC & Warehouse Operations |
| W1041 | DC-Level Outbound Quality Sampling & Pre-Shipment Inspection | DC & Warehouse Operations |
| W585 | DC Dock Scheduling & Appointment Management | DC & Warehouse Operations |
| W649 | DC Safety Operations & Compliance | DC & Warehouse Operations |
| W681 | DC Quality Control & Vendor Compliance Inspection at Receiving | DC & Warehouse Operations |
| W785 | Vendor Returnable Transport Packaging Reconciliation & Settlement | DC & Warehouse Operations |
| W514 | Inventory Count Reconciliation & Variance Root Cause Analysis | Inventory Lifecycle |
| W587 | Inventory Obsolescence Identification & Write-Off Management | Inventory Lifecycle |
| W653 | Fleet Accident & Incident Management | Logistics & Fleet |
| W799 | Vehicle Acquisition, Registration, Insurance & Disposal Lifecycle Management | Logistics & Fleet |
| W5181 | DC Emergency Staging Zone Allocation & Fast-Track Pick Operations | Disaster Relief Supply Chain Logistics |
| W5186 | ERP Price Freeze Configuration & Store-Level Price Lock Execution | Disaster Relief Supply Chain Logistics |
| W5187 | Department of Trade and Industry (DTI) Price Compliance Reporting | Disaster Relief Supply Chain Logistics |
| W5188 | Price Freeze Audit, Margin Impact Analysis & Financial Provisioning | Disaster Relief Supply Chain Logistics |
| W5189 | Anti-Hoarding & Quantity-Limit Rules POS Configuration | Disaster Relief Supply Chain Logistics |
| W5190 | State of Calamity LGU Regulatory Permit Clearance & Fee Deferrals | Disaster Relief Supply Chain Logistics |
| W5191 | Emergency Import Tariffs/Customs Duty Deferral Application | Disaster Relief Supply Chain Logistics |
| W5192 | Disaster Tax Relief & BIR Casualty Loss Deduction Certification | Disaster Relief Supply Chain Logistics |
| W5197 | Disaster Area Store Reopening Safety Clearance & Structural Integrity Audit | Disaster Relief Supply Chain Logistics |
| W5199 | Humanitarian Delivery Cash Reconciliation & Driver Safety Vetting | Disaster Relief Supply Chain Logistics |
| W5200 | Post-Disaster Supply Chain Recovery, Lessons-Learned & BCP Update | Disaster Relief Supply Chain Logistics |
| W5443 | Job Site Cleanup Pre-Job Hazard & Regulated-Material Assessment | Construction Debris & Site Cleanup |
| W5445 | Skip/Dumpster & Container Fleet Sourcing, Placement & LGU Permit | Construction Debris & Site Cleanup |
| W5447 | Subcontractor Hauler & Accredited-Disposer Vendor Onboarding | Construction Debris & Site Cleanup |
| W5450 | Demolition Debris Load-Out, Dust/Noise & Neighbor Management | Construction Debris & Site Cleanup |
| W5452 | DENR-Compliant C&D Transporter Permitting & Hauling Manifest | Construction Debris & Site Cleanup |
| W5454 | Hazardous / Regulated Debris Discovery & Rerouting During Cleanup | Construction Debris & Site Cleanup |
| W5456 | Hauling Safety, Spill Response & Road/Route Compliance | Construction Debris & Site Cleanup |
| W5460 | ESG, GRI/IRIS+ & Decarbonization Reporting Feed | Construction Debris & Site Cleanup |
| W5463 | DENR/LGU Periodic Waste Reporting & Permit Evidence | Construction Debris & Site Cleanup |

#### Sell & Serve

| ID | Workflow | Value Stream |
|---|---|---|
| W1003 | Store-Level Paint Mixing Station Daily Cleaning, Calibration & Waste Disposal | Store Operations |
| W1005 | Store-Level Shelf Stock Rotation & Paint/Chemical Expiry Monitoring | Store Operations |
| W1008 | Store-Level Power Tool Battery Charging Station Safety & Maintenance | Store Operations |
| W1010 | Store-Level Outdoor Garden Center Weather Protection & Seasonal Display Setup | Store Operations |
| W1012 | Store-Level Hazardous Material Spill Kit Inspection & Restocking | Store Operations |
| W1015 | Store-Level Forklift & Heavy Equipment Daily Safety Check & Log | Store Operations |
| W1019 | Store-Level Construction Material Safety Data Sheet (SDS) Customer Access & Compliance | Store Operations |
| W1021 | Store-Level Loading Dock Equipment Maintenance & Safety Inspection | Store Operations |
| W1023 | Store-Level Post-Typhoon Damage Assessment, Cleanup & Rapid Reopening | Store Operations |
| W1025 | Store-Level Shelving, Racking & Display Fixture Safety Inspection & Maintenance | Store Operations |
| W1028 | Store-Level Shopping Cart, Basket & Customer Equipment Inventory Management | Store Operations |
| W1030 | Multi-Store District Manager Weekly Operations Review & Compliance Audit | Store Operations |
| W1037 | Store-Level Annual Physical Inventory Preparation, Execution & Variance Resolution | Store Operations |
| W1040 | Store-Level Customer Parking Lot Traffic Safety & Exterior Facility Management | Store Operations |
| W1047 | Store-Level Rainy Season Floor Safety, Anti-Slip Mat & Entrance Canopy Management | Store Operations |
| W1051 | Store-Level Fire Extinguisher Monthly Inspection, Annual Recharge & BFP Compliance | Store Operations |
| W1070 | Store-Level Customer Building Permit Documentation Package Preparation Assistance | Store Operations |
| W1125 | Store-Level Seasonal Typhoon Pre-Positioning & Emergency Stock Buffer Management | Store Operations |
| W1156 | Store-Level Customer Construction Site Safety Equipment Rental & Delivery | Store Operations |
| W497 | PWD Accessibility Compliance & Store Facilities Audit | Store Operations |
| W501 | Store-Level First Aid & Medical Emergency Response | Store Operations |
| W502 | Store-Level Non-Hazardous Waste Management | Store Operations |
| W554 | Store-Level Daily Shelf Replenishment & Restocking | Store Operations |
| W559 | Store-Level Non-Emergency Incident & Hazard Reporting | Store Operations |
| W562 | Store-Level Loss Prevention Daily Routine | Store Operations |
| W571 | Store-Level Daily Communication & Memo Acknowledgment | Store Operations |
| W573 | Store-Level Daily Planogram Execution & Shelf Compliance Check | Store Operations |
| W574 | Store-Level Daily Closing Procedure | Store Operations |
| W576 | Store-Level Typhoon & Severe Weather Preparedness Protocol | Store Operations |
| W579 | Store-Level Daily Equipment & Specialized Fixture Safety Check | Store Operations |
| W580 | Store-Level Emergency Manual Operations Protocol (Total System/Power Failure) | Store Operations |
| W582 | Store-Level Fire Drill Execution & Documentation | Store Operations |
| W601 | Store-Level Daily HR Operations & People Management | Store Operations |
| W603 | Store-Level Employee Disciplinary Process & DOLE Due Process Compliance | Store Operations |
| W666 | Store-Level Inventory Receiving Quality Control | Store Operations |
| W667 | Store-Level Price Verification & Daily Compliance Operations | Store Operations |
| W720 | Store-Level Daily Safety Briefing & Toolbox Talk | Store Operations |
| W721 | Store-Level Vendor Promodizer Floor Activity Coordination & Compliance | Store Operations |
| W739 | Store-Level Daily Huddle & Morning Team Briefing | Store Operations |
| W741 | Store-Level Fuel Inventory & Backup Generator Management | Store Operations |
| W743 | Store-Level Daily Cleaning & Sanitation Checklist Execution | Store Operations |
| W771 | Store-Level BOPIS Order Aging & Abandoned Pickup Processing | Store Operations |
| W958 | Store-Level Daily Cash Variance Threshold Monitoring & Exception Escalation | Store Operations |
| W517 | POS Cashier Shift Handover & Drawer Accountability | POS & Checkout |
| W519 | POS Suspicious Transaction & AML Compliance Reporting | POS & Checkout |
| W520 | Age-Restricted Product Verification & Compliance at POS | POS & Checkout |
| W521 | POS Transaction Suspend, Park & Recall | POS & Checkout |
| W522 | POS Daily Transaction Review & Cashier Performance Audit | POS & Checkout |
| W525 | POS Continuous Near-Real-Time Sync & Nightly Reconciliation | POS & Checkout |
| W527 | POS Tax Exemption Processing (Government / PEZA / Institutional) | POS & Checkout |
| W528 | POS Digital Receipt / E-Receipt Delivery | POS & Checkout |
| W529 | POS Void & Refund Tiered Authorization | POS & Checkout |
| W530 | POS High-Value Transaction Documentation & Customer ID | POS & Checkout |
| W531 | POS Bagging, Carry-Out & Bag Fee Compliance | POS & Checkout |
| W532 | POS Clearance & "Final Sale" Item Processing | POS & Checkout |
| W533 | POS Real-Time Event Streaming & Continuous Sync | POS & Checkout |
| W534 | Multi-Origin / Mixed-Basket Fulfillment Orchestration | POS & Checkout |
| W535 | POS Offline Capability Scope & Local Operations | POS & Checkout |
| W536 | Unified Order Management & Cross-Channel Fulfillment Routing | POS & Checkout |
| W749 | POS Heavy Equipment & Power Tool Safety Acknowledgment & Release Processing | POS & Checkout |
| W1056 | Store-Level Customer Construction Permit Advisory & Municipal Building Requirements Guidance | In-Store Customer Services |
| W1062 | Store-Level Customer Scaffolding Rental, Safety Harness Package & Delivery Service | In-Store Customer Services |
| W1067 | Store-Level Customer Fire Suppression System Design & Product Recommendation | In-Store Customer Services |
| W1080 | Store-Level Customer Construction Scaffold & Ladder Safety Consultation | In-Store Customer Services |
| W1098 | Customer Emergency Home Repair Quick-Fix Bundle Curation & Package Service | In-Store Customer Services |
| W1104 | Customer Tool Rental Return Damage Assessment & Billing | In-Store Customer Services |
| W1138 | Customer Construction Worker Safety Gear Bundle Recommendation & Compliance Package | In-Store Customer Services |
| W1144 | Store-Level Customer Hazardous Material Transport Regulation Advisory | In-Store Customer Services |
| W1154 | Store-Level Customer Paint VOC & Indoor Air Quality Compliance Advisory | In-Store Customer Services |
| W827 | Store-Level Building Material Load Calculation & Safety Advisory | In-Store Customer Services |
| W913 | Store-Level Emergency Generator Fuel Reserve Management & DOE Compliance | In-Store Customer Services |
| W1013 | E-Commerce Last-Mile Delivery Partner Performance Weekly Review | Ecommerce & Digital Channels |
| W1034 | Customer Ecommerce Payment Failure Recovery, Retry & Abandoned Checkout Rescue | Ecommerce & Digital Channels |
| W1155 | Customer Ecommerce Same-Day / Express Delivery Operations | Ecommerce & Digital Channels |
| W509 | Ecommerce Product Return Inspection, Grading & Disposition | Ecommerce & Digital Channels |
| W591 | E-Commerce Fulfillment SLA Monitoring & Exception Escalation | Ecommerce & Digital Channels |
| W592 | E-Commerce Customer Delivery Tracking & Proof of Delivery Management | Ecommerce & Digital Channels |
| W659 | Ecommerce Platform Incident Management | Ecommerce & Digital Channels |
| W724 | Marketplace Channel Daily Operations & Order Management (Lazada/Shopee) | Ecommerce & Digital Channels |
| W725 | Ecommerce Platform Daily Health Monitoring & Performance Dashboard | Ecommerce & Digital Channels |
| W829 | Customer Ecommerce Order Split & Partial Delivery Proactive Communication | Ecommerce & Digital Channels |
| W899 | Customer Bulk/Project Delivery Scheduling & Multi-Drop Coordination (B2C) | Ecommerce & Digital Channels |
| W809 | Wholesale Consignment Inventory Management & Settlement | Trade, Project & Wholesale |
| W600 | Service Contractor Accreditation & Onboarding Management | Installation & Services |
| W560 | Customer Account Dormancy Identification & Deactivation | Customer Experience & Loyalty |
| W597 | Customer Complaint Escalation Matrix & Resolution SLA Tracking | Customer Experience & Loyalty |
| W617 | B2B Customer Success & Quarterly Business Review Operations | Customer Experience & Loyalty |
| W619 | Customer Account Merge & Deduplication Request Processing | Customer Experience & Loyalty |
| W660 | Service Recovery & Customer Retention Program | Customer Experience & Loyalty |
| W675 | Customer Data Platform Daily Operations & Data Quality Management | Customer Experience & Loyalty |
| W996 | Store-Level Contractor Loyalty Tier Upgrade & VIP Retention Program Management | Customer Experience & Loyalty |
| W5298 | Cooperative Board Resolution Collection & KYC Vetting | B2B Cooperative Credit & Procurement |
| W5299 | Cooperative Development Authority (CDA) Status Verification | B2B Cooperative Credit & Procurement |
| W5302 | Cooperative Group Credit Limit Allocation & System Activation | B2B Cooperative Credit & Procurement |
| W5304 | Annual Cooperative Account Credit Limit Review & Renewal | B2B Cooperative Credit & Procurement |
| W5305 | Cooperative Member Digital POS Account Association & Verification | B2B Cooperative Credit & Procurement |
| W5306 | Cooperative Member Authorization and Purchase Order Match | B2B Cooperative Credit & Procurement |
| W5307 | Real-time Credit Line Availability Check at Checkout | B2B Cooperative Credit & Procurement |
| W5309 | Credit Billing to Central Cooperative Account and Invoice Dispatch | B2B Cooperative Credit & Procurement |
| W5315 | Cooperative Patronage Dividend Tax Certification & Accounting | B2B Cooperative Credit & Procurement |
| W5335 | Equipment Rental Billing, Deposit/Hold Management & Settlement | Construction Equipment Rental Fleet |
| W5338 | Equipment Breakdown, Field Service Dispatch & Substitute Unit Provisioning | Construction Equipment Rental Fleet |
| W5339 | Equipment LTO/LTFRB Registration, Crane/Rigging Permit & Roadworthiness Compliance | Construction Equipment Rental Fleet |
| W5340 | Operator Safety Compliance, DOLE-OSH Equipment Certification & Plant-Equipment Logbook | Construction Equipment Rental Fleet |
| W5341 | Equipment Rental Accident, Injury & Third-Party Damage Incident Management | Construction Equipment Rental Fleet |
| W5344 | Cross-Store Equipment Rebalancing, Inter-DC Transport & Demand Seasonality Planning | Construction Equipment Rental Fleet |

#### Finance

| ID | Workflow | Value Stream |
|---|---|---|
| W486 | Related Party Transaction Disclosure & Reporting (PAS 24) | Procure-to-Pay |
| W487 | Revenue Recognition Review (PFRS 15 Complex Scenarios) | Procure-to-Pay |
| W488 | Credit Card Chargeback Dispute Management | Procure-to-Pay |
| W498 | Vendor Advance Payment & Prepayment Management | Procure-to-Pay |
| W499 | BIR Percentage Tax Computation & Payment | Procure-to-Pay |
| W556 | AP Payment Run & Batch Processing Execution | Procure-to-Pay |
| W611 | Payment Gateway Daily Operations & Settlement Monitoring | Procure-to-Pay |
| W634 | Revenue Assurance & POS Revenue Reconciliation | Procure-to-Pay |
| W635 | PFRS 16 Lease Accounting Operations | Procure-to-Pay |
| W640 | Merchant Fee Analysis & Payment Cost Optimization | Procure-to-Pay |
| W662 | AP Aging Management & Vendor Payment Prioritization | Procure-to-Pay |
| W713 | Corporate Credit Card Program Management & Expense Reconciliation | Procure-to-Pay |
| W750 | Credit Card Installment Sales Reconciliation & Bank Settlement Processing | Procure-to-Pay |
| W751 | Store-Level Emergency Cash Float Request & Expedited Replenishment | Procure-to-Pay |
| W752 | Intercompany Management Fee Allocation & Monthly Billing | Procure-to-Pay |
| W764 | Store-Level Daily Opening Safe Count & Cash Float Preparation | Procure-to-Pay |
| W765 | Multi-Entity Consolidation Monthly Execution & Elimination Processing | Procure-to-Pay |
| W766 | Customer Credit Note Aging Management & Unredeemed Credit Write-Off | Procure-to-Pay |
| W767 | Vendor Rebate Claim Filing & Settlement Documentation Processing | Procure-to-Pay |
| W768 | BIR VAT Refund Claim Processing & Input VAT Recovery | Procure-to-Pay |
| W769 | Customer Overpayment Detection & Refund Processing | Procure-to-Pay |
| W813 | AP Vendor Invoice Duplicate Detection & Resolution | Procure-to-Pay |
| W814 | Credit Card Settlement Exception & Chargeback Recovery Processing | Procure-to-Pay |
| W919 | Intercompany Inventory Movement Accounting & Goods-in-Transit Reconciliation | Procure-to-Pay |
| W939 | Customer Store Credit Expiration Management & Unclaimed Credit Processing | Procure-to-Pay |
| W572 | Customer Credit Monitoring & Automated Alert Management | Order-to-Cash |
| W663 | Customer Credit Portfolio Periodic Review & Collection Strategy | Order-to-Cash |
| W81 | Bad Debt Provisioning, Write-Off & Recovery | Order-to-Cash |
| W812 | Customer Credit Field Collection Operations & Legal Escalation | Order-to-Cash |
| W886 | Customer Credit Application Processing & Scoring | Order-to-Cash |
| W887 | Customer Credit Limit Review, Adjustment & Approval | Order-to-Cash |
| W888 | Customer Credit Hold Management & Order Blocking | Order-to-Cash |
| W889 | Customer AR Aging Analysis & Collection Prioritization | Order-to-Cash |
| W890 | Customer Collection Call Execution & Promise Tracking | Order-to-Cash |
| W891 | Customer Bad Debt Write-Off Proposal & Approval | Order-to-Cash |
| W893 | Customer Credit Scorecard Annual Review & Portfolio Analysis | Order-to-Cash |
| W14 | Intercompany Transactions & Settlement | Record-to-Report |
| W39 | Fixed Asset Disposal & Retirement | Record-to-Report |
| W407 | Corporate Income Tax — Computation & Deferred Tax (PAS 12) | Record-to-Report |
| W481 | SEC Reportorial Requirements Compliance (GIS, AFS, MC 28) | Record-to-Report |
| W590 | Monthly Tax Provision & Compliance Review | Record-to-Report |
| W612 | Intercompany Rate Setting & Quarterly Transfer Pricing Review | Record-to-Report |
| W636 | Standardized Balance Sheet Account Reconciliation | Record-to-Report |
| W637 | Financial Controls Testing & Monitoring | Record-to-Report |
| W638 | Period-End Journal Entry Review & Approval | Record-to-Report |
| W661 | Fixed Asset Depreciation Run & Component Accounting Operations | Record-to-Report |
| W70 | Credit Note & Debit Note Aging Reconciliation | Record-to-Report |
| W711 | BIR Withholding Tax (EWT) Certificate Form 2307 Issuance to Vendors | Record-to-Report |
| W873 | Product Safety Incident Triage & Recall Risk Assessment | Record-to-Report |
| W874 | Product Recall Customer Notification Campaign Execution | Record-to-Report |
| W875 | Product Recall Inventory Quarantine, Hold & Disposition | Record-to-Report |
| W876 | Product Recall Regulatory Reporting & DTI/BIR/FDA Compliance | Record-to-Report |
| W877 | Product Recall Vendor Recovery & Cost Reimbursement | Record-to-Report |
| W878 | Product Recall Effectiveness Audit & Close-Out | Record-to-Report |
| W589 | Weekly Cash Flow Forecast & Treasury Planning | Treasury & Cash |
| W664 | Cash Flow Variance Analysis & Liquidity Stress Testing | Treasury & Cash |
| W80 | FX Hedging & Forward Contract Management | Treasury & Cash |
| W5202 | Project Purchase Order Matching & Contract Price Alignment | B2B Project Financing & Escrow |
| W5205 | Project Credit Limit Allocation & Temporary Excess Approval | B2B Project Financing & Escrow |
| W5208 | Project Onboarding Compliance Check (Anti-Money Laundering & Sanctions) | B2B Project Financing & Escrow |
| W5209 | Project Material Goods Delivery Receipt (DR) Matching & Verification | B2B Project Financing & Escrow |
| W5213 | Escrow Draw Fund Settlement Tracking, Cash Application & Match Reconciliation | B2B Project Financing & Escrow |
| W5218 | Unconditional Progress Waiver of Lien Issuance (upon Fund Settlement) | B2B Project Financing & Escrow |
| W5219 | Project Material Return, Credit Note & Reconciliation with Escrow draws | B2B Project Financing & Escrow |
| W5224 | Project Account Financial Close, Final Waiver of Lien & Release of Escrow | B2B Project Financing & Escrow |
| W5372 | Dealer Inventory Collateral Verification, Floor-Plan Audit & Stocking-List Reconciliation | Trade Reseller Floor-Plan Financing |
| W5376 | BSP/SEC Lending-Company Compliance, Disclosure & Truth-in-Lending (RA 3765) Setup | Trade Reseller Floor-Plan Financing |
| W5378 | Floor-Plan Disbursement to Vendor, Dual-Payee Check & Supplier Settlement | Trade Reseller Floor-Plan Financing |
| W5381 | Dealer Stocking-List Audit, Physical Inventory Verification & Field Examination | Trade Reseller Floor-Plan Financing |
| W5384 | Dealer Payment Processing, Cash Application & Loan Account Reconciliation | Trade Reseller Floor-Plan Financing |
| W5386 | Dealer Collection, Workout, Restructuring & Skip-Tracing for Missing Collateral | Trade Reseller Floor-Plan Financing |
| W5388 | Floor-Plan Portfolio Risk Rating, Concentration & Dealer Credit Limit Review | Trade Reseller Floor-Plan Financing |
| W5392 | Regulatory Reporting, BSP Compliance Examination & Internal Audit Support | Trade Reseller Floor-Plan Financing |
| W5400 | BSP/SEC Compliance, Truth-in-Lending & Assignment-Notification Legal Setup | Trade Receivables Factoring |
| W5402 | Factor Funding/Drawdown, Advance Posting & Bank Reconciliation | Trade Receivables Factoring |
| W5404 | Lockbox/Cash Receipt Processing, Customer Payment Matching & Clearing | Trade Receivables Factoring |
| W5406 | Dilution Reconciliation, Reserve Release & Holdback Settlement | Trade Receivables Factoring |
| W5409 | Factor/Funder Reconciliation, Fee/Interest Settlement & Monthly Account Statement | Trade Receivables Factoring |
| W5415 | Internal Controls, Audit & Regulatory Examination Support | Trade Receivables Factoring |

#### People

| ID | Workflow | Value Stream |
|---|---|---|
| W1001 | Store-Level Employee Performance-Based Profit Sharing & Incentive Bonus Management | Hire-to-Retire |
| W1032 | Employee Overtime Pre-Approval, Monitoring & DOLE Weekly Cap Enforcement | Hire-to-Retire |
| W494 | Employee Wellness & Mental Health Program Management | Hire-to-Retire |
| W512 | Store-Level Health & Safety Committee Operations | Hire-to-Retire |
| W561 | Employee Attendance Exception Management | Hire-to-Retire |
| W594 | Store-Level Employee Daily Attendance Verification & Exception Processing | Hire-to-Retire |
| W628 | Employee Exit Interview & Attrition Analysis | Hire-to-Retire |
| W629 | Store-Level Employee Engagement Survey & Action Planning | Hire-to-Retire |
| W630 | Employee Recognition & Rewards Program Management | Hire-to-Retire |
| W642 | HMO & Private Benefits Administration | Hire-to-Retire |
| W643 | Final Pay Computation & Separation Settlement | Hire-to-Retire |
| W644 | 13th Month Pay Reconciliation & Compliance | Hire-to-Retire |
| W645 | Strategic Workforce Planning | Hire-to-Retire |
| W646 | HR Service Desk Operations | Hire-to-Retire |
| W647 | Employee Data Privacy Compliance Operations | Hire-to-Retire |
| W682 | Employee Career Development & Internal Job Posting Operations | Hire-to-Retire |
| W716 | Internal Communication & Company-Wide Announcement Management | Hire-to-Retire |
| W717 | Workplace Violence Prevention & Response Protocol | Hire-to-Retire |
| W718 | Employee Relocation & Housing Assistance Management | Hire-to-Retire |
| W719 | Diversity, Equity & Inclusion (DEI) Program Management | Hire-to-Retire |
| W753 | Store-Level Employee Meal Break & Rest Period Scheduling & DOLE Compliance | Hire-to-Retire |
| W755 | Store-Level Employee Internal Theft Prevention Awareness & Compliance Daily Operations | Hire-to-Retire |
| W777 | Employee Leave Balance Management & Annual Leave Carry-Forward Processing | Hire-to-Retire |
| W778 | Employee Benefits Annual Open Enrollment & Plan Selection Management | Hire-to-Retire |
| W780 | Store-Level Employee Uniform & PPE Periodic Issuance & Replacement Processing | Hire-to-Retire |
| W815 | Employee Business Travel Request, Approval & Expense Management | Hire-to-Retire |
| W816 | Multi-Entity Payroll Consolidation & Cross-Entity Reconciliation | Hire-to-Retire |
| W817 | Employee Sabbatical, Study Leave & Secondment Management | Hire-to-Retire |
| W956 | Employee Annual Physical Examination & Occupational Health Clearance Management | Hire-to-Retire |
| W957 | Employee Tuition Assistance & Educational Advancement Program Management | Hire-to-Retire |
| W973 | Employee Long Service Award & Milestone Recognition Management | Hire-to-Retire |
| W977 | Employee Retirement Benefit Fund (RA 7641) Administration & Processing | Hire-to-Retire |
| W994 | Employee Typhoon Disaster Relief Emergency Assistance & No-Interest Loan Program | Hire-to-Retire |
| W5249 | TESDA DTS Dual Training Accreditation and Site Inspection | DTS & TESDA Partnership |
| W5260 | Trainee Incident Management OHS Violations and Safety Escalation | DTS & TESDA Partnership |
| W5265 | DTS Allowance Stipend Calculation Payroll Matching and Disbursement | DTS & TESDA Partnership |
| W5266 | DTS Training Expense Accounting and BIR Deduction Ledgers Setup | DTS & TESDA Partnership |
| W5267 | Monthly TESDA Compliance Report Compilation and Submission | DTS & TESDA Partnership |
| W5268 | TVI Monthly Administrative Billing and Expense Sharing Reconciliation | DTS & TESDA Partnership |
| W5269 | BIR Certificate of DTS Training Expense Audit | DTS & TESDA Partnership |
| W5272 | Annual DTS Tax Savings Computation and Assessment Records | DTS & TESDA Partnership |

#### Asset & Infrastructure

| ID | Workflow | Value Stream |
|---|---|---|
| W5131 | Real Property Tax (RPT) Arrears Investigation & Settlement | Landbanking & Site Acquisition |
| W5132 | Extrajudicial Settlement (EJS) of Estate Negotiation & Heir Consent | Landbanking & Site Acquisition |
| W5136 | Land Title Consolidation & Subdivision (Subdivision of Lots) | Landbanking & Site Acquisition |
| W5137 | Department of Agrarian Reform (DAR) Clearance & Exemption Application | Landbanking & Site Acquisition |
| W5138 | National Commission on Indigenous Peoples (NCIP) Ancestral Domain Verification | Landbanking & Site Acquisition |
| W5139 | Free, Prior, and Informed Consent (FPIC) Assessment & Tribal Council Negotiation | Landbanking & Site Acquisition |
| W5140 | Certificate of Non-Overlap (CNO) Application & Boundary Survey | Landbanking & Site Acquisition |
| W5142 | Land Use Conversion Order Application (DAR Central/Regional level) | Landbanking & Site Acquisition |
| W5143 | Tenant Farmer Compensation, Settlement & Relocation Governance | Landbanking & Site Acquisition |
| W5144 | DENR Environmental Compliance Certificate (ECC) / CNC Application for New Sites | Landbanking & Site Acquisition |
| W5146 | BuildRight Property Management intercompany Lease Structuring & Transfer Pricing | Landbanking & Site Acquisition |
| W5149 | LGU Locational Clearance & Zoning Permit Application | Landbanking & Site Acquisition |
| W5278 | Insurance Settlement Negotiation and Recovery Accounting | Post-Disaster Store Reconstruction |
| W5286 | LGU Building Official Inspections and Structural Safety Clearance | Post-Disaster Store Reconstruction |
| W5287 | Bureau of Fire Protection BFP FSIC Re-Certification | Post-Disaster Store Reconstruction |
| W5289 | Temporary Container Sales Office Site Selection and Setup | Post-Disaster Store Reconstruction |
| W5290 | Mobile POS Terminal Routing and Network Activation | Post-Disaster Store Reconstruction |
| W5291 | Temporary Utility Connection and Safety Accreditation | Post-Disaster Store Reconstruction |
| W5292 | Emergency Vault and Cash Staging Security Setup | Post-Disaster Store Reconstruction |
| W5293 | LGU Temporary Selling Permit Application and Zoning Variance | Post-Disaster Store Reconstruction |

#### Governance & Assurance

| ID | Workflow | Value Stream |
|---|---|---|
| W448 | LGU Sanitary & Health Permit Management | Compliance & Regulatory |
| W468 | DTI Price Freeze / Emergency Price Control Implementation (RA 7581) | Compliance & Regulatory |
| W483 | DOLE Drug-Free Workplace Program Compliance | Compliance & Regulatory |
| W485 | BIR Branch Registration & RDO Transfer Management | Compliance & Regulatory |
| W505 | DOLE Labor Inspection Response Protocol | Compliance & Regulatory |
| W506 | Unified Regulatory Compliance Calendar & Dashboard | Compliance & Regulatory |
| W656 | Anti-Bribery & Anti-Corruption (ABAC) Compliance Program | Compliance & Regulatory |
| W657 | Regulatory Change Management & Impact Assessment | Compliance & Regulatory |
| W658 | General Regulatory Inspection Response Protocol | Compliance & Regulatory |
| W730 | Anti-Money Laundering (AML) Compliance Program Operations | Compliance & Regulatory |
| W731 | Consumer Act (RA 7394) Compliance Monitoring & Enforcement | Compliance & Regulatory |
| W732 | Vendor Tax Compliance Monitoring & BIR TIN Validation | Compliance & Regulatory |
| W834 | Customer Account Data Deletion & RA 10173 Privacy Compliance Processing | Compliance & Regulatory |
| W837 | Daily Store Exception-Based Reporting & Transaction Monitoring | Loss Prevention & Asset Protection |
| W838 | CCTV & Surveillance System Daily Operations & Incident Review | Loss Prevention & Asset Protection |
| W839 | Internal Theft Investigation & Employee Dishonesty Case Management | Loss Prevention & Asset Protection |
| W840 | Organized Retail Crime Detection, Tracking & Task Force Coordination | Loss Prevention & Asset Protection |
| W841 | Refund & Return Fraud Detection, Investigation & Prevention | Loss Prevention & Asset Protection |
| W842 | Cash Handling Exception Monitoring & Sweethearting Detection | Loss Prevention & Asset Protection |
| W843 | Vendor & Delivery Fraud Detection & Dock Security Audit | Loss Prevention & Asset Protection |
| W844 | Store Entrance/Exit Audit & Electronic Article Surveillance (EAS) Management | Loss Prevention & Asset Protection |
| W845 | Shrinkage Analysis, Root Cause Investigation & Reduction Program | Loss Prevention & Asset Protection |
| W846 | Loss Prevention Training, Awareness & Compliance Program | Loss Prevention & Asset Protection |
| W140 | Occupational Health & Safety (OHS) Incident Management | Health, Safety & Environment |
| W695 | Emergency Response & Evacuation Protocol Management | Health, Safety & Environment |
| W696 | Contractor & Visitor Safety Induction & Access Control | Health, Safety & Environment |
| W697 | Workplace Ergonomics Assessment & Musculoskeletal Injury Prevention | Health, Safety & Environment |
| W698 | Safety Data Sheet (SDS) Lifecycle Management & Distribution | Health, Safety & Environment |
| W699 | Hazmat Transportation & Carrier Compliance Management | Health, Safety & Environment |
| W758 | Store-Level Fire Safety Equipment Daily Inspection & Compliance | Health, Safety & Environment |
| W759 | Store-Level Hazardous Material Customer Advisory & Safe Handling Guidance | Health, Safety & Environment |
| W803 | Hazmat Regulatory Change Management & Compliance Update | Health, Safety & Environment |
| W804 | Occupational Health Surveillance, Employee Medical Monitoring & Record Management | Health, Safety & Environment |
| W847 | Business Continuity Plan Annual Review & Update | Business Continuity & Insurance |
| W848 | Typhoon & Natural Disaster Store Emergency Protocol & Response | Business Continuity & Insurance |
| W849 | IT Disaster Recovery Site Activation & Failover Execution | Business Continuity & Insurance |
| W850 | Store Emergency Closure & Reopening Procedure | Business Continuity & Insurance |
| W851 | Critical System Recovery & Service Restoration | Business Continuity & Insurance |
| W852 | Supply Chain Disruption Business Impact Assessment & Recovery | Business Continuity & Insurance |
| W853 | Business Continuity Plan Tabletop Exercise & Drill Execution | Business Continuity & Insurance |
| W854 | Pandemic/Epidemic Business Continuity Activation & Operations | Business Continuity & Insurance |
| W855 | Communication Tree Activation & Crisis Communication Management | Business Continuity & Insurance |
| W856 | Post-Incident Review, Lessons Learned & Plan Update | Business Continuity & Insurance |
| W857 | Store & DC Property Insurance Claim Filing & Documentation | Business Continuity & Insurance |
| W858 | Typhoon, Flood & Natural Disaster Damage Assessment & Insurance Claim | Business Continuity & Insurance |
| W859 | Vehicle & Fleet Insurance Claim Processing | Business Continuity & Insurance |
| W860 | Business Interruption Insurance Claim & Loss Documentation | Business Continuity & Insurance |
| W861 | Employee Injury Insurance Claim Coordination & SSS/ECC Filing | Business Continuity & Insurance |
| W864 | Insurance Claim Recovery, Settlement & Accounting Entry | Business Continuity & Insurance |
| W5154 | ERP Item Master Plastic/Packaging Weight Fields Configuration | EPR Compliance & Plastic Recovery |
| W5157 | Outbound Retail Plastic/Packaging Weight Calculation & Transaction Matching | EPR Compliance & Plastic Recovery |
| W5158 | National Solid Waste Management Commission (NSWMC) EPR Program Registration | EPR Compliance & Plastic Recovery |
| W5161 | Retail Store In-Store Plastic Waste Sorting, Collection & Storage | EPR Compliance & Plastic Recovery |
| W5164 | Logistics Consolidation, Baling & Transport of Recovered Plastics to DCs | EPR Compliance & Plastic Recovery |
| W5169 | EPR Plastic Waste Recovery Certificate (PRC) Verification & Matching | EPR Compliance & Plastic Recovery |
| W5171 | Third-Party Independent Auditor Engagement & Scope Agreement | EPR Compliance & Plastic Recovery |
| W5172 | EPR Annual Audit Documentation Preparation & Reconciliation | EPR Compliance & Plastic Recovery |
| W5173 | National Solid Waste Management Commission (NSWMC) Annual Compliance Filing | EPR Compliance & Plastic Recovery |
| W5346 | DENR-EMB Hazardous Waste Generator/Treater Registration & Permitting (RA 6969) | Household Hazardous Waste Take-Back |
| W5347 | Take-Back Partner, Transporter & TSD (Treatment-Storage-Disposal) Facility Accreditation | Household Hazardous Waste Take-Back |
| W5349 | In-Store Take-Back Collection Point Design, Containment & Safety Infrastructure | Household Hazardous Waste Take-Back |
| W5351 | Hazardous Waste Manifest, Transporter Accreditation & Chain-of-Custody System Setup | Household Hazardous Waste Take-Back |
| W5354 | Used Motor Oil, Lubricant & Filter Collection & Bulk Consolidation | Household Hazardous Waste Take-Back |
| W5355 | Lead-Acid & Lithium Battery Collection, Safe Storage & Fire-Separation Compliance | Household Hazardous Waste Take-Back |
| W5356 | Fluorescent, CFL & Mercury-Vapor Lamp Collection & Mercury Containment | Household Hazardous Waste Take-Back |
| W5360 | Hazardous Waste Consolidation, Manifest Generation & Licensed Transporter Pickup | Household Hazardous Waste Take-Back |
| W5364 | Take-Back Volume Tracking, DENR-EMB Annual Hazardous Waste Report & NSWMC Filing | Household Hazardous Waste Take-Back |
| W5367 | Stewardship Program Cost Recovery, Co-Funding Reconciliation & Vendor Settlement | Household Hazardous Waste Take-Back |

#### Technology & Data

| ID | Workflow | Value Stream |
|---|---|---|
| W382 | IT Backup & Recovery Operations | IT Operations & Security |
| W383 | IT Security Incident Response (General) | IT Operations & Security |
| W385 | Data Cleansing & Migration Operational Lifecycle | IT Operations & Security |
| W393 | Remote Access, VPN & Zero Trust Connectivity Management | IT Operations & Security |
| W495 | ERP Patch, Upgrade & Release Management | IT Operations & Security |
| W595 | ERP System Daily Health Check & Integration Monitoring | IT Operations & Security |
| W614 | Data Warehouse & ETL Pipeline Daily Operations & Monitoring | IT Operations & Security |
| W615 | Customer Mobile App Daily Operations & Content Management | IT Operations & Security |
| W616 | ERP Business Change Request & Enhancement Backlog Management | IT Operations & Security |
| W710 | Loss Prevention Analytics & Shrinkage Investigation System Operations | IT Operations & Security |
| W73 | System Upgrade & New Entity Integration Testing | IT Operations & Security |
| W733 | Enterprise API Gateway Daily Monitoring & Health Dashboard | IT Operations & Security |
| W831 | POS Terminal Emergency Swap & Rapid Replacement Protocol | IT Operations & Security |
| W5430 | OT Cyber Incident Detection, Containment & Fail-Secure Response | OT/ICS Cybersecurity |
| W5431 | OT Forensics, Root-Cause & Cross-Regulator (BSP/NPC/BFP) Notification | OT/ICS Cybersecurity |
| W5435 | OT Cybersecurity Compliance (IEC 62443 / NIST SP 800-82) & Audit Evidence | OT/ICS Cybersecurity |
| W5437 | OT-Aware Business Continuity, Recovery & Fail-Secure Operating Mode | OT/ICS Cybersecurity |

#### Post-Catalog Confirmation (2026-09-02)

Six post-catalog workflows confirmed **Tier 1** — statutory / regulatory execution (W5497 CODI machinery per RA 7877/RA 11313; W5508 quarterly BIR 1605 FBT filing) or core-transactional checkout integrity (W5505 barcode/price-label governance per the RA 7394 posted-tag regime), including three promotions from the keyword-proposed Tier 2 on statutory-execution grounds (W5498 RA 11165 agreement mandate + DOLE inspection readiness; W5503 DENR CCO lead-cap gates + agency response deadlines; W5504 RA 11058/DO 252-25 threshold work-interruption duty — W576/W140 sibling precedent). Rows in family order (People, Governance & Assurance, Sell & Serve, Finance):

| ID | Workflow | Value Stream |
|---|---|---|
| W5497 | POSH / Safe Spaces Compliance Program — CODI Committee, Statutory Investigation & Reporting (RA 7877 / RA 11313) | Labor Relations & Collective Bargaining |
| W5498 | Telecommuting & Flexible / Hybrid Work Arrangement Program (RA 11165) | Hire-to-Retire |
| W5503 | Restricted-Substance & Chemical-Content Product Compliance — Lead-in-Paint (DENR CCO), Formaldehyde Emission & VOC Limits | Quality Management & Product Compliance |
| W5504 | Extreme-Heat Work Interruption & Occupational Heat-Stress Management (DOLE Heat-Index Advisory Response) | Health, Safety & Environment |
| W5505 | Concession Item Catalog, Barcode & Price-Label Onboarding & Governance | Store Operations |
| W5508 | Fringe Benefits Tax (FBT) Determination, Valuation & Quarterly BIR Form 1605 Filing | Tax Management & BIR Reporting |

#### Finance-Workflow Gap-Fill Pass (2026-09-03)

The finance-workflow gap fill added three workflows — two confirmed directly **Tier 1** on the statutory-execution class of their Record-to-Report siblings (W407 corporate income-tax computation, W481 SEC reportorial filing, W5508 quarterly BIR 1605 FBT filing — the W5508 statutory-filing precedent): the MCIT computation is the statutory tax-floor machinery feeding the 1702RT/1702Q filings, and the PFRS 8 segment-note production is the statutory disclosure layer the AFS cannot file without:

| ID | Workflow | Value Stream |
|---|---|---|
| W5530 | Minimum Corporate Income Tax (MCIT) Computation, Regime Evaluation & 3-Year Excess-Credit Carry-Forward | Record-to-Report |
| W5531 | PFRS 8 Operating-Segment Reporting, CODM Disclosure Package & Segment-Note Production | Record-to-Report |

#### Operations-Workflow Gap-Fill Pass (2026-09-04)

The operations-workflow gap fill added one workflow confirmed directly **Tier 1** on the statutory-execution class of its PA-79.2 siblings (W2764 compensation-withholding remittances, W2765 annual 1604E/1604C filing, and the W5508 quarterly-BIR-filing precedent): the BIR Form 2316 furnishing to every employee is the certificate layer of the same withholding regime — a January 31 statutory deadline whose evidence pack the BIR examines first:

| ID | Workflow | Value Stream |
|---|---|---|
| W5533 | BIR Form 2316 Annual Issuance, Employee Acknowledgment & Certificate Lifecycle | Tax Management & BIR Reporting |

#### Emergency & Continuity Workflow Gap-Fill Pass (2026-09-05)

The emergency & continuity workflow gap fill added three workflows confirmed directly **Tier 1** — the life-safety in-store emergency class of their W330/W501/W576 siblings (W5536 missing-child/Code Adam, W5537 fire event response, W5538 bomb threat): each executes a life-safety duty of care to the ~99,000 people on premises chain-wide per day (customers + staff, the W330 canon) with statutory anchors (RA 7610 child protection, RA 9514 Fire Code re-occupancy clearance, PNP-EOD coordination) and gates reopening/reunification on verified external clearance:

| ID | Workflow | Value Stream |
|---|---|---|
| W5536 | Missing-Child / Code Adam In-Store Response Protocol | Store Operations |
| W5537 | Fire Event Response, Suppression & Post-Fire BFP Clearance (Store & DC) | Health, Safety & Environment |
| W5538 | Bomb Threat Response & Search-or-Evacuation Decision Protocol | Health, Safety & Environment |

#### Regulatory-Shock, Platform-Outage & Governance-Continuity Gap-Fill Pass (2026-09-05)

The batch-17 gap fill added two workflows confirmed directly **Tier 1** — the statutory-deadline-protection class of the W2764/W2765/W5508 filing siblings: W5545 BIR tax-enforcement suspension & closure-order response (the Oplan Kandado class — the highest-severity tax-enforcement event, each closed day costing the site its full revenue day, reopening gated on the written BIR lifting order) and W5546 BIR eFPS/government-portal outage filing contingency (the statutory-filing failure path — evidence pack, AAB fallback, payment-protection rule and penalty-relief documentation; eFPS downtime was cited as a pain point in four PA files with only a one-bullet mitigation and no event owner):

| ID | Workflow | Value Stream |
|---|---|---|
| W5545 | BIR Tax-Enforcement Suspension & Closure-Order Response (Oplan Kandado) | Tax Management & BIR Reporting |
| W5546 | BIR eFPS & Government-Portal Outage Filing Contingency, AAB Fallback & Penalty-Relief Documentation | Tax Management & BIR Reporting |

#### Channel-Enforcement, Employee-Legal-Status, OSH-Enforcement & App-Store-Removal Gap-Fill Pass (2026-09-05)

The batch-18 gap fill added one workflow confirmed directly **Tier 1** — the OSH statutory-enforcement class of the W5545 closure-order precedent: W5552 DOLE imminent-danger work-stoppage order response (a regulator-ordered halt gated on life safety — comply-first abatement, the no-wage-loss rule for stoppage-affected workers, and reopening only on DOLE's written lifting order, the E-25 reopen-gate pattern; RA 11058 appeared only as the inspection/penalties context of W505, with 'work stoppage'/'stoppage order'/'imminent danger' in zero dedicated headers):

| ID | Workflow | Value Stream |
|---|---|---|
| W5552 | DOLE Imminent-Danger Work-Stoppage Order Response, Abatement & Reinstatement Gate | Health, Safety & Environment |

#### In-Transit-Security, Fatality-Scene, Tampering-Extortion & Recruitment-Fraud Gap-Fill Pass (2026-09-05)

The batch-19 gap fill added two workflows confirmed directly **Tier 1** — the life-safety scene-and-clearance class of the W5536/W5537/W5538 in-store emergency precedent, each gating a physical-state transition (scene release / stop-sale-to-trading) on documented external assessment: W5555 customer or visitor death on premises (W4401 owns injuries and names fatality only as W4405's notification trigger — 'death on premises'/'died in store' in zero PA files as protocol content; the potential-crime-scene nothing-moves discipline until PNP/SOCO documented clearance, family liaison with no social-media-first discovery, the dignity-first trading-continuity decision, and the witnessing-staff stand-down had no owner) and W5556 product-tampering threat & extortion demand (VS-89 owns every found-defect trigger — W2993 intake, W2994 recall decision, W3000 stop-sale — but 'tampering threat'/'contamination threat'/'extortion' appear in zero dedicated headers; the never-pay rule, the specificity-gated sweep-or-monitor decision — the W5538 bomb-threat decision law transposed to merchandise — and the law-enforcement assessment preceding any W3000 stop-sale had no owner):

| ID | Workflow | Value Stream |
|---|---|---|
| W5555 | Customer or Visitor Death on Premises — Scene Protocol, Family Liaison & Trading-Continuity Decision | Customer Safety, Premises Liability & In-Store Risk Management |
| W5556 | Product-Tampering Threat, Extortion Demand & Merchandise-Integrity Sweep Protocol | Product Recall & Safety Corrective Action Management |

The batch-20 gap fill added one workflow confirmed directly **Tier 1** — the enterprise-trading-halt & statutory-continuity class of the W5545/W5546 enforcement-and-filing precedent (a chain-wide destructive attack halts trading and can block statutory filings and payroll — the same protection-of-trading-and-filing rationale, in the cyber domain): W5558 ransomware & destructive cyber-attack enterprise response ('ransomware'/'extortion demand'/'data-destruction' appeared in the corpus only as pain points and drill injects — PA-27.2's DR risk names the isolate-DR-before-failover trap, W1330 injects the scenario, W5529 drills the OT variant, and zero dedicated headers owned the event; the no-payment default with Board/counsel-gated departure, the isolate-DR-before-failover sequencing, chain-wide manual trading mode, the privileged forensics clock, the staged clean rebuild, and the cyber-insurance & disclosure clocks had no owner; the data-privacy core rides the Tier-1 W53 and the OT variant rides W5529):

| ID | Workflow | Value Stream |
|---|---|---|
| W5558 | Ransomware & Destructive Cyber-Attack Enterprise Response Protocol | IT Operations & Security |

#### Storefront-Crash, Brand-Impersonation-Scam, Wallet-Outage & Adjacent-Works Gap-Fill Pass (2026-09-05)

The batch-21 gap fill added one workflow confirmed directly **Tier 1** — the life-safety structural-clearance class of the W5537/W5555 precedent, gating a physical-state transition (zone reopening) on documented external assessment: W5562 vehicle-impact & storefront-crash response ('vehicle into building'/'storefront crash' appear in zero PA files — W330's in-store emergency trigger names structural failure generically but defers event-specific execution, W5555 owns the fatality scene, and W1450's structural assessment is quake-specific; the crash-scene safety law, the driver's-CTPL-first liability ordering with BuildRight's loss as subrogation, the red-tag structural discipline before any zone reopens, and the bollard/barrier retrofit feedback had no owner):

| ID | Workflow | Value Stream |
|---|---|---|
| W5562 | Vehicle-Impact & Storefront-Crash Response Protocol | Customer Safety, Premises Liability & In-Store Risk Management |

#### Gas-Leak, Tsunami/Storm-Surge, Media-Exposé & Server-Room-Environmental Gap-Fill Pass (2026-09-05)

The batch-23 gap fill added two workflows confirmed directly **Tier 1** — the pre-ignition life-safety and coastal-water-evacuation classes of the W5537/W5538/W1449 precedent, each gating a physical-state transition on documented external assessment: W5570 gas-leak event response ('gas leak'/'gas odor'/'smell of gas' appear in zero PA files as event content — W5069 owns cylinder leak *inspection/quarantine* at the cage as intake QC, W5537 owns fire *after ignition*; nobody owned the pre-ignition odor event: the odor-is-real-until-proven-otherwise law, the ignition-source ban with the exterior master kill, the heavier-than-air evacuate-up-and-out discipline, the trained-only two-person isolation boundary, or the documented detector-clear + source-disposition + ventilation reopen gate) and W5571 tsunami & storm-surge coastal-intrusion response ('tsunami' appears in zero PA files and 'storm surge' only as PA-09.2's customer-advisory context — W1450's quake protocol ends at structural assessment and W1387's flood canon is rainfall/riverine; nobody owned the coastal-intrusion class: the quake-is-the-warning law, the move-up-not-out vertical-evacuation rule, the no-return law until PHIVOLCS cancellation, the surge-forecast-not-signal-number closure ladder riding the E-02 custody, or the saltwater desalination gate before re-energization):

| ID | Workflow | Value Stream |
|---|---|---|
| W5570 | Gas-Leak Event Response (LPG/Natural-Gas Odor on Premises) | Health, Safety & Environment |
| W5571 | Tsunami & Storm-Surge Coastal-Intrusion Response Protocol (PHIVOLCS Advisory / PAGASA Storm-Surge Warning) | Business Continuity & Insurance |

### Tier 2 Additions (547 Workflows)

#### Plan & Source

| ID | Workflow | Value Stream |
|---|---|---|
| W515 | Loyalty Tier Re-evaluation & Migration Processing | Merchandise Strategy |
| W564 | New Product Introduction (NPI) & Full Store Rollout | Merchandise Strategy |
| W678 | Multi-Channel Pricing Consistency Monitoring & Governance | Merchandise Strategy |
| W679 | Assortment Optimization & Rationalization Review | Merchandise Strategy |
| W737 | Markdown Optimization & Analytics Operations | Merchandise Strategy |
| W738 | Vendor Trade Fund Management & Promotional Budget Tracking | Merchandise Strategy |
| W830 | Product Phase-Out Inventory Disposition Planning & Execution | Merchandise Strategy |
| W900 | Vendor New Product In-Store Launch Event & Demonstration Coordination | Merchandise Strategy |
| W908 | Store-Level Barangay & Local Fiesta Merchandising Calendar Management | Merchandise Strategy |
| W910 | Customer Product Bundle Assembly & Pre-Packaged Solution Kit Management | Merchandise Strategy |
| W925 | Vendor Consignment Shelf Space Performance Monitoring & Optimization | Merchandise Strategy |
| W1031 | Customer Delivery Service Area Geo-Fencing & Coverage Management | Supply Planning |
| W492 | Temperature-Controlled & Sensitive Goods Logistics | Supply Planning |
| W622 | Mock Product Recall Exercise & Recall Readiness Testing | Supply Planning |
| W623 | Cross-Functional New Store Opening Readiness Review | Supply Planning |
| W786 | DC-to-Store Delivery Route Optimization & Multi-Stop Planning | Supply Planning |
| W1002 | Vendor Product Sampling & Test Batch Inventory Lifecycle Management | Vendor Management & Procurement |
| W1033 | Vendor Lead Time Accuracy Monitoring & Supply Planning Impact Assessment | Vendor Management & Procurement |
| W1035 | Store-Level Return-to-Vendor (RTV) Consolidation & Batch Shipping Processing | Vendor Management & Procurement |
| W1100 | Customer Contractor Project Financing & Supplier Credit Line Partnership Management | Vendor Management & Procurement |
| W1105 | Vendor Early Payment Discount Capture & Dynamic Discounting Optimization | Vendor Management & Procurement |
| W1110 | Vendor-Managed Inventory (VMI) Seasonal Ramp-Up & Wind-Down | Vendor Management & Procurement |
| W1115 | Vendor Performance-Based Shelf Space Allocation Review | Vendor Management & Procurement |
| W1128 | Vendor Catalog New Product Sample Request & In-Store Trial Evaluation | Vendor Management & Procurement |
| W1132 | Vendor Logistics Performance Weekly Scorecard & Carrier Lane Analysis | Vendor Management & Procurement |
| W1141 | Vendor Payment Term Annual Renegotiation & Cost Savings Tracking | Vendor Management & Procurement |
| W1145 | Vendor Seasonal Import Container Consolidation & Optimization Planning | Vendor Management & Procurement |
| W1151 | Vendor Product Recall Cost Recovery & Margin Impact Assessment | Vendor Management & Procurement |
| W491 | Supplier Financial Health & Credit Risk Monitoring | Vendor Management & Procurement |
| W513 | Vendor-Funded Promotional Activity & Co-op Advertising Management | Vendor Management & Procurement |
| W621 | Vendor-Managed Inventory (VMI) Daily Performance Monitoring | Vendor Management & Procurement |
| W631 | Strategic Sourcing & Category Strategy | Vendor Management & Procurement |
| W672 | VMI Quarterly Business Review & Program Optimization | Vendor Management & Procurement |
| W705 | Vendor Self-Service Portal Operations & Supplier Collaboration | Vendor Management & Procurement |
| W706 | Supplier Performance Scorecard & Quarterly Business Review | Vendor Management & Procurement |
| W788 | Vendor New Product Submission Review & Evaluation Processing | Vendor Management & Procurement |
| W868 | Vendor Catalog & Product Information Self-Service Management | Vendor Management & Procurement |
| W869 | Vendor Dispute Resolution & Issue Ticketing | Vendor Management & Procurement |
| W871 | Supplier Scorecard Portal Publication & Performance Transparency | Vendor Management & Procurement |
| W872 | Vendor RFQ & Bid Submission Portal Management | Vendor Management & Procurement |
| W901 | Vendor Seasonal Buy-Back & Stock Return Agreement Execution | Vendor Management & Procurement |
| W932 | Vendor Catalog Price Change Intake, Assessment & ERP Synchronization | Vendor Management & Procurement |
| W978 | Vendor Seasonal Product Post-Season Performance Review & Assortment Rationalization | Vendor Management & Procurement |
| W5225 | B2B Project Custom Sourcing Intake and Specifications Scoping | B2B Bulk-Project Custom Import |
| W5226 | Overseas Supplier RFQ Factory Vetting and Sample Approval | B2B Bulk-Project Custom Import |
| W5227 | Project Landing Cost Calculation Pricing and Margin Matrix Modeling | B2B Bulk-Project Custom Import |
| W5228 | Custom Indent Sourcing Contract Drafting and Legal Signing | B2B Bulk-Project Custom Import |
| W5230 | Indent Order Technical Review and Production Quality Agreement Setup | B2B Bulk-Project Custom Import |
| W5231 | Production Scheduling and Weekly Factory Progress Verification | B2B Bulk-Project Custom Import |
| W5232 | Pre-Shipment Inspection Coordination and Quality Gate Sign-off | B2B Bulk-Project Custom Import |
| W5233 | Letter of Credit Opening and Trade Finance Allocation for Indent Orders | B2B Bulk-Project Custom Import |
| W5234 | Pro-Forma Invoice Verification and LC Amendment Processing | B2B Bulk-Project Custom Import |
| W5237 | Marine Insurance Coverage Mobilization and Port Risk Underwriting | B2B Bulk-Project Custom Import |
| W5241 | Direct Port-to-Jobsite Transit Logistics Planning and Route Survey | B2B Bulk-Project Custom Import |
| W5242 | Jobsite Unloading Site Readiness and Heavy Equipment Coordination | B2B Bulk-Project Custom Import |
| W5244 | Materials Discrepancy Damage Claims and Transit Insurance Execution | B2B Bulk-Project Custom Import |
| W5247 | Project Sourcing Closeout Warranty Activation and Customer Handover | B2B Bulk-Project Custom Import |

#### Make & Move

| ID | Workflow | Value Stream |
|---|---|---|
| W648 | DC Cycle Counting & Inventory Accuracy Program | DC & Warehouse Operations |
| W651 | Reverse Logistics Processing (Customer/Store Returns at DC) | DC & Warehouse Operations |
| W652 | Seasonal Warehouse Surge Planning & Execution | DC & Warehouse Operations |
| W784 | DC Inventory Slotting Optimization & Periodic Re-Slotting Execution | DC & Warehouse Operations |
| W796 | DC Workforce Scheduling, Labor Planning & Productivity Tracking | DC & Warehouse Operations |
| W797 | DC Security Operations, Perimeter Management & Access Control | DC & Warehouse Operations |
| W836 | DC Outbound Load Verification & Pre-Dispatch Quality Check | DC & Warehouse Operations |
| W588 | Seasonal Inventory Build-Down & Transition Execution | Inventory Lifecycle |
| W5177 | Disaster Relief Supply Forecasting & Category Inventory Staging Plan | Disaster Relief Supply Chain Logistics |
| W5178 | Emergency Building Materials (Galvanized Sheets, Nails, Lumber) Priority Allocation | Disaster Relief Supply Chain Logistics |
| W5179 | Disaster Relief Home Rebuilding Kit Kitting & Staging | Disaster Relief Supply Chain Logistics |
| W5180 | Emergency Power Generator & Solar Portable Kit Pre-Positioning | Disaster Relief Supply Chain Logistics |
| W5182 | Emergency Vendor Direct-to-Store Delivery (DSD) Fast-Track PO Issuance | Disaster Relief Supply Chain Logistics |
| W5183 | Inter-Island Relief Freight Capacity Reservation & Shipping Coordination | Disaster Relief Supply Chain Logistics |
| W5185 | LGU State of Calamity Declaration Trigger & Pricing Monitoring | Disaster Relief Supply Chain Logistics |
| W5193 | LGU Disaster Operations Center (DRRMC) Collaboration & Communication | Disaster Relief Supply Chain Logistics |
| W5194 | DSWD (Social Welfare) & Red Cross Priority Relief Delivery Operations | Disaster Relief Supply Chain Logistics |
| W5195 | NGO & Corporate Foundation Emergency Logistics Sponsorship Matching | Disaster Relief Supply Chain Logistics |
| W5196 | Store-Level Disaster Relief Hub Setup & Community Distribution Point Operations | Disaster Relief Supply Chain Logistics |
| W5198 | Emergency Fleet Fuel Allocation & Auxiliary Power Logistics | Disaster Relief Supply Chain Logistics |
| W5441 | Site Cleanup Service Product Design, Pricing & Catalog | Construction Debris & Site Cleanup |
| W5442 | Customer Debris Volume & Container Size Estimation | Construction Debris & Site Cleanup |
| W5444 | Crew, Container & Truck Dispatch Scheduling | Construction Debris & Site Cleanup |
| W5446 | B2B Project & Bulk Debris Engagement, SLA & Quotation | Construction Debris & Site Cleanup |
| W5448 | Site Cleanup Service Work Order, Pricing & Booking Confirmation | Construction Debris & Site Cleanup |
| W5449 | On-Site Debris Collection, Segregation & Load-Out Execution | Construction Debris & Site Cleanup |
| W5451 | C&D Debris Weight/Volume Verification & Weighbridge Ticket Capture | Construction Debris & Site Cleanup |
| W5453 | Multi-Stream Routing to Recycler / Reprocessor / MDRF / Landfill | Construction Debris & Site Cleanup |
| W5455 | Site Final Cleanup, Handover & Customer Sign-Off | Construction Debris & Site Cleanup |
| W5457 | Job Settlement, Container Demurrage & Scrap/Rebate Recovery Billing | Construction Debris & Site Cleanup |
| W5458 | Customer Invoicing, Dispute Resolution & Collections | Construction Debris & Site Cleanup |

#### Sell & Serve

| ID | Workflow | Value Stream |
|---|---|---|
| W1049 | Store-Level Customer Tool Sharpening, Blade Replacement & Small Engine Maintenance Service | Store Operations |
| W1058 | Store-Level Customer Bulk Construction Water Delivery & Site Logistics Coordination | Store Operations |
| W1085 | Store-Level Appliance Display Model Lifecycle & Periodic Refresh Management | Store Operations |
| W1091 | Store-Level Customer Fence & Gate Installation Service Partner Coordination | Store Operations |
| W1103 | Store-Level Outdoor Lumber Yard Rain Protection & Inventory Preservation | Store Operations |
| W1106 | Store-Level Community Building Materials Donation & LGU Partnership | Store Operations |
| W1112 | Store-Level Inventory Age-Based Auto-Markdown & Clearance Trigger | Store Operations |
| W1116 | Store-Level Customer Complaint Trend Analysis & Systemic Issue Escalation | Store Operations |
| W1119 | Store-Level Outdoor Garden Center Seasonal Plant Inventory Lifecycle | Store Operations |
| W1121 | Store-Level Intercom & Public Address System Daily Operations | Store Operations |
| W1123 | Store-Level Customer Project Progress Site Visit & Material Delivery Verification | Store Operations |
| W1130 | Store-Level Paint Tinting Machine Calibration Verification & Color Accuracy Audit | Store Operations |
| W1133 | Store-Level Customer Special Order Cancellation & Partial Refund Processing | Store Operations |
| W1135 | Store-Level Daily Temperature-Sensitive Product Monitoring & Quality Check | Store Operations |
| W1139 | Store-Level Lumber Yard Inventory Seasonal Rotation & Grade Segregation | Store Operations |
| W1142 | Store-Level Customer Waiting Area Comfort & Amenities Daily Management | Store Operations |
| W503 | Store-Level Pest Control & Sanitation Management | Store Operations |
| W524 | Demo / Display Unit Selling at POS | Store Operations |
| W575 | Store-Level Weekly Sales & Operations Review | Store Operations |
| W577 | Store-Level Holiday Season (Ber Months) Operational Ramp-Up | Store Operations |
| W578 | Store-Level Payday Weekend & Peak Day Operational Readiness | Store Operations |
| W581 | Store-Level Vendor Representative Access & Activity Management | Store Operations |
| W583 | Store-Level Seasonal Promotional Transition & Display Reset | Store Operations |
| W602 | Store-Level Labor Cost Monitoring & Overtime Budget Control | Store Operations |
| W606 | Store-Level Water & Utility Conservation Operations | Store Operations |
| W609 | Store-Level New Employee Buddy System & First-Week Onboarding | Store Operations |
| W665 | Store-Level KPI Dashboard & Daily Performance Monitoring | Store Operations |
| W668 | Store-Level Home Delivery & Third-Party Logistics Coordination | Store Operations |
| W702 | New Store Opening Project Management & Go-Live Execution | Store Operations |
| W703 | Store Closure, Consolidation & Asset Recovery | Store Operations |
| W722 | Store-Level Exterior Display & Garden Center Daily Operations | Store Operations |
| W723 | Store-Level Loading Bay Traffic & Truck Queue Management | Store Operations |
| W742 | Store-Level Key, Access Card & Secure Area Daily Management | Store Operations |
| W745 | Store-Level Receiving Dock Scheduling & DSD Vendor Delivery Window Management | Store Operations |
| W774 | Store-Level Parking Lot & Exterior Facility Daily Management | Store Operations |
| W824 | Store-Level Lumber Yard & Outdoor Area Daily Operations | Store Operations |
| W825 | Store-Level Bulky Item Delivery Proof Collection & Documentation | Store Operations |
| W826 | Store-Level Layaway Payment Reminder & Forfeiture Processing | Store Operations |
| W950 | Store-Level Customer Vehicle Loading Assistance & Load Securing | Store Operations |
| W951 | Store-Level Bulk Material Breaking & Custom Quantity Packaging | Store Operations |
| W952 | Store-Level Customer Gratuity & Service Tip Processing | Store Operations |
| W974 | Store-Level Customer Project Staged Delivery & Phased Material Release | Store Operations |
| W999 | Store-Level Customer Tile & Flooring Sample Loan & Return Program | Store Operations |
| W523 | POS Promotional Terminal Setup & Pre-Live Verification | POS & Checkout |
| W526 | POS Customer Queue Management & Express Lane Operations | POS & Checkout |
| W605 | Return Fraud Detection & Serial Returner Management | POS & Checkout |
| W747 | POS Credit Card Installment Selling & 0% Interest Promotion Processing | POS & Checkout |
| W748 | POS Customer Loyalty On-the-Spot Upselling & Cross-Selling | POS & Checkout |
| W896 | Customer Gift Card Corporate & Bulk Purchase Processing | POS & Checkout |
| W935 | Customer Product Registration at POS for Vendor Extended Warranty | POS & Checkout |
| W1000 | Customer Ceiling System Material Calculator & Design Recommendation Service | In-Store Customer Services |
| W1004 | Customer Material Delivery Scheduling & Rescheduling Self-Service Portal | In-Store Customer Services |
| W1007 | Customer Tool & Equipment Demo Reservation & Scheduling Service | In-Store Customer Services |
| W1009 | Customer Custom Order Special Pricing Approval & Quotation Lifecycle | In-Store Customer Services |
| W1014 | Customer Multi-Entity Billing & Consolidated Invoicing for Corporate Accounts | In-Store Customer Services |
| W1016 | Customer Product Installation Warranty Registration & Follow-Up Service | In-Store Customer Services |
| W1018 | Customer Project Progress Payment Verification & Invoice Matching | In-Store Customer Services |
| W1043 | Customer Paint Coverage Area Calculator & Primer/Finish Quantity Estimator Service | In-Store Customer Services |
| W1044 | Customer Concrete Mix Ratio & Volume Calculator for Slab/Foundation/Column Service | In-Store Customer Services |
| W1045 | Store-Level Customer PVC Pipe Cutting, Jointing & Fabrication Service | In-Store Customer Services |
| W1046 | Customer Door & Window Measurement, Sizing & Custom Order Service | In-Store Customer Services |
| W1048 | Customer Rainwater Harvesting System Design & Material Sizing Service | In-Store Customer Services |
| W1050 | Customer Staircase Tread, Riser & Railing Material Calculator Service | In-Store Customer Services |
| W1052 | Customer Gutter, Downspout & Flashing Sizing Calculator Service | In-Store Customer Services |
| W1053 | Customer Bathroom & Kitchen Exhaust Fan & Ventilation Duct Sizing Service | In-Store Customer Services |
| W1054 | Store-Level Customer Wire & Cable Cut-to-Length Spool Service | In-Store Customer Services |
| W1055 | Customer Water Filtration & Purification System Sizing for Residential & Commercial | In-Store Customer Services |
| W1057 | Customer Insulation Material Calculator (Wall, Ceiling, Roof Thermal & Acoustic) | In-Store Customer Services |
| W1059 | Customer Kitchen Countertop Measurement & Custom Fabrication Order Service | In-Store Customer Services |
| W1060 | Customer Rebar Stirrup, Tying Wire & Binding Material Quantity Estimator Service | In-Store Customer Services |
| W1061 | Customer Tile Grout, Adhesive & Thin-Set Mortar Quantity Calculator Service | In-Store Customer Services |
| W1063 | Store-Level Customer Welding Gas Cylinder Exchange & Refill Service | In-Store Customer Services |
| W1064 | Customer Electrical Panel & Circuit Breaker Sizing Recommendation Service | In-Store Customer Services |
| W1065 | Customer Bathroom Renovation Complete Project Planning & Material Bundle Service | In-Store Customer Services |
| W1066 | Customer Termite & Pest Control Product Selection & Treatment Plan Recommendation | In-Store Customer Services |
| W1068 | Customer Earthquake-Resistant Construction Material Selection & Retrofit Advisory | In-Store Customer Services |
| W1069 | Customer Flood-Resistant Construction Material Recommendation | In-Store Customer Services |
| W1072 | Store-Level Customer Marine & Coastal Construction Material Selection Advisory | In-Store Customer Services |
| W1073 | Customer House Foundation Type Recommendation & Material Estimation Service | In-Store Customer Services |
| W1075 | Customer Roof Truss & Structural Frame Material Estimation Service | In-Store Customer Services |
| W1077 | Store-Level Customer Construction Site Portable Toilet & Temporary Facility Rental Coordination | In-Store Customer Services |
| W1078 | Customer Rainwater Collection & Storage System Complete Package Design | In-Store Customer Services |
| W1079 | Customer Swimming Pool Construction Material Estimation Service | In-Store Customer Services |
| W1081 | Customer Construction Project Insurance Coverage Advisory Service | In-Store Customer Services |
| W1083 | Store-Level Customer Plumbing Fixture & Fitting Compatibility Verification Service | In-Store Customer Services |
| W1084 | Customer Home Security & CCTV System Design & Product Recommendation Service | In-Store Customer Services |
| W1086 | Customer Construction Waste Disposal & Skip/Dumpster Rental Coordination | In-Store Customer Services |
| W1089 | Store-Level Customer Tile & Flooring Digital Room Visualizer Kiosk Operations | In-Store Customer Services |
| W1090 | Customer HVAC Ductwork Design & Complete Material Sizing Recommendation | In-Store Customer Services |
| W1093 | Customer Interior Paint Color Scheme Consultation & Material Board Service | In-Store Customer Services |
| W1094 | Customer Construction Equipment Rental Partner Coordination & Booking | In-Store Customer Services |
| W1095 | Store-Level Customer Electrical Residential Wiring Diagram & Material List Service | In-Store Customer Services |
| W1097 | Store-Level Customer Outdoor Deck, Patio & Pergola Material Estimation Service | In-Store Customer Services |
| W1101 | Store-Level Customer Door & Window Security Grille Custom Fabrication Coordination | In-Store Customer Services |
| W1102 | Customer Retaining Wall & Foundation Formwork Material Estimation Service | In-Store Customer Services |
| W1113 | Customer E-Gift Card Purchase & Digital Delivery | In-Store Customer Services |
| W1114 | Customer Product Availability Real-Time Stock Lookup & Reservation Service | In-Store Customer Services |
| W1122 | Customer Project Material Delivery Photo Documentation & Proof Service | In-Store Customer Services |
| W1124 | Customer Construction Material Compatibility Cross-Reference & Substitution Advisory | In-Store Customer Services |
| W1126 | Customer Bulk Cement & Sand Order Direct-to-Site Delivery Tracking | In-Store Customer Services |
| W1129 | Customer Interior Design Material Board Curation & Mood Board Assembly Service | In-Store Customer Services |
| W1131 | Customer Construction Project Milestone Photo Documentation & Progress Tracking Portal | In-Store Customer Services |
| W1140 | Customer Post-Construction Punch List Material Fulfillment & Callback Order | In-Store Customer Services |
| W1143 | Customer Construction Material Pre-Order Reservation & Price Lock Service | In-Store Customer Services |
| W1146 | Store-Level Customer Cement & Bagged Material Shelf Life Monitoring & Freshness Guarantee | In-Store Customer Services |
| W1148 | Store-Level Customer Construction Site Vehicle Access Assessment & Delivery Feasibility | In-Store Customer Services |
| W1150 | Store-Level Customer Lumber & Plywood Moisture Content Testing & Quality Verification | In-Store Customer Services |
| W1152 | Store-Level Customer Project Material Quantity Verification & Completeness Check | In-Store Customer Services |
| W1158 | Store-Level Customer Project Material List Sharing & Contractor Collaborative Shopping | In-Store Customer Services |
| W1159 | Customer Construction Material Price Escalation Protection & Forward Pricing Agreement | In-Store Customer Services |
| W1160 | Store-Level DC-to-Store Delivery Inter-Island Ferry Scheduling & Coordination | In-Store Customer Services |
| W1162 | Store-Level Customer Power Tool & Equipment Pre-Purchase Try-Before-You-Buy Program | In-Store Customer Services |
| W604 | Store-Level Customer Experience Standards & Daily Service Operations | In-Store Customer Services |
| W607 | Store-Level Product Demo & Trial Station Daily Operations | In-Store Customer Services |
| W608 | Store-Level Customer Feedback Collection & Daily CX Pulse Monitoring | In-Store Customer Services |
| W740 | Store-Level Customer Complaint On-the-Spot Resolution & Floor Staff Empowerment | In-Store Customer Services |
| W744 | Store-Level Special Order Follow-Up & Proactive Customer Notification | In-Store Customer Services |
| W746 | Store-Level Building Material Sample Management & Customer Selection Assistance | In-Store Customer Services |
| W772 | Store-Level Rain Check Issuance for Out-of-Stock Promotional Items | In-Store Customer Services |
| W773 | Store-Level Customer Hold & Will-Call Order Management | In-Store Customer Services |
| W775 | Store-Level Customer Loyalty Card Replacement & Account Recovery | In-Store Customer Services |
| W776 | Store-Level Product Recall Customer Notification Execution | In-Store Customer Services |
| W823 | Store-Level Customer Material Calculator & Quantity Estimation Service | In-Store Customer Services |
| W897 | Store-Level Trade Professional Verification & Pro Badge Issuance for Discount Program | In-Store Customer Services |
| W903 | Store-Level Customer Material Sample Loan & Return Management | In-Store Customer Services |
| W916 | Customer Trade-In & Used Power Tool Buy-Back Program | In-Store Customer Services |
| W922 | Customer Walk-In Bulk Purchase Negotiation & Volume Pricing Approval | In-Store Customer Services |
| W924 | Store-Level Self-Service Kiosk & Interactive Product Information Station Management | In-Store Customer Services |
| W929 | Store-Level Lost & Found Item Management | In-Store Customer Services |
| W931 | Store-Level Customer Comfort Room & Amenity Daily Operations | In-Store Customer Services |
| W937 | Store-Level Customer Wheelchair & PWD Mobility Assistance Service | In-Store Customer Services |
| W941 | Store-Level Customer Baggage Hold & Parcel Custody Service | In-Store Customer Services |
| W943 | Customer Glass Cutting & Custom Flat Glass Service | In-Store Customer Services |
| W944 | Customer Pipe Threading, Cutting & Fabrication Service | In-Store Customer Services |
| W945 | Customer Key Duplication & Lock Rekeying Service | In-Store Customer Services |
| W946 | Customer Screen Door & Window Screen Custom Fabrication Service | In-Store Customer Services |
| W954 | Customer Delivery & Installation Quality Follow-Up Verification | In-Store Customer Services |
| W955 | Customer Daily-Wage Construction Worker Hiring Facilitation Service | In-Store Customer Services |
| W960 | Seasonal Forward Stock Pre-Positioning & Regional Buffer Management | In-Store Customer Services |
| W963 | Customer Tile & Flooring Quantity Calculator & Waste Factor Recommendation | In-Store Customer Services |
| W964 | Customer Bulk Cement, Sand & Aggregates Order & Direct-to-Site Delivery | In-Store Customer Services |
| W965 | Customer Complete Bathroom/Kitchen Renovation Package Assembly & Order | In-Store Customer Services |
| W967 | Store-Level Customer Project Material Takeoff & Professional Estimation Service | In-Store Customer Services |
| W968 | Customer Multi-Store Aggregated Order & Consolidated Single Delivery | In-Store Customer Services |
| W971 | Customer Power Tool Battery & Accessory Cross-Compatibility Checker & Recommendation | In-Store Customer Services |
| W976 | Store-Level Customer Lumber & Plywood Grade Selection & Quality Verification | In-Store Customer Services |
| W981 | Customer Paint Color Matching from Physical Sample & Digital Photo | In-Store Customer Services |
| W982 | Customer Electrical Load Calculation & Wire Size Recommendation Service | In-Store Customer Services |
| W983 | Customer Roofing Material Calculator & GI Sheet/Insulation Sizing Recommendation | In-Store Customer Services |
| W984 | Customer Water Tank & Pump System Sizing Recommendation Service | In-Store Customer Services |
| W985 | Store-Level Customer Aircon Sizing & BTU/Horsepower Calculation Service | In-Store Customer Services |
| W986 | Store-Level Customer Rebar Cutting, Bending & Fabrication Service | In-Store Customer Services |
| W987 | Customer Fence & Gate Material Estimation & Design Recommendation Service | In-Store Customer Services |
| W988 | Store-Level Customer Welding & Custom Metal Fabrication Service | In-Store Customer Services |
| W989 | Customer Plumbing System Layout Design & Material Takeoff Service | In-Store Customer Services |
| W991 | Customer Electrical Circuit Design & Residential Load Planning Service | In-Store Customer Services |
| W993 | Customer Construction Project Timeline & Phased Material Delivery Planner | In-Store Customer Services |
| W997 | Customer Bathroom/Kitchen Fixture Compatibility Checker & Bundle Builder | In-Store Customer Services |
| W998 | Customer Septic Tank & Wastewater System Sizing Recommendation Service | In-Store Customer Services |
| W569 | E-Commerce New Product Launch & Go-Live Process | Ecommerce & Digital Channels |
| W905 | Customer Project Photo Gallery & Social Proof/Inspiration Platform | Ecommerce & Digital Channels |
| W923 | Ecommerce Assembly & Installation Service Upsell at Online Checkout | Ecommerce & Digital Channels |
| W948 | Social Commerce Order Processing (Facebook, Instagram, TikTok Shop) | Ecommerce & Digital Channels |
| W1011 | Customer Trade Account Credit Insurance & Bad Debt Protection Processing | Trade, Project & Wholesale |
| W1022 | Customer Trade Account Statement Dispute & Resolution Processing | Trade, Project & Wholesale |
| W1024 | Customer Material Escrow & Project Fund Management for B2B Construction Accounts | Trade, Project & Wholesale |
| W1092 | Customer B2B Recurring Standing Order & Scheduled Auto-Replenishment Management | Trade, Project & Wholesale |
| W1107 | Customer Bulk Purchasing Group / Co-Op Buying Program Management | Trade, Project & Wholesale |
| W1111 | Customer Contractor Crew Registration & Job Site Badge Management | Trade, Project & Wholesale |
| W1117 | Customer Trade Account Statement of Account Auto-Generation & Email Delivery | Trade, Project & Wholesale |
| W1118 | Customer Contractor Project Bidding Support & Material Quote Service | Trade, Project & Wholesale |
| W1134 | Customer B2B Project Retention Money Release & Final Billing Reconciliation | Trade, Project & Wholesale |
| W1147 | Customer B2B Project Material Return Window Management & Excess Inventory Reconciliation | Trade, Project & Wholesale |
| W1149 | Customer Multi-Store Consolidated Purchase & Single Invoice Billing | Trade, Project & Wholesale |
| W1153 | Customer B2B Standing Order Seasonal Volume Adjustment & Forecast Sharing | Trade, Project & Wholesale |
| W1161 | Customer B2B Annual Volume Rebate Tier Qualification Tracking & Earned Benefit Management | Trade, Project & Wholesale |
| W598 | Wholesale Pricing & Quotation Management | Trade, Project & Wholesale |
| W599 | Wholesale Returns, Credit & Adjustment Processing | Trade, Project & Wholesale |
| W704 | Wholesale Customer Contract Renewal & Tier Reclassification | Trade, Project & Wholesale |
| W792 | Project Change Order Management & Margin Re-Impact Assessment | Trade, Project & Wholesale |
| W793 | Project Close-Out, Final Reconciliation & Warranty Handover | Trade, Project & Wholesale |
| W810 | Wholesale Backorder Management, Allocation & Customer Communication | Trade, Project & Wholesale |
| W811 | Wholesale Delivery Proof, Discrepancy Resolution & POD Reconciliation | Trade, Project & Wholesale |
| W918 | Customer Project Budget Tracking & Material Cost Variance Management | Trade, Project & Wholesale |
| W972 | Customer Franchise & Dealer Mini-Store Program Management | Trade, Project & Wholesale |
| W979 | Customer B2B Blanket Purchase Agreement & Scheduled Call-Off Management | Trade, Project & Wholesale |
| W980 | Store-Level Customer Construction Site Delivery Scheduling & Multi-Drop Coordination (B2B) | Trade, Project & Wholesale |
| W1036 | Customer Digital Product Passport & Sustainability Information Access | Customer Experience & Loyalty |
| W507 | Customer Complaint Root Cause Analysis & Systemic Improvement | Customer Experience & Loyalty |
| W508 | Customer Account Maintenance & B2B Information Update | Customer Experience & Loyalty |
| W673 | Customer Segmentation & Target Marketing Operations | Customer Experience & Loyalty |
| W674 | Customer Loyalty Program Partner Management | Customer Experience & Loyalty |
| W707 | Omnichannel Returns & Refund Orchestration | Customer Experience & Loyalty |
| W708 | Customer Communication Management & Proactive Notification Operations | Customer Experience & Loyalty |
| W735 | Customer Onboarding Journey Management & First-90-Day Engagement | Customer Experience & Loyalty |
| W756 | Customer Post-Purchase Follow-Up & Satisfaction Verification | Customer Experience & Loyalty |
| W757 | Customer On-the-Spot Loyalty Tier Upgrade Offer Processing | Customer Experience & Loyalty |
| W781 | Customer Store Credit Issuance & Lifecycle Management | Customer Experience & Loyalty |
| W782 | Customer B2B Order-to-Cash Cycle Monitoring & Proactive Communication | Customer Experience & Loyalty |
| W783 | Customer Credit Application Scoring & Risk Assessment Processing | Customer Experience & Loyalty |
| W820 | Customer Project BOM Estimation & Material Planning Service | Customer Experience & Loyalty |
| W821 | Customer Project Warranty Registration & Multi-Year Tracking | Customer Experience & Loyalty |
| W822 | Customer Loyalty Tier Benefit Fulfillment & Welcome Package Processing | Customer Experience & Loyalty |
| W894 | Customer Project Material List (BOM) Save, Share & Reorder Service ("Project Vault") | Customer Experience & Loyalty |
| W895 | Store-Level Pro Desk Appointment Scheduling & Priority Service Queue Management | Customer Experience & Loyalty |
| W914 | Customer Project Completion Celebration & Review Incentive Program | Customer Experience & Loyalty |
| W928 | Customer Price Protection & Price Adjustment Policy Processing | Customer Experience & Loyalty |
| W933 | Customer Loyalty Account Deceased Member Processing & Points Estate Transfer | Customer Experience & Loyalty |
| W936 | Customer B2B Self-Service Portal Order Management & Account Access | Customer Experience & Loyalty |
| W942 | Customer Loyalty Family/Household Account Linking & Shared Benefits Management | Customer Experience & Loyalty |
| W969 | Customer Quick Reorder from Purchase History (Trade & Loyalty Members) | Customer Experience & Loyalty |
| W5297 | Cooperative Partner Account Creation & Initial Contact | B2B Cooperative Credit & Procurement |
| W5301 | Tripartite Credit Agreement Drafting & Legal Sign-off | B2B Cooperative Credit & Procurement |
| W5303 | Cooperative Guarantor Setup and Surety Bond Validation | B2B Cooperative Credit & Procurement |
| W5308 | Multi-Member Group Purchase Discount Routing | B2B Cooperative Credit & Procurement |
| W5310 | Cooperative Account Payment Posting and Cash Application | B2B Cooperative Credit & Procurement |
| W5311 | Cooperative Credit Hold Flagging and Delinquency Lockout | B2B Cooperative Credit & Procurement |
| W5312 | Dispute Resolution for Member Unauthorized Purchases | B2B Cooperative Credit & Procurement |
| W5313 | Quarterly Cooperative Purchase Volume Accumulation Audit | B2B Cooperative Credit & Procurement |
| W5314 | Patronage Rebate Calculation & Tier Matching | B2B Cooperative Credit & Procurement |
| W5316 | Rebate Credit Memo Issuance and Voucher Disbursement | B2B Cooperative Credit & Procurement |
| W5317 | Joint Cooperative Community Build Project Procurement Scoping | B2B Cooperative Credit & Procurement |
| W5318 | Cooperative Social Fund Contribution Routing & CSR Verification | B2B Cooperative Credit & Procurement |
| W5319 | Annual Cooperative General Assembly Partnership Review | B2B Cooperative Credit & Procurement |
| W5322 | Construction Equipment Vendor Selection, Procurement & Fleet Acquisition | Construction Equipment Rental Fleet |
| W5323 | Rental Equipment Yard, Wash Bay & Heavy-Equipment Storage Infrastructure Setup | Construction Equipment Rental Fleet |
| W5326 | Rental Operator Certification, Customer Pre-Qualification & Credit/License Vetting | Construction Equipment Rental Fleet |
| W5327 | Heavy Equipment Insurance, Collision Damage Waiver (CDW) & Liability Program Setup | Construction Equipment Rental Fleet |
| W5328 | Equipment Rental Catalog, Merchandising & Digital Booking Channel Integration | Construction Equipment Rental Fleet |
| W5329 | Heavy Equipment Reservation, Quoting & Rental Agreement Generation | Construction Equipment Rental Fleet |
| W5330 | Equipment Pre-Rental Inspection, Safety Briefing & Operator Handover | Construction Equipment Rental Fleet |
| W5331 | Customer Equipment Transport, Delivery-to-Jobsite & Pickup Logistics | Construction Equipment Rental Fleet |
| W5333 | Equipment Extension, Rollover, Early Return & Re-rental Processing | Construction Equipment Rental Fleet |
| W5334 | Heavy Equipment Return Inspection, Damage Assessment & Repair Cost Recovery | Construction Equipment Rental Fleet |
| W5336 | Lost, Stolen or Abandoned Equipment Recovery, Recovery Agent & Police Coordination | Construction Equipment Rental Fleet |
| W5337 | Heavy Equipment Preventive Maintenance Schedule, Service Bay & Mechanic Operations | Construction Equipment Rental Fleet |
| W5343 | Fleet Age, Lifecycle Replacement, Disposition & Trade-In Management | Construction Equipment Rental Fleet |

#### Finance

| ID | Workflow | Value Stream |
|---|---|---|
| W489 | Store-Level Operating Budget & Cost Control | Procure-to-Pay |
| W500 | Transfer Order In-Transit Damage Claim & Resolution | Procure-to-Pay |
| W613 | Store-Level Weekly Payroll Accrual & Labor Cost Flash Report | Procure-to-Pay |
| W714 | Store-Level Daily Financial Summary Reporting & Flash P&L | Procure-to-Pay |
| W770 | AP Vendor Debit Memo Processing & Account Deduction Management | Procure-to-Pay |
| W712 | Financial Restatement & Prior-Year Adjustment Processing | Order-to-Cash |
| W892 | Customer Statement Generation & Distribution | Order-to-Cash |
| W482 | Annual Stockholders' Meeting (ASHM) Management | Record-to-Report |
| W610 | Insurance Claims Processing & Recovery Management | Record-to-Report |
| W639 | Rolling Forecast & Financial Scenario Planning | Record-to-Report |
| W85 | Product Costing & Margin Analysis Review | Record-to-Report |
| W5201 | Developer Bank-Escrow Agreement Review, Onboarding & Credit Setup | B2B Project Financing & Escrow |
| W5203 | B2B Project Materials Requirements Forecasting & Staging Plan | B2B Project Financing & Escrow |
| W5204 | Bank Escrow Financing Trust Account System Mapping | B2B Project Financing & Escrow |
| W5206 | Developer Project Escrow Funding Verification & Collateral Assessment | B2B Project Financing & Escrow |
| W5207 | Escrow Bank Agent Communication Protocols & Portal Integrations | B2B Project Financing & Escrow |
| W5210 | Bank Inspector Joint Quantity Survey (JQS) Staging & Schedule Coordination | B2B Project Financing & Escrow |
| W5211 | Escrow Draw Request Documentation Assembly & Submission | B2B Project Financing & Escrow |
| W5212 | Bank Escrow Agent Inspector Audits & Deviation Clarification | B2B Project Financing & Escrow |
| W5214 | Project Retainage (Milestone Retention Money) Accounting & Release Tracking | B2B Project Financing & Escrow |
| W5215 | Project Escrow Payment Dispute, Resolution & Negotiation | B2B Project Financing & Escrow |
| W5217 | Conditional Progress Waiver of Lien Issuance (upon Delivery) | B2B Project Financing & Escrow |
| W5220 | Project Escrow Delay Credit-Hold Hold-and-Release Execution | B2B Project Financing & Escrow |
| W5221 | Developer-Subcontractor Tripartite Payment Agreement Governance | B2B Project Financing & Escrow |
| W5222 | Project-Restricted Inventory Allocation Hold & Release Control | B2B Project Financing & Escrow |
| W5223 | Progressive Billing Audit, Revenue Leakage Prevention & Internal Control Review | B2B Project Financing & Escrow |
| W5369 | Floor-Plan & Dealer Financing Program Strategy, Product Design & Risk Appetite | Trade Reseller Floor-Plan Financing |
| W5370 | Dealer Eligibility, Credit Underwriting & Floor-Plan Limit Setting | Trade Reseller Floor-Plan Financing |
| W5371 | Dealer Floor-Plan Agreement, Security Agreement & Collateral Perfection (Civil Code Pledge) | Trade Reseller Floor-Plan Financing |
| W5373 | Floor-Plan Financing Funding Source, Bank Credit Line & Capital Allocation | Trade Reseller Floor-Plan Financing |
| W5374 | Dealer Onboarding, System Integration & Inventory Reporting Feed Setup | Trade Reseller Floor-Plan Financing |
| W5375 | Floor-Plan Pricing, Interest/Markup Rate Structure & Subvention/Manufacturer Support | Trade Reseller Floor-Plan Financing |
| W5377 | Dealer Purchase/Floor-Plan Funding Request & Loan Origination | Trade Reseller Floor-Plan Financing |
| W5379 | Unit-Level Collateral Registration, Serial/VIN Tracking & Floor-Plan Ledger Posting | Trade Reseller Floor-Plan Financing |
| W5380 | Dealer Inventory Movement, Transfer & Subordinate-Lien Notification | Trade Reseller Floor-Plan Financing |
| W5382 | Sold-Unit Reporting, Curtailment Schedule & Floor-Plan Paydown Processing | Trade Reseller Floor-Plan Financing |
| W5383 | Floor-Plan Interest/Markup Accrual, Billing & Dealer Statement Generation | Trade Reseller Floor-Plan Financing |
| W5385 | Dealer Aging, Curtailment Default & Out-of-Trust (OOT) Detection | Trade Reseller Floor-Plan Financing |
| W5387 | Collateral Repossession, Redemption & Disposition of Defaulted Floor-Plan Units | Trade Reseller Floor-Plan Financing |
| W5389 | Loss Provisioning, Charge-off & Recovery Accounting for Floor-Plan Losses | Trade Reseller Floor-Plan Financing |
| W5393 | Receivables Financing Strategy, Instrument Selection & Working-Capital Plan | Trade Receivables Factoring |
| W5394 | Factor/Funder Selection, Facility Negotiation & Master Factoring Agreement | Trade Receivables Factoring |
| W5395 | Eligible-Receivable Criteria, Concentration Limits & Advance-Rate Framework | Trade Receivables Factoring |
| W5396 | Customer Notification Strategy (Notification vs. Silent/Confidential Factoring) | Trade Receivables Factoring |
| W5397 | Receivables Sale Accounting Design, True-Sale/Off-Balance-Sheet Opinion & Derecognition (PFRS 9) | Trade Receivables Factoring |
| W5398 | Factoring/Securitization Platform, Lockbox & Remittance Infrastructure Setup | Trade Receivables Factoring |
| W5399 | Dilution, Reserve & Holdback Modeling, and Credit-Protection/Insurance Sourcing | Trade Receivables Factoring |
| W5401 | Eligible Invoice Batch Selection, Pooling & Submission to Factor | Trade Receivables Factoring |
| W5403 | Customer Invoice Reissuance/Re-assignment & Remit-To Instruction Update | Trade Receivables Factoring |
| W5405 | Non-Recourse Credit Risk Event, Customer Dispute & Short-Pay Handling | Trade Receivables Factoring |
| W5407 | Recourse Period Expiry, Unpaid-Invoice Buyback & Repurchase Processing | Trade Receivables Factoring |
| W5408 | Securitization Pool Reporting, Investor/Trustee Reporting & Servicing | Trade Receivables Factoring |
| W5410 | Receivables Aging, Sub-Limits, Concentration & Pool Health Monitoring | Trade Receivables Factoring |
| W5411 | Customer Notification Compliance, Audit-Trail & Dispute/Query Handling | Trade Receivables Factoring |
| W5412 | Recourse Exposure, Bad-Debt Buyback Reserve & ECL Provisioning (PFRS 9) | Trade Receivables Factoring |
| W5413 | Factor Performance, Dispute Rate & Service-Level Monitoring | Trade Receivables Factoring |

#### People

| ID | Workflow | Value Stream |
|---|---|---|
| W493 | Labor Union & Collective Bargaining Management | Hire-to-Retire |
| W511 | Employee Cross-Entity & Cross-Location Transfer Processing | Hire-to-Retire |
| W555 | Seasonal & Temporary Staffing Process | Hire-to-Retire |
| W567 | Employee Cross-Training & Skill Matrix Management | Hire-to-Retire |
| W641 | Off-Cycle & Ad-Hoc Payment Processing | Hire-to-Retire |
| W754 | Store-Level New Hire First-30-Day Performance Check-In & Early Intervention | Hire-to-Retire |
| W779 | Store-Level Employee Injury Incident Reporting & Workers' Compensation Claim Processing | Hire-to-Retire |
| W5250 | Technical-Vocational Institution TVI Partner Screening and SLA | DTS & TESDA Partnership |
| W5251 | DTS Training Plan and Curriculum Design Collaboration | DTS & TESDA Partnership |
| W5252 | Student Recruitment Interviewing and Intake Scheduling | DTS & TESDA Partnership |
| W5253 | DTS Program Onboarding Safety Induction and Uniform Issuance | DTS & TESDA Partnership |
| W5254 | Student-Trainee Profiling and Non-Employee Profile Provisioning | DTS & TESDA Partnership |
| W5255 | TVI Coordinator Communication Portal and Escalation Matrix Setup | DTS & TESDA Partnership |
| W5256 | Annual DTS Partnership Performance Audit and Contract Renewal | DTS & TESDA Partnership |
| W5257 | Student Biometric Time and Attendance Monitoring | DTS & TESDA Partnership |
| W5258 | In-Store Skills Mentoring Trainee Logbook and Output Verification | DTS & TESDA Partnership |
| W5259 | Store Department Rotation and Skills Diversification Scheduling | DTS & TESDA Partnership |
| W5261 | Mid-Term Practical Evaluation and Skills Competency Sign-off | DTS & TESDA Partnership |
| W5262 | Trainee Grievance Handling Harassment Guard and Well-being Check | DTS & TESDA Partnership |
| W5263 | DTS Trainee Graduation TESDA Assessment and Certification Support | DTS & TESDA Partnership |
| W5264 | Permanent Employment Transition Interviewing and Store Placement | DTS & TESDA Partnership |
| W5270 | Internal Audit of DTS Program Compliance and Policy Adherence | DTS & TESDA Partnership |

#### Asset & Infrastructure

| ID | Workflow | Value Stream |
|---|---|---|
| W5129 | Store Footprint Expansion Site Suitability & Strategic Assessment | Landbanking & Site Acquisition |
| W5130 | Land Ownership Search, Title Verification & Due Diligence | Landbanking & Site Acquisition |
| W5133 | Boundary Dispute, Land Survey & Technical Description Verification | Landbanking & Site Acquisition |
| W5134 | Deed of Absolute Sale (DOAS) Negotiation, Drafting & Execution | Landbanking & Site Acquisition |
| W5135 | Registry of Deeds (RD) Title Transfer & Registration | Landbanking & Site Acquisition |
| W5141 | Agricultural-to-Commercial Land Reclassification Application (LGU level) | Landbanking & Site Acquisition |
| W5145 | Joint-Venture (JV) Landowner Development Agreement Negotiation & Structuring | Landbanking & Site Acquisition |
| W5147 | LGU Comprehensive Land Use Plan (CLUP) Conformity & Zoning Variance Application | Landbanking & Site Acquisition |
| W5148 | Barangay Clearance, Road Right-of-Way (RROW) & Easement Agreement Negotiation | Landbanking & Site Acquisition |
| W5150 | Groundbreaking Site Mobilization & Fencing Permit Management | Landbanking & Site Acquisition |
| W5151 | Site Development Capex Budgeting & Milestone Release | Landbanking & Site Acquisition |
| W5152 | Site Handover to Construction Project PMO | Landbanking & Site Acquisition |
| W5273 | Disaster Incident Staging and Physical Site Access Control | Post-Disaster Store Reconstruction |
| W5274 | Rapid Structural Integrity and Safety Assessment | Post-Disaster Store Reconstruction |
| W5275 | Detailed Technical Damage Quantification and Geodetic Survey | Post-Disaster Store Reconstruction |
| W5276 | Insurance Loss Adjuster Audit Coordination and Proof of Loss Submission | Post-Disaster Store Reconstruction |
| W5277 | Emergency Scrap Defective Inventory and Asset Disposal Routing | Post-Disaster Store Reconstruction |
| W5279 | LGU Civil Defense / Building Official Coordination | Post-Disaster Store Reconstruction |
| W5280 | Post-Disaster Incident Review and Hazard Mapping Update | Post-Disaster Store Reconstruction |
| W5281 | Post-Disaster Rebuilding CAPA Budget Approval and Financing Setup | Post-Disaster Store Reconstruction |
| W5282 | Fast-Track Construction Contractor Vetting and Procurement SLA | Post-Disaster Store Reconstruction |
| W5283 | Site Reconstruction PMO Activation and Schedule Coordination | Post-Disaster Store Reconstruction |
| W5284 | Rebuilding Site Safety Fencing and Public Access Exclusion | Post-Disaster Store Reconstruction |
| W5285 | Building Systems HVAC Electrical MEP Refurbishment | Post-Disaster Store Reconstruction |
| W5288 | Reconstructed Store Facility Inspection and Commissioning Sign-off | Post-Disaster Store Reconstruction |
| W5294 | High-Priority Safety and Reconstruction Material Stocking | Post-Disaster Store Reconstruction |
| W5295 | Temporary Site Handover and Store Manager Operations Sign-off | Post-Disaster Store Reconstruction |
| W5296 | Temporary Facility Decommissioning and Site Re-entry Checklist | Post-Disaster Store Reconstruction |

#### Governance & Assurance

| ID | Workflow | Value Stream |
|---|---|---|
| W484 | Pandemic/Epidemic Business Response Protocol | Compliance & Regulatory |
| W626 | Enterprise Risk Register Maintenance & Quarterly Risk Review | Compliance & Regulatory |
| W627 | Product Recall Effectiveness Verification & Post-Recall Review | Compliance & Regulatory |
| W685 | Business Continuity Plan Maintenance & Annual BIA Refresh | Compliance & Regulatory |
| W802 | LGU Local Business Tax Computation, Payment & Receipt Management | Compliance & Regulatory |
| W961 | BSP Anti-Money Laundering (AML) Covered Transaction Reporting | Compliance & Regulatory |
| W805 | Workers' Compensation, SSS/ECC Claims & Return-to-Work Processing | Health, Safety & Environment |
| W862 | Insurance Policy Annual Renewal & Coverage Review | Business Continuity & Insurance |
| W863 | Third-Party Liability Claim & Customer Incident Insurance Response | Business Continuity & Insurance |
| W5153 | Plastic Packaging Footprint Baseline Audit & Material Taxonomy Setup | EPR Compliance & Plastic Recovery |
| W5155 | Inbound Supplier Plastic/Packaging Certification Audit | EPR Compliance & Plastic Recovery |
| W5156 | Private Label Packaging Material Substitution & Eco-Design Review | EPR Compliance & Plastic Recovery |
| W5159 | Producer Responsibility Organization (PRO) Enrollment & SLA Management | EPR Compliance & Plastic Recovery |
| W5160 | EPR Budgeting, Cost Allocation & Plastic Fee Management | EPR Compliance & Plastic Recovery |
| W5162 | LGU/MRF (Materials Recovery Facility) Plastic Waste Recovery Collaboration | EPR Compliance & Plastic Recovery |
| W5163 | Junk Shop & Informal Waste Collector Network Registration & Incentivization | EPR Compliance & Plastic Recovery |
| W5165 | Cement Kiln Co-Processing Partnership Agreement & Recovery Logistics | EPR Compliance & Plastic Recovery |
| W5166 | Mechanical Recycling Partner Onboarding, Sourcing & Recovery Logistics | EPR Compliance & Plastic Recovery |
| W5167 | Waste-to-Energy (WTE) Co-processing Certification & Recovery Audit Trails | EPR Compliance & Plastic Recovery |
| W5168 | Multi-Region Recovery Operations Safety & OSH Compliance | EPR Compliance & Plastic Recovery |
| W5170 | EPR Recovery Credit Purchase Agreement (RCPA) Negotiation & Trading | EPR Compliance & Plastic Recovery |
| W5174 | EPR Program Variance Analysis, Penalty Provisioning & Remediation | EPR Compliance & Plastic Recovery |
| W5175 | Plastic Reduction / Eco-Fulfillment Consumer Marketing Support | EPR Compliance & Plastic Recovery |
| W5345 | Product Stewardship & Take-Back Program Strategy, Scope & Regulatory Mapping | Household Hazardous Waste Take-Back |
| W5348 | Manufacturer/Brand Stewardship Partnership, Co-Funding & EPR Alignment | Household Hazardous Waste Take-Back |
| W5350 | Take-Back Acceptance Policy, Eligibility, Quantity Limits & Customer Incentive Program | Household Hazardous Waste Take-Back |
| W5352 | Take-Back Program Digital Platform, Customer Lookup & Awareness Campaign | Household Hazardous Waste Take-Back |
| W5353 | Customer Paint Take-Back, Latex/Oil Sorting & Usable Paint Reblending (PaintCare) | Household Hazardous Waste Take-Back |
| W5357 | Pesticide, Garden Chemical & Solvent Take-Back & Restricted-Substance Handling | Household Hazardous Waste Take-Back |
| W5358 | Consumer E-Waste, Power Tool & Appliance Take-Back & Data-Bearing Device Sanitization | Household Hazardous Waste Take-Back |
| W5359 | Propane/LPG Cylinder Take-Back, Condemned-Cylinder Handling & Cross-link to VS-175 | Household Hazardous Waste Take-Back |
| W5361 | TSD Facility Processing, Recovery, Recycling & Energy-Recovery Verification | Household Hazardous Waste Take-Back |
| W5362 | Latex Paint Reblending, Donation-to-Community & Reuse-Product Sales Channel | Household Hazardous Waste Take-Back |
| W5363 | Hazardous Waste Disposal, Incineration/Cement-Kiln & Landfill Diversion Tracking | Household Hazardous Waste Take-Back |
| W5365 | Product Stewardship Compliance Audit, TPRM of Transporters/TSD & Regulatory Inspection Response | Household Hazardous Waste Take-Back |
| W5366 | Take-Back Program Incident, Spill/Leak & Exposure Response | Household Hazardous Waste Take-Back |

#### Technology & Data

| ID | Workflow | Value Stream |
|---|---|---|
| W684 | Business Intelligence Report Development & Governance Lifecycle | IT Operations & Security |
| W709 | Enterprise Data Governance & Quality Management Operations | IT Operations & Security |
| W734 | Data Quality Daily Triage & Remediation Operations | IT Operations & Security |
| W787 | ERP System Monthly Performance Review & Capacity Planning Update | IT Operations & Security |
| W5417 | OT/ICS Asset Discovery, Inventory & Cyber Risk Taxonomy | OT/ICS Cybersecurity |
| W5418 | OT Security Architecture, Purdue-Model Zone Design & IT/OT Segmentation | OT/ICS Cybersecurity |
| W5419 | OT Identity, Credential & Role-Based Access Control Governance | OT/ICS Cybersecurity |
| W5420 | OT Device Hardening, Secure Configuration Baseline & Change Control | OT/ICS Cybersecurity |
| W5421 | Connected-Retail-Device Onboarding Security Gate (POS, SCO, RF, Locker, EV, BMS) | OT/ICS Cybersecurity |
| W5422 | OT Network Architecture Review, Firewall Rule & Zone-Boundary Lifecycle | OT/ICS Cybersecurity |
| W5423 | OT Asset End-of-Life Security, Secure Decommissioning & Cryptographic Erase | OT/ICS Cybersecurity |
| W5424 | OT Security Posture Dashboard, Criticality Tiering & Risk Acceptance Register | OT/ICS Cybersecurity |
| W5425 | OT Monitoring, Detection (OT-IDS) & SIEM Correlation Operations | OT/ICS Cybersecurity |
| W5426 | OT Threat Intelligence, ICS-CERT/Advisory Triage & Indicator Management | OT/ICS Cybersecurity |
| W5427 | OT Vulnerability Management, CVE Triage & Risk-Based Patch/Compensating-Control | OT/ICS Cybersecurity |
| W5428 | OT Patch, Firmware & PLC-Update Change-Window Management | OT/ICS Cybersecurity |
| W5429 | OT Cyber Drill, Tabletop & Cross-Functional (IT/OT/HSE) Exercise Program | OT/ICS Cybersecurity |
| W5433 | OT-Aware Third-Party / Vendor Remote-Access Governance & Session Recording | OT/ICS Cybersecurity |
| W5434 | OT Cyber Supply-Chain & SBOM Risk Management | OT/ICS Cybersecurity |
| W5438 | OT Cyber Awareness, Engineering-Workstation Hygiene & Insider-Threat Controls | OT/ICS Cybersecurity |
| W5439 | Connected-Channel (POS/SCO/EV/Locker/BMS) Cyber Coordination & Incident Liaison | OT/ICS Cybersecurity |

#### Post-Catalog Confirmation (2026-09-02)

Six post-catalog workflows confirmed **Tier 2** — standard operational support: four adopted at the keyword-proposed tier (W5499 director education, W5500 WCAG accessibility program, W5502 financial wellness, W5506 price-change approval/propagation) and two demoted from the keyword-proposed Tier 1 because the `barcode` core-transactional keyword is incidental to their billing/recovery core (W5507 concession service-fee billing; W5510 supplier service-fee billing & account deduction — the W1614 chargeback-pattern class). Rows in family order (Governance & Assurance, Sell & Serve, People, Finance):

| ID | Workflow | Value Stream |
|---|---|---|
| W5499 | Director Induction, Onboarding & Continuing Board Education Program | Corporate Governance |
| W5500 | Customer Digital Accessibility Program — WCAG 2.1 AA Compliance for Web, App & Digital Channels | Ecommerce & Digital Channels |
| W5502 | Employee Financial Wellness Program — Literacy Education, Salary-Linked Lender Governance & Debt-Stress Support | Occupational Health & Employee Wellness |
| W5506 | Concessionaire Self-Service Price Change Request, Approval & Store-Level Propagation | Store Operations |
| W5507 | Concession Service-Fee Billing & Cost Recovery for Labels, Barcode Changes & Admin Services | Store Operations |
| W5510 | Supplier Service-Fee Billing & Account Deduction for Store-Rendered Services (Barcode Labels & Promotional Collaterals) | Procure-to-Pay |

#### Event-Custody Pass (2026-09-03)

The event-custody pass added one workflow-level gap fill and confirmed it directly **Tier 2** — the finance-operations class of its W2158–W2165 VS-54.3 siblings (the statutory escheat filing rides the Legal Counsel gate inside the workflow rather than a standalone statutory register, matching the sibling pattern where statutory execution lives in VS-79/VS-118 registers):

| ID | Workflow | Value Stream |
|---|---|---|
| W5511 | Gift Card Dormancy Monitoring, Escheat Evaluation & Expired-Liability Derecognition | Gift Card & Stored Value Management |

#### Agentic-AI Platform Gap-Fill Pass (2026-09-03)

The agentic gap-fill pass added three workflows and confirmed them directly **Tier 2** — the lifecycle-operations class of their PA-128.3 siblings (W3945–W3948 model lifecycle ops); the hard-boundary dimension (no statutory filings, no POS/OT, no SoD conflicts) rides W5513's ratification gate inside the workflow rather than a standalone statutory register:

| ID | Workflow | Value Stream |
|---|---|---|
| W5512 | Agentic Candidate Intake, Sourcing Routing & Agent Registry Registration | AI/ML Governance & Responsible AI |
| W5513 | Agent Shadow & Canary Evaluation, Graduation & Autonomy-Tier Ratification | AI/ML Governance & Responsible AI |
| W5514 | Agent Runtime Operations, Guardrail & Kill-Switch Telemetry, Quarterly Re-Registration & Portfolio Sunset | AI/ML Governance & Responsible AI |

#### Sourcing-Model Gap-Fill Pass (2026-09-03)

The sourcing-model gap-fill pass added three workflows and confirmed them directly **Tier 2** — the governance/lifecycle-operations class of their VS-113 siblings (W3588/W3589); the contract-clause dimension (RA 10173 data-residency terms, statutory-readiness warranties) rides W5516's Step-3 verification gate inside the workflow rather than a standalone statutory register:

| ID | Workflow | Value Stream |
|---|---|---|
| W5515 | Sourcing Decision Gate Operation & Capability Sourcing Register | Enterprise Architecture, Application Portfolio & Technology Strategy |
| W5516 | Best-of-Breed Product Lifecycle Management, Vendor Release Intake & Exit Reserves | Enterprise Architecture, Application Portfolio & Technology Strategy |
| W5517 | SEP Paved Road & Engineering Standard Governance for Built Products | Enterprise Architecture, Application Portfolio & Technology Strategy |

#### IT Operating-Model Gap-Fill Pass (2026-09-03)

The IT gap-fill pass added five workflows and confirmed them directly **Tier 2** — the infrastructure-operations and governance/assurance class of their VS-27 siblings (W366 network ops, W367 vulnerability ops, W387 ITGC CSA, W1409 CAB); the statutory dimension (RA 10173 proportionality for W5524's employee monitoring, BIR CAS timestamp integrity inside W5520) rides verification steps inside the workflows rather than standalone statutory registers, matching the W5513/W5515 sibling pattern:

| ID | Workflow | Value Stream |
|---|---|---|
| W5518 | Collaboration & Productivity Platform (M365/Email/Teams) Operations & Tenant Governance | IT Operations & Security |
| W5520 | Core Network Services & IPAM (DNS/DHCP/IP-Schema) Management | IT Operations & Security |
| W5521 | Enterprise Release Calendar & Peak-Season Change-Freeze Governance | IT Operations & Security |
| W5522 | ISMS Program, Security Certification & Security-Policy Lifecycle (ISO/IEC 27001) | IT Operations & Security |
| W5524 | Enterprise DLP & Insider-Risk Monitoring (Endpoint/Email/Cloud) | IT Operations & Security |

#### People-Capability & Reporting-Policy Gap-Fill Pass (2026-09-03)

The people-capability gap fill added four workflows and confirmed them directly **Tier 2** — the platform-operations, governance-layer and program-support class of their PA siblings (W3351 HRIS administration, W51 training programs, W9 financial close); the statutory dimension (OSH training-record evidence in W5525, mandatory pass/fail regulatory courses in W5526) rides verification steps inside the workflows, matching the W5513/W5515/W5518 sibling pattern:

| ID | Workflow | Value Stream |
|---|---|---|
| W5525 | Learning Platform (LMS) Administration, Integration & Learning-Records Operations | Hire-to-Retire |
| W5526 | Learning-Content Development, Course-Catalog & Certification-Program Lifecycle | Hire-to-Retire |
| W5527 | Leadership Development & Management-Capability Program (HiPo Development) | Hire-to-Retire |
| W5528 | Accounting Policy, Technical Accounting (PFRS) Position & New-Standard Adoption Governance | Record-to-Report |

#### Finance-Workflow Gap-Fill Pass (2026-09-03)

The finance-workflow gap fill added one workflow confirmed directly **Tier 2** — the treasury-asset-lifecycle class of its PA siblings (W1867 landlord security-deposit management, W317 bank-account lifecycle): the deposits-paid register rides the same finance-operations machinery without a statutory filing dependency:

| ID | Workflow | Value Stream |
|---|---|---|
| W5529 | Utility, Telecommunications & Site Deposits Paid — Register, Interest Reconciliation, Surety Replacement & Recovery-on-Closure | Property & Lease Administration |

#### Operations-Workflow Gap-Fill Pass (2026-09-04)

The operations-workflow gap fill added two workflows confirmed directly **Tier 2** — the platform-operations class of W5525/W3351 (W5532, the T&A/biometric estate whose exception queues W561/W594 already own) and the physical-security control class of W1477/W1478 (W5534, the property-exit sibling of the people/visitor gate controls):

| ID | Workflow | Value Stream |
|---|---|---|
| W5532 | Workforce Time & Attendance (Biometric/Time-Clock) Platform Estate & Punch-Data Operations | Hire-to-Retire |
| W5534 | Company-Property Gate Pass & Asset-Exit Control (Stores, DCs & HQ) | Loss Prevention & Asset Protection |

#### Demand-Intake Gap-Fill Pass (2026-09-04)

The demand-intake gap fill added one workflow confirmed directly **Tier 2** — the governance/lifecycle-operations class of its VS-113 siblings (W5515 gate, W5516 BoB lifecycle): the stakeholder front door that receives, triages, and routes capability demand upstream of the sourcing gate — the statutory-free routing dimension (the front door routes and never executes statutory filings) rides the workflow's own accepted/routed/declined state:

| ID | Workflow | Value Stream |
|---|---|---|
| W5535 | Capability Demand Intake & Backlog Triage | Enterprise Architecture, Application Portfolio & Technology Strategy |

#### Emergency & Continuity Workflow Gap-Fill Pass (2026-09-05)

The emergency & continuity workflow gap fill added five workflows confirmed directly **Tier 2** — the contingency-operations and integrity-event class of their W470/W641/W319/W3697 siblings: W5539 elevator/escalator entrapment (premises-emergency response whose life-safety medical dimension rides the Tier-1 W501 chain), W5540 payroll run failure & emergency off-cycle payment (the failure-path class of the W641 off-cycle mechanic; the statutory dimension is protected by riding W10/W1527/W1306 rather than adding a new statutory register), W5541 bank-failure/frozen-deposit contingency (the counterparty-governance class of W319/W1474), W5542 liquidity stress & payment-prioritization escalation (the covenant-breach handling class of W319 above its Tier-3 routine siblings W3382/W3400), and W5543 price-file integrity event response (the integrity-event operations class above the Tier-3 W3697 monitoring, below the Tier-1 W13/W427 execution canons):

| ID | Workflow | Value Stream |
|---|---|---|
| W5539 | Elevator & Escalator Entrapment Response Protocol | Store Operations |
| W5540 | Payroll Run Failure, Correction & Emergency Off-Cycle Payment | Hire-to-Retire |
| W5541 | Bank-Failure & Frozen-Deposit Contingency | Treasury & Cash |
| W5542 | Liquidity Stress, Covenant-Breach & Payment-Prioritization Escalation | Supply Chain Finance & Working Capital Management |
| W5543 | Price-File Integrity Event Response & Mass-Mispricing Rollback | Revenue Assurance, Pricing Integrity & Leakage Management |

#### Regulatory-Shock, Platform-Outage & Governance-Continuity Gap-Fill Pass (2026-09-05)

The batch-17 gap fill added four workflows confirmed directly **Tier 2** — the governance-continuity and platform-contingency classes: W5544 emergency executive succession & decision-rights continuity (the governance-continuity class of its PA-36.1 siblings — the emergency bridge from vacancy to interim stability, with the statutory dimensions riding W1717/W317/W1408/W5019; the permanent succession rides the W178 planning machinery), W5547 payment-network & acquirer outage response (the chain-wide tender-policy contingency class of its PA-08.1 siblings — the W535 offline layer is store-connectivity, this owns the network-side outage), W5548 stored-value & loyalty platform outage (the program-contingency class of its PA-54.2 siblings — the downtime-acceptance matrix, manual-redemption mode and liability true-up), and W5549 suicide/self-harm incident response & psychosocial aftermath (the specialized incident-handling class around the Tier-1 W501/W140 canons — scene discipline, witness care, no-speculation communication and the aftermath program):

| ID | Workflow | Value Stream |
|---|---|---|
| W5544 | Emergency Executive Succession & Decision-Rights Continuity Protocol | Corporate Governance & Board Management |
| W5547 | Payment-Network & Acquirer Outage Response (Card Scheme / Acquirer Downtime) | POS & Checkout |
| W5548 | Stored-Value & Loyalty Platform Outage, Downtime-Acceptance & Manual-Redemption Protocol | Gift Card & Stored Value Management |
| W5549 | Suicide Attempt / Self-Harm Incident Response & Psychosocial-Aftermath Protocol | Health, Safety & Environment |

#### Channel-Enforcement, Employee-Legal-Status, OSH-Enforcement & App-Store-Removal Gap-Fill Pass (2026-09-05)

The batch-18 gap fill added three workflows confirmed directly **Tier 2** — the channel-contingency and specialized-employment-event classes: W5550 marketplace account suspension, enforcement freeze & appeal recovery (the channel-enforcement class of the W5547/W5548 platform-contingency precedent — 'account suspension'/'account health'/'delisting' in zero PA files while W1470 owns only the preventive seller-metrics layer and W659 the own-platform incidents; demand re-routing, the appeal pack, the settlement-freeze accounting and the reinstatement gate), W5551 employee arrest/detention & criminal-case employment-status response (the specialized employee-relations event class — 'arrest' appeared only as a vetting trigger and an LP case-closure outcome; the leave-of-absence placement, the work-relatedness/legal-support decision, family liaison, acquittal-reinstatement and the two-notice separation gate on verified facts), and W5553 mobile app store removal & re-listing recovery (the store-distribution contingency class of the W5547/W5548 pattern — 'app store removal'/'policy violation' in zero PA files while W2647 owns listing upkeep and W2650 performance monitoring; class-specific fix paths, the appeal with remediation in hand, and the release-checklist prevention gate):

| ID | Workflow | Value Stream |
|---|---|---|
| W5550 | Marketplace Account Suspension, Enforcement Freeze & Appeal Recovery Protocol | Ecommerce & Digital Channels |
| W5551 | Employee Arrest, Detention & Criminal-Case Employment-Status Response Protocol | Hire-to-Retire |
| W5553 | Mobile App Store Removal, Policy-Violation Response & Re-Listing Recovery Protocol | Customer Digital Engagement & Mobile App Operations |

#### In-Transit-Security, Fatality-Scene, Tampering-Extortion & Recruitment-Fraud Gap-Fill Pass (2026-09-05)

The batch-19 gap fill added two workflows confirmed directly **Tier 2** — the contingency-operations and brand-integrity event classes: W5554 in-transit cargo hijacking, armed truck robbery & driver-safety first response (cargo theft is named only inside W1337's ORC intelligence background and VS-180's relief-convoy escorts — 'hijack'/'holdup'/'cargo robbery' in zero dedicated headers while W653 owns accidents, W2814 the CIT-vendor robbery, and E-21 armed violence on premises; the comply-first/no-pursuit discipline with the no-discipline guarantee, the first-hour PNP hot-pursuit escalation, the GPS/seal evidence preservation, and the carrier-liability vs own-fleet claim split had no owner; the crew-safety dimension rides the Tier-1 W501/W717 chains) and W5557 recruitment fraud & fake job-offer scam response ('recruitment scam'/'fake job'/'job scam' in zero PA files while PA-100.2's digital-IP machinery watches impersonating accounts through the customer-phishing lens — nobody owned the event whose victims arrive at BuildRight's own door: the same-day never-charges-fees advisory, the simultaneous multi-surface takedown wave via W3272, the empathy-first victim-guidance desk, and the PNP Anti-Cybercrime referral pack):

| ID | Workflow | Value Stream |
|---|---|---|
| W5554 | In-Transit Cargo Hijacking, Armed Truck Robbery & Driver-Safety First Response Protocol | Logistics & Fleet |
| W5557 | Recruitment Fraud & Fake Job-Offer Scam Response, Takedown & Victim-Guidance Protocol | Talent Acquisition, Employer Brand & Candidate Experience |

The batch-20 gap fill added three workflows confirmed directly **Tier 2** — the financial-crime contingency, landbanking asset-protection, and facility-continuity classes: W5559 vendor payment-diversion & business email compromise (BEC) fraud event response (BEC appears in the corpus only as PA-18.2 pain points — vendor bank-detail impersonation and executive-impersonation urgent transfers — with callback verification as the one-bullet mitigation, while VS-125.2's monitoring watches only the customer-side receivables diversion class; nobody owned the event after prevention fails: the same-day bank-recall race, the honest-ledger treatment that keeps the still-owed vendor's aging truthful, the master-data forensics separating insider from mailbox compromise, the PNP ACG/crime-policy files, or the cooling-off verification retrofit), W5560 informal-settler invasion & illegal occupation of banked land ('informal settler'/'squatter'/'illegal occupation'/'adverse possession' in zero PA files while W5133 owns titled-neighbor boundary disputes, W5143 the agrarian tenant program, and W5150 groundbreaking fencing only — nobody owned the detect–document–negotiate–eject lifecycle of parcels held vacant for years, the prescription-interruption evidence discipline, the RA 7279 syndicate-vs-settler classification, the no-self-help eviction rule, or the caretaker-fraud variant), and W5561 sustained water-service interruption response ('water interruption'/'water rationing' appeared only as product-selling context in PA-09.2's rainwater-harvesting advisory while W470 owns the power analog and W1387 flood owns excess water — nobody owned the absence-of-water event: the HSE-gated restroom/sanitation decision law under the store's Sanitation Permit obligations, the live-goods watering priority, emergency trucked-water procurement, the trading-continuity decision riding the E-02 closure custody, or the flush-and-confirm gate before restrooms and food services reopen after pressure loss):

| ID | Workflow | Value Stream |
|---|---|---|
| W5559 | Vendor Payment-Diversion & Business Email Compromise (BEC) Fraud Event Response & Recovery Protocol | Treasury & Cash |
| W5560 | Informal-Settler Invasion & Illegal Occupation of Banked Land — Detection, Relocation & Ejection Protocol | Landbanking & Site Acquisition |
| W5561 | Sustained Water-Service Interruption Response & Store Continuity Protocol | Store Operations |

The batch-21 gap fill added three workflows confirmed directly **Tier 2** — the brand-integrity event, payment-platform contingency, and asset-protection contingency classes: W5563 brand-impersonation commerce-scam response ('fake seller'/'scam listing' appear in zero PA files while W3271/W3272 own the takedown machinery and W5557 the recruitment variant — nobody owned the commerce-scam event whose victims arrive at stores demanding goods they 'paid' a fake seller: the empathy-first victim-arrival protocol, the same-day advisory with a single verification source of truth, the one-simultaneous-wave takedown discipline, the e-wallet recall guidance and PNP-ACG referral, or the data-harvesting variant routing to the W53 clock), W5564 mobile-wallet platform outage response (one tender-outage canon per rail: W5547 owns the card-scheme/acquirer rail and W535 the store-connectivity layer, but the wallet-provider rail — GCash/Maya-class QR/NFC authorization, provider-side — had no owner: the rail-diagnosis protocol, the tender-type directive flag, the no-manual-receipt double-charge rule, and the stranded-authorization sweep against the provider's T+1 statement), and W5565 third-party construction damage & adjacent-works response ('adjacent construction'/'neighboring construction'/'excavation damage' in zero dedicated headers while W650 executes emergency repairs with no liability discipline, W5133 owns boundary lines not damage events, and W5560 owns occupation of banked land — nobody owned the third-party-damage event: the evidence-before-repair rule with the dated crack survey and engineering baseline, the red-tag safety gate, the adjacent contractor's CAR/TPD-first claim ordering, the LGU permit-leverage track, or the monitoring regime while works continue):

| ID | Workflow | Value Stream |
|---|---|---|
| W5563 | Brand-Impersonation Commerce-Scam Response (Fake Sellers & Fraudulent Pickup Offers) | Legal Operations, Litigation & IP Management |
| W5564 | Mobile-Wallet Platform Outage Response (E-Wallet Tender Downtime) | POS & Checkout |
| W5565 | Third-Party Construction Damage & Adjacent-Works Response Protocol | Real Estate & Construction |

The batch-22 gap fill added four workflows confirmed directly **Tier 2** — the payment-device security, procurement-fraud, channel-contingency, and workforce-continuity classes: W5566 payment-terminal tampering & card-skimmer response ('card skimmer'/'tampered terminal' appear in zero PA files while W537 owns the terminal's daily operations, W1205 the PCI compliance program, and VS-125.2 transaction-level card-present fraud — nobody owned the device-compromise event: the freeze-in-place evidence rule, the chain-wide terminal-fleet sweep, the acquirer/card-brand notification duty with its 24-hour liability clock, the compromised-card population assessment, or the tamper-evident-seal retrofit into the daily check), W5567 procurement-impersonation & fake-PO goods-diversion response ('fake PO'/'fraudulent purchase order'/'supplier impersonation' appear in zero PA files while W5559 owns diverted payments on genuine obligations and W5563 fake sellers defrauding consumers — nobody owned fraudsters impersonating BuildRight as the buyer: the void-order posture with no genuine payable to freeze, the supplier-notification wave with portal-only verification, the receiving hold flags on diverted PO numbers, the insider check, or the self-verifiable order-code retrofit), W5568 official-channel account-takeover response ('account hijack'/'brand account' appear in zero PA files while W5563 owns the fake pages that only pretend to be BuildRight, W3871 customer-account ATO, and W5550 platform-side enforcement — nobody owned the takeover of BuildRight's own verified accounts, where a scam post inherits the platform's verification badge: the first-hour credential kill-chain, the platform-recovery appeal with corporate proof, the follower advisory from unaffected channels, or the W53 privacy clock where follower messages were exposed), and W5569 mass-commute disruption & transport-strike continuity ('transport strike'/'commute disruption' appear in zero PA files while W4255 responds to a single shuttle incident and the closure canon targets sites, not commutes — nobody owned the event where every site is open yet unstaffed: the attendance-forecast call, the critical-role matrix with no-penalty absence coding, the W4253-gated shuttle-surge and ride-share activation, or the customer-impact decision riding the E-02 custody):

| ID | Workflow | Value Stream |
|---|---|---|
| W5566 | Payment-Terminal Tampering & Card-Skimmer Response (PIN-Pad Compromise Event) | POS & Checkout |
| W5567 | Procurement-Impersonation & Fake-PO Goods-Diversion Response | Vendor Management & Procurement |
| W5568 | Official-Channel Account-Takeover Response (Brand-Account Hijack) | Marketing & Communications |
| W5569 | Mass-Commute Disruption & Transport-Strike Continuity Protocol | Employee Transport, Shuttle & Daily Commute Management |

The batch-23 gap fill added two workflows confirmed directly **Tier 2** — the brand-integrity comms-contingency and IT-facility-contingency classes: W5572 undercover-investigation & media-exposé response ('undercover'/'hidden camera'/'investigative report'/'right of reply' appear in zero PA files — W1562 owns recall/safety-incident media response and W3271/W3272 the fake-brand-content class, which is the *opposite* case; nobody owned genuine-fault journalism: the verification-before-response law that never rebuts unauthenticated footage, the no-obstruction rule that never dismisses or pressures a suspected source, the single-channel right-of-reply discipline with the deadline honored, the self-report calculus where the footage proves a regulatory failing, or the remediation track with audit-verifiable milestones) and W5573 server-room & data-center environmental event response ('server room'/'cooling failure'/'fire-suppression discharge' appear in zero PA files — W55 owns DR failover execution once declared, W380 alert triage, and VS-138 the base-building HVAC to the landlord boundary; nobody owned the physical-room event: the thermal-runaway clock that acts at inlet threshold, the power-before-water rule, the suppression-aftermath discipline with the certified re-arm before restart, the RTO-bounded failover decision, or the staged-repower validation):

| ID | Workflow | Value Stream |
|---|---|---|
| W5572 | Undercover-Investigation & Media-Exposé Response Protocol (Investigative-Newsroom Event) | Marketing & Communications |
| W5573 | Server-Room & Data-Center Environmental Event Response (Cooling Failure, Water Intrusion, Fire-Suppression Discharge) | IT Operations & Security |

The batch-24 gap fill added one workflow confirmed directly **Tier 2** — the concession-operations governance class: W5574 concessionaire connectivity request, approval & independent-circuit governance ('concessionaire internet'/'independent circuit'/'own internet connection' appear in zero PA files as owned surfaces — W177 treats connectivity as a bundled utility inside the monthly concessionaire invoice, W366 manages the store link and its segmented Wi-Fi, and W5520/W5421 guard the network and device boundaries, but nobody owned the request-and-exception path when a concessionaire wants its own circuit: the default-posture rule with the segmented-Wi-Fi alternative evaluated first, the eligibility gate (documented regulatory, banking or capacity need only), the isolation envelope (separate conduit, no physical or logical crossing into BuildRight networks, DHCP confined to the concessionaire's own equipment, no BuildRight credentials), the addendum clause keeping every concession sale on the BuildRight POS throughput SKU so commission never rides on connectivity choice, the incident demarcation that keeps the unmanaged circuit off the BuildRight helpdesk, and the restoration holdback released only on the W62 exit walk-through):

| ID | Workflow | Value Stream |
|---|---|---|
| W5574 | Concessionaire Connectivity Request, Approval & Independent-Circuit Governance | Store Operations |

The batch-25 gap fill added three workflows confirmed directly **Tier 2** — the in-suite customization-governance class of the W5515–W5517 siblings: W5575 the customization decision record's intake and admissibility gate, W5576 the customization register's quarterly object-inventory audit, and W5577 the de-customization and extension-retirement programme; the ARB, change-management and patch rails they invoke are already in place, so nothing here is go-live blocking.

| ID | Workflow | Value Stream |
|---|---|---|
| W5575 | Customization Decision Record (CDR) Intake, Admissibility Gate & ARB Approval | Enterprise Architecture, Application Portfolio & Technology Strategy |
| W5576 | CEMLI Register Maintenance & Quarterly Object-Inventory Audit | Enterprise Architecture, Application Portfolio & Technology Strategy |
| W5577 | Extension De-Customization, Retirement & Budget Reclamation | Enterprise Architecture, Application Portfolio & Technology Strategy |

The batch-26 gap fill added two workflows confirmed directly **Tier 2** — the EBS-documentation-coverage class: the environmental system-of-record capture behind the ESG reporting family, and the customer bill-presentment layer behind the adopted iReceivables.

| ID | Workflow | Value Stream |
|---|---|---|
| W5578 | Environmental Data Capture, Emission-Factor Governance & GHG Transaction Batch Processing | ESG & Sustainability |
| W5579 | Customer Bill Presentment Template, Assignment-Rule & Data-Source Governance | Order-to-Cash |

The capability-switchboard admission (by executive direction, 2026-09-23) added one workflow confirmed directly **Tier 2** — the online-capability governance class: **W5580 Capability Switchboard Operation & Channel Enablement Impact Governance** (PA-113.2, VS-113), the owning workflow for the channel-capability registry's state changes — cross-workflow flip-set assessment, volume re-basing, revenue/recording-vehicle impact, headcount & staffing impact (the no-silent-absorption rule), config-flip execution and canon settlement.

| ID | Workflow | Value Stream |
|---|---|---|
| W5580 | Capability Switchboard Operation & Channel Enablement Impact Governance | Enterprise Architecture, Application Portfolio & Technology Strategy |

### Tier 3 Additions (132 Workflows)

#### Plan & Source

| ID | Workflow | Value Stream |
|---|---|---|
| W624 | Competitor Store Visit Program & Market Intelligence Operations | Merchandise Strategy |
| W625 | Product Quality Lab Testing & Certification Management | Merchandise Strategy |
| W728 | Port & Customs Clearance Daily Status Tracking & Escalation | Supply Planning |
| W927 | Store-Level Rainy Season Emergency Product Deployment & Rapid Stock Replenishment | Supply Planning |
| W1087 | Store-Level Power Tool Brand Ambassador & Vendor Demo Day Event Management | Vendor Management & Procurement |
| W1099 | Store-Level Vendor-Sponsored Product Training Academy & Staff Certification Program | Vendor Management & Procurement |
| W1157 | Vendor Sustainable Packaging Assessment & Plastic Reduction Collaboration | Vendor Management & Procurement |
| W761 | Supplier Innovation & New Product Introduction Collaboration Processing | Vendor Management & Procurement |
| W865 | Vendor Portal User Onboarding, Access Provisioning & Training | Vendor Management & Procurement |
| W995 | Vendor Consignment Inventory Aging Analysis & Automatic Markdown Trigger | Vendor Management & Procurement |
| W5248 | Post-Project Margin Variance Analysis and Supplier Scorecard Review | B2B Bulk-Project Custom Import |

#### Make & Move

| ID | Workflow | Value Stream |
|---|---|---|
| W584 | DC Daily Operations & Shift Management | DC & Warehouse Operations |
| W586 | DC Daily KPI Dashboard & Performance Tracking | DC & Warehouse Operations |
| W650 | Warehouse Equipment Preventive Maintenance | DC & Warehouse Operations |
| W798 | DC Building Maintenance, Utility Operations & Facility Condition Monitoring | DC & Warehouse Operations |
| W654 | Driver Onboarding, Training & Certification | Logistics & Fleet |
| W5184 | DC-to-Store Emergency Transport Route Optimization | Disaster Relief Supply Chain Logistics |
| W5459 | Diversion Rate, Stream Composition & Circular-Economy Analytics | Construction Debris & Site Cleanup |
| W5461 | Service Performance, SLA & Customer Satisfaction Analytics | Construction Debris & Site Cleanup |
| W5462 | Vendor Scorecard, Cost-to-Serve & Hauling Optimization | Construction Debris & Site Cleanup |
| W5464 | Program Strategy, Pricing Health & Capacity Planning | Construction Debris & Site Cleanup |

#### Sell & Serve

| ID | Workflow | Value Stream |
|---|---|---|
| W1017 | Store-Level Scrap Metal & Recyclable Material Collection & Revenue Recognition | Store Operations |
| W1108 | Store-Level Forklift Operator Daily Certification Check & Compliance | Store Operations |
| W504 | Store-Level Digital Signage & Content Management | Store Operations |
| W516 | Self-Checkout (SCO) Daily Operations | POS & Checkout |
| W518 | Cashier Onboarding, POS Training & Competency Certification | POS & Checkout |
| W1027 | Customer AI-Powered Chatbot & Virtual Shopping Assistant Operations | In-Store Customer Services |
| W1071 | Customer Smart Home System Design & Product Recommendation Service | In-Store Customer Services |
| W1074 | Customer Home Office & Workspace Design Consultation Service | In-Store Customer Services |
| W1076 | Customer Garden & Outdoor Kitchen Design Consultation Service | In-Store Customer Services |
| W1082 | Store-Level Customer Construction Material Quality Verification & Grade Certification Assistance | In-Store Customer Services |
| W1088 | Customer Mortgage & Housing Loan Partner Bank Referral Desk Operations | In-Store Customer Services |
| W1096 | Customer Solar Water Heater System Sizing & Complete Package Recommendation | In-Store Customer Services |
| W1109 | Customer Project Material Surplus Buy-Back & Recycling Program | In-Store Customer Services |
| W1136 | Customer Product Knowledge Video Library & How-To Tutorial Content Management | In-Store Customer Services |
| W920 | Store-Level Vendor-Led Product Knowledge Training & Staff Certification Program | In-Store Customer Services |
| W949 | Customer AI-Powered Home Renovation Visualizer & Material Estimator | In-Store Customer Services |
| W953 | Customer Contractor Micro-Lending Partnership Program Management | In-Store Customer Services |
| W966 | Customer Construction Loan Documentation Assistance & Partner Bank Referral | In-Store Customer Services |
| W970 | Customer Post-Disaster Insurance Claim Material Replacement Coordination | In-Store Customer Services |
| W975 | Customer Home Energy Audit Referral & Energy-Efficient Product Recommendation | In-Store Customer Services |
| W990 | Customer Solar Panel System Sizing & ROI Calculator Service | In-Store Customer Services |
| W992 | Customer Garden & Landscape Design Consultation & Material Estimation Service | In-Store Customer Services |
| W510 | Ecommerce Product Review & Rating Management | Ecommerce & Digital Channels |
| W557 | E-Commerce Abandoned Cart Recovery & Retargeting | Ecommerce & Digital Channels |
| W563 | E-Commerce SEO & Digital Merchandising Management | Ecommerce & Digital Channels |
| W568 | E-Commerce Flash Sale & Limited-Time Offer Operations | Ecommerce & Digital Channels |
| W726 | Ecommerce Product Content Enrichment & Catalog Daily Operations | Ecommerce & Digital Channels |
| W828 | Ecommerce Platform Feature Release, A/B Testing & UX Optimization | Ecommerce & Digital Channels |
| W907 | Customer Consumables Subscription & Auto-Replenishment Service | Ecommerce & Digital Channels |
| W917 | Ecommerce Live Commerce & Social Selling Operations | Ecommerce & Digital Channels |
| W930 | Customer Back-in-Stock Notification Subscription & Alert Management | Ecommerce & Digital Channels |
| W934 | Ecommerce Customer Wishlist, Save-for-Later & Price Drop Alert | Ecommerce & Digital Channels |
| W940 | Ecommerce Customer Product Comparison Tool & Buying Guide Content Management | Ecommerce & Digital Channels |
| W947 | Ecommerce Live Video Shopping & Virtual Store Walkthrough | Ecommerce & Digital Channels |
| W794 | Service SKU Catalog Management, Pricing & Material Linkage | Installation & Services |
| W795 | Service Customer Complaint, Rework & Warranty Claim Management | Installation & Services |
| W898 | Store-Level Custom Paint Formula Save, Recall & Reorder Service | Installation & Services |
| W906 | Store-Level Community Workshop Space Booking & DIY Event Management | Installation & Services |
| W1039 | Customer Housewarming & New Home Gift Registry Service | Customer Experience & Loyalty |
| W1120 | Customer Loyalty Points Donation to Charity / Community Cause | Customer Experience & Loyalty |
| W566 | Mystery Shopping Program & CX Compliance Audit | Customer Experience & Loyalty |
| W618 | Customer Churn Prediction & Proactive Retention Management | Customer Experience & Loyalty |
| W904 | Store-Level Contractor Referral & Customer-Contractor Matchmaking Service | Customer Experience & Loyalty |
| W911 | Customer Digital Warranty Vault & Multi-Vendor Warranty Claim Aggregation | Customer Experience & Loyalty |
| W496 | Customer Loyalty Fraud Detection & Prevention | Marketing & Communications |
| W565 | Marketing Campaign ROI & Attribution Analysis | Marketing & Communications |
| W570 | Loyalty Points Expiry Management & Annual Liability Cleanup | Marketing & Communications |
| W676 | Digital Marketing Campaign Operations & Cross-Channel Execution | Marketing & Communications |
| W677 | Marketing Budget Management & Spend Analytics | Marketing & Communications |
| W736 | Marketing Data Platform Daily Operations & Campaign Analytics | Marketing & Communications |
| W833 | Marketing Campaign Compliance Review & Regulatory Approval | Marketing & Communications |
| W902 | Customer Loyalty Partner Reward Catalog Management & Fulfillment | Marketing & Communications |
| W909 | Customer Trade Account Co-Branded Credit Card Program Management | Marketing & Communications |
| W912 | Store-Level Customer Loyalty Points Gifting & Transfer Between Members | Marketing & Communications |
| W926 | Customer Loyalty Reward Physical Fulfillment & Partner Logistics Management | Marketing & Communications |
| W5300 | Cooperative Financial Performance Review & Balance Sheet Analysis | B2B Cooperative Credit & Procurement |
| W5320 | Cooperative Partnership Performance Analytics and Scorecard Reporting | B2B Cooperative Credit & Procurement |
| W5321 | Compact & Heavy Equipment Rental Fleet Strategy, Category Mix & Business Case | Construction Equipment Rental Fleet |
| W5324 | Heavy Equipment Rental Fleet Asset Registration, Tracking & Telematics Provisioning | Construction Equipment Rental Fleet |
| W5325 | Equipment Rental Rate Card, Pricing Structure & Competitor Benchmarking | Construction Equipment Rental Fleet |
| W5332 | In-Period Equipment Monitoring, Telematics Tracking & Misuse Detection | Construction Equipment Rental Fleet |
| W5342 | Fleet Utilization, Idle-Time, Rate-Realization & Yield Analytics | Construction Equipment Rental Fleet |

#### Finance

| ID | Workflow | Value Stream |
|---|---|---|
| W5216 | Project Progress Billing Status Dashboard & Cashflow Forecast | B2B Project Financing & Escrow |
| W5390 | Dealer Performance, Sales Velocity, Stocking Health & Relationship Analytics | Trade Reseller Floor-Plan Financing |
| W5391 | Floor-Plan Portfolio Yield, Cost-of-Funds, NPL & Profitability Analytics | Trade Reseller Floor-Plan Financing |
| W5414 | Receivables-Sale P&L, Cost-of-Funds vs. Discount Analytics & Funding-Mix Optimization | Trade Receivables Factoring |
| W5416 | Portfolio Cash-Conversion-Cycle, DSO Impact & Treasury Integration Analytics | Trade Receivables Factoring |

#### People

| ID | Workflow | Value Stream |
|---|---|---|
| W1042 | Employee Store-Level Rotational Cross-Training & Multi-Skill Certification Program | Hire-to-Retire |
| W1127 | Store-Level Employee Annual Competency Re-Certification & Skills Refresher | Hire-to-Retire |
| W683 | Employee Competency Assessment & Certification Management | Hire-to-Retire |
| W715 | Employee Referral Program Management & Reward Processing | Hire-to-Retire |
| W5271 | DTS Program Learning and Development Impact Analytics and Cost-Benefit Review | DTS & TESDA Partnership |

#### Asset & Infrastructure

| ID | Workflow | Value Stream |
|---|---|---|
| W700 | Facility Condition Assessment & Capital Planning Support | Real Estate & Construction |
| W701 | Utility Infrastructure Management & Metering Operations | Real Estate & Construction |
| W789 | Construction Safety Management & DOLE DO 13 Compliance | Real Estate & Construction |
| W790 | Construction Quality Assurance, Milestone Inspection & Material Testing | Real Estate & Construction |
| W791 | Construction Document Control, Drawing Revision & As-Built Management | Real Estate & Construction |
| W807 | Store Closure, Lease Termination & Asset Recovery Management | Real Estate & Construction |
| W808 | Generator Preventive Maintenance, Fuel Management & Load Testing | Real Estate & Construction |

#### Governance & Assurance

| ID | Workflow | Value Stream |
|---|---|---|
| W490 | Organized Retail Crime (ORC) Investigation & Task Force | Internal Audit & Risk |
| W447 | DTI-BPS Mandatory Product Certification (ICC/SOC) | Compliance & Regulatory |
| W655 | Safety Training & Certification Tracking | Health, Safety & Environment |
| W806 | Annual Fire Safety System Testing, Certification & BFP Compliance | Health, Safety & Environment |
| W692 | Store Energy Efficiency Monitoring & Utility Cost Optimization | ESG & Sustainability |
| W693 | Water Consumption Tracking & Conservation Management | ESG & Sustainability |
| W694 | ESG Data Collection, Validation & Annual Sustainability Report Preparation | ESG & Sustainability |
| W800 | Green Building Certification (BERDE/LEED) & Sustainable Store Design Standards | ESG & Sustainability |
| W801 | ESG Incident Response, Regulatory Citation Management & Stakeholder Communication | ESG & Sustainability |
| W5176 | Board-Level Sustainability/EPR Dashboard & Program Performance Review | EPR Compliance & Plastic Recovery |
| W5368 | Diversion Rate, Recycling Yield, Customer Participation & Program Impact Analytics | Household Hazardous Waste Take-Back |

#### Technology & Data

| ID | Workflow | Value Stream |
|---|---|---|
| W832 | ERP User Access Quarterly Recertification & Compliance Review | IT Operations & Security |
| W879 | Daily Report Distribution & Automated Dashboard Refresh | Data, Analytics & BI |
| W880 | BI Dashboard Development, Enhancement & User Request Management | Data, Analytics & BI |
| W881 | Data Warehouse ETL Job Monitoring & Exception Handling | Data, Analytics & BI |
| W882 | Self-Service BI Governance, Access Provisioning & Training | Data, Analytics & BI |
| W883 | Ad-hoc Analytics Request Fulfillment & SLA Management | Data, Analytics & BI |
| W884 | Data Quality Monitoring, Exception Triage & Remediation | Data, Analytics & BI |
| W885 | Monthly Executive Reporting Package Preparation | Data, Analytics & BI |
| W686 | Document Approval Routing & Digital Signature Management | Innovation & Digital Transformation |
| W687 | Document Template Management & Version Control | Innovation & Digital Transformation |
| W688 | Contract & Agreement Lifecycle Management | Innovation & Digital Transformation |
| W689 | AI/ML Model Governance, Bias Audit & Ethical Review | Innovation & Digital Transformation |
| W690 | Digital Transformation Initiative Portfolio Management | Innovation & Digital Transformation |
| W691 | Emerging Technology Scouting & Proof-of-Concept Evaluation | Innovation & Digital Transformation |
| W5432 | OT Detection Engineering, Use-Case Tuning & False-Positive Reduction | OT/ICS Cybersecurity |
| W5436 | OT Penetration Testing, Red-Team & Cyber-Physical Assessment | OT/ICS Cybersecurity |
| W5440 | OT Cybersecurity Performance, Maturity & Investment Analytics | OT/ICS Cybersecurity |


#### Post-Catalog Confirmation (2026-09-02)

Two post-catalog workflows confirmed **Tier 3** — analytics/optimization class: W5501 promoted from the keyword-proposed Tier 2 (hazard-exposure modeling, scenario definition/quantification, KRIs feeding W122's governance) and W5509 demoted from the keyword-proposed Tier 1 (substitution analytics & replenishment-feedback core; the capture layer is instrumentation). Rows in family order (Governance & Assurance, Plan & Source):

| ID | Workflow | Value Stream |
|---|---|---|
| W5501 | Climate Physical & Transition Risk Assessment, Scenario Analysis & Resilience Response Planning | Internal Audit & Risk |
| W5509 | Unfulfilled-Demand & Lost-Sales Capture, Substitution Analytics & Replenishment Feedback | Supply Planning |
#### IT Operating-Model Gap-Fill Pass (2026-09-03)

Two IT gap-fill workflows confirmed **Tier 3** — the support-layer/periodic-assurance class: W5519 (store telephony/UCC — support-layer communications with a continuity failover slice) and W5523 (enterprise pentest/red-team — periodic adversarial assurance; the annual program sits above W367's continuous operations). Both ride the absorbed-staffing statement; no statutory register dimension:

| ID | Workflow | Value Stream |
|---|---|---|
| W5519 | Enterprise Messaging & Store Telephony Services (UCC) Lifecycle | IT Operations & Security |
| W5523 | Enterprise Pentest, Red/Purple-Team & Attack-Surface Management Program | IT Operations & Security |

### Statutory-Compliance Classification Pass (192 workflows; VS-79/85/89/91/114/117/118/125)

> **Hand-reviewed 2026-06-20.** The classifier's `FAMILY_DEFAULTS` force all 8 wholly-statutory
> value streams to a blanket Tier 1 proposal. This pass confirms the statutory-*execution*
> workflows as Tier 1 and demotes 38 program-support workflows to Tier 2/3 per the documented
> tier definitions (Tier 2 = standard support / training / reporting / change-monitoring /
> cost-or-insurance recovery; Tier 3 = analytics / continuous-improvement / enhancement-only).
> Result: **154 Tier 1** (statutory execution) · **32 Tier 2** (program support) · **6 Tier 3**
> (analytics/enhancement). The 38 demotions are listed inline below each table block for audit.

#### Tier 1 — Statutory execution (154 workflows)

**Finance** (59)

| ID | Workflow | Value Stream |
|---|---|---|
| W2753 | VAT Output/Input Ledger Reconciliation & Monthly Form 2550M Preparation | VS-79 |
| W2754 | Quarterly VAT Return (2550Q) & Transitional Input Tax Processing | VS-79 |
| W2755 | BIR eFPS Filing, e-Payment (PESONet/InstaPay) & Validation | VS-79 |
| W2756 | BIR EIS E-Invoicing Transmission & Daily Sales Report Sync | VS-79 |
| W2757 | VAT-Exempt & Zero-Rated Sale Documentation (PEZA/BOI/Education/Housing) | VS-79 |
| W2758 | Capital Goods Input VAT — Full-Credit Regime & Grandfathered 60-Month Amortization Tracking | VS-79 |
| W2759 | Percentage Tax (2551Q) & Entities Below VAT Threshold Management | VS-79 |
| W2760 | POS BIR-Registered Accreditation, CAS Registration & Compliance Audit | VS-79 |
| W2761 | Expanded Withholding Tax (EWT) Determination & Quarterly Form 1601EQ | VS-79 |
| W2762 | Creditable Withholding Tax (CWT) at Source & Vendor 2307 Issuance | VS-79 |
| W2763 | Customer CWT Collection (2307) & AR Application | VS-79 |
| W2764 | Compensation Withholding Tax (1601C) & TRAIN Tax Table Maintenance | VS-79 |
| W2765 | Annual Information Return (1604E/1604C) & Alphabetical Employee List | VS-79 |
| W2766 | Final Withholding Tax (Interest, Dividends, Rentals) Management | VS-79 |
| W2767 | EWT Rate Master Governance & Tax Code Mapping | VS-79 |
| W2768 | Withholding Tax Reconciliation, 2307 Discrepancy & Vendor Dispute Resolution | VS-79 |
| W2769 | Quarterly Corporate Income Tax (1702Q) & Annual Return (1702RT) Preparation | VS-79 |
| W2770 | Tax-Adjusted Financial Income (TAFI) Schedule & Permanent/Temporary Differences | VS-79 |
| W2771 | Local Business Tax (LBT) Computation & LGU Filing per Location | VS-79 |
| W2772 | Documentary Stamp Tax (DST) on Leases, Loans & Documents | VS-79 |
| W2773 | BIR Tax Audit / LOAN Response & Assessment Contestation | VS-79 |
| W2774 | CREATE / CREATE More Tax Incentive Monitoring & Entity Structure Review | VS-79 |
| W2775 | Tax Provision (PAS/IFRS 12) & Deferred Tax Asset / Liability Reconciliation | VS-79 |
| W2776 | Tax Risk Register, Tax Calendar & Tax Controversy Governance | VS-79 |
| W3689 | Revenue Assurance Program Strategy & Governance | VS-118 |
| W3691 | Sales-to-Cash Reconciliation & Settlement Integrity | VS-118 |
| W3692 | POS Transaction Integrity & Data-Flow Assurance | VS-118 |
| W3693 | Revenue Assurance Controls & Exception Monitoring Framework | VS-118 |
| W3694 | Multi-Channel Revenue Consolidation & Reconciliation | VS-118 |
| W3697 | Pricing Accuracy & Price-Override Integrity Monitoring | VS-118 |
| W3698 | Promotion, Discount & Markdown Integrity Assurance | VS-118 |
| W3699 | Loyalty Points, Gift Card & Stored-Value Integrity | VS-118 |
| W3700 | Mandatory Discount & Tax-Exempt Sale Integrity | VS-118 |
| W3701 | Payment, Tender & Settlement Integrity (MDR/Fees) | VS-118 |
| W3702 | Catch-Weight, Cut-Length & Measurement-Based Revenue Assurance | VS-118 |
| W3703 | Ecommerce, Marketplace & 3P Settlement Revenue Assurance | VS-118 |
| W3704 | Refund, Reversal & Return Leakage Monitoring | VS-118 |
| W3705 | Leakage Detection, Quantification & Root-Cause Analysis | VS-118 |
| W3706 | Revenue Leakage Recovery & Corrective Action | VS-118 |
| W3708 | Fraud, Collusion & Abuse Revenue-Loss Investigation | VS-118 |
| W3709 | Pricing & Promo System Governance & Master-Data Integrity | VS-118 |
| W3711 | Multi-Entity Revenue Assurance & Consolidated Reporting | VS-118 |
| W3857 | Enterprise Fraud Management Strategy, Risk Appetite & Governance | VS-125 |
| W3859 | Fraud Detection Rules, Models & Orchestration Platform | VS-125 |
| W3860 | Fraud Case Management & Investigation Workflow | VS-125 |
| W3861 | Fraud Data, Network Analytics & Consortium/Device Intelligence | VS-125 |
| W3865 | POS / Store Transaction Fraud Monitoring | VS-125 |
| W3866 | Ecommerce & Digital Channel Fraud Prevention | VS-125 |
| W3867 | Returns & Refund Abuse Prevention | VS-125 |
| W3868 | Promotion, Coupon & Loyalty Abuse Prevention | VS-125 |
| W3869 | Gift Card & Stored-Value Fraud Prevention | VS-125 |
| W3870 | Payment, Chargeback & First-Party/Friendly Fraud Management | VS-125 |
| W3871 | Account Takeover & Credential Abuse Prevention | VS-125 |
| W3872 | Trade / B2B Account & Application First-Party Fraud Prevention | VS-125 |
| W3873 | Fraud Investigation, Evidence & Case Adjudication | VS-125 |
| W3874 | Fraud Recovery, Restitution & Asset Recovery | VS-125 |
| W3875 | Chargeback Representment & Dispute Management | VS-125 |
| W3876 | Internal / Employee Fraud & Collusion Investigation | VS-125 |
| W3877 | Fraud Reporting, Regulatory & Law-Enforcement Coordination | VS-125 |

**Governance & Assurance** (95)

| ID | Workflow | Value Stream |
|---|---|---|
| W2897 | SC/PWD/Solo Parent ID Validation & Eligibility Verification at POS | VS-85 |
| W2898 | Mandatory Discount Computation, Stack Rules & Basket Validation | VS-85 |
| W2899 | SC/PWD Purchase Book of Sales Transaction Recording | VS-85 |
| W2900 | Discount Abuse, ID Sharing & Fraud Prevention Monitoring | VS-85 |
| W2901 | Medicine & Prime Commodity Discount Compliance (RA 9994/7394) | VS-85 |
| W2902 | Solo Parent Discount Program Configuration & Eligible-SKU Mapping | VS-85 |
| W2904 | Customer Complaint & DTI/NCSC Escalation Handling | VS-85 |
| W2905 | PEZA/BOI VAT-Zero-Rated Sale Customer Onboarding & Certificate Management | VS-85 |
| W2906 | Government / Diplomatic VAT-Exempt Purchase Documentation | VS-85 |
| W2907 | Educational Institution & Housing (PAG-IBIG) VAT-Exempt Sale Processing | VS-85 |
| W2908 | VAT-Exempt Agricultural/Fisherfolk Input Customer Verification | VS-85 |
| W2909 | Export Sale (Direct/Constructive) Zero-Rating Documentation | VS-85 |
| W2910 | BIR Tax-Exempt Entity Master Maintenance & Renewal Tracking | VS-85 |
| W2911 | Mixed Basket (Taxable + Exempt) Allocation & Apportionment | VS-85 |
| W2912 | VAT-Exempt Sale Invoice, ATC & Disclosure Compliance | VS-85 |
| W2913 | SC/PWD/Solo Parent Tax Credit Computation & Monthly Claim Buildup | VS-85 |
| W2914 | SC/PWD Book-of-Sales Quarterly Compilation & Submission (RR 7-2010) | VS-85 |
| W2915 | Tax Credit Certificate (TCC) Application & Tracking | VS-85 |
| W2916 | LGU Local Tax Credit & Real Property Tax Exemption Coordination | VS-85 |
| W2918 | BIR Audit of Statutory Discount Books & Tax Credit Defense | VS-85 |
| W2993 | Product Safety Issue Intake, Triage & Hazard Classification | VS-89 |
| W2994 | Recall Risk Assessment & Corrective Action Decision | VS-89 |
| W2995 | DTI-BPS / FDA Regulatory Notification & Filing | VS-89 |
| W2996 | Recall Strategy, Scope & Lot/Shipment Traceability Definition | VS-89 |
| W2997 | Recall Committee Activation & Cross-Functional Command | VS-89 |
| W2998 | Vendor / Manufacturer Coordination & Corrective Action Agreement | VS-89 |
| W2999 | Recall Effectiveness Check Planning & Sample Design | VS-89 |
| W3000 | Stop-Sale, Quarantine & Inventory Hold Execution | VS-89 |
| W3001 | Multi-Channel Customer Recall Notice & Public Communication | VS-89 |
| W3002 | Store-Level Recall Execution, POS Block & Shelf Removal | VS-89 |
| W3003 | Ecommerce & Marketplace Recall Handling (Listing Block, Buyer Notify) | VS-89 |
| W3004 | Customer Return, Refund, Repair & Replacement Processing (Recall) | VS-89 |
| W3005 | Recall Product Retrieval Logistics & Reverse Consolidation | VS-89 |
| W3006 | Trade / B2B Account Recall Outreach & Bulk Recovery | VS-89 |
| W3007 | Field / Job Site Recall Recovery for Delivered Goods | VS-89 |
| W3008 | Recall Progress Tracking, Daily Status Reporting & Effectiveness Measurement | VS-89 |
| W3010 | Recalled Product Destruction, Recycling & Disposal Compliance | VS-89 |
| W3011 | Recall Root Cause Analysis & CAPA (Corrective & Preventive Action) | VS-89 |
| W3013 | Regulatory Close-Out Reporting (DTI-BPS / FDA) & Recall Termination | VS-89 |
| W3041 | Data Privacy Program Governance, NPC Registration & DPO Operations | VS-91 |
| W3042 | Personal Data Inventory, Data Mapping & Records of Processing Activities (ROPA) | VS-91 |
| W3043 | Consent Capture, Preference Management & Lawful Basis Tracking | VS-91 |
| W3044 | Data Subject Access Request (DSAR) Fulfillment & Verification | VS-91 |
| W3045 | Data Rectification, Erasure & Objection Request Processing | VS-91 |
| W3046 | Marketing Consent, Unsubscribe & Communication Preference Sync | VS-91 |
| W3047 | Loyalty Member Data Portability & Account Data Export | VS-91 |
| W3048 | Minors' Data, Sensitive Data & Special Category Processing Controls | VS-91 |
| W3049 | Privacy Impact Assessment (PIA) & DPIA for New Initiatives | VS-91 |
| W3050 | Cross-Border Transfer Assessment & Adequacy Determination | VS-91 |
| W3051 | Data Processing Agreement (DPA) & Vendor Privacy Due Diligence | VS-91 |
| W3052 | Third-Party Processor Oversight & Privacy Audit | VS-91 |
| W3053 | Data Minimization, Retention & Privacy-by-Design Review | VS-91 |
| W3055 | CCTV / Surveillance Privacy Impact & Signage Compliance | VS-91 |
| W3057 | Personal Data Breach Detection, Triage & Incident Activation | VS-91 |
| W3058 | Breach Containment, Forensic Investigation & Scope Assessment | VS-91 |
| W3059 | NPC Breach Notification (72-Hour) & Regulatory Reporting | VS-91 |
| W3060 | Affected Data Subject Notification & Remediation | VS-91 |
| W3064 | Data Privacy Audit, NPC Investigation Response & Remediation | VS-91 |
| W3593 | DG/Hazmat Compliance Program Strategy & Governance | VS-114 |
| W3594 | DG Product Classification (UN/IMDG/IATA/ADR) & Master Data | VS-114 |
| W3595 | Hazmat Inventory, SDS & Chemical Information Management | VS-114 |
| W3598 | DG Transport Packaging, Marking & Labeling Standards | VS-114 |
| W3599 | DG Procurement, Vendor & Import Compliance | VS-114 |
| W3601 | DG Transport Carrier Qualification & Contracting | VS-114 |
| W3602 | DG Transport Documentation & Manifest Management | VS-114 |
| W3603 | DG Ocean / Air / Road Modal Transport Compliance | VS-114 |
| W3604 | DG Ecommerce Ship-Eligibility & Channel Rules | VS-114 |
| W3605 | DG Last-Mile & 3PL DG Shipping Management | VS-114 |
| W3606 | DG Transport Incident, Spill & Emergency Response | VS-114 |
| W3607 | DG Transport Permit, Escort & Port / Airport Handling | VS-114 |
| W3609 | DG Storage Compliance & Fixed-Site Risk Management | VS-114 |
| W3610 | DG Handling Procedures, PPE & Worker Safety | VS-114 |
| W3611 | DG Spill Response, Containment & Remediation | VS-114 |
| W3612 | DG Hazardous Waste Transport, Disposal & DENR-EMB Manifest | VS-114 |
| W3613 | DG Incident Investigation, Reporting & Regulatory Notification | VS-114 |
| W3614 | DG Site Permitting, Fire Code & BFP Compliance | VS-114 |
| W3665 | DTI-BPS Certification Program Strategy & Governance | VS-117 |
| W3666 | Regulated-Product Identification & BPS Standards Mapping | VS-117 |
| W3667 | Vendor/Manufacturer PS Mark License Management | VS-117 |
| W3668 | Product Standards Technical File & Documentation Management | VS-117 |
| W3669 | New-Product Certification & Assortment Compliance Gate | VS-117 |
| W3670 | Vendor Certification Audit, Verification & PS License Renewal | VS-117 |
| W3673 | Import ICC/SOC Application & PCIMS Portal Management | VS-117 |
| W3674 | Shipment Documentation & BPS Documentary Review | VS-117 |
| W3675 | DTI Inspection, Sampling & Witness Coordination | VS-117 |
| W3676 | Accredited Laboratory Testing & Results Management | VS-117 |
| W3677 | ICC/SOC Certificate Issuance & Customs Release Coordination | VS-117 |
| W3678 | ICC Sticker Procurement, Control & Application | VS-117 |
| W3679 | Sample Failure, Re-export & Disposition Management | VS-117 |
| W3681 | In-Market Compliance Monitoring & Store Shelf Audit | VS-117 |
| W3682 | DTI Market Surveillance Response & Oplan Coordination | VS-117 |
| W3683 | Consumer Complaint & Certification Non-Conformance Investigation | VS-117 |
| W3684 | Stop-Sale, Withdrawal & Certification Corrective Action | VS-117 |
| W3686 | Vendor Recovery, Penalty & Certification Chargeback | VS-117 |
| W3687 | Multi-Entity Certification Coordination & Reporting | VS-117 |


#### Tier 2 — Program support (32 workflows)

**Finance** (11)

| ID | Workflow | Value Stream |
|---|---|---|
| W3690 | Revenue Leakage Taxonomy & Risk Mapping | VS-118 |
| W3695 | Revenue Assurance Policy, Authority & Approval Matrix | VS-118 |
| W3696 | Revenue Assurance Audit, Documentation & Records | VS-118 |
| W3707 | Revenue Assurance Analytics & KPI Reporting | VS-118 |
| W3858 | Fraud Risk Assessment & Cross-Channel Fraud Typology Catalog | VS-125 |
| W3862 | Fraud Policy, Rules Lifecycle & Model Governance | VS-125 |
| W3863 | Fraud Vendor & Third-Party Data/Tool Governance | VS-125 |
| W3864 | Fraud Program Budget, Reporting & Continuous Improvement | VS-125 |
| W3878 | Fraud Controls Assurance & Audit Support | VS-125 |
| W3879 | Fraud Awareness Training & Store/Agent Enablement | VS-125 |
| W3880 | Fraud Analytics, Loss Rates & Program KPI Reporting | VS-125 |

**Governance & Assurance** (21)

| ID | Workflow | Value Stream |
|---|---|---|
| W2903 | Staff Training, ID Recognition & Customer Service Protocol | VS-85 |
| W2917 | Discount Cost Allocation, Store Margin Impact & Reimbursement Policy | VS-85 |
| W2919 | Mandatory Discount Regulatory Change Monitoring & Policy Update | VS-85 |
| W2920 | Statutory Discount Program KPI, Cost & Compliance Reporting | VS-85 |
| W3009 | Vendor Reimbursement, Credit & Cost Recovery for Recalls | VS-89 |
| W3012 | Post-Recall Surveillance & Re-Occurrence Monitoring | VS-89 |
| W3014 | Recall Records Retention, Documentation & Audit File | VS-89 |
| W3015 | Recall Insurance Claim & Recovery Processing | VS-89 |
| W3054 | De-identification, Anonymization & Test Data Management | VS-91 |
| W3056 | Privacy Awareness Training & Employee Compliance Program | VS-91 |
| W3061 | Cyber Insurance Coordination & Breach Cost Recovery | VS-91 |
| W3062 | Breach Post-Incident Review & Corrective Action | VS-91 |
| W3063 | Privacy Metrics, Compliance Reporting & DPO Board Reporting | VS-91 |
| W3596 | DG Regulatory Intelligence & Compliance Monitoring | VS-114 |
| W3597 | DG Training, Certification & Competency Management | VS-114 |
| W3600 | DG Program Audit, Documentation & Records | VS-114 |
| W3608 | DG Transport Audit, Carrier Performance & Analytics | VS-114 |
| W3615 | DG Insurance, Liability & Risk Transfer | VS-114 |
| W3671 | BPS Standards Monitoring & Regulatory Change Management | VS-117 |
| W3672 | Certification Records, Reporting & Program Audit | VS-117 |
| W3680 | Testing Laboratory Relationship, Accreditation & Cost Management | VS-117 |


#### Tier 3 — Analytics / enhancement (6 workflows)

**Finance** (2)

| ID | Workflow | Value Stream |
|---|---|---|
| W3710 | Revenue Assurance Technology, Tooling & Automation | VS-118 |
| W3712 | Revenue Assurance Maturity & Continuous Improvement | VS-118 |

**Governance & Assurance** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W3016 | Recall Lessons Learned, Process & Quality System Improvement | VS-89 |
| W3616 | DG Compliance Analytics, Loss-Event Review & Continuous Improvement | VS-114 |
| W3685 | Certification Cost, Lead-Time & Landed-Cost Analytics | VS-117 |
| W3688 | Certification Program Analytics & Continuous Improvement | VS-117 |


**Demotion audit (38 workflows moved off the classifier's blanket Tier 1):**

- **→ Tier 2** (32): W2903, W2917, W2919, W2920, W3009, W3012, W3014, W3015, W3054, W3056, W3061, W3062, W3063, W3596, W3597, W3600, W3608, W3615, W3671, W3672, W3680, W3690, W3695, W3696, W3707, W3858, W3862, W3863, W3864, W3878, W3879, W3880
- **→ Tier 3** (6): W3016, W3616, W3685, W3688, W3710, W3712

---

### Support & Governance Classification Pass (192 workflows; VS-100/104/112/113/126/129/133/139)

> **Hand-reviewed 2026-06-20 (batch 2).** Eight family-decisive Tier-2 VSs (legal operations,
> government affairs, PMO, enterprise architecture, customer-data platform, competition/
> antitrust, operational excellence, trade-show marketing). The classifier's conservative
> default put nearly all of these at Tier 2; genuine review against the tier definitions —
> **calibrated to the existing register's placement** of optimization/analytics workflows in
> Tier 3 (Route Optimization, Cost Optimization, Assortment Optimization, Retail Analytics &
> AI, QAIP) and operational performance reviews in Tier 2 — yields:
> **14 Tier 1** (statutory execution the keyword rules missed) · **149 Tier 2** (confirmed
> standard support) · **29 Tier 3** (analytics / optimization / enhancement defaulted to T2).
> The 14 promotions and 29 demotions are audited below; the remaining 149 confirm the
> classifier's Tier 2 default. Result moves Check 1 unclassified 3,644 → 3,452.

#### Tier 1 — Statutory execution (14 workflows)

**Governance & Assurance** (12)

| ID | Workflow | Value Stream |
|---|---|---|
| W3261 | Settlement, Judgment & Loss Accrual Accounting | VS-100 |
| W3262 | Litigation Hold Initiation & Evidence Coordination | VS-100 |
| W3263 | Court Filing, Service & Judgment Enforcement | VS-100 |
| W3275 | Legal Entity Management & Corporate Secretarial Support | VS-100 |
| W3276 | Regulatory & Government Investigation Defense | VS-100 |
| W3277 | Legal Risk Register, Loss Contingency & Disclosure | VS-100 |
| W3360 | Political-Activity Compliance, Lobbying Disclosure & Ethics | VS-104 |
| W3967 | Merger, Acquisition & Joint-Venture Notification (PCC Pre-Filing) Control | VS-129 |
| W3970 | Competition Inquiry, Dawn Raid & Information Request Response | VS-129 |
| W3971 | PCC Investigation, Preliminary Inquiry & Motu Proprio Matter Defense | VS-129 |
| W3973 | Competition Litigation, Appeal (Court of Appeals / SC) & Judgment Management | VS-129 |
| W3974 | Competition Penalty, Fine & Damages Payment & Disclosure Management | VS-129 |

**Technology & Data** (1)

| ID | Workflow | Value Stream |
|---|---|---|
| W3900 | Data Subject Access Request (DSAR) & Consumer Rights Workflow | VS-126 |

**Sell & Serve** (1)

| ID | Workflow | Value Stream |
|---|---|---|
| W4198 | Event Compliance, Permits & Promo-Prize Governance | VS-139 |


#### Tier 2 — Standard support (149 workflows)

**Governance & Assurance** (68)

| ID | Workflow | Value Stream |
|---|---|---|
| W3257 | Legal Matter Intake, Triage & Matter Master | VS-100 |
| W3258 | Litigation Case Lifecycle & Pre-Trial Management | VS-100 |
| W3259 | Outside Counsel Selection, Engagement & Billing | VS-100 |
| W3260 | Alternative Dispute Resolution, Arbitration & Mediation | VS-100 |
| W3265 | Trademark, Copyright & Industrial Design Portfolio Strategy | VS-100 |
| W3266 | Trademark Search, Prosecution & IPOPHL Filing | VS-100 |
| W3267 | IP Renewal, Maintenance & Portfolio Lifecycle | VS-100 |
| W3268 | IP Enforcement, Cease-and-Desist & Infringement Action | VS-100 |
| W3269 | Brand Licensing, Franchise & IP Commercialization | VS-100 |
| W3270 | Trade Secret, Confidentiality & Non-Disclosure Management | VS-100 |
| W3271 | Domain Name, Anti-Cybersquatting & Digital IP Protection | VS-100 |
| W3273 | Contract Template, Clause Library & Legal Review Support | VS-100 |
| W3274 | Contract Lifecycle Support & Obligation Tracking | VS-100 |
| W3278 | Ethics, Whistleblower & Investigation Case Management | VS-100 |
| W3279 | Legal Operations Technology & e-Billing | VS-100 |
| W3353 | National Government Stakeholder Mapping & Relationship Management | VS-104 |
| W3354 | Legislative & Regulatory Monitoring, Horizon Scanning & Impact Assessment | VS-104 |
| W3355 | Public Policy Position Development & Advocacy Campaign Execution | VS-104 |
| W3356 | Congressional & Executive-Agency Engagement (DTI/DOLE/BIR/BSP/NTC etc.) | VS-104 |
| W3357 | Policy Submission, Consultation & Position-Paper Filing | VS-104 |
| W3358 | Cross-Industry Coalition Building & Joint Advocacy | VS-104 |
| W3359 | Government Affairs Calendar, Briefing & Executive Liaison | VS-104 |
| W3361 | Industry Association Membership Strategy, Selection & Dues Management | VS-104 |
| W3362 | Trade Association Leadership, Committee & Board Representation | VS-104 |
| W3363 | Industry Standard, Code & Best-Practice Development Participation | VS-104 |
| W3364 | Peer-Retailer Benchmarking, Knowledge Exchange & Industry Research | VS-104 |
| W3365 | Industry Event, Conference & Award Program Participation | VS-104 |
| W3366 | Supplier/Channel Industry Forum & Ecosystem Engagement | VS-104 |
| W3367 | Association Sponsorship, Partnership & ROI Evaluation | VS-104 |
| W3368 | Industry Relations Performance & Influence Reporting | VS-104 |
| W3369 | Public Affairs Strategy & Issue Management (Non-Crisis) | VS-104 |
| W3370 | Corporate Positioning & Stakeholder Narrative Development | VS-104 |
| W3371 | Community Relations & Local Stakeholder Engagement (National Brand Level) | VS-104 |
| W3372 | Think-Tank, Academic & Policy-Institution Partnership | VS-104 |
| W3373 | Media & Analyst Relations for Policy/Industry Topics | VS-104 |
| W3374 | Corporate Political & Regulatory Risk Assessment | VS-104 |
| W3376 | External-Affairs Annual Plan, KPI & Board Reporting | VS-104 |
| W3953 | Competition & Antitrust Compliance Program Strategy, Governance & Operating Model | VS-129 |
| W3954 | Market Definition, Market Share & Market Power Assessment | VS-129 |
| W3955 | Pricing & Promotional Conduct Competition Risk Assessment | VS-129 |
| W3956 | Vendor / Trade-Partner Vertical-Restraint & RPM Risk Assessment | VS-129 |
| W3957 | Association, Trade-Body & Competitor-Interaction Risk Assessment | VS-129 |
| W3958 | Procurement, Buyer-Power & Supplier-Coordination Risk Assessment | VS-129 |
| W3959 | Digital, Marketplace & Platform Competition Risk Assessment | VS-129 |
| W3960 | Competition Law Training, Awareness & Culture Program | VS-129 |
| W3961 | Pricing Decision & Competitor-Information-Exchange Controls | VS-129 |
| W3962 | Vendor Agreement, RPM & Exclusivity Clause Review & Contract Controls | VS-129 |
| W3963 | Joint Venture, Strategic Alliance & Cooperation Agreement Clearance | VS-129 |
| W3964 | Trade / B2B Distribution, Resale & Channel Pricing Compliance Controls | VS-129 |
| W3965 | Association Meeting & Industry-Gathering Compliance Protocol | VS-129 |
| W3966 | Market-Allocation, Customer-Allocation & Territory Conduct Controls | VS-129 |
| W3968 | Competition Compliance Monitoring, Audit & Continuous Improvement | VS-129 |
| W3969 | Philippine Competition Commission (PCC) Relationship & Engagement Management | VS-129 |
| W3972 | Leniency, Settlement & Commitment (Whistleblower) Program Management | VS-129 |
| W3975 | Remediation, Conduct Change & Compliance-Monitoring Implementation | VS-129 |
| W4049 | Operational Excellence Strategy, Charter & Operating Model | VS-133 |
| W4050 | Enterprise Process Architecture, Ownership & RACI Governance | VS-133 |
| W4051 | Continuous Improvement Methodology Standards (Lean / Six Sigma / Kaizen) | VS-133 |
| W4052 | Improvement Opportunity Pipeline & Prioritization (Impact-Effort) | VS-133 |
| W4053 | Cross-Functional Improvement Project Governance & Stage-Gate | VS-133 |
| W4054 | Process KPI Library, Baseline Measurement & Target Setting | VS-133 |
| W4055 | OpEx Capability Building, Green Belt / Black Belt Certification | VS-133 |
| W4056 | Continuous Improvement Culture, Suggestion System & Recognition | VS-133 |
| W4057 | Process Discovery & End-to-End Process Mapping | VS-133 |
| W4060 | Process Re-Design, Standard Work & SOP Authoring | VS-133 |
| W4063 | Control Design & Re-Engineering for Risk Reduction | VS-133 |
| W4064 | Improvement Rollout, Change Management & Sustainment | VS-133 |
| W4071 | Improvement Project Portfolio Review & Lessons Learned | VS-133 |

**Asset & Infrastructure** (22)

| ID | Workflow | Value Stream |
|---|---|---|
| W3545 | Enterprise Project Portfolio Strategy & Governance | VS-112 |
| W3546 | Project Intake, Classification & Portfolio Registration | VS-112 |
| W3547 | Project Prioritization, Scoring & Resource Allocation | VS-112 |
| W3548 | Stage-Gate Methodology & Project Lifecycle Standards | VS-112 |
| W3549 | Program Management (Multi-Project Initiatives) | VS-112 |
| W3550 | Project Portfolio Risk, Dependency & Conflict Management | VS-112 |
| W3551 | Project Approval, Charter & Business Case Governance | VS-112 |
| W3552 | Portfolio Dashboards, Reporting & Executive / Board Oversight | VS-112 |
| W3553 | Project Manager Assignment, Resource & Capacity Planning | VS-112 |
| W3554 | Project Planning, Scheduling & WBS Management | VS-112 |
| W3555 | Project Budget & Cost Control | VS-112 |
| W3556 | Project Scope, Change & Configuration Management | VS-112 |
| W3557 | Project Quality, Deliverable & Acceptance Management | VS-112 |
| W3558 | Project Risk, Issue & Decision Management | VS-112 |
| W3559 | Project Communications & Stakeholder Management | VS-112 |
| W3560 | Project Closure, Handover & Lessons Learned | VS-112 |
| W3561 | Project Benefits Realization Tracking & Validation | VS-112 |
| W3562 | Project Management Information System (PMIS) & Tooling | VS-112 |
| W3564 | Program / Project Financial Performance vs Business Case | VS-112 |
| W3566 | Project Management Standards, Templates & Methodology | VS-112 |
| W3567 | Vendor / Contractor Project Performance & Governance | VS-112 |
| W3568 | Enterprise Transformation & Change Management Portfolio | VS-112 |

**Technology & Data** (37)

| ID | Workflow | Value Stream |
|---|---|---|
| W3569 | Enterprise Architecture Strategy, Framework & Governance | VS-113 |
| W3570 | Architecture Principles, Standards & Reference Architecture | VS-113 |
| W3571 | Architecture Review Board & Solution Architecture Review | VS-113 |
| W3572 | Technology Standards & Approved Technology List | VS-113 |
| W3573 | Architecture Compliance, Exception & Waiver Management | VS-113 |
| W3574 | Architecture Capability, Skills & Center of Excellence | VS-113 |
| W3575 | Architecture Repository, Documentation & Knowledge Management | VS-113 |
| W3577 | Application Portfolio Management & Rationalization | VS-113 |
| W3578 | Application Lifecycle, Retirement & Technical Debt Management | VS-113 |
| W3579 | Integration Architecture & API Strategy | VS-113 |
| W3580 | Solution Architecture for New Initiatives & Projects | VS-113 |
| W3581 | Data Architecture & Information Strategy | VS-113 |
| W3582 | Cloud & Infrastructure Architecture | VS-113 |
| W3583 | Security Architecture | VS-113 |
| W3584 | Architecture for ERP Platform & Core Systems Evolution | VS-113 |
| W3585 | Technology Strategy & Multi-Year Technology Roadmap | VS-113 |
| W3587 | Architecture for Digital Transformation Programs | VS-113 |
| W3588 | Technology Investment Governance & Architecture ROI | VS-113 |
| W3589 | Vendor & Platform Strategy for Enterprise Systems | VS-113 |
| W3590 | Architecture Risk, Resilience & Disaster-Recovery Design | VS-113 |
| W3591 | Enterprise Architecture Stakeholder Engagement & Communication | VS-113 |
| W3881 | CDP Strategy, Architecture & Governance | VS-126 |
| W3882 | Customer Data Ingestion & Source-System Integration | VS-126 |
| W3883 | Customer Identity Resolution & Profile Stitching | VS-126 |
| W3884 | Customer Golden Record & Master Profile Management | VS-126 |
| W3885 | Customer Consent, Preference & Compliance Center | VS-126 |
| W3886 | Customer Data Quality, Deduplication & Hygiene | VS-126 |
| W3887 | CDP Data Model, Taxonomy & Segmentation Foundation | VS-126 |
| W3888 | CDP Platform Operations, Security & Access Governance | VS-126 |
| W3889 | Customer Segmentation & Targeting Operations | VS-126 |
| W3891 | Audience Activation & Cross-Channel Syndication | VS-126 |
| W3893 | Customer Journey Orchestration & Trigger Management | VS-126 |
| W3897 | Customer 360 Consumption & Self-Service Access | VS-126 |
| W3898 | B2B / Trade & Key-Account Profile Enrichment | VS-126 |
| W3899 | Loyalty Program Data & Tier/Behavior Enrichment | VS-126 |
| W3901 | Customer Data Privacy, Consent Audit & DPIA | VS-126 |
| W3902 | Customer Data Retention, Archival & Purge | VS-126 |

**Sell & Serve** (22)

| ID | Workflow | Value Stream |
|---|---|---|
| W4193 | Event Marketing Strategy & Channel Role | VS-139 |
| W4194 | Annual Event Portfolio & Calendar Planning | VS-139 |
| W4195 | Event Budget, Business Case & Sponsorship Funding | VS-139 |
| W4196 | Event Audience, Targeting & Trade-Pro Invitation | VS-139 |
| W4197 | Vendor Co-Funding, Co-Exhibition & MDF Coordination | VS-139 |
| W4199 | Event Cross-Functional Team & Resource Planning | VS-139 |
| W4200 | Event Brief, Objectives & Success-Metric Definition | VS-139 |
| W4201 | Booth/Stand Design, Build & Logistics | VS-139 |
| W4202 | Show Registration, Sponsorship & Space Contracting | VS-139 |
| W4203 | Product Display, Demo & Sample Coordination | VS-139 |
| W4204 | On-Site Sales, Engagement & Lead Capture | VS-139 |
| W4205 | Hospitality, VIP & Account-Manager Meetings | VS-139 |
| W4206 | Event Travel, Accommodation & Per-Diem Management | VS-139 |
| W4207 | Show Teardown, Asset Recovery & Return Logistics | VS-139 |
| W4208 | Health, Safety & Incident Management at Events | VS-139 |
| W4209 | Hosted Trade Day & Contractor Event Operations | VS-139 |
| W4210 | Product Launch & New-Arrival Showcase Events | VS-139 |
| W4211 | Store Grand-Opening & In-Store Event Marketing | VS-139 |
| W4212 | Partner, Association & Sponsored-Event Management | VS-139 |
| W4213 | Digital & Hybrid Event / Webinar Operations | VS-139 |
| W4214 | Lead Capture, Qualification & CRM Routing | VS-139 |
| W4215 | Post-Event Nurture, Follow-Up & Sales Conversion | VS-139 |


#### Tier 3 — Analytics / optimization / enhancement (29 workflows)

**Governance & Assurance** (16)

| ID | Workflow | Value Stream |
|---|---|---|
| W3264 | Legal Matter Analytics & Loss Forecasting | VS-100 |
| W3272 | IP Portfolio Valuation & Risk Analytics | VS-100 |
| W3280 | Legal Department Performance & Cost Analytics | VS-100 |
| W3375 | Government Affairs & Industry-Relations Budget, Spend & Analytics | VS-104 |
| W3976 | Competition Compliance Program Analytics, Reporting & Board Oversight | VS-129 |
| W4058 | Process Mining & Task Mining from ERP/System Event Logs | VS-133 |
| W4059 | Bottleneck, Root-Cause & Value-Stream Analysis | VS-133 |
| W4061 | Improvement Pilot Design, Execution & Hypothesis Testing | VS-133 |
| W4062 | Process Automation & Digitization Opportunity Scoping | VS-133 |
| W4065 | Benefit Case Modeling, Tracking & Realization Reporting | VS-133 |
| W4066 | Process Performance Monitoring & Control Tower Dashboard | VS-133 |
| W4067 | Productivity & Labor Efficiency Improvement Program | VS-133 |
| W4068 | Cost-Out / Cost-Reduction Program Management | VS-133 |
| W4069 | Cycle-Time, Throughput & Lead-Time Improvement Tracking | VS-133 |
| W4070 | Quality, Defect & Rework Reduction Program | VS-133 |
| W4072 | OpEx Maturity Assessment & Annual Program Review | VS-133 |

**Asset & Infrastructure** (2)

| ID | Workflow | Value Stream |
|---|---|---|
| W3563 | Project Portfolio Performance & KPI Analytics | VS-112 |
| W3565 | PMO Maturity Assessment & Continuous Improvement | VS-112 |

**Technology & Data** (10)

| ID | Workflow | Value Stream |
|---|---|---|
| W3576 | Architecture Maturity Assessment & Continuous Improvement | VS-113 |
| W3586 | Emerging Technology Evaluation & Adoption Governance | VS-113 |
| W3592 | Architecture Metrics, Portfolio Health & Technology Analytics | VS-113 |
| W3890 | Real-Time Customer Profile & Next-Best-Action Serving | VS-126 |
| W3892 | Personalization & Recommendation Engine Operations | VS-126 |
| W3894 | Customer Lifetime Value, Churn & Propensity Modeling | VS-126 |
| W3895 | Marketing Analytics, Attribution & Experimentation | VS-126 |
| W3896 | Campaign & Offer Measurement (Lift, ROI) | VS-126 |
| W3903 | Customer Analytics & Insights Reporting | VS-126 |
| W3904 | CDP Value Realization, ROI & Continuous Improvement | VS-126 |

**Sell & Serve** (1)

| ID | Workflow | Value Stream |
|---|---|---|
| W4216 | Event Performance, ROI & Portfolio Analytics | VS-139 |


**Promotion audit (14 → Tier 1, statutory execution the keyword rules missed):**

- **Governance & Assurance** (12): W3261, W3262, W3263, W3275, W3276, W3277, W3360, W3967, W3970, W3971, W3973, W3974
- **Technology & Data** (1): W3900
- **Sell & Serve** (1): W4198

**Demotion audit (29 → Tier 3, analytics/optimization defaulted to Tier 2):**

- **Governance & Assurance** (16): W3264, W3272, W3280, W3375, W3976, W4058, W4059, W4061, W4062, W4065, W4066, W4067, W4068, W4069, W4070, W4072
- **Asset & Infrastructure** (2): W3563, W3565
- **Technology & Data** (10): W3576, W3586, W3592, W3890, W3892, W3894, W3895, W3896, W3903, W3904
- **Sell & Serve** (1): W4216

---

### Operational Support Classification Pass (192 workflows; VS-40/43/55/63/64/65/83/84)

> **Hand-reviewed 2026-06-20 (batch 3).** Eight family-decisive Tier-2 VSs spanning capex
> project accounting, trade-professional program, planogram & space optimization, store
> communication, seasonal merchandise, e-commerce marketplace, occupational health, and
> labor relations. Genuine review yields **21 → Tier 1** (statutory execution: PFRS capex
> accounting, DOLE occupational-health reporting, DOLE/NLRC labor-relations mandatory
> processes, emergency-communication protocol), **30 → Tier 3** (analytics: space/productivity/
> clearance/post-season/channel analysis, churn prediction, ROI analytics, engagement surveys),
> and **141 confirmed Tier 2** (the core operational/program-management workflows).
> Result moves Check 1 unclassified 3,452 → 3,260.

#### Tier 1 — Statutory execution (21 workflows)

**Finance** (3)

| ID | Workflow | Value Stream |
|---|---|---|
| W1823 | Project Cost Capitalization vs. Expense Determination | VS-40 |
| W1824 | Capitalized Interest Calculation & Recording | VS-40 |
| W1829 | CIP-to-Fixed Asset Conversion Processing | VS-40 |

**Sell & Serve** (1)

| ID | Workflow | Value Stream |
|---|---|---|
| W2360 | Emergency Communication Protocol | VS-63 |

**People** (17)

| ID | Workflow | Value Stream |
|---|---|---|
| W2850 | Workplace Injury / Illness First Aid & Medical Case Opening | VS-83 |
| W2852 | SSS EC / Sickness Benefit & PhilHealth Claim Coordination | VS-83 |
| W2853 | Work-Relatedness Determination & EC Claim Documentation (DOLE) | VS-83 |
| W2858 | Annual / Periodic Medical Examination (APE) Program Execution | VS-83 |
| W2859 | DOLE-Required Periodic Exam by Hazard Category (Chemical/Physical/Biological) | VS-83 |
| W2863 | DOLE Annual Medical Report (AMR) & OHS Statistics Compilation | VS-83 |
| W2864 | Workplace Exposure Monitoring (Noise/Air/Chemical) & DOLE Compliance | VS-83 |
| W2866 | Mental Health Act (RA 11036) Compliance & DOH Mental Health Program | VS-83 |
| W2873 | Labor Organization Certification, Recognition & Verification (DOLE) | VS-84 |
| W2875 | CBA Negotiation Sessions, Deadlock Management & DOLE Conciliation | VS-84 |
| W2876 | CBA Drafting, Ratification, Registration & Publication | VS-84 |
| W2883 | Preventive Suspension, Due Process & Notice Workflow (2-Notice Rule) | VS-84 |
| W2884 | Disciplinary Investigation, Hearing & Decision | VS-84 |
| W2885 | DOLE Conciliation-Mediation (SENA) & Single-Entry Approach | VS-84 |
| W2886 | Labor Arbitration, NLRC Representation & Appeal Management | VS-84 |
| W2887 | Illegal Dismissal, Reinstatement & Backpay Compliance Execution | VS-84 |
| W2888 | Strike / Lockout Notice, Contingency & Resolution | VS-84 |


#### Tier 2 — Operational support (141 workflows)

**Finance** (19)

| ID | Workflow | Value Stream |
|---|---|---|
| W1811 | Capital Expenditure Request Submission | VS-40 |
| W1812 | Capex Financial Evaluation & Business Case Review | VS-40 |
| W1813 | Capex Approval Workflow & Authorization | VS-40 |
| W1814 | Capex Budget Allocation & Commitment Tracking | VS-40 |
| W1815 | Capex Request Revision & Scope Change Management | VS-40 |
| W1816 | Emergency Capex Request Processing | VS-40 |
| W1817 | Capex Requisition to Purchase Order Conversion | VS-40 |
| W1818 | Capex Approval Documentation & Audit Trail | VS-40 |
| W1819 | Project Cost Capture & Allocation | VS-40 |
| W1820 | Construction Progress Payment & Contractor Billing | VS-40 |
| W1821 | Project Material & Equipment Cost Tracking | VS-40 |
| W1822 | Professional Service & Consulting Fee Tracking | VS-40 |
| W1825 | Project Budget vs. Actual Variance Reporting | VS-40 |
| W1826 | Multi-Entity Project Cost Allocation | VS-40 |
| W1827 | Construction-in-Progress (CIP) Account Management | VS-40 |
| W1828 | Project Completion Certification & Asset Turnover | VS-40 |
| W2749 | Partial Asset Turnover (Phased Project Completion) | VS-40 |
| W2750 | Abandoned Project Write-Off & Cost Recovery | VS-40 |
| W2751 | Project Closeout Documentation & Archiving | VS-40 |

**Sell & Serve** (76)

| ID | Workflow | Value Stream |
|---|---|---|
| W1878 | Trade Professional Account Application & Onboarding | VS-43 |
| W1879 | Trade Account Annual Recertification & Tier Review | VS-43 |
| W1880 | Trade Account Manager Assignment & Coverage Planning | VS-43 |
| W1881 | Trade Account Quarterly Business Review & Relationship Health Assessment | VS-43 |
| W1882 | Trade Account Dormancy Detection & Reactivation Campaign | VS-43 |
| W1884 | Trade Account Offboarding & Account Closure | VS-43 |
| W1885 | Trade Account Master Data Quality & Segmentation Review | VS-43 |
| W1886 | Contractor Loyalty Program Tier Design & Benefit Structure Management | VS-43 |
| W1887 | Contractor Points Earning, Redemption & Statement Management | VS-43 |
| W1888 | Contractor Volume Rebate & Spend-Based Incentive Calculation | VS-43 |
| W1889 | Contractor Referral Program & New Account Acquisition Incentive | VS-43 |
| W1890 | Contractor Early Payment Discount & Supply Chain Finance Program | VS-43 |
| W1891 | Contractor Seasonal Promotion & Project Bundle Pricing Execution | VS-43 |
| W1893 | Contractor Loyalty Program Financial Governance & Liability Management | VS-43 |
| W1894 | Trade Professional Product Training Program Planning & Execution | VS-43 |
| W1895 | Contractor Skills Workshop & Certification Event Management | VS-43 |
| W1896 | Trade Community Online Forum & Knowledge Base Management | VS-43 |
| W1897 | Vendor-Sponsored Trade Seminar & Product Demo Coordination | VS-43 |
| W1898 | Contractor Advisory Board & Feedback Program | VS-43 |
| W1899 | Trade Show Participation & Industry Event Representation | VS-43 |
| W1900 | Contractor Safety Training & Compliance Certification Support | VS-43 |
| W1901 | Trade Professional Recognition Awards & Community Building | VS-43 |
| W2166 | Seasonal Planogram Refresh | VS-55 |
| W2167 | New Product Shelf Placement | VS-55 |
| W2168 | Cross-Merchandising Display Planning | VS-55 |
| W2170 | Planogram Version Control | VS-55 |
| W2171 | Store Layout Zone Optimization | VS-55 |
| W2172 | Category Adjacency Planning | VS-55 |
| W2174 | Planogram Compliance Audit | VS-55 |
| W2175 | Photo-Based Remote Compliance Check | VS-55 |
| W2176 | Shelf Label & Price Accuracy Audit | VS-55 |
| W2177 | Endcap & Promotional Display Compliance | VS-55 |
| W2179 | Fixture & Display Equipment Inventory | VS-55 |
| W2180 | Store Cleanliness & Visual Standards Audit | VS-55 |
| W2181 | Planogram Change Implementation Tracking | VS-55 |
| W2183 | Fixture Procurement & Budgeting | VS-55 |
| W2184 | Shelf Capacity & Stocking Optimization | VS-55 |
| W2186 | Store Format Segmentation | VS-55 |
| W2187 | Seasonal Display Space Rotation | VS-55 |
| W2358 | Corporate Announcement Broadcasting | VS-63 |
| W2359 | Merchandising Directive Communication | VS-63 |
| W2361 | Weekly Store Manager Newsletter | VS-63 |
| W2362 | Two-Way Store Feedback Channel | VS-63 |
| W2363 | Policy & Procedure Update Distribution | VS-63 |
| W2364 | Seasonal Preparation Communication Package | VS-63 |
| W2365 | Communication Platform Training & Support | VS-63 |
| W2366 | Task Creation & Assignment from HQ | VS-63 |
| W2367 | Store-Level Task Execution & Reporting | VS-63 |
| W2368 | Task Compliance Dashboard | VS-63 |
| W2369 | Regional Operations Follow-Up | VS-63 |
| W2370 | Task Template & Standardization Management | VS-63 |
| W2371 | Task Completion Quality Audit | VS-63 |
| W2372 | Seasonal Task Calendar Management | VS-63 |
| W2376 | Store Manager Satisfaction Survey | VS-63 |
| W2378 | Information Overload Assessment | VS-63 |
| W2380 | Store Communication Best Practice Sharing | VS-63 |
| W2381 | Communication Strategy Annual Review | VS-63 |
| W2406 | Marketplace Platform Selection & Registration | VS-65 |
| W2407 | Marketplace Store Setup & Branding | VS-65 |
| W2408 | Marketplace Catalog & Pricing Configuration | VS-65 |
| W2409 | Marketplace API Integration | VS-65 |
| W2410 | Marketplace Promotional Campaign Setup | VS-65 |
| W2411 | Marketplace Customer Service Setup | VS-65 |
| W2412 | Marketplace Inventory Allocation Strategy | VS-65 |
| W2413 | Marketplace Channel Performance Baseline | VS-65 |
| W2414 | Marketplace Order Download & Processing | VS-65 |
| W2415 | Marketplace Inventory Synchronization | VS-65 |
| W2416 | Marketplace Fulfillment & Shipping | VS-65 |
| W2417 | Marketplace Return & Refund Processing | VS-65 |
| W2418 | Marketplace Pricing Sync & Competitor Monitoring | VS-65 |
| W2419 | Marketplace Listing Quality Management | VS-65 |
| W2420 | Marketplace Stock-Out Prevention | VS-65 |
| W2421 | Marketplace Customer Review Management | VS-65 |
| W2422 | Marketplace Financial Reconciliation | VS-65 |
| W2428 | Marketplace Platform Relationship Management | VS-65 |
| W2429 | Marketplace Strategy Annual Review | VS-65 |

**Plan & Source** (18)

| ID | Workflow | Value Stream |
|---|---|---|
| W2382 | Seasonal Assortment Planning | VS-64 |
| W2383 | Seasonal Inventory Positioning at DCs | VS-64 |
| W2384 | Seasonal Planogram & Display Setup | VS-64 |
| W2385 | Seasonal Pricing & Promotion Setup | VS-64 |
| W2386 | Seasonal Staff Training & Product Knowledge | VS-64 |
| W2387 | Seasonal Launch Monitoring | VS-64 |
| W2388 | Seasonal Vendor Coordination | VS-64 |
| W2389 | Multi-Season Inventory Transition Planning | VS-64 |
| W2390 | Sell-Through Based Markdown Trigger | VS-64 |
| W2391 | Progressive Markdown Strategy Execution | VS-64 |
| W2392 | Store-Level Clearance Event Execution | VS-64 |
| W2393 | Clearance Inventory Consolidation | VS-64 |
| W2394 | Vendor Markdown Allowance Processing | VS-64 |
| W2395 | Clearance Pricing Compliance Audit | VS-64 |
| W2396 | Employee Purchase Program for Clearance | VS-64 |
| W2397 | Clearance Financial Reconciliation | VS-64 |
| W2400 | Vendor Seasonal Performance Review | VS-64 |
| W2405 | Seasonal Playbook Update | VS-64 |

**People** (28)

| ID | Workflow | Value Stream |
|---|---|---|
| W2849 | Company Clinic Operations & Occupational Health Nurse Coverage | VS-83 |
| W2851 | Referral to Network Hospital, Specialist & Diagnostics Management | VS-83 |
| W2854 | Return-to-Work Clearance, Restricted Duty & Accommodation | VS-83 |
| W2855 | Medical Record Confidentiality, Consent & DOH Recordkeeping | VS-83 |
| W2856 | Clinic Pharmacy, First-Aid Station & Medical Supply Management | VS-83 |
| W2857 | Pre-Employment Medical Examination & Fitness-to-Work Clearance | VS-83 |
| W2860 | Vaccine & Immunization Program (Flu, Hep-B, Tetanus, COVID) | VS-83 |
| W2861 | Disease Surveillance & Outbreak Response (Store/DC Cluster) | VS-83 |
| W2862 | Ergonomics Assessment & Musculoskeletal Disorder Prevention | VS-83 |
| W2865 | Employee Assistance Program (EAP) Provision & Confidential Counseling | VS-83 |
| W2867 | Critical Incident Stress Debriefing & Crisis Support | VS-83 |
| W2868 | Substance Abuse Policy, Testing & Rehabilitation Support | VS-83 |
| W2869 | Lifestyle Disease (Diabetes/Hypertension) Management & Screening | VS-83 |
| W2870 | Nutrition, Fitness & Workplace Wellness Campaign | VS-83 |
| W2871 | Maternal & Reproductive Health Program | VS-83 |
| W2874 | CBA Negotiation Preparation, Data Assembly & Bargaining Strategy | VS-84 |
| W2877 | CBA Implementation, Wage/Benefit Administration & Compliance Tracking | VS-84 |
| W2878 | CBA Economic Impact Modeling, Costing & Mid-Term Review | VS-84 |
| W2879 | Union Dues Check-Off, Agency Fee & Authorization Management | VS-84 |
| W2880 | Labor-Management Council (LMC) Charter & Joint Governance Operations | VS-84 |
| W2881 | Grievance Intake, Classification & Step-1 Conference | VS-84 |
| W2882 | Grievance Escalation, Step-2/3 Review & CBA Dispute Resolution | VS-84 |
| W2890 | Town Hall, Skip-Level & Communication Forum Operations | VS-84 |
| W2891 | Suggestion Box / Idea Program & Recognition of Contributions | VS-84 |
| W2892 | Whistleblower & Fair Treatment (Non-Retaliation) Program Governance | VS-84 |
| W2893 | Labor Coalition & Industry Association Engagement (ECOP/FWE) | VS-84 |
| W2894 | Government Labor Policy Advocacy & DOLE/BIR/SSS Liaison | VS-84 |
| W2895 | Labor Relations Risk Register & ULP Prevention Audit | VS-84 |


#### Tier 3 — Analytics / analytics (30 workflows)

**Finance** (2)

| ID | Workflow | Value Stream |
|---|---|---|
| W2748 | Post-Implementation Review & Actual vs. Projected ROI Analysis | VS-40 |
| W2752 | Annual Capex Portfolio Review & Process Improvement | VS-40 |

**Sell & Serve** (19)

| ID | Workflow | Value Stream |
|---|---|---|
| W1883 | Trade Account Churn Risk Prediction & Retention Intervention | VS-43 |
| W1892 | Contractor Program Cost & ROI Analysis | VS-43 |
| W2169 | Space Productivity Analysis | VS-55 |
| W2173 | Planogram Cost-Benefit Analysis | VS-55 |
| W2178 | Store Walk-In Traffic & Heatmap Analysis | VS-55 |
| W2182 | Sales Per Square Meter Analysis | VS-55 |
| W2185 | Promotional Space ROI Analysis | VS-55 |
| W2188 | Planogram Performance Dashboard | VS-55 |
| W2189 | Space Capital Investment Analysis | VS-55 |
| W2373 | Task Analytics & Process Improvement | VS-63 |
| W2374 | Communication Read Rate Analysis | VS-63 |
| W2375 | Task Completion Rate Trending | VS-63 |
| W2377 | Communication Channel Effectiveness | VS-63 |
| W2379 | Communication Platform Usage Analytics | VS-63 |
| W2423 | Marketplace Commission & Fee Analysis | VS-65 |
| W2424 | Marketplace Channel P&L | VS-65 |
| W2425 | Marketplace Performance Dashboard | VS-65 |
| W2426 | Marketplace vs. Own Ecommerce Channel Comparison | VS-65 |
| W2427 | Marketplace Customer Acquisition Analysis | VS-65 |

**Plan & Source** (6)

| ID | Workflow | Value Stream |
|---|---|---|
| W2398 | Post-Season Sales Performance Analysis | VS-64 |
| W2399 | Seasonal Forecast Accuracy Review | VS-64 |
| W2401 | Customer Seasonal Purchase Behavior Analysis | VS-64 |
| W2402 | Seasonal Planogram Effectiveness Review | VS-64 |
| W2403 | Seasonal Markdown Strategy Effectiveness | VS-64 |
| W2404 | Seasonal Category Profitability Report | VS-64 |

**People** (3)

| ID | Workflow | Value Stream |
|---|---|---|
| W2872 | Wellness Program Effectiveness Analytics & ROI | VS-83 |
| W2889 | Employee Engagement Survey, Pulse & Sentiment Analytics | VS-84 |
| W2896 | Labor Relations KPI, Cost & Partnership Health Reporting | VS-84 |


**Promotion audit (21 → Tier 1, statutory execution):**

- **Finance** (3): W1823, W1824, W1829
- **Sell & Serve** (1): W2360
- **People** (17): W2850, W2852, W2853, W2858, W2859, W2863, W2864, W2866, W2873, W2875, W2876, W2883, W2884, W2885, W2886, W2887, W2888

**Demotion audit (30 → Tier 3, analytics/optimization):**

- **Finance** (2): W2748, W2752
- **Sell & Serve** (19): W1883, W1892, W2169, W2173, W2178, W2182, W2185, W2188, W2189, W2373, W2374, W2375, W2377, W2379, W2423, W2424, W2425, W2426, W2427
- **Plan & Source** (6): W2398, W2399, W2401, W2402, W2403, W2404
- **People** (3): W2872, W2889, W2896

---

### Mixed Operations Classification Pass (192 workflows; VS-57/58/66/69/70/71/74/101)

> **Hand-reviewed 2026-06-20 (batch 4).** Eight family-decisive VSs — competitive price
> intelligence, coupon/promotions, customer project services, typhoon/disaster response,
> solar energy, anti-counterfeit, contractor job-site delivery, merchandise financial
> planning. Genuine review: **15 → Tier 1** (typhoon-BCP emergency response, anti-
> counterfeit enforcement/investigation/regulatory-reporting, electrical-permit compliance,
> open-to-buy financial gate), **36 → Tier 3** (analytics: price-elasticity/markdown-optimization/
> coupon-ROI/halo-effect/trend, project-margin/scorecard, typhoon-after-action/financial-
> impact, solar-degradation/sales-analytics, counterfeit-trend/KPI, delivery-KPI/cost/route,
> markdown-optimization/vendor-margin/cluster-analytics/dashboard), **141 confirmed Tier 2**.
> Moves Check 1 unclassified 3,260 → 3,068.

#### Tier 1 — Statutory / emergency (15)

**Governance & Assurance** (13)

| ID | Workflow | Value Stream |
|---|---|---|
| W2507 | Typhoon Emergency Pricing Freeze Activation | VS-69 |
| W2510 | Store Emergency Closure Decision & Execution | VS-69 |
| W2511 | DC Emergency Shutdown & Asset Protection | VS-69 |
| W2513 | Real-Time Disaster Operations Center Activation | VS-69 |
| W2514 | Emergency Generator & Power Contingency Operations | VS-69 |
| W2517 | Active Typhoon Customer Safety & In-Store Emergency Protocol | VS-69 |
| W2518 | Post-Typhoon Store Damage Assessment & Rapid Reopening | VS-69 |
| W2558 | In-Store Counterfeit Product Detection & Seizure | VS-71 |
| W2559 | Counterfeit Investigation & Evidence Collection | VS-71 |
| W2561 | Law Enforcement & Regulatory Reporting for Counterfeiting | VS-71 |
| W2562 | Customer Counterfeit Product Exchange & Restitution | VS-71 |
| W2563 | Online Marketplace Counterfeit Monitoring & Takedown | VS-71 |
| W2565 | Internal Counterfeit Prevention & Staff Integrity Program | VS-71 |

**Sell & Serve** (1)

| ID | Workflow | Value Stream |
|---|---|---|
| W2538 | Solar Electrical Permit & LGU Compliance | VS-70 |

**Plan & Source** (1)

| ID | Workflow | Value Stream |
|---|---|---|
| W3283 | Open-to-Buy (OTB) Calculation, Maintenance & Weekly Recalculation | VS-101 |


#### Tier 2 — Operational (141)

**Governance & Assurance** (29)

| ID | Workflow | Value Stream |
|---|---|---|
| W2502 | Typhoon Season Pre-Positioning & Emergency Stock Planning | VS-69 |
| W2503 | Store-Level Typhoon Readiness Checklist Execution | VS-69 |
| W2504 | DC & Warehouse Typhoon Preparedness Protocol | VS-69 |
| W2505 | Emergency Merchandise Demand Surge Forecasting | VS-69 |
| W2506 | Pre-Typhoon Customer Communication & Advisory | VS-69 |
| W2508 | Pre-Typhoon Cash Float & Payment Contingency Setup | VS-69 |
| W2509 | Staff Safety Notification & Deployment Readiness | VS-69 |
| W2512 | Emergency Merchandise Rapid Replenishment Dispatch | VS-69 |
| W2515 | Disaster-Affected Employee Welfare & Deployment Tracking | VS-69 |
| W2516 | Emergency Vendor Coordination & Expedite Procurement | VS-69 |
| W2519 | Post-Disaster Inventory Loss Quantification & Insurance Claim | VS-69 |
| W2520 | Community Building Materials Donation & Relief Operations | VS-69 |
| W2521 | Post-Disaster Emergency Product Pricing & Availability Management | VS-69 |
| W2524 | Post-Disaster Vendor Recovery & Supply Chain Re-Establishment | VS-69 |
| W2525 | Annual Typhoon Season Readiness Program & Drill Execution | VS-69 |
| W2550 | High-Risk Product Serialization & Registration | VS-71 |
| W2551 | QR Code Authentication System Management | VS-71 |
| W2552 | Customer Product Verification Support | VS-71 |
| W2553 | Vendor Serialization Compliance Audit | VS-71 |
| W2554 | Product Authentication Data Platform Management | VS-71 |
| W2555 | Gray Market & Unauthorized Channel Detection | VS-71 |
| W2556 | Serialization Label & Packaging Standard Management | VS-71 |
| W2557 | Product Authentication Staff Training | VS-71 |
| W2560 | Vendor Counterfeit Alert & Coordination | VS-71 |
| W2566 | Vendor Anti-Counterfeit Compliance Program Management | VS-71 |
| W2567 | Supply Chain Integrity Audit & Verification | VS-71 |
| W2570 | Vendor Brand Protection Partnership Management | VS-71 |
| W2572 | Industry Anti-Counterfeit Collaboration & Intelligence Sharing | VS-71 |
| W2573 | Annual Anti-Counterfeit Strategy Review & Program Update | VS-71 |

**Sell & Serve** (59)

| ID | Workflow | Value Stream |
|---|---|---|
| W2238 | Coupon Design & Configuration | VS-58 |
| W2239 | Digital Voucher Distribution | VS-58 |
| W2240 | In-Store Coupon Printing & Display | VS-58 |
| W2241 | Coupon Budget & Liability Management | VS-58 |
| W2242 | Vendor-Funded Coupon Program | VS-58 |
| W2243 | Loyalty Point Multiplier Campaign | VS-58 |
| W2244 | Coupon Fraud Prevention Design | VS-58 |
| W2246 | In-Store Coupon Redemption | VS-58 |
| W2247 | Online Coupon & Promo Code Redemption | VS-58 |
| W2248 | Multi-Coupon Stacking Management | VS-58 |
| W2249 | Coupon Redemption Fraud Detection | VS-58 |
| W2250 | Coupon Return & Reversal | VS-58 |
| W2251 | Expired Coupon Exception Handling | VS-58 |
| W2252 | Digital Coupon Device & Account Binding | VS-58 |
| W2253 | Coupon Vendor Reconciliation | VS-58 |
| W2260 | Competitor Promotion Intelligence | VS-58 |
| W2430 | Customer Project Inquiry & Qualification | VS-66 |
| W2431 | In-Home Measurement Visit | VS-66 |
| W2432 | Kitchen & Bathroom Design Proposal | VS-66 |
| W2433 | Material Estimation & Specification | VS-66 |
| W2434 | Project Quotation & Pricing | VS-66 |
| W2435 | Design Revision & Customer Approval | VS-66 |
| W2436 | Design Consultant Training & Certification | VS-66 |
| W2437 | Design Software & Tool Management | VS-66 |
| W2438 | Project Sales Order Processing | VS-66 |
| W2439 | Project Material Procurement | VS-66 |
| W2440 | Project Delivery Coordination | VS-66 |
| W2441 | Project Installation Coordination | VS-66 |
| W2442 | Project Change Order Management | VS-66 |
| W2443 | Project Payment Collection & Milestone Billing | VS-66 |
| W2444 | Project Warranty Handover | VS-66 |
| W2445 | Project Material Returns & Surplus Handling | VS-66 |
| W2446 | Project Dashboard & Status Tracking | VS-66 |
| W2447 | Project Timeline Management | VS-66 |
| W2448 | Project Quality Inspection | VS-66 |
| W2449 | Project Completion & Punch List | VS-66 |
| W2450 | Post-Project Customer Follow-Up | VS-66 |
| W2453 | Project Services Annual Strategy Review | VS-66 |
| W2526 | Solar Product Assortment Planning & Vendor Selection | VS-70 |
| W2527 | In-Store Solar Consultation & System Sizing | VS-70 |
| W2528 | Solar Package & Bundle Configuration | VS-70 |
| W2529 | Solar Product Pricing & Net Metering ROI Calculator | VS-70 |
| W2530 | Solar Product Staff Training & Certification | VS-70 |
| W2531 | Solar Product Inventory & Lead Time Management | VS-70 |
| W2532 | Solar Lead Capture & CRM Funnel Management | VS-70 |
| W2533 | Solar Promotional Campaign & Trade Show Coordination | VS-70 |
| W2534 | Solar Site Survey & Assessment | VS-70 |
| W2535 | Solar Installation Partner Scheduling & Dispatch | VS-70 |
| W2536 | Net Metering Application & DU Coordination | VS-70 |
| W2537 | Solar Installation Quality Inspection & Commissioning | VS-70 |
| W2539 | Solar Installation Material Staging & Delivery Coordination | VS-70 |
| W2540 | Solar System Grid Connection & Net Metering Activation | VS-70 |
| W2541 | Solar Installation Warranty Registration & Handover | VS-70 |
| W2542 | Solar System Remote Monitoring & Performance Alerting | VS-70 |
| W2544 | Solar Warranty Claim & Vendor Recovery Processing | VS-70 |
| W2545 | Solar Installation Partner Performance Scoring | VS-70 |
| W2546 | Solar Customer Satisfaction & NPS Survey | VS-70 |
| W2548 | Solar Product Return & Exchange Processing | VS-70 |
| W2549 | Solar Market Intelligence & Regulatory Update Monitoring | VS-70 |

**Plan & Source** (34)

| ID | Workflow | Value Stream |
|---|---|---|
| W2214 | Competitor Price Scraping & Collection | VS-57 |
| W2215 | Price Matching Decision & Execution | VS-57 |
| W2216 | Competitor Promotion Monitoring | VS-57 |
| W2217 | Price Positioning Strategy Review | VS-57 |
| W2218 | Dynamic Pricing Rule Management | VS-57 |
| W2221 | Competitor Pricing Intelligence Report | VS-57 |
| W2222 | Rapid Price Response Workflow | VS-57 |
| W2223 | Promotional Price Planning | VS-57 |
| W2225 | Store-Level Price Override | VS-57 |
| W2226 | Price Change Communication to Stores | VS-57 |
| W2227 | Trade Price Competitive Alignment | VS-57 |
| W2228 | Price Audit & Compliance | VS-57 |
| W2229 | Customer Price Match Guarantee | VS-57 |
| W2232 | Vendor Cost-Driven Price Adjustment | VS-57 |
| W2233 | Pricing Strategy Annual Review | VS-57 |
| W2235 | Price Image & Customer Perception Survey | VS-57 |
| W2236 | Pricing System & Master Data Accuracy | VS-57 |
| W2237 | Cross-Channel Price Consistency | VS-57 |
| W3281 | Annual Merchandise Financial Plan & Sales/Margin Budget Development | VS-101 |
| W3282 | Seasonal Merchandise Plan & Department/Category Financial Plan | VS-101 |
| W3284 | Category & Sub-Class Receipt Planning & Commitment Tracking | VS-101 |
| W3285 | Markdown & Clearance Budget Allocation & Spend Authorization | VS-101 |
| W3286 | Gross-Margin Plan, Initial Markup (IMU) & Markdown-Margin Modeling | VS-101 |
| W3287 | Multi-Channel Revenue & Margin Allocation Planning | VS-101 |
| W3288 | Merchandise Plan-vs-Actual Review, In-Season Forecast & Reforecast | VS-101 |
| W3289 | Ending Stock & Weeks-of-Supply (WOS) Target Planning by Category | VS-101 |
| W3290 | Inventory Turn & GMROI Target Setting & Performance Tracking | VS-101 |
| W3291 | Stock-to-Sales Ratio & Flow Planning | VS-101 |
| W3292 | New-Store Inventory Investment Planning & Pre-Open Stock Build | VS-101 |
| W3293 | Discontinuation & Exit Inventory Liquidation Planning | VS-101 |
| W3294 | Aged/Slow-Mover Inventory Provisioning & Reserve Planning | VS-101 |
| W3295 | Import vs Domestic Inventory Investment & Landed-Cost Margin Planning | VS-101 |
| W3298 | Key-Item / Item-Class Performance Review & Reorder/Cancel Decisioning | VS-101 |
| W3303 | Markdown/OTB Audit & Merchandise Financial Control Review | VS-101 |

**Make & Move** (19)

| ID | Workflow | Value Stream |
|---|---|---|
| W2622 | Contractor Job Site Delivery Order Capture & Planning | VS-74 |
| W2623 | Multi-Drop Job Site Delivery Route Optimization | VS-74 |
| W2624 | Crane & Boom Truck Delivery Scheduling | VS-74 |
| W2625 | Phased Construction Delivery Schedule Management | VS-74 |
| W2626 | Emergency & Same-Day Contractor Delivery Processing | VS-74 |
| W2627 | Job Site Delivery Access & Permit Coordination | VS-74 |
| W2628 | Night & Weekend Delivery Scheduling | VS-74 |
| W2629 | Contractor Delivery Special Equipment Coordination | VS-74 |
| W2630 | Job Site Delivery Unloading & Material Placement | VS-74 |
| W2631 | Job Site Delivery Damage & Shortage Resolution | VS-74 |
| W2632 | Delivery Return & Excess Material Pickup | VS-74 |
| W2633 | Job Site Delivery Proof of Delivery & Documentation | VS-74 |
| W2634 | Contractor Site Safety Compliance During Delivery | VS-74 |
| W2635 | Bulk Material Handling at Job Site | VS-74 |
| W2636 | Job Site Delivery Quality Verification | VS-74 |
| W2637 | Job Site Delivery Real-Time Tracking & ETA Communication | VS-74 |
| W2640 | Contractor Delivery Satisfaction Survey & Feedback | VS-74 |
| W2643 | 3PL Partner Performance for Contractor Deliveries | VS-74 |
| W2645 | Annual Contractor Delivery Strategy Review | VS-74 |


#### Tier 3 — Analytics (36)

**Governance & Assurance** (6)

| ID | Workflow | Value Stream |
|---|---|---|
| W2522 | Typhoon Event After-Action Review & Lessons Learned | VS-69 |
| W2523 | Disaster Recovery Financial Impact Reporting & Budget Rebalancing | VS-69 |
| W2564 | Counterfeit Trend Analysis & Threat Assessment | VS-71 |
| W2568 | Anti-Counterfeit Technology Evaluation & Deployment | VS-71 |
| W2569 | Counterfeit Financial Impact & Loss Reporting | VS-71 |
| W2571 | Anti-Counterfeit KPI Dashboard & Executive Reporting | VS-71 |

**Sell & Serve** (12)

| ID | Workflow | Value Stream |
|---|---|---|
| W2245 | Coupon Performance Dashboard | VS-58 |
| W2254 | Campaign ROI Analysis | VS-58 |
| W2255 | Channel-Specific Promotion Effectiveness | VS-58 |
| W2256 | Customer Segment Promotion Response | VS-58 |
| W2257 | Promotion Halo Effect Analysis | VS-58 |
| W2258 | Year-over-Year Promotion Trend | VS-58 |
| W2259 | Digital Coupon Technology Performance | VS-58 |
| W2261 | Promotion Calendar Optimization | VS-58 |
| W2451 | Project Revenue & Margin Analysis | VS-66 |
| W2452 | Project Consultant Performance Scorecard | VS-66 |
| W2543 | Solar Panel Performance Degradation Tracking | VS-70 |
| W2547 | Solar Sales Analytics & Revenue Attribution | VS-70 |

**Plan & Source** (13)

| ID | Workflow | Value Stream |
|---|---|---|
| W2219 | Market Basket Price Comparison | VS-57 |
| W2220 | Price Elasticity Analysis | VS-57 |
| W2224 | Markdown Optimization for Clearance | VS-57 |
| W2230 | Gross Margin Analysis by Category | VS-57 |
| W2231 | Price Sensitivity Dashboard | VS-57 |
| W2234 | Promotional Pricing ROI Analysis | VS-57 |
| W3296 | Inventory Investment Scenario Modeling & Working-Capital Constraint | VS-101 |
| W3297 | Weekly Merchandise P&A Reporting & Variance Analysis | VS-101 |
| W3299 | Markdown Optimization & Price-Engineering Analytics | VS-101 |
| W3300 | Promotion Post-Mortem, Halo & Cannibalization Margin Analysis | VS-101 |
| W3301 | Vendor Margin Contribution, Terms & Rebate Impact Analysis | VS-101 |
| W3302 | Store/Cluster Merchandise Performance & Localization Analytics | VS-101 |
| W3304 | Merchandise KPI Dashboard, Category Scorecard & Executive Review | VS-101 |

**Make & Move** (5)

| ID | Workflow | Value Stream |
|---|---|---|
| W2638 | Contractor Delivery On-Time Performance Measurement | VS-74 |
| W2639 | Contractor Delivery Cost per Order Analytics | VS-74 |
| W2641 | Contractor Delivery Route Optimization Analytics | VS-74 |
| W2642 | Emergency Delivery Frequency & Root Cause Analysis | VS-74 |
| W2644 | Contractor Delivery KPI Dashboard | VS-74 |


**Promotion audit (15 → Tier 1):**
- **Governance & Assurance** (13): W2507, W2510, W2511, W2513, W2514, W2517, W2518, W2558, W2559, W2561, W2562, W2563, W2565
- **Sell & Serve** (1): W2538
- **Plan & Source** (1): W3283

**Demotion audit (36 → Tier 3):**
- **Plan & Source** (13): W2219, W2220, W2224, W2230, W2231, W2234, W3296, W3297, W3299, W3300, W3301, W3302, W3304
- **Sell & Serve** (12): W2245, W2254, W2255, W2256, W2257, W2258, W2259, W2261, W2451, W2452, W2543, W2547
- **Governance & Assurance** (6): W2522, W2523, W2564, W2568, W2569, W2571
- **Make & Move** (5): W2638, W2639, W2641, W2642, W2644

---

### Shared Services & Specialized Support Classification Pass (192 workflows; VS-103/106/107/109/115/116/119/123)

> **Hand-reviewed 2026-06-20 (batch 5).** Eight VSs — HR shared services, commodity-risk,
> strategic key-account, store remodel, calibration/metrology, performance-bond/surety,
> whistleblower/ethics, skilled-trade apprenticeship. **18 → Tier 1** (PFRS 9 hedge
> accounting, DTI Weights & Measures compliance, bid/performance-bond statutory issuance,
> speak-up/whistleblower investigations & anti-retaliation, TESDA apprenticeship compliance);
> **36 → Tier 3** (analytics); **138 confirmed Tier 2**. Moves Check 1 3,068 → 2,876.

#### Tier 1 — Statutory (18)

**People** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W3811 | TESDA Program Registration, Dual-Training & Compliance | VS-123 |
| W3812 | Apprenticeship Funding, Stipend & DOLE Labor Compliance | VS-123 |
| W3815 | Apprenticeship Records, Certification Issuance & Compliance Documentation | VS-123 |
| W3831 | Trade-Certification Compliance Audit & External Accreditation Maintenance | VS-123 |

**Plan & Source** (1)

| ID | Workflow | Value Stream |
|---|---|---|
| W3413 | Hedge Accounting (PFRS 9), Effectiveness & Mark-to-Market Reporting | VS-106 |

**Technology & Data** (2)

| ID | Workflow | Value Stream |
|---|---|---|
| W3633 | DTI Weights & Measures Compliance & Inspection | VS-115 |
| W3639 | Customer Measurement Dispute & Resolution | VS-115 |

**Finance** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W3649 | Bid Bond Application & Issuance | VS-116 |
| W3650 | Performance & Payment Bond Application & Issuance | VS-116 |
| W3658 | Bond Claim, Demand & Default Response Management | VS-116 |
| W3660 | Bond Dispute, Litigation & Resolution | VS-116 |

**Governance & Assurance** (7)

| ID | Workflow | Value Stream |
|---|---|---|
| W3715 | Speak-Up Channel Operations & Multi-Channel Intake | VS-119 |
| W3716 | Whistleblower Anonymity, Confidentiality & Protection Framework | VS-119 |
| W3721 | Investigation Planning, Scoping & Evidence Collection | VS-119 |
| W3722 | Investigation Interview & Witness Management | VS-119 |
| W3723 | Investigation Finding, Conclusion & Adjudication | VS-119 |
| W3725 | Retaliation Monitoring & Protection | VS-119 |
| W3727 | External/Regulatory Reporting & Law-Enforcement Coordination | VS-119 |


#### Tier 2 — Operational (138)

**People** (34)

| ID | Workflow | Value Stream |
|---|---|---|
| W3329 | Employee Service Center (HR Helpdesk) Case Intake, Triage & Resolution | VS-103 |
| W3330 | Employee Self-Service (ESS) & Manager Self-Service (MSS) Portal Operations | VS-103 |
| W3331 | HR Case Management, Knowledge Base & Tiered Escalation | VS-103 |
| W3332 | Multi-Entity HR Shared Services Delivery & Cross-Entity Case Routing | VS-103 |
| W3333 | Employee Document Management, e-Signature & HR Records | VS-103 |
| W3334 | HR Transaction Processing (Verifications, Certifications, Employment Letters) | VS-103 |
| W3335 | Employee Lifecycle Event Service (Onboarding/Change/Separation Ticket Execution) | VS-103 |
| W3337 | Employee Onboarding Experience & Day-1 Readiness Program | VS-103 |
| W3338 | Employee Engagement Pulse, Survey Operations & Action Planning | VS-103 |
| W3339 | Internal Communications, Intranet & Company-Wide Broadcast Operations | VS-103 |
| W3340 | Town Hall, Leadership Communication & All-Hands Event Management | VS-103 |
| W3341 | Recognition & Peer-to-Peer Appreciation Platform Operations | VS-103 |
| W3342 | Employee Feedback Loop, Suggestion & Idea Management | VS-103 |
| W3343 | Diversity, Equity & Inclusion (DEI) Program Operations | VS-103 |
| W3345 | Workforce Planning, Headcount Forecasting & Capacity Planning | VS-103 |
| W3350 | HR Data Governance, Integration & People-Data Quality | VS-103 |
| W3351 | HR Technology (HRIS/Core-HR) Administration & Configuration Management | VS-103 |
| W3809 | Trade-Capability Strategy & Apprenticeship Program Charter | VS-123 |
| W3810 | Apprenticeship Curriculum & Competency Standard Design | VS-123 |
| W3813 | Apprenticeship Governance, Authority & Policy | VS-123 |
| W3814 | Apprentice Recruitment, Selection & Employer-Brand Linkage | VS-123 |
| W3817 | Apprenticeship Cohort Planning, Scheduling & Resource Allocation | VS-123 |
| W3818 | Apprentice On-the-Job Training, Rotation & Store Assignment Operations | VS-123 |
| W3819 | Trade Competency Assessment, Practical Examination & Certification Sign-Off | VS-123 |
| W3820 | Mentor / Master-Tradesperson Network & Coaching Operations | VS-123 |
| W3821 | Apprentice Progress Tracking, Feedback & Welfare Management | VS-123 |
| W3822 | Apprentice-to-Role Conversion, Placement & Career Pathway | VS-123 |
| W3823 | Apprenticeship Safety, PPE & Trade-Specific HSE Integration | VS-123 |
| W3824 | Apprenticeship Vendor/Product Training Integration & Sponsorship | VS-123 |
| W3825 | Vocational School, Senior-High & TESDA Partner Network Management | VS-123 |
| W3826 | Vocational Feeder Pipeline, OJT Placement & School-to-Work Transition | VS-123 |
| W3827 | Instructor / Master-Trainer Pipeline, Qualification & Development | VS-123 |
| W3828 | Assessor Qualification, Standardization & Calibration | VS-123 |
| W3829 | Trade Knowledge Management, Content Library & Curriculum Asset Management | VS-123 |

**Plan & Source** (19)

| ID | Workflow | Value Stream |
|---|---|---|
| W3401 | Commodity Exposure Mapping by SKU / Category / Vendor | VS-106 |
| W3402 | Bill-of-Material (BOM) & Input-Cost Decomposition Modeling | VS-106 |
| W3403 | Commodity Market-Price Intelligence & Benchmark Data Management | VS-106 |
| W3405 | Vendor Cost-Structure & Pass-Through Clause Transparency | VS-106 |
| W3406 | Commodity Risk Register, Appetite & Governance Framework | VS-106 |
| W3407 | Market Outlook, Forecast & Commodity Intelligence Briefing | VS-106 |
| W3409 | Commodity Mitigation Strategy Selection & Hedge Program Design | VS-106 |
| W3410 | Forward Buying, Strategic Inventory & Physical Hedge Execution | VS-106 |
| W3411 | Indexed / Formula / Floating Vendor Contract Structuring | VS-106 |
| W3412 | Financial Commodity Hedge Execution, Broker & Counterparty Management | VS-106 |
| W3414 | Vendor Raw-Material Surcharge & Formula-Price Administration | VS-106 |
| W3415 | Long-Term Supply Agreement & Volume Commitment Negotiation | VS-106 |
| W3416 | Hedge & Mitigation Performance Review and Strategy Adjustment | VS-106 |
| W3417 | Input-Cost-to-Price Pass-Through Governance & SRP/Cost Adjustment | VS-106 |
| W3418 | Rapid Commodity-Shock Price Response & Margin Recovery | VS-106 |
| W3420 | Competitor Price-Sensitivity & Pass-Through Feasibility Assessment | VS-106 |
| W3421 | Vendor Recovery / Claim & Commodity Savings Capture | VS-106 |
| W3422 | Commodity-Driven Markdown & Clearance Discipline | VS-106 |
| W3424 | Commodity Risk Policy Compliance, Audit & Continuous Improvement | VS-106 |

**Sell & Serve** (18)

| ID | Workflow | Value Stream |
|---|---|---|
| W3425 | Strategic Account Definition, Tiering & Selection Criteria | VS-107 |
| W3426 | Strategic Account Identification, Qualification & Onboarding to KAM | VS-107 |
| W3427 | Key Account Plan (KAP) Development & Annual Joint Business Planning | VS-107 |
| W3428 | Account Team Structure, Assignment & Executive Sponsorship | VS-107 |
| W3429 | Strategic Account Relationship Map & Stakeholder Management | VS-107 |
| W3430 | Account Governance Cadence: QBR, Operating Reviews & Joint Planning | VS-107 |
| W3431 | Cross-Functional Account Coordination & Internal Alignment | VS-107 |
| W3432 | Strategic Account Compliance, Ethics & Conflict-of-Interest Governance | VS-107 |
| W3434 | Enterprise Pricing, Contract & Trading-Terms Negotiation | VS-107 |
| W3435 | Solutioning & Value-Proposition Development for Strategic Accounts | VS-107 |
| W3436 | Strategic Project Pursuit, Bid Strategy & Win-Plan | VS-107 |
| W3437 | Customer Success, Adoption & Product/Service Expansion | VS-107 |
| W3438 | Executive-to-Executive Engagement & C-Suite Relationship Programs | VS-107 |
| W3439 | Joint Marketing, CSR & Co-Marketing with Strategic Accounts | VS-107 |
| W3440 | Strategic Account Innovation, Feedback & Co-Creation Loop | VS-107 |
| W3443 | Account Performance Scorecard & Tier Health Assessment | VS-107 |
| W3444 | Strategic Account Credit, Concentration & Receivable Risk Management | VS-107 |
| W3446 | At-Risk Account Identification, Save-Plan & Win-Back | VS-107 |

**Asset & Infrastructure** (20)

| ID | Workflow | Value Stream |
|---|---|---|
| W3473 | Store Lifecycle & Remodel Portfolio Strategy | VS-109 |
| W3474 | Store Performance Assessment & Remodel Trigger / Qualification | VS-109 |
| W3475 | Remodel Concept, Format & Scope Definition | VS-109 |
| W3476 | Remodel Business Case, Capex Funding & Approval | VS-109 |
| W3477 | Store Design, Layout & Fixture Planning | VS-109 |
| W3478 | Remodel Merchandising & Assortment Reset Planning | VS-109 |
| W3479 | Remodel Site Survey, Permitting & Regulatory Compliance | VS-109 |
| W3480 | Remodel Project Plan, Phasing & Live-Operations Continuity | VS-109 |
| W3481 | Remodel Fixture, Equipment & FF&E Procurement | VS-109 |
| W3482 | Remodel Construction Vendor Selection & Contracting | VS-109 |
| W3483 | Remodel Construction Execution & Site Coordination | VS-109 |
| W3484 | Remodel Mechanical, Electrical, Plumbing & HVAC Works | VS-109 |
| W3485 | Store Fixture Installation, Signage & Graphics Rollout | VS-109 |
| W3486 | Remodel Technology & POS / IT Refresh | VS-109 |
| W3487 | Remodel Merchandise Reset, Restock & Planogram Implementation | VS-109 |
| W3488 | Remodel Quality, Snag List & Commissioning / Handover | VS-109 |
| W3489 | Remodel Soft Launch / Grand Re-opening & Marketing | VS-109 |
| W3490 | Remodel Staff Training & Change Management | VS-109 |
| W3495 | Store Refurbishment Cadence & Lifecycle Refresh Planning | VS-109 |
| W3496 | Store Format Innovation & Remodel Program Governance | VS-109 |

**Technology & Data** (18)

| ID | Workflow | Value Stream |
|---|---|---|
| W3617 | Calibration & Metrology Program Strategy & Governance | VS-115 |
| W3618 | Measurement Standards, Traceability & ISO 17025 Alignment | VS-115 |
| W3619 | Calibration Intervals, Tolerance & MRA Methodology | VS-115 |
| W3620 | Calibration Master Data & Device Registry | VS-115 |
| W3621 | External Calibration Lab Qualification & Vendor Management | VS-115 |
| W3622 | In-House Calibration Operations & Standards Lab | VS-115 |
| W3623 | Calibration Training, Competency & Technician Certification | VS-115 |
| W3624 | Calibration Audit, Documentation & Records | VS-115 |
| W3625 | POS Scale & Weight-Based Item Calibration | VS-115 |
| W3626 | Catch-Weight & Bulk Material Scale Calibration | VS-115 |
| W3627 | Cutting Equipment Measurement Calibration | VS-115 |
| W3628 | Paint Mixing & Tinting Dispenser Calibration | VS-115 |
| W3629 | DC Weighbridge & Truck Scale Calibration | VS-115 |
| W3630 | Fuel & Logistics Measurement Calibration | VS-115 |
| W3631 | Environmental & Process Instrument Calibration | VS-115 |
| W3632 | Test & Measurement Tool Calibration | VS-115 |
| W3634 | Out-of-Tolerance Investigation & Measurement Correction | VS-115 |
| W3636 | Device Lifecycle, Repair & Retirement Management | VS-115 |

**Finance** (16)

| ID | Workflow | Value Stream |
|---|---|---|
| W3641 | Surety & Guarantee Program Strategy & Governance | VS-116 |
| W3642 | Surety Facility, Line & Counter-Indemnity Management | VS-116 |
| W3643 | Surety Provider & Bank Guarantee Relationship Management | VS-116 |
| W3644 | Indemnity Agreement, Collateral & Security Management | VS-116 |
| W3645 | Surety Pricing, Cost & Facility Optimization | VS-116 |
| W3646 | Surety Risk, Capacity & Encumbrance Planning | VS-116 |
| W3647 | Surety Program Policy, Authority & Approval Matrix | VS-116 |
| W3648 | Surety Program Audit, Documentation & Records | VS-116 |
| W3651 | Warranty & Retention Bond Management | VS-116 |
| W3652 | Bank Guarantee Issuance & LC-for-Guarantee Management | VS-116 |
| W3653 | Cash Retention, Margin & Escrow Management | VS-116 |
| W3654 | Bond/Guarantee Tracking, Encumbrance & Register Management | VS-116 |
| W3655 | Multi-Entity Bond Coordination | VS-116 |
| W3656 | Bond Amendment, Extension & Renewal Management | VS-116 |
| W3657 | Bond Release, Retrieval & Closeout | VS-116 |
| W3659 | Counter-Indemnity Call, Recovery & Subrogation | VS-116 |

**Governance & Assurance** (13)

| ID | Workflow | Value Stream |
|---|---|---|
| W3713 | Ethics & Integrity Program Strategy & Governance | VS-119 |
| W3714 | Code of Conduct, Ethics Policy & Standards Management | VS-119 |
| W3717 | Report Triage, Classification & Routing | VS-119 |
| W3718 | Ethics Awareness, Training & Culture Program | VS-119 |
| W3719 | Ethics Committee & Case Governance | VS-119 |
| W3720 | Speak-Up Vendor/Platform & Records Management | VS-119 |
| W3724 | Disciplinary, Corrective & Remediation Action | VS-119 |
| W3726 | ABC/AML/Audit/Legal Investigation Coordination | VS-119 |
| W3728 | Case Closure, Documentation & Lessons Learned | VS-119 |
| W3732 | Conflict of Interest & Gifts/Integrity Disclosure Management | VS-119 |
| W3733 | Third-Party & Supply-Chain Integrity Due Diligence | VS-119 |
| W3734 | Ethics Program Audit & Assurance | VS-119 |
| W3735 | Multi-Entity Ethics Coordination & Governance Reporting | VS-119 |


#### Tier 3 — Analytics (36)

**People** (10)

| ID | Workflow | Value Stream |
|---|---|---|
| W3336 | HR Service Center SLA, Quality & CSAT Monitoring | VS-103 |
| W3344 | Employee Value Proposition, Culture & EX Measurement | VS-103 |
| W3346 | Recruitment Analytics, Time-to-Fill & Hiring-Funnel Reporting | VS-103 |
| W3347 | Turnover/Attrition Analytics, Retention Risk & Exit Insight | VS-103 |
| W3348 | Diversity, Pay-Equity & Workforce Composition Reporting | VS-103 |
| W3349 | HR Dashboard, Scorecard & Executive People Report Operations | VS-103 |
| W3352 | HR Process Excellence, Automation & Continuous Improvement | VS-103 |
| W3816 | Apprenticeship Program Continuous Improvement & Curriculum Refresh | VS-123 |
| W3830 | Trade-Capability Workforce Planning & Demand Modeling | VS-123 |
| W3832 | Trade-Capability Analytics, ROI & Program Effectiveness Reporting | VS-123 |

**Plan & Source** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W3404 | Commodity Sensitivity, Value-at-Risk (VaR) & Exposure Measurement | VS-106 |
| W3408 | Import-FX-Commodity Interaction & Landed-Cost Exposure Analysis | VS-106 |
| W3419 | Maintained-Margin Impact Analysis & Commodity Variance Reporting | VS-106 |
| W3423 | Input-Cost Risk Dashboard & Executive/Board Reporting | VS-106 |

**Sell & Serve** (6)

| ID | Workflow | Value Stream |
|---|---|---|
| W3433 | Share-of-Wallet, Opportunity & White-Space Analysis | VS-107 |
| W3441 | Account-Level Profitability, Cost-to-Serve & Margin Analytics | VS-107 |
| W3442 | Strategic Account Revenue Forecasting & Pipeline Analytics | VS-107 |
| W3445 | Customer Lifetime Value (CLV), Retention Economics & Churn Prediction | VS-107 |
| W3447 | Strategic Account Loss & Competitive-Displacement Analysis | VS-107 |
| W3448 | KAM Program Performance, ROI & Executive/Board Reporting | VS-107 |

**Asset & Infrastructure** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W3491 | Post-Remodel Sales Lift & Performance Tracking | VS-109 |
| W3492 | Remodel Customer Experience & Feedback Assessment | VS-109 |
| W3493 | Remodel Capex Variance & Post-Implementation Review | VS-109 |
| W3494 | Remodel Lessons Learned & Store-Lifecycle Knowledge Management | VS-109 |

**Technology & Data** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W3635 | Measurement Variance, Revenue Impact & Loss Analytics | VS-115 |
| W3637 | Calibration Cost, Outsourcing & Service-Level Analytics | VS-115 |
| W3638 | Measurement System Analysis (MSA) & Gage R&R | VS-115 |
| W3640 | Metrology Maturity, Continuous Improvement & Innovation | VS-115 |

**Finance** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W3661 | Surety Spend, Encumbrance & Cost Analytics | VS-116 |
| W3662 | Surety Provider Performance & Scorecard | VS-116 |
| W3663 | Contract / Bond Compliance & Performance Analytics | VS-116 |
| W3664 | Surety Program Maturity & Continuous Improvement | VS-116 |

**Governance & Assurance** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W3729 | Ethics & Speak-Up Analytics & KPI Reporting | VS-119 |
| W3730 | Ethics Risk Assessment & Heat-Mapping | VS-119 |
| W3731 | Culture, Engagement & Trust Measurement | VS-119 |
| W3736 | Ethics Program Maturity & Continuous Improvement | VS-119 |


**Promotion audit (18 → Tier 1):**
- **Finance** (4): W3649, W3650, W3658, W3660
- **Technology & Data** (2): W3633, W3639
- **Governance & Assurance** (7): W3715, W3716, W3721, W3722, W3723, W3725, W3727
- **People** (4): W3811, W3812, W3815, W3831

**Demotion audit (36 → Tier 3):**
- **People** (10): W3336, W3344, W3346, W3347, W3348, W3349, W3352, W3816, W3830, W3832
- **Plan & Source** (4): W3404, W3408, W3419, W3423
- **Sell & Serve** (6): W3433, W3441, W3442, W3445, W3447, W3448
- **Asset & Infrastructure** (4): W3491, W3492, W3493, W3494
- **Technology & Data** (4): W3635, W3637, W3638, W3640
- **Finance** (4): W3661, W3662, W3663, W3664
- **Governance & Assurance** (4): W3729, W3730, W3731, W3736

---

### Sales & Transformation Classification Pass (192 workflows; VS-124/130/132/134/137/140/155/159)

> **Hand-reviewed 2026-06-20 (batch 6).** Eight VSs — sales enablement, corporate development/
> M&A, political engagement, OCM/digital-adoption, PIM/DAM, field sales, trade-in/buy-back,
> corporate security. **10 → Tier 1** (PCC merger notification, political-contribution disclosure,
> election-period compliance, anti-graft controls, K&R/active-assailant response, corporate
> investigations); **24 → Tier 3** (analytics/CI); **158 T2**. → 2,684 unclassified (45.9%).

#### Tier 1 (10)

**Governance & Assurance** (10)

| ID | Workflow | Value Stream |
|---|---|---|
| W3992 | Regulatory Clearance, PCC Merger Notification & Antitrust Approval | VS-130 |
| W4027 | Political Contribution & Donation Policy, Approval & Disclosure | VS-132 |
| W4028 | Lobbying, Advocacy & Public-Affairs Activity Governance & Disclosure | VS-132 |
| W4033 | Election-Period Compliance Protocol (Omnibus Election Code, RA 9006, COMELEC) | VS-132 |
| W4034 | Campaign-Finance, Contribution-Limit & Prohibited-Donation Controls | VS-132 |
| W4037 | Government Official, Employee & Procurement Interaction (Anti-Graft) Controls | VS-132 |
| W4686 | Kidnap & Ransom (K&R), Extortion & Blackmail Response Protocol | VS-159 |
| W4689 | Corporate Investigations: Fraud, Theft, Embezzlement & IP Misappropriation | VS-159 |
| W4692 | Active-Assailant, Civil-Unrest & Protest / Crowd Response Protocol | VS-159 |
| W4693 | Surveillance, Evidence Collection & Coordination with Law Enforcement (PNP/NBI) | VS-159 |


#### Tier 2 (158)

**Sell & Serve** (57)

| ID | Workflow | Value Stream |
|---|---|---|
| W3833 | Sales Enablement Strategy, Operating Model & Governance | VS-124 |
| W3834 | Selling-Skills Curriculum & Consultative Selling Playbook Development | VS-124 |
| W3835 | Department & Category Selling Playbooks (Attachment, Linked, Project Selling) | VS-124 |
| W3836 | Sales Coaching, Field Enablement & Store-Level Reinforcement | VS-124 |
| W3837 | Trade-Pro / B2B Consultative Selling Enablement | VS-124 |
| W3838 | Sales Contest, Incentive & Motivation Program Design | VS-124 |
| W3839 | Sales Enablement Technology & Content Delivery Platform | VS-124 |
| W3841 | Product Knowledge Mastery Program & Role-Based Knowledge Standards | VS-124 |
| W3842 | Product Knowledge Certification, Assessment & Recertification | VS-124 |
| W3843 | New-Product Launch Enablement & Rapid Knowledge Rollout | VS-124 |
| W3844 | Clienteling Tool, Customer-360 & Associate Mobile Selling Assistant | VS-124 |
| W3845 | Loyalty, Identification & Enrollment Enablement at Point of Sale | VS-124 |
| W3846 | Service / Installation / Add-On Selling Enablement | VS-124 |
| W3847 | Selling Quality Assurance, Mystery Shopping & Customer Interaction Audit | VS-124 |
| W3848 | Product Knowledge Content & Vendor Training Governance | VS-124 |
| W3856 | Executive Selling-Performance Review & Commercial Linkage | VS-124 |
| W4217 | Field Sales Strategy & Go-to-Coverage Model | VS-140 |
| W4218 | Force Sizing, Structure & Role Design | VS-140 |
| W4219 | Territory Design, Alignment & Balancing | VS-140 |
| W4220 | Account Segmentation, Tiering & Coverage Plan | VS-140 |
| W4221 | Quota, Target Setting & Capacity Planning | VS-140 |
| W4222 | Route-to-Market & Channel Assignment (Field vs Digital vs Store) | VS-140 |
| W4223 | Field Sales Onboarding, Enablement & Certification | VS-140 |
| W4224 | Field Sales Tooling, CRM & Mobility Platform | VS-140 |
| W4225 | Daily Route & Call Planning | VS-140 |
| W4226 | Customer Visit, Needs Analysis & Relationship Management | VS-140 |
| W4227 | Project Discovery, Estimating & Quoting | VS-140 |
| W4228 | Opportunity, Pipeline & Forecast Management | VS-140 |
| W4229 | Field Order Capture, Pricing & Fulfillment Coordination | VS-140 |
| W4230 | Project Bid, Tender & Specification Pursuit | VS-140 |
| W4231 | Field Sample, Demo & Merchandising Support | VS-140 |
| W4232 | Compliance, ABC & Data-Quality in the Field | VS-140 |
| W4233 | Field Sales Performance & Quota Attainment Management | VS-140 |
| W4234 | Field Sales Compensation & Incentive Administration | VS-140 |
| W4237 | Customer Retention, Churn & Account-Health Management | VS-140 |
| W4238 | Field Sales Coaching, Performance Management & Recognition | VS-140 |
| W4577 | Trade-In Program Strategy, Scope & Economics | VS-155 |
| W4578 | Eligible-Product & Take-Back Channel Policy | VS-155 |
| W4579 | Trade-In Valuation Engine & Condition-Grading Model | VS-155 |
| W4580 | Trade-In Credit, Pricing & New-Purchase Linkage | VS-155 |
| W4581 | Certified Pre-Owned Pricing, Margin & Positioning | VS-155 |
| W4583 | Warranty, Liability & Consumer-Protection Framework | VS-155 |
| W4584 | Systems, Item-Coding & Inventory Setup for Pre-Owned | VS-155 |
| W4585 | Customer Take-Back Intake & Custody Transfer | VS-155 |
| W4586 | Intake Inspection, Safety Screen & Data Wipe | VS-155 |
| W4587 | Triage, Routing & Disposition Decision | VS-155 |
| W4588 | Refurbishment Processing (Repair, Refinish, Parts Replacement) | VS-155 |
| W4589 | Certification Testing, Grading & Certification Issuance | VS-155 |
| W4590 | Parts Harvesting, Recycling & Non-Certified Disposition | VS-155 |
| W4591 | Refurbishment Quality, Cost Tracking & Service-Center Operations | VS-155 |
| W4592 | Refurbisher Safety, HSE & Hazmat Handling | VS-155 |
| W4593 | Certified Pre-Owned Listing, Content & Channel Syndication | VS-155 |
| W4594 | Resale Order, Pricing Integrity & Checkout | VS-155 |
| W4595 | Pre-Owned Fulfillment, Pickup & Delivery | VS-155 |
| W4596 | Certified Pre-Owned Warranty Claim & Service | VS-155 |
| W4597 | Pre-Owned Returns, Refunds & Re-disposition | VS-155 |
| W4598 | Customer Experience, Trust & Reviews Management | VS-155 |

**Governance & Assurance** (79)

| ID | Workflow | Value Stream |
|---|---|---|
| W3977 | Corporate Development & Growth Strategy, Portfolio & Capital Allocation | VS-130 |
| W3978 | Inorganic Growth Strategy & Build-vs-Buy-vs-Partner Framework | VS-130 |
| W3979 | Acquisition Target Sourcing, Pipeline & Deal Origination | VS-130 |
| W3980 | Target Screening, Strategic Fit & Preliminary Assessment | VS-130 |
| W3981 | Financial Modeling, Valuation & Investment Sizing | VS-130 |
| W3982 | Deal Structuring, Term Sheet & Letter of Intent (LOI) Negotiation | VS-130 |
| W3983 | M&A Governance, Approval Authority & Stage-Gate Process | VS-130 |
| W3984 | M&A Project Setup, Deal Team & Deal Management Office | VS-130 |
| W3985 | Commercial & Strategic Due Diligence | VS-130 |
| W3986 | Financial & Tax Due Diligence | VS-130 |
| W3987 | Legal, Regulatory & Corporate Due Diligence | VS-130 |
| W3988 | Operational, IT, Systems & Integration Due Diligence | VS-130 |
| W3989 | HR, People & Culture Due Diligence (incl. Labor/Union) | VS-130 |
| W3990 | ESG, Environmental & Compliance Due Diligence | VS-130 |
| W3991 | Purchase Agreement (SPA), Negotiation & Signing Management | VS-130 |
| W3993 | Post-Merger Integration (PMI) Strategy, Planning & Synergy Realization | VS-130 |
| W3994 | Day-1 Readiness, Cutover & Transaction Close Management | VS-130 |
| W3995 | Systems, Data & ERP Integration for Acquired Entities | VS-130 |
| W3996 | Organization, Culture & Change Integration Management | VS-130 |
| W3997 | Carve-Out, Separation & Transitional Service Agreement (TSA) Management | VS-130 |
| W3998 | Divestiture & Asset/Entity Disposal Execution | VS-130 |
| W3999 | Joint Venture & Strategic Partnership Post-Close Management | VS-130 |
| W4025 | Corporate Political Engagement Policy, Governance & Operating Model | VS-132 |
| W4026 | Political Activity Risk Assessment & Stakeholder / Issue Mapping | VS-132 |
| W4029 | Trade Association, Industry-Body & Third-Party Advocacy Membership Review | VS-132 |
| W4030 | Employee Political Activity, Time-Off & Non-Coercion Governance | VS-132 |
| W4031 | Political-Engagement Vendor, Consultant & PAC (if any) Management | VS-132 |
| W4032 | Political Engagement Records, Transparency & Public Disclosure | VS-132 |
| W4035 | Election-Period Marketing, Advertising & Promotion Restrictions | VS-132 |
| W4036 | Candidate Engagement, Endorsement & Non-Partisanship Governance | VS-132 |
| W4038 | Revolving-Door, Post-Employment & Confidential-Information Controls | VS-132 |
| W4039 | Grassroots & Employee Advocacy Governance & Compliance | VS-132 |
| W4040 | Political Intelligence, Monitoring & Early-Warning System | VS-132 |
| W4041 | Political-Engagement Stakeholder & Relationship Management | VS-132 |
| W4042 | Public-Affairs Position Development, Submission & Advocacy Execution | VS-132 |
| W4044 | Coalition, Partnership & Multi-Stakeholder Initiative Governance | VS-132 |
| W4045 | Crisis Political & Reputational Issue Management | VS-132 |
| W4046 | Political-Engagement Compliance Audit & Assurance | VS-132 |
| W4048 | Political-Engagement Program Review, Continuous Improvement & Board Oversight | VS-132 |
| W4073 | OCM Strategy, Operating Model & Transformation Governance | VS-134 |
| W4074 | Change Portfolio Prioritization & Capacity Planning | VS-134 |
| W4075 | Stakeholder Mapping, Analysis & Engagement Planning | VS-134 |
| W4076 | Change Impact Assessment & Affected-Person Analysis | VS-134 |
| W4077 | Organizational Readiness & Change Culture Assessment | VS-134 |
| W4078 | Change Risk Assessment & Mitigation Planning | VS-134 |
| W4079 | Executive Sponsorship Activation & Alignment | VS-134 |
| W4080 | OCM Resource, Competency & Partner Management | VS-134 |
| W4081 | Change Communications Strategy, Messaging & Channel Plan | VS-134 |
| W4082 | Transformation Roadmap, Sequencing & Change Saturation Management | VS-134 |
| W4083 | Leadership & Manager Change Cascade & "Equip-the-Manager" Program | VS-134 |
| W4084 | Frontline Change Champion / Super-User Network Operations | VS-134 |
| W4085 | Resistance Management & Change Intervention | VS-134 |
| W4086 | Change Event & Engagement Campaign Execution | VS-134 |
| W4087 | Go-Live Readiness, Cutover Support & Hypercare | VS-134 |
| W4088 | Cross-Functional Transformation Coordination | VS-134 |
| W4089 | Digital Adoption Strategy & In-App Guidance (Digital Adoption Platform) | VS-134 |
| W4090 | Role-Based Learning, Training & Enablement for Change | VS-134 |
| W4092 | Behavioral Change & Process Compliance Sustainment | VS-134 |
| W4093 | Post-Implementation Reinforcement & Continuous Improvement Loop | VS-134 |
| W4094 | Employee Experience & Change Fatigue Monitoring | VS-134 |
| W4673 | Corporate Security Strategy, Charter & Risk-Appetite Framework | VS-159 |
| W4674 | Protective Intelligence & Threat Assessment Program | VS-159 |
| W4675 | Open-Source & Human Intelligence (OSINT/HUMINT) Monitoring & Alerting | VS-159 |
| W4676 | Corporate Security Operations Center (GSOC) — 24/7 Monitoring & Coordination | VS-159 |
| W4677 | Physical Security Architecture, Access Control & Guard-Force Standards (Enterprise) | VS-159 |
| W4678 | Executive & Principal Threat Profile, Risk Register & Quarterly Review | VS-159 |
| W4679 | Travel Risk Intelligence, Geopolitical & Kidnap/Extortion Monitoring | VS-159 |
| W4680 | Corporate Security Vendor, Guard-Agency & Investigator Management | VS-159 |
| W4681 | Executive Protection Program Design & Close-Protection Operations | VS-159 |
| W4682 | Principal (Board/Family/CEO) Travel Security & Advance Operations | VS-159 |
| W4683 | Executive Transport, Convoy & Route Security | VS-159 |
| W4684 | Corporate Event, AGM & High-Profile Appearance Security | VS-159 |
| W4685 | Residences, Estate & Perimeter Security for Principals | VS-159 |
| W4687 | Employee Travel Risk, Pre-Travel Briefing & Itinerary Tracking | VS-159 |
| W4688 | Employee Travel Risk, Lost-Contact & Medical-Evacuation Coordination (Duty of Care) | VS-159 |
| W4690 | Insider-Threat Detection, Background Re-Check & Offboarding Risk | VS-159 |
| W4691 | Workplace-Violence Threat Assessment, Intervention & De-escalation | VS-159 |
| W4694 | Security Incident Response, Crisis Management & Executive Notification | VS-159 |
| W4695 | Executive & Corporate Extortion, Defamation & Coordinated-Attack Response | VS-159 |

**Technology & Data** (22)

| ID | Workflow | Value Stream |
|---|---|---|
| W4145 | Product Information Model & Canonical Catalog Architecture | VS-137 |
| W4146 | Attribute Taxonomy, Spec Schema & Category Modeling | VS-137 |
| W4147 | Data Governance, Ownership & Completeness Standards | VS-137 |
| W4148 | New-Product Content Onboarding & Item Setup | VS-137 |
| W4149 | Content Authoring Workflow & Enrichment Roles | VS-137 |
| W4150 | Translation, Multilingual & Unit-of-Measure Localization | VS-137 |
| W4151 | Product Relationship, Cross-Sell & Kit/Bundle Content Modeling | VS-137 |
| W4152 | Vendor-Supplied Content Intake & Supplier Portal Governance | VS-137 |
| W4153 | Digital Asset Repository, Taxonomy & Metadata | VS-137 |
| W4154 | Product Image & Media Production Lifecycle | VS-137 |
| W4155 | Safety Data Sheet (SDS) & Regulatory Certificate Management | VS-137 |
| W4156 | How-To & Rich Content Authoring (Guides, Video, 360°) | VS-137 |
| W4157 | Asset Rights, Licensing & Brand-Approval Management | VS-137 |
| W4158 | Asset Versioning, Localization & Obsolescence | VS-137 |
| W4159 | Channel Content Publishing & Distribution Rules | VS-137 |
| W4160 | Content Quality Assurance & Rendering Validation | VS-137 |
| W4161 | Marketplace & Third-Party Channel Content Syndication | VS-137 |
| W4162 | Price, Promotion & Availability Content Sync | VS-137 |
| W4165 | Vendor & Internal Content SLA Reporting | VS-137 |
| W4166 | Catalog Data Quality, Duplicate & GSR Remediation | VS-137 |
| W4167 | Seasonal & Promotional Catalog Event Management | VS-137 |
| W4168 | PIM/DAM Platform, Integration & Lifecycle Governance | VS-137 |


#### Tier 3 (24)

**Sell & Serve** (15)

| ID | Workflow | Value Stream |
|---|---|---|
| W3840 | Sales Enablement Budget, Vendor/Partner Governance & Continuous Improvement | VS-124 |
| W3849 | Selling-Effectiveness KPI Framework & Associate/Store Performance Scorecard | VS-124 |
| W3850 | Basket, Conversion & Attach Analytics | VS-124 |
| W3851 | Clienteling & Customer-360 Effectiveness Analytics | VS-124 |
| W3852 | Trade-Pro Capture & B2B Selling Analytics | VS-124 |
| W3853 | Loyalty-Driven Selling & Member Behavior Analytics | VS-124 |
| W3854 | Sales-Enablement ROI & Program-Effectiveness Reporting | VS-124 |
| W3855 | Customer-Facing Tool / POS / Mobile Experience Optimization for Selling | VS-124 |
| W4235 | Pipeline Conversion, Win/Loss & Sales Analytics | VS-140 |
| W4236 | Route Efficiency, Coverage Adherence & Field Productivity | VS-140 |
| W4239 | Field Sales Force Cost, ROI & Workforce Planning | VS-140 |
| W4240 | Field Sales Continuous Improvement & Capability Building | VS-140 |
| W4582 | Refurbishment Cost, Yield & Unit-Economics Modeling | VS-155 |
| W4599 | Trade-In/Resale Analytics, Yield & Margin Intelligence | VS-155 |
| W4600 | Circular-Economy Impact, ESG Reporting & Program Review | VS-155 |

**Governance & Assurance** (7)

| ID | Workflow | Value Stream |
|---|---|---|
| W4000 | M&A Portfolio Performance, Value Realization & Lessons-Learned Analytics | VS-130 |
| W4043 | Political & Regulatory Risk Monitoring, Scenario & Exposure Analysis | VS-132 |
| W4047 | Political-Engagement Analytics, ROI & Performance Measurement | VS-132 |
| W4091 | User Adoption Measurement, System Usage & Adoption Analytics | VS-134 |
| W4095 | Change Benefit Realization & Adoption ROI Tracking | VS-134 |
| W4096 | OCM Maturity Assessment & Lessons Learned | VS-134 |
| W4696 | Corporate Security Metrics, Assurance & Post-Incident Review | VS-159 |

**Technology & Data** (2)

| ID | Workflow | Value Stream |
|---|---|---|
| W4163 | Product Content Performance & SEO Analytics | VS-137 |
| W4164 | Content-Driven Conversion, Attach & Basket Analytics | VS-137 |


**Promotion audit (10 → Tier 1):**
- **Governance & Assurance** (10): W3992, W4027, W4028, W4033, W4034, W4037, W4686, W4689, W4692, W4693

**Demotion audit (24 → Tier 3):**
- **Sell & Serve** (15): W3840, W3849, W3850, W3851, W3852, W3853, W3854, W3855, W4235, W4236, W4239, W4240, W4582, W4599, W4600
- **Governance & Assurance** (7): W4000, W4043, W4047, W4091, W4095, W4096, W4696
- **Technology & Data** (2): W4163, W4164

---

### Final Family-Decisive Classification Pass (120 workflows; VS-165/169/172/176/177)

> **Hand-reviewed 2026-06-20 (batch 7, final).** The last 5 family-decisive ≥92%-Tier-2 VSs:
> PCAB contractor licensing, uniform/workwear/PPE, third-party installer network, blueprint
> reprographics, field retail operations. **12 → Tier 1** (PCAB license annual-renewal/project-
> registration/audit-response/personnel-credentialing, DOLE PPE compliance, data-privacy for
> employee health/sizing data, PCAB installer verification, copyright/IP controls, document
> confidentiality, store exception-override authorization); **12 → Tier 3** (analytics/CI);
> **96 T2**. → 2,588 unclassified (48.5%). **All 53 family-decisive VSs now confirmed.**

#### Tier 1 (12)

**Governance & Assurance** (6)

| ID | Workflow | Value Stream |
|---|---|---|
| W4818 | PCAB License Application, Documentation Package & Registration Issuance (RA 4566) | VS-165 |
| W4820 | PCAB Annual License Renewal, Registration Compliance & Expiry Calendar | VS-165 |
| W4824 | License Lapse/Revocation Prevention, Condition Breach Reporting & Reinstatement | VS-165 |
| W4825 | PCAB Project Registration per Contract & Notice-of-Award Filing | VS-165 |
| W4833 | CIAP/PCAB & LGU Construction Inspection/Audit Response & Corrective Action | VS-165 |
| W4835 | Technical-Personnel Credentialing — PRC Engineer-of-Record, Responsible Officers & PCAB-Required Staff | VS-165 |

**People** (2)

| ID | Workflow | Value Stream |
|---|---|---|
| W4930 | PPE Compliance, Usage & DOLE-Compliance Audit | VS-169 |
| W4935 | Data Privacy & Employee Records (Sizing/Health Data, RA 10173) | VS-169 |

**Sell & Serve** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W4987 | Contractor Vetting, PCAB License (RA 4566) & Insurance Verification | VS-172 |
| W5087 | Copyright, IP & Sensitive-Document Handling Policy & Controls | VS-176 |
| W5100 | Customer Document Confidentiality, RA 10173 Data-Privacy & Secure Disposal | VS-176 |
| W5123 | Exception & Override Authorization Handling (Store→HQ Approval Workflow) | VS-177 |


#### Tier 2 (96)

**Governance & Assurance** (16)

| ID | Workflow | Value Stream |
|---|---|---|
| W4817 | PCAB Licensing Strategy, Entity Eligibility & Contractor-Category Decision | VS-165 |
| W4819 | License Category, Classification & Size/Capacity Upgrade Management | VS-165 |
| W4821 | CIAP/PCAB Board Engagement, Petitions & Regulatory Liaison | VS-165 |
| W4822 | Multi-Entity License Coverage, Affiliate & Entity-Level Licensing Decisions | VS-165 |
| W4823 | PCAB License Compliance Recordkeeping, Evidence Repository & Audit Trail | VS-165 |
| W4826 | Performance & Surety Bonding for PCAB-Licensed Project Work | VS-165 |
| W4827 | Construction Safety & Health Program (COSP) & DOLE D.O. 13-98 Compliance for Licensed Work | VS-165 |
| W4828 | Bidding/Bid-Support License Proof, Capacity Pre-Check & PhilGEPS Eligibility Sync | VS-165 |
| W4829 | Subcontractor License Verification, Approved-Subcontractor List & Cascading Compliance | VS-165 |
| W4830 | Project Warranty Period, Acceptance Certificate & Retention/Maintenance Obligations | VS-165 |
| W4831 | Construction Payment Security — Mechanic's-Lien Rights, Lien Waivers & Payment-Bond Claims | VS-165 |
| W4832 | Government/Institutional Project Closeout, Audited Records & Statutory Turnover | VS-165 |
| W4834 | License-Condition Compliance Monitoring (Insurance, Technical Capacity, CPD, Personnel) | VS-165 |
| W4836 | Unlicensed-Contracting Risk Control — In-Scope/Out-of-Scope Boundary & Material-Supply-vs-Install Decision | VS-165 |
| W4837 | Joint Ventures, Consortiums & Foreign Contractor Licensing | VS-165 |
| W4838 | Penalty/Violation Management, Administrative Proceedings & Reinstatement | VS-165 |

**People** (20)

| ID | Workflow | Value Stream |
|---|---|---|
| W4913 | Uniform, Workwear & PPE Program Strategy & Operating Model | VS-169 |
| W4914 | Role-Based Uniform / Workwear Standards & Brand-Guideline Design | VS-169 |
| W4915 | PPE Standards, Role Hazard Assessment & Issuance Matrix | VS-169 |
| W4916 | Uniform Allowance, Replenishment Cycle & Policy Framework | VS-169 |
| W4917 | Uniform / Workwear / PPE Vendor Selection & Contracting | VS-169 |
| W4918 | Sizing, Fit & Body-Measurement Program | VS-169 |
| W4919 | Branded Apparel Design, Procurement & Quality | VS-169 |
| W4920 | Multi-Entity Program Governance & Cross-Company Standards | VS-169 |
| W4921 | New-Hire Uniform / Workwear Issuance & Onboarding Kit | VS-169 |
| W4922 | Role-Based PPE Issuance, Fit-Testing & Training | VS-169 |
| W4923 | Contingent / Outsourced & Vendor-Personnel Uniform & PPE Provision | VS-169 |
| W4924 | Uniform / Workwear Laundering Service — In-House vs Vendor (Industrial Laundry) | VS-169 |
| W4925 | PPE Inspection, Maintenance, Replacement & End-of-Life | VS-169 |
| W4926 | Uniform Damage, Loss & Replacement Processing | VS-169 |
| W4927 | Promotion / Transfer / Role-Change Uniform Re-Issuance | VS-169 |
| W4928 | Separation / End-of-Employment Uniform Return & Recovery | VS-169 |
| W4931 | Uniform Quality, Vendor SLA & Performance Governance | VS-169 |
| W4932 | Uniform / PPE Inventory, Stock-Level & Distribution Management | VS-169 |
| W4933 | Employee Satisfaction, Fit & Comfort Feedback | VS-169 |
| W4934 | Sustainability — Textile Recycling, Eco-Uniform & Circularity | VS-169 |

**Sell & Serve** (60)

| ID | Workflow | Value Stream |
|---|---|---|
| W4985 | Installer & Contractor Network Strategy, Trade-Coverage & Capacity Design | VS-172 |
| W4986 | Contractor Recruitment, Pipeline & Trade-Segment Sourcing | VS-172 |
| W4988 | Contractor Background, Reference & Quality-Capability Due Diligence | VS-172 |
| W4989 | Installer Network Onboarding, Agreement & Tier Classification | VS-172 |
| W4990 | Pro-Referral Marketplace Platform, Profile & Catalog Management | VS-172 |
| W4991 | Trade-Coverage Gap Analysis, Geographic Expansion & Recruitment Targeting | VS-172 |
| W4992 | Network Governance, Code-of-Conduct & Installer Relationship Management | VS-172 |
| W4993 | Customer "Find-a-Pro" Request Intake, Qualification & Consent | VS-172 |
| W4994 | Installer Matchmaking, Routing & Lead Distribution | VS-172 |
| W4995 | Lead Handoff, Customer-Installer Communication & Quote Management | VS-172 |
| W4996 | Project Booking, Scope Confirmation & Materials-Link Sales Attach | VS-172 |
| W4997 | Referral Fee, Commission & Settlement Management | VS-172 |
| W4998 | Project Execution Tracking, Milestone & Completion Verification | VS-172 |
| W4999 | Installer Capacity, Calendar & Workload Balancing | VS-172 |
| W5000 | Lost/Declined Lead Recovery, Alternate Referral & Demand Capture | VS-172 |
| W5001 | Customer Rating, Review & Feedback Collection | VS-172 |
| W5003 | Quality Assurance, Workmanship Inspection & Site Audit | VS-172 |
| W5004 | Warranty, Defect Liability & Post-Installation Service Obligation | VS-172 |
| W5005 | Dispute Resolution, Complaint Handling & Installer Discipline/Removal | VS-172 |
| W5006 | License, Insurance & Compliance Continuous Monitoring | VS-172 |
| W5008 | Installer Network Risk, TPRM & Data Privacy Assurance | VS-172 |
| W5081 | Reprographics Service Strategy, Catalog & Business-Model Design | VS-176 |
| W5082 | Large-Format Printer/Plotter/Scanner Equipment Selection, Procurement & Setup | VS-176 |
| W5083 | Reprographics Pricing, Cost-per-SQM & Service Tariff Strategy | VS-176 |
| W5084 | Print Media, Toner/Ink & Consumables Procurement & Inventory Management | VS-176 |
| W5085 | Reprographics Service Counter, Layout & Self-Service Workstation Setup | VS-176 |
| W5086 | Cloud/Mobile Print-Submission Portal & File-Format Standardization | VS-176 |
| W5088 | Equipment Maintenance, Vendor Service Contract & Calibration Management | VS-176 |
| W5089 | Customer Print-Job Intake, File Check, Quotation & Order Confirmation | VS-176 |
| W5090 | Large-Format Plan Printing, Plotting & Print-Quality Control | VS-176 |
| W5091 | Document Scanning, Archiving & Large-Format Digitization Service | VS-176 |
| W5092 | Plan Copying, Binding, Folding & Reproduction Service | VS-176 |
| W5093 | Customer File Storage, Reprint-on-Demand & Version Control Service | VS-176 |
| W5094 | Customer Job Notification, Pickup, Delivery & Will-Call Management | VS-176 |
| W5095 | Bulk/Tender Bid-Set, Project Plan-Room & Multi-Set Reproduction Service | VS-176 |
| W5096 | Customer Job Billing, Prepaid Account & Credit-Term Management | VS-176 |
| W5097 | Print Quality, Color/Scale Accuracy & Dimensional Verification | VS-176 |
| W5101 | Software License, Cloud Subscription & Print-Management System Administration | VS-176 |
| W5102 | Reprographics Customer Satisfaction, Complaint & Rework Management | VS-176 |
| W5103 | Service Demand Seasonality, Capacity Forecasting & Staffing | VS-176 |
| W5105 | Field Retail Operations Strategy, Charter & Operating-Model Design | VS-177 |
| W5106 | Regional/District Territory Design, Alignment & Store-Group Assignment | VS-177 |
| W5107 | Field Organization Staffing, Span-of-Control & Regional-Manager Workforce Planning | VS-177 |
| W5108 | Regional/District Manager Onboarding, Certification & Capability Building | VS-177 |
| W5109 | Multi-Store P&L Governance, Store Grading & Performance Tiering | VS-177 |
| W5110 | New-Store Stabilization, Maturity Ramp & Field Handover Support | VS-177 |
| W5111 | Underperforming/Distressed-Store Diagnosis & Turnaround Program | VS-177 |
| W5112 | Field Compensation, Incentive & Multi-Store Performance Recognition | VS-177 |
| W5113 | Regional/District Store-Visit Cadence, Routing & Itinerary Planning | VS-177 |
| W5114 | Store-Visit Execution, Retail-Standards Audit & Compliance Scoring | VS-177 |
| W5115 | Store-Manager Coaching, Development & Performance Conversations | VS-177 |
| W5116 | Retail-Execution Field Audit (Planogram/Price/Signage/Merchandising Standards) | VS-177 |
| W5117 | Competitor & Market Field Intelligence Collection | VS-177 |
| W5118 | Field Action-Item Tracking, Follow-Up & CAP Closure | VS-177 |
| W5119 | Field Communication, Regional Meetings & Best-Practice Sharing | VS-177 |
| W5121 | Store Operations Support Center (Store Hotline) Setup, Staffing & Operating Model | VS-177 |
| W5122 | Store Issue Intake, Triage, Resolution & Escalation Management | VS-177 |
| W5124 | Store Grievance, Concern & Feedback Resolution Channel | VS-177 |
| W5125 | Cross-Functional Store-Issue Coordination (Merch/IT/HR/Facilities/LP) | VS-177 |
| W5126 | Store Knowledge Base, SOP Support & Field Self-Service Enablement | VS-177 |


#### Tier 3 (12)

**Governance & Assurance** (2)

| ID | Workflow | Value Stream |
|---|---|---|
| W4839 | Contractor Compliance Analytics — Bid Win-Rate, Project Margin, Penalty/Reputation, License Economics | VS-165 |
| W4840 | PCAB Compliance Governance, Board Reporting & Program Continuous Improvement | VS-165 |

**People** (2)

| ID | Workflow | Value Stream |
|---|---|---|
| W4929 | Uniform / PPE Program Cost, Spend & TCO Analytics | VS-169 |
| W4936 | Program Maturity, Benchmarking & Continuous Improvement | VS-169 |

**Sell & Serve** (8)

| ID | Workflow | Value Stream |
|---|---|---|
| W5002 | Installer Performance Scorecard & KPI Management | VS-172 |
| W5007 | Network Health, Revenue Impact & Program Analytics | VS-172 |
| W5098 | Reprographics Equipment Performance, Utilization & Downtime Management | VS-176 |
| W5099 | Consumables Yield, Print-Cost Accounting & Margin Analytics | VS-176 |
| W5104 | Reprographics Program Performance, ROI & Cross-Sell Analytics | VS-176 |
| W5120 | Field Coaching Quality, Visit Effectiveness & Standards-Compliance Analytics | VS-177 |
| W5127 | Field & Store Operations Performance Dashboard & Comp-Store Analytics | VS-177 |
| W5128 | Field Retail Operations Continuous Improvement, Benchmarking & Program Review | VS-177 |


**Promotion audit (12 → Tier 1):**
- **Governance & Assurance** (6): W4818, W4820, W4824, W4825, W4833, W4835
- **People** (2): W4930, W4935
- **Sell & Serve** (4): W4987, W5087, W5100, W5123

**Demotion audit (12 → Tier 3):**
- **Governance & Assurance** (2): W4839, W4840
- **People** (2): W4929, W4936
- **Sell & Serve** (8): W5002, W5007, W5098, W5099, W5104, W5120, W5127, W5128

### Pass 26–29 Confirmation Classification Pass (336 workflows; VS-178–VS-191)

The 336 workflows added across gap-analysis Passes 26–29 (VS-178–VS-191; W5129–W5464) were promoted from the keyword proposal into the confirmed register after genuine tier review calibrated to the register's existing rules (statutory/regulatory execution → Tier 1; analytics/scorecard/optimization/strategy → Tier 3; standard operational support → Tier 2). Rows are tabulated by tier and family in the **Additions** family subsections above (this batch is the first to use the family-grouped Additions layout exclusively, so no per-batch row tables are duplicated here). **117 → Tier 1** (statutory/regulatory execution the keyword rules missed: DAR/NCIP/FPIC land clearances and DENR ECC in VS-178; NSWMC EPR registration/audit/filing under RA 11898 in VS-179; DTI price-compliance reporting and State-of-Calamity LGU permits in VS-180; TESDA monthly compliance report and BIR DTS tax-savings certificate in VS-183; BFP/LGU structural and temporary-selling-permit clearances in VS-184; CDA verification and patronage-dividend tax certification in VS-185; DOLE-OSH equipment certification in VS-186; DENR-EMB RA 6969 generator/TSD permitting and annual hazardous-waste report in VS-187; BSP/SEC/Truth-in-Lending RA 3765 disclosure and compliance-examination support in VS-188/189). **24 → Tier 3** (analytics/scorecard/dashboards the keyword default sent to Tier 2: program-impact/diversion-rate/yield/profitability analytics and board dashboards across VS-179/181/182/183/185/186/187/188/189/190/191). **195 confirmed Tier 2** (the operational-support majority). Confirmed 2,440→2,776 rows (2,417→2,753 unique; T1 684→801, T2 1,354→1,549, T3 402→426); unclassified 2,900→2,564 (51.8%); proposed 507/1,912/145. **All 103 gap-analysis value streams (VS-89–VS-191) now confirmed.** `validate-repo.sh`: 0 errors / 1 warning.

### Full-Coverage Confirmation Pass (every remaining unclassified workflow; 2,596 → 0)

> **Confirmed 2026-06-28** via [`07-methodology/confirm-all-workflows.py`](../../07-methodology/confirm-all-workflows.py),
> closing the unclassified backlog entirely. Each workflow's keyword-proposed tier was adopted
> unless a calibrated rule overrode it — the same calibration documented by batches v7.19–v7.27
> (statutory/regulatory execution → Tier 1; analytics/scorecard/optimization → Tier 3; standard
> operational support → Tier 2). **65 promoted to Tier 1** (statutory/regulatory execution the keyword rules defaulted to Tier 2), **179 promoted to Tier 3** (analytics/optimization the keyword default sent to Tier 2), **3 demoted from proposed Tier 1 to Tier 2** (program support: training/awareness/strategy design), and the remaining **2349 adopted at their proposed tier** (the documented safe default).
> Confirmation arithmetic: register 2,776 → 5,372 rows (2,753 → 5,349 unique `##` workflows); T1 801 → 1375, T2 1,549 → 3243, T3 426 → 754; unclassified 2,596 → 0. The proposed register now stands at zero rows.

#### Tier 1 (574)

**Plan & Source** (51)

| ID | Workflow | Value Stream |
|---|---|---|
| W1187 | Post-Disaster Construction Material Demand Surge Fulfillment & Emergency Replenishment | VS-2 |
| W1230 | Vendor Consignment Inventory Monthly Settlement, Revenue Share & Reconciliation | VS-3 |
| W1233 | Philippine Bureau of Customs Import Entry Processing & Duty Assessment Automation | VS-2 |
| W1236 | Vendor Promotional Funding, Co-Op Advertising & Markdown Reconciliation | VS-3 |
| W1264 | Import Container Consolidation, Multi-Vendor FCL Assembly & Space Optimization | VS-2 |
| W1345 | Product Barcode & Label Accuracy Verification, GS1 Compliance & Print Quality Audit | VS-1 |
| W1347 | Product Recall Communication, Customer Notification & Affected Inventory Quarantine | VS-1 |
| W1411 | Import PO Customs Documentation Package Preparation, Broker Coordination & Compliance Checklist | VS-3 |
| W1432 | Store-Level Typhoon Season Advance Inventory Pre-Positioning, Protective Stocking & Post-Storm Rapid Replenishment | VS-2 |
| W1435 | Import Container Consolidation Optimization, Carrier Space Allocation & Port Congestion Mitigation | VS-2 |
| W1495 | Vendor-Managed Inventory (VMI) Replenishment, Min/Max Review & Automated PO Generation | VS-3 |
| W1533 | S&OP Monthly Consensus Demand Review, Cross-Functional Alignment & Supply Plan Ratification | VS-2 |
| W1546 | Vendor Factory Social Compliance Audit Scheduling, Scoring & Corrective Action Tracking | VS-3 |
| W1547 | Product Regulatory Compliance Certification Management (DTI-BPS, FPA, DENR) & Renewal Tracking | VS-1 |
| W1834 | Private Label Purchase Order & Import Logistics Management | VS-41 |
| W1839 | Private Label Customer Quality Complaint Investigation & Corrective Action | VS-41 |
| W1841 | Private Label Product Recall & Safety Notification | VS-41 |
| W1844 | Private Label Incoming Quality Trend Analysis & Factory Scorecard Integration | VS-41 |
| W1926 | Consignment Goods Receipt & Non-Valuated Inventory Posting | VS-45 |
| W1928 | Consignment Sell-Through at POS & Ownership Transfer | VS-45 |
| W1930 | Consignment Physical Inventory & Vendor Reconciliation | VS-45 |
| W1933 | Consignment Stock Transfer Between Locations | VS-45 |
| W1936 | VMI Automated Replenishment & ASN Processing | VS-45 |
| W1937 | VMI Goods Receipt & Auto-Confirmation | VS-45 |
| W1942 | Consignment Sell-Through Settlement & Vendor Payment | VS-45 |
| W1948 | Consignment & VMI Intercompany Settlement (Multi-Entity) | VS-45 |
| W2455 | Automated Vendor Data Collection | VS-67 |
| W3124 | Cooperative Inbound Logistics, Consolidation & Last-Mile Pickup | VS-94 |
| W3125 | Cooperative Goods Receipt, Quality Inspection & Acceptance | VS-94 |
| W3126 | Cooperative Invoice, Livelihood Settlement & Direct-to-Account Pay | VS-94 |
| W3792 | Trade Compliance & Sourcing Linkage (Tariff, Country, Sanctions) | VS-122 |
| W3795 | Import Vendor Onboarding, Qualification & Master Governance | VS-122 |
| W3800 | Overseas-Office & Agent Risk, Anti-Bribery & Conflict-of-Interest Governance | VS-122 |
| W3801 | Import Order Consolidation, Container Planning & Consolidated Buying | VS-122 |
| W3802 | Multi-Vendor / Multi-Category Container & LCL Consolidation Operations | VS-122 |
| W3905 | S&OP/IBP Strategy, Operating Rhythm & Governance | VS-127 |
| W3914 | Inventory & Replenishment Plan Reconciliation | VS-127 |
| W3916 | Pre-S&OP Reconciliation & Issue Escalation | VS-127 |
| W3919 | Executive S&OP Review & Decision Meeting | VS-127 |
| W3920 | S&OP Plan Publication & Cross-Function Alignment | VS-127 |
| W3921 | Financial Reconciliation to Plan (Revenue/Margin/Inventory Budget) | VS-127 |
| W3925 | S&OP KPIs, Scorecard & Performance Reporting | VS-127 |
| W3926 | S&OP Plan-vs-Actual Variance & Root-Cause Review | VS-127 |
| W3927 | S&OP Data, Tooling & Model Maintenance | VS-127 |
| W3928 | S&OP Maturity Assessment & Continuous Improvement | VS-127 |
| W4012 | Non-Conformance, Corrective Action & Remediation Management | VS-131 |
| W4016 | Living Wage, Working Hours & Wage-Data Assurance Program | VS-131 |
| W4020 | Modern Slavery / Human Rights Statutory & Voluntary Reporting | VS-131 |
| W5494 | New-Store-Opening Demand Induction and Initial-Stock S&OP | VS-127 |
| W5495 | Vendor-Managed Inventory (VMI) and Consignment S&OP Integration | VS-127 |
| W5496 | Government-Mandated Price Events and Calamity Price-Freeze S&OP Response | VS-127 |

**Make & Move** (81)

| ID | Workflow | Value Stream |
|---|---|---|
| W1169 | Import Container Inbound Logistics, Port Drayage & DC Delivery | VS-6 |
| W1188 | Consignment Inventory Monthly Reconciliation & Vendor Settlement Processing | VS-5 |
| W1190 | Inter-Island DC-to-Store RoRo & Ferry Consolidated Shipment Planning | VS-6 |
| W1208 | Customer Home Delivery White-Glove Service & Installation Add-On Dispatch | VS-6 |
| W1216 | Vendor-Managed Inventory (VMI) Replenishment Monitoring & Exception Management | VS-5 |
| W1228 | DC Multi-Stop Route Optimization & Dynamic Load Consolidation for Store Delivery | VS-6 |
| W1237 | DC Value-Added Kit Assembly, Bundle Preparation & Pre-Pack Operations | VS-4 |
| W1255 | Inter-Island Consolidated Shipping, Vessel Booking & RoRo Space Optimization | VS-6 |
| W1256 | Returnable Transport Packaging (RTP) Pool Management, Tracking & Reconciliation | VS-6 |
| W1271 | DC Inbound Import Container Devanning, Staging & Quality Sampling | VS-4 |
| W1275 | Store-Level Daily Consignment Inventory Sales Reconciliation & Vendor Reporting | VS-5 |
| W1279 | DC Cross-Dock Fast-Mover Processing & Direct Putaway to Outbound | VS-4 |
| W1298 | Consignment Inventory Reconciliation, Settlement & Ownership Transfer Processing | VS-5 |
| W1307 | DC Cross-Dock Fast-Mover Expedited Receiving, Sortation & Same-Day Dispatch Processing | VS-4 |
| W1352 | DC Outbound Pick Accuracy Verification, Short-Ship Prevention & Error Reporting | VS-4 |
| W1353 | DC Outbound Staging, Loading Bay Scheduling & Dock Door Assignment Management | VS-4 |
| W1365 | DC Inbound Vendor ASN Pre-Receipt Verification & PO Matching Exception Management | VS-4 |
| W1368 | DC Store Replenishment Wave Planning, Release & Prioritization Management | VS-4 |
| W1369 | DC Outbound Multi-Stop Route Optimization & Philippine Road Constraint Management | VS-4 |
| W1370 | DC Outbound Shipment Tracking, Store Delivery Confirmation & POD Reconciliation | VS-4 |
| W1372 | Customer Delivery Damage, Loss & Shortage Claim Processing & Carrier Liability Settlement | VS-6 |
| W1373 | 3PL Carrier Driver Accreditation, Vehicle Inspection & Compliance Management | VS-6 |
| W1400 | Driver License Expiration Monitoring, LTO Compliance & Renewal Tracking | VS-6 |
| W1401 | Fleet Vehicle Annual LTO Registration Renewal & Motor Vehicle Inspection Compliance | VS-6 |
| W1402 | DC Seasonal Merchandise Pre-Staging, Forward-Pick Slot Reallocation & Promotional Lane Setup | VS-4 |
| W1413 | DC-Level Cycle Count Discrepancy Root Cause Analysis, Corrective Action & Recount Protocol | VS-5 |
| W1423 | DC-to-DC Inter-DC Inventory Rebalancing Transfer Execution & In-Transit Monitoring | VS-5 |
| W1433 | Store-Level Daily Catch-Weight Item Inventory Valuation, WAC Calculation & Shrinkage Reconciliation | VS-5 |
| W1514 | Inter-Island Emergency Cargo Air Freight & Charter Coordination for Critical Stock Replenishment | VS-6 |
| W1534 | DC Night Shift Operations, Security Protocol & Shift Handover Management | VS-4 |
| W1535 | Emergency Inter-DC Stock Transfer for Critical Out-of-Stock Prevention | VS-5 |
| W1536 | Fleet Vehicle Registration Renewal, LTO Compliance & LTFRB Cargo Freight License Management | VS-6 |
| W1625 | Customer Return Without Receipt Processing | VS-32 |
| W1627 | Customer Return Credit Issuance & Refund Processing | VS-32 |
| W1631 | Vendor Return-to-Vendor (RTV) Shipment Planning & Consolidation | VS-32 |
| W1632 | Vendor RTV Credit Recovery & Reconciliation | VS-32 |
| W1634 | Vendor Product Recall Return & Recovery Processing | VS-32 |
| W1636 | Vendor Consignment Unsold Inventory Return & Settlement | VS-32 |
| W1638 | Store-to-DC Reverse Logistics Consolidation Program, In-Transit Tracking & DC Hand-Off | VS-32 |
| W2200 | Customer Home Delivery SLA Management | VS-56 |
| W2201 | Delivery Quality Inspection | VS-56 |
| W2206 | Monthly 3PL Invoice Processing | VS-56 |
| W2801 | Store Cash Office End-of-Day Skim, Denomination & Bundle Preparation | VS-81 |
| W2807 | Cash Office Security, Dual-Control & CCTV Correlation | VS-81 |
| W2809 | Armored Car Partner Onboarding, Vetting & Contract Management | VS-81 |
| W2812 | DC/Regional Vault Operations, Counting & Reconciliation | VS-81 |
| W2813 | Bank Deposit Posting, Clearance & Difference Resolution | VS-81 |
| W2814 | CIT Service Disruption, Robbery & Emergency Response | VS-81 |
| W2818 | Cash Holding Limit Compliance & Store Vault Capacity Planning | VS-81 |
| W2822 | CIT Regulatory Compliance (PNP SOSIA/BSP) & Reporting | VS-81 |
| W3022 | Damaged Inventory Quarantine, Write-Off & GL Posting | VS-90 |
| W3027 | Import Container Damage, Short-Landing & Surveyor Coordination | VS-90 |
| W3029 | Claim Negotiation, Settlement & Credit/Refund Resolution | VS-90 |
| W3036 | Damage Claim Refund, Credit Note & Financial Reconciliation | VS-90 |
| W3077 | Kit Inventory Reconciliation, Variance & Shrinkage Control | VS-92 |
| W3081 | Bundle Promotion Execution, Price Override & POS Application | VS-92 |
| W3096 | Dark Store Closure, Migration & Decommissioning | VS-93 |
| W3099 | Pack Station Operations, Quality Check & Right-Box Selection | VS-93 |
| W3100 | Pack-Station Consumables, Labeling & Manifest Management | VS-93 |
| W3101 | Dispatch Scheduling, Carrier Handoff & Route Consolidation | VS-93 |
| W3103 | BOPIS / Click-and-Collect Stage & Customer Handover | VS-93 |
| W3104 | Dark Store Returns, Reverse Putaway & Exception Handling | VS-93 |
| W3105 | Dark Store Inventory Positioning, Safety Stock & Replenishment | VS-93 |
| W3109 | Dark Store Pick/Pack Accuracy, Damages & Cost-per-Order | VS-93 |
| W3505 | Outbound DC-to-Store Freight Planning & Load Tendering | VS-110 |
| W3507 | Multi-Stop Route Optimization & Load Consolidation | VS-110 |
| W3515 | Landed Cost & Freight Cost Component Capture | VS-110 |
| W3520 | Freight Risk, Insurance & Business Continuity | VS-110 |
| W3531 | RTI (Totes / Cages / Containers) Tracking & Reconciliation | VS-111 |
| W3536 | Pallet / RTI Pool Reconciliation & Pool-Provider Settlement | VS-111 |
| W3539 | Packaging Compliance Audit & DENR / EPR Reporting | VS-111 |
| W4126 | Outbound Distribution Flow & Lane / Routing Architecture | VS-136 |
| W4140 | Network Cost-to-Serve & Total Landed Cost Analytics | VS-136 |
| W4297 | Daily Delivery Manifest, Load Planning & Dispatch | VS-143 |
| W4298 | In-Home Delivery Execution, Site Protection & Handoff | VS-143 |
| W4304 | Field Service Safety, DOLE OSH, Heavy-Lifting & Customer-Premises Liability | VS-143 |
| W4306 | Refrigerant Recovery, ODS/RA 8749 & DENR-Compliant Appliance Handling | VS-143 |
| W4308 | Haul-Away Reverse Logistics, Consolidation & Vendor Scrap Partner | VS-143 |
| W5477 | Range-Aware Route Dispatch, Payload Optimization & Charging-Stop Planning | VS-192 |
| W5482 | DOE / LTO / LTFRB Green-Fleet Compliance, EV Inspection & Franchise Reporting | VS-192 |
| W5483 | EV & Alt-Fuel Fleet Safety — High-Voltage, Battery Fire & DOLE-OSH Program | VS-192 |

**Sell & Serve** (123)

| ID | Workflow | Value Stream |
|---|---|---|
| W1170 | Subcontractor Installation Daily Dispatch, Work Order & Capacity Management | VS-12 |
| W1180 | Government Procurement (PhilGEPS) Bidding, Accreditation & Public Sector Account Management | VS-11 |
| W1196 | Ship-from-Store Fulfillment Operations & Store-Level Inventory Reservation | VS-10 |
| W1268 | E-Wallet (GCash/Maya) Daily Settlement & Reconciliation | VS-8 |
| W1276 | POS Multi-Tender Split Payment Processing & Reconciliation | VS-8 |
| W1282 | Paint Mixing Station Daily Setup, Color Formula Management & Consumables Replenishment | VS-7 |
| W1288 | Customer B2B Project Progress Billing & Milestone Payment Collection | VS-11 |
| W1301 | E-Wallet (GCash/Maya) Settlement Reconciliation & Discrepancy Resolution | VS-8 |
| W1305 | Catch-Weight & Variable-Quantity Item POS Pricing Verification & Scale Calibration Compliance | VS-8 |
| W1354 | Store Daily Cash Deposit Preparation, Armored Car Pickup & Bank Credit Reconciliation | VS-8 |
| W1359 | Ecommerce Promotional Price Sync, Markdown Conflict Resolution & POS Price Parity Verification | VS-10 |
| W1374 | Tool Rental Equipment Breakdown, Emergency Repair Dispatch & Substitute Unit Provisioning | VS-12 |
| W1412 | Store-Level Receiving Dock Safety Inspection, Material Handling Compliance & Incident Reporting | VS-7 |
| W1419 | Store-Level Daily Sales Flash Report Generation & HQ Consolidation Dashboard Update | VS-7 |
| W1425 | Multi-Tender POS Transaction Daily Reconciliation, Settlement Matching & Variance Resolution | VS-8 |
| W1426 | Trade Account Project Progress Billing, Milestone Payment Collection & Retention Warranty Release | VS-11 |
| W1429 | E-Commerce BOPIS Same-Day Pick SLA Monitoring, Exception Escalation & Customer Notification | VS-10 |
| W1434 | Loyalty Program Partner Quarterly Rebate Settlement, Tier Benefit Cost Allocation & ROI Analysis | VS-13 |
| W1442 | BOPIS Customer No-Show Rate Monitoring, Auto-Cancel Processing & Restocking Workflow | VS-10 |
| W1467 | Store Petty Cash Replenishment, Expense Tracking, Float Audit & Custody Management | VS-8 |
| W1468 | Multi-Entity Cash Concentration, Zero-Balance Sweeping & Intercompany Settlement Automation | VS-8 |
| W1471 | Trade Account Consolidated Monthly Billing, Multi-Store Purchase Aggregation & Payment Processing | VS-11 |
| W1485 | Store Paint Mixing Station Daily Calibration, Color Formula Database Update & Tint Inventory Replenishment | VS-7 |
| W1494 | POS Customer Project Receipt, Multi-Store Purchase Aggregation & Tax Credit Certificate Processing | VS-8 |
| W1506 | Customer Non-Stock / Special Order Full Lifecycle Management | VS-7 |
| W1516 | Philippine BIR Electronic Invoicing System (EIS) Sales Data Transmission & Compliance | VS-8 |
| W1538 | POS Multi-Tender Partial Refund Processing, Change Allocation & Tender Reversal Management | VS-8 |
| W1539 | Installation Service Post-Completion Quality Inspection, Customer Sign-Off & Punch List Resolution | VS-12 |
| W1562 | Crisis Communications & Media Response Protocol for Product Recall, Safety Incident & Public Relations Event | VS-14 |
| W1739 | Initial Inventory Planning & Allocation | VS-37 |
| W1762 | Lessons Learned & Store Opening Process Improvement | VS-37 |
| W1912 | Competitive New Store Opening & Expansion Monitoring | VS-44 |
| W1954 | BIR Tax Clearance & Government Supplier Compliance Maintenance | VS-46 |
| W1961 | Government Contract Award & Purchase Order Processing | VS-46 |
| W1963 | Government Multi-Year Contract & Blanket Purchase Order Management | VS-46 |
| W1966 | Government Invoice Submission & BIR-Compliant Billing | VS-46 |
| W1967 | Government Account Collection & Payment Follow-Up | VS-46 |
| W1968 | Government EWT Certificate (BIR 2307) Collection & Reconciliation | VS-46 |
| W1970 | Institutional Account Billing & Collection | VS-46 |
| W1971 | Government Account Revenue Recognition (PFRS 15) | VS-46 |
| W1976 | Subscription SKU & Service Item Master Setup | VS-47 |
| W1977 | Subscription Enrollment Flow Design (POS & Online) | VS-47 |
| W1984 | Subscription Cancellation & Pro-Rata Refund Processing | VS-47 |
| W1986 | Subscription Payment Failure & Dunning Management | VS-47 |
| W1990 | Service Visit Scheduling & Dispatch Management | VS-47 |
| W1993 | Service Quality Inspection & Partner Scoring | VS-47 |
| W2015 | Retail Media Vendor Collection & AR Management | VS-48 |
| W2020 | Retail Media Intercompany Revenue Allocation (Multi-Entity) | VS-48 |
| W2118 | POS Warranty Capture at Checkout | VS-53 |
| W2131 | Warranty Refund Processing | VS-53 |
| W2135 | Extended Warranty POS Upsell | VS-53 |
| W2288 | Ship-from-Store Order Processing | VS-60 |
| W2289 | Vendor Drop-Ship Order Processing | VS-60 |
| W2291 | Order Routing Exception Management | VS-60 |
| W2293 | Order Routing Cost Optimization | VS-60 |
| W2295 | Consolidated Delivery Management | VS-60 |
| W2300 | Fulfillment Quality Control | VS-60 |
| W2304 | Order Routing Algorithm Optimization | VS-60 |
| W2337 | Sample Inventory Tracking & Replenishment | VS-62 |
| W2656 | Self-Checkout Pilot & Operations | VS-75 |
| W2658 | Digital Receipt & Transaction History Management | VS-75 |
| W2665 | App Conversion Rate Optimization & Checkout Analytics | VS-75 |
| W2698 | Multi-Project Material Demand Consolidation | VS-77 |
| W2703 | On-Site Material Verification & Receipt | VS-77 |
| W2709 | Project Completion Material Reconciliation & Close-Out | VS-77 |
| W2825 | Sari-Sari Store & MSME Prospecting, Onboarding & KYC | VS-82 |
| W2835 | Micro-Wholesale Pick, Pack & Aggregated Basket Build | VS-82 |
| W2837 | MSME Cash-on-Delivery, E-Wallet & Micro-Receipt Settlement | VS-82 |
| W2838 | MSME Returns, Damages & Empty Container/Packaging Recovery | VS-82 |
| W3139 | Seller Onboarding, Contracting & KYB | VS-95 |
| W3149 | Multi-Seller Basket Split, Consolidation & Customer Experience | VS-95 |
| W3157 | Marketplace Tax (VAT / Percentage Tax) & BIR Compliance per Seller | VS-95 |
| W4351 | Live-Goods POS, Catch-Handling & Carry/Load Assistance | VS-145 |
| W4355 | Live-Goods Waste, Composting & DENR/Composting Compliance | VS-145 |
| W4356 | Pesticide/Chemical Handling, PPE & FPA/DENR Compliance | VS-145 |
| W4358 | Live-Goods Inventory Accuracy, Cycle Count & Reconciliation | VS-145 |
| W4433 | Self-Checkout & Unattended Retail Strategy, Scope & Operating Model | VS-149 |
| W4442 | Customer SCO Transaction Processing & Assistance | VS-149 |
| W4444 | Scan-&-Go Mobile App Session & Checkout Reconciliation | VS-149 |
| W4452 | SCO Cash Reconciliation, Variance & Investigation | VS-149 |
| W4453 | SCO Compliance — BIR CAS, e-Invoicing, Price/Tag (RA 7394) | VS-149 |
| W4454 | SCO Accessibility (PWD/Senior) & Inclusive Design | VS-149 |
| W4605 | BSP Agent Accreditation, Licensing & Compliance Setup | VS-156 |
| W4609 | Bills-Payment Counter Transaction Processing | VS-156 |
| W4610 | Domestic Remittance Send/Receive Transaction Processing | VS-156 |
| W4611 | E-Money Cash-In/Cash-Out Transaction Processing | VS-156 |
| W4612 | Mobile Load/Top-Up Transaction Processing | VS-156 |
| W4613 | VAS Cash Handling, Custody & End-of-Day Reconciliation | VS-156 |
| W4614 | VAS Customer Identity (KYC) & Transaction Verification | VS-156 |
| W4617 | Principal Settlement, Float & Commission Management | VS-156 |
| W4618 | VAS General Ledger, Revenue Recognition & Intercompany | VS-156 |
| W4619 | AML/KYC Monitoring, Suspicious-Transaction Reporting & Sanctions | VS-156 |
| W4620 | BSP & Regulatory Reporting, Cash-Transaction Reporting | VS-156 |
| W4747 | Rental Vehicle LTO Registration, Conduction Sticker & Motor-Vehicle Titling | VS-162 |
| W4760 | Rental Billing, Settlement, Deposit Release & POS/Account Posting | VS-162 |
| W4762 | Damage Recovery, Insurance Claim, Deductible Settlement & Subrogation | VS-162 |
| W4766 | Rental Regulatory Compliance — LTO/LTFRB, DOLE Driver Fitness, Consumer Act | VS-162 |
| W4767 | Rental Data Privacy — License/Image/Telematics Data Governance & DSAR | VS-162 |
| W4801 | BOPIS-to-Locker Staging, Compartment Assignment & Replenishment | VS-164 |
| W4808 | Daily Locker Reconciliation, Inventory Accuracy & Exception Handling | VS-164 |
| W4810 | Reactive Fault Triage, Field Repair & Vendor Dispatch | VS-164 |
| W4812 | Accessibility (PWD/Senior) Compliance & Inclusive Locker Operations | VS-164 |
| W4891 | Music Royalty Licensing — FILSCAP / OPM / IP Compliance & Statutory Reporting | VS-168 |
| W4909 | Accessibility & Regulatory Compliance (RA 7394 Price-Integrity, RA 10173 Voice/Privacy) | VS-168 |
| W4965 | Order Readiness, Pre-Stage Pick & Bulk-Goods Staging Area Operations | VS-171 |
| W4967 | BOPIS / Ecommerce / Special-Order Pickup Integration at the Will-Call Counter | VS-171 |
| W4973 | Forklift Operator Qualification, Equipment Inspection & DOLE OSH Compliance | VS-171 |
| W4982 | Loading-Zone Safety Incident, CAPA & Customer-Injury Response | VS-171 |
| W5036 | Portable & Mobile Storage Container-Fleet Strategy, Sizing & Procurement | VS-174 |
| W5045 | Portable/Mobile Container Delivery, Placement, Relocation & Pickup Operations | VS-174 |
| W5046 | Customer Move-Out, Unit Inspection, Damage Assessment & Final Settlement | VS-174 |
| W5052 | Storage Fire/Life-Safety, BFP Compliance & Emergency Preparedness | VS-174 |
| W5053 | Portable Container Fleet Maintenance, Cleaning, Sanitization & Lifecycle | VS-174 |
| W5055 | Customer Move-In/Move-Out Seasonality & Demand Forecasting | VS-174 |
| W5061 | LPG Storage Cage & Yard Design, BFP Fire-Code Infrastructure & Safety Setup | VS-175 |
| W5063 | LPG DOE Retailer Accreditation, DTI-BPS Standards & Metrology Compliance | VS-175 |
| W5065 | Customer Cylinder Exchange Transaction & POS Workflow (Full-for-Empty) | VS-175 |
| W5067 | In-Store LPG Cage Daily Operations, Inventory & Cylinder Receiving/Dispatch | VS-175 |
| W5070 | Cylinder-Fleet Replenishment, Inter-Store Transfer & Rebalancing | VS-175 |
| W5073 | LPG Daily Safety Inspection, Leak Detection & BFP Fire-Code Compliance | VS-175 |
| W5074 | Cylinder Inventory Reconciliation, Shrink & Deposit/Float Accounting | VS-175 |
| W5075 | LPG Incident, Leak, Fire & Emergency Response & Reporting (DOLE/BFP/DOE) | VS-175 |
| W5076 | Cylinder-Asset, Deposit & Float Reconciliation & Audit | VS-175 |

**Finance** (118)

| ID | Workflow | Value Stream |
|---|---|---|
| W1181 | BIR Point-of-Sale (POS) System Registration & CAS Compliance Maintenance | VS-17 |
| W1200 | Trade Account Monthly Statement Review, Credit Limit Recalibration & Churn Prevention | VS-16 |
| W1201 | Intercompany Monthly Settlement Batch Processing & Netting Execution | VS-17 |
| W1202 | Store Daily Cash Collection, Armored Car Pickup & Bank Deposit Reconciliation | VS-18 |
| W1218 | Intercompany Service Agreement Annual Review, Rate Adjustment & Renewal | VS-17 |
| W1245 | Customer Trade Account Credit Limit Periodic Review, Risk Scoring & Adjustment | VS-16 |
| W1277 | Intercompany Warehouse Service Fee Monthly Calculation, Billing & Reconciliation | VS-17 |
| W1293 | Multi-Entity Intercompany Service Fee Billing & Settlement | VS-17 |
| W1299 | Intercompany Transfer Pricing Review, Adjustment & Arm's-Length Compliance Documentation | VS-17 |
| W1300 | Trade Account Credit Limit Annual Review, Adjustment & Exposure Monitoring | VS-16 |
| W1310 | Import Letter of Credit (LC) Lifecycle Management, Amendment & Settlement Processing | VS-15 |
| W1342 | Real-Time Gross Settlement (RTGS) & High-Value Payment Processing | VS-18 |
| W1343 | Petty Cash Fund Lifecycle, Custodian Accountability & Periodic Replenishment | VS-18 |
| W1344 | Intercompany Fund Transfer, Cash Pooling & Entity Settlement | VS-18 |
| W1362 | Vendor Payment Run Execution, File Generation & Multi-Bank Disbursement Processing | VS-18 |
| W1380 | Customer Post-Dated Check (PDC) Receipt, Register Management & Bank Deposit Processing | VS-16 |
| W1381 | Customer Bounced Check (DAIF) Resolution, Legal Action & BIR Reporting | VS-16 |
| W1382 | Customer Electronic Payment (PESONet/InstaPay) Reconciliation & Auto-Application | VS-16 |
| W1417 | Intercompany E-Commerce Platform Per-Order Fee Monthly Calculation, Settlement & Revenue Recognition | VS-17 |
| W1418 | Multi-Entity Consolidated VAT Input-Output Reconciliation, Monthly BIR 2550M Filing & Credit Tracking | VS-17 |
| W1420 | Trade Account Monthly Statement Generation, Aging Analysis & Field Collection Route Planning | VS-16 |
| W1431 | Multi-Entity Fixed Asset Capitalization, Intercompany Asset Transfer & Depreciation Consolidation | VS-17 |
| W1456 | Multi-Entity Intercompany FX Settlement & Transfer Pricing Rate Management | VS-18 |
| W1496 | Intercompany Warehouse Service Fee Dispute Resolution, Rate Review & Quarterly Settlement Agreement | VS-17 |
| W1503 | BIR Percentage Tax vs. VAT Threshold Monitoring, Quarterly Tax Regime Evaluation & Registration Adjustment | VS-17 |
| W1524 | Philippine Government & Institutional Customer Tax-Exempt Sales Processing, BIR-Compliant Documentation & OR Requirements | VS-16 |
| W1525 | Philippine BIR Computerized Accounting System (CAS) Registration, Permit Renewal & Annual Compliance | VS-17 |
| W1540 | Trade Account Monthly Statement Generation, Aging Analysis & Collection Priority Scoring | VS-16 |
| W1688 | Petty Cash Management & Reconciliation | VS-34 |
| W1766 | Consumer Credit Application Processing at POS | VS-38 |
| W1770 | Financing Compliance & BSP Regulatory Monitoring | VS-38 |
| W1773 | Installment Payment Collection & Monitoring | VS-38 |
| W1774 | Installment Delinquency Tracking & Collection Action | VS-38 |
| W1777 | Installment Sale Tax Compliance (VAT, WHT) | VS-38 |
| W1779 | Financing Partner Daily Settlement Reconciliation | VS-38 |
| W1780 | Monthly Financing Partner Statement Reconciliation | VS-38 |
| W1783 | Multi-Tender Transaction Reconciliation | VS-38 |
| W1785 | Ecommerce Financing Settlement Reconciliation | VS-38 |
| W1786 | Annual Financing Program Financial Close & Audit | VS-38 |
| W1790 | Growth Incentive & New Store Opening Rebate Management | VS-39 |
| W1794 | Rebate Accrual-to-Settlement Reconciliation | VS-39 |
| W1799 | Vendor Co-Op Fund Reimbursement Claim & Settlement | VS-39 |
| W1803 | Rebate Settlement Processing (Credit Note & Cash) | VS-39 |
| W1804 | Rebate Income Recognition & GL Posting | VS-39 |
| W2143 | Gift Card Sale & Activation at POS | VS-54 |
| W2150 | In-Store Gift Card Redemption at POS | VS-54 |
| W2158 | Daily Gift Card Liability Reconciliation | VS-54 |
| W2486 | Credit Limit Setting & Approval | VS-68 |
| W2487 | Real-Time Credit Limit Monitoring | VS-68 |
| W2488 | Credit Limit Increase Request | VS-68 |
| W2489 | Credit Limit Reduction & Suspension | VS-68 |
| W2494 | Pre-Legal Collections & Negotiation | VS-68 |
| W2495 | Legal Collection Escalation | VS-68 |
| W2582 | Intercompany Service Agreement Management | VS-72 |
| W2583 | Monthly IC Invoice Generation & Settlement | VS-72 |
| W2586 | Intercompany Cash Settlement & Netting | VS-72 |
| W2592 | IC Profit Elimination & Consolidation Impact Analysis | VS-72 |
| W2594 | Transfer Pricing Documentation & BIR Compliance | VS-72 |
| W2745 | Customer AR Payment Application & Unapplied Cash Resolution | VS-16 |
| W2746 | Customer AR Dispute Resolution & Credit Note Processing | VS-16 |
| W2780 | BNPL (Home Credit/Billease) Provider Integration & Reconciliation | VS-80 |
| W2783 | Payment Partner Offboarding & Business Continuity Cutover | VS-80 |
| W2784 | Multi-Entity Merchant Settlement Hierarchy & GL Mapping | VS-80 |
| W2785 | Daily Card/E-Wallet Settlement File Ingestion & GL Posting | VS-80 |
| W2786 | Settlement-to-POS Capture Reconciliation & Exception Triage | VS-80 |
| W2787 | Mid-Batch / End-of-Day Terminal Close & Capture Totals Validation | VS-80 |
| W2790 | Refund, Void & Partial-Reversal Settlement Matching | VS-80 |
| W2792 | Aged Unreconciled Settlement & Suspense GL Clearing | VS-80 |
| W2794 | Cardholder Data Environment (CDE) Boundary & Tokenization Vault Governance | VS-80 |
| W2799 | Acquirer/Network Compliance (Visa/MC/BSP) & Assessment Response | VS-80 |
| W3170 | Lease Billing Cycle, Auto-Debit & AR Management | VS-96 |
| W3182 | Lease Regulatory Compliance (BSP, Truth in Lending, BIR) | VS-96 |
| W3183 | Lease Tax, VAT & Withholding Treatment | VS-96 |
| W3379 | Vendor SCF Eligibility, Enrollment & KYC Onboarding | VS-105 |
| W3380 | Approved-Payable Monetization, Invoice Upload & Funder Settlement | VS-105 |
| W3387 | Self-Funded Early-Payment Execution, Funding & Bank Settlement | VS-105 |
| W3391 | Multi-Entity / Intercompany Payable Discount Coordination | VS-105 |
| W3392 | Discount Capture Reconciliation, GL Posting & Audit Trail | VS-105 |
| W4271 | COD Governance, Compliance & BIR/Cash-Reporting Framework | VS-142 |
| W4274 | Doorstep Cash Collection, Receipting & POD Capture | VS-142 |
| W4277 | Daily COD Cash-vs-Order Reconciliation & Exception Resolution | VS-142 |
| W4279 | COD Bank Deposit Verification & GL Cash Posting | VS-142 |
| W4281 | COD Settlement Cycle, Clearing & Inter-Entity Settlement | VS-142 |
| W4415 | PFRS 16 Transition (Modified vs Full Retrospective) | VS-148 |
| W4416 | Multi-Entity (5 Entities) Consolidated Lease Accounting Setup | VS-148 |
| W4424 | Intercompany Lease Elimination & Consolidation Entries | VS-148 |
| W4425 | Lease Accounting Period-End Close, Reconciliation & Disclosures | VS-148 |
| W4429 | Tax (VAT/WHT/Documentary Stamp) on Lease Payments | VS-148 |
| W4430 | Lessor/Property-Owner Counterparty Settlement (links VS-97/VS-72) | VS-148 |
| W4535 | Captive Tax, Transfer Pricing & Intercompany Framework | VS-153 |
| W4546 | Captive Reinsurance Recovery & Collections | VS-153 |
| W4547 | Captive Finance, Statutory Accounting & Reporting | VS-153 |
| W4554 | Lender/Partner Network Development (Banks, Pag-IBIG, Financing Companies) | VS-154 |
| W4555 | Brokerage/Referral Licensing, Accreditation & Contract Setup | VS-154 |
| W4571 | Draw-Milestone Monitoring, Variation & Project-Loan Reconciliation | VS-154 |
| W4573 | Regulatory Compliance, Consumer Protection & BSP Reporting | VS-154 |
| W4638 | Variable Consideration, Constraint & Estimate-Update (Rebates, Refunds, SC/PWD, Price-Freeze) | VS-157 |
| W4642 | Year-End Comprehensive PFRS 15 Review, Policy Refresh & Recalculation | VS-157 |
| W4644 | External-Audit PFRS 15 Coordination, Sampling & Evidence | VS-157 |
| W4645 | New-Revenue-Stream / New-Channel Pre-Launch PFRS 15 Assessment & Accounting Decision | VS-157 |
| W4647 | Contract-Liability, Contract-Asset & AR-Receivable Reconciliation & Cut-off | VS-157 |
| W4651 | Import Landed-Cost Build-Up: Freight, Duty, Brokerage, Insurance & Port Freight | VS-158 |
| W4660 | Inventory Adjustment, Write-Down & NRV Cost Impact | VS-158 |
| W4663 | Cost-of-Goods-Sold Reconciliation, Cut-off & Period Matching | VS-158 |
| W4667 | Intercompany Cost Transfer & Transfer-Pricing Cost Build | VS-158 |
| W4937 | ABL & Inventory/AR-Pledge Financing Strategy, Facility Structuring & Bank-Relationship Governance | VS-170 |
| W4945 | Trust-Receipt Financing Program Setup & PD 115 Compliance Framework | VS-170 |
| W4946 | Import Document Release Against Trust Receipt & Goods-in-Trust Establishment | VS-170 |
| W4947 | Trust-Receipt Sell-Through Tracking & Proceeds Segregation | VS-170 |
| W4948 | Trust-Receipt Proceeds Remittance & Release Lifecycle | VS-170 |
| W4949 | Warehouse-Receipt & Field-Warehousing Collateral Operations | VS-170 |
| W4950 | Import-Inventory-In-Transit Financing & Pre-Shipment / LC Settlement | VS-170 |
| W4954 | Borrowing-Base to Inventory/AR Subledger Reconciliation | VS-170 |
| W4955 | PFRS Encumbrance Disclosure, PAS 37 / Contingent-Liability Reporting & Note Reconciliation | VS-170 |
| W4959 | Interest Accrual, Charge Settlement & Bank Fee Reconciliation | VS-170 |
| W5018 | Annual Report, General Information Sheet & Statutory SEC/Commissioner Investor Disclosure | VS-173 |
| W5022 | Insider List, Trading-Window & Securities-Trading Compliance (RA 8799 SRC) | VS-173 |
| W5026 | Stock Transfer, Share-Movement & Investor Position Reconciliation | VS-173 |

**People** (37)

| ID | Workflow | Value Stream |
|---|---|---|
| W1306 | Multi-Entity Statutory Benefits Consolidation, Remittance Reconciliation & Government Portal Compliance | VS-19 |
| W1324 | Employee Retrenchment & Redundancy Processing (Labor Code Art. 298–299 Compliance) | VS-19 |
| W1383 | Employee Resignation Processing, Clearance & Final Pay Computation (Philippine Labor Code) | VS-19 |
| W1384 | Employee 13th Month Pay Computation, Proration & BIR Taxable Benefit Reporting | VS-19 |
| W1385 | Employee Separation Pay Computation, DOLE Clearance & Retirement Benefit Settlement | VS-19 |
| W1416 | Philippine 13th Month Pay Computation, Monthly Accrual Booking & Year-End Compliance Processing | VS-19 |
| W1527 | Employee SSS, PhilHealth, Pag-IBIG Monthly Contribution Filing, Remittance & Reconciliation | VS-19 |
| W3211 | DOLE D.O. 174 Labor-Only Contracting Compliance & Contract Structuring | VS-98 |
| W3217 | Work Order, Requisition & Dispatch Coordination | VS-98 |
| W3221 | Invoice Validation, Timesheet Reconciliation & Approval | VS-98 |
| W3226 | Misclassification Audit & DOLE Inspection Defense | VS-98 |
| W3309 | Pay Equity, Equal-Pay-for-Equal-Work Analysis & Gender/Wage-Gap Remediation | VS-102 |
| W3310 | Geographic/Differential Pay & Multi-Region Minimum-Wage Compliance | VS-102 |
| W3314 | Statutory Benefits (SSS/PhilHealth/Pag-IBIG) Program Administration & Compliance | VS-102 |
| W4250 | Daily Shuttle Dispatch, Manifest & Passenger Check-In | VS-141 |
| W4259 | Transport Vendor Invoice, Reconciliation & Settlement | VS-141 |
| W4317 | Housing Cost, Subsidy, Salary-Deduction & Intercompany Allocation Policy | VS-144 |
| W4318 | Housing Safety, Welfare & DOLE/OSH Compliance Standard | VS-144 |
| W4327 | Health, Emergency & Evacuation in Dormitories | VS-144 |
| W4331 | Housing Cost Recovery, Rent/Utility Recharge & Reconciliation | VS-144 |
| W4333 | Dormitory Fire/Life-Safety, BFP & Inspections | VS-144 |
| W4458 | DOLE D.O. 53-03 & PH Regulatory Framework Alignment | VS-150 |
| W4459 | Safety-Sensitive & Driver (LTFRB/DOTr) Role Identification | VS-150 |
| W4460 | Drug Testing Vendor (Collection/Lab/MRO) Selection & Contract | VS-150 |
| W4469 | Specimen Collection, Chain-of-Custody & Laboratory Testing | VS-150 |
| W4477 | Drug-Free Workplace Audit, Inspection & DOLE Documentation | VS-150 |
| W4705 | DOLE Alien Employment Permit (AEP) Application & Renewal Operations | VS-160 |
| W4709 | Foreign Executive, Director & Board-Officer Visa & SEC-Related Compliance | VS-160 |
| W4711 | Immigration Document, Expiry & Compliance Tracking (BI/DOLE Audits) | VS-160 |
| W4712 | Foreign-Worker Wage, Minimum-Wage & Anti-Discrimination Compliance (DOLE) | VS-160 |
| W4713 | Assignment Payroll, Multi-Currency & Home/Host Split-Pay Operations | VS-160 |
| W4715 | Assignment Statutory Benefits, SSS/PhilHealth/Pag-IBIG & Home-Country Continuity | VS-160 |
| W4719 | Immigration/DOLE Inspection, Audit Defense & Penalty Management | VS-160 |
| W4867 | Screening-Vendor Selection, PNP-SOSIA Licensing & Contracting | VS-167 |
| W4872 | Screening Data Governance, Retention, DSAR & Records Management | VS-167 |
| W4885 | Screening Cost & ROI Analytics — Spend, Loss-Avoided, Vendor Consolidation | VS-167 |
| W4886 | Regulatory Change Monitoring (DOLE/NPC/NBI/PNP) & Policy Update | VS-167 |

**Asset & Infrastructure** (26)

| ID | Workflow | Value Stream |
|---|---|---|
| W1183 | Store Lease CAM Reconciliation, Rent Escalation & Landlord Relationship Management | VS-20 |
| W1702 | Fixed Asset Register Reconciliation & Reporting | VS-35 |
| W1703 | Entity-Level & Consolidated Asset Reporting | VS-35 |
| W1704 | Tax Depreciation & BIR Compliance Reporting | VS-35 |
| W1705 | Capital Work-in-Progress Reconciliation | VS-35 |
| W1864 | Common Area Maintenance (CAM) Charge Reconciliation & Dispute Resolution | VS-42 |
| W1868 | Multi-Entity Rent Settlement & Intercompany Billing | VS-42 |
| W1871 | Local Business Tax (LBT) & LGU Permit Renewal Management | VS-42 |
| W1872 | PFRS 16 Lease Accounting — Month-End Processing & Disclosure | VS-42 |
| W1873 | Building & Occupancy Permit Compliance Monitoring | VS-42 |
| W1876 | Fire Safety Inspection & Bureau of Fire Protection (BFP) Compliance | VS-42 |
| W1877 | Property Utility Account Management & Meter Reading Reconciliation | VS-42 |
| W2265 | Store Closure Communication Plan | VS-59 |
| W2275 | Final Financial Settlement | VS-59 |
| W2281 | Store Closure Database & Knowledge Management | VS-59 |
| W3193 | Master Lease & Intercompany Lease Framework | VS-97 |
| W3207 | Intercompany Rent Benchmarking & Transfer Pricing | VS-97 |
| W3463 | Net-Metering Settlement, Export Billing & Import/Export Reconciliation | VS-108 |
| W3464 | Renewable Asset Safety, Structural & Insurance Incident Management | VS-108 |
| W3755 | DOE EICC/Energy Reporting & Compliance Submission | VS-120 |
| W3758 | Multi-Entity/Site Energy Management & Consolidated Reporting | VS-120 |
| W4191 | Facilities Business Continuity & Critical-Systems Resilience | VS-138 |
| W4786 | Reactive Fault Triage, Field Repair & Vendor Dispatch | VS-163 |
| W4787 | Charging-Site Safety, Emergency Response & Incident Management | VS-163 |
| W4790 | Host-Revenue Settlement, CPO Recon & Financial Close | VS-163 |
| W4791 | Charging Compliance Audit — DOE/LGU/RA 11697/RA 7394 & Cyber/Privacy | VS-163 |

**Governance & Assurance** (99)

| ID | Workflow | Value Stream |
|---|---|---|
| W1203 | Philippine Data Privacy Act (RA 10173) Compliance Audit, DPO Reporting & NPC Registration | VS-22 |
| W1204 | Store-Level Business Continuity Plan (BCP) Annual Update, Tabletop Exercise & Certification | VS-26 |
| W1219 | BIR Electronic Invoicing System (EIS) Onboarding & Compliance Readiness | VS-22 |
| W1244 | Philippine LGU Business Permit Batch Renewal, Monitoring & Compliance Tracking for Store Network | VS-22 |
| W1248 | BOPIS Staging Area Security & Omnichannel Fulfillment Fraud Prevention | VS-23 |
| W1249 | Consignment & Vendor-Managed Inventory Shrinkage Monitoring & Reconciliation | VS-23 |
| W1266 | Store-Level Customer Safety Incident Management, First Aid Response & Liability Documentation | VS-24 |
| W1296 | Store-Level Fire Safety Equipment Inspection & BFP Compliance | VS-24 |
| W1304 | BIR Computerized Accounting System (CAS) Registration, Compliance & Audit Readiness | VS-22 |
| W1312 | Store-Level Hazardous Material (Paint/Chemical/Solvent) Spill Response, Cleanup & Environmental Reporting | VS-24 |
| W1322 | IT Disaster Recovery (DR) Failover Test Execution, Validation & Recovery Time Assessment | VS-26 |
| W1367 | BIR CAS Registration Renewal, System Change Notification & Annual Compliance Attestation | VS-22 |
| W1392 | DC-Level Business Continuity Plan, Annual Tabletop Exercise & Recovery Time Objective Validation | VS-26 |
| W1393 | Store-Level IT Disaster Recovery, POS System Failover & Manual Operations Procedure | VS-26 |
| W1397 | Philippine SEC Sustainability Reporting (Memo Circular No. 4) Annual Data Collection & Report Preparation | VS-25 |
| W1404 | DENR Environmental Compliance Inspection Response, Documentation Package & Corrective Action Management | VS-22 |
| W1421 | Philippine LGU Business Permit Annual Renewal, Local Business Tax Filing & Multi-Location Compliance Tracking | VS-22 |
| W1449 | Volcanic Eruption & Ashfall Business Continuity Protocol for BuildRight Stores and DCs | VS-26 |
| W1489 | BIR Electronic Invoicing (E-Invoice) Compliance, System Registration & Monthly Transmission | VS-22 |
| W1529 | Responsible Timber & Wood Product Sourcing, Chain-of-Custody Verification & DENR Compliance | VS-25 |
| W1600 | DC Goods Receipt Quality Sampling & Acceptance | VS-31 |
| W1610 | Vendor Corrective Action Request (VCAR) Management | VS-31 |
| W1615 | Product Recall Assessment & Decision | VS-31 |
| W1616 | Product Recall Execution & Customer Notification | VS-31 |
| W1617 | Product Recall Effectiveness Verification & Closure | VS-31 |
| W1618 | Regulatory Incident Reporting & Government Notification | VS-31 |
| W1661 | Competitor Store Visit Program & Systematic Data Collection | VS-33 |
| W1718 | SEC Annual Filing & Corporate Information Update | VS-36 |
| W1724 | Stock Transfer & Ownership Change Processing | VS-36 |
| W1731 | Intercompany Service Agreement Governance, Transfer Pricing & Board Authorization | VS-36 |
| W1735 | Data Privacy Governance & NPC Compliance | VS-36 |
| W2598 | Store-Level Waste Segregation & Daily Collection | VS-73 |
| W2603 | E-Waste & Battery Collection & Disposal | VS-73 |
| W2609 | DENR Hazardous Waste Permit & Registration Management | VS-73 |
| W2611 | Spill Response & Containment Protocol | VS-73 |
| W2670 | Multi-Location Business Permit Renewal Calendar | VS-76 |
| W2671 | New Store Business Permit Application | VS-76 |
| W2672 | Fire Safety Inspection & BFP Compliance | VS-76 |
| W2675 | Sanitary & Health Permit Compliance | VS-76 |
| W2681 | DOLE Regional Labor Standard Compliance | VS-76 |
| W2682 | Consumer Protection Compliance (RA 7394) | VS-76 |
| W2684 | LGU Disaster & Emergency Response Regulatory Compliance | VS-76 |
| W2685 | BIR CAS Registration Per Location | VS-76 |
| W2692 | Store Closure LGU Regulatory Decommissioning | VS-76 |
| W2693 | Annual Multi-Region Regulatory Compliance Report | VS-76 |
| W2747 | DTI Sales Promotion Permit Application & Compliance | VS-22 |
| W2921 | Customer KYC Tiering, Risk Scoring & Due Diligence Level Determination | VS-86 |
| W2922 | Vendor/Supplier Due Diligence, UBO Identification & Beneficial Ownership | VS-86 |
| W2923 | PEP (Politically Exposed Person) Screening & Enhanced Due Diligence | VS-86 |
| W2924 | Sanctions & Watchlist Screening (UN/OFAC/EU/AMLC/INTERPOL) | VS-86 |
| W2926 | KYC Document Verification, TIN/BIR & SEC Registry Validation | VS-86 |
| W2927 | Periodic KYC Refresh, Trigger Event Re-Review & Offboarding | VS-86 |
| W2928 | KYC Data Quality, Consent & Data Privacy Compliance | VS-86 |
| W2930 | Suspicious Transaction Detection, Alert Triage & Escalation | VS-86 |
| W2931 | Suspicious Transaction Report (STR) Filing with AMLC | VS-86 |
| W2932 | Covered Transaction Report (CTR) Filing & AMLC Portal Management | VS-86 |
| W2935 | AML Case Management, Investigation & Law Enforcement Cooperation | VS-86 |
| W2936 | AML Rule Tuning, Threshold Governance & False-Positive Reduction | VS-86 |
| W2945 | HS Tariff Classification & AHTN Code Assignment per Imported SKU | VS-87 |
| W2946 | Tariff Commission Advance Ruling on Tariff Classification Application | VS-87 |
| W2947 | Customs Valuation (Transaction Value) & Adjustments Management | VS-87 |
| W2948 | Assists, Royalties & Additions to Customs Value Capture | VS-87 |
| W2951 | Tariff Classification Master Maintenance & Item Master Integration | VS-87 |
| W2952 | Classification Audit, Discrepancy & Reconciliation | VS-87 |
| W2954 | Certificate of Origin (Form D/RCEP CO) Procurement & Vendor Onboarding | VS-87 |
| W2956 | Customs Bonded Warehouse (CBW) Compliance & Inventory Reconciliation | VS-87 |
| W2957 | VAT Zero-Rating of Import for Resale/Export Documentation | VS-87 |
| W2961 | Customs Broker Selection, Accreditation & Performance Management | VS-87 |
| W2962 | BOC Post-Entry Audit (PEA) Readiness & Response | VS-87 |
| W2963 | BOC Alert Order, Hold & Detention Resolution | VS-87 |
| W2965 | Data Privacy Act (RA 10173) Compliance for Customs Data Sharing | VS-87 |
| W2967 | BIR-to-BOC Reconciliation (Import VAT, Duties, BCOR/SSDT on Imports) | VS-87 |
| W2973 | Physical Records Storage, Barcode & Retrieval Management | VS-88 |
| W2975 | BIR-Compliant E-Invoice, E-Receipt & E-Book Archiving | VS-88 |
| W2977 | Retention Schedule Maintenance by Record Class (BIR/SEC/DOLE/NPC) | VS-88 |
| W2979 | Legal Hold Issuance, Scope & Release Management | VS-88 |
| W2983 | Data Subject Erasure Requests & Retention Conflict Resolution | VS-88 |
| W2984 | Records Insurance, Off-Site Vaulting & Disaster Recovery | VS-88 |
| W2985 | e-Discovery Request Response, Collection & Production | VS-88 |
| W2986 | BIR Records Inspection (LOA) Support & Production | VS-88 |
| W2987 | SEC Corporate Records Filing & Inspection Support | VS-88 |
| W2988 | NPC Data Privacy Audit & Records Production | VS-88 |
| W2989 | DOLE Labor Inspection Records Production | VS-88 |
| W4375 | Service-Quality Data Validation, Scoring & Quality Control | VS-146 |
| W4377 | Store/Unit Service-Findings Feedback & Corrective Action | VS-146 |
| W4391 | Customer Safety Compliance — Consumer Act, BFP Fire Code, OSH & Local Codes | VS-147 |
| W4400 | Vulnerable-Customer (PWD/Senior/Child) Safety & Accommodation | VS-147 |
| W4405 | Regulatory (BFP/DOLE/LGU/BIR) & Insurance Incident Notification | VS-147 |
| W4506 | Foundation Legal Setup, SEC Registration & BIR Qualified-Donee Status | VS-152 |
| W4507 | Foundation Governance, Board & PCNC Accreditation | VS-152 |
| W4518 | Employee Volunteerism, Payroll-Giving & Donation Drives | VS-152 |
| W4524 | Foundation Annual Report, Audit & Regulatory Filing | VS-152 |
| W4730 | Cybersecurity & IT-Controls Attestation (SOC 2 / ISO 27001 / PCI DSS) Collection | VS-161 |
| W4732 | ABC, Sanctions & Beneficial-Ownership Due Diligence | VS-161 |
| W4733 | Operational, Resilience & BCP/DR Evidence Collection (RTO/RPO, Substitutes) | VS-161 |
| W4742 | Regulator-Facing TPRM Evidence (BSP Data-Processor, NPC, BIR, DOLE) | VS-161 |
| W4842 | Unified License/Permit/Accreditation Inventory & Register Build | VS-166 |
| W4845 | Renewal Calendar, Expiry-Risk Engine & Compliance Dashboard | VS-166 |
| W4850 | Multi-Site Permit Renewal Campaigns (LGU Business Permit, Mayor's Permit, BFP FSIC) | VS-166 |

**Technology & Data** (39)

| ID | Workflow | Value Stream |
|---|---|---|
| W1205 | PCI-DSS Compliance for POS Payment Card Data & Annual QSA Audit Management | VS-27 |
| W1206 | AI-Powered Demand Forecasting Model Training, Accuracy Monitoring & Retraining Cycle | VS-30 |
| W1341 | Intelligent Document Processing (IDP) for Invoice & Receipt Automation | VS-30 |
| W1390 | Store POS Transaction Data Quality Validation, Anomaly Detection & Correction Processing | VS-28 |
| W1453 | IoT-Enabled Shelf Monitoring, Real-Time Stock-Out Detection & Automated Replenishment Trigger | VS-30 |
| W1454 | Augmented Reality (AR) Home Visualization Tool Operations, 3D Product Catalog & Customer Project Planning | VS-30 |
| W1457 | RFID-Based Smart Shelf Inventory Monitoring & Automated Replenishment Trigger PoC | VS-30 |
| W1481 | Data Pipeline Disaster Recovery, Failover Testing & RTO/RPO Validation | VS-28 |
| W1531 | Philippine Store WAN Connectivity Monitoring, ISP SLA Management & Failover Testing | VS-27 |
| W1544 | POS Terminal Lifecycle Management, Hardware Refresh Cycle & Peripheral Standardization | VS-27 |
| W1545 | Cost Center & Profit Center Hierarchy Governance, Allocation Rule Review & Reporting Validation | VS-29 |
| W1569 | Computer Vision-Based Shelf Gap Detection, Planogram Compliance Monitoring & Automated Replenishment Alerting PoC | VS-30 |
| W1571 | AI-Powered Vendor Negotiation Price Optimization, Cost Prediction & Purchase Order Timing Recommendation Engine | VS-30 |
| W1572 | Intelligent Document Processing for Vendor Invoice Automation, Receipt OCR & GL Code Auto-Classification | VS-30 |
| W3233 | IT Asset Discovery, Inventory & CMDB Reconciliation | VS-99 |
| W3242 | License Optimization, Reharvesting & Reconciliation | VS-99 |
| W3247 | Open Source License Compliance & Security | VS-99 |
| W3254 | Asset Disposal Compliance (Data Privacy / BIR / E-Waste) | VS-99 |
| W3929 | AI/ML Strategy, Operating Model & Governance Framework | VS-128 |
| W3930 | AI/ML Policy, Standards & Risk Appetite | VS-128 |
| W3931 | AI Model Inventory, Registry & Tiering | VS-128 |
| W3932 | Model Risk Management & Independent Validation | VS-128 |
| W3933 | AI/ML Roles, Ownership & the Three Lines of Defense | VS-128 |
| W3934 | AI/ML Vendor, Open-Source & Foundation-Model Governance | VS-128 |
| W3937 | AI Fairness, Bias Testing & Non-Discrimination | VS-128 |
| W3938 | AI Explainability, Transparency & Customer Disclosure | VS-128 |
| W3939 | AI Data Governance, Privacy (RA 10173) & Consent for Profiling | VS-128 |
| W3940 | AI Safety, Robustness & Adversarial/Failure Management | VS-128 |
| W3941 | Human Oversight, Intervention & the Human-in-the-Loop | VS-128 |
| W3942 | Generative AI & Content Governance (IP, Hallucination, Misuse) | VS-128 |
| W3949 | AI Controls Assurance, Audit Support & Internal Audit | VS-128 |
| W4117 | Technology Financial Month-End, Accruals & GL Reconciliation | VS-135 |
| W4481 | GS1 Membership, GTIN/Barcode Standard & Item-Identification Policy | VS-151 |
| W4482 | Item Auto-ID Data Model (GTIN, Serial, Lot/Batch, Expiry, Variable-Measure) | VS-151 |
| W4486 | Barcode Quality, Read-Rate & Label-Conformance Standard | VS-151 |
| W4487 | Regulatory Labeling Compliance (RA 7394 Price Tag, DTI-BPS, DG/SDS, Energy Label) | VS-151 |
| W4494 | Catch-Weight / Variable-Measure Labeling at POS & Cutting | VS-151 |
| W4496 | Label Application Quality, Reconciliation & End-of-Life Media Control | VS-151 |
| W4500 | EAS/RFID Tag Detachment, Reuse & Reconciliation | VS-151 |

#### Tier 2 (1,694)

**Plan & Source** (130)

| ID | Workflow | Value Stream |
|---|---|---|
| W1220 | Seasonal Forward-Buy & Pre-Season Stock Build Planning for Philippine Weather Cycles | VS-1 |
| W1231 | Store-Level Construction Material Price Volatility Monitoring & Dynamic Cost Adjustment | VS-1 |
| W1278 | Store-Level Competitor Price Monitoring & Market Intelligence Reporting | VS-1 |
| W1303 | Vendor Rebate, Co-Op Advertising Fund & Promotional Incentive Management | VS-3 |
| W1313 | Vendor-Supplied Merchandising Fixture, Display & Point-of-Purchase (POP) Material Lifecycle Management | VS-1 |
| W1346 | Multilingual Product Content Localization (Filipino/English) & Regional Variant Management | VS-1 |
| W1355 | Typhoon & Natural Disaster Demand Surge Forecasting & Pre-Positioning | VS-2 |
| W1356 | Store-Level Demand Sensing & Local Event-Driven Forecast Adjustment | VS-2 |
| W1422 | Seasonal Merchandise Forward Buy Planning, Import Pre-Booking & Arrival Calendar Management | VS-1 |
| W1436 | Philippine Construction Material Price Volatility Monitoring, Forward Buy Decision & Cost Hedge Planning | VS-2 |
| W1465 | Product Safety Data Sheet (SDS) Management, Hazmat Technical Documentation & Compliance Tracking | VS-1 |
| W1466 | Seasonal Product Content Pre-Staging, Launch Readiness Verification & Cross-Channel Publishing | VS-1 |
| W1492 | Typhoon Season Pre-Positioning of Emergency Construction Materials (Tarpaulins, Plywood, CGI Sheets) & Demand Allocation Across Store Network | VS-2 |
| W1830 | Private Label Category Opportunity Assessment & Product Selection | VS-41 |
| W1831 | Private Label Factory Sourcing, Audit & Qualification | VS-41 |
| W1832 | Private Label Product Specification & Sample Development | VS-41 |
| W1835 | Private Label Product Lifecycle Performance Review & Rationalization | VS-41 |
| W1836 | Exclusive Brand Partnership Negotiation & Onboarding | VS-41 |
| W1837 | Private Label Supplier Contract Renewal, Renegotiation & Transition Management | VS-41 |
| W1838 | Private Label Ongoing Production Quality Monitoring & Factory Audit Program | VS-41 |
| W1840 | Private Label Product Regulatory Compliance Testing & Certification Renewal | VS-41 |
| W1842 | Private Label Shelf-Life Monitoring & Near-Expiry Management | VS-41 |
| W1843 | Private Label Packaging & Labeling Compliance Audit | VS-41 |
| W1845 | Private Label Supplier Social Compliance & Environmental Audit Management | VS-41 |
| W1846 | Private Label Brand Identity Development & Guideline Management | VS-41 |
| W1847 | Private Label Packaging Design, Artwork Approval & Production | VS-41 |
| W1848 | Private Label In-Store Display, Planogram & Merchandising Standards | VS-41 |
| W1849 | Private Label Launch Campaign Planning & Execution | VS-41 |
| W1852 | Private Label Digital Content & Ecommerce Presentation Management | VS-41 |
| W1853 | Private Label Trade Marketing & Contractor Program Integration | VS-41 |
| W1927 | Consignment Stock Display & Shelf Management | VS-45 |
| W1929 | Consignment Stock Rotation & Aging Management | VS-45 |
| W1931 | Consignment Return-to-Vendor Processing | VS-45 |
| W1932 | Consignment Price Change & Promotional Price Handling | VS-45 |
| W1934 | VMI Agreement Setup & Parameter Configuration | VS-45 |
| W1935 | VMI Data Sharing & Demand Signal Transmission | VS-45 |
| W1938 | VMI Stock Level Monitoring & Exception Management | VS-45 |
| W1939 | VMI New Product Introduction & Phase-Out | VS-45 |
| W1940 | VMI Promotional Stock Planning & Allocation | VS-45 |
| W1941 | VMI Vendor Performance & Compliance Review | VS-45 |
| W1943 | Consignment Margin Analysis & Vendor Negotiation | VS-45 |
| W1946 | Consignment Agreement Renewal & Terms Negotiation | VS-45 |
| W1947 | VMI-to-Standard Procurement Conversion Decision | VS-45 |
| W1949 | Consignment & VMI Audit Trail & Compliance Documentation | VS-45 |
| W2456 | Vendor Quality Data Aggregation | VS-67 |
| W2458 | Vendor Score Calculation & Weighting | VS-67 |
| W2460 | New Vendor Baseline Performance Establishment | VS-67 |
| W2462 | Monthly Vendor Performance Report | VS-67 |
| W2463 | Quarterly Strategic Vendor Review | VS-67 |
| W2464 | Annual Vendor Tier Classification | VS-67 |
| W2465 | Vendor Performance Improvement Plan (PIP) | VS-67 |
| W2466 | Vendor Delisting Decision & Execution | VS-67 |
| W2467 | Vendor Recognition & Award Program | VS-67 |
| W2469 | Cross-Functional Vendor Feedback Integration | VS-67 |
| W2470 | Vendor Capability Assessment | VS-67 |
| W2471 | Vendor Training & Development Program | VS-67 |
| W2472 | Vendor Technology Enablement | VS-67 |
| W2473 | Joint Business Planning with Strategic Vendors | VS-67 |
| W2474 | Vendor Sustainability Development | VS-67 |
| W2475 | Vendor Financial Health Monitoring | VS-67 |
| W3113 | Cooperative Sourcing Strategy & Category Coverage Planning | VS-94 |
| W3114 | Cooperative & Social Enterprise Identification & Due Diligence | VS-94 |
| W3115 | Cooperative Onboarding, Capability Assessment & Certification | VS-94 |
| W3116 | Cooperative Pricing, Fair-Trade Terms & Contract Negotiation | VS-94 |
| W3117 | Cooperative Capacity Building & Production Planning | VS-94 |
| W3118 | Cooperative Quality Standards & Inspection Setup | VS-94 |
| W3119 | Cooperative Livelihood Program & Government Partnership | VS-94 |
| W3120 | Cooperative Offboarding, Exit & Transition | VS-94 |
| W3121 | Cooperative Demand Aggregation & PO Placement | VS-94 |
| W3122 | Cooperative Production Monitoring & Progress Tracking | VS-94 |
| W3123 | Cooperative Harvest / Production Cycle & Seasonal Calendar Management | VS-94 |
| W3127 | Cooperative Advance Financing & Working Capital Support | VS-94 |
| W3128 | Cooperative Dispute, Short-Shipment & Quality Claim Resolution | VS-94 |
| W3129 | Social Impact Measurement & Beneficiary Tracking | VS-94 |
| W3130 | Fair-Trade Certification & Third-Party Audit | VS-94 |
| W3131 | Cooperative Income & Livelihood Outcome Reporting | VS-94 |
| W3132 | ESG / Sustainability Disclosure & Storytelling Content | VS-94 |
| W3133 | Cooperative Development & Enterprise Graduation Program | VS-94 |
| W3134 | Indigenous Communities & Ancestral Domain (IPRA) Engagement | VS-94 |
| W3135 | Cooperative Risk, Governance & Anti-Exploitation Safeguard | VS-94 |
| W3785 | Global Sourcing Strategy & Import Category Sourcing Plan | VS-122 |
| W3786 | Source-Market & Country Strategy, Geographic Risk Diversification | VS-122 |
| W3787 | Sourcing-Model Decision: Direct vs Sourcing Agent vs Overseas Buying Office | VS-122 |
| W3788 | Total-Landed-Cost Sourcing Framework, Incoterms & Payment-Terms Strategy | VS-122 |
| W3789 | Import Sourcing Make-to-Order, OEM & Private-Label Linkage | VS-122 |
| W3790 | Global Sourcing Risk, Resilience & Alternate-Source Strategy | VS-122 |
| W3791 | Import Sourcing Governance, Authority & Policy | VS-122 |
| W3793 | Sourcing Agent Selection, Contracting & Performance Management | VS-122 |
| W3794 | Overseas Buying Office Strategy, Establishment & Operations | VS-122 |
| W3796 | Import Vendor Negotiation, FOB Pricing & Cost-Reduction Management | VS-122 |
| W3797 | Import Vendor Development, Capacity & Relationship Management | VS-122 |
| W3798 | Source-Side Quality, Social-Compliance & Factory Audit Program | VS-122 |
| W3799 | Import Vendor Portal, EDI & B2B Integration at Source | VS-122 |
| W3804 | Import Sourcing Cycle-Time, Lead-Time & Flow Management | VS-122 |
| W3807 | Total-Landed-Cost Variance, Savings Realization & Margin Linkage | VS-122 |
| W3808 | Global Sourcing Executive Review & Strategic Reporting | VS-122 |
| W3906 | Demand Planning & Statistical Baseline Forecasting | VS-127 |
| W3907 | Demand Consensus Review (Sales/Marketing/Merchandising/Finance) | VS-127 |
| W3908 | New-Product Introduction (NPI) & Phase-In/Phase-Out Forecasting | VS-127 |
| W3910 | Demand Sensing & Short-Cycle Forecast Adjustment | VS-127 |
| W3912 | Constrained Demand Plan & Gap-to-Target Analysis | VS-127 |
| W3913 | Supply Review & Capacity/Constraints Plan | VS-127 |
| W3915 | Sourcing, Import & Lead-Time Constraint Planning | VS-127 |
| W3918 | Rough-Cut Capacity & Financial Constraints Plan | VS-127 |
| W3922 | Merchandise Financial Plan & Open-to-Buy Alignment | VS-127 |
| W3923 | Supply-Chain Design & Network/Inventory Strategy Input | VS-127 |
| W3924 | Working-Capital & Inventory Investment Planning | VS-127 |
| W4001 | Human Rights & Responsible Sourcing Policy, Commitments & Governance | VS-131 |
| W4002 | Salient Human Rights Risk Identification & Materiality Assessment | VS-131 |
| W4003 | Human Rights Due Diligence (HRDD) Framework & Operating Model | VS-131 |
| W4004 | Supply Chain Mapping, Transparency & Traceability Program | VS-131 |
| W4005 | Supplier Code of Conduct, Onboarding & Contractual Safeguards | VS-131 |
| W4007 | Responsible Recruitment, Migrant Labor & Recruitment-Fee Controls | VS-131 |
| W4008 | Conflict-Affected, Indigenous Peoples & Land-Rights Risk Assessment | VS-131 |
| W4009 | Supplier Human Rights Risk Assessment & Tiering | VS-131 |
| W4010 | Social Compliance Audit, Verification & Capability Building | VS-131 |
| W4011 | On-Site Assessment, Worker Voice & Grievance Verification | VS-131 |
| W4013 | Worker Grievance Mechanism & Remediation (Supply-Chain Level) | VS-131 |
| W4014 | Sourcing Decision, Pause & Exit (Responsible Disengagement) Management | VS-131 |
| W4015 | Conflict Minerals, Responsible Materials & Smelter Due Diligence | VS-131 |
| W4017 | Responsible Sourcing Governance, Cross-Functional Steering & Decision Rights | VS-131 |
| W4018 | Supplier Development, Capacity Building & Incentive Program | VS-131 |
| W4021 | Human Rights Stakeholder, NGO & Investor Engagement | VS-131 |
| W4022 | Own-Operations Human Rights, DEI & Worker-Voice Integration | VS-131 |
| W4023 | Human Rights Training, Capability & Culture Program | VS-131 |
| W5489 | Typhoon & Calamity Demand-Surge Forecasting and Pre-Positioning | VS-127 |
| W5490 | Ber-Months (September–December) Seasonal Ramp Planning | VS-127 |
| W5491 | Summer Season (Aircon, Garden & Dry-Season Construction) Planning | VS-127 |
| W5492 | Inter-Island Inventory Rebalancing and Allocation Under Disruption | VS-127 |
| W5493 | B2B / Trade-Project Demand Induction into the Consensus Plan | VS-127 |

**Make & Move** (199)

| ID | Workflow | Value Stream |
|---|---|---|
| W1167 | Reverse Logistics & Vendor Return Shipment Management | VS-6 |
| W1168 | Direct Store Delivery (DSD) Receiving, Verification & Vendor Compliance | VS-6 |
| W1189 | Cement & Bagged Material Shelf Life Expiry Monitoring & Proactive Markdown | VS-5 |
| W1191 | Construction Site Delivery Coordination, Access Assessment & Crane/Boom Truck Scheduling | VS-6 |
| W1207 | Third-Party Logistics (3PL) Provider Quarterly Performance Review & Contract Renewal | VS-6 |
| W1222 | DC Hazardous Material Storage Compliance & Inspection Program | VS-4 |
| W1226 | DC Cross-Dock Operations for Fast-Moving Items & Direct-to-Truck Fulfillment | VS-4 |
| W1241 | DC Labor Shift Scheduling, Overtime Management & Cross-Training Coordination | VS-4 |
| W1257 | Seasonal Inventory Pre-Positioning, Forward-Buy Execution & Phase-Out Calendar Management | VS-5 |
| W1280 | Vendor Return-to-Vendor (RTV) Defective & Excess Merchandise Processing | VS-5 |
| W1348 | Fleet Vehicle Preventive Maintenance Scheduling, Work Order & Parts Management | VS-6 |
| W1349 | Fleet Tire Lifecycle Management, Tread Monitoring & Replacement Scheduling | VS-6 |
| W1366 | DC Inbound Damage Claim Processing, Vendor Chargeback & Freight Recovery Management | VS-4 |
| W1371 | 3PL Carrier Onboarding, Qualification Audit & Service Level Agreement Management | VS-6 |
| W1415 | New Store Pre-Opening Merchandise Loading, DC Allocation & Initial Stock Build Execution | VS-4 |
| W1428 | DC Seasonal Surge Temporary Staffing, Onboarding & Season-End Separation Processing | VS-4 |
| W1437 | Store-Level Building Material Damaged Package Reconditioning & Resaleable Recovery Processing | VS-5 |
| W1438 | Seasonal SKU End-of-Life Transition, Markdown Cadence & Remaining Stock Balancing Across Stores | VS-5 |
| W1486 | Lumber Yard Inventory Measurement, Board Foot Calculation & Dimensional Grading Verification | VS-5 |
| W1488 | Customer Bulk Sand, Gravel & Cement Delivery Scheduling, Weight Ticket Verification & Site Unloading Coordination | VS-6 |
| W1498 | DC Temperature-Sensitive Material (Adhesives, Sealants, Paint) Storage Monitoring, Expiry Alert & FIFO Enforcement | VS-4 |
| W1515 | Delivery Vehicle Fuel Card Management, Consumption Tracking & Cost Control | VS-6 |
| W1622 | In-Store Customer Return Processing | VS-32 |
| W1623 | Ecommerce Customer Return Initiation & Authorization | VS-32 |
| W1624 | Customer Exchange Processing | VS-32 |
| W1626 | Customer Return Quality Assessment & Disposition | VS-32 |
| W1629 | B2B Trade Account Return & Credit Note Processing | VS-32 |
| W1630 | Customer Warranty Claim Processing & Vendor Claim Initiation | VS-32 |
| W1633 | Vendor Defective Product Investigation & Root Cause Analysis | VS-32 |
| W1635 | Vendor Seasonal/Promotional Return Processing | VS-32 |
| W1637 | Vendor Shipping Error & Wrong Item Return Processing | VS-32 |
| W1639 | Returns Processing Center Operations | VS-32 |
| W1640 | Refurbishment & Repackaging Operations | VS-32 |
| W1641 | Returns Disposition Decision Engine & Automation | VS-32 |
| W1642 | Returned Product Liquidation & Channel Management | VS-32 |
| W1643 | Reverse Logistics Carrier & Cost Management | VS-32 |
| W2190 | Delivery Partner Identification & Screening | VS-56 |
| W2191 | 3PL System Integration & Onboarding | VS-56 |
| W2192 | Driver & Vehicle Compliance Verification | VS-56 |
| W2193 | 3PL Rate Card Negotiation & Renewal | VS-56 |
| W2194 | 3PL Insurance & Liability Management | VS-56 |
| W2195 | 3PL Capacity Planning & Allocation | VS-56 |
| W2197 | 3PL Contract Termination & Transition | VS-56 |
| W2198 | Real-Time Delivery Tracking & Monitoring | VS-56 |
| W2199 | SLA Compliance Monitoring | VS-56 |
| W2202 | Proof of Delivery & Documentation | VS-56 |
| W2203 | Delivery Exception Management | VS-56 |
| W2205 | Seasonal Delivery Surge Management | VS-56 |
| W2207 | Per-Delivery Cost Analysis | VS-56 |
| W2210 | 3PL Fuel Surcharge Management | VS-56 |
| W2211 | Delivery Cost Allocation by Category | VS-56 |
| W2212 | 3PL Payment Terms Management | VS-56 |
| W2310 | Fleet Fuel Card Program Management | VS-61 |
| W2312 | Vehicle Fuel Efficiency Monitoring | VS-61 |
| W2314 | Driver Fuel Efficiency Training | VS-61 |
| W2315 | Alternative Fuel Vehicle Evaluation | VS-61 |
| W2316 | Fuel Cost Pass-Through to 3PL | VS-61 |
| W2317 | Emergency Fuel Supply Management | VS-61 |
| W2319 | RFID Fleet Toll Account Management | VS-61 |
| W2320 | Parking & Loading Dock Fee Management | VS-61 |
| W2322 | Backhaul Utilization & Revenue | VS-61 |
| W2323 | Fleet Insurance Cost Management | VS-61 |
| W2324 | Vehicle Maintenance Cost Tracking | VS-61 |
| W2326 | Annual Fleet TCO Analysis | VS-61 |
| W2327 | Vehicle Replacement Cost-Benefit Analysis | VS-61 |
| W2328 | Fleet Utilization Rate Analysis | VS-61 |
| W2329 | Fleet Carbon Footprint Estimation | VS-61 |
| W2330 | Fleet Safety Cost Analysis | VS-61 |
| W2332 | Logistics Cost as % of Revenue | VS-61 |
| W2333 | 5-Year Fleet Investment Plan | VS-61 |
| W2803 | Mid-Day Cash Skim & Cash Drawer Threshold Management | VS-81 |
| W2804 | CIT Pickup Schedule Planning & Store Request Management | VS-81 |
| W2805 | Change Order (Coin/Small Bill) Forecast & Request Workflow | VS-81 |
| W2806 | Counterfeit Detection, Note Authentication & Suspect Handling | VS-81 |
| W2808 | Foreign Currency & Mutilated/Soiled Note Handling | VS-81 |
| W2810 | Pickup Execution, Guard Verification & Handover Protocol | VS-81 |
| W2815 | Cash Recirculation & Cross-Store Float Rebalancing | VS-81 |
| W2816 | CIT Vendor Performance, SLA & Cost Management | VS-81 |
| W2817 | CIT Insurance Program, Coverage Limits & Claims Management | VS-81 |
| W2819 | Cash Loss Event Investigation, LP Correlation & Write-Off | VS-81 |
| W2821 | Tender Mix Shift Strategy & Cash Reduction Program | VS-81 |
| W3017 | Inbound Receiving Damage & Shortage Identification & Documentation | VS-90 |
| W3018 | In-Transit & DC Damage Identification, Quarantine & Classification | VS-90 |
| W3019 | Store-Level Damaged-on-Arrival (DOA) & In-Store Damage Reporting | VS-90 |
| W3020 | Damage Documentation, Photographic Evidence & ERP Capture | VS-90 |
| W3021 | Damage Disposition Decision (Scrap / Return-to-Vendor / Salvage / Recondition) | VS-90 |
| W3023 | Hazardous / Regulated Damaged Goods Handling & Disposal | VS-90 |
| W3025 | Vendor Shortage, Damage & Non-Conformance Claim Filing | VS-90 |
| W3026 | Freight Carrier / 3PL Damage & Shortage Claim Filing | VS-90 |
| W3028 | Claim Evidence Package, Liability Determination & Valuation | VS-90 |
| W3030 | Subrogation, Insurance Recovery & Dual-Claim Coordination | VS-90 |
| W3031 | Claim Denial Dispute, Escalation & Legal Handoff | VS-90 |
| W3033 | Customer Delivery Damage & Shortage Claim Intake | VS-90 |
| W3034 | B2B / Trade Delivery Damage Claim Investigation & Resolution | VS-90 |
| W3035 | Customer Goodwill & Damage Replacement Authorization | VS-90 |
| W3037 | Third-Party Delivery Partner (Lalamove / Transportify) Damage Recovery | VS-90 |
| W3038 | Damage Claims Subrogation to Vendor / Carrier | VS-90 |
| W3040 | Damage Cost Allocation, Vendor Recovery Rate & Margin Impact Analysis | VS-90 |
| W3065 | Kit & Bundle Product Strategy, Definition & Lifecycle | VS-92 |
| W3066 | Kit Bill of Materials (BOM), Component Mapping & Yield Definition | VS-92 |
| W3067 | Bundle Pricing, Margin Validation & Component Cost Roll-Up | VS-92 |
| W3068 | Kit/Bundle Master Data, SKU Setup & Configuration | VS-92 |
| W3069 | Component Availability, Allocation & Build Feasibility Planning | VS-92 |
| W3070 | Seasonal & Promotional Kit Planning & Phase-In | VS-92 |
| W3071 | Private-Label & Co-Branded Kit Development Coordination | VS-92 |
| W3072 | Kit/Bundle Discontinuation, Liquidation & Component Recovery | VS-92 |
| W3073 | Centralized Kit Build (DC) Work Order & Assembly Execution | VS-92 |
| W3074 | Store-Level Kit Build, Display Assembly & Light Value-Add | VS-92 |
| W3075 | Component Picking, Kit Quality Check & Build Verification | VS-92 |
| W3076 | Kit Lot/Serial Tracking, Expiry & Traceability | VS-92 |
| W3078 | Kit Disassembly (Tear-Down) & Component Return-to-Stock | VS-92 |
| W3079 | Outsourced / 3PL Kit Assembly & Co-Manufacturing Management | VS-92 |
| W3080 | Build Capacity, Labor & Throughput Planning | VS-92 |
| W3082 | Dynamic Bundle Pricing, Quantity Break & Tier Execution | VS-92 |
| W3083 | Vendor-Funded Bundle Allowance & Co-Op Recovery | VS-92 |
| W3085 | Bundle Margin Analysis, Component Contribution & Profitability | VS-92 |
| W3089 | Dark Store Network Strategy & Market Catchment Analysis | VS-93 |
| W3090 | Dark Store Site Selection, Lease & Build-Out | VS-93 |
| W3091 | Dark Store Layout Design, Fixture & Automation Configuration | VS-93 |
| W3092 | Dark Store System Integration, WMS & Robotics Commissioning | VS-93 |
| W3093 | Dark Store Staffing Model, Recruitment & Training | VS-93 |
| W3094 | Dark Store Go-Live, Pilot & Ramp-Up | VS-93 |
| W3095 | Dark Store Capacity Planning & Expansion Triggers | VS-93 |
| W3097 | Dark Store Order Wave Planning & Batch Release | VS-93 |
| W3102 | Same-Day / Next-Day Delivery Cut-Off & SLA Management | VS-93 |
| W3106 | Dark Store Slotting, Velocity Analysis & Re-Slotting | VS-93 |
| W3108 | Dark Store Order Cycle Time, Cut-Off Adherence & SLA Reporting | VS-93 |
| W3110 | Dark Store Demand Sensing & Dynamic SKU Ranging | VS-93 |
| W3497 | Freight Category Strategy & Spend Baseline | VS-110 |
| W3498 | Carrier & 3PL Sourcing, RFQ & Qualification | VS-110 |
| W3499 | Carrier Contracting, Rate Negotiation & Tariff Structures | VS-110 |
| W3500 | Routing Guide, Carrier Compliance & Lane Assignment | VS-110 |
| W3501 | Freight Tendering, Spot Quote & Capacity Booking | VS-110 |
| W3502 | Inbound Freight Management & Vendor Routing Compliance | VS-110 |
| W3503 | Import Ocean Freight, Forwarder & NVOCC Management | VS-110 |
| W3504 | Carrier Onboarding, Insurance & Regulatory Compliance | VS-110 |
| W3506 | Last-Mile & Customer Delivery Freight Management | VS-110 |
| W3508 | Freight Tracking, Visibility & Exception Management | VS-110 |
| W3509 | Demurrage, Detention & Accessorial Charge Management | VS-110 |
| W3510 | Inter-Island / Inter-Region Freight Coordination | VS-110 |
| W3511 | Freight Claims, Loss & Damage Recovery | VS-110 |
| W3513 | Freight Invoice Audit & Match | VS-110 |
| W3514 | Freight Payment, Allocation & Chargeback to Entities | VS-110 |
| W3517 | Freight Budget, Forecast & Variance Management | VS-110 |
| W3519 | Fuel Surcharge, Index Management & Freight Rate Volatility | VS-110 |
| W3521 | Packaging Strategy, Standards & Governance | VS-111 |
| W3522 | Product Packaging Engineering & Specification | VS-111 |
| W3523 | Transport & Protective Packaging Design | VS-111 |
| W3524 | Packaging Material Procurement & Supplier Management | VS-111 |
| W3525 | Private-Label & Vendor Packaging Compliance | VS-111 |
| W3526 | Sustainable Packaging & EPR / Extended Producer Responsibility | VS-111 |
| W3527 | Packaging Labeling, Hazmat & Regulatory Compliance | VS-111 |
| W3529 | Pallet & RTI Pool Strategy | VS-111 |
| W3530 | Pallet Procurement, Issuance & Inventory Management | VS-111 |
| W3532 | Pallet / RTI Deposit, Transfer & Customer / Carrier Exchange | VS-111 |
| W3533 | Pallet / RTI Loss, Damage & Write-Off Management | VS-111 |
| W3534 | Inbound Vendor Pallet / RTI Compliance & Chargeback | VS-111 |
| W3535 | Pallet / RTI Reverse Logistics & Retrieval | VS-111 |
| W3538 | Recyclable / Biodegradable Material Transition Program | VS-111 |
| W3543 | Single-Use Plastic Reduction & Bag Policy Compliance | VS-111 |
| W4121 | Supply Chain Network Strategy & Design Principles | VS-136 |
| W4124 | Store Coverage, Territory & Service-Area Assignment | VS-136 |
| W4125 | Inbound Flow, Sourcing Lane & Port-of-Entry Design | VS-136 |
| W4127 | Network Resilience, Redundancy & Risk-Adjusted Design | VS-136 |
| W4128 | Network Design Business Case & Investment Planning | VS-136 |
| W4129 | Inventory Strategy, Postponement & Pooling Policy | VS-136 |
| W4133 | Seasonal & Promotional Inventory Buffer Planning | VS-136 |
| W4135 | Inventory Parameter Governance & Master Data | VS-136 |
| W4289 | Bulky & White-Goods Delivery Program Strategy, Channel Scope & Operating Model | VS-143 |
| W4290 | Bulky Delivery Network, Capacity & Crew Sizing | VS-143 |
| W4291 | Customer Delivery Scheduling, Time-Window & Routing Management | VS-143 |
| W4292 | Bulky Item Order Capture, Eligibility & Pre-Delivery Verification | VS-143 |
| W4293 | Two-Man Crew, Driver & Installer Authorization, Training & Certification | VS-143 |
| W4294 | Delivery Vehicle, Equipment & Lift-Gate Fleet Provisioning | VS-143 |
| W4295 | Bulky Delivery Pricing, Fee & Zone Structure | VS-143 |
| W4299 | Appliance & White-Goods Installation, Hookup & Commissioning | VS-143 |
| W4300 | Installation Quality, Damage/Defect-on-Delivery & Field Resolution | VS-143 |
| W4301 | Customer Acceptance, e-POD, Warranty Registration & Satisfaction Capture | VS-143 |
| W4302 | Failed/Rescheduled Delivery, Redelivery & Customer-Not-At-Home Handling | VS-143 |
| W4303 | Subcontracted/3PL Bulky Delivery Partner Operations & SLA | VS-143 |
| W4305 | Old-Appliance Haul-Away Policy, Eligibility & Customer Consent | VS-143 |
| W4307 | E-Waste, Scrap Metal & Appliance Recycling/Disposition | VS-143 |
| W4309 | Recycling Compliance, EPR (RA 11898) & Documentary Trail | VS-143 |
| W4311 | Bulky Reverse-Logistics Asset Recovery, Refurb/Open-Box & Liquidation | VS-143 |
| W5467 | Electric & Alternative-Fuel Vehicle Procurement, OEM Vendor Selection & Homologation | VS-192 |
| W5468 | Depot / DC Charging & Alt-Fuel Infrastructure Planning, Siting & Grid Coordination | VS-192 |
| W5469 | Green Fleet Total Cost of Ownership (TCO), Lifecycle & Capital Investment Analysis | VS-192 |
| W5470 | RA 11697 (EVIDA) Incentives, EV Registration, Toll/Lane Exemption & Compliance Management | VS-192 |
| W5471 | Green Fleet Capital Governance, Financing & Board Investment Approval | VS-192 |
| W5472 | Delivery Network & Route Re-Design for EV Range, Charging & Payload Constraints | VS-192 |
| W5473 | EV Fleet Daily Charging Operations, Load Scheduling & Smart-Charge Management | VS-192 |
| W5474 | Depot Charging Station Operations, Maintenance & Uptime Management | VS-192 |
| W5475 | EV Battery State-of-Health, Range Assurance & Battery Lifecycle Management | VS-192 |
| W5478 | Alternative-Fuel (Biodiesel/B20, LNG, Hybrid) Operations & Fuel Quality Management | VS-192 |
| W5479 | Charging–Renewable Integration, Demand Response & On-Site Solar Load Matching | VS-192 |
| W5480 | EV-Specific Preventive Maintenance, Diagnostics, Roadside & Towing Operations | VS-192 |
| W5484 | Green Fleet Driver & Technician Training, Certification & Behavior Incentive Program | VS-192 |
| W5486 | EV Charging Billing, Electricity Cost Allocation, Reimbursement & Home-Charge Policy | VS-192 |
| W5487 | EV Battery Second-Life, End-of-Life Recycling & RA 11898 EPR Linkage | VS-192 |

**Sell & Serve** (459)

| ID | Workflow | Value Stream |
|---|---|---|
| W1171 | Installation Defect Punch List, Customer Walk-Through & Quality Sign-Off | VS-12 |
| W1172 | Tool Rental Fleet Procurement, Lifecycle Planning & Retirement Management | VS-12 |
| W1179 | Store-Level Gift Card Sales, Redemption & Balance Management | VS-9 |
| W1185 | Post-Purchase Review Solicitation, Loyalty Review Incentives & Fake-Review Detection | VS-10 |
| W1186 | Loyalty Program Partner Cross-Promotion & Third-Party Reward Integration | VS-13 |
| W1192 | Post-Typhoon Store Damage Assessment, Insurance Claim & Rapid Reopening Protocol | VS-7 |
| W1193 | Heavy & Bulky Material Customer Pickup Scheduling & Loading Bay Priority Management | VS-7 |
| W1195 | Mixed-Basket Multi-Origin Order Orchestration & Split Shipment Coordination | VS-10 |
| W1197 | Government Agency & LGU Annual Procurement Catalog Listing & Price Registration | VS-11 |
| W1198 | Installation Material Kit Pre-Stage, Quality Check & Site-Ready Packing | VS-12 |
| W1209 | E-Commerce Mega-Sale Event Preparation & Execution (Lazada/Shopee 9.9, 11.11, 12.12) | VS-10 |
| W1210 | Customer In-Home Site Measurement, Assessment & Quotation for Installation Services | VS-12 |
| W1217 | Loyalty Program Tier Annual Review, Downgrade Notification & Win-Back Processing | VS-13 |
| W1225 | Government Infrastructure Project Supply Bid, Pricing & Award Fulfillment | VS-11 |
| W1227 | Store-Level Customer Kitchen & Bathroom Complete Renovation Material Calculator & Project Quote | VS-9 |
| W1229 | Customer Power Tool & Appliance Product Registration & Extended Warranty Processing | VS-13 |
| W1232 | Customer In-Store Paint Color Archival, Historic Color Retrieval & Match-from-Sample Service | VS-9 |
| W1234 | Customer E-Commerce Same-Day & Next-Day Express Delivery Fulfillment | VS-10 |
| W1235 | Store-Level Customer Financing Partner Kiosk Management & Application Processing | VS-8 |
| W1238 | Customer Building Plan Review, Material Take-Off & Professional Estimation Service | VS-9 |
| W1239 | Store-Level Power Tool Live Demo, Safety Briefing & Customer Engagement Event | VS-9 |
| W1242 | E-Commerce B2B Corporate Punchout Catalog & Procurement Integration | VS-10 |
| W1243 | Store-Level Customer Lumber Grading Verification, Quality Dispute & Claims Processing | VS-7 |
| W1246 | Store-Level Customer Roofing & Structural Material Load Calculation & Estimation Service | VS-9 |
| W1254 | Customer Project Digital Completion Certificate & Post-Installation Warranty Registration | VS-12 |
| W1259 | Trade Professional Community Building, Retention Program & Contractor Loyalty Management | VS-14 |
| W1260 | In-Store DIY Workshop & Community Event Calendar Management | VS-14 |
| W1263 | Government & Institutional Emergency Procurement Rapid Response & Relief Supply Fulfillment | VS-11 |
| W1269 | Customer Trade Account Application, Credit Assessment & Onboarding | VS-11 |
| W1270 | Seasonal Promotional Catalog Production, Printing & Store Distribution | VS-14 |
| W1272 | Store-Level Emergency Local Cash Purchase Authorization & Reimbursement | VS-7 |
| W1273 | Customer E-Commerce In-Store Return Drop-Off Processing & Cross-Channel Refund | VS-10 |
| W1274 | Customer Loyalty Points Financial Liability Monthly Valuation & Accounting Reserve | VS-13 |
| W1281 | Lumber Yard Daily Operations & Inventory Management | VS-7 |
| W1283 | Cement & Building Material Vendor Direct Store Delivery (DSD) Coordination | VS-7 |
| W1284 | Customer Bulk Material Quantity Takeoff & Quotation Service | VS-9 |
| W1285 | Customer Tile & Flooring Sample Loan Program | VS-9 |
| W1286 | Ecommerce UGC Moderation Playbook, Content Seeding & Product Q&A Management | VS-10 |
| W1287 | Customer Ecommerce Product Availability Notification & Back-in-Stock Alert | VS-10 |
| W1289 | Store-Level Tool Demonstration & Product Launch Event Coordination | VS-12 |
| W1290 | Store-Level Appliance Warranty Registration & After-Sales Service Coordination | VS-13 |
| W1291 | Customer Loyalty Tier Upgrade & Benefits Personalization | VS-13 |
| W1292 | Seasonal Builder's Expo & Community Event Planning | VS-14 |
| W1297 | Store-Level Perimeter Security & Parking Lot Safety Management | VS-7 |
| W1302 | Typhoon Season Store Protection, Rapid Reopening & Post-Disaster Assessment Protocol | VS-7 |
| W1308 | B2B Project Bid, Tender Response & Government Procurement Compliance Management | VS-11 |
| W1311 | Negative-Review Quality-Pattern Escalation, Seller Response Governance & Positive-Review Amplification | VS-10 |
| W1314 | Customer Project Material List (Bill of Materials) Creation, Management & Reorder Tracking | VS-9 |
| W1316 | Loyalty Points Liability Accounting, Redemption Forecasting & Program Financial Management | VS-13 |
| W1317 | Store-Level Generator Backup Power Operations, Fuel Management & Load Shedding Protocol | VS-7 |
| W1318 | Tool Rental Reservation, Waitlist & Scheduling | VS-12 |
| W1319 | Tool Rental Customer Safety Briefing, Liability Waiver & Equipment Operation Acknowledgment | VS-12 |
| W1360 | Omnichannel Inventory Reservation, Oversell Prevention & Multi-Channel Stock Allocation Governance | VS-10 |
| W1363 | Trade Professional VIP Priority Support Hotline & Dedicated Account Manager Escalation | VS-13 |
| W1364 | Customer Product Knowledge Base & DIY Self-Service Help Center Content Management | VS-13 |
| W1375 | Tool Rental Overdue Return Escalation, Recovery & Penalty Processing | VS-12 |
| W1377 | DIY Workshop Instructor Recruitment, Certification & Training Content Management | VS-12 |
| W1378 | Customer DIY Workshop Registration, Waitlist Management & Attendance Tracking | VS-12 |
| W1394 | Customer Trade Account Annual Credit Review, Tier Reclassification & Terms Adjustment | VS-11 |
| W1395 | Customer Trade Account Suspension, Reactivation & Delinquent Account Rehabilitation | VS-11 |
| W1407 | Store Seasonal Department Reset, Category Space Reallocation & New Product Introduction Floor Execution | VS-7 |
| W1430 | Paint Tinting Color Formula Master Management, New Vendor Color Onboarding & Seasonal Formula Library Update | VS-9 |
| W1443 | Trade Professional WhatsApp Commerce Integration, Contractor Group Management & Digital Engagement | VS-14 |
| W1463 | TikTok Shop Integration, Content-to-Commerce & Livestream Selling Operations | VS-10 |
| W1464 | Marketplace Product Listing Syndication, Pricing Synchronization & Catalog Governance | VS-10 |
| W1469 | Facebook Marketplace & Community Group Selling Operations, Order Capture & Fulfillment | VS-10 |
| W1490 | Store-Level Plumbing & Electrical Fixture Display Model Rotation, Demo Unit Tracking & Write-Off | VS-7 |
| W1499 | Customer Loyalty Program Tier Qualification Period Reset, Points Expiration Management & Downgrade Communication | VS-13 |
| W1502 | Customer E-Commerce Product Comparison Tool, Alternate/Substitute Product Recommendation & Cross-Sell Engine | VS-10 |
| W1505 | Store-Level Typhoon & Natural Disaster Preparation, Response & Business Recovery | VS-7 |
| W1507 | Customer Trade Account Mobile QR-Onboarding & Instant Activation | VS-11 |
| W1508 | Customer Project Financing & Partner Bank Consumer Loan Coordination | VS-11 |
| W1509 | Customer Bulk Construction Material Direct-to-Jobsite Delivery Order Management | VS-11 |
| W1510 | Customer Digital Home Project Planner, Materials Calculator & Shopping List | VS-10 |
| W1511 | Store-Level Community Engagement, Barangay Relations & Local Partnership Management | VS-7 |
| W1512 | Omnichannel Customer Unified Profile, Identity Resolution & Cross-Channel Activity Merge | VS-10 |
| W1517 | Customer Structural Steel & Rebar Estimation, Span Calculation & Engineering Advisory Service | VS-9 |
| W1519 | Plumbing Fixture & Water System Installation Service Management | VS-12 |
| W1520 | Customer Tile & Flooring Installation Service Measurement, Layout Planning & Waste Factor Management | VS-12 |
| W1521 | Customer Verified Contractor & Installer Referral Directory Management | VS-13 |
| W1522 | Monthly Flyer & Promotional Catalog Production, Print Run & In-Store Distribution | VS-14 |
| W1523 | New Store Grand Opening Marketing Campaign, Local Launch Event & Community Introduction | VS-14 |
| W1537 | Store-Level Parking Lot & Exterior Area Daily Operations, Customer Vehicle Flow & Security Management | VS-7 |
| W1548 | Ecommerce Customer Product Bundle Builder & Custom Project Kit Assembly Order Processing | VS-10 |
| W1549 | Contractor Annual Spend Tier Review, Loyalty Tier Recalculation & Benefit Adjustment | VS-11 |
| W1551 | Local Store Marketing Campaign Execution, Barangay-Level Outreach & Community Event Partnership | VS-14 |
| W1553 | Tool Rental Fleet Seasonal Demand Management, Cross-Store Fleet Rebalancing & Capital Replacement Planning | VS-12 |
| W1554 | Power Tool Rental Preventive Maintenance, Wear Parts Replacement & Servicing Vendor Coordination | VS-12 |
| W1555 | Tool Rental Customer Damage Assessment, Repair Cost Recovery & Dispute Resolution | VS-12 |
| W1556 | Youth & Student Skilled Trade Exposure Program, TESDA Partnership & School Career Day Participation | VS-12 |
| W1557 | Seasonal DIY Workshop Series Planning, Content Development & Customer Conversion Funnel Management | VS-12 |
| W1559 | Localized Geo-Targeted Digital Advertising for Store-Level Promotions & Event Traffic Driving | VS-14 |
| W1560 | Customer Review & User-Generated Content Management, Online Reputation Monitoring & Response | VS-14 |
| W1737 | New Store Project Charter & Kickoff | VS-37 |
| W1738 | Store Layout Design & Planogram Planning | VS-37 |
| W1740 | Store Equipment & Fixture Procurement | VS-37 |
| W1741 | IT Infrastructure & Systems Setup Planning | VS-37 |
| W1742 | Permit & License Acquisition for New Store | VS-37 |
| W1743 | Vendor & Supplier Notification for New Store | VS-37 |
| W1744 | Pre-Opening Timeline & Critical Path Management | VS-37 |
| W1745 | New Store Budget Tracking & Variance Management | VS-37 |
| W1746 | Store Manager Selection & Appointment | VS-37 |
| W1747 | Store Staff Recruitment & Hiring | VS-37 |
| W1748 | New Store Staff Onboarding & Orientation | VS-37 |
| W1749 | POS & Systems Training for New Store Staff | VS-37 |
| W1750 | Product Knowledge & Category Training | VS-37 |
| W1751 | Safety & Compliance Training for New Store | VS-37 |
| W1752 | Store System Configuration & Go-Live Verification | VS-37 |
| W1753 | Soft Opening Operations & Dry Run | VS-37 |
| W1754 | Store Cash Float & Financial Setup | VS-37 |
| W1755 | Grand Opening Event Planning & Execution | VS-37 |
| W1756 | Grand Opening Day Operations Management | VS-37 |
| W1757 | Opening Week Performance Monitoring | VS-37 |
| W1758 | Post-Opening Inventory Rebalancing | VS-37 |
| W1759 | First Month Performance Review & Stabilization | VS-37 |
| W1760 | Store Handover from Project to Operations | VS-37 |
| W1761 | Post-Opening Issue Resolution & Punch List Closure | VS-37 |
| W1904 | Customer Effort Score (CES) Measurement for Key Service Touchpoints | VS-44 |
| W1907 | Customer Complaint Root Cause Analysis & Voice of Customer (VOC) Integration | VS-44 |
| W1908 | Mystery Shopping Program Execution & Compliance Scoring | VS-44 |
| W1911 | Philippine Home Improvement Market Size & Growth Tracking | VS-44 |
| W1914 | Industry Trend & Macro-Economic Impact Analysis | VS-44 |
| W1915 | Trade Area Demographic Analysis & Store Location Market Sizing | VS-44 |
| W1916 | Supplier Market Intelligence & Raw Material Price Trend Monitoring | VS-44 |
| W1917 | Competitive Intelligence Report & Strategic Decision Support | VS-44 |
| W1918 | Category Shopper Behavior Analysis & Purchase Path Research | VS-44 |
| W1919 | New Category Viability Study & Consumer Demand Assessment | VS-44 |
| W1920 | Price Sensitivity & Elasticity Research by Category | VS-44 |
| W1921 | Seasonal Demand Pattern Analysis & Forecast Calibration | VS-44 |
| W1922 | DIY vs. Trade Professional Shopper Segment Research | VS-44 |
| W1924 | Store Layout & Category Adjacency Effectiveness Research | VS-44 |
| W1925 | Consumer Trend & Emerging Product Category Monitoring | VS-44 |
| W1950 | PHILGEPS Registration & Renewal Management | VS-46 |
| W1951 | Government Entity Account Creation & Credit Assessment | VS-46 |
| W1952 | LGU & Government Agency Relationship Development | VS-46 |
| W1953 | Government Procurement Calendar Monitoring & Opportunity Identification | VS-46 |
| W1955 | Government Procurement Training & Staff Certification | VS-46 |
| W1956 | Institutional & NGO Account Qualification & Onboarding | VS-46 |
| W1958 | Government Competitive Bidding Preparation & Submission | VS-46 |
| W1959 | Government Shopping & Small Value Procurement Quotation | VS-46 |
| W1960 | Government Negotiated Procurement & Emergency Purchase Processing | VS-46 |
| W1962 | Government Project Delivery & Site Coordination | VS-46 |
| W1964 | Government Bid Protest & Dispute Resolution | VS-46 |
| W1965 | Government Catalog & Price List Maintenance | VS-46 |
| W1969 | Government Year-End Liquidation & Reporting | VS-46 |
| W1972 | Government Sales Tax Compliance & Reporting | VS-46 |
| W1973 | Government Account Aging & Bad Debt Provision | VS-46 |
| W1974 | Subscription Service Product Definition & Pricing | VS-47 |
| W1975 | Service Partner Qualification & Onboarding | VS-47 |
| W1978 | Subscription Revenue Model & Deferred Revenue Configuration | VS-47 |
| W1979 | Service Territory & Coverage Mapping | VS-47 |
| W1980 | Subscription Pilot Program Execution & Evaluation | VS-47 |
| W1981 | Subscription Product Launch & Go-to-Market | VS-47 |
| W1982 | Subscription Monthly Billing & Payment Processing | VS-47 |
| W1983 | Subscription Annual Renewal & Upsell Processing | VS-47 |
| W1985 | Subscription Upgrade & Tier Change Processing | VS-47 |
| W1987 | Subscription Pause & Reactivation Processing | VS-47 |
| W1988 | Subscription Gift & Transfer Processing | VS-47 |
| W1989 | Subscription Customer Communication & Notification Management | VS-47 |
| W1991 | Service Visit Execution & Customer Interaction | VS-47 |
| W1992 | Service Completion Confirmation & Revenue Recognition Trigger | VS-47 |
| W1994 | Service Complaint & Revisit Management | VS-47 |
| W1996 | Service Visit No-Show & Rescheduling Management | VS-47 |
| W2000 | In-Store Advertising Placement Setup & Maintenance | VS-48 |
| W2001 | Ecommerce Sponsored Product & Banner Ad Position Management | VS-48 |
| W2003 | Digital Signage Content Management & Scheduling | VS-48 |
| W2006 | Vendor Media Campaign Briefing & Creative Development | VS-48 |
| W2007 | Multi-Channel Campaign Orchestration & Launch | VS-48 |
| W2008 | In-Store Campaign Compliance Monitoring & Photo Verification | VS-48 |
| W2010 | Vendor Co-Op Advertising Fund Integration | VS-48 |
| W2012 | Seasonal Media Package Development & Sales | VS-48 |
| W2119 | Online Purchase Warranty Registration | VS-53 |
| W2120 | Bulk Warranty Registration for Trade Accounts | VS-53 |
| W2121 | Warranty Transfer for Resold Properties | VS-53 |
| W2122 | Warranty Master Data Configuration | VS-53 |
| W2123 | Warranty Data Quality Audit | VS-53 |
| W2124 | Warranty Digital Wallet & Customer Portal | VS-53 |
| W2126 | In-Store Warranty Claim Initiation | VS-53 |
| W2127 | Online Warranty Claim Submission | VS-53 |
| W2128 | Vendor Warranty Claim Escalation | VS-53 |
| W2129 | Service Center Repair Coordination | VS-53 |
| W2130 | Warranty Replacement Fulfillment | VS-53 |
| W2132 | Warranty Claim Dispute Resolution | VS-53 |
| W2134 | Extended Warranty Product Design & Pricing | VS-53 |
| W2136 | Extended Warranty Contract Management | VS-53 |
| W2137 | Extended Warranty Claim Processing | VS-53 |
| W2138 | Extended Warranty Renewal & Extension | VS-53 |
| W2139 | Extended Warranty Cancellation & Refund | VS-53 |
| W2140 | Performance Guarantee Management | VS-53 |
| W2141 | Warranty Partner & Insurer Management | VS-53 |
| W2286 | Order Source Selection Engine | VS-60 |
| W2287 | Mixed-Basket Order Splitting | VS-60 |
| W2290 | Inventory Reservation & Allocation | VS-60 |
| W2292 | Fulfillment Priority & SLA Management | VS-60 |
| W2294 | Multi-Source Fulfillment Coordination | VS-60 |
| W2296 | Split Order Customer Communication | VS-60 |
| W2297 | Partial Order Cancellation & Modification | VS-60 |
| W2298 | Backorder Management in Split Orders | VS-60 |
| W2299 | Cross-Entity Fulfillment Coordination | VS-60 |
| W2301 | Same-Day & Express Fulfillment | VS-60 |
| W2303 | Source Performance Comparison | VS-60 |
| W2305 | Customer Delivery Experience Analysis | VS-60 |
| W2306 | Omnichannel Inventory Visibility Monitoring | VS-60 |
| W2307 | Fulfillment Capacity Planning | VS-60 |
| W2308 | Return Rate by Fulfillment Source | VS-60 |
| W2309 | Omnichannel Fulfillment Strategy Annual Review | VS-60 |
| W2334 | Tile & Flooring Sample Procurement | VS-62 |
| W2335 | Paint Color Card & Swatch Management | VS-62 |
| W2336 | Countertop & Surface Material Sample Distribution | VS-62 |
| W2338 | Sample Vendor Negotiation & Cost Management | VS-62 |
| W2340 | Sample-to-Order Conversion Process | VS-62 |
| W2341 | Seasonal Sample Refresh Execution | VS-62 |
| W2342 | Monthly Display Condition Inspection | VS-62 |
| W2343 | Damaged Sample Replacement Process | VS-62 |
| W2344 | Sample Display Area Cleaning & Maintenance | VS-62 |
| W2345 | Sample Display Signage & Pricing Update | VS-62 |
| W2346 | Interactive Display Technology Maintenance | VS-62 |
| W2347 | Vendor-Funded Display Program Management | VS-62 |
| W2348 | Sample Display Performance Review | VS-62 |
| W2349 | Sample Display Decommissioning | VS-62 |
| W2350 | Sample Program Cost Tracking | VS-62 |
| W2351 | Sample-to-Order Conversion Rate Analysis | VS-62 |
| W2354 | Customer Feedback on Sample Experience | VS-62 |
| W2355 | Digital vs. Physical Sample Effectiveness | VS-62 |
| W2647 | Mobile App Store Listing & Review Management | VS-75 |
| W2648 | Mobile App Push Notification Strategy & Execution | VS-75 |
| W2649 | Mobile App Loyalty Integration & Points Display | VS-75 |
| W2651 | Mobile App Content Management & Catalog Sync | VS-75 |
| W2652 | Mobile App Security & Data Privacy Compliance | VS-75 |
| W2654 | In-Store Kiosk Management & Content Updates | VS-75 |
| W2655 | QR Code Product Information & Review Display | VS-75 |
| W2657 | Mobile App In-Store Mode Activation | VS-75 |
| W2659 | In-Store Associate Mobile App & Task Management | VS-75 |
| W2660 | Customer In-Store Wi-Fi & Engagement Platform | VS-75 |
| W2661 | Digital Price Tag & Electronic Shelf Label Management | VS-75 |
| W2663 | App User Acquisition & Retention Funnel Analysis | VS-75 |
| W2666 | Digital Customer Satisfaction & App NPS | VS-75 |
| W2667 | Digital Personalization & Recommendation Engine Performance | VS-75 |
| W2668 | Omnichannel Digital Integration Health Monitoring | VS-75 |
| W2694 | Construction Project Material Requirements Planning | VS-77 |
| W2695 | Project Material Reservation & Inventory Allocation | VS-77 |
| W2696 | Project Material Substitution & Alternative Approval | VS-77 |
| W2697 | Project Material Price Lock & Escalation Management | VS-77 |
| W2699 | Project Material Change Order Processing | VS-77 |
| W2700 | Project Material Quality Specification Documentation | VS-77 |
| W2701 | Project Account Credit & Payment Terms Management | VS-77 |
| W2702 | Phase Delivery Trigger & Material Staging at DC | VS-77 |
| W2704 | Site Material Storage & Protection Coordination | VS-77 |
| W2705 | Cross-Phase Material Transfer & Reallocation | VS-77 |
| W2706 | Project Material Surplus & Return Processing | VS-77 |
| W2707 | Multi-Vendor Project Material Coordination | VS-77 |
| W2708 | Project Delivery SLA Compliance & Penalty Management | VS-77 |
| W2710 | Project Material Consumption vs. Estimate Variance Analysis | VS-77 |
| W2712 | Project Portfolio Revenue & Profitability Analysis | VS-77 |
| W2713 | Project Inventory Carrying Cost Analysis | VS-77 |
| W2715 | Project Material Waste & Sustainability Tracking | VS-77 |
| W2717 | Annual Project Business Review & Strategy Update | VS-77 |
| W2718 | Green Product Identification & Certification Verification | VS-78 |
| W2719 | Green Product Supplier Evaluation & Development | VS-78 |
| W2720 | Green Building Standards Knowledge Management | VS-78 |
| W2721 | Green Product Pricing & Margin Management | VS-78 |
| W2722 | Green Product Merchandising & In-Store Display | VS-78 |
| W2723 | Green Product Customer Education Content Development | VS-78 |
| W2724 | BERDE/LEED Project Material Documentation Support | VS-78 |
| W2725 | Green Product Ecommerce & Digital Catalog Management | VS-78 |
| W2726 | Green Building Project Material Consultation Service | VS-78 |
| W2727 | Green Home Energy Audit Referral Service | VS-78 |
| W2728 | BERDE/LEED Project Partnership with Architects & Engineers | VS-78 |
| W2729 | Green Building Workshop & Event Management | VS-78 |
| W2730 | Sustainable Product Return & Recycling Program | VS-78 |
| W2731 | Green Building Project Pipeline Management | VS-78 |
| W2733 | Green Building Advisory Customer Feedback & Improvement | VS-78 |
| W2735 | Environmental Impact Quantification of Green Product Sales | VS-78 |
| W2736 | Green Building Regulatory Compliance Monitoring | VS-78 |
| W2739 | Green Building Award & Recognition Program | VS-78 |
| W2742 | Customer Construction Material Quantity Calculator & Project Estimation Assistance | VS-9 |
| W2743 | Customer Project Shopping List Creation, Multi-Trip Purchase Coordination & Staged Fulfillment | VS-9 |
| W2744 | Customer Emergency Repair & Urgent Need Rapid-Fulfillment Assistance | VS-9 |
| W2826 | "BuildRight Negosyo Partner" Tier, Pricing & Benefits Configuration | VS-82 |
| W2827 | Micro-Reseller Right-Sized Assortment & Reorder List Curation | VS-82 |
| W2828 | MSME Product Knowledge, Negosyo Academy & Retailer Training | VS-82 |
| W2829 | Micro-Wholesale Pricing, Margin & Competitiveness Governance | VS-82 |
| W2830 | MSME Co-op & "Aling Mary" Cluster Group Buying Aggregation | VS-82 |
| W2831 | Field Sales / Promodizer Route Management & Micro-Account Coverage | VS-82 |
| W2832 | MSME Account Health, Churn Prevention & Win-Back | VS-82 |
| W2833 | MSME Multi-Channel Ordering (App/WhatsApp/Call/Sales Rep) Capture | VS-82 |
| W2834 | MSME Order Validation, Credit Check & Confirmation | VS-82 |
| W2836 | Last-Mile Delivery to Sari-Sari / Micro-Account (Tricycle/Multicab) | VS-82 |
| W2839 | Delivery POD, Discrepancy & Customer Satisfaction Capture | VS-82 |
| W2840 | Micro-Wholesale SLA, Exception & Capacity Management | VS-82 |
| W2841 | MSME Micro-Credit & "Negosyo Loan" Origination (Partner Bank/SBCorp) | VS-82 |
| W2842 | MSME Receivables Financing, Factor & Receivable Discounting | VS-82 |
| W2843 | MSME Digital Store Upgrade & E-Load/E-Wallet Onboarding | VS-82 |
| W2844 | MSME Point-of-Sale / Inventory App Provisioning & Support | VS-82 |
| W2845 | MSME Data Monetization & BuildRight Supplier Co-Marketing | VS-82 |
| W2846 | MSME Loyalty, Incentive & Gamified Growth Program | VS-82 |
| W2848 | MSME Ecosystem Expansion (DTI/GoNegosyo/Cooperative Partnership) | VS-82 |
| W3137 | Marketplace Platform Strategy, Business Model & Catalog Coverage | VS-95 |
| W3138 | Third-Party Seller Recruitment & Vetting | VS-95 |
| W3140 | Seller Catalog Integration, Mapping & Listing Quality | VS-95 |
| W3141 | Seller Pricing Rules, Commission & Fee Structure | VS-95 |
| W3142 | Seller Enablement, Training & Self-Service Portal | VS-95 |
| W3143 | Seller Account Management & Relationship Tiering | VS-95 |
| W3144 | Seller Offboarding, Exit & Data Portability | VS-95 |
| W3145 | Unified Marketplace Catalog & Search Merchandising | VS-95 |
| W3146 | First-Party vs Third-Party Offer Comparison & Buy-Box | VS-95 |
| W3147 | Marketplace Order Capture, Fraud Screening & Routing | VS-95 |
| W3148 | Seller Fulfillment SLA, Shipment Tracking & POD | VS-95 |
| W3150 | Seller Inventory Sync, Reservation & Oversell Prevention | VS-95 |
| W3151 | Marketplace Returns, Seller Responsibility & Disposition | VS-95 |
| W3152 | Seller-Initiated Promotions, Coupons & Co-Funded Campaigns | VS-95 |
| W3153 | Marketplace Commission, Fee Deduction & Seller Payout | VS-95 |
| W3155 | Seller Quality, Complaint & Dispute Resolution | VS-95 |
| W3156 | Seller Fraud, Counterfeit & Policy Violation Handling | VS-95 |
| W3158 | Marketplace Consumer Protection & Trust Program | VS-95 |
| W3159 | Marketplace Data Privacy, Seller Data Governance & DPA Compliance | VS-95 |
| W4337 | Live-Goods & Garden Center Strategy, Assortment & Seasonal Calendar | VS-145 |
| W4338 | Live Plant Sourcing, Grower/Vendor Management & Phytosanitary Compliance | VS-145 |
| W4339 | Live-Goods Inbound Receiving, Acclimatization & Quarantine | VS-145 |
| W4340 | Garden Center Nursery, Propagation & Plant Health Care | VS-145 |
| W4341 | Live-Goods Pricing, Markdown-on-Decline & Shrink Policy | VS-145 |
| W4342 | Live-Goods Consignment, Vendor-Managed & Pay-by-Scan Operations | VS-145 |
| W4343 | Live-Goods Master Data, Care Attributes & Customer Content | VS-145 |
| W4344 | Seasonal Garden Program, Promotions & Calendar Planning | VS-145 |
| W4345 | Garden Center Daily Care, Watering, Pruning & Rotation | VS-145 |
| W4346 | Live-Goods Merchandising, Space & Display (incl. Outdoor Yard) | VS-145 |
| W4347 | Plant Health Monitoring, Pest/Disease & Treatment | VS-145 |
| W4348 | Live-Goods Customer Advisory, Plant Selection & Guarantee | VS-145 |
| W4349 | Seasonal/Event Selling (Ber-Months, Valentine, Holy Week, Rainy) | VS-145 |
| W4350 | Garden Center Staffing, Trade Knowledge & Capability | VS-145 |
| W4352 | Customer Returns, Plant Guarantee & Replacement Policy | VS-145 |
| W4353 | Live-Goods Shrink, Mortality & Write-Off Management | VS-145 |
| W4354 | Decline/Markdown Trigger, Aging & Clearance | VS-145 |
| W4357 | Invasive/Restricted Species, CITES & BPI Compliance | VS-145 |
| W4434 | SCO/Scan-&-Go Technology Selection & Architecture | VS-149 |
| W4435 | SCO Lane Layout, Store Design & Capacity Planning | VS-149 |
| W4436 | Assisted & Mobile Scan-&-Go (Bring-Your-Own-Device) Program Design | VS-149 |
| W4437 | Weight-Security, Computer-Vision & Loss-Prevention Design | VS-149 |
| W4438 | Age-Restricted, Hazmat & Controlled-Item Intervention Design | VS-149 |
| W4439 | Unattended / 24-Hour & Contactless Store Format Design | VS-149 |
| W4440 | SCO Acceptance, Change Management & Associate Role Redesign | VS-149 |
| W4441 | SCO & Scan-&-Go Lane Daily Open/Close & Staffing | VS-149 |
| W4443 | SCO Intervention, Age-Verification & Override Handling | VS-149 |
| W4445 | SCO Cash Management, Cash-Recycler & Tender Handling | VS-149 |
| W4446 | SCO Hardware/Software Incident, Fault & Uptime Management | VS-149 |
| W4447 | Customer SCO Education, Signage & Friction Reduction | VS-149 |
| W4448 | SCO Peak/Queue Management & Host Allocation | VS-149 |
| W4449 | SCO/Scan-&-Go Loss, Sweethearting & Swap-Fraud Detection | VS-149 |
| W4451 | SCO Refund, Return & Void Integrity | VS-149 |
| W4601 | VAS/Financial-Agency Strategy, Portfolio & Footfall Model | VS-156 |
| W4602 | Bills-Payment Aggregator Partnering & Biller Onboarding | VS-156 |
| W4603 | Remittance & E-Money Principal/Partner Selection | VS-156 |
| W4604 | Mobile Load/Top-Up & Telco Partner Setup | VS-156 |
| W4606 | Agency Contract, Liability & SLA Framework | VS-156 |
| W4607 | VAS Counter Design, Staffing & Enablement | VS-156 |
| W4608 | VAS Systems, Integration & Data-Architecture Setup | VS-156 |
| W4615 | VAS Exception, Error & Reversal Handling | VS-156 |
| W4616 | VAS Customer Service, Complaints & Disclosure | VS-156 |
| W4621 | VAS Fraud, Risk & Loss Management | VS-156 |
| W4623 | VAS Audit, Controls & Assurance | VS-156 |
| W4624 | VAS Program Performance Review & Strategic Adjustment | VS-156 |
| W4745 | Self-Haul Rental Fleet Strategy, Sizing & Business Model | VS-162 |
| W4746 | Rental Vehicle Procurement, Specification & Fleet Acquisition | VS-162 |
| W4748 | Rental Fleet Insurance Program — CTPL, Comprehensive & Self-Insurance Layer | VS-162 |
| W4750 | Rental Vehicle Preventive Maintenance, Safety Inspection & Servicing Schedule | VS-162 |
| W4751 | Rental Fleet Cross-Store Rebalancing & Seasonal Demand Matching | VS-162 |
| W4752 | Rental Vehicle End-of-Life Disposition, Remarketing & Replacement Cycle | VS-162 |
| W4753 | Rental Inquiry, Reservation & Availability Promise | VS-162 |
| W4754 | Driver-License Verification, Age/Eligibility Check & Driving-Record Screen | VS-162 |
| W4756 | Security Deposit Authorization, Card Hold & Pre-Authorization Capture | VS-162 |
| W4757 | Loss Damage Waiver (LDW) Sale, Insurance Upsell & Coverage Explanation | VS-162 |
| W4758 | Vehicle Handover, Time-and-Mileage Capture & Yard Loading Coordination | VS-162 |
| W4759 | Return Inspection, Damage Assessment, Fuel/Cleaning Check & Re-Release Gate | VS-162 |
| W4761 | Rental Vehicle Accident, Damage & Roadside Event Response | VS-162 |
| W4763 | Vehicle Non-Return, Theft & Fraud Recovery (Geofence-Breach Response) | VS-162 |
| W4764 | Traffic Violation, Citation & Toll Violation Handling (Customer Recharge) | VS-162 |
| W4765 | Customer Dispute, Complaint & Chargeback Resolution | VS-162 |
| W4794 | Locker-Vendor/Operator Selection & Contracting | VS-164 |
| W4796 | Locker Hardware Specification, Procurement & Asset Registration | VS-164 |
| W4797 | Locker Installation, Access-Control Integration & Commissioning | VS-164 |
| W4798 | Off-Site / Partner-Location Locker Hosting & Host Agreement | VS-164 |
| W4799 | Third-Party Parcel Pickup Integration & Carrier Onboarding | VS-164 |
| W4800 | Network Expansion Governance, Capex Approval & Portfolio Prioritization | VS-164 |
| W4802 | Access-Code/QR Generation, Delivery & Pickup Authentication | VS-164 |
| W4803 | Returns Drop-Off via Locker & Reverse-Logistics Handoff | VS-164 |
| W4804 | Overflow Management, Abandonment & Compartment Reclaim | VS-164 |
| W4805 | Customer Pickup Journey, Notifications & Support Escalation | VS-164 |
| W4806 | Oversize / Bulky & Refrigerated Locker Handling | VS-164 |
| W4807 | ERP / Ecommerce / OMS / Loyalty Real-Time Integration Operations | VS-164 |
| W4809 | Locker Preventive Maintenance, Cleaning & Hardware Health | VS-164 |
| W4811 | Security, Vandalism, Theft & Loss Prevention at Lockers | VS-164 |
| W4813 | Data Privacy & Consent for Locker Customer/Recipient Data | VS-164 |
| W4814 | Uptime/SLA Management, Availability Reporting & Vendor Governance | VS-164 |
| W4816 | Go-Live Readiness, Site Acceptance & Hypercare for New Locker Sites | VS-164 |
| W4889 | In-Store Audio, Ambient Media & Customer-Experience Strategy | VS-168 |
| W4890 | Background Music Programming, Playlist Strategy & Brand-Sound Standards | VS-168 |
| W4892 | Commercial Music Service / Background-Music Provider Selection & Contracting | VS-168 |
| W4893 | In-Store Digital Signage Content Strategy & Programming | VS-168 |
| W4894 | Ambient Scent & Sensory Experience Program | VS-168 |
| W4895 | In-Store Media Budget, Allowance & Vendor Co-Funding | VS-168 |
| W4896 | Multi-Entity / Multi-Region Ambient Media Standards & Governance | VS-168 |
| W4897 | PA / Paging System Daily Operations & Live Announcement Protocol | VS-168 |
| W4898 | Background Music Daily Operations, Scheduling & Volume / Zone Control | VS-168 |
| W4899 | In-Store Digital Signage Content Scheduling, Publishing & Playback Operations | VS-168 |
| W4900 | Audio / PA / Digital-Signage Equipment Preventive Maintenance & Health Monitoring | VS-168 |
| W4901 | Seasonal / Event / Promotional Media Campaign Deployment | VS-168 |
| W4902 | Emergency Override & Public-Address Incident Protocol | VS-168 |
| W4903 | In-Store Media Content Localization & Filipino / Regional-Language Voice | VS-168 |
| W4904 | Vendor Music / Signage Content Refresh & Asset Library Management | VS-168 |
| W4906 | Audio / Signage Equipment Lifecycle, Asset Management & Refresh Capex | VS-168 |
| W4907 | In-Store Media Technology & Integration Architecture | VS-168 |
| W4908 | Music Licensing Compliance Audit, Royalty True-Up & Records | VS-168 |
| W4910 | Vendor / Service SLA, Performance Governance & TPRM | VS-168 |
| W4961 | Customer Pickup, Will-Call & Loading-Zone Program Strategy & Operating Model | VS-171 |
| W4962 | Will-Call Counter Operations, Order Staging & Customer Identification/Release | VS-171 |
| W4963 | Pickup Appointment, Time-Slot & Loading-Bay Capacity Management | VS-171 |
| W4964 | Loading-Zone Layout, Signage, Wayfinding & Pedestrian/Vehicle Flow | VS-171 |
| W4966 | Customer Notification, Arrival Confirmation & Queue Management | VS-171 |
| W4968 | Self-Haul Rental (VS-162) & Customer-Hired-Vehicle Pickup Coordination | VS-171 |
| W4969 | Forklift & Loading Equipment Operations in the Customer Vehicle Area | VS-171 |
| W4970 | Bulky-Goods Loading into Customer Vehicles (Lumber, Tile, Cement, Appliance) | VS-171 |
| W4971 | Spotter, Banksperson & Pedestrian-Safety Protocol for Customer-Area Loading | VS-171 |
| W4972 | Load Securement, Weight Distribution & Vehicle Overload Prevention | VS-171 |
| W4974 | Carry-Out, Curbside & Drive-Up Assistance Service | VS-171 |
| W4975 | Bulk Material Breaking, Handling & Yard-to-Vehicle Transfer | VS-171 |
| W4976 | Hazardous / Fragile / High-Value Goods Loading Protocol | VS-171 |
| W4977 | Pickup SLA, Wait-Time & Customer Experience Measurement | VS-171 |
| W4978 | No-Show, Hold-Expiry, Restocking & Cancellation Management | VS-171 |
| W4979 | Loading Damage, Shortage & Wrong-Load Exception Resolution | VS-171 |
| W4980 | Pickup-Channel Fraud, Identity & Release-Integrity Controls | VS-171 |
| W4983 | Pickup Loading Service Chargeback, Fees & Documentation | VS-171 |
| W4984 | Customer Pickup Channel Data Privacy, Consent & Records Management | VS-171 |
| W5033 | Storage Program Strategy, Product Portfolio & Business-Model Design | VS-174 |
| W5034 | Storage Site Selection, Real-Estate Acquisition & Unit-Capacity Planning | VS-174 |
| W5035 | Storage Unit-Type Mix, Rate Card & Pricing Strategy | VS-174 |
| W5037 | Storage Facility Design, Build-Out, Security & Access Infrastructure | VS-174 |
| W5038 | Storage Lease/Rental Agreement, Terms & Insurance Program Administration | VS-174 |
| W5040 | Storage Operator Partner, Franchise & Third-Party-Manager Network Management | VS-174 |
| W5041 | Customer Storage Inquiry, Reservation & Unit Assignment | VS-174 |
| W5042 | Customer Move-In, Lease Execution, Access Credential & Insurance Setup | VS-174 |
| W5043 | Storage Facility Daily Access Control, Security Monitoring & Audit Trail | VS-174 |
| W5044 | Storage Tenant Billing, Auto-Pay, Late-Fee & Delinquency Management | VS-174 |
| W5047 | Abandoned-Unit Contents Disposition, Lien Sale & Regulatory Compliance | VS-174 |
| W5048 | Storage Customer Service, Complaint & Inquiry Resolution | VS-174 |
| W5049 | Storage Facility Daily Operations, Housekeeping & Maintenance Management | VS-174 |
| W5050 | Storage Security Operations, Surveillance, Access System & Incident Response | VS-174 |
| W5051 | Stored-Goods Restrictions, Hazardous/Prohibited-Items Inspection & Enforcement | VS-174 |
| W5057 | Propane/LPG Cylinder Exchange & Refill Program Strategy & Business-Model Design | VS-175 |
| W5058 | LPG Bulk Supply, Vendor Selection, Pricing & Procurement Management | VS-175 |
| W5059 | LPG Cylinder-Fleet Strategy, Standardization, Branding & RA 11592 Compliance | VS-175 |
| W5060 | Cylinder Procurement, Ownership/Pool Model, Asset Tracking & Lifecycle Management | VS-175 |
| W5062 | LPG Retail Pricing, Exchange Fee, Refill Tariff & Margin Strategy | VS-175 |
| W5064 | LPG HAZMAT Handling, PPE & Emergency-Response Program Design | VS-175 |
| W5066 | Cylinder Refill, Re-Valve & Hydrostatic-Test Vendor Coordination & Logistics | VS-175 |
| W5068 | Customer-Owned-Cylinder Refill Service (Weigh, Fill, Seal, Charge) | VS-175 |
| W5069 | Cylinder Leak/Damage Inspection, Condemnation & Out-of-Service Quarantine | VS-175 |
| W5071 | Customer Cylinder Delivery, Exchange-at-Home & Will-Call Service | VS-175 |
| W5072 | LPG Forklift & Bulk-Customer Account, Delivery & Refill Management | VS-175 |
| W5079 | LPG Customer Demand Seasonality, Forecasting & Stock-Out Prevention | VS-175 |

**Finance** (288)

| ID | Workflow | Value Stream |
|---|---|---|
| W1199 | Import Letter of Credit (LC) Lifecycle, Amendment & Bank Release Management | VS-15 |
| W1294 | Import Letter of Credit (LC) Application & Bank Coordination | VS-18 |
| W1326 | Customer B2B Project Payment Plan Negotiation, Arrears Management & Restructuring | VS-16 |
| W1361 | Multi-Bank Cash Position Daily Aggregation & Automated Zero-Balance Sweep | VS-18 |
| W1405 | Store-Level P&L Auto-Generation, Contribution Margin Analysis & Monthly Financial Performance Review | VS-17 |
| W1414 | Customer Trade Account Credit Insurance Premium Review, Claims Filing & Recovery Management | VS-16 |
| W1455 | Import Letter of Credit (LC) Opening, Amendment & Bank Fee Management | VS-18 |
| W1473 | FX Hedge Effectiveness Testing, Mark-to-Market Valuation & Accounting Compliance | VS-18 |
| W1504 | Supplier Invoice Price Discrepancy Investigation, Debit Note Issuance & Resolution Tracking | VS-15 |
| W1668 | Store Supplies & Consumables Procurement | VS-34 |
| W1669 | IT Equipment & Software Procurement | VS-34 |
| W1670 | Uniform, PPE & Safety Equipment Procurement | VS-34 |
| W1671 | Marketing Materials & Print Procurement | VS-34 |
| W1672 | Facility Maintenance Supplies & Services Procurement | VS-34 |
| W1673 | Office Supplies & Administrative Procurement | VS-34 |
| W1674 | Emergency & Urgent Non-Merchandise Purchase Processing | VS-34 |
| W1675 | Non-Merchandise Purchase Requisition to Payment Workflow | VS-34 |
| W1676 | Annual Service Contract Renewal & Renegotiation | VS-34 |
| W1677 | New Service Provider Evaluation & Onboarding | VS-34 |
| W1678 | Service Level Agreement (SLA) Monitoring & Performance Tracking | VS-34 |
| W1679 | Professional Services Engagement & Statement of Work Management | VS-34 |
| W1680 | Third-Party Logistics (3PL) Service Contract Management | VS-34 |
| W1681 | Security & Cleaning Service Provider Management | VS-34 |
| W1682 | Service Provider Contract Termination & Transition Management | VS-34 |
| W1683 | Monthly Department Expense Budget vs. Actual Tracking | VS-34 |
| W1685 | Company Expense Card & Corporate Credit Card Management | VS-34 |
| W1686 | Travel & Business Entertainment Expense Management | VS-34 |
| W1689 | Expense Policy Compliance Monitoring & Audit | VS-34 |
| W1763 | Financing Partner Selection & Agreement Negotiation | VS-38 |
| W1764 | In-Store Financing Desk Setup & Staff Training | VS-38 |
| W1765 | Promotional Financing Campaign Planning (0% Installment) | VS-38 |
| W1768 | Buy-Now-Pay-Later (BNPL) Integration & Processing | VS-38 |
| W1769 | Financing Program Performance Monitoring & Partner Review | VS-38 |
| W1771 | Installment Sale Transaction Recording & Revenue Recognition | VS-38 |
| W1772 | In-House Installment Receivable Management (Trade Accounts) | VS-38 |
| W1775 | Installment Sale Returns & Cancellation Processing | VS-38 |
| W1776 | Promotional Installment Subsidy Accounting | VS-38 |
| W1778 | Installment Portfolio Reporting & Aging Analysis | VS-38 |
| W1781 | Financing Chargeback & Dispute Resolution | VS-38 |
| W1782 | MDR Fee Tracking & Expense Reporting | VS-38 |
| W1784 | Financing Partner Payment Exception Handling | VS-38 |
| W1787 | Vendor Rebate Agreement Negotiation & Setup | VS-39 |
| W1788 | Rebate Accrual Estimation & Monthly Posting | VS-39 |
| W1789 | Volume-Based Rebate Tracking & Threshold Monitoring | VS-39 |
| W1791 | Special Pricing Agreement (SPA) Management | VS-39 |
| W1792 | Vendor Markdown Allowance & Damage Claim Recovery | VS-39 |
| W1793 | Rebate Claim Submission & Verification | VS-39 |
| W1795 | Co-Op Advertising Fund Agreement & Budget Allocation | VS-39 |
| W1796 | Vendor-Funded Promotional Activity Planning | VS-39 |
| W1797 | Co-Op Marketing Activity Execution & Vendor Notification | VS-39 |
| W1798 | Co-Op Marketing Expense Documentation & Proof of Performance | VS-39 |
| W1800 | In-Store Vendor Display & Endcap Program Management | VS-39 |
| W1807 | Rebate Forecasting & Annual Income Projection | VS-39 |
| W1808 | Rebate Audit & Compliance Review | VS-39 |
| W1810 | Rebate Process Automation & System Enhancement | VS-39 |
| W2142 | Physical Gift Card Stock Management | VS-54 |
| W2144 | Digital Gift Card Sale & Delivery | VS-54 |
| W2145 | Corporate Bulk Gift Card Program | VS-54 |
| W2146 | Gift Card Promotional Campaign | VS-54 |
| W2147 | Gift Card Distribution Channel Management | VS-54 |
| W2148 | Gift Card Compliance & Regulatory Management | VS-54 |
| W2149 | Gift Card Denomination & Pricing Strategy | VS-54 |
| W2151 | Online Gift Card Redemption | VS-54 |
| W2152 | Gift Card Balance Inquiry & Statement | VS-54 |
| W2153 | Lost/Stolen Gift Card Management | VS-54 |
| W2154 | Gift Card Partial Redemption & Multi-Card Payment | VS-54 |
| W2155 | Gift Card Reload & Top-Up | VS-54 |
| W2156 | Gift Card Expiry & Breakage Management | VS-54 |
| W2157 | Gift Card Refund & Cancellation | VS-54 |
| W2159 | Monthly Gift Card Financial Reporting | VS-54 |
| W2160 | Gift Card Fraud Monitoring & Prevention | VS-54 |
| W2162 | Gift Card Customer Satisfaction Monitoring | VS-54 |
| W2163 | Gift Card System Integration & API Management | VS-54 |
| W2165 | Gift Card Channel Profitability Analysis | VS-54 |
| W2478 | New Trade Account Credit Application | VS-68 |
| W2479 | Credit Scoring Model Maintenance | VS-68 |
| W2480 | Existing Account Periodic Credit Review | VS-68 |
| W2481 | Credit Bureau & External Data Integration | VS-68 |
| W2482 | Customer Financial Statement Analysis | VS-68 |
| W2483 | Industry & Economic Risk Factor Assessment | VS-68 |
| W2484 | Trade Credit Insurance Policy Assessment | VS-68 |
| W2485 | Portfolio Risk Concentration Analysis | VS-68 |
| W2490 | Overdue Payment Monitoring & Escalation | VS-68 |
| W2491 | Customer Payment Behavior Scoring | VS-68 |
| W2492 | Credit Hold Order Management | VS-68 |
| W2493 | Aging Report & Provisioning Analysis | VS-68 |
| W2496 | Bad Debt Write-Off Decision | VS-68 |
| W2497 | Bad Debt Recovery from Written-Off Accounts | VS-68 |
| W2498 | Credit Insurance Claim Filing | VS-68 |
| W2500 | Credit Policy Annual Review & Update | VS-68 |
| W2574 | Shared Services Cost Pool Identification & Classification | VS-72 |
| W2575 | Monthly Shared Services Cost Pool Compilation | VS-72 |
| W2576 | IT Shared Services Chargeback Calculation & Allocation | VS-72 |
| W2577 | HR Shared Services Cost Allocation | VS-72 |
| W2578 | New Shared Service Establishment & Cost Pool Setup | VS-72 |
| W2579 | Shared Service Cost Budget & Variance Management | VS-72 |
| W2580 | Shared Services Cost Pool Audit & Documentation | VS-72 |
| W2581 | Shared Service Provider Recharge to External Third Parties | VS-72 |
| W2584 | IC Pricing Dispute Resolution | VS-72 |
| W2585 | IC Billing Accuracy Audit | VS-72 |
| W2587 | IC Service Level Performance Monitoring | VS-72 |
| W2588 | New Entity IC Service Onboarding | VS-72 |
| W2589 | IC Service Agreement Renewal & Renegotiation | VS-72 |
| W2593 | Shared Services Staff Productivity & Capacity Planning | VS-72 |
| W2596 | Shared Services Entity Profitability Contribution Analysis | VS-72 |
| W2597 | Shared Services Annual Performance Report & Board Presentation | VS-72 |
| W2777 | Acquirer & Card Scheme Registration, MID/MCC Setup | VS-80 |
| W2778 | E-Wallet (GCash/Maya) Merchant Onboarding & QR/Intent Integration | VS-80 |
| W2779 | Payment Gateway (PayMongo/Dragonpay) Configuration & Key Rotation | VS-80 |
| W2782 | Payment Partner SLA, Pricing & MDR Contract Review | VS-80 |
| W2788 | Chargeback Notification, Evidence Compilation & Representment | VS-80 |
| W2789 | Retrieval Request, Fraud Alert & Pre-Arbitration Handling | VS-80 |
| W2791 | Payment Fee & Interchange Cost Allocation to Store/Channel | VS-80 |
| W2793 | PCI-DSS SAQ Scope Management & Annual Self-Assessment | VS-80 |
| W2795 | Payment Fraud Rule & Velocity/Limit Configuration | VS-80 |
| W2796 | Terminal Key Injection, HSM & PIN Security Management | VS-80 |
| W2797 | 3-D Secure (3DS) Authentication & Liability Shift Tracking | VS-80 |
| W2798 | Payment System Incident, Breach & Forensic Response | VS-80 |
| W3161 | Lease Product Strategy & Portfolio Design | VS-96 |
| W3163 | Customer Credit Underwriting & Lease Approval | VS-96 |
| W3164 | Lease Quote, Proposal & Contract Generation | VS-96 |
| W3165 | Lessor Partner / Funding Source Management | VS-96 |
| W3166 | Lease vs Buy vs Rent Decision Support & Sales Enablement | VS-96 |
| W3167 | Asset Specification, Vendor Selection & Procurement for Lease | VS-96 |
| W3168 | Lease Origination Documentation, Insurance & Perfection | VS-96 |
| W3169 | Lease Booking, Asset Capitalization & Start-Day Setup | VS-96 |
| W3171 | Lease Asset Tracking, Maintenance & Inspection | VS-96 |
| W3172 | Lease Mid-Term Modification, Upgrade & Add-On | VS-96 |
| W3173 | Lease Insurance, Loss & Damage Management | VS-96 |
| W3174 | Lease Delinquency, Restructure & Cure Period | VS-96 |
| W3175 | Lease Maturity, Return Inspection & Disposition | VS-96 |
| W3176 | Lease Buyout, Early Termination & Renewal | VS-96 |
| W3178 | Lease Credit Risk, Scoring & Provisioning | VS-96 |
| W3179 | Residual Value Realization & Used-Equipment Remarketing | VS-96 |
| W3181 | Lease Portfolio Securitization & Funding Strategy | VS-96 |
| W3377 | SCF Strategy, Program Charter & Multi-Funder Facility Design | VS-105 |
| W3378 | Bank / Fintech SCF Partner Selection, Onboarding & Agreement Management | VS-105 |
| W3381 | Extended-Terms / Payable-Restructuring Negotiation & Vendor Agreement | VS-105 |
| W3382 | SCF Facility Limit, Utilization & Covenant Monitoring | VS-105 |
| W3383 | SCF Vendor Dispute, Pricing Discrepancy & Off-Platform Exception Handling | VS-105 |
| W3384 | SCF Program Risk, Concentration & Counterparty Governance | VS-105 |
| W3385 | Dynamic-Discounting Platform Setup, Discount-Curve Design & Vendor Enrollment | VS-105 |
| W3386 | Sliding-Scale Early-Payment Offer Generation & Vendor Acceptance | VS-105 |
| W3389 | Cash-Availability-Aware Discount Throttling & Treasury Authorization | VS-105 |
| W3390 | Vendor-Initiated Early-Payment Request & Ad-Hoc Discount Approval | VS-105 |
| W3393 | Working-Capital KPI Definition, Baseline & Target Setting (DPO/DIO/DSO/DWC) | VS-105 |
| W3394 | Days-Payable-Outstanding (DPO) Improvement Initiative Management | VS-105 |
| W3395 | Inventory Days (DIO) Cash-Release & Inventory-Working-Capital Program | VS-105 |
| W3396 | Days-Sales-Outstanding (DSO) & Receivable Cash-Release Coordination | VS-105 |
| W3398 | Working-Capital Initiative Portfolio, Prioritization & Benefits Realization | VS-105 |
| W3400 | Working-Capital Policy, Governance & Board-Level Cash Discipline | VS-105 |
| W4265 | COD Program Strategy, Channel Scope & Operating Model | VS-142 |
| W4266 | COD Order Eligibility, Limit & Risk-Tier Policy | VS-142 |
| W4267 | COD Pricing, Fee & Incentive Structure | VS-142 |
| W4268 | Driver/3PL COD Authorization, Bonding & Contract Terms | VS-142 |
| W4269 | COD Risk Framework, Insurance & Loss-Account Policy | VS-142 |
| W4270 | COD Cash-Handling Controls, SoD & Custody Standard | VS-142 |
| W4272 | COD System & Integration Architecture (Order↔Payment↔Cash) | VS-142 |
| W4273 | COD Order Handoff, Delivery Note & Amount-Due Computation | VS-142 |
| W4275 | Driver/3PL Daily Cash Custody, Remittance & Deposit | VS-142 |
| W4276 | COD Refusal, Short-Pay & Failed-Delivery Cash Handling | VS-142 |
| W4278 | 3PL COD Cash File Ingest, Match & Discrepancy Handling | VS-142 |
| W4280 | COD Physical Cash Security, Robbery/Loss Response & Recovery | VS-142 |
| W4282 | COD Float, Working-Capital & Cash-Conversion-Cycle Management | VS-142 |
| W4283 | COD Fraud Detection, Investigation & Loss Recovery | VS-142 |
| W4285 | COD Chargeback-Equivalent, Deduction & Refund Integrity | VS-142 |
| W4409 | Lease Accounting Strategy, Policy & PFRS 16/IFRS 16 Framework | VS-148 |
| W4410 | Lease Portfolio Discovery, Identification & Lease-Component Extraction | VS-148 |
| W4411 | Lease Contract Data Capture & Abstracting (Terms, Payments, Options) | VS-148 |
| W4412 | Discount Rate, Lease Term & Payment Determination | VS-148 |
| W4413 | Lease Classification (Recognition Exemption vs On-Balance-Sheet) | VS-148 |
| W4414 | Initial Recognition — ROU Asset & Lease Liability Calculation | VS-148 |
| W4417 | Subsequent Measurement — Depreciation, Interest & Payment Unwind | VS-148 |
| W4418 | Lease Modification, Reassessment & Remeasurement | VS-148 |
| W4419 | Lease Renewal, Termination & Early-Exit Accounting | VS-148 |
| W4420 | Variable & Index-Based Lease Payment Reassessment | VS-148 |
| W4421 | Sublease & Sale-and-Leaseback (Lessor-Side) Accounting | VS-148 |
| W4422 | Short-Term & Low-Value Lease Exemption Management | VS-148 |
| W4423 | Lease Impairment, Derecognition & Disposal | VS-148 |
| W4426 | Lease Data Governance, Master & Contract Repository | VS-148 |
| W4427 | Lease Accounting System (Technology) Configuration & Integration | VS-148 |
| W4428 | Audit, Internal Control & SOX-Style Compliance for Leases | VS-148 |
| W4529 | Total-Cost-of-Risk Baseline & Captive Feasibility/Business Case | VS-153 |
| W4530 | Captive Strategy, Structure & Risk-Scope Design | VS-153 |
| W4531 | Domicile Selection, Licensing & Regulatory Setup | VS-153 |
| W4532 | Captive Formation, Capitalization & Legal Entity Setup | VS-153 |
| W4533 | Captive Governance, Board & Investment Policy | VS-153 |
| W4534 | Fronting Carrier & Service-Provider Arrangements | VS-153 |
| W4536 | Captive Implementation, Transition & Go-Live Readiness | VS-153 |
| W4537 | Captive Underwriting Policy, Guidelines & Risk Acceptance | VS-153 |
| W4538 | Program Rating, Premium Pricing & Actuarial Valuation | VS-153 |
| W4539 | Policy Issuance, Fronting & Ceding to Captive | VS-153 |
| W4540 | Reinsurance Program Design & Treaty Placement | VS-153 |
| W4541 | Risk-Transfer Testing & Commutation/Reinsurance-Agreement Management | VS-153 |
| W4542 | Loss-Emergence, Reserving & Actuarial Reserve Review | VS-153 |
| W4543 | Aggregate-Loss & Cat-Aggregate Management | VS-153 |
| W4544 | Underwriting Performance Monitoring & Cycle Management | VS-153 |
| W4545 | Captive Claims Administration & TPA Management | VS-153 |
| W4548 | Captive Regulatory Compliance, RBC & Domicile Filings | VS-153 |
| W4549 | Captive Audit, Actuarial Opinion & External Review | VS-153 |
| W4550 | Captive Investment Portfolio & Treasury Management | VS-153 |
| W4552 | Captive Performance Review, Run-Off & Strategic Options | VS-153 |
| W4553 | Construction-Finance Strategy & Product Portfolio Design | VS-154 |
| W4556 | Loan Product Terms, Eligibility & Pricing Framework | VS-154 |
| W4557 | Construction-Finance Risk, Credit-Policy & Anti-Predatory-Lending Standard | VS-154 |
| W4558 | BuildRight↔Lender↔Contractor Integration & Draw-Schedule Design | VS-154 |
| W4559 | Frontline Enablement — Finance Desk, Store & Trade-Channel Offer | VS-154 |
| W4560 | Systems, Data Privacy & Integration Architecture | VS-154 |
| W4561 | Customer Identification, Finance-Need Discovery & Pre-Qualification | VS-154 |
| W4562 | Loan Application Intake & Documentation | VS-154 |
| W4563 | Credit Assessment, Affordability & Bureau Scoring Handoff | VS-154 |
| W4564 | Property/Project Valuation & Collateral Assessment | VS-154 |
| W4565 | Lender Underwriting, Approval & Conditions | VS-154 |
| W4566 | Loan Closing, Documentation & Disclosure | VS-154 |
| W4567 | Disbursement Setup, Draw Schedule & Escrow | VS-154 |
| W4568 | Post-Closing Handoff, Project Activation & Material Release | VS-154 |
| W4569 | Loan Servicing Coordination, Payment & Customer Support | VS-154 |
| W4570 | Referral Commission, Incentive & Revenue Management | VS-154 |
| W4572 | Delinquency, Default & BuildRight Exposure Management | VS-154 |
| W4574 | Partner-Lender Performance, Dispute & Renewal Management | VS-154 |
| W4576 | Program Performance Review, Risk & Strategic Adjustment | VS-154 |
| W4625 | Revenue-Stream & Contract-Portfolio Register Maintenance | VS-157 |
| W4626 | Contract Identification, Combination & Modification Assessment | VS-157 |
| W4627 | Performance-Obligation Identification for Bundled Product + Service Arrangements | VS-157 |
| W4629 | Consignment & VMI Revenue-Timing & Sell-Through Recognition | VS-157 |
| W4630 | Layaway, Customer-Deposit & Bill-and-Hold Recognition Assessment | VS-157 |
| W4631 | Loyalty-Points, Rewards & Deferred-Revenue Performance Obligation Setup | VS-157 |
| W4632 | Project & Government Over-Time-vs-Point-in-Time Recognition Assessment | VS-157 |
| W4633 | Standalone Selling Price (SSP) Methodology & Estimation Framework | VS-157 |
| W4634 | Transaction-Price Allocation Across Performance Obligations | VS-157 |
| W4635 | Gift-Card Breakage Estimation, Recognition & Remote-Redemption Testing | VS-157 |
| W4636 | Loyalty-Points Liability Measurement, Fair-Value & Forfeiture Adjustment | VS-157 |
| W4637 | Subscription & Extended-Warranty Deferred-Revenue Amortization | VS-157 |
| W4639 | Significant-Financing-Component & Advance/Prepayment Assessment | VS-157 |
| W4640 | Contract Costs — Cost-to-Obtain & Cost-to-Fulfill (Capitalization, Amortization & Impairment) | VS-157 |
| W4641 | Monthly/Quarterly Revenue Close, Reassessment & Journal-Entry Cycle | VS-157 |
| W4643 | Revenue Disaggregation, Disclosure Schedule & AFS Note Preparation | VS-157 |
| W4646 | Revenue-Recognition IT Configuration: SSP Engine, Deferral Schedules & GL Mapping | VS-157 |
| W4648 | Revenue-Recognition Internal Controls, SoD & Audit-Trail Governance | VS-157 |
| W4649 | Item Cost-Master & Standard-Cost Policy Framework | VS-158 |
| W4650 | Purchase-Price, Vendor-Quote & Should-Cost Data Aggregation | VS-158 |
| W4652 | Domestic Freight, Handling & Inbound Cost Allocation to SKU | VS-158 |
| W4653 | Catch-Weight & Cut-to-Length Unit-Cost Computation (per Board-Foot / Meter / Kg) | VS-158 |
| W4654 | Kit / BOM Cost Roll-Up & Component Costing | VS-158 |
| W4655 | Private-Label Fully-Burdened Cost Build (COGS+, Tooling, Royalty, MOQ) | VS-158 |
| W4656 | Periodic Standard-Cost Roll, Revaluation & WAC/Standard Reclass | VS-158 |
| W4657 | Purchase-Price Variance (PPV) Analysis & Vendor Accountability | VS-158 |
| W4658 | Landed-Cost Variance vs. Standard & Import Rate Volatility Analysis | VS-158 |
| W4659 | Production / Conversion Variance for Kitting & Build-to-Order | VS-158 |
| W4662 | Freight, Duty & Handling Cost Absorption vs. Billback Analysis | VS-158 |
| W4664 | Markdown, Promo & Vendor-Funding Net-Cost Impact Accounting | VS-158 |
| W4665 | Project / Job Costing for B2B & Government Contracts | VS-158 |
| W4666 | Service & Installation Costing (Labor, Subcontractor, Burden) | VS-158 |
| W4668 | Consignment & VMI Cost-Basis & Margin-on-Sell-Through | VS-158 |
| W4669 | Cost-Accounting Calendar, Period Close & Cost Allocation Cycles | VS-158 |
| W4670 | Cost-Master Data Governance, Change-Control & Approval Matrix | VS-158 |
| W4671 | Costing System Configuration: Cost-Sheet, Overhead Rates & GL Integration | VS-158 |
| W4672 | Cost-Accounting Internal Controls, Variance-Threshold & SoD Governance | VS-158 |
| W4938 | Borrowing-Base Model, Advance-Rate Matrix & Eligibility Criteria Definition | VS-170 |
| W4939 | Borrowing-Base Certificate Preparation & Periodic Submission | VS-170 |
| W4940 | Eligible-Inventory Analysis, Locations & In-Stock Eligibility Testing | VS-170 |
| W4941 | Eligible-Receivables Analysis, Aging & Concentration Limits | VS-170 |
| W4942 | Availability Calculation, Draws, Repayments & Excess-Availability Monitoring | VS-170 |
| W4943 | Field Examination Coordination, Bank Audit Response & True-Down Management | VS-170 |
| W4944 | Covenant Monitoring, Facility Reporting & Multi-Entity Governance | VS-170 |
| W4951 | Inventory Pledge Perfection, Registration & Security Documentation | VS-170 |
| W4952 | Pledged-Inventory Movement, Location Control & Release Authorization | VS-170 |
| W4953 | Facility Paydown, Collateral Release & Exit/Refinance Management | VS-170 |
| W4957 | Over-Advance, Fraud & Proceeds-Diversion Detection | VS-170 |
| W4958 | Internal Audit, Bank Covenant Assurance & Issue Remediation | VS-170 |
| W5009 | IR Program Strategy, Investor Audience & Equity-Story / Capital-Markets Narrative Design | VS-173 |
| W5010 | Investor & Shareholder Database, Targeting & Ownership Intelligence | VS-173 |
| W5011 | Periodic Investor Communications — Earnings, Results & Guidance Management | VS-173 |
| W5012 | Investor Events, Analyst Day, Roadshow & Conference Participation Management | VS-173 |
| W5013 | Sell-Side Analyst, Credit-Rating-Agency & Consensus-Estimate Relationship Management | VS-173 |
| W5014 | Investor Relations Website, IR Portal & Digital Disclosure-Channel Management | VS-173 |
| W5015 | Investor Inquiry, CRM & Proactive-Outreach Response Management | VS-173 |
| W5016 | ESG-Investor, Sustainable-Finance & Multi-Stakeholder Investor Communications | VS-173 |
| W5017 | Corporate Disclosure Controls, Materiality Assessment & Selective-Disclosure / Fair-Disclosure Program | VS-173 |
| W5019 | Material-Event / Ad-Hoc Disclosure, Press-Release Control & Rumor-Response Protocol | VS-173 |
| W5020 | Annual Stockholders' Meeting (ASHM) Investor Notice, Proxy Statement & Information Circular | VS-173 |
| W5021 | Capital-Markets & Securities-Offering Transaction Disclosure & Reporting | VS-173 |
| W5023 | Related-Party Transaction, Beneficial-Ownership & Group / Corporate-Structure Disclosure | VS-173 |
| W5024 | Disclosure Governance, Investor-Feedback-to-Management & Board/Committee Reporting | VS-173 |
| W5025 | Share Register, Stock Ledger & Ownership / Cap-Table Administration | VS-173 |
| W5027 | Dividend & Distribution Program — Declaration-to-Payment, DRIP/Election & Unclaimed-Property | VS-173 |
| W5028 | Shareholder Services, Investor Self-Service Portal & Inquiry Handling | VS-173 |
| W5032 | Crisis, Activist-Investor & Transaction IR Response Coordination | VS-173 |

**People** (147)

| ID | Workflow | Value Stream |
|---|---|---|
| W1182 | Multi-Entity Cross-Company Workforce Scheduling & Labor Cost Allocation | VS-19 |
| W1325 | Employee Death-in-Service Benefits Processing & Beneficiary Claim Management | VS-19 |
| W1358 | Seasonal Workforce Scaling, Temporary Hiring Ramp & Post-Season Right-Sizing | VS-19 |
| W1410 | Store Employee Inter-Location Transfer Processing, Labor Cost Reallocation & Benefit Continuity | VS-19 |
| W1500 | Store New Employee Shadow Training Program, Buddy Assignment & 90-Day Competency Checklist | VS-19 |
| W1526 | Store-Level Seasonal & Project-Based Temporary Staff Hiring, Contract Management & Separation | VS-19 |
| W3209 | Contingent Labor Strategy & Workforce Category Planning | VS-98 |
| W3210 | Agency & Service Contractor Sourcing & Qualification | VS-98 |
| W3212 | Statement of Work & Service Level Agreement Drafting | VS-98 |
| W3214 | Insurance, Bonding & Contractor Risk Transfer | VS-98 |
| W3215 | Worker Classification & Co-Employment Risk Assessment | VS-98 |
| W3216 | Contractor Renewal, Offboarding & Replacement | VS-98 |
| W3218 | Contractor Onboarding, Badging & Site Access | VS-98 |
| W3219 | Contractor Safety Orientation & Permit-to-Work | VS-98 |
| W3220 | Time Tracking, Attendance & Deliverable Confirmation | VS-98 |
| W3222 | Asset, Tool & Uniform Issuance & Recovery | VS-98 |
| W3223 | Background Check, NBI & Pre-Engagement Screening | VS-98 |
| W3224 | Daily Contractor Supervision & Performance Monitoring | VS-98 |
| W3228 | Incident, Injury & Contractor Claims Management | VS-98 |
| W3229 | Contractor Fraud, Theft & Background Investigation | VS-98 |
| W3230 | Conversion-to-Regular & Headcount Boundary Management | VS-98 |
| W3231 | Outsourced Function Transition & Insourcing/Outsourcing Decisions | VS-98 |
| W3232 | Workforce Composition Strategy & Integrated Workforce Planning | VS-98 |
| W3305 | Job Analysis, Documentation & Job Description Management | VS-102 |
| W3306 | Job Evaluation, Grading & Job Architecture (Career Framework) Maintenance | VS-102 |
| W3307 | Annual Salary Structure Design, Range Setting & Range Penetration | VS-102 |
| W3311 | Pay Range Administration, Promotion/Merit Increase & Range-Outlier Management | VS-102 |
| W3312 | Compensation Policy, Governance & Executive Pay Review | VS-102 |
| W3313 | Employee Benefits Program Design, Enrollment & Annual Renewal (HMO/Medical) | VS-102 |
| W3315 | Retirement, Pension & Long-Service Benefit Program Management | VS-102 |
| W3316 | Employee Allowances, Reimbursements & Flexible Benefits Administration | VS-102 |
| W3317 | Wellness, EAP & Lifestyle Benefit Program Operations | VS-102 |
| W3318 | Dependent & Life-Event Benefits Management (Maternity, Paternity, Bereavement) | VS-102 |
| W3319 | Benefits Vendor Management, Broker & Provider Relations | VS-102 |
| W3321 | Short-Term Incentive (STI) / Bonus Plan Design & Administration | VS-102 |
| W3322 | Sales Commission & Trade-Incentive Plan Design, Calculation & Payout | VS-102 |
| W3323 | Store/Team Performance Bonus & Gainshare Plan Management | VS-102 |
| W3324 | Long-Term Incentive (LTI), Retention & Recognition Program Design | VS-102 |
| W3325 | Total Rewards Statement Generation & Value-Proposition Communication | VS-102 |
| W3326 | Recognition, Awards & Service-Anniversary Program Operations | VS-102 |
| W3327 | Compensation & Benefits Budget Planning, Forecasting & Spend Control | VS-102 |
| W3761 | Employer Brand Strategy, Positioning & EVP Development | VS-121 |
| W3762 | Career Site, Candidate Portal & Talent Content Product Management | VS-121 |
| W3763 | Talent Marketing Campaign Planning & Channel Strategy | VS-121 |
| W3764 | Social Recruiting, Employer Review-Site & Online Reputation Management | VS-121 |
| W3767 | Diversity Recruiting Brand, Inclusive Hiring Marketing & Accessibility | VS-121 |
| W3768 | TA Marketing Budget, Agency/Channel Governance & Vendor Management | VS-121 |
| W3769 | Candidate Journey Design & Candidate Experience Standard | VS-121 |
| W3770 | Candidate Relationship Management (Talent CRM) & Talent Community Operations | VS-121 |
| W3771 | Proactive Candidate Sourcing & Talent Mining Operations | VS-121 |
| W3772 | Candidate Screening, Assessment & Structured Interview Operations | VS-121 |
| W3773 | Offer Management, Pre-Boarding & Offer-to-Hire Conversion | VS-121 |
| W3774 | Candidate Communication, Interview Scheduling & Feedback SLA Operations | VS-121 |
| W3775 | Recruiter Capacity, Requisition Management & Hiring-Manager Partnership | VS-121 |
| W3777 | Campus, University & Vocational School Partnership & Early-Career Pipeline | VS-121 |
| W3778 | Management Trainee / Cadetship Program Design & Talent-Brand Integration | VS-121 |
| W3779 | Internal Mobility Marketing, Talent Marketplace & Career Pathing Communication | VS-121 |
| W3780 | Alumni, Boomerang & Former-Employee Re-engagement Program | VS-121 |
| W3782 | TA Technology Stack, ATS/CRM Integration & Candidate-Data Governance | VS-121 |
| W3783 | TA Compliance, Equal-Opportunity, Consent & Audit Readiness | VS-121 |
| W4241 | Employee Commute-Need Assessment & Transport Strategy | VS-141 |
| W4242 | Transport Policy, Eligibility & Shift-Coverage Rules | VS-141 |
| W4243 | Transport-Allowance Design, Rate Setting & Tax Treatment | VS-141 |
| W4244 | Transport Operating-Model Decision (Owned vs Leased vs Contracted vs Allowance) | VS-141 |
| W4245 | Shuttle Fleet Requirement, Capital & Leasing Plan | VS-141 |
| W4246 | Transport Budget, Cost Allocation & Chargeback to Sites | VS-141 |
| W4247 | Transport Governance, DOLE/LTFRB Compliance Framework & Insurance | VS-141 |
| W4248 | Commute Experience, EVP Linkage & Continuous-Improvement Plan | VS-141 |
| W4249 | Shuttle Route Design, Shift Schedule & Pickup-Point Network | VS-141 |
| W4251 | Employee Entitlement, Ridership Eligibility & Seat Allocation | VS-141 |
| W4252 | Driver Roster, Qualification & Daily Pre-Trip Operations | VS-141 |
| W4253 | Transport Allowance, Service-Vehicle & Ride-Share/Van-Pool Operations | VS-141 |
| W4254 | Late-Night, Women-Safe & Special-Shift Transport Service | VS-141 |
| W4255 | Transport Incident, Breakdown & Passenger-Safety Response | VS-141 |
| W4256 | Transport Helpdesk, Employee Inquiry & Exception Handling | VS-141 |
| W4257 | Shuttle/Charter Vendor Sourcing, Qualification & Contracting | VS-141 |
| W4258 | Transport Vendor SLA, Performance & Rate Management | VS-141 |
| W4260 | Transport Compliance Audit, Vehicle Inspection & Insurance/License Registry | VS-141 |
| W4264 | Transport Program Performance Review & Reporting | VS-141 |
| W4313 | Employee Housing Strategy, Eligibility & Operating Model | VS-144 |
| W4314 | Housing Portfolio Planning, Lease-vs-Own & Site Selection | VS-144 |
| W4315 | Housing Policy, House Rules, Code of Conduct & Resident Agreement | VS-144 |
| W4316 | Housing Allocation, Assignment & Occupancy Entitlement | VS-144 |
| W4319 | Housing Governance, Compliance & Audit Framework | VS-144 |
| W4320 | Housing System & Resident Data Architecture (HR↔Facilities↔Finance) | VS-144 |
| W4321 | Dormitory Daily Operations, Check-In/Out & Front-Desk Management | VS-144 |
| W4322 | Occupancy Management, Bed Allocation & Waitlist | VS-144 |
| W4323 | Resident Welfare, Grievance & Conflict Resolution | VS-144 |
| W4324 | Housekeeping, Sanitation, Linen & Common-Area Operations | VS-144 |
| W4325 | Security, Access Control & Visitor Management | VS-144 |
| W4326 | Utilities, Water, Electricity & Internet Provisioning | VS-144 |
| W4328 | Resident Experience, Engagement & Retention Linkage | VS-144 |
| W4329 | Dormitory Preventive & Reactive Maintenance Operations | VS-144 |
| W4330 | Housing Vendor/Property-Manager Sourcing, Contract & SLA | VS-144 |
| W4332 | Housing Asset, Furniture/FF&E Lifecycle & Inventory | VS-144 |
| W4334 | Housing Closure, Move-Out Inspection & Deposit Refund | VS-144 |
| W4335 | Housing Compliance, LGU Permitting & Local Tax | VS-144 |
| W4457 | Drug-Free Workplace Strategy, Policy & Operating Model | VS-150 |
| W4461 | Drug-Free Workplace Training, Communication & Culture | VS-150 |
| W4462 | Drug Testing Consent, Privacy (RA 10173) & Confidentiality Framework | VS-150 |
| W4463 | Contractor/Agency/Contingent Workforce Coverage (links VS-98) | VS-150 |
| W4464 | Drug-Free Program Data, Records & System Architecture | VS-150 |
| W4465 | Pre-Employment Drug Testing (links VS-121 recruitment) | VS-150 |
| W4466 | Random Drug Testing — Selection, Notice & Execution | VS-150 |
| W4467 | Reasonable-Suspicion & For-Cause Drug Testing | VS-150 |
| W4468 | Post-Incident & Post-Accident Drug Testing (links VS-24/VS-147) | VS-150 |
| W4470 | MRO Review, Results Validation & Confirmation | VS-150 |
| W4471 | Positive/Refusal Result Case Management & Due Process | VS-150 |
| W4472 | Disciplinary, Separation & Legal (NLRC) Handling of Positive Cases | VS-150 |
| W4473 | Employee Assistance Program (EAP) & Referral to Rehabilitation | VS-150 |
| W4474 | Return-to-Duty, Return-to-Work Agreement & Follow-Up Testing | VS-150 |
| W4475 | Substance-Abuse Rehabilitation Provider Network & Coverage | VS-150 |
| W4476 | Confidentiality, Records Retention & RA 10173 Data Protection | VS-150 |
| W4479 | Drug-Impairment (Alcohol/Prescription/Cannabis-equivalent) Policy | VS-150 |
| W4697 | Global Mobility Strategy, Policy & Assignment-Tax Framework | VS-160 |
| W4698 | Assignment Types: Long-Term, Short-Term, Commuter, Localization & Business-Visitor Policy | VS-160 |
| W4699 | Mobility Cost-Budget, Package Design & Balance-Sheet vs. Lump-Sum | VS-160 |
| W4700 | Mobility Governance, Vendor (Relocation/Immigration Agent) Management | VS-160 |
| W4701 | Domestic Mobility, Transfers & Provincial Relocation Program | VS-160 |
| W4702 | Mobility Data, Systems & Assignment-Record Administration | VS-160 |
| W4704 | Cross-Border Assignment Security & Travel-Risk Linkage | VS-160 |
| W4706 | Bureau of Immigration 9G Pre-Arranged Employee Visa & ACR I-Card Processing | VS-160 |
| W4707 | Special Work Permit (SWP), Treaty-Trader (9D) & Other Visa Category Selection | VS-160 |
| W4708 | Sourcing-Agent, Secondment & Intra-Company Transferee Immigration | VS-160 |
| W4710 | Dependent & Family Visa, Schooling & Relocation Support | VS-160 |
| W4714 | Assignment Tax: Resident/Non-Resident, Tax-Treaty, 19-Series & Equalization | VS-160 |
| W4716 | Assignment Housing, Relocation & Settling-In Administration | VS-160 |
| W4717 | Assignment Performance, Engagement & Family-Wellbeing Support | VS-160 |
| W4718 | Assignment End, Repatriation & Localization Transition | VS-160 |
| W4865 | Workforce Vetting & Background-Screening Program Strategy & Operating Model | VS-167 |
| W4866 | Screening Policy, Role-Based Screening Matrix & Adverse-Action/Fair-Chance Framework | VS-167 |
| W4868 | Consent, RA 10173 Privacy & Data-Minimization Governance | VS-167 |
| W4869 | Screening-Package Design — NBI/Police/Court, Employment, Education, Credit, Sanctions | VS-167 |
| W4870 | Screening Quality Standards, SLA & Evidence Chain-of-Custody | VS-167 |
| W4871 | Program Governance, Separation-of-Duties, Adverse-Action Review Board & Appeals | VS-167 |
| W4873 | Employee Pre-Hire Screening Integration & Offer-Conditional Workflow | VS-167 |
| W4874 | Contingent/Outsourced Worker Screening Governance & Agency Accountability | VS-167 |
| W4875 | Vendor & 3PL Personnel Site-Access Vetting (Drivers, Delivery, Service) | VS-167 |
| W4876 | Executive & Sensitive-Role Enhanced Vetting | VS-167 |
| W4877 | Periodic Re-Screening, Continuous Monitoring & Triggered Re-Vet | VS-167 |
| W4878 | Cross-Entity (5 Entities) & Regional Screening Consistency & Transfer Handling | VS-167 |
| W4879 | Drug-Test, Health & License-Check Integration | VS-167 |
| W4880 | Adverse-Action Decisioning, Disqualification Handling & NLRC/Due-Process | VS-167 |
| W4882 | Insider-Risk Linkage — Screening to LP/Fraud/Security Event Correlation | VS-167 |
| W4883 | Screening Fraud & False-Document Detection (Forged Clearances/Credentials) | VS-167 |
| W4884 | Screening-Vendor/Agency Risk Management & TPRM | VS-167 |
| W4887 | Internal Audit Coordination, Control Testing & Compliance Assurance | VS-167 |

**Asset & Infrastructure** (153)

| ID | Workflow | Value Stream |
|---|---|---|
| W1295 | New Store Opening Readiness, Systems Go-Live & Staff Training Validation | VS-20 |
| W1403 | Store-Level Material Handling Equipment Inspection, Preventive Maintenance & Operator Safety Certification | VS-20 |
| W1427 | Store Expansion Pipeline Management, Site Readiness Milestone Tracking & Go-Live Checklist | VS-20 |
| W1445 | New Store Site Feasibility Assessment, Traffic Analysis, Competitive Mapping & Real Estate Due Diligence | VS-20 |
| W1564 | Store Waste Management, Construction Material Scrap Disposal, Cardboard Baling & Recycling Revenue Recovery | VS-20 |
| W1690 | New Fixed Asset Registration & Capitalization | VS-35 |
| W1691 | Asset Classification & Category Assignment | VS-35 |
| W1692 | Asset Tag & Label Generation & Application | VS-35 |
| W1693 | Asset Transfer Between Locations | VS-35 |
| W1694 | Asset Component & Sub-Asset Management | VS-35 |
| W1695 | Asset Maintenance Schedule & History Tracking | VS-35 |
| W1696 | Asset Lease vs. Buy Decision & Recording | VS-35 |
| W1697 | Asset Insurance Coverage Tracking & Linkage | VS-35 |
| W1698 | Monthly Depreciation Run & Journal Posting | VS-35 |
| W1699 | Depreciation Method Review & Useful Life Adjustment | VS-35 |
| W1700 | Impairment Assessment & Testing | VS-35 |
| W1701 | Revaluation of Fixed Assets | VS-35 |
| W1706 | Annual Fixed Asset Physical Verification (Wall-to-Wall Count) | VS-35 |
| W1707 | Spot Check & Rolling Asset Verification | VS-35 |
| W1708 | Asset Retirement & Disposal Processing | VS-35 |
| W1709 | Asset Write-Off Due to Loss, Theft or Damage | VS-35 |
| W1710 | Asset Sale, Trade-In & Salvage Processing | VS-35 |
| W1711 | Gain/Loss on Asset Disposal Recognition | VS-35 |
| W1712 | Asset Return to Vendor (Warranty Claim) | VS-35 |
| W1713 | Asset Register Cleanup & Archiving | VS-35 |
| W1854 | New Site Lease Negotiation & Execution | VS-42 |
| W1855 | Lease Agreement Registration, Document Management & Key Date Tracking | VS-42 |
| W1856 | Lease Renewal Negotiation & Extension Processing | VS-42 |
| W1857 | Lease Termination & Move-Out Coordination | VS-42 |
| W1858 | Landlord Relationship & Communication Management | VS-42 |
| W1859 | Lease Modification & Amendment Processing | VS-42 |
| W1860 | Sublease & Assignment Management | VS-42 |
| W1862 | Monthly Rent Payment Processing & Scheduling | VS-42 |
| W1863 | Annual Rent Escalation Execution & Verification | VS-42 |
| W1865 | Percentage Rent Calculation & Payment | VS-42 |
| W1866 | Rent Abatement & Concession Tracking | VS-42 |
| W1867 | Security Deposit Management & Return Processing | VS-42 |
| W1869 | Landlord Invoice Verification & Payment Exception Handling | VS-42 |
| W1870 | Real Property Tax (RPT) Assessment Review & Payment | VS-42 |
| W1874 | Property Insurance Portfolio Management & Annual Renewal | VS-42 |
| W1875 | Lease Accounting Policy Review & IFRS Update Assessment | VS-42 |
| W2262 | Store Performance Trigger Analysis | VS-59 |
| W2263 | Closure Business Case Development | VS-59 |
| W2264 | Closure Decision & Board Approval | VS-59 |
| W2266 | Closure Project Planning & Timeline | VS-59 |
| W2267 | Customer Migration Planning | VS-59 |
| W2268 | Vendor & Supplier Notification | VS-59 |
| W2269 | Closure Regulatory & LGU Compliance | VS-59 |
| W2270 | Inventory Liquidation Planning & Execution | VS-59 |
| W2271 | Fixed Asset Recovery & Disposal | VS-59 |
| W2272 | Lease Termination & Handover | VS-59 |
| W2273 | Employee Redeployment & Separation | VS-59 |
| W2274 | IT Systems Decommissioning | VS-59 |
| W2276 | Post-Closure Site Monitoring | VS-59 |
| W2277 | Closure Lessons Learned | VS-59 |
| W2278 | Redeployed Employee Onboarding at New Location | VS-59 |
| W2279 | Customer Migration Success Tracking | VS-59 |
| W2280 | Post-Closure Financial Impact Analysis | VS-59 |
| W2282 | Regional Sales Impact Assessment | VS-59 |
| W2283 | Employee Redeployment Success Metrics | VS-59 |
| W2285 | Closure Playbook Maintenance | VS-59 |
| W3185 | Property Portfolio Strategy & Investment Plan | VS-97 |
| W3186 | Site Acquisition & Real Estate Investment Underwriting | VS-97 |
| W3187 | Land & Building Purchase and Sale-and-Leaseback Origination | VS-97 |
| W3188 | Property Development, Ground-Up Construction & Tenant-Improvement Build-Out | VS-97 |
| W3189 | Investment Property Valuation & Fair-Value Measurement (PFRS 40) | VS-97 |
| W3190 | Real Estate Capital Stack & Financing Structuring | VS-97 |
| W3191 | Property Due Diligence, Title Transfer & ENC Acquisition | VS-97 |
| W3192 | Property Disposition & Portfolio Rationalization | VS-97 |
| W3194 | Commercial Tenant Acquisition & Lease Origination | VS-97 |
| W3195 | Rent Billing, CAM Recovery & Tenant Receivables | VS-97 |
| W3196 | Tenant Service, Maintenance & Relationship Management | VS-97 |
| W3197 | Lease Renewal, Escalation & Rent Review | VS-97 |
| W3198 | Vacancy Marketing & Space Commercialization | VS-97 |
| W3199 | Tenant Default, Eviction & Recovery | VS-97 |
| W3200 | Outlot, Pad & Ground Lease Management | VS-97 |
| W3201 | Property-Level P&L, NOI & Yield Reporting | VS-97 |
| W3202 | Real Property Tax, Assessment & LGU Compliance (as Owner) | VS-97 |
| W3203 | Capital Improvements, Repair Reserve & CAPEX Governance | VS-97 |
| W3204 | Property Insurance, Risk Transfer & Coverage Program | VS-97 |
| W3205 | Common Area, Grounds & Facility Operations Oversight | VS-97 |
| W3206 | Environmental, Zoning & Land-Use Compliance | VS-97 |
| W3449 | Renewable Generation Portfolio Strategy & Site Prioritization | VS-108 |
| W3450 | Site Feasibility, Solar Resource Assessment & Structural/Capacity Evaluation | VS-108 |
| W3451 | Business Case, Capex Funding & Financing/Incentive Structuring | VS-108 |
| W3452 | EPC Vendor Selection, Contracting & Project Management | VS-108 |
| W3453 | Equipment Procurement, PV/Inverter/BESS Specification & Quality | VS-108 |
| W3454 | Construction, Commissioning, Testing & Asset Acceptance | VS-108 |
| W3455 | Ownership-Model Selection: Own / Lease / PPA / RECOA Structuring | VS-108 |
| W3456 | Renewable Asset Registration, Capitalization & Handover to Operations | VS-108 |
| W3457 | Daily Generation Monitoring, SCADA & Performance Surveillance | VS-108 |
| W3459 | Asset Operations & Maintenance (O&M), Cleaning & Troubleshooting | VS-108 |
| W3460 | Inverter / BESS Fault Management & Vendor Warranty Resolution | VS-108 |
| W3461 | Grid Outage / Brownout Resilience & Islanding Operations | VS-108 |
| W3462 | ERC / DU Interconnection, Net-Metering Registration & Compliance | VS-108 |
| W3469 | Asset Lifecycle, Degradation & Renewable Refresh/Repower Planning | VS-108 |
| W3470 | ESG/Sustainability Disclosure & Climate Reporting Integration | VS-108 |
| W3471 | Renewable Portfolio Risk, Resilience & Insurance Governance | VS-108 |
| W3472 | Renewable Energy Program Strategy, Policy & Executive/Board Governance | VS-108 |
| W3737 | Energy Efficiency & Conservation Program Strategy & Governance | VS-120 |
| W3738 | RA 11285 Designated-Establishment Classification & DOE Registration | VS-120 |
| W3739 | Energy Efficiency Officer, Energy Manager & Energy Team Management | VS-120 |
| W3740 | Energy Policy, Targets & ISO 50001 Energy Management System | VS-120 |
| W3741 | Energy Data, Metering & Energy Accounting Infrastructure | VS-120 |
| W3742 | Energy Procurement, Retail Competition (RES) & Contract Management | VS-120 |
| W3743 | EEC Budget, Capex & Investment Governance | VS-120 |
| W3744 | EEC Policy, Authority & Records Management | VS-120 |
| W3745 | Mandatory Energy Audit & Audit-Firm Management | VS-120 |
| W3746 | Investment-Grade Energy Audit & ECM Identification | VS-120 |
| W3747 | Measurement & Verification (M&V) and Energy Performance Tracking | VS-120 |
| W3748 | Energy Conservation Plan Development & DOE Submission | VS-120 |
| W3749 | ECM Business Case, Prioritization & Investment Decision | VS-120 |
| W3751 | Behavioral, Organizational & Store-Level Energy Management | VS-120 |
| W3752 | Renewable, Self-Generation & Grid-Interaction Integration | VS-120 |
| W3753 | ECM Project Delivery, Commissioning & Handover | VS-120 |
| W3759 | Energy Compliance Audit & Assurance | VS-120 |
| W4169 | Facilities Management Strategy & Operating Model | VS-138 |
| W4170 | IFM Provider Strategy, Sourcing & Contract Management | VS-138 |
| W4171 | Facilities Service Catalog & SLA Framework | VS-138 |
| W4172 | Facilities Asset Register & Building Condition Management | VS-138 |
| W4173 | Preventive Maintenance Planning & Scheduling | VS-138 |
| W4174 | Facilities Helpdesk, Work-Order & Reactive Maintenance | VS-138 |
| W4175 | Facilities Compliance, Permits & Fire/Life-Safety Coordination | VS-138 |
| W4176 | Facilities Budget, Cost-to-Serve & Vendor Performance Governance | VS-138 |
| W4177 | Janitorial, Cleaning & Hygiene Service Operations | VS-138 |
| W4178 | Pest Control, Vector & Rodent Management | VS-138 |
| W4179 | Security Guarding Service Coordination & Site Protection | VS-138 |
| W4180 | Grounds, Landscaping & Exterior Maintenance | VS-138 |
| W4181 | Waste, Recycling & Utilities Coordination at Site | VS-138 |
| W4182 | Workplace Services — Cafeteria, Canteen & Employee Amenities | VS-138 |
| W4183 | Mailroom, Courier & Site Logistics Services | VS-138 |
| W4184 | Hard FM Trades — HVAC, Electrical, Plumbing & Fire Systems Service | VS-138 |
| W4187 | Space Management, Occupancy & Utilization | VS-138 |
| W4188 | Facilities Sustainability & Green-Building Operations | VS-138 |
| W4189 | Facilities Project & Minor-Works Management | VS-138 |
| W4190 | Site Opening/Closing Facilities Handover | VS-138 |
| W4770 | Charge-Point-Operator (CPO) & e-Mobility-Service-Partner Selection & Contracting | VS-163 |
| W4772 | Host-Revenue, Lease & Cost-Sharing Commercial Structure | VS-163 |
| W4773 | EV Customer Experience, Loyalty Integration & Drive-to-Store Basket Design | VS-163 |
| W4774 | Regulatory & Utility Engagement — ERC, RA 11697, Meralco/Cooperative, LGU | VS-163 |
| W4775 | Charging Tariff Design, Energy Pricing & Demand-Charge Management Strategy | VS-163 |
| W4776 | Network Expansion Governance, Capex Approval & Portfolio Prioritization | VS-163 |
| W4777 | EVSE Hardware Specification, Standards & Procurement | VS-163 |
| W4778 | Site Civil & Electrical Construction, EVSE Installation & Commissioning | VS-163 |
| W4779 | Utility Interconnection, Metering & Grid Service Connection | VS-163 |
| W4780 | Solar/Storage Integration & Behind-the-Meter Energy Coordination | VS-163 |
| W4781 | CSMS Backend, OCPP Configuration & Network Commissioning | VS-163 |
| W4782 | OCPI Roaming, eMSP Integration & Cross-Network Interoperability | VS-163 |
| W4783 | Payment, Access (RFID/App/QR) & Loyalty/Promotion Activation at the Charger | VS-163 |
| W4784 | Go-Live Readiness, Site Acceptance & Hypercare Handover | VS-163 |
| W4785 | Preventive Maintenance, Cleaning & EVSE Health Monitoring | VS-163 |
| W4788 | Accessibility, Bay Compliance & Customer-Assistance Operations | VS-163 |
| W4789 | Uptime/SLA Management, Availability Reporting & Penalty Administration | VS-163 |

**Governance & Assurance** (246)

| ID | Workflow | Value Stream |
|---|---|---|
| W1173 | High-Risk SKU Protection Plan & Product Security Fixture Deployment | VS-23 |
| W1174 | Loss Prevention Store Compliance Audit Program & Scoring | VS-23 |
| W1175 | Sustainable Packaging Reduction & Single-Use Plastic Elimination Program | VS-25 |
| W1176 | Green Procurement & Sustainable Vendor Certification Program | VS-25 |
| W1211 | Store-Level Vendor & Delivery Driver Access Control & Yard Security Protocol | VS-23 |
| W1212 | Store-Level Construction & Renovation Waste Recycling & Scrap Revenue Management | VS-25 |
| W1213 | Store-Level Flood Response, Water Damage Mitigation & Post-Flood Recovery Protocol | VS-26 |
| W1221 | Store-Level Typhoon Preparation, Merchandise Protection & Quick Response Protocol | VS-26 |
| W1223 | Store-Level Emergency Generator Operations & Extended Power Outage Management | VS-24 |
| W1247 | Outdoor Lumber Yard & Building Material Yard Theft Prevention & Surveillance | VS-23 |
| W1320 | Supplier ESG Due Diligence Assessment & Sustainable Procurement Qualification | VS-25 |
| W1328 | Third-Party Risk Assessment & Vendor Criticality Tiering | VS-21 |
| W1329 | Key Risk Indicator (KRI) Monitoring & Automated Alert Management | VS-21 |
| W1330 | Strategic Risk Scenario Planning & War Gaming Exercise | VS-21 |
| W1331 | Employee Volunteer Program Management, Tracking & Impact Measurement | VS-25 |
| W1332 | Indigenous Peoples (IP) & Cultural Sensitivity Compliance for Store Expansion | VS-25 |
| W1333 | Stakeholder Engagement Matrix & Materiality Assessment Refresh | VS-25 |
| W1335 | Extended Producer Responsibility (EPR) Compliance, Plastic Packaging Tracking & Recovery Target Reporting | VS-25 |
| W1336 | Return Fraud & Abuse Pattern Detection, Investigation & Prevention | VS-23 |
| W1337 | Organized Retail Crime (ORC) Intelligence Network, Case Management & Law Enforcement Coordination | VS-23 |
| W1386 | Typhoon Early Warning Response, Store Pre-Closure Preparation & Post-Disaster Assessment | VS-24 |
| W1387 | Store-Level Flood Response, Inventory Elevation Protocol & Water Damage Recovery | VS-24 |
| W1388 | Store CCTV System Daily Health Check, Footage Retention & Incident Retrieval Processing | VS-23 |
| W1389 | Store After-Hours Burglary Alarm Response, Police Coordination & Incident Documentation | VS-23 |
| W1447 | Store-Level Construction Material Pallet, Packaging & Wooden Crate Recovery & Supplier Return Program | VS-25 |
| W1450 | Earthquake Response Protocol, Structural Assessment & Store Reopening Safety Verification | VS-26 |
| W1461 | Supply Chain Disruption Risk Monitoring & Geopolitical Alert Management | VS-21 |
| W1462 | Store-Level Cash Handling Risk Assessment & Robbery/Fraud Incident Response | VS-21 |
| W1475 | Coupon & Promotional Discount Abuse Detection, Pattern Analysis & Prevention | VS-23 |
| W1476 | Gift Card & Store Credit Fraud Detection, Balance Manipulation Investigation & Controls | VS-23 |
| W1477 | Key & Access Credential Management, Master Key System & Store Lock Rotation | VS-23 |
| W1478 | DC Perimeter Security, Gate Access Control & Visitor Management System | VS-23 |
| W1479 | Disaster Relief & Community Resilience Program Coordination & Emergency Product Distribution | VS-25 |
| W1480 | Supplier Diversity Program, Small & Medium Enterprise (SME) Vendor Development & Capacity Building | VS-25 |
| W1497 | Store-Level Anti-Theft Cable & Sensor Tag Deployment, Deactivation Compliance & Equipment Maintenance | VS-23 |
| W1528 | Store-Level Construction Material High-Value Shrinkage Hotspot Monitoring & Intervention | VS-23 |
| W1530 | Store-Level Rainwater Harvesting System, Green Infrastructure Initiative & Sustainability Demonstration Management | VS-25 |
| W1542 | Organized Retail Crime (ORC) Pattern Detection, Multi-Store Correlation & Law Enforcement Coordination | VS-23 |
| W1552 | Typhoon Post-Event Rapid Store Damage Assessment, Safety Clearance & Phased Reopening Protocol | VS-26 |
| W1566 | Store-Level Slip-and-Fall, Customer Injury & Third-Party Liability Incident Response & Claims Management | VS-26 |
| W1601 | Store-Level DSD Quality Verification | VS-31 |
| W1602 | Import Shipment Pre-Delivery Inspection (PDI) | VS-31 |
| W1603 | Batch / Lot Quality Hold & Release | VS-31 |
| W1604 | AQL Sampling Plan Configuration & Category Management | VS-31 |
| W1605 | Paint & Chemical Product Quality Verification | VS-31 |
| W1606 | Electrical Product Safety Verification & Certification Check | VS-31 |
| W1607 | Lumber & Building Materials Dimensional & Structural Quality Check | VS-31 |
| W1609 | Annual Vendor Quality Audit Program | VS-31 |
| W1611 | New Vendor Quality Qualification & First Article Inspection | VS-31 |
| W1612 | Vendor Certification & Compliance Document Tracking | VS-31 |
| W1613 | Import Vendor Quality & Compliance Pre-Shipment Verification | VS-31 |
| W1614 | Quality Cost Analysis & Vendor Chargeback Processing | VS-31 |
| W1619 | Product Safety Complaint Triage & Escalation | VS-31 |
| W1620 | Product Safety Testing & Certification Renewal Management | VS-31 |
| W1621 | Consumer Product Safety Monitoring & Market Surveillance | VS-31 |
| W1646 | Annual Budget Preparation & Bottoms-Up Forecasting | VS-33 |
| W1647 | Store-Level Annual Target Setting & P&L Budget Allocation | VS-33 |
| W1648 | Capital Expenditure Budget Planning & Prioritization | VS-33 |
| W1649 | Department Annual Operating Plan Development | VS-33 |
| W1650 | Budget Approval, Board Presentation & Communication | VS-33 |
| W1651 | Mid-Year Budget Review & Recalibration | VS-33 |
| W1652 | New Store Financial Model & Pre-Opening Budget Planning | VS-33 |
| W1653 | Monthly Executive Performance Review (Operating Review) | VS-33 |
| W1656 | Category Manager Monthly Performance Review & Margin Ownership | VS-33 |
| W1657 | Quarterly Board Performance Report & Governance Package | VS-33 |
| W1658 | Annual Performance Assessment & Incentive Compensation Calculation | VS-33 |
| W1659 | KPI Definition, Target Setting & Cascading Framework | VS-33 |
| W1660 | Cross-Functional Initiative Tracking & Status Reporting | VS-33 |
| W1662 | Market & Industry Trend Monitoring | VS-33 |
| W1665 | New Market Entry & Store Location Feasibility Analysis | VS-33 |
| W1666 | Philippine Retail Regulatory & Policy Impact Assessment | VS-33 |
| W1667 | Competitive Intelligence Quarterly Briefing & Strategy Input | VS-33 |
| W1714 | Quarterly Board Meeting Scheduling & Agenda Preparation | VS-36 |
| W1715 | Board Meeting Materials Preparation & Distribution | VS-36 |
| W1716 | Board Meeting Minutes Recording & Approval | VS-36 |
| W1717 | Corporate Resolution Generation & Authentication | VS-36 |
| W1719 | Corporate Record Retention & Document Management | VS-36 |
| W1720 | Related-Party Transaction Identification & Disclosure | VS-36 |
| W1721 | Board Committee Management & Reporting | VS-36 |
| W1722 | Stock & Transfer Ledger Management | VS-36 |
| W1723 | Annual Stockholders' Meeting Preparation & Conduct | VS-36 |
| W1725 | Dividend Declaration & Distribution | VS-36 |
| W1726 | Capital Increase & Stock Issuance | VS-36 |
| W1727 | Officer & Director Appointment & Changes | VS-36 |
| W1728 | Corporate Entity Registration & Amendment | VS-36 |
| W1729 | Corporate Policy Development & Approval | VS-36 |
| W1730 | Annual Corporate Governance Self-Assessment | VS-36 |
| W1732 | Corporate Signing Authority & Delegation of Authority Matrix | VS-36 |
| W1733 | Whistleblower & Ethics Reporting Channel Management | VS-36 |
| W1734 | Conflict of Interest Disclosure & Management | VS-36 |
| W1736 | Corporate Social Responsibility Oversight | VS-36 |
| W2599 | Cardboard & Paper Waste Baling & Recycling Revenue | VS-73 |
| W2600 | Plastic & Shrink Wrap Waste Management | VS-73 |
| W2601 | Pallet & Wood Waste Recovery & Reuse | VS-73 |
| W2602 | Lumber Yard Waste & Offcut Management | VS-73 |
| W2604 | Construction & Renovation Waste Management | VS-73 |
| W2606 | Paint & Chemical Waste Storage & Disposal | VS-73 |
| W2607 | Solvent & Flammable Material Waste Handling | VS-73 |
| W2608 | Battery & Lead-Acid Waste Management | VS-73 |
| W2610 | Mercury-Containing Waste Disposal | VS-73 |
| W2612 | Hazardous Waste Compliance Audit & Record Keeping | VS-73 |
| W2613 | Asbestos & Special Hazardous Material Handling | VS-73 |
| W2614 | Vendor Packaging Take-Back Program Management | VS-73 |
| W2617 | Store-Level Composting & Organic Waste Program | VS-73 |
| W2618 | Customer Reusable Bag & Packaging Reduction Program | VS-73 |
| W2620 | Community Recycling Partnership & Education Program | VS-73 |
| W2621 | Waste-to-Energy Feasibility & Biomass Program | VS-73 |
| W2673 | Barangay Clearance & Community Relations Management | VS-76 |
| W2674 | Signage & Billboard Permit Management | VS-76 |
| W2676 | Store Location Tax & Fee Variance Tracking | VS-76 |
| W2678 | Local Business Tax Computation & Payment Across LGUs | VS-76 |
| W2679 | Real Property Tax Assessment & Payment | VS-76 |
| W2680 | LGU Regulatory Change Monitoring & Impact Assessment | VS-76 |
| W2683 | Philippine Competition Law Compliance | VS-76 |
| W2686 | LGU Official Relationship & Engagement Management | VS-76 |
| W2688 | LGU Regulatory Compliance Audit & Gap Analysis | VS-76 |
| W2689 | LGU Incentive & Investment Promotion Evaluation | VS-76 |
| W2690 | Store-Level Regulatory Issue Escalation & Resolution | VS-76 |
| W2691 | LGU Regulatory Intelligence Network | VS-76 |
| W2925 | Adverse Media, Reputation & Legal Risk Check | VS-86 |
| W2929 | Cash Transaction Monitoring & Covered Transaction (PHP 500K Single-Day) Detection | VS-86 |
| W2933 | Structuring / Smurfing Pattern Detection & Investigation | VS-86 |
| W2934 | Trade-Based Money Laundering (TBML) Monitoring for Import/Export | VS-86 |
| W2937 | ABC Policy Maintenance, Risk Assessment & Training | VS-86 |
| W2938 | Gifts, Hospitality & Entertainment Register & Approval | VS-86 |
| W2939 | Facilitation Payment, Solicitation & Extortion Reporting | VS-86 |
| W2940 | Conflict of Interest Disclosure & Annual Declaration | VS-86 |
| W2941 | Government Interaction, Public Official Engagement & Procurement Integrity | VS-86 |
| W2942 | Third-Party Intermediary (Agent/Consultant) Due Diligence & ABC Controls | VS-86 |
| W2943 | ABC Investigation, Whistleblower Coordination & Remediation | VS-86 |
| W2944 | ABC Program Assurance, Metrics & Board Reporting | VS-86 |
| W2949 | Rules of Origin Determination (AFTA/RCEP/ATIGA) | VS-87 |
| W2950 | Country of Origin Marking & Labeling Compliance | VS-87 |
| W2953 | FTA Preference Strategy & Annual Duty Savings Analysis | VS-87 |
| W2955 | Duty Drawback Scheme Application & Re-export Processing | VS-87 |
| W2958 | Duty Deferment, Bond & Guarantee Management | VS-87 |
| W2959 | Tariff-Rate Quota (TRQ) & Safeguard Duty Monitoring | VS-87 |
| W2960 | Freeport / Economic Zone Sourcing Strategy & Incentive Coordination | VS-87 |
| W2964 | Anti-Dumping & Countervailing Duty (ADC/CVD) Compliance | VS-87 |
| W2966 | Trade Compliance Risk Register & Control Self-Assessment | VS-87 |
| W2968 | Trade Compliance KPI, Duty Cost & Savings Reporting | VS-87 |
| W2969 | Enterprise Document Taxonomy & Classification Scheme Maintenance | VS-88 |
| W2970 | Document Capture, Indexing & Metadata Tagging | VS-88 |
| W2971 | Version Control, Check-Out/In & Authoritative Source Management | VS-88 |
| W2972 | Document Access Control, Permissions & Confidentiality Tiering | VS-88 |
| W2974 | Digital Repository Architecture, Search & Records Declaration | VS-88 |
| W2976 | Document Quality, Duplicate Detection & Cleanup | VS-88 |
| W2978 | Retention Clock Start, Pause & Event-Driven Extension | VS-88 |
| W2980 | Disposition Review, Approval & Secure Destruction Execution | VS-88 |
| W2981 | Physical Records Destruction (Shredding/Pulping) & Certificate of Destruction | VS-88 |
| W2982 | Digital Records Crypto-Shredding & Backup Purge | VS-88 |
| W2990 | Litigation Records Management & Chain of Custody | VS-88 |
| W2991 | Records Compliance Audit, Self-Assessment & CAP | VS-88 |
| W2992 | Records Management KPI, Cost & Maturity Reporting | VS-88 |
| W4361 | Service-Quality Assurance Strategy, Scope & Operating Model | VS-146 |
| W4362 | Service Standards, Customer-Journey Touchpoint Definition & Scoring Rubric | VS-146 |
| W4363 | Mystery Shopping & Service-Audit Program Design & Methodology | VS-146 |
| W4365 | Service-Quality Governance, Independence & Ethics Framework | VS-146 |
| W4366 | Service-Quality Vendor (Mystery-Shop Agency) Selection & Contract | VS-146 |
| W4367 | Service-Quality Compliance, RA 10173 Consent & Data Privacy | VS-146 |
| W4368 | Service-Quality System & Measurement Data Architecture | VS-146 |
| W4369 | Mystery-Shop Visit Scheduling, Scenario & Shopper Deployment | VS-146 |
| W4370 | In-Store Mystery Shopping Execution & Evidence Capture | VS-146 |
| W4371 | Omnichannel, Ecommerce & Digital Mystery-Shop & Service Test | VS-146 |
| W4372 | B2B/Trade/Field-Sales & Phone/Contact-Center Service Audit | VS-146 |
| W4373 | Service Recovery/Complaint-Handling & Recovery Audit | VS-146 |
| W4374 | Internal Service Audit, Store Walkthrough & Standards Compliance Check | VS-146 |
| W4376 | Findings Triage, Severity Classification & Escalation | VS-146 |
| W4378 | Root-Cause Service Failure Analysis & Remediation Plan | VS-146 |
| W4379 | Service Recognition, Incentive & Performance Linkage | VS-146 |
| W4380 | Service-Finding Dispute, Validation & Appeal | VS-146 |
| W4381 | Mystery-Shopper Integrity, Fraud & Collusion Control | VS-146 |
| W4383 | Service-Quality Reporting to Leadership & Board Assurance | VS-146 |
| W4385 | Customer Safety & Premises-Liability Strategy, Scope & Operating Model | VS-147 |
| W4386 | Customer Safety Standards, Hazard Register & Risk Assessment | VS-147 |
| W4387 | Premises-Liability, Insurance & Legal Framework | VS-147 |
| W4388 | Customer Safety Governance, Roles & Accountability (RACI) | VS-147 |
| W4389 | Customer Safety by Zone — Sales Floor, Yard, Lumber/Tile & Parking Design | VS-147 |
| W4390 | Contractor, Vendor & Third-Party On-Premises Safety Accountability | VS-147 |
| W4392 | Customer Safety Data, Incident System & Measurement Architecture | VS-147 |
| W4393 | Daily Store Safety Inspection, Hazard Hunt & Housekeeping | VS-147 |
| W4394 | Aisle, Merchandise-Stack & Falling-Stock Safety Control | VS-147 |
| W4395 | Powered Equipment (Forklift/Reach/Order-Picker) In-Sales-Area Safety | VS-147 |
| W4396 | Parking Lot, Exterior & Site-Access Customer Safety | VS-147 |
| W4397 | Chemical, Paint & Hazmat Customer Exposure Control (In-Store) | VS-147 |
| W4398 | Customer Safety Signage, Wayfinding & Barrier Management | VS-147 |
| W4399 | Crowding, Queue & Peak-Period (Sale-Event) Customer Safety | VS-147 |
| W4401 | Customer Incident & Accident Response (First Aid, Stabilize, Secure) | VS-147 |
| W4402 | Customer Incident Investigation, Documentation & Root Cause | VS-147 |
| W4403 | Customer Injury/Premises-Liability Claim Handling & TPA Liaison | VS-147 |
| W4404 | Customer-Safety Corrective & Preventive Action (CAPA) | VS-147 |
| W4406 | Customer-Safety Training, Drills & Competency | VS-147 |
| W4407 | Customer-Safety Audit, Assurance & Board Reporting | VS-147 |
| W4505 | CSR Strategy, Pillars & Social-License Framework | VS-152 |
| W4508 | CSR Budgeting, Endowment & Fund Allocation Governance | VS-152 |
| W4509 | CSR Policy, Code of Conduct & Partnership Ethics Standard | VS-152 |
| W4510 | CSR Operating Model, Staffing & Field Network | VS-152 |
| W4511 | CSR Risk, Safeguarding & Whistleblower Linkage | VS-152 |
| W4512 | CSR Data, Systems & Integration Architecture | VS-152 |
| W4513 | Community-Needs Assessment & Partnership Identification | VS-152 |
| W4514 | Housing, Shelter & "Home Building Partner" Community Programs | VS-152 |
| W4515 | Livelihood, Skills & Cooperative Development Programs | VS-152 |
| W4516 | Education, School-Build & Vocational Support Programs | VS-152 |
| W4517 | Community Disaster Relief & Resilience Programs | VS-152 |
| W4519 | NGO, LGU & Multilateral Partnership Management | VS-152 |
| W4520 | In-Kind Donation, Product-Giving & Logistics Operations | VS-152 |
| W4521 | CSR Impact Measurement, Logic Model & Outcome Tracking | VS-152 |
| W4522 | Social Return on Investment (SROI) & Benefit Valuation | VS-152 |
| W4525 | Community & Beneficiary Stakeholder Engagement | VS-152 |
| W4526 | Customer & Employee CSR Communication & Engagement | VS-152 |
| W4527 | CSR Brand, Reputation & Greenwashing-Risk Management | VS-152 |
| W4721 | Enterprise Third-Party Inventory & Relationship Register | VS-161 |
| W4722 | TPRM Framework, Risk Taxonomy & Cross-Domain Risk Appetite | VS-161 |
| W4723 | Third-Party Tiering & Criticality Methodology (Inherent/Residual, All Domains) | VS-161 |
| W4724 | Fourth-Party (Sub-Processor / Sub-Contractor) Risk Identification & Mapping | VS-161 |
| W4725 | Concentration, Single-Source & Geographic Risk Exposure Analysis | VS-161 |
| W4726 | Third-Party Data Classification & Data-Access/Processing Risk Scoping | VS-161 |
| W4727 | Third-Party Financial, Solvency & ESG/Human-Rights Risk Screening | VS-161 |
| W4728 | TPRM Governance, Ownership Matrix & Board Reporting | VS-161 |
| W4729 | Risk-Based Due Diligence Library & Assessment Workflow (Pre-Contract & Periodic) | VS-161 |
| W4731 | Data-Privacy & Processor Due Diligence (DPA, Transfer Mechanism) | VS-161 |
| W4734 | Continuous Monitoring Platform: Financial, Cyber, Compliance, Performance Feed | VS-161 |
| W4735 | Attestation, Certification & Insurance (COI) Renewal Tracking Lifecycle | VS-161 |
| W4736 | Third-Party Incident, Breach & Performance-Degradation Handling | VS-161 |
| W4737 | Concentration-Risk Mitigation: Dual-Source, Multi-Vendor & Alternate Qualification | VS-161 |
| W4738 | Critical-Third-Party Resilience, Stress-Test & Tabletop Exercise | VS-161 |
| W4739 | Third-Party Exit, Transition & Succession Planning | VS-161 |
| W4740 | Offboarding, Data-Return/Deletion & Access-Revocation Assurance | VS-161 |
| W4741 | TPRM Findings, Remediation & Corrective-Action Tracking | VS-161 |
| W4841 | Regulatory License/Permit Portfolio Strategy & Operating Model | VS-166 |
| W4843 | Regulatory Intelligence — Obligation Mapping by Site/Entity/Activity | VS-166 |
| W4844 | License/Permit Governance, Ownership Matrix & Accountability | VS-166 |
| W4846 | Evidence Repository, Document-of-Record & Audit Trail | VS-166 |
| W4847 | Regulatory Change Monitoring & Impact-to-Portfolio Assessment | VS-166 |
| W4848 | Portfolio Risk Tiering, Single-Points-of-Failure & Resilience | VS-166 |
| W4849 | Renewal-Cycle Execution & Cross-Domain Coordination | VS-166 |
| W4851 | New-Site/New-Activity License Acquisition Coordination | VS-166 |
| W4852 | Regulator Inspection/Audit Coordination, Calendar & Response Hub | VS-166 |
| W4853 | Expiring/Lapsed Permit Remediation & Business-Continuity Workaround | VS-166 |
| W4854 | Third-Party Permit/Compliance Service-Provider (Fixer/Consultant/Agent) Management | VS-166 |
| W4855 | Inter-Agency Coordination & Multi-Permit Concurrent Renewals | VS-166 |
| W4856 | Permit Variation, Scope Change & Site-Transfer/Closure Handling | VS-166 |
| W4858 | Penalty/Fine Management, Dispute Resolution & Regulatory-Debt Tracking | VS-166 |
| W4860 | Audit-Ready Evidence, Regulator Data Requests & Subpoena Response | VS-166 |
| W4861 | License/Permit Data Governance, Master-Data Sync & Duplicates Cleanup | VS-166 |
| W4863 | Internal Audit Coordination, Control Testing & SOX/COSO-Style Assurance | VS-166 |

**Technology & Data** (72)

| ID | Workflow | Value Stream |
|---|---|---|
| W1177 | Enterprise Data Governance Council, Standards & Stewardship Program | VS-28 |
| W1340 | Conversational AI Customer Service Chatbot Lifecycle Management & Escalation | VS-30 |
| W1391 | Master Data Duplicate Detection, Merge Processing & Golden Record Management | VS-28 |
| W1398 | Customer Churn Prediction Model, At-Risk Account Identification & Proactive Retention Campaign | VS-28 |
| W1399 | Store-Level Sales Forecasting Accuracy Monitoring, Model Drift Detection & Retraining Trigger | VS-28 |
| W1408 | ERP User Access Quarterly Review, Segregation of Duties (SoD) Audit & Excessive Access Remediation | VS-27 |
| W1409 | IT Change Advisory Board (CAB) Weekly Review, Risk Assessment & Deployment Approval | VS-27 |
| W1459 | Store Operations SOP Digital Library, Mobile Access & Version-Controlled Update Distribution | VS-30 |
| W1460 | Customer-Facing Project Guide & DIY Tutorial Content Management & Publishing | VS-30 |
| W1482 | Master Data Change Impact Analysis, Propagation Tracking & Downstream Notification | VS-28 |
| W1483 | Vendor Document Portal, Compliance Certificate Tracking & Expiration Alert Management | VS-30 |
| W1484 | Employee Onboarding Knowledge Path, Role-Based Training Curriculum & Competency Assessment | VS-30 |
| W1532 | Seasonal SKU Lifecycle Master Data Setup, Phase-In/Phase-Out Calendar & Attribute Management | VS-29 |
| W3234 | Hardware Procurement, Standardization & Catalog Management | VS-99 |
| W3235 | Device Provisioning, Imaging & Deployment | VS-99 |
| W3236 | Mobile Device, RF Gun & Peripheral Management | VS-99 |
| W3237 | Asset Maintenance, Break/Fix & Spare Pool Management | VS-99 |
| W3238 | Technology Refresh, Replacement Cycle & Rollout | VS-99 |
| W3239 | Asset Retirement, Data Sanitization & E-Waste Disposal | VS-99 |
| W3240 | Lost / Stolen Asset Recovery & Loss Investigation | VS-99 |
| W3241 | Software & License Entitlement Inventory | VS-99 |
| W3243 | SaaS Subscription & Cloud Application Portfolio Management | VS-99 |
| W3245 | Vendor True-Up, Renewal & Contract Management | VS-99 |
| W3246 | Software Compliance Audit Response & Defense | VS-99 |
| W3248 | License Forecasting & Software Budget Planning | VS-99 |
| W3249 | IT Asset Security Hardening & Configuration Baseline | VS-99 |
| W3250 | End-of-Life / Vulnerable Asset Remediation | VS-99 |
| W3252 | Asset Utilization, Right-Sizing & Chargeback | VS-99 |
| W3253 | ITAM Governance, Policy & Stewardship Program | VS-99 |
| W3255 | IT Vendor & Hardware Warranty Management | VS-99 |
| W3256 | Technology Asset Risk Register & Audit Support | VS-99 |
| W3935 | AI/ML Budget, Platform & Talent Strategy | VS-128 |
| W3943 | AI Incident Management & Adverse-Outcome Response | VS-128 |
| W3944 | AI Regulatory & Standards Monitoring (ISO 42001, NIST AI RMF, future PH AI rules) | VS-128 |
| W3945 | AI/ML Development Lifecycle & Responsible-by-Design Controls | VS-128 |
| W3946 | AI Testing, Evaluation & Pre-Deployment Assurance | VS-128 |
| W3947 | AI Monitoring, Drift Detection & Performance in Production | VS-128 |
| W3948 | AI Change, Re-training & Model Retirement | VS-128 |
| W3950 | AI Security, Adversarial Threats & Data Protection | VS-128 |
| W4097 | Technology Business Management (TBM) Framework & Cost Taxonomy | VS-135 |
| W4098 | Annual IT Budget Planning, Zero-Based & Capacity-Based Budgeting | VS-135 |
| W4099 | Technology Investment Portfolio & Capex/Opex Planning | VS-135 |
| W4101 | IT Demand Management & Intake / Prioritization | VS-135 |
| W4102 | Technology Cost Allocation, Showback / Chargeback to Business Units | VS-135 |
| W4103 | Application Portfolio Rationalization & Run-Cost Analysis | VS-135 |
| W4104 | Software License & Subscription Entitlement Planning | VS-135 |
| W4105 | Cloud FinOps Operating Model & FinOps Culture (Inform / Optimize / Operate) | VS-135 |
| W4106 | Cloud & SaaS Spend Visibility, Unit Economics & Forecasting | VS-135 |
| W4108 | Waste Elimination, Idle Resource & Storage Cost Reduction | VS-135 |
| W4109 | Cloud Cost Anomaly Detection & Budget Alerting | VS-135 |
| W4111 | Technology Procurement, Contract Negotiation & Vendor Spend | VS-135 |
| W4112 | Shadow IT Discovery & Technology Spend Governance | VS-135 |
| W4113 | Technology Value Realization & Benefit Tracking | VS-135 |
| W4116 | Cloud Carbon & Sustainability Footprint of Technology | VS-135 |
| W4118 | IT Audit & Compliance for Technology Spend | VS-135 |
| W4119 | Technology Financial Risk, FX & Commitment Exposure Management | VS-135 |
| W4483 | Label & Price-Tag Format Specification and Artwork Standards | VS-151 |
| W4484 | EAS/RFID Tag Selection & SKU-Tagging Policy | VS-151 |
| W4485 | Print/Scan/RFID Hardware Standard & Vendor Selection | VS-151 |
| W4488 | Auto-ID Change Control, Synchronization & Master-Data Handshake | VS-151 |
| W4489 | Label Production Fleet Operations & Consumable Management | VS-151 |
| W4490 | Centralized Label/Price-Tag Print Job Management | VS-151 |
| W4491 | Shelf-Edge Label & Planogram Price Application | VS-151 |
| W4492 | Hang-Tag, Adhesive & Bulk-Yard Tag Application | VS-151 |
| W4493 | Price-Change & Promotional Re-Labeling Execution | VS-151 |
| W4495 | Markdown, Clearance & Seasonal Transition Labeling | VS-151 |
| W4497 | EAS System Operations (Gates, Deactivators, Exception Alerts) | VS-151 |
| W4498 | Source-Tagging & Vendor-Applied EAS/RFID Program | VS-151 |
| W4499 | RFID Infrastructure, Encoding & Read-Zone Operations | VS-151 |
| W4501 | EAS Exception Response, Detention & Investigation Handoff | VS-151 |
| W4502 | Auto-ID Data Integration to Loss-Prevention & Inventory Systems | VS-151 |
| W4504 | Auto-ID Security, Privacy & Fraud-Vector Control | VS-151 |

#### Tier 3 (328)

**Plan & Source** (26)

| ID | Workflow | Value Stream |
|---|---|---|
| W1224 | Vendor Quarterly Business Review, Scorecard Meeting & Strategic Relationship Management | VS-3 |
| W1265 | Private Label Product Lifecycle Management, Quality Governance & Brand Performance Analytics | VS-1 |
| W1487 | Store Garden Center & Plant Nursery Seasonal Assortment Rotation, Vendor-Managed Inventory & Markdown Optimization | VS-1 |
| W1513 | Private Label Supplier Performance Scorecard, Quality Audit & Range Refresh Management | VS-1 |
| W1833 | Private Label Cost Modeling, Pricing Strategy & Margin Target Setting | VS-41 |
| W1850 | Private Label Customer Perception Survey & Brand Health Tracking | VS-41 |
| W1851 | Private Label Competitor Benchmarking & Market Positioning Review | VS-41 |
| W1944 | VMI Inventory Carrying Cost & Optimization Analysis | VS-45 |
| W1945 | Consignment & VMI Dashboard & Executive Reporting | VS-45 |
| W2454 | Vendor KPI Framework Management | VS-67 |
| W2457 | Vendor Survey & Qualitative Assessment | VS-67 |
| W2459 | Vendor Scorecard Data Quality Audit | VS-67 |
| W2461 | Vendor KPI Benchmarking & Industry Comparison | VS-67 |
| W2468 | Vendor Scorecard System Enhancement | VS-67 |
| W2476 | Vendor Innovation Partnership Program | VS-67 |
| W2477 | Vendor Development ROI Measurement | VS-67 |
| W3136 | Cooperative Program Performance & ROI Analytics | VS-94 |
| W3803 | Freight & Route Optimization for Import Sourcing | VS-122 |
| W3805 | Import Vendor Performance Analytics & Scorecard | VS-122 |
| W3806 | Sourcing Agent / Overseas-Office Performance & Value Analytics | VS-122 |
| W3909 | Promotional & Event Demand Modeling | VS-127 |
| W3911 | Forecast Accuracy Measurement & Bias Correction | VS-127 |
| W3917 | Scenario Modeling & What-If Analysis | VS-127 |
| W4006 | Modern Slavery, Forced Labor & Child Labor Risk Modeling | VS-131 |
| W4019 | Human Rights KPI, Performance Management & Analytics | VS-131 |
| W4024 | Human Rights Program Maturity, Continuous Improvement & Emerging Regulation | VS-131 |

**Make & Move** (65)

| ID | Workflow | Value Stream |
|---|---|---|
| W1258 | Multi-Location Inventory Aging Dashboard & Automated Write-Down Recommendation Engine | VS-5 |
| W1315 | Delivery Vehicle Loading Optimization, Weight Compliance & LTFRB Regulation Adherence | VS-6 |
| W1439 | Third-Party Logistics (3PL) Partner Quarterly Business Review, Rate Benchmarking & Contract Optimization | VS-6 |
| W1440 | Fuel Price Volatility Impact Assessment, Freight Cost Adjustment & Route Efficiency Optimization | VS-6 |
| W1628 | Customer Return Trend Analysis & Fraud Detection | VS-32 |
| W1644 | Returns Financial Analytics & Cost-to-Serve Reporting | VS-32 |
| W2196 | 3PL Partner Performance Scorecard | VS-56 |
| W2204 | Multi-Stop Route Optimization | VS-56 |
| W2208 | 3PL Cost Benchmarking | VS-56 |
| W2209 | Route Cost Optimization | VS-56 |
| W2213 | Total Delivery Cost Dashboard | VS-56 |
| W2311 | Fuel Price Monitoring & Procurement Optimization | VS-61 |
| W2313 | Fuel Consumption Reporting & Analytics | VS-61 |
| W2318 | Toll Expense Management & Optimization | VS-61 |
| W2321 | Route Cost Benchmarking | VS-61 |
| W2325 | Total Fleet Cost of Ownership Dashboard | VS-61 |
| W2331 | 3PL Cost Benchmarking & Negotiation | VS-61 |
| W2802 | Smart Safe Cash Drop, Validation & CIT-Ready Flagging | VS-81 |
| W2811 | In-Transit Custody Chain, GPS Telematics & Route Monitoring | VS-81 |
| W2820 | Cash Forecasting, Bank Sweep & Liquidity Optimization | VS-81 |
| W2823 | Cash Logistics Cost-to-Serve & Channel Benchmarking | VS-81 |
| W2824 | Cash Operations Maturity, Automation & Innovation Roadmap | VS-81 |
| W3024 | Damage Trend Analysis & Root Cause Reporting | VS-90 |
| W3032 | Vendor/Carrier Claim Aging, Recovery Analytics & Scorecard Feed | VS-90 |
| W3039 | Enterprise Damage & Claims Recovery Dashboard & KPI Reporting | VS-90 |
| W3084 | Kit/Bundle Sell-Through, Attachment & Cannibalization Analytics | VS-92 |
| W3086 | Customer Bundle Uptake, Basket Analysis & Cross-Sell Optimization | VS-92 |
| W3087 | Competitor Bundle Benchmarking & Response | VS-92 |
| W3088 | Kit/Bundle Performance Review & Portfolio Optimization | VS-92 |
| W3098 | Multi-Order Batch Picking & RF/Automation-Guided Walk Optimization | VS-93 |
| W3107 | Dark Store Throughput, Utilization & Labor Productivity Analytics | VS-93 |
| W3111 | Dark Store Service Level & Customer Experience Analytics | VS-93 |
| W3112 | Dark Store Sustainability, Energy & Waste Optimization | VS-93 |
| W3512 | Carrier Performance Scorecard & Quarterly Business Review | VS-110 |
| W3516 | Freight Cost-to-Serve & Lane Profitability Analytics | VS-110 |
| W3518 | Freight Cost Reduction & Continuous Improvement Program | VS-110 |
| W3528 | Packaging Cost, Bill of Material & Lifecycle Analytics | VS-111 |
| W3537 | Packaging Waste Reduction & Circular Economy | VS-111 |
| W3540 | Packaging Damage Analytics & Root Cause | VS-111 |
| W3541 | Packaging Cube / Freight Optimization Analytics | VS-111 |
| W3542 | Total Cost of Packaging & ROI Analytics | VS-111 |
| W3544 | Packaging Innovation & Program Governance | VS-111 |
| W4122 | Network Modeling, Scenario Simulation & What-If Analysis | VS-136 |
| W4123 | DC Footprint, Location & Capacity Optimization | VS-136 |
| W4130 | Multi-Echelon Inventory Optimization (MEIO) Modeling | VS-136 |
| W4131 | Safety Stock, Reorder Point & Service-Level Optimization | VS-136 |
| W4132 | ABC/XYZ Segmentation & Differentiated Inventory Policy | VS-136 |
| W4134 | Slow-Mover, Long-Tail & Obsolescence Risk Optimization | VS-136 |
| W4136 | Inventory Investment, Turns & Working Capital Optimization | VS-136 |
| W4137 | Network & Inventory Performance Dashboard & KPI Monitoring | VS-136 |
| W4138 | Inventory Health, Aging & Stock-Out Analytics | VS-136 |
| W4139 | Fill Rate, Service Level & OTIF Performance Analytics | VS-136 |
| W4141 | Demand & Supply Variability Monitoring for Re-Optimization Triggers | VS-136 |
| W4142 | Network & Inventory Re-Optimization Cycle & Parameter Refresh | VS-136 |
| W4143 | Simulation, Digital Twin & Network Stress Testing | VS-136 |
| W4144 | Annual Network & Inventory Strategy Review | VS-136 |
| W4296 | Bulky Delivery Service-Level, Capacity Analytics & Peak (Ber-Month) Planning | VS-143 |
| W4310 | Haul-Away/Recycling Revenue, Recovery & Cost Analytics | VS-143 |
| W4312 | Bulky Delivery/Install/Recycle Program Performance & Sustainability Analytics | VS-143 |
| W5465 | Green Fleet Strategy, Emissions Baseline & Decarbonization Target Setting | VS-192 |
| W5466 | Fleet Asset Inventory, Electrification Readiness Assessment & Transition Roadmap | VS-192 |
| W5476 | Green Fleet Telematics, Eco-Driving & Driver Behavior Management | VS-192 |
| W5481 | Fleet GHG Emissions Measurement, MRV & Scope 1 Reduction Reporting | VS-192 |
| W5485 | Third-Party / 3PL Carrier Green-Fleet Requirements, Contract Clauses & Scorecard | VS-192 |
| W5488 | Green Fleet Performance Analytics, Decarbonization Tracking & Continuous Improvement | VS-192 |

**Sell & Serve** (91)

| ID | Workflow | Value Stream |
|---|---|---|
| W1184 | Influencer & Home Improvement Content Creator Partnership Management | VS-14 |
| W1240 | Customer Project Completion Follow-Up, Satisfaction Survey & Cross-Sell Opportunity | VS-13 |
| W1253 | Subcontractor Performance Scorecard, Quality Assurance & Remediation Management | VS-12 |
| W1350 | Email Marketing Campaign Operations, Segmentation & Engagement Analytics | VS-14 |
| W1351 | Customer Referral Program Operations, Reward Fulfillment & Fraud Prevention | VS-14 |
| W1376 | Tool Rental Revenue Analytics, Utilization Optimization & Store Performance Benchmarking | VS-12 |
| W1379 | Vendor-Sponsored In-Store Product Demo Day Planning, Execution & ROI Measurement | VS-12 |
| W1424 | Store-Level DSD Vendor Delivery Performance Monitoring, Scorecard & Compliance Tracking | VS-7 |
| W1441 | Ecommerce Product Content Enrichment, How-To Guide Integration & SEO Optimization for Home Improvement | VS-10 |
| W1444 | Store-Level Grand Opening Digital Marketing Campaign, Community Outreach & Social Media Amplification | VS-14 |
| W1470 | Marketplace Customer Review Management, Seller Rating Optimization & Dispute Resolution | VS-10 |
| W1472 | Trade Account Referral Program, Contractor Network Development & Lead Tracking | VS-11 |
| W1491 | Customer Kitchen & Bathroom Design Consultation, 3D Rendering & Material Take-Off Generation | VS-9 |
| W1493 | Store-Level Contractor Lounge & Trade Amenities Management, Satisfaction Survey & Retention | VS-9 |
| W1518 | Customer Solar PV System Sizing, ROI Modeling, Net Metering Application & Installation Package Advisory | VS-9 |
| W1550 | Customer Voice-of-Customer (VOC) Monthly Analysis, Trend Dashboard & Strategic Insight Reporting | VS-13 |
| W1558 | Builder & Contractor Social Media Influencer Partnership Program, Content Co-Creation & Performance Tracking | VS-14 |
| W1561 | BuildRight Brand Ambassador & Pro Advocate Program, Trade Professional Community Building & Referral Tracking | VS-14 |
| W1902 | Quarterly Customer Satisfaction (CSAT) Survey Design & Execution | VS-44 |
| W1903 | Net Promoter Score (NPS) Monthly Measurement & Trend Analysis | VS-44 |
| W1905 | In-Store Customer Intercept Survey & Shopper Journey Mapping | VS-44 |
| W1906 | Post-Purchase Experience Survey & Product Satisfaction Tracking | VS-44 |
| W1909 | Store-Level Customer Experience Benchmarking & Improvement Action Planning | VS-44 |
| W1910 | Quarterly Competitive Store Visit & Price Benchmarking | VS-44 |
| W1913 | Digital Commerce Competitive Benchmarking & Online Price Monitoring | VS-44 |
| W1923 | Product Package Size & Format Optimization Research | VS-44 |
| W1957 | Government Supplier Performance Scorecard & Annual Review | VS-46 |
| W1995 | Service Partner Performance Dashboard & Quarterly Review | VS-47 |
| W1997 | Subscription Service Annual Program Review & Optimization | VS-47 |
| W1998 | Retail Media Inventory Audit & Availability Mapping | VS-48 |
| W1999 | Retail Media Rate Card Development & Pricing Governance | VS-48 |
| W2002 | Retail Media Booking & Reservation System Management | VS-48 |
| W2004 | Retail Media Vendor Self-Service Portal Management | VS-48 |
| W2005 | Retail Media Conflict Resolution & Competitive Separation | VS-48 |
| W2009 | Ecommerce Campaign Performance Optimization & A/B Testing | VS-48 |
| W2011 | Retail Media Campaign Reporting & Vendor Presentation | VS-48 |
| W2013 | Retail Media Campaign Exception & Quality Issue Resolution | VS-48 |
| W2014 | Retail Media Revenue Recognition & Billing | VS-48 |
| W2016 | Retail Media Network Profitability Analysis | VS-48 |
| W2017 | Retail Media Sales Lift Attribution & Vendor ROI Reporting | VS-48 |
| W2018 | Retail Media Inventory Yield & Utilization Optimization | VS-48 |
| W2019 | Retail Media Annual Business Plan & Revenue Forecasting | VS-48 |
| W2021 | Retail Media Network Audit & Compliance Review | VS-48 |
| W2125 | Warranty Program KPI Monitoring | VS-53 |
| W2133 | Warranty Claim Analytics & Trends | VS-53 |
| W2302 | Fulfillment KPI Dashboard | VS-60 |
| W2339 | Digital Sample & Augmented Reality Tool Management | VS-62 |
| W2352 | Display Zone Sales Attribution | VS-62 |
| W2353 | Sample Program Annual ROI | VS-62 |
| W2356 | Competitor Sample Display Benchmarking | VS-62 |
| W2357 | Sample Program Innovation & Technology Roadmap | VS-62 |
| W2646 | Mobile App Feature Roadmap & Prioritization | VS-75 |
| W2650 | Mobile App Performance Monitoring & Optimization | VS-75 |
| W2653 | Mobile App A/B Testing & Conversion Optimization | VS-75 |
| W2662 | Digital Channel Attribution & Customer Journey Analytics | VS-75 |
| W2664 | In-Store Digital Feature Usage Analytics | VS-75 |
| W2669 | Annual Digital Strategy Review & Investment Planning | VS-75 |
| W2711 | Project Delivery Performance Analytics | VS-77 |
| W2714 | Project Customer Satisfaction & Repeat Business Analytics | VS-77 |
| W2716 | Project Supply Chain Risk & Resilience Analytics | VS-77 |
| W2732 | Green Product Vendor Sustainability Scorecard | VS-78 |
| W2734 | Green Product Sales Analytics & Market Intelligence | VS-78 |
| W2737 | Green Product Lifecycle Assessment Data Management | VS-78 |
| W2738 | ESG Reporting Green Product Revenue Disclosure | VS-78 |
| W2740 | Sustainability Competitor Benchmarking | VS-78 |
| W2741 | Annual Green Building Strategy Review & Program Update | VS-78 |
| W2847 | MSME Segment P&L, Cohort Analytics & Lifetime Value | VS-82 |
| W3154 | Seller Performance Scorecard & Tier Management | VS-95 |
| W3160 | Marketplace P&L, Take-Rate & Growth Analytics | VS-95 |
| W4359 | Garden Center Performance, Sell-Through & Margin Analytics | VS-145 |
| W4360 | Live-Goods Sustainability, Pollinator/Native & ESG Reporting | VS-145 |
| W4450 | SCO Exception, Video-Analytics & Case Management | VS-149 |
| W4455 | SCO/Scan-&-Go Performance, Throughput & Adoption Analytics | VS-149 |
| W4456 | SCO/Scan-&-Go Continuous Improvement & Format Evolution | VS-149 |
| W4622 | VAS Analytics, Footfall & Basket-Linkage Intelligence | VS-156 |
| W4749 | Rental Fleet Telematics, GPS Tracking & Geofence Deployment | VS-162 |
| W4755 | Rental Agreement Execution, Liability Waiver & Telematics Consent | VS-162 |
| W4768 | Rental Revenue, Utilization, Attach-Uplift & Fleet-Performance Analytics | VS-162 |
| W4793 | Smart-Locker Network Strategy, Business Model & Roadmap | VS-164 |
| W4795 | Locker Site Selection, Placement & Capacity Modeling | VS-164 |
| W4815 | Network Analytics, Utilization & Footfall-to-Basket Measurement | VS-164 |
| W4905 | In-Store Media Performance & Customer-Experience Analytics | VS-168 |
| W4911 | In-Store Media Innovation — AI Music, Programmatic Signage & IoT Sensing | VS-168 |
| W4912 | Program Maturity, Benchmarking & Continuous Improvement | VS-168 |
| W4981 | Pickup Program Performance Analytics & Continuous Improvement | VS-171 |
| W5039 | Storage Occupancy/Yield Management & Dynamic Rate Optimization | VS-174 |
| W5054 | Storage Occupancy, Revenue, Delinquency & Yield Analytics | VS-174 |
| W5056 | Storage Program Performance, ROI & Cross-Sell/Basket-Linkage Analytics | VS-174 |
| W5077 | LPG Price/Promotion Execution, Competitor Monitoring & Margin Analytics | VS-175 |
| W5078 | Cylinder Turn, Refill Yield, Asset Utilization & Leak-Rate Analytics | VS-175 |
| W5080 | LPG Program Performance, Compliance Audit & ROI Analytics | VS-175 |

**Finance** (42)

| ID | Workflow | Value Stream |
|---|---|---|
| W1327 | Customer Trade Account Spend Analysis, Category Insights & Quarterly Business Review | VS-16 |
| W1406 | Weekly Flash Sales Report, Chain-Wide KPI Dashboard & Executive Performance Summary | VS-17 |
| W1474 | Surplus Cash Investment Portfolio Review, Counterparty Risk Assessment & Yield Optimization | VS-18 |
| W1684 | Store-Level Controllable Expense Monitoring & Benchmarking | VS-34 |
| W1687 | Utility Expense Monitoring & Energy Cost Optimization | VS-34 |
| W1767 | Home Improvement Loan Referral Program | VS-38 |
| W1801 | Vendor-Funded Digital Marketing & Social Media Campaign | VS-39 |
| W1802 | Co-Op Marketing ROI Analysis & Vendor Reporting | VS-39 |
| W1805 | Rebate Vendor Scorecard & Partnership Tiering | VS-39 |
| W1806 | Rebate Analytics & Margin Impact Dashboard | VS-39 |
| W1809 | Vendor Rebate Agreement Renewal & Optimization | VS-39 |
| W2161 | Gift Card Program ROI Analysis | VS-54 |
| W2164 | Gift Card Benchmarking & Competitive Analysis | VS-54 |
| W2499 | Bad Debt Trend Analysis & Prevention | VS-68 |
| W2501 | Credit Portfolio Performance Dashboard | VS-68 |
| W2590 | Shared Services Efficiency & Cost-per-Transaction Analytics | VS-72 |
| W2591 | Cross-Entity Shared Services Benchmarking | VS-72 |
| W2595 | Shared Services Technology Investment ROI Tracking | VS-72 |
| W2781 | Merchant Category Code (MCC) Optimization & Interchange Classification | VS-80 |
| W2800 | Payment Channel Performance, Cost-to-Serve & Tender Mix Analytics | VS-80 |
| W3162 | Lease Pricing, Residual Setting & Yield Modeling | VS-96 |
| W3177 | Lease Portfolio Composition & Concentration Analytics | VS-96 |
| W3180 | Lease Yield, IRR & Profitability Analytics | VS-96 |
| W3184 | Lease Customer Lifetime Value & Portfolio Strategy | VS-96 |
| W3388 | Annual-Percentage-Rate (APR) / Discount-Yield Monitoring & Optimization | VS-105 |
| W3397 | Cash-Conversion-Cycle (CCC) Forecasting & Scenario Modeling | VS-105 |
| W3399 | Working-Capital Performance Dashboard & Executive Reporting | VS-105 |
| W4284 | COD Driver/3PL Performance, Scorecard & Deduction Management | VS-142 |
| W4286 | COD Customer Experience, Success Rate & Conversion Optimization | VS-142 |
| W4287 | COD Program Analytics, Leakage & KPI Reporting | VS-142 |
| W4288 | COD Program Continuous Improvement & Future-State (BNPL/Digital Shift) | VS-142 |
| W4431 | Lease Portfolio Analytics, Total Cost of Occupancy & Benchmarking | VS-148 |
| W4432 | Lease vs Buy, Renewal & Optimization Decision Support | VS-148 |
| W4551 | Captive Loss Data, Analytics & Risk-Financing Intelligence | VS-153 |
| W4575 | Construction-Finance Analytics, Basket-Lift & Portfolio Intelligence | VS-154 |
| W4628 | Principal-vs-Agent (Gross-vs-Net) Determination for Marketplace, Retail Media, VAS & COD | VS-157 |
| W4661 | Gross-Margin, MMU/IMU & Maintained-Margin Analytics by SKU / Category / Store | VS-158 |
| W4956 | Financing-Cost, Effective-Rate & Capital-Structure Analytics | VS-170 |
| W4960 | Financing Program Continuous Improvement, Stress-Testing & Strategy Feedback | VS-170 |
| W5029 | Investor Perception, Sentiment & Ownership Analytics | VS-173 |
| W5030 | Peer, Valuation-Multiple & Capital-Structure Benchmarking | VS-173 |
| W5031 | IR Function Budget, Spend & Performance / ROI Management | VS-173 |

**People** (22)

| ID | Workflow | Value Stream |
|---|---|---|
| W1357 | Store Shift Optimization Based on Foot Traffic Analytics & Sales Pattern Analysis | VS-19 |
| W3213 | Rate Negotiation, Benchmarking & Master Services Agreement | VS-98 |
| W3225 | SLA Performance & Vendor Scorecard Management | VS-98 |
| W3227 | Contingent Workforce Spend Analytics & Cost Control | VS-98 |
| W3308 | Market Compensation Benchmarking Survey Participation & Pay Positioning | VS-102 |
| W3320 | Benefits Cost Modeling, Total-Cost & Utilization Analytics | VS-102 |
| W3328 | Total Rewards Effectiveness, Engagement-Link & Retention Analytics | VS-102 |
| W3765 | Employer Brand Measurement, Brand Health & Benchmarking | VS-121 |
| W3766 | Employee Advocacy, Storytelling & Brand Ambassador Program | VS-121 |
| W3776 | Candidate NPS, Funnel Analytics & Offer-Decline / Drop-Off Insights | VS-121 |
| W3781 | Referral Program Marketing, Incentive Design & Operations | VS-121 |
| W3784 | TA Analytics, Workforce-Planning Linkage & Strategic Talent Reporting | VS-121 |
| W4261 | Transport Cost Analytics & Total-Cost-of-Commute | VS-141 |
| W4262 | Ridership, Attendance & Attrition Correlation Analytics | VS-141 |
| W4263 | Route/Service Optimization & Continuous Improvement | VS-141 |
| W4336 | Housing Portfolio Performance, Cost & Welfare Analytics | VS-144 |
| W4478 | Program Metrics, Deterrence Effectiveness & Benchmarking | VS-150 |
| W4480 | Drug-Free Program Governance, Continuous Improvement & Reporting | VS-150 |
| W4703 | Mobility Risk, Compliance Calendar & KPI Framework | VS-160 |
| W4720 | Mobility Analytics, Cost & ROI Dashboard | VS-160 |
| W4881 | Screening Operations Analytics — Volume, TAT, Hit-Rate, Vendor Performance | VS-167 |
| W4888 | Program Maturity, Benchmarking & Continuous Improvement | VS-167 |

**Asset & Infrastructure** (22)

| ID | Workflow | Value Stream |
|---|---|---|
| W1446 | Store Lease Renewal Negotiation, Market Rent Benchmarking & Strategic Exit or Relocation Decision | VS-20 |
| W1501 | Store Rooftop Solar Panel Installation ROI Assessment, Net Metering Application & Monthly Energy Offset Tracking | VS-20 |
| W1563 | Store Energy Management, Electricity Consumption Monitoring, HVAC Optimization & Utility Cost Reduction Program | VS-20 |
| W1861 | Lease Portfolio Dashboard & Exposure Analysis | VS-42 |
| W2284 | Network Optimization Analysis | VS-59 |
| W3208 | Portfolio Performance, Valuation & ESG Reporting | VS-97 |
| W3458 | Self-Consumption Optimization & Load Matching | VS-108 |
| W3465 | Renewable Energy Certificate (REC) / Carbon Offset Generation, Registry & Trading | VS-108 |
| W3466 | GHG Emissions Reduction Accounting & Scope 2 Attribution | VS-108 |
| W3467 | Renewable Asset Performance Benchmarking & Portfolio Analytics | VS-108 |
| W3468 | Renewable Investment ROI, Savings Realization & Benefits Tracking | VS-108 |
| W3750 | Building Systems & Operations Energy Optimization | VS-120 |
| W3754 | Continuous Energy Performance Monitoring & Optimization | VS-120 |
| W3756 | Energy Cost, Consumption & GHG Analytics | VS-120 |
| W3757 | Benchmarking, Store-Energy Rating & Performance Comparison | VS-120 |
| W3760 | EEC Program Maturity & Continuous Improvement | VS-120 |
| W4185 | Building Management System (BMS) & IoT Integration | VS-138 |
| W4186 | HVAC, Lighting & Environmental Control Optimization | VS-138 |
| W4192 | Facilities Performance Analytics & Continuous Improvement | VS-138 |
| W4769 | EV Charging Host-Network Strategy, Business Model & Roadmap | VS-163 |
| W4771 | Charging Site Selection, Traffic/Demand Modeling & Store-Pairing | VS-163 |
| W4792 | Network Analytics, Utilization & Decarbonization Impact Reporting | VS-163 |

**Governance & Assurance** (35)

| ID | Workflow | Value Stream |
|---|---|---|
| W1261 | Construction & Renovation Waste Recycling, Circular Economy Program & Salvage Revenue Management | VS-25 |
| W1262 | Product Carbon Footprint Tracking, Green Product Labeling & Sustainable Sourcing Analytics | VS-25 |
| W1321 | ESG Target Setting, Quarterly Progress Tracking & Board Dashboard Reporting | VS-25 |
| W1323 | Supply Chain Disruption Simulation & Alternate Sourcing Activation Drill | VS-26 |
| W1334 | Carbon Footprint Calculation, Scope 3 Value Chain Emissions & Reduction Roadmap | VS-25 |
| W1338 | Employee Theft Prevention, Behavioral Analytics & Internal Investigation Protocol | VS-23 |
| W1396 | Store-Level Energy Consumption Benchmarking, Carbon Footprint Estimation & Reduction Target Tracking | VS-25 |
| W1448 | Store-Level Solar Panel Performance Monitoring, Energy Savings Tracking & ROI Reporting | VS-25 |
| W1541 | Key Risk Indicator (KRI) Monthly Monitoring, Threshold Alert & Risk Appetite Dashboard Operations | VS-21 |
| W1543 | Utility Data Collection & Store-Level Energy Consumption Monitoring | VS-25 |
| W1565 | Annual Insurance Portfolio Review, Coverage Gap Analysis & Market Benchmarking for Policy Renewal | VS-26 |
| W1608 | Vendor Quality Scorecard & Performance Review | VS-31 |
| W1645 | Annual Strategic Planning Workshop & Strategy Refresh | VS-33 |
| W1654 | Weekly Sales Flash & KPI Dashboard | VS-33 |
| W1655 | Store-Level Monthly Performance Review & Scorecard | VS-33 |
| W1663 | Customer Market Research & Segmentation Analysis | VS-33 |
| W1664 | Competitive Pricing Intelligence & Benchmarking | VS-33 |
| W2605 | Store Waste Analytics & Reduction Target Management | VS-73 |
| W2615 | Recycling Revenue Optimization & Vendor Management | VS-73 |
| W2616 | Circular Economy Product Development | VS-73 |
| W2619 | Corporate Waste Reduction Target & ESG Reporting | VS-73 |
| W2677 | Multi-LGU Compliance Dashboard & Alert Management | VS-76 |
| W2687 | Multi-LGU Regulatory Cost Benchmarking | VS-76 |
| W4364 | Service-Quality KPI Framework, Targets & Weighting | VS-146 |
| W4382 | Service-Quality Trend, Benchmarking & Competitive Tracking | VS-146 |
| W4384 | Service-Quality Program Maturity, ROI & Continuous Improvement | VS-146 |
| W4408 | Customer-Safety Performance Analytics, Benchmarking & Continuous Improvement | VS-147 |
| W4523 | CSR/ESG/Sustainability Reporting (GRI, IRIS+, Integrated Reporting) | VS-152 |
| W4528 | CSR Continuous Improvement, Learning & Portfolio Review | VS-152 |
| W4743 | TPRM Analytics, Heat-Map & KRIs | VS-161 |
| W4744 | TPRM Program Assurance, Audit & Continuous Improvement | VS-161 |
| W4857 | Executive Compliance Dashboard, Board Reporting & KPI Suite | VS-166 |
| W4859 | Permit-Portfolio Cost Management & Compliance-Spend Analytics | VS-166 |
| W4862 | Compliance Analytics, Trend & Benchmark Reporting | VS-166 |
| W4864 | Program Maturity Assessment, Operating-Model Optimization & Continuous Improvement | VS-166 |

**Technology & Data** (25)

| ID | Workflow | Value Stream |
|---|---|---|
| W1178 | Predictive Analytics Model Development, Deployment & Monitoring | VS-28 |
| W1214 | Store Performance Scorecard Weekly Review & Regional Benchmarking | VS-28 |
| W1215 | Customer Segmentation & Basket Analysis for Category Management | VS-28 |
| W1250 | Store Foot Traffic Analytics, Conversion Rate Monitoring & Sales Floor Productivity Insights | VS-28 |
| W1251 | Category Space Productivity Analytics & Planogram Performance Measurement | VS-28 |
| W1252 | Supply Chain Predictive Analytics, Demand Sensing & Early Warning System | VS-28 |
| W1339 | Computer Vision-Based Shelf Audit & Planogram Compliance Monitoring | VS-30 |
| W1451 | Merchandise Category Performance Analytics, Gross Margin Optimization & Assortment Rationalization Insights | VS-28 |
| W1452 | Customer Segmentation & Lifetime Value Analytics: Trade Professional vs. Retail vs. Corporate Account Profiling | VS-28 |
| W1458 | Autonomous Mobile Robot (AMR) Goods-to-Person Picking PoC for DC Operations | VS-30 |
| W1567 | Store Manager Self-Service Analytics Dashboard, Daily KPI Monitoring & Actionable Insight Delivery | VS-28 |
| W1568 | Executive Strategy Dashboard, C-Suite Performance Reporting & Board-Level Analytics Package | VS-28 |
| W1570 | In-Store Customer Navigation & Wayfinding Mobile App PoC, Indoor Positioning & Product Location Service | VS-30 |
| W3244 | Cloud Spend (FinOps) & Usage Optimization | VS-99 |
| W3251 | IT Asset Total Cost of Ownership Analytics | VS-99 |
| W3936 | AI Maturity Assessment & Continuous Improvement | VS-128 |
| W3951 | AI Performance, Value Realization & ROI Analytics | VS-128 |
| W3952 | AI Ethics Review Board, Stakeholder Engagement & Continuous Improvement | VS-128 |
| W4100 | Business Case, TCO & ROI Modeling for Technology Initiatives | VS-135 |
| W4107 | Cloud Resource Rightsizing, Reservation & Commitment Optimization | VS-135 |
| W4110 | SaaS License Utilization & Renewal Optimization | VS-135 |
| W4114 | IT Cost-to-Serve, Unit Cost & Productivity Ratio Analytics | VS-135 |
| W4115 | Technology Vendor Financial Performance & Benchmarking | VS-135 |
| W4120 | Annual Technology Financial Review & TBM Maturity Assessment | VS-135 |
| W4503 | EAS/RFID Performance, Tag-ROI & Shrink Analytics | VS-151 |

---


*Date: 2026-09-03 | Workflow Criticality Classification v7.47 — people-capability & reporting-policy gap fill (batch 9): the dedicated People/organization-domain gap analysis (workflow-gap-analysis-people.md) re-ran the §2 gap methodology across the People family and adjacent corporate/finance-policy streams and found four workflow-level surfaces unowned — the LMS platform & learning-records layer, the learning-content/course-catalog production lifecycle, the leadership-development program, and the accounting-policy/technical-accounting (PFRS) layer ('LMS' 58 PA files / 101 hits / zero dedicated `## W` headers with even an LMS Administrator role named in W1484's staffing; 'instructional design'/'course catalog'/a true 'accounting-policy owner' all absent — PFRS appears in 93 PA files but every dedicated owner is transaction-specific: VS-157 PFRS 15, VS-148 PFRS 16, W407 PAS 12, W1875 lease policy; adjacent slices program-generic: W51 training programs, W178 succession planning, W645 workforce planning, W3351 HRIS, W9 financial close). Four workflows added — W5525 Learning Platform (LMS) Administration, Integration & Learning-Records Operations, W5526 Learning-Content Development, Course-Catalog & Certification-Program Lifecycle, W5527 Leadership Development & Management-Capability Program (HiPo Development) (all PA-19.4), and W5528 Accounting Policy, Technical Accounting (PFRS) Position & New-Standard Adoption Governance (PA-17.4) — and confirmed directly **Tier 2 (4)** (the platform-operations/governance-layer/program-support class of their siblings W3351/W51/W9); statutory dimensions (OSH training-record evidence, mandatory pass/fail regulatory courses) ride verification steps inside the workflows, matching the W5513/W5515/W5518 precedent. All four absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Register 5,400 → 5,404 rows (5,377 → 5,381 unique; T2 3,261 → 3,265); proposed register stays empty (0 unclassified). Downstream figures re-pointed (workflows/README Quick Stats + Finance/People families + reconciliation line, value-stream-index header/VS-17+VS-19 rows/grand total/footer/detailed sections, VS-19 README 75 → 78, VS-17 README 67 → 68, root-README tree/Key-Metrics/coverage rows, WORKFLOW-FORMAT-GUIDE anchors, requirement-matrix inventory line, dependency-map intro, touchpoint-map reconciliation footer, gap-analysis batch-9 note + companion doc, executive-summary footer, OM v2.6 FIN 798 → 799 / PEO 437 → 440 and 4,868+509 → 4,872+509=5,381, sourcing-model v1.6 §12.1 ladder 3,261 → 3,265, semantic-audit-coverage registry annotated). `validate-repo.sh`: 0 errors / 0 warnings.*

*Date: 2026-09-23 | Workflow Criticality Classification v7.63 — capability-switchboard admission (batch 30, by direction): **W5580** Capability Switchboard Operation & Channel Enablement Impact Governance (PA-113.2, VS-113) — the owning workflow for the channel-capability registry's enable/disable state changes: flip-set cross-workflow assessment, volume re-basing (designed-capacity ↔ live load), revenue/recording-vehicle impact, headcount & staffing impact assessment with the no-silent-absorption rule, feature-flag change-chain execution and canon settlement. Confirmed directly **Tier 2**. Register 5,455 → 5,456 rows (5,432 → 5,433 unique; T2 3,301 → 3,302); `### Tier 2 Additions` trued 546 → 547; proposed register stays empty. All absorbed within the sized CIO Office (OM stays 122 FTE / 17 teams; TO stays HQ 532 / 6,932). `validate-repo.sh`: 0 errors / 0 warnings.*

*Date: 2026-09-21 | Workflow Criticality Classification v7.62 — EBS documentation-coverage gap fill (batch 26): the first closures from the inward-direction register (the ebs-documentation-coverage register's rows 02 and 05) — **W5578** Environmental Data Capture, Emission-Factor Governance & GHG Transaction Batch Processing (VS-25.3; the ESG reporting family consumed environmental quantities but no workflow owned their capture into a system of record, and W1334's touchpoint literally read 'spreadsheet or specialized platform' while EBS ships Environmental Accounting and Reporting) and **W5579** Customer Bill Presentment Template, Assignment-Rule & Data-Source Governance (VS-16.2; iReceivables is adopted at fit-gap A14 and renders through Bill Presentment Architecture, which no workflow owned). Both confirmed directly **Tier 2**. Register 5,453 → 5,455 rows (5,430 → 5,432 unique; T2 3,299 → 3,301); `### Tier 2 Additions` trued 544 → 546; proposed register stays empty. All absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 532 / 6,932). `validate-repo.sh`: 0 errors / 0 warnings.*

*Date: 2026-09-21 | Workflow Criticality Classification v7.61 — ERP customization-governance gap fill (batch 25): the EBS blueprint layer issued from 2026-09-14 defines recurring post-go-live processes no gap pass had read — the customization decision record and its eight-gate admissibility test, the hard extension budget with its retire-one-to-add-one rule, the customization register and its quarterly object-inventory audit against the databases, and the de-customization programme with its five retirement triggers ('CEMLI'/'de-customization'/'extension budget'/'customization governance' in zero PA files; 'customization' in eight with no dedicated `## W` header, all incidental). Three workflows added to PA-113.1 and confirmed directly **Tier 2** (the W5515–W5517 architecture-governance sibling class): **W5575** Customization Decision Record (CDR) Intake, Admissibility Gate & ARB Approval; **W5576** CEMLI Register Maintenance & Quarterly Object-Inventory Audit; **W5577** Extension De-Customization, Retirement & Budget Reclamation. Register 5,450 → 5,453 rows (5,427 → 5,430 unique; T2 3,296 → 3,299); proposed register stays empty (0 unclassified); the `### Tier 2 Additions` sub-heading trued 541 → 544. All absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 532 / 6,932). `validate-repo.sh`: 0 errors / 0 warnings.*

*Date: 2026-09-15 | Workflow Criticality Classification v7.60 — thirtieth-wave consistency review (title-only register change, v7.34 precedent): all 49 drifted W-title cells trued to the exact PA `##`/`###` W-header canon (the generator-read primary source and the bpmn process names) — four token defects the semantic batches had repaired in the PA files but never re-pointed into the register (W2904 'DTI/NCSD' → the web-verified NCSC form per review #60; W3673 'I-SEAL' → the PCIMS portal named by PA-117.2's own steps and PA-117.1's instrument map; W4955 'PAS 39' → PAS 37, the contingent-liability standard its own title names; W2791 'Intercharge' → 'Interchange' per the card-scheme fee canon), plus the stranded abbreviation/prefix/spacing drifts (initial-commit short forms such as W26/W30/W2C/W271 and the 'Ecommerce —'/'E-commerce' prefix and W99 spacing families). No tier assignments, register-row counts, or totals changed; W423/W425's treasury-companion annotated titles stand per v7.31 and are now pinned by literal in the new Check-18 title mirror. `validate-repo.sh`: 0 errors / 0 warnings across 77 checks.*

*Date: 2026-09-10 | Workflow Criticality Classification v7.59 — concessionaire connectivity gap fill (batch 24): a concessionaire operating-model review found the connectivity-exception surface unowned ('concessionaire internet'/'independent circuit' appear in zero PA files as owned content — W177 bundles internet into the monthly 'Rent + Utilities + Commission' concessionaire invoice as a BuildRight-provided utility and W111 benchmarks it as a store utility, W366 manages the store link with its segmented Wi-Fi, and W5520/W5418/W5421 guard the IPAM and device boundaries, but nobody owned the request path when a concessionaire wants its own internet connection: the default-posture rule with the segmented-Wi-Fi alternative evaluated first, the eligibility gate for documented regulatory/banking/capacity needs only, the isolation envelope (separate conduit, no physical or logical crossing into BuildRight networks, DHCP confined to the concessionaire's own equipment, no BuildRight credentials), the W47 works approval with landlord and LGU consent for exterior terminations, the W117 connectivity addendum with incident demarcation and VS-147 insurance, the commission-integrity clause keeping every concession sale on the BuildRight POS throughput SKU, and the restoration holdback released only on the W62 exit walk-through). One workflow added — W5574 Concessionaire Connectivity Request, Approval & Independent-Circuit Governance (PA-07.1) — confirmed directly **Tier 2** (the concession-operations governance class of the W5505–W5507 siblings; the network-boundary machinery it invokes is already in place, so nothing is go-live blocking). All absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Register 5,449 → 5,450 rows (5,426 → 5,427 unique; T1 unchanged at 1,396, T2 3,295 → 3,296, Tier 3 unchanged at 758); proposed register stays empty (0 unclassified). Prior v7.58 — gas-leak, tsunami/storm-surge, media-exposé & server-room-environmental gap fill (batch 23): the batch-16/17/18/19/20/21/22 edge-case sweeps were re-run across scenario families not yet probed (pre-ignition gas events at sites with LPG exchange cages, coastal water intrusion by tsunami or storm surge, genuine-fault investigative journalism, and physical-room failures inside the IT estate) and found four unowned surfaces (keyword verification: 'gas leak'/'gas odor'/'smell of gas' = 0 corpus hits as event content, with W5069 owning only cylinder intake/periodic leak inspection and W5537 the post-ignition fire event; 'tsunami' = 0 corpus hits and 'storm surge' only as PA-09.2's customer-advisory context, with W1450's structural assessment quake-specific and W1387's flood canon rainfall/riverine; 'undercover'/'hidden camera'/'investigative report'/'right of reply' = 0 corpus hits, with W1562 owning recall/safety-incident media response and W3271/W3272 the fake-content impersonation class; 'server room'/'cooling failure'/'fire-suppression discharge' = 0 corpus hits, with W55 owning failover execution once a disaster is declared and W380 alert triage). Four workflows added — W5570 Gas-Leak Event Response (LPG/Natural-Gas Odor on Premises) (PA-24.2), W5571 Tsunami & Storm-Surge Coastal-Intrusion Response Protocol (PHIVOLCS Advisory / PAGASA Storm-Surge Warning) (PA-26.1), W5572 Undercover-Investigation & Media-Exposé Response Protocol (Investigative-Newsroom Event) (PA-14.3), W5573 Server-Room & Data-Center Environmental Event Response (Cooling Failure, Water Intrusion, Fire-Suppression Discharge) (PA-27.2) — confirmed directly **Tier 1 (2)** (W5570 the pre-ignition life-safety class of the W5537/W5538 precedent; W5571 the coastal-water evacuation-and-clearance class of the W1449/W5562 precedent) and **Tier 2 (2)** (W5572 the brand-integrity comms-contingency class of W5563/W5568; W5573 the IT-facility-contingency class of W5547/W5564). The same pass produced the tenth custody wave (v1.10, E-46–E-49). All four absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Register 5,445 → 5,449 rows (5,422 → 5,426 unique; T1 1,394 → 1,396, T2 3,293 → 3,295, Tier 3 unchanged at 758); proposed register stays empty (0 unclassified). Prior v7.57 — terminal-tampering, procurement-impersonation, account-takeover & commute-disruption gap fill (batch 22):* the batch-16/17/18/19/20/21 edge-case sweeps were re-run across scenario families not yet probed (payment-device compromise at the lane, fraudsters impersonating BuildRight as the buyer, takeover of BuildRight's own verified accounts, commute interruptions stranding crews at undamaged sites) and found four unowned surfaces (keyword verification: 'card skimmer'/'tampered terminal' = 0 corpus hits, with W537 owning only daily terminal operations and W1205 the compliance program; 'fake PO'/'fraudulent purchase order'/'supplier impersonation' = 0 corpus hits, the fraud being the buyer-side mirror of W5559's payment diversion and W5563's fake sellers; 'account hijack'/'brand account' = 0 corpus hits, W5563 covering only the fake-page class; 'transport strike'/'commute disruption' = 0 corpus hits, W4255 being vehicle-level and W850/W2510 site-level). Four workflows added — W5566 Payment-Terminal Tampering & Card-Skimmer Response (PA-08.2), W5567 Procurement-Impersonation & Fake-PO Goods-Diversion Response (PA-03.2), W5568 Official-Channel Account-Takeover Response (PA-14.2), W5569 Mass-Commute Disruption & Transport-Strike Continuity Protocol (PA-141.2) — all confirmed directly **Tier 2 (4)** (W5566 the payment-device security class of W1205/W5547, W5567 the procurement-fraud contingency class of W5559/W5563, W5568 the brand-integrity channel-contingency class of W5563/W5550, W5569 the workforce-continuity class of W5561/W4255). The same pass produced the ninth custody wave (v1.9, E-42–E-45). All four absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Register 5,441 → 5,445 rows (5,418 → 5,422 unique; T1 unchanged at 1,394, T2 3,289 → 3,293, Tier 3 unchanged at 758); proposed register stays empty (0 unclassified). Prior v7.56 — storefront-crash, brand-impersonation-scam, wallet-outage & adjacent-works gap fill (batch 21): the batch-16/17/18/19/20 edge-case sweeps were re-run across scenario families not yet probed (vehicle impact into an operating store, brand-impersonation commerce scams, mobile-wallet provider outages, adjacent construction damaging occupied property) and found four unowned surfaces (keyword verification: 'vehicle into building'/'storefront crash' = 0 corpus hits, with W330's emergency trigger naming structural failure only generically; 'fake seller'/'scam listing' = 0 corpus hits, with only the W3271/W3272 takedown machinery and W5557's recruitment variant present; wallet-platform outages unowned — W5547's trigger names the card-scheme/acquirer rail only and W535 the store link; 'adjacent construction'/'neighboring construction'/'excavation damage' = 0 dedicated headers). Four workflows added — W5562 Vehicle-Impact & Storefront-Crash Response Protocol (PA-147.2), W5563 Brand-Impersonation Commerce-Scam Response (Fake Sellers & Fraudulent Pickup Offers) (PA-100.2), W5564 Mobile-Wallet Platform Outage Response (E-Wallet Tender Downtime) (PA-08.1), W5565 Third-Party Construction Damage & Adjacent-Works Response Protocol (PA-20.3) — confirmed directly **Tier 1 (1)** (W5562, the life-safety structural-clearance class of the W5537/W5555 precedent) and **Tier 2 (3)** (W5563 the brand-integrity event class of W5557/W5550, W5564 the payment-platform contingency class of W5547/W5548, W5565 the asset-protection contingency class of W5560/W5133). The same pass produced the eighth custody wave (v1.8, E-38–E-41). All four absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Register 5,437 → 5,441 rows (5,414 → 5,418 unique; T1 1,393 → 1,394, T2 3,286 → 3,289, Tier 3 unchanged at 758); proposed register stays empty (0 unclassified). Prior v7.55 — cyber-extortion, payment-diversion, land-occupation & water-continuity gap fill (batch 20): the batch-16/17/18/19 edge-case sweeps were re-run across scenario families not yet probed (destructive cyber attack with extortion, disbursement-diversion fraud, vacant-land occupation, utility-service failure beyond power) and found four unowned surfaces (keyword verification: 'ransomware'/'extortion demand'/'data-destruction' = 0 dedicated headers, appearing only as PA-27.2's DR pain point, W1330's exercise inject and W5529's OT drill; BEC named only in PA-18.2 pain points with a one-bullet callback mitigation while VS-125.2 watches only the customer-side diversion class; 'informal settler'/'squatter'/'illegal occupation'/'adverse possession' = 0 corpus hits; 'water interruption'/'water rationing' only as product-selling context in PA-09.2). Four workflows added — W5558 Ransomware & Destructive Cyber-Attack Enterprise Response Protocol (PA-27.3), W5559 Vendor Payment-Diversion & Business Email Compromise (BEC) Fraud Event Response & Recovery Protocol (PA-18.2), W5560 Informal-Settler Invasion & Illegal Occupation of Banked Land — Detection, Relocation & Ejection Protocol (PA-178.1), W5561 Sustained Water-Service Interruption Response & Store Continuity Protocol (PA-07.2) — confirmed directly **Tier 1 (1)** (W5558, the enterprise-trading-halt & statutory-continuity class of the W5545/W5546 enforcement-and-filing precedent — the data-privacy core rides the Tier-1 W53 chain and the OT variant rides W5529) and **Tier 2 (3)** (W5559 the financial-crime contingency class of W5541/W2814, W5560 the landbanking asset-protection class of W5133/W5143, W5561 the facility-continuity class of the W470 power analog). The same pass produced the seventh custody wave (v1.7, E-34–E-37). All four absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Register 5,433 → 5,437 rows (5,410 → 5,414 unique; T1 1,392 → 1,393, T2 3,283 → 3,286, Tier 3 unchanged at 758); proposed register stays empty (0 unclassified).*
*Date: 2026-09-05 | Workflow Criticality Classification v7.54 — in-transit-security, fatality-scene, tampering-extortion & recruitment-fraud gap fill (batch 19): the batch-16/17/18 edge-case sweeps were re-run across scenario families not yet probed (in-transit cargo crime, on-premises death events, merchandise-integrity extortion, employment-brand impersonation) and found four unowned surfaces (keyword verification: 'hijack'/'holdup'/'cargo robbery' = 0 dedicated headers with cargo theft named only inside W1337's ORC intelligence background and VS-180's relief-convoy escorts; 'death on premises'/'died in store' = 0 protocol content with W4401 owning injuries and naming fatality only as W4405's notification trigger; 'tampering threat'/'contamination threat'/'extortion' = 0 dedicated headers with VS-89 owning only found-defect triggers; 'recruitment scam'/'fake job'/'job scam' = 0 hits with W3272 watching impersonating accounts through the customer-phishing lens only). Four workflows added — W5554 In-Transit Cargo Hijacking, Armed Truck Robbery & Driver-Safety First Response Protocol (PA-06.2), W5555 Customer or Visitor Death on Premises — Scene Protocol, Family Liaison & Trading-Continuity Decision (PA-147.3), W5556 Product-Tampering Threat, Extortion Demand & Merchandise-Integrity Sweep Protocol (PA-89.1), W5557 Recruitment Fraud & Fake Job-Offer Scam Response, Takedown & Victim-Guidance Protocol (PA-121.1) — confirmed directly **Tier 1 (2)** (W5555/W5556, the life-safety scene-and-clearance class of the W5536/W5537/W5538 precedent — each gates a physical-state transition on documented external assessment) and **Tier 2 (2)** (W5554/W5557 — the contingency-operations class of W653/W2814 with the crew-safety dimension riding the Tier-1 W501/W717 chains, and the brand-integrity channel-contingency class of the W5550/W5553 precedent). The same pass produced the sixth custody wave (v1.6, E-30–E-33). All four absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Register 5,429 → 5,433 rows (5,406 → 5,410 unique; T1 1,390 → 1,392, T2 3,281 → 3,283, Tier 3 unchanged at 758); proposed register stays empty (0 unclassified).*
*Date: 2026-09-05 | Workflow Criticality Classification v7.53 — channel-enforcement, employee-legal-status, OSH-enforcement & app-store-removal gap fill (batch 18): the batch-16/17 edge-case sweeps were re-run across scenario families not yet probed and found four unowned surfaces (keyword verification: 'account suspension'/'account health'/'delisting' = 0 hits with W1470 owning only the preventive metrics layer and W659 the own-platform incidents; 'arrest' present only as a VS-167 re-screening trigger and an LP case-closure outcome — no owner of the employment-status mechanics; 'work stoppage'/'stoppage order'/'imminent danger' = 0 dedicated headers with RA 11058 cited in ~15 PA files only as W505's penalties context; 'app store removal'/'policy violation' = 0 hits with W2647 owning listing upkeep only). Four workflows added — W5550 Marketplace Account Suspension, Enforcement Freeze & Appeal Recovery Protocol (PA-10.3), W5551 Employee Arrest, Detention & Criminal-Case Employment-Status Response Protocol (PA-19.1), W5552 DOLE Imminent-Danger Work-Stoppage Order Response, Abatement & Reinstatement Gate (PA-24.1), W5553 Mobile App Store Removal, Policy-Violation Response & Re-Listing Recovery Protocol (PA-75.1) — confirmed directly **Tier 1 (1)** (W5552, the OSH statutory-enforcement class of the W5545 closure-order precedent) and **Tier 2 (3)** (W5550/W5551/W5553 — the channel-contingency class of the W5547/W5548 precedent and the specialized employee-relations event class). The same pass produced the fifth custody wave (v1.5, E-27–E-29). All four absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Register 5,425 → 5,429 rows (5,402 → 5,406 unique; T1 1,389 → 1,390, T2 3,278 → 3,281, Tier 3 unchanged at 758); proposed register stays empty (0 unclassified).*
*Date: 2026-09-05 | Workflow Criticality Classification v7.52 — regulatory-shock, platform-outage & governance-continuity gap fill (batch 17): the batch-16 edge-case sweep was re-run across scenario families not yet probed and found six unowned surfaces (keyword verification: 'emergency succession'/'board continuity' = 0 hits with 'incapacity' appearing only as PA-36.2's records trigger; 'Oplan Kandado'/'tax suspension'/'closure order' = 0 hits; 'card network outage'/'card scheme outage'/'acquirer failure' = 0 hits; 'gift card system outage'/'loyalty system failure' = 0 hits; 'suicide'/'self-harm' = 0 hits; eFPS downtime cited as a pain point in 4 PA files with a one-bullet mitigation only — the batch-11 'adjacent-owners-exist-but-no-event-owner' pattern). Six workflows added — W5544 Emergency Executive Succession & Decision-Rights Continuity Protocol (PA-36.1), W5545 BIR Tax-Enforcement Suspension & Closure-Order Response (Oplan Kandado) (PA-79.3), W5546 BIR eFPS & Government-Portal Outage Filing Contingency, AAB Fallback & Penalty-Relief Documentation (PA-79.3), W5547 Payment-Network & Acquirer Outage Response (Card Scheme / Acquirer Downtime) (PA-08.1), W5548 Stored-Value & Loyalty Platform Outage, Downtime-Acceptance & Manual-Redemption Protocol (PA-54.2), W5549 Suicide Attempt / Self-Harm Incident Response & Psychosocial-Aftermath Protocol (PA-24.1) — confirmed directly **Tier 1 (2)** (W5545/W5546, the statutory-deadline-protection class of the W2764/W2765/W5508 filing siblings) and **Tier 2 (4)** (W5544/W5547/W5548/W5549 — governance-continuity and platform-contingency classes; the medical core of W5549 rides the Tier-1 W501 chain, the batch-16 W5539 precedent). The same pass produced the fourth custody wave (v1.4, E-23–E-26). All six absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Register 5,419 → 5,425 rows (5,396 → 5,402 unique; T1 1,387 → 1,389, T2 3,274 → 3,278, Tier 3 unchanged at 758); proposed register stays empty (0 unclassified).*

*Date: 2026-09-05 | Workflow Criticality Classification v7.51 — emergency & continuity workflow gap fill (batch 16): a dedicated emergency/edge-case gap analysis re-ran the §2 gap methodology at *scenario* granularity (rare events and failure modes rather than capabilities) across the corpus and found eight unowned surfaces: the missing-child / Code Adam response ('missing child' appeared in the corpus only as cart-child-straps — PA-07.3's cart-fleet narrative — with zero emergency-protocol hits; the retail-standard Code Adam protocol with exit-hold, coded PA, zone sweep, verified-reunification and a 10-minute police-escalation clock had no owner), the fire *event* ('fire' was owned only as prevention/testing — W806 annual BFP certification, W1296 equipment inspection, VS-04 DC PM checks — plus the generic W330 protocol's one classification row; nobody owned suppression activation, BFP coordination, the structural assessment or the three-party BFP-clearance-to-reopen gate, for stores or DCs), the bomb threat (a W330 Major-classification example and a PA-24.2 plan-template bullet; no call-takedown checklist, search-vs-evacuate decision rule, PNP-EOD handoff or radio-RF discipline), elevator/escalator entrapment (25 files mention elevators — all maintenance/accessibility; the 'entrapment' hits were law-enforcement ops; nobody owned passenger contact, the ≤ 10-minute medical-vulnerability triage, the licensed-technician-only release rule or the 2-in-12-months modernization trigger), the payroll run *failure* (W10 owns the run, W641 planned off-cycle payments; nobody owned the abort/reject classification clock, bank-file reject regeneration, the < 24 h emergency-net-pay decision via W641 rails, or the statutory remittance protection when the register is broken — 0 corpus hits for 'payroll failure'), the bank-failure / frozen-deposit event (W1474 owns steady-state counterparty limits and the PDIC-cap note; nobody owned the exposure census, 10-day obligations-vs-stranded-cash gap, disbursement rerouting or the PDIC claim file), liquidity-stress & payment-prioritization escalation (W319/W3400 own routine covenant monitoring and WC policy; nobody owned the stress declaration, cash council, reversibility-ordered lever sequence, statutory-first payment tiers or the never-lapse covenant-engagement rule — 'liquidity crisis'/'cash crunch' = 0 hits), and the mass-mispricing / price-file integrity *event* (W13 executes price files, W3697 monitors accuracy, W1622/W1538 refund; nobody owned the event: blast-radius scoping, RA 7581 SRP triage, the rollback + re-label sweep, overcharge remediation or the DTI evidence pack). The same analysis produced the third custody wave (event-custody-and-precedence-register.md v1.3, E-19–E-22: fire, earthquake — naming W1450 as the canon the register had never routed — armed violence W717-vs-W330 during-event command, and the mispricing event). Eight workflows added — W5536 Missing-Child / Code Adam In-Store Response Protocol (PA-07.2), W5537 Fire Event Response, Suppression & Post-Fire BFP Clearance (Store & DC) (PA-24.2), W5538 Bomb Threat Response & Search-or-Evacuation Decision Protocol (PA-24.2), W5539 Elevator & Escalator Entrapment Response Protocol (PA-07.2), W5540 Payroll Run Failure, Correction & Emergency Off-Cycle Payment (PA-19.2), W5541 Bank-Failure & Frozen-Deposit Contingency (PA-18.3), W5542 Liquidity Stress, Covenant-Breach & Payment-Prioritization Escalation (PA-105.3), W5543 Price-File Integrity Event Response & Mass-Mispricing Rollback (PA-118.2) — confirmed directly **Tier 1 (3)** (W5536/W5537/W5538, the life-safety in-store emergency class of W330/W501/W576 — each gates reopening/reunification on verified external clearance: RA 7610 safeguarding, RA 9514 re-occupancy, PNP-EOD all-clear) and **Tier 2 (5)** (W5539–W5543: the contingency-operations and integrity-event classes of W470/W641/W319/W3697 — the statutory dimensions ride the existing Tier-1 chains W501/W10/W1527/W1306/W13/W427 rather than new statutory registers). All eight absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Register 5,411 → 5,419 rows (5,388 → 5,396 unique; T1 1,384 → 1,387, T2 3,269 → 3,274, Tier 3 unchanged at 758); proposed register stays empty (0 unclassified).*

*Date: 2026-09-04 | Workflow Criticality Classification v7.50 — demand-intake gap fill (batch 15): re-running the workflow-granularity gap methodology against the end-to-end stakeholder demand cycle (IT operating model OM §5.1/§7 governance; sourcing model §3 gate) found one program surface unowned at workflow level — the capability demand-intake & backlog-triage front door (raise → log & triage → route to team backlog / workflow-catalog gap-admission / SIB sourcing gate → Product-Council capacity funding; 'capability demand intake'/'backlog triage' in zero dedicated `## W` headers while the adjacent VS-113 slices are each post-intake: W3577 portfolio rationalization, W3580 solution architecture for approved initiatives, W3588 investment ROI, and the batch-7 machinery W5515–W5517). One workflow added — **W5535 Capability Demand Intake & Backlog Triage** (PA-113.2, the application-portfolio front door it feeds: triage pack with IAP integration sketch W3579, rough TCO W4100, RA 10173/BIR compliance constraints, preliminary Tier proposal; routing to W5515's gate; accepted/routed/declined closed loop via the BPO) — and confirmed directly **Tier 2** (the governance/lifecycle-operations class of its W5515/W5516 siblings; no statutory dimension — the front door routes and never executes statutory filings, matching the batch-7 precedent). Absorbed within the sized CIO Office (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Register 5,410 → 5,411 rows (5,387 → 5,388 unique; T2 3,268 → 3,269; Tier 1/3 unchanged); proposed register stays empty (0 unclassified). Downstream figures re-pointed (workflows/README Quick Stats + Technology & Data family + reconciliation line, value-stream-index header/VS-113 rows/T&D subtotal/grand total/footer, VS-113 README 27 → 28, PA-113.2 footer 9 → 10, root-README tree/Key-Metrics/coverage/diagram rows, WORKFLOW-FORMAT-GUIDE anchors, requirement-matrix inventory line, VS-133 README + PA-133.1/.3 Volume rows, dependency-map intro + §8 block + §8.3 VS-113 row + VS-133 row, touchpoint-map v90.0, gap-analysis batch-15 note, executive-summary top footer, OM v2.9 CIO Office 80 → 81 and 4,878+509 → 4,878+510=5,388, sourcing-model v1.9 §12.1 ladder 3,268 → 3,269 + §12.2 intake figure + header/§13 OM pins, semantic-audit-coverage registry pending note W5535). `validate-repo.sh`: 0 errors / 0 warnings.*

*Date: 2026-09-04 | Workflow Criticality Classification v7.49 — operations-workflow gap fill (batch 11): the dedicated operations-domain gap analysis (workflow-gap-analysis-operations.md) re-ran the §2 gap methodology across the four workflow-level families not yet covered by batches 8–10 (Plan & Source, Make & Move, Sell & Serve, Asset & Infrastructure, Governance & Assurance) and found three workflow-level surfaces unowned — the workforce time-&-attendance (biometric/time-clock) platform estate ('time and attendance'/'timekeeping'/'biometric' = 38 PA files / ~130 hits / 0 dedicated headers — the W561 trigger names 'biometric/attendance system', W586/W796 name 'timekeeping' as a labor-metrics data source and new-store readiness names 'biometric system installed', but the ~420–450-device estate, its punch-data payroll interfaces and offline fallback have no owner — the batch-9 LMS pattern), the BIR Form 2316 annual issuance layer ('2316' = 10 PA files / 22 hits / 0 dedicated headers — generation exists only as sub-steps W90.8/W1384.7 and an ESS view bullet, with no owner of the January 31 furnishing campaign to ~6,762 employees, its acknowledgment gate or its reconciliation to W2764/W2765), and the company-property gate-pass & asset-exit control ('gate pass'/'property pass' = 5 PA files / 7 hits / 0 dedicated headers — W585 passes trucks at DC gates and PA-09.1 expects 'Gate Pass Integration (Security exit clearance)', but nobody owns the ~8,000–12,000-movement/year property-exit control across ~205 stores + 4 DCs + HQ). Three workflows added — W5532 Workforce Time & Attendance (Biometric/Time-Clock) Platform Estate & Punch-Data Operations (PA-19.3), W5533 BIR Form 2316 Annual Issuance, Employee Acknowledgment & Certificate Lifecycle (PA-79.2), and W5534 Company-Property Gate Pass & Asset-Exit Control (Stores, DCs & HQ) (PA-23.2) — and confirmed directly **Tier 2 (2)** — W5532 (the platform-operations class of W5525/W3351) and W5534 (the physical-security control class of W1477/W1478) — and **Tier 1 (1)** — W5533 (the statutory furnishing layer of the withholding regime, the W2764/W2765/W5508 class). All three absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Register 5,407 → 5,410 rows (5,384 → 5,387 unique; T1 1,383 → 1,384, T2 3,266 → 3,268); proposed register stays empty (0 unclassified). Downstream figures re-pointed (workflows/README Quick Stats + Sell & Serve/Finance/People families + reconciliation line, value-stream-index header/VS-19+VS-23+VS-79 rows/family subtotals/grand total/footer/detailed sections, VS-19 README 78 → 79, VS-79 README 25 → 26, VS-23 README 28 → 29, root-README tree/Key-Metrics/coverage rows, WORKFLOW-FORMAT-GUIDE anchors, requirement-matrix inventory line, dependency-map intro + VS-133 row, touchpoint-map v89.0 footer, gap-analysis batch-11 note + companion doc, executive-summary footer, IT-model v2.8 PEO 440 → 441 / FIN 801 → 802 / SSP 873 → 874 and 4,875+509 → 4,878+509=5,387 with the §4.9 FIN straggler 799 → 802 trued, sourcing-model v1.8 §12.1 ladder 1,384/3,268, semantic-audit-coverage registry annotated, audit-model-docs/audit-exec-ctl ANCHOR re-pins). `validate-repo.sh`: 0 errors / 0 warnings.*

*Date: 2026-09-03 | Workflow Criticality Classification v7.48 — finance-workflow gap fill (batch 10): the dedicated Finance-domain gap analysis (workflow-gap-analysis-finance.md) re-ran the §2 gap methodology across the Finance family (775 workflows) plus treasury/tax/property-adjacent streams and found three workflow-level surfaces unowned — the utility/telecom/site deposits-paid lifecycle (PA-42.3's own W1877 pain point carries the PHP 10M–40M locked-capital canon with no downstream owner; recovery exists only as a closure sub-step in PA-20.3 and a connection-transaction step in W1877, while the landlord-deposit sibling W1867 shows the owned pattern), the minimum corporate income tax layer ('MCIT'/'minimum corporate income' = 0 corpus-wide hits — W407 computes normal tax and deferred tax but the 2% gross-income floor, its regime evaluation and the 3-year excess-credit carry-forward are absent), and the PFRS 8 operating-segment disclosure layer ('segment reporting'/'operating segment' = 0 corpus-wide hits — the CODM review packages exist in W1653/W231/W102/W1657 and the AFS filing machinery in W9B/W481, but the segment-note production that binds them for the audited statements is unowned). Three workflows added — W5529 Utility, Telecommunications & Site Deposits Paid — Register, Interest Reconciliation, Surety Replacement & Recovery-on-Closure (PA-42.3), W5530 Minimum Corporate Income Tax (MCIT) Computation, Regime Evaluation & 3-Year Excess-Credit Carry-Forward (PA-17.3), and W5531 PFRS 8 Operating-Segment Reporting, CODM Disclosure Package & Segment-Note Production (PA-17.4) — and confirmed directly **Tier 1 (2)** — W5530 (the statutory tax-floor computation feeding the 1702RT/1702Q filings, the W407/W481/W5508 class) and W5531 (the statutory disclosure layer of the audited AFS, the W481 class) — and **Tier 2 (1)** — W5529 (the treasury-asset-lifecycle class of W1867/W317, no statutory filing dependency). All three absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Register 5,404 → 5,407 rows (5,381 → 5,384 unique; T1 1,381 → 1,383, T2 3,265 → 3,266); proposed register stays empty (0 unclassified). Downstream figures re-pointed (workflows/README Quick Stats + Finance family + reconciliation line, value-stream-index header/VS-17+VS-42 rows/Finance subtotal/grand total/footer/detailed sections, VS-17 README 68 → 70, VS-42 README 24 → 25, root-README tree/Key-Metrics/coverage rows, WORKFLOW-FORMAT-GUIDE anchors, requirement-matrix inventory line, dependency-map intro + VS-133 row, touchpoint-map v88.0 footer, gap-analysis batch-10 note + companion doc, executive-summary footer, IT-model v2.7 FIN 799 → 802 and 4,872+509 → 4,875+509=5,384, sourcing-model v1.7 §12.1 ladder 3,265 → 3,266, semantic-audit-coverage registry annotated, audit-model-docs/audit-exec-ctl ANCHOR re-pins). `validate-repo.sh`: 0 errors / 0 warnings.*

*Date: 2026-09-03 | Workflow Criticality Classification v7.46 — IT operating-model gap fill (batch 8): the dedicated IT-domain gap analysis (workflow-gap-analysis-it.md) re-ran the §2 gap methodology across all 9 Technology & Data value streams plus IT-facing adjacent streams and found seven workflow-level surfaces unowned — the ~6,762-user M365/email/collaboration/telephony estate, internal core network services (DNS/DHCP/IPAM), the cross-estate peak-season change freeze, and the ISMS / adversarial-validation / insider-risk assurance layer ('Microsoft 365'/'tenant administration'/'digital workplace'/'email security'/'DMARC'/'IPAM'/'DHCP'/'change freeze' and a true-word 'ISMS' in zero dedicated `## W` headers; adjacent slices operations-generic: W366 WAN/ISP/Wi-Fi, W367 vulnerability ops, W387 quarterly ITGC CSA, W1205 PCI QSA cycle, W1409 weekly CAB). Seven workflows added to VS-27 and confirmed directly **Tier 2 (5)** — W5518 Collaboration & Productivity Platform (M365/Email/Teams) Operations & Tenant Governance, W5520 Core Network Services & IPAM (DNS/DHCP/IP-Schema) Management, W5521 Enterprise Release Calendar & Peak-Season Change-Freeze Governance (PA-27.1), W5522 ISMS Program, Security Certification & Security-Policy Lifecycle (ISO/IEC 27001), W5524 Enterprise DLP & Insider-Risk Monitoring (Endpoint/Email/Cloud) — the infrastructure-operations and governance/assurance class of their VS-27 siblings — and **Tier 3 (2)** — W5519 Enterprise Messaging & Store Telephony Services (UCC) Lifecycle (support-layer communications) and W5523 Enterprise Pentest, Red/Purple-Team & Attack-Surface Management Program (periodic assurance). Statutory dimensions (RA 10173 employee-monitoring proportionality in W5524, BIR CAS timestamp integrity in W5520) ride verification steps inside the workflows, matching the W5513/W5515 precedent. All seven absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Register 5,393 → 5,400 rows (5,370 → 5,377 unique; T2 3,256 → 3,261; T3 756 → 758); proposed register stays empty (0 unclassified). Downstream figures re-pointed (workflows/README Quick Stats + Technology & Data family + reconciliation line, value-stream-index header/VS-27 row/T&D subtotal/grand total/footer/detailed section, VS-27 README 62 → 69, root-README tree/Key-Metrics/coverage rows, WORKFLOW-FORMAT-GUIDE anchors, requirement-matrix inventory line, VS-133 README + PA-133.1/.3 Volume rows, dependency-map intro + VS-133 row, touchpoint-map v86.0 footer, gap-analysis batch-8 note, executive-summary footer, IT-model v2.5 INFRA 116 → 123 and 4,868+502 → 4,868+509=5,377, sourcing-model companion pin, audit-model-docs ANCHOR re-pin).

*Date: 2026-09-03 | Workflow Criticality Classification v7.45 — sourcing-model gap-fill pass: re-running the workflow-granularity gap methodology against the rest of the 2026-09-03 hybrid capability-sourcing extension (capability-sourcing-and-engineering-model.md §3–§9 — the surface batch 6's §12 scope deliberately left unexamined) found three program surfaces unowned at workflow level — the sourcing decision gate + Capability Sourcing Register, the best-of-breed product lifecycle, and the SEP paved road/engineering standard ('sourcing gate'/'golden path'/'paved road'/'ring deployment'/'upgrade currency'/'exit reserve'/'release intake'/'DORA'/'best-of-breed'/'configure' in zero dedicated `## W` headers while the adjacent VS-113 slices are each strategy/portfolio-generic: W3588 investment-governance ROI, W3589 vendor/platform strategy, W3577 portfolio rationalization, W3573 architecture exceptions). Three workflows added to VS-113 (one per PA, hosted where their theme lives) and confirmed directly **Tier 2** (the W3588/W3589 governance sibling class; the RA 10173/statutory-warranty clause dimension carried inside W5516's Step-3 verification gate, matching the W5513/W5511 precedent): **W5515** Sourcing Decision Gate Operation & Capability Sourcing Register (PA-113.3 — scored configure → buy → build assessment, the five mandatory appendices incl. the 808-control mapping, decision-rights routing to Product Council > PHP 25M and the CEO core-tier waiver, Register record + annual QBR reaffirmation + re-evaluation triggers); **W5516** Best-of-Breed Product Lifecycle Management, Vendor Release Intake & Exit Reserves (PA-113.2 — staging-ring intake with Tier-1-mandatory regression pack, defer-one-never-two upgrade currency with Tier & Control Board escalation, RA 10173/statutory-warranty/export/price-cap clause verification, tier-1 annual TPRM reassessment, QBR exit-reserve accrual); **W5517** SEP Paved Road & Engineering Standard Governance for Built Products (PA-113.1 — golden-path starts with ARB-recorded exceptions, trunk-based/feature-flag delivery, contract-first IAP with data contracts, ring deployment with SLO-burn rollback and the AppSec block right, production readiness review with typhoon resilience as a launch criterion, DORA-at-QBR reporting). All three absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Register 5,390 → 5,393 rows (5,367 → 5,370 unique; T2 3,253 → 3,256); proposed register stays empty (0 unclassified); the Tier-2 section heading + intro prose — stragglered at 3,250 by the batch-6 pass, which trued only the Summary — trued 3,250 → 3,256, and the `### Tier 2 Additions` sub-heading — stragglered at 495 by the same two passes (their six rows were appended to this section without bumping its parenthetical) — trued 495 → 501 by the 2026-09-03 consistency review pass. Downstream figures re-pointed (workflows/README Quick Stats + Technology & Data family + reconciliation line, value-stream-index header/VS-113 row/T&D subtotal/grand total/footer, VS-113 README 24 → 27, root-README tree/coverage/Key-Metrics/diagram, WORKFLOW-FORMAT-GUIDE anchors, requirement-matrix inventory line, VS-133 README + PA-133.1/.3 Volume rows + W5512's own intake figure, dependency-map intro + §8 block + §8.1 anchors + VS-113 row, touchpoint-map, gap-analysis batch-7 note + canonical totals line, executive-summary top footer, IT-model §3.2 CIO 77 → 80 and 4,868+499 → 4,868+502=5,370, sourcing-model §12.1 Tier-2 ladder 3,253 → 3,256 and §12.2 intake figure, OM v2.4, semantic-audit-coverage registry 5,370/5,370). `validate-repo.sh`: 0 errors / 0 warnings.*

*Date: 2026-09-03 | Workflow Criticality Classification v7.44 — agentic-AI platform gap-fill pass: re-running the workflow-granularity gap methodology against the 2026-09-03 Agentic-AI extension (sourcing model §12; OM v2.1 AAP team #15) found the agent lifecycle (intake → SIB sourcing routing → VS-128 registration → shadow/canary evaluation → runtime operation → QBR sunset) unowned at workflow level — 'agentic'/'agent runtime'/'shadow mode'/'canary'/'kill-switch'/'non-human identity' in zero dedicated `## W` headers while the adjacent VS-128 slices are each model-generic (W3931 registry, W3946 pre-deployment assurance, W3947 monitoring, W3948 retirement). Three workflows added to VS-128.3 and confirmed directly **Tier 2** (the W3945–W3948 lifecycle-operations sibling class; hard boundaries carried inside W5513's ratification gate, matching the W5511 precedent): **W5512** candidate intake, SIB sourcing routing & agent registry registration; **W5513** shadow & canary evaluation, graduation & autonomy-tier ratification; **W5514** runtime operations, guardrail & kill-switch telemetry, quarterly re-registration & portfolio sunset. Register 5,387 → 5,390 rows (5,364 → 5,367 unique; T2 3,250 → 3,253); proposed register stays empty (0 unclassified). Downstream figures re-pointed (workflows/README Quick Stats + Technology & Data family + reconciliation line, value-stream-index header/VS-128 row/T&D subtotal/grand total/footer, root-README tree/coverage/Key-Metrics/diagram, WORKFLOW-FORMAT-GUIDE anchors, requirement-matrix inventory line, VS-133 README + PA-133.1/.3 Volume rows, dependency-map intro + VS-133 row, gap-analysis batch-6 note, executive-summary top footer, IT-model §3.2/§9.1 DP 210 → 213 and 4,868+499=5,367 reconciliation, sourcing-model §12.1 Tier-2 ladder count 3,250 → 3,253, semantic-audit-coverage registry 5,367/5,367). `validate-repo.sh`: 0 errors / 0 warnings.*

*Date: 2026-09-03 | Workflow Criticality Classification v7.43 — event-custody pass: W5511 (gift-card dormancy monitoring, escheat evaluation & expired-liability derecognition; VS-54.3) added to the catalog and confirmed directly Tier 2 (the finance-operations class of its W2158–W2165 siblings; the statutory escheat filing rides the Legal Counsel gate inside the workflow). Register 5,386 → 5,387 rows (5,363 → 5,364 unique; T2 3,249 → 3,250); proposed register stays empty (0 unclassified). Downstream figures re-pointed (workflows/README Quick Stats + Finance family + reconciliation line, root-README coverage rows + tree rows, WORKFLOW-FORMAT-GUIDE anchors, requirement-matrix inventory line, VS-133 README + PA-133.1/.3 Volume rows, dependency-map intro + VS-133 row, gap-analysis current-state clause, IT-model §4.9 reconciliation 4,864+499 → 4,865+499). `validate-repo.sh`: 0 errors / 0 warnings across 64 checks.*

*Date: 2026-09-02 | Workflow Criticality Classification v7.42 — post-catalog confirmation pass: the fourteen post-catalog workflows W5497–W5510 (added 2026-08-24/26) confirmed 6 → Tier 1 / 6 → Tier 2 / 2 → Tier 3 by `07-methodology/confirm-postcatalog-14.py` (adjudications in the dated confirmation note above; three statutory-execution promotions W5498/W5503/W5504, one analytics promotion W5501, demotions W5509 → T3 and W5507/W5510 → T2, eight adoptions). Register 5,372 → 5,386 rows (5,349 → 5,363 unique; T1 1,375 → 1,381, T2 3,243 → 3,249, T3 754 → 756); proposed register regenerated empty (0 unclassified); downstream figures re-pointed (workflows/README Quick Stats + nav row, root-README coverage rows + tree rows, WORKFLOW-FORMAT-GUIDE anchors, dependency-map intro + v4.16 footer, gap-analysis current-state clause). `validate-repo.sh`: 0 errors / 0 warnings across 63 checks.*
*Date: 2026-08-28 | Workflow Criticality Classification v7.41 — consistency review #33 house-spelling normalization: the W4710 register-row title corrected **Dependant** → **Dependent** & Family Visa, Schooling & Relocation Support (VS-160), re-joining the register to the dominant repo spelling (dependent 118 vs dependant 23 occurrences before the sweep; the PA-160.2 H2 and its TOC anchor were normalized in the same pass, and the v7.39 footer paragraph was un-merged from inside v7.40's note where review #31 had absorbed it). No tier assignment, row count, or canonical total changed (5,372 rows / 5,349 unique; 5,363 workflows). `validate-repo.sh`: 0 errors / 0 warnings across 48 checks.*

*Date: 2026-08-26 | Workflow Criticality Classification v7.40 — consistency review #31 statutory-citation repair: the W5059 register-row title carries the correct LPG Industry Regulation Act number (RA 10617 → RA 11592; the act is the 2021 LPG Industry Regulation Act (RA 10617 -> RA 11592 because RA 10617 sits in the late-2013 numbering, predating the 17th/18th-Congress LPG bills' passage), so the number chain across reviews #13/#29/#31 reads RA 10862 -> RA 10617 -> RA 11592). No tier assignment, row count, or canonical total changed (5,372 rows / 5,349 unique; 5,363 workflows). `validate-repo.sh`: 0 errors / 0 warnings across 48 checks.*

*Date: 2026-08-26 | Workflow Criticality Classification v7.39 — one further post-catalog workflow-level gap fill added to the catalog (W5510 supplier service-fee billing & account deduction for store-rendered services — barcode labels & promotional collaterals — in VS-15.1; totals 5,362 → 5,363 workflows; Finance family 772 → 773). No confirmed register rows changed (5,372 rows / 5,349 unique stand); W5510 ships **unclassified** with a keyword-driven proposed Tier 1 tier (the `barcode` core-transactional keyword, same precedent as W5507 — the proposal register now holds 6 Tier 1 / 8 Tier 2 across the 14) in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) pending the next confirmation pass. Intro banner, §Summary proposed/coverage rows, Domain-Breakdown prose, and a dated 2026-08-26 batch-5 addition note re-pointed to 5,363 / 14-unclassified. `validate-repo.sh` green.*

*Date: 2026-08-26 | Workflow Criticality Classification v7.38 — two further post-catalog workflow-level gap fills added to the catalog (W5508 fringe benefits tax determination/valuation & quarterly BIR 1605 filing in VS-79.2; W5509 unfulfilled-demand & lost-sales capture, substitution analytics & replenishment feedback in VS-02.1; totals 5,360 → 5,362 workflows). No confirmed register rows changed (5,372 rows / 5,349 unique stand); the two ship **unclassified** with keyword-driven proposed Tier 1 tiers (the proposal register now holds 5 Tier 1 / 8 Tier 2 across the 13) in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) pending the next confirmation pass. Intro banner, §Summary proposed/coverage rows, Domain-Breakdown prose, and a dated 2026-08-26 batch-4 addition note re-pointed to 5,362 / 13-unclassified. `validate-repo.sh`: 0 errors / 0 warnings across 48 checks.*

*Date: 2026-08-26 | Workflow Criticality Classification v7.37 — consistency review #29 statutory-citation repair: the W5059 register-row title carries the correct LPG Industry Regulation Act number (RA 10862 → RA 10617; 1 spot — the superseded number had propagated from the PA-175.1 workflow title at Pass-24 authoring, and consistency review #13's statutory audit had adjudicated the wrong number correct). No tier assignment, row count, or canonical total changed (5,372 rows / 5,349 unique; 5,360 workflows). `validate-repo.sh`: 0 errors / 0 warnings across 46 checks.*

*Date: 2026-08-25 | Workflow Criticality Classification v7.36 — three further post-catalog workflow-level gap fills added to the catalog (W5505 concession item catalog/barcode/price-label onboarding & governance, W5506 concessionaire self-service price change request/approval & store-level propagation, W5507 concession service-fee billing & cost recovery — all in VS-07.1, extending W177; totals 5,357 → 5,360 workflows; Sell & Serve family 1,532 → 1,535). No confirmed register rows changed (5,372 rows / 5,349 unique stand); the three ship **unclassified** with keyword-driven proposed tiers (W5505/W5507 Tier 1 `barcode`, W5506 Tier 2; with W5497 the proposal register now holds 3 Tier 1 / 8 Tier 2 across the 11) in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) pending the next confirmation pass. Intro banner, §Summary proposed/coverage rows, Domain-Breakdown prose, and a dated 2026-08-25 batch-3 addition note re-pointed to 5,360 / 11-unclassified. `validate-repo.sh`: 0 errors / 0 warnings across 43 checks.*

*Date: 2026-08-25 | Workflow Criticality Classification v7.35 — two further post-catalog workflow-level gap fills added to the catalog (W5503 restricted-substance/chemical-content product compliance in VS-31.3; W5504 extreme-heat work-interruption & heat-stress management in VS-24.1; totals 5,355 → 5,357 workflows). No confirmed register rows changed (5,372 rows / 5,349 unique stand); the two ship **unclassified** with keyword-driven proposed Tier 2 tiers, joining W5497–W5502 (1 Tier 1 / 7 Tier 2 across the 8) in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) pending the next confirmation pass. Intro banner, §Summary proposed/coverage rows, Domain-Breakdown prose, and a dated 2026-08-25 addition note re-pointed to 5,357 / 8-unclassified. `validate-repo.sh`: 0 errors / 0 warnings across 43 checks.*
*Date: 2026-08-24 | Workflow Criticality Classification v7.34 — consistency review #26 (title-only register change, PDC-repair precedent): four duplicate-title repairs — W1185 retitled to its solicitation/incentives/fake-review slice, W1286 to its moderation-playbook/seeding/Q&A slice and W1311 to its escalation/amplification slice (W510 declared the canonical own-platform review workflow in PA-10.1, resolving the four-way same-scope cluster with conflicting review volumes), and W1543 retitled to its data-collection/monitoring layer (W1396 remains the benchmarking/carbon analytics layer; same-title pair in VS-25 resolved); W1638 retitled to the reverse-logistics program view (store-side execution stays canonical in W176, whose cadence/volume W1638 now follows) and W1731 retitled to the governance/TP layer (operational registry stays in W2582, agreement counts harmonized at ~20 across 5 entities). No tier assignments, register-row counts, or totals changed. `validate-repo.sh`: 0 errors / 0 warnings across 42 checks.*
*Date: 2026-08-24 | Workflow Criticality Classification v7.33 — six post-catalog workflow-level gap fills added to the catalog (W5497–W5502; totals 5,349 → 5,355 workflows). No confirmed register rows changed (5,372 rows / 5,349 unique stand); the six ship **unclassified** with keyword-driven proposed tiers (1 Tier 1 / 5 Tier 2) in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md), mirroring the pre-2026-06-28 convention until the next confirmation pass. Intro banner, §Summary proposed/coverage rows, and Domain-Breakdown prose re-pointed to 5,355 / 6-unclassified. `validate-repo.sh`: 0 errors / 0 warnings across 41 checks.*
*Date: 2026-08-24 | Workflow Criticality Classification v7.32 — consistency review #25 (repo hygiene, no register change): validator Checks 40 (validator self-description agreement) and 41 (quoted requirement-total/category-count agreement) added; no tier assignments, register rows, headings, or totals altered in this document. `validate-repo.sh`: 0 errors / 0 warnings across 41 checks.*
*Date: 2026-08-24 | Workflow Criticality Classification v7.31 — PDC consistency repair: the Core Financial rows W423 and W425 are retitled to their treasury-companion scope (W423 — treasury execution companion of the canonical customer-PDC lifecycle W1380; W425 — treasury financial-reversal companion of the canonical bounced-check resolution W1381; both canonical workflows are defined in VS-16 and carry their own register rows). No tier assignments, register-row counts, or totals changed. `validate-repo.sh`: 0 errors / 0 warnings across 39 checks.*

*Date: 2026-08-24 | Workflow Criticality Classification v7.30 — consistency review #23: the Classification Rules intro still quoted the pre-review-#22 priority split — **Must Have requirements (431)** / **Should Have requirements (296)** — although the register itself had shrunk to 728 rows (429 Must / 293 Should / 6 Nice) when the five exact-duplicate requirement rows were removed; both figures re-pointed to the canonical counts (no tier assignments affected). Validator Check 37 added (derives the split from the erp-requirements.md register and validates every quoted figure against it, including the root-README Key Metrics rows and repo-wide 'N Must / M Should / K Nice' triples). `validate-repo.sh`: 0 errors / 0 warnings across 37 checks. Prior v7.29 (2026-06-28) — consistency review #15: two stale pre-confirmation figures repaired in current-state §Summary prose — the register note's canonical-`##`-workflow complement and the §Domain Breakdown's classified-register-row figure, both frozen at their v7.26 values (register 2,776 → 5,372 rows; unique 2,753 → 5,349) — both introduced by the Full-Coverage Confirmation Pass updating the Summary table but not the surrounding prose. Validator Check 27 Part A now guards those two figures in current-state prose. Prior v7.28 — Full-Coverage Confirmation Pass: every remaining unclassified workflow promoted into the confirmed register via [`07-methodology/confirm-all-workflows.py`](../../07-methodology/confirm-all-workflows.py), applying the calibrated rules documented across batches v7.19–v7.27 (statutory/regulatory execution → Tier 1; analytics/scorecard/optimization → Tier 3; standard operational support → Tier 2). Of the final batch (2,596 → 0): **65 promoted to Tier 1** (statutory/regulatory execution the keyword default sent to Tier 2 — BOC advance rulings/post-entry audit/alert-order resolution, CTR/AMLC filing, SEC annual filing, PFRS 15/16 statutory accounting, DOLE D.O. 174/OSH/AEP, BFP fire-code, DENR hazardous-waste/EPR, NPC audits, legal hold, DSAR erasure, LTFRB, BSP reporting), **179 promoted to Tier 3** (analytics/optimization), **3 demoted from proposed Tier 1 to Tier 2** (program support: staff training/design), and **2,349 adopted at the proposed tier** (the documented safe default). Register 2,776 → 5,372 rows (2,753 → 5,349 unique; T1 801 → 1,375, T2 1,549 → 3,243, T3 426 → 754); unclassified 2,596 → 0; `workflow-criticality-proposed.md` regenerated to zero rows. Cross-reference docs reconciled (workflows/README Quick Stats, root README coverage row, dependency-map v4.6, touchpoint-map v75.0, format-guide layout). `validate-repo.sh`: 0 errors.*

*Date: 2026-06-26 | Workflow Criticality Classification v7.27 — §Summary *Proposed classification* mirror reconciled to the regenerated proposed register: proposed/unclassified **2,564 → 2,596** (per-tier **507 / 1,912 / 145 → 512 / 1,935 / 149**). The intro banner and Grand-Total coverage row already carried the then-current figure — the drift came from the 2026-06-25 VS-127 PA-127.4 regeneration of [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) not being propagated into this mirror. Validator **Check 25** added (Part A guards exactly this mirror-vs-register reconciliation). `validate-repo.sh`: 0 errors / 3 warnings. Prior v7.26 — Pass 26–29 confirmation batch: 14 value streams (VS-178–VS-191, 336 workflows). **117 → T1** (statutory/regulatory execution the keyword rules missed — DAR/NCIP/FPIC land clearances, NSWMC EPR filings, DTI price-freeze reporting, TESDA/BIR DTS reports, BFP/LGU structural clearances, CDA verification, DOLE-OSH equipment certification, DENR-EMB RA 6969 hazardous-waste permitting/reporting, BSP/SEC/Truth-in-Lending RA 3765 disclosure & examination support); **24 → T3** (analytics/scorecard/dashboards); **195 T2**. Confirmed 2,440→2,776 rows (2,417→2,753 unique; T1 684→801, T2 1,354→1,549, T3 402→426); unclassified 2,900→2,564 (51.8%); proposed 507/1,912/145. Rows placed in the family-grouped Additions subsections (Asset & Infrastructure and Finance family subsections created where absent). **All 103 gap-analysis VSs (VS-89–VS-191) now confirmed.** `validate-repo.sh`: 0/1. Prior v7.25 — seventh & final family-decisive batch: 5 VSs (VS-165/169/172/176/177, 120 workflows). **12 → T1** (PCAB license/registration/renewal/project-filing/audit-response/personnel, DOLE PPE, RA 10173 health-data, PCAB installer verification, copyright/IP, doc confidentiality, store override auth); **12 → T3**; **96 T2**. Confirmed 2,320→2,440 rows (2,297→2,417 unique; T1 672→684, T2 1,258→1,354, T3 390→402); unclassified 2,684→2,564 (48.5%); proposed 507/1,912/145. **All 53 family-decisive VSs confirmed.** `validate-repo.sh`: 0/2. Prior v7.24 — sixth batch. **10 → T1** (PCC merger notification, political-contribution/election-compliance/anti-graft, corporate-security K&R/active-assailant/investigations); **24 → T3**; **158 T2**. Confirmed 2,128→2,320 rows (2,105→2,297 unique; T1 662→672, T2 1,100→1,258, T3 366→390); unclassified 2,876→2,684 (46.1%); proposed 514/2,023/147 (zero drift). `validate-repo.sh`: 0/2. Prior v7.23 — fifth batch (Shared Services & Specialized Support): 8 VSs (VS-103/106/107/109/115/116/119/123, 192 workflows). **18 → Tier 1** (PFRS 9 hedge accounting, DTI Weights & Measures, bid/performance-bond statutory issuance/claim/dispute, whistleblower speak-up/investigation/anti-retaliation/external-reporting, TESDA apprenticeship compliance); **36 → Tier 3** (analytics); **138 T2**. Confirmed 1,936→2,128 rows (1,913→2,105 unique; T1 644→662, T2 962→1,100, T3 330→366); unclassified 3,068→2,876 (42.3%); proposed 518/2,209/149 (zero drift). `validate-repo.sh`: 0/2. Prior v7.22 — fourth hand-confirmation batch (Mixed Operations): 8 VSs (VS-57/58/66/69/70/71/74/101, 192 workflows). **15 → Tier 1** (typhoon-BCP emergency, anti-counterfeit enforcement, electrical-permit compliance, OTB financial gate); **36 → Tier 3** (analytics); **141 T2**. Confirmed 1,744→1,936 rows (1,721→1,913 unique; T1 629→644, T2 821→962, T3 294→330); unclassified 3,260→3,068 (38.4%); proposed 525/2,389/154 (zero drift). `validate-repo.sh`: 0/2. Prior v7.21 — third hand-confirmation batch (Operational Support): 8 VSs (VS-40/43/55/63/64/65/83/84, 192 workflows). **21 → Tier 1** (PFRS capex capitalization/interest/conversion, DOLE occupational-health reporting/exposure-monitoring/Mental-Health-Act, DOLE/NLRC labor-relations mandatory: union certification, CBA conciliation/ratification, 2-notice-rule/discipline/SENA, reinstatement, strike-lockout notice, emergency-comm-protocol); **30 → Tier 3** (space/productivity/clearance/channel analytics, churn prediction, planogram/seasonal analytics, engagement surveys, ROI analyses); **141 confirmed Tier 2**. Confirmed 1,552→1,744 rows (1,529→1,721 unique; T1 608→629, T2 680→821, T3 264→294); unclassified 3,452→3,260 (34.6%); proposed regenerated (535/2,566/159, no drift). `validate-repo.sh`: 0/2. Prior v7.20 — second hand-confirmation batch (Support & Governance): 8 family-decisive Tier-2 VSs (VS-100/104/112/113/126/129/133/139, 192 workflows) promoted from the keyword proposal after genuine review calibrated to the register's existing optimization/analytics=Tier 3 placement. **14 → Tier 1** (statutory execution the keyword rules missed: litigation hold/filing/enforcement & loss-contingency, corporate-secretarial/SEC, regulatory-investigation defense, merger-notification/PCC pre-filing, PCC investigation/dawn-raid/litigation/penalty, political-activity/lobbying disclosure, CDP DSAR/consumer-rights, event-permit/prize-withholding); **29 → Tier 3** (analytics/optimization defaulted to Tier 2: process/task mining, cost-out & productivity programs, OpEx maturity, CDP recommendation/CLV/attribution analytics, IP/legal/portfolio analytics); **149 confirmed Tier 2**. Confirmed 1,360→1,552 rows (1,337→1,529 unique; T1 594→608, T2 531→680, T3 235→264); unclassified 3,644→3,452 (30.7% classified); proposed regenerated (543/2,747/162). `validate-repo.sh`: 0 errors / 2 warnings. Prior v7.19 — first hand-confirmation batch: the 8 wholly-statutory value streams (VS-79/85/89/91/114/117/118/125, 192 workflows) promoted from the keyword proposal into the confirmed register after genuine tier review — 154 confirmed Tier 1 (statutory execution), 32 demoted to Tier 2 (program support: training / reporting / change-monitoring / cost-or-insurance recovery), 6 demoted to Tier 3 (analytics / continuous improvement); see the 'Statutory-Compliance Classification Pass' block above. Confirmed 1,168→1,360 rows (1,145→1,337 unique; Tier 1 440→594, Tier 2 499→531, Tier 3 229→235); unclassified 3,836→3,644; proposed register regenerated via `classify-workflows.py --write` (now 548 / 2,929 / 167 — which also dissolved one row of prior proposed-file drift). `validate-repo.sh`: 0 errors / 2 warnings. Prior v7.18 — grand total reconciled to 4,981 unique workflows (1,145 confirmed + 3,836 unclassified) after restoring the VS-12 PA-12.2 ghost workflow's missing `## W1318.` header (Tool Rental Reservation, Waitlist & Scheduling); the §Summary table and intro/banner above now read 4,981/3,836, the proposed register was regenerated via `classify-workflows.py --write`, and `validate-repo.sh` Check 17 (ghost detection) now reports 0. Prior v7.17 — §Summary *Proposed classification* subsection reconciled to the regenerated proposed register: unclassified **3,595 → 3,835** (per-tier **688 / 2,608 / 155 → 741 / 2,927 / 167**), now matching [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) exactly. The drift accumulated across Passes 19–25 (VS-162–VS-177, +240 workflows) because only the proposed file was being regenerated, not this mirror. The Confirmed Total (1,168 rows / 1,145 unique) and Grand Total (4,980) were already correct. v7.16 — Summary-table `% of Classified` percentages corrected (Phase 1 37.6%→37.7%, Phase 2 42.8%→42.7%) to match standard rounding of 440/1,168 and 499/1,168 (Phase 3 19.6% was already correct). v7.15 — W40 (Regular Price Change Execution) moved from Core Finance to Core Merchandising & Pricing (subsection move only; a pricing workflow refiled next to its sibling W13; tier-1 total unchanged). v7.14 — 1,145 unique `##` workflows are classified (Tier 1: 440 · Tier 2: 499 · Tier 3: 229 = 1,168 register rows, of which 23 are `###` parent/summary sub-workflows e.g. W2, W5B, W9A that are double-counted against a `##` parent, so unique classified = 1,145). 3,451 workflows remain unclassified (4,596 unique `##` workflows − 1,145 classified); all 3,451 carry a keyword-driven proposed tier in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) (688 Tier 1 / 2,608 Tier 2 / 155 Tier 3). The authoritative tier summary is the `## Summary` table above. VS-49–VS-52 were retired in the 2026-06-14 placeholder-content review (96 placeholder workflows removed; numbers unused); VS-89–VS-161 were added across eighteen gap-analysis passes (W2993–W4744). Full per-pass history — candidates considered, workflow-ID allocation, and the register-rows-vs-unique reconciliation — is in [`workflow-gap-analysis.md`](workflow-gap-analysis.md) and [`CHANGELOG.md`](../../CHANGELOG.md).*
