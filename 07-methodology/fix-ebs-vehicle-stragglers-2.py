#!/usr/bin/env python3
"""Wave-2 straggler repairs (fifty-second wave, part 2) — see fix-ebs-vehicle-stragglers.py."""
import os
# 2026-09-17 fifty-fourth-wave consistency review — repo-relative resolution per the
# eighteenth-wave shipped-tooling portability repair (the authored '/home/alden'
# absolute path was unrunnable on any other checkout).
WF = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                  "01-model-company", "workflows")
fixes = [
    ("VS-115-calibration-metrology-and-measurement-traceability-management/PA-115.1-calibration-program-standards-and-measurement-traceability.md",
     "device-class procedures, software/CMMS, standards handling",
     "device-class procedures, software/Oracle eAM, standards handling"),
    ("VS-174-self-storage-portable-container-and-mobile-storage-operations/PA-174.3-storage-operations-maintenance-safety-and-analytics.md",
     "CMMS PM auto-generation",
     "Oracle eAM PM auto-generation (fit-gap F5)"),
    ("VS-192-green-fleet-transition-electric-vehicle-fleet-operations-and-sustainable-transportation/PA-192.2-ev-alt-fuel-fleet-operations-charging-and-energy-management.md",
     "BMS→CMMS SoH feed",
     "BMS→Oracle eAM SoH feed (fit-gap F5)"),
    ("VS-192-green-fleet-transition-electric-vehicle-fleet-operations-and-sustainable-transportation/PA-192.2-ev-alt-fuel-fleet-operations-charging-and-energy-management.md",
     "OBD/fault-code → CMMS auto-ticketing",
     "OBD/fault-code → Oracle eAM auto-ticketing (fit-gap F5)"),
    ("VS-04-dc-warehouse/PA-04.2-dc-outbound-operations.md",
     "- Route optimization system processing: automated",
     "- Route Optimization Engine processing: automated (in-house build — fit-gap C14)"),
    ("VS-06-logistics-fleet/PA-06.1-outbound-distribution.md",
     "**Optimization**: Route optimization engine calculates most efficient sequence",
     "**Optimization**: Route Optimization Engine (in-house build — fit-gap C14) calculates most efficient sequence"),
    ("VS-136-supply-chain-network-design-multi-echelon-inventory-optimization-flow-engineering/PA-136.1-supply-chain-network-strategy-modeling-and-design.md",
     "- Route optimization engine; dynamic re-routing on disruption",
     "- Route Optimization Engine (in-house build — fit-gap C14); dynamic re-routing on disruption"),
    ("VS-17-record-to-report/PA-17.2-consolidation-and-intercompany.md",
     "- ERP intercompany module — automated IC transaction recording and elimination entries",
     "- AGIS — automated IC transaction recording and elimination entries (fit-gap A7)"),
    ("VS-21-internal-audit-risk/PA-21.3-specialized-audit-domains.md",
     "- HRIS Succession Module",
     "- Oracle Succession Planning (fit-gap E2)"),
    ("VS-22-compliance-regulatory/PA-22.2-government-audit-and-inspection-response.md",
     "- Compliance case management system",
     "- Oracle Internal Controls Manager compliance-case tracking (fit-gap H11)"),
    ("VS-03-vendor-management/PA-03.1-vendor-sourcing-and-onboarding.md",
     "- Quality inspection module",
     "- Oracle Quality receiving inspection (fit-gap C12)"),
    ("VS-11-trade-project-wholesale/PA-11.2-project-sales-and-b2b.md",
     "- Revenue recognition module with financing-specific booking per PFRS 15",
     "- Oracle Revenue Management and Invoicing with financing-specific booking per PFRS 15 (fit-gap A11)"),
    ("VS-12-installation-services/PA-12.1-installation-and-repair-services.md",
     "| 2 | ERP Subscription Billing module generates a recurring contract and defers revenue. |",
     "| 2 | Oracle Revenue Management and Invoicing subscription billing (fit-gap A11) generates a recurring contract and defers revenue. |"),
    ("VS-29-master-data/PA-29.1-foundational-masters.md",
     "- Revenue Recognition Module (PFRS 15 compliance)",
     "- Oracle Revenue Management and Invoicing (PFRS 15 — fit-gap A11)"),
    ("VS-03-vendor-management/PA-03.1-vendor-sourcing-and-onboarding.md",
     "- Rebate tracking module",
     "- Oracle Trade Management rebate tracking (fit-gap B10)"),
    ("VS-39-vendor-rebate-incentive/PA-39.1-rebate-agreement-accrual.md",
     "- Monthly rebate accrual engine — YTD purchases × applicable % with tier recognition (step 1)",
     "- Trade Management monthly rebate accrual (fit-gap B10) — YTD purchases × applicable % with tier recognition (step 1)"),
    ("VS-08-pos-checkout/PA-08.1-transaction-processing.md",
     "| CS-5 | ERP loyalty module consumes event; posts points earned/redeemed to customer account |",
     "| CS-5 | Loyalty engine (in-house stack — fit-gap D9) consumes event; posts points earned/redeemed to customer account |"),
    ("VS-08-pos-checkout/PA-08.1-transaction-processing.md",
     "**Loyalty consumer**: ERP loyalty module consumes event;",
     "**Loyalty consumer**: Loyalty engine (in-house stack — fit-gap D9) consumes event;"),
    ("VS-13-customer-experience/PA-13.3-customer-data-and-crm.md",
     "- ERP Loyalty module: points balance consolidation",
     "- Loyalty engine (in-house stack — fit-gap D9): points balance consolidation"),
    ("VS-04-dc-warehouse/PA-04.1-dc-inbound-operations.md",
     "scan-registers container number in Yard Management System (YMS)",
     "scan-registers container number in Oracle WMS Yard Management (fit-gap C6)"),
    ("VS-182-b2b-bulk-project-custom-import-indent-sourcing-and-brokerage/PA-182.3-direct-port-to-jobsite-customs-and-logistics.md",
     "Register materials serial numbers and batches in warranty tracking module.",
     "Register materials serial numbers and batches in Oracle Install Base (warranty tracking — fit-gap D16)."),
    ("VS-20-real-estate-construction/PA-20.2-engineering-and-construction.md",
     "- e-Procurement module for RFP issuance, bid submission, and bid tabulation",
     "- Oracle Sourcing RFP/bid events (fit-gap B5) for RFP issuance, bid submission, and bid tabulation"),
]
applied = 0
for rel, old, new in fixes:
    p = os.path.join(WF, rel)
    t = open(p, encoding="utf-8").read()
    n = t.count(old)
    if n != 1:
        print(f"SKIP({n}) {rel} :: {old[:60]}")
        continue
    open(p, "w", encoding="utf-8").write(t.replace(old, new))
    applied += 1
print(f"APPLIED {applied}/{len(fixes)}")
