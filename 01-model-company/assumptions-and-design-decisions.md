# BuildRight Depot Corp. — Assumptions & Design Decisions

> This document consolidates the key assumptions and design decisions embedded across the
> model company documents. It serves as a single reference for understanding *why* certain
> parameters were chosen. Each assumption is cross-referenced to its source document.

---

## A1. Scale & Revenue Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A1.1 | All 200 stores are mature | Revenue figures assume all stores are past ramp-up | Simplifies modeling; real-world would have 10–15 stores in ramp-up at any time | Profile §9.4 |
| A1.2 | Average Transaction Value | PHP 1,800 | Benchmarked against Philippine big-box home improvement retail; calibrated to reflect a provincial store footprint | Profile §9.4 |
| A1.3 | Monthly POS transactions per store | 14,000 (~467/day) | Derived from 2.8M monthly ÷ 200 stores; consistent with high-traffic big-box retail | Profile §5 |
| A1.4 | Ecommerce penetration Year 1 | ~3% of revenue | Conservative for Philippine retail; aligns with early-stage omnichannel in the market | Profile §8.5 |
| A1.5 | Gross margin | 28–32% | Standard for regional big-box retail format in the Philippines | Profile §9.4 |
| A1.6 | EBITDA margin | 12–14% | Calibrated for higher logistics costs from a 4-DC provincial footprint | Profile §9.4 |

## A2. Organizational Assumptions
| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A2.1 | Single format (big-box only) | No Express/small format | Simplifies the model; tests one format thoroughly vs. two superficially | Profile §2 |
| A2.2 | Store staffing: 29 per store | Optimized model | Viable with a curated 35K SKU assortment and implementing recommended coverage for Stock Associates | Profile §12.1 |
| A2.3 | HQ in Davao City | Provincial HQ | Deliberately non-Manila to test provincial operations and connectivity | Profile §2 |
| A2.4 | 5 legal entities | Separate Holdings, Depot, Logistics, Digital Commerce, Property Mgmt | Tests multi-entity/intercompany capability; each entity has a distinct role | Profile §2 |
| A2.5 | Depot Inc. owns all inventory | Even though Logistics Inc. operates DCs | Simplifies inventory accounting; Logistics Inc. charges service fees, not goods transfer | Profile §2, W14 |
| A2.6 | Revenue per employee | ~PHP 8.99M/year | Driven by optimized staffing and high automation (re-derived at the 2026-09-18 gap-fill: ~PHP 62.3B ÷ 6,932); HQ rebalanced 315 → 357 (2026-06-20), then → 362 (2026-06-25), then promoted to the optimal structure HQ 511 (2026-09-14) and gap-filled to HQ 532 (2026-09-18) — see `optimal-table-of-organization.md` | Profile §4 |

## A3. Supply Chain & Logistics Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A3.1 | 4 DCs for 200 stores | DC-to-selling-area ratio ~8–12% | Industry norm for big-box retail; 4 DCs reduces average store-to-DC distance in archipelago | Profile §3.2 |
| A3.2 | DC4 (Clark) oversized at 25K sqm | Only 20 stores currently | Intentional: absorbs planned North/Central Luzon expansion | Profile §3.2 |
| A3.3 | 30% DSD by value | Cement, lumber, sand, gravel | Bulky items uneconomical to double-handle through DCs | Profile §7.1 |
| A3.4 | ~400–600 TEUs/month imports | ~40% of COGS from imports | Consistent with Philippine home improvement import volumes at this scale | Profile §7.1 |
| A3.5 | Inventory turns target: 6–8x | Curated 35K SKU assortment | Philippine island geography and import lead times make higher turns aspirational | Profile §12.3 |
| A3.6 | Shrinkage target: <1.5% | Aspirational for Philippine retail | Industry average ~1.5–2.5%; requires mature LP systems | Profile §12.3 |

## A4. Product & Merchandise Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A4.1 | 35,000 active SKUs | Curated assortment | Focused on faster turn; density of 2.3–4.4 SKUs/sqm | Profile §6.1 |
| A4.2 | Inventory valuation: WAC | Weighted Average Cost | Standard in Philippine retail; simpler than FIFO for big-box | Profile §6.3 |
| A4.3 | ~800–1,000 active vendors | 60% local, 40% import | Realistic mix for Philippine home improvement at this scale | Profile §6.5 |
| A4.4 | Top 20 vendors = 45% of COGS | Vendor concentration | Realistic for organized retail; drives blanket PO and rebate strategies | Profile §6.5 |

## A5. Financial Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A5.1 | PHP functional currency | PHP base; USD for imports | Philippine company; imports in USD | Profile §10.1 |
| A5.2 | VAT 12% | Standard Philippine VAT | Applied to most goods; some exempt/zero-rated customers exist | Profile §10.5 |
| A5.3 | Monthly IC settlement | All IC flows settled monthly on 5th | Simplifies cash management; may need twice-monthly for ecommerce as it grows | W14 |
| A5.4 | Loyalty deferred revenue ~1% | PFRS 15 allocation | Face value of points; actual allocation may differ based on expected redemption rate | W17 |
| A5.5 | Month-end close ≤ 5 days | Target | Achievable with automated IC elimination and bank reconciliation | Profile §15.3 |

## A6. IT & System Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A6.1 | POS offline ≥ 8 hours | Local cache of product/price | Philippine internet reliability; stores must sell during outages | NFR-011 |
| A6.1a | POS event-driven architecture | Near-real-time (< 30 sec) continuous event streaming | POS transactions stream continuously to ERP via message bus, not nightly batch; nightly reconciliation batch validates completeness only | POS-013, POS-034, POS-042 |
| A6.1b | POS local embedded data store | Full SKU catalog + customer cache on each terminal | Enables full offline selling with accurate pricing; continuous push from ERP with nightly full refresh | POS-043 |
| A6.1c | POS multi-origin fulfillment | Mixed-basket with items from store, DC, vendor, other stores | Single POS transaction can contain items fulfilled from multiple origins; unified financial posting | POS-044, POS-045 |
| A6.1d | POS terminal-to-terminal LAN sync | Peer sync when WAN down | Prevents overselling across terminals in same store during offline period | POS-046 |
| A6.2 | On-premises deployment — data residency under BuildRight control | Philippine facilities favored for latency; colocation permitted, no public-cloud hosting | Oracle EBS is an on-premises suite, not a cloud/SaaS ERP — running it in BuildRight-controlled facilities keeps RA 10173 data residency fully under the company's control | Technical Guidelines §2.1; `02-oracle-ebs/` §1 |
| A6.3 | Ecommerce platform | Already-built in-house platform | The custom ecommerce platform is an existing in-house asset (never rebuilt, never bought under the two-tier doctrine); integrated to the ERP core for real-time inventory and pricing sync | Profile §14.1 |
| A6.4 | Mobile app: branded native app | iOS + Android | Required for BOPIS pickup notifications, loyalty, and customer engagement; built on ERP-provided APIs or third-party | This document |
| A6.5 | 10-year data retention | BIR requirement (TRAIN/NIRC — Sec. 235, as amended by RA 10963) | Drives storage sizing (~1,000 GB uncompressed over 10 years) | Profile §15.3 |



---

## Design Decisions

| Decision | Choice Made | Alternative Considered | Why This Choice |
|---|---|---|---|
| DC network | 4 regional DCs | 3 mega-DCs | Better island coverage; lower outbound transport cost; industry-norm DC-to-selling-area ratio |
| IC model | Service-based (primary) | Goods-based between all entities | Depot Inc. owns all merchandise; simpler inventory accounting; Logistics Inc. charges service fees |
| SKU depth | 35,000 curated | 60,000+ deep | Faster turns; less floor coverage needed; viable with fewer store staff |
| Store format | Big-box only | Multi-format (Depot + Express) | Simpler model; single format tests one scenario thoroughly |
| Loyalty earn rate | 1 point per PHP 100 | Tiered earn by membership | Simpler to implement and communicate; standard in Philippine retail |
| BOPIS hold period | 5 days | 3 days or 7 days | 5 days balances customer convenience with inventory hold cost |
| POS terminals per store | 3 | 1–5 variable | 3 handles ~467 daily transactions across 10 operating hours with reasonable queues |
| POS sync architecture | Near-real-time event streaming | Nightly batch or periodic sync | Real-time inventory accuracy across 200 stores; prevents overselling; supports omnichannel ATP; Philippine internet reliability requires offline resilience rather than batch dependency |
| POS offline data model | Local embedded data store | Flat file cache | Full SKU catalog + customer cache enables comprehensive offline selling; not just emergency mode |
| POS fulfillment model | Multi-origin / mixed-basket | Store-only or store+DC only | Customer convenience: buy some items in-store, order others for delivery from DC or vendor from same transaction; competitive necessity for omnichannel retail |
| POS LAN architecture | Terminal-to-terminal sync | Independent terminals | 3 terminals per store can oversell each other during offline; LAN sync prevents this without requiring WAN |
| Payroll frequency | Semi-monthly (15th & 30th) | Monthly | Philippine standard; mandated by many CBAs and DOLE guidelines |
| Fiscal year | Calendar year (Jan–Dec) | April–March or other | Aligned with Philippine tax year (BIR) |
| Blanket PO coverage | ~45% of COGS | Higher or lower | Aligned with top-20 vendor concentration; remaining 55% on standard POs |

> **Note**: For definitions of all abbreviations and terms used in this document, see the canonical glossary in [model-company-profile.md §18](model-company-profile.md#18-glossary).

---

*Date: 2026-06-19 (v2 — A6.5 data-retention assumption updated to **10 years (BIR per TRAIN/NIRC — Sec. 235, as amended by RA 10963)** and storage-sizing recomputed to ~1,000 GB uncompressed over 10 years (was 7 years / ~700 GB); aligns with NFR-006, profile §15.3, data-volumes §1.2, technical-guidelines §2.3. v1: "unified cloud ERP" terminology standardized across all documents; counts reconciled with README.md and model-company-profile.md)*
