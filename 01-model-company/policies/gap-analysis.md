# Policy Layer Gap Analysis — 2026-09-25 (fourth pass)

> Follow-up to §4 of the [Policy Manual README](README.md). Pass 1 built the
> base 50; pass 2 added ten corpus-evidenced policies (60 total); pass 3 added
> ten statutory-exposure policies (70 total) and *claimed* all chains complete.
> **Pass 4 (this pass) did not accept the prose claims** — it mechanically
> re-derived every one of the 188 VS domains against the anchors actually
> written in the nine domain manuals + the master register, and found the
> pass-3 completion claim false in two material ways. Both defect classes are
> repaired here, the register is completed at **75 policies**, and every VS
> domain now ends in a *written* anchor or a documented SOP-layer decision.

## 1. Method (pass 4) — mechanical, not narrative

Every `VS-xx` domain in `workflows/` was tested against three anchor surfaces,
each resolved to the domains it actually reaches:

1. **Direct** — `VS-xx` cited in a domain manual or register row;
2. **Process-area** — `PA-xx.y` cited (resolves to `VS-xx`);
3. **Workflow** — a `W-id` cited (resolved through the corpus's own
   `## W-id.` headers, 5,431 headers across 569 PA files).

Domains reaching none of the three were classified against the documented
fold/SOP decisions. The pass-3 records were then spot-audited by grep — with
surprising results (§2).

## 2. Findings — the pass-3 "complete" claim was false in two ways

### 2.1 Fifteen fold decisions had never been written (broken chains)

The pass-3 record said *"Fold candidates — anchors written: VS-110 → POL-P02
· VS-111 → POL-P02/S03 · VS-126 → POL-D01/D05 · VS-130 → POL-F03/Board DOA ·
VS-137 → POL-D05 · VS-141 → POL-H03 · VS-143 → POL-R02 · VS-168 → POL-G09 ·
VS-94/185 → POL-P02 · VS-180 → POL-S02/B01 · VS-191 → POL-S03 · VS-68 →
POL-F05"* and *"VS-190 → POL-I03/I04"*. **None of these fifteen domains
appeared anywhere in the nine manuals or the register** — the routing existed
only in the README prose. grep verified: zero hits for each `VS-xx` token
across `10-*.md` … `90-*.md`.

**Repaired:** all fifteen folds now carry written anchors and statements in
their named policies (e.g. POL-P02.5 covers VS-110/111/94/185 + the P2P chain;
POL-G05.7 reserves M&A/property disposals to the Board; POL-F05.6 folds the
trade-credit lifecycle and the B2B channels).

### 2.2 Subject-matter anchors missing — policies governed domains they never cited

Where a policy's register row cited only *older* workflow ids (W29, W28,
W632…), the anchor reached the id's own domain but not the VS family whose
**substance** the policy governs. Confirmed cases (all repaired):

| Policy | Governs (now cited) | Why it matters |
|---|---|---|
| POL-R06 | VS-89 (recall/CAPA), VS-117 (DTI-BPS PS/ICC), VS-31 (QMS), VS-41 (private-label QA) | the recall & certification programs were the policy's core subject |
| POL-R07 | VS-54 (gift-card program lifecycle) | register cited only W28 (a VS-07 workflow) |
| POL-R08 | VS-58 (coupons), VS-14 (marketing ops) | coupon fraud/permit chain now explicit |
| POL-R03 | VS-64 (seasonal clearance) | markdown discipline extended to clearance events |
| POL-R04 | VS-45 (consignment/VMI) | owner-flagged stock + settlement rule |
| POL-R01 | VS-81 (CIT/vault), VS-142 (COD) | custody chain extended off-store |
| POL-R02 | VS-143 (bulky delivery/haul-away) | doorstep custody chain |
| POL-F06 | VS-118 (revenue assurance program) | leak-detection framework is the standing method |
| POL-F07 | VS-157 (PFRS 15), VS-35 (fixed assets) | standards folds completed |
| POL-F08 | VS-38 (consumer installment financing) | charter letter (g) added |
| POL-F01 | VS-105 (supplier finance) | disclosure discipline added |
| POL-F02 | VS-106 (commodity hedging) | same no-speculation discipline as FX |
| POL-F03 / POL-G05 | VS-130 (M&A) | reserved-authority + capex gates |
| POL-P02 | VS-15 (P2P chain), VS-110/111/94/185 | one vendor lifecycle, every spend class |
| POL-H01 | VS-121 (TA program), VS-167 (screening) | proportionate vetting + RA 10173 handling |
| POL-H03 | VS-141 (employee transport) | welfare-program codification |
| POL-S01 | VS-24 (OSH execution), VS-61 (fuel/fleet) | fuel handling tied to POL-S04 classes |
| POL-S02 / POL-B01 | VS-180 (disaster relief) | relief logistics under crisis organization |
| POL-S03 | VS-25 (ESG reporting), VS-70 (solar line), VS-191 (debris) | claims substantiation; EOL stewardship |
| POL-S05 | VS-83 (occ-health clinic) | medical program = POL-S01 case management |
| POL-S07 | VS-172 (installer network) | licensed-installer gate on referrals |
| POL-G08 | VS-129 (competition program) | PCC engagement/investigation protocol |
| POL-G06 | VS-104 (government affairs) | advocacy runs the statement-3 tiers |
| POL-G09 | VS-168 (music royalties) | licensed repertoires only |
| POL-G11 | VS-21 (internal audit) | IA charter = Audit-Committee-approved |
| POL-G12 | VS-37/59/109 (site lifecycle) | permits gate openings/closures/remodels |
| POL-I03 / POL-I04 | VS-190 (OT/ICS), VS-99 (IT assets) | OT segmentation; certified data sanitization |
| POL-D01 / POL-D05 | VS-126 (CDP), VS-137 (PIM/DAM) | identity resolution never manufactures consent |

## 3. New policies — created (batch 4, +5 → register 75)

| # | Policy | Corpus gap closed | Statutory base |
|---|---|---|---|
| 1 | **POL-G14 — Government & Institutional Sales Compliance** | VS-46 (PA-46.1–46.3) | RA 9184 as supplier-facing, RA 3019 (per POL-G02), COA billing rules |
| 2 | **POL-H11 — Labor Relations & Collective Bargaining** | VS-84 (PA-84.1–84.3) | Labor Code arts. 263–290, grievance/CBA framework |
| 3 | **POL-F09 — Property Acquisition, Land-Use & Lease Compliance** | VS-20, VS-42, VS-97, VS-178 | CARPER/RA 9700 conversion, RA 8371 NCIP/FPIC, LGC zoning, PFRS 16 interface |
| 4 | **POL-S09 — Corporate Security, Executive Protection & Travel Risk** | VS-159 (PA-159.1–159.3) | RA 5487 (licensed guarding), duty-of-care travel risk |
| 5 | **POL-S10 — Product Stewardship & Take-Back** | VS-187 (PA-187.1–187.3) | RA 6969, RA 9003, RA 11898 EPR interface (plastic EPR stays POL-S03.7) |

Count check: **14+9+5+11+7+5+11+10+3 = 75.**

## 4. Remaining unanchored domains — classified, all documented

After the repairs, the residual unanchored set is entirely
**SOP/engineering layer** (process-execution and analytics domains whose
control substance is the policies above), now enumerated in README §4:
VS-02, VS-04, VS-09, VS-12, VS-28, VS-44, VS-47, VS-48, VS-55, VS-56,
VS-57, VS-62, VS-63, VS-65, VS-66, VS-72, VS-75, VS-77, VS-78, VS-92,
VS-112, VS-127 — plus the batch-3 SOP list (VS-60, VS-93, VS-95, VS-101,
VS-103, VS-115, VS-123, VS-124, VS-133, VS-134, VS-135, VS-136, VS-138,
VS-139, VS-140, VS-146, VS-149, VS-162, VS-163, VS-164, VS-171, VS-174,
VS-176, VS-177). Where these domains touch a risk-bearing edge, the edge is
individually anchored (marketplace customer data → POL-D01; IT asset
disposal → POL-I04.5; price-match conduct → POL-R03.5).

## 5. Pre-existing authoring backlog (unchanged, still open)

- Employee Handbook (consolidation of POL-G01/H05/H06)
- Ecommerce T&C and loyalty program terms (derived from POL-D01/R02)
- W1729 Volume-canon re-baseline (~50–60 → 75) at the next review — the
  corpus edit cascades bpmn regeneration, deliberately deferred from this pass

---

**Bottom line (pass 4):** 75 policies; every one of the 188 VS domains ends
in a **written** anchor or a **documented** SOP-layer decision; the pass-3
broken-fold class is repaired and its lesson recorded — *coverage claims are
only as good as the grep that checks them.*
