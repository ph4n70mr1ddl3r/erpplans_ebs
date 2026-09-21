# EBS Documentation Coverage Register — the Suite's Own Library vs This Model

> **The inward direction.** The [fit-gap register](fit-gap-analysis.md) was built *outward*:
> it starts from the model company's 5,430 workflows and asks, per capability, "does EBS have
> this?" That direction can only find what the workflows already thought to ask for. This
> register runs the **opposite** direction — it starts from Oracle's own R12.2 documentation
> library and asks, per documented product, "**does the model company need this, and if so,
> which workflow says so?**" A product EBS documents, that this business needs, and that no
> workflow names, is a coverage defect by the two-tier doctrine (*if it's in EBS we use it*)
> — the suite is not maximized if the model never learned the capability exists.
>
> Source of record: [`../ebs_docs/current/`](../ebs_docs/) — the R12.2 documentation library
> (376 PDFs / 133,782 pages), indexed by `R122_doc.txt`. Dispositions land in the
> [fit-gap register](fit-gap-analysis.md); owning workflows land in the
> [workflow catalog](../01-model-company/workflows/value-stream-index.md).

Part of the [02-oracle-ebs blueprint](README.md).

---

## 1. The library

| Class | Guides | Pages | In scope for this register |
|---|---:|---:|---|
| **Business capability** | **216** | **77,098** | **Yes — the register below** |
| Technical / platform (developer, API, eTRM, flexfields, install, upgrade, Cloud Manager, AMP, mobile-apps admin, personalization, security/setup/maintenance) | 45 | 13,258 | No — governed by [customization-governance.md](customization-governance.md), [integrations.md](integrations.md) and [ebs-platform-architecture.md](ebs-platform-architecture.md) |
| Other-country localizations & supplements (US, UK, Canada, India, Mexico, Australia, NZ, Japan, Ireland, Netherlands, Saudi Arabia, China Golden Tax, EU Intrastat, US Vertex/Taxware) | 38 | 21,580 | No — the model company is Philippine-only, 5 PH legal entities |
| CRM sales & contact-centre stack (TeleSales, Sales, Quoting, Proposals, Territory Manager, Scripting, Interaction Blending, Email Center, Universal Work Queue, telephony) | 29 | 5,778 | Partially — see §4 EDC-16 |
| Discrete/process manufacturing depth (OPM, Shop Floor, Flow, Project Manufacturing, Outsourced Manufacturing, Complex MRO, e-Records, Manufacturing Operations Center) | 19 | 5,870 | No — the model company retails and lightly fabricates; the adopted depth is BOM/WIP + Engineering + Quality (fit-gap C9/C12/C17) |
| Public sector (Contract Lifecycle Management, US Federal HR, Grants Accounting, G-Invoicing, Labor Distribution) | 18 | 8,424 | No — private commercial retailer |
| Functional Testing Suite advanced packs | 11 | 1,774 | No — test automation, not business capability |
| **Total** | **376** | **133,782** | |

The 216 business guides collapse to **164 distinct products** (a product may ship an
implementation guide, a user guide and a reference guide).

## 2. Method

1. Extract every guide's title and page count from the PDF library (`pdftotext` over page 1;
   `pdfinfo` for pages). The shipped `R122_doc.txt` index names only 105 of the 376 files, so
   the filename→title map is derived from the PDFs themselves, not from the index.
2. Classify each guide into the seven classes of §1; collapse the business class to products.
3. For each business product, search the blueprint (`02-oracle-ebs/*.md`) and the model
   (`01-model-company/**/*.md`) for the product and its house aliases.
4. Three outcomes: **ADOPTED/ADJUDICATED** (the blueprint already names it — the fit-gap row
   carries the disposition), **WORKFLOW-ONLY** (the business capability is in the workflow
   catalog but the blueprint never asked whether EBS ships it), **UNEXAMINED** (neither).
5. Every WORKFLOW-ONLY and UNEXAMINED product is adjudicated here: needed → **EDC gap row**
   with a required action; not needed → recorded with its reason, so the answer is on the
   record and the next sweep does not re-ask.

**Result: 107 of 164 products already adjudicated; 57 were not.** Of the 57, 32 are
recorded not-needed in §5, and **25 are open gap rows in §4**.

## 3. What the library confirms

The documentation settles three questions the blueprint had answered from reasoning alone:

| Confirmation | Evidence |
|---|---|
| **The PH localization build is correct — EBS ships no Philippine localization.** `Oracle Financials for Asia/Pacific` (240p) covers Australia, China, Japan, Korea, Singapore and Taiwan only; the word "Philippines" does not appear in it. The LOC pack (fit-gap §6) is therefore not a shortfall of the audit but a documented absence in the product. | `122jaug.pdf` §Contents (ch. 1–7); zero "Philipp*" matches in 240 pages |
| **No EBS POS product exists in the library.** Confirms the in-house POS decision and the module-coverage map's POS row. | No POS/retail-store product among 376 guides |
| **The VCP stack really is a separate family.** ASCP, Demantra (8 guides), Inventory Optimization, Rapid Planning, Strategic Network Optimization, Production Scheduling, Collaborative Planning, Advanced Planning Command Center and Service Parts Planning all ship their own guides — consistent with licensing-BOM decision 3 (off the public GPL, custom quote). | 13 VCP-family guides / 5,285 pages |

## 4. Gap register — EBS documents it, the model company needs it

Every row here requires (a) a fit-gap disposition row and (b) either an owning workflow that
names the EBS product, or a recorded reason why the capability is met otherwise. Rows are
ordered by strength of evidence that the model company needs the capability.

| ID | EBS product (guides / pages) | The model company's need — evidence from this repo | Current state | Required action |
|---|---|---|---|---|
| **EDC-01** | **Price Protection** (`122dppig`, `122dppug` / 108p) | **Proven.** W161 *Vendor Price Protection & Market Markdown Claims* (VS-03.1) and W928 *Customer Price Protection & Price Adjustment* (VS-13.1); requirements PUR-020, CRM-044 | W161's System Touchpoints name a generic "automated claim calculation module" and "vendor portal claim submission". EBS ships the product: price-protection dashboard, transactions, adjustments & approvals, covered-inventory adjustment by item/warehouse, **inventory claims and customer claims**, transaction history, import & notification programs | Fit-gap row; re-point W161/W928 System Touchpoints to the product; a workflow must own the dashboard/approval run |
| **EDC-02** | **Environmental Accounting and Reporting** (`122ghgug` / 164p) | **Proven.** W1334 carbon footprint & Scope 3, W3466 GHG Scope 2 attribution, W5481 fleet Scope 1 MRV, W1396 store energy benchmarking, W1262 product carbon footprint; VS-25 ESG family | Built/generic ESG tooling. EBS ships GHG accounting & reporting with organization hierarchy, UOM classes & conversions, emissions formulas per operating unit, reporting flexfields and combinations — the two-tier doctrine says use it | Fit-gap row; re-point the GHG/ESG workflow touchpoints; a workflow must own emissions-factor/UOM setup and the environmental-data load |
| **EDC-03** | **Incentive Compensation** (`122cnig`, `122cnug`, `122cnauig` / 592p) | **Proven.** W3322 *Sales Commission & Trade-Incentive* (VS-102.3), W4570 referral commission (VS-154.3); 31 workflows carry commission mechanics | Never named in the blueprint. EBS ships the full compensation-plan, quota, crediting and payment engine | Fit-gap row; re-point W3322/W4570; a workflow must own plan/quota maintenance and the compensation run |
| **EDC-04** | **Financials Accounting Hub** (`122fsahig` / 438p) | **Strong.** Licensing-BOM decision 1 routes **134.4M POS line-items/year** to AR via AutoInvoice + the inventory interface rather than through OM; loyalty liability, the in-house ecommerce and POS platforms all need accounting representations in GL | Never named. FAH is EBS's documented engine for generating SLA accounting from **external** transaction systems — precisely this architecture | Adjudicate against the current AutoInvoice design; fit-gap row either way, since this is the single largest accounting-integration decision in the model |
| **EDC-05** | **Bill Presentment Architecture** (`122bpaug` / 88p) | **Strong.** ~5,200 trade + ~200 corporate accounts; W5403 invoice reissuance/re-assignment; iReceivables is already adopted (fit-gap A14) | Never named. BPA is the presentment layer **iReceivables renders through** — templates, data sources, grouping, attachments, hyperlinks | Fit-gap row under A14; a workflow must own bill-template/data-source governance |
| **EDC-06** | **Demand Signal Repository** (`122dsrug` / 272p) | **Strong.** 200 stores × POS sell-through; W31 demand forecasting, W312 forecast-parameter calculation, W2A replenishment, VS-127 S&OP | Never named. DSR is the EBS-family retail demand-signal repository: store clusters, item clusters, retail calendars, measures, goals & thresholds, allocation/aggregation | Adjudicate against the adopted Demantra stack; fit-gap row; if adopted, a workflow must own signal load and cluster maintenance |
| **EDC-07** | **Customer Data Librarian** (`122dlig`, `122dlug` / 150p) + **Customers Online** (`122imcig`, `122imcug` / 174p) | **Strong.** W253 TCA DQM dedup; the licensing BOM's "TCA DQM (entitlement verify)" line; TCA is the customer master of record | DQM named, the two data-steward products never adjudicated | Fit-gap row under the TCA/MDM family; a workflow must own the steward queue (merge/dedup review) |
| **EDC-08** | **E-Business Tax Reporting** (`122zxrg` / 128p) | **Strong.** The BIR pack is the heaviest statutory surface in the corpus (CAS, EIS, 2307, 1601-EQ, alphalists, VAT registers) | eBTax adopted; the **Tax Reporting** guide — tax registers, the reporting ledger, register extracts — never named | Fit-gap row under the LOC pack; the BIR-report workflows must name the tax reporting ledger as their extract source |
| **EDC-09** | **Asset Tracking** (`122cseig`, `122cseug` / 200p) + **iAssets** (`122iaug` / 44p) | **Strong.** 600 POS terminals, store/DC equipment, eAM adopted (F5), FA adopted (A6); W34/W5101 device estates | Never named. Asset Tracking links Install Base deployments to FA; iAssets is self-service asset request/transfer | Fit-gap row; a workflow must own deployed-asset tracking and the self-service transfer path |
| **EDC-10** | **Consigned Inventory from Supplier** (`122cipg` / 78p) + **Supplier Ship and Debit** (`122ssdig`, `122ssdug` / 80p) | **Strong.** W177 concessionaire model, W5505–W5507 concession catalog, W5574 concession connectivity; W245 vendor chargebacks | Concession is modelled as a commercial arrangement only; the EBS consigned-inventory and ship-and-debit mechanics were never adjudicated | Fit-gap rows; the concession/consignment workflows must state which inventory-ownership model they run on |
| **EDC-11** | **Knowledge Management** (`122cskig`, `122cskug` / 348p) | **Confirmed.** VS-30.3 document & knowledge management, PA-30.3; TeleService (D14) is adopted and renders KM solutions to agents | Never named | Fit-gap row; the service/knowledge workflows must name their repository of record |
| **EDC-12** | **Report Manager** (`122frmug` / 88p) | **Confirmed.** The W9 FSG family and the statutory report estate | Never named. Report Manager publishes and distributes FSG/Web ADI output | Fit-gap row under the reporting stack |
| **EDC-13** | **e-Commerce Gateway** (`122eccig`, `122eccim`, `122eccug` / 1,518p across 3 files — `122eccig`/`122eccim` are two 680p editions of the Implementation Guide) | **To decide.** 800–1,000 vendors; 22 PA files describe ASN/PO/invoice exchange, several literally as "EDI" | The blueprint names **XML Gateway (ECX)** only. e-Commerce Gateway (ECE) is the separate classic X12/EDIFACT engine — trading partners, transaction enablement, code conversion | Adjudicate ECE vs ECX explicitly and record it; today the corpus says "EDI" while the blueprint provides only cXML/XML |
| **EDC-14** | **Sales Contracts** (`122okoig` / 248p) | **To decide.** VS-11 trade/project contracts; Procurement Contracts already adopted for the buy side | Sell-side contract terms never adjudicated | Fit-gap row |
| **EDC-15** | **Project Portfolio Analysis** (86p), **Project Resource Management** (60p), **Project Contracts** (316p) | **To decide.** Projects (Costing/Billing/Management) adopted; VS-112 PMO, VS-20/40 capex | The three sibling products never adjudicated | Fit-gap rows or a recorded not-needed |
| **EDC-16** | **iSupport** (`122ibuig` / 370p) + **Customer Interaction History** (264p) + **Common Application Calendar** (678p) | **To decide.** In-house customer portal already built; TeleService adopted needs interaction history | Never adjudicated | Fit-gap rows: iSupport against the already-built portal; CIH/Calendar as TeleService foundations |
| **EDC-17** | **Electronic Kanban** (`122ekflmug` / 154p) | **To decide.** Store/DC replenishment (W2A min-max/ROP) | Never adjudicated | Fit-gap row or recorded not-needed against min-max |
| **EDC-18** | **Procurement Command Center Plus** (164p) + **Project Procurement Command Center Plus** (202p) | **To decide.** ECC is adopted; these are the procurement ECC dashboards | Never adjudicated | Fit-gap rows under the ECC family |
| **EDC-19** | **Advanced Planning Command Center** (500p), **Collaborative Planning** (478p), **Strategic Network Optimization** (546p), **Value Chain Planning Collections** (278p), **AIA VCP Integration Base Pack** (392p), **Service Parts Planning** (464p), **In-Memory Performance-Driven Planning** (24p) | **To decide as a family.** ASCP, Demantra, Inventory Optimization and Rapid Planning are adopted (C5) and sit on the custom-quote register | The seven sibling VCP products were never named | One fit-gap family row recording which VCP components are in and which are out, so the custom-quote scope is exact |
| **EDC-20** | **Loans** (`122lnsug` / 132p) | **To decide.** VS-38 consumer credit & financing, W966/W1088 construction/housing loan referral, VS-154 loan servicing referral | Never named; the referral model may make it unnecessary | Fit-gap row or recorded not-needed |
| **EDC-21** | **HRMSi Strategic Reporting** (3 guides / 474p) | **To decide.** HR analytics currently ride the in-house DP platform | Never adjudicated | Fit-gap row under the HRMS family |
| **EDC-22** | **Release Management** (328p) | **To decide.** Customer demand/ship-schedule releases | Never adjudicated; likely automotive-shaped and not needed | Record the reason |
| **EDC-23** | **Order Management Using Oracle Workflow** (352p) | **To decide.** OM is adopted; this guide governs the order-flow workflow customization the CDR gate (W5575) would police | Never named | Cross-reference from customization-governance |
| **EDC-24** | **Financial Services** (342p) + **Financial Services Reporting** (138p) | **To decide.** Almost certainly the banking/insurance vertical, not this retailer | Never adjudicated | Record the reason |
| **EDC-25** | **Inventory Copy Inventory Organization** (`122cioig` / 40p) | **Confirmed, small.** W16 new-store org runbook creates an INV org per store, 10–15 new stores/year | Never named. This is the supported org-copy utility | Name it in W16's System Touchpoints |

## 5. Adjudicated not needed (recorded, so the next sweep does not re-ask)

| Product(s) | Reason |
|---|---|
| Telecommunications Service Ordering, Telecommunications Billing Integrator, Number Portability, Service Fulfillment Manager, Interaction Center Server Manager, Advanced/Outbound Telephony, One-to-One Fulfillment, Leads Management | Telecommunications and outbound-contact-centre verticals; the model company runs an in-house contact centre against TeleService (D14) |
| HRMS supplements for Ireland, Netherlands, Saudi Arabia; all US/UK/Canada/India/Mexico/Australia/NZ/Japan HRMS and Payroll guides | Philippine-only employer; Payroll PH is the in-house build (fit-gap E5–E8) |
| Receivables: Golden Tax Adaptor for Mainland China; Inventory Movement Statistics; E-Business Tax Vertex/Taxware | China VAT, EU Intrastat and US sales-tax engines — none applies to a PH-only operation |
| Manufacturing Operations Center, In-Memory Cost Management for Process Industries, Production Scheduling, Process Manufacturing family, Shop Floor Management, Flow Manufacturing, Project Manufacturing, Outsourced Manufacturing, Complex MRO, e-Records | The model company retails and lightly fabricates; the adopted depth is BOM/WIP (C9), Engineering (C17), Quality (C12) and In-Memory Cost for Discrete (C15) |
| Contract Lifecycle Management for Public Sector (5 guides), US Federal HR (4), Grants Accounting, G-Invoicing, Labor Distribution | Public-sector products; the model company is a private commercial retailer |
| Functional Testing Suite advanced packs (11) | Test automation tooling, not business capability; testing discipline lives in customization-governance §5 |
| iStore, iStore Quick | Deliberately not adopted — the ecommerce platform is already built (licensing BOM §2.2) |

## 6. Re-running this register

The register is re-derived, not maintained by hand:

1. Re-extract the library inventory when `ebs_docs/` changes (title + page count per PDF).
2. Re-run the three-way match (product ↔ blueprint ↔ model) with the house alias table.
3. Any product that moves into **UNEXAMINED** or **WORKFLOW-ONLY** is a new EDC row.
4. Any EDC row that gains a fit-gap disposition and an owning workflow closes.

Guarded by `07-methodology/audit-model-docs.py` (`ebs_doc_coverage_hits`) via
[`validate-repo.sh`](../07-methodology/validate-repo.sh) Check 59: the §1 inventory must foot
to the library on disk, the §4 EDC ids must be contiguous, and the §2 outcome arithmetic
(107 adjudicated + 32 recorded + 25 open = 164) must hold.

---

*Document Version: 1.0 | Date: 2026-09-21 | Initial issue — the inward-direction reconciliation of Oracle's own R12.2 documentation library (376 guides / 133,782 pages, `ebs_docs/current/`) against this model. 216 business guides collapse to 164 distinct products; 107 were already adjudicated by the fit-gap register, 32 are recorded not-needed here, and 25 open EDC gap rows carry required actions. Three existing decisions are confirmed by the library itself — most importantly that `Oracle Financials for Asia/Pacific` covers Australia, China, Japan, Korea, Singapore and Taiwan with **no Philippine content**, making the PH localization pack a documented product absence rather than an audit shortfall. Companions: [fit-gap-analysis.md](fit-gap-analysis.md) (dispositions), [module-coverage-map.md](module-coverage-map.md) (realization), [licensing-bom.md](licensing-bom.md) (cost of anything adopted here).*
