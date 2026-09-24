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
| 10 | Employees + assignments + EITs | 6,918 headcount (200×29 stores + 600 DC + 518 HQ active; Trade / Account Management's 7 disabled — prepared (x); the IT estate's TPS build squad's 7 deferred — prepared (ad), registry CAP-B01) | `HR_PERSON_API`/assignment APIs + EIT loads | W4 — per mapping §2.x |
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
| 22 | Equipment lease book — lessor side (active contracts, billing schedules, serviced assets) | Legacy lease/rental register | Lease & Finance Management contract & billing-schedule import; serviced assets to Install Base (fit-gap A13, §4 resolution 9) | W5 — billing schedules verified against AR before go-live |
| 23 | Maintainable asset & equipment register (facility equipment, DC MHE, tool-rental fleet, measurement/calibration devices, EVSE, renewable assets, delivery-fleet vehicles & tires — VS-06 W1348/W1349) | FA asset register + equipment logs & PM calendars | eAM asset import (FA-linked instance numbers); PM schedules, activity codes and calibration attributes (fit-gap F5, §4 resolution 13) | W5 — PM generation verified against the equipment register before go-live |
| 24 | Internal-control register (CTL-01–CTL-808) | 808 controls | In-house Audit & GRC platform control-library load (BUILD — fit-gap H11, re-dispositioned 2026-09-22 per Vision VF-2; the load design is unchanged) — objective/activity/owner/workflow mapping from the [internal-controls matrix](../01-model-company/internal-controls-matrix.md) (§4 resolution 30/36) | W0 — before the first assessment cycle |

Volumes anchor to the canonical
[data-migration-mapping](../01-model-company/data-migration-mapping.md) targets — no
new totals are introduced here.

---

## 2. Sequence & Dependencies

```
W0  Foundation setup (rows 1–3) + the control register into the Audit & GRC platform (24)
      └─> W1  Financial core: suppliers (8) → banks (20) → open AP/PO (13, 15)
      │       → opening GL (12) → AR books (14)
      └─> W2  Supply chain: items (4) → costs (5) → BOMs (7→6) → price lists (7)
      │       → onhand (16, per wave)
      └─> W3  O2C: customers (9) → channels live (POS/ecom cutover)
      └─> W4  People: employees (10) → payroll YTD into the build (11) → payroll posting verified (E8)
      └─> W5  Assets/projects/property: FA (17) → projects (18) → leases (19) → equipment lease book (22) → maintainable asset & equipment register (23)
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

*Document Version: 2.0 | Date: 2026-09-23 | **TPS build squad deferred — prepared (2026-09-23 (ad)): §2 row 10.** The target employee count re-bases 6,925 → 6,918 active (525 → 518 HQ; the TPS build squad's 7 deferred — prepared alongside the disabled—prepared Trade department; OM v3.25, TO v3.1). No mapping-row, sequence or load-order change. Prior 1.9 |
Prior 1.9 | Date: 2026-09-23 | Trade-desk disablement (2026-09-23 (x)): §2 row 10's target employee count re-based 6,932 → 6,925 active (registry CAP-B01). Prior 1.8 | Date: 2026-09-22 | **Sixty-fifth-wave review (the §2 sequence tree's retired ICM load target).** The VF-2 re-point (v1.7) trued row 24's load target to the in-house Audit & GRC platform control-library load but missed the §2 'Sequence & Dependencies' tree one section below — the W0 line still routed 'the control register into ICM (24)', contradicting the row it summarizes (the same unguarded summary-surface class the fifty-fifth wave swept); the tree line re-pointed to the platform. No row, load path, sequence edge or gate changed. Guard: ebs_blueprint_hits gains the arm (the 'into ICM (24)' form banned on the footer-stripped body, the corrected W0 anchor required). Prior v1.7 | Date: 2026-09-22 | **Vision-VF-2 execution:** row 24's load target re-pointed from Oracle Internal Controls Manager (obsolete, not installed on either installation of record) to the in-house Audit & GRC platform build (fit-gap H11 → BUILD); the W0 sequence and load design unchanged. Prior v1.6 | Date: 2026-09-16 | **Sixth-pass EBS-exhaustion audit:** row 24 added — the internal-control register (CTL-01–CTL-808) loads into Oracle Internal Controls Manager (fit-gap H11, §4 resolution 30; W0, before the first assessment cycle); the sequence diagram trued in the same pass — W0's line names row 24 and W5's line gains the stranded row 23 (the second-pass eAM register, whose W5 gate the v1.4 diagram never carried). No other mapping rows changed. Prior v1.5 | Date: 2026-09-16 | **Fourth-pass EBS-exhaustion audit:** row 23's eAM estate list extended to name the delivery-fleet vehicles & tires (VS-06 W1348/W1349 — the F5 fourth-pass true; same load path, same gate). No new rows — the W424 outgoing-PDC book accumulates into Bills Payable transactionally from go-live, the same posture as the AR Bills-Receivable side. Prior v1.4 | Date: 2026-09-16 | **Second-pass EBS-exhaustion audit:** row 23 added — the maintainable asset & equipment register loads into Oracle eAM (fit-gap F5; facility/DC/tool-rental/calibration/EVSE/renewable equipment, FA-linked, PM calendars verified before go-live). No other mapping rows changed. Prior v1.3 | Date: 2026-09-15 | **EBS-exhaustion audit:** row 22 added — the VS-96 lessor equipment lease book migrates into Lease & Finance Management (fit-gap A13, §4 resolution 9; serviced assets to Install Base per D13's Field Service disposition), W5 sequence line updated. No other mapping rows changed. Prior v1.2 | Date: 2026-09-14 | Structure-promotion re-base (profile v3.0 / TO v2.3): row 10's headcount re-based 6,762 → 6,911 (200×29 stores + 600 DC + 511 HQ). No other mapping rows changed. Prior v1.1 | Date: 2026-09-14 | Two-tier sourcing doctrine enacted: row 11 re-pointed (payroll YTD loads into the in-house Payroll PH build; EBS receives postings, not balances), W4 sequence line updated. Prior v1.0 (2026-09-14): initial issue — 21-row load-path register (object → EBS interface/API), wave sequence, six validation gates tied to W73/W385, historical-data strategy, cutover sequence and roles. Volume anchors quoted from data-migration-mapping.md and the canon (55,000 item-master / ~800–1,000 vendors / ~5,400 AR accounts / 6,762 HC); no new totals introduced.*
