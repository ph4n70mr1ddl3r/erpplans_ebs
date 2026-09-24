#!/usr/bin/env python3
"""Role-anchoring worklist remediation sweep (batch 31; 2026-09-23, by direction).

Clears the zero-anchor worklist emitted by the role-coverage matrix's
Role-Anchoring Contract section: every chartered role must carry >=1 explicit
RACI anchor (Owner / Participant / Step-R / Step-A) so headcount optimization
is scientific. Three mechanisms, each a recorded governance decision:

  1. Participants-line anchors — the role's chartered title appended to the
     Participants line of the workflow(s) its TO §5.3 mandate (or roster
     mandate) names as its operating home. Ownership and step cells are
     untouched (no displaced accountability; time-estimate arithmetic
     unchanged).
  2. Alias promotions — corpus vocabulary that already names the function
     ('Payroll Accountant', 'Marketing Data Analyst', 'Ecommerce Customer
     Support', 'Integration Specialist', picker/packer forms, 'Assistant
     Controller') promoted from the department/workforce buckets to the
     chartered title it actually denotes, plus re-pointing the wave-36
     department-grain picker/packer mappings to the §7.3 DC roster roles.
  3. Store-roster fragment re-scope — three §7.2 staffing-note fragments
     ('Receiving pair (lead clerk + 1)', 'Sales Associates + 1 Stock
     Associate each', 'holds Safety Officer 1 duty') are roster prose, not
     roles; parse_toc now skips them instead of minting phantom chartered
     titles that could never be anchored.

Idempotent: re-running is a no-op. Every edit asserts its anchor text; any
drift fails loudly rather than mis-anchoring.
"""
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WF = os.path.join(REPO, "01-model-company", "workflows")
GEN = os.path.join(REPO, "07-methodology", "generate-role-coverage.py")

# --- 1. Participants-line anchors -------------------------------------------
# (file, unique substring of the target Participants line, [roles to append])
PARTICIPANT_ADDITIONS = [
    # Finance & Accounting
    ("VS-17-record-to-report/PA-17.4-fpanda-and-reporting.md",
     "Chief Accountant, Accounting Manager, Tax Compliance Manager (PAS 12 interplay)",
     ["Technical Accounting Manager", "Accounting Policy Analyst"]),
    ("VS-17-record-to-report/PA-17.4-fpanda-and-reporting.md",
     "Chief Accountant, AP Supervisor, AR Supervisor, Treasury Analyst, Tax Accountant, Cost Accountant, GL Accountant, CFO",
     ["Assistant Controller"]),  # short form; aliased to the register title
    ("VS-17-record-to-report/PA-17.4-fpanda-and-reporting.md",
     "Controller, CFO, Department Heads, Category Managers (merchandising budget)",
     ["Senior FP&A Analyst"]),
    ("VS-33-strategic-planning/PA-33.2-corporate-performance-management.md",
     "FP&A, CEO, COO, CMO, VP Store Operations",
     ["Senior FP&A Analyst", "CPM (Corporate Performance Management) Analyst"]),
    ("VS-18-treasury-cash/PA-18.2-banking-and-payments.md",
     "Import Coordinator, Buyer, Bank, Finance",
     ["Banking & Cash-Management Specialist"]),
    ("VS-18-treasury-cash/PA-18.2-banking-and-payments.md",
     "Cash Office Clerk, Store Manager, Regional Manager (approval > PHP 5,000)",
     ["Banking & Cash-Management Specialist"]),
    ("VS-79-tax-management-bir-reporting/PA-79.1-indirect-tax-vat-and-einvoicing.md",
     "Tax Manager, GL Accountant, AP/AR, Tax Accountant",
     ["Tax Compliance & eFPS Specialist"]),
    ("VS-79-tax-management-bir-reporting/PA-79.3-income-tax-local-tax-and-audit-defense.md",
     "Tax Manager, GL, Tax Accountant, External Auditor",
     ["Tax Compliance & eFPS Specialist"]),
    ("VS-110-freight-procurement-carrier-management-and-freight-audit/PA-110.3-freight-audit-payment-and-freight-cost-analytics.md",
     "Logistics (links to VS-06), FP&A (links to VS-17.4/VS-33.2), BI (links to VS-28.1)",
     ["DC Cost-to-Serve Analyst"]),
    ("VS-61-fuel-fleet-cost-management/PA-61.3-fleet-total-cost-analytics.md",
     "| **Participants** | VP Supply Chain, CFO |",
     ["DC Cost-to-Serve Analyst"]),
    # Human Resources
    ("VS-19-hire-to-retire/PA-19.2-payroll-and-compensation.md",
     "Payroll Officer, HR Assistant, Department Heads (OT/leave approval), Finance (bank file)",
     ["Payroll Supervisor", "Payroll & Statutory Remittance Officer"]),
    ("VS-19-hire-to-retire/PA-19.2-payroll-and-compensation.md",
     "HR Business Partner (requester), Finance Manager (approver), Payroll Specialist (processor)",
     ["Payroll Supervisor"]),
    ("VS-102-compensation-benefits-total-rewards/PA-102.1-job-architecture-pay-structure-and-market-benchmarking.md",
     "C&B Manager, HR Business Partners, Hiring Managers, Master Data (links to VS-29)",
     ["Compensation Analyst"]),
    ("VS-102-compensation-benefits-total-rewards/PA-102.1-job-architecture-pay-structure-and-market-benchmarking.md",
     "C&B Manager, CHRO, CFO, FP&A (links to VS-17.4), Payroll (links to VS-19.2)",
     ["Compensation Analyst"]),
    ("VS-19-hire-to-retire/PA-19.3-workforce-management.md",
     "Store Manager, Assistant Store Manager, Department Supervisors, HR Assistant",
     ["Timekeeping & Attendance Analyst"]),
    ("VS-19-hire-to-retire/PA-19.3-workforce-management.md",
     "Employee (R for self-service), Department Supervisor (R for approval), HR Supervisor, Payroll Specialist (I)",
     ["Timekeeping & Attendance Analyst"]),
    ("VS-121-talent-acquisition-employer-brand-candidate-experience/PA-121.2-candidate-experience-sourcing-and-selection-operations.md",
     "TA Sourcing, Recruiting (links to VS-19.1), Hiring Managers (links to VS-07/VS-19), Analytics (links to VS-28.1), Loyalty/CRM (links to VS-13)",
     ["Sourcing & Screening Coordinator"]),
    ("VS-121-talent-acquisition-employer-brand-candidate-experience/PA-121.2-candidate-experience-sourcing-and-selection-operations.md",
     "Recruiting, Hiring Managers (links to VS-07/VS-19), TA Operations, Trade/Technical assessors",
     ["TA Coordinator"]),
    # Supply Chain & Logistics
    ("VS-02-supply-planning/PA-02.1-demand-forecasting-and-sandop.md",
     "Demand Planner, Supply Planner, Category Manager, Pricing Analyst",
     ["Senior Demand Planner"]),
    ("VS-02-supply-planning/PA-02.1-demand-forecasting-and-sandop.md",
     "CEO, COO, CFO, VP Merchandising, VP Store Operations, Supply Planning Manager, Demand Planner, Category Managers",
     ["Senior Demand Planner"]),
    ("VS-04-dc-warehouse/PA-04.3-dc-operations-management.md",
     "DC Shift Supervisors, DC Receiving Supervisor, DC Dispatch Supervisor, VP Supply Chain, Supply Planning Manager",
     ["DC Operations Analyst"]),
    ("VS-04-dc-warehouse/PA-04.2-dc-outbound-operations.md",
     "DC Operations Manager, Warehouse Planner, WMS Analyst, Stock Associates",
     ["DC Operations Analyst"]),
    ("VS-03-vendor-management/PA-03.2-purchase-order-cycle.md",
     "System (auto-suggest), Buyer, Category Manager (approval if > PHP 50K)",
     ["Purchasing / PO Specialist"]),
    ("VS-03-vendor-management/PA-03.2-purchase-order-cycle.md",
     "Buyer, Import Coordinator, Finance (LC), Customs Broker, Warehouse (receiving)",
     ["Purchasing / PO Specialist"]),
    ("VS-03-vendor-management/PA-03.2-purchase-order-cycle.md",
     "Buyer, Category Manager, VP Merchandising, Finance (budget), Vendor",
     ["Purchasing / PO Specialist"]),
    ("VS-02-supply-planning/PA-02.2-import-and-customs-operations.md",
     "Buyer, Import Coordinator, Freight Forwarder, Customs Broker, Finance, DC Receiving",
     ["Import Documentation Specialist"]),
    ("VS-02-supply-planning/PA-02.2-import-and-customs-operations.md",
     "Buyer, Insurance Provider, Finance, Freight Forwarder",
     ["Import Documentation Specialist"]),
    ("VS-07-store-operations/PA-07.3-store-receiving-and-replenishment.md",
     "Department Supervisor, Stock Associate, Merchandise Planner, Store Manager, Regional Manager",
     ["Replenishment & Allocation Analyst"]),
    ("VS-64-seasonal-merchandise-clearance/PA-64.2-markdown-clearance-execution.md",
     "Category Mgr, Pricing Analyst, Merch Planner",
     ["Promotions Specialist", "Promotions & Vendor-Funding Coordinator"]),
    # Marketing
    ("VS-10-ecommerce-digital/PA-10.1-ecommerce-platform-operations.md",
     "Customer Experience Representative, Category Manager, Vendor Manager",
     ["Ecommerce Marketing Specialist"]),
    ("VS-48-retail-media-network/PA-48.2-vendor-advertising-campaign-execution.md",
     "Account Manager, Creative Designer, Vendor",
     ["Retail Media Operations Specialist"]),
    ("VS-48-retail-media-network/PA-48.3-retail-media-revenue-analytics.md",
     "Marketing Manager, Digital Marketing Manager, Category Manager",
     ["Retail Media Operations Specialist"]),
    # Store Operations
    ("VS-63-store-communication-task-management/PA-63.1-hq-store-communication.md",
     "VP Corp Comms, COO, Regional Ops Manager",
     ["Field Communications Manager"]),
    ("VS-138-integrated-facilities-management-workplace-services-and-building-automation/PA-138.1-facilities-management-strategy-ifm-provider-and-sla-governance.md",
     "COO, Store Ops (VS-07), Real Estate (VS-97/VS-20), Procurement (VS-34), Finance (VS-17.4)",
     ["Facilities Coordination Specialist"]),
    ("VS-138-integrated-facilities-management-workplace-services-and-building-automation/PA-138.2-hard-and-soft-fm-service-operations.md",
     "Site staff (VS-07/VS-04), Provider workforce (VS-98), HSE (VS-24), Store Ops",
     ["Facilities Coordination Specialist"]),
    # Facilities & Real Estate
    ("VS-138-integrated-facilities-management-workplace-services-and-building-automation/PA-138.1-facilities-management-strategy-ifm-provider-and-sla-governance.md",
     "Providers/contractors, Store Ops (VS-07), DC Ops (VS-04), HSE (VS-24), Calibration (VS-115)",
     ["Maintenance & Projects Coordinator"]),
    ("VS-109-store-remodel-renovation-lifecycle-refurbishment/PA-109.1-remodel-strategy-portfolio-planning-and-scope-definition.md",
     "Project Manager (links to VS-112), Store Manager (links to VS-07), Contractor",
     ["Maintenance & Projects Coordinator"]),
    ("VS-97-corporate-real-estate-property-portfolio/PA-97.1-property-acquisition-investment-portfolio-strategy.md",
     "Director, Facilities & Real Estate, Real Estate Investment Mgr, Finance/Treasury (links to VS-18), Strategy (links to VS-33), Store Ops (links to VS-37), Legal",
     ["Real-Estate & Site-Selection Analyst"]),
    ("VS-20-real-estate-construction/PA-20.1-site-selection-and-lease-management.md",
     "Property Acquisition Manager, Finance (ROI analysis), CEO/Board (approval)",
     ["Real-Estate & Site-Selection Analyst"]),
    # Legal & Compliance
    ("VS-173-investor-relations-capital-markets-and-securities-disclosure/PA-173.2-corporate-disclosure-securities-and-regulatory-compliance.md",
     "Legal (VS-100), Compliance (VS-22), CFO/CEO, Disclosure Committee, Internal Audit (VS-21)",
     ["Corporate Secretary Analyst"]),
    ("VS-173-investor-relations-capital-markets-and-securities-disclosure/PA-173.2-corporate-disclosure-securities-and-regulatory-compliance.md",
     "R2R (VS-17), Legal (VS-100), Compliance (VS-22), Treasury (VS-18), ESG (VS-25), External Auditor, Governance (VS-36)",
     ["Corporate Secretary Analyst"]),
    ("VS-17-record-to-report/PA-17.1-gl-and-financial-close.md",
     "W230",
     ["Contracts & Commercial Manager (Senior Counsel)"]),  # W230 legal-review gate lives in PA-17.1 — line located by its own rule below
    # Internal Audit & Risk
    ("VS-21-internal-audit-risk/PA-21.1-audit-planning-and-execution.md",
     "Audit Team, Board Audit Committee, CEO, CFO",
     ["Audit Manager"]),
    ("VS-21-internal-audit-risk/PA-21.1-audit-planning-and-execution.md",
     "Audit Team, Store/DC Manager (Auditee)",
     ["Audit Manager", "Field Compliance Auditor"]),
    ("VS-119-whistleblower-ethics-and-corporate-integrity-speak-up-program/PA-119.2-investigation-case-management-and-retaliation-protection.md",
     "Lead Investigator, Ethics & Compliance Officer",
     ["Forensic / Fraud Investigator"], 2),  # both investigation workflows
    ("VS-23-loss-prevention/PA-23.1-exception-monitoring-and-investigation.md",
     "LP Investigator, HR Manager, Legal Counsel, Store Manager, Finance Controller, Union Representative (if applicable)",
     ["Forensic / Fraud Investigator"]),
    ("VS-22-compliance-regulatory/PA-22.2-government-audit-and-inspection-response.md",
     "Tax Accountant, Controller, CFO, Chief Accountant, AP Clerk, AR Clerk, IT, Legal",
     ["Operations Compliance Lead"]),
    ("VS-177-field-retail-operations-regional-district-management-and-multi-store-execution/PA-177.2-store-visit-field-coaching-and-retail-standards-execution.md",
     "Director Field Retail Operations, Store Managers (VS-07), Analytics (VS-28), Travel/Fleet (VS-06/VS-61)",
     ["Operations Compliance Lead", "Field Compliance Auditor"]),
    ("VS-177-field-retail-operations-regional-district-management-and-multi-store-execution/PA-177.2-store-visit-field-coaching-and-retail-standards-execution.md",
     "Store Manager (VS-07), Department Supervisors, LP (VS-23), CX (VS-13), Facilities (VS-138)",
     ["Field Compliance Auditor"]),
    # Customer Service
    ("VS-11-trade-project-wholesale/PA-11.1-trade-account-management.md",
     "Customer (B2B), Sales Associate/Store, AR Analyst, Credit Manager, AP Analyst (for vendor-side resolution)",
     ["B2B Support Representative"]),
    ("VS-11-trade-project-wholesale/PA-11.3-wholesale-operations.md",
     "B2B Sales Manager, Sales Representative, Category Manager (A for below-threshold pricing)",
     ["B2B Support Representative"]),
    ("VS-13-customer-experience/PA-13.1-customer-support-and-complaints.md",
     "CSR, CS Manager, Department Supervisor, Store Manager, Buyer, Call Center Agent, Logistics",
     ["Quality & Workforce Analyst"]),
    # Regional Loss Prevention
    ("VS-23-loss-prevention/PA-23.1-exception-monitoring-and-investigation.md",
     "Store Manager, LP Analyst, POS System Administrator, Finance Controller",
     ["Senior LP Analytics Analyst"]),
    # Strategy / Corporate Planning
    ("VS-33-strategic-planning/PA-33.2-corporate-performance-management.md",
     "CFO, CEO, Corporate Secretary, Board of Directors",
     ["CPM (Corporate Performance Management) Analyst"]),
    ("VS-33-strategic-planning/PA-33.1-annual-business-planning.md",
     "CEO, CFO, COO, CIO, CMO, CHRO, VP Legal, VP Supply Chain",
     ["Strategy Analyst"]),
    ("VS-33-strategic-planning/PA-33.3-competitive-intelligence.md",
     "Category Managers, Regional Managers, Pricing Analysts, Store Managers",
     ["Strategy Analyst"]),
    ("VS-30-innovation-digital/PA-30.3-document-and-knowledge-management.md",
     "End Users, ERP Administrator",
     ["Business Process & IMS Lead", "Document Control Coordinator"]),
    ("VS-133-operational-excellence-process-mining-continuous-improvement/PA-133.1-opex-strategy-governance-and-improvement-methodology.md",
     "All process owners (function VPs), Enterprise Architecture (links to VS-113), Master Data (links to VS-29)",
     ["Business Process & IMS Lead"]),
    ("VS-88-document-control-records-retention/PA-88.1-document-classification-versioning-taxonomy.md",
     "Records Mgr, Compliance, IT, Department Owners",
     ["Document Control Coordinator"]),
    ("VS-88-document-control-records-retention/PA-88.1-document-classification-versioning-taxonomy.md",
     "Document Owner, Records Manager",
     ["Document Control Coordinator"]),
    # Information Technology (product-model seats)
    ("VS-27-it-operations-security/PA-27.2-infrastructure-and-platform.md",
     "Cloud Architect, Database Administrator, Network Engineer, CIO, Finance (Budgeting)",
     ["IAP Integration Engineer", "IAP Integration Support Engineer"]),
    # DC roster (explicit anchors alongside the alias promotions)
    ("VS-04-dc-warehouse/PA-04.2-dc-outbound-operations.md",
     "DC Dispatch Supervisor, DC Supervisor, Loaders, Drivers, Fleet Manager, Supply Planner",
     ["Assistant DC Manager — Outbound", "Tile & Heavy/Breakbulk Crew"]),
    ("VS-04-dc-warehouse/PA-04.1-dc-inbound-operations.md",
     "Receiving Clerk, Quality Checker, Putaway Staff, DC Supervisor, Buyer (if discrepancy)",
     ["Special Handling Lead", "Discrepancy Analysts"]),
    ("VS-04-dc-warehouse/PA-04.3-dc-operations-management.md",
     "DC Shift Supervisors (2 per DC), DC Receiving Supervisor, DC Dispatch Supervisor, DC Receiving Clerks, Putaway Staff, Pickers, Loaders, Quality Checkers, Yard Staff, Forklift Operators, Cross-Dock Coordinator, Gate Guard",
     ["DC Office Administrator"]),
    ("VS-138-integrated-facilities-management-workplace-services-and-building-automation/PA-138.2-hard-and-soft-fm-service-operations.md",
     "Site staff (VS-07/VS-04), Waste hauler (VS-73), Utility providers, HSE (VS-24.3)",
     ["Facilities/Utility (DC)"]),
]

# --- 2. Alias promotions ------------------------------------------------------
# New ROLE_ALIASES entries (inserted after the DC block): corpus form → the
# chartered title it denotes. 'DC:'/'STORE:' targets are roster roles.
NEW_ALIASES = {
    "picker": "DC:Order Pickers",
    "pickers": "DC:Order Pickers",
    "packer": "DC:Packers / Load Builders",
    "packers": "DC:Packers / Load Builders",
    "load builder": "DC:Packers / Load Builders",
    "load builders": "DC:Packers / Load Builders",
    "cross-dock coordinator": "DC:Cross-Dock Team",
    "cross-dock team": "DC:Cross-Dock Team",
    "dc outbound supervisor": "DC:Assistant DC Manager — Outbound",
    "outbound supervisor": "DC:Assistant DC Manager — Outbound",
    "payroll accountant": "Payroll Accounting Liaison",
    "assistant controller": "Manager, GL & Consolidation (Assistant Controller)",
    "marketing data analyst": "Insights Analyst",
    "ecommerce customer support": "Ecommerce Support Specialist",
    "integration specialist": "IAP Integration Support Engineer",
    "dc packer": "DC:Packers / Load Builders",
    "dc pick staff": "DC:Order Pickers",
    "dc picker": "DC:Order Pickers",
    "outbound picker": "DC:Order Pickers",
    "warehouse picker": "DC:Order Pickers",
}

# Wave-36 department-grain promotions: picker/packer forms moved OUT of
# DEPT_ACTORS_W36 (the 'Supply Chain & Logistics' department bucket) into
# ROLE_ALIASES with the §7.3 DC roster roles they actually denote.
ALIAS_MOVES = {
    "dc packer": "DC:Packers / Load Builders",
    "dc pick staff": "DC:Order Pickers",
    "dc picker": "DC:Order Pickers",
    "outbound picker": "DC:Order Pickers",
    "warehouse picker": "DC:Order Pickers",
}

ALIAS_BLOCK_MARKER = '    "receiving clerk": "DC:Receiving Clerk",'
NEW_ALIAS_BLOCK = '''    "receiving clerk": "DC:Receiving Clerk",
    # --- Role-anchoring worklist remediation (batch 31, 2026-09-23): corpus
    # forms promoted to the chartered titles they denote (zero-anchor worklist
    # clearance; see fix-role-anchor-worklist.py and the matrix's
    # Role-Anchoring Contract section).
    "picker": "DC:Order Pickers",
    "pickers": "DC:Order Pickers",
    "packer": "DC:Packers / Load Builders",
    "packers": "DC:Packers / Load Builders",
    "load builder": "DC:Packers / Load Builders",
    "load builders": "DC:Packers / Load Builders",
    "cross-dock coordinator": "DC:Cross-Dock Team",
    "cross-dock team": "DC:Cross-Dock Team",
    "dc outbound supervisor": "DC:Assistant DC Manager — Outbound",
    "outbound supervisor": "DC:Assistant DC Manager — Outbound",
    "payroll accountant": "Payroll Accounting Liaison",
    "assistant controller": "Manager, GL & Consolidation (Assistant Controller)",
    "marketing data analyst": "Insights Analyst",
    "ecommerce customer support": "Ecommerce Support Specialist",
    "integration specialist": "IAP Integration Support Engineer",
    "dc packer": "DC:Packers / Load Builders",
    "dc pick staff": "DC:Order Pickers",
    "dc picker": "DC:Order Pickers",
    "outbound picker": "DC:Order Pickers",
    "warehouse picker": "DC:Order Pickers",'''


def apply_participant_additions():
    by_file = {}
    for item in PARTICIPANT_ADDITIONS:
        rel, anchor, roles = item[0], item[1], item[2]
        by_file.setdefault(rel, []).append((anchor, roles, item[3] if len(item) > 3 else 1))
    total = 0
    for rel, items in sorted(by_file.items()):
        path = os.path.join(WF, rel)
        lines = open(path, encoding="utf-8").read().splitlines(keepends=True)
        changed = 0
        for item in items:
            anchor, roles = item[0], item[1]
            expected = item[2] if len(item) > 2 else 1
            if anchor.startswith("| **Participants** |"):
                # exact-line anchor (PA-61.3's minimal cell)
                hits = [i for i, ln in enumerate(lines) if ln.rstrip("\n") == anchor.rstrip(" |").rstrip() + " |" or ln.strip() == anchor.strip()]
            elif anchor == "W230":
                # the W230 legal-review workflow's own Participants line
                wstart = None
                for i, ln in enumerate(lines):
                    if re.match(r"^## W230\.", ln):
                        wstart = i
                        break
                assert wstart is not None, f"{rel}: W230 heading not found"
                pend = None
                for i in range(wstart, len(lines)):
                    if lines[i].startswith("### "):
                        break
                    if "| **Participants** |" in lines[i]:
                        pend = i
                        break
                assert pend is not None, f"{rel}: W230 Participants not found"
                hits = [pend]
            else:
                hits = [i for i, ln in enumerate(lines)
                        if "| **Participants** |" in ln and anchor in ln]
            assert len(hits) == expected, f"{rel}: anchor {anchor[:60]!r} matched {len(hits)} lines (expected {expected})"
            i = hits[0]
            line = lines[i].rstrip("\n")
            add = [r for r in roles if r not in line]
            if not add:
                continue
            assert line.endswith(" |"), f"{rel}:{i+1} unexpected cell ending: {line[-30:]}"
            lines[i] = line[:-2] + ", " + ", ".join(add) + " |\n"
            changed += 1
            total += len(add)
        if changed:
            open(path, "w", encoding="utf-8").write("".join(lines))
        print(f"  {rel}: {changed} Participants line(s) updated")
    print(f"Participants anchors appended: {total}")


def apply_alias_changes():
    src = open(GEN, encoding="utf-8").read()
    for k in ALIAS_MOVES:
        pat = re.compile(r'\n[ \t]*"%s": "[^"]*",' % re.escape(k))
        src, n = pat.subn("\n", src, count=1)
        assert n == 1, f"alias move {k!r}: {n} occurrences"
    assert ALIAS_BLOCK_MARKER in src, "alias insertion marker not found"
    if '"marketing data analyst"' not in src.split('def ')[0].split(ALIAS_BLOCK_MARKER)[0]:
        src = src.replace(ALIAS_BLOCK_MARKER, NEW_ALIAS_BLOCK, 1)
    open(GEN, "w", encoding="utf-8").write(src)
    print(f"alias moves: {len(ALIAS_MOVES)}, new aliases: {len(NEW_ALIASES)}")


def apply_store_fragment_filter():
    src = open(GEN, encoding="utf-8").read()
    old = """        add_store(re.sub(r"\\s*\\(.*?\\)$", "", cells[0]))
        for token in re.split(r";", cells[1]):
            t = re.sub(r"^\\d+\\s+", "", norm(token))
            t = re.sub(r"\\s*\\(.*?\\)$", "", t).strip()
            add_store(t)"""
    new = """        add_store(re.sub(r"\\s*\\(.*?\\)$", "", cells[0]))
        for token in re.split(r";", cells[1]):
            t = re.sub(r"^\\d+\\s+", "", norm(token))
            t = re.sub(r"\\s*\\(.*?\\)$", "", t).strip()
            # batch 31: skip staffing-note fragments — §7.2 roster-cell prose
            # ('Receiving pair (lead clerk + 1)', '3 Sales Associates + 1 Stock
            # Associate each', 'holds Safety Officer 1 duty') describes the
            # model's composition, it does not charter role titles.
            if (not t or t.startswith("holds ") or " pair" in f" {t} "
                    or re.search(r"\\+\\s*\\d+", t) or t.endswith(" each")):
                continue
            add_store(t)"""
    assert old in src, "store tokenizer block not found (already patched?)"
    src = src.replace(old, new, 1)
    open(GEN, "w", encoding="utf-8").write(src)
    print("store-roster fragment filter installed")


def main():
    apply_participant_additions()
    apply_alias_changes()
    apply_store_fragment_filter()
    print("done — regenerate the matrix and trees, then re-pin the census")
    return 0


if __name__ == "__main__":
    sys.exit(main())
