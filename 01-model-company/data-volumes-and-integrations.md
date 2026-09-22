# Model Company — Data Volumes & Integration Map

> Supplementary reference for ERP planning. Contains detailed volume calculations,
> integration touchpoints, and data flow architecture. Cross-references:
> - Company profile & POS details: [model-company-profile.md](model-company-profile.md)
> - Full requirements list: [erp-requirements.md](erp-requirements.md)

---

## 1. Transaction Volume Summary

### 1.1 Daily Volumes (assuming 30 operating days/month)

| Transaction Type | Daily Volume | Peak Factor | Peak Daily |
|---|---|---|---|
| POS Transactions | 93,333 | 2.0x (weekends/sales) | 186,666 |
| POS Line Items | 373,333 | 2.0x | 746,666 |
| Store Replenishment Orders | 1,700 | 1.5x | 2,550 |
| Goods Receipts (DC) | 200 | 1.5x | 300 |
| DSD Goods Receipts (Store) | ~20 | 1.5x | ~30 |
| Purchase Orders Created | 55–65 | 2.0x (batch days) | 110–130 |
| AP Invoices Processed | ~300 | 2.0x (month-end) | ~600 |
| Customer Returns (AR Credit Memos) | ~40 | 1.5x | ~60 |
| Inventory Adjustment Documents | ~30 | 8.0x (physical-inventory events) | 240 |
| Ecommerce Orders | ~1,430 | 3.0x (sale events) | ~4,290 |
| Customer Registrations | ~150 | 3.0x (sale events) | ~450 |

> **Note:** Each physical delivery to a store consolidates the replenishment transfer orders generated since the previous drop (~20–30 per delivery at the production-measured ~3 lines/order), reconciling to 2–3 deliveries/store/week from ~250 replenishment orders/store/month. The production calibration raises the order-document count ~10x; the physical-delivery cadence (and truck count) is unchanged — trucks consolidate more, smaller orders.
>
> **Production calibration basis (2026-09-23):** the operating rows above are re-derived against the actual operator's production EBS read-outs (CitiHardware PROD — 171 active stores, ~9.75 years of live history; the model company mirrors this estate at 200 stores): inter-branch transfer orders **480,541 (2024) / 529,399 (2025) docs at ~3 lines/order** (~250–265/store/month) ground the replenishment row; purchase orders **20,275 (2024) / 18,782 (2025) at 6.9–7.4 lines/PO** ground the PO row; AR credit memos **14,744 (2024) / 13,584 (2025) at ~1.05 lines/doc** (OM RMA orders a thin ~1,660-lifetime slice) ground the returns row; adjustment documents **3,508–11,652/year** with single physical-inventory months posting 60–90K lines ground the adjustment row's 8.0x peak; POS receipts measured at **126–510/store/day** (6-store × 2-day probe; sample mean ~330 receipts/store/day, ~3.1 lines/receipt, ~⅓ of POS lines non-inventory items that correctly do not post to inventory) — the 93,333/day × 4-line planning canon is retained as the 200-store design target at the top of the measured band. Sources: po_monthly / stock_transfer / customer_returns / stock_adjustment / return_to_supplier / top_tables_by_record_count / pos_to_ebs_timestamps / active_items_with_inventory reports (2026-06 read-outs).
>
> **AP volume note:** the daily figure is total AP — ~6,715 merchandise invoices (3-way match per W7) + ~2,000–3,000 non-PO/recurring invoices (2-way match per W7C) = ~8,500–9,500/month per `model-company-profile.md` §10.2; ~300/day is the midpoint (÷30 operating days), with month-end close pushing peak to ~600/day.

### 1.2 Data Storage Estimates (Annual Growth)

| Data Type | Annual Records | Est. Size |
|---|---|---|
| POS Transaction Headers | 33,600,000 | ~17 GB |
| POS Transaction Lines | 134,400,000 | ~67 GB |
| Inventory Movements | ~55,000,000 | ~28 GB |
| Accounting Lines (Subledger XLA + GL) | ~30,000,000 | ~4 GB |
| Purchase Orders + Lines | ~175,000 | ~0.6 GB |
| AP/AR Documents & Lines | ~1,440,000 | ~4 GB |
| Ecommerce Orders + Lines | ~515,000 | ~1.5 GB |
| Master Data (all types) | ~2,500,000 | ~1 GB |
| **Total Annual Increment** | | **~123 GB** |
| **10-Year Retention** | | **~1,230 GB** (uncompressed); ~865 GB with compression |

---

## 2. Integration Architecture Map

> **This is the canonical integration architecture diagram.** The diagram also appears in [technical-guidelines.md](../07-methodology/technical-guidelines.md) for convenience; any updates should be made here first.

```
┌─────────────────────────────────────────────────────────────────────┐
│                        BUILDRIGHT DEPOT CORP                        │
│                      INTEGRATION ARCHITECTURE                       │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐   │
│  │ 600 POS  │  │ 4 WMS    │  │ Ecommerce │  │ Loyalty Engine   │   │
│  │Terminals │  │Systems   │  │ Platform │  │ (CRM)            │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────────┬─────────┘   │
│       │              │              │                  │             │
│       └──────────────┴──────┬───────┴──────────────────┘             │
│                             │                                        │
│                    ┌────────▼────────┐                               │
│                    │   ERP SYSTEM    │                               │
│                    │   (Core Hub)    │                               │
│                    └────────┬────────┘                               │
│                             │                                        │
│       ┌─────────────┬──────┴──────┬──────────────┐                  │
│       │             │             │              │                   │
│  ┌────▼─────┐ ┌────▼─────┐ ┌────▼─────┐  ┌────▼──────┐            │
│  │   Banks   │ │ BIR/eFPS │ │ SSS/PH/  │  │ Delivery  │            │
│  │(BDO, BPI, │ │ (Tax     │ │ Pag-IBIG │  │ Partners  │            │
│  │MB, CB)    │ │ filing)  │ │ (Stat.)  │  │(Lalamove, │            │
│  └──────────┘ └──────────┘ └──────────┘  │ Transp.)  │            │
│                                           └───────────┘            │
│       ┌─────────────┐         ┌─────────────────┐                  │
│       │  Payment     │         │   Supplier       │                 │
│       │  Gateways    │         │   Portal         │                 │
│       │(PayMongo,   │         │                   │                 │
│       │ Dragonpay)  │         └─────────────────┘                  │
│       └─────────────┘                                               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. Integration Detail Matrix

| Source | Target | Data | Direction | Frequency |
|---|---|---|---|---|
| POS | ERP | Sales transactions | POS → ERP | Near real-time (continuous event streaming, < 30 sec latency); nightly reconciliation batch validates completeness |
| ERP | POS | Price file, item master, promos | ERP → POS | Continuous push (updates within 60 sec of activation); nightly full refresh |
| ERP | POS | Customer lookup | ERP → POS | Real-time; local cache for offline (loyalty members + trade accounts) |
| Ecommerce | ERP | Orders, customer registrations | ECOM → ERP | Real-time |
| ERP | Ecommerce | Inventory levels, prices, catalog | ERP → ECOM | Near real-time (5 min) |
| ERP | Ecommerce | Order fulfillment status | ERP → ECOM | Real-time |
| ERP | WMS | Transfer orders, PO receipts | ERP → WMS | Real-time |
| WMS | ERP | Pick confirmation, ship confirm, inventory | WMS → ERP | Real-time |
| ERP | Loyalty/CRM | Points earning triggers | ERP → CRM | Real-time |
| CRM/POS | ERP | Points redemption | CRM → ERP | Real-time |
| ERP | Banks | Payment files (AP) | ERP → Bank | Batch (daily) |
| Banks | ERP | Bank statements | Bank → ERP | Batch (daily) |
| ERP | BIR eFPS | Tax returns | ERP → BIR | Monthly/Quarterly |
| ERP | SSS/PhilHealth/Pag-IBIG | Contribution files | ERP → Statutory | Monthly |
| ERP | Delivery Partners | Delivery orders | ERP → 3PL | Real-time |
| Delivery Partners | ERP | Delivery status | 3PL → ERP | Real-time |
| Payment GW | ERP | Payment confirmation | GW → ERP | Real-time |
| ERP | Supplier Portal | POs, schedules | ERP → Portal | Real-time |
| Supplier Portal | ERP | ASN, invoices | Portal → ERP | As submitted |
| Payroll PH (in-house build) | ERP | Period costing journals, statutory accruals | Payroll → ERP | Monthly |

---

## 4. Critical Timings & SLAs

| Integration | Max Latency | Impact if Exceeded |
|---|---|---|
| POS → ERP (sales) | 30 seconds | Inventory inaccuracy, stockouts, overselling on other channels |
| ERP → POS (prices) | 60 seconds | Wrong pricing at checkout, DTI price freeze non-compliance |
| ERP → ECOM (inventory) | 5 minutes | Overselling online |
| ECOM → ERP (orders) | 1 minute | Delayed order processing |
| WMS ↔ ERP (inventory) | 1 minute | DC inventory inaccuracy |
| Payment confirmation | 30 seconds | Failed order completion |

---

## 5. Batch Processing Windows

| Process | Schedule | Estimated Duration | Window |
|---|---|---|---|
| POS transaction sync (continuous event streaming) | Continuous (near real-time, < 30 sec per event) | < 1 second per event | Ongoing |
| POS nightly reconciliation batch | Daily at 01:00 (after all stores closed) | 1–3 hours | 01:00–04:00 |
| Nightly inventory snapshot | Daily at 01:00 | 15–30 minutes | 01:00–03:00 |
| Nightly price/promo full refresh to POS | Daily at 02:00 (continuous push runs throughout day; nightly is full reconciliation) | 10–20 minutes | 02:00–04:00 |
| Day-end close per store | Daily at 23:30 local | 5–10 minutes per store | 23:30–00:30 |
| Week-on-week sales report generation | Weekly (Monday 06:00) | 10–20 minutes | 06:00–07:00 |
| Month-end close | Last day of month + 5 working days | 2–4 hours for heavy jobs | 22:00–03:00 (off-peak) |
| Payroll processing (5 entities) | Semi-monthly (15th & 30th) | 1–2 hours per entity | 20:00–23:00 |
| VAT / tax report generation | Monthly (by 10th) | 30–60 minutes | Evening batch |
| BIR eFPS tax filing file export | Monthly / Quarterly | < 30 minutes | On-demand |
| Full inventory reindex / valuation | Monthly (1st) | 30–60 minutes | 01:00–03:00 |
| Demand planning / forecast recalculation | Weekly (Sunday) | 1–3 hours | 00:00–04:00 |
| Database backup | Daily at 03:00 | 1–2 hours | 03:00–05:00 |

### Peak Load Calendar

| Period | Activity | Additional Load |
|---|---|---|
| Month-end (last 3 days) | Close, accruals, reconciliation | +30% AP/AR processing, heavy reporting |
| Bi-monthly sale events | Promotional pricing, traffic surge | +100% POS volume, +200% ecommerce |
| Payroll dates (15th & 30th) | Payroll runs, bank file generation | Heavy HR/payroll module usage |
| Q1 inventory count (Jan) | Annual wall-to-wall physical count | Heavy inventory module, RF gun usage |
| Christmas season (Nov–Dec) | Peak retail period | Sustained +50% volume across all channels |

---

*Document Version: 4.7 | Date: 2026-09-23 | Production-volume calibration (by direction: check the operator's production data for realistic transaction volumes and adjust accordingly): the §1.1 operating-transaction rows re-derived against the CitiHardware PROD read-outs (the production estate this model company mirrors at 171 active stores) — the Store-Replenishment-Orders row 167/day (~5,000/month) → **1,700/day (~50,000/month; ~250/store)** on the measured STROO inter-branch run-rate (480,541 docs 2024 / 529,399 docs 2025 at ~3 lines/order — a 10x underestimate in the plan), the Purchase-Orders row 40–50/day → **55–65/day** (peak 80–100 → 110–130) on the measured 18.8K–20.3K POs/year at 6.9–7.4 lines/PO, and two production-evidenced rows added (Customer Returns — AR credit memos, ~40/day at ~1.05 lines/doc; Inventory Adjustment Documents, ~30/day with an 8.0x physical-inventory peak); the POS planning canon (93,333/day × 4 lines) deliberately retained and annotated with the production measurement (126–510 receipts/store/day, sample mean ~330, ~3.1 lines/receipt, ~⅓ of POS lines non-inventory) — the design target sits at the top of the measured band; §1.2 storage rows calibrated to measured row counts and bytes/row (Inventory Movements ~3M → ~55M records — the POS canon alone implies ~50M inventory-issue rows at the measured ~37% posting fraction, plus both legs of ~50K transfer orders; Journal Entries + Lines relabelled **Accounting Lines (Subledger XLA + GL)** ~1.5M → ~30M on the measured ~19–27M XLA/GL lines/year; POs + Lines ~233K → ~175K at the 7-line order profile; Master Data ~700K → ~2.5M on the item-org assignment cadence of ~8K new items/year × ~286 sites) — annual increment ~100 GB → **~123 GB**, 10-year retention **~1,230 GB uncompressed (~865 GB compressed)**; cascade: profile §7.2/§15.1/§3.3/§9 (footer v3.2), NFR-031, A6.5 (assumptions v3), ai-first guide §7 D1 reference (v1.14), PA-02.1/PA-02.3/PA-04.2/PA-04.3/PA-06.1/PA-110.2, VS-02 README; the §2 diagram and §3 Integration Detail Matrix untouched (the calibration is volumes, not flows). Prior v4.6 (2026-09-14): Twenty-first-wave consistency review — the §3 Integration Detail Matrix (the canonical flow register the EBS pattern register's Flow column quotes) extended with the two-tier doctrine's payroll posting flow (row 20: Payroll PH (in-house build) → ERP, period costing journals & statutory accruals, monthly — the fit-gap E8 INT canon asserted by 02-oracle-ebs integrations §2, data-migration row 11 and the sourcing register; the doctrine commits created the flow but never reached this matrix), and the statutory target row named in full (SSS/PhilHealth/Pag-IBIG). The §2 diagram box set deliberately unchanged — it predates the OMO/TPS/AAP estates equally, so extending it for payroll alone would be arbitrary; the §3 matrix is the flow canon. Prior v4.5 (2026-09-07): the §1.1 Customer-Registrations peak factor stated ('—' → 3.0x sale-event basis — the row already carried a ~450 peak and registrations spike with the same sale-event driver as the ecommerce row above it); no volume figures changed, and the §1.1/§1.2 arithmetic on this page is now re-derived on every `validate-repo.sh` run by the audit-model-docs guard (the document joined that guard's doc set in the 2026-09-07 eighth-wave consistency review, having shipped with zero validator coverage). Prior v4.4 (2026-06-19): BIR record retention corrected from 7 years to **10 years** (TRAIN/NIRC — Sec. 235, as amended by RA 10963): the retention storage row is relabelled **10-Year Retention** and recomputed to **~1,000 GB uncompressed (~700 GB compressed)** at ~100 GB/year × 10 (was 7-Year/~700 GB/~500 GB); aligns with NFR-006, A6.5, profile §15.3, technical-guidelines §2.3. Prior v4.3: AP daily-volume figure reconciled to total AP (merchandise + non-PO) per model-company-profile.md §10.2 (~8,500–9,500/month; was merchandise-only 217/day); annual AP/AR storage row relabelled "Documents & Lines" so the ~1.44M record count (≈9–10 lines/doc over ~150K invoice docs) is self-consistent with the corrected daily figure — record count and ~4 GB size unchanged. Prior: integration architecture diagram designated as canonical source; canonical payroll cycle reconciled to semi-monthly 15th & 30th (per model-company-profile.md §11.2); bank list reconciled to 4 banks (BDO, BPI, Metrobank, Chinabank); counts reconciled with README.md.*
