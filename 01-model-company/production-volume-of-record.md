# Production Volume of Record — the actual operator's PROD (generated)

> **Generated** by [`production-volume-of-record.py`](../07-methodology/production-volume-of-record.py) `--refresh` on **2026-09-25 00:20 UTC** — read-only `appsro` against the production Active Data Guard standby. **This file is generated — do not hand-edit.** Validator Check 81 runs the instrument's `--check` mode: the register is re-rendered from the committed JSON cache (`production-volume-of-record-cache.json`) and byte-compared, so it cannot drift from its extraction of record. The instrument carries **no credentials** — they come from the environment or the operator's own access notes outside this repository. This register changes **no** model-company canon: every §6 delta is an explicit decision (W5580 governance, executive direction), never an automatic re-base.

## §1 Operating volumes — trailing 12 months, measured live

| Metric | Actual (12 mo) |
|---|---|
| POS transactions (headers) | 13,306,019 |
| POS-active stores (last 7 days) | 132 |
| Purchase orders | 22,180 |
| PO lines | 141,866 |
| Inter-branch transfer orders (STROO) | 532,538 |
| OM order lines (all types) | 1,596,414 |
| AP supplier invoices | 188,596 |
| AR credit memos (returns instrument) | 14,810 |
| PO receipt lines | 3,143,963 |
| GL journal batches | 291,432 |

## §2 Structure & estate

| Metric | Actual |
|---|---|
| Legal entities (inventory-org view) | 15 |
| Inventory organizations | 291 |
| Suppliers total / active | 8,237 / 6,950 |
| EBS accounts active / logged-in 30d | 514 / 468 |

## §3 Masterfiles

- Items defined in the item master: **113,954**
- Items with on-hand inventory: **31,475**
- POS-active stores (distinct STORE_ID, last 7 days): **132**
- Top item catalog groups: none maintained on the item master (catalog groups unused — the operator's item taxonomy, if any, lives in item categories)

## §4 Store size segments — POS-measured, last 90 days

Segmentation of the 132 POS-posting stores by transactions per store per day (90-day basis; tercile cuts at 201.5 and 312.7 trx/day):

| Segment | Stores | Store share | Mean trx/store/day | 90-day volume | Volume share |
|---|---|---|---|---|---|
| Big | 45 | 34% | 425.8 | 1,724,453 | 53% |
| Medium | 44 | 33% | 251.2 | 994,632 | 30% |
| Small | 43 | 33% | 143.5 | 555,458 | 17% |

Largest store: TAG (109) at 823.7 trx/day; smallest: GUN (2307) at 13.1 — a 63x spread the uniform per-store model-company canon does not capture.

## §5 Distribution-network tiers — STROO outbound, trailing 12 months

Tiering the network by each org's share of outbound transfer lines (hub ≥5%, regional 1–5%, satellite <1%):

| Tier | Orgs | Line share | Lines/month | Cut | Members (top) |
|---|---|---|---|---|---|
| National hubs | 7 | 88% | 116,871.0 | ≥5% of lines | SDC (113), CDC (818), BDC (1341), CD2 (1521), CD3 (1561), CD4 (1562), … |
| Regional DCs | 3 | 4% | 4,774.7 | 1–5% | CD5 (2206), CD6 (2207), CD7 (2326) |
| Satellite / store-attached | 143 | 8% | 11,228.1 | <1% | BAJ (101), MAT (102), ILI (103), CAG (104), PAR (105), MAN (106), … |

**Inbound sourcing at stores** (DELIVER receipt lines, trailing 12 mo; 1,473,853 store receipt lines / 182,364,007 units):

- **INTERNAL ORDER (DC/inter-branch transfers): 92% of lines, 94% of quantity** — the DC network is the store-replenishment artery
- VENDOR direct-to-store: 6% of lines, 4% of quantity — a supplementary slice, not the artery
- INVENTORY (other internal) sources: 2% of lines, 2% of quantity

Landing-zone context: 93% of ALL DELIVER receipt lines land at stores — but as transfer receipts from the DC network, not vendor deliveries. (The (bb) wave's '94% store-direct' reading conflated the landing zone with the source; corrected here.)

## §6 Calibration surface — model-company canon vs production actual

| Parameter | Model-company canon (source) | Production actual | Reading |
|---|---|---|---|
| Stores | 200 (root README; data-volumes §1.1 mirrors the operator) | 132 POS-active (§2 inventory orgs 291) | OPEN — reconcile the 171-store calibration basis (data-volumes v4.7) vs the ~232-store audit figure vs the live POS-active count |
| POS receipts per store per day (design target 467 = 93,333/day ÷ 200) | 467 | ≈ 276.0 (12-mo POS ÷ stores ÷ days) | OPEN — the 2026-07-30 probe measured 126–510/store/day, mean ~330; decide target-vs-measured |
| Purchase orders per month (canon 1,650–1,950) | 1,650–1,950 | ≈ 1,848 | CONFIRMED if within band — the §1.1 calibration held |
| Replenishment transfers per month (canon ~50,000) | ~50,000 | ≈ 44,378 | CONFIRMED if ~250/store on the live store count |
| Customer returns AR credit memos per month (canon ~1,200) | ~1,200 | ≈ 1,234 | CONFIRMED if within band |
| Active SKUs | 35,000 | 31,475 items with on-hand | OPEN — near-canon if within ±15% |
| Item master | ~55,000 | 113,954 defined | OPEN — the operator runs ~2x the modeled master |
| Legal entities | 5 (ebs-platform-architecture) | 15 | BY DESIGN — the model company consolidates; the operator runs 15 entity books |
| Inventory organizations | 205 | 291 | BY DESIGN — re-base only with the store/DC estate decision |
| Suppliers on the master | — | 8,237 total / 6,950 active | NEW BASIS — adopt as the supplier-master scale when the P2P docs are next revised |
| EBS application users | — | 514 active / 468 30-day logins | NEW BASIS — the licensing-BOM user driver grounds here |

## §7 Decision register

1. **Store-count basis** — one number of record for the mirrored estate (the §1.1
   calibration used 171; the capability audit says ~232; §2 is the live POS-active
   count). Re-point data-volumes §1.1, the profile and the TO store math to it in one
   governed pass.
2. **POS design target** — keep the 467/store/day planning canon (top of the measured
   band) or re-base to the measured mean; either way, state the choice once, here and
   in data-volumes §1.1, not per-document.
3. **Entity posture** — the model company's 5-entity consolidation is a design choice
   against the operator's 15 books; confirm it stays a design choice as the fit-gap
   and ledger-model docs evolve.
4. **Masterfile scale** — the ~55,000 item-master canon and the supplier-master
   vacuum: adopt §3 actuals as the P2P/master-data planning basis at the next
   revision of the docs that quote them.
5. **Role-load reliability** — the load model's cadence layer graduates from prose
   parsing (53% coverage) to this register: per-workflow-event cadences ground on the
   measured 12-month volumes above before any headcount optimization is taken.
6. **Store segmentation** — adopt the measured size segments (§4) for the model
   company's store estate: a big/medium/small mix with per-segment POS volumes
   replaces the uniform 200-store canon, driving differentiated staffing per segment
   (the TO's flat 29/store) — the single highest-leverage headcount insight in this
   register.
7. **Distribution tiers** — re-cut the model company's 4-DC design into the measured
   network tiers (§5: national hubs / regional / satellite) with per-tier outbound
   volumes. The inbound correction stands: the DC network is the store-replenishment
   artery (§5 inbound sourcing — the (bb) wave's '94% store-direct' reading was wrong,
   it conflated landing zone with source); vendor direct-to-store stays a supplementary
   P2P slice, not the artery.

## §8 Method & freshness

- Extracted: **2026-09-25 00:20 UTC**; query window: trailing 12 months from the database SYSDATE.
- Route: read-only `appsro` on the Active Data Guard standby (the operator's own
  access route; credentials via environment or ACCESS_EBS_HOME notes — never committed).
- Timeout/error queries degrade to '—' here and are listed in the cache with their
  status; `--refresh` re-attempts everything. Prior published sources: the 2026-06
  reports and the 2026-07-30 POS probe under the operator's access_ebs folder.
- Pinned by validate-repo.sh **Check 81** (`--check` byte-verify from the committed
  cache). Refresh cadence: monthly, or before any calibration decision.

*Generated 2026-09-25 00:20 UTC by production-volume-of-record.py — do not hand-edit.*
