# IT Workflow Gap Analysis — BuildRight Depot Corp.

> Focused gap analysis of **IT-related workflows**, performed per the methodology in
> [workflow-gap-analysis.md](workflow-gap-analysis.md) §2 (defining-term keyword search across all
> PA files to distinguish *dedicated* coverage — a `## W` header that owns the capability — from
> *incidental* single-step references). Companion to the canonical thirty-pass gap history; this
> document does **not** amend that record. **Status (2026-09-03): adopted.** All six gaps were
> confirmed and filled as workflows **W5518–W5524**, allocated in
> [workflow-gap-analysis.md](workflow-gap-analysis.md) batch 8 and confirmed into the criticality
> register (5 × Tier 2, 2 × Tier 3); the G6 extension option was implemented as W5520 (the
> dedicated-workflow disposition rather than the W366 step-extension).

---

## 1. Scope

All workflows governing the **information-technology function** of the model company (200 stores,
4 DCs, HQ; ~6,911 employees (active; the TO's 532-design retains the disabled—prepared Trade department, the deferred—prepared TPS build squad (ad) and the deferred—prepared OMO build squad (ah)); ~1,500 ERP users; ~2,500+ endpoints; 600 POS terminals; the in-suite
ERP core of record — Oracle E-Business Suite 12.2 under the two-tier doctrine — plus in-house
built and already-built platforms per the Capability Sourcing Register), across:

- The **Technology & Data family** — 13 dedicated value streams, **394 workflows**:
  VS-27 (71), VS-28 (24), VS-29 (43), VS-30 (29), VS-99 (24), VS-113 (32), VS-115 (24),
  VS-126 (24), VS-128 (27), VS-135 (24), VS-137 (24), VS-151 (24), VS-190 (24).
- **Adjacent value streams with IT-facing scope**: VS-91 (consumer data privacy, 24), VS-26
  (BCP/IT-DR design, 31), VS-21 (internal audit/ITGC, 49), VS-161 (TPRM cyber attestations, 24),
  VS-149 (SCO/unattended tech ops, 24), VS-125 (fraud, 24),
  VS-112 (PMO), VS-134 (OCM/digital adoption), VS-88 (records/legal hold).

## 2. Method

1. **Inventory** every `## W` header in the 13 Technology & Data value streams (394 workflows) plus
   IT-scoped workflows hosted elsewhere (e.g., W434 NPC registration, W1205 PCI-DSS).
2. **Map** each capability of a reference full-stack IT operating model — ITIL 4 service/value
   stream practices, COBIT 2019 governance/management objectives, ISO/IEC 27001:2022 Annex A
   themes, NIST CSF 2.0 functions, plus enterprise-IT specialties (collaboration estate, identity,
   engineering enablement) — to the owning workflow(s).
3. **Flag** capabilities with no owning workflow, thin-partial coverage, or scattered ownership.
4. **Validate** each candidate gap by keyword search across all PA files; discard false positives
   (e.g., `"ISMS"` surface hits were substring matches inside *"mec**hanisms**"* — true hits: 0).

## 3. Current-State Coverage Map (confirmed covered — no gap)

| IT Capability | Owner workflow(s) | VS / PA |
|---|---|---|
| Service desk, incident, problem, request catalog, SLM/BRM, knowledge | W48, W378, W379, W392, W381, W380 | VS-27.1 |
| Change/CAB, release & patch mgmt, QA/testing, environments | W132, W1409, W495, W391, W384 | VS-27.1/.2 |
| ERP health, capacity & performance, archiving, data migration | W595, W787, W376, W396, W385 | VS-27.1/.2 |
| Network/WAN/ISP/Wi-Fi, SD-WAN failover, SLA credits | W366, W1531 | VS-27.2 |
| Cloud & database infrastructure, backup/recovery, IT-DR (design in VS-26) | W368, W382, W55, W390 | VS-27.2, VS-26 |
| API/integration lifecycle & gateway ops | W257, W733 | VS-27.1 |
| Certificates & domains | W377 | VS-27.2 |
| Vulnerability mgmt, EDR ops, patching, phishing simulation, firewall/WAF review | W367 | VS-27.3 |
| Threat intel & hunting, security incident response, PAM, zero-trust remote access | W397, W383, W375, W393 | VS-27.3 |
| User provisioning/JML, access recertification, SoD, ghost-account reconciliation | W152, W1408, W832 | VS-27.1 |
| IT policy & security awareness, DPIA lifecycle, shadow IT, NPC/DPO registration | W372, W389, W388, W434 | VS-27.3, VS-91 |
| ITGC control self-assessment (quarterly) | W387 | VS-27.1 |
| PCI-DSS compliance & QSA audit | W1205 | VS-27.3 |
| IT service continuity/BIA refresh | W390 | VS-27.1 |
| IT demand/intake, strategy & roadmap, technical training/certification | W374, W386, W394 | VS-27.1/.3 |
| ITAM: discovery/CMDB, procurement catalog, provisioning/imaging, break-fix, refresh, retirement/e-waste | W3233–W3240, W3249–W3256 | VS-99 |
| SAM: entitlement inventory, optimization, SaaS portfolio, true-ups, audit defense, open source | W3241–W3248 | VS-99 |
| FinOps & IT finance: TBM taxonomy, budgeting, showback/chargeback, cloud unit economics, rightsizing | W4097–W4120 | VS-135 |
| EA: principles, ARB, standards/ATL, exceptions, repository, app portfolio & rationalization, security architecture | W3569–W3592 | VS-113 |
| In-house built-product engineering: golden path, CI/CD, rings/canary, AppSec gates (SAST/DAST/SBOM), DORA | W5517 (+ W5515/W5516) | VS-113 |
| Data/BI: warehouse ETL ops, report dev & governance, data-quality ops, data governance council | W684, W614, W734, W1177 | VS-28 |
| Advanced analytics/model lifecycle, drift monitoring | W1178, W1399 | VS-28 |
| Master data (43 masters across foundational/financial/extended) | W252–W316 | VS-29 |
| Innovation: emerging tech PoC, RPA lifecycle, IDP, chatbots, document mgmt | W690–W691, W201, W1341, W1340, W255–W256 | VS-30 |
| AI/ML governance incl. model risk, responsible-AI controls, agentic-AI registry & kill-switch ops | W3929–W3952, W5512–W5514 | VS-128 |
| OT/ICS security incl. Purdue segmentation, OT-IDS, OT pentest/red team, IEC 62443, SBOM supply chain | W5417–W5440 | VS-190 |
| IT-facing third-party attestations (SOC 2 / ISO 27001 / PCI DSS *collection*) | W4730 | VS-161 |
| New-store IT setup & store tech dispatch (POS swap, break-fix, spare pool) | VS-37.1, W831, W265, W3237 | VS-37, VS-27, VS-99 |

## 4. Gaps Identified

### G1 — Collaboration & productivity estate (M365/email/collaboration/intranet/store telephony) — **HIGH**

The single largest end-user technology estate — **~6,911 M365/email users** (cited as a volume
figure in W370/W152/W1408) plus HQ/store telephony and the employee intranet — has **no owning
workflow anywhere in the inventory**.

- **Evidence (dedicated-header hits / defining terms):** 'Microsoft 365' **0**; 'tenant
  administration' **0**; 'digital workplace' **0**; 'email security' **0**; 'DMARC / SPF / DKIM'
  **0 real hits** (surface matches were "SPF" false positives); 'telephony' **1** (incidental —
  CS agent queue login, PA-13.1); 'VoIP' **1** (incidental — a service-request example step in
  W379); 'intranet' **8** (all incidental — an HR communications *channel* in VS-19, never an
  owned platform).
- **Why it matters:** email is the #1 attack vector (W367 runs phishing *simulations*, but nothing
  owns the gateway, DMARC/DKIM/SPF enforcement, or mailbox lifecycle); M365 is the de-facto
  identity anchor for W152 provisioning yet the tenant itself is unmanaged in the model; tenant/
  license lifecycle is only partially touched by VS-99 SAM (entitlements) — configuration,
  security baselines, collaboration governance, and telephony have no owner.
- **Proposed disposition:** 2 workflows in **PA-27.2 (Infrastructure & Platform)** —
  *"Collaboration & Productivity Platform (M365/Email/Teams) Operations & Tenant Governance"* and
  *"Enterprise Messaging & Store Telephony Services (UCC) Lifecycle"*; email-security controls
  (gateway, DMARC/DKIM/SPF) fold into the first.

### G2 — ISMS / security-compliance program (ISO 27001, policy hierarchy, security GRC) — **HIGH**

- **Evidence:** 'ISMS' **0 real hits**; 'ISO 27001' appears **only as third-party attestation**
  collected from vendors (W4730, VS-161.2) and as an audit *request* reviewed by Internal Audit
  (PA-21.1). W387 (IT Compliance CSA) tests ITGC samples quarterly but owns no management system:
  no SoA, no risk-assessment cadence, no certification/attestation roadmap, no security-policy
  hierarchy lifecycle (W372 owns awareness *training*, not the policy set itself).
- **Why it matters:** the closest analogs the company will face (NPC orders, cyber-insurance
  underwriting in VS-26, enterprise B2B customers' security reviews in VS-107/VS-46) increasingly
  demand a certified or attestable ISMS. With 394 Technology & Data workflows, the *certification/management-
  system layer* is the missing capstone.
- **Proposed disposition:** 1 workflow in **PA-27.3** — *"ISMS Program, Security Certification &
  Security-Policy Lifecycle (ISO/IEC 27001)"* (risk-assessment cadence, SoA, statement of
  applicability upkeep, internal security audit program, policy hierarchy ownership).

### G3 — Enterprise IT penetration testing, red teaming & attack-surface management — **MEDIUM-HIGH**

- **Evidence:** dedicated pentest/red-team workflows exist only for **OT** (W5436) and **AI
  models** (VS-128.3 red-teaming); 'penetration test' otherwise appears as a *PCI gap-remediation
  bullet* in W1205, a mobile-app pentest step (VS-75.1), and an IA audit activity (PA-21.1).
  'bug bounty' **0**; external attack-surface management **0**.
- **Why it matters:** the enterprise estate (ERP, 50+ integrations, API gateway, ecommerce, mobile
  app, 200-store SD-WAN) has scanning (W367) but no adversarial validation cadence; W1205 itself
  flags "insufficient penetration testing frequency" as a common retail PCI gap.
- **Proposed disposition:** 1 workflow in **PA-27.3** — *"Enterprise Pentest, Red/Purple-Team &
  Attack-Surface Management Program"* (annual internal/external pentest, post-major-change
  testing, remediation tracking, PT-sponsor governance).

### G4 — Enterprise data-loss prevention & insider-risk monitoring (IT scope) — **MEDIUM**

- **Evidence:** 'DLP' / 'data exfiltration' / 'UEBA' **0 dedicated** (single false-positive hit);
  insider-threat workflows exist for **physical** security (PA-159.3) and **OT** scope (W5438)
  only. W375 (PAM) governs privileged sessions but nobody owns endpoint/email/cloud DLP policies,
  exfiltration analytics, or departure-window data-theft monitoring.
- **Proposed disposition:** 1 workflow in **PA-27.3** — *"Enterprise DLP & Insider-Risk Monitoring
  (Endpoint/Email/Cloud)"*; coordinate with VS-23/VS-159 for investigation handoff.

### G5 — Peak-season change freeze & enterprise release-calendar governance — **MEDIUM**

- **Evidence:** 'change freeze' **0** across all PA files. The estate runs three independent
  change engines — ERP monthly train (W495), built-product weekly rings (W5517), store-system
  patches (W367/W495) — coordinated only by weekly CAB (W1409) and event-level bandwidth moves
  (W366 step 6). No workflow freezes/derisks the estate for ber-months, 12.12, paydays, or
  typhoon-mode operations, and no single release calendar reconciles the three trains.
- **Proposed disposition:** 1 workflow in **PA-27.1** — *"Enterprise Release Calendar & Peak-Season
  Change-Freeze Governance"* (freeze windows, exception path via CAB, freeze-entry/exit readiness
  gates linked to VS-69/VS-26).

### G6 — Core network services & IP address management (DNS/DHCP/IPAM) — **LOW-MEDIUM**

- **Evidence:** 'IPAM' **0**; 'DHCP' **0**; 'DNS' appears only in DR failover contexts (VS-26.1/
  26.2) and legal domain-portfolio management (PA-100.2). W366 owns SD-WAN/ISP/Wi-Fi but not the
  internal core-services lifecycle (internal DNS zones, DHCP scopes, IP schema across 205+
  sites, certificate-to-service mapping).
- **Proposed disposition:** extend **W366** with explicit core-services steps, or 1 workflow in
  **PA-27.2** — *"Core Network Services & IPAM (DNS/DHCP/IP-Schema) Management"*.

## 5. Thin-Partial Coverage (monitor; no immediate new workflow required)

| Topic | State | Note |
|---|---|---|
| Enterprise SSO/IdP & MFA platform lifecycle | MFA appears as touchpoints in W375/W393/W152; 'single sign-on' 1 incidental (vendor portal, VS-48) | JML, recertification & PAM are well owned; the IdP/SSO platform itself would naturally fold into G1's M365-tenant workflow |
| Cryptographic/key management beyond payment & SSL | Payment HSM/tokenization owned in VS-80.3; SSL certs in W377; SEP gates cover secrets | Enterprise KMS/rotation for built products largely handled via golden path (W5517); revisit at next SEP review |
| Software/source-code escrow for critical third-party apps | 'software escrow' **0** | Recommend a due-diligence clause under VS-161.2 (W4730-adjacent) rather than a new workflow |
| Managed print / office output services | 'managed print' / 'print server' **0** | Receipt printing is owned under POS peripherals (W265/W1544); office print is low-criticality — watchlist only |
| Hypercare/application support transitions | Covered (6 PA files across VS-30/VS-133/VS-134/VS-163/VS-164) | No action |
| Service-desk field/second-line store support | Covered by W48 + W831 + W265 + W3237 dispatch model | No action |

## 6. Summary

| ID | Gap | Priority | Proposed home | Proposed workflows | Status (2026-09-03) |
|---|---|---|---|---|---|
| G1 | M365/collaboration/email/telephony/intranet estate | High | PA-27.2 | 2 | **Adopted — W5518, W5519** |
| G2 | ISMS & security-compliance program | High | PA-27.3 | 1 | **Adopted — W5522** |
| G3 | Enterprise pentest / red team / attack surface | Med-High | PA-27.3 | 1 | **Adopted — W5523** (Tier 3) |
| G4 | Enterprise DLP & insider-risk (IT) | Medium | PA-27.3 | 1 | **Adopted — W5524** |
| G5 | Peak-season change freeze & release calendar | Medium | PA-27.1 | 1 | **Adopted — W5521** |
| G6 | Core network services & IPAM | Low-Med | PA-27.2 (or W366 extension) | 0–1 | **Adopted — W5520** (dedicated workflow) |
| | **Total** | | | **6–7 workflows** | **7 shipped: W5518–W5524** |

**Overall verdict:** the IT workflow inventory is deep and well-partitioned — service management,
infrastructure, cyber operations, ITAM/SAM, FinOps, EA (including built-product engineering),
data/BI/MDM, AI governance and OT security are all owned at workflow granularity with explicit
boundaries (e.g., VS-99 vs. VS-27 vs. VS-35 vs. VS-34). The residual exposure concentrated in the
**end-user collaboration estate (G1)** and the **management-system / assurance layer (G2, G3,
G4)** — the capabilities that sit *above* operations (certify, attest, adversarially validate,
govern the change calendar) rather than *within* them. Filling the six gaps added **7 workflows
(W5518–W5524, ~2% growth to the IT family)** and closed every unowned capability surfaced by this
analysis. VS-27 now stands at **71 workflows** (PA-27.1: 30 · PA-27.2: 24 · PA-27.3: 17).

---

*Methodology note: candidate gaps surviving keyword validation follow §2 step 4 of
[workflow-gap-analysis.md](workflow-gap-analysis.md). The adoption was recorded there as batch 8
(workflow-ID allocation W5518–W5524), with criticality tiers confirmed (5 × Tier 2, 2 × Tier 3)
in [workflow-criticality-classification.md](workflow-criticality-classification.md).*
