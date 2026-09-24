# BuildRight Depot Corp. — The AI-First Operating Guide

> The complete operating guide for running a company of this industry **AI-first**: every rule
> needed to organize, decide, automate, and improve — written to be **ERP-agnostic** (no vendor
> is named or required), **sourcing-neutral** (best-of-breed COTS and in-house builds are
> interchangeable behind capability contracts), **agent-capable** (the company builds and runs
> AI agents as governed digital workers), and **knowledge-centred** (one central knowledge base
> is the persistent memory of every human and every agent, which is what makes the whole system
> consistent). Any company of similar industry can adopt this model by following §11; the
> BuildRight Depot Corp. corpus in [`01-model-company/`](../01-model-company/) is the reference
> instantiation of every construct defined here. At any point, in any situation, §9 tells every
> person and every agent exactly what to do.

---

## 1. Purpose, Scope & Reading Guide

### 1.1 What this guide is

This guide is the **operating system of the company** — the single, complete description of how
the enterprise runs when it is AI-first. It synthesizes the reference corpus into portable
doctrine: the process catalog (188 value streams, 569 process areas, 5,433 workflows), the
control register (808 controls), the sourcing model, the IT product operating model, and the
AI/ML governance discipline are the **evidence base**; this document is the **playbook** an
adopting company runs.

Everything in it is enforced by a mechanism defined in this guide or in the corpus it cites —
there are no aspirational principles. Every law (§2) names its enforcement; every role (§9)
names its decision rights; every situation (§9.5) names its first move.

### 1.2 Who reads it, and where to start

| Reader | Start at | Then |
|---|---|---|
| New employee (any function) | §9.7 The One-Page Card | §2 laws; the workflows of your own value stream |
| People manager / department head | §9 (ownership, decision rights, escalation) | §10 cadence and KPIs |
| Executive / board member | §2 laws; §3 architecture | §5 sourcing; §10 governance |
| IT / platform engineer | §3 architecture; §4 ERP-agnosticism | §7 agent factory; §8 knowledge base |
| Agent (AI digital worker) | §8.3 the read rule; §9.3 the decision procedure | its own Agent Charter (§7.2) |
| Adopting company (new to the model) | §11 adoption path | everything, in §11's order |

### 1.3 Scope

**In scope:** the operating doctrine — principles, architecture, sourcing, AI/agent operations,
knowledge management, decision rights, governance cadence, performance, and adoption.

**Out of scope (defined elsewhere in the corpus):** the workflow-level process detail
(`01-model-company/workflows/`), the requirement and control registers, vendor selection for a
specific platform (deliberately unnamed — see §4), and implementation project plans.

### 1.4 The model company reference parameters

The doctrine is calibrated on the reference instantiation — a PHP 62.3B-revenue big-box
home-improvement retailer: 200 stores × 29 staff, 4 DCs × 150,
HQ 511 active (TO design 532 — promoted from 362 on 2026-09-14, gap-filled +21 on 2026-09-18;
the 7-role Trade / Account Management department disabled — prepared 2026-09-23, registry
CAP-B01; the TPS build squad deferred — prepared 2026-09-23 (ad) and the OMO build squad
deferred — prepared 2026-09-23 (ah)), 6,911 employees (TO design 6,932), 5 legal entities, 35,000 active SKUs, 600 POS terminals, 2.8M
monthly transactions, ~600K loyalty members. Adopters substitute their own parameters using
the scaling rules in §11.3; nothing else in the model changes shape.

---

## 2. The Ten Operating Laws

These laws are absolute. Every other rule in the corpus is an application of one of them.

| # | Law | Statement | Enforced by |
|---|---|---|---|
| 1 | **One truth** | The enterprise knowledge base (EKB) is the only source of operational truth. No system, document, meeting, or model may carry a competing version of a canonical fact. | §8 (EKB, consistency engine, citation-or-refusal read rule) |
| 2 | **One owner** | Every workflow, agent, system, control, dataset, and KB artifact has exactly one accountable owner — a named role, never a committee. Unowned means broken; the absence of an owner is itself a P2 incident. | §9.1; the catalog's Owner field on all 5,433 workflows; W5535 gap-admission |
| 3 | **Contracts, not products** | Systems are interchangeable behind capability contracts. Nothing above the integration layer may know or care whether a capability is COTS, configured, or in-house. | §4 (capability-contract doctrine); single integration path (§3.5) |
| 4 | **Configure the core, buy the commodity, build the differentiator** | Every capability is sourced through one two-exit gate — use the core, else build — with scored criteria and registered decisions; commodity services are procured (tier-1 TPRM), not capability-sourced. Neither "we already own it" nor "we can build it" is an argument. | §5 (sourcing doctrine; the W5515 gate) |
| 5 | **Agents are workers, not features** | Every AI agent is a registered digital worker with an owner, a charter, an autonomy tier, a cost code, and a kill-switch — managed in the same portfolio governance as human staff and systems. | §7 (agent factory; lifecycle; portfolio) |
| 6 | **Autonomy is earned, tiered, and revocable** | An agent acts with exactly the autonomy its workflow's criticality tier licenses — drafted/approved for Tier 1, bounded for Tier 2, autonomous-in-bounds for Tier 3 — and any autonomy can be revoked instantly. | §6.3 (autonomy ladder); kill-switch (§7.1) |
| 7 | **Humans own judgment, law, and money** | Statutory filings, SoD-conflicting duties, the POS/OT estate, and Tier-1 decisions are terminal-human. AI prepares; people decide and sign where the law and the control register require it. | §6.4 (hard boundaries); the 808-control register |
| 8 | **Every action leaves evidence** | Every consequential action — human or agent — is immutably logged and traceable to a workflow step and a control objective. The log is audit evidence, not telemetry. | §8.7; control mapping; agent audit trail (§7.1) |
| 9 | **If it is not in the KB, it does not exist** | Decisions, exceptions, learnings, and new rules enter the EKB through the write path or they never happened. The same question must never need answering twice. | §8.4 (write path); §9.6 (gap-admission flywheel) |
| 10 | **No one is ever stuck** | For any situation there is always a next move: the universal decision procedure (§9.3), the escalation ladders with clocks (§9.4), and the closed-loop intake (§9.6) guarantee it — for humans and agents alike. | §9 (the no-confusion system) |

---

## 3. The Reference Architecture

### 3.1 Five layers on one knowledge plane, three cross-cutting disciplines

```
┌─────────────────────────────────────────────────────────────────────────┐
│  L6 EXPERIENCE        POS & store apps · mobile/web · agent consoles ·  │
│                       portals · alerts & approvals in-channel           │
├─────────────────────────────────────────────────────────────────────────┤
│  L5 INTELLIGENCE      AI & Agent Platform: agent runtime · tool         │
│                       registry · guardrails · evaluation harness ·      │
│                       model services (forecast, fraud, vision, LLM)     │
├─────────────────────────────────────────────────────────────────────────┤
│  L4 INTEGRATION       single integration path: event bus & API          │
│                       contracts · orchestration · non-human identity    │
├─────────────────────────────────────────────────────────────────────────┤
│  L3 SYSTEMS           composable estate: configured core (ledger of     │
│                       record) · bought commodity services · built       │
│                       differentiators — all behind contracts (§4–§5)    │
├─────────────────────────────────────────────────────────────────────────┤
│  L2 DATA              data platform · master data & MDM · data          │
│                       contracts · analytics & BI                        │
├─────────────────────────────────────────────────────────────────────────┤
│  L1 KNOWLEDGE PLANE   the Enterprise Knowledge Base (EKB): process      │
│                       catalog · registers · policies · decisions ·      │
│                       runbooks · the consistency engine (§8)            │
└─────────────────────────────────────────────────────────────────────────┘
      CROSS-CUTTING:  Identity & Security (human + non-human)  ·
                      Controls & Audit (control register, evidence)  ·
                      FinOps & Value (TCO per product, cost telemetry)
```

The layer rule: **each layer may only consume the layer below it through its published
interface** — experience surfaces call agents and APIs, agents call contract-registered tools,
integration carries contract-validated events, systems expose contracts, data publishes data
contracts, and the knowledge plane grounds everything. Skipping a layer (an agent querying a
database directly, a report screenscraping a UI) is an architecture violation escalated to the
Architecture Review Board.

### 3.2 The knowledge plane is a plane, not a project

L1 is infrastructure: the EKB exists before the first system is configured and outlives every
system (§8). This is what makes the model ERP-agnostic — the catalog, controls, and decisions
live in the knowledge plane; systems merely implement them. A core-system replacement
re-platforms L3 only; L1, L2, L4, L5, and L6 survive intact. That is the architectural meaning
of Law 3.

### 3.3 The system estate (L3) — composable by design

The estate holds every capability in one of exactly two sourcing postures, assigned per
capability by the gate in §5 — plus vendor commodity services, which are procurement
(tier-1 TPRM), not capability sourcing:

| Posture | What it holds (reference instantiation) | Property |
|---|---|---|
| **Configured core** | Financial ledger, procure-to-pay, the inventory ledger, warehouse & transport execution, HR/payroll, POS, approvals workflow | The systems of record (§4.2); protected by a core-tier guardrail — removal requires a CEO-noted waiver |
| **Built differentiator** | Omnichannel order orchestration; trade & project services platform; workforce scheduling & the field-service dispatch experience layer (the dispatch core rides the in-suite field-service module); the agent platform | In-house products on the engineering paved road — built only where the core platform has no adequate answer |
| **Commodity services** | Foundation-model APIs and other vendor utilities | Procured, not sourced: commodity procurement under tier-1 TPRM; integrated via L4; run-discipline per §5.4 |

### 3.4 L2 — Data

One data platform; master data governed under a single MDM discipline with one steward per
domain (§4.2); every dataset carries a **data contract** (tested schema, quality SLOs, named
owner); analytics/BI consume contracts, never system back-ends. The data layer is where the
EKB's canonical figures (§8.5) and the operational metrics (§10.2) are computed from — one
definition, one pipeline, one number.

### 3.5 L4 — Integration: the single path

All integration — system-to-system, agent-to-system, store-to-HQ — flows through one
integration plane (event bus + API gateway) of published, versioned contracts. Rules:

1. **No point-to-point** links and no direct database access across product boundaries.
2. **Contract-first:** a consumer may be built only against a published contract; breaking
   changes follow the versioning policy with consumer-driven contract tests.
3. **Events carry custody:** every cross-cutting event names its accountable value stream and
   precedence order (the reference corpus maintains an event-custody-and-precedence register —
   the generalizing rule: when two processes react to the same event, custody is decided once,
   in writing, never improvised).
4. **Non-human identity:** every agent and integration runs under its own least-privilege
   identity, reviewed like an employee's.

### 3.6 L5 — Intelligence (overview)

The AI & Agent Platform (AAP) is the paved road on which **all** AI runs — analytics models,
LLM assistants, and autonomous agents alike. Its components, the agent lifecycle, and the
portfolio discipline are specified in §7. Nothing outside the paved road may touch production:
unregistered models and unregistered agents are the same class of violation (Law 5).

### 3.7 L6 — Experience

Every human task is surfaced where the work happens — POS, store handheld, driver app, buyer
workbench, executive dashboard, chat. Approvals arrive in-channel with one-click context (the
workflow, the data, the agent's draft, and the evidence), because a slow approval path is the
ordinary failure mode of an AI-first company (the human is the scarce resource; §6.5).

### 3.8 Cross-cutting: identity, controls, value

| Discipline | Doctrine |
|---|---|
| **Identity & Security** | One identity fabric for humans, agents, and integrations; least privilege; SoD enforced across both human and non-human identities; security gates (SAST/DAST, dependency policy, secrets management) in every delivery path; OT/POS estate physically and logically separated — agents never act on it (§6.4) |
| **Controls & Audit** | The control register (808 objectives in the reference corpus) is the single control surface; every workflow maps to controls; every agent action and human approval is evidence against those objectives (Law 8); internal audit tests against the register, never against folklore |
| **FinOps & Value** | 100% of technology spend is tagged to a product; every product (human-staffed, bought, built, or agent) reports TCO and outcome KPIs at the quarterly review; agents report cost-per-task against the human baseline they replaced (§7.5) |

---

## 4. ERP Agnosticism — The Capability-Contract Doctrine

### 4.1 The rule set

The company is ERP-agnostic in architecture, not merely in procurement posture. The rules:

1. **Describe capabilities, not products.** Requirements, workflows, controls, and tests are
   written in capability language ("reserve inventory across origins within 2 seconds"), never
   in product language ("the ERP module does X"). The reference corpus demonstrates this at
   scale: 728 requirements in 38 categories and 5,433 workflows whose System-Touchpoints fields
   name capabilities and objects, not vendors.
2. **One system of record per data domain** (§4.2). Everything else subscribes. There is no
   such thing as "the same data in two systems" — only a system of record and its subscribers.
3. **Contract boundaries.** A system's scope ends at its published contracts. Whether the
   ledger is product A, product B, or in-house is invisible to workflows, agents, and analytics.
4. **Statutory localization is a scored criterion, not an assumption** (§5.1) — and the
   statutory obligation itself lives in the knowledge plane, so it survives any replacement.
5. **Portability is tested, not promised** (§4.3).

### 4.2 Systems of record (reference assignment)

| Data domain | System of record | Everyone else |
|---|---|---|
| Financial ledger (GL, AP, AR, assets) | Core ledger | Subscribes via posted-event contracts |
| Inventory ledger (quantities, values, accuracy) | Core inventory ledger | WMS/WFM/POS/commerce subscribe; the WMS executes, it never owns the ledger |
| Sales transactions & tender | Core (POS + commerce events) | Ledger, fraud, analytics subscribe |
| Vendor master | Core, MDM-stewarded | Subscribes |
| Product/item master & content | PIM (L2), synchronized to core | All channels consume PIM contracts |
| Customer identity & profile | Customer data platform | All channels consume CDP contracts |
| Employee master & payroll outcomes | Core HR master (people data); statutory payroll computed on the built payroll engine, posting journals to the core ledger | WFM subscribes for schedule/time |
| Order state (omnichannel) | Order-orchestration product (built or bought) | Ledger posts, commerce displays, WMS/FSM execute — all on its contracts |
| Warehouse/transport/workforce/dispatch execution state | Execution products of record — in-suite modules (WMS/TMS and the field-service dispatch core) or built platforms (workforce scheduling, the dispatch experience layer) per the two-tier sourcing register | Core subscribes for financial and HR effects |
| Enterprise knowledge (processes, controls, decisions) | The EKB (L1) | Everything reads; nothing else claims process truth |

**The rule that matters:** any capability may be re-sourced (§5) and at most L3 changes. If a
proposed change would move a system of record, that is a re-platform decision (§4.3), not a
sourcing decision, and carries the CEO-level weight of the core-tier guardrail.

### 4.3 The core portability test & re-platform procedure

The estate is ERP-agnostic only if replacing the core is a bounded program, not a rewrite.
The standing **portability test** (rehearsed annually as a tabletop, executed only via the
procedure below):

1. **Catalog intact?** All workflows, requirements, and controls read cleanly without naming
   the incumbent (capability language). Gaps are fixed in the KB, not in the migration.
2. **Contracts complete?** Every integration touching the core is a published contract with a
   consumer test suite — no hidden couplings (screenscraping, direct DB reads, file drops).
3. **Ledger exportable?** Ten-year statutory retention (the reference: ~1,230 GB uncompressed)
   exports in open formats on schedule; trial balances reconcile to the cent.
4. **Controls re-mappable?** Each of the register's control objectives has a demonstrated
   evidence source on the candidate platform (vendor attestation, API evidence, or audit trail).
5. **Agents re-targetable?** Agents act only through L4 tools; re-pointing a tool to a new
   contract is configuration, and the evaluation harness re-runs before re-entry (§7.4).

If the test fails, the defect is logged in the KB and remediated in the architecture — never
accepted as lock-in.

### 4.4 Anti-patterns that break agnosticism (forbidden)

- Workflows or requirements naming a product instead of a capability.
- Reports or agents reading another product's database.
- Business logic embedded in integration code rather than in the owning product or contract.
- "Temporary" direct links that outlive their migration (there are no temporary links).
- Statutory knowledge (rules, forms, deadlines) living only inside a vendor product rather
  than the knowledge plane.

---

## 5. Best-of-Breed Neutrality — The Sourcing Doctrine

### 5.1 The gate

Every capability decision — new capability, replacement, or re-sourcing — routes through one
gate (operated by the Sourcing & Investment Board, chaired by the CIO; demand enters through
the capability demand-intake front door, W5535 in the reference corpus). The test is ordered:
**use the core → build** — if the core platform ships the function (or can be configured to),
the answer is *use it*; build is admitted only when the core platform's standard answer
demonstrably does not exist (in the reference corpus, the fit-gap register is the standing
evidence base).
Scoring is the reference model's: strategic differentiation, fit-to-standard gap, integration
cost, data gravity, statutory localization (a vendor without the jurisdiction's statutory
readiness is disqualified where the capability is statutory), TCO, talent/key-person risk, and
exit strategy. Every decision carries five mandatory appendices: integration estimate,
control-mapping appendix against the control register, TCO sheet, the run-cost & talent
plan (build), and a re-evaluation trigger. Decisions with 3-year TCO above the investment threshold escalate to the
Product Council; core-tier removals require a CEO-noted waiver (Law 4 and §3.3).

### 5.2 The register

Every decision is recorded in the **Capability Sourcing Register** — capability, value streams,
decision, product/system, owning team, re-evaluation trigger. The register is the KB artifact
that makes the landscape auditable: any system that cannot be found in the register is
unmanaged, and its continued operation is a governance breach.

### 5.3 COTS and in-house are equal before the doctrine

Sourcing posture changes **who builds it**, never **how it is run**. Both a bought product and
an in-house product receive, identically:

| Obligation | Bought | Built |
|---|---|---|
| Named product owner | Vendor Product Manager in the owning team | Squad Product Manager |
| Lifecycle & release discipline | Staging-ring release intake; regression pack (Tier-1 workflows mandatory); at most one major version behind vendor current | Trunk-based delivery on the paved road; ring deployment; DORA targets (deploy ≥ weekly, lead < 1 week, MTTR < 4 h, change-failure < 15%) |
| Security gates | Vendor security attestation + integration tests | SAST/DAST/dependency gates in the pipeline; AppSec block right on ring expansion |
| Control evidence | Contractual attestation + API evidence mapped to the register | In-product audit trail mapped to the register |
| Exit/continuity | Exit clauses, data export in open formats, funded exit reserve | Bus-factor ≥ 2 per service, runbooks, production-readiness review |
| Capacity funding | License + integration run cost in the product envelope | Squad + cloud run cost in the product envelope |

The consequence: "best of breed" is decided per capability on merit (Law 4), and the operating
doctrine above the contract line never changes when the posture flips. A capability moving from
buy to build (or back) re-runs the gate, updates the register, and changes the owning team's
shape — nothing else.

### 5.4 The bought-edge lifecycle

Each bought product carries: the named Vendor Product Manager (contract, SLA, roadmap
intelligence, escalation single point); contract clauses for data protection/residency,
statutory-readiness warranty where applicable, exit/transition assistance, data export, and
price-escalation caps; tiered third-party risk management with annual reassessment for tier-1
vendors; and a centrally accrued **exit reserve** so no vendor exit is ever unfundable.

---

## 6. The AI-First Doctrine

### 6.1 What "AI-first" means operationally

AI-first is not "we use AI." It is a design discipline with eight rules:

| # | Rule | Test of compliance |
|---|---|---|
| D1 | Every workflow is authored with an explicit Automation Opportunity analysis | The catalog's Automation field is populated workflow-specifically, not generically (the reference corpus: 100% of 5,433 workflows) |
| D2 | Default-assume automatable; a manual step needs a reason | Each surviving manual step cites why: judgment, law, relationship, or physical presence |
| D3 | Humans do judgment, exception, and relationship work; agents do volume, pattern, and paperwork | Role charters and workflow steps reflect the split; "clerk of drafts" roles are redesigned at the QBR (§10.3) |
| D4 | Every AI capability runs on the paved road, registered and tiered | No shadow AI — unregistered models/agents are a security incident (§3.6, §7) |
| D5 | The approval path is as engineered as the work path | Approvals are in-channel, with context and one-click evidence (§3.7) |
| D6 | Every agent has a human owner who answers for it | The Owner field of every agent charter names a role in an owning product team (Law 2) |
| D7 | AI output is cited or refused | Agents answer from the knowledge plane with citation to canonical IDs; outside their ground truth they decline and route (§8.3) |
| D8 | Automation dividends are re-invested deliberately | Hours released are re-allocated by the QBR to service, coverage, or growth — not silently absorbed (§10.3; augmentation-first, §7.7) |

### 6.2 The hybrid workforce

The company operates one workforce roster with two worker classes:

- **Human workers**, with role charters in the table of organization, RACI accountability in
  workflows, and performance KPIs.
- **Digital workers (agents)**, with Agent Charters (§7.2) in the agent registry, RACI
  accountability in the same workflows (an agent may hold R — Responsible — for a step; the A
  — Accountable — role is always a human role), cost codes, and KPIs.

Where a workflow step's Role (R) is held by an agent, the step table records the agent's
registry ID. No workflow may assign A to an agent (Law 7).

### 6.3 The autonomy ladder

Agent autonomy is wired to the workflow criticality tiers — the same register that drives
regression coverage and incident SLAs (reference counts: Tier 1 = 1,396 register rows, Tier 2 =
3,302, Tier 3 = 758 of 5,456 rows over 5,433 unique workflows):

| Workflow tier | Agent autonomy | Rule |
|---|---|---|
| **Tier 1** (revenue-critical, statutory, safety) | **Human-approval-gated only** | The agent drafts, summarizes, flags, or prepares — a named human decides and signs, with approval-matrix evidence retained |
| **Tier 2** (operational core) | **Bounded autonomy** | The agent acts inside hard guardrails (value caps, whitelists, rate limits); sampled human audit; auto-escalation on anomaly |
| **Tier 3** (analytics, low-risk support) | **Autonomous-in-bounds** | The agent completes the task unattended with full audit trail; kill-switch active |

Promotion up the ladder requires evaluation evidence (§7.4) and Tier & Control Board sign-off
where Tier-1 workflows are touched; demotion is instant and does not require a meeting — any
owner may pull their agent down a rung, and the platform may do it automatically on guardrail
or drift breach.

### 6.4 Hard boundaries (non-negotiable, any tier)

1. **No agent owns a statutory filing.** BIR/tax and social-statutory filing paths terminate in
   human sign-off, always.
2. **No agent acts on the POS/OT estate.** Store sales systems, RF guns, and operational
   technology are human-only surfaces; agents may consume their event streams read-only.
3. **No agent holds SoD-conflicting duties.** The same duty-conflict matrix that governs human
   roles governs agents (e.g., no agent both creates vendors and approves payments).
4. **No unregistered agent acts at all.** Registration (§7.3) precedes first production action.

### 6.5 Human–agent interaction patterns

| Pattern | When | Shape |
|---|---|---|
| **P1 Draft-and-approve** | Tier-1 steps | Agent produces the artifact with citations; human approves/edits/rejects in-channel; the approval is the control evidence |
| **P2 Copilot** | Knowledge work (buying, legal review, service) | Human drives; agent retrieves, drafts, checks; every artifact shows what the agent contributed |
| **P3 Exception-only operations** | Tier-2 volume work | The agent processes the queue; humans see only the exceptions, with the agent's reasoning and evidence pre-assembled |
| **P4 Autonomous-with-audit** | Tier-3 work | The agent acts; a sampled audit and anomaly detectors stand in for review |
| **P5 Agent-to-agent escalation** | Multi-step processes | Agents hand work to each other via contracts; the chain carries one consolidated human escalation when any link exceeds its guardrails |

The engineering corollary (D5): every pattern's human touchpoint is designed to cost seconds,
not hours — context pre-assembled, decision binary where possible, evidence one click deep.

### 6.6 What AI-first does to the organization

Spans widen and coordinator roles shrink because agents absorb coordination volume; the
 liberated hours fund exception-handling, customer-facing, and trade-skill roles. In the
 reference instantiation this is explicit and quantified: HQ rebalanced 362 → 532 (promotion 511 2026-09-14, gap-fill +21 2026-09-18) and the total
 6,762 → 6,932 (promoted to the actual structure 2026-09-14), with the IT function sized at
 122 FTE inside a 65–130 FTE band
 (including the 7-FTE AAP platform team). Every change of this class passes through change
 management with labor-relations sensitivity assessment before it touches a represented role
 (§7.7). The generalizing rule: **headcount is a model output, not an input** — the workflow
 catalog and automation portfolio compute it, and the table of organization is re-derived at
 each QBR.

---

## 7. The Agent Factory — Agents as Products

### 7.1 The paved road

All agents run on one platform (the AI & Agent Platform — in the reference corpus, a 7-FTE
platform team: platform lead, 3 agent engineers, 1 evaluation/AI-QA engineer, 1 agent-ops SRE,
1 AI-governance liaison). Domain teams deliver agents **on** the platform; the platform
enforces the road:

| Component | Doctrine |
|---|---|
| **Agent runtime** | One managed runtime for all agents; versioned, observable, replayable |
| **Tool registry** | An agent's entire action surface, and every tool wraps an L4 contract (§3.5) — never a direct database, file share, or admin console |
| **Guardrails** | Declarative limits per charter: value caps, whitelists, rate limits, content policies; breaches auto-escalate (P3/P5) |
| **Human-in-the-loop gates** | The tier ladder's approval points, wired into the approval matrix so evidence is captured automatically |
| **Evaluation harness** | Offline evals → shadow → canary (§7.4); graduation is gated, not assumed |
| **Observability & cost** | Per-agent, per-task telemetry: actions, escalations, takeovers, latency, token/cost — FinOps-tagged to the owning product |
| **Non-human identity** | Each agent = one identity, least-privilege roles, included in access reviews and SoD enforcement (§3.8) |
| **Kill-switch** | Instant revert to the rule-based fallback that existed before the agent; every agent ships with its fallback defined before go-live |
| **Registry** | The single inventory of agents (§7.3) — the agent twin of the sourcing register |

### 7.2 The Agent Charter (required fields)

No agent enters intake without a complete charter. The twelve required fields (the agent's
twin of the workflow format's required fields):

| # | Field | Content |
|---|---|---|
| 1 | Identity & registry ID | Name, version, unique registry ID |
| 2 | Purpose | The workflow(s) it automates, by W-ID, with the specific steps it owns (R) |
| 3 | Owning team & human owner | Exactly one accountable human role (Law 2) |
| 4 | Autonomy tier | Tier per §6.3, with the tier rationale |
| 5 | Tools | The whitelist of registry tools (contracts) it may call |
| 6 | Guardrails | Caps, whitelists, rate limits, content rules; escalation triggers |
| 7 | Escalation & fallback | Who/what receives escalations; the rule-based fallback on kill |
| 8 | Evaluation evidence | Dataset, thresholds, current pass rates, last eval date |
| 9 | Privacy & DPIA status | RA 10173-class assessment where personal data or data-subject decisions are involved |
| 10 | Cost code & baseline | FinOps tag; the human-hour baseline it is measured against |
| 11 | Boundaries acknowledgment | The four hard boundaries (§6.4) affirmed as not-violated |
| 12 | Re-registration due date | Quarterly cycle (§7.3, stage 6) |

### 7.3 The lifecycle (six stages, each with an owner and a gate)

| Stage | What happens | Gate to pass |
|---|---|---|
| 1. Intake | Candidate scored from the automation inventory (hours × frequency × error rate × feasibility — derivable from the workflow catalog's own Time Estimate/Staffing data); sourcing routed (platform-native automation = use the core, custom agent = paved-road build; vendor agent products are not a sourcing exit) | Sourcing gate (§5.1) |
| 2. Registration & review | Charter registered; risk tier assigned; ethics review for anything touching customers, employees, money, or personal data (DPIA where automated decisions affect data subjects) | Complete charter + review sign-off |
| 3. Evaluation | Offline evals on the frozen dataset → **shadow** (runs beside humans, no actions) → **canary** (bounded actions, sampled audit) | Thresholds met at each rung; QA + evaluation engineer sign-off |
| 4. Operation | Production on the paved road; telemetry live; sampled audit per tier; anomalies auto-escalate | Standing — drift or breach pulls the tier down (§6.3) |
| 5. Re-registration | Quarterly: charter re-affirmed, evals re-run, tier re-ratified, cost-per-task reviewed | Re-registration before the due date or the agent stops |
| 6. Sunset | Underperforming agents retired like any product at the portfolio review | Fallback re-validated, knowledge written back to the EKB (Law 9) |

In the reference corpus, stages 1–2, 3, and 4–6 are owned end-to-end by dedicated workflows
(W5512–W5514, VS-128.3) — the generalizing rule: **the agent lifecycle itself is a governed
process with workflow-level owners**, not a best-effort practice.

### 7.4 The evaluation standard

- Every agent has a frozen evaluation dataset with expected outcomes, built from real
  operational history; thresholds (e.g., task success, factual-citation rate, harm rate) are
  set at registration and may only tighten.
- Evals re-run on: model-version change, tool-contract change, prompt/flow change, and the
  quarterly re-registration — no exceptions, including "minor" changes.
- Production audit supplements evals: sampled human review (Tier 2) and outcome reconciliation
  (both tiers) feed a defect backlog; a failing agent is demoted before it is debated.

### 7.5 Operating telemetry & the value case

Every agent reports: hours of manual work automated per month, task success rate,
human-takeover/escalation rate, incident MTTR, and **cost-per-task vs. the human baseline** —
reviewed at the QBR beside the owning team's product KPIs. An agent green on engineering
metrics but failing its value case is sunset (Law 5 makes agents as accountable as people).

### 7.6 Portfolio governance

The agent registry is reviewed at every QBR like the rest of the portfolio: adoption, value,
risk tier distribution, and drift. New agent proposals follow the same intake as any other
demand (§9.6) — there is no separate, easier path for AI ideas, and no harder one.

### 7.7 Rollout posture and workforce transition

- **Crawl (read-only):** leak-detection candidates, scorecard drafts, exception triage, audit
  prep, contract-clause checks — agents that only read and propose.
- **Walk (draft-with-approval):** reorder drafts, journal-entry drafts, audit-matching
  proposals — P1 pattern on Tier-1/Tier-2 steps.
- **Run (bounded autonomy):** Tier-2/Tier-3 execution under guardrails — returns triage,
  document classification, compliance checks, data-hygiene sweeps.

Workforce rules: augmentation-first sequencing; task redesign and reskilling owned by the
change-management discipline; labor-relations assessment before any agent materially changes a
represented role; released hours re-invested by decision at the QBR (D8) — the portfolio,
not the platform, decides what automation means for jobs.

---

## 8. The Enterprise Knowledge Base — Persistent Memory & the Consistency Engine

The EKB is Law 1's mechanism and the model's center of gravity: **one governed corpus that is
the persistent memory of every human and every agent**, versioned, owned, validated, and
self-repairing. This is what makes the company consistent at scale — and what makes the model
adoptable, because the knowledge plane is the asset; systems come and go under it.

### 8.1 The canon — what the EKB holds

Every artifact class has exactly one canonical source, one accountable owner, and a version:

| Artifact class | Canonical content | Owner (reference) | Reference instantiation |
|---|---|---|---|
| Process catalog | Value streams → process areas → workflows, each with the required fields (trigger, frequency, volume, owner, participants, steps with RACI and durations, system touchpoints, time estimate, pain points/risks, automation opportunity, controls, cross-references) | The owning business-product owner, paired with IT | `workflows/` — 188 VS / 569 PA / 5,433 W |
| Workflow metadata registers | Criticality tiers, dependency map, system-touchpoint map, event custody & precedence | EA / owning teams | `workflows/workflow-*.md`, `event-custody-and-precedence-register.md` |
| Requirements register | Capability requirements with priority and traceability | Business + EA | `erp-requirements.md` (728 / 38 categories) |
| Control register | Control objectives, type, owner, mapped workflows | Finance/GRC with process owners | `internal-controls-matrix.md` (808) |
| Sourcing decisions | The Capability Sourcing Register | CIO Office / SIB | sourcing model §4 |
| Agent registry | Agent Charters, tiers, evaluation status | AAP + owning teams | VS-128 registry |
| Organization | Table of organization, role charters, headcount model | CHRO / executives | `optimal-table-of-organization.md` |
| Architecture & doctrine | This guide, the sourcing model, the operating model, technical guidelines | CIO / Head of EA | `07-methodology/` |
| Decisions & learnings | Decision log (deadlocks, precedents), incident post-mortems, retired-practice notes | The deciding body; EA curates | KB decision log |
| Glossary & vocabulary | Canonical terms, abbreviations, banned variants | EA | profile glossary + validator vocabulary guards |

**Corollary of Law 1:** a policy, rule, or number that is not in one of these artifact classes
does not exist operationally and cannot be enforced. The remedy is to write it into the canon
(§8.4), not to enforce it informally.

### 8.2 Architecture: canonical layer, derived layer, consumption layer

1. **Canonical layer.** Human-authored, version-controlled sources of truth (the reference
   corpus is a Git repository of Markdown + registers). Every change is reviewed, validated,
   and attributable. This layer is deliberately boring: plain files, plain tables, no magic.
2. **Derived layer.** Machine-generated indexes over the canon — search indexes, embeddings,
   knowledge-graph links, figure extracts — rebuilt from canonical sources on every change.
   The derived layer is **regenerable and never authoritative**: if it disagrees with the
   canon, it is wrong by definition.
3. **Consumption layer.** The retrieval interfaces humans and agents query: search, chat with
   citation, workflow viewers, register dashboards. Consumers never read systems' private
   documentation; they read the EKB.

### 8.3 The read rule (citation-or-refusal)

Every consumer of the EKB — human tool or agent — obeys one rule:

> **Answer from the canon, citing canonical IDs (VS / PA / W / CTL / REQ / registry IDs), or
> decline and route.** Guessing, improvising from training memory, or answering without a
> citation is a defect — for an agent, a defect with a ticket and an eval consequence.

This rule is what makes agents safe to scale: their knowledge is the company's knowledge,
versioned and current as of the last validated change, and every answer is checkable against
its citation.

### 8.4 The write path (how knowledge changes)

All changes to canon artifacts follow one path:

1. **Propose** — anyone (human or agent) files a change with rationale and evidence.
2. **Review** — the artifact's owner (and, where the change touches Tier-1 workflows, statutory
   surfaces, or the control register, the Tier & Control Board / GRC) reviews.
3. **Validate** — the consistency engine (§8.5) runs; the change passes only with zero errors.
4. **Publish** — version bumped with a change note (the house convention: a dated footer line);
   derived indexes rebuild; subscribers (agents' retrieval indexes, dashboards) update.

Emergency lane: during incidents, the incident commander may direct interim practice verbally,
but the write-back must land within the incident-review SLA or the interim practice is
retroactively void (Law 8/9).

### 8.5 The consistency engine

The EKB validates itself. A conformance suite (in the reference corpus: the repository
validator — 79 checks, run in CI and before every publish) enforces, at minimum, these check
classes:

| Check class | Invariant |
|---|---|
| Referential integrity | Every cited workflow, control, requirement, value stream, §-ref, and link resolves |
| Completeness | Every workflow carries every required field; every artifact class is populated |
| Canonical agreement | Figures quoted anywhere (counts, tier splits, totals) match the canonical register |
| Structure | Table integrity, anchor resolution, TOC completeness, name agreement across surfaces (file ↔ index ↔ register) |
| Vocabulary | One spelling per term; retired literals and superseded citations cannot reappear |
| Arithmetic | Inline scaling math re-derivable from the artifact's own data |
| Custody | Cross-cutting events have exactly one accountable value stream; declared splits are bidirectional |
| Uniqueness | No duplicate IDs; no duplicate titles; no orphan artifacts |
| Self-description | Documents' claims about their own checks/totals equal the live state |
| Registry closure | Live set = admitted set + declared-pending set (no silent coverage drift) |

The engine is what turns "consistent" from a hope into a property: **a change to the canon
that would make any two documents disagree is mechanically refused.** Adopters start the suite
small (referential integrity + completeness) and grow it with every defect class they meet —
the reference corpus grew it to 79 checks, each one the scar tissue of a real defect.

### 8.6 Agent memory rules

- **No private truth.** Agents hold no operational memory that overrides the canon; conversation
  state is session-scoped; long-term memory is the EKB.
- **Grounding.** Every task-relevant fact an agent uses is retrieved from the EKB (or from L2
  data via contracts) with citation (§8.3).
- **Write-back protocol.** When an agent discovers a gap (a workflow that does not match
  reality, a missing rule, a dead link), it files a KB change proposal (§8.4 step 1) — agents
  are the cheapest sensors the knowledge plane has.
- **Forgetting is governance.** Retired practices, superseded figures, and expired rules are
  moved to the canon's history layers with pointers — never left where retrieval can serve them
  as current (the reference corpus enforces this with retired-literal guards).

### 8.7 Ownership, versioning, evidence

Every canon artifact carries: one accountable owner (Law 2), a version (dated change note), and
— where the artifact evidences controls — audit-trail status as control evidence (Law 8).
Knowledge is retained per the records-retention policy; KB versions are themselves evidence of
what the company believed and enforced at any past date, which is what makes audits fast and
settles disputes with facts.

### 8.8 Knowledge SLAs

| Rule | SLA |
|---|---|
| Incident-driven canon change | Write-back within the incident-review window (§9.4) |
| Statutory/regulatory change | Canon updated before the effective date, owner named |
| Agent-discovered gap | Proposal filed within one business day of discovery |
| Stale artifact | Any artifact unreviewed for four quarters is flagged at the QBR and re-owned or retired |
| Retrieval currency | Derived layer rebuilt on every publish; consumers never serve stale indexes after a publish notice |

---

## 9. Who Does What — The No-Confusion System

This section is the answer to "at any point, anyone must not be confused on what to do."

### 9.1 The Ownership Rule

Every countable thing has exactly one accountable owner — a named role on the org chart:

| Thing | Owner is recorded in |
|---|---|
| Workflow | The workflow's Owner field (the "single throat to choke") |
| Process area / value stream | The business process owner (BPO) of the stream |
| System/product | The product team (IT PO/squad PM) with the BPO as business co-owner |
| Agent | The charter's human owner (§7.2 field 3) |
| Control | The control register's owner column |
| Dataset | The data contract's steward |
| KB artifact | The canon table (§8.1) owner column |

If a thing cannot be found in one of these registers, it is unowned: raising that gap is
everyone's job, and closing it is the intake path (§9.6). Ownership disputes are resolved by
the owning executive; unresolved past the deadlock clock, they escalate to the governance
cadence (§9.4).

### 9.2 Decision-rights master table

| Decision | Decides | Escalation |
|---|---|---|
| Day-to-day workflow execution & exceptions | The workflow's Owner field (R/A per step) | Department head |
| Capability sourcing (use-the-core/build) | Sourcing & Investment Board (CIO chair) | Product Council (TCO threshold); CEO for core-tier removal |
| Funding & portfolio priorities | Product Council | CEO/Board by materiality |
| Architecture exceptions & contracts | Architecture Review Board | CIO |
| Tier-1 changes, control-affecting changes | Tier & Control Board (with GRC) | CFO/CIO jointly |
| Agent autonomy tier & registration | AI governance discipline (VS-128-class) with AAP | AI ethics review for data-subject impacts; Tier & Control Board where Tier 1 is touched |
| Personal-data processing & DPIA | Data Protection Officer | General Counsel |
| Vendor contracts & exit | Vendor Product Manager + Procurement (clause set §5.4) | SIB for renewals/breaks |
| Incident response | Incident Commander per the incident ladder | Crisis executive for P1/disaster |
| HR/labor-relation impacts of automation | CHRO with change-management discipline | Executive committee; CBA process where represented |
| KB canon changes | The artifact owner (§8.4 review step) | Tier & Control Board / GRC where scoped |

"No decision" has an owner too: a decision that sits past its clock escalates automatically
(§9.4) — a decision may be appealed, never orphaned.

### 9.3 The Universal Decision Procedure (UDP)

Any person, at any level, facing any "what do I do now?":

1. **STOP-CHECK (only if needed).** If there is imminent danger to life/safety, suspected
   fraud, a statutory deadline at risk, or an active P1: act on the stop-check ladder first
   (§9.4) — contain, preserve, notify.
2. **Search the EKB.** Phrase the situation; read the canonical answer with its citations.
   (Agents: §8.3 is this step.)
3. **Locate the workflow.** Map the situation to its value stream/process area/workflow; the
   Trigger field tells you if this workflow applies; the Owner field tells you who owns the
   outcome; the Steps table tells you what good looks like.
4. **Check decision rights.** If a decision is needed, the master table (§9.2) says who decides
   — that is not for you to guess, and if it is you, decide; if not, route with context.
5. **Apply the defaults ladder if the canon is silent:**
   (a) protect life & safety → (b) comply with law & statutory deadlines → (c) protect the
   customer → (d) protect company assets & money → (e) preserve evidence → then act with the
   smallest reversible step, and notify the workflow owner.
6. **Record & close the loop.** Log the decision and its basis. If the canon was silent,
   ambiguous, or wrong, file the KB change proposal (§9.6) — you have found a defect in the
   operating system, and fixing it is part of the work.

The UDP is deliberately mechanical. It requires no seniority to run, it terminates (every step
has an exit), and step 6 makes the company smarter every time it is used.

### 9.4 Escalation ladders & clocks

| Ladder | Trigger | Path & clock |
|---|---|---|
| **Incident (P1/P2)** | Service down / control failure / safety event | On-call → Incident Commander (15 min for P1, 1 h for P2) → crisis executive if unresolved past SLA; post-mortem with KB write-back within the review window |
| **Decision deadlock** | Owner cannot decide or owners disagree | Owner → department heads (2 business days) → the governance body from §9.2 (next sitting, or on demand) |
| **Statutory at risk** | Any filing/compliance deadline in jeopardy | Named statutory owner + deputy immediately (dual-control never-miss rule); GRC and Counsel same day |
| **Agent anomaly** | Guardrail breach, drift alert, takeover spike | Auto-demotion (§6.3) + owner notification (minutes); AI incident process (§7) if harmful |
| **Ethics concern** | Suspected unfair/harmful automated or human decision | AI ethics review / speak-up channel (24 h acknowledgment, protected) |
| **Safety event** | Hazard to people | Stop work → safety officer → statutory reporting where required |

Clocks are commitments, not aspirations: missing one is itself reportable at the governance
cadence.

### 9.5 Situation playbook index

| Situation | Canonical custody | First moves |
|---|---|---|
| Normal operations | The workflow catalog | Run the workflow; UDP only on exception |
| Peak season / change freeze | Release-calendar & freeze workflow (W5521-class) | Freeze honored; only break-fix with Tier & Control Board approval |
| Typhoon / natural disaster | Disaster value stream (VS-69-class) + PAGASA-ladder custody in the event-custody register | Follow the signal ladder; incident command assumes custody of cross-cutting events |
| Vendor / edge-system outage | Owning team runbook + exit/continuity plan (§5.4) | Invoke fallback; incident ladder; BoB vendor escalation by the Vendor PM |
| Core (ledger) outage | Core continuity plan | Paper/branch continuity procedures; reconcile from event log on recovery |
| Agent misbehavior | §7 kill-switch + AI incident process | Kill → fallback → assess → post-mortem → re-evaluate before re-entry |
| Model drift / quality decay | VS-128-class monitoring | Demote a tier; re-train or retire; write back |
| Data breach / privacy event | Privacy value stream (VS-91-class) + DPO | Contain → preserve → DPO statutory clock → notify per law |
| Product recall / safety | Recall value stream (VS-89-class) | Traceability query via the catalog; quarantine; statutory notification |
| Internal/external audit | Control register + evidence trail | Answer with register citations; gaps become register changes, not side-letters |
| New capability needed | Intake front door (W5535-class) | §9.6 |
| "The KB and reality disagree" | §8.4 write path | Stop-check if harmful; file the change proposal; follow the canon until amended |

### 9.6 If the KB has no answer — the closed loop

A silence in the canon is a **defect with a workflow**, not a judgment call:

1. **Raise** it to the paired intake owner (the demand-intake front door — W5535-class).
2. **Triage** against the catalog: is this an enhancement (team backlog), a missing
   workflow-level owner (gap-admission path), or a new capability (sourcing gate)?
3. **Route** — and the raiser receives an accepted/routed/declined-with-reason answer (closed
   loop; nothing is dropped).
4. **Canonize** — the resolution lands in the EKB with a version note, so the question never
   needs asking again (Law 9). This flywheel is why an adopting company converges: every
   confusion, once raised, permanently reduces future confusion.

### 9.7 The One-Page Card

> **When facing any "what do I do?":**
> 1. Danger, fraud, statutory deadline, or P1? → Stop-check ladder (contain, preserve, notify).
> 2. Search the knowledge base — read the answer with its citations.
> 3. Find the workflow — its Owner owns the outcome; its Steps define the work.
> 4. Decision needed? → The decision-rights table says who decides. If you — decide.
> 5. Canon silent? → Defaults ladder: safety → law → customer → assets → evidence; smallest
>    reversible step; notify the owner.
> 6. Record it, and file the gap so the canon grows.
>
> **You are never stuck: there is always a next move, and moving makes the system better.**

---

## 10. Governance Cadence, KPIs & the Optimization Loop

### 10.1 Cadence

| Forum | Frequency | Agenda spine |
|---|---|---|
| Team standups / ops huddles | Daily | Exceptions, incidents, queue health |
| Operations review | Weekly | KPI deltas, incident post-mortems status, change calendar |
| Sourcing & Investment Board | Monthly + on demand | Sourcing gate decisions; register amendments |
| Tier & Control Board | Monthly + on demand | Tier-1/control-affecting changes; agent tier ratifications |
| Architecture Review Board | Bi-weekly | Contracts, exceptions, retirement of capabilities |
| AI ethics review | On demand + quarterly sweep | Data-subject impacts, fairness findings |
| **Quarterly business review** | Quarterly | Portfolio (products, vendors, agents) value & sunset; control register reaffirmation; agent re-registration sweep; headcount model re-derivation; exit-reserve accrual |
| Annual | Annually | Core portability test (§4.3); tier-1 vendor reassessments; strategy and catalog re-baseline |

### 10.2 KPI sets by layer

| Layer | Representative KPIs |
|---|---|
| Experience | Adoption, approval latency, task completion |
| Intelligence (agents) | Hours automated, task success, takeover rate, agent-incident MTTR, cost-per-task vs. human baseline, registry currency (100%) |
| Integration | Contract coverage (100% of flows), event latency vs. budget, failed-message rate |
| Systems | Uptime by tier, offline endurance (POS ≥ 8 h), release currency, DORA (built products: deploy ≥ weekly, lead < 1 week, MTTR < 4 h, CFR < 15%) |
| Data | Accuracy (inventory ≥ 97%), contract-test pass rate, SLA on pipelines |
| Knowledge | Validator green (0 errors), citation answer rate, gap-admission cycle time, artifact currency |
| Business | Close ≤ 5 working days, statutory filings on time (100%), shrinkage, turns, service levels |

Each KPI has one owner, one definition, one pipeline (§3.4) — a KPI without all three is
retired at the QBR.

### 10.3 The optimization loop

The company improves itself on a fixed loop, not by heroics:

1. **Measure** — process mining and the telemetry plane surface where work actually is (the
   reference corpus maintains a dedicated process-mining & continuous-improvement value stream).
2. **Prioritize** — automation candidates score hours × frequency × error rate × feasibility
   from the catalog's own data (§7.3 stage 1); defects and debt compete in the same backlog.
3. **Decide** — sourcing gate for capability moves; portfolio review for sunset/merge.
4. **Execute** — on the paved road; agents per §7; process changes through the write path.
5. **Re-derive** — headcount, staffing, and cost models re-computed from the changed catalog
   (§6.6); released hours re-invested by explicit decision (D8).
6. **Canonize & verify** — every change lands in the EKB and the consistency engine re-runs.

### 10.4 Continuous compliance

Controls are tested continuously where automation permits: control evidence flows from the same
audit trails that operations generate (Law 8), so audit readiness is a by-product of running
the system, and the control register — not tribal memory — defines what "compliant" means.

---

## 11. Adoption Path for a Similar Company

### 11.1 Preconditions

Adopting companies need: executive sponsorship (the CEO-noted core guardrail must mean
something), a paired business–IT leadership willingness (Law 2 is cultural before it is
mechanical), and the honesty to write down how work actually happens. Nothing else is a
precondition — the model assumes no incumbent systems (§4), no incumbent vendors, and no
prior documentation beyond what Phase 1 creates.

### 11.2 The seven-phase program

| Phase | Name | Outputs | Exit criteria |
|---|---|---|---|
| 0 | **Model the company** | Company profile: sites, volumes, org, financials, statutory context | Profile complete; reference parameters substituted (§11.3) |
| 1 | **Catalog the operating model** | Value streams → process areas → workflows with all required fields; tier classification; dependency map; event-custody register | Every capability has a workflow-level owner; validator checks 1–2 classes green |
| 2 | **Registers** | Requirements register; internal-controls register; requirement↔workflow matrix | Every workflow maps to ≥ 1 control; traceability bijection |
| 3 | **Organize** | Table of organization & role charters; headcount model derived from the catalog; IT product operating model (teams, RACI, governance) | Every workflow's owner resolves to a charted seat; gap-free team ownership |
| 4 | **Architect & source** | Technical guidelines; integration architecture; sourcing gate + Capability Sourcing Register decisions | Every capability carries a registered decision with the five appendices |
| 5 | **Stand up the knowledge plane** | EKB (canon in version control), derived indexes, consistency engine in CI | Zero validator errors; citation-grade retrieval live for humans |
| 6 | **Light the agent factory** | AAP paved road; registry; first crawl-phase agents; evaluation harness | First agents productive with kill-switches and baselines |
| 7 | **Optimize & scale** | Process-mining loop; walk/run-phase agents; QBR portfolio governance; expansion playbooks | The §10.3 loop runs unaided; conformance test (§11.4) passing |

Phases overlap once 1–2 are stable; the sequencing constraint is real, though: **the knowledge
plane (5) is fed by the catalog (1) and must exist before the agent factory scales (6)** — an
agent on an uncataloged process is an unmanaged risk, and a catalog without the validator is a
document, not a system.

### 11.3 Tailoring knobs (what scales, what doesn't)

| Parameter | Reference value | Scales how |
|---|---|---|
| Sites / staff | 200 stores × 29; 4 DCs × 150 | Linear in the catalog's Volume fields; store-standard workflows clone with local parameters |
| Assortment | 35,000 SKUs | Category structure scales; workflow shapes do not |
| HQ | 362 → 532 | Re-derived from the catalog at each QBR (§6.6) — never copy another company's HQ |
| IT function | 122 FTE (band 65–130 at ~6,900 staff) | Band scales with estate complexity; the team taxonomy (9–11 domain + platform teams) holds to ~2× the reference scale |
| Agents | Crawl → walk → run | The ladder, not the count, is the constant; start with five read-only agents, not fifty |
| Governance | The bodies in §9.2 | Merge bodies below the reference scale (SIB+ARB is viable early); never merge ownership (Law 2) |
| Statutory context | Philippines (BIR, SSS/PhilHealth/Pag-IBIG, RA 10173) | Substitute the jurisdiction's set in the registers; the hard-boundary structure (§6.4) is jurisdiction-independent |

### 11.4 The conformance test (you are running the model when…)

1. Every workflow has an owner, and every owner resolves to the org chart.
2. Every consequential action is traceable to a workflow step and a control objective.
3. Any employee can find "what do I do" in under a minute, with a citation.
4. Every system's scope ends at published contracts; there are zero point-to-point links.
5. The sourcing register names a decision, owner, and re-evaluation trigger for every capability.
6. Replacing the core ledger is a bounded program (the portability test passes on paper today).
7. Every agent is registered, chartered, tiered, evaluated, kill-switched, and cost-baselined.
8. No agent touches statutory filings, POS/OT, or SoD-conflicting duties — enforced by machine.
9. The knowledge base validates green in CI; nothing publishes with errors.
10. Agents answer with citations or refuse; the refusal rate is monitored, not hidden.
11. Every quoted figure in every document reconciles to a canonical register.
12. Decision deadlocks escalate on clocks without anyone lobbying for an exception.
13. The QBR reviews products, vendors, and agents in one portfolio with TCO and outcome KPIs.
14. Released human hours are re-invested by decision, visibly (D8).
15. The same question never needs answering twice — the gap flywheel is draining the queue.

Fourteen of fifteen at any audit is the working bar; item 9 is non-waivable.

### 11.5 Anti-pattern catalogue (what kills the model)

| Anti-pattern | Why it kills the model | Countermeasure |
|---|---|---|
| "AI strategy" without the catalog | Automating undescribed processes automates chaos | Phase 1 before Phase 6, no exceptions |
| Shadow AI (unregistered models/agents) | Ungoverned risk and duplicate truth | Registry + security-incident treatment (§3.6) |
| Vendor-shaped requirements | Lock-in through the back door; breaks portability | Capability language + validator vocabulary checks (§8.5) |
| Committee ownership | Nothing is owned when everything is co-owned | Law 2; named-role rule |
| Private agent memory | Divergent truth; unauditable behavior | §8.6 memory rules |
| Approval theater | Humans become the bottleneck; agents idle | In-channel approvals with context (D5, §3.7) |
| Validator as decoration | Consistency decays silently | CI enforcement; zero-error publish gate |
| Automation without re-investment decisions | Workforce distrust; value leaks | D8 and the QBR decision |
| Pilot purgatory | Perpetual demos, no production discipline | The lifecycle's gates are the same for pilots (§7.3) |

---

## 12. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Model drift or vendor model change silently degrades agents | Frozen eval sets re-run on every change; automatic tier demotion on breach (§6.3, §7.4) |
| Knowledge base becomes stale / shadow documents appear | One-canon rule; derived layer regenerable; currency SLAs; QBR staleness sweep (§8.8) |
| Automation sprawl recreates unmanaged complexity | Every agent/model through one gate and registry; QBR sunset like any product |
| Vendor lock-in despite contracts | Portability test annually; exit reserves; data-export clauses (§4.3, §5.4) |
| Over-automation of judgment work | Hard boundaries + tier ladder; D2's manual-step rationale is auditable |
| Governance overhead outgrows value | Bodies merged at small scale (§11.3); every governance artifact must name a decision it accelerates or it is retired |
| Key-person risk on built platforms | Bus-factor ≥ 2; paved-road runbooks; engineering career track (§5.3) |
| Workforce resistance / labor disputes | Augmentation-first, change-management ownership, CBA sensitivity assessment, visible re-investment (§7.7) |
| Statutory change outpaces systems | Statutory knowledge lives in the canon (§4.1); change SLA before effective date (§8.8) |
| Consistency engine itself rots | The engine validates its own self-descriptions (§8.5); adding a check is part of every defect repair |

---

## 13. Related Documents

| Document | Relationship |
|---|---|
| [`../01-model-company/model-company-profile.md`](../01-model-company/model-company-profile.md) | The reference company this doctrine is calibrated on (§1.4 parameters) |
| [`../01-model-company/workflows/value-stream-index.md`](../01-model-company/workflows/value-stream-index.md) | The process catalog — the EKB's largest canon artifact (188 VS / 569 PA / 5,433 W) |
| [`../01-model-company/erp-requirements.md`](../01-model-company/erp-requirements.md) | The capability-language requirements register (728 across 38 categories) demonstrating §4.1 rule 1 |
| [`../01-model-company/internal-controls-matrix.md`](../01-model-company/internal-controls-matrix.md) | The 808-control register behind Laws 7–8 |
| [`capability-sourcing-and-engineering-model.md`](capability-sourcing-and-engineering-model.md) | The reference sourcing gate, register, SEP paved road, and agentic program (§5, §7 instantiated) |
| [`it-product-operating-model.md`](it-product-operating-model.md) | The reference product-team operating model (17 teams of record / 122 FTE design; 15 teams / 108 FTE active — the TPS build squad deferred — prepared, 2026-09-23 (ad), and the OMO build squad deferred — prepared, 2026-09-23 (ah)) behind §9–§10 |
| [`technical-guidelines.md`](technical-guidelines.md) | The reference infrastructure, integration, security, and agentic-runtime architecture behind §3 |
| [`../01-model-company/workflows/event-custody-and-precedence-register.md`](../01-model-company/workflows/event-custody-and-precedence-register.md) | The event-custody doctrine (§3.5 rule 3, §9.5 disaster rows) |
| [`validate-repo.sh`](validate-repo.sh) | The reference consistency engine (79 checks) behind §8.5 |

---

*Document Version: 1.20 | Date: 2026-09-23 | **Eighty-first-wave consistency review — check-count self-descriptions re-pointed 78 → 79 with the validator's new Check 79.** The Oracle EBS behavioral-canon guard (`audit-oracle-conformance.py --guard`) — issued with the 2026-09-23 custody-and-treatment review and run manually beside the validator by every consistency wave since — is wired into the standard validation entry point as Check 79, and this guide's three check-count mentions (§8.5's two narrative forms and the §13 validate-repo row) re-point with it; Check 40's quoted-count forms extended with the two narrative phrasings so a future check addition cannot strand them again. No law, layer, lifecycle, or program changes. Prior v1.19 | Date: 2026-09-23 | **OMO build squad deferred — prepared (2026-09-23 (ah)): §1.4 re-base.** With BOPIS the only enabled online fulfillment option (registry CAP-F01) every sale completes as a regular POS sale and order routing is deterministic; the OMO build squad's 7 seats defer (IT 115 → 108 active; OM v3.28) and the active HQ population drops 518 → 511; the §1.4 reference-parameters cell re-bases ('HQ 511 active (TO design 532 … registry CAP-B01; the TPS build squad deferred — prepared (ad) and the OMO build squad deferred — prepared (ah)), 6,911 employees (TO design 6,932)'). §6.6's dated promotion arrows stand as frozen history. No law, layer, lifecycle, or program changes. Companion pin re-pointed: the methodology-index row moves to v1.19. Prior v1.18 | Date: 2026-09-23 | **Eighty-fourth-wave consistency review — the §13 OM navigation row's (ad) state annotation.** The §13 Related-Documents row for the IT operating model still described it as '(17 teams, 122 FTE)' — the bare pre-(ad) design form on a live navigation row, while the sibling instance (the sourcing model's §13 OM row) carries the full two-state form (16 active / 115 FTE active of the 122-design) and this guide's own §1.4 was re-based at (ad); the row re-cut to the two-state form. §11.3's tailoring-knob rows ('HQ | 362 → 532'; 'IT function | 122 FTE (band 65–130 at ~6,900 staff)') adjudicated NOT defects — the reference-value knob frame, the arrow form the §6.6 frozen-history adjudication covers, '~6,900 staff' rounding the 6,918 active canon. No law, layer, lifecycle, or program changes. Companion pin re-pointed: the methodology-index row moves to v1.18. Prior v1.17 | Date: 2026-09-23 | **TPS build squad deferred — prepared (2026-09-23 (ad)): §1.4 re-base.** With the trade desk disabled (x), the TPS build squad's 7 seats defer (IT 122 → 115 active; OM v3.25) and the active HQ population drops 525 → 518; the §1.4 reference-parameters cell re-bases ('HQ 518 active (TO design 532 … registry CAP-B01; the TPS build squad deferred — prepared 2026-09-23 (ad)), 6,918 employees (TO design 6,932)'). §6.6's dated promotion arrows stand as frozen history. No law, layer, lifecycle, or program changes. Companion pin re-pointed: the methodology-index row moves to v1.17. Prior v1.16 | Date: 2026-09-23 | **Seventy-seventh-wave consistency review (the (x) disablement's §1.4 straggler).** The reference-parameters cell still read 'HQ 532 … 6,932 employees' — the 2026-09-23 (x) trade-desk disablement re-based every active population canon to 6,925 / HQ 525 but skipped this guide (its cascade touched the OM, sourcing and technical-guidelines companions), and the cell's promotion parenthetical shipped a mangled fragment ('gap-filled +21 on 2026-09-18 — was 2026-09-14') the 09-18 gap-fill edit left behind; §1.4 re-based to the active canon with the design annotation ('HQ 525 active (TO design 532 … disabled — prepared 2026-09-23, registry CAP-B01), 6,925 employees (TO design 6,932)') and the fragment repaired. §6.6's dated promotion arrows (362 → 532; 6,762 → 6,932 — both endpoints dated events) adjudicated frozen history. No law, layer, lifecycle, or program changes. Guard: guide_figure_hits gains the §1.4 arm (the retired census form and the fragment banned, the active anchors required). Companion pin re-pointed: the methodology-index row moves to v1.16. Prior v1.15 | Date: 2026-09-23 | **Capability-switchboard admission (batch 30).** W5580 Capability Switchboard Operation & Channel Enablement Impact Governance (PA-113.2, VS-113 — the owning workflow for the channel-capability registry's enable/disable state changes) joins the catalog; the catalog triple, Law-2 owner row, D1 conformance row and §KB canon-table W counts re-point 5,432 → 5,433 (Tier ladder: Tier 2 = 3,302 of 5,456 rows over 5,433 unique workflows). No law, layer, lifecycle, or program changes. Companion pin re-pointed: the methodology-index row moves to v1.15. Prior v1.14 | Date: 2026-09-23 | **Production-volume calibration.** The §7 D1 ledger-exportable reference figure trued to the production-calibrated retention canon (~1,000 → ~1,230 GB uncompressed, per data-volumes-and-integrations.md §1.2 v4.7); no law, layer, lifecycle, or program changes. Companion pin re-pointed: the methodology-index row moves to v1.14. Prior v1.13 | Date: 2026-09-21 | **Sixty-second-wave consistency review (batch-26 straggler — the two count rows the catalog-triple pass missed).** Batch 26 re-pointed this guide's §1 catalog triple, §4/§7 canon-table counts and §KB artifacts to 5,432 but stranded the Law-2 owner row ('the catalog's Owner field on all 5,427 workflows') and the D1 conformance row ('100% of 5,427 workflows') at the retired total — both trued; no law, layer, lifecycle, or program changes. Companion pin re-pointed: the methodology-index row moves to v1.13. Prior v1.12 | Date: 2026-09-14 | Structure-promotion re-base (profile v3.0 / TO v2.3): the §1.4 reference-parameters line re-based (HQ 511 promoted from 362; 6,911 employees) and the §7/L9 liberated-hours instantiation re-worded to the promoted canon (6,762 → 6,911 promoted 2026-09-14; IT sized at 122 FTE in the 65–130 band). No law, layer, lifecycle, or governance changes. Prior v1.11 | Date: 2026-09-14 | Two-tier sourcing-doctrine alignment (sourcing model v3.0): the §3 L3 reference-architecture layer line trued — 'bought best-of-breed edges' → 'bought commodity services' (the two-tier doctrine eliminates bought capability products; vendor LLM APIs remain commodity procurement); the §4.2 systems-of-record reference assignment trued to the model canon — the execution-state row re-assigned from 'The bought edge systems (WMS/TMS/WFM/FSM)' to in-suite modules (WMS/TMS) or built platforms (workforce/dispatch) per the two-tier sourcing register, and the employee/payroll row re-assigned from 'payroll stays statutory-core' to the core HR master with statutory payroll computed on the built payroll engine posting journals to the core ledger (Payroll PH; Oracle Payroll not adopted). §5.3/§5.4 stand unchanged as posture-neutral doctrine. Companion pin re-pointed: the methodology-index row moves to v1.11. Prior v1.10 (2026-09-10) | Batch-24 gap-fill reconciliation (concessionaire connectivity request, approval & independent-circuit governance — W5574 in PA-07.1, confirmed directly Tier 2; workflow-gap-analysis.md batch 24) — catalog triple and §KB canon-table W counts re-pointed 5,426 → 5,427; §Tier-wired autonomy-ladder reference counts re-pointed (Tier 1 = 1,396 register rows, Tier 2 = 3,296, Tier 3 = 758 of 5,450 rows over 5,427 unique workflows). No doctrine, law, lifecycle, or program changes — the ladder obeys the workflow Tier register unchanged. Companion pin re-pointed: the methodology-index row moves to v1.10. Prior v1.9 (2026-09-07) | Eleventh-wave consistency-review repair (version-chain inversion): the version header had stayed at '1.0 | 2026-09-04 | Initial issue' through all eight re-point cascades (batch-16–23, v1.1–v1.8), each new clause appending below the initial-issue clause labeled 'Prior' with a higher version number and a later date — the only inverted version chain in the corpus (every other maintained doc keeps its newest clause leading under the live version), and invisible to the methodology-index rule because the index row's own '(v1.0' pin satisfied itself off the same stale footer. Chain re-based newest-first: live v1.9 (this clause), the eight prior clauses (v1.8 down to v1.1) standing as written in descending order, and the initial issue demoted to the v1.0 (2026-09-04) clause at the chain's end. No body-content changes — the catalog triple, Tier ladder, canon tables and §KB counts were already at batch-23 state; the quoted check-count self-descriptions re-point 71 → 72 with the validator's new Check 72. Guard gap closed: validate-repo.sh Check 72 added — every '*Document Version:' footer in the repo must carry a strictly decreasing Prior chain with no Prior at or above the live version (repo-wide, so the class is caught at the first inverted clause). Companion pins re-pointed: the methodology-index row and the root-README tree row move to v1.9. Prior v1.8 (2026-09-05): batch-23 gap-fill reconciliation (gas-leak, tsunami/storm-surge, media-exposé & server-room-environmental) — catalog triple and §KB canon-table W counts re-pointed 5,422 → 5,426; §Tier-wired autonomy-ladder reference counts re-pointed (Tier 1 = 1,396 register rows, Tier 2 = 3,295, Tier 3 = 758 of 5,449 rows over 5,426 unique workflows). Prior v1.7 (2026-09-05): batch-22 gap-fill reconciliation (terminal-tampering, procurement-impersonation, account-takeover & commute-disruption) — catalog triple and §KB canon-table W counts re-pointed 5,418 → 5,422; §Tier-wired autonomy-ladder reference counts re-pointed (Tier 1 = 1,394 register rows, Tier 2 = 3,293, Tier 3 = 758 of 5,445 rows over 5,422 unique workflows). Prior v1.6 (2026-09-05): batch-21 gap-fill reconciliation (storefront-crash, brand-impersonation-scam, wallet-outage & adjacent-works) — catalog triple and §KB canon-table W counts re-pointed 5,414 → 5,418; §Tier-wired autonomy-ladder reference counts re-pointed (Tier 1 = 1,394 register rows, Tier 2 = 3,289, Tier 3 = 758 of 5,441 rows over 5,418 unique workflows). Prior v1.5 (2026-09-05): batch-20 gap-fill reconciliation (cyber-extortion, payment-diversion, land-occupation & water-continuity) — catalog triple and §KB canon-table W counts re-pointed 5,410 → 5,414; §Tier-wired autonomy-ladder reference counts re-pointed (Tier 1 = 1,393 register rows, Tier 2 = 3,286, Tier 3 = 758 of 5,437 rows over 5,414 unique workflows). Prior v1.4 (2026-09-05): batch-19 gap-fill reconciliation (in-transit-security, fatality-scene, tampering-extortion & recruitment-fraud) — catalog triple and §KB canon-table W counts re-pointed 5,406 → 5,410; §Tier-wired autonomy-ladder reference counts re-pointed (Tier 1 = 1,392 register rows, Tier 2 = 3,283, Tier 3 = 758 of 5,433 rows over 5,410 unique workflows). Prior v1.3 (2026-09-05): batch-18 gap-fill reconciliation (channel-enforcement, employee-legal-status, OSH-enforcement & app-store-removal) — catalog triple and §KB canon-table W counts re-pointed 5,402 → 5,406; §Tier-wired autonomy-ladder reference counts re-pointed (Tier 1 = 1,390 register rows, Tier 2 = 3,281, Tier 3 = 758 of 5,429 rows over 5,406 unique workflows). Prior v1.2 (2026-09-05): batch-17 gap-fill reconciliation (regulatory-shock, platform-outage & governance-continuity) — catalog triple and §KB canon-table W counts re-pointed 5,396 → 5,402; §Tier-wired autonomy-ladder reference counts re-pointed (Tier 1 = 1,389 register rows, Tier 2 = 3,278, Tier 3 = 758 of 5,425 rows over 5,402 unique workflows). Prior v1.1 (2026-09-05): emergency & continuity gap-fill reconciliation (batch 16) — catalog triple and §KB canon-table W counts re-pointed 5,388 → 5,396; §Tier-wired autonomy-ladder reference counts re-pointed (Tier 1 = 1,387 register rows, Tier 2 = 3,274, Tier 3 = 758 of 5,419 rows over 5,396 unique workflows); the guide joins the register's confirmation chain for W5536–W5543 Prior v1.0 (2026-09-04): Initial issue: the complete AI-first, ERP-agnostic operating guide synthesized from the model-company corpus — ten operating laws; the six-layer reference architecture on the knowledge plane; the capability-contract doctrine (ERP agnosticism: systems of record, the core portability test); sourcing neutrality (COTS/built equivalence); the AI-first doctrine with the Tier-wired autonomy ladder and hard boundaries; the agent factory (paved road, twelve-field Agent Charter, six-stage lifecycle, evaluation standard); the Enterprise Knowledge Base as persistent memory (canon table, citation-or-refusal read rule, write path, consistency engine, agent memory rules); the no-confusion system (ownership rule, decision-rights master table, the six-step Universal Decision Procedure, escalation clocks, situation playbook index, the One-Page Card, the gap-admission flywheel); governance cadence, layered KPIs, and the optimization loop; and the seven-phase adoption path with tailoring knobs, the fifteen-point conformance test, and the anti-pattern catalogue. Companion figures re-verified against the canonical registers (5,388 workflows / 5,411 register rows / 808 controls / 728 requirements / 69 validator checks).*
