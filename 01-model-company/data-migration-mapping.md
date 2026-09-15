# BuildRight Depot Corp. — Data Migration Mapping Template

> This document outlines the data mapping standards, data cleansing rules, and validation
> criteria established for the ERP master records. It defines the standard field layouts
> and formatting rules to maintain database integrity.

---

## 1. Migration Scope Summary

| Legacy System | Data Domain | Migration Approach | Timing |
|---|---|---|---|
| Legacy on-premise accounting | GL, AP, AR, FA | Balance migration as of go-live; open items individually | Pilot go-live weekend |
| Standalone POS | Sales history, item master | Summarized daily by store (12 months); detailed last 3 months | Pilot go-live weekend |
| Spreadsheet purchasing | Vendor master, open POs | Active POs migrated; vendor master cleansed | Pilot go-live weekend |
| Separate payroll software | Employee master, YTD earnings | Full employee master to EBS Core HR; year-to-date earnings & deductions to the in-house Payroll PH build for BIR reconciliation (EBS receives postings, not balances) | Pilot go-live weekend |
| Custom ecommerce | Customer/loyalty accounts, order history | Full loyalty member migration; order history last 6 months | Phase 5 (optimization) |
| Manual inventory | On-hand quantities per location | Full wall-to-wall count at go-live; counts loaded as opening balances | Per-wave go-live |

---

## 2. Master Data Migration Templates

### 2.1 Item Master (from POS system + spreadsheets)

| Target Field | Source | Cleansing Rule | Validation |
|---|---|---|---|
| Item Code / SKU | POS item master | Assign new ERP item codes if format changes; maintain cross-reference table | Uniqueness check; no duplicates |
| Item Description | POS item master | Standardize naming convention; trim whitespace; max length per ERP | Non-blank; length check |
| Category / Subcategory | Spreadsheet / manual mapping | Map to new hierarchical category tree (MDM-007); validate all items assigned | Every item in valid category |
| Unit of Measure (UOM) | POS item master | Standardize UOM codes (EA, KG, M, BF, PK); validate catch-weight flag | Valid UOM code; catch-weight items flagged |
| Barcode / GTIN | POS item master | Validate check digits; flag duplicates; standardize to GS1 format | Uniqueness; valid check digit |
| Item Type | Manual classification | Classify as: Standard Stock, Seasonal, Consignment, Non-Stock, Kit, Service, Catch-Weight | Valid type; consignment items linked to vendor |
| Active / Inactive status | POS item master + manual | Items with sales in last 12 months = Active; otherwise = Inactive (retained for history) | Total active = ~35,000 |
| WAC unit cost | Legacy accounting | Take last known cost from accounting system; will be recalculated at first GR in new system | Positive value; reasonable range check |
| SRP (Selling Price) | POS item master | Validate as positive; flag items with margin < 10% for review | Positive; margin check |
| Tax classification | Manual (VATable by default) | Default to VATable; manually classify VAT-exempt items | Valid tax code |
| Catch-weight indicator | Manual classification | Flag items sold by weight/length (lumber, wire, bulk nails) | Boolean; linked to UOM |

**Target record count**: 55,000 (35,000 active + 20,000 inactive/seasonal)

### 2.2 Vendor Master (from purchasing spreadsheets + accounting)

| Target Field | Source | Cleansing Rule | Validation |
|---|---|---|---|
| Vendor Code | Accounting vendor list | Assign new ERP codes or retain existing; maintain cross-reference | Uniqueness |
| Vendor Name | Accounting + PO data | Standardize: trim whitespace, proper case; deduplicate | Non-blank; no duplicates |
| TIN (Tax Identification Number) | Accounting vendor list | Validate format (XXX-XXX-XXX or XXX-XXX-XXX-XXX); flag missing TIN | Valid TIN format; non-blank |
| Business Address | Accounting vendor list | Standardize address format; validate city/province | Non-blank |
| Payment Terms | PO data / contracts | Map to standard terms (Net 30, Net 60, LC, TT); default Net 30 | Valid term code |
| Currency | PO data | PHP for local; USD for import vendors | Valid currency code |
| Bank Account Details | Accounting vendor list | Validate bank name, account number format; flag missing | Format validation |
| EWT Alphanumeric Tax Code (ATC) | Manual classification | Map vendor to correct ATC (WI010 for goods 1%, WI020 for services 2%, etc.) per BIR | Valid ATC code |
| Lead Time (days) | PO data analysis | Calculate average actual lead time from historical POs; validate reasonableness | Positive integer; 1–180 days |
| Vendor Category | Manual mapping | Link to merchandise category for reporting | Valid category |
| Status (Active/Inactive) | Accounting + PO data | Vendors with POs in last 12 months = Active; flag others for review | Boolean |

**Target record count**: ~800–1,000 active vendors (per `model-company-profile.md` §6.5)

### 2.3 Customer Master — Loyalty Members (from ecommerce platform)

| Target Field | Source | Cleansing Rule | Validation |
|---|---|---|---|
| Customer ID | Ecommerce platform | Assign new ERP IDs; maintain cross-reference | Uniqueness |
| Name | Ecommerce registration | Proper case; split into first/last name; deduplicate per fuzzy matching rules (email + phone) | Non-blank |
| Email | Ecommerce registration | Lowercase; validate format; deduplicate | Valid email format; unique |
| Mobile Number | Ecommerce registration | Standardize to +63 format; validate 11-digit PH mobile | Valid PH mobile format |
| Loyalty Tier | Ecommerce platform | Default Bronze; recalculate based on trailing 12-month spend after migration | Valid tier |
| Points Balance | Ecommerce platform | Migrate current outstanding points balance; validate against source total | Non-negative; sum matches source |
| Data Privacy Consent | Ecommerce registration | Migrate consent flag with date and version per RA 10173 | Boolean + date |
| Registration Date | Ecommerce platform | Retain original registration date for tenure calculation | Valid date |

**Target record count**: ~600,000 loyalty members

### 2.4 Employee Master (from payroll software)

| Target Field | Source | Cleansing Rule | Validation |
|---|---|---|---|
| Employee ID | Payroll system | Retain or assign new; maintain cross-reference | Uniqueness |
| Name | Payroll system | Proper case; split first/middle/last | Non-blank |
| Entity Assignment | Payroll system | Map to correct legal entity (5 entities) | Valid entity |
| Department / Position | Payroll system | Map to new department structure and position codes | Valid dept + position |
| Hire Date | Payroll system | Retain original hire date for seniority/benefits | Valid date |
| Salary / Rate | Payroll system | Migrate current basic salary; validate range | Positive; reasonable range |
| Tax Status (BIR) | Payroll system | Map to BIR tax status codes (ME, S, HF, etc.) | Valid tax status |
| SSS / PhilHealth / Pag-IBIG numbers | Payroll system | Validate format; flag missing | Valid format per agency |
| TIN | Payroll system | Validate format (XXX-XXX-XXX or XXX-XXX-XXX-XXX) | Valid TIN format |
| Bank Account | Payroll system | Validate bank name + account number | Format validation |
| Employee Type | Payroll system | Regular, Probationary, Fixed-term, Project-based | Valid type |
| YTD Earnings & Deductions | Payroll system | Load into the in-house Payroll PH build — not EBS (EBS receives postings, not balances); retained for BIR annual reconciliation (1702/1604) | Sum validates to payroll register |
| Leave Balances | Payroll system | Migrate VL/SL balances as of go-live | Non-negative |

**Target record count**: 6,911 employees

### 2.5 Financial Balances (from legacy accounting)

| Target Field | Source | Cleansing Rule | Validation |
|---|---|---|---|
| GL Account Code | Legacy COA | Map legacy account codes to new COA structure (shared COA with entity segment); maintain cross-reference table | Every legacy account mapped to new account; uniqueness check |
| GL Account Description | Legacy COA | Standardize naming; assign to correct financial statement line (BS, IS, CF) | Non-blank; valid FS line |
| GL Account Type | Manual classification | Classify as: Asset, Liability, Equity, Revenue, Expense; map to PFRS/IFRS category | Valid account type |
| Entity Segment | Manual mapping | Assign each GL account to the correct legal entity (5 entities); shared accounts marked as intercompany | Valid entity code |
| GL Account Balances | Legacy trial balance | Map to new COA; load as opening balances per entity | Trial balance balances (debit = credit) |
| Open AP Invoices | Legacy AP subledger | Migrate individually with vendor, amount, due date, PO reference | AP subledger = GL AP balance |
| Open AR Invoices | Legacy AR subledger | Migrate individually with customer, amount, due date | AR subledger = GL AR balance |
| Fixed Asset Register | Legacy FA register | Migrate per asset: cost, accumulated depreciation, NBV, useful life remaining | FA register = GL FA balances |
| Open Purchase Orders | Spreadsheet purchasing | Migrate active POs with line items, quantities received and remaining | PO liability = GRNI balance |
| Bank Account Balances | Legacy GL + bank statements | Reconcile to most recent bank statement before migration | GL cash = bank balance ± outstanding |

**Target record count**: ~2,000–3,000 GL accounts across 5 entities; ~open items variable

### 2.6 Pricing Master (from POS system + spreadsheets)

| Target Field | Source | Cleansing Rule | Validation |
|---|---|---|---|
| SRP (Standard Retail Price) | POS item master | Validate as positive; flag items with margin < 10% for review | Positive; margin check |
| Trade Price (B2B) | Spreadsheets / contracts | Map to trade customer price list; validate discount % from SRP (5–15%) | Positive; ≤ SRP |
| Corporate / Project Price | Spreadsheets / contracts | Migrate negotiated prices per corporate account; validate against contract terms | Positive; linked to valid customer |
| Quantity Break Pricing | POS system / spreadsheets | Migrate tiered pricing rules (e.g., buy 10+ get 5% off); validate break points and discounts | Valid break quantities; discount % reasonable |
| Promotional Pricing | Spreadsheets / calendars | Migrate active promotions with start/end dates, applicable SKUs, and discount amounts | Valid date range; linked to valid items |
| Clearance / Markdown Pricing | Spreadsheets | Migrate current markdown prices; flag items with margin < 0% for review | Positive; linked to valid items |

**Target record count**: 35,000 SRP records + ~5,200 trade price records + ~200 corporate price records + ~500 quantity break rules + ~50 active promotions

### 2.7 Inventory Opening Balances (from physical counts)

| Target Field | Source | Cleansing Rule | Validation |
|---|---|---|---|
| Location | Physical count sheet | Map to new location master (200 stores + 4 DCs + HQ) | Valid location code |
| Item / SKU | Physical count | Match to migrated item master | Valid item code |
| Quantity on Hand | Physical count (wall-to-wall) | Load as opening balance per location per SKU | Positive or zero |
| Unit Cost (WAC) | Migrated item master | Apply current WAC from item master to opening quantity | Positive; WAC × qty = total inventory value |
| Consignment flag | Physical count + vendor master | Flag vendor-owned items separately from owned inventory | Boolean; linked to vendor |
| Batch / Lot (if applicable) | Physical count | Capture lot/batch numbers for lot-tracked items during count | Alphanumeric; non-blank for lot items |
| Expiry Date (if applicable) | Physical count | Capture for date-sensitive items during count | Valid date; future date |

**Load approach**: Full wall-to-wall physical count at each location immediately before go-live; counts entered into system as opening balances. No historical inventory transactions migrated — new system starts with perpetual inventory from go-live forward.

---

## 3. Data Cleansing Rules

| Rule | Applies To | Description |
|---|---|---|
| **Deduplication** | Items, Vendors, Customers | Fuzzy matching on name + key attribute (items: barcode, vendors: TIN, customers: email/phone); merge duplicates before migration; retain most recently active record |
| **TIN Validation** | Vendors, Employees | Validate Philippine TIN format (XXX-XXX-XXX or XXX-XXX-XXX-XXX); flag invalid for manual correction |
| **Blanket Default Values** | All masters | Where source data is missing, apply configured defaults (e.g., payment terms = Net 30, currency = PHP, UOM = EA, tax = VATable) |
| **Trim & Standardize** | All text fields | Remove leading/trailing whitespace; standardize casing (proper case for names, uppercase for codes) |
| **Range Validation** | Numeric fields | Validate that costs, prices, and quantities are within reasonable ranges; flag outliers for manual review |
| **Referential Integrity** | All transactional data | Every transaction must reference valid master records (vendor, customer, item, location, employee) |
| **Historical Data Cutoff** | Transactions | Summarize historical data older than 12 months at daily level; keep detailed records for last 3–12 months only |

---

## 4. Migration Validation Checklist

| Checkpoint | Method | Success Criteria |
|---|---|---|
| **Record count reconciliation** | Source count = Target count for each data domain | 100% match |
| **Financial balance reconciliation** | Legacy trial balance = New system opening trial balance (per entity) | Debits = Credits; net income matches |
| **AP subledger reconciliation** | Open AP in legacy = Open AP in new system | Total matches; vendor-level detail matches |
| **AR subledger reconciliation** | Open AR in legacy = Open AR in new system | Total matches; customer-level detail matches |
| **Inventory valuation reconciliation** | Legacy inventory value = New system opening inventory (per location) | Total matches within 1% (tolerance for count adjustments) |
| **Employee master completeness** | All active employees migrated with valid mandatory fields | Zero employees missing SSS/PhilHealth/Pag-IBIG/TIN |
| **Loyalty points reconciliation** | Source total outstanding points = New system total points liability | Total matches |
| **Vendor master completeness** | All active vendors migrated with valid TIN and payment terms | Zero vendors missing TIN |
| **Parallel run: payroll** | One payroll cycle in both legacy and new system | Net pay matches per employee within PHP 1 |
| **Parallel run: month-end** | One month-end close in both systems | Financial statements match within tolerance |



---

*Date: 2026-09-14 (v2.7 — structure-promotion re-base: the target employee-record count re-based 6,762 → 6,911 employees, per the promoted HQ 511 / total 6,911 canon (profile v3.0, TO v2.3). No mapping-row routing changes. Prior v2.6 — twenty-first-wave consistency review: §1 scope row and §2.4 YTD row re-pointed to the two-tier sourcing doctrine — payroll year-to-date earnings & deductions load into the in-house Payroll PH build, not EBS; EBS receives postings, not balances, mirroring 02-oracle-ebs/data-migration.md row 11 — the doctrine commits re-pointed the blueprint side but never reached this template. Prior v2.5 — consistency review #19: §2 trade price-record count aligned to the canonical B2B scheme (~5,000 → ~5,200 trade price records, matching §9.2 of the profile). Prior v2.4 — consistency review #15: the §2.1 employee-master TIN rule aligned to the both-formats standard the rest of the file already carries (COM-011 / §TIN Validation): `Validate format (XXX-XXX-XXX)` → `(XXX-XXX-XXX or XXX-XXX-XXX-XXX)`; the same repair was applied to the single-format TIN checks in PA-17.3, PA-22.2, and PA-29.1. Prior v2.3 — §2.2 vendor-master target count reconciled to `model-company-profile.md` §6.5 range `~800–1,000 active vendors` (was `~1,000`); vendor TIN cleansing rule updated to accept both Philippine TIN formats (`XXX-XXX-XXX or XXX-XXX-XXX-XXX`) per COM-011 / §3, was 12-digit only. Prior v2.2: counts reconciled with README.md; canonical glossary reference added)*
