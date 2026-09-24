# Operations Workflow Gap Analysis — BuildRight Depot Corp.

> Focused gap analysis of the **operations-facing workflow families** — Plan & Source, Make & Move,
> Sell & Serve, Asset & Infrastructure and Governance & Assurance — performed per the methodology in
> [workflow-gap-analysis.md](workflow-gap-analysis.md) §2 (defining-term keyword search across all
> PA files to distinguish *dedicated* coverage — a `## W` header that owns the capability — from
> *incidental* single-step references). Companion to the canonical thirty-pass gap history and to
> the batch-8/9/10 domain companions ([workflow-gap-analysis-it.md](workflow-gap-analysis-it.md),
> [workflow-gap-analysis-people.md](workflow-gap-analysis-people.md),
> [workflow-gap-analysis-finance.md](workflow-gap-analysis-finance.md)); this document does **not**
> amend that record. **Status (2026-09-04): adopted.** All three gaps were confirmed and filled as
> workflows **W5532–W5534**, allocated in
> [workflow-gap-analysis.md](workflow-gap-analysis.md) batch 11 and confirmed into the criticality
> register (2 × Tier 2, 1 × Tier 1).

---

## 1. Scope

All workflows in the five workflow-level families not yet covered by a dedicated domain pass
(IT = batch 8, People = batch 9, Finance = batch 10), across:

- **Plan & Source** — 462 workflows in 15 value streams (VS-01/02/03/41/45/57/64/67/94/101/106/122/127/131/182).
- **Make & Move** — 500 workflows in 19 value streams (VS-04/05/06/32/56/61/74/81/90/92/93/110/111/136/143/155/180/191/192).
- **Sell & Serve** — 1,546 workflows in 46 value streams (VS-07/08/09/10/11/12/13/14/37/43/44/46/47/48/53/55/58/60/62/63/65/66/70/75/77/78/82/95/107/124/139/140/145/149/156/162/164/168/171/172/174/175/176/177/185/186).
- **Asset & Infrastructure** — 323 workflows in 13 value streams (VS-20/35/42/59/97/108/109/112/120/138/163/178/184).
- **Governance & Assurance** — 977 workflows in 37 value streams incl. **VS-23 Loss Prevention & Asset Protection** (VS-21/22/23/24/25/26/31/33/36/69/71/73/76/85/86/87/88/89/91/100/104/114/117/119/129/130/132/133/146/147/152/159/161/165/166/179/187; includes this pass's W5534).
- **Cross-family hosts touched by the gaps**: VS-19.3 (People — workforce management) and
  VS-79.2 (Finance — withholding tax), because the capabilities the gaps describe are executed
  inside operations but owned on those PA boundaries.

## 2. Method

1. **Inventory** every `## W` header in the five families (≈3,808 workflows) plus the
   cross-family hosts above.
2. **Map** each capability of a reference retail operating model — merchandising & sourcing,
   supply chain & logistics, store & DC operations, loss prevention & safety, facilities & asset
   management, workforce field operations, governance & compliance — to the owning workflow(s).
3. **Flag** capabilities with no owning workflow, thin-partial coverage, or scattered ownership,
   prioritizing the three recurring gap signatures from batches 8–10: (a) a *platform cited only
   as infrastructure* but never operated (the M365/LMS class), (b) a *statutory layer computed
   and filed around but never named* (the MCIT/PFRS 8 class), and (c) a *control lifecycle every
   adjacent owner assumed was somebody else's job* (the utility-deposits class).
4. **Validate** each candidate gap by keyword search across all PA files; discard false positives
   and near-misses (§5).

## 3. Current-State Coverage Map (confirmed covered — no gap)

| Operations Capability | Owner workflow(s) | VS / PA |
|---|---|---|
| DC yard & dock: container yard, dock scheduling, gate/visitor control, unscheduled deliveries | W222, W585, W745, W1478, W3C.5-class protocol | VS-04.1/.3, VS-23.2 |
| Warehouse equipment: forklift/MHE preventive maintenance, loading-dock equipment, daily checks | W650, W240, W1403, W1021, W1015, W4973 | VS-04.3, VS-20.3, VS-07.2 |
| Inter-store / inter-DC stock balancing & transfers | W154, W204, W218, W1423, W500 (in-transit claims) | VS-02, VS-05 |
| Trailer logistics: inter-island RoRo bookings, haulage, demurrage/detention | W66, W1164/W1169, W249, W3509 | VS-04.1, VS-06.1 |
| Yard overflow storage: outdoor lumber/building-materials yard | W3B, W1247 | VS-04.1, VS-23.2 |
| Cardboard baling & recycling revenue | W1564 (weekly baling operation) | VS-20.3, VS-73 |
| Elevator/escalator & building-systems servicing | PA-07.2 PM table (monthly contractor + annual DOLE-accredited inspection), W47, VS-138 hard-services catalog | VS-07.2, VS-138.1 |
| Marketing paid-media planning & buying (traditional + digital) | W83 (step 12 media-buying agency coordination), W676, W677, W1559 | VS-14.1/.2 |
| Retail media network (vendor-funded) | W153, W286, W1998–W2013 | VS-14.3, VS-48 |
| Email/CRM campaign, social, influencer, SEO, review management | W1350, W142, W1184, W563, W1560, W736 | VS-14.2 |
| Wage-order monitoring & pay-structure adjustment | PA-102.1 wage-order-triggered workflow (DOLE/RTWPB) | VS-102.1 |
| Corporate secretarial & SEC records | W2987, W1719, W1714–W1716 (board mechanics), W243 (POA/board resolutions), W1731–W1734 | VS-100, VS-102, VS-36 |
| OSH program & committee | W512 (committee operations), W436 (WAIR/AMR statutory reporting), W4973 (DOLE OSH accreditation) | VS-19.3, VS-24.1 |
| Business continuity & drills | W158, W49, W1204, W1392, W4191, W582 | VS-21, VS-24.2, VS-07/27 |
| Regulatory compliance calendar | W506 (unified calendar & dashboard) | VS-22 |
| Key & credential control; DC gate & visitor management | W1477, W1478 | VS-23.2 |
| Inter-store cash & float; petty cash; cash office | W2815, W25/W1343/W1467/W1688, W541/W2801 | VS-81, VS-34, VS-08 |
| Customer complaints & DTI escalation | W41, W597, W740, W1116, W1907, W469/W2904 | VS-13, VS-07 |
| Layaway & customer deposits | W75, W826, W94, W4630 | VS-13, VS-16, VS-54 |
| Failed delivery & redelivery handling | W4302, W500 | VS-143, VS-05 |
| Product recalls & safety incidents | W1615–W1617, W1347, W1562, W1566 | VS-31, VS-14.3, VS-24, VS-147 |
| Product photography & media production | W4154 (image & media production lifecycle) | VS-137.2 |
| MRO & facilities spares; repair dispatch | W188, W3237, W5088, W1348 | VS-04.3, VS-99, VS-186 |
| Statutory benefits remittance & consolidation | W1527, W1306, W251 | VS-19.2 |
| Time & attendance exceptions; scheduling; OT governance | W561, W594, W34, W1357, W1032, W753, W796, W1241 | VS-19.3, VS-04.3 |
| Fuel, fleet & telematics | VS-61, W199, W1348, W5476 | VS-06, VS-61 |
| Anti-money laundering (financial-agency ops) | W730, W961, W5208 | VS-156, VS-181 |

## 4. Gaps Identified

### G1 — Workforce time-&-attendance (biometric/time-clock) platform estate & punch-data operations — **MEDIUM**

The corpus runs attendance *operations* end-to-end — W561 manages ~800–1,200 exceptions/day from a
"biometric/attendance system", W594 verifies daily attendance, W34/W1357 build the shift plans the
punches are reconciled against, W586/W796 extract "timekeeping" as a labor-metrics data source, and
new-store readiness requires "biometric system installed" — but the **platform itself has no owner**.

- **Evidence (dedicated-header hits / defining terms):** 'time and attendance'/'timekeeping'/
  'biometric' **38 PA files / ~130 hits with zero dedicated `## W` headers** (the only header
  containing "biometric" is W5257 — the DTS *student* monitoring workflow in VS-183);
  'biometric device'/'fingerprint scanner' **0**; 'payroll interface'/'payroll file' **0 dedicated
  headers**. The batch-9 LMS signature exactly: an adjacent HR-platform owner exists (W3351 owns
  the HRIS *core-HR*; W561/W594 own exception *processing*) but no one operates the ~420–450-device
  estate, its punch-data payroll interfaces, its offline-outage fallback, or its provisioning on the
  site/employee lifecycle.
- **Why it matters:** ~3.2–3.6M punch events/year feed the W10/W816 payroll of 6,911 employees —
  silent interface failure at a cut-off stalls pay for the whole company; devices fail unseen in hot,
  humid, dust-exposed back-rooms; typhoon/power outages break capture exactly when emergency staffing
  matters; and biometric templates are RA 10173-sensitive data whose separation deletion is currently
  nobody's step. DOLE labor-standards evidence (hours worked, OT authorization) hangs off the same feed.
- **Proposed disposition:** 1 workflow in **PA-19.3** — *"Workforce Time & Attendance
  (Biometric/Time-Clock) Platform Estate & Punch-Data Operations"* (device registry & heartbeat
  monitoring, payroll interface reconciliation, offline fallback, lifecycle provisioning, retention &
  DOLE-evidence governance).

### G2 — BIR Form 2316 annual issuance, employee acknowledgment & certificate lifecycle — **HIGH** (statutory)

Every employee must receive BIR Form 2316 (Certificate of Compensation Payment/Tax Withheld) by
**January 31** of the following year — and the corpus generates the certificates and files around
them without ever owning the campaign.

- **Evidence:** '2316' appears in **10 PA files / 22 hits with zero dedicated `## W` headers**.
  Generation exists only as sub-steps: W90.8 bundles 2316 into a "tax certificate generation"
  step budgeted at ~2 hours/month, W1384.7 notes 13th-month inclusion, W43 references tax
  documents "per W643" at separation, and the ESS portal lists "view and download BIR Form 2316
  annually" as a portal capability (W3330-class). W2764 owns the monthly 1601C remittances and
  W2765 the annual 1604E/1604C + alphalist — but the furnishing campaign to ~6,911 employees, its
  acknowledgment evidence, and its reconciliation to those filings are unowned.
- **Why it matters:** statutory furnishing dependency (the W5508 precedent — statutory-execution
  class → Tier 1); a 2316 file that doesn't tie to the 1604C/alphalist is the standard first BIR
  examination finding (W77's defense surface); ~93–95% of employees are store/DC staff requiring a
  printed-distribution logistics exercise; separation 2316s gate final-pay releases (W643) and feed
  the W2972 financing-desk evidence demand.
- **Proposed disposition:** 1 workflow in **PA-79.2** — *"BIR Form 2316 Annual Issuance, Employee
  Acknowledgment & Certificate Lifecycle"* (year-end assembly & reconciliation to W2764/W2765,
  generation & QC, ESS + printed distribution with acknowledgment gates, separation/interim
  issuance, corrections, deadline-evidence archive).

### G3 — Company-property gate pass & asset-exit control (stores, DCs & HQ) — **MEDIUM**

Cycle counts cover merchandise; nothing covers the company's own assets crossing a premises exit.
The corpus shows every ingredient of the control and its absence at the same time.

- **Evidence (dedicated-header hits / defining terms):** 'gate pass'/'property pass' **5 PA files /
  7 hits with zero dedicated `## W` headers** — W585 issues gate passes to inbound *trucks* at DC
  gates, PA-09.1's fabrication workflow expects a "Gate Pass Integration (Security exit clearance)"
  system integration, and the corpus's other "gate pass" hits are the BOC port gate pass (import
  side, W239-class) or the *customer's* gated-community access. W1477 owns keys/credentials,
  W1478 the DC perimeter & *visitor* management, W3239 asset retirement, W5088 repair-vendor
  coordination — nobody owns the **property-exit control** binding them.
- **Why it matters:** ~8,000–12,000 asset movements/year cross ~205 store + 4 DC + HQ exits
  (repair dispatches, inter-site transfers, IT-asset moves, customer bulky releases, e-waste
  removals, vendor tool sign-outs) with no unified numbered-pass control; repair-vendor leakage and
  "disappearing equipment" are the classic fixed-asset shrinkage blind spot that stock-count-based
  LP programs (W845's merchandise scope) structurally cannot see.
- **Proposed disposition:** 1 workflow in **PA-23.2** — *"Company-Property Gate Pass & Asset-Exit
  Control (Stores, DCs & HQ)"* (numbered-pass issuance & authority-matrix approvals, exit
  verification incl. invoice tie-out for customer releases, return-window escalation, one-way
  disposal/transfer document control, monthly reconciliation, W1174 audit sampling).

## 5. Thin-Partial Coverage (monitor; no immediate new workflow required)

| Topic | State | Note |
|---|---|---|
| DC trailer yard / drop-trailer pool / yard jockeys | 'yard jockey'/'drop trailer'/'live unload' = **0 hits** | The operating model runs live-unload with scheduled dock appointments (W585) and container yards (W222); no trailer-pool discipline exists to own. Revisit only if drop-trailer operations are introduced |
| Elevator/escalator servicing lifecycle | PM table row in PA-07.2 + VS-138 hard-services catalog | Owned as part of generic facility maintenance; the accessibility workflow (PA-07.2) handles elevator capital works |
| Corporate secretarial residual (secretary's certificates, bylaws/STB custody) | W2987 owns SEC records & inspection support; W1714–16 board mechanics; W243 POA/board resolutions | The role is referenced ~331× but the residual custody items are thin; monitor at the next VS-100 review |
| Office print fleet / managed print services | Copiers appear only as PFRS 16 embedded-lease examples; W241 owns HQ facilities maintenance | HQ-centric, low volume; monitor |
| Toll/RFID (Autosweep/Easytrip) reconciliation | 2 incidental hits | Rides VS-61 fleet cost management; monitor if toll volume grows |
| Denied-party / sanctions screening (imports) | 2 hits; W5208 covers sanctions for project onboarding | Philippine-import relevance is low; monitor trade-compliance scope |
| Sponsorship/donation solicitation intake | VS-152 owns the CSR program end-to-end (W4518 drives, W4520 in-kind, W4525 stakeholder engagement) | Inbound request pipeline rides the program workflows; monitor volume |
| Marketing-automation platform beyond W1350/W736 | CDP (VS-126) + W1350 email + W736 data platform own the stack | No separate MA-platform owner warranted at current scale |

## 6. Summary

| ID | Gap | Priority | Proposed home | Proposed workflows | Status (2026-09-04) |
|---|---|---|---|---|---|
| G1 | Workforce T&A (biometric/time-clock) platform estate & punch-data operations | Medium | PA-19.3 | 1 | **Adopted — W5532** (Tier 2) |
| G2 | BIR Form 2316 annual issuance, acknowledgment & certificate lifecycle | High (statutory) | PA-79.2 | 1 | **Adopted — W5533** (Tier 1) |
| G3 | Company-property gate pass & asset-exit control | Medium | PA-23.2 | 1 | **Adopted — W5534** (Tier 2) |
| | **Total** | | | **3 workflows** | **3 shipped: W5532–W5534** |

**Overall verdict:** the operations families are the oldest and deepest in the corpus — thirty
gap-analysis passes plus ten workflow-level batches have left no unowned *capability* in
merchandising, supply chain, store, DC, fleet, facilities or LP operations. What remained were the
same three residual classes batches 8–10 found elsewhere: a **platform operated by implication**
(G1 — the attendance estate every exception workflow reads from), a **statutory layer generated
around** (G2 — the 2316 furnishing inside W90's two-hour monthly step), and a **control lifecycle
with no owner** (G3 — the property gate pass PA-09.1 expects as a system integration). Filling the
three gaps added **3 workflows (~0.08% growth to the covered families)** and closed every unowned
capability surfaced by this analysis. VS-19 now stands at **81 workflows** (PA-19.3: 12), VS-79 at
**28** (PA-79.2: 10) and VS-23 at **29** (PA-23.2: 10).

---

*Methodology note: candidate gaps surviving keyword validation follow §2 step 4 of
[workflow-gap-analysis.md](workflow-gap-analysis.md). The adoption was recorded there as batch 11
(workflow-ID allocation W5532–W5534), with criticality tiers confirmed (1 × Tier 1, 2 × Tier 2)
in [workflow-criticality-classification.md](workflow-criticality-classification.md).*
