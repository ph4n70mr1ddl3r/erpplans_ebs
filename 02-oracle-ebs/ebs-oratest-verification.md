# EBS oratest Capability Verification — erpplans_ebs Documentation Set vs the CitiHardware R12.2.4 PROD-Clone Test Rig

> Live capability verification of the blueprint's platform claims against the second installation
> of record: the operating company's actual EBS production clone (the `~/access_oratest` test rig —
> database tier `proddb` 192.168.8.211, applications tier `cloneapp` 192.168.8.212). Where the
> companion report (the [EBS Vision instance verification](ebs-vision-verification.md), the
> 12.2.12 latest-codelevel reference appliance) left a mechanism blocked or unproven, this
> verification asks the question that actually matters for the implementation — *can the company's
> own installation do what the documentation says?* — and answers it from the rig's banked
> concurrent-request evidence plus, where no banked evidence existed, end-to-end tests executed
> for this report on 2026-09-21. Method: read-only catalog/history probes and scripted
> interface/API/concurrent-path executions over the rig's ssh→sqlplus harness; UI screens are never
> exercised (the rig's own standing methodology). Nothing is quoted from vendor literature.

---

## 1. Environment of record (rig)

| Attribute | Value | Evidence |
|---|---|---|
| EBS release | **12.2.4** (AD C.Delta.7 + TXK Delta 17 applied 2026-09-14; RUP 37182900 pending per the 12.2.15 upgrade path) | `fnd_product_groups.release_name`; the rig's own patch-cycle audit |
| Database | Oracle Database 12.1.0.2 (ARCHIVELOG, FORCE_LOGGING), instance `PROD` | rig architecture reference |
| Instance tiers | `proddb` 192.168.8.211 (DB) / `cloneapp` 192.168.8.212 (OHS :8000, WebLogic, concurrent managers) | rig healthchecks |
| Business group | **81 — CITIHARDWARE INC**; 29,026 current employees on the clone | `per_business_groups`, `per_people_f` |
| Ledgers / OUs | 18 PHP operational ledgers + 1 consolidation ledger (2041 `CONSOLIDATION_LS`); 18 operating units (legacy company OUs — 82 Davao, 83 Bacolod, 84 Gensan, 85 Decoarts, 86 Mindanao, the LCY trading corporations, and the campaign-built 2768/2770/2772 `_OPS` OUs) | `gl_ledgers`, `hr_operating_units` |
| Inventory / assets | 237 inventory organizations; 11 FA corporate books with live depreciation (book `CTBAC CORP BOOK` open at **MAY-26**; last depreciation run 2026-05-14); 468,764 AR transactions | `mtl_parameters`, `fa_deprn_periods`, `ra_customer_trx_all` |
| Probe basis | footprint + history probes and both E2E drivers executed 2026-09-21; banked concurrent-request history windowed to the preceding 60 days | `erpplans_fp_probe2_20260921_raw.txt`, `erpplans_cphist_probe_20260921_raw.txt`, `erpplans_vt9_hire_20260921_raw.txt`, `erpplans_vt10_famapt_20260921_raw.txt` (rig side) |

---

## 2. Footprint conformance on the rig (FP × rig)

The Vision report's FP-01–FP-39 rows map the fit-gap register's **adopted** vehicles to the
12.2.12 registry, where 33 of 39 rows are CONFIRMED installed. This table re-maps the same 39 rows
onto the rig — the company's **today** installation — and reads the difference for what it is: an
**adoption gap**, not a documentation defect. The blueprint is the target state; the rig is the
baseline the implementation starts from. Rig statuses: **Installed** (`fnd_product_installations`
status `I`), **Shared** (status `S` — installed as a shared/secondary codelevel), **Not installed**
(status `N` — registered in the 176-product registry but no installation row activity), and
**Registered, not installed** (the AMW case).

| FP | Adopted vehicle (short name) | Rig status | Reading |
|---|---|---|---|
| FP-01 | General Ledger (SQLGL) Installed; Subledger Accounting (XLA) Shared; e-Business Tax (ZX) Not installed | Mixed | the accounting core is the rig's daily workhorse; the company operates PH taxation on legacy tax codes — ZX adoption remains a target-state decision |
| FP-02 | Payables (SQLAP), Receivables (AR), Assets (OFA) | Installed | confirmed — AP/AR/FA are live on the clone with production history |
| FP-03 | iReceivables / Lockbox / BR / BFB (AR features) | Feature | AR installed; feature enablement is an implementation task |
| FP-04 | Cash Management (CE) | Installed | confirmed |
| FP-05 | Treasury (XTR) | Not installed | adoption gap — license + install per the licensing BOM |
| FP-06 | Revenue Management — in-suite AR capability (VF-1 adjudication) | Feature | AR installed; consistent with the VF-1 naming correction |
| FP-07 | Lease & Finance Management (OKL) | Not installed | adoption gap |
| FP-08 | Sourcing (PON) | Not installed | adoption gap |
| FP-09 | Trade Management (OZF) | Not installed | adoption gap |
| FP-10 | Internet Expenses (SQLAP + ICX responsibilities) | Installed | confirmed — iExpenses enablement already exercised on the rig |
| FP-11 | Purchasing (PO) Installed; Contracts Core (OKC) Not installed | Mixed | PO live (banked PO/receipt/invoice chains); OKL-class adoption gap on OKC |
| FP-12 | Product Hub (EGO) | Not installed | adoption gap |
| FP-13 | Inventory (INV) Installed; Mobile/MSCA (MWA) Not installed | Mixed | INV live (banked INCTCM 2,230/2,230 Normal); MSCA mobile adoption gap |
| FP-14 | Site Hub | Registered, not installed | consistent with Vision VF-3 (release availability) |
| FP-15 | ASCP (MSC) Shared; MSO/MSD/MSR Not installed | Mixed | MRP (704) is Installed and its E2E was exercised on the rig; the ASCP/optimization suite is an adoption gap |
| FP-16 | Demantra | Separate | unchanged — not an EBS application |
| FP-17 | Warehouse Management (WMS), Yard Management (YMS) | Not installed | adoption gap (org enablement + install) |
| FP-18 | Bills of Material (BOM), Work in Process (WIP) | Installed | confirmed — the rig's WIP costing campaigns ran real CMCCTW/WICDCL cycles |
| FP-19 | Quality (QA) | Shared | installed at shared codelevel; adoption decision unchanged |
| FP-20 | Shipping Execution (WSH), Transportation Execution (FTE) | Installed | confirmed — FTE was enabled and E2E-tested on the rig |
| FP-21 | In-Memory Cost Management (CMI) | Not installed | adoption gap |
| FP-22 | Configurator (CZ) | Shared | installed at shared codelevel |
| FP-23 | Engineering (ENG) | Shared | installed at shared codelevel |
| FP-24 | Credit Management (AR responsibilities) | Feature | AR installed; responsibility presence is an implementation check |
| FP-25 | Field Service (CSF/CSL/CSM), Scheduler (CSR) | Not installed | adoption gap |
| FP-26 | TeleService (CS) | Shared | installed at shared codelevel |
| FP-27 | Global Order Promising — no standalone application (VF-4) | Feature | consistent with the Vision adjudication (OM-embedded ATP + planning server) |
| FP-28 | Installed Base (CSI), Service Contracts (OKS) | Not installed | adoption gap |
| FP-29 | Depot Repair (CSD) | Not installed | adoption gap |
| FP-30 | HR (PER) Installed; iRecruitment (IRC), Learning (OTA) Not installed | Mixed | Core HR live (29k employees; the VT-9 hire below ran on it); IRC/OTA adoption gaps |
| FP-31 | Performance Management — PER self-service appraisal feature (VF-5) | Feature | unchanged naming adjudication |
| FP-32 | Payroll (PAY) Installed but unadopted by doctrine | Installed | consistent — installed on the clone, unadopted per the two-tier doctrine |
| FP-33 | Advanced Benefits (BEN) | Not installed | adoption gap |
| FP-34 | Property Manager (PN) | Not installed | adoption gap |
| FP-35 | Enterprise Asset Management (EAM) | Not installed | adoption gap |
| FP-36 | GL budgets + budgetary control (GL feature) | Feature | GL installed |
| FP-37 | Alert (ALR) | Installed | confirmed |
| FP-38 | Internal Controls Manager (AMW) | Registered, not installed | **consistent with Vision VF-2** — obsolete-not-installed on both installations; the H11 build-side re-disposition stands |
| FP-39 | AME Not installed; EDR/XDO Installed; Web ADI (BNE), XLE Not installed; IBY Installed; Projects (PA) Installed | Mixed | IBY live (quick payments proven); EDR/XDO installed; AME/BNE/XLE adoption gaps — note AME's absence is consistent with the rig's dead approval workflows (OR-4) |

**FP × rig reading:** the rig confirms the adopted **baseline core** — GL/AP/AR/FA/CE, PO, INV,
OM, BOM/WIP, WSH/FTE, PA, PER/PAY, IBY, ALR, EDR, XDO — as live, production-proven capability, and
records **24 adopted vehicles not (fully) installed** on the company's today installation (the
treasury/leasing/sourcing/trade/contracts/product-hub/planning/WMS/service-suite/EAM/PN/BEN/AME/
BNE/XLE adoption families). Every gap row is an implementation task with its license already
carried by the licensing BOM — this report changes no disposition, no count and no register.

---

## 3. Transactional cross-verification (VT × rig)

The Vision report's ten-path transactional matrix, re-executed **against the rig**. Verdicts:
**GREEN** (the documented mechanism proven on the rig — banked concurrent-request evidence in the
60-day window, or executed live for this report on 2026-09-21), **PARTIAL** (mechanism proven with
a scoped exception). The Vision round-3 verdicts are frozen history and quoted only for contrast.

| VT | Path (workflow class) | Rig verdict | Evidence |
|---|---|---|---|
| VT-1 | AP supplier invoice → payment (W7 class) | GREEN (banked) | `APXIIMPT` **144 of 145 Normal** in the window; the rig's `wf_ap_invoice_payment` chain — invoice import → approval → quick payment → PCACCT accounting → GL journal — GREEN (2026-08-24 suite); P2P one-shot invoice 1852790-era (2026-08-25) |
| VT-2 | GL journal import (W9A/W90 class) | GREEN (banked) | `GLLEZLSRS` **138/138 Normal** + child `GLLEZL` **156 of 175 Normal** in the window — the Vision VF-7 block (4,102/4,102 historical failures) **does not reproduce** on the company's installation (OR-2); journals land balanced with posting deliberately deferred (the rig's posting safety-skip) |
| VT-3 | AR AutoInvoice (W8 class) | GREEN (banked) | `RAXMTR` **9 Normal** in the window on original operating unit **82 (Davao)** with the company's real seeded sources — `Intercompany` (trx_date 2026-06-15 batch), `NON TRADE SALES - INV` (source 4006), `NONTRADE INTERSTORE` (source 13010), requests 76960675–76960708 (2026-09-09) |
| VT-4 | OM Order Import (W56 class) | GREEN (banked) | `OEOIMP` **116 of 124 Normal** on OU 82 (requests 76887187–76887196 of 2026-08-25 and 76960629/76960633/76960634 of 2026-09-09) — the Vision VF-8 binding defect likewise does not reproduce |
| VT-5 | OM sales order via OE_ORDER_PUB (W56 class) | GREEN (banked) | ISO **26218695** booked via the requisition→approval→`OE_ORDER_PUB.Process_Order` path (rig marketing campaign W-09, 2026-09-10) |
| VT-6 | PO requisition import + approval (W2/W2A class) | PARTIAL (banked) | `REQIMPORT` **11 Normal** in the window on OU 82 (sources `WIP` and `Supplier`, requests 76960607–76960625 and 76956663 of 2026-09-01); the approval **workflow** leg never runs on the clone — REQAPPRV/POAPPRV items abort in ≈1 s on the no-approver-found path (no usable hierarchies/limits; AME not installed) and documents take the rig's documented fallback approval stamp — approval hierarchy setup is an implementation task (OR-4) |
| VT-7 | Receiving open interface (W3 class) | GREEN (banked) | `RVCTP` **44 of 44 Normal** in the window — the P2P cycle's supplier→PO→receipt chain (OK 8 / WARN 5 / FAIL 0, 2026-08-25); scoped exception banked separately: the internal-order store-receipt row shape is rejected by this rig's ROI (four shapes tried, rig campaign S1-08) |
| VT-8 | Inventory misc receipt (W4/W91 class) | GREEN (banked) | `INCTCM` **2,230 of 2,230 Normal** in the window; the rig's inventory campaigns exercised MTL_TRANSACTIONS_INTERFACE misc receipt → on-hand → subinv transfer → misc issue with real cost processing (W-04/W-11 family), with the direct-MMT + on-hand-maintenance path documented as the locator-flexfield fallback |
| VT-9 | Core-HR employee hire via the public API (W15/W292 class) | GREEN (2026-09-21, this verification) | `HR_EMPLOYEE_API.Create_Employee` (overload 1, named notation) in business group 81: **person_id 48086 / employee_number 10029015 / assignment 49020** (type E, primary, `current_employee_flag` Y) — the H2R person+assignment path proven on the company's own HR data model; en-route contract finding: the comment OUT parameter is `p_per_comment_id` |
| VT-10 | Fixed asset via mass additions (W39/W35 class) | GREEN (2026-09-21, this verification) | `FA_MASS_ADDITIONS` row 1352523 staged into the POST queue (book `CTBAC CORP BOOK`, category 14, charge ccid 24016, location 11, DPIS 2026-05-01 inside the open MAY-26 period) → Mass Additions Post: first attempt 76976813 errored on `depreciate_flag='Y'` (the rig requires **YES/NO** — banked log l76976813.req), corrected → request **76976818 Normal**, `posting_status` POSTED, `fa_additions_b` asset **E2E-ERP-F-001** (asset_id 22165) |

**Rig tally: 9 GREEN + 1 PARTIAL of the 10 paths.** Every mechanism the Vision report proved on the
appliance reproduces on the company's installation; both Vision instance-side blocks (VT-2 GL
journal import, VT-7 receiving) are **GREEN on the rig**; the one partial (VT-6's approval leg) is
an un-loaded setup artifact of the clone, not a product capability gap.

---

## 4. Findings and consistency dispositions

| OR | Finding | Disposition |
|---|---|---|
| OR-1 | The documentation set now has **two installations of record**: the Vision 12.2.12 appliance (latest-codelevel reference instance) and this rig (the operating company's actual installation — the capability of record for what can be executed today) | both verification reports stand; this document governs capability questions, the Vision report governs codelevel questions |
| OR-2 | The Vision report's two SR-grade instance blocks do **not** reproduce on the rig: GL journal import runs Normal daily (VT-2), receiving processes receipts via RVCTP normally (VT-7) | strengthens the Vision VF-7/VF-10 instance-defect adjudications — both are properties of the Vision appliance, not of EBS 12.2 or of the company's installation; no documentation change required beyond this record |
| OR-3 | 24 adopted vehicles are not (fully) installed on the rig (§2 adoption families) | no register change — the fit-gap register is the target-state adoption record and the licensing BOM already carries the licenses; the gap rows are implementation tasks (license → install → org/responsibility setup) |
| OR-4 | The rig's approval workflows never run (no approver hierarchies/limits; AME not installed — consistent with FP-39) | the documentation's approval-ladder doctrine presupposes implementation-phase approval-matrix setup; flagged as an implementation dependency for the TO/controls cascade |
| OR-5 | Rig-specific contract facts banked for the implementer: FAMAPT requires `depreciate_flag` YES/NO; `FA_MASS_ADDITIONS.ASSET_NUMBER` is 15 characters; the 12.1.0.2 SQL*Plus harness mis-parses variables declared after inline procedures (declare variables first); direct workstation→DB connectivity is dead — all execution rides the rig's ssh→sqlplus harness | recorded here as the rig's contract appendix; none touches the documentation canon |
| OR-6 | This verification moves **no canonical numbers** — no workflow, control, requirement, headcount, tier or disposition totals change | the report is a capability record; the fit-gap/coverage/TO registers are untouched |

---

## 5. Verification artifacts

| Artifact | Location | Content |
|---|---|---|
| Footprint probe | rig: `erpplans_fp_probe2_20260921.py` + `_raw.txt` | release/ledger/OU inventory, the full `fnd_product_installations` × FP-set matrix, INV/FA/HR/AR state reads |
| Banked-history probe | rig: `erpplans_cphist_probe_20260921.py` + `_raw.txt` | 60-day concurrent-request history for the ten VT mechanisms (3,000 requests tabulated) |
| HR-hire E2E | rig: `erpplans_vt9_hire_20260921.py` + `_raw.txt` | VT-9 — employee 10029015 hired and verified |
| FA mass-additions E2E | rig: `erpplans_vt10_famapt_20260921.py` + `_raw.txt` | VT-10 — mass addition 1352523 staged, posted via request 76976818, asset E2E-ERP-F-001 verified |
| Failed-first evidence | rig: request log l76976813.req | the depreciate-flag rejection (OR-5) |

---

*Document Version: 1.0 | Date: 2026-09-21 | Initial issue — capability verification of the blueprint documentation set against the operating company's R12.2.4 PROD-clone test rig: footprint re-mapped FP-01–FP-39 onto the rig's registry (baseline core confirmed installed; the adoption families recorded as implementation tasks; AMW consistent with Vision VF-2 on both installations); the ten-path Vision transactional matrix re-executed against the rig — 9 GREEN + 1 PARTIAL (VT-6's approval leg: clone approval hierarchies not loaded; AME uninstalled), with both Vision instance-side blocks (VT-2 GL journal import, VT-7 receiving) GREEN on the rig and the two no-banked-evidence paths (VT-9 HR hire, VT-10 FA mass additions) executed end-to-end for this report (employee 10029015; asset E2E-ERP-F-001 via request 76976818 Normal); findings OR-1–OR-6 with no canon, register or count change. Exact rig markers (footer-exempt): E2E-ERP-F-001 / 10029015 / 76976818 / 1352523.*
