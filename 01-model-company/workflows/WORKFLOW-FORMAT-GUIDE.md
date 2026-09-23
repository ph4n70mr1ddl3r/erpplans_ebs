# Workflow Format Guide

> Describes the standard format, conventions, and role key used across all operational
> workflow domain files in this repository. Enforced (informationally) by
> [`07-methodology/validate-repo.sh`](../../07-methodology/validate-repo.sh).

---

## Purpose of Workflows

The operational workflows serve three purposes:

1. **Validate headcount** — by mapping work volume to roles, we can verify staffing assumptions
2. **Inform ERP design** — each workflow reveals system touchpoints, automation opportunities, and integration needs
3. **Optimize organization** — by exposing handoffs, bottlenecks, and spans of control

For these purposes to hold, the analysis fields (**Pain Points / Risks**, **System Touchpoints**,
**Time Estimate**, and **Automation / Controls** where used) must contain *workflow-specific*
content. Verbatim boilerplate (identical text copied across many workflows) defeats all three
purposes and is flagged by the validator (Check 10).

---

## Standard Workflow Format

Each workflow is a `## W<number>. <Name>` block inside a Process Area (PA) file, with the
following fields.

### Required fields (every workflow)

| Field | Meaning |
|---|---|
| **Trigger** | What initiates the workflow |
| **Frequency** | How often it occurs |
| **Volume** | How many instances per occurrence, with the ×-math that scales it to the enterprise |
| **Owner** | Role accountable for the outcome (the single throat-to-choke) |
| **Participants** | All other roles involved |
| **Steps** | Sequential activities in a table with Responsible (R) and Accountable (A) columns and a per-step Duration |
| **System Touchpoints** | Where ERP/system support is needed — name the *specific* module/object/integration (e.g. "Goods receipt exception; damage quarantine bin"), not a generic pointer |
| **Time Estimate** | Estimated effort per occurrence, rolled up to an annual or per-store figure where it drives headcount |
| **Pain Points / Risks** | What can go wrong, named specifically (e.g. "**Evidence risk**: damage not documented at receipt forfeits claim rights"), with the mitigating control |

> **Time-Estimate finalization note (2026-08-28).** The 407 `### Time Estimate` sections still carrying
> `backfill-time-estimate.py`'s honest-draft roll-up were finalized via
> [`07-methodology/finalize-time-estimates.py`](../../07-methodology/finalize-time-estimates.py):
> 118 mechanically unambiguous drafts (uniform per-occurrence step Durations × an explicit
> Frequency occurrence count) were auto-decided, and the 289 mixed-cadence / per-unit /
> event-driven cases were adjudicated one by one — every paragraph derives its figures from
> the workflow's own step Durations, Frequency, and Volume (per-unit steps scaled by Volume
> counts shown explicitly; own-cadence steps annualized at their own cadence; elapsed
> timelines reported, never summed into effort; event-driven frequencies honestly carry no
> annual figure). The retired draft literal and full section coverage are guarded by
> validator Check 49.

> **Inline-arithmetic audit note (2026-08-29).** Every explicit scaling chain written into the finalized
> Time Estimate and Staffing Implication paragraphs (`<per-occurrence> × <count> (=|≈) <result>`) was
> re-derived by [`07-methodology/audit-time-estimate-math.py`](../../07-methodology/audit-time-estimate-math.py)
> under the unit conventions this guide licenses — min↔hours (÷/× 60), sec→hours, workday (×8) and
> workweek (×5/×7) alternates, month-length alternates, per-cadence annualization (×12 / ×4 / ×52 /
> ×365 / ×6), noun/suffix cancellation (`2 hours/visit × 20–30 visits/month`), the canonical 200-store
> and 4-DC chain scalings, shared-factor inheritance (`× 200 stores … + 3 hours per store`), and K/M
> endpoints. Twenty-five workflows carried defective chains (minutes labelled hours, counts
> double-multiplied, over- and understated products) and were repaired against their own step
> Durations, Frequency, and Volume; the strict `--guard` subset of the tool is enforced by validator
> Check 50. Accepted prose classes the tool reports but does not flag: house-style range padding
> (±35%), elapsed-window days/weeks reported verbatim, and hidden context factors stated elsewhere
> in the workflow.

> **Completeness note (2026-06-27; figure updated 2026-09-23).** All 5,433 workflows now carry all 9 required fields (validator Check 22 green; W5515–W5517 added 2026-09-03 with all fields; W5518–W5524 — the IT operating-model gap fill in VS-27 — added 2026-09-03 with all fields; W5525–W5528 — the people-capability & reporting-policy gap fill in VS-19.4/VS-17.4 — added 2026-09-03 with all fields; W5529–W5531 — the finance-workflow gap fill in VS-42.3/VS-17.3/VS-17.4 — added 2026-09-03 with all fields; W5532–W5534 — the operations-workflow gap fill in VS-19.3/VS-79.2/VS-23.2 — added 2026-09-04 with all fields; W5535 — the capability demand-intake & backlog-triage gap fill in PA-113.2/VS-113 — added 2026-09-04 with all fields; W5536–W5543 — the emergency & continuity workflow gap fill in VS-07.2/VS-24.2/VS-19.2/VS-18.3/VS-105.3/VS-118.2 — added 2026-09-05 with all fields; W5544–W5549 — the regulatory-shock, platform-outage & governance-continuity gap fill in VS-36.1/VS-79.3/VS-08.1/VS-54.2/VS-24.1 — added 2026-09-05 with all fields; W5550–W5553 — the channel-enforcement, employee-legal-status, OSH-enforcement & app-store-removal gap fill in VS-10.3/VS-19.1/VS-24.1/VS-75.1 — added 2026-09-05 with all fields; W5554–W5557 — the in-transit-security, fatality-scene, tampering-extortion & recruitment-fraud gap fill in VS-06.2/VS-147.3/VS-89.1/VS-121.1 — added 2026-09-05 with all fields; W5558–W5561 — the cyber-extortion, payment-diversion, land-occupation & water-continuity gap fill in VS-27.3/VS-18.2/VS-178.1/VS-07.2 — added 2026-09-05 with all fields; W5562–W5565 — the storefront-crash, brand-impersonation-scam, wallet-outage & adjacent-works gap fill in VS-147.2/VS-100.2/VS-08.1/VS-20.3 — added 2026-09-05 with all fields; W5566–W5569 — the terminal-tampering, procurement-impersonation, account-takeover & commute-disruption gap fill in VS-08.2/VS-03.2/VS-14.2/VS-141.2 — added 2026-09-05 with all fields; W5570–W5573 — the gas-leak, tsunami/storm-surge, media-exposé & server-room-environmental gap fill in VS-24.2/VS-26.1/VS-14.3/VS-27.2 — added 2026-09-05 with all fields; W5574 — the concessionaire connectivity request, approval & independent-circuit governance gap fill in VS-07.1 — added 2026-09-10 with all fields). The last 645 missing instances were closed as follows: the 224 missing **Participants** rows (VS-53–VS-63 plus VS-86/87/99/189) were mechanically derived from each workflow's own Steps-table roles via [`07-methodology/backfill-participants.py`](../../07-methodology/backfill-participants.py) (honest-draft: values come from authored steps; no invented roles); the 175 missing **System Touchpoints** and 246 missing **Pain Points / Risks** sections (VS-15–18, VS-27, VS-31–40, VS-48) were authored per-workflow, grounded in each workflow's own steps and cross-references. Treat these like any authored field: refine freely during per-workflow review.

### Standard analysis fields (add to every fully-detailed workflow)

These two fields were previously listed as "recommended"; a 2026-06-15 review found **Automation Opportunity absent from all 376 PA files** and **Controls present in only 5**. They are now standard for any fully-detailed workflow (see VS-73 for the reference implementation). As of 2026-06-20 the field **headers** are present on all **5,433 workflows (100% presence)** across all blocks (Core, Expansion, Statutory, and Gap analysis).

> **Content-quality caveat (2026-06-21).** Presence ≠ quality. The repo-wide insertion was performed by a first-pass generator (`add-automation-controls.py`), and a 2026-06-21 review found the bulk of the generated content is **draft** quality: Automation bullets were emitted as mid-phrase fragments (e.g. `- auto-review (account manager reviews application: (a) verify)`) and most Controls sections cited no CTL-XX from the controls register. Two corrections shipped in that review: (1) `backfill-controls.py` retroactively injected real CTL-XX references wherever `internal-controls-matrix.md` provides a workflow→control mapping, and normalized the missing blank line before the next `###` header; (2) validator **Check 21** now reports the live quality metrics (fragment-bullet count, CTL-XX coverage %, pure-boilerplate count) so the backlog is tracked rather than silently claimed as complete. Because the 67-control register was originally authored against the Core workflows (W1–W942), only ~60 workflows had a CTL mapping; the 2026-06-27 register extension (CTL-68–CTL-171, one anchor control per gap-analysis value stream VS-89–VS-192) raised mapped coverage via `backfill-controls.py`, and the 2026-06-28 process-area operating controls (CTL-240–CTL-808, `add-pa-controls.py`) closed CTL-XX citation to 100% of workflows — every Controls section now cites at least one register control (PA controls are honest-draft derived mappings pending per-workflow review). Treat any generated Automation/Controls bullet not matching the quality bar below as a draft pending per-workflow human refinement.

| Field | Meaning |
|---|---|
| **Automation Opportunity** | Steps that are manual today but are candidates for system automation — directly informs ERP design (purpose 2) |
| **Controls** | Internal-control IDs (from [`internal-controls-matrix.md`](../internal-controls-matrix.md)) exercised by this workflow — closes the loop with the 808-control register |

### Cross-reference field

| Field | Meaning |
|---|---|
| **Cross-references** | Links to related workflows in other value streams (e.g. "links to VS-04", "per W533") using the `VS-NN` and `W<number>` identifiers |

### Quality bar for the analysis fields

The fields that deliver the workflow's value are **System Touchpoints**, **Time Estimate**, and
**Pain Points / Risks**. Each must be specific to the workflow:

- ❌ `System Touchpoints: ERP integration point (W2599)` — generic, adds no information
- ✅ `System Touchpoints: Damage-case module with evidence attachments; image repository (links to VS-88)`
- ❌ `Pain Points: **Execution risk**: Operational variability mitigated by standard procedures and system controls` — generic boilerplate
- ✅ `Pain Points: **Evidence risk**: damage not documented at receipt forfeits claim rights; mitigated by mandatory photo + discrepancy capture at goods receipt`
- ❌ `Time Estimate: 30–120 min per occurrence` — generic range with no scaling math
- ✅ `Time Estimate: 5–15 min per discrepancy; ~72,000 receipts/yr → ~6,000 discrepancies/yr`
- ❌ `Automation Opportunity: Automate manual steps` — vacuous
- ✅ `Automation Opportunity: Weigh-scale → ERP auto-posting (eliminates hand-keyed volumes); mobile damage-flag → disposition-suggestion`
- ❌ `Controls: Standard controls apply` — vacuous
- ✅ `Controls: CTL-06 (DENR-certified vendor onboarding); CTL-44 (duplicate-invoice guard); operational: manifest-vs-invoice match before payment`

---

## Role Key (Responsible / Accountable)

The per-step **Steps** table uses two columns:

| Column | Meaning |
|---|---|
| **Role (R)** — Responsible | Does the work |
| **Role (A)** — Accountable | Owns the outcome (exactly one per step) |

Full **RACI** (adding **C**onsulted and **I**nformed) is **not** enumerated as per-step columns —
in practice it crowds the table and almost every step ends up R/A only. Instead:

- **Consulted** and **Informed** parties are captured in the workflow-level **Participants** field and in the narrative, and are called out explicitly only on the specific step where a consultation or notification handoff is material.
- Where a step genuinely needs a separate authorizer (e.g. a manager swipe for an override), that role is named in the step's **Role (A)** column or in the step prose.

This keeps the table readable while preserving accountability on every step.

---

## Naming Conventions

| Pattern | Example | Meaning |
|---|---|---|
| `W<number>` | W7, W2598, W3017 | Primary workflow. New value streams use sequential IDs allocated in blocks (see [`workflow-gap-analysis.md`](workflow-gap-analysis.md)); legacy streams use small numbers (W1–W999) |
| `W<number><letter>` | W5A, W5B, W9A | Sub-workflow or variant of a parent (e.g. W5A Store Opening / W5B In-Store Selling under W5). Mostly used in the original (VS-01–VS-31) streams |
| `W<number>.<step>` | W7.2, W5B.4 | Reference to a specific step within a workflow (used in cross-references and the requirement-workflow matrix) |
| `PA-<VS>.<n>` | PA-07.1, PA-90.2 | Process Area file within a value stream folder |
| `VS-<number>` | VS-07, VS-124 | Value stream. Numbers 49–52 are intentionally retired (see [Value Stream Index](value-stream-index.md)) |

Workflow IDs are unique across the whole repository (not just within a value stream), so a `W`
number never needs a VS prefix.

> **Namespace rule for cross-references (validator Check 35).** A workflow is cited as
> `W<number>` (`W469`, `W289`); a process area as `VS-<VS>.<PA>` or `PA-<VS>.<n>`
> (`VS-03.4`, `PA-03.4`); a value stream as `VS-<number>` (`VS-88`) — and only value
> streams take a bare `VS-<n>` token. Writing a workflow number behind the VS prefix
> (e.g. "links to `VS-469` DTI", where W469 is the DTI-escalation workflow) produces a
> citation that resolves to no value stream; review #21 repaired 87 such instances and
> the check now fails on any recurrence.

---

## Repository Layout

```
workflows/
├── README.md                         Navigation hub & quick stats
├── value-stream-index.md              Master index (8 families · 188 VS · 569 PAs)
├── WORKFLOW-FORMAT-GUIDE.md           This file
├── workflow-gap-analysis.md           Gap-analysis methodology & workflow-ID allocation log
├── workflow-criticality-classification.md  Tier 1/2/3 priorities (5,456 confirmed rows; 0 post-catalog workflows keyword-proposed)
├── workflow-criticality-proposed.md      Keyword-driven tier proposal register (currently empty — 0 unclassified; regenerates via classify-workflows.py)
├── workflow-dependency-map.md         Prerequisite relationships, critical path
├── workflow-system-touchpoint-map.md  ERP module-to-workflow cross-reference
├── event-custody-and-precedence-register.md  Cross-cutting event routing (accountable VS · PAGASA signal ladder · incident command · enforced overlap pairs)
└── VS-<NN>-<slug>/
    ├── README.md                      Value-stream summary + PA list
    └── PA-<VS>.<n>-<slug>.md          Process area file containing the workflow blocks
```

---

## Related Documents

| Document | Purpose |
|---|---|
| [value-stream-index.md](value-stream-index.md) | Master index of all value streams and process areas |
| [workflow-criticality-classification.md](workflow-criticality-classification.md) | Tier 1/2/3 priority classification (confirmed) |
| [workflow-criticality-proposed.md](workflow-criticality-proposed.md) | Keyword-driven tier proposal register for unclassified workflows (companion; currently empty — 0 unclassified since the 2026-09-02 post-catalog confirmation) |
| [workflow-dependency-map.md](workflow-dependency-map.md) | Prerequisite relationships and critical path |
| [workflow-system-touchpoint-map.md](workflow-system-touchpoint-map.md) | ERP module-to-workflow cross-reference |
| [workflow-gap-analysis.md](workflow-gap-analysis.md) | Gap-analysis methodology and workflow-ID allocation log |
| [../requirement-workflow-matrix.md](../requirement-workflow-matrix.md) | Requirement-to-workflow traceability |
| [../internal-controls-matrix.md](../internal-controls-matrix.md) | 808 internal controls mapped to workflows and requirements |
| [../../07-methodology/validate-repo.sh](../../07-methodology/validate-repo.sh) | Consistency & boilerplate validator |

---

*Date: 2026-09-21 (batch 25 — ERP customization-governance gap fill: W5575–W5577 added in VS-113.1 — the customization decision record's intake and admissibility gate, the customization register's quarterly object-inventory audit, and the de-customization and extension-retirement programme — all three with all 9 required fields; completeness and 100%-presence figures re-pointed 5,427 → 5,430 and the layout row's confirmed-rows figure 5,450 → 5,453). Prior 2026-09-10 (batch 24 — concessionaire connectivity request, approval & independent-circuit governance gap fill: W5574 added in VS-07.1, extending the W177 concessionaire lineage with the owned exception path for a concessionaire wanting its own internet circuit — default posture (BuildRight-provided utility per W177 step 4/W111) restated, segmented Wi-Fi on the BuildRight link (W366 step 4) evaluated first, eligibility gate (documented regulatory/banking/capacity need), W5520/W5418-class isolation envelope, W47 works approval with landlord/LGU consent, W117 addendum with incident demarcation and VS-147 insurance, the commission-integrity clause keeping all sales on the BuildRight throughput SKU, and the W62-gated restoration holdback — ships directly confirmed Tier 2 — see the classification register v7.59; canonical totals now 5,427 workflows / 188 value streams / 569 process areas; completeness and 100%-field-header-presence claims re-pointed 5,426 → 5,427; confirmed-rows layout figure re-pointed 5,449 → 5,450. Prior 2026-09-05 (batch 23 — gas-leak, tsunami/storm-surge, media-exposé & server-room-environmental gap fill: W5570–W5573 added across VS-24.2/VS-26.1/VS-14.3/VS-27.2 — gas-leak event response with the odor-is-real law, ignition-source ban, trained-only two-person isolation and the detector-clear + source-disposition + ventilation reopen gate; tsunami & storm-surge coastal-intrusion response with the quake-is-the-warning law, move-up-not-out vertical evacuation, no-return-until-PHIVOLCS-cancellation and the salt-intrusion desalination gate; undercover-investigation & media-exposé response with the authentication-before-response law, no-obstruction rule, single-channel right-of-reply discipline and audit-tracked remediation; server-room & data-center environmental event response with the thermal-runaway clock, power-before-water rule, suppression re-arm discipline and RTO-bounded failover boundary — after the batch-16/17/18/19/20/21/22 edge-case sweeps were re-run across scenario families not yet probed (pre-ignition gas events at sites with LPG exchange cages, coastal water intrusion, genuine-fault investigative journalism, physical-room failures inside the IT estate); the same analysis produced the custody register's tenth wave, events E-46–E-49, v1.10; canonical totals now 5,426 workflows / 188 value streams / 569 process areas; completeness and 100%-field-header-presence claims re-pointed 5,422 → 5,426; all four ship directly confirmed Tier 1 (2) / Tier 2 (2) — see the classification register v7.58). Prior 2026-09-05 (batch 22 — terminal-tampering, procurement-impersonation, account-takeover & commute-disruption gap fill: W5566–W5569 added across VS-08.2/VS-03.2/VS-14.2/VS-141.2 — payment-terminal tampering & card-skimmer response with the freeze-in-place evidence rule, chain-wide fleet sweep and 24-hour acquirer-notification clock; procurement-impersonation & fake-PO goods-diversion response with the void-order posture, portal-only verification wave and receiving hold flags; official-channel account-takeover response with the first-hour credential kill-chain, platform-recovery appeal and unaffected-channel advisory; mass-commute disruption & transport-strike continuity with the critical-role matrix, no-penalty attendance coding and W4253-gated surge transport — after the batch-16/17/18/19/20/21 edge-case sweeps were re-run across scenario families not yet probed (payment-device compromise at the lane, fraudsters impersonating BuildRight as the buyer, takeover of BuildRight's own verified accounts, commute interruptions stranding crews at undamaged sites); the same analysis produced the custody register's ninth wave, events E-42–E-45, v1.9; canonical totals now 5,422 workflows / 188 value streams / 569 process areas; completeness and 100%-field-header-presence claims re-pointed 5,418 → 5,422; all four ship directly confirmed Tier 2 — see the classification register v7.57). Prior 2026-09-05 (batch 21 — storefront-crash, brand-impersonation-scam, wallet-outage & adjacent-works gap fill: W5562–W5565 added across VS-147.2/VS-100.2/VS-08.1/VS-20.3 — vehicle-impact & storefront-crash response with the crash-scene safety law, driver's-CTPL-first liability ordering and red-tag structural reopen gate; brand-impersonation commerce-scam response with the empathy-first victim-arrival protocol, single-source-of-truth advisory and simultaneous takedown wave; mobile-wallet platform outage response with one-tender-outage-canon-per-rail scope, directive tender flags and the stranded-authorization settlement sweep; third-party construction damage & adjacent-works response with the evidence-before-repair rule, red-tag safety gate and CAR/TPD-first claim ordering — after the batch-16/17/18/19/20 edge-case sweeps were re-run across scenario families not yet probed (vehicle impact into an operating store, brand-impersonation commerce scams, mobile-wallet provider outages, adjacent construction damaging occupied property); the same analysis produced the custody register's eighth wave, events E-38–E-41, v1.8; canonical totals now 5,418 workflows / 188 value streams / 569 process areas; completeness and 100%-field-header-presence claims re-pointed 5,414 → 5,418; the four ship directly confirmed Tier 1 (1) / Tier 2 (3) — see the classification register v7.56). Prior 2026-09-05 (batch 20 — cyber-extortion, payment-diversion, land-occupation & water-continuity gap fill: W5558–W5561 added across VS-27.3/VS-18.2/VS-178.1/VS-07.2 — ransomware & destructive cyber-attack enterprise response with the extortion-decision law, isolate-DR-before-failover sequencing and chain-wide manual trading mode; vendor payment-diversion & BEC fraud response with the same-day bank-recall race, honest-ledger treatment and cooling-off verification retrofit; informal-settler invasion of banked land with the 72-hour prescription-interruption evidence discipline, RA 7279 classification and no-self-help eviction rule; sustained water-service interruption response with the HSE-gated sanitation decision law, live-goods watering priority and flush-and-confirm recovery gate — after the batch-16/17/18/19 edge-case sweeps were re-run across scenario families not yet probed (destructive cyber attack with extortion, disbursement-diversion fraud, vacant-land occupation, utility-service failure beyond power); the same analysis produced the custody register's seventh wave, events E-34–E-37, v1.7; canonical totals now 5,414 workflows / 188 value streams / 569 process areas; completeness and 100%-field-header-presence claims re-pointed 5,410 → 5,414; the four ship directly confirmed Tier 1 (1) / Tier 2 (3) — see the classification register v7.55). Prior 2026-09-05 (batch 18 — channel-enforcement, employee-legal-status, OSH-enforcement & app-store-removal gap fill: W5550–W5553 added across VS-10.3/VS-19.1/VS-24.1/VS-75.1 — marketplace account suspension, enforcement freeze & appeal recovery; employee arrest/detention & criminal-case employment-status response; DOLE imminent-danger work-stoppage order response, abatement & reinstatement gate; mobile app store removal, policy-violation response & re-listing recovery — after the batch-16/17 edge-case sweeps were re-run across scenario families not yet probed; the same analysis produced the custody register's fifth wave, events E-27–E-29, v1.5; canonical totals now 5,406 workflows / 188 value streams / 569 process areas; completeness and 100%-field-header-presence claims re-pointed 5,402 → 5,406; the four ship directly confirmed Tier 1 (1) / Tier 2 (3) — see the classification register v7.53). Prior 2026-09-05 (batch 17 — regulatory-shock, platform-outage & governance-continuity gap fill: W5544–W5549 added across VS-36.1/VS-79.3/VS-08.1/VS-54.2/VS-24.1 — emergency executive succession & decision-rights continuity, BIR Oplan Kandado enforcement-closure response, eFPS/portal-outage filing contingency with AAB fallback & penalty-relief documentation, payment-network & acquirer outage response, stored-value & loyalty platform outage with downtime-acceptance & manual-redemption mode, and suicide/self-harm incident response & psychosocial aftermath — after the batch-16 edge-case sweep was re-run across scenario families not yet probed; the same analysis produced the custody register's fourth wave, events E-23–E-26, v1.4; canonical totals now 5,402 workflows / 188 value streams / 569 process areas; completeness and 100%-field-header-presence claims re-pointed 5,396 → 5,402; the six ship directly confirmed Tier 1 (2) / Tier 2 (4) — see the classification register v7.52). Prior 2026-09-05 (batch 16 — emergency & continuity workflow gap fill: W5536–W5543 added across VS-07.2/VS-24.2/VS-19.2/VS-18.3/VS-105.3/VS-118.2 — missing-child/Code Adam, fire event response & BFP clearance, bomb threat, elevator/escalator entrapment, payroll run failure & emergency off-cycle payment, bank-failure/frozen-deposit contingency, liquidity stress & payment-prioritization escalation, price-file integrity event & mass-mispricing rollback — after a dedicated edge-case gap analysis re-running the §2 methodology at *scenario* granularity; the same analysis produced the custody register's third wave, events E-19–E-22, v1.3; canonical totals now 5,396 workflows / 188 value streams / 569 process areas; completeness and 100%-field-header-presence claims re-pointed 5,388 → 5,396; all eight ship directly confirmed Tier 1 (3) / Tier 2 (5) — see the classification register v7.51). Prior 2026-08-26 (post-catalog batch 5 added — W5510 supplier service-fee billing & account deduction for store-rendered services: barcode labels & promotional collaterals (VS-15.1) — transposing the W5507 concessionaire service-fee pattern onto merchandise suppliers, settling via W770 debit memos netted at the W556 payment run with a co-op double-billing guard against W1799; canonical totals now 5,363 workflows / 188 value streams / 569 process areas; it ships unclassified with a keyword-driven proposed Tier 1 tier (the `barcode` keyword, W5507 precedent), joining W5497–W5509 in the 14-row proposal register). Prior 2026-08-26 (post-catalog batch 4 added — W5508 fringe benefits tax determination, valuation & quarterly BIR 1605 filing (VS-79.2) and W5509 unfulfilled-demand & lost-sales capture, substitution analytics & replenishment feedback (VS-02.1) — after re-running the gap methodology at workflow granularity; canonical totals now 5,362 workflows / 188 value streams / 569 process areas; the two ship unclassified with keyword-driven proposed Tier 1 tiers, joining W5497–W5507 in the 13-row proposal register). Prior 2026-08-25 (consistency review #28: five current-state figures re-pointed — required-fields completeness claim and 100%-field-header-presence claim 5,357 → 5,360, Repository Layout and Related Documents proposed-register rows 8 / W5497–W5504 → 11 / W5497–W5507 — drift left by the post-catalog batches; now guarded by validator Checks 44–45). Prior 2026-08-25 (post-catalog batch 3 added — W5505–W5507, inside VS-07.1, extending W177 with concession item catalog/barcode/price-label governance, concessionaire self-service price change request/approval & label-first propagation, and concession service-fee billing & cost recovery — after re-running the gap methodology at workflow granularity; canonical totals now 5,360 workflows / 188 value streams / 569 process areas; the three ship unclassified with keyword-driven proposed tiers (W5505/W5507 proposed Tier 1 on the `barcode` keyword, W5506 Tier 2), joining W5497–W5504 in the 11-row proposal register). Prior 2026-08-25 (batch 2): two further post-catalog workflow-level gap fills added — W5503 restricted-substance & chemical-content product compliance (VS-31.3) and W5504 extreme-heat work interruption & occupational heat-stress management (VS-24.1) — after re-running the gap methodology at workflow granularity; canonical totals then 5,357 workflows / 188 value streams / 569 process areas; the two ship unclassified with keyword-driven proposed Tier 2 tiers, so the Repository Layout and Related Documents rows for workflow-criticality-proposed.md then described an 8-row register. Prior 2026-08-24: six post-catalog workflow-level gap fills added — W5497–W5502, inside VS-84.2/VS-19.3/VS-36.1/VS-10.1/VS-21.2/VS-83.3 — after re-running the gap methodology at workflow granularity; canonical totals then 5,355 workflows / 188 value streams / 569 process areas; the six ship unclassified with keyword-driven proposed tiers, so the Repository Layout and Related Documents rows for workflow-criticality-proposed.md then described a 6-row register. Prior 2026-08-24: Naming Conventions gained an explicit namespace rule for cross-references — workflows are cited `W<number>`, process areas `VS-<VS>.<PA>`/`PA-<VS>.<n>`, and only value streams take a bare `VS-<n>` — after review #21 repaired 87 workflow references written in the VS namespace across 25 PA files, now guarded by validator Check 35. Prior 2026-06-28: workflow-criticality-proposed.md descriptions aligned to the register's current state — the Repository Layout diagram row and the Related Documents row now carry the 'currently empty (0 rows)' marker with the repopulation note; same repair in workflows/README.md and the root README tree; validator Check 28 Part B now guards the descriptions. Prior 2026-06-27: required-field completeness achieved — Participants backfilled from Steps roles via `backfill-participants.py`; System Touchpoints + Pain Points authored for VS-15–18/27/31–40/48; Check 22 green across all 5,349 workflows. Prior 2026-06-26: stale proposed-count figure `2,564` → `2,596` corrected in the Repository Layout diagram — drift from the 2026-06-25 PA-127.4 regeneration of `workflow-criticality-proposed.md`. 2026-06-25: VS-127 PA-127.4 added — 8 workflows, W5489–W5496 — specializing the S&OP/IBP consensus cycle for BuildRight's PH-retail context; totals now 5,349 workflows / 188 value streams / 569 process areas. Prior 2026-06-21: Pass 30 added VS-192 Green Fleet Transition — 24 workflows — bringing totals to 5,341 workflows / 188 value streams / 568 process areas; the family-subtotal, grand-total, and criticality-proposed coverage line are reconciled. Prior 2026-06-20: adoption sentence in “Standard analysis fields” corrected to 100% of all 5,317 workflows after reformatting W641–W647. Repository Layout counts reconciled to 188 value streams / 568 process areas / 2,588 proposed; `README.md` (navigation hub) added to the layout diagram so it lists all 8 support files; classified-register reconciliation note aligned with workflow-criticality-classification.md)*
