# BuildRight Depot Corp. — Capability Sourcing & Engineering Model

> Companion to [`it-product-operating-model.md`](it-product-operating-model.md) (v3.30): how
> each business capability is **sourced** under the **two-tier doctrine** (2026-09-14) —
> *if it's in Oracle EBS we use it; otherwise we build* — plus the decision gate, the
> Capability Sourcing Register, the build-squad engineering standard, and the Software
> Engineering Platform (SEP) team definition.

---

## 1. Purpose & Scope

The IT product operating model v1.x assumed a **single-vendor unified cloud ERP**. On
2026-09-03 the company adopted a hybrid three-tier posture (configure / buy / build); on
**2026-09-14 the doctrine collapsed to two tiers**: *if it's in Oracle EBS we use it —
standard, configured; otherwise we build it in-house.* The best-of-breed buy tier is
**eliminated for capability products** (vendor LLM APIs remain commodity procurement under
tier-1 TPRM, not capability sourcing); the 2026-09-03 Buy decisions (WMS/TMS/WFM/FSM) are
superseded — warehouse and transport execution moved **in-suite** (Oracle WMS/MSCA,
Shipping/Transportation Execution), workforce scheduling and dispatch flipped to **build**;
the POS estate, the custom ecommerce platform and the gift-card/loyalty stack are recorded
as **already-built in-house platforms** whose program is integration, not sourcing; and
**payroll is an in-house build** (Payroll PH) posting journals to EBS. The realization
blueprint lives in [`../02-oracle-ebs/`](../02-oracle-ebs/README.md) (its fit-gap §4 carries
the full resolution record).

This document defines:

1. The **landscape principle** — what runs in-suite, what is built (§2).
2. The **sourcing decision gate** (Use-EBS / Build) and its governance (§3).
3. The **Capability Sourcing Register** — the single record of every sourcing decision (§4).
4. The **team archetypes and build-squad shape** the strategy requires (§5).
5. The **Software Engineering Platform (SEP)** team and the paved road (§6).
6. The **engineering standard** build squads must meet (SDLC, security, delivery) (§7).
7. The **vendor & platform lifecycle** — vendor commodities, already-built platforms, in-suite EBS currency; release intake, exit reserves (§8).
8. **Funding, TCO and capitalization** rules per archetype (§9).
9. KPIs and **risks** (§10–§11).

Scope is the same steady state as the operating model: post-go-live operations of the 188
value streams. Team membership, RACI, sizing and governance bodies live in the operating
model; this document governs the sourcing decisions that determine team shape.

---

## 2. Landscape Principle — In-Suite Core, Built Differentiators

The strategy does **not** abandon the unified ERP. It partitions the landscape into two
tiers, each with a default sourcing posture:

| Tier | What it contains | Default posture | Why |
|---|---|---|---|
| **In-suite (EBS standard)** | Financials & consolidation, procure-to-pay, the inventory ledger, warehouse & transport execution (Oracle WMS/MSCA, Shipping/Transportation Execution), planning (ASCP/Demantra), trade management, HR core data, approvals — everything the suite ships | **Use EBS standard, configured** — never rebuilt, never bought around | Protects the 5-working-day close (FIN KPI), the 808-control register's single control surface, and one ledger of record; buying around a function EBS already ships is prohibited outright |
| **Built (in-house products)** | Capabilities EBS does not ship: omnichannel order orchestration (OMO), trade & project services coordination (TPS), the agentic runtime (AAP), the integration platform (IAP), the data platform (DP), **Payroll PH** (statutory engine + outputs), **store workforce scheduling & time capture** (shift scheduling/optimization — OTL covers timecards, not retail planning), the **dispatch experience layer** (consumer appointment/route optimization/contractor portal — the Field Service dispatch core is in-suite per fit-gap D13), **space/planogram optimization** — plus the **already-built platforms** (the POS estate, the custom ecommerce platform, the gift-card/loyalty stack), whose program is integration, never rebuild | **Build in-house** on the SEP paved road; already-built platforms integrate | EBS offers no substitute, and the doctrine bars the middle: no vendor product may be bought where a build is required |

**Guardrails:** nothing may be removed from the in-suite tier without a CEO-noted waiver of
the unified-core principle (the same protection the single-vendor principle had in operating
model v1.x); and **no capability product may be bought** — a proposal that cannot name the
EBS module that ships the function routes straight to build, or to the already-built roster
if the platform exists.

---

## 3. The Sourcing Decision Gate

Every capability decision routes through one gate with two exits. The test is ordered:
**in-EBS → build**. If an EBS module ships the function (or can be configured to), the
answer is *use it* — that exit needs no scored assessment beyond the configuration design.
Build is admitted only when the EBS-standard answer demonstrably does not exist (the
[fit-gap register](../02-oracle-ebs/fit-gap-analysis.md) is the standing evidence base).
Demand reaches the gate through the capability demand-intake & backlog-triage
front door (**W5535**, PA-113.2): stakeholders raise needs with their paired IT PO/PM; the
PO logs the item and EA triages it against the 188-VS catalog — enhancements stay in team
backlogs, missing workflow-level owners enter the gap-analysis admission path, and only
genuine new-capability candidates arrive here as sourcing proposals with their triage pack.

### 3.1 Decision criteria (scored, not vibes)

| Criterion | Points toward **Use EBS** | Points toward **Build** |
|---|---|---|
| Strategic differentiation | Commodity or suite-standard | Customers would notice if a competitor had it — and EBS doesn't ship it |
| EBS fit-to-standard gap | Ships in-suite (any 12.2 module) | No EBS module covers it, and configuration/personalization cannot close the gap |
| Integration cost | Zero — the function is already in-suite | IAP estimate must be < value gained |
| Data gravity | Ledger/master data stays in EBS where it belongs | Deep data control genuinely required (e.g., an order-state machine) |
| Regulatory fit | eBTax/SLA/AME carry the PH statutory configuration | BuildRight owns the compliance burden entirely (e.g., Payroll PH) — accepted because the doctrine prefers building to buying |
| Total cost of ownership | Config analysts; the license is already owned | Squad cost + permanent tech-debt backlog — accepted consciously |
| Talent & key-person risk | Low | Permanent hiring/retention obligation — bus-factor ≥ 2 mandatory |
| Exit strategy | Not applicable — suite-standard retires with the suite | In-house is forever — the de-customization triggers still apply |

### 3.2 Decision rights

| Decision | Body | Notes |
|---|---|---|
| Use-EBS/build routing (any capability) | **Sourcing & Investment Board (SIB)** — chaired by CIO; Head of EA runs the assessment; members: affected IT PO/BPO, FinOps/TBM analyst, CFO delegate, SEC lead (TPRM, VS-161), Head of Engineering (for builds) | Monthly and on demand; every decision recorded in the Register (§4) |
| Sourcing decision with 3-year TCO > PHP 25M | SIB recommends → **Product Council** ratifies | Product Council already holds funding rights above PHP 5M |
| Removal of a capability from the in-suite tier | SIB recommends → **CEO** (noted waiver) | Rare; same weight as the v1.x single-vendor waiver |
| Architecture opinion on any sourcing proposal | **Architecture Review Board (ARB)** | Integration patterns, data ownership, retirement of capabilities |

### 3.3 Mandatory appendices per decision

No sourcing decision is valid without:

1. **IAP integration estimate** — flows, contracts, latency budget, run cost.
2. **Control-mapping appendix** — which of the 808 controls in
   [`internal-controls-matrix.md`](../01-model-company/internal-controls-matrix.md) touch the
   capability, and where evidence will come from after the change (vendor attestation, API,
   or in-product audit trail).
3. **TCO sheet** — 3-year license + integration + run + (build) squad cost, FinOps-verified.
4. **Run-cost & talent plan** (build) — the buy exit does not exist: nothing is bought.
5. **Re-evaluation trigger** — e.g., "revisit if the ERP vendor ships native WMS execution
   at parity", "revisit at 260 stores".

---

## 4. Capability Sourcing Register (initial issue)

The Register is the single source of truth for what is sourced how. Issued 2026-09-03
(hybrid posture); **re-issued 2026-09-14 under the two-tier doctrine** — amendments only via
the SIB:

| Capability | Value streams | Decision | Product / system | Owning team | Re-evaluation trigger |
|---|---|---|---|---|---|
| The in-suite estate: financials, P2P, inventory ledger, warehouse & transport execution, planning, trade management, HR core data, approvals | VS-15–VS-19, VS-04/05/06 and the rest of the in-suite estate | **Use EBS** (2026-09-14; supersedes the 2026-09-03 Buy rows for WMS/TMS) | Oracle EBS 12.2 — incl. Oracle WMS/MSCA, Shipping/Transportation Execution, ASCP/Demantra, Trade Management | FIN, WLI, MSC, CORP as mapped in OM §4 | Annual reaffirmation at QBR |
| **Payroll PH** (statutory engine + outputs) | VS-19.2, VS-79 | **Build** (2026-09-14) | In-house Payroll PH; Core HR (PER) + the GL stay in EBS; period costing posts via the GL interface | PEO | Statute/format change = pack-style release; Oracle Payroll not adopted |
| **Store workforce scheduling & time capture** | VS-07 (staffing PAs) | **Build** (2026-09-14; supersedes the BoB WFM row) | In-house workforce platform; validated feeds into payroll and EBS | SSP | None scheduled |
| **Installation & home-service dispatch** | VS-12 | **In-suite core + narrowed build** (2026-09-15 exhaustion audit; supersedes the BoB FSM row) | Oracle Field Service is the in-suite dispatch core (correcting this register's own 'not in EBS' claim); the build owns the consumer appointment/route-optimization/contractor-portal experience layer; remit (extend TPS vs new squad) at SIB/OM | CCP | None scheduled |
| **POS estate** (checkout, offline, peripherals) | VS-08 | **Already built** — integrate | The in-house POS platform (existing); EBS owns item/price/tax masters and the posting | SSP | None — integration flows per `02-oracle-ebs/integrations.md` |
| **Ecommerce platform** | VS-10 | **Already built** — integrate | The in-house custom ecommerce platform (existing) | CCP | None |
| **Gift cards / stored value & loyalty** | VS-54, VS-13 | **Already built** — integrate | The in-house stack (existing); EBS holds the GL liability and AR settlement | SSP/CCP | None |
| Omnichannel order routing, split-order & mixed-basket fulfillment | VS-60 | **Build — squad deferred — prepared** (2026-09-23 (ah), by direction: with BOPIS the only enabled online fulfillment option (registry CAP-F01) every sale completes as a regular POS sale at the customer-selected store and routing is deterministic — the multi-source orchestration workload is the disabled—prepared fulfillment estate; the OMO build squad's 7 seats defer — IT 115 → 108 active — with the platform's prepared design retained; the live BOPIS path rides the already-built ecommerce platform's capability-configuration service and in-suite order flows; re-evaluation/stand-up trigger = any second online fulfillment origin (CAP-F04–F09) or a marketplace channel (CAP-C03/C04) enabled) | In-house Order Orchestration product (OMO) | OMO | Second fulfillment origin / marketplace channel enablement (supersedes 'None — differentiating') |
| Trade & project services coordination (job-site delivery, material staging/phased delivery, bulky install/haul-away) | VS-74, VS-77, VS-143 | **Build — squad deferred — prepared** (2026-09-23 (ad), by direction: the project-side workload is dormant with the trade desk disabled (registry CAP-B01); the TPS build squad's 7 seats defer — IT 122 → 115 active — with the platform's prepared design retained; consumer bulky install/haul-away stays covered by the in-suite Field Service dispatch core and the CCP dispatch experience layer; re-evaluation/stand-up trigger = CAP-B01 re-enablement) | In-house Trade & Project Services platform (TPS) | TPS | CAP-B01 re-enablement (supersedes 'None — differentiating') |
| Agentic automation runtime (agent platform) | VS-30 (PA-30.2 AI/ML & Automation engineering); governed by VS-128 | **Build** (unchanged) | In-house agent runtime: tool registry (IAP contracts only), guardrails, evaluation harness, human-in-the-loop gates | AAP | Foundation-model vendor ships a governed agent runtime at parity |
| Foundation-model access (LLM APIs) | Cross-cutting (all agent use cases) | **Buy — commodity procurement** (not capability sourcing; the doctrine's sole vendor product line in capability sourcing — IT-tooling SaaS such as the A6.6 Atlassian suite is vendor-commodity procurement under §8, not a register row) | Vendor foundation models consumed through IAP-governed API edges | AAP with SEC (TPRM) | Philippine AI-regulation / NPC guidance change |

History: the 2026-09-03 issue carried four Buy rows (WMS, TMS, WFM, FSM). The 2026-09-14
two-tier doctrine superseded all four — WMS/TMS moved in-suite (Oracle WMS/MSCA, Shipping/
Transportation Execution), WFM/FSM flipped to build — and reclassified the POS/ecommerce/
loyalty estate as already-built platforms. Product/vendor management capacity (OM §5) is
re-pointed from BoB product management to the Oracle relationship, in-suite currency
(RUP/CPU), and the commodity vendor line. Team-estate mapping (OM §4) is unchanged — no
value stream changes business-process owner. W5515 (PA-113.3) remains the gate's
workflow-level owner; W5516 (PA-113.2, registered under its 2026-09-03 title) remains the
lifecycle owner for the vendor/platform line of §8.

---

## 5. Team Archetypes & Build Squads

Domain teams come in three shapes (full membership tables in OM §5):

| Archetype | Teams | Shape |
|---|---|---|
| **Configure** | MSC, FIN, PEO, CORP | The OM v1.x six-role core: PO, product/process architect, 2–4 ERP functional analysts, data & reporting analyst, QA & release analyst |
| **Configure-and-integrate** | WLI, SSP, CCP | Configure core **plus** one **Platform Product Manager** each (OM §9.1) re-pointed by the two-tier doctrine: WLI's seat doubles as the chain-wide **Oracle Relationship & In-Suite Currency Manager** (RUP/CPU cadence), SSP/CCP seats product-manage the **already-built platforms** (POS estate → SSP; ecommerce/loyalty/gift-card → CCP) and the in-house builds in their domain (store workforce → SSP; dispatch → CCP) |
| **Build** (squads) | TPS deferred — prepared (ad); OMO deferred — prepared (ah) — plus the doctrine's new build scope (Payroll PH, store workforce, dispatch), squad/remit assignment at SIB/OM | Product Manager, Tech Lead, 3–4 software engineers, QA automation engineer; shared UX/product designer (SEP pool); matrixed IAP engineer and DP data analyst |

### 5.1 Build-squad roles

| Role | Reports to | Responsibilities |
|---|---|---|
| **Product Manager (PM)** | CIO (solid); product-domain exec (dotted) | The build-side equivalent of the IT PO: outcomes, discovery, roadmap, budget; pairs with the BPO like any domain PO; owns product KPIs and DORA-aware delivery trade-offs |
| **Tech Lead** | Head of Engineering (solid); squad PM (dotted) | Technical design authority for the product; chairs squad design reviews; owns the product's architecture record at the ARB; one of the two build-side seats in the architect community |
| **Software Engineers (3–4)** | Tech Lead | Build and run the product: implementation, code review, on-call for P1/P2, telemetry, cost of the services they own (FinOps tags) |
| **QA Automation Engineer** | Squad PM | Test strategy, automated acceptance and contract tests, regression harness, release verification — the build twin of the configure teams' QA & release analyst |
| **UX / Product Designer** (SEP pool, ~0.5 FTE per squad) | Head of Engineering | Flows, screens, and usability for internal and customer-facing surfaces of built products |

Engineers are **hired into the engineering career track** under the Head of Engineering, not
into per-squad silos — the track and the SEP paved road (§6) are what keep two squads from
becoming two incompatible cultures.

---

## 6. Software Engineering Platform (SEP)

A new **platform team** (the sixth) in the operating model's platform layer. SEP treats build
squads — and, increasingly, configure teams' automation needs — as its customers.

| Member | Role |
|---|---|
| **Head of Engineering** | Engineering standards, squad staffing, technical career track, SEP roadmap; ARB member |
| **DevEx engineers (2)** | The **paved road**: golden-path service templates, CI/CD pipelines, feature-flag and telemetry tooling, internal developer platform — the default way to ship, so squads never assemble their own toolchain |
| **AppSec engineer** | SDLC security: SAST/DAST gates, dependency and SBOM policy, secrets management, threat-review facilitation (dotted to SEC lead) |
| **QA automation lead** | Shared test framework, contract-testing harness against IAP contracts, load-test rigs |
| **Product designer** | Shared UX pool for build squads (~0.5 FTE each) |
| **Build SRE** | Ring-deployment infrastructure, production readiness reviews, on-call coaching for squads (pairs with INFRA SRE) |

---

## 7. Engineering Standard (SDLC for built products)

Built products follow one standard, enforced by the paved road rather than by memo:

1. **Golden path.** New services start from SEP templates (repo layout, CI/CD, observability,
   IaC). Deviating requires an ARB-recorded exception.
2. **Trunk-based development, feature flags.** Continuous integration; incomplete work ships
   dark behind flags; no long-lived branches.
3. **Contract-first integration.** Every integration to another product is an IAP-published
   contract (event or API) with automated consumer-driven contract tests; no squad may call
   another product's database directly.
4. **Ring deployment.** Internal ring → canary stores/DCs → fleet, with automated rollback
   gates on SLO burn. Built products deploy independently of the ERP monthly train (OM §8.2).
5. **Security gates.** SAST + dependency scan on every merge; DAST before each release ring
   expansion; SBOM per release; secrets never in code. The AppSec engineer can block a ring
   expansion.
6. **Data contracts.** Every dataset a built product publishes to DP carries a tested schema
   contract; breaking changes go through the DP shared-object change process (OM §6.3).
7. **Production readiness review** (SEP + INFRA) before first fleet ring: on-call runbook,
   SLOs, capacity model, DR posture — typhoon-season resilience is a launch criterion, not a
   follow-up.
8. **DORA targets** (per squad, reported at QBR): deployment frequency ≥ weekly; change lead
   time < 1 week; MTTR < 4 hours; change-failure rate < 15%.

---

## 8. Vendor & Platform Lifecycle Management

The two-tier doctrine eliminated BoB capability products, but not lifecycle management —
it re-scoped it. What remains under managed lifecycle:

- **Vendor commodities** (LLM APIs, the Atlassian Cloud IT-tooling suite — JSM/Jira/Confluence/Bitbucket under Atlassian Guard, per A6.6; managed SOC, outsourced L1 contact center, hardware and
  license vendors): **operational ownership stays in the owning team** — vendor roadmap
  intelligence, release-intake owner, SLA escalation single point of contact (the team's
  Platform Product Manager, OM §5.4); **commercial ownership consolidates in the CIO Office
  vendor-portfolio analyst** (v3.1, with OM v3.12) — contracts, price-escalation caps,
  renewal/exit clauses and the tier-1 TPRM interface — one register and one negotiating
  posture for the doctrine's commodity-only vendor estate. IT-tooling SaaS such as the A6.6
  suite is commodity procurement exactly like the rest of this line — outside capability
  sourcing, and no conflict with the no-buy guardrail (which bars bought *capability*
  products).
- **Already-built in-house platforms** (the POS estate, the ecommerce platform, the
  gift-card/loyalty stack): owned like any product — release rings, regression packs,
  currency KPIs — by their owning teams. W5516 (registered under its 2026-09-03 title)
  remains the workflow-level owner of this lifecycle.
- **In-suite EBS currency:** the RUP/CPU cadence, the ADOP rehearsal discipline, and the
  de-customization reviews of `02-oracle-ebs/customization-governance.md` replace the old
  bought-product upgrade-currency KPI.

Contract clauses required at signature (vendor commodities): Philippine
 data-residency/processing terms (RA 10173), statutory-readiness warranty where applicable,
 exit/transition assistance, data-export in open formats, and price-escalation caps. The
 staging-ring release-intake ring and tier-1 TPRM reassessment apply to vendor commodities
 exactly as before; the exit-reserve accrual applies to replaceable vendor dependencies —
 the in-house platforms are forever by doctrine, so their resilience is a DR/run-cost
 question, not an exit question. Upgrade currency: vendor commodities at most one major
 version behind vendor current — two versions behind is a Tier & Control Board escalation.

---

## 9. Funding, TCO & Capitalization

| Rule | Detail |
|---|---|
| **Persistent envelopes survive** | All teams — configure, integrate, build — remain persistent-capacity funded (OM §8.4); nothing reverts to project funding |
| **Build envelopes** | Build squads carry their run cost (squad + infrastructure) in the product envelope; **PFRS / IAS 38** capitalization of qualifying development costs is assessed quarterly with FIN (Controller) — FIN owns the accounting policy, the squad owns the evidence trail |
| **TCO-per-product accounting** | FinOps tags 100% of spend to products (already OM policy); in-suite and vendor-commodity licenses carry license/support + integration run cost; built products carry squad + cloud cost. Every QBR shows TCO per product |
| **Sourcing reserve** | The CIO Office central bucket (OM §8.4) funds sourcing transitions — evaluations, migrations, exit execution — so no team's steady-state capacity is cannibalized by a sourcing move |
| **Exit reserves** | Per §8 — accrued centrally, disclosed in the QBR FinOps pack |

---

## 10. KPIs by Archetype

Headline KPIs live in OM §8.3 (which adds OMO, TPS and SEP rows). Summary:

- **Configure products:** unchanged OM v1.x KPIs (uptime, close cycle, filing timeliness…).
- **Vendor commodities:** SLA attainment, integration latency vs budget, version currency,
  regression-pack pass rate on vendor releases. **Already-built platforms:** currency and
  regression-pack pass rate like any build product.
- **Build products:** DORA metrics (§7 rule 8) **plus** product outcome KPIs (e.g., OMO: routing
  decision latency, split-order success rate; TPS: on-time job-site delivery, staging
  schedule adherence) — a squad green on DORA but flat on outcomes is failing.

---

## 11. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Integration sprawl silently recreating the pre-ERP silo estate | IAP is the only integration path; contract-first rule (§7 rule 3); ARB reviews every new pipeline; SEP/IAP co-own the contract catalog |
| Fragmented statutory compliance (payroll built outside EBS) | The statutory split (fit-gap §6) keeps every output with exactly one owning system; Payroll PH posts journals to the EBS ledger with per-period tie-out; control-mapping appendix per decision (§3.3) |
| Build squads drifting from the paved road into private toolchains | Golden path + exception records; Head of Engineering owns the engineering track; DORA reporting surfaces drift quickly |
| Key-person risk on built products | Bus-factor ≥ 2 per service (squad review rule); SEP owns runbooks; no solo-owned services |
| Vendor lock-in on commodities (LLM APIs) | Exit clauses, data-export rights, funded exit reserves (§8), annual re-evaluation triggers (§4) |
| Sizing creep — engineering hiring outpacing value | SIB gate requires the build case to beat the in-suite answer; QBR structural review can merge/sunset squads like any product (OM §10); IT sizing stays inside the 65–130 two-tier band (OM §9.2) |
| Control-evidence gaps across vendor boundaries | Control-mapping appendix at decision time; Tier & Control Board signs off changes touching Tier-1 workflows on any product (OM §6.3) |

---

## 12. Agentic Automation Program (VS-30 Engineering · VS-128 Governance)

The company maximizes **agentic AI**: AI agents that execute manual tasks end-to-end inside
guardrails. The program rides entirely on structures that already exist — the sourcing gate
(§3), the register (§4), the AAP platform team (OM §5.3), and VS-128's governance discipline
(model registry, risk tiering, kill-switch, AI incident management, ethics review, RA 10173
automated-decision obligations, ISO 42001/NIST-AI-RMF alignment).

### 12.1 The autonomy ladder (agents obey the workflow Tier register)

| Workflow tier | Agent autonomy | Rule |
|---|---|---|
| **Tier 1** (1,396 workflows) | **Human-approval-gated only** | Agent drafts, summarizes, flags, or prepares — a named human decides and signs (approval-matrix evidence retained) |
| **Tier 2** (3,302) | **Bounded autonomy** | Agent acts inside hard guardrails (limits, whitelists, value caps); sampled human audit; auto-escalation on anomaly |
| **Tier 3** (758) | **Autonomous-in-bounds** | Agent completes the task unattended; full audit trail; kill-switch active |

Hard boundaries regardless of tier: no agent owns a statutory filing path (BIR/SSS/PhilHealth/Pag-IBIG — human sign-off terminal); no agent acts on the POS/OT estate; no agent may hold SoD-conflicting duties (e.g., vendor-create + payment-approve); every agent action is audit-trailed as control evidence against the 808-control register.

### 12.2 Agent lifecycle (extends the VS-128 model discipline)

1. **Candidate intake** — the per-workflow Automation Opportunity inventory (5,433 workflows)
   plus VS-133 process mining surface candidates; scored by hours × frequency × error rate ×
   feasibility (derivable from each workflow's Time Estimate / Staffing Implication data).
2. **Proposal** — the **owning product team** (the team whose workflow it is) proposes with its
   BPO; SIB routes the sourcing per the §3 gate (in-suite platform-native automation = use
   EBS; custom agents on the paved road = build — vendor agent products are not a sourcing
   exit; foundation-model APIs remain commodity procurement under tier-1 TPRM) — the same
   gate, one more domain.
3. **Registration & review** — agent registered in the VS-128 registry with a risk tier; AI
   ethics review for anything touching customers, employees, money, or personal data
   (RA 10173 DPIA where automated decisions affect data subjects).
4. **Evaluation** — offline evals → **shadow mode** (agent runs beside humans, no actions) →
   **canary** (bounded actions, sampled audit) — graduation gated by AAP's eval engineer and
   the owning team's QA analyst.
5. **Operation** — AAP runtime: tools are IAP contracts only (no direct database access);
   non-human identity with its own ERP roles; kill-switch with rule-based fallback; drift and
   cost telemetry; quarterly re-registration (or retirement).
6. **Sunset** — QBR portfolio review retires underperforming agents like any product.

### 12.3 Rollout posture (crawl → walk → run)

- **Crawl (read-only):** revenue-assurance leak candidates (VS-118), vendor-scorecard drafts
  (VS-67), LP exception triage (VS-23), store-audit prep, contract-clause checks (VS-100).
- **Walk (draft-with-approval):** PO/reorder drafts feeding the VS-02 ROP engine, journal-entry
  drafts for FIN's close pack, freight-audit matching proposals (VS-110).
- **Run (bounded autonomy on T2/T3):** returns triage, document classification (VS-88),
  planogram-compliance checks (VS-55), data-hygiene sweeps.

### 12.4 Workforce and change

Augmentation-first sequencing; VS-134 owns task redesign, reskilling, and adoption metrics;
CBA/labor-relations sensitivity (VS-84) is assessed before any agent that materially changes
a represented role; the Change & Training Lead pool carries rollout for the 6,911-user base.

## 13. Related Documents

| Document | Relationship |
|---|---|
| [`it-product-operating-model.md`](it-product-operating-model.md) | The operating model this sourcing strategy reshapes (v3.30: 17 teams of record incl. AAP — 15 active, the TPS and OMO build squads deferred — prepared — archetypes per the two-tier doctrine, SEP, SIB, 108 FTE active of the 122-design — the IT department's structure of record; active headcount re-based 6,911 with the Trade department disabled — prepared (registry CAP-B01) and the TPS and OMO build squads deferred — prepared on this register's §4 amendments) |
| [`technical-guidelines.md`](technical-guidelines.md) | §1 POS/offline architecture protected by the Core-tier guardrail; §5 multi-vendor integration reference |
| [`../01-model-company/model-company-profile.md`](../01-model-company/model-company-profile.md) | §14.1 two-tier landscape (in-suite EBS core + in-house/already-built products) |
| [`../01-model-company/data-volumes-and-integrations.md`](../01-model-company/data-volumes-and-integrations.md) | The ten external integration clusters and transaction volumes IAP dimensions against |
| [`../01-model-company/internal-controls-matrix.md`](../01-model-company/internal-controls-matrix.md) | The 808-control register every sourcing decision must map to |
| [`../01-model-company/headcount-reality-check.md`](../01-model-company/headcount-reality-check.md) | IT need band (65–80 pre-hybrid; 65–130 hybrid/two-tier) the 122-FTE sizing lands in |

---

*Document Version: 3.20 | Date: 2026-09-23 | **Role-anchoring-remediation companion re-point only (batch 31).** The companion operating model bumps to v3.30 (its IAP seats anchored per the official TO v3.4 batch-31 remediation — anchoring census 259 chartered / 259 anchored / 0 zero-anchor / 65 weakly anchored, the zero-anchor worklist cleared) and the companion OM pin moves to v3.30; the Downstream TO pin moves to v3.4. No sourcing-register, gate, archetype or §4 amendment change. Prior v3.19 | Date: 2026-09-23 | **Role-anchoring-contract companion re-point only.** The companion operating model bumps to v3.29 (its Downstream pin moves to the official TO **v3.3** role-level workflow-anchoring contract — by direction every chartered role must carry ≥1 explicit RACI anchor in the catalog, census 262 chartered / 206 anchored / 56 zero-anchor / 18 weakly anchored pinned by validate-repo.sh Check 71, the zero-anchor worklist and weak-anchor watchlist emitted in the role-coverage matrix's Role-Anchoring Contract section); the header and §13 companion pins re-point and the companion OM pin moves to v3.29. No sourcing-register, gate, archetype or §4 amendment change. Prior v3.18 | Date: 2026-09-23 | **OMO build squad deferred — prepared (2026-09-23 (ah), by direction): §4 register amendment.** The Omnichannel order routing row (VS-60) moves from **Build (unchanged 2026-09-03)** to **Build — squad deferred — prepared** — with BOPIS the only enabled online fulfillment option (registry CAP-F01) every sale completes as a regular POS sale at the customer-selected store and routing is deterministic; the OMO build squad's 7 seats defer (IT 115 → 108 active; OM v3.28), the platform's prepared design retained, the row's re-evaluation trigger re-pointed from 'None — differentiating' to any second online fulfillment origin (CAP-F04–F09) or marketplace channel (CAP-C03/C04) enabled, and the §5 archetype table's Build-squads row annotated. No gate, §8, §12 program, or sizing change; the companion OM pin moves to v3.28 on the header and the §13 row. Prior v3.17 | Date: 2026-09-23 | **Eighty-fourth-wave consistency review — companion re-point only.** The operating model gains a v3.27 body true (the Downstream profile pin moves to v3.10 — profile §14.1's TPS landscape row re-cut to 'Deferred — prepared' with the Field-Service-dispatch seam clause, the executive-summary sibling the (ad) pass itself re-cut), so the companion OM pin moves to v3.27 on the header and the §13 row. No sourcing-rule, §12.1 ladder, or §12.2 intake-figure changes. Prior v3.16 | Date: 2026-09-23 | **Eighty-third-wave consistency review — the §13 companion-artifacts row's own (ad)-cascade residue.** The §13 OM row this register's own (ad) amendment had version-re-pointed still carried the stale clause 'active headcount re-based 6,925 with the Trade department disabled — prepared' — the half-repaired-cell class on the very row the (ad) pass touched (the active canon is 6,918 since the TPS build squad's deferral); the row re-pointed to v3.26 with the clause recut to name both deferrals (the trade-desk disablement per registry CAP-B01 and the squad deferral per this register's §4 amendment). No register row, archetype, gate or TCO change; companion OM pin moves to v3.26 (header and §13 row). Prior v3.15 | Date: 2026-09-23 | **TPS build squad deferred — prepared (2026-09-23 (ad), by direction): §4 register amendment.** The Trade & project services coordination row (VS-74/VS-77/VS-143) moves from **Build (unchanged)** to **Build — squad deferred — prepared** — the TPS build squad's 7 seats defer with the trade desk disabled (IT 122 → 115 active; OM v3.25), the platform's prepared design retained, the row's re-evaluation trigger re-pointed from 'None — differentiating' to CAP-B01 re-enablement, and the §5 archetype table's Build-squads row annotated; consumer bulky install/haul-away stays covered by the in-suite Field Service dispatch core and the CCP dispatch experience layer. No gate, §8, §12 program, or sizing change; the companion OM pin moves to v3.25 on the header and the §13 row. Prior v3.14 | Date: 2026-09-23 | **Companion re-point only — the seventy-ninth-wave profile/technical-guidelines trues.** The profile (v3.8) re-cuts §4's Corporate-HQ-Personnel row to the two-canon active form (525 active of the 532-role design — the (x) settlement's §4-table footing residue) and technical-guidelines (v3.6) re-bases §2.2's HQ bandwidth-sizing cell to the active canon, so the companion OM pin moves to v3.24 on the header and the §13 row (the OM's own companion re-point for these bumps). No sourcing-rule, §12.1 ladder, or §12.2 intake-figure changes. Prior 3.13 | Date: 2026-09-23 | **Companion re-point only — the OM's trade-desk-disablement Downstream pins.** The operating model gains a v3.23 body true (the Downstream TO/profile pins move to v3.0/v3.7 — the Trade / Account Management department is DISABLED — PREPARED per registry CAP-B01; the active headcount canon re-bases HQ 525 / total 6,925 with the 7-role design retained in the TO §5.3 register), so the companion OM pin moves to v3.23 on the header and the §13 row; the §12.4 Change-&-Training-Lead line's user base re-points to the 6,925 active population. No sourcing-rule, §12.1 ladder, or §12.2 intake-figure changes. Prior 3.12 | Date: 2026-09-23 | **Companion re-point only — the OM's capability-switchboard reconciliation.** The operating model gains a v3.22 body true (batch 30 admits W5580 Capability Switchboard Operation & Channel Enablement Impact Governance into PA-113.2/VS-113 — the CIO Office load trues 84 → 85 and the reconciliation reads 4,937 + 496 = 5,433), so the companion OM pin moves to v3.22 on the header and the §13 row. The §12.1 autonomy ladder's Tier-2 reference count re-bases 3,301 → 3,302 and the §12.2 candidate-intake inventory reads 5,433 workflows (W5580 confirmed directly Tier 2). No sourcing-rule, §12.2 intake-figure program, or lifecycle changes. Prior v3.11 | Date: 2026-09-23 | **Companion re-point only — the OM's capability-registry Downstream pin.** The operating model gains a v3.21 body true (the Downstream profile pin moves to v3.6 — profile §8.1 now defers to the new channel-capability-registry, BOPIS the only enabled online sales capability), so the companion OM pin moves to v3.21 on the header and the §13 row. No sourcing-rule, §12.1 ladder, §12.2 intake-figure, or program changes. Prior v3.10 | Date: 2026-09-23 | **Companion re-point only — the OM's pickup-only-BOPIS Downstream pin.** The operating model gains a v3.20 body true (the Downstream profile pin moves to v3.5 by the pickup-only BOPIS mandate — every ecommerce sale completes as a regular POS sale at the customer-chosen store), so the companion OM pin moves to v3.20 on the header and the §13 row. No sourcing-rule, §12.1 ladder, §12.2 intake-figure, or program changes. Prior v3.9 | Date: 2026-09-23 | **Seventy-fifth-wave consistency review — the vendor-commodity estate names the Atlassian suite.** The 2026-09-23 A6.6 incorporation (assumptions v4/v5) put the company's IT toolchain on the Atlassian Cloud SaaS subscription but never reached this model: §8's vendor-commodity enumeration (LLM APIs, managed SOC, outsourced L1 contact center, hardware and license vendors) had no line for it and §12.2's 'the doctrine's sole vendor product line' parenthetical could be misread against A6.6. §8's line names the Atlassian Cloud IT-tooling suite (JSM/Jira/Confluence/Bitbucket under Atlassian Guard, per A6.6) with the clause stating IT-tooling SaaS is commodity procurement outside capability sourcing (the no-buy guardrail bars bought *capability* products, not tooling); §12.2's parenthetical trued to 'in capability sourcing' with the §8 cross-reference. Ownership routing unchanged — operational in the owning team, commercial in the CIO Office vendor-portfolio analyst. No sourcing-rule, §12.1 ladder, §12.2 intake-figure, or program changes; the companion OM pin moves to v3.19 on the header and the §13 row (the OM's own companion re-point for this bump). Prior v3.8 | Date: 2026-09-23 | **Seventy-first-wave consistency review — companion re-point only.** The operating model gains a v3.18 body true (the Downstream profile pin moves to v3.4 by the seventy-first wave's returns-canon cascade — the profile §5 POS-mix returns bullet trued to the production-measured ~0.04% AR-credit-memo canon), so the companion OM pin moves to v3.18 on the header and the §13 row. No sourcing-rule, §12.1 ladder, §12.2 intake-figure, or program changes. Prior v3.7 | Date: 2026-09-23 | **Sixty-sixth-wave consistency review — companion re-point only.** The operating model gains a v3.17 body true (the Downstream TO/profile pins moved to v2.8/v3.3 by the same-day TO and profile sizing-basis true-ups), so the companion OM pin moves to v3.17 on the header and the §13 row. No sourcing-rule, §12.1 ladder, §12.2 intake-figure, or program changes. Prior v3.6 | Date: 2026-09-21 | **Sixty-second-wave consistency review — companion re-point only.** The operating model gains a v3.16 body true (§11 companion-artifacts catalog quote 5,427-WF → 5,432-WF, the batch-26 straggler), so the companion OM pin moves to v3.16 on the header and the §13 row. No sourcing-rule, §12.1 ladder, §12.2 intake-figure, or program changes. Prior v3.5 | Date: 2026-09-21 | **EBS documentation-coverage gap fill (batch 26) — companion re-point and ladder re-base.** W5578/W5579 join the catalog: the §12.1 autonomy ladder's Tier-2 reference count re-bases 3,299 → 3,301 and the §12.2 candidate-intake inventory 5,430 → 5,432 workflows; the companion OM pin moves to v3.15 on the header and the §13 row (CORP 924 → 925, FIN 809 → 810, domain subtotal 4,935 → 4,937). The six fit-gap closures behind this batch (H12–H17) are all in-suite adoptions, so the two-tier posture is reinforced, not changed: nothing moved to the build tier. Prior v3.4 | Date: 2026-09-21 | **ERP customization-governance gap fill (batch 25) — companion re-point and ladder re-base.** W5575–W5577 (Customization Decision Record intake & admissibility gate; CEMLI register maintenance & quarterly object-inventory audit; extension de-customization, retirement & budget reclamation — PA-113.1, VS-113) join the catalog: the §12.1 autonomy ladder's Tier-2 reference count re-bases 3,296 → 3,299 and the §12.2 candidate-intake inventory 5,427 → 5,430 workflows; the companion OM pin moves to v3.14 on the header and the §13 row (CIO Office 81 → 84, platform + CIO subtotal 492 → 495). The three workflows sit downstream of this model's own gate: W5515 decides use-EBS versus build, and the new records govern the configure-versus-extend boundary inside the suite — no sourcing posture, tier, archetype or §1–§11 content changes. Prior v3.3 | Date: 2026-09-15 | **EBS-exhaustion audit (with fit-gap v1.2):** by direction, every Oracle EBS capability that can be used is used — §2's Built row re-worded (dispatch leaves the 'EBS does not ship' list: Oracle Field Service is the in-suite dispatch core per fit-gap D13; the build narrows to the consumer appointment/route-optimization/contractor-portal experience layer; store workforce re-scoped to the genuinely-absent scheduling/optimization layer, OTL covering timecards), §4's dispatch row re-classed **In-suite core + narrowed build**. No gate, §5 archetype/seat, §8, §12 program, or sizing changes — the companion OM pin stays v3.13. Prior v3.2 (2026-09-14): **Structure-promotion conformance (with OM v3.13 / TO v2.3 / profile v3.0):** §12.4's user-base figure re-based 6,762 → 6,911 (the promoted headcount); the OM companion is confirmed as the IT department's structure of record. No gate, Register, §12 program, or sizing changes — the companion OM pin moves to v3.13. Prior v3.1 (2026-09-14): **Vendor-estate shape optimization (with OM v3.12):** §5's configure-and-integrate row names the single **Platform Product Manager** seat per team (WLI's seat doubling as the chain-wide **Oracle Relationship & In-Suite Currency Manager**; OM §9.1 converts WLI's second vendor seat to in-suite WMS/OTE functional-analyst depth); §8's vendor-commodity line re-scoped — operational ownership (roadmap intelligence, release intake, SLA escalation) stays in the owning teams while **commercial ownership (contracts, price-escalation caps, renewal/exit clauses, tier-1 TPRM interface) consolidates in the CIO Office vendor-portfolio analyst**. No gate, Register, §12 program, or sizing changes — the companion OM pin moves to v3.12. Prior v3.0 (2026-09-14): **Two-tier sourcing doctrine (2026-09-14):** *if it's in Oracle EBS we use it; otherwise we build* — the Buy tier is eliminated for capability products (vendor LLM APIs remain commodity procurement under tier-1 TPRM, not capability sourcing). The §2 landscape collapses to in-suite/build with the no-buy guardrail; the §3 gate becomes use-EBS → build (the fit-gap register is the standing evidence base); the §4 Register is re-issued — the four 2026-09-03 Buy rows superseded (WMS/TMS → in-suite Oracle WMS/MSCA + Shipping/Transportation Execution; WFM/FSM → build), the POS estate, the custom ecommerce platform and the gift-card/loyalty stack recorded as already-built platforms (integrate, never rebuild), **Payroll PH** issued as a build (Oracle Payroll not adopted; Core HR + GL stay in EBS; period costing posts via the GL interface) — the realization blueprint and the full resolution record live in `../02-oracle-ebs/` (fit-gap §4). The §5 archetype 'Buy-and-integrate' is renamed **'Configure-and-integrate'** with product/vendor management re-pointed to the Oracle relationship, in-suite currency (RUP/CPU) and the commodity vendor line (OM v3.11); §8 re-scopes to Vendor & Platform Lifecycle Management — vendor commodities + already-built platforms + in-suite currency, with W5516 remaining the lifecycle owner under its 2026-09-03 registered title; §10/§11 KPIs and risks re-worded. §12 unchanged — the autonomy ladder reads Tier 1 = 1,396 register rows, Tier 2 = 3,296, Tier 3 = 758 of 5,450 rows over 5,427 unique workflows, and the §12.2 intake figure reads 5,427 workflows (Check 59 pins); the companion OM pin moves to v3.11. No §12 program-rule changes. Prior v2.10 (2026-09-10): **Batch-24 gap-fill reconciliation:** W5574 Concessionaire Connectivity Request, Approval & Independent-Circuit Governance (PA-07.1, VS-07; workflow-gap-analysis.md batch 24 — confirmed directly Tier 2) true the §12.1 ladder's Tier-2 count 3,295 → 3,296 (register 5,450 rows = 5,427 unique + 23 sub-workflow rows; Tier 1 unchanged at 1,396; Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,427 workflows; the companion OM pin moves to v3.10 (SSP 906 → 907 in the OM's §3.2/§4.9, reconciliation 4,935 + 492 = 5,427). No sourcing-rule, §12.2 intake-figure program, or §12.2 lifecycle changes. Prior v2.9 (2026-09-07) | **Tenth-wave consistency-review companion re-point:** the tenth-wave adjudication of the sixth-wave-flagged VS-151 workload-attribution residual (SSP 906 / DP 189, subtotals re-based to their member sums 4,934 + 492, total unchanged 5,426) bumped the operating model to **v3.9**; the companion OM pin moves to v3.9. No sourcing-rule, §12.1 ladder, §12.2 intake-figure, or program changes. Prior v2.8 (2026-09-07): **Ninth-wave consistency-review repair (companion-pin chain):** the sixth-wave OM bump to v3.8 (2026-09-05, post-batch-23 reconciliation repair) never cascaded to this model's companion-pin chain — the footer's newest OM-pin clause still pointed at v3.7, the header companion pin had been stranded at v3.3 since batch-19 (the batch-20 cascade's 'header/§13 OM pins re-pointed' claim re-pointed only the §13 row), and the §13 Related-Documents OM row itself froze at v3.4 at batch-20 — all three live pins re-pointed in one pass, the companion OM pin moves to v3.8, and this clause restores the newest-pin chain. No sourcing-rule, §12.1 ladder, §12.2 intake-figure, or program changes. Prior v2.7 (2026-09-05): **Batch-23 gap-fill reconciliation:** the four gas-leak, tsunami/storm-surge, media-exposé & server-room-environmental workflows (W5570 in PA-24.2; W5571 in PA-26.1; W5572 in PA-14.3; W5573 in PA-27.2; workflow-gap-analysis.md batch 23 — the same analysis produced the custody register's tenth wave, events E-46–E-49) true the §12.1 ladder's Tier-1 count 1,394 → 1,396 (W5570 the pre-ignition life-safety class of the W5537/W5538 precedent; W5571 the coastal-water evacuation-and-clearance class of the W1449/W5562 precedent) and Tier-2 count 3,293 → 3,295 (W5572 the brand-integrity comms-contingency class of W5563/W5568; W5573 the IT-facility-contingency class of W5547/W5564; register 5,449 rows = 5,426 unique + 23 sub-workflow rows; Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,426 workflows; the companion OM pin moves to v3.7. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v2.6 (2026-09-05): **Batch-22 gap-fill reconciliation:** the four terminal-tampering, procurement-impersonation, account-takeover & commute-disruption workflows (W5566 in PA-08.2; W5567 in PA-03.2; W5568 in PA-14.2; W5569 in PA-141.2; workflow-gap-analysis.md batch 22 — the same analysis produced the custody register's ninth wave, events E-42–E-45) true the §12.1 ladder's Tier-2 count 3,289 → 3,293 (W5566 the payment-device security class of W1205/W5547, W5567 the procurement-fraud contingency class of W5559/W5563, W5568 the brand-integrity channel-contingency class of W5563/W5550, and W5569 the workforce-continuity class of W5561/W4255; register 5,445 rows = 5,422 unique + 23 sub-workflow rows; Tier 1 unchanged at 1,394; Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,422 workflows; the companion OM pin moves to v3.6. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v2.5 (2026-09-05): **Batch-21 gap-fill reconciliation:** the four storefront-crash, brand-impersonation-scam, wallet-outage & adjacent-works workflows (W5562 in PA-147.2; W5563 in PA-100.2; W5564 in PA-08.1; W5565 in PA-20.3; workflow-gap-analysis.md batch 21 — the same analysis produced the custody register's eighth wave, events E-38–E-41) true the §12.1 ladder's Tier-1 count 1,393 → 1,394 (W5562, the life-safety structural-clearance class of the W5537/W5555 precedent) and Tier-2 count 3,286 → 3,289 (W5563/W5564/W5565 — the brand-integrity event class of W5557/W5550, the payment-platform contingency class of W5547/W5548, and the asset-protection contingency class of W5560/W5133; register 5,441 rows = 5,418 unique + 23 sub-workflow rows; Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,418 workflows; the companion OM pin moves to v3.5. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v2.4 (2026-09-05): **Batch-20 gap-fill reconciliation:** the four cyber-extortion, payment-diversion, land-occupation & water-continuity workflows (W5558 in PA-27.3; W5559 in PA-18.2; W5560 in PA-178.1; W5561 in PA-07.2; workflow-gap-analysis.md batch 20 — the same analysis produced the custody register's seventh wave, events E-34–E-37) true the §12.1 ladder's Tier-1 count 1,392 → 1,393 (W5558, the enterprise-trading-halt & statutory-continuity class of the W5545/W5546 enforcement-and-filing precedent) and Tier-2 count 3,283 → 3,286 (W5559/W5560/W5561 — the financial-crime contingency class of W5541/W2814, the landbanking asset-protection class of W5133/W5143, and the facility-continuity class of the W470 power analog; register 5,437 rows = 5,414 unique + 23 sub-workflow rows; Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,414 workflows; the companion OM pin moves to v3.4. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v2.3 (2026-09-05): **Batch-19 gap-fill reconciliation:** the four in-transit-security, fatality-scene, tampering-extortion & recruitment-fraud workflows (W5554 in PA-06.2; W5555 in PA-147.3; W5556 in PA-89.1; W5557 in PA-121.1; workflow-gap-analysis.md batch 19) true the §12.1 ladder's Tier-1 count 1,390 → 1,392 (W5555/W5556, the life-safety scene-and-clearance class of the W5536/W5537/W5538 precedent) and Tier-2 count 3,281 → 3,283 (W5554/W5557; register 5,433 rows = 5,410 unique + 23 sub-workflow rows; Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,410 workflows; the companion OM pin moves to v3.3. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v2.2 (2026-09-05): **Batch-18 gap-fill reconciliation:** the four channel-enforcement, employee-legal-status, OSH-enforcement & app-store-removal workflows (W5550 in PA-10.3; W5551 in PA-19.1; W5552 in PA-24.1; W5553 in PA-75.1; workflow-gap-analysis.md batch 18) true the §12.1 ladder's Tier-1 count 1,389 → 1,390 (W5552, the DOLE imminent-danger stop-work order — the OSH statutory-enforcement class) and Tier-2 count 3,278 → 3,281 (W5550/W5551/W5553; register 5,429 rows = 5,406 unique + 23 sub-workflow rows; Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,406 workflows; the companion OM pin moves to v3.2. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v2.1 (2026-09-05): **Batch-17 gap-fill reconciliation:** the six regulatory-shock, platform-outage & governance-continuity workflows (W5544 in PA-36.1; W5545/W5546 in PA-79.3; W5547 in PA-08.1; W5548 in PA-54.2; W5549 in PA-24.1; workflow-gap-analysis.md batch 17) true the §12.1 ladder's Tier-1 count 1,387 → 1,389 (W5545/W5546, the statutory-deadline-protection class) and Tier-2 count 3,274 → 3,278 (W5544/W5547/W5548/W5549; register 5,425 rows = 5,402 unique + 23 sub-workflow rows; Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,402 workflows; the companion OM pin moves to v3.1. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v2.0 (2026-09-05): **Emergency & continuity gap-fill reconciliation:** the eight emergency & continuity workflows (W5536/W5539 in PA-07.2; W5537/W5538 in PA-24.2; W5540 in PA-19.2; W5541 in PA-18.3; W5542 in PA-105.3; W5543 in PA-118.2; workflow-gap-analysis.md batch 16 — the same analysis produced the custody register's third wave, events E-19–E-22) true the §12.1 ladder's Tier-1 count 1,384 → 1,387 (W5536/W5537/W5538, the life-safety in-store emergency class) and Tier-2 count 3,269 → 3,274 (W5539–W5543; register 5,419 rows = 5,396 unique + 23 sub-workflow rows; Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,396 workflows; the companion OM pin moves to v3.0. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v1.9 (2026-09-04): **Demand-intake gap-fill reconciliation:** the §3 gate's upstream front door now has a workflow-level owner — **W5535** (Capability Demand Intake & Backlog Triage; PA-113.2 — raise → log & triage against the 188-VS catalog → route to team backlog / workflow-catalog gap-admission / the W5515 sourcing gate → Product-Council capacity funding, with an accepted/routed/declined-with-reason closed loop via the BPO; workflow-gap-analysis.md batch 15) — admitted directly confirmed Tier 2 — so the §12.1 ladder's Tier-2 count is trued 3,268 → 3,269 (register 5,411 rows = 5,388 unique + 23 sub-workflow rows; Tiers 1/3 unchanged at 1,384/758) and the §12.2 intake figure reads 5,388 workflows; the §3 intro names the front door explicitly; the companion OM pin moves to v2.9. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v1.8 (2026-09-04): **Operations-workflow gap-fill reconciliation:** the three operations workflows (W5532 in PA-19.3; W5533 in PA-79.2; W5534 in PA-23.2; workflow-gap-analysis-operations.md) true the §12.1 ladder's Tier-1 count 1,383 → 1,384 (W5533, the statutory BIR 2316-furnishing admission) and Tier-2 count 3,266 → 3,268 (W5532/W5534; register 5,410 rows = 5,387 unique + 23 sub-workflow rows; Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,387 workflows; the companion OM pin moves to v2.8. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v1.7 (2026-09-03): **Finance-workflow gap-fill reconciliation:** the three finance workflows (W5529 in PA-42.3; W5530/W5531 in PA-17.3/PA-17.4; workflow-gap-analysis-finance.md) true the §12.1 ladder's Tier-2 count 3,265 → 3,266 (register 5,407 rows = 5,384 unique + 23 sub-workflow rows; Tier 1 rises 1,381 → 1,383 on the two statutory-execution admissions W5530/W5531, Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,384 workflows; the companion OM pin moves to v2.7. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v1.6 (2026-09-03): **People-capability & reporting-policy gap-fill reconciliation:** the four people/finance-policy workflows (W5525–W5527 in PA-19.4; W5528 in PA-17.4; workflow-gap-analysis-people.md) true the §12.1 ladder's Tier-2 count 3,261 → 3,265 (register 5,404 rows = 5,381 unique + 23 sub-workflow rows; Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,381 workflows; the companion OM pin moves to v2.6. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v1.5 (2026-09-03): **IT gap-fill reconciliation:** the seven VS-27 IT-operating-model workflows (W5518–W5524, workflow-gap-analysis-it.md) true the §12.1 ladder's Tier-2 count 3,256 → 3,261 and Tier-3 count 756 → 758 (register 5,400 rows = 5,377 unique + 23 sub-workflow rows) and the §12.2 intake figure reads 5,377 workflows. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v1.4 (2026-09-03): **Sourcing-model gap-fill reconciliation:** the rest of this model's program machinery now has workflow-level owners — **W5515** (Sourcing Decision Gate Operation & Capability Sourcing Register; PA-113.3 — the §3 gate and §4 Register: scored configure → buy → build assessment, the §3.3 mandatory appendices incl. the 808-control mapping, SIB/Product-Council/CEO decision-rights routing, annual QBR reaffirmation and re-evaluation triggers), **W5516** (Best-of-Breed Product Lifecycle Management, Vendor Release Intake & Exit Reserves; PA-113.2 — the §8 lifecycle: staging-ring release intake with the Tier-1-mandatory regression pack, the defer-one-never-two upgrade-currency KPI, §8 contract-clause verification, tier-1 TPRM reassessment, QBR exit-reserve accrual), and **W5517** (SEP Paved Road & Engineering Standard Governance for Built Products; PA-113.1 — the §6/§7 standard: golden-path starts with ARB-recorded exceptions, trunk-based/feature-flag delivery, contract-first IAP + data contracts, ring deployment with SLO-burn rollback and the AppSec block right, production readiness review, DORA-at-QBR) — admitted directly confirmed Tier 2 — so the §12.1 ladder's Tier-2 count is trued 3,253 → 3,256 (register 5,393 rows = 5,370 unique + 23 sub-workflow rows) and the §12.2 intake figure reads 5,370 workflows. No program-rule changes. Prior v1.3 (2026-09-03): **Agentic gap-fill reconciliation:** the §12.2 agent lifecycle now has workflow-level owners — W5512–W5514 in VS-128.3 (intake/sourcing/registration, shadow & canary evaluation with autonomy-tier ratification, runtime/guardrail/kill-switch telemetry with quarterly re-registration & QBR sunset), admitted directly confirmed Tier 2 — so the §12.1 ladder's Tier-2 count is trued 3,250 → 3,253 (register 5,390 rows = 5,367 unique + 23 sub-workflow rows) and the §12.2 intake figure reads 5,367 workflows. No program-rule changes. Prior v1.2 (2026-09-03): **Consistency repair (§12.1 tier-count true-up):** the
autonomy ladder's tier figures are re-pointed to the criticality register's current Summary counts
(1,381 / 3,250 / 756 register rows; sum 5,387 rows = 5,364 unique workflows + 23 parent/summary
sub-workflow rows) — v1.1 had quoted the pre-confirmation snapshot (1,375 / 3,243 / 754 of the
5,372-row register as it stood before the 2026-09-02 post-catalog confirmation of
W5497–W5510 and the 2026-09-03 W5511 addition). Guarded going forward: validator Check 59
now re-derives this table from the register's Summary on every run. No program-rule changes.
Prior v1.1 (2026-09-03): **Agentic extension (with OM v2.1):** new §12
Agentic Automation Program — autonomy ladder wired to the workflow Tier register, agent
lifecycle (intake → SIB routing → VS-128 registration → shadow/canary evaluation → operation
→ QBR sunset), hard boundaries (statutory filings, POS/OT, SoD), crawl-walk-run posture, and
workforce/change rules (VS-134, VS-84); two register rows added (agentic runtime = build →
AAP; foundation-model access = buy under tier-1 TPRM); related-docs table renumbered to §13.
Prior v1.0 (2026-09-03): initial issue with the hybrid capability-sourcing decision
(unified ERP core + best-of-breed WMS/TMS/WFM/FSM edges + in-house OMO/TPS differentiators);
IT sizing impact in OM §9 (115 FTE at v2.0) and `optimal-table-of-organization.md`
(HQ 504 / total 6,904 at v1.3).*
