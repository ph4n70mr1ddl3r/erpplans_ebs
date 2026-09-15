# Data Migration into Oracle EBS

> Load paths, sequence, and validation for populating EBS from the legacy estate, building
> on the canonical field mappings in
> [`data-migration-mapping.md`](../01-model-company/data-migration-mapping.md) and the
> operational quality gates W385 (data cleansing & migration lifecycle) and W73 (migration
> validation & parallel-run testing). Rule zero: **data enters EBS only through supported
> interfaces and public APIs** — the same doctrine as
> [integrations.md](integrations.md) §1, applied to history.

Part of the [02-oracle-ebs blueprint](README.md).

---

## 1. Load-Path Register (Object → EBS Mechanism)

| # | Object | Volume anchor | EBS load path | Timing |
|---|---|---|---|---|
| 1 | Chart of accounts, value sets, calendars, currencies | 1 CoA · 5 ledgers | FND/GL setup (KeyFlex, calendar, rate types) | W0 — direct setup |
| 2 | Org structure (business group, legal entities, OUs, 205 inventory orgs) | 200 stores + 4 DCs + master | HR/INV/PO setups + MOAC security profiles | W0/W2 — per the add-org runbook (W16) |
| 3 | eBTax configuration (rates, VATEX classes, withholding/ATCs) | PH canon ATCs | eBTax setup | W0 |
| 4 | Items + categories + UOM + cross-references | ~55,000 item-master records (35,000 active) | Item open interface / `EGO_ITEM_PUB` + catalog/template assignment | W2 — per mapping §2.1 |
| 5 | Item costs (opening WAC) | 35,000 active SKUs | Cost API / `CST_ITEM_CST_DTLS_INTERFACE`, then live WAC from first GR | W2 — per mapping §2.1 WAC rule |
| 6 | Kits/BOMs | VS-92 bundle catalog | `BOM_BO_PUB` / BOM interface | W2 |
| 7 | Price lists & modifiers | Regular/clearance/promo hierarchy | `QP_PRICE_LIST_PUB` + modifier/qualifier loads | W2 — before any channel cutover |
| 8 | Suppliers + sites + TIN/ATC | ~800–1,000 active vendors | TCA/supplier APIs (`AP_VENDOR_PUB_PKG` class) | W1 — per mapping §2.2 |
| 9 | Customers (trade, corporate, loyalty members) | ~5,400 AR accounts canon | TCA party/site/account APIs (`HZ_*`) + customer profile classes | W3 — per mapping §2.3 |
| 10 | Employees + assignments + EITs | 6,911 headcount (200×29 stores + 600 DC + 511 HQ) | `HR_PERSON_API`/assignment APIs + EIT loads | W4 — per mapping §2.x |
| 11 | Payroll YTD balances | Per BIR reconciliation needs | Loaded into the **in-house payroll build** (Payroll PH); EBS receives no payroll balances — period costing journals post via row-12's interface path (E8) | W4 — statutory reconciliation gate |
| 12 | Opening GL balances (all 5 ledgers) | Balance-sheet + P&L stubs | `GL_INTERFACE` → Journal Import, one journal per entity/segment check | W1 — go-live weekend |
| 13 | Open AP invoices + advances | Legacy accounting | `AP_INVOICES_INTERFACE` (+ withholding at interface) | W1 |
| 14 | Open AR transactions + PDC registers | Trade/corporate books | AutoInvoice (`RA_INTERFACE_LINES_ALL`) + receipt APIs | W1 |
| 15 | Open purchase orders / blanket agreements | Active POs only | Purchasing document open interface | W1 |
| 16 | Opening onhand per org/locator | Post wall-to-wall count (W42 discipline) | `MTL_TRANSACTIONS_INTERFACE` (opening-balance issue/receipt pair per org) | Per-wave go-live |
| 17 | Fixed assets + accumulated depreciation | FA register | `FA_MASS_ADDITIONS` / asset API | W5 |
| 18 | Projects (active capex/construction) | Open projects | Project APIs + cost-interface for open commitments | W5 |
| 19 | Leases (active portfolio) | Property/lease register | Property Manager contract import + abstracts | W5 — PFRS 16 EXT schedules rebuild from abstracts |
| 20 | Banks, accounts, signatories | Treasury register | CE bank model + IBY setup | W1 |
| 21 | Attachments & documents (contracts, permits) | Per VS-88 retention rules | FND attachments API against migrated entities | Rolling |

Volumes anchor to the canonical
[data-migration-mapping](../01-model-company/data-migration-mapping.md) targets — no
new totals are introduced here.

---

## 2. Sequence & Dependencies

```
W0  Foundation setup (rows 1–3)
      └─> W1  Financial core: suppliers (8) → banks (20) → open AP/PO (13, 15)
      │       → opening GL (12) → AR books (14)
      └─> W2  Supply chain: items (4) → costs (5) → BOMs (7→6) → price lists (7)
      │       → onhand (16, per wave)
      └─> W3  O2C: customers (9) → channels live (POS/ecom cutover)
      └─> W4  People: employees (10) → payroll YTD into the build (11) → payroll posting verified (E8)
      └─> W5  Assets/projects/property: FA (17) → projects (18) → leases (19)
```

Hard rules:

1. **Setup before data, masters before transactions** — org/tax/UOM precede items; items
   precede onhand, prices, and orders.
2. **One mock-load cycle minimum per wave**, two for W1/W2 — mock loads exercise the full
   validate-convert-reconcile loop on masked clones (W384 masking rule holds for mocks).
3. **No back-door corrections**: post-load fixes go through the same interfaces/APIs, so the
   audit trail shows one path in.

---

## 3. Validation Gates (per W73 / W385)

| Gate | Check | Pass criterion |
|---|---|---|
| G1 Pre-load profile | Field completeness/format per mapping doc (TIN formats, ATC validity, UOM codes) | 100% of rows clean or waived by data owner |
| G2 Load acceptance | Interface rejection report per object | Rejections triaged to zero; waivers logged |
| G3 Count reconciliation | Source count vs loaded count per object/org | Exact tie-out (counts, not estimates) |
| G4 Value reconciliation | Monetary totals: GL stubs vs legacy trial balance; AP/AR aging vs legacy; onhand value vs costing | Zero unexplained difference; differences documented with sign-off |
| G5 Process validation | End-to-end business cycle on loaded data (receipt→match→pay; order→ship→invoice→receipt→reconcile) | Tier-1 workflows execute clean in UAT |
| G6 Parallel run | Legacy vs EBS outputs for 1–2 periods (W73) | Finance-certified tie-out before legacy retirement |

Each gate produces evidence retained against the migration register — the same
control-evidence discipline the 808-register expects in steady state.

---

## 4. Historical Data Strategy

| Domain | Decision | Rationale |
|---|---|---|
| POS sales history | Summarized 12 months + detailed 3 months into DP/warehouse, **not** into EBS transaction tables | Keeps OM/AR lean; analytics need history, the ledger does not |
| Legacy GL detail | Archived read-only; EBS holds balances + open items | Statutory retention satisfied via the archive (VS-88) |
| Closed POs/orders | Archived; only active documents migrate | Open-item clarity |
| Loyalty/order history | Full member migration; order history 6 months (phase-5 scope) | Per canonical mapping table |
| Payroll history | YTD-for-year only; prior years archived | BIR reconciliation is the driver |

---

## 5. Cutover Sequence (per-wave weekend)

1. Freeze legacy transactions; final extracts.
2. Load open items and balances (rows 12–16) through interfaces; run G3/G4.
3. Finance sign-off on tie-out; channel masters pushed to POS/ecommerce/WMS (price/item
   version manifests per [integrations.md](integrations.md) §2).
4. Legacy read-only; EBS transactional. Parallel-run window starts (W73).
5. Hypercare: interface exception queues staffed; reconciliation batches verified daily
   for the agreed stabilization window.

Rollback: legacy remains intact and read-only through the parallel window — reversal is a
decision, not a rebuild.

---

## 6. Roles

| Role | Duty |
|---|---|
| Data & reporting analyst (configure-team archetype) | Owns the load scripts, mappings, and gate evidence per object |
| Functional analyst (module) | Accepts the load per G2/G5 |
| Controller (FIN) | Signs G4 monetary tie-out |
| IT PO (owning team) | Owns the wave plan and cutover go/no-go pack |
| SEC lead | Signs masking/waiver register for non-production environments |

---

*Document Version: 1.2 | Date: 2026-09-14 | Structure-promotion re-base (profile v3.0 / TO v2.3): row 10's headcount re-based 6,762 → 6,911 (200×29 stores + 600 DC + 511 HQ). No other mapping rows changed. Prior v1.1 | Date: 2026-09-14 | Two-tier sourcing doctrine enacted: row 11 re-pointed (payroll YTD loads into the in-house Payroll PH build; EBS receives postings, not balances), W4 sequence line updated. Prior v1.0 (2026-09-14): initial issue — 21-row load-path register (object → EBS interface/API), wave sequence, six validation gates tied to W73/W385, historical-data strategy, cutover sequence and roles. Volume anchors quoted from data-migration-mapping.md and the canon (55,000 item-master / ~800–1,000 vendors / ~5,400 AR accounts / 6,762 HC); no new totals introduced.*
