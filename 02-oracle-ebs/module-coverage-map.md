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
| **POS / Retail** | No EBS POS exists. POS edge owns checkout/offline; **EBS owns everything behind it**: item/UOM/tax/price masters (INV, QP, eBTax), store orgs & subinventories (INV), near-real-time sales interface into OM/AR, nightly completeness reconciliation, trade/corporate pricing via QP qualifiers | EDGE-executed, EBS-mastered |
| **Inventory Management** | **Oracle Inventory** — orgs per store/DC, subinventories/locators, UOM & conversions, perpetual WAC (cost groups), min-max/reorder points, cycle counts & physical inventory (tags, ABC classes), inter-org transfers w/ in-transit, consigned inventory, lot/serial where required | Standard |
| **Procurement** | **Purchasing + iProcurement + Sourcing + iSupplier + SLM**: req→PO with AME approvals, blanket releases (W2C), receiving, 3-way match, supplier registration & portal ASNs/invoices, RFQ/tender (W166), import POs (W2B) with **Landed Cost Management** true-up | Standard |
| **Warehouse Management** | Execution stays BoB WMS per the sourcing register (VS-04/05). EBS side: org/subinventory/locator model, LPN interface, ship-confirm (WSH). **Oracle WMS/MSCA is the in-suite parity candidate** — the register's own re-evaluation trigger; SIB assessment scheduled (fit-gap §4) | EDGE (EBS-ledgered) |
| **Financials (GL/AP/AR)** | **GL + SLA + AP + AR + CE + IBY + FA**: ledgers for 5 legal entities on one CoA; 3-way match AP with EWT via eBTax withholding; AR AutoInvoice + credit memos (W540); PDC registers (W423/W424) via AR/AP special terms + CE; bank reconciliation (W89); FSG statements; asset accounting incl. CIP (W276) | Standard |
| **Supply Chain Planning** | Min-max/reorder-point planning in INV (W2A auto-replenishment); **ASCP + Demantra are license-flagged** for statistical forecasting/S&OP (W31, W133, VS-127) — dispositioned in fit-gap §4; transfers & allocation logic via internal requisitions and IAP orchestration (OMO owns omnichannel allocation per register) | Standard core; planning license decision open |
| **HR & Payroll** | **Oracle HRMS (PER) + Oracle Payroll (PAY)**: org/position/employee master, EITs, absence; payroll gross-to-net with the **PH localization pack** (SSS/PhilHealth/Pag-IBIG, PD 851 13th month, BIR withholding tables, 2316/1601-C/1604-C, alphalist) — the single largest localization (fit-gap §6). Store scheduling/time capture stays BoB WFM per register; BEE imports into PAY | Standard core + LOC pack |
| **Ecommerce** | Ecommerce platform stays edge (VS-10). EBS: order import (OM), inventory availability feeds (5-min SLA), fulfillment status via business events, payment reconciliation to AR, IC settlement for BOPIS (W11). **iStore deliberately not adopted** | EDGE-executed, EBS-fulfilled |
| **CRM / Loyalty** | Loyalty/CRM stays edge per the integration map. EBS side: **Trading Community Architecture (TCA)** is the customer master of record (party/site/account model, DQM dedup for W253), credit profile & limit management (Credit Management), collections (IEX), complaint/credit workflows ride workflow + EITs where ledger-adjacent | EBS-master (TCA), EDGE-engagement |
| **Pricing / Merchandising** | **Advanced Pricing**: price lists (regular W40, clearance W93), modifiers & qualifiers (promo rules W13, coupon W539), PH mandatory-discount qualifiers (VS-85), price-break/quantity pricing, competitor price-match rules (W61) as controlled modifiers; pricing hierarchy governance (W107) via QP lists & categories; markdown accounting via margin analysis feeds (W85) | Standard (execution at POS edge under EBS masters) |
| **Master Data** | EBS **is** the MDM system of record for: items (INV/EGO catalogs & templates — W252), suppliers (SLM — W287), customers (TCA — W253), UOM (W294), payment terms (W295), banks (CE — W309), fiscal calendars (GL — W308), FX rates (GL daily rates — W307), cost/RP parameters. Governance runs via Web ADI mass-update + workflow approvals; the non-EBS domains (planogram templates, digital assets, CDP identities) stay with their edge owners per the touchpoint map | Standard |
| **Reporting / Analytics** | **FSG** (financial statements W9 family), **BI Publisher** (statutory & operational formats incl. the BIR pack), **Enterprise Command Centers** (payables/receivables/inventory/procurement dashboards — Tier-3 analytics), Web ADI reports; enterprise BI stays with the in-house **DP** data platform (OM §5) fed by EBS — reporting is deliberately *not* consolidated into a BoB BI on top of EBS | Standard + DP |
| **Loss Prevention** | POS exception feeds land in IAP → LP exception queues (edge/agent surface per VS-23); EBS carries the **financial terminus**: shrinkage write-off journals with approval ladders (W37, W92), quarantine write-offs (W219), SLOB provisioning (W220) | Split by design |
| **Store Lifecycle** | W16 new-store org runbook (INV org, MOAC, price list, POS mapping); W45/W59 closure/relocation via org close + FA transfers; store P&L by org; permits (W54) tracked via EITs on location records | Standard |
| **Facility Maintenance** | Work orders are **not** run in EBS (no native EAM in this footprint — Oracle EAM/WIP not licensed for facilities); maintenance is edge/process with FA linkage (asset IDs via DFF); costs post through AP/FA | Process-owned, EBS-accounted |
| **IT Operations** | ITSM stays with its tooling (VS-27); EBS-side touchpoints: FND user & responsibility lifecycle (W152), environment & masking management (W384), archiving (W396) | Process-owned |
| **Business Continuity** | DR via Data Guard + the environment strategy (architecture §4); BCP process itself is VS-26 documentation, not EBS function | Platform-provided |
| **Product Information** | PIM/DAM stays edge (VS-137); EBS item master holds the commercial spine (codes, categories, UOM, tax, barcodes/GTIN via item cross-references W311) | EDGE-rich, EBS-core |
| **Training & Development** | Oracle Learning Management for calendar/enrollment/compliance basics; deep LMS stays edge | Standard-light |
| **Fleet Management** | No EBS fleet product in footprint; vehicles as FA assets + fuel/maintenance via AP and edge telematics (VS-06) | EDGE-executed, EBS-accounted |
| **Data Privacy & Compliance** | Consent/DSAR workflows are edge/process (VS-91); EBS carries audit-trail options, data-masking in clones (W384), and retention via archiving | Supporting |
| **Regulatory Operations** | Permits/licences tracked via EITs/attachments on the governed records (VS-166); no EBS regulatory module exists — registers stay process-owned | Process-owned |
| **Customer Order Management** | **Order Management**: backorders (W56) via ATP + scheduling, order holds, customer notifications via workflow events | Standard |
| **Corporate Account Management** | OM sales agreements + project record structures (Projects for W58 project budgets), staged call-off orders (W164) via blanket releases against agreements, retention billing (W165) via project billing | Standard |
| **Vendor Contract Management** | PO blanket/contract agreements + contract terms as PO terms/DFFs; 3PL contracts as supplier agreements (W62B) | Standard |
| **Customer Experience** | CSAT/NPS/complaints stay edge (VS-13); EBS touchpoints limited to TCA data quality | EDGE |
| **Marketing / Campaign** | Edge (VS-14); EBS touchpoint: Trade Management *evaluation* for vendor-funded promo claims (fit-gap §4), otherwise AP for spend | EDGE |
| **Real Estate** | **Property Manager**: lease abstraction, rent/CAM/indexation billing (W117/W118), critical-date workflows; real-property tax via AP + PN schedules (W119) | Standard |
| **Internal Audit** | EBS-native evidence: FND audit, ERES, AME logs, role-assignment queries for W338 SoD review; audit management itself is process (VS-21) | Evidence-provider |
| **Governance / Strategy** | Process-owned; EBS touchpoints limited to budgets (GL) and board-approval evidence via workflow | Process-owned |
| **Engineering & Construction** | **Projects** carries construction cost capture/CIP for W223–W227; scheduling stays PMO tooling | Standard-light |
| **HSE / Safety** | Process-owned (VS-24); EBS touchpoint: incident-driven AP/FA entries | Process-owned |
| **Services / Rental** | Service work orders (W544) via OM service lines + Projects where project-ized; tool rental deposits via AR deposits/commitments (W139) | Standard-light |
| **Wholesale / B2B** | OM + QP corporate price books (W163), punch-out via XML Gateway/cXML (W283), EWT on wholesale (W145) | Standard |

---

## 2. Family Coverage Summary

Roll-up by the workflow catalog's 8 value-stream families
([workflows/README.md](../01-model-company/workflows/README.md)):

| Family | EBS posture | Headline |
|---|---|---|
| **Plan & Buy** (462 WF) | Core EBS | Merchandise planning analytics split (edge/DP), sourcing/PO/landing fully EBS |
| **Make & Improve** (500 WF) | Split | Inventory ledger/kits/quality EBS; process-mining & CI tooling edge |
| **Sell & Serve** (1,546 WF) | EBS-mastered, edge-executed | POS/ecommerce/loyalty edges execute; EBS owns item/price/tax/credit/order masters and the AR ledger |
| **Move & Store** (785 WF) | EBS-ledgered, edge-executed | WMS/TMS/WFM edges execute; EBS owns inventory ledger, freight cost accounting, landed cost |
| **Count & Comply** (445 WF) | Process + EBS evidence | Statutory filings generated from EBS/PAY via the BIR pack; registers process-owned |
| **People & Culture** (323 WF) | Core EBS + LOC pack | Core HR/payroll EBS; WFM scheduling edge; LMS light-EBS |
| **Finance & Growth** (976 WF) | Core EBS | GL/AP/AR/CE/XTR/FA/PA — the strongest standard fit in the suite |
| **Technology & Data** (390 WF) | Process + platform | EBS is itself the governed platform (W384/W396); DP/IAP in-house per register |

---

## 3. What EBS Is Deliberately *Not* Used For

Restating the boundary keeps later scope-creep honest. The suite is not adopted for:

1. **Storefront/checkout execution** — POS and ecommerce edges (VS-08/10) execute under EBS
   masters. No iStore, no Forms-based selling.
2. **Warehouse/transport/labor execution** — BoB WMS/TMS/WFM per the sourcing register §4
   (subject to the register's own Oracle-WMS parity trigger, fit-gap §4).
3. **Omnichannel order orchestration & trade-project coordination** — in-house OMO/TPS per
   the register; EBS OM carries the fulfillment legs OMO routes to.
4. **Deep PIM/DAM, planogram/space, CDP** — edge products (VS-55/137/126).
5. **Enterprise BI** — in-house DP (OM §5); EBS provides FSG/BI Publisher/ECC for
   operational and statutory reporting only.

---

*Document Version: 1.0 | Date: 2026-09-14 | Initial issue — generic-module → EBS realization register mirroring the touchpoint-map section headings; family roll-up; deliberate non-adoption boundary. Canon anchors: touchpoint-map module set; sourcing register §4; family totals 462/500/1,546/785/445/323/976/390 = 5,427.*
