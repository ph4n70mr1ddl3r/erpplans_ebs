# EBS Module Coverage Map — Making the Most of the Suite

> The model company's [workflow-system-touchpoint-map](../01-model-company/workflows/workflow-system-touchpoint-map.md)
> classifies every workflow against **generic ERP modules**. This document maps each generic
> module to the **specific Oracle EBS products and setups** that carry it — the constructive
> half of the fit-gap exercise: what the suite already does, before any gap discussion.
> Gaps and their dispositions live in the [fit-gap analysis](fit-gap-analysis.md).

Part of the [02-oracle-ebs blueprint](README.md).

---

## 1. Generic Module → EBS Realization Register

The module names in column 1 are exactly the section headings of the touchpoint map, so the
two documents read side-by-side.

| Touchpoint-map module | EBS realization (products + key setups) | Coverage posture |
|---|---|---|
| **POS / Retail** | No EBS POS exists and none is needed — **the in-house POS platform is already built**. The program is integration: **EBS owns everything behind it** (item/UOM/tax/price masters in INV, QP, eBTax; store orgs & subinventories; near-real-time sales interface into OM/AR; nightly completeness reconciliation; trade/corporate pricing via QP qualifiers) | Already built — EBS-mastered |
| **Inventory Management** | **Oracle Inventory** — orgs per store/DC, subinventories/locators, UOM & conversions, perpetual WAC (cost groups), min-max/reorder points, cycle counts & physical inventory (tags, ABC classes), inter-org transfers w/ in-transit, consigned inventory, lot/serial where required; **In-Memory Cost Management** for real-time costing/margin analytics (C15) | Standard |
| **Procurement** | **Purchasing + iProcurement + Sourcing + iSupplier + SLM**: req→PO with AME approvals, blanket releases (W2C), receiving, 3-way match, supplier registration & portal ASNs/invoices, RFQ/tender (W166), import POs (W2B) with **Landed Cost Management** true-up | Standard |
| **Warehouse Management** | Executed **in-suite on Oracle WMS/MSCA** — adopted under the two-tier doctrine (it ships with EBS, so we use it). EBS side: org/subinventory/locator model, LPN interface, ship-confirm (WSH) | In-suite |
| **Financials (GL/AP/AR)** | **GL + SLA + AP + AR + CE + IBY + FA**: ledgers for 5 legal entities on one CoA; 3-way match AP with EWT via eBTax withholding; AR AutoInvoice + credit memos (W540); PDC registers (W423/W424) via AR/AP special terms + CE; bank reconciliation (W89); FSG statements; asset accounting incl. CIP (W276); **GL budgets + budgetary control** funds-check the capex chain (F6); **Revenue Management and Invoicing** carries the multi-element revenue schedules (A11 — the PFRS 15 EXT retired 2026-09-16) | Standard |
| **Supply Chain Planning** | Min-max/reorder-point planning in INV (W2A auto-replenishment); **Oracle ASCP + Demantra (EBS-family Value Chain Planning) adopted** as the planning stack for statistical forecasting and S&OP (W31, W133, VS-127) — resolved under the two-tier doctrine; the same stack's **Inventory Optimization/Rapid Planning** engines serve VS-136's multi-echelon network & inventory engineering (W4129–W4136); license cost is a FinOps decision | Standard core + Oracle planning stack |
| **HR & Payroll** | **Oracle HRMS (PER)** carries the people data of record — org/positions/employees, EITs, absence (Core HR stays in EBS). Benefits enrollment/eligibility rides **Advanced Benefits (OAB)**, its deduction envelopes feeding Payroll PH. **Payroll is an in-house build (Payroll PH)**: PH statutory gross-to-net (SSS/PhilHealth/Pag-IBIG, PD 851 13th month, BIR withholding) and compensation outputs live there; it posts costing journals into GL (EBS stays the ledger of record). Store scheduling/time capture is likewise an in-house build feeding validated interfaces (timecards retire through OTL/BEE) | EBS core + in-house builds |
| **Ecommerce** | The **custom ecommerce platform is already built** (the canonical migration table records it as the in-house estate). EBS: order import (OM), inventory availability feeds (5-min SLA), fulfillment status via business events, payment reconciliation to AR, IC settlement for BOPIS (W11). **iStore deliberately not adopted** | Already built — EBS-fulfilled |
| **CRM / Loyalty** | The **loyalty/engagement stack is already built** in-house. EBS side: **Trading Community Architecture (TCA)** is the customer master of record (party/site/account model, DQM dedup for W253), credit profile & limit management (Credit Management), collections (IEX), complaint/credit workflows ride workflow + EITs where ledger-adjacent | EBS-master (TCA), built-engagement |
| **Pricing / Merchandising** | **Advanced Pricing**: price lists (regular W40, clearance W93), modifiers & qualifiers (promo rules W13, coupon W539), PH mandatory-discount qualifiers (VS-85), price-break/quantity pricing, competitor price-match rules (W61) as controlled modifiers; pricing hierarchy governance (W107) via QP lists & categories; markdown accounting via margin analysis feeds (W85) | Standard (execution in the POS platform under EBS masters) |
| **Master Data** | EBS **is** the MDM system of record for: items (INV/EGO catalogs & templates — W252), suppliers (SLM — W287), customers (TCA — W253), UOM (W294), payment terms (W295), banks (CE — W309), fiscal calendars (GL — W308), FX rates (GL daily rates — W307), cost/RP parameters. Governance runs via Web ADI mass-update + workflow approvals; the non-EBS domains (planogram templates, digital assets, CDP identities) are owned by their in-house builds per the touchpoint map | Standard |
| **Reporting / Analytics** | **FSG** (financial statements W9 family), **BI Publisher** (statutory & operational formats incl. the BIR pack), **Enterprise Command Centers** (payables/receivables/inventory/procurement dashboards — Tier-3 analytics), Web ADI reports; enterprise BI stays with the in-house **DP** data platform (OM §5) fed by EBS — reporting is deliberately *not* consolidated into a BoB BI on top of EBS | Standard + DP |
| **Loss Prevention** | POS exception feeds land in IAP → LP exception queues (in-house/agent surface per VS-23); EBS carries the **financial terminus**: shrinkage write-off journals with approval ladders (W37, W92), quarantine write-offs (W219), SLOB provisioning (W220) | Split by design |
| **Store Lifecycle** | W16 new-store org runbook (INV org, MOAC, price list, POS mapping); W45/W59 closure/relocation via org close + FA transfers; store P&L by org; permits (W54) tracked via EITs on location records | Standard |
| **Facility Maintenance** | **Oracle eAM** — adopted in-suite 2026-09-16 (fit-gap F5, §4-13; the prior 'no native EAM' claim corrected): eAM asset register FA-linked, work-request intake, PM scheduling with generated work orders, work-order costing to GL/AP. Carries store/DC/HQ facility work orders (W47/W240/W241), generator & MHE PM (W808/W1403), tool-rental fleet lifecycle (W1172), EVSE and renewable O&M (W4785/W4786, W3459/W3460), and the calibration device estate as maintainable assets (VS-115) | Standard (in-suite) |
| **IT Operations** | ITSM stays with its tooling (VS-27); EBS-side touchpoints: FND user & responsibility lifecycle (W152), environment & masking management (W384), archiving (W396) | Process-owned |
| **Business Continuity** | DR via Data Guard + the environment strategy (architecture §4); BCP process itself is VS-26 documentation, not EBS function | Platform-provided |
| **Product Information** | PIM/DAM is an in-house build (VS-137); EBS item master holds the commercial spine (codes, categories, UOM, tax, barcodes/GTIN via item cross-references W311) | Build-rich, EBS-core |
| **Training & Development** | Oracle Learning Management for calendar/enrollment/compliance basics; deeper LMS function, if ever needed, is a build | Standard-light |
| **Fleet Management** | No EBS fleet product in footprint; vehicles as FA assets + fuel/maintenance via AP and telematics feeds (VS-06) | Build-fed, EBS-accounted |
| **Data Privacy & Compliance** | Consent/DSAR workflows are build/process (VS-91); EBS carries audit-trail options, data-masking in clones (W384), and retention via archiving | Supporting |
| **Regulatory Operations** | Permits/licences tracked via EITs/attachments on the governed records (VS-166); date alerting rides **Oracle Alert (ALR)** over the EIT registers (G9); no EBS regulatory module exists — registers stay process-owned | Process-owned + EBS alerting |
| **Customer Order Management** | **Order Management**: backorders (W56) via **Global Order Promising** multi-org ATP + allocation rules (D15), order holds, customer notifications via workflow events | Standard |
| **Corporate Account Management** | OM sales agreements + project record structures (Projects for W58 project budgets), staged call-off orders (W164) via blanket releases against agreements, retention billing (W165) via project billing | Standard |
| **Vendor Contract Management** | **Oracle Procurement Contracts** (B12, adopted 2026-09-16): clause library, contract authorship, deliverables with due dates, expiry/amendment alerts, PO/agreement integration driving W669 compliance monitoring; 3PL contracts as supplier agreements (W62B); facility-vendor SLAs on the same spine (W241) | Standard |
| **Customer Experience** | CSAT/NPS capture and personalization run on the in-house CX surfaces (VS-13); complaint service requests — ticket, SLA timers, tiered escalation — ride **EBS Teleservice/Service Requests + Escalation Management** on the TCA party model (fit-gap D14) | Built + EBS |
| **Marketing / Campaign** | In-house marketing stack (VS-14); EBS touchpoints: Trade Management for vendor-funded promo claims (resolved in-suite), otherwise AP for spend | Built + EBS |
| **Real Estate** | **Property Manager**: lease abstraction, rent/CAM/indexation billing (W117/W118), critical-date workflows; real-property tax via AP + PN schedules (W119) | Standard |
| **Internal Audit** | EBS-native evidence: FND audit, ERES, AME logs, role-assignment queries for W338 SoD review; audit management itself is process (VS-21) | Evidence-provider |
| **Governance / Strategy** | Process-owned; EBS touchpoints limited to budgets (GL) and board-approval evidence via workflow | Process-owned |
| **Engineering & Construction** | **Projects** carries construction cost capture/CIP for W223–W227; scheduling stays PMO tooling | Standard-light |
| **HSE / Safety** | Process-owned (VS-24); EBS touchpoint: incident-driven AP/FA entries | Process-owned |
| **Services / Rental** | Service work orders (W544) via OM service lines + Projects where project-ized; tool rental deposits via AR deposits/commitments (W139); in-store fabrication configuration & quotes ride **Oracle Configurator** (CZ, in-store counter scope — C16); **Lessor equipment leasing (VS-96) rides Lease & Finance Management** — booking, billing schedules → AR, asset/end-of-term (fit-gap A13); installation dispatch rides the **Field Service** core (fit-gap D13) with the consumer experience layer built | Standard-light + EBS |
| **Wholesale / B2B** | OM + QP corporate price books (W163), punch-out via XML Gateway/cXML (W283), EWT on wholesale (W145) | Standard |
| **Innovation & Digital Transformation** | Not an EBS function — the AI/ML/RPA/innovation lifecycle (W200–W203, W208, W420) runs on the in-house platforms (the AAP agentic runtime, DP) reaching EBS only through IAP contracts; EBS's own surfaces are its operational dashboards (Enterprise Command Centers) and approval eventing | Build-led, EBS-integrated |
| **Document Management** | Process-owned under the VS-88 retention discipline; EBS carries FND attachments on the migrated entities, ERES e-signature evidence on controlled approvals, and the W396 archiving/retention tier | Process-owned + ERES/attachments |

---

## 2. Family Coverage Summary

Roll-up by the workflow catalog's 8 value-stream families
([workflows/README.md](../01-model-company/workflows/README.md)):

| Family | EBS posture | Headline |
|---|---|---|
| **Plan & Source** (462 WF) | Core EBS | Merchandise planning, S&OP and the sourcing/PO spine fully EBS (Purchasing/iProcurement/LCM); statistical forecasting and IBP ride the adopted Oracle ASCP + Demantra planning stack; merchandise-planning analytics split with the in-house DP |
| **Make & Move** (500 WF) | EBS-ledgered, in-suite-executed | Warehouse and carrier execution run in-suite (Oracle WMS/MSCA, Shipping/OTE); EBS owns the inventory ledger, kitting/BOM, inter-org transfers, freight-cost accounting and landed cost |
| **Sell & Serve** (1,546 WF) | EBS-mastered, built-executed | The POS estate, ecommerce platform, and loyalty stack are already built — they execute; EBS owns item/price/tax/credit/order masters and the AR ledger |
| **Finance** (785 WF) | Core EBS | GL/AP/AR/CE/XTR/FA — the strongest standard fit in the suite; the BIR indirect-tax pack is the one EBS-held localization (VS-79); gift-card liability, vendor rebates and capex accounting post natively; GL budgets funds-check the capex chain (F6) and RM&I retires the PFRS 15 extension (A11) |
| **People** (445 WF) | Core EBS + in-house payroll/workforce builds | Core HR data of record in EBS (PER); the payroll engine, its statutory outputs and the store workforce platform are in-house builds posting into EBS (E3–E8) |
| **Asset & Infrastructure** (323 WF) | Core EBS | eAM carries facility/equipment work orders and PM (F5); Property Manager, FA and Projects carry leases, right-of-use schedules (the A12 EXT), capex/CIP, store construction and facilities |
| **Governance & Assurance** (976 WF) | Process + EBS evidence | Registers, filings and assurance workflows are process-owned; EBS supplies the evidence layer (FND audit, ERES, AME logs) and the financial termini (shrinkage write-offs, claims, quarantine) |
| **Technology & Data** (390 WF) | Process + platform | EBS is itself the governed platform (W384/W396); DP/IAP in-house per register |

---

## 3. What EBS Is Deliberately *Not* Used For

Restating the boundary keeps later scope-creep honest. The suite is not adopted for:

1. **Storefront/checkout execution** — the **already-built in-house POS estate and ecommerce
   platform** execute under EBS masters. No iStore, no Forms-based selling, no rebuild — the
   program is integration (flows W533–W541 and the W2B-class ecommerce imports).
2. **Warehouse/transport execution and store scheduling** — warehouse and carrier execution
   run **in-suite** (Oracle WMS/MSCA, Shipping/Transportation Execution, adopted under the
   two-tier doctrine); store workforce scheduling/time capture is an **in-house build**.
3. **Omnichannel order orchestration & trade-project coordination** — in-house OMO/TPS per
   the register; EBS OM carries the fulfillment legs OMO routes to.
4. **Deep PIM/DAM, planogram/space, CDP** — in-house builds (VS-55/137/126).
5. **Enterprise BI** — in-house DP (OM §5); EBS provides FSG/BI Publisher/ECC for
   operational and statutory reporting only.

---

*Document Version: 1.3 | Date: 2026-09-16 | **Second-pass EBS-exhaustion audit realization trues:** the Facility Maintenance row re-pointed in-suite to Oracle eAM (fit-gap F5, §4-13 — the 'no native EAM in this footprint' claim corrected, the same doctrine logic as the WMS adoption); the Vendor Contract Management row re-pointed to Oracle Procurement Contracts (B12); the Financials row names GL budgets + budgetary control (F6) and Revenue Management and Invoicing for the retired PFRS 15 extension (A11); the Inventory Management row names In-Memory Cost Management (C15); the Supply Chain Planning row names Inventory Optimization/Rapid Planning for VS-136; the Customer Order Management row names Global Order Promising (D15); the Services / Rental row names Oracle Configurator for in-store fabrication (C16); the Regulatory Operations row names Oracle Alert (G9); the Finance and Asset & Infrastructure family headlines trued. No row-set or count changes. Prior v1.2 | Date: 2026-09-15 | **EBS-exhaustion audit realization trues:** the HR & Payroll row names Advanced Benefits (OAB) enrollment feeding Payroll PH; the Customer Experience row re-pointed — complaint service requests ride EBS Teleservice/Escalation Management (fit-gap D14) while CSAT/personalization stay in-house; the Services / Rental row names Lease & Finance Management for VS-96 lessor leasing (A13) and the Field Service dispatch core (D13). No row-set, family-table or count changes. Prior v1.1 | Date: 2026-09-14 | Two-tier sourcing doctrine enacted (in EBS → use it; otherwise → build): WMS/TMS execution adopted in-suite (Oracle WMS/MSCA, Shipping/OTE), POS/ecommerce/loyalty re-pointed as already-built in-house platforms (integrate, never rebuild), payroll and store-workforce re-scoped to in-house builds with PER/EBS keeping the data and ledger of record, Oracle planning stack (ASCP/Demantra) adopted, family table and non-adoption boundary re-worded. Prior v1.0 (2026-09-14): initial issue — generic-module → EBS realization register mirroring the touchpoint-map section headings; family roll-up; deliberate non-adoption boundary. Canon anchors: touchpoint-map module set; sourcing register §4; family totals 462/500/1,546/785/445/323/976/390 = 5,427.*
