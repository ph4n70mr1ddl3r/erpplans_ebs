# EBS Vision Instance Verification — erpplans_ebs Documentation Set vs Oracle E-Business Suite 12.2.12

> Live verification of the blueprint's platform claims against the designated ERP system of
> record: the Oracle E-Business Suite 12.2.12 Vision appliance (VirtualBox, NAT; see
> `~/virtualbox_ol/ebs.md` on the authoring workstation). Every claim in this document was
> executed against the instance over SSH/SQL*Plus (2026-09-17 v1.0; extended 2026-09-18 v2.0 —
> verification round 2, ten transactional paths; extended 2026-09-18 v3.0 — verification round 3:
> eight of the ten paths PASS end-to-end, the v2.0 AR/OM-import/INV blocks resolved by one seeded-setup
> correction and two submission-contract/data corrections, GL and receiving root-caused to conclusive
> SR-grade instance defects); nothing is quoted from vendor literature. Method: (1) platform footprint conformance — every adopted vehicle in
> the [fit-gap register](fit-gap-analysis.md) and [module coverage map](module-coverage-map.md)
> checked against `FND_PRODUCT_INSTALLATIONS` × `FND_APPLICATION_VL` (176 registered
> products) and the seeded responsibility catalog; (2) transactional smoke tests — ten
> representative workflow families executed through their standard interface/API/concurrent
> paths (the paths the workflows themselves name); (3) setup-conformance reads for the
> model-company entities the workflows presuppose.

---

## 1. Environment of record

| Attribute | Value | Evidence |
|---|---|---|
| EBS release | **12.2.12** | `fnd_product_groups.release_name` |
| Database | Oracle Database 19c Enterprise Edition (CDB/PDB; PDB `EBSDB`) | `v$version`; `EBSCDB_apps.env` |
| Instance tier | apps.example.com:8000 (HTTP 200) / :4443 (HTTPS 200) / :7001 (WebLogic) | healthcheck 6 ok / 0 fail, 2026-09-17 |
| Ledger of record | Vision Operations (USA), USD, ledger_id 1; access set 1017 | `gl_ledgers`, `gl_access_sets` |
| Operating unit | Vision Operations, org_id 204; master org V1 (204), child M1 (207) | `org_organization_definitions` |
| Open periods | last open: **NOV-2016** (Dec-16/Adj-16 = Future) | `gl_period_statuses` |
| Verified users | SYSADMIN (0), OPERATIONS (1318), MFG (1068) — all demo passwords verified by login | `fnd_user` |
| Sample run baseline | 43,307 booked Vision orders; 140 ASCP plans; seeded journals/invoices/receipts | `oe_order_headers_all`, `msc_plans`, `gl_je_headers` |
| Inventory transaction calendars | earliest unclosed period per org is the open one — org 204 (V1) Dec-07, org 207 (M1) Oct-10 | v3.0 correction of the v2.0 VF-11 false negative |
| FA book calendar | corporate book OPS CORP open period Sep-2010 (`fa_deprn_periods`) | v2.0 finding VF-11 |

## 2. Footprint conformance (FP rows)

Each FP row maps one register vehicle to the instance registry. Verdicts: **CONFIRMED**
(installed, status `I`, responsibility/feature verified), **CORRECTION** (naming claim wrong —
see the linked VF finding), **NOT PRESENT** (product does not exist in the 12.2.12 registry or
is marked obsolete), **SEPARATE** (real Oracle product but not an EBS application — outside the
registry by design).

| FP | Fit-gap rows | Product (short name, app id) | Vision registry | Verdict |
|---|---|---|---|---|
| FP-01 | A1/A2 | General Ledger (SQLGL, 101); Subledger Accounting (XLA, 602); e-Business Tax (ZX, 235) | I | CONFIRMED |
| FP-02 | A3 | Payables (SQLAP, 200); Receivables (AR, 222); Assets (OFA, 140) | I | CONFIRMED |
| FP-03 | A3/A14 | iReceivables (AR responsibilities, e.g. 'iReceivables 2.0 Internal'); Lockbox/Bills Receivable/Balance Forward Billing (AR features) | I (AR) | CONFIRMED |
| FP-04 | A4 | Cash Management (CE, 260) | I | CONFIRMED |
| FP-05 | A8 | Treasury (XTR, 185) | I | CONFIRMED |
| FP-06 | A11 | 'Oracle Revenue Management and Invoicing (RM&I)' — **no such registered application in 12.2.12**; the in-suite revenue-schedule engine ships inside Receivables ('Revenue Management Super User' responsibilities under AR; Revenue Recognition program ARBARL) | absent as app; present as AR capability | CORRECTION (VF-1) |
| FP-07 | A13 | Lease and Finance Management (OKL, 540) — 18 lease responsibilities seeded | I | CONFIRMED |
| FP-08 | B5 | Sourcing (PON, 396) | I | CONFIRMED |
| FP-09 | B10 | Trade Management (OZF, 682) — 5 responsibilities | I | CONFIRMED |
| FP-10 | B11 | Internet Expenses / iExpenses (SQLAP 200 + ICX 178 responsibilities) | I | CONFIRMED |
| FP-11 | B12/B13 | Purchasing (PO, 201); Contracts Core (OKC, 510); contingent labor (PO feature) | I | CONFIRMED |
| FP-12 | C1 | Product Hub (EGO, 431) | I | CONFIRMED |
| FP-13 | C2 | Inventory (INV, 401); Mobile Applications / MSCA (MWA, 405) | I | CONFIRMED |
| FP-14 | C3 | Site Hub — **not registered in 12.2.12 Vision** | absent | NOT PRESENT (VF-3) |
| FP-15 | C5 | Advanced Supply Chain Planning (MSC, 724); Constraint Based Optimization (MSO, 723); Demand Planning (MSD, 722); Inventory Optimization (MSR, 726); 140 seeded ASCP plans | I | CONFIRMED |
| FP-16 | C5/C5 note | Demantra — **not an EBS application** (separate Oracle VCP product; never in `FND_APPLICATION`) | not an EBS app | SEPARATE (consistent with the licensing BOM's custom-quote register) |
| FP-17 | C6 | Warehouse Management (WMS, 385); Yard Management (YMS, 9009) | I | CONFIRMED (no WMS-enabled org seeded — org enablement is an implementation task, `mtl_parameters.wms_enabled_flag='N'` on all 18 orgs) |
| FP-18 | C9 | Bills of Material (BOM, 702); Work in Process (WIP, 706) | I | CONFIRMED |
| FP-19 | C12 | Quality (QA, 250) | I | CONFIRMED |
| FP-20 | C14 | Shipping Execution (WSH, 665); Transportation Execution (FTE, 716) | I | CONFIRMED |
| FP-21 | C15 | In-Memory Cost Management (CMI, 9010) | I | CONFIRMED |
| FP-22 | C16 | Configurator (CZ, 708) | I | CONFIRMED |
| FP-23 | C17 | Engineering (ENG, 703) | I | CONFIRMED |
| FP-24 | D3 | Credit Management (AR responsibilities: 'Credit Management Super User'/'Credit Management User') | I (AR) | CONFIRMED |
| FP-25 | D13 | Field Service (CSF, 513; + CSL 868, CSM 883); Scheduler (CSR, 698) | I | CONFIRMED |
| FP-26 | D14 | TeleService (CS, 170) | I | CONFIRMED |
| FP-27 | D15 | Global Order Promising — **no standalone application registered**; in-suite promising rides OM-embedded ATP (per the licensing BOM's own decision 3) plus the installed MSC/MSO planning server | absent as app | NOT PRESENT as standalone (VF-4) |
| FP-28 | D16 | Installed Base (CSI, 542); Service Contracts (OKS, 515) | I | CONFIRMED |
| FP-29 | D17 | Depot Repair (CSD, 512) — 5 responsibilities | I | CONFIRMED |
| FP-30 | E2 | iRecruitment (IRC, 821); Learning Management (OTA, 810); Human Resources (PER, 800); Succession Planning (PER responsibilities 'Succession Planning', 'Succession Planning for Administrators') | I | CONFIRMED |
| FP-31 | E2 | 'Performance Management' — the EBS appraisal/objectives vehicle is the PER self-service appraisal feature; the registered BSC app ('Balanced Scorecard') that seeded the 'Performance Management …' responsibilities is marked **(Obsolete)** and not installed | PER feature; BSC obsolete | NAMING NUANCE (VF-5) |
| FP-32 | E5–E8 | Payroll (PAY, 801) installed in Vision — the register keeps Oracle Payroll **unadopted** by doctrine (in-house Payroll PH build), so installation is not a conflict | I | CONFIRMED (no conflict) |
| FP-33 | E9 | Advanced Benefits (BEN, 805); Compensation Workbench (BEN responsibilities) | I | CONFIRMED |
| FP-34 | F3 | Property Manager (PN, 240) — 22 responsibilities | I | CONFIRMED |
| FP-35 | F5 | Enterprise Asset Management (EAM, 426) | I | CONFIRMED (no eAM-enabled org seeded — implementation task, `eam_enabled_flag='N'`) |
| FP-36 | F6 | GL budgets + budgetary control (GL feature) | I | CONFIRMED |
| FP-37 | G9 | Alert (ALR, 160) | I | CONFIRMED |
| FP-38 | H11 | Internal Controls Manager (AMW, 242) — registered as **'Internal Controls Manager (Obsolete)'**, **no installation row** (`fnd_product_installations` has no record); seeded responsibilities are leftover menu definitions | obsolete, not installed | NOT PRESENT — RETIREMENT REQUIRED (VF-2) |
| FP-39 | cross | Approvals Management (AME, 203); E-Records/ERES (EDR, 709); BI Publisher (XDO, 603); Web ADI (BNE, 231); Legal Entity Configurator (XLE, 204); Payments (IBY, 673); Projects (PA, 275); Landed Cost Management (INL, 9004); Loans (LNS, 206); Collections (IEX, 695); iSupplier Portal (POS, 177); iProcurement (ICX, 178); Advanced Pricing (QP, 661); Order Management (ONT, 660) | I | CONFIRMED |

Tally: **33 of the 39 FP rows CONFIRMED, 1 CORRECTION (VF-1), 1 NAMING NUANCE (VF-5), 2 NOT PRESENT (VF-2, VF-3), 1 NOT PRESENT-as-standalone (VF-4), 1 SEPARATE (FP-16)** — across the 97-row register's adopted-vehicle set.

## 3. Transactional verification (VT rows)

All tests executed as user OPERATIONS (1318) with `fnd_global.apps_initialize` +
`mo_global.init/set_policy_context('S',204)` (GL/FA/PER run without MOAC init — non-MOAC
products), dated inside the open NOV-2016 period, using
Vision master data (item AS18947 id 155; customer Computer Service and Rentals, account 1004,
bill-to site use 1017 → acct site 1030 / ship-to 1018; supplier Boise Cascade 558 / site 4970; price list Corporate 1000;
order type Standard 1000; line type Standard (Line Invoicing) 1427). v2.0 adds the requisition,
receiving, inventory, HR, FA and OM-API paths (round 2, 2026-09-18) and re-adjudicates the
five v1.0 rows with per-program submission contracts extracted from the SRS registry, the
spawned-C argv contracts and the installed package signatures. Concurrency ids are the
instance's own. Round 3 (2026-09-18 v3.0) re-executed the matrix and adjudicated every block:
eight paths PASS, two root-caused SR-grade instance defects (VF-7, VF-10).

| VT | Workflow family | Path exercised | Result | Evidence |
|---|---|---|---|---|
| VT-1 | AP supplier invoice via the open interface (W7 class) | `AP_INVOICES_INTERFACE` + `AP_INVOICE_LINES_INTERFACE` → Payables Open Interface Import (APXIIMPT) — v1.0 request **7625505**; v2.0 re-run request 7625573 (report-type positional contract) and **7625583** proc-order submission — Normal, 0 rejections | **PASS (evidence re-inventoried intact, v3.0)** | `ap_invoices_all` holds the BRW-AP test invoice (v1.0) and **brw-e2e-ap-002 / invoice_id 565060, USD 175, vendor 558, site 4970, org 204** (v2.0; `ap_interface_rejections` = 0). v1.0 finding stands: the header `invoice_amount` is mandatory and the supplier site's default payment method must exist |
| VT-2 | GL manual journal via the interface (W638 class) | `GL_INTERFACE` (balanced 100/100, CCIDs 16902/17021, source Manual, category Adjustment, ledger 1, 30-NOV-2016) + `GL_INTERFACE_CONTROL` → Journal Import (GLLEZL) — v2.0 requests 7625557/7625563/7625572 and v3.0 requests **7625621/7625622/7625624**, all in the binary-verified positional order (run_id, source, sus_on, from, to, summary, archive) | **BLOCKED (SR-grade — conclusive, v3.0)** | The appliance's full GLLEZL request history holds **4,102 runs, every one Error — zero successes ever** (100% failure across the appliance's life), and all three v3.0 submissions fail identically at `gllacc`/`gllmai` ORA-01403 while **every prerequisite is individually verified present**: access set 1017 exists in `gl_access_sets` (security_segment_code F, default ledger 1) with a full-privilege `gl_access_set_norm_assign` row over ledger 1, the profile `GL_ACCESS_SET_ID`=1017, period Nov-16 open, both CCIDs enabled and detail-postable, source Manual / category Adjustment seeded, USD rows balanced. System-level event-1403 errorstack (armed CDB-wide and PDB-scoped) and a manager-session 10046 trace both confirm the ORA-01403 is raised and handled inside the spawned process, so the failing statement cannot be captured client-side — an SR/patch-grade instance defect (VF-7). GL interface rows (groups 999101/999105) left staged |
| VT-3 | AR invoice via AutoInvoice (fit-gap A14; the VS-16 AR billing side) | `RA_INTERFACE_LINES_ALL` (batch source ORDER ENTRY id 1001, context 'ORDER ENTRY', all 14 required flexfield segments, bill-to acct-site 1030) → AutoInvoice Master (RAXMTR) via its binary argv contract → child RAXTRX — v3.0 request **7625631** Normal after the AutoAccounting setup correction | **PASS (v3.0 — resolves the v2.0 block)** | Root cause found and corrected: the REV derivation's SEGMENT2 sources `RA_SALESREPS`, and **org 204 holds zero salesreps** — the exact empty segment in the invalid derived combination '01--4110-0000-000'. Setup correction applied (one row, documented, reversible): `ra_account_default_segments` gl_default_id 1000 SEGMENT2 constant '000', yielding the seeded enabled combination **01-000-4110-0000-000** (ccid 21829/125608). RAXMTR 7625631 Normal → RAXTRX imported the staged line: **ra_customer_trx_all trx_number 10047280 / customer_trx_id 1201202, complete=Y**, REV distribution ccid 125608, amount 100 (VF-9 resolved) |
| VT-4 | OM sales order via Order Import (W56/W146 class) | `OE_HEADERS_IFACE_ALL` + `OE_LINES_IFACE_ALL` (ref brw-om-001) → Order Import (OEOIMP) — v3.0 requests 7625633/7625635/7625639/**7625641** with the exact installed signature's registered 16-argument order | **PASS (v3.0 — resolves the v2.0 block)** | The v2.0 FDPSTP ORA-06502 was a submission-contract defect, not a program defect: `all_arguments` gives the installed `OE_ORDER_IMPORT_MAIN_PVT.ORDER_IMPORT_CONC_PGM` formals (errbuf; retcode NUMBER; p_operating_unit NUMBER; p_order_source, p_orig_sys_document_ref, p_operation_code VARCHAR2; p_validate_only; p_debug_level NUMBER; p_num_instances; …18 total), and the registered SRS order binds cleanly at 16 arguments. Two data-level findings en route: p_order_source takes the source **id** ('10'), and source 10 'Internal' is requisition-driven — `Pre_Process.Req_Header_Id_derivation` casts the reference to a PO-requisition header id (ORA-06502/01403) — so the staged rows moved to seeded source **1023 'Custom Order Entry'**, with `unit_list_price` and primary UOM 'Ea' fixes clearing the earlier 'Incorrect list or selling price' / 'Invalid unit of measure' rejections. OEOIMP 7625641 Normal → **oe_order_headers_all header 358773 / brw-om-001, flow ENTERED**, line AS18947 ×2 @ 100 (VF-8 overturned) |
| VT-5 | OM sales order create+book via OE_ORDER_PUB.Process_Order (W56 class) | Full public-API create + book in one pass (header + line, MOAC context 204) — v2.0 request-free in-session API call | **PASS (v2.0 — resolves the v1.0 block)** | The v1.0 failure was the call shape: the installed 12.2.12 signature opens `p_org_id`, `p_operating_unit`, `p_action_commit` (there is **no `p_commit`**) and carries `p_old_*` variants — the v1.0 attempt bound a nonexistent parameter. With the exact installed signature and a fixed-price line (`calculate_price_flag='N'` requires both `unit_selling_price` **and** `unit_list_price`), the API returns S: **order header_id 358770 / line 672218, orig_sys_document_ref brw-e2e-om-002, booked_flag Y** |
| VT-6 | Purchase requisition via the open interface + approval workflow (W2/W60 class) | `PO_REQUISITIONS_INTERFACE_ALL` (source BRW-E2E, INVENTORY destination, org 204, item AS18947 ×3, preparer 24) → Requisition Import (REQIMPORT) with `INITIATE_REQAPPR_AFTER_REQIMP='Y'` — request **7625580** completed Normal | **PASS** | `po_requisition_headers_all` holds requisition **533793 / num 15906, approval_status APPROVED** — import plus the full approval workflow completed end-to-end. Findings en route: the interface UOM needs the unit **name** ('Each', not the code 'Ea') and the preparer/requestor must be active workers |
| VT-7 | PO receipt via the receiving open interface (W3 class) | `RCV_TRANSACTIONS_INTERFACE` + `RCV_HEADERS_INTERFACE` → Receiving Transaction Processor (RVCTP, mode/group/org) — v2.0 + v3.0 requests 7625623/7625625/7625627/7625628/**7625630** across five row shapes: Direct+RECEIVE-only, Standard+RECEIVE (clean `RCV_TP_INVALID_AUTO_TRANSACT`), Standard+auto-DELIVER+EXPENSE+po_distribution_id, receiver employees 31 and active-receiver candidates, transaction dates 30-NOV-2016 and 15-DEC-2012 (inside employee 31's assignment window and an open PO period), BATCH and ONLINE modes | **BLOCKED (SR-grade — root-caused, v3.0)** | The manager-session 10046 trace (enabled via the request-level `enable_trace` flag) shows the ROI claim `UPDATE … SET processing_status_code='RUNNING' WHERE … (lpn_group_id is not null or lpn_id is not null or license_plate_number is not null or interface_transaction_id in (select interface_transaction_id from wms_lpn_contents_interface))` executing **r=0** — standard non-LPN rows are never claimed — after which the pre-processor marks the header ERROR **without creating any `rcv_shipment_headers` row** (zero INSERTs into it in the whole traced session), and `rvtshiline()` then dies on `select nvl(asn_type,'STD') into :b0 from rcv_shipment_headers where shipment_header_id = :b1` → ORA-01403 (RVTSH-140/189, handled inside the process, invisible to event-1403 errorstack). ONLINE mode aborts earlier ('afptpput failed'). Opaque-looking in v2.0, now a precise SR-grade instance defect (VF-10); interface groups 999401…999411 staged |
| VT-8 | Inventory misc receipt via the transaction interface (W3/W92 class) | `MTL_TRANSACTIONS_INTERFACE` (misc receipt, type 42/action 27/source 13, item 155 ×2 at cost, subinventory Depot, 15-OCT-2010, org 207) → `INV_TXN_MANAGER_PUB.Process_Transactions` (10-argument function form) — v3.0 in-session API call (no concurrent submission) | **PASS (v3.0 — resolves the v2.0 SKIP)** | The v2.0 SKIP was a false negative: `org_acct_periods.open_flag` holds 'Y'/'N' (the v2.0 open-period query required 'O'), and the earliest unclosed period per org **is** the open one — org 207 (M1) open at **Oct-10**. No setup change was needed: the API returned S, trans_count=1, and **mtl_material_transactions holds transaction 26212144** (org 207, item 155, qty 2, dated 15-OCT-2010) — the inventory-posting path works end-to-end inside Vision's own calendars (VF-11 corrected) |
| VT-9 | Core-HR employee hire via the public API (W15/W292 class) | `HR_EMPLOYEE_API.Create_Employee` (full 141-argument overload-1 call, Business Group 'Vision Corporation' 202, hire date 01-NOV-2016) — v2.0 in-session | **PASS** | `per_people_f` holds **person_id 32849 / employee_number 2397** (assignment 34073, `current_employee_flag` Y) — the H2R person+assignment creation path works end-to-end in a scripted session |
| VT-10 | Fixed asset via mass additions (W39/W35 class) | `FA_MASS_ADDITIONS` (asset brw-e2e-fa-001, book OPS CORP, category COMPUTER-PC, USD 1,200, prepared into the POST queue) → Mass Additions Post (FAMAPT, arguments Book + Mode) — v2.0 request **7625607** completed Normal | **PASS** | The asset posts: `fa_mass_additions` row **POSTED/POSTED** and `fa_additions_b` × `fa_books` holds **brw-e2e-fa-001 in book OPS CORP**. Findings en route: `asset_type` must be 'CAPITALIZED' (not 'CAPITAL'), the row needs `expense_code_combination_id` and `location_id`, and the date-placed-in-service must fall within the book's open period (Sep-2010 — VF-11) |

Read-only conformance confirmed without exception: item master (AS18947 present in master org
204 and child 207), Corporate price list (1000), Vision customers/terms/types, suppliers with
org-204 sites, 150+ seeded super-user responsibilities across the footprint, WMS/eAM org flags
off everywhere (both are implementation-task enablements, not product gaps), and the
`.jnlp`/Forms client chain documented in the instance notes. Round-3 tally: **eight of the ten
paths PASS end-to-end** (VT-1 AP, VT-3 AR AutoInvoice, VT-4 Order Import, VT-5 OM API, VT-6
requisition import + approval, VT-8 inventory posting, VT-9 HR hire, VT-10 FA mass additions);
the two remaining blocks (VT-2 GL Journal Import, VT-7 Receiving) are root-caused SR-grade
instance defects, not documentation or platform gaps — in every block the product, program,
interface tables and seeded data were all verified present.

## 4. Findings (VF) and required documentation corrections

- **VF-1 — A11 vehicle naming (CORRECTION REQUIRED).** The register's second-pass claim that
  EBS 12.2 ships a standalone 'Oracle Revenue Management and Invoicing (RM&I)' application is
  not borne out: the 12.2.12 registry contains no RM&I application, and the in-suite
  revenue-schedule engine is Receivables' own Revenue Management / Revenue Recognition
  ('Revenue Management Super User' responsibility; program ARBARL). The disposition itself
  (in-suite, FIT-CFG) stands — only the vehicle naming must be trued (A11 row, §4 resolution
  15 addendum, coverage-map Financials row, licensing BOM row: RM&I rides the AR/Financials
  base — no separate license line, per the BOM's own included-entitlements convention).
- **VF-2 — H11 vehicle retirement (RE-DISPOSITION REQUIRED).** 'Oracle Internal Controls
  Manager' (AMW, 242) is registered '(Obsolete)' with no installation record in 12.2.12 — the
  CTL-01–808 hosting and audit-management adoption cannot be delivered by that product in the
  designated instance. Per the two-tier doctrine the audit-management/controls-governance
  surface re-dispositions to the build side (or process-owned register), which moves the
  register counts (FIT-CFG 37 → 36, BUILD 14 → 15, standard 74 → 73 = 75.3%) and cascades to
  the intro headline, §3 table, §7 KPI, coverage-map Internal Audit row, architecture row and
  the licensing BOM's ICM line and totals.
- **VF-3 — C3 Site Hub (FOOTPRINT GAP).** Site Hub is not registered in 12.2.12 Vision; the
  site-attribute register adoption needs either a product-availability confirmation for the
  12.2 target release or a Product-Hub/process-owned fallback note on C3.
- **VF-4 — D15 GOP standalone (ANNOTATION).** No standalone GOP application is registered;
  the promising function is covered in-suite by OM-embedded ATP and the installed MSC/MSO
  planning server — consistent with the licensing BOM's custom-quote register; the fit-gap
  D15 vehicle cell should carry the same annotation.
- **VF-5 — E2 Performance Management (NAMING NUANCE).** The appraisal/objectives vehicle is
  the PER self-service appraisal feature (the BSC-based 'Performance Management Framework'
  responsibilities are obsolete and uninstalled); E2's naming should attribute appraisals to
  Core HR/SSHR rather than to a standalone product.
- **VF-6 — VT evidence (IMPLEMENTATION-PHASE ITEMS — narrowed v2.0, adjudicated v3.0).** The v1.0 blanket
  'submission plumbing' diagnosis was superseded by the round-2 root causes (VF-7…VF-10); round 3
  adjudicated them: VF-8 is overturned (Order Import PASS), VF-9 is resolved by a documented one-row
  setup correction (AR AutoInvoice PASS), VF-11 is corrected (a false negative — inventory posting
  PASS inside Vision's own calendars), and VF-7/VF-10 stand as root-caused SR-grade instance defects
  with conclusive evidence. Documentation defects: none.
- **VF-7 — GLLEZL Journal Import (SR-GRADE — conclusive, v3.0).** The GLLEZL spawned binary parses
  legacy positional argv (run_id, source, sus_on, from, to, summary, archive — debug-echo verified);
  the registered SRS order ($SRS$.GLLEZLSRS: Source, Group ID, Post-Errors-to-Suspense,
  Create-Summary, Import-DDF, Access-Set, Ledger) differs; and with the binary order the import
  still exits `gllacc`/`gllmai` ORA-01403 (logs `l7625563.req`, requests 7625621/7625622/7625624).
  v3.0 makes the defect conclusive: the appliance's full GLLEZL request history holds **4,102 runs,
  all Error — zero successes ever**, while every prerequisite is individually verified present
  (access set 1017 in `gl_access_sets` — security_segment_code F, default ledger 1 — with a
  full-privilege `gl_access_set_norm_assign` row over ledger 1, site profile `GL_ACCESS_SET_ID`=1017,
  period Nov-16 open, CCIDs 16902/17021 enabled, Manual/Adjustment seeded, balanced USD rows).
  System-level event-1403 errorstack (armed CDB-wide and PDB-scoped) and a manager-session 10046
  trace both confirm the ORA-01403 is raised and handled inside the spawned process, so the failing
  statement cannot be captured client-side. SR/patch follow-up; interface groups 999101/999105
  staged.
- **VF-8 — Order Import works as installed (OVERTURNED, v3.0).** The v2.0 'broken as installed'
  verdict is overturned: the FDPSTP ORA-06502 was a 15-argument SRS-contract guess, not a program
  defect. The installed `OE_ORDER_IMPORT_MAIN_PVT.ORDER_IMPORT_CONC_PGM` formals (18, per
  `all_arguments`: errbuf; retcode **NUMBER**; p_operating_unit NUMBER; p_order_source,
  p_orig_sys_document_ref, p_operation_code VARCHAR2; …) bind cleanly at the registered 16-argument
  order. Two usage findings en route: p_order_source takes the source **id**, not the name; and
  source 10 'Internal' is requisition-driven — `Pre_Process.Req_Header_Id_derivation` casts
  `orig_sys_document_ref` to a `po_requisition_headers_all.requisition_header_id` (hence
  ORA-06502/01403 for string references) — so general imports must use a general source (seeded
  1023 'Custom Order Entry'), with `unit_list_price` and primary-UOM fixes clearing the earlier
  'Incorrect list or selling price' / 'Invalid unit of measure' line rejections. OEOIMP 7625641
  imported the staged order end-to-end: header 358773 / brw-om-001 ENTERED with one line. The
  v2.0 'zero successful runs in request history' observation stands explained: the appliance's
  users never had occasion to run Order Import.
- **VF-9 — AutoInvoice: AutoAccounting setup correction applied (RESOLVED, v3.0).** The v2.0
  'setup gap' is precisely root-caused and corrected: the REV derivation's SEGMENT2 sources
  `RA_SALESREPS`, and org 204 holds zero salesreps — hence the empty segment in the invalid derived
  combination '01--4110-0000-000' (the explicit `ra_interface_distributions_all` REV row was
  rejected alongside because the same derivation result is validated). One-row setup correction
  applied and documented (reversible): `ra_account_default_segments` gl_default_id 1000 SEGMENT2
  constant '000' — yielding the seeded enabled combination 01-000-4110-0000-000. AutoInvoice then
  imported the staged line end-to-end: trx_number 10047280 / customer_trx_id 1201202, complete=Y,
  REV distribution ccid 125608.
- **VF-10 — RVCTP receiving-processor defect (SR-GRADE — root-caused, v3.0).** The manager-session
  10046 trace (enabled via the request-level `enable_trace` flag) shows the ROI claim statement
  claims **only LPN-context rows** (lpn_group_id/lpn_id/license_plate_number non-null or
  WMS_LPN_CONTENTS_INTERFACE members); standard rows are never claimed (exec r=0), the
  pre-processor marks the header interface row ERROR without creating any `rcv_shipment_headers`
  row (zero INSERTs into it in the whole traced session), and `rvtshiline()` then fails its
  `select nvl(asn_type,'STD') from rcv_shipment_headers where shipment_header_id = :b1` with
  ORA-01403 (RVTSH-140/189) — handled inside the process, invisible to event-1403 errorstack.
  Five row shapes, two routing values, auto-transact variants, two receivers, two transaction
  dates and both BATCH and ONLINE modes tried — the defect is upstream of all of them. SR
  follow-up; interface groups 999401…999411 staged.
- **VF-11 — v2.0 calendar-freeze finding corrected (FALSE NEGATIVE, v3.0).**
  `org_acct_periods.open_flag` holds 'Y'/'N', not 'O' — the v2.0 open-period query required 'O'
  and found none. The earliest unclosed period per org **is** the open one (org 204 Dec-07, org
  207 Oct-10), and the FA book OPS CORP sits open at Sep-2010 exactly as v2.0 recorded. With the
  correct reading, VT-8's misc receipt posted into org 207's Oct-10 period **without any setup
  modification** — mtl_material_transactions 26212144. The GL ledger calendar stands as v2.0
  recorded: NOV-2016 open, Dec-16/Adj-16 future.

## 5. Verification artifacts

Interface rows and created rows left in the instance (verification round 3 markers): the GL interface rows `GL_INTERFACE` groups 999101/999105 (import blocked VF-7, staged for the SR), the AP invoices **brw-e2e-ap-002 = ap_invoices_all 565060** (imported, validated), the AR invoice **brw-ar-001 imported = ra_customer_trx_all 1201202 / trx_number 10047280, complete=Y** with REV distribution ccid 125608, the OM interface order **brw-om-001 imported = oe_order_headers_all 358773, ENTERED**, the booked OM API order **brw-e2e-om-002 = oe_order_headers_all 358770**, the hired employee **BRWE2E* = per_people_f 32849**, the posted FA mass addition **brw-e2e-fa-001 = mass_addition_id 1767530** and its `fa_additions_b`/`fa_books` rows, the PO requisition **533793 / 15906 (APPROVED)**, the posted inventory misc transaction **mtl_material_transactions 26212144** (org 207, item 155, 15-OCT-2010), and the receiving interface groups 999401…999411 (blocked VF-10, staged for the SR). One documented setup correction was applied to the instance (VF-9 resolution, reversible): `ra_account_default_segments` gl_default_id 1000 SEGMENT2 → constant '000'. Exact marker values are quoted in the footer below. Concurrent logs (round 3): `/u01/install/APPS/fs_ne/inst/EBSDB_apps/logs/appl/conc/log/l7625621.req` … `l7625641.req`; the round-3 diagnostics (GLLEZL history census, event-1403 errorstack captures, the manager-session 10046 receiving trace `EBSCDB_ora_14394_ANONY_0917_182500.trc`, the ORDER_IMPORT_CONC_PGM `all_arguments` signature dump and the AutoAccounting setup reads) are reproducible from the harness. The SQL/PLSQL harness (ten self-contained suites plus a summary sweep and a master runner, extended with the round-3 diagnostic and fix-and-run scripts) is preserved on the authoring workstation at `~/ebs-e2e/` for re-runs. No Vision master-data tables were modified; the single setup-table correction is the documented VF-9 row; created rows carry the
BRW-/BRW-E2E- prefixes.

---

Part of the [02-oracle-ebs blueprint](README.md). Platform claims verified against the
[fit-gap register](fit-gap-analysis.md), [module coverage map](module-coverage-map.md) and
[license bill of materials](licensing-bom.md).

*Document Version: 3.0 | Date: 2026-09-18 | **Verification round 3 — eight of the ten paths PASS end-to-end; the v2.0 AR/OM-import/INV blocks resolved and the GL/receiving blocks root-caused to conclusive SR-grade instance defects:** VT-3 AR AutoInvoice **PASS** — VF-9 resolved by the one-row setup correction (the REV derivation's SEGMENT2 sourced RA_SALESREPS and org 204 holds zero salesreps, the exact empty segment in the invalid '01--4110-0000-000'; ra_account_default_segments gl_default_id 1000 SEGMENT2 → constant '000' yields the seeded combination 01-000-4110-0000-000) — RAXMTR 7625631 Normal, trx_number 10047280 / customer_trx_id 1201202 complete=Y, REV ccid 125608; VT-4 Order Import **PASS — VF-8 overturned** (the v2.0 FDPSTP ORA-06502 was a 15-argument SRS guess: the installed OE_ORDER_IMPORT_MAIN_PVT.ORDER_IMPORT_CONC_PGM formals from all_arguments bind at the registered 16-argument order; p_order_source takes the source id, source 10 'Internal' is requisition-driven — Pre_Process casts the reference to a requisition header id — so the staged rows moved to seeded source 1023 'Custom Order Entry' with unit_list_price and primary-UOM fixes; OEOIMP 7625641 Normal → header 358773 ENTERED, line AS18947 ×2 @ 100); VT-8 inventory misc receipt **PASS — VF-11 corrected as a false negative** (org_acct_periods.open_flag holds 'Y'/'N', not 'O'; the earliest unclosed period per org is the open one — org 207 open at Oct-10 — so no setup change was needed: INV_TXN_MANAGER_PUB posted mtl_material_transactions 26212144); VT-1/VT-5/VT-6/VT-9/VT-10 evidence re-inventoried intact; VT-2 GL **BLOCKED conclusively** (VF-7 strengthened: the appliance's GLLEZL history holds 4,102 runs all Error — zero successes ever — with every prerequisite individually verified present; PDB-scoped event-1403 errorstack and manager 10046 traces confirm the ORA-01403 is handled inside the spawned process); VT-7 receiving **BLOCKED with exact root cause** (VF-10: the ROI claim claims only LPN-context rows — exec r=0 in the manager 10046 trace — so no rcv_shipment_headers row is ever created and rvtshiline dies on its asn_type select ORA-01403; five row shapes and both processing modes tried); §1 calendar row corrected; §4 findings VF-6…VF-11 re-adjudicated; §5 artifacts re-inventoried with the one documented setup correction named (request span l7625621…l7625641). Exact instance markers (footer-exempt): BRW-AP-001 / BRW-AP-002 / BRW-AR-001 / BRW-OM-001 / BRW-E2E-OM-002 / BRW-E2E-GL-001 / BRW-E2E-FA-001. Prior v2.0 | Date: 2026-09-18 | **Verification round 2 — end-to-end workflow-path matrix extended 5 → 10 and the v1.0 blocks root-caused:** the transactional matrix gains five paths — VT-6 PO requisition import + approval workflow **PASS** (req 15906 APPROVED end-to-end), VT-7 receiving open interface **BLOCKED** (VF-10 rvtshiline internal error), VT-8 inventory misc transaction **SKIP** (VF-11 calendar freeze), VT-9 Core-HR employee hire via the public API **PASS** (person 32849), VT-10 FA mass additions → post **PASS** (asset BRW-E2E-FA-001 in book OPS CORP) — and the five v1.0 rows re-adjudicated: VT-1 AP **PASS re-confirmed** (invoice BRW-E2E-AP-002 / 565060 via the report-type positional contract), VT-2 GL root cause narrowed (VF-7: GLLEZL binary parses legacy positional argv; SRS order inconsistent; gllacc ORA-01403 persists with a resolvable access set), VT-3 AutoInvoice superseded (VF-9: first successful RAXMTR master runs via the binary argv contract; blocked at the AR AutoAccounting revenue derivation '01--4110-0000-000'), VT-4 Order Import confirmed broken as installed (VF-8: immediate binding fails for every argument arrangement; zero historical successes), VT-5 OM Process_Order **PASS** (resolves v1.0: the installed signature opens p_org_id/p_operating_unit/p_action_commit — no p_commit — and fixed-price lines need unit_list_price; order 358770 booked); findings register extended VF-7…VF-11 (GLLEZL contract inconsistency, OEOIMP binding defect, AutoInvoice master contract + AutoAccounting setup gap, RVCTP internal error, Vision calendar freeze: inventory periods closed org-wide and FA book OPS CORP open at Sep-2010); environment table gains the calendar-freeze rows; §5 artifacts re-inventoried (BRW-E2E-AP-002 / 15906 / 358770 / 32849 / BRW-E2E-FA-001 / GL group 999101; request span l7625553…l7625610). Exact instance markers (footer-exempt): BRW-AP-001 / BRW-AP-002 / BRW-AR-001 / BRW-OM-001 / BRW-E2E-OM-002 / BRW-E2E-GL-001 / BRW-E2E-FA-001. Prior v1.0 | Date: 2026-09-17 | Initial issue — live verification of the blueprint documentation set against the Oracle EBS 12.2.12 Vision instance (platform footprint conformance: 33 of 39 FP rows CONFIRMED across the register's adopted vehicles; findings VF-1 RM&I naming correction, VF-2 ICM/AMW obsolete-not-installed retirement with register re-disposition, VF-3 Site Hub not present, VF-4 GOP standalone annotation, VF-5 E2 naming nuance, VF-6 instance follow-ups; transactional matrix VT-1 AP open-interface invoice PASS end-to-end, VT-2–VT-5 blocked paths evidenced with concurrent logs). Exact instance markers (footer-exempt): BRW-AP-001 / BRW-AR-001 / BRW-OM-001.*
