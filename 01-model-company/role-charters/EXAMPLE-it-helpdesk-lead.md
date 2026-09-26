# Role Charter — IT Helpdesk Lead

> Worked example for `TEMPLATE.md`, built **only from verified canon** (every
> [D] field cites its source). Cells marked `⟨regen⟩` are demonstrated as
> generator pulls — fill from the named register, never by hand-copy, so
> canon moves refresh them mechanically.

---

## 1. Identity [D]

| Field | Value | Source |
|---|---|---|
| Role title | **IT Helpdesk Lead** (workflow-catalog canonical title; resolves to the FS Supervisor seat) | W48 Owner cell; ITOM §5.3 Field & End-User Services roster |
| Team / department | Field & End-User Services (FS) — Platform archetype, product 16 of 17 | ITOM §3.2 (row 16: all 205 locations; 6,911 users) |
| Reports to | ⟨regen: ITOM FS team line⟩ | ITOM §5.3 |
| Headcount (seats with this charter) | 1 (team roster: Supervisor + 2 helpdesk L2 analysts + 1 ITAM administrator + 5 regional field technicians; L1 is an outsourced contact center) | ITOM §5.3 |
| Charter ID / version / review date | RC-IT-FS-01 · v0.1 · quarterly | this layer |

## 2. Mission [A]

> Every user in every location gets their issue resolved within the published
> SLA, and the company sees why its incidents happen.

## 3. Ownership — accountable for [D→A]

- **The full support-ticket lifecycle and its SLAs** — intake, triage, tiering,
  escalation, closure, resolution codes (W48: continuous; ~800–1,200
  tickets/month across ~6,911 users, 600 POS terminals, ~500 RF devices,
  200+ network locations).
- **Monthly service analytics** — volume by category, resolution by tier, SLA
  compliance, MTTR, top recurring issues per location (W48 step 11, 2 h/month,
  A: CIO).
- **Change intake classification** — every change request is classified
  standard / normal / emergency before it proceeds (~20–30 changes/month;
  W48 Change Management, A: CIO on classification).
- **P2 integration-degradation ownership** — on W595's daily health check, P2
  items notify this role with an 8-hour resolution target; P1 goes to CIO
  immediately, P3 logs as W48 tickets (24 h).

## 4. Contribution — executes, does not own [D]

- **W595 ERP Daily Health Check & Integration Monitoring** — R for *user
  communication*; receives the 07:00 Daily Health Check Report (Owner: ERP
  System Administrator).
- **On-site dispatch**: W48 step 8 hands unresolved hardware/network/POS
  tickets to IT Field Support — scheduling is the Helpdesk's, the site visit
  the technician's (A: CIO).
- Tier-3 vendor engagement is *tracked* by this role; vendor response SLAs are
  managed per vendor contracts (W48 step 9).

## 5. Decision rights [A]

| May decide alone | Recommends, others approve | Must escalate |
|---|---|---|
| Ticket triage, tier assignment, severity per W48 matrix | Change classification → A: CIO (W48 CM) | P1 anything → CIO immediately (15-min response clock) |
| Tier-1/2 routing among helpdesk & specialist queues | Vendor engagement (Tier 3) → A: CIO (W48 step 9) | Security-suspected incidents → the cybersecurity workflow's owner |
| Resolution & closure codes (user-confirmed) | On-site field dispatch schedule within store-visit SLAs | Anything touching the peak-season change freeze → W5521 governance |
| Standard (pre-approved) changes | Normal & emergency changes → CAB path (W1409) | |

## 6. Workflow anchors — demand signal [D]

| W# | Workflow | This role | Tier | Cadence/volume | Demand status |
|---|---|---|---|---|---|
| W48 | IT Operations & Helpdesk Support | **Owner** | ⟨regen: confirmed tier register⟩ | Continuous; ~800–1,200 tickets/mo | ⟨regen: gemba verdict⟩ |
| W595 | ERP Daily Health Check & Integration Monitoring | R (user comms); P2 recipient | ⟨regen⟩ | Daily 05:00/07:00 + 24/7 monitoring | ⟨regen⟩ |
| … | *(full anchor set pulled from coverage-matrix row)* | | | | |

## 7. Priority rules [D — mirrors W48 canon]

1. **P1 Critical** (system down / revenue-affecting; e.g. all POS down, ERP
   inaccessible, DC WMS failure) — response 15 min, resolution 4 h.
2. **P2 High** (major function impaired, workaround exists) — 30 min / 8 h.
3. **P3 Medium** (productivity, non-critical) — 2 h / 24 h.
4. **P4 Low** (minor/enhancement) — 8 h / 72 h.
5. Then: confirmed workflow tier; then Owner's call.
Tie-breaker: simultaneous P1s → CIO sequences; simultaneous same-priority →
store/DC down before HQ, revenue-adjacent before back-office.

## 8. Escalation — when stuck [A]

| Situation | First ask | If unresolved, decides |
|---|---|---|
| Tier-2 unresolved | IT Specialist queue (W48 step 7) | CIO |
| Vendor-dependent fix | Vendor support line, tracked (W48 step 9) | CIO |
| Integration red-status (W595) | ERP System Administrator | CIO |
| Novel — not in any row | FS Supervisor within 4 business hours | CIO |

## 9. Boundaries & handoffs — explicitly NOT this role [A]

| Not this role's job | Belongs to |
|---|---|
| Field site visits (hardware swaps, cabling, POS replacement) | IT Field Support (W48 step 8) |
| Network/server root-cause work | IT Infrastructure Engineer (W595 R) |
| API/integration root-cause work | Integration Specialist (W595 R) |
| Change *approval* (only classification) | CIO / CAB per W1409 / W5521 freeze rules |
| POS/printer/RF hardware lifecycle planning | FS team ITAM track (VS-99; ITAM administrator) |
| L1 scripted resolution | Outsourced contact center (escalates in) |

## 10. Definition of done [D/A]

- Severity-matrix SLA compliance ≥ target, reported monthly (W48 step 11).
- Queue state: no P1/P2 aging past SLA at shift handover without a CIO-visible
  exception note.
- Monthly analytics delivered with top recurring issues per location and
  actions proposed.
- Every closed ticket carries a resolution code and root-cause category
  (feeds recurring-issue flagging).

## 11. Coverage & backup [A]

| Duty | Covered by | Activation |
|---|---|---|
| P1 response outside hours | ⟨A: named on-call deputy seat⟩ | Automatic via alerting (W380) |
| Daily health-check P2 watch (05:00–08:00) | Senior helpdesk L2 analyst | Standing: reviews 07:00 report when Lead absent |
| Change classification | FS Supervisor delegate | Explicit delegation |

*P1 obligation with a blank backup row = org defect — resolve before v1.0.*

## 12. Provenance & change log [D]

| Field | Value |
|---|---|
| Canon sources | W48 (PA-27.1: Owner, steps 7–11, Severity & SLA Matrix, Change Management); W595 (PA-27.2: Participants, steps 3/9/11–12); ITOM §3.2 row 16, §5.3 FS roster; coverage-matrix row ⟨regen⟩ |
| Refresh trigger | Any batch touching W48/W595 anchors or the FS roster — regenerate derived fields |
| Authored / reviewed with | ⟨author⟩ · ⟨incumbent⟩ · ⟨FS Supervisor's manager⟩ · ⟨ERP System Administrator (counterparty)⟩ |
| Changes | v0.1 — drafted from TEMPLATE as pilot example |
