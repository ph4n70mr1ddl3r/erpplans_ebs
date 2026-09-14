# Customization Governance — CEMLI Discipline for BuildRight's EBS

> How the "only customize where there are gaps" doctrine stays true after go-live: the
> CEMLI framework operationalized, the decision ladder, technical standards that keep every
> extension safe under 12.2 online patching, the Customization Decision Record workflow,
> the CEMLI register, and the de-customization program. The [fit-gap register](fit-gap-analysis.md)
> decided *what* is custom; this document governs *how* custom is done and *when it dies*.

Part of the [02-oracle-ebs blueprint](README.md).

---

## 1. CEMLI — the Framework

| Letter | Tier | BuildRight rule |
|---|---|---|
| **C** — Configuration | Setup only | The default. Documented in config guides, owned by the configure teams (OM §5 archetypes) |
| **E** — Extensions | Custom objects *beside* the product | Permitted only via an approved CDR (§4). Includes OAF personalizations, custom schema objects, concurrent programs, AME-custom conditions, ISG-wrapped custom APIs |
| **M** — Modifications | Changes *to* the product | **Prohibited absolutely** — no Forms modification, no base-table DML, no database triggers on base tables, no patched-file edits. A modification makes every future patch a manual merge; the doctrine does not trade that away |
| **L** — Localizations | Statutory country-specific function | Confined to the [PH localization pack](fit-gap-analysis.md) §6; every output cites its statute/format and is versioned as a pack release |
| **I** — Interfaces | Inbound/outbound data bridges | Governed by [integrations.md](integrations.md); built on EBS open interfaces/APIs, never on direct table writes by external systems |

The fit-gap ladder (FIT-STD → FIT-CFG → PER → EXT → LOC → INT → BUILD) is this
framework with the two-tier doctrine's build tier appended (in EBS → use it; otherwise →
build — never buy). Lowest wins.

---

## 2. The Extension Budget

Scarcity is the control. Extensions compete for a hard budget:

| Budget item | Cap at go-live | Cap steady state | Current (fit-gap register) |
|---|---|---|---|
| EXT builds | 10 | 10 | 2 (PFRS 15 schedules; PFRS 16 schedules) |
| LOC pack components | — (versioned pack) | versioned | 4 components |
| PER (personalizations) | 150 | 150 | 2 register rows (page-level counts tracked in the register) |
| Custom schema objects (tables/packages total) | 120 | 120 | — |

Adding beyond cap requires CIO sign-off **and** retiring another extension of the same
class — the budget forces a portfolio, not an accretion.

---

## 3. When an EXT Is Admissible

A CDR passes only if all eight are true:

1. **Gap is real** — the fit-gap ladder alternatives (STD/CFG/PER) are documented as tried
   or ruled out with reasons, and no BUILD product is register-assigned to it.
2. **Edge-clean** — the extension has a defined input, output, and trigger; it does not
   fork a business process into "the EBS way and our way".
3. **Registered objects only** — custom objects live in the `BDR` schema/top, registered in
   the EBS object registry (application, menu, concurrent program, message, lookup).
4. **Upgrade-safe** — coded to the online-patching standard (§6); the PATCH-environment
   rehearsal includes it.
5. **Control-mapped** — every CTL the extension touches is named, and the control's
   evidence path post-change is stated (sourcing model §3.3 appendix, applied inside EBS).
6. **Owned** — a named owning team (OM §4) accepts run cost, monitoring, and the quarterly
   re-registration duty.
7. **Reversible** — a de-customization trigger and retirement plan exist (§8).
8. **Cheaper than the gap** — 3-year TCO of build-and-run < value of closing the gap,
   FinOps-verified.

---

## 4. The Customization Decision Record (CDR)

One page + appendices, stored with the CEMLI register entry:

| Section | Content |
|---|---|
| Context | Workflow(s) (W-ids), capability register row, gap statement |
| Alternatives | STD/CFG/PER/BUILD attempts and why inadequate |
| Design | Objects, APIs used, event/interface points; architecture sketch |
| Controls | CTL-XX mapping and evidence path |
| Operations | Owning team, runbook link, monitoring, batch window |
| Retirement | De-customization trigger, data-migration-out plan |
| Sign-offs | Owning IT PO, Head of EA (ARB record), SEC lead (if controls/PII), FIN controller (if accounting-adjacent) |

CDRs are approved by the ARB and reported to the SIB quarterly — the same bodies that
govern sourcing, so "inside-EBS build" never becomes a shadow of the governed build class.

---

## 5. Technical Standards (What Every Extension Must Do)

| Standard | Rule |
|---|---|
| Schema | All custom objects in `BDR` (custom application/top); **never** new objects in APPS/base schemas |
| Data access | Read base tables via registered views; write **only** through public APIs/open interfaces — no base-table DML |
| Business logic | Extend via supported points: OAF controller extensions, personalizations, AME conditions, Workflow customization (copy-then-modify, version suffix), business-event subscriptions, SLA user-entity derivations where supported |
| Reporting | BI Publisher templates + data templates; no direct production reporting off base tables by end users — custom SQL is wrapped in registered, tuned, audited BDR objects |
| Concurrency | Custom batch programs: registered concurrent programs with request groups, restartable, logging to FND tables, inside the batch windows ([data-volumes §5](../01-model-company/data-volumes-and-integrations.md)) |
| Security | Custom functions/menus registered; grantees via responsibilities only; row-level org scoping via MOAC-aware code (`mo_global`) |
| Errors | FND message dictionary, no hard-coded text; custom exceptions raise to the IAP error taxonomy ([integrations.md](integrations.md) §6) |
| Testing | Unit + SIT scripts versioned with the CDR; Tier-1-touching extensions re-run the regression pack every RUP |
| Documentation | CDR + runbook + object inventory row are the ship gate — undocumented objects fail the quarterly register audit |

---

## 6. Online Patching (ADOP) Rules for Custom Code

EBS 12.2 patches online via edition-based redefinition; custom code must respect it:

1. **Every custom table is edition-enabled** (or correctly non-editioned with documented
   cross-edition semantics) — the ADOP cutover must never fail on a BDR object.
2. **No code differences without editioning awareness**: custom PL/SQL deployed through the
   patch framework (`adop phase=apply` with custom patch directories), not ad-hoc `@d:` edits.
3. **Triggers/views on base objects** follow the supported custom-on-base rules (editioned
   view cross-edition triggers only where Oracle documents them).
4. **The PATCH environment rehearses every patch** — RUPs, CPUs, and the localization pack
   releases — with the CEMLI register's full inventory applied; a rehearsal failure blocks
   production patching.
5. **Quarterly CPU discipline**: applied ≤ 30 days; extensions re-verified by their owners
   as part of the patch runbook.

---

## 7. The CEMLI Register

Single inventory of every non-Configuration object in the estate:

| Column | Purpose |
|---|---|
| ID / class | EXT/LOC/INT/PER + sequence |
| CDR link | The decision record |
| Objects | Schema objects, programs, templates, personalization paths |
| Workflows / CTLs | W-ids and control ids touched |
| Owner team | OM §4 team |
| Last verified | Patch rehearsal that last proved it |
| De-customization trigger | The event that retires it |
| Status | Active / retirement-in-progress / retired |

The register is audited quarterly against the databases (object inventory diff) — an
unregistered object in a BDR schema is an incident, not a finding.

---

## 8. De-customization — Extensions Are Born to Die

| Trigger | Action |
|---|---|
| A RUP ships equivalent function | Owner has 2 quarters to retire the extension and adopt the shipped function — the same re-evaluation discipline the two-tier doctrine applies to in-house builds, applied inside the suite |
| Usage falls below threshold (2 quarters) | Retirement review at QBR |
| A PROCESS-mining finding shows the fork costs more than the gap | ARB-initiated retirement |
| Philippine statute/format changes | Pack release replaces the component (never a live patch) |
| Module re-tiers (e.g., a doctrine resolution re-scopes a module's in-suite footprint) | Dependent EXT/INT rows re-planned in the same decision |

Retirements celebrate: the KPI (fit-gap §7) is extensions trending to zero.

---

## 9. KPIs & Governance Bodies

| KPI | Target |
|---|---|
| M-class objects | 0 (absolute) |
| EXT count | ≤ 10, trending down |
| Register audit exceptions | 0 |
| Patch rehearsal pass rate | 100% before PROD patching |
| RUP currency | Within one RU of current |
| CDR cycle time | ≤ 15 working days median |
| De-customization completions | ≥ 1 per half-year once stable |

Bodies: ARB approves CDRs; SIB reviews the register quarterly; the Tier & Control Board
signs any change touching Tier-1 workflows (OM §6.3 discipline).

---

*Document Version: 1.1 | Date: 2026-09-14 | Two-tier sourcing doctrine enacted (in EBS → use it; otherwise → build): fit-gap ladder and CDR alternative set re-worded (EDGE/Buy tier retired), de-customization triggers re-pointed to the doctrine's re-evaluation discipline. Prior v1.0 (2026-09-14): initial issue — CEMLI framework, extension budget, CDR workflow, technical & ADOP standards, CEMLI register, de-customization triggers, KPIs. Canon anchors: fit-gap register (2 EXT / 1 LOC row); sourcing model §3.3 appendices and §12 agentic boundaries; OM §6.3 tier-and-control discipline.*
