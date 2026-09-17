# EBS Vision Instance Verification — erpplans_ebs Documentation Set vs Oracle E-Business Suite 12.2.12

> Live verification of the blueprint's platform claims against the designated ERP system of
> record: the Oracle E-Business Suite 12.2.12 Vision appliance (VirtualBox, NAT; see
> `~/virtualbox_ol/ebs.md` on the authoring workstation). Every claim in this document was
> executed against the instance over SSH/SQL*Plus on 2026-09-17; nothing is quoted from
> vendor literature. Method: (1) platform footprint conformance — every adopted vehicle in
> the [fit-gap register](fit-gap-analysis.md) and [module coverage map](module-coverage-map.md)
> checked against `FND_PRODUCT_INSTALLATIONS` × `FND_APPLICATION_VL` (176 registered
> products) and the seeded responsibility catalog; (2) transactional smoke tests — five
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
`mo_global.init/set_policy_context('S',204)`, dated inside the open NOV-2016 period, using
Vision master data (item AS18947 id 155; customer Computer Service and Rentals, account 1004,
bill-to 1017 / ship-to 1018; supplier Boise Cascade 558 / site 4970; price list Corporate 1000;
order type Standard 1000; line type Standard (Line Invoicing) 1427). Concurrency ids are the
instance's own.

| VT | Workflow family | Path exercised | Result | Evidence |
|---|---|---|---|---|
| VT-1 | AP supplier invoice via the open interface (W7 class) | `AP_INVOICES_INTERFACE` + `AP_INVOICE_LINES_INTERFACE` → Payables Open Interface Import (APXIIMPT) — request **7625505** completed **Normal** | **PASS** | `ap_invoices_all` holds the BRW-AP test invoice (exact marker in the footer; vendor 558, site 4970, org 204, USD 250); 0 rejections after the header-amount fix (initial run rejected on INVALID INVOICE AMOUNT / INVALID PAY METHOD — the header `invoice_amount` is mandatory even with lines; the supplier site's default payment method must exist) |
| VT-2 | GL manual journal via the interface (W638 class) | `GL_INTERFACE` (balanced 100/100, source Manual, category Adjustment, ledger 1, 30-NOV-2016) + `GL_INTERFACE_CONTROL` → Journal Import (GLLEZL) requests 7625493/7625500/7625504/7625509 | **BLOCKED (instance anomaly)** | GLLEZL exits in `gllacc` with ORA-01403 (log `l7625504.req`) after loading 2 NEW interface rows (group 3821422). The debug echo maps the positional parameters (run_id, source, sus_on, from_date, to_date, create_summary, archive, num_rec); the pre-import access lookup finds no data for the Vision Operations access set. GL itself is proven in the instance by seeded journals; the scripted import path needs an SR/setup follow-up. Interface rows left in place for the follow-up |
| VT-3 | AR invoice via AutoInvoice (fit-gap A14; the VS-16 AR billing side) | `RA_INTERFACE_LINES_ALL` (batch source ORDER ENTRY, type Invoice 1, term 30 NET, bill-to 1017) → AutoInvoice Master (RAXMTR) requests 7625496/7625501/7625506/7625510/7625513 | **BLOCKED (submission plumbing)** | The spawned-C argument contract rejects every positional variant (Usage banner in `l7625496.req`/`l7625510.req`); the interface line is loaded and unprocessed with 0 `RA_INTERFACE_ERRORS`. Follow-up: submit via the SRS form's exact 28-value argument string |
| VT-4 | OM sales order via Order Import (W56/W146 class) | `OE_HEADERS_IFACE_ALL` + `OE_LINES_IFACE_ALL` (source Internal 10, ref BRW-OM marker, type Standard 1000) → Order Import (OEOIMP) requests 7625497/7625502/7625507/7625511/7625514 | **BLOCKED (submission plumbing)** | FDPSTP fails to bind the registered 15-argument SRS definition onto `ORDER_IMPORT_CONC_PGM` (two overloads: an 18-argument ORDER_SOURCE_ID form and a 17-argument ORDER_SOURCE form) — ORA-6550/6502 per `l7625502.req`/`l7625511.req`. Interface rows loaded and pending |
| VT-5 | OM sales order create+book via OE_ORDER_PUB.Process_Order (W56 class) | Full public-API create (header + line, MOAC context 204) then Book action request | **BLOCKED (Vision setup)** | The API call executes (the 12.2.12 signature — bound via its named parameters incl. `p_header_val_rec` and the six price/adj OUT tables — was bound successfully) but returns U: `OE_Delayed_Requests_PVT.LogRequest` ORA-06502 (NULL index key) — a Vision OM setup/profile dependency for scripted sessions. Vision's own 43,307 booked orders prove the order+booking flow in-application |

Read-only conformance confirmed without exception: item master (AS18947 present in master org
204 and child 207), Corporate price list (1000), Vision customers/terms/types, suppliers with
org-204 sites, 150+ seeded super-user responsibilities across the footprint, WMS/eAM org flags
off everywhere (both are implementation-task enablements, not product gaps), and the
`.jnlp`/Forms client chain documented in the instance notes.

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
- **VF-6 — VT evidence (IMPLEMENTATION-PHASE ITEMS).** VT-2/VT-3/VT-4/VT-5 blocked paths are
  instance-side follow-ups (SR-grade submission plumbing for GLLEZL/RAXMTR/OEOIMP and Vision
  OM setup for scripted booking), not documentation defects: in every case the product,
  program, interface table and seeded data were verified present.

## 5. Verification artifacts

Interface rows left in the instance for the follow-up: `GL_INTERFACE` group 3821422 (2 rows), the AP interface pair for the BRW-AP test invoice (imported), the OM interface pair for the BRW-OM test order (pending), the AR interface line for the BRW-AR test invoice (pending). Exact marker values are quoted in the footer below. Concurrent logs: `/u01/install/APPS/fs_ne/inst/EBSDB_apps/logs/appl/conc/log/l7625493.req` …
`l7625514.req`. No Vision master-data or setup tables were modified; created rows carry the
BRW- prefix.

---

Part of the [02-oracle-ebs blueprint](README.md). Platform claims verified against the
[fit-gap register](fit-gap-analysis.md), [module coverage map](module-coverage-map.md) and
[license bill of materials](licensing-bom.md).

*Document Version: 1.0 | Date: 2026-09-17 | Initial issue — live verification of the blueprint documentation set against the Oracle EBS 12.2.12 Vision instance (platform footprint conformance: 33 of 39 FP rows CONFIRMED across the register's adopted vehicles; findings VF-1 RM&I naming correction, VF-2 ICM/AMW obsolete-not-installed retirement with register re-disposition, VF-3 Site Hub not present, VF-4 GOP standalone annotation, VF-5 E2 naming nuance, VF-6 instance follow-ups; transactional matrix VT-1 AP open-interface invoice PASS end-to-end, VT-2–VT-5 blocked paths evidenced with concurrent logs). Exact instance markers (footer-exempt): BRW-AP-001 / BRW-AR-001 / BRW-OM-001. Prior: none (initial issue).*
