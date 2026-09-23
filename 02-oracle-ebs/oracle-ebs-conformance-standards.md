# Oracle EBS Conformance Standards — the Best-Practice Canon for Transactional Workflows

> Codifies how the model company's workflows must behave so the [workflow corpus](../01-model-company/workflows/README.md) runs the way Oracle E-Business Suite 12.2 is designed to be run — destination-type routing, mass-additions capitalization, custody-of-record, derived tax books, controlled-issue consumables — rather than fighting the suite's grain. Every rule names its Oracle mechanism, its workflow surface, and how conformance is checked. Companion tool: [`audit-oracle-conformance.py`](../07-methodology/audit-oracle-conformance.py).

---

## 1. Why this document exists

The workflow corpus (5,432 workflows across 569 process areas) was authored business-first and
platform-aligned through the [fit-gap register](fit-gap-analysis.md) at the *vehicle* level — which
EBS product serves which capability. This canon goes one level deeper: the *behavioral* standards
Oracle's own implementation methodology (AIM/OUIM) expects transactions to follow. A workflow can
name the right module and still behave in a way that produces audit findings, ghost assets, or
unreconcilable sub-ledgers. These rules close that gap; the audit tool enforces them mechanically.

## 2. The routing principle — one decision drives everything

Every purchased good in EBS is routed by the purchase-order line **destination type** — the master
switch that separates the model company's three non-merchandise worlds:

| Destination type | Meaning | Lands in | Model-company category |
|---|---|---|---|
| **Inventory** | Item for resale or controlled internal stock; item-master record, valued on-hand | Oracle Inventory org / subinventory | Trade items |
| **Expense** | Consumed on receipt; charged directly to a cost-center expense account, never capitalized | Oracle GL via the AP invoice | Office supplies and consumables |
| **Asset** or a CIP project | Capitalized item at or above the capitalization threshold with a useful life over one year | Oracle Payables → Mass Additions → Oracle Assets | Fixed assets |

The requisitioner never chooses an accounting treatment. Classification happens at master-data
level — item templates, asset categories, non-catalog request templates — so the transaction
cannot be misrouted by judgment at the point of entry. This is the core Oracle design standard.

## 3. The standards

### A. Routing and classification

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-01 | The destination type on the PO line — Inventory, Expense, or Asset — decides the accounting treatment; no transaction-level overrides | PO line destination type; receiving routing | All PA-15, PA-34 workflows |
| OC-02 | Classification lives in master data, not user judgment: item templates and iProcurement stores pre-flag asset vs expense vs inventory before requisition | Item templates, iProcurement stores, non-catalog request templates | PA-29 master data; PA-34.1 catalogs |
| OC-03 | The capitalization threshold is enforced as a category-driven default plus PO flag, never as requester discretion; threshold gaming is detected by repeat-purchase flags | Asset category defaults; purchasing category flags | W1690 step 3 |

### B. Fixed-asset lifecycle and custody

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-04 | Every capitalizable purchase flows PO → receipt → AP invoice → **Mass Additions**, and nothing posts to the register without the queue review — the Fixed Asset Accountant posts as addition, charges to expense, splits, merges, or rejects | Mass Additions Create; the FA mass-additions review queue | W1690, W1690.1 touchpoints |
| OC-05 | Every asset carries a **custodian of record** — populated in the asset record's Assigned-To field at registration. Named individual for IT equipment, tools and vehicles; role-level of record for fixtures. Custody is never blank and never a department alone | Oracle Assets Assigned-To and Location fields | W1690 step 2; the custody table in §4 |
| OC-06 | **Tag before use, scan as acceptance**: no asset goes productive without a tag tied to the asset number, and the location's tag-scan confirmation doubles as the custodian of record's custody acceptance | Barcode/QR tag generation; mobile scan confirmation writing to the asset record | W1692 |
| OC-07 | **Transfers are custody events, not moves**: the sending custodian of record releases the asset and the receiving custodian accepts it — custody is in transit, never unassigned; the register update is the evidence of transfer | Oracle Assets transfer; location and Assigned-To update | W1693 steps 1 and 4 |
| OC-08 | Depreciation calculates in each entity's **corporate book**; tax books **derive from** the corporate book — tax schedules are never maintained independently of the corporate register | Corporate book per ledger; tax books derived from corporate | W1698 step 2; W1704 |
| OC-09 | Retirements are approval-gated before the register is touched: location-initiated request, Finance review, disposal evidence attached, then system retirement with proceeds and gain/loss | Oracle Assets retirement with proceed-of-sale; AME approval above threshold | W1708, W1711 |
| OC-10 | Physical verification is executed by the location's custodian of record and attested by signature, counted down by a party independent of the book owner — the Fixed Asset Accountant never counts their own register alone | Register extract by location; mobile scan reconciliation | W1706 |
| OC-11 | CIP assets are owned by the project until a formal **custody handover**: the completion certificate includes the operating custodian of record's acceptance, and registration assigns the custodian so no asset turns over unowned | CIP-to-asset conversion; Projects handover | W1828 step 2; W1829 |

### C. Supplies, consumables and non-trade items

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-12 | Supplies are never capitalized regardless of local opinion — below the threshold or under one year of life means expense, full stop | Destination type Expense | PA-34.1 |
| OC-13 | Treatment is chosen per class of spend, not one size for all: direct expense for fast-consumed low-value items; **expense subinventory** where issues must be counted; blanket PO releases for predictable recurring volume | iProcurement non-catalog requests; expense subinventories; blanket releases | W1668, W1673 |
| OC-14 | **Controlled-issue items** — PPE, uniforms, toner-class consumables, company-grade equipment below the threshold — are issued per requisition from a custodied storeroom or expense subinventory with a named custodian, and counted on a recurring cycle: expensed in the books, accountable in custody | Expense subinventory issues; cycle count program | W1670, W1673 |
| OC-15 | A **tractable-item pool** catches what the capitalization threshold would otherwise lose: items below the threshold but accountable by nature — power tools, measuring instruments, cameras — are expensed yet carried on a countable minor-asset register so the physical count covers them | Descriptive flexfield or minor-asset register alongside Oracle Assets | W1690 step 3 |

### D. Approvals and segregation of duties

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-16 | No single person records the asset, receives it, holds it, and disposes of it: the Fixed Asset Accountant owns the register, receiving owns the receipt, the custodian of record holds the asset, Finance leadership approves disposal | EBS responsibility design; SoD role queries | PA-35 RACI columns |
| OC-17 | Approvals ride position hierarchies and AME rules above value thresholds — not ad-hoc name chains | Position hierarchy; AME | PA-15, PA-40.1 |
| OC-18 | High-value capitalization and retirement carry a second gate: capitalization approval for assets at or above the executive threshold, and CFO-visible disposal review with gain/loss reporting | AME rules; FA approval workflows | W1690 step 4; W1708 |

### E. Receiving and matching

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-19 | Asset lines require receipt — the three-way match of PO, receipt and invoice is mandatory for capitalized purchases; two-way matching is reserved for true expense consumables | Purchasing receiving options; AP matching | PA-15.1 steps 2–4 |

### F. Master data

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-20 | The asset category key flexfield — major and minor segments — defaults the asset and clearing GL accounts, book, depreciation method and useful life; accounts are never keyed per asset | Asset Category KFF defaults | W1691 category tree |
| OC-21 | Asset Key carries the cost-center dimension and Location carries the physical place; together with Assigned-To they form the custody triangle that every custody report reads | Asset Key and Location KFFs; Assigned-To | W1690, W1693, W1706 |

### G. Assurance

| ID | Standard | Oracle EBS mechanism | Model-company surface |
|---|---|---|---|
| OC-22 | The sub-ledger reconciles to the GL every period — gross, accumulated depreciation and net book value, per entity, before close | FA-to-GL reconciliation report | W1705 reconciliation |
| OC-23 | Counting is a program, not an event: the annual wall-to-wall count for fixed assets, cycle counts for controlled-issue supplies, and the tractable pool inside the annual count | Physical inventory and cycle count; the W1706 program | W1706, W1707; OC-14 |

## 4. Custody of record — the operating model

Oracle's implicit standard, reflected in the Assigned-To field and in audit methodology, is a
three-way split of record ownership, physical custody and custody at birth:

| Function | Owner | What they hold | Where it lives |
|---|---|---|---|
| Record ownership | Fixed Asset Accountant — Finance | The register truth: cost, book, depreciation | Oracle Assets |
| Physical custody | The custodian of record — the location manager, DC supervisor or department head of record | The physical asset; answerable for its existence and condition | Assigned-To plus Location on the asset record |
| Custody at birth | Receiving Clerk, then the first custodian of record after the acceptance scan | From dock to tag to acceptance — brief, documented, signed | Receipt plus the W1692 acceptance scan |

The five rules of custody, each testable at audit:

1. Every asset has exactly one custodian of record — never blank, never a department alone.
2. Custody transfers are events with a release and an acceptance — never conventions.
3. Record owner, receiver, custodian and disposal approver are four different people.
4. The custodian attests at the count; Internal Audit verifies independently.
5. No asset goes productive without a tag, and the acceptance scan is the signature.

## 5. Enforcement

The companion tool [`audit-oracle-conformance.py`](../07-methodology/audit-oracle-conformance.py)
implements this canon as machine-checkable rules over the workflow corpus:

- **Anchor rules** — the repaired workflows must carry their conformance clauses; stripping one
  fires and forces a conscious re-point. Enforced in `--guard` mode per the house convention.
- **Retired-form rules** — the replaced phrasings are banned in their files of scope so the
  defect class cannot silently return.
- **Corpus scans** — informational sweeps for the judgment classes the anchors cannot reach
  (supplies capitalized in PA-34, Fixed Asset Accountant receiving steps, unattested counts),
  reported as a findings census for per-workflow triage.

## 6. Initial conformance review — 2026-09-23

The review audited the custody and treatment chain — the highest-risk class under this canon —
across VS-35, VS-34, VS-40 and VS-15. Eleven findings; all repaired in the same pass:

| # | Finding | Rule | Disposition |
|---|---|---|---|
| 1 | W1690 registered assets without a custodian of record — the responsible department was recorded, no Assigned-To | OC-05 | Fixed — step 2(h) |
| 2 | W1690's capitalization pipeline did not name the mass-additions queue as the AP-to-Assets gate | OC-04 | Fixed — step 1(a) + touchpoint |
| 3 | W1690 had no below-threshold accountable pool — countable items fell out of the estate at the threshold | OC-15 | Fixed — step 3 |
| 4 | W1692 tag confirmation was not custody acceptance — assets went productive unsigned | OC-06 | Fixed — step 4 |
| 5 | W1693 transfers moved assets without a release step — custody was unassigned in transit | OC-07 | Fixed — steps 1, 4 |
| 6 | W1698 depreciation did not name corporate-book derivation of the tax book | OC-08 | Fixed — step 2(f) |
| 7 | W1706 count lacked the custodian attestation signature | OC-10 | Fixed — step 2(e) |
| 8 | W1828 turnover certificate omitted the custody handover to the operating custodian | OC-11 | Fixed — step 2(e) |
| 9 | W1670 PPE and uniforms issued without requisition control from a custodied storeroom | OC-14 | Fixed — step 4 |
| 10 | W1673 office supplies lacked the controlled-issue treatment for accountable consumables | OC-14 | Fixed — step 3 |
| 11 | W1708 retirement approvals, W1706 audit independence, PA-15.1 three-way match, W1711 gain/loss — verified conformant | OC-09, OC-10, OC-19 | None — recorded conformant |

Tracked for per-workflow triage via the tool's corpus scans: the corpus-wide segregation-of-duties
role-pair sweep, and the W1695 maintenance-history vehicle naming against the adopted eAM row.

---

*Document Version: 1.0 | Date: 2026-09-23 | **Initial canon.** OC-01–OC-23 issued in seven families; §4 custody-of-record operating model; §5 enforcement contract; §6 initial conformance review — eleven findings, all repaired same-pass.*
