# Quote Coverage Review — 8-Scenario License RFQ vs the Model-Company Footprint

> **Purpose:** register the functional-coverage audit of the send-to-Oracle RFQ
> [`../../erp_compare_infor/oracle-quote-license-bom-8-scenarios.md`](../../erp_compare_infor/oracle-quote-license-bom-8-scenarios.md)
> (E1–E4 EBS · F1–F4 Fusion, go-live Jan 2028 — the Infor-WMS × HRMAX retention matrix) against
> this folder's adopted footprint: [`licensing-bom.md`](licensing-bom.md) v2.1,
> [`fit-gap-analysis.md`](fit-gap-analysis.md) §4 resolutions 9–34, and
> [`module-coverage-map.md`](module-coverage-map.md) v2.0. Every gap carries a disposition, and
> the RFQ's **v2 amendment** (its own version footer) implements the CLOSED resolutions in
> place. Companions: the RFQ's doctrine companion
> [`../../erp_compare_infor/golive-licenses-ebs-fusion-8-scenarios-v2.md`](../../erp_compare_infor/golive-licenses-ebs-fusion-8-scenarios-v2.md)
> already adopts metric rules R1–R7 from [`licensing-bom.md`](licensing-bom.md) — this review
> closes the functional gaps the v2 companion's restatement did not carry.
>
> **Verdict (pre-amendment):** the RFQ handled the T1 core, the full HR block on both platforms
> (9-product EBS HRMS / 6-product Fusion HCM at the full Employee metric), the WMS/HCM
> retention-vs-replace mechanics, the conservative INV/MSCA stacking (R2/R3) and the payroll
> exclusion consistently with this repo — but **5 repo-adopted EBS products were silently
> absent (G1–G5)**, **5 were excluded by a blanket out-of-scope note that conflicts with
> adopted workflows (G6–G10)**, **5 Fusion parity lines were missing (G11–G15)**, **WMS labor
> management sat in the optional swing (G16)**, and **$887,920 list of repo-required EBS
> products sat in the optional select-at-PO swing tier — a doctrine-R1 violation (G17)**.

---

## 1. Method

Each product line in the RFQ's four EBS sheets (E-COMMON, E-WMS, E-HR, E-SWING) and four Fusion
sheets (F-COMMON, F-WMS, F-HCM, F-SWING) was matched against the adopted-product set this repo
derives from the 728 requirements / 5,433 workflows / 808 controls: the licensing-BOM line
items (§2.1–§2.10, §3.1), the fit-gap register's 97 rows and §4 resolutions 9–34, and the
coverage-map realization register. A gap is any repo-adopted product with no RFQ line, an RFQ
line priced in a non-committed tier, or a blanket exclusion touching an adopted workflow
family. Quantity divergences against the model-company drivers are registered separately
(§4) — the RFQ prices the real company at go-live (155 stores, actual role mapping) while this
repo canonizes the 200-store steady state, so quantity deltas are reconciliation items, not
coverage failures.

## 2. Coverage register

| ID | Requirement (repo anchor) | RFQ v1 disposition | RFQ v2 resolution | Status |
|---|---|---|---|---|
| **G1** | Electronic Order Line — ecommerce order import via OM (licensing-bom decision 1, §2.2; ~515K orders/yr ≈ 2.5M lines; VS-10/60/65/93/95) | **Absent** — Q3 asked only about POS→AR exposure | Added EBS line 50 (L10128, 2.5M ⚠ repo canon) + Fusion line 46 (B111914, 20 blocks); sizing question Q11 | **CLOSED** (sizing ⚠ Q11) |
| **G2** | Lease & Finance Management (A13 — fit-gap first pass; lessor leasing VS-96 + rental family VS-162/174/186) | **Absent silently** (not even in the out-of-scope note) | Added EBS line 51 (8 AU, † price); adopt/de-scope confirmation Q14 | **CLOSED** (decision Q14) |
| **G3** | Services Procurement (licensing-bom §2.4, 50 AU; contingent workforce VS-98 — in tension with fit-gap resolution 24, which adopted Purchasing contingent labor B13 riding the Purchasing base) | **Absent silently** | Added EBS line 52 (L31820, 50 AU) marked creditable if Oracle confirms the B13 entitlement covers VS-98 — question Q13 | **CLOSED** (verify Q13) |
| **G4** | Advanced Scheduler (licensing-bom §2.6 field-scheduling option) | **Absent silently** | Added EBS line 53 (40 FT — the RFQ's own technician canon; repo sized 100 at 200 stores) | **CLOSED** |
| **G5** | In-Memory Cost Management (C15 — fit-gap resolution 18; margin analytics W85/W633/VS-101) | **Absent silently** | Added EBS line 54 (15 AU, † price) | **CLOSED** |
| **G6** | Oracle Configurator (C16 — fit-gap resolution 16; in-store fabrication quoting, W1009 family: W943/W944/W946/W986/W988/W1045/W1054/W1059/W1046) | **"Confirmed out of scope"** — conflicts with the adopted register row | Replaced blanket note with priced PD-1 (L11093, 200 AU ⚠ repo canon); Fusion fallback CPQ B111751 named; decision Q14 | **OPEN — decision** |
| **G7** | Teleservice / Service Requests + Escalation (D14 — fit-gap first pass; complaint SRs W41, VS-13.1) | **"Out of scope (no install-base service business)"** | Priced PD-2 (A85666, 50 AU); Q12 tests the Field Service foundation dependency | **OPEN — decision** |
| **G8** | Install Base + Service Contracts (D16 — fit-gap resolution 22; warranty records of record, VS-53/W33/W544/VS-155) | **Out of scope** (same note) | Priced PD-3 (A92483, 15 AU); Q12 | **OPEN — decision** |
| **G9** | Depot Repair (D17 — fit-gap resolution 23; in-house repair/refurbish orders W440/W544, VS-155 refurbish-before-resale) | **Out of scope** (same note) | Priced PD-4 (A85565, 25 AU); Q12 | **OPEN — decision** |
| **G10** | Project Billing (licensing-bom §2.7, 15 AU; retention/milestone billing W165 — VS-11, PA-11.2) | **"Out of scope (no external project billing)"** — but W165 is trade-project retention billing, not external billing | Priced PD-5 (L31923, 15 AU); adopt or re-route W165 via OM milestone invoicing — Q14 | **OPEN — decision** |
| **G11** | Fusion Global Order Promising (D15 parity — repo Fusion BOM line; W56/W1114/W3097 promising) | **Absent from F-COMMON** (EBS side correctly defers to OM-embedded ATP + custom quote) | Added committed line 43 (10 HNU @ $425 TBD†); pricing Q15 | **CLOSED** (price †) |
| **G12** | Fusion Revenue Management (A11 parity — PFRS-15 multi-element schedules, VS-47/VS-157; EBS swing line 41 existed) | **Absent on the Fusion side** | Added committed line 44 (6 HNU @ $150 TBD†); Q15 | **CLOSED** (price †) |
| **G13** | Fusion Quality Management (C12 parity — incoming inspection/CAPA, VS-31/VS-89) | **Absent on the Fusion side** | Added committed line 45 (10 HNU @ $200 TBD†, RFQ's Quality canon); Q15 | **CLOSED** (price †) |
| **G14** | Field Service Cloud (D13 parity on Fusion — repo Fusion BOM line B110413; installation dispatch VS-12) | **Absent**; §4 acknowledged the gap ("floor-bound") without pricing a line | Added committed line 47 (360 Pooled NU ⚠min floor = $81,000/mo ≈ ₱33.6M/yr); floor-relief question Q15 | **CLOSED** (relief Q15) |
| **G15** | Fusion Transportation Management (freight audit — VS-110, PA-15.1; EBS shapes carry OTE inside the OM base, Fusion shapes had nothing) | **"Out of scope (transport stays with warehouse decision)"** | Priced as PD under the F-PARITY block (25 HNU @ $650 TBD† ≈ ₱6.7M/yr); decision Q14 | **OPEN — decision** |
| **G16** | WMS Labor Management parity on Fusion (repo C6/W796 — engineered standards, real-time productivity) in the WMS-replaced shapes F2/F4 | Priced only as swing (`WWM` B90537, ₱9.0M/yr) — not selecting it silently drops an adopted C6 surface | Re-tiered **committed in F2/F4**; swing remainder restated (₱76.1M/yr common + ₱4.1M/yr WMS Automation) | **CLOSED** |
| **G17** | Doctrine R1 (adopted = licensed at go-live — licensing-bom decision 5 / v2 companion rule R1) | **$887,920 of adopted EBS products** (Treasury A8, Credit Mgmt D3, RM&I A11, iReceivables A14, ICM H11, Quality C12, Site Hub C3 ×3, SLM B6, Project Mgmt) sat in the optional select-at-PO swing | RFQ section 2.4 renamed **E-SCOPE**, re-tiered committed; section 2.5/4 totals restated so committed = former max (plus closure lines); the select-at-PO mechanism survives only for genuinely optional Fusion lines and the PD block | **CLOSED** |

**Aligned and sound (no action):** the Financials spine and AR instruments via base entitlements
(Bills Receivable/Lockbox/Balance Forward Billing ride Financials — R6); the procurement family;
INV/WMS/LCM with the conservative stacking and LMS credit-back questions (Q1/Q2); the full HR
blocks both platforms (Employee-metric 7,247 ≥ the 6,911 canon); payroll excluded on both
platforms (decision 2 / E5); floors register (Q5); part-# verification (Q6); payroll GL
integration (Q7); Site Hub vs TCA (Q8); bundle rejection rationale (Q9); Fusion additions this
repo lacked (GTM for VS-87 customs, Risk 188, FRC, OIC, Analytics, EPM, test env, storage); the
technology-tier deferral (EE + RAC + ADG + Partitioning) consistent with licensing-bom §2.12.

## 3. What the RFQ prices that this repo does not require

For completeness — additions the RFQ carries beyond the repo BOM (kept; they are cheap or
operationally sensible, none contradicts the doctrine): Application Management Suite (200 NUP),
Load Testing Suite, Fusion Accounting Hub swing (RedBox→GL formalization), WMS Automation swing,
AI-agent swing lines, Workforce Scheduling / Labor Optimization / H&S / Help Desk / Communicate
swing (the repo retains store scheduling in-house — swing pricing keeps the option open without
committing), HCM Analytics.

## 4. Quantity reconciliation — the store-operating-model divergence (Q10)

The RFQ prices a **backroom-only, non-RF store model** (v2 companion §1: "store side stays
non-RF in all 8 permutations"; store selling floor never touches ERP — POS). This repo's canon
is **12 ERP users per store plus store RF receiving** (profile §12.1: 2,400 store ERP users;
licensing-bom §2.3: 2,000 store MSCA RF users). The divergence is documented, not an error —
but it is the single largest quantity swing in the whole comparison, and Q10 correctly asks
Oracle LMS to validate it:

| Driver | RFQ go-live (Jan 2028) | RFQ 2030 rider | Repo canon (200-store steady state) | Lines affected |
|---|--:|--:|--:|---|
| Stores | 155 | 200 | 200 | all AU-metric lines |
| Total employees (Employee metric) | 7,247 | 9,271 | 6,911 | HR/HCM blocks (RFQ ≥ canon — conservative ✓) |
| DC execution workforce | 289 | ~373 | 600 (4 DC × 150) | WMS/WWM/AIM/INV/MSCA stacking |
| Store ERP users | backroom-only, inside INV 844/1,133 | grows with stores | 2,400 (12/store) + 2,000 store RF | INV, MSCA, iProcurement, Purchasing, iExpenses |
| SKU master (Product Hub records) | 30,000 ⚠min 20,000 | grows | 55,000 records / 35,000 active | line 24 |
| Annual COGS (LCM) | $1,171M | true-up | $750–800M | line 12 (RFQ conservative ✓) |
| Field technicians | 40 licensed (of 136 HC) | — | 100 | lines 22/23, 53 |
| Ecommerce order lines | not stated | — | ~2.5M/yr (515K orders) | lines 50/46 — sized to repo canon ⚠ Q11 |

Starkest per-product deltas if the store model ever converges to the repo canon: INV 844/1,133
vs 3,600 · MSCA 289 vs 2,700 · iProcurement 100 vs 1,850 · Purchasing 43 vs 700 · eAM 12 vs 60
· SS Work Requests 20 vs 250 · Quality 10 vs 40 · BOM/WIP 14 vs 50 · Project Costing 10 vs 60 ·
Sourcing 5 vs 40 · Property Manager 8 vs 15 · iSupplier 5 vs 10. Every AU line true-ups
annually (RFQ §5), so the exposure is a re-quote, not a compliance gap — but the architecture
decision (RF-capable stores or not) should be recorded before the PO.

## 5. Metric & part-# verification items (fold into RFQ Q6)

1. **Internet Expenses metric conflict:** the RFQ prices the **Expense Report** metric
   (7,250 reports @ $6, min 1,000); licensing-bom §2.4 carried the **Application User** metric
   (700 @ $115, TBD†). Both cannot be right against the current GPL — the RFQ's reading is
   plausibly the current-GPL one; the repo row trues at its next pass. Verify at quote.
2. **† lines needing part #/price:** Discrete Mfg bundle (line 6), AMS (line 13), L&FM (line
   51), In-Memory Cost (line 54), Credit Mgmt/RM&I/ICM/Quality/Project Mgmt (as before), and
   Fusion parity lines 43/44/45 + TMS PD. *RFQ v2.0.2 status (2026-09-18): six of these resolved
   on the September 10, 2026 EBS GPL — Discrete Manufacturing A81412, AMS L93139, L&FM L10090
   (re-metric'd to the GPL managed-asset SKU, qty TBC pending our managed-asset figure, excluded
   from totals), In-Memory Cost L98184 (trued to $25,000/user, min 25 — qty 15, $625,000), Load
   Testing L107647, Internet Expenses A85655; the TBC set shrinks to Credit Mgmt, RM&I, ICM,
   Oracle Quality and Project Management (not on the EBS GPL) plus Fusion GOP/Revenue
   Management/Quality Management.*
3. **ICM on 12.2.12** — availability check stands (Vision-instance findings, VF register).
4. **PD block pricing** is repo-canon sizing (200-store CZ users; 50/15/25 service users) —
   resize to the actual operation when the section-6 decisions land.
5. **Asset Tracking rider entitlement (2026-09-23 GPL sweep — coverage register §7 / fit-gap
   resolution 37):** the no-line treatment rides decision 6, but the GPL sells Asset Tracking
   separately (`L11496` @ $6,895/AU, min 50 ⇒ ~$344,750) — confirm the Install Base/Inventory
   entitlement at quote, or add the line.
6. **Supplier Ship and Debit + the QP EOL component (same sweep):** `L72211` ($3,000/AU min
   20) is unlicensed while EDC-10/B10 name the accrual-offer mechanism — confirm it rides the
   licensed `L72178` base + Advanced Pricing; and confirm QP-modified ecommerce order lines
   consume only the OM EOL metric (`L10128`), not the QP-family component (`L31659`).
7. **Product Hub Add-on and the `L72189` scope (same sweep):** confirm whether the licensed
   Product Hub (`L42168`) requires the add-on (`L42175` — the Site Hub precedent licenses
   `L69447`), and which scope the Channel Rebates & POS Management option carries against
   coverage register §5's not-needed record of the same-named product.

## 6. Decisions required (the PD register — no silent drops)

| # | Decision | RFQ vehicle | Repo anchor | Owner |
|---|---|---|---|---|
| D-1 | In-store fabrication quoting: adopt Configurator CZ or de-scope (Fusion fallback CPQ B111751) | PD-1 / RFQ section-3.4 note | C16, W1009 family | Store Ops + IT |
| D-2 | Service family: adopt TeleService/Service Contracts/Depot Repair for W41 complaints, VS-53 warranty, VS-155 refurbish — or record the re-homing (build/POS side) | PD-2/3/4 | D14/D16/D17 | Customer Experience + Service |
| D-3 | Field Service foundation: if PD-2/3/4 are dropped, confirm with Oracle that Field Service functions without the SR/Install-Base foundation (Q12) | Q12 | D13 | IT Licensing |
| D-4 | Project Billing: adopt for W165 retention/milestone billing or re-route via OM milestone invoicing | PD-5 | §2.7, VS-11 | Finance + Trade Sales |
| D-5 | Fusion freight audit: adopt the TMS PD or record the VS-110 posture (EBS shapes already carry OTE in the OM base) | F-PARITY PD | VS-110 | Supply Chain Finance |
| D-6 | Services Procurement vs Purchasing contingent-labor entitlement (line 52 creditable?) | Q13 | B13 / VS-98 | Procurement |
| D-7 | Field Service Cloud floor relief: 360 pooled vs 40 actual technicians | Q15 | D13 | IT Licensing |
| D-8 | Ecommerce order-line sizing: confirm the line histogram behind lines 50/46 | Q11 | decision 1 | Digital + IT Licensing |
| D-9 | Store operating model: backroom-only (RFQ) vs 12-users-plus-RF (repo canon) — record before PO | Q10 | profile §12.1 | Store Ops |

## 7. RFQ v2 amendment summary (what changed in the quote document)

- RFQ **section 2.4** renamed **E-SCOPE** and re-tiered committed (G17); coverage-closure lines 50–54 added
  (G1–G5); the blanket out-of-scope note replaced by the priced PD-1–PD-5 block (G6–G10).
- RFQ **section 3.4** gains the committed **F-PARITY block** (lines 43–47: GOP, Revenue Mgmt, Quality,
  Pooled Order Lines, Field Service Cloud — $100,650/mo ≈ ₱41.7M/yr, all four F shapes) with
  TMS as PD (G11–G15); `WWM` re-tiered committed in F2/F4 (G16); swing restated to
  ₱76.1M/yr common + ₱4.1M/yr WMS Automation.
- RFQ **sections 2.5 / 3.5 / 4** totals restated: EBS E4 committed $18,774,765 → **$19,771,525**
  (≈ ₱648.7M → **₱683.1M** one-time; ₱142.7M → **₱150.3M/yr** support); Fusion max F4
  ₱501.3M → **₱543.0M/yr** (committed ₱416.2M → **₱466.9M/yr**). PD block carried outside the
  committed columns: +$1,099,475 ≈ ₱38.0M one-time · ₱8.4M/yr if all five PD lines are adopted
  (EBS 5-yr ≈ ₱1,515M with PD vs ≈ ₱1,435M without).
- RFQ **section 6** gains **Q11–Q15** (ecommerce order-line metric; Field Service foundation; Services
  Procurement vs contingent labor; recorded de-scope decisions; Fusion parity pricing and
  floor relief). Q6's † list extended with the closure/parity lines.

> **Post-review RFQ movement (recorded 2026-09-18, fifty-fifth-wave review).** The RFQ has
> evolved past the v2 amendment this section summarizes, in two same-day revisions in its own
> repository: **v2.0.1** (consistency pass — WWM re-housed from the swing table into the
> F-PARITY block as line 48, F2 & F4 only, parity total restated $122,325/mo ≈ ₱50.7M/yr;
> E-HR minimum-quantity flags; the support-convention and per-line-PHP-rounding sentences; Q5
> floor-relief list completed; Q11 split into the derived ~2.3M-line and licensed 2.5M-line
> counts) and **v2.0.2** (GPL-verification errata — the six formerly-TBC part #s resolved on
> the September 10, 2026 EBS GPL per §5.2 above; L&FM re-metric'd and excluded from totals
> pending the managed-asset figure; In-Memory Cost trued to $625,000; E-SCOPE $1,884,680 →
> $2,386,670; E1–E4 committed restated to $9,550,365 / $14,149,800 / $15,674,080 /
> **$20,273,515** ≈ ₱330.0 / 488.9 / 541.6 / **₱700.5M** one-time · 72.6 / 107.6 / 119.1 /
> **₱154.1M**/yr support — superseding the v2-amendment figures quoted above, whose E4 read
> $19,771,525 ≈ ₱683.1M · ₱150.3M/yr; §4 decision table restated at EBS 5-yr ₱1,471M, ₱1,551M
> with PD; TMS PD trued to B91099). The **coverage dispositions stand unchanged** — every
> G1–G17 gap and its v2 resolution, the PD register D-1–D-9 and the quantity reconciliation
> are unaffected by the repricing; the audited licensing-bom baseline itself moved v2.1 →
> v2.2 the same day (the actual-org gap-fill re-base — quantities and footings only, no
> product-set change), so no disposition moves on that account either.

---

*Document Version: 1.5 | Date: 2026-09-25 | **Method-sentence census true (the unguarded-surface sweep).** §1's derivation sentence still read 'the 728 requirements / 5,427 workflows / 808 controls' — the batch-23 census, stale since batch 30 moved the corpus to 5,433 (2026-09-23); this review is one of the four live surfaces no validator check reads (with module-coverage-map, ebs-documentation-coverage and customization-governance), so the drift class stayed invisible to every wave's guards until the 2026-09-25 sixth policy-pass sweep greped the unguarded set. Count trued to 5,433; no coverage register, verification item, PD decision or RFQ-amendment content change. Prior v1.4 | Date: 2026-09-23 | **OMO build squad deferred — prepared (2026-09-23 (ah)): the §3 employee-metric canon.** The quote-coverage employee canon re-bases 6,918 → 6,911 (518 → 511 HQ; the OMO build squad's 7 deferred — prepared with every sale completing as a regular POS sale; OM v3.28); the RFQ ≥ canon conservatism verdicts stand (7,247 / 9,271 ≥ 6,911). No quote-total, decision or restatement change. Prior 1.3 |
Prior 1.2 | Date: 2026-09-23 | **GPL sweep verification items (§5.5–5.7).** The coverage register's new §7 sellable-SKU sweep opened four entitlement flags and one naming-collision reconciliation; the three licensing-shaped ones fold into this review's verification register as §5 items 5–7 (Asset Tracking `L11496` rider entitlement; Supplier Ship and Debit `L72211` + the QP EOL component `L31659`; Product Hub Add-on `L42175` + the `L72189` scope question) — no G-item, PD decision, quantity reconciliation or RFQ-amendment figure changed; the flags ride the existing Q6 verification fold-in. Prior v1.1 | Date: 2026-09-18 | **Fifty-fifth-wave consistency review (post-review RFQ movement recorded):** the RFQ's own v2.0.1 (WWM re-housed as F-PARITY line 48, E-HR min-quantity flags, Q5/Q11 completions) and v2.0.2 (September 2026 GPL errata — six part #s resolved, L&FM re-metric'd qty-TBC, In-Memory Cost trued $625,000, E-SCOPE $2,386,670, E1–E4 committed restated with E4 at $20,273,515 ≈ ₱700.5M · ₱154.1M/yr, §4 restated ₱1,471M/₱1,551M, TMS PD B91099) revisions supersede the v2-amendment figures the §7 summary quotes — recorded as a dated status note in §7 with the §5.2 † list trued to the resolved part-# set; the G1–G17 dispositions, the PD register and the quantity reconciliation stand unchanged, as does the licensing-bom baseline movement v2.1 → v2.2 (quantity-only re-base, no product-set change). No repo canon change: no requirement, workflow, control, register-row, disposition, HC, role or count movement. Prior v1.0 | Date: 2026-09-18 | Initial issue — the cross-repo coverage audit of the
8-scenario license RFQ against the adopted footprint (licensing-bom v2.1, fit-gap resolutions
9–34, coverage-map v2.0); register G1–G17 with dispositions, the quantity reconciliation
(Q10 divergence), the metric-verification items, the PD decision register D-1–D-9, and the RFQ
v2 amendment summary. The amendment itself ships in the RFQ's own repository
(`erp_compare_infor/oracle-quote-license-bom-8-scenarios.md`, its version footer). No repo
canon change: no requirement, workflow, control, register-row, disposition, HC, role or count
movement.*
