# IT & Information Security Policies (POL-I)

> Domain manual of the [Corporate Policy Manual](README.md). Approval class:
> **CIO** (company-facing conduct policies — POL-I01, POL-I07 — co-approved by
> CEO). IT operates under the product-centric operating model
> ([it-product-operating-model](../../07-methodology/it-product-operating-model.md));
> security workflows live in VS-27 (IT operations & security) and VS-113
> (enterprise architecture). Estate canon: Oracle EBS 12.2 core + in-house
> platforms + M365 identity plane with the EBS ADOP online-patching boundary.

---

## POL-I01 — Acceptable Use of IT Resources

| | |
|---|---|
| Owner (R) / Approver | CIO / **CIO + CEO** |
| Cadence | 2-year review; acknowledgment at hire + annually |
| Anchors | VS-27; M365/EBS audit-log monitoring (W5518) |
| Version | 1.0 — initial issue, 2026-09-25 codification |

**Policy statements.**
1. Company accounts, devices, networks and systems are for business use;
   incidental personal use is tolerated only where lawful, non-commercial and
   non-disruptive — never for: harassment or discriminatory content, illegal
   material, gambling, crypto-mining, personal business, or political
   campaigning (POL-G06).
2. Credentials are personal and non-transferable: no sharing, no lending, no
   writing down in reachable places; reporting of compromise is same-day
   (POL-I05).
3. Software: only IT-managed or approved installs; unlicensed software is
   prohibited (licensing compliance is a board-audited exposure); browser
   extensions on POS/store systems are prohibited outright.
4. Data handling on the endpoint follows POL-D02 classification; company data
   never lands on personal storage, personal email or unapproved AI tools
   (POL-I07).
5. Monitoring: the company logs and reviews usage on company systems consistent
   with law and the privacy notice; employees are informed at onboarding
   (W1735 consent items — CCTV, monitoring).

---

## POL-I02 — Access Control & Joiner–Mover–Leaver

| | |
|---|---|
| Owner (R) / Approver | Identity & Access Platform (IAP) / **CIO** |
| Cadence | 1-year review (role catalogs + SoD rules) |
| Anchors | W132 (branch/access provisioning), W5518, EBS roles/responsibilities, W43 exit cascade |
| Version | 1.0 — initial issue, 2026-09-25 codification |

**Policy statements.**
1. Access = approved role + least privilege: entitlements provision only from
   the role catalog mapped to the DOA (POL-G05) and SoD rules; standing
   personal high-privilege accounts are prohibited — privileged access is
   time-boxed, approved and session-logged.
2. **JML discipline:** joiner access on HR-triggered workflow only (no manual
   side doors); mover access re-derived (no accumulation across roles); leaver
   access cuts **same day** on the W43 trigger with the signatory/DOA cascade
   (W30, W1732).
3. SoD: maker ≠ checker in finance master data and payments; vendor-master
   change rights sit apart from PO and payment rights (the VS-29 audit-trail
   dependency); conflicts documented or remediated.
4. Recertification: managers re-approve their teams' access quarterly;
   privileged accounts monthly; dormant accounts (90 days) disable
   automatically; the signatory-staleness rule (> 12 months) from W30 applies
   to bank portals.
5. Third parties: vendor/partner access is individual, time-boxed, sponsor-
   owned and reviewed — shared vendor logins are prohibited (fraud-control
   canon).

---

## POL-I03 — Authentication, Encryption, Mobile & BYOD

| | |
|---|---|
| Owner (R) / Approver | Security Engineering (SEC) / **CIO** |
| Cadence | 1-year review |
| Anchors | M365 identity plane, EBS authentication, mobile-app estate (mobile-app-strategy), VS-10 ecommerce, the OT/ICS estate ([VS-190](../workflows/VS-190-operational-technology-ot-ics-cybersecurity-and-retail-technology-asset-protection/), PA-190.1–190.3) |
| Version | 1.0 — initial issue, 2026-09-25 codification |

**Policy statements.**
1. MFA is mandatory for: all remote access, all administrative/privileged
   access, email, and finance/payment systems; passwords follow the managed
   policy (length-first, breached-password screening, no reuse); service
   accounts use vaulted secrets with rotation.
2. **Encryption:** data in transit encrypted on all external and store↔DC↔HQ
   links; data at rest encrypted for sensitive classes (customer PII, payment
   data, HR data, credentials); payment-card data follows the PCI-DSS scope
   rules — store POS stays out of scope by design (tokenized/segregated).
3. **Mobile & BYOD:** company data on mobile devices flows only through the
   managed app estate (MDM-enrolled); BYOD access is web/Container-only —
   no local company data on unmanaged devices; jailbroken/rooted devices are
   blocked; lost-device remote-wipe is pre-authorized by the AUP (POL-I01).
4. Store-hardening: POS terminals are locked-down builds, no local admin,
   USB ports controlled; POS network segmentation from LAN/guest Wi-Fi.
5. Keys & certificates: corporate PKI/keys lifecycle-managed by SEC; no
   production keys in source code or chat/tool artifacts (SDLC hook, POL-I06).
6. **OT/ICS estate** (DC building controls, refrigeration/energy
   controllers, POS-adjacent unmanaged devices — VS-190): segmented from IT
   networks per the IT/OT architecture (PA-190.1), monitored with the same
   incident discipline (PA-190.2), and third-party OT access only through
   time-boxed, logged conduits (PA-190.3) — availability-safety tradeoffs
   in OT follow the OT standard's rules, not improvisation.

---

## POL-I04 — Change, Release & IT Resilience (incl. Backup)

| | |
|---|---|
| Owner (R) / Approver | CIO Office / **CIO** |
| Cadence | 1-year review |
| Anchors | VS-27 change workflows, EBS ADOP online-patching boundary, DR/backup runbooks, the technology-asset lifecycle ([VS-99](../workflows/VS-99-it-asset-technology-lifecycle-management/), PA-99.1–99.3) |
| Version | 1.0 — initial issue, 2026-09-25 codification |

**Policy statements.**
1. **No unauthorized change:** every production change carries an approved
   change record (risk, test evidence, rollback, comms plan); emergency changes
   retro-document within 48 hours; the EBS estate follows the ADOP
   online-patching boundary as the built-product scoping rule.
2. Segregation: developers do not move their own code to production
   (maker-checker via the release pipeline); deployments follow the paved-road
   pipeline (SEP) with gates.
3. **Backups:** the recovery catalog defines RPO/RTO per system tier; backups
   run on schedule with **restoration tests** (not just job-success checks) at
   the stated cadence; EBS cold/e-biz backups and database RMAN chain verify
   monthly; config/secret stores back up encrypted.
4. Resilience: store operations have documented degraded-mode runbooks (POS
   offline procedure) that are tested per the store-operations calendar;
   capacity/headroom reviews are quarterly for tier-1 systems (POS, WMS, EBS);
   OT/estate recovery objectives (PA-190.2) sit inside the same recovery
   catalog as IT systems — no system tier is exempt from a tested restore.
5. **Technology-asset lifecycle** (VS-99): assets register, track and
   retire through the lifecycle workflows — software license compliance is
   a standing audit surface (PA-99.2, publisher-audit readiness), and
   decommissioning includes **certified data sanitization** before disposal
   or resale (PA-99.3; media leaving custody without sanitization is a
   reportable incident, POL-D03/D04 interfaces).
6. Major releases freeze during peak trading windows (ber-month peak,
   sale events) except security-emergency patches (CISO/CIO-approved).

---

## POL-I05 — Security Incident Response

| | |
|---|---|
| Owner (R) / Approver | SEC platform / SOC on-call / **CIO** (Board notice: material incidents) |
| Cadence | 1-year review + post-incident updates |
| Anchors | W383 (host/incident core), W5518 (M365 audit), PA-26.1 (BCP linkage), DPA breach interface (POL-D03) |
| Version | 1.0 — initial issue, 2026-09-25 codification |

**Policy statements.**
1. Every suspected incident (malware, intrusion, account compromise, data
   exfiltration, POS tampering, ransomware, vendor breach notification)
   reports immediately to the SOC hotline — no employee triages alone, no
   evidence destroyed, no silent "fix-and-forget".
2. **Severity ladder** drives response: containment → eradication → recovery →
   post-incident review; forensic preservation (logs, images, memory) precedes
   cleanup for sev-1/sev-2.
3. Breach overlap: incidents involving personal data trigger POL-D03 (72-hour
   NPC assessment path) in parallel — one incident, two coordinated tracks.
4. Vendor-caused incidents invoke the third-party clauses (POL-P03): vendor
   cooperates, evidence is shared, costs per contract.
5. Post-incident reviews are blameless-to-people, ruthless-to-controls: every
   sev-1/sev-2 produces control remediations with owners and dates tracked to
   closure by the CIO Office; material incidents brief the Audit Committee.

---

## POL-I06 — Secure SDLC & Custom Application Standards

| | |
|---|---|
| Owner (R) / Approver | SEP platform / **CIO** |
| Cadence | 1-year review |
| Anchors | VS-113 (architecture/technology strategy), ai-first operating guide (agent factory, paved road) |
| Version | 1.0 — initial issue, 2026-09-25 codification |

**Policy statements.**
1. Custom/in-house applications build on the paved road (SEP): approved stacks,
   repos with branch protection, CI with automated security gates (SCA/SAST/
   secret scanning) — unscanned code does not deploy.
2. Threat modeling is mandatory for systems touching payments, PII, or store
   operations before build; data classification drives the control set
   (POL-D02).
3. Production data never seeds dev/test unmasked; masked or synthetic data
   only (privacy-by-design; DPA processing limitation).
4. Change safety: feature flags and staged rollout for customer-facing estate;
   rollback plans are test-executed, not written-only.
5. AI components in products follow POL-I07 in addition to this policy;
   architecture decisions log in the technology-strategy register (VS-113) with
   the build-vs-adopt posture per the two-tier sourcing doctrine.

---

## POL-I07 — AI & Agent Use Governance

| | |
|---|---|
| Owner (R) / Approver | CIO Office / AAP platform / **CIO + CEO** |
| Cadence | 1-year review (fast-moving domain) |
| Anchors | [ai-first operating guide](../../07-methodology/ai-first-operating-guide.md) (laws, autonomy ladder, agent factory); [VS-128](../workflows/VS-128-ai-ml-governance-responsible-ai/) (AI/ML governance & responsible AI: PA-128.1 strategy & model risk, PA-128.2 fairness/explainability/privacy/safety, PA-128.3 lifecycle assurance), VS-30.2 (AI/ML & automation) |
| Version | 1.0 — initial issue, 2026-09-25 codification |

**Policy statements.**
1. **Sanctioned tools only:** company data processes only through approved AI
   platforms/agents on the enterprise knowledge plane; pasting customer PII,
   credentials, vendor pricing or unreleased financials into public/consumer AI
   tools is prohibited (AUP-hard rule).
2. **Autonomy follows the ladder:** agents operate at the autonomy tier their
   charter grants (crawl-walk-run); no agent takes irreversible actions
   (payments, master-data commits, price publishes) beyond its charter — human
   approval gates are system-enforced, not cultural.
3. **Agent lifecycle:** every agent has an owner, a charter, an evaluation
   record and a kill switch; rogue/shadow agents are decommissioned on
   discovery; agent actions are logged and attributable (who/what/why).
4. Knowledge plane writes follow the citation-or-refusal write path; agents
   never bypass the consistency engine or canon rules when writing.
5. Model/agent outputs are decision support, not authority: outputs used in
   finance, HR, pricing or legal contexts carry the same approval trails as
   manual work (POL-G05 unchanged by automation).
