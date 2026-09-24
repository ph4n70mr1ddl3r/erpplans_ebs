# Production Volume of Record — the actual operator's PROD (generated)

> **Generated** by [`production-volume-of-record.py`](../07-methodology/production-volume-of-record.py) `--refresh` on **2026-09-24 23:48 UTC** — read-only `appsro` against the production Active Data Guard standby. **This file is generated — do not hand-edit.** Validator Check 81 runs the instrument's `--check` mode: the register is re-rendered from the committed JSON cache (`production-volume-of-record-cache.json`) and byte-compared, so it cannot drift from its extraction of record. The instrument carries **no credentials** — they come from the environment or the operator's own access notes outside this repository. This register changes **no** model-company canon: every §4 delta is an explicit decision (W5580 governance, executive direction), never an automatic re-base.

## §1 Operating volumes — trailing 12 months, measured live

| Metric | Actual (12 mo) |
|---|---|
| POS transactions (headers) | 13,305,968 |
| POS-active stores (last 7 days) | 132 |
| Purchase orders | 22,175 |
| PO lines | 141,839 |
| Inter-branch transfer orders (STROO) | 532,542 |
| OM order lines (all types) | 1,596,418 |
| AP supplier invoices | 188,566 |
| AR credit memos (returns instrument) | 14,801 |
| PO receipt lines | 3,144,047 |
| GL journal batches | 291,374 |

## §2 Structure & estate

| Metric | Actual |
|---|---|
| Legal entities (inventory-org view) | 15 |
| Inventory organizations | 291 |
| Suppliers total / active | 8,237 / 6,950 |
| EBS accounts active / logged-in 30d | 514 / 468 |

## §3 Masterfiles

- Items defined in the item master: **113,950**
- Items with on-hand inventory: **31,475**
- POS-active stores (distinct STORE_ID, last 7 days): **132**
- Top item catalog groups: none maintained on the item master (catalog groups unused — the operator's item taxonomy, if any, lives in item categories)

## §4 Calibration surface — model-company canon vs production actual

| Parameter | Model-company canon (source) | Production actual | Reading |
|---|---|---|---|
| Stores | 200 (root README; data-volumes §1.1 mirrors the operator) | 132 POS-active (§2 inventory orgs 291) | OPEN — reconcile the 171-store calibration basis (data-volumes v4.7) vs the ~232-store audit figure vs the live POS-active count |
| POS receipts per store per day (design target 467 = 93,333/day ÷ 200) | 467 | ≈ 276.0 (12-mo POS ÷ stores ÷ days) | OPEN — the 2026-07-30 probe measured 126–510/store/day, mean ~330; decide target-vs-measured |
| Purchase orders per month (canon 1,650–1,950) | 1,650–1,950 | ≈ 1,848 | CONFIRMED if within band — the §1.1 calibration held |
| Replenishment transfers per month (canon ~50,000) | ~50,000 | ≈ 44,378 | CONFIRMED if ~250/store on the live store count |
| Customer returns AR credit memos per month (canon ~1,200) | ~1,200 | ≈ 1,233 | CONFIRMED if within band |
| Active SKUs | 35,000 | 31,475 items with on-hand | OPEN — near-canon if within ±15% |
| Item master | ~55,000 | 113,950 defined | OPEN — the operator runs ~2x the modeled master |
| Legal entities | 5 (ebs-platform-architecture) | 15 | BY DESIGN — the model company consolidates; the operator runs 15 entity books |
| Inventory organizations | 205 | 291 | BY DESIGN — re-base only with the store/DC estate decision |
| Suppliers on the master | — | 8,237 total / 6,950 active | NEW BASIS — adopt as the supplier-master scale when the P2P docs are next revised |
| EBS application users | — | 514 active / 468 30-day logins | NEW BASIS — the licensing-BOM user driver grounds here |

## §5 Decision register

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

## §6 Method & freshness

- Extracted: **2026-09-24 23:48 UTC**; query window: trailing 12 months from the database SYSDATE.
- Route: read-only `appsro` on the Active Data Guard standby (the operator's own
  access route; credentials via environment or ACCESS_EBS_HOME notes — never committed).
- Timeout/error queries degrade to '—' here and are listed in the cache with their
  status; `--refresh` re-attempts everything. Prior published sources: the 2026-06
  reports and the 2026-07-30 POS probe under the operator's access_ebs folder.
- Pinned by validate-repo.sh **Check 81** (`--check` byte-verify from the committed
  cache). Refresh cadence: monthly, or before any calibration decision.

*Generated 2026-09-24 23:48 UTC by production-volume-of-record.py — do not hand-edit.*
