# BuildRight Depot Corp. — Assumptions & Design Decisions

> This document consolidates the key assumptions and design decisions embedded across the
> model company documents. It serves as a single reference for understanding *why* certain
> parameters were chosen. Each assumption is cross-referenced to its source document.

---

## A1. Scale & Revenue Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A1.1 | All 200 stores are mature | Revenue figures assume all stores are past ramp-up | Simplifies modeling; real-world would have 10–15 stores in ramp-up at any time | Profile §9.4 |
| A1.2 | Average Transaction Value | PHP 1,800 | Benchmarked against Philippine big-box home improvement retail; calibrated to reflect a provincial store footprint | Profile §9.4 |
| A1.3 | Monthly POS transactions per store | 14,000 (~467/day) | Derived from 2.8M monthly ÷ 200 stores; consistent with high-traffic big-box retail | Profile §5 |
| A1.4 | Ecommerce penetration Year 1 | ~3% of revenue | Conservative for Philippine retail; aligns with early-stage omnichannel in the market | Profile §8.5 |
| A1.5 | Gross margin | 28–32% | Standard for regional big-box retail format in the Philippines | Profile §9.4 |
| A1.6 | EBITDA margin | 12–14% | Calibrated for higher logistics costs from a 4-DC provincial footprint | Profile §9.4 |

## A2. Organizational Assumptions
| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A2.1 | Single format (big-box only) | No Express/small format | Simplifies the model; tests one format thoroughly vs. two superficially | Profile §2 |
| A2.2 | Store staffing: 29 per store | Optimized model | Viable with a curated 35K SKU assortment and implementing recommended coverage for Stock Associates | Profile §12.1 |
| A2.3 | HQ in Davao City | Provincial HQ | Deliberately non-Manila to test provincial operations and connectivity | Profile §2 |
| A2.4 | 5 legal entities | Separate Holdings, Depot, Logistics, Digital Commerce, Property Mgmt | Tests multi-entity/intercompany capability; each entity has a distinct role | Profile §2 |
| A2.5 | Depot Inc. owns all inventory | Even though Logistics Inc. operates DCs | Simplifies inventory accounting; Logistics Inc. charges service fees, not goods transfer | Profile §2, W14 |
| A2.6 | Revenue per employee | ~PHP 9.0M/year | Driven by optimized staffing and high automation (re-derived at the 2026-09-23 (x) trade-desk disablement: ~PHP 62.3B ÷ 6,925; was ~PHP 8.99M ÷ 6,932); HQ rebalanced 315 → 357 (2026-06-20), then → 362 (2026-06-25), then promoted to the optimal structure HQ 511 (2026-09-14) and gap-filled to HQ 532 (2026-09-18) — see `optimal-table-of-organization.md` | Profile §4 |

## A3. Supply Chain & Logistics Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A3.1 | 4 DCs for 200 stores | DC-to-selling-area ratio ~8–12% | Industry norm for big-box retail; 4 DCs reduces average store-to-DC distance in archipelago | Profile §3.2 |
| A3.2 | DC4 (Clark) oversized at 25K sqm | Only 20 stores currently | Intentional: absorbs planned North/Central Luzon expansion | Profile §3.2 |
| A3.3 | 30% DSD by value | Cement, lumber, sand, gravel | Bulky items uneconomical to double-handle through DCs | Profile §7.1 |
| A3.4 | ~400–600 TEUs/month imports | ~40% of COGS from imports | Consistent with Philippine home improvement import volumes at this scale | Profile §7.1 |
| A3.5 | Inventory turns target: 6–8x | Curated 35K SKU assortment | Philippine island geography and import lead times make higher turns aspirational | Profile §12.3 |
| A3.6 | Shrinkage target: <1.5% | Aspirational for Philippine retail | Industry average ~1.5–2.5%; requires mature LP systems | Profile §12.3 |

## A4. Product & Merchandise Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A4.1 | 35,000 active SKUs | Curated assortment | Focused on faster turn; density of 2.3–4.4 SKUs/sqm | Profile §6.1 |
| A4.2 | Inventory valuation: WAC | Weighted Average Cost | Standard in Philippine retail; simpler than FIFO for big-box | Profile §6.3 |
| A4.3 | ~800–1,000 active vendors | 60% local, 40% import | Realistic mix for Philippine home improvement at this scale | Profile §6.5 |
| A4.4 | Top 20 vendors = 45% of COGS | Vendor concentration | Realistic for organized retail; drives blanket PO and rebate strategies | Profile §6.5 |

## A5. Financial Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A5.1 | PHP functional currency | PHP base; USD for imports | Philippine company; imports in USD | Profile §10.1 |
| A5.2 | VAT 12% | Standard Philippine VAT | Applied to most goods; some exempt/zero-rated customers exist | Profile §10.5 |
| A5.3 | Monthly IC settlement | All IC flows settled monthly on 5th | Simplifies cash management; may need twice-monthly for ecommerce as it grows | W14 |
| A5.4 | Loyalty deferred revenue ~1% | PFRS 15 allocation | Face value of points; actual allocation may differ based on expected redemption rate | W17 |
| A5.5 | Month-end close ≤ 5 days | Target | Achievable with automated IC elimination and bank reconciliation | Profile §15.3 |

## A6. IT & System Assumptions

| ID | Assumption | Value | Rationale | Source |
|---|---|---|---|---|
| A6.1 | POS offline ≥ 8 hours | Local cache of product/price | Philippine internet reliability; stores must sell during outages | NFR-011 |
| A6.1a | POS event-driven architecture | Near-real-time (< 30 sec) continuous event streaming | POS transactions stream continuously to ERP via message bus, not nightly batch; nightly reconciliation batch validates completeness only | POS-013, POS-034, POS-042 |
| A6.1b | POS local embedded data store | Full SKU catalog + customer cache on each terminal | Enables full offline selling with accurate pricing; continuous push from ERP with nightly full refresh | POS-043 |
| A6.1c | POS multi-origin fulfillment | Mixed-basket with items from store, DC, vendor, other stores | Single POS transaction can contain items fulfilled from multiple origins; unified financial posting | POS-044, POS-045 |
| A6.1d | POS terminal-to-terminal LAN sync | Peer sync when WAN down | Prevents overselling across terminals in same store during offline period | POS-046 |
| A6.2 | On-premises deployment — data residency under BuildRight control | Philippine facilities favored for latency; colocation permitted, no public-cloud hosting | Oracle EBS is an on-premises suite, not a cloud/SaaS ERP — running it in BuildRight-controlled facilities keeps RA 10173 data residency fully under the company's control | Technical Guidelines §2.1; `02-oracle-ebs/` §1 |
| A6.3 | Ecommerce platform | Already-built in-house platform | The custom ecommerce platform is an existing in-house asset (never rebuilt, never bought under the two-tier doctrine); integrated to the ERP core for real-time inventory and pricing sync | Profile §14.1 |
| A6.4 | Mobile app: branded native app | iOS + Android | Required for BOPIS pickup notifications, loyalty, and customer engagement; built on ERP-provided APIs or third-party | This document |
| A6.5 | 10-year data retention | BIR requirement (TRAIN/NIRC — Sec. 235, as amended by RA 10963) | Drives storage sizing (~1,230 GB uncompressed over 10 years) | Profile §15.3 |
| A6.6 | IT collaboration & delivery platform: Atlassian Cloud (SaaS subscription) — Jira Service Management (JSM), Jira Software, Confluence, Bitbucket, administered under Atlassian Guard (centralized identity: SAML SSO, enforced MFA, SCIM provisioning, organization audit logs) | Seats licensed to IT staff only (agent/creator seats); all other employees remain free JSM portal customers; vendor-managed cloud hosting | IT-staff-sized licensing avoids ~6,925-seat cost; vendor-managed SaaS removes platform administration from the small IT team; does not conflict with the A6.2 on-premises doctrine (which governs the ERP estate, not IT tooling SaaS); employee requester data in JSM and Confluence profiles are RA 10173-relevant — covered by vendor data-processing agreements and NPC registration per W434; governed as a managed SaaS subscription under W370 | W370, W434, PA-27.1 (W48/W132/W374/W378/W379/W381/W391/W616/W1409/W152/W615/W372/W495/W5521), PA-27.3 (W367), VS-21 (PA-21.1), VS-113 (W3575) |



---

## Design Decisions

| Decision | Choice Made | Alternative Considered | Why This Choice |
|---|---|---|---|
| DC network | 4 regional DCs | 3 mega-DCs | Better island coverage; lower outbound transport cost; industry-norm DC-to-selling-area ratio |
| IC model | Service-based (primary) | Goods-based between all entities | Depot Inc. owns all merchandise; simpler inventory accounting; Logistics Inc. charges service fees |
| SKU depth | 35,000 curated | 60,000+ deep | Faster turns; less floor coverage needed; viable with fewer store staff |
| Store format | Big-box only | Multi-format (Depot + Express) | Simpler model; single format tests one scenario thoroughly |
| Loyalty earn rate | 1 point per PHP 100 | Tiered earn by membership | Simpler to implement and communicate; standard in Philippine retail |
| BOPIS hold period | 5 days | 3 days or 7 days | 5 days balances customer convenience with inventory hold cost |
| Ecommerce fulfillment mode | Pickup-only BOPIS: checkout offers store pickup only; the customer selects the store; every order completes as a regular POS sale at that store (order recall, Online-Prepaid tender + balance tender, BIR receipt from POS; revenue/12% VAT via the POS chain) | Home delivery / ship-from-store / DSV as standard checkout options | One revenue-recording vehicle (POS) for all selling; no delivery-failure/3PL cost exposure; store-level sales comparability; single BIR/VAT trail; the delivery estate is retained dormant for BCP reactivation (BCP-008, VS-69) — profile §8; W11; PA-08.1 |
| Capability-configuration model | Online sales capabilities are governed by the canonical channel-capability registry (states: ENABLED / ENABLED-PHASED / DISABLED—PREPARED / DISABLED—NOT PREPARED) with a runtime feature-flag service in the already-built platform as its execution twin; prepared-not-enabled is the default posture for new capabilities; state changes ride the built-product change chain with same-change registry-row updates | Ad-hoc enable/disable per release, or hard-retiring unused capabilities' documentation | New capabilities can be fully designed ahead and enabled later at configuration cost only; the corpus never loses a prepared design; registry (documentation of record) and flags (execution of record) are kept in step by the same-change rule — channel-capability-registry.md; W1409; A6.6 guardrails 2/4 |
| Trade & Account Management capability | **DISABLED — PREPARED (2026-09-23 (x)): the company does not staff the Trade / Account Management department** — the 7-role HQ design (TO §5.3) is retained for re-enablement but not active, and with it the dedicated B2B machinery: trade credit accounts, key-account programs, the project quote desk, volume rebates, the Trade Pro program (registry §3.4, CAP-B01–B04). Trade customers are served as **retail POS customers** — they purchase at any store through the standard POS chain; every sale is a regular POS sale. Re-enablement = checklist (re-staff the 7 roles, re-open the account estate, re-base the canons) through W5580 | A permanently-staffed B2B desk, or deleting the department's design from the corpus | The store network serves trade walk-ins without the HQ overhead; the corpus never loses a prepared design (disable ≠ delete); headcount is honest — the active canon drops HQ 532 → **525**, total 6,932 → **6,925**, with the 7-role design retained in the TO register — channel-capability-registry.md §3.4; W5580; TO §5.3; profile §3.3 |
| POS terminals per store | 3 | 1–5 variable | 3 handles ~467 daily transactions across 10 operating hours with reasonable queues |
| POS sync architecture | Near-real-time event streaming | Nightly batch or periodic sync | Real-time inventory accuracy across 200 stores; prevents overselling; supports omnichannel ATP; Philippine internet reliability requires offline resilience rather than batch dependency |
| POS offline data model | Local embedded data store | Flat file cache | Full SKU catalog + customer cache enables comprehensive offline selling; not just emergency mode |
| POS fulfillment model | Multi-origin / mixed-basket | Store-only or store+DC only | Customer convenience: buy some items in-store, order others for delivery from DC or vendor from same transaction; competitive necessity for omnichannel retail |
| POS LAN architecture | Terminal-to-terminal sync | Independent terminals | 3 terminals per store can oversell each other during offline; LAN sync prevents this without requiring WAN |
| Payroll frequency | Semi-monthly (15th & 30th) | Monthly | Philippine standard; mandated by many CBAs and DOLE guidelines |
| Fiscal year | Calendar year (Jan–Dec) | April–March or other | Aligned with Philippine tax year (BIR) |
| Blanket PO coverage | ~45% of COGS | Higher or lower | Aligned with top-20 vendor concentration; remaining 55% on standard POs |
| IT service management & SDLC toolchain | Atlassian Cloud (SaaS subscription): JSM (ITSM — incidents, requests, problems, change/CAB, project intake), Jira Software (delivery/backlog tracking), Confluence (IT knowledge & controlled documents), Bitbucket (source control + Pipelines CI/CD), administered under Atlassian Guard (SAML SSO, enforced MFA, SCIM provisioning, organization audit logs); seats limited to IT staff | Atlassian Data Center (self-hosted), or a multi-vendor stack (ServiceNow + SharePoint + separate Git service) | Vendor-managed SaaS frees the small IT team from platform administration; the single-vendor spine gives end-to-end traceability (JSM intake → Jira issue → Bitbucket branch/PR → Pipelines deploy → JSM change ticket) that the CAB (W1409) and internal audit (VS-21) rely on; the A6.2 on-premises rule is scoped to the ERP estate and does not extend to IT collaboration SaaS — privacy exposure is handled via Atlassian data-processing agreements + NPC registration (W434) and SaaS governance (W370) |

### A6.6 Operating Standards — Atlassian Cloud Suite (Best-Practice Guardrails)

1. **Single IT intake** — all IT-facing work enters through JSM: incidents (W48), service requests (W379), problem records (W378), change requests (W1409), and project/demand intake (W374). Jira boards are downstream of JSM intake, never a parallel entry point (shadow-IT guard of W374). The one deliberate split intake: business-side ERP enhancement requests enter via the ERP self-service portal (W616.1) and sync to the Jira Software backlog — JSM never re-collects what EBS already captures transactionally.
2. **End-to-end traceability (built-product estate)** — every built-product production change carries the chain **JSM change ticket ↔ Jira issue ↔ Bitbucket branch/PR (issue key in the branch name) ↔ Bitbucket Pipelines deployment log**; the chain is the CAB evidence pack (W1409) and internal audit's change-testing sample frame (VS-21). EBS-estate changes ride their own chain — JSM change ticket ↔ Confluence runbook ↔ ADOP online-patching execution (the W495 monthly train, customization-governance §6) — JSM never collects what EBS already captures transactionally.
3. **Confluence is the system of record for IT knowledge** — IT KB (W381), runbooks, IT policies (W372), the EA repository (W3575), and RCA reports (W378) live in Confluence spaces with page-level permissions; no secrets/credentials in pages (W381 review gate); employees consume knowledge via the JSM portal, not direct Confluence access (seats stay IT-staff-only).
4. **Bitbucket is the only path to production for the built-product estate** — trunk-based development with short-lived branches, branch permissions on the production branches (no direct pushes — merges only through PR with the reviewer rule enforced as a merge check; two reviewers for payment/POS-facing code), and Pipelines as the sole deployment mechanism with rollback artifacts retained (W132/W495); no manual server deployments. (The EBS estate's path to production is the ADOP online-patching discipline — customization-governance §6 — not Pipelines.)
5. **Access discipline** — SSO with MFA enforced through Atlassian Guard (the suite's centralized identity plane: SAML SSO, enforced MFA policies, SCIM provisioning from the corporate directory groups, admin-role auditing), backed by the directory (W152); IT-staff group membership is the license gate; admin roles restricted to the IT platform team and reviewed with the quarterly entitlement review (W1408); API tokens are personal, scoped, and rotated.
6. **SaaS governance** — the suite is registered in the SaaS Management Platform with the Software Asset Manager as subscription owner (W370): quarterly seat-vs-usage audit, 24-hour harvest on separation (W43), annual Atlassian true-up.
7. **Data privacy** — JSM employee requester data and Confluence profiles are RA 10173-relevant: processor agreements with Atlassian verified by the DPO and the suite covered in the NPC registration (W434); **no customer PII** in Jira/Confluence/Bitbucket (retail customer data stays in the ERP/CDP); Atlassian Guard organization audit logs streamed to the SIEM (W367).
8. **Continuity** — vendor-managed backups per the Atlassian cloud shared-responsibility model, supplemented by periodic Jira/Confluence exports into the W382 backup estate; the suite rides W380 monitoring via REST-API health checks and is tiered in W55 DR planning.

> **Note**: For definitions of all abbreviations and terms used in this document, see the canonical glossary in [model-company-profile.md §18](model-company-profile.md#18-glossary).

---

*Date: 2026-09-23 (v8 — Trade & Account Management disabled — prepared: new Design-Decisions row — the company does not staff the 7-role Trade / Account Management department; B2B customers are retail POS customers; the registry §3.4 B2B estate (CAP-B01–B04) is disabled — prepared with the design retained; active headcount re-based HQ 532 → 525, total 6,932 → 6,925; A2.6 revenue-per-employee re-derived ~PHP 62.3B ÷ 6,925 ≈ PHP 9.0M; A6.6's seat-avoidance note re-based to the 6,925 active population. Companions: registry v1.2, TO v3.0, profile v3.7, W5580.)*

*Date: 2026-09-23 (v7 — capability-configuration model: new Design-Decisions row — online sales capabilities are governed by the canonical channel-capability-registry (ENABLED / ENABLED-PHASED / DISABLED—PREPARED / DISABLED—NOT PREPARED, with enable checklists) and its runtime feature-flag twin in the already-built platform; prepared-not-enabled is the default posture for new online capabilities; marketplace, social commerce, COD join the delivery estate as DISABLED—PREPARED, curbside recorded DISABLED—NOT PREPARED. No workflow, role, CTL, requirement, volume or headcount change.)*

*Date: 2026-09-23 (v6 — ecommerce pickup-only BOPIS mandate with POS-tender completion: new Design-Decisions row — checkout offers store pickup only, the customer selects the pickup store, and every order completes as a regular POS sale at that store (order recall on the terminal, Online-Prepaid tender for any prepaid amount plus balance tender, BIR receipt from POS; revenue/12% VAT via the standard POS chain); the delivery estate is retained dormant for BCP reactivation. Companions: profile §2/§8 (v3.5), PA-10.1/PA-10.2 (W11 rewrite + mandate banners), PA-08.1 banner, ECOM-003, CTL-47 scope line. No workflow, role, CTL, requirement, volume or headcount change.)*

*Date: 2026-09-23 (v5 — seventy-fifth-wave consistency review: A6.6 completed to the full Atlassian best-practice stack — **Atlassian Guard** added as the suite's centralized identity plane (SAML SSO, enforced MFA, SCIM provisioning, organization audit logs) in the A6.6 row, the Design-Decisions row and guardrails 5/7 (the enforcement vehicle guardrails 5 and 7 already assumed but never named); guardrail 2/4's universal production-change phrasing scoped to the **built-product estate** with the EBS estate's own chain named (JSM ↔ Confluence ↔ ADOP online patching, the W495 train — customization-governance §6), and Bitbucket branch permissions (no direct pushes; the reviewer rule as a merge check) pinned; the A6.6 Source cell completed to all 16 PA-27.1 workflows the v4 note enumerates (W495/W5521 joined). Companion: data-volumes §3 gains the two EBS-adjacent suite flows (W616.1 → Jira enhancement-request sync; Guard org audit logs → SIEM) with the EBS pattern register mirroring; sourcing model §8 names the suite in the vendor-commodity estate. No workflow, role, CTL, requirement, volume or headcount change.)

*Date: 2026-09-23 (v4 — A6.6 added: the IT collaboration & delivery platform standardized on the **Atlassian Cloud suite (SaaS subscription)** — Jira Service Management, Jira Software, Confluence, Bitbucket — seats licensed to IT staff only, with the SaaS-governance, access and data-privacy guardrails recorded in §A6.6, the Design Decisions table, and the workflow references trued in PA-27.1 (W48/W132/W374/W378/W379/W381/W391/W434/W495/W5521/W616/W1409/W152/W615/W370/W372), PA-27.3 (W367), VS-21 (PA-21.1) and VS-113 (W3575). v3 — storage-sizing recomputed to **~1,230 GB uncompressed over 10 years** (was ~1,000 GB), the production-calibrated data-volumes §1.2 annual increment of ~123 GB × 10; the A6.5 requirement/vehicle cells unchanged; aligns with NFR-006, profile §15.3, data-volumes §1.2, technical-guidelines §2.3. v2 (2026-06-19): A6.5 data-retention assumption updated to **10 years (BIR per TRAIN/NIRC — Sec. 235, as amended by RA 10963)** and storage-sizing recomputed to ~1,000 GB uncompressed over 10 years (was 7 years / ~700 GB); aligns with NFR-006, profile §15.3, data-volumes §1.2, technical-guidelines §2.3. v1: "unified cloud ERP" terminology standardized across all documents; counts reconciled with README.md and model-company-profile.md)*
