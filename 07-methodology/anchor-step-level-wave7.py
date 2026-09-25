#!/usr/bin/env python3
"""Step-level anchoring wave 7 — batch 50 (2026-09-25, by direction).

Elevations for the participant-only weak-anchor roles (the batch-39
co-performer pattern — full chartered title appended to the Role (R) cell of
the mandate-exact step; no durations, frequencies, step texts or ownership
cells changed):

  Assistant DC Manager — Outbound → dispatch plan review & load assignment
                                    (PA-04.2 W106.2; §7.3 outbound-oversight seat)
  Tile & Heavy/Breakbulk Crew     → truck loading per manifest (PA-04.2 W106.4;
                                    §7.3 specialty handling crew)
  DC Operations Analyst           → weekly KPI trend review (PA-04.3 W586.7;
                                    mandate: DC performance analytics)
  DC Office Administrator         → shift handover log (PA-04.3 W584.7; mandate:
                                    DC office/records administration)
  Ecommerce Marketing Specialist  → public review responses (PA-10.1 W510.6;
                                    brand-voice seat on the review estate)
  Facilities Coordination Specialist → daily cleaning service coordination
                                    (PA-138.2 W4177.1; IFM coordination seat)
  Special Handling Lead           → putaway supervision (PA-04.1 W3.9; §7.3
                                    special-handling class team, reports to AM Inbound)
  Business Process & IMS Lead     → enterprise process architecture maintenance
                                    (PA-133.1 W4050.1; process-architecture steward)
  DC Cost-to-Serve Analyst        → freight cost-to-serve computation
                                    (PA-110.3 W3516.1; mandate-exact analytics seat)
  IAP Integration Engineer        → capacity/performance baselining (PA-27.2 W376.1;
                                    integration-platform capacity slice)
  IAP Integration Support Engineer → scaling implementation (PA-27.2 W376.6; run-side seat)
  Build-Squad Tech Lead           → SEP paved-road service bootstrap (PA-113.1 W5517.1;
                                    pairs with the batch-50 IT_SEATS resolver alias)

Deliberately NOT elevated: Facilities/Utility (DC) — its chartered form is
slash-compound, which the corpus's own cell grammar (grc_split's '/' split)
would tear into two unresolvable parts; it stays on the NO PARSED CADENCE
watchlist as a named vocabulary-form item until its charter form is
adjudicated. The five IT seats already carrying step-R anchors (AAP Agent
Engineer, INFRA Site Reliability Engineer, and the newly-elevated IAP pair)
measure through the verification tool's capacity-unmapped arm — the engine's
TO-based capacity map reads the IT department by reference and carries no
per-seat HC.

Idempotent; regenerating the matrix, bpmn/ and dmn/ trees and the gap/
verification artefacts afterwards is required.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.join(HERE, "..", "01-model-company", "workflows")
P = lambda *a: os.path.join(WF, *a)

EDITS = [
    (P("VS-04-dc-warehouse", "PA-04.2-dc-outbound-operations.md"),
     "reviews dispatch plan and assigns loads to trucks", "DC Dispatch Supervisor",
     "Assistant DC Manager — Outbound"),
    (P("VS-04-dc-warehouse", "PA-04.2-dc-outbound-operations.md"),
     "loads truck per load manifest and loading sequence", "Loading Crew",
     "Tile & Heavy/Breakbulk Crew"),
    (P("VS-04-dc-warehouse", "PA-04.3-dc-operations-management.md"),
     "analyzes 7-day KPI trends", "DC Manager",
     "DC Operations Analyst"),
    (P("VS-04-dc-warehouse", "PA-04.3-dc-operations-management.md"),
     "completes shift handover log in system", "DC Shift Supervisor (A) / DC Shift Supervisor (B)",
     "DC Office Administrator"),
    (P("VS-10-ecommerce-digital", "PA-10.1-ecommerce-platform-operations.md"),
     "drafts public vendor response", "CX Rep",
     "Ecommerce Marketing Specialist"),
    (P("VS-138-integrated-facilities-management-workplace-services-and-building-automation",
       "PA-138.2-hard-and-soft-fm-service-operations.md"),
     "execute the daily cleaning schedule", "Provider / Facilities Soft-Services Lead",
     "Facilities Coordination Specialist"),
    (P("VS-04-dc-warehouse", "PA-04.1-dc-inbound-operations.md"),
     "Putaway staff moves goods to assigned bin", "Putaway Staff",
     "Special Handling Lead"),
    (P("VS-133-operational-excellence-process-mining-continuous-improvement",
       "PA-133.1-opex-strategy-governance-and-improvement-methodology.md"),
     "maintain the enterprise process architecture", "OpEx CoE / Process Owners",
     "Business Process & IMS Lead"),
    (P("VS-110-freight-procurement-carrier-management-and-freight-audit",
       "PA-110.3-freight-audit-payment-and-freight-cost-analytics.md"),
     "compute cost-to-serve", "Logistics / BI / FP&A",
     "DC Cost-to-Serve Analyst"),
    (P("VS-27-it-operations-security", "PA-27.2-infrastructure-and-platform.md"),
     "Utilization Baselining", "IT Infra Lead",
     "IAP Integration Engineer"),
    (P("VS-27-it-operations-security", "PA-27.2-infrastructure-and-platform.md"),
     "Execute scaling actions during maintenance windows", "IT Infrastructure",
     "IAP Integration Support Engineer"),
    (P("VS-113-enterprise-architecture-application-portfolio-and-technology-strategy",
       "PA-113.1-enterprise-architecture-framework-standards-and-governance.md"),
     "bootstrap every new service from the SEP golden-path templates", "DevEx engineers / Squad Tech Lead",
     "Build-Squad Tech Lead"),
]


def main():
    for path, anchor, oldr, role in EDITS:
        lines = open(path, encoding="utf-8").read().splitlines(keepends=True)
        if any(anchor in ln and role in ln for ln in lines):
            print(f"  {os.path.basename(path)}: {role} already elevated")
            continue
        hits = [i for i, ln in enumerate(lines)
                if anchor in ln and ln.startswith("| ") and ln.split("|")[3].strip() == oldr]
        assert len(hits) == 1, f"{os.path.basename(path)}: anchor {anchor!r} matched {len(hits)}"
        i = hits[0]
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        cells[2] = f"{cells[2]}, {role}"
        lines[i] = "| " + " | ".join(cells) + " |\n"
        open(path, "w", encoding="utf-8").write("".join(lines))
        print(f"  {os.path.basename(path)}: {role} elevated on '{anchor[:40]}...' step")
    print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
