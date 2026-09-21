# Workflow Gap Analysis — BuildRight Depot Corp.

> Methodology and results of the operational workflow gap analysis (Pass 1, Pass 2, Pass 3, Pass 4,
> Pass 5, Pass 6, Pass 7, Pass 8, Pass 9 (all 2026-06-14), Pass 10, Pass 11, and Pass 12 (2026-06-15),
> Pass 13 and Pass 14 (2026-06-16), Pass 15, Pass 16, and Pass 17 (all 2026-06-17), Pass 18 (2026-06-18),
> Pass 19, Pass 20, Pass 21, and Pass 22 (all 2026-06-19), Pass 23, Pass 24, Pass 25, Pass 26, Pass 27, Pass 28, and Pass 29 (all 2026-06-20), and Pass 30 (2026-06-21)).
> Companion document to [value-stream-index.md](value-stream-index.md) and
> [workflow-criticality-classification.md](workflow-criticality-classification.md).

---

## 1. Purpose

Validate that the operational workflow inventory **comprehensively covers the operations of the
model company** (BuildRight Depot Corp. — a Philippine hardware/DIY/home-improvement big-box
retailer: 200 stores, 4 DCs, 35,000 active SKUs, ~800–1,000 vendors, ~PHP 62.3B annual revenue,
5 legal entities) as described in [model-company-profile.md](../model-company-profile.md), and
identify capability gaps not addressed by any existing value stream.

---

## 2. Method

1. **Inventory** the existing value streams, process areas, and workflows grouped by the
   8 operating families (Plan & Source, Make & Move, Sell & Serve, Finance, People, Asset &
   Infrastructure, Governance & Assurance, Technology & Data).
2. **Map** each major operational domain in the model company profile (merchandising, supply
   chain, store operations, POS/ecommerce, finance, HR, assets, governance/compliance, IT/data,
   legal/real-estate) to the value stream(s) that cover it.
3. **Flag gaps** where a domain had no dedicated value stream, only partial coverage, or was a
   known retired value stream (VS-49/50/51/52) not yet re-introduced.
4. **Validate** each candidate gap by keyword search across all PA files to confirm it is not
   already covered (avoiding redundant value streams) and to scope it so the new value stream is
   distinct from adjacent ones. For Pass 10, every candidate gap was confirmed to have its defining
   terms appear in zero or near-zero PA files with no dedicated owner — 'fraud orchestration' (0 PA
   files) and 'fraud management' (1) for VS-125; 'customer golden record' (0) and 'identity
   resolution' (2) for VS-126; 'integrated business planning' (0), 'IBP' (0), and 'sales and
   operations planning' (0) for VS-127; and 'model risk management' (0) and 'algorithmic
   fairness' (0) for VS-128 — each with only incidental single-step references to the broader
   capability scattered
   across multiple adjacent value streams. For Pass 11, every candidate gap was confirmed to be
   either a single workflow within another value stream ripe for elevation (W2683 Philippine
   Competition Law Compliance in VS-76.2, elevated to VS-129 following the Pass-1/Pass-5/Pass-7/
   Pass-8/Pass-10 pattern) or genuinely uncovered with zero (or only one incidental) PA-file
   references for the defining terms ('merger and acquisition'/'divestiture' for VS-130;
   'human rights'/'modern slavery' for VS-131; 'political contribution'/'election compliance'/
   'COMELEC' for VS-132). For prior passes, each candidate gap was confirmed to
   have only incidental single-workflow coverage (or none) in the existing PA files;
   for Pass 7 specifically, 'enterprise architecture' appeared in **zero** PA files, calibration was
   referenced across **50+** PA files with no dedicated owner, dangerous-goods transport was
   confirmed distinct from VS-24.3 fixed-site storage, and performance bonds/surety were confirmed
   sprinkled across VS-46/VS-11/VS-18 as single steps. For Pass 8, every candidate gap was confirmed
   to be either a single workflow within another value stream ripe for elevation (W447 DTI-BPS in
   VS-22.1; W348 Revenue Assurance in VS-21.3; W2943 ABC-Whistleblower in VS-86.3) or genuinely
   uncovered with no dedicated owner and only incidental references (RA 11285 energy-efficiency
   compliance across 14 PA files with zero dedicated headers). For Pass 9, every candidate gap was
   confirmed to be genuinely uncovered with **zero** dedicated PA-file references for the defining
   terms ('candidate experience' / 'career site' / 'talent community' for VS-121; 'global sourcing' /
   'sourcing agent' / 'overseas buying office' for VS-122; 'apprenticeship program' for VS-123;
   'clienteling' for VS-124) and only incidental single-workflow references to the broader capability
   (employer brand in 3 PA files, vocational/TESDA participation in 4, product knowledge in 33 with
   no dedicated owner), each scoped to be distinct from adjacent covered capabilities.
5. **Prioritize** gaps by operational criticality, regulatory exposure, and volume, and select the
   set to fill in each revision pass.

---

## 3. Gaps Identified

> **Status (2026-06-21): all 104 gap-analysis value streams (VS-89–VS-192; W2993–W5488) are now**
> **fully classified.** They were confirmed into the criticality register across batches
> v7.19–v7.26 (Statutory, Support & Governance, Operational Support, Mixed Operations, Shared
> Services, Sales & Transformation, Final Family-Decisive, and Pass 26–29 Confirmation) — see
> [`workflow-criticality-classification.md`](workflow-criticality-classification.md). The per-pass
> narratives below retain their original "**unclassified** … will be confirmed in a follow-up
> criticality review" / "anticipated Tier 1" wording as the *contemporaneous* record of each
> pass; that forward-looking language has since been acted on, and the authoritative current
> tier assignment lives in the classification register (not by retrofitting each pass narrative).

> **Post-Pass-30 extension (2026-06-25) — not a gap pass.** VS-127 (Sales & Operations Planning &
> Integrated Business Planning) was extended with a fourth process area, **PA-127.4 — Calamity,
> Seasonality & Philippine-Retail Demand–Supply Dynamics** (+8 workflows **W5489–W5496**). Unlike
> the thirty gap-analysis passes above (which each filled a *genuinely-unowned capability*), this
> extension specializes an already-owned value stream for BuildRight's Philippine operating
> context (typhoon/calamity demand surge, ber-months & summer seasonality, inter-island
> rebalancing, B2B/trade-project & new-store demand induction, VMI/consignment, DTI/Price-Act
> mandated price events) and closes the VS-127 "unowned-as-a-program" finding by standing up a
> dedicated S&OP/IBP sub-team in Supply Chain & Logistics (`model-company-profile.md` §3.3). It is
> recorded here only because workflow-ID allocation is tracked in this document; it is **not**
> appended to the Pass-1–30 progression tables in §4 (those are the historical, unadjusted
> thirty-pass record). Canonical totals are now **188 value streams · 569 process areas · 5,349
> workflows**.

> **Post-Pass-30 workflow-level additions (2026-08-24) — not a gap pass.** A fresh review re-ran
> the §2 gap methodology at *workflow* granularity (defining-term keyword search across all PA
> files for dedicated `## W` headers) and filled six single-workflow gaps inside existing value
> streams: **W5497** POSH / Safe Spaces compliance (RA 7877 / RA 11313 CODI committee,
> statutory investigation & reporting — VS-84.2; 'Safe Spaces'/'RA 11313'/'CODI' appeared in zero
> PA files, with only the W719 training step and W2881 generic grievance adjacent), **W5498**
> Telecommuting & flexible/hybrid work program (RA 11165 — VS-19.3; 'telecommuting'/'RA 11165' in
> zero PA files, only temporary pandemic BCP references adjacent), **W5499** Director induction &
> continuing board education (VS-36.1; 'director induction'/'board education' in zero PA files
> while W1727/W1730 bookend appointments and self-assessment), **W5500** Customer digital
> accessibility / WCAG 2.1 AA (VS-10.1; 'digital accessibility' in zero PA files and 'WCAG' only
> for the career site in VS-121.1), **W5501** Climate physical & transition risk assessment &
> scenario analysis (VS-21.2; TCFD existed only as a reporting framework, and W1330 is a generic
> single-event exercise), and **W5502** Employee financial wellness program (VS-83.3; W76 owns the
> payroll-loan mechanic and W2865 the counseling channel, but nobody owned literacy education,
> salary-linked lender governance, or the debt-stress pathway). Three candidates examined in the
> same review were confirmed already covered and deliberately not duplicated: lost & found
> (**W929**, VS-09.3 — surfaced by searching 'lost and found' but present as 'Lost & Found'),
> permit-to-work (**W3219**, VS-98.2), and counterfeit-currency handling (step-level coverage in
> W37/W185 and VS-81.2 vault counting). Like the PA-127.4 extension, these additions are recorded
> here because workflow-ID allocation is tracked in this document and are not appended to the
> §4 pass tables. Canonical totals are now **188 value streams · 569 process areas · 5,355
> workflows** (the six ship unclassified with keyword-driven proposed tiers pending a
> confirmation pass).

> **Post-Pass-30 workflow-level additions, batch 11 (2026-09-04) — operations-workflow gap fill.**
> A dedicated operations-domain gap analysis ([workflow-gap-analysis-operations.md](workflow-gap-analysis-operations.md))
> re-ran the §2 methodology across the four workflow-level families not yet covered by batches 8–10
> (Plan & Source 461, Make & Move 499, Sell & Serve 1,535, Asset & Infrastructure 321, Governance &
> Assurance 964), and filled three single-workflow gaps:
> **W5532** Workforce Time & Attendance (Biometric/Time-Clock) Platform Estate & Punch-Data Operations
> (PA-19.3; 'time and attendance'/'timekeeping'/'biometric' appeared in 38 PA files with zero dedicated
> `## W` headers — W561's own trigger names the "biometric/attendance system", W586/W796 name
> "timekeeping" as a labor-metrics data source and new-store readiness names "biometric system
> installed", but the ~420–450-device estate, its punch-data payroll interfaces and offline-outage
> fallback have no owner — the batch-9 LMS pattern), **W5533** BIR Form 2316 Annual Issuance, Employee
> Acknowledgment & Certificate Lifecycle (PA-79.2; '2316' appeared in 10 PA files with zero dedicated
> `## W` headers — generation exists only as sub-steps W90.8/W1384.7 and an ESS view bullet, with no
> owner of the January 31 furnishing campaign to ~6,762 employees, its ≥ 98% acknowledgment gate or
> its reconciliation to W2764/W2765), and **W5534** Company-Property Gate Pass & Asset-Exit Control
> (Stores, DCs & HQ) (PA-23.2; 'gate pass'/'property pass' appeared in 5 PA files with zero dedicated
> `## W` headers — W585 passes trucks at DC gates and PA-09.1 expects a "Gate Pass Integration
> (Security exit clearance)" system integration, but nobody owns the ~8,000–12,000-movement/year
> property-exit control across ~205 stores, 4 DCs and HQ).
> Workflow-ID allocation: W5532–W5534 (next available). W5533 shipped **directly confirmed Tier 1**
> (the statutory furnishing layer of the withholding regime — the W2764/W2765 sibling class and the
> W5508 statutory-filing precedent) and W5532/W5534 **directly confirmed Tier 2** (the
> platform-operations class of W5525/W3351 and the physical-security control class of W1477/W1478).
> All three are absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911).
> Candidates examined in the same review and confirmed already covered (not duplicated): DC trailer
> yard/dock discipline (W585 dock scheduling + W222 container yard + W1478 gate/visitor control; the
> operating model runs live-unload — 'yard jockey'/'drop trailer' = 0 hits), forklift & warehouse
> equipment maintenance (W650/W240/W1403/W1021), elevator/escalator servicing (PA-07.2 PM table +
> VS-138 hard-services SLA), marketing paid-media planning & buying (W83 step 12 + W676/W677/W1559),
> wage-order monitoring & pay-structure adjustment (PA-102.1's wage-order-triggered workflow),
> corporate secretarial (W2987 SEC records + W1714–W1716 board mechanics + W243 POA/board
> resolutions + W1719 retention), OSH program/committee (W512 + W436 + W4973), office print fleet
> (W241 HQ facilities scope — monitor), inter-store stock balancing (W154/W204/W218/W1423), customer
> complaints (W41/W597/W1116/W1907), sponsorship/donation intake (VS-152 program-owned), baler/cardboard
> recycling (W1564), counterfeit banknote handling (W541/W842 variance protocol), product photography
> (W4154), toll/RFID reconciliation (VS-61 scope — 2 incidental hits, monitor). Canonical totals are
> now **188 value streams · 569 process areas · 5,387 workflows** (5,410 confirmed register rows;
> Tier 1 1,383 → 1,384, Tier 2 3,266 → 3,268).
>
> **Post-Pass-30 workflow-level additions, batch 20 (2026-09-05) — cyber-extortion, payment-diversion, land-occupation & water-continuity gap fill.**
> The batch-16/17/18/19 edge-case sweeps were re-run across scenario families not yet probed (destructive
> cyber attack with extortion, disbursement-diversion fraud, vacant-land occupation, utility-service failure
> beyond power) and filled four single-workflow gaps inside existing value streams: **W5558** Ransomware &
> Destructive Cyber-Attack Enterprise Response Protocol (VS-27.3; 'ransomware'/'extortion demand'/'data-
> destruction' appear in zero dedicated headers — the class survives only as pain points and drill injects
> (PA-27.2's DR risk names the isolate-DR-before-failover trap, W1330 injects the scenario, W5529 drills the
> OT variant); W383 owns host-level incident response (5–10 investigations/month), W55 DR failover, W53 the
> RA 10173 notification, W1205 the PCI layer — nobody owned the enterprise class: the no-payment default with
> Board/counsel-gated departure, the isolate-DR-before-failover sequencing, chain-wide manual trading mode
> under the E-02 closure custody, the privileged forensics clock, the staged clean rebuild, or the cyber-
> insurance and listed-company disclosure clocks), **W5559** Vendor Payment-Diversion & Business Email
> Compromise (BEC) Fraud Event Response & Recovery Protocol (VS-18.2; BEC appears in the corpus only as this
> PA's own pain points — vendor bank-detail impersonation and executive-impersonation urgent transfers, with
> callback verification as the one-bullet mitigation — while VS-125.2's monitoring watches only the customer-
> side trade-account diversion class; nobody owned the event after prevention fails: the same-day bank-recall
> race, the honest-ledger treatment that keeps the still-owed vendor's aging truthful, the master-data
> forensics separating insider collusion from mailbox compromise, the PNP ACG and crime-policy files, or the
> cooling-off verification retrofit), **W5560** Informal-Settler Invasion & Illegal Occupation of Banked Land —
> Detection, Relocation & Ejection Protocol (VS-178.1; 'informal settler'/'squatter'/'illegal occupation'/
> 'adverse possession' appear in zero PA files — W5133 owns titled-neighbor boundary disputes, W5143 the
> agrarian tenant-compensation program, W5150 groundbreaking fencing only, and construction-site security
> lives on active build sites; nobody owned the detect–document–negotiate–eject lifecycle of parcels held
> vacant for years: the 72-hour prescription-interruption evidence discipline, the RA 7279 syndicate-vs-settler
> classification, the no-self-help eviction rule, the caretaker-fraud variant, or the RPT-continuity hygiene),
> and **W5561** Sustained Water-Service Interruption Response & Store Continuity Protocol (VS-07.2; 'water
> interruption'/'water rationing' appear only as product-selling context in PA-09.2's rainwater-harvesting
> advisory — W470 owns the power analog, W1223 generator operations, W1387 flood (excess water), W692
> consumption tracking; nobody owned the absence-of-water event: the HSE-gated restroom/sanitation decision
> law under the store's Sanitation Permit obligations, the ~200 garden centers' live-goods watering priority,
> emergency trucked-water procurement, the trading-continuity decision riding the E-02 closure custody, or the
> flush-and-confirm gate before restrooms and food services reopen after pressure loss). The same analysis
> produced the custody register's seventh wave (event-custody-and-precedence-register.md v1.7, events E-34–
> E-37: destructive cyber attack canon W5558, vendor payment diversion canon W5559, informal-settler invasion
> canon W5560, sustained water-service interruption canon W5561). Workflow-ID allocation: W5558–W5561 (next
> available). W5558 shipped **directly confirmed Tier 1** (the enterprise-trading-halt & statutory-continuity
> class of the W5545/W5546 enforcement-and-filing precedent — the data-privacy core rides the Tier-1 W53
> chain and the OT variant rides W5529) and W5559/W5560/W5561 **directly confirmed Tier 2** (the financial-
> crime contingency class of W5541/W2814, the landbanking asset-protection class of W5133/W5143, and the
> facility-continuity class of the W470 power analog). All four are absorbed within sized teams (OM stays 122
> FTE / 17 teams; TO stays HQ 511 / 6,911). Canonical totals are now **188 value streams · 569 process areas ·
> 5,414 workflows** (5,437 confirmed register rows; Tier 1 1,392 → 1,393, Tier 2 3,283 → 3,286).
>
> **Post-Pass-30 workflow-level additions, batch 21 (2026-09-05) — storefront-crash, brand-impersonation-scam,
> wallet-outage & adjacent-works gap fill.**
> The batch-16/17/18/19/20 edge-case sweeps were re-run across scenario families not yet probed (vehicle impact
> into an operating store, brand-impersonation commerce scams whose victims arrive at stores, mobile-wallet
> provider outages, adjacent construction damaging occupied property) and filled four single-workflow gaps
> inside existing value streams: **W5562** Vehicle-Impact & Storefront-Crash Response Protocol (VS-147.2;
> 'vehicle into building'/'storefront crash' appear in zero PA files — W330's in-store emergency trigger names
> structural failure generically but defers event-specific execution, W5555 owns the fatality scene protocol,
> W1450's structural assessment is quake-specific, and W653 owns our fleet crashing elsewhere; nobody owned the
> survivable-crash class: the crash-scene safety law (unstable vehicle, fuel leak, compromised glazing), the
> driver's-CTPL-first liability ordering with BuildRight's loss running as subrogation, the red-tag structural
> discipline before any zone reopens (the W5537 BFP-gate analog for impact damage), or the bollard/barrier
> retrofit feedback into the site-standards register), **W5563** Brand-Impersonation Commerce-Scam Response
> (Fake Sellers & Fraudulent Pickup Offers) (VS-100.2; 'fake seller'/'scam listing' appear in zero PA files —
> W3271/W3272 own the monitoring and takedown machinery, W5557 the recruitment variant whose victims also
> arrive at BuildRight's door, and VS-125 watches customer-side payment fraud; nobody owned the commerce-scam
> event: the victims-arrive-at-our-stores protocol, the same-day advisory with a single verification source of
> truth, the one-simultaneous-wave takedown discipline, the e-wallet recall guidance and PNP-ACG referral, or
> the data-harvesting variant that triggers the W53 breach-assessment clock), **W5564** Mobile-Wallet Platform
> Outage Response (E-Wallet Tender Downtime) (VS-08.1; one tender-outage canon per rail — W5547 owns the
> card-scheme/acquirer rail and W535 the store-connectivity layer, but the wallet-provider rail had no owner:
> the counterparty is the wallet provider, the authorization rail is QR/NFC wallet APIs, the fallback is a clean
> tender-type suspension (cards and cash keep working), the settlement catch-up runs on the provider's T+1
> payout statement, and the fraud window is phished-OTP social engineering and double-scan attempts rather than
> offline-auth abuse; nobody owned the rail-diagnosis protocol, the tender-type directive flag, the
> no-manual-receipt double-charge rule, or the stranded-authorization sweep against the provider statement),
> and **W5565** Third-Party Construction Damage & Adjacent-Works Response Protocol (VS-20.3; 'adjacent
> construction'/'neighboring construction'/'excavation damage' appear in zero dedicated headers — W650 executes
> emergency repairs with no liability discipline, W5133 owns boundary lines not damage events, W5560 owns
> occupation of banked land, and W876 processes whatever claim reaches it; nobody owned the third-party-damage
> event: the evidence-before-repair rule with the dated crack survey and engineering baseline, the red-tag
> safety gate for affected zones, the adjacent contractor's CAR/TPD-first claim ordering, the LGU
> permit-leverage track, or the monitoring regime while works continue beside an operating site). The same
> analysis produced the custody register's eighth wave (event-custody-and-precedence-register.md v1.8, events
> E-38–E-41: vehicle-impact crash canon W5562, brand-impersonation commerce-scam canon W5563, mobile-wallet
> platform-outage canon W5564, adjacent-works damage canon W5565). Workflow-ID allocation: W5562–W5565 (next
> available). W5562 shipped **directly confirmed Tier 1** (the life-safety structural-clearance class of the
> W5537/W5555 precedent — gating zone reopening on documented external assessment) and W5563/W5564/W5565
> **directly confirmed Tier 2** (the brand-integrity event class of W5557/W5550, the payment-platform
> contingency class of W5547/W5548, and the asset-protection contingency class of W5560/W5133). All four are
> absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Canonical totals are now
> **188 value streams · 569 process areas · 5,418 workflows** (5,441 confirmed register rows; Tier 1 1,393 →
> 1,394, Tier 2 3,286 → 3,289).
>
> **Post-Pass-30 workflow-level additions, batch 23 (2026-09-05) — gas-leak, tsunami/storm-surge,
> media-exposé & server-room-environmental gap fill.**
> The batch-16/17/18/19/20/21/22 edge-case sweeps were re-run across scenario families not yet probed (pre-ignition
> gas events at sites operating LPG exchange cages, coastal water intrusion by tsunami or storm surge, genuine-fault
> investigative journalism, and physical-room failures inside the IT estate) and filled four single-workflow gaps
> inside existing value streams: **W5570** Gas-Leak Event Response (LPG/Natural-Gas Odor on Premises) (VS-24.2;
> 'gas leak'/'gas odor'/'smell of gas' appear in zero PA files as event content — W5069 owns cylinder leak
> inspection/condemnation/quarantine as intake QC at the cage, W5537 owns the fire event after ignition, and W330
> names in-store emergencies generically; nobody owned the pre-ignition odor event: the odor-is-real-until-proven-
> otherwise law, the ignition-source ban with the exterior master kill, the heavier-than-air evacuate-up-and-out
> discipline, the trained-only two-person isolation boundary, or the documented detector-clear + source-disposition +
> ventilation reopen gate), **W5571** Tsunami & Storm-Surge Coastal-Intrusion Response Protocol (VS-26.1;
> 'tsunami' appears in zero PA files and 'storm surge' only as PA-09.2's customer-advisory context — W1450's quake
> protocol ends at structural assessment, W1387's flood canon is rainfall/riverine, and W1449's volcanic canon owns
> ashfall; nobody owned the coastal-intrusion class: the quake-is-the-warning law, the move-up-not-out vertical
> evacuation rule, the no-return law until PHIVOLCS cancellation, the surge-forecast-not-signal-number closure
> ladder riding the E-02 custody, or the saltwater desalination gate before re-energization), **W5572**
> Undercover-Investigation & Media-Exposé Response Protocol (Investigative-Newsroom Event) (VS-14.3;
> 'undercover'/'hidden camera'/'investigative report'/'right of reply' appear in zero PA files — W1562 owns
> recall/safety-incident media response and W3271/W3272 own the fake-brand-content class, which is the opposite
> case; nobody owned genuine-fault journalism: the verification-before-response law, the no-obstruction rule, the
> single-channel right-of-reply discipline, the self-report calculus, or the remediation track with audit-verifiable
> milestones), and **W5573** Server-Room & Data-Center Environmental Event Response (VS-27.2; 'server room'/'cooling
> failure'/'fire-suppression discharge' appear in zero PA files — W55 owns DR failover execution once a disaster is
> declared, W380 owns alert triage into incident tickets, and VS-138 owns base-building HVAC to the landlord
> boundary; nobody owned the physical-room event: the thermal-runaway clock, the power-before-water rule, the
> suppression-aftermath discipline with the certified re-arm before restart, the RTO-bounded failover decision, or
> the staged-repower validation). The same analysis produced the custody register's tenth wave
> (event-custody-and-precedence-register.md v1.10, events E-46–E-49: gas-leak event canon W5570, coastal-intrusion
> canon W5571, media-exposé canon W5572, server-room-environmental canon W5573). Workflow-ID allocation:
> W5570–W5573 (next available). W5570/W5571 ship **directly confirmed Tier 1** (the pre-ignition life-safety class
> of the W5537/W5538 precedent and the coastal-water evacuation-and-clearance class of the W1449/W5562 precedent —
> each gates a physical-state transition on documented external assessment) and W5572/W5573 **directly confirmed
> Tier 2** (the brand-integrity comms-contingency class of W5563/W5568 and the IT-facility-contingency class of
> W5547/W5564). All four are absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911).
> Canonical totals are now **188 value streams · 569 process areas · 5,426 workflows** (5,449 confirmed register
> rows; Tier 1 1,394 → 1,396, Tier 2 3,293 → 3,295).
>
> **Post-Pass-30 workflow-level additions, batch 25 (2026-09-21) — ERP customization-governance gap fill.**
> A fresh corpus-wide re-sweep of the §2 methodology against the surface no prior pass had read — the EBS blueprint layer issued
> from 2026-09-14, whose documents define recurring post-go-live processes rather than one-time implementation activity — found one
> genuine capability gap. `customization-governance.md` defines the customization decision record (CDR) and its eight-gate
> admissibility test, a hard extension budget (10 extension builds / 150 page-level personalizations / 120 custom schema objects)
> with a retire-one-to-add-one rule, the customization register audited quarterly against the databases by object-inventory diff (an
> unregistered object in the custom schema is an incident, not a finding), and a de-customization programme with five named
> retirement triggers; `integrations.md` §7 makes the CDR a ship gate for every new interface touching a custom object. Keyword
> verification: 'CEMLI' (0 PA files), 'de-customization'/'decustomization' (0), 'extension budget' (0), 'customization governance'
> (0), and 'customization' in 8 PA files with **zero** dedicated `## W` headers — every hit incidental (product/bundle
> customization, the software-capitalization gray area in W-level capex prose, an over-customization risk bullet). The adjacent
> owners were each read in full and each governs a different boundary: W5515 decides use-EBS versus build (the sourcing gate),
> W3571 reviews initiative solution architectures and W3573 their deviations and waivers, W132/W1409 deliver and approve a change,
> W495 checks custom-code compatibility inside a patch cycle, and W3578 manages application lifecycle and technical debt — nothing
> owned the gate between *configure* and *extend* inside the suite, nor the register and retirement loops that keep the extension
> estate from accreting. Three workflows added to PA-113.1: **W5575** Customization Decision Record (CDR) Intake, Admissibility Gate
> & ARB Approval; **W5576** CEMLI Register Maintenance & Quarterly Object-Inventory Audit; **W5577** Extension De-Customization,
> Retirement & Budget Reclamation — split by their differing cadences (event-driven at the ARB cycle, quarterly audit, and
> trigger-driven retirement at the QBR). Workflow-ID allocation: W5575–W5577 (next available). All three ship **directly confirmed
> Tier 2** (the W5515–W5517 architecture-governance sibling class; the ARB, change-management and patch rails they invoke are
> already in place, so nothing is go-live blocking). Absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 532 /
> 6,932). Canonical totals are now **188 value streams · 569 process areas · 5,430 workflows** (5,453 confirmed register rows;
> Tier 1 1,396 unchanged, Tier 2 3,296 → 3,299).
>
> **Post-Pass-30 workflow-level additions, batch 24 (2026-09-10) — concessionaire connectivity request,
> approval & independent-circuit governance gap fill.**
> A concessionaire operating-model review (the batch-3 concession-catalog lineage) found the connectivity-exception
> surface unowned: W177 bundles internet into the monthly 'Rent + Utilities + Commission' concessionaire invoice as a
> BuildRight-provided utility and W111 benchmarks internet as a store utility, W366 manages the store link with its
> segmented Wi-Fi, and W5520/W5418/W5421 guard the IPAM and device boundaries — but no workflow owned the case where a
> concessionaire wants its own internet connection ('concessionaire internet'/'independent circuit' appear in zero PA
> files as owned content): the default-posture rule with the segmented-Wi-Fi alternative evaluated first, the eligibility
> gate (documented regulatory, banking or capacity need only — never convenience or cost), the isolation envelope
> (separate conduit, no physical or logical crossing into BuildRight networks, DHCP confined to the concessionaire's own
> equipment, no BuildRight credentials), the W47 works approval with landlord and LGU consent for exterior terminations,
> the W117 connectivity addendum with incident demarcation and VS-147 insurance, the commission-integrity clause keeping
> every concession sale on the BuildRight POS throughput SKU, and the restoration holdback released only on the W62 exit
> walk-through. **W5574** Concessionaire Connectivity Request, Approval & Independent-Circuit Governance (VS-07.1)
> fills the surface. Workflow-ID allocation: W5574 (next available). Ships **directly confirmed Tier 2** (the
> concession-operations governance class of the W5505–W5507 siblings; the network-boundary machinery it invokes is
> already in place, so nothing is go-live blocking). Absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays
> HQ 511 / 6,911). Canonical totals are now **188 value streams · 569 process areas · 5,427 workflows** (5,450
> confirmed register rows; Tier 1 1,396 unchanged, Tier 2 3,295 → 3,296).
>
> **Post-Pass-30 workflow-level additions, batch 22 (2026-09-05) — terminal-tampering, procurement-impersonation,
> account-takeover & commute-disruption gap fill.**
> The batch-16/17/18/19/20/21 edge-case sweeps were re-run across scenario families not yet probed (payment-device
> compromise at the lane, fraudsters impersonating BuildRight as the buyer, takeover of BuildRight's own verified
> accounts, commute interruptions stranding crews at undamaged sites) and filled four single-workflow gaps inside
> existing value streams: **W5566** Payment-Terminal Tampering & Card-Skimmer Response (PIN-Pad Compromise Event)
> (VS-08.2; 'card skimmer'/'tampered terminal' appear in zero PA files — W537 owns the terminal's daily operations
> and settlement, W5547/W5564 the outage rails, W1205 the PCI compliance program and annual QSA audit, and VS-125.2
> transaction-level card-present fraud; nobody owned the device-compromise event: the freeze-in-place evidence rule
> (the overlay is forensic evidence under chain of custody, never pried off by store staff), the lane quarantine and
> chain-wide terminal-fleet sweep, the acquirer/card-brand notification duty with its 24-hour liability clock, the
> compromised-card population assessment, or the tamper-evident-seal retrofit into the W537 daily check),
> **W5567** Procurement-Impersonation & Fake-PO Goods-Diversion Response (VS-03.2; 'fake PO'/'fraudulent purchase
> order'/'supplier impersonation' appear in zero PA files — the buyer-side mirror of W5559's diverted payments and
> W5563's fake sellers: fraudsters posing as BuildRight order goods to a fraudster's address with a carrier
> BuildRight never booked, so no payment moves and no recall exists; nobody owned the void-order posture with
> same-day authenticated notice, the supplier-notification wave with portal-only verification, the receiving hold
> flags on diverted PO numbers, the W839 insider check, or the self-verifiable order-code retrofit),
> **W5568** Official-Channel Account-Takeover Response (Brand-Account Hijack) (VS-14.2; 'account hijack'/'brand
> account' appear in zero PA files — W5563 owns the fake pages that only pretend to be BuildRight, W3871
> customer-account ATO, and W5550 platform-side enforcement against us; nobody owned the takeover of BuildRight's
> own verified accounts, where a scam post inherits the platform's verification badge and defeats follower
> self-verification: the first-hour credential kill-chain and queue freeze, the platform-recovery appeal with
> corporate proof, the same-day follower advisory from unaffected channels, or the W53 privacy clock where follower
> messages were exposed), and **W5569** Mass-Commute Disruption & Transport-Strike Continuity Protocol (VS-141.2;
> 'transport strike'/'commute disruption' appear in zero PA files — W4255 responds to a single shuttle incident,
> W850/W2510 decide site closures, and the W576/W848/W1387 site-protection canons target buildings, not commutes;
> nobody owned the event where every site is open yet unstaffed: the attendance-forecast call, the critical-role
> matrix with no-penalty absence coding, the W4253-gated shuttle-surge and ride-share activation, the explicit
> service-level matrix for skeleton-crew trading, or the customer-impact decision riding the E-02 custody). The same
> analysis produced the custody register's ninth wave (event-custody-and-precedence-register.md v1.9, events
> E-42–E-45: payment-terminal tampering canon W5566, procurement-impersonation canon W5567, brand-account-hijack
> canon W5568, commute-disruption canon W5569). Workflow-ID allocation: W5566–W5569 (next available). All four ship
> **directly confirmed Tier 2** (W5566 the payment-device security class of W1205/W5547, W5567 the procurement-fraud
> contingency class of W5559/W5563, W5568 the brand-integrity channel-contingency class of W5563/W5550, and W5569
> the workforce-continuity class of W5561/W4255). All four are absorbed within sized teams (OM stays 122 FTE / 17
> teams; TO stays HQ 511 / 6,911). Canonical totals are now **188 value streams · 569 process areas · 5,422
> workflows** (5,445 confirmed register rows; Tier 1 unchanged at 1,394, Tier 2 3,289 → 3,293).
>
> **Post-Pass-30 workflow-level additions, batch 19 (2026-09-05) — in-transit-security, fatality-scene, tampering-extortion & recruitment-fraud gap fill.**
> The batch-16/17/18 edge-case sweeps were re-run across scenario families not yet probed (in-transit cargo crime,
> on-premises death events, merchandise-integrity extortion, employment-brand impersonation) and filled four
> single-workflow gaps inside existing value streams: **W5554** In-Transit Cargo Hijacking, Armed Truck Robbery &
> Driver-Safety First Response Protocol (VS-06.2; cargo theft is named only inside W1337's ORC intelligence
> background — "cargo theft targeting BuildRight deliveries in transit or at DC loading docks" — and VS-180's
> relief-convoy escort note; 'hijack'/'holdup'/'cargo robbery' appear in zero dedicated headers — W653 owns the
> accident/cargo-damage event, W2814 the CIT-vendor robbery, E-21 armed violence on premises; nobody owned the
> roadside armed-robbery event, whose first rule is the opposite of loss prevention: comply, surrender the load,
> protect the crew — with the first-hour PNP hot-pursuit escalation, the GPS/seal evidence preservation, and the
> own-fleet vs 3PL-carrier claim split), **W5555** Customer or Visitor Death on Premises — Scene Protocol, Family
> Liaison & Trading-Continuity Decision (VS-147.3; W4401 owns injuries and names fatality only as W4405's
> notification trigger — 'death on premises'/'died in store' appear in zero PA files as protocol content; nobody
> owned the potential-crime-scene nothing-moves discipline until PNP/SOCO documented clearance, the family-liaison
> sequencing that prevents social-media-first discovery, the dignity-first trading-continuity decision, or the
> witnessing-staff stand-down), **W5556** Product-Tampering Threat, Extortion Demand & Merchandise-Integrity Sweep
> Protocol (VS-89.1; VS-89 owns every found-defect trigger — W2993 intake, W2994 recall decision, W2995 regulatory
> notification, W3000 stop-sale — but 'tampering threat'/'contamination threat'/'extortion' appear in zero dedicated
> headers; nobody owned the never-pay rule, the specificity-gated sweep-or-monitor decision — the W5538 bomb-threat
> decision law transposed to merchandise — or the law-enforcement assessment that must precede any W3000 stop-sale),
> and **W5557** Recruitment Fraud & Fake Job-Offer Scam Response, Takedown & Victim-Guidance Protocol (VS-121.1;
> 'recruitment scam'/'fake job'/'job scam' appear in zero PA files — PA-100.2's W3272 digital-IP machinery watches
> impersonating sites/accounts through the customer-phishing lens and W3764 the review-site reputation; nobody owned
> the event whose victims arrive at BuildRight's own door: the same-day never-charges-fees advisory, the simultaneous
> multi-surface takedown wave, the empathy-first victim-guidance desk, and the PNP Anti-Cybercrime referral pack).
> The same analysis produced the custody register's sixth wave (event-custody-and-precedence-register.md v1.6, events
> E-30–E-33: in-transit cargo hijacking canon W5554, death on premises canon W5555, product-tampering threat canon
> W5556, recruitment fraud canon W5557). Workflow-ID allocation: W5554–W5557 (next available). W5555/W5556 shipped
> **directly confirmed Tier 1** (the life-safety scene-and-clearance class of the W5536/W5537/W5538 precedent — each
> gates a physical-state transition on documented external assessment: PNP/SOCO scene release, and the
> law-enforcement-assessed sweep/stop-sale decision) and W5554/W5557 **directly confirmed Tier 2** (the
> contingency-operations class of W653/W2814 with the crew-safety dimension riding the Tier-1 W501/W717 chains, and
> the brand-integrity channel-contingency class of the W5550/W5553 precedent). All four are absorbed within sized
> teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Canonical totals are now **188 value streams · 569
> process areas · 5,410 workflows** (5,433 confirmed register rows; Tier 1 1,390 → 1,392, Tier 2 3,281 → 3,283).
>
> **Post-Pass-30 workflow-level additions, batch 18 (2026-09-05) — channel-enforcement, employee-legal-status, OSH-enforcement & app-store-removal gap fill.**
> The batch-16/17 edge-case sweeps were re-run across scenario families not yet probed (platform-side channel
> enforcement, employee criminal-case events, OSH enforcement orders, store-distribution takedowns) and filled
> four single-workflow gaps inside existing value streams: **W5550** Marketplace Account Suspension, Enforcement
> Freeze & Appeal Recovery Protocol (VS-10.3; 'account suspension'/'account health'/'delisting' in zero PA files —
> W1470 owns the preventive seller-metrics layer, ending its escalation at "corrective action plan to avoid platform
> penalties," and W659 owns incidents on BuildRight's *own* platform; nobody owned the enforcement event itself —
> freeze-scope containment, demand re-routing to the own channel, the appeal pack with platform deadlines, the
> settlement-freeze accounting and the reinstatement gate), **W5551** Employee Arrest, Detention & Criminal-Case
> Employment-Status Response Protocol (VS-19.1; 'arrest' appears only as a VS-167 re-screening trigger and an LP
> case-closure outcome — nobody owned the employment-status mechanics: the involuntary-absence leave placement
> (detention is neither misconduct nor severance), the work-relatedness classification that fixes who pays for
> counsel and opens the employer's Arts. 2176/2180 quasi-delict exposure, family liaison with written pay
> computations, the 30/60/90-day reviews, acquittal-reinstatement, and the W2883/W2884 two-notice separation gate
> on verified facts), **W5552** DOLE Imminent-Danger Work-Stoppage Order Response, Abatement & Reinstatement Gate
> (VS-24.1; RA 11058 is cited in ~15 PA files only as the duties/penalties context of W505, and PA-24.1's own DOLE
> pain point names work-stoppage orders solely as a late-reporting consequence — 'work stoppage'/'stoppage order'/
> 'imminent danger' in zero dedicated headers; the OSH analog of the W5545 BIR closure-order class: comply-first
> abatement with evidence, the no-wage-loss rule for stoppage-affected workers, and reopening only on DOLE's written
> lifting order), and **W5553** Mobile App Store Removal, Policy-Violation Response & Re-Listing Recovery Protocol
> (VS-75.1; 'app store removal'/'policy violation'/'app takedown' in zero PA files — W2647 owns listing upkeep and
> review response, W2650 performance monitoring; nobody owned the removal event: class-specific fix paths
> (privacy-declaration, payment-rule, metadata, binary), the appeal with remediation in hand, interim-channel
> customer comms and the release-checklist prevention gate). The same analysis produced the fifth custody wave
> (event-custody-and-precedence-register.md v1.5, events E-27–E-29: marketplace account suspension canon W5550,
> DOLE work-stoppage order canon W5552, employee arrest/detention canon W5551). Workflow-ID allocation: W5550–W5553
> (next available). W5552 shipped **directly confirmed Tier 1** (the OSH statutory-enforcement class of the W5545
> closure-order precedent — a regulator-ordered halt gated on life safety with a written-lifting reopen gate) and
> W5550/W5551/W5553 **directly confirmed Tier 2** (the channel-contingency class of the W5547/W5548 precedent and
> the specialized employee-relations event class). All four are absorbed within sized teams (OM stays 122 FTE /
> 17 teams; TO stays HQ 511 / 6,911). Canonical totals are now **188 value streams · 569 process areas · 5,406
> workflows** (5,429 confirmed register rows; Tier 1 1,389 → 1,390, Tier 2 3,278 → 3,281).

> **Post-Pass-30 workflow-level additions, batch 17 (2026-09-05) — regulatory-shock, platform-outage & governance-continuity gap fill.**
> The batch-16 edge-case sweep was re-run across scenario families not yet probed (governance continuity,
> regulatory enforcement, payment-platform failure, tender-program failure, sensitive psychosocial incidents)
> and filled six single-workflow gaps inside existing value streams: **W5544** Emergency Executive Succession &
> Decision-Rights Continuity Protocol (VS-36.1; 'emergency succession'/'board continuity' appeared in zero PA
> files and 'incapacity' only as PA-36.2's records-update trigger "(d) death or incapacity" — W178 owns planned
> succession and PA-36.2 the SEC-records update, but nobody owned the first-24-hour board mechanics, the
> delegation-of-authority bridge, bank/BIR signatory continuity, or the listed-company disclosure clock),
> **W5545** BIR Tax-Enforcement Suspension & Closure-Order Response — Oplan Kandado (VS-79.3; 'Oplan Kandado'/
> 'tax suspension'/'closure order' in zero PA files — W2773 owns audit defense and W658 inspection response,
> but the enforcement closure order that halts trading at a site had no owner: the comply/protest/settle
> decision, the W850 execution linkage and the written-lifting-order reopen gate), **W5546** BIR eFPS &
> Government-Portal Outage Filing Contingency, AAB Fallback & Penalty-Relief Documentation (VS-79.3; eFPS
> downtime is cited as a pain point in four PA files — the W590-class and PA-17.3 filing workflows and PA-79.1
> — with only a one-bullet AAB mitigation and 'filing 3+ days early', and no owner of the filing-day decision
> tree, the timestamped evidence pack that makes abatement possible, or the pay-even-if-return-follows
> protection rule), **W5547** Payment-Network & Acquirer Outage Response (VS-08.1; 'card network outage'/'card
> scheme outage'/'acquirer failure' in zero PA files — W535 owns store-side offline POS and W537 the settlement
> cycle, but the network-side outage is a chain-wide tender-policy event: alternative-tender surge, offline
> floor-limit discipline, double-charge sweep on recovery), **W5548** Stored-Value & Loyalty Platform Outage,
> Downtime-Acceptance & Manual-Redemption Protocol (VS-54.2; 'gift card system outage'/'loyalty system
> failure' in zero PA files — W2150–W2157 own the lifecycle and W3699 integrity monitoring, but the
> downtime-acceptance matrix (honor-to-cap vs suspend), the manual-redemption mode with its fraud exposure,
> the earn-posting catch-up and the liability true-up had no owner), and **W5549** Suicide Attempt / Self-Harm
> Incident Response & Psychosocial-Aftermath Protocol (VS-24.1; 'suicide'/'self-harm' in zero PA files —
> W140/W1266 own the incident frameworks but not the potential-crime-scene discipline, witness care, the
> no-speculation communication rule, or the 72-hour debrief/aftermath program; the medical core rides W501).
> The same analysis produced the fourth custody wave (event-custody-and-precedence-register.md v1.4, events
> E-23–E-26: stored-value & loyalty outage, card-network/acquirer outage, regulator-ordered suspension/closure,
> and key-executive incapacitation). Workflow-ID allocation: W5544–W5549 (next available). W5545/W5546 shipped
> **directly confirmed Tier 1** (the statutory-deadline-protection class of the W2764/W2765/W5508 filing
> siblings — enforcement response and filing-failure protection) and W5544/W5547/W5548/W5549 **directly
> confirmed Tier 2** (the governance-continuity and platform-contingency classes of their PA siblings; the
> life-safety medical dimension of W5549 rides the Tier-1 W501 chain, the batch-16 W5539 precedent). All six
> are absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Canonical totals are
> now **188 value streams · 569 process areas · 5,402 workflows** (5,425 confirmed register rows; Tier 1
> 1,387 → 1,389, Tier 2 3,274 → 3,278).
>
> **Post-Pass-30 workflow-level additions, batch 16 (2026-09-05) — emergency & continuity workflow gap fill.**
> A dedicated emergency/edge-case gap analysis re-ran the §2 methodology at *scenario* granularity (rare events and
> failure modes rather than capabilities) — probing the corpus for the questions "what happens when X fails" and
> "who owns the event" across the disaster, life-safety, finance-failure and integrity-event families — and filled
> eight single-workflow gaps inside existing value streams: **W5536** Missing-Child / Code Adam In-Store Response
> Protocol (VS-07.2; 'missing child' appeared in the corpus only as cart-child-straps — PA-07.3's cart-fleet narrative
> — with zero emergency-protocol hits; the retail-standard Code Adam protocol with exit-hold, coded PA, zone sweep,
> verified reunification and a 10-minute police-escalation clock had no owner), **W5537** Fire Event Response,
> Suppression & Post-Fire BFP Clearance — Store & DC (VS-24.2; fire was owned only as prevention/testing — W806
> annual BFP certification, W1296 equipment inspection, VS-04 DC PM checks — plus W330's one classification row;
> nobody owned suppression activation, BFP coordination, structural assessment or the three-party
> BFP-clearance-to-reopen gate), **W5538** Bomb Threat Response & Search-or-Evacuation Decision Protocol (VS-24.2;
> a W330 Major-classification example and a PA-24.2 plan-template bullet only; no call-takedown checklist,
> search-vs-evacuate decision rule, PNP-EOD handoff or radio-RF discipline), **W5539** Elevator & Escalator Entrapment
> Response Protocol (VS-07.2; 25 files mention elevators — all maintenance/accessibility; the 'entrapment' hits were
> law-enforcement ops; nobody owned passenger contact, the medical-vulnerability triage, the licensed-technician-only
> release rule or the 2-in-12-months modernization trigger), **W5540** Payroll Run Failure, Correction & Emergency
> Off-Cycle Payment (VS-19.2; W10 owns the run and W641 planned off-cycle payments; 'payroll failure' = 0 hits;
> nobody owned the abort/reject classification clock, bank-file reject regeneration, the < 24 h emergency-net-pay
> decision or statutory-remittance protection when the register is broken), **W5541** Bank-Failure & Frozen-Deposit
> Contingency (VS-18.3; W1474 owns steady-state counterparty limits and the PDIC-cap note; nobody owned the exposure
> census, the 10-day obligations-vs-stranded-cash gap, disbursement rerouting or the PDIC claim file), **W5542**
> Liquidity Stress, Covenant-Breach & Payment-Prioritization Escalation (VS-105.3; W319/W3400 own routine covenant
> monitoring and working-capital policy; 'liquidity crisis'/'cash crunch' = 0 hits; nobody owned the stress
> declaration, cash council, reversibility-ordered lever sequence, statutory-first payment tiers or the never-lapse
> covenant-engagement rule), and **W5543** Price-File Integrity Event Response & Mass-Mispricing Rollback (VS-118.2;
> W13 executes price files, W3697 monitors accuracy, W1622/W1538 refund; nobody owned the event: blast-radius
> scoping, RA 7581 SRP triage, the rollback + re-label sweep, overcharge remediation or the DTI evidence pack).
> The same analysis produced the custody register's third wave (event-custody-and-precedence-register.md v1.3,
> events E-19–E-22: structure fire, earthquake — naming W1450 as the canon the ladder had never routed — armed
> violence (W717 vs W330 during-event command), and the mispricing event). Workflow-ID allocation: W5536–W5543
> (next available). W5536/W5537/W5538 shipped **directly confirmed Tier 1** (the life-safety in-store emergency
> class of W330/W501/W576 — each gates reopening/reunification on verified external clearance: RA 7610 safeguarding,
> RA 9514 re-occupancy, PNP-EOD all-clear) and W5539–W5543 **directly confirmed Tier 2** (the contingency-operations
> and integrity-event classes of W470/W641/W319/W3697 — the statutory dimensions ride the existing Tier-1 chains
> W501/W10/W1527/W1306/W13/W427). All eight are absorbed within sized teams (OM stays 122 FTE / 17 teams; TO stays
> HQ 511 / 6,911). Canonical totals are now **188 value streams · 569 process areas · 5,396 workflows** (5,419
> confirmed register rows; Tier 1 1,384 → 1,387, Tier 2 3,269 → 3,274).
>
> **Post-Pass-30 workflow-level additions, batch 15 (2026-09-04) — capability demand-intake & backlog-triage gap fill.**
> The end-to-end stakeholder demand cycle — a BPO/executive raises a new software-capability need with their paired
> IT PO/PM → the need is logged and triaged by EA (existing coverage vs. missing workflow-level owners vs. genuinely
> new value stream vs. sourcing candidate) → routed (team backlog, workflow-catalog gap-admission, or the W5515 SIB
> sourcing gate) → funded as capacity at the Product Council — had no dedicated workflow-level owner: every stage
> existed only as governance prose in the IT operating model (OM §5.1/§7) and the sourcing model (§3), with the
> downstream sourcing machinery itself owned since batch 7 by W5515–W5517. Keyword verification: 'capability demand
> intake'/'backlog triage' appear in zero dedicated `## W` headers (the adjacent VS-113 slices are each post-intake:
> W3577 portfolio rationalization, W3580 solution architecture for approved initiatives, W3588 investment-governance
> ROI — and W5515's gate opens only for a fully triaged sourcing proposal). One workflow added inside the existing
> VS-113 — **W5535 Capability Demand Intake & Backlog Triage** (PA-113.2, the application-portfolio front door it
> feeds: triage pack with IAP integration sketch W3579, rough TCO W4100, RA 10173/BIR compliance constraints and a
> preliminary Tier proposal; routing to the W5515 gate; an accepted/routed/declined-with-reason closed loop back to
> the stakeholder via the BPO) — and confirmed **directly confirmed Tier 2** (the governance/lifecycle-operations
> class of its W5515/W5516 siblings; no statutory dimension — the front door routes and never executes statutory
> filings). Absorbed within the sized CIO Office (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911).
> Workflow-ID allocation: W5535 (next available). Canonical totals are now **188 value streams · 569 process areas ·
> 5,388 workflows** (5,411 confirmed register rows; Tier 1 unchanged at 1,384, Tier 2 3,268 → 3,269).
>
> **Post-batch-11 confirmation sweep & controls-register gap fill (2026-09-04) — not a capability gap pass.**
> A fresh corpus-wide re-sweep of the §2 methodology at workflow granularity — ~200 candidate
> capabilities drawn from reference operating-model lenses not yet exhausted after batches 8–11
> (counter-service fabrication, statutory-filing layers incl. BIR 0605/eSales/PTU/books-of-accounts,
> IT platform/endpoint/IAM/monitoring estates, contact-center & social ops, customer-journey
> services, support functions incl. canteen/mailroom/office-supplies, people programs incl.
> OJT/internship/seasonal staffing, POS-consumables & store supplies, review/reputation ops) —
> found **zero surviving capability gaps**: every validated candidate resolved to a dedicated
> `## W`-header owner (representative adjudications: key duplication W945, glass cutting W943,
> pipe threading W944, screen fabrication W946, tool-rental damage W1104 + rental-fleet VS-186,
> identity & access W152/W375/W393/W832/W1408, endpoint lifecycle W3235/W3236/W3249/W3250,
> test environments W384, backups W382, ERP monitoring W595/W787, mPOS queue-busting W206,
> price matching W61, canteen/cafeteria W4182, mailroom W4183, office supplies W1673, store
> supplies category W1668, OJT placement W3826, seasonal staffing W555, consent & cookies
> W3043/W3046/W3885, back-in-stock W930, wishlist W934, SEO/on-site search W563, marketplace
> feeds W2415/W2419, store-locator/product pages VS-10.1, BIR annual registration fee — repealed
> by CREATE (RA 11534), correctly absent; recall mock-drill/effectiveness testing W627). The
> batch-11 §5 verdict therefore extends
> corpus-wide: **no unowned capability remains at workflow granularity**.
> The same sweep did close the one genuine residual *content* gap class carried on the
> batch-26/27 worklist (batch23-deferred-candidates.txt item B residue): **8 degenerate
> unnumbered `CTL (gloss)` references across 8 workflows** (the last of the batch-27-measured
> unnumbered family) were re-mapped to their owning register controls with definition-matched
> glosses — W2146→CTL-283 (campaign regulatory compliance — DTI promo-permit review per W833;
> the old gloss's 'links to W868' was a fabricated pointer to a vendor-catalog workflow),
> W2206→CTL-178 (3PL SLA penalties applied at billing), W2246/W2247→CTL-196 (coupon & promo-code
> abuse prevention), W2250→CTL-179 (refunds/credits to original tender with exception approval),
> W2269→CTL-221 (store-closure regulatory deregistration & labor-law separation; two degenerate
> refs collapsed to one), W2397→CTL-176 (clearance events reconciled financially post-event),
> W2595→CTL-637 (technology value realization) — with the four newly-cited controls' W-ref
> lists extended in [internal-controls-matrix.md](../internal-controls-matrix.md)
> (CTL-178 + W2206, CTL-179 + W2250, CTL-283 + W2146, CTL-637 + W2595). The `CTL:` colon-form
> family measured at batch 27 was already 0. Canonical totals unchanged: **188 value streams ·
> 569 process areas · 5,387 workflows · 808 controls** (88 P / 720 D).
>
> **Post-batch-12 confirmation sweep & item-B colon-form closure (2026-09-04) — not a capability gap pass.**
> A second fresh corpus-wide re-sweep of the §2 methodology at workflow granularity — ~40 further
> candidate capabilities across lenses not yet exhausted after batch 12 (pro-customer
> estimation/takeoff services, rain checks, returns-to-vendor, customer warranty & vendor
> recovery, delivery-slot scheduling, own-loss insurance-claims intake, own-site pest control,
> water potability & treatment, sharpening, paint tint/color-matching, cut-to-size services,
> standby power, guard-services contracting, duty drawback, transfer pricing, intercompany
> allocations, gift registry, Incoterms/trade-finance documentation, FX & commodity hedging,
> cold chain, data-science platform, API management/middleware, ITSM/service desk,
> physical-security monitoring, board evaluation, subsidiary governance, tax-treaty relief,
> warranty spares, loaner tools, loyalty accrual accounting) — found **zero surviving capability
> gaps**: every candidate resolved to a dedicated `## W`-header owner (representative
> adjudications: gift registry W1039, duty drawback W2955 + PA-87.2 bonded operations,
> Incoterm & marine-insurance tracking W191, FX hedging PA-18.3 + commodity hedging VS-106,
> unfulfilled-demand/rain-check capture W5509, board evaluation & committees W1727/W1730 +
> VS-36, reinsurance treaty placement W4540, guard-force contracting inside the W5A/W5F/W37
> physical-security estate, generator & standby power W808 + PA-24.2, loyalty-liability
> accuracy CTL-32/W17.11a, middleware/API governance inside the PA-113.1 architecture
> standards + W595/W614/W733/W787 integration-monitoring estate) or dissolved under
> verification (water potability & treatment = customer-advisory content in PA-09.2 plus
> BuildRight's own wastewater/DENR compliance in PA-25.1/PA-22; cold chain = "if applicable"
> paint/chemical environmental zones in PA-04.3 plus the PA-83 clinic vaccine cold chain;
> loaner units = PA-13.1/PA-53.2 repair-accommodation steps; cut-to-size blinds & sharpening =
> not offered services in the VS-09 fabrication catalog — correctly absent; tax-treaty relief =
> a computed sub-step of the PA-18.1 dividend withholding schedule). The batch-12 corpus-wide
> verdict — no unowned capability at workflow granularity — is confirmed and extended.
>
> The same pass executed the **definition-aware adjudication of the entire residual item-B
> colon-form family** — the batch-27-classified, batch-12-remaining citations (9 fabricated +
> 62 uncertain by token-overlap scoring; 95 unique lines after de-duplication against the
> unnumbered family). Every line was hand-read against the two-sided test (gloss
> definition-matches the cited control AND the control plausibly governs the workflow's
> subject): **53 lines re-mapped/re-pointed** to the semantically correct register control with
> definition-matched glosses — the CTL-46 loyalty-fraud misdirects in the OT estate
> (PA-190.2/190.3) → CTL-151 OT/ICS posture + the files' own CTL-801/CTL-802; CTL-06
> vendor-onboarding guard → CTL-41 LGU-permit compliance for the PA-76.1 permit workflows and
> → CTL-50 master-data change control for vendor-master status/assessment updates; the CTL-44
> duplicate-*vendor*-payment paste family re-pointed by subject — CTL-185 B2B billing
> integrity (W2443), CTL-212 trade-credit exposure (W2490/W2701), CTL-213 chargeback integrity
> (W2575), CTL-21 inventory accuracy (W2383); the CTL-26 fixed-asset-disposal paste family
> re-pointed by subject — CTL-104 equipment-rental safety & recovery
> (W5323/W5327/W5330/W5334/W5337/W5338/W5341), CTL-198 sample/display-asset accountability
> (W2179/W2240/W2341/W2349), CTL-219 fixed-asset register (W5324/W2672/W2674), CTL-178 fleet
> maintenance (W2324), CTL-176 clearance disposition (W2270), CTL-227 ESG evidence (W2474),
> CTL-171/CTL-100 take-back & cylinder controls (W5349/W5353/W5359); privacy misdirects →
> CTL-153 (W2121/W2192/W2481/W2491/W5262); competition-law gloss → CTL-159 (W2683); BSP/SEC
> truth-in-lending → CTL-208 (W5400); factoring-fee accuracy → CTL-120 (W5409); proof-of-loss
> tax → CTL-34 (W5276/W5383); board-governance receipts → CTL-349 (W2597/W2284); site access →
> CTL-311 (W5273); collections fraud → CTL-109 (W5386); return-fraud → CTL-179
> (W5353/W2308/W2335/W2336); incentive gaming → CTL-46 (W5350); cylinder assets → CTL-100
> (W5359); recovery revenue → CTL-114 (W5362); pick/fulfillment fraud → CTL-197
> (W2300/W2290/W2286); damage claims → CTL-75 (W2201); TPRM tiering → CTL-167 (W2190);
> margin-floor guard → CTL-108 (W2215/W2218/W2224/W2225); DTI-permit pointers corrected
> W868 → W833 and re-mapped → CTL-283 (W2223/W2238); vendor-cost accuracy → CTL-115 (W2232);
> multi-account abuse → CTL-196 (W2252); tax settlement/filing → CTL-214 (W2275/W2594);
> TP arm's-length → CTL-18 (W2584/W2592); entity profitability → CTL-213 (W2596); mobile-app
> privacy → CTL-203 (W2652); 3PL payment-terms accuracy → own CTL-399 (W2212, already listed);
> stored-value expiry → CTL-211 (W2148, already listed); drop-ship revenue-recognition →
> CTL-114 with the line's primary citation folded to the own CTL-409 (W2289) — and **18 lines
> confirmed as legitimate deliberate cross-references** and left unchanged (e.g., CTL-02 capex
> Board-tier in W5281 — "capex" vs "capital expenditure" is a token-mismatch false positive;
> the CTL-51 master-data-currency family in W2174/W2184/W2186/W2281/W2339; CTL-39 rebate/co-op
> terms in W2382; CTL-37 warranty validation in W5247; CTL-22 VAT in W5238; CTL-13 payroll/time
> SoD in W5257; CTL-26 disposals in W5277/W5296; CTL-20 cash accountability in W5292; CTL-24
> receiving fraud in W5294; CTL-41 LGU/agency renewals in W5256; CTL-06 vendor-master blocking
> in W2466; CTL-05 credit re-check in W5333; CTL-349 board resolution in W2264). The **last 24
> mid-line unnumbered `CTL (gloss)` degenerate forms** — a family the batch-12 sweep (which
> measured the unnumbered-bullet surface) reported closed at 8 — were folded to numbered
> register controls or honest prose (the two RA 7394 consumer-act fragments re-written as
> compliance prose; a further W868 DTI-pointer straggler in PA-64.1 prose repaired).
> [internal-controls-matrix.md](../internal-controls-matrix.md) W-ref lists were extended for
> the 37 newly-cited controls. The corpus-wide `CTL (`-without-number sweep now returns **0 at
> any line position**, and the DTI-context 'links to W868' family is 0 (remaining W868 links
> are vendor-catalog-appropriate). Token-overlap scoring now reports 170 isolated colon-form
> citations — every one a hand-adjudicated verbatim-objective restatement or
> definition-matched paraphrase (the residual low scores are token-mismatch false positives
> such as 'capex'/'anti-competitive'). Canonical totals unchanged: **188 value streams · 569
> process areas · 5,387 workflows · 808 controls** (88 P / 720 D); the workflow-dependency-map
> §8.1 anchor table refreshed (VS-91 979 → 980, membership unchanged, v4.20 footer).
>
> **Post-Pass-30 workflow-level additions, batch 10 (2026-09-03) — finance-workflow gap fill.**
> A dedicated Finance-domain gap analysis ([workflow-gap-analysis-finance.md](workflow-gap-analysis-finance.md))
> re-ran the §2 methodology across the Finance family (775 workflows) plus treasury/tax/property-adjacent
> streams, and filled three single-workflow gaps:
> **W5529** Utility, Telecommunications & Site Deposits Paid — Register, Interest Reconciliation,
> Surety Replacement & Recovery-on-Closure (PA-42.3; 'utility deposit' appeared in 2 PA files with
> zero dedicated `## W` headers — PA-42.3's own W1877 pain point carries the **PHP 10M–40M
> locked-capital** canon for ~205 locations with no downstream owner, recovery exists only as a
> closure sub-step in PA-20.3 and a connection-transaction step in W1877, while the landlord-deposit
> sibling W1867 shows the fully-owned pattern), **W5530** Minimum Corporate Income Tax (MCIT)
> Computation, Regime Evaluation & 3-Year Excess-Credit Carry-Forward (PA-17.3; 'MCIT'/'minimum
> corporate income' appeared in **zero** PA files corpus-wide — W407 computes normal tax and
> deferred tax (PAS 12) but the 2% gross-income floor of NIRC §27(E)/§28(A)(e), its regime
> evaluation and the 3-year excess-credit carry-forward are absent), and **W5531** PFRS 8
> Operating-Segment Reporting, CODM Disclosure Package & Segment-Note Production (PA-17.4;
> 'segment reporting'/'operating segment' appeared in **zero** PA files corpus-wide — the CODM
> review packages exist in W1653/W231/W102/W1657 and the AFS filing machinery in W9B/W481, but the
> segment-note production binding them for the audited statements is unowned).
> Workflow-ID allocation: W5529–W5531 (next available). W5530 and W5531 shipped **directly
> confirmed Tier 1** (the statutory-execution class of their Record-to-Report siblings W407/W481
> and the W5508 statutory-filing precedent) and W5529 **directly confirmed Tier 2** (the
> treasury-asset-lifecycle class of W1867/W317). All three are absorbed within sized teams
> (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Candidates examined in the same review
> and confirmed already covered (not duplicated): bank-relationship & fee governance (W317 owns
> the annual relationship review and monthly fee review; W320 step 9 + W1468 step 6 are
> supplementary), electricity supply/retail-competition sourcing (PA-120.1 step 1 owns the RCOA
> contestable-account program), insurance broking (W59 step 3), BIR audit defense (W77), deposits
> received from customers (W94/W4630) and from landlords (W1867), RTP/pallet deposits (PA-04.3),
> collection agencies (W108 steps 6–7), payroll accounting (W816/W1416), financial-statement
> preparation (W9/W9B + W481), prior-period restatement (W712), ECL provisioning (W81 + W5412),
> corporate cards (W713/W1685), promotion-effectiveness analytics (W2254–W2258), electricity
> tariff structures (W4775/W163.1 steps). Canonical totals are now **188 value streams · 569
> process areas · 5,384 workflows** (5,407 confirmed register rows; Tier 1 1,381 → 1,383,
> Tier 2 3,265 → 3,266).
>
> **Post-Pass-30 workflow-level additions, batch 9 (2026-09-03) — people-capability & reporting-policy gap fill.**
> A dedicated People/organization-domain gap analysis ([workflow-gap-analysis-people.md](workflow-gap-analysis-people.md))
> re-ran the §2 methodology across the People family (437 workflows) plus people-scoped and
> finance-policy adjacent streams, and filled four single-workflow gaps:
> **W5525** Learning Platform (LMS) Administration, Integration & Learning-Records Operations
> (PA-19.4; 'LMS' appeared in 58 PA files / 101 hits with zero dedicated `## W` headers — even a
> 'LMS Administrator' role was named in W1484's staffing note with no owning workflow — while
> W3351 HRIS and W3782 ATS own the adjacent HR platforms), **W5526** Learning-Content
> Development, Course-Catalog & Certification-Program Lifecycle (PA-19.4; 'instructional
> design'/'course catalog' in zero PA files — W51 step 2 develops materials as a sub-duty of the
> calendar owner and W1484 owns only the onboarding curriculum slice), **W5527** Leadership
> Development & Management-Capability Program (HiPo Development) (PA-19.4; 'leadership
> development' existed only as one W51 calendar line-item while W178 identifies HiPos and nothing
> develops them), and **W5528** Accounting Policy, Technical Accounting (PFRS) Position &
> New-Standard Adoption Governance (PA-17.4; PFRS appears in 93 PA files but every dedicated
> owner is transaction-specific — VS-157 PFRS 15, VS-148 PFRS 16, W407 PAS 12, W1875 lease
> policy — leaving the policy manual, position papers and new-standard adoption layer unowned).
> Workflow-ID allocation: W5525–W5528 (next available). All four shipped **directly confirmed
> Tier 2** (the platform-operations/governance-layer/program-support class of their siblings
> W3351/W51/W9). All four are absorbed within the existing HR and corporate-accounting
> organizations (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Canonical totals are
> now **188 value streams · 569 process areas · 5,381 workflows** (5,404 confirmed register
> rows; Tier 2 3,261 → 3,265).
>
> **Post-Pass-30 workflow-level additions, batch 8 (2026-09-03) — IT operating-model gap fill.**
> A dedicated IT-domain gap analysis ([workflow-gap-analysis-it.md](workflow-gap-analysis-it.md))
> re-ran the §2 methodology across all 9 Technology & Data value streams (284 workflows) and the
> IT-facing adjacent value streams, and filled seven single-workflow gaps inside VS-27:
> **W5518** Collaboration & Productivity Platform (M365/Email/Teams) Operations & Tenant
> Governance (PA-27.2; 'Microsoft 365'/'tenant administration'/'digital workplace'/'email
> security'/'DMARC' appeared in zero PA files — the ~6,762-user M365 estate was cited only as a
> license count in W370/W152/W1408), **W5519** Enterprise Messaging & Store Telephony Services
> (UCC) Lifecycle (PA-27.2; 'telephony' 1 incidental CS-queue reference, 'VoIP' 1 incidental
> service-request example), **W5520** Core Network Services & IPAM (DNS/DHCP/IP-Schema)
> Management (PA-27.2; 'IPAM'/'DHCP' in zero PA files, DNS only in DR-failover contexts — W366
> owns WAN/ISP/Wi-Fi but not core services), **W5521** Enterprise Release Calendar &
> Peak-Season Change-Freeze Governance (PA-27.1; 'change freeze' in zero PA files — W1409 CAB,
> W495 ERP train and W5517 rings run with no cross-estate freeze), **W5522** ISMS Program,
> Security Certification & Security-Policy Lifecycle (ISO/IEC 27001) (PA-27.3; a true-word
> 'ISMS' appeared in zero PA files — ISO 27001 existed only as a *vendor* attestation in W4730
> and an IA audit request, while W387 owns only quarterly ITGC CSA sampling), **W5523**
> Enterprise Pentest, Red/Purple-Team & Attack-Surface Management Program (PA-27.3; pentest
> existed only for OT in W5436, AI models in VS-128.3, and as a PCI gap-remediation bullet in
> W1205), and **W5524** Enterprise DLP & Insider-Risk Monitoring (Endpoint/Email/Cloud)
> (PA-27.3; 'DLP' in zero dedicated headers — insider threat was owned only at physical scope
> in PA-159.3 and OT scope in W5438). Workflow-ID allocation: W5518–W5524 (next available).
> Five shipped **directly confirmed Tier 2** (W5518/W5520/W5521/W5522/W5524) and two **Tier 3**
> (W5519, W5523). All seven are absorbed within the existing IT organization (OM stays
> 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Canonical totals are now **188 value streams ·
> 569 process areas · 5,377 workflows** (5,400 confirmed register rows; Tier 2 3,256 → 3,261,
> Tier 3 756 → 758).
>
> **Post-Pass-30 workflow-level additions, batch 7 (2026-09-03) — not a gap pass.** The
> sourcing-model gap-fill review re-ran the §2 gap methodology at *workflow* granularity
> against the rest of the 2026-09-03 hybrid capability-sourcing extension
> (capability-sourcing-and-engineering-model.md §3–§9 — the surface batch 6's §12 scope
> deliberately left unexamined) and found three program surfaces unowned at workflow level:
> 'sourcing gate', 'golden path', 'paved road', 'ring deployment', 'upgrade currency',
> 'exit reserve', 'release intake', 'DORA', 'best-of-breed', and 'configure' each appeared
> in zero dedicated `## W` headers, while the adjacent VS-113 slices are each
> strategy/portfolio-generic (W3588 owns investment-governance ROI, W3589 vendor/platform
> strategy direction, W3577 portfolio rationalization, W3573 architecture exceptions). Three
> workflows fill the gap inside VS-113 — one per PA, hosted where the theme lives: **W5515**
> Sourcing Decision Gate Operation & Capability Sourcing Register (PA-113.3 — the scored
> configure → buy → build assessment, the five mandatory §3.3 appendices incl. the
> 808-control mapping, SIB/Product-Council/CEO decision-rights routing, the Register record
> with annual QBR reaffirmation and re-evaluation triggers), **W5516** Best-of-Breed Product
> Lifecycle Management, Vendor Release Intake & Exit Reserves (PA-113.2 — staging-ring
> release intake with the Tier-1-mandatory regression pack, the defer-one-never-two
> upgrade-currency KPI with Tier & Control Board escalation, RA 10173/statutory-warranty/
> export/price-cap clause verification, tier-1 TPRM reassessment, QBR exit-reserve accrual),
> and **W5517** SEP Paved Road & Engineering Standard Governance for Built Products
> (PA-113.1 — golden-path starts with ARB-recorded exceptions, trunk-based/feature-flag
> delivery, contract-first IAP + data contracts, ring deployment with SLO-burn rollback and
> the AppSec block right, production readiness review, DORA-at-QBR reporting). All three
> shipped **directly confirmed Tier 2** — the governance/lifecycle-operations class of their
> VS-113 siblings (W3588/W3589), with the contract-clause dimension carried inside W5516's
> Step-3 verification gate (matching the W5513/W5511 precedent) — and were admitted to the
> semantic-audit registry via the documented transition path (full read + D1–D4 detector
> sweep over the VS-113 PA blocks, 0 flags). All three are absorbed within sized teams
> (OM stays 122 FTE / 17 teams; TO stays HQ 511 / 6,911). Workflow-ID allocation: W5515–
> W5517 (next available). Canonical totals are now **188 value streams · 569 process areas · 5,370 workflows**
> (5,393 confirmed register rows; Tier 2 3,253 → 3,256).
>
> **Post-Pass-30 workflow-level additions, batch 6 (2026-09-03) — not a gap pass.** The
> agentic gap-fill review re-ran the §2 gap methodology at *workflow* granularity against the
> 2026-09-03 Agentic-AI extension (capability-sourcing-and-engineering-model.md §12; OM v2.1
> AAP platform team #15) and found the agent lifecycle unowned at workflow level: 'agentic',
> 'agent runtime', 'shadow mode', 'canary', 'kill-switch', and 'non-human identity' each
> appeared in zero dedicated `## W` headers, while the adjacent VS-128 slices are each
> model-generic (W3931 owns the model registry, W3946 model pre-deployment assurance, W3947
> model monitoring, W3948 model retirement). Three workflows fill the gap inside PA-128.3,
> owning the sourcing-model §12 lifecycle end-to-end: **W5512** Agentic Candidate Intake,
> Sourcing Routing & Agent Registry Registration (quarterly hours × frequency × error ×
> feasibility scoring over the Automation Opportunity inventory + VS-133 process-mining
> candidates; owning-team proposal with BPO case; SIB configure → buy → build routing;
> VS-128 registry registration as the gate behind runtime-identity provisioning; ethics/DPIA
> routing per W3952/W3939), **W5513** Agent Shadow & Canary Evaluation, Graduation &
> Autonomy-Tier Ratification (offline evals → shadow beside humans → canary with tier-scaled
> sampled audit; dual-sign graduation gate; Tier-1/2/3 autonomy-ladder ratification with the
> hard boundaries verified — no statutory filing path, no POS/OT estate, no SoD conflicts —
> at SIB), and **W5514** Agent Runtime Operations, Guardrail & Kill-Switch Telemetry,
> Quarterly Re-Registration & Portfolio Sunset (IAP-contract-only tool access under non-human
> least-privilege identity per VS-27/W1408; drift/takeover/cost-per-task telemetry feeding the
> AAP KPI row and VS-135 TBM; quarterly kill-switch drills; quarterly registry re-registration
> with suspension of lapsed agents; QBR sunset of underperformers). All three shipped
> **directly confirmed Tier 2** — the lifecycle-operations class of their PA-128.3 siblings
> (W3945–W3948), with the hard-boundary dimension carried inside W5513's ratification gate
> (matching the W5511 precedent where the statutory check rides inside the workflow). The
> trio was admitted to the semantic-audit registry via the documented transition path (full
> read + D1–D4 detector sweep over the PA-128.3 block, 0 flags). Canonical totals are now
> **188 value streams · 569 process areas · 5,367 workflows** (5,390 confirmed register rows;
> Tier 2 3,250 → 3,253).
>
> **Post-Pass-30 workflow-level additions, batch 5 (2026-08-26) — not a gap pass.** A
> supplier-expense-model review found the two existing supplier-recovery paths each own a
> different money flow — co-op marketing funds (W513/W1799 in VS-03/VS-39) settle *pre-agreed
> campaign reimbursement*, and compliance chargebacks (W245) settle *penalties for
> non-performance* — while per-event, store-rendered services billed to the supplier's account
> (barcode/price-label printing for supplier items, promotional-collateral production, source-tag
> re-application) had no owner: 'service fee' and 'supplier billing' appeared in zero
> merchandise-supplier PA files as dedicated headers, with only the concessionaire analog W5507
> (VS-07.1) modeling the pattern. **W5510** fills the gap inside PA-15.1, transposing the W5507
> concessionaire service-fee pattern onto merchandise suppliers and settling through the W770 AP
> debit-memo mechanism: contracted per-event fee schedule with free allowances versioned on the
> trade agreement (W688) behind a vendor opt-in flag; chargeable events auto-logged at source
> (W4490/W181 print runs, W4488 barcode changes, W1796/W1798 campaign collateral, W4498
> source-tag re-application) as evidence-linked records provisional until service completion,
> with a co-op coverage flag preventing double-billing against W1799 settlement; monthly
> itemized statement in the vendor portal (W705) with a 5-business-day dispute window before
> posting; settlement as W770 debit memos (deduction type "service fee") netted at the next
> W556 payment run, with an AR invoice fallback (W8/W108) for un-nettable vendors and a
> cash-settlement route where a BIR 2307 is required; separate service-revenue/VAT treatment per
> W473; and a quarterly fee-income-vs-service-cost recovery review. Canonical totals are now
> **188 value streams · 569 process areas · 5,364 workflows** (the fourteen post-catalog workflows
> were confirmed 2026-09-02 by the post-catalog confirmation pass — full classification coverage;
> W5511 gift-card dormancy/escheat shipped confirmed 2026-09-03 in the event-custody pass).

> **Post-Pass-30 workflow-level additions, batch 4 (2026-08-26) — not a gap pass.** A fresh
> review re-ran the §2 gap methodology at *workflow* granularity (defining-term keyword search
> across all PA files for dedicated `## W` headers, candidate-by-candidate confirmation against
> adjacent owners) and filled two single-workflow gaps inside existing value streams: **W5508**
> Fringe Benefits Tax (FBT) Determination, Valuation & Quarterly BIR Form 1605 Filing (VS-79.2;
> 'fringe benefit'/'FBT'/'1605' appeared in zero PA files as dedicated headers — PA-144.1 flags
> 'BIR (fringe benefit)' as a dormitory-housing compliance obligation with no downstream owner —
> while the adjacent workflows each own a different tax species: W2764 cash-compensation
> withholding, W2766 final withholding on passive income, W3314 statutory contributions, W3316
> allowance administration, and VS-144 dormitory housing is the largest recurring benefit
> *source*; the workflow owns the NIRC §33 rank test, de-minimis and employer-convenience
> exclusions (RR 3-98 as updated by RR 5-2018), valuation rules for housing/vehicle/loan
> benefits, the 35% gross-up computation under RA 10963, monthly accrual via W9A, and the
> quarterly 1605 filing per entity via eFPS with 10-year evidence retention feeding W2773), and
> **W5509** Unfulfilled-Demand & Lost-Sales Capture, Substitution Analytics & Replenishment
> Feedback (VS-02.1; 'lost sales' appears across 37 PA files but only ever as a consequence or
> estimate — forecast pain points, vendor lead-time stockout cost math, recall shelf-gap
> costing, disruption estimation per W852/BCP-006 — and 'unfulfilled demand' in zero, while the
> adjacent slices are each transactional: W772 rain checks only advertised promos, W56/W38
> capture committed orders, W1252/W1356 sense leading indicators; the workflow owns the POS
> no-sale/floor-inquiry/quote-decline capture instrumentation, the deduplicated demand-event
> fact table, gross-vs-net quantification with substitution recovery, and the feedback loop into
> W31/W2A forecasting, W1451 assortment, W44 vendor attribution and the W1533 S&OP review).
> Ten candidates examined in the same review were confirmed already covered and deliberately
> not duplicated: annual stockholders' meeting (**W482**, VS-17.1 — missed by the initial
> keyword search because its title carries the apostrophe form 'Stockholders' Meeting', the
> same failure mode as batch 2's ampersand-blind miss), vendor drop-ship / direct-to-customer
> (**W273** endless aisle, **W1283** cement DSD, **W5182** emergency vendor-direct), store
> footfall analytics (**W1250**, VS-28.1), employee purchase discount (**W5B.12** with W93
> pricing-conflict rules and W205.2 category rules), BIR Authority-to-Print invoice/OR
> accreditation (**W485** branch registration & RDO transfer in PA-22.1, incl. ATP 5-year expiry
> tracking),
> LGU plastic-bag fees and bans (**W531** bagging & bag-fee compliance in PA-08.3 with the
> W193 reusable-bag program and VS-111.3 ordinance mapping), social live-selling (**W917**, VS-10.3), retirement pay (**W3315** program
> + **W643** final pay), and elevator/escalator maintenance (**W47** external-contractor work
> order class in PA-07.2). Like the earlier batches, these additions are recorded here because
> workflow-ID allocation is tracked in this document and are not appended to the §4 pass tables.
> Canonical totals are now **188 value streams · 569 process areas · 5,362 workflows** (the
> thirteen post-catalog workflows ship unclassified with keyword-driven proposed tiers pending
> a confirmation pass).

> **Post-Pass-30 workflow-level additions, batch 3 (2026-08-25) — not a gap pass.** A follow-up
> review re-ran the same workflow-granularity methodology against the concessionaire operating
> model and found that W177 (Vending & Concessionaire Management) — the single workflow the gap
> analysis had relied on to close the in-store concessionaire/kiosk/vending candidate ("covered by
> VS-07.1 (W177)") — modeled only agreement admin and a single throughput SKU: item-level
> concession pricing, barcodes, labels, and any concessionaire self-service had no owner
> ('concession item', 'concessionaire price' and 'concessionaire portal' appeared in zero PA files
> as dedicated headers). Three workflows fill the gap inside PA-07.1, following the VS-95
> marketplace seller-portal pattern (W3140/W3141/W3142/W3152) transposed in-store: **W5505**
> Concession Item Catalog, Barcode & Price-Label Onboarding & Governance (item-level concession
> SKUs with concessionaire-owner flags distinct from W252 merchandise and W23 consignment; GS1 or
> internal-barcode governance per W311 with collision blocking; BuildRight-printed vs
> concessionaire-printed label ownership; RA 7394 tag compliance; annual catalog reconciliation
> and exit purge), **W5506** Concessionaire Self-Service Price Change Request, Approval &
> Store-Level Propagation (portal request → automated guardrails incl. W468 price-freeze and
> undercut checks → Store Manager / Category Manager approve-reject with SLA and guardrail
> auto-approval → an unambiguous label-first cutover: label batch T-1 16:00, scan/photo-confirmed
> swap, 06:00 POS activation within 60 s, 05:30 auto-hold when the swap is unconfirmed — POS
> price can never lead the shelf tag per RA 7394; barcode-change cutover with 7-day alias ring;
> emergency rollback; 10-year audit trail feeding W177 commission settlement), and **W5507**
> Concession Service-Fee Billing & Cost Recovery (contracted per-event fee schedule — label
> printing, barcode changes, expedited/excess price changes — auto-logged as evidence-linked
> events, aggregated into the monthly W177 invoice as a Service Fees section with a 5-day portal
> dispute window, separate service-revenue/VAT treatment per W473, and quarterly recovery
> review). Canonical totals are now **188 value streams · 569 process areas · 5,360 workflows**
> (the eleven post-catalog workflows ship unclassified with keyword-driven proposed tiers pending
> a confirmation pass).

> **Post-Pass-30 workflow-level additions, batch 2 (2026-08-25) — not a gap pass.** A follow-up
> review re-ran the same workflow-granularity methodology and filled two further single-workflow
> gaps inside existing core value streams: **W5503** Restricted-Substance & Chemical-Content
> Product Compliance — lead-in-paint (DENR CCO 2013-24 under RA 6969), formaldehyde-emission
> classes and VOC limits (VS-31.3; 'restricted substance', 'lead in paint' and 'formaldehyde'
> appeared in zero PA files as dedicated headers — the content-compliance layer between SDS hazard
> communication (W698/W1465) and certification renewals (W1620/VS-117) was unowned, with only
> incidental paint-standard mentions and the W1605 goods-receipt shelf-life check adjacent), and
> **W5504** Extreme-Heat Work Interruption & Occupational Heat-Stress Management (VS-24.1; 'heat
> stress'/'heat index' appeared in zero PA files as dedicated headers while every other recurring
> PH hazard has an owned protocol — typhoon VS-69/W576, earthquake W1450, ashfall W1449, brownout
> W470, pandemic W484/W854 — leaving only a toolbox-talk topic in VS-07.2 and a hydration bullet
> in VS-19.1). One candidate examined in the same review was confirmed already covered and
> deliberately not duplicated: in-store PWD accessibility (**W497**, VS-07.2 — surfaced only after
> correcting an ampersand-blind search that had missed its title). Canonical totals are now **188
> value streams · 569 process areas · 5,357 workflows** (the eight post-catalog workflows ship
> unclassified with keyword-driven proposed tiers pending a confirmation pass).

| # | Capability gap | Why it matters for BuildRight | Existing (partial) coverage | Decision |
|---|---|---|---|---|
| 1 | **Product Recall & Safety Corrective Action** | 35K SKUs incl. electrical, paint/chemical, power tools, appliances; Consumer Act (RA 7394) + DTI-BPS + FDA recall obligations; ~3–8 recalls/yr | Only the store-level *customer-notification execution* step exists (W776 in VS-09); no end-to-end recall program | **FILLED — VS-89** |
| 2 | **Damage, Claims & Freight Recovery** | ~72K inbound receipts/yr, ~5K store replenishment orders/month, ~42.9K ecommerce orders/month; vendor/carrier/customer damage and shortage across all legs; claim notice windows are short | Retired VS-50 (placeholder) was the home; typhoon damage handled in VS-69; no systematic damage/claims program | **FILLED — VS-90** |
| 3 | **Consumer Data Privacy & Data Protection** | ~600K loyalty members, ~5,200 B2B contacts, ~515K ecommerce orders/yr, CCTV across 200 stores; Data Privacy Act (RA 10173) + NPC, 72-hour breach notification | Employee data privacy only (W647 in VS-19); consumer program (consent, DSAR, PIA/DPIA, breach) absent | **FILLED — VS-91** |
| 4 | **Kitting, Bundling & Build-to-Order Assembly** | Kit/Bundle is an explicit item type (profile §6.4); bundle pricing (§9.3); contractor combo packs, seasonal kits | Retired VS-51 (placeholder); custom *fabrication* heavily covered (VS-09 PA-09.1); build-to-stock kit/bundle operations absent | **FILLED — VS-92** |
| 5 | Workforce Management & Labor Scheduling | 200 stores × 2–3 shifts × 29 staff; DOLE labor-code compliance | **Already covered** — PA-19.3 (Workforce Management, 10 workflows) in VS-19 | No action |
| 6 | Facilities, Equipment & Maintenance Management | 600 POS terminals, paint mixers, cutting equipment, forklifts, HVAC across 205 locations | **Substantially covered** — PA-20.3 (VS-20) + PA-07.2 (VS-07, incl. W47, W579, W1025, W1403) | No action |
| 7 | Dark Store & Micro-Fulfillment | Emerging micro-fulfillment for ecommerce | Retired VS-49 (placeholder); low near-term relevance for PH big-box provincial footprint | **FILLED — VS-93** |
| 8 | Cooperative & Community Enterprise Procurement | Community/cooperative buying programs | Retired VS-52 (placeholder); lower priority than items 1–4 | **FILLED — VS-94** |
| 9 | Marketplace Operator & Third-Party Seller Management | BuildRight operating its own 3P marketplace to expand assortment | **New gap (Pass 2)** — VS-48 retail media and VS-65 marketplace presence (selling on Lazada/Shopee) did not cover BuildRight as marketplace operator | **FILLED — VS-95** |
| 10 | Equipment Leasing & Capital Equipment Finance | B2B lease/lease-to-own for expensive contractor equipment (generators, scaffolding, solar, HVAC) | **New gap (Pass 2)** — VS-12 short-term tool rental and VS-38 consumer credit did not cover B2B multi-year equipment leasing | **FILLED — VS-96** |
| 11 | **Corporate Real Estate & Property Portfolio Management** | BuildRight Property Management Inc. (one of the 5 named legal entities, profile §2) owns ~205 store/DC/office sites and leases them to BuildRight Depot Inc.; PFRS 40 investment-property accounting, landlord-side leasing & CAM, real property tax as owner, portfolio NOI/yield | **New gap (Pass 3)** — only the *lessee* side was covered (VS-20 site selection/CAM-as-tenant, VS-42 lease administration as tenant, VS-35 fixed-asset accounting); the *lessor / property-owner / investor* operating model was entirely uncovered | **FILLED — VS-97** |
| 12 | **Contingent, Contract & Outsourced Workforce Management** | ~10–20% of store/DC labor is non-employee (outsourced security guards, janitorial, promodizers, construction/agency labor); DOLE Department Order 174 labor-only-contracting compliance, worker-misclassification and co-employment risk before the NLRC | **New gap (Pass 3)** — VS-19 covers BuildRight's own employees (incl. directly-hired seasonal W555) and VS-34 covers commercial service contracts at the PO/invoice level, but no dedicated contingent-workforce *program* (DOLE D.O. 174 structuring, four-fold-test classification, contractor onboarding/access/safety, time-vs-invoice reconciliation, spend analytics) | **FILLED — VS-98** |
| 13 | **IT Asset & Technology Lifecycle Management** | 600 POS terminals + RF/handheld scanners + mobile devices + network/Wi-Fi + servers/storage + the full software/SaaS estate across 205+ locations; license true-up/audit exposure (BSA), data-privacy obligations on device disposal (RA 10173), DENR e-waste rules | **New gap (Pass 3)** — VS-35 fixed-asset *accounting* and VS-27 IT *operations/service desk* did not cover the ITAM discipline (hardware/software discovery & CMDB, SAM & license optimization, SaaS portfolio & FinOps, technology refresh, secure retirement with sanitization) | **FILLED — VS-99** |
| 14 | **Legal Operations, Litigation & IP Management** | Active legal matters and outside counsel across the 5-entity group; commercial/contract, labor (NLRC), consumer/DTI, property/lease, tax (BIR), customs (BOC), insurance/subrogation, and IP exposure; the board receives periodic litigation updates (per VS-36.1) | **New gap (Pass 3)** — VS-36 corporate governance, VS-22 compliance/regulatory, and VS-88 records/retention/legal-hold *execution* covered adjacent areas but not the *litigator work* (matter/case management, litigation lifecycle, outside counsel, IP portfolio prosecution & enforcement, settlement/loss-contingency) | **FILLED — VS-100** |
| 15 | **Merchandise Financial Planning, Open-to-Buy & Margin Management** | ~PHP 62.3B revenue, ~PHP 42–45B COGS, 28–32% gross margin, ~40% import component, 6–8x inventory-turn target; the open-to-buy, receipt-budget, markdown-margin, and inventory-investment discipline that governs whether EBITDA (12–14%) and turn targets are met | **New gap (Pass 4)** — VS-01.1 (assortment = *which* products), VS-02 (supply operations = *how much/when* operationally), VS-33.1 (corporate revenue/OPEx budget), and VS-17.4 (finance FP&A) all touched adjacent territory, but no value stream owned the *merchandise-financial* layer (seasonal merchandise plan, OTB, markdown budget, IMU/maintained-margin modeling, turn/GMROI/WOS planning, in-season reforecast, merchandise P&A) | **FILLED — VS-101** |
| 16 | **Compensation, Benefits & Total Rewards Strategy** | 6,757 employees across 5 entities/205 locations, 15–20% turnover, region-varying minimum wages, mandatory 13th-month/statutory benefits, executive-pay governance before the board; pay equity and market competitiveness directly drive attract-and-retain | **New gap (Pass 4)** — VS-19.2 (Payroll & Compensation) executes *payroll processing* only (pay runs, statutory remittance, 13th-month, final pay, garnishments); no value stream owned the *design and governance* of pay/benefits (job architecture, salary structure, market benchmarking, pay equity, benefits/HMO design, retirement, STI/LTI plans) | **FILLED — VS-102** |
| 17 | **HR Shared Services, Employee Experience & People Analytics** | 6,757 employees, ~1,200–1,600 hires and ~1,000–1,340 exits/year, 5 entities, distributed 200-store footprint; a structured HR service-center, EX program, and people-analytics function is essential to service quality, self-service adoption, compliance, and data-driven people decisions | **New gap (Pass 4)** — VS-19 owns the employee *lifecycle* (recruitment, payroll, WFM, learning, separation) and VS-84 owns labor relations, but no value stream owned the *service-delivery* layer (HR helpdesk/case management, ESS/MSS, multi-entity shared services, EX, engagement, DEI, workforce planning, people analytics, HRIS admin) | **FILLED — VS-103** |
| 18 | **Government Affairs, Public Policy & Industry Relations** | A PHP 62.3B retailer operating under Philippine national regulation (BIR tax/e-invoicing, DTI consumer, DOLE labor, BSP payments, DENR environmental, customs/tariff, data privacy) and participating in retail/supply-chain industry associations; 200 stores across regions require consistent national policy engagement and the board expects external-affairs reporting | **New gap (Pass 4)** — VS-76 covers *local* (LGU) permits/tax/relationships, VS-22 executes *permit/license operations* and government-audit response, VS-84.3 covers *labor-specific* policy advocacy/associations (W2893/W2894), VS-14.3 handles PR/crisis-comms, and VS-100 handles litigation; no value stream owned *proactive national corporate government affairs and industry relations* (stakeholder mapping, legislative/regulatory monitoring, advocacy, coalition building, association leadership, public affairs, political/regulatory risk) | **FILLED — VS-104** |
| 19 | **Supply Chain Finance & Working Capital Management** | ~PHP 37B annual procurement spend, ~800–1,000 vendors, 30–60-day standard terms; the supplier-finance / reverse-factoring / dynamic-discounting / cash-conversion-cycle discipline that releases working capital and supports vendor liquidity at PHP 62.3B-revenue scale | **New gap (Pass 5)** — VS-18 (treasury cash) contained a single program-summary workflow W324 “Supply Chain Finance & Dynamic Discounting Program”; VS-15 (P2P) processed the payable and VS-39 handled rebates, but no value stream owned the comprehensive SCF & working-capital program (multi-funder facility, vendor enrollment, dynamic-discounting platform, CCC governance) | **FILLED — VS-105** |
| 20 | **Commodity & Input-Cost Risk Management** | 35K-SKU assortment heavily weighted to commodity-intensive categories (steel/cement/lumber 14%+14%, copper 10%+12%, oil-derived paint/plastics 8%); ~40% import; a 10% commodity swing can move COGS by ~PHP 0.5–1.5B and threatens the 28–32% gross-margin target | **New gap (Pass 5)** — VS-02.3 touched supply-chain disruption risk and VS-18.3 hedged FX only; VS-101 modeled margin; “commodity hedg” appeared in only 1 PA file and no value stream owned the dedicated commodity-exposure / hedging / indexed-pricing / pass-through program | **FILLED — VS-106** |
| 21 | **Strategic Key Account & Enterprise Customer Management** | ~40% of revenue concentrated in ~5,200 B2B accounts; the top ~700 strategic accounts (developers, large enterprises, government, large contractors) materially move the P&L and warrant dedicated relationship/growth management | **New gap (Pass 5)** — VS-11 executed transactional trade/project/wholesale, VS-43 operated the trade loyalty program, VS-46 executed government bidding, and VS-13 served mass support; “key account” appeared across 16 files but no value stream owned the strategic key-account program (tiering, KAP/JBP, account teams, executive sponsorship, account profitability, CLV/churn) | **FILLED — VS-107** |
| 22 | **On-Site Renewable Energy & Prosumer Asset Operations** | ~205 large rooftops (1.6–3.0M sqm) in a high-irradiance, high-tariff market; rooftop solar/storage cuts grid cost, hedges brownouts (links to VS-07/W470), and delivers the ESG decarbonization target (links to VS-25) | **New gap (Pass 5)** — VS-70 sold solar products to customers, VS-35 accounted for fixed assets, and VS-07/VS-20.3 contained single energy/solar-monitoring workflows (W111/W173); no value stream owned BuildRight's own generation/prosumer program (capex, EPC, net-metering, REC, decarbonization accounting) | **FILLED — VS-108** |
| 23 | **Store Remodel, Renovation & Lifecycle Refurbishment Program** | 200-store chain remodels/refurbishes on a ~5–7-year cycle (~30–40 events/year at PHP 8–25M each; ~PHP 300–700M/yr program) — the single largest lever for comp-sales growth, format relevance, and asset-value preservation | **New gap (Pass 6)** — VS-37 covers only *new* store opening/commissioning, VS-59 only closure/decommissioning, VS-20 only *new-build* construction, VS-97 the landlord/owner investment view, and VS-40 only the *capex accounting* of remodel spend (W1811–W2752); the *operational* remodel program (lifecycle scoring, scope/concept/design, phasing around a live trading store, FF&E/signage rollout, technology/POS refresh, merchandise reset, re-opening, post-remodel analytics) was entirely uncovered | **FILLED — VS-109** |
| 24 | **Freight Procurement, Carrier Management & Freight Audit** | Freight is a major cost line (inbound/import, line-haul, last-mile; ~400–600 import TEUs/month, ~5,000 replenishment orders/month, ~80% third-party fleet, ~42.9K ecommerce orders/month); PHP-hundreds-of-millions-to-low-billions of spend with no single owner for carrier contracting/rate/routing-guide/freight-audit/landed-cost | **New gap (Pass 6)** — the freight-financial discipline was sprinkled across VS-02.2 (import freight, W66 inter-island, W249 demurrage), VS-04 (DC), VS-06.1 (outbound), and VS-06.3 (last-mile, incl. the single carrier-rate/freight-audit workflow W1166 and W1371/W1439/W1440); VS-56 covers only the last-mile 3PL *delivery-partner* relationship, VS-87 customs/tariff, and VS-15 AP processing — no value stream owned the end-to-end freight-spend/carrier-relationship/landed-cost program | **FILLED — VS-110** |
| 25 | **Packaging, Pallet & Returnable Transport Item (RTI) Management** | At BuildRight's volume (~72K inbound receipts/yr, ~134M POS line items/yr), packaging/pallets/RTI are a material cost line (PHP 200–500M/yr), a damage/shrink source, a freight-cube driver, and a sustainability/EPR (RA 11898) and single-use-plastic exposure | **New gap (Pass 6)** — referenced incidentally across VS-04 (DC receiving/palletization), VS-05 (merchandise inventory), VS-06 (logistics), VS-32 (reverse), VS-73 (waste), VS-41 (private-label packaging), VS-87 (import/ISPM-15), VS-24.3 (hazmat); no value stream owned the packaging-engineering, pallet/RTI pool, tracking/reconciliation, compliance/EPR, or cost-analytics discipline | **FILLED — VS-111** |
| 26 | **Corporate Project & Program Management Office (PMO)** | PHP 800M–1.2B annual capex plus major transformation programs (ERP/digital, net-zero/renewable, omnichannel, store-format evolution) run dozens of concurrent projects and several multi-project programs requiring portfolio governance, stage-gate discipline, resource/capacity planning, dependency/risk management, and benefits realization | **New gap (Pass 6)** — VS-40 performs only the *financial accounting* of capital projects (request/approval/commitment/CIP/turnover/variance/ROI-review W1811–W2752); VS-33 sets the budget envelope and tracks corporate KPIs; and the delivery-domain VSs (VS-20/VS-37/VS-109/VS-108/VS-27/VS-06) execute their respective project types — no value stream owned the enterprise project-portfolio governance/methodology/program-management/benefits-realization discipline | **FILLED — VS-112** |
| 27 | **Enterprise Architecture, Application Portfolio & Technology Strategy** | A 5-entity, 200-store, PHP 62.3B-revenue retailer on a unified cloud ERP with ~10+ active integration touchpoints (POS, ecommerce, payments, bank, BIR eFPS, statutory, delivery, loyalty, WMS, supplier portal) and an expanding digital perimeter (ecommerce, marketplace, retail media, mobile app, BIR e-invoicing, AI/ML) requires a continuous enterprise-architecture discipline to keep the application landscape coherent, integrated, secure, standards-compliant, and strategy-aligned | **New gap (Pass 7)** — 'enterprise architecture' appeared in **0** PA files; VS-27 operates/secures platforms, VS-28 consumes data, VS-30 evaluates emerging tech/POCs, VS-99 manages hardware/software asset lifecycle — none designs and governs the application landscape, integration architecture, technology standards, solution architecture, or multi-year technology strategy | **FILLED — VS-113** |
| 28 | **Dangerous Goods (DG) & Hazardous Materials Transport, Ecommerce & Regulatory Compliance** | An 8–10%+ DG-intensive assortment (paint/solvents ~2,800 SKUs, adhesives/thinners, aerosols, garden/agro chemicals, cleaning chemicals, fuels/lubricants, gas cylinders, lithium-battery products) moves by import ocean freight (~400–600 TEUs/month), inter-island sea/land, DC-to-store distribution, and ecommerce last-mile (~42,900 orders/month) under multiple regulators (DENR-EMB RA 6969, BFP Fire Code, DOLE OSH, MARINA/Coast Guard, CAB, LTFRB/DOTr) and international modal rules (IMDG/IATA/ADR); non-compliance causes carrier refusal, ecommerce channel blocking, port seizure, fines, and fire/spill/injury risk | **New gap (Pass 7)** — VS-24.3 (HSE) covers only **fixed-site** storage/handling safety; VS-87 covers import customs; VS-89 covers defective-product recall; VS-111 engineers product/transport packaging generally — no value stream owned the DG transport, ecommerce ship-eligibility, DG documentation/carrier-qualification, DENR-EMB hazardous-waste transport manifest, DG site permitting, or DG incident/spill/claim lifecycle | **FILLED — VS-114** |
| 29 | **Calibration, Metrology & Measurement Traceability Management** | Catch-weight and cut-to-length selling (lumber/board-foot, wire/meter, nails bulk, tiles/sq-m) at 600 POS across 2.8M monthly transactions; custom fabrication (pipe/lumber/sheet/wire cutting) and paint mixing/tinting at every store; DC weighbridges/truck scales at 4 DCs; fuel & logistics meters; environmental/process instruments; and test & measurement tools — measurement accuracy directly determines revenue accuracy, inventory accuracy (≥97% target), quality acceptance, and DTI weights & measures / Consumer Act RA 7394 compliance | **New gap (Pass 7)** — calibration/metrology was referenced incidentally across **53** PA files (VS-08 POS scales, VS-09 cutting/paint, VS-04 DC scales, VS-07 store equipment, VS-31 quality instruments, VS-12 rental tools, VS-61 fuel, VS-23 system calibration) with **no dedicated owner** and **zero** PA with 'calibration' or 'metrology' in its title — no value stream owned the program, standards/traceability, scheduling, records, or compliance discipline | **FILLED — VS-115** |
| 30 | **Performance Bond, Surety & Bank Guarantee Management** | ~10% B2G + ~30% B2B/project revenue under RA 9184 (Government Procurement Reform Act) and large enterprise contracts require bid bonds, performance bonds (5–30%), payment bonds, warranty bonds, and retention — secured by surety bonds or bank guarantees/LCs/cash that encumber on the order of **PHP 5M–50M+** of credit facility simultaneously and tie up capacity that otherwise supports operations | **New gap (Pass 7)** — VS-46 (B2G) references the bond as one bid step, VS-11 (B2B/project) references tender/performance bonds in bidding, VS-18 (Treasury) manages the bank/facility — no value stream owned the surety facility strategy, bond application/issuance/tracking/encumbrance lifecycle, counter-indemnity/collateral, release/closeout, claim/default response, or surety analytics | **FILLED — VS-116** |
| 31 | **DTI-BPS Product Standards Certification & PS Mark/ICC Compliance** | ~44% of the 35,000-SKU assortment by category mix is DTI-BPS-regulated (steel/cement/PVC ~14%, tiles ~12%, electrical ~10%, paint/coatings ~8%) and ~40% is imported; RA 4109 and DTI-BPS DAOs make PS Mark / ICC / SOC certification a legal prerequisite to sale, with ~10–15 regulated import shipments/month, market-surveillance exposure, and per-unit ICC-sticker obligations | **New gap (Pass 8)** — only the single import-clearance workflow **W447** in VS-22.1 existed; VS-87 clears customs, VS-31 runs internal QC, VS-89 recalls defective product — no value stream owned the full PS-Mark-license / vendor-certification / accredited-testing / ICC-sticker / market-surveillance / vendor-recovery program | **FILLED — VS-117** |
| 32 | **Revenue Assurance, Pricing Integrity & Leakage Management** | ~PHP 62.3B revenue / 2.8M monthly POS transactions across 600 terminals / ~42,900 ecommerce orders/month / ~600K loyalty members / gift-card / marketplace-3P / catch-weight selling; retail revenue leakage benchmarks 1–3% of gross revenue = **PHP 0.6B–1.9B/yr** at risk from pricing, promo/loyalty/gift-card, refund/reversal, catch-weight/weighing, discount-stacking, VAT/tax, payment/MDR, and settlement leakage | **New gap (Pass 8)** — only the single monthly-audit workflow **W348** in VS-21.3 existed; VS-23 addresses inventory shrink (a different vector), VS-17.4 reports revenue, VS-08 executes the transaction — no value stream owned the continuous, all-channel revenue-assurance / leakage-detection / recovery program | **FILLED — VS-118** |
| 33 | **Whistleblower, Ethics & Corporate Integrity (Speak-Up) Program** | 6,757 employees + ~10–20% contingent labor across 200 stores/4 DCs/5 entities; ~800–1,000 vendors; ~10% B2G + ~30% B2B revenue (ABC exposure); cash/data handling at scale — an enterprise speak-up channel, independent investigation, and whistleblower protection is a governance expectation (board audit/risk oversight, ISO 37001/37301) | **New gap (Pass 8)** — only the single ABC-specific workflow **W2943** in VS-86.3 existed; VS-21 audits controls, VS-100 manages litigation, VS-23 investigates theft, VS-84 handles grievances, VS-103 runs HR cases — no value stream owned the multi-channel intake / triage / investigation / retaliation-protection / culture / analytics program across **all** violation types | **FILLED — VS-119** |
| 34 | **Energy Efficiency, Conservation & RA 11285 Compliance Program** | ~205 large energy-consuming sites (200 stores at 8,000–15,000 sqm + 4 DCs + HQ) are RA 11285 (Energy Efficiency & Conservation Act, 2019) designated establishments with statutory obligations: designate an Energy Efficiency Officer, conduct mandatory energy audits (Type-1 every 3 yrs / Type-2 annually), prepare and submit an Energy Conservation Plan and annual reporting to DOE; energy is a material cost line and decarbonization lever | **New gap (Pass 8)** — referenced incidentally across 14 PA files (W692/W1543 energy consumption in VS-25.1, W701/W1563 in VS-20.3, W111 utility bill, VS-108 own-generation) with **zero** dedicated workflow headers; VS-25 reports the footprint, VS-108 generates clean energy, VS-34 buys transactionally — no value stream owned the RA 11285 compliance program / ISO 50001 EnMS / ECM pipeline / M&V / energy-procurement-retail-competition discipline | **FILLED — VS-120** |
| 35 | **Talent Acquisition, Employer Brand & Candidate Experience** | ~1,200–1,600 hires/yr at 15–20% turnover across a 5-entity, 205-location, ~6,757-employee group competing for scarce corporate *and* trade-knowledgeable frontline talent in the Philippine market; the strategic candidate-side discipline (EVP, career site, candidate experience, sourcing-channel strategy, talent community, campus/vocational feeder, candidate NPS, TA operations) directly drives time-to-fill, cost-per-hire, offer-acceptance, and early-attrition | **New gap (Pass 9)** — VS-19.1 executes recruitment *transaction* processing only (W15/W179/W715/W682) and VS-103.2 owns the *employee* experience; 'candidate experience', 'career site', and 'talent community' each appeared in **zero** PA files and 'employer brand' only incidentally (3 PA files) — no value stream owned the *attraction and candidate-side* discipline | **FILLED — VS-121** |
| 36 | **Global Sourcing, Import Buying & Sourcing Agent Management** | ~40% of COGS imported (~PHP 17–18B/yr), ~400 international vendors across China/Taiwan/Indonesia/Malaysia/Japan/Europe, ~400–600 import TEUs/month, ~PHP 1.4B/month import value, commodity-intensive assortment; the strategic source-side discipline (source-market/country strategy, sourcing-model decision, sourcing-agent/overseas-buying-office governance, import vendor development, consolidated container buying, total-landed-cost sourcing) materially drives COGS, availability, and supply-base resilience | **New gap (Pass 9)** — VS-02.2 executes operational import/customs, VS-03 executes transactional vendor/PO, VS-87 customs compliance, VS-31/VS-41 quality/factory audit; 'global sourcing', 'sourcing agent', and 'overseas buying office' each appeared in **zero** PA files — no value stream owned the *strategic source-side* discipline | **FILLED — VS-122** |
| 37 | **Skilled-Trade Apprenticeship, Vocational Education & Capability Pipeline** | BuildRight's differentiation is knowledgeable trade staff (lumber/tile/plumbing/electrical/paint/tools) plus fabrication/estimation/installation specialists, in a Philippine market where trade certification runs through the TESDA (RA 7796) NC/COC framework and such talent is scarce; a structured apprenticeship/vocational capability pipeline is the primary lever on service quality, attach, and the credible "home-building partner" positioning | **New gap (Pass 9)** — VS-19.4 runs general employee L&D/competency, VS-12.3 W1556 is a single TESDA school career-day *participation* workflow, VS-43.3 trains trade *customers*; 'apprenticeship program' appeared in **zero** PA files and 'vocational' only incidentally (4) — no value stream owned BuildRight's *own* structured apprenticeship and vocational feeder | **FILLED — VS-123** |
| 38 | **Sales Enablement, Product Knowledge Mastery & Clienteling** | ~5,800 store staff serving 2.8M monthly POS transactions, ~PHP 1,800 ATV, ~40% B2B/trade revenue, ~600K loyalty members; associate selling effectiveness (product-knowledge mastery, consultative selling, clienteling/customer-360 at POS, attachment/linked/category selling, trade-pro consultative selling) is the single largest controllable lever on basket size, conversion, attach, and trade-pro capture | **New gap (Pass 9)** — product knowledge referenced across ~33 PA files and product training ~13 with **no dedicated owner**; 'clienteling' appeared in **zero** PA files and 'sales enablement'/'selling skills' in 2/1 — VS-19.4 owns general L&D, VS-13 loyalty/CRM, VS-07 daily store execution, VS-09 in-store services — no value stream owned the *associate selling-effectiveness* discipline | **FILLED — VS-124** |
| 39 | **Cross-Channel Fraud Management & Payment Fraud Protection** | ~PHP 62.3B revenue / 2.8M monthly POS transactions across 600 terminals / ~42,900 ecommerce orders/month (COD-heavy) / ~600K loyalty members / gift-card balances / ~5,200 trade accounts; retail fraud benchmarks 0.5–1.5% of gross revenue = **PHP 0.3B–0.9B/yr** at risk across payment fraud, return/refund abuse, promo/coupon/loyalty abuse, gift-card fraud, account takeover, first-party/friendly fraud, chargebacks, employee/internal collusion, and trade-account/application fraud | **New gap (Pass 10)** — fraud detection referenced across ~17 PA files and specific fraud types handled as single steps within VS-32 (return), VS-58 (coupon), VS-80 (payment/chargeback), VS-13.2 (loyalty), VS-23 (physical shrink), VS-118 (pricing leakage), VS-86 (AML) — 'fraud orchestration' appeared in **zero** PA files and 'fraud management' in one — no value stream owned the *cross-channel fraud program* (detection rules/ML, case management, investigation, recovery, chargeback representment, internal-fraud, regulatory/law-enforcement, analytics) | **FILLED — VS-125** |
| 40 | **Customer Data Platform, Single Customer View & Identity Resolution** | ~600K loyalty members + ~5,200 trade accounts + ~200 corporate accounts + ~515K ecommerce orders/yr + 2.8M monthly POS transactions + clienteling/personalization ambition; the inability to resolve a single customer across cash/loyalty/ecommerce/trade/app touchpoints blocks personalization, loyalty accuracy, retention, CLV decisions, and consent-compliant marketing under RA 10173 | **New gap (Pass 10)** — 'CDP' referenced across ~23 PA files and 'customer data platform' ~12 with no dedicated owner; 'customer golden record' appeared in **zero** PA files and 'identity resolution' in two — sprinkled across VS-13 (loyalty), VS-29 (master data), VS-107 (key account), VS-10 (ecommerce), VS-75 (app) — no value stream owned the *CDP platform and single-customer-view discipline* | **FILLED — VS-126** |
| 41 | **Sales & Operations Planning (S&OP) & Integrated Business Planning (IBP)** | 35K SKUs across 200 stores + 4 DCs, ~40% imports with 45–90-day lead times (demand errors compound over long lead times), heavy Philippine seasonality (rainy-season, ber-months, summer), 6–8x inventory-turn target, ~PHP 42–45B COGS; the monthly cross-functional consensus demand-supply cycle that balances forecast, supply constraints, inventory, and the financial plan | **New gap (Pass 10)** — 'S&OP' referenced across ~20 PA files and 'demand planning/forecasting' ~24–31 with no dedicated owner; 'integrated business planning', 'IBP', and 'sales and operations planning' each appeared in **zero** PA files — sprinkled as single steps inside VS-02 (operational supply), VS-101 (merchandise financial plan), VS-33 (corporate strategy), VS-106 (commodity) — no value stream owned the *S&OP/IBP consensus-planning process* | **FILLED — VS-127** |
| 42 | **AI/ML Governance & Responsible AI** | Rapidly expanding AI/ML footprint — fraud detection (VS-125), demand forecasting (VS-127), personalization/recommendation (VS-126), pricing/markdown, inventory optimization, LP analytics, customer-service chatbots, document/OCR automation, and generative-AI assistants across the PHP 62.3B-revenue, 5-entity, ~6,757-employee operation; uncontrolled models cause revenue loss (bad forecast/price), customer harm (unfair bias, wrongful fraud decline, privacy breach), and regulatory/reputational exposure under RA 10173 automated-decision rights and emerging PH AI rules | **New gap (Pass 10)** — 'AI governance' referenced in ~3 PA files, 'responsible AI' in 1, and the defining terms 'model risk management' and 'algorithmic fairness' in **zero** PA files each — AI/ML is engineered inside VS-30.2 and used by VS-125/VS-126/VS-127/VS-28/VS-113 — no value stream owned the *AI-governance and responsible-AI discipline* (model inventory/risk, fairness/bias, explainability, AI privacy/consent, safety/robustness, human oversight, GenAI governance, ISO 42001/NIST AI RMF) | **FILLED — VS-128** |
| 43 | **Competition & Antitrust Compliance (RA 10667 / PCC)** | A dominant-share, 200-store, ~PHP 62.3B-revenue retailer with pervasive pricing (VS-57), trade/resale-pricing and RPM exposure with ~800–1,000 vendors (VS-03/VS-11/VS-43/VS-82), association/coalition conduct (VS-104), buyer-power in procurement, marketplace/retail-media platform conduct (VS-95/VS-48), and an M&A pipeline (VS-130) — each a distinct antitrust vector under RA 10667 and PCC guidance, with fines up to PHP 250M (first offense) and private damages exposure | **New gap (Pass 11)** — only the single workflow **W2683** (Philippine Competition Law Compliance) in VS-76.2 existed, with scattered antitrust guardrail references in VS-104/VS-46/VS-71.3/VS-100.3/VS-119 — no value stream owned the end-to-end competition-compliance program (market-power assessment, pricing/conduct controls, RPM/clause controls, association protocol, merger notification, PCC engagement/investigation/leniency, penalty/remediation) | **FILLED — VS-129** |
| 44 | **Corporate Development, Mergers, Acquisitions, Divestiture & Strategic Transactions** | A growth-stage, 5-entity, 200-store retailer growing 10–15 stores/year whose path includes acquiring competitor chains/banners, specialty/service businesses, JVs (property/digital/fintech), and divesting/carving out non-strategic assets — the inorganic-growth lifecycle (target sourcing, valuation, DD, SPA, regulatory clearance incl. PCC, Day-1, PMI/synergy, carve-out/TSA, divestiture) carries PHP-hundreds-of-millions-to-low-billions per major transaction and a 60–70% integration-failure rate | **New gap (Pass 11)** — 'merger and acquisition' and corporate-transaction 'divestiture' each appeared in **zero** PA files (the only 'divestiture' references were conflict-of-interest divestiture) — VS-33 sets strategy, VS-37 opens stores, VS-40 accounts for capex, VS-112 runs PMO, VS-100.3 provides legal advisory, VS-129 handles PCC clearance — no value stream owned the *M&A transaction lifecycle* | **FILLED — VS-130** |
| 45 | **Human Rights, Modern Slavery & Responsible Supply Chain Due Diligence** | A commodity-intensive, ~40%-import assortment (tools/electronics, paint/chemicals, lumber, tiles, PPE, garden/agro) sourced from China/Taiwan/Indonesia/Malaysia/Japan/Europe, sold to international B2B customers subject to UK MSA/German LkSG/EU CSDDD/US UFLPA — exposing BuildRight to forced/modern-slavery labor, child labor, unsafe conditions, irresponsible recruitment, conflict-minerals, and land-rights risk across its own operations and supply chain | **New gap (Pass 11)** — 'human rights' and 'modern slavery' each appeared in only **one** PA file (an ESG *reporting topic* in VS-25.2 and an audit *risk* in VS-21.3) — VS-25.2 touches environmental/diversity sourcing, VS-03 runs vendor ops, VS-122 executes import sourcing, VS-31/VS-117 address product quality/standards, VS-119 internal ethics — no value stream owned the *human-rights due-diligence program* | **FILLED — VS-131** |
| 46 | **Corporate Political Engagement, Election Compliance & Public Affairs Governance** | A PHP 62.3B, 5-entity, 200-store, multi-region retailer with substantial B2G sales (VS-46), LGU relationships (VS-76), industry advocacy (VS-104), and board/investor transparency expectations — operating under the Omnibus Election Code, RA 9006/COMELEC (corporate political contributions largely prohibited, with criminal liability), RA 3019 anti-graft, and RA 6713 | **New gap (Pass 11)** — 'political contribution', 'election compliance', and 'COMELEC' each appeared in **zero** PA files — VS-104 manages govt-affairs *relationships*, VS-86 addresses *bribery*, VS-119 handles *misconduct*, VS-46 executes *B2G sales*, VS-14.3 manages *comms* — no value stream owned the *political-activity governance/compliance/discipline* | **FILLED — VS-132** |
| 47 | **Operational Excellence, Process Mining & Continuous Improvement Program** | A PHP 62.3B, ~6,757-employee, 200-store, 4-DC operation running ~4,860 documented workflows; without a dedicated OpEx/CI program, cycle-time drag, rework, manual handoffs, and process variants compound and erode the 12–14% EBITDA and 6–8x inventory-turn targets — the systematic-improvement discipline (process architecture/ownership, Lean/Six Sigma methodology, an improvement pipeline, process mining from ERP event logs, bottleneck/root-cause analysis, standard-work authoring, pilot execution, benefit realization, productivity/cost-out programs) | **New gap (Pass 12)** — 'operational excellence', 'process mining', 'continuous improvement', 'lean', 'six sigma', and 'kaizen' each appeared in **zero** PA files as dedicated workflow headers (the only matches were literal 'cleaning/cleanup' workflows) — VS-30 scouts *emerging tech/PoCs*, VS-21 *assures* controls, VS-112 delivers *projects*, VS-27 runs the *service desk* — no value stream owned the *continuous-improvement operating system* | **FILLED — VS-133** |
| 48 | **Organizational Change Management, Digital Adoption & Transformation Enablement** | A 5-entity, ~6,757-employee, 200-store workforce running a continuous pipeline of major change (cloud ERP, omnichannel/marketplace/retail-media build-out, 10–15 new-store openings/yr, the store-remodel program, net-zero/renewable, BIR e-invoicing) where the 60–70% transformation-failure benchmark is driven overwhelmingly by people-side failure (resistance, low adoption, change saturation) — the people-side-of-change discipline (stakeholder mapping, change-impact/readiness assessment, sponsor activation, equip-the-manager cascade, super-user network, resistance management, change-saturation management, go-live readiness/hypercare, digital-adoption platform, adoption measurement/sustainment) | **New gap (Pass 12)** — 'change management', 'OCM', 'change enablement', and 'adoption management' each appeared in **zero** PA files as dedicated workflow headers (only incidental ~45 PA-file mentions where a project notes 'communicate the change') — VS-30.1 owns the *digital-transformation portfolio*, VS-112 *project delivery*, VS-19.4/VS-124 *training content*, VS-103.1 *HR comms*, VS-27.1 the *IT service desk* — no value stream owned the *OCM discipline* | **FILLED — VS-134** |
| 49 | **Technology Business Management, IT Financial Management & Cloud FinOps** | A cloud-first, integration-heavy retailer with ~10+ integration touchpoints and an expanding SaaS/AI perimeter where technology spend runs ≈1–3% of revenue (PHP 0.6B–1.9B/yr) across cloud, SaaS, software, telco/network (205+ sites), and the IT org — ungoverned, that spend leaks value through under-used licenses, idle cloud resources, shadow IT, and un-optimised commitments — the financial-management-of-technology discipline (TBM cost taxonomy, zero-based IT budgeting, TCO/business-case modeling, showback/chargeback, FinOps inform/optimize/operate, SaaS license utilization, value realization, unit economics) | **New gap (Pass 12)** — 'finops', 'cloud cost', 'technology business management', 'IT financial management', and 'TBM' each appeared in **zero** PA files as dedicated workflow headers — VS-99 tracks *asset inventory/disposal*, VS-113 designs the *application landscape*, VS-27 *operates* platforms, VS-17.4/VS-33 do *corporate FP&A*, VS-34 buys *transactionally* — no value stream owned the *technology-financial discipline* | **FILLED — VS-135** |
| 50 | **Supply Chain Network Design, Multi-Echelon Inventory Optimization & Flow Engineering** | A 4-DC, 200-store, 35K-SKU retailer with ~40% imports (45–90-day lead times), Philippine island geography, and a 6–8x turn target where network/inventory positioning is the single largest controllable lever on working capital, service level, and total landed cost — a 1% inventory reduction releases ~PHP 0.4B of working capital — the structural-engineering discipline (network strategy/modeling, DC footprint/location/capacity, inbound sourcing-lane and outbound flow architecture, network resilience, inventory strategy/postponement/pooling, MEIO, safety-stock/service-level optimization, ABC/XYZ-differentiated policy, simulation/digital-twin, continuous re-optimization) | **New gap (Pass 12)** — 'multi-echelon', 'inventory optimization', 'network design', 'safety stock optimization', and 'postponement' each appeared in **zero** PA files as dedicated workflow headers (only the single periodic W183 network-review workflow in VS-02.3) — VS-02 runs *operational* replenishment, VS-127 the *consensus cycle*, VS-05 inventory *transactions*, VS-06 *logistics execution* — no value stream owned the *network/inventory-engineering discipline* | **FILLED — VS-136** |
| 51 | **Product Information Management (PIM) & Digital Asset Management (DAM)** | A 35,000-active-SKU (≈55,000-master) hardware assortment sold across six channels (POS/web/app/marketplace/retail-media/print) plus B2B, with ~44% DTI-BPS-regulated and ~8–10% DG (paint/solvents ~2,800 SKUs) requiring accessible Safety Data Sheets — product-content completeness/accuracy directly drives ecommerce conversion, marketplace win-rate, associate consultative selling, and labeling compliance; content fragmentation and stale/missing content (an un-declared SDS, a wrong spec/load rating, a stale SRP) cause lost sales, returns, and Consumer Act (RA 7394)/DTI-BPS exposure | **New gap (Pass 13)** — 'product information management'/'PIM' and 'digital asset management'/'DAM' appeared scattered across ~30 PA files (VS-01 assortment, VS-10 ecommerce, VS-09 in-store, VS-48 retail media, VS-29 master data) with **zero** dedicated workflow headers; each channel kept its own copy and assets lived on shared drives — no value stream owned the *product-content operating model* (canonical model/taxonomy, onboarding, DAM/SDS lifecycle, rich content, channel syndication, quality, analytics) | **FILLED — VS-137** |
| 52 | **Integrated Facilities Management, Workplace Services & Building Automation** | ~205 large sites (200 stores at 8,000–15,000 sqm + 4 DCs ~130,000 sqm + HQ) under tropical-climate, typhoon/seismic, and fire/life-safety (BFP Fire Code, OSH) pressure, running hard building services (HVAC, lighting, fire/life-safety, plumbing, elevators, generators, BMS) and soft workplace services (cleaning, pest, guarding, grounds, waste, cafeteria) as a material opex line — fragmented/overlapping service contracts leak value, and a failed AC or fire system directly closes a store | **New gap (Pass 13)** — facility/building-service terms were sprinkled across ~30 PA files (VS-20.3 facility maintenance, VS-07.2 store equipment, VS-120 energy, VS-98 outsourced workforce, VS-73 waste, VS-23 security, VS-34 procurement) with **zero** dedicated workflow headers for the *integrated* IFM operating model — no value stream owned IFM strategy/provider governance, the hard+soft service catalog/SLA, PM/reactive maintenance coordination, workplace services, BMS/building-automation, or facilities analytics | **FILLED — VS-138** |
| 53 | **Trade Show, Exhibition & Field Event Marketing** | ~40% B2B revenue (30% trade + 10% corporate) targeting contractors/builders/developers/architects/government-project buyers via construction/home-building trade shows (PhilConstruct ~100K+ attendees, Worldbex, CebuCon) and hosted field events (contractor trade days, product launches); ~PHP millions/yr spent on booths/sponsorship/samples with vendor co-funding — the relationship-driven, time-bound event channel where projects and trade accounts are won, and where lead-follow-up failure converts the entire spend to zero return | **New gap (Pass 13)** — trade-show/exhibition/event-marketing terms appeared scattered across ~9 PA files (VS-01, VS-02, VS-03, VS-14, VS-30, VS-41, VS-43, VS-44, VS-70) with **zero** dedicated workflow headers; each event run ad-hoc by its sponsor — no value stream owned the *event-marketing operating model* (portfolio/calendar, booth/sponsorship logistics, lead capture/follow-up, vendor co-fund, permits/ABC compliance, ROI) | **FILLED — VS-139** |
| 54 | **Field Sales, Outside Sales & Route-to-Market Force Management** | ~40% B2B revenue (~PHP 25B/yr) across ~5,000 trade accounts + ~200 corporate accounts is project-driven, relationship-driven, and specification-driven, won or lost at the jobsite/architect's office/developer's procurement — a field sales force covering territories, calling accounts, estimating/quoting, and pursuing project bids/specifications is the primary revenue engine for the B2B segment; a mis-sized/mis-routed/under-enabled force forfeits B2B share and lets the ~5,000-account base churn unnoticed | **New gap (Pass 13)** — field/outside-sales/territory terms appeared in only ~1–3 PA files (VS-82, VS-11) with **zero** dedicated workflow headers; field activity happens inside trade-account/B2B-project workflows but no value stream owned the *field-sales operating model* (force-sizing/territory design, quota/coverage, route/call planning, daily field activity, CRM pipeline/forecast, field compensation, enablement/coaching, performance/route analytics) | **FILLED — VS-140** |
| 55 | **Employee Transport, Shuttle & Daily Commute Management** | ~6,757 employees across 205 distributed sites (200 stores + 4 DCs + HQ) on 2–3 shifts/day including the 10 PM–6 AM night-differential window; provincial/island sites have thin or unsafe after-hours public transport, and commute difficulty is a documented frontline attrition driver at the 15–20% turnover rate — an owned daily people-movement discipline directly affects attendance, safety, payroll (transport allowance), and retention | **New gap (Pass 14)** — 'employee shuttle', 'staff shuttle', 'company bus', 'shuttle route', 'transport allowance', and 'daily commute' each appeared in **zero** PA files as dedicated workflow headers; only adjacent coverage exists (VS-19.1 *business travel* ~600–960 trips/yr, VS-18.2 petty-cash *errand* transport, VS-138 *building* services, VS-06 *goods* fleet) — no value stream owned the *daily people-movement discipline* (commute-need assessment, transport policy/allowance, shuttle fleet/routes/manifest, driver/vendor/safety, late-night/women-safe transport, cost allocation, commute-EX/analytics) | **FILLED — VS-141** |
| 56 | **Cash-on-Delivery (COD) Operations, Driver Cash Handling & Reconciliation** | The Philippines is a COD-dominant ecommerce market and BuildRight accepts COD (profile §8.1) across ~42,900 ecommerce orders/month plus MSME (VS-82) and trade deliveries (VS-74); at a 30–50% COD share that is ~13,000–21,000 COD orders/month, each carrying physical cash through a multi-party field chain with float, short-pay/refusal, and theft/fraud exposure — unreconciled COD cash directly distorts revenue, inventory, and AR, with leakage benchmarked at 0.3–1.0% of COD GMV | **New gap (Pass 14)** — 'COD operations', 'driver cash handling', 'COD reconciliation', and 'cash-on-delivery settlement' each appeared in **zero** PA files as dedicated workflow headers; only W2837 (MSME-segment COD in VS-82) and W1202 (store daily cash collection) existed, with COD scattered as single steps across VS-06.3/VS-08.2/VS-10.2/VS-16.3/VS-80/VS-56 — no value stream owned the *enterprise COD cash-chain discipline* (policy/limits, doorstep collection/custody, driver/3PL remittance & reconciliation, settlement/float, fraud, analytics) | **FILLED — VS-142** |
| 57 | **Bulky & White-Goods Delivery, Installation, Haul-Away & Recycling** | Appliances (1,750 SKUs, 5%) + furniture (1,750) + large-format tile + lumber packs + solar water heaters are *scheduled, two-person, in-home* deliveries with installation, old-unit haul-away, and refrigerant/e-waste/scrap recycling — a distinct bulky last-mile + reverse-logistics chain where a failed window or a mishandled refrigerant charge costs a sale (VS-16), a return (VS-32), a safety incident (VS-24), and a DENR/RA 9275/RA 11898 exposure | **New gap (Pass 15)** — 'bulky delivery', 'appliance installation', 'haul-away', 'old-unit recycling', and 'refrigerant recovery' each appeared in **zero** PA files as dedicated workflow headers; only adjacent coverage exists (VS-06.3 generic last-mile, VS-12 generic install/tool-rental, VS-32 customer returns, VS-73 store waste) — no value stream owned the *bulky delivery + install + haul-away + recycling program* | **FILLED — VS-143** |
| 58 | **Employee Accommodation, Dormitory & Staff Housing** | ~6,757 employees across ~205 distributed provincial/island sites (200 stores + 4 DCs + HQ) on 2–3 shifts incl. the 10 PM–6 AM window, plus transferees and the 10–15 new-store/yr expansion — staff housing is a frontline-attrition and site-staffing lever (alongside VS-141 daily transport) carrying welfare, BFP/OSH, and cost-recovery obligations | **New gap (Pass 15)** — 'staff dormitory', 'staff house', 'bunkhouse', 'employee housing', and 'company barracks' each appeared in **zero** PA files as dedicated workflow headers (5 incidental mentions) — only adjacent coverage exists (VS-141 daily commute, VS-138 commercial facilities, VS-20.3/VS-97 buildings, VS-34 transactional procurement) — no value stream owned the *workforce-housing program* | **FILLED — VS-144** |
| 59 | **Garden Center, Live Goods & Plant Nursery Operations** | Garden & Outdoor (~3% of SKUs = ~1,050 live-plant/nursery SKUs across 200 store garden centers) is *perishable biological merchandise* requiring daily care (watering/pruning/acclimatization), with visible decline, pest/disease, and live-goods shrink benchmarks of 8–20% — fundamentally unlike hard-goods inventory (VS-05) and frequently vendor-consigned/seasonal/regulated (phytosanitary-BPI, pesticide-FPA, restricted-species) | **New gap (Pass 15)** — 'live goods', 'plant nursery', 'plant care', 'live-goods shrink/mortality', and 'live-goods markdown-on-decline' each appeared in **zero** PA files as dedicated workflow headers; only the single W1487 (garden seasonal rotation/VMI) in VS-07.1 existed — no value stream owned the *live-goods operating discipline* | **FILLED — VS-145** |
| 60 | **Customer Mystery Shopping & Service Quality Assurance** | 2.8M monthly POS transactions across 200 stores + ecommerce/app + B2B/field/contact-center — service quality is a primary controllable lever on conversion, basket, loyalty, and the 'Your Home Building Partner' positioning, but is only credible as *independent, objective, evidence-based assurance* (not self-reported store metrics), and carries its own integrity (shopper collusion/gaming) and RA 10173 consent/fairness dimensions | **New gap (Pass 15)** — 'mystery shopping', 'service audit', 'service quality assurance', and 'service standards compliance' each appeared in **zero** PA files as dedicated workflow headers (~13 incidental mentions) — scattered as single steps inside VS-13 (reactive CX/complaints), VS-07 (self-reported standards), VS-21 (financial-control audit), VS-133 (process improvement), VS-124 (selling-skills) — no value stream owned the *independent service-quality assurance program* | **FILLED — VS-146** |
| 61 | **Customer Safety, Premises Liability & In-Store Risk Management** | ~205 high-traffic public sites (200 stores at 8,000–15,000 sqm + 4 DCs will-call + doorstep) running 2.8M monthly POS transactions where customers/trade-pros/contractors share the floor with **forklifts, reach trucks, lumber/tile/cement loads, overhead racking, paint/chemical aisles, and a lumber yard** — the customer premises-liability exposure (slip/trip/fall, falling/shifted merchandise, powered-equipment contact, parking, chemical exposure, crowd crush, child/PWD harm) is structurally one of BuildRight's largest and most litigation-exposed operational risks | **New gap (Pass 16)** — 'premises liability', 'customer safety', 'falling merchandise', 'aisle safety', and 'forklift-in-sales-area' each appeared in **zero** PA files as dedicated workflow headers — sprinkled as single steps inside VS-24 (employee/occupational HSE), VS-23 (shrink/theft LP), VS-07 (self-reported housekeeping), VS-138 (building IFM), VS-20/VS-109 (site design as a project) — no value stream owned the *customer-facing premises-liability & in-store safety program* | **FILLED — VS-147** |
| 62 | **Lease Accounting (PFRS 16/IFRS 16) & Right-of-Use Asset Management** | A 5-entity group operating ~205 mostly-**leased** sites (200 stores + 4 DCs + HQ, many leased from its own BuildRight Property Mgmt Inc.) plus leased forklifts/fleet/IT/POS/fixtures — a large heterogeneous lease portfolio recognized under **PFRS 16** as right-of-use assets and lease liabilities (since 2019); mis-recognition distorts EBITDA/EBIT, leverage covenants, and the audited PFRS financials, with heavy disclosure/judgment areas (discount rate, term, renewal options, variable payments) | **New gap (Pass 16)** — 'right-of-use', 'lease liability', and 'ROU asset' each appeared in **zero** PA files as dedicated workflow headers and 'PFRS 16' in only 3 (scattered single-step mentions) — conflated with VS-42 (lessee commercial lease admin), VS-17.3 (tax deduction), VS-18 (cash), VS-20.1 (lease intake), VS-35 (owned assets), VS-29 (contract master) — no value stream owned the *PFRS 16 recognition/measurement/disclosure program* | **FILLED — VS-148** |
| 63 | **Self-Checkout, Scan-&-Go & Unattended Retail Technology Operations** | A 200-store, 600-terminal, 2.8M-monthly-transaction big-box retailer under wage (DOLE minimum/13th-month) pressure with a self-service-conditioned customer base — SCO/scan-&-go/unattended is a strategic wage-and-queue lever, but without a dedicated program leaks margin (SCO loss benchmarks 2–5× staffed-POS shrink from scan-avoidance/swap/weight-manipulation), creates cash/tender-reconciliation exposure, and risks Consumer Act (RA 7394) price-integrity and BIR CAS/e-invoicing non-compliance | **New gap (Pass 16)** — 'scan-and-go', 'scan-go', 'unattended', and 'self-checkout' each appeared in **zero** PA files as dedicated workflow headers (only scattered single-step mentions) — conflated with VS-08 (staffed POS), VS-07 (store execution), VS-23 (broad shrink LP), VS-09.3 (amenity), VS-109 (project deployment) — no value stream owned the *SCO/scan-&-go/unattended operating program* | **FILLED — VS-149** |
| 64 | **Drug-Free Workplace & Substance Abuse Program** | ~6,757 employees across 5 entities/~205 sites plus ~10–20% contingent labor and a large **safety-sensitive** population (forklift/reach operators, delivery drivers under LTFRB/DOTr, paint/chemical handlers) inside a premises-liability-exposed customer environment (VS-147) — DOLE D.O. 53-03 and RA 9165 Art. V make a drug-free workplace program a legal obligation (non-compliance → DOLE finding/penalty + officers' personal RA 9165 liability), and an impaired operator/driver is a catastrophic safety risk | **New gap (Pass 16)** — 'drug test', 'drug-free workplace', 'substance abuse', 'reasonable suspicion', and 'random drug testing' each appeared in **zero** PA files as dedicated workflow headers — sprinkled as single steps inside VS-83 (clinic/exam), VS-19.1 (pre-employment onboarding), VS-24 (post-incident), VS-06.2 (driver), VS-22 (DOLE documentation), VS-56 (partner driver) — no value stream owned the *end-to-end drug-free workplace program* | **FILLED — VS-150** |
| 65 | **Auto-ID, Barcode, RFID, Price-Tag Labeling & EAS Operations** | At 35,000 active SKUs, 600 POS terminals, 200 stores, and 134.4M annual POS line items, the physical item-identification and labeling infrastructure (GS1/GTIN governance, label/price-tag format & production, shelf-edge/hang-tag/bulk-yard application, EAS/RFID tagging & detection) makes every SKU scannable, correctly priced (RA 7394 price-tag compliance), loss-protected (< 1.5% shrink target ≈ PHP 0.9B/yr), and traceable — a 1% scan-fail/misprice rate is ~1.3M failure events/yr (checkout friction + revenue leakage) | **New gap (Pass 17)** — 'auto-ID', 'barcode governance', 'RFID operations', 'price-tag labeling', and 'EAS operations' each appeared in **zero** PA files as dedicated workflow headers and **zero** VS directory names; the terms were scattered across VS-29 (W1345 barcode/GS1), VS-71 (authentication tags), VS-08 (POS scan), VS-23 (EAS/exception), VS-04/VS-05 (RFID bin/lot), VS-115 (calibration), VS-111 (transport labeling) — no value stream owned the *labeling & auto-ID operating discipline* (GS1 governance, label spec/production, in-store application, EAS/RFID operations, RA 7394 price-tag compliance, read-rate/label-conformance, fraud-vector control) | **FILLED — VS-151** |
| 66 | **Corporate Social Responsibility, Foundation & Community Investment** | A PHP 62.3B retailer operating across 200 Philippine communities with a stated ESG posture (VS-25) and a cooperative/community sourcing program (VS-94) requires a structured social-impact/community-investment discipline (the BuildRight Foundation, housing/shelter/livelihood/education/disaster-relief programs, employee volunteerism & payroll-giving, NGO/LGU partnerships, impact measurement & reporting); CSR spend benchmarks 0.5–2% of net profit (PHP ~0.2B–0.8B/yr) and ungoverned spend leaks value or fails measurable impact | **New gap (Pass 17)** — 'CSR' appeared across ~58 PA files, 'foundation' ~24, but as incidental *references*; 'CSR', 'social responsibility', 'foundation', and 'community investment' appeared in **zero** PA files as dedicated workflow headers — no value stream owned the *CSR/Foundation operating discipline* (strategy/governance, Foundation SEC/BIR-donee/PCNC setup, community-investment portfolio, disaster relief, volunteerism, impact measurement/SROI, GRI/IRIS+ reporting) | **FILLED — VS-152** |
| 67 | **Captive Insurance, Reinsurance & Enterprise Risk Financing** | At PHP 62.3B revenue, 205 typhoon/earthquake-prone sites, 600 POS, ~42.9K monthly ecommerce orders, ~6,757 employees, and ~5,200 trade accounts, the total cost of risk (property catastrophe, liability, fleet, crime, cyber, D&O, employee) is a material opex line, and the Philippine commercial market under-serves catastrophe/specialty lines — a captive that retains the predictable layer and reinsures the catastrophic layer is a standard risk-financing tool for large PH groups, reducing net cost of risk 10–25% | **Future business-model extension flagged in §6 of prior passes** — 'captive insurance', 'reinsurance', and 'self-insur' appeared in only 1–4 PA files as incidental references; this Pass 17 activates the previously-flagged future capability. Distinct from VS-26 (buys/claims commercial policies — this value stream operates the captive that underwrites/reinsures), VS-21.2 (measures risk — this finances it), and VS-18 (group cash — this manages captive capital) | **FILLED — VS-153** |
| 68 | **Home Construction Finance, Loan Brokerage & Mortgage Referral Services** | Home building/renovation is capital-constrained — many B2C homeowners and small contractors cannot start or complete projects without financing; BuildRight's 'Home Building Partner' positioning, project/design capability (VS-66), installation (VS-12), and B2B trade base make a construction-loan/mortgage brokerage offering a natural adjacency that lifts basket size, conversion, and project completion, with referral economics (0.5–2% of loan value) on a multi-billion financing flow | **Future business-model extension flagged in §6 of prior passes** — 'construction loan', 'home loan', and 'mortgage' appeared in only 1–6 PA files as incidental references; this Pass 17 activates the previously-flagged future capability *within BuildRight's retail charter* (broker/referral, not lending). Distinct from VS-38 (in-house store credit), VS-16 (trade AR), VS-66 (project design), and VS-12 (the build the financing releases funds to) | **FILLED — VS-154** |
| 69 | **Trade-In, Buy-Back & Certified Pre-Owned / Refurbished Product Resale** | Power tools, appliances, and equipment (~3,500 hand tools, ~1,750 power tools, ~1,750 appliances) have residual value and a price-sensitive secondhand market in the Philippines; a trade-in program drives new-purchase attach, captures the budget segment with certified pre-owned, differentiates on sustainability (VS-25/VS-73), and creates a circular revenue stream | **Future business-model extension flagged in §6 of prior passes** — 'trade-in', 'buy-back', 'pre-owned', and 'second-hand' appeared in 0–10 PA files as incidental references; this Pass 17 activates the previously-flagged future capability in a BuildRight-charter-consistent way (certified resale, not an open C2C marketplace). Distinct from VS-32 (defective returns for refund), VS-73 (end-of-life disposal/recycling), VS-12.1 (repair for the owning customer — this refurbishes for resale), and VS-05.3 (disposition of BuildRight's own unsold stock) | **FILLED — VS-155** |
| 70 | **In-Store Value-Added Services & Financial Agency Operations** | 200 provincial stores serving communities where bills-payment, domestic remittance, e-money cash-in/out, and mobile load are high-demand footfall drivers; ~600 customer-service counters with existing cash handling; a trust/community brand; and a commission-revenue + basket-linkage opportunity — but financial-agency operations carry BSP regulatory exposure (consumer protection, AML), cash-settlement risk, and data-privacy obligations | **New gap (Pass 17)** — 'bills payment', 'e-money', 'cash-in', and 'value-added service' appeared in 0–2 PA files as incidental references and in **zero** PA files as dedicated workflow headers — no value stream owned the *financial-agency/VAS operating discipline* (product/partner portfolio, BSP agent accreditation, counter operations/KYC, settlement/reconciliation/commission, AML/BSP compliance, fraud, analytics). Distinct from VS-80 (BuildRight's own merchandise payment rail), VS-08.2 (in-store retail cash), VS-86 (AML program — this executes it as agent), VS-142 (COD — BuildRight's own cash), and VS-146 (project financing) | **FILLED — VS-156** |
| 71 | **Revenue Recognition (PFRS 15) & Complex Contract Accounting** | ~PHP 62.3B revenue with a fast-expanding multi-element-arrangement portfolio (loyalty points on 2.8M monthly POS transactions, gift-card breakage, ~515K ecommerce orders/yr with mixed-basket fulfillment, bundles, product+installation, consignment/VMI sell-through, subscription, extended warranty, retail-media, marketplace commissions, COD, VAS/bills-payment, trade-in, construction-finance referral) — PFRS 15 five-step recognition, principal-vs-agent, SSP/allocation, variable consideration, financing component, contract-cost capitalization, and AFS disclosure are high-judgment, auditor-scrutinized areas that distort EBITDA and the audited PFRS financials if mis-applied | **New gap (Pass 18)** — the discipline existed only as the single over-stuffed workflow W487 in VS-15.1 (referenced across 12 PA files, explicitly acknowledging it covers 'complex scenarios' for eleven revenue streams with 'no PFRS 15 accounting assessment'), plus one-off recognition workflows per channel (W2014/W1971/W1992/W4618/W1771) and deferred-revenue accounting sprinkled across VS-13/VS-54/VS-17.4 — no value stream owned the *end-to-end contract-accounting discipline*. Distinct from VS-118 (revenue-leakage protection at the transaction), VS-17.4 (FP&A reporting), and each channel value stream (which operates the channel) | **FILLED — VS-157** |
| 72 | **Product Costing, Landed-Cost & Cost Accounting** | ~PHP 42–45B annual COGS, ~40% import (volatile freight/duty/FX), heavy commodity exposure (steel/cement/lumber/copper), catch-weight/cut-to-length selling at 600 POS, private-label growth, kitting/BOM, and large B2B/G2G project costing — the per-unit cost layer beneath every pricing/assortment/markdown/bid/private-label decision and the PFRS inventory provision | **New gap (Pass 18)** — the discipline existed only as the single workflow W85 in VS-17.4 (referenced across 25 PA files as the catch-all cost reference) — no value stream owned the *cost-accounting operating system* (standard-cost setup, import landed-cost build-up, catch-weight unit cost, kit/BOM roll, PL fully-burdened cost, PPV/landed-cost/conversion variance, margin analytics, project/service/intercompany costing, cost-master governance). Distinct from VS-05 (inventory transactions), VS-01.2/VS-101 (pricing that consumes margin), VS-106 (commodity hedging), and VS-17.4 (FP&A) | **FILLED — VS-158** |
| 73 | **Corporate Security, Executive Protection & Travel Risk Management** | A high-profile PHP 62.3B Filipino family corporation (named CEO/board), 200 stores across Philippine regions with elevated kidnap/extortion/civil-unrest exposure, executive and buyer travel (domestic inter-island + international sourcing VS-122), high-value cash/inventory, and an increasingly public brand — corporate security, executive protection, protective intelligence, travel-risk/duty-of-care, corporate investigations, and K&R response are a recognized gap in Philippine large-enterprise risk management | **New gap (Pass 18)** — 'executive protection', 'protective intelligence', 'corporate security', 'travel security', and 'kidnap & ransom' each appeared in **zero** PA files (the single 'threat intelligence' reference is cyber VS-27.3 W397); site-level physical security (store W71/W171, DC W797) and its audit (VS-21.3 W358), retail-shrink LP (VS-23), customer premises safety (VS-147), cyber (VS-27.3), and crisis comms (VS-14.3) cover adjacent ground — no value stream owned the *corporate-security & executive-protection program* | **FILLED — VS-159** |
| 74 | **Global Mobility, Immigration & Foreign Worker Compliance** | A family corporation operating global sourcing (VS-122 — likely with seconded experts), potential foreign executives/specialists across the 5-entity structure, provincial inter-island transfers across a 200-store footprint, and 10–15 new stores/yr — Philippine immigration/labor law (DOLE Alien Employment Permit, BI 9G Pre-Arranged Employee Visa & ACR I-Card, minimum-wage parity for foreign workers, tax-treaty/19-series residency rules) carries real compliance, penalty, and officer-personal-liability exposure | **New gap (Pass 18)** — 'immigration', '9G visa', 'alien employment', 'expatriate', 'international assignment', and 'employee mobility' each appeared in **zero** PA files as dedicated workflow headers (a single incidental 'work permit' reference); VS-19 (PH employees), VS-122 (vendor-side sourcing), VS-98 (contingent workforce), VS-103 (domestic HR shared services) cover adjacent ground — no value stream owned the *foreign-worker immigration & global-mobility program* | **FILLED — VS-160** |
| 75 | **Third-Party & Supplier Risk Management (TPRM)** | ~800–1,000 merchandise vendors, ~80% third-party logistics/fleet, heavy SaaS/cloud and payment dependencies, BPO/contact-center, CIT and security-guard agencies, sourcing agents, marketplace sellers, and professional/EPC contractors — a single significant third-party failure (financial collapse, cyber breach, regulatory action, concentration shock, modern-slavery exposure) can halt operations, breach data, or trigger regulator action; TPRM is a board-level discipline cited in BSP/NPC/ISO 31000/NIST CSF/SOC 2 supply-chain criteria | **New gap (Pass 18)** — each risk domain owned only its *slice* (W1328 supply-side criticality in VS-21.2, W334 audit in VS-21.1, W2942 ABC in VS-86.3, W3052 privacy in VS-91.2, W3863 fraud in VS-125.1, W3733 integrity in VS-119.3, human-rights in VS-131, commercial in VS-03/VS-67) — no value stream owned the *unified cross-domain enterprise TPRM program* (single inventory, cross-domain tiering, continuous monitoring, fourth-party mapping, concentration, resilience/exit, regulator-facing evidence) | **FILLED — VS-161** |
| 76 | **Customer Pickup Truck & Cargo Van Rental (Self-Haul) Operations** | 55% of revenue is B2C walk-in and the big-box format sells bulky, jobsite-bound merchandise (lumber 14%, tiles 12%, appliances 5%, furniture 5%) that won't fit a typical sedan/UV and is uneconomical to pay last-mile delivery for on a single trip; the well-known "Load N Go" self-haul rental operated by every major big-box home-improvement retailer converts the "I can't get it home" basket-abandonment into a same-day completed sale, plus rental/fuel/LDW income — across 200 stores even a small fleet (2–3 trucks + 1 van per store ≈ 600–800 vehicles) materially lifts large-item attach | **New gap (Pass 19)** — 'pickup truck rental', 'cargo van rental', 'self-haul rental', 'rent-a-truck', and 'customer vehicle rental' each appeared in **zero** PA files as dedicated workflow headers; the discipline is genuinely uncovered and distinct from VS-06 (goods delivery fleet / LTFRB freight), VS-12.2 (item/tool rental), VS-74/VS-56 (delivery services), and VS-141 (employee transport) — this rents a *titled registered motor vehicle to a customer to self-drive* under motor-vehicle-liability law | **FILLED — VS-162** |
| 77 | **Electric Vehicle (EV) Charging Station Host Network Operations** | BuildRight sells EV chargers as merchandise (Electrical category), already owns a rooftop solar/prosumer program (VS-108) and energy-efficiency/RA 11285 program (VS-120), runs a sustainability brand (VS-25), and holds ~205 large parking-rich sites; Philippine electrification is accelerating under RA 11697 (EVIDA, 2022) which mandates EV charging infrastructure in certain new buildings/parking — hosting EV charging converts BuildRight's real-estate + energy footprint into dwell-time basket, own-solar energy sales, decarbonization, and property future-proofing | **New gap (Pass 19)** — 'EV charging station host', 'EVSE host network', 'charging network operator', 'OCPI roaming', and 'EV charge point operations' each appeared in **zero** PA files as dedicated workflow headers (the ~28 incidental 'charging station'/'EV charg' references are almost all about selling chargers as merchandise or generic energy); genuinely uncovered and distinct from VS-108 (own-consumption generation — this *sells* energy/services to EV drivers), VS-120 (own energy efficiency), VS-06/VS-61 (own diesel fleet fueling — this also owns the *forward green-fleet charging* path), and VS-138 (general facilities) | **FILLED — VS-163** |
| 78 | **Smart Locker & Automated Parcel Collection Network** | ~42,900 ecommerce orders/month (~515K/yr) with a BOPIS share across all 200 stores, a COD-heavy market (VS-142), a growing marketplace presence (VS-65/VS-95), and ~2.8M monthly in-store footfall — a network of automated, self-service collection lockers (in-store, parking, and off-site) extends BOPIS beyond the counter and beyond store hours, removes the queue/within-hours friction that limits BOPIS convenience, unlocks returns drop-off (a major VS-32 friction), and enables a 3P-parcel-pickup revenue stream (the Amazon-Hub / Lazada-locker model) | **New gap (Pass 19)** — 'smart locker network', 'automated parcel collection', 'locker fleet operations', 'parcel pickup locker', and 'returns locker' each appeared in **zero** PA files as dedicated workflow headers (the ~19 incidental 'smart locker' references are scattered single-step mentions with no owning PA); genuinely uncovered and distinct from VS-10 (the BOPIS fulfillment *transaction* at the counter — this owns the *locker network infrastructure & channel*), VS-149 (in-store unattended *selling* tech — this owns outdoor/transit/off-site *parcel lockers*), VS-93/VS-60 (fulfillment — this owns the *collection endpoint*), and VS-32 (returns — this owns the *locker returns-drop-off channel* that feeds it) | **FILLED — VS-164** |
| 79 | **PCAB Contractor Licensing & RA 4566 Construction Contractor Compliance** | BuildRight performs installation (VS-12), customer design-build (VS-66), government delivery-and-install bids (VS-46/VS-11.2 — explicitly noting PCAB license "may be required for delivery-and-install bids"), bulky white-goods install (VS-143), and own-store construction (VS-20) — a body of work in which BuildRight is the *contractor of record*; under RA 4566 (Contractors' License Law), engaging in the business of contracting without a valid PCAB license is an unlawful act punishable by **fine and imprisonment** (Sec. 6/8), can render contracts unenforceable, and disqualifies the entity from public bidding (RA 9184) | **New gap (Pass 20)** — 'PCAB license', 'RA 4566', 'PCAB project registration', and 'contractor accreditation' each appeared in **zero** PA files as dedicated workflow headers for BuildRight's *own* license; every existing PCAB reference verifies *someone else's* license (trade-pro customer W590 in VS-09.1/VS-43.1; vendor/contractor eligibility W162 in VS-11.2/VS-46.1; employee PCAB tracking VS-19.4) with no owner for BuildRight's own contractor-license lifecycle | **FILLED — VS-165** |
| 80 | **Regulatory License, Permit & Accreditation Portfolio Management** | ~205 large sites (200 stores + 4 DCs + HQ + off-site lockers/EV chargers) across the 5 entities hold a large, heterogeneous, constantly-renewing portfolio of regulatory authorizations (LGU business/mayor's permit, barangay clearance, BFP FSIC, DENR ECC/hazardous-waste generator, BIR registration + CAS permit + ATP, DTI-BPS, PCAB, PhilGEPS, FDA-adjacent/FPA/BPI, PEZA/BOI, SSS/PhilHealth/Pag-IBIG employer, DOLE OSH, LTO/LTFRB fleet, BSP agency, NPC registration) numbering in the **thousands** — a single lapsed LGU permit, BFP FSIC, or BIR registration can close a store or block sales | **New gap (Pass 20)** — 'license portfolio', 'permit portfolio', 'regulatory inventory', 'permit register', and 'centralized compliance calendar' each appeared in **zero** PA files as dedicated workflow headers (the 4 existing 'renewal tracking' headers — W1547/W1400/W4735/W2910 — are each a single-domain slice); each compliance domain owns its execution slice (VS-22/76/79/114/117/138/145/165/46/06) but no value stream owns the unified cross-domain register/calendar/dashboard (the VS-161 TPRM scattered-slice-consolidation pattern) | **FILLED — VS-166** |
| 81 | **Workforce Background Screening, Credentialing & Personnel Vetting** | ~6,757 employees with ~1,200–1,600 hires/yr at 15–20% turnover, ~10–20% contingent labor (security/janitorial/promodizers/agency per VS-98), ~800–1,000 vendors + 3PL/delivery personnel (VS-56/VS-110) entering sites, and executives — in a cash-and-inventory-rich, customer-facing, safety-sensitive environment (cashiers, forklift/drivers, paint/chemical handlers) where negligent-hiring (quasi-delict/Civil Code, DOLE) and insider-threat/fraud exposure is material | **New gap (Pass 20)** — 'background screening program', 'pre-employment screening', 'credentialing', and 'workforce vetting' each appeared in **zero** PA files as dedicated workflow headers for a cross-category program; the only existing screen is the single **contingent-worker** workflow W3223 in VS-98.2 (a slice analogous to how VS-161 TPRM unified the scattered supplier-risk slices) — employees are screened as a single onboarding step within VS-121, vendor drivers have license-only checks (W1400), and executive vetting is ad-hoc | **FILLED — VS-167** |
| 82 | **In-Store Audio, Ambient Media & Music Royalty Licensing** | Playing copyrighted sound recordings/musical works across 200 stores is a statutory licensing obligation under RA 8293 (Intellectual Property Code) administered by **FILSCAP** (Filipino Society of Composers, Authors and Publishers) and the international PRO/sound-recording societies (per-work statutory damages + injunction); background music + in-store digital signage + PA/paging + ambient scent are also a material opex line (commercial music service + royalty + equipment + content across ~205 sites), a proven footfall/dwell/basket lever, and a brand-consistency and accessibility surface (RA 7394 price-integrity announcements, RA 7277/BP 344) | **New gap (Pass 21)** — 'music licensing', 'FILSCAP', 'background music', 'in-store audio', and 'ambient media' each appeared in **zero** PA files as dedicated workflow headers (only one incidental 'FILSCAP' system-list mention in VS-07.1 and a PA-announcement *step* embedded inside store daily management) — VS-14 owns brand/campaign/PR, VS-07 embeds one PA step, VS-48 sells vendor-paid retail-media ads, VS-138 maintains the building, VS-27 runs the network — none owned the ambient-media operating model (royalty program, music programming, PA protocol, signage content, scent, AV lifecycle, analytics) | **FILLED — VS-168** |
| 83 | **Employee Uniform, Workwear & PPE-Issuance Program** | The group outfits ~6,757 employees plus ~10–20% contingent/vendor personnel in branded uniform/workwear and issues role-specific PPE to a large safety-sensitive population (lumber-yard/forklift operators, paint/chemical handlers, DC manual handlers, cutting-station staff, delivery drivers) inside a customer-facing environment — a material opex line (~PHP 20–55M/yr across allowance + laundering + PPE), a proven CX/brand-consistency lever across 200 stores, and a DOLE-OSH legal obligation (missing/worn PPE → injury + officer personal liability) | **New gap (Pass 21)** — 'uniform program', 'workwear program', 'PPE issuance program', 'uniform allowance', and 'industrial laundering' each appeared in **zero** PA files as dedicated workflow headers ('uniform' referenced incidentally across ~29 PA files with no owner) — VS-19 issues one onboarding kit as a step, VS-24 *requires* PPE, VS-102 may carry an allowance, VS-98 governs the contingent worker, VS-34 buys transactionally — none owned the unified uniform/workwear/PPE operating model (standards, branded-apparel sourcing, PPE issuance/fit/laundering, sizing, damage/loss, role-change & separation return, multi-entity, sustainability, analytics) | **FILLED — VS-169** |
| 84 | **Inventory Pledge, Asset-Based Lending (ABL) & Trust-Receipt (Warehouse-Receipt) Financing** | BuildRight carries ~PHP 37B of merchandise inventory at cost (its largest balance-sheet asset), ~40% of COGS imported (~PHP 17–18B/yr; ~400–600 import TEUs/month), ~5,200 trade + ~200 corporate accounts + a COD-heavy ecommerce AR base, and operates across 5 entities; inventory + AR are the natural collateral for the revolving facilities and import lines that fund the 45–90-day cash-conversion cycle. The *collateral operations* that sustain those facilities — the borrowing-base certificate, field exams, eligible-inventory/AR analysis, advance rates, and **trust-receipt financing under PD 115 (the dominant Philippine import-financing instrument, where misuse is a criminal matter)** — directly govern availability, cost, covenant compliance, and the risk of over-advance, true-down, a frozen borrowing base, or PD 115 trust-receipt violation | **New gap (Pass 22)** — 'borrowing base', 'asset-based lending', 'trust receipt', 'trust-receipt financing', 'field warehouse', and 'notional pool' each appeared in **zero** PA files; adjacent coverage was only the single treasury workflow **W319** (debt facility & covenant compliance in VS-18.1 — owns the *facility contract*, not the *collateral operations* beneath it) plus the import-LC settlement **W232** and demurrage **W249** in VS-15.1/VS-02.2 — no value stream owned the *inventory-pledge / ABL borrowing-base / trust-receipt / warehouse-receipt collateral-operations discipline* | **FILLED — VS-170** |
| 85 | **Customer Pickup, Loading Zone & Will-Call Counter Operations** | ~55% of revenue is B2C walk-in and the big-box format sells bulky jobsite-bound merchandise (lumber 14%, tiles 12%, appliances 5%, furniture 5%) that customers take home same-day — customer self-pickup of bulky goods is a primary fulfillment channel, but it places **forklifts and reach equipment in shared customer-vehicle areas**, requires staging/appointment throughput at the loading bay, and is one of BuildRight's highest customer-premises-liability exposures (load shift, forklift contact, falling cargo, pedestrian conflict — links VS-147); at 2.8M monthly POS transactions with a meaningful bulky-pickup share across 200 stores, loading-bay/will-call friction converts completed sales into abandoned baskets, complaints, and returns | **New gap (Pass 22)** — a scattered-slice consolidation (the VS-161 TPRM / VS-166 license-portfolio pattern): the capability existed only as the single **W1193** (Heavy & Bulky Material Customer Pickup Scheduling & Loading Bay Priority Management) buried in **VS-07.3 Store Receiving & Replenishment**, plus **W773** (Store-Level Customer Hold & Will-Call Order Management) in **VS-09.3** and **W4805** (Customer Pickup Journey) in **VS-164.2** — no value stream owned the end-to-end *customer bulky-pickup, loading-bay, and will-call counter operating model* | **FILLED — VS-171** |
| 86 | **Third-Party Installer & Contractor Network (Pro-Referral) Management** | BuildRight's 'Your Home Building Partner' positioning and ~55% B2C revenue mean many homeowners/small contractors buy materials but lack the trade skill, license, or capacity to install them, and project non-completion drives basket abandonment and returns — a vetted third-party installer/contractor network and customer 'Find-a-Pro' referral (a recognized big-box discipline) directly lifts basket size, conversion, project completion, and attach (financing VS-154, design VS-66); a mis-managed referral (unlicensed/uninsured installer, shoddy work) damages the brand, creates selection/vicarious liability, and triggers complaints and warranty disputes | **New gap (Pass 22)** — a single-workflow elevation (the Pass 1/5/7/8/10/11 pattern): the only dedicated workflow was the single **W1472** (Trade Account Referral Program, Contractor Network Development & Lead Tracking) in **VS-11.1**, which tracks the trade-account side but not the end-to-end installer-network & pro-referral operating model; 'contractor network' appeared in 7 PA files, 'installer network' in 2, 'preferred contractor'/'pro referral' in 0–1 — no value stream owned the *third-party installer network & customer-referral program* (vetting, matchmaking, referral economics, performance, warranty, license monitoring) | **FILLED — VS-172** |
| 87 | **Investor Relations, Capital Markets & Securities Disclosure** | BuildRight is a ~PHP 62.3B-revenue holding group operating across 5 legal entities with material institutional ownership, bank/debt and capital-markets counterparties (links VS-170 ABL / VS-18 treasury), a credit-rating posture that sets borrowing cost across every facility, ESG-rated investors (links VS-25), and securities-law obligations under RA 8799 (the Securities Regulation Code) on insider-trading, selective-disclosure and related-party reporting — and it holds an Annual Stockholders' Meeting, pays dividends, files statutory SEC disclosures, and maintains a share register/cap table — yet no value stream owned the shareholder-, analyst- and market-facing communications & disclosure program that sustains the equity story, valuation, cost of capital and securities-law compliance | **New gap (Pass 23)** — 'investor relations', 'SEC reporting', 'SEC filing', 'securities disclosure', 'equity story', 'capital markets narrative', 'sell-side analyst', 'credit rating agency', 'proxy statement', and 'cap table' each appeared in **zero** PA files as dedicated workflow headers; the only adjacent coverage was scattered single-workflow slices — **W327** (dividend *payment* in VS-18.1, not the dividend *program*), **W482** (ASHM *logistics* in VS-17.1, not investor/proxy content), **W4684** (AGM *security* in VS-159), **W4524** (foundation *annual report* in VS-152), and **W3373** (policy/industry *analyst* relations in VS-104) — the VS-161 TPRM / VS-166 license-portfolio scattered-slice-consolidation pattern | **FILLED — VS-173** |
| 88 | **Self-Storage, Portable Container & Mobile-Storage Operations** | BuildRight operates ~205 large parking-rich sites and serves a customer base for whom storage is a *direct consequence of the purchase* — a homeowner renovating a kitchen (VS-143), a contractor staging materials/tools for a multi-week jobsite (VS-77), a trade pro between projects, or a disaster-affected household (VS-69); self-storage is one of the highest-margin recurring-revenue businesses in retail real estate (90%+ occupancy, ~PHP 1,500–4,000/month per unit), and portable/mobile (PODS-style) storage extends it to the doorstep — at ~50 stores × ~80 units + a ~200-container fleet it is a multi-hundred-million-PHP recurring stream that also lifts large-item attach (VS-143/VS-162), basket, and dwell; ungoverned it leaks value through mispriced/under-occupied units, delinquency, security/theft loss, fire/life-safety exposure, and abandoned-unit legal liability | **New gap (Pass 24)** — 'self-storage', 'storage unit', 'portable storage', 'mobile storage', 'storage container', 'storage rental', 'storage lien', and 'storage lease' each appeared in **zero** PA files as dedicated workflow headers and in **zero** VS directory names; adjacent coverage was only conflated slices (VS-04 merchandise warehousing; VS-77 jobsite staging; VS-164 small-parcel lockers; VS-111 BuildRight's own pallets; VS-97 the store/DC portfolio; VS-162 vehicle rental) — no value stream owned the *customer storage-rental operating model* | **FILLED — VS-174** |
| 89 | **Propane, LPG Cylinder Exchange & Gas Refill Operations** | BuildRight sells the appliances/equipment that consume propane/LPG — BBQ/patio grills, patio heaters, camping stoves, plumbing/brazing torches, and LPG forklifts — and the Philippines is one of the world's largest LPG markets, so cylinder exchange (the full-for-empty 'Blue Rhino' model) and customer-owned-cylinder refill are recognized high-velocity recurring big-box services; at ~50–100 exchanges/store/week across 200 stores plus a forklift/bulk-account base it moves hundreds of thousands of cylinders/yr with material deposit-float and a returnable-cylinder pool worth tens of millions of pesos — and LPG is a **flammable gas stored under pressure** carrying acute fire/explosion, OSH (DOLE), BFP Fire Code, DOE retailer-accreditation, DTI-BPS cylinder-standard (RA 11592), DENR and LGU exposure | **New gap (Pass 24)** — 'propane', 'LPG', 'cylinder exchange', 'gas refill', 'LP gas', 'cylinder fleet', and 'cylinder deposit' each appeared in **zero** PA files as dedicated workflow headers and in **zero** VS directory names; the only adjacent reference was the single **W1063** (Store-Level Customer Welding Gas Cylinder Exchange & Refill Service) buried in **VS-09.1** covering *industrial welding gas* for the fabrication counter, not the consumer/retail LPG program — no value stream owned the *LPG cylinder-exchange & refill operating model* (supply, returnable cylinder fleet, BFP-rated cage, exchange/refill transaction, deposit float, safety program) | **FILLED — VS-175** |
| 90 | **Blueprint, Reprographics & Large-Format Plan Printing Services** | ~40% of BuildRight's revenue is B2B (trade, project, government) and the professionals who buy from it — contractors, architects, engineers, developers, LGU/project buyers — live in large-format drawings (site/floor/structural/electrical/plumbing plans, shop drawings, bid sets, permit sets, as-builts); large-format plan printing/scanning/copying (reprographics) is a recognized contractor-facing in-store service that supports the 'Your Home Building Partner' positioning and design/pro capabilities (VS-66/VS-43/VS-46/VS-140), is margin-accretive and dwell/attach-driving, and carries copyright/IP and RA 10173 document-confidentiality exposure (client plans, signed docs, sealed government bids) | **New gap (Pass 24)** — 'blueprint', 'reprographics', 'large-format printing', 'plan printing', 'plotter', 'engineering print', 'plan copying', and 'plan scanning' each appeared in **zero** PA files as dedicated workflow headers and in **zero** VS directory names; adjacent coverage was only conflated (VS-66 *creates* designs; VS-14 produces BuildRight's *own* promo print; VS-09 covers *physical* custom fabrication; VS-46/VS-11 consume plan-room/bid-set needs as a step) — no value stream owned the *reprographics service operating model* (equipment fleet, consumables, job lifecycle, file/IP/confidentiality controls, cost/quality analytics) | **FILLED — VS-176** |
| 91 | **Field Retail Operations, Regional/District Management & Multi-Store Retail Execution Network** | BuildRight runs **200 stores across six Philippine regions** (Mindanao 60, Visayas 40, Luzon-outside-NCR 50, Metro Manila 30, North/Central Luzon 20) staffed by ~5,800 store personnel, growing 10–15 stores/year, with a documented HQ "Store Operations" department of ~24 regional managers / operations-standards / facilities-coordination staff and 20 Regional LP officers (profile §3.3, §4); at that footprint the field layer — regional/district managers each overseeing ~40–50 stores, running a monthly store-visit cadence, coaching store managers, enforcing retail standards, diagnosing underperformers, stabilizing new stores, and operating the store-operations support center — is the single controllable lever on comp-sales growth, format relevance, standardized CX, and the consistent field execution of every HQ program (merch resets, promotions, new-product rollouts, remodels, compliance mandates) | **New gap (Pass 25)** — a single-workflow-elevation + scattered-slice-consolidation candidate (the combined Pass-1/5/7/8/10/11/22/23 and VS-161/166/171 patterns): the Regional Manager role already appears as the accountable/informed party across **~66 PA files** (VS-07 daily mgmt/delay-incident/delivery review, VS-37 opening, VS-109 remodel, VS-146 mystery-shopping remediation) yet the field-management discipline existed only as the scattered single workflows **W1030** (Multi-Store District Manager Weekly Review in VS-07.1), **W2369** (Regional Operations Follow-Up in VS-63.2), **W3836** (Sales Coaching/Field Enablement in VS-124), and **W1214** (Store Performance Scorecard Weekly Review & Regional Benchmarking); the defining terms 'field retail', 'field operations', 'field execution', 'retail execution', 'multi-store management', 'store operations support', 'store support center', 'store hotline', 'store escalation', 'store operations center', 'district manager', 'field coach', 'store turnaround', and 'new-store stabilization' each appeared in **zero** PA files as dedicated workflow headers — no value stream owned the *field-management operating model* (distinct from VS-07 single-store ops, VS-33 strategy, VS-63 HQ→store broadcast, VS-146 independent assurance) | **FILLED — VS-177** |
| 92 | **Landbanking, Site Acquisition & Agrarian/LGU Zoning Conversion Operations** | Store footprint expansion of 10-15 stores/year requires title consolidation, land use reclassification, DAR conversion orders, and NCIP clearances in provincial Philippines | None; VS-20 covers only leasing/construction, and VS-97 landlord property operations, leaving landbanking completely unowned | **FILLED — VS-178** |
| 93 | **Extended Producer Responsibility (EPR) Compliance & Plastic Recovery Network** | Statutory compliance under RA 11898 (EPR Act) requiring 20% to 80% plastic recovery/recycling, audits, NSWMC registrations, and cement-kiln co-processing | Basic store waste covered in VS-73, pallets in VS-111, but no end-to-end statutory compliance program | **FILLED — VS-179** |
| 94 | **Disaster Relief Supply Chain Logistics & Humanitarian Aid Coordination** | The Philippines faces ~20 typhoons/yr. BuildRight must allocate emergency building materials, stage relief kits, enforce DTI calamity price freezes, and coordinate relief routes | Store-level safety and BCP covered in VS-69, but outbound relief logistics and pricing compliance was completely unowned | **FILLED — VS-180** |
| 95 | **B2B Project Financing, Escrow Account Orchestration & Lien Release** | B2B accounts represent ~40% of sales. Developer bank-escrow releases depend on Joint Quantity Surveys, draw packages, tripartite agreements, and progressive lien waivers | Transactional billing in VS-11, consumer credit in VS-154, but no developer escrow or lien management program | **FILLED — VS-181** |
| 96 | **B2B Bulk-Project Custom Import (Indent Sourcing & Brokerage Operations)** | ~40% of revenue is B2B; developers and contractors routinely need bulk custom materials (custom marble layouts, high-spec structural steel, project-specific elevators) that cannot be stocked in standard retail inventory; the indent-import lifecycle (factory identification/vetting, LC and bank trust-receipt coordination, port-to-jobsite devanning, joint quantity survey, progressive milestone billing, landed-cost reconciliation) optimizes working capital and freight | **New gap (Pass 27)** — 'indent order', 'indent sourcing', 'port-to-jobsite', and 'custom import brokerage' each appeared in **zero** PA files as dedicated workflow headers. VS-03 (catalog vendor POs), VS-87 (customs compliance), VS-02 (import planning) cover adjacent ground but none owned the bespoke indent-import operating model | **FILLED — VS-182** |
| 97 | **Dual Training System (DTS) & TESDA Partnership Program** | With 6,757 employees, frontline technical expertise (paint mixing, tools, logistics) is a core brand differentiator; the DTS under RA 7686 builds a certified capability pipeline while claiming a 50% training-expense tax deduction and stabilizing turnover | **New gap (Pass 27)** — 'dual training system', 'DTS', 'TESDA partnership', and 'RA 7686' each appeared in **zero** PA files as dedicated workflow headers. VS-19.4 (general L&D) and VS-123 (skilled-trade apprenticeship) cover adjacent ground but none owned the statutory DTS/TESDA partnership operating model | **FILLED — VS-183** |
| 98 | **Post-Disaster Store Infrastructure Reconstruction & Rehabilitation** | 200 stores across an archipelago exposed to ~20 typhoons/year plus seismic activity make structural resilience and rapid rehabilitation critical; owns the medium-to-long-term recovery lifecycle (damage survey, insurance/adjuster coordination, CAPA engineering, contractor mobilization, BFP/LGU re-certification, temporary container-sales office, utility restoration, handover) and optimizes insurance recoveries | **New gap (Pass 27)** — 'post-disaster reconstruction', 'structural rehabilitation', and 'building reconstruction' each appeared in **zero** PA files as dedicated workflow headers. VS-69 (typhoon active response), VS-20 (new-build construction), VS-26 (BCP/insurance) cover adjacent ground but none owned the post-calamity reconstruction operating model | **FILLED — VS-184** |
| 99 | **B2B Cooperative Credit & Procurement Partnerships** | With 170 stores outside Metro Manila, cooperatives (agricultural, consumer, credit) represent massive economic groups; structured credit and joint procurement partnerships drive large-ticket provincial purchasing (warehouses, dryers, community facilities) and secure highly loyal cohorts | **New gap (Pass 27)** — 'cooperative credit', 'cooperative procurement partnership', and 'CDA cooperative onboarding' each appeared in **zero** PA files as dedicated workflow headers. VS-94 (cooperative as supplier), VS-82 (sari-sari/MSME micro-wholesale), VS-68 (trade credit risk) cover adjacent ground but none owned BuildRight as a *creditor and procurement partner* to cooperatives | **FILLED — VS-185** |
| 100 | **Compact & Heavy Construction Equipment Rental Fleet Operations** | ~40% B2B trade/project revenue and a large lumber/building-materials & tool assortment; contractors routinely need to rent compact/heavy equipment (mini-excavators, concrete mixers/pumps, boom/scissor lifts, plate compactors/breakers, generators, light towers, air compressors) by the day/week — a recognized big-box discipline (the “Home Depot Rentals” model) that converts “I can't do this job without a machine” basket abandonment into a completed sale | **New gap (Pass 28)** — the discipline was scattered as single steps: VS-12.2 (W139 “Tool & Equipment Rental”, scoped to Bosch/Makita/DeWalt/Hilti *power tools*), W1062 (scaffolding rental in VS-09), W1094 (construction-equipment *partner brokerage*, not an owned fleet), W1156 (safety-equipment rental). 'heavy equipment rental', 'construction equipment fleet', 'compact excavator rental', and 'scissor/boom lift rental' each appeared in **zero** PA files as dedicated workflow headers for a BuildRight-owned heavy/compact equipment fleet — no value stream owned the heavy-equipment rental-fleet operating model (distinct from VS-12.2 tool rental, VS-162 truck rental, VS-96 multi-year leasing, and VS-175 propane) | **FILLED — VS-186** |
| 101 | **Household Hazardous Waste, Paint & Used-Product Stewardship Take-Back Program** | Paint is ~8% of the assortment (~2,800 SKUs) and the catalog also sells used-oil-generating lubricants, lead-acid & lithium batteries, fluorescent/CFL/mercury lamps, pesticides/garden chemicals, solvents, and e-waste — all DENR-EMB-regulated hazardous waste (RA 6969, RA 8749, RA 9275) for which a retailer take-back/stewardship program (the PaintCare / Call2Recycle / lamp-&-battery model) diverts from landfill, satisfies cradle-to-grave obligations, strengthens ESG, drives footfall, and recovers reblended-paint/scrap value | **New gap (Pass 28)** — 'paint take-back', 'paint stewardship', 'household hazardous waste', 'used oil collection', 'battery take-back', 'fluorescent/CFL take-back', and 'product stewardship' each appeared in **zero** PA files as dedicated workflow headers. VS-73 is store *operational* waste, VS-179 (EPR) is scoped to *plastic* packaging, VS-114 is DG *transport*, VS-25 is ESG *reporting* — no value stream owned the customer take-back/stewardship operating model | **FILLED — VS-187** |
| 102 | **Trade Reseller Floor-Plan & Dealer Inventory Financing** | BuildRight is a wholesaler to its trade base (~5,000 trade accounts incl. sari-sari/MSME per VS-82 and cooperatives per VS-94/VS-185), and ~40% of revenue is B2B — a base for whom inventory purchase is the binding constraint on growth; a floor-plan program (the manufacturer/wholesaler-finances-dealer-inventory model used in autos/equipment/building materials) releases that constraint, lifts wholesale volume, and earns financing margin | **New gap (Pass 28)** — 'floor plan', 'dealer financing', 'inventory financing', and 'reseller financing' each appeared in **zero** PA files as dedicated workflow headers. VS-105 is supply-chain finance on BuildRight's *own payables*, VS-170 is BuildRight's *own* inventory pledged as ABL collateral, VS-38 is consumer credit, VS-154 is home-loan brokerage, VS-181 is B2B project escrow — no value stream owned BuildRight as a floor-plan/dealer-inventory lender | **FILLED — VS-188** |
| 103 | **Trade Accounts Receivable Factoring, Invoice Discounting & Receivables Securitization** | At ~40% B2B revenue (~PHP 25B/yr), ~5,200 trade accounts, Net 30–90 terms, and a COD/ecommerce AR base, trade receivables are BuildRight's second-largest balance-sheet asset after inventory; factoring/discounting/securitization releases that working capital immediately, diversifies funding, and can transfer customer credit risk | **New gap (Pass 28)** — 'factoring', 'invoice discounting', 'receivable sale', and 'securitization' each appeared in **zero** PA files as dedicated workflow headers (the lone 'securitization' reference was W3181 *lease-portfolio* securitization in VS-96). VS-105 is reverse factoring on BuildRight's *payables*, VS-170 is AR *pledged as collateral* (not sold), VS-18 is cash ops — no value stream owned BuildRight as a *seller* of its own trade receivables | **FILLED — VS-189** |
| 104 | **Operational Technology (OT) / ICS Cybersecurity & Retail Technology Asset Protection** | BuildRight operates a vast, safety-coupled OT estate across ~205 sites — 600 POS terminals (VS-08), WMS/RF at 4 DCs (VS-04), BMS/fire/life-safety/access-control panels (VS-138), standby generators & fuel systems, SCADA on the rooftop-solar prosumer plant (VS-108), EV-charging controllers (VS-163), smart-locker & SCO controllers (VS-164/VS-149), CCTV/EAS (VS-23), paint-mixing & cutting-station PLCs, lumber-yard automation, weighbridges, and IoT sensors (VS-69) — where a compromised fire panel, suppressed alarm, BMS lockout, or POS/SCO ransomware has direct safety-of-life, store-closure, and cash/revenue consequences that corporate IT controls do not address; OT cannot be patched on IT cadences and is increasingly converged with the corporate network | **New gap (Pass 29)** — 'operational technology security', 'OT cybersecurity', 'ICS security', 'SCADA security', 'building automation security', 'OT network segmentation', 'OT incident response', 'IEC 62443', and 'NIST SP 800-82' each appeared in **zero** PA files as dedicated workflow headers (the lone SCADA reference is the *generation-operations* workflow W3457 in VS-108, not a security discipline); VS-27.3 owns IT cybersecurity, VS-138 operates the BMS, VS-163/VS-164/VS-149 operate their connected-device channels, VS-115 calibrates measurement devices — no value stream owned the *cross-domain OT/ICS cybersecurity operating discipline* | **FILLED — VS-190** |
| 105 | **Customer Construction Debris, Demolition Waste & Site Cleanup Operations** | BuildRight's 'Your Home Building Partner' positioning and ~45% B2B + B2C project revenue mean it routinely performs work that generates jobsite debris (drywall, tile/masonry rubble, lumber offcuts, concrete/cement debris, metal/pipe scraps, roofing, packaging) via installation (VS-12), customer design-build (VS-66), bulky white-goods install (VS-143), solar installation (VS-70), equipment rental return (VS-186), and disaster-recovery repair (VS-184); ungoverned this stream creates illegal-dumping liability under RA 9003/RA 6969, raises the ESG/circular-economy footprint (VS-25/VS-73/VS-179), and forfeits scrap/reprocessing recovery value | **New gap (Pass 29)** — a single-workflow elevation (the Pass-1/5/7/8/10/11/22/23/25 pattern): the only dedicated workflow was the single **W1086** (Customer Construction Waste Disposal & Skip/Dumpster Rental Coordination in VS-09.1); 'construction debris hauling', 'demolition waste', 'site cleanup', and 'C&D diversion' each appeared in **zero** PA files as dedicated workflow headers except W1086. VS-73 (store's own waste), VS-187 (household hazmat take-back at the store counter), VS-143.3 (old-appliance haul-away), VS-111 (own inbound packaging/RTI), VS-179 (EPR plastic packaging), VS-90 (transit damage claims) cover adjacent ground but none owned the *customer jobsite debris hauling & site cleanup service* | **FILLED — VS-191** |
| 106 | **Green Fleet Transition, Electric Vehicle (EV) Fleet Operations & Sustainable Transportation** | The Philippines' Electric Vehicle Industry Development Act (RA 11697 / EVIDA, 2022) and its IRR establish a national EV roadmap that explicitly includes commercial/fleet adoption, corporate fleet EV-share expectations, and building/Parking-Space EV-readiness provisions that interact with BuildRight's EV-charging host network (VS-163) and rooftop-solar prosumer program (VS-108); at ~5,000 monthly store-replenishment orders, ~42,900 ecommerce orders/month, 10–15 new stores/yr, and ~6,757 employees across a 200-store archipelago, transportation is a material Scope 1 emissions and operating-cost line, and a structured green-fleet transition (electrification/alt-fuel roadmap, EV procurement & homologation, depot charging & grid coordination, TCO/lifecycle, RA 11697 EVIDA incentives, charging operations & smart-load, battery SoH/lifecycle, eco-driving, range-aware dispatch, charging–renewable integration, EV maintenance/roadside, GHG MRV, DOE/LTO/LTFRB compliance, HV/battery-fire safety, 3PL green clauses, charging billing, battery second-life/recycling) is the primary lever on both the ESG decarbonization commitment (VS-25) and the 12–14% EBITDA target | **New gap (Pass 30)** — 'fleet electrification', 'electric fleet', 'EV fleet', 'green fleet', and 'fleet decarbonization' each appeared in **zero** PA files as dedicated workflow headers, with only a forward-pointer inside VS-163 PA-163.1 step 1 ("BuildRight's own EV-fleet charging need (VS-06/VS-61 green-fleet transition)") and a single VS-25.3 ESG-reporting example mention; VS-06 operates the current diesel fleet, VS-61 owns diesel fuel/cost, VS-163 hosts customer EV charging, VS-108 generates own solar, VS-25 reports the footprint — none owned BuildRight's own *fleet decarbonization transition program* | **FILLED — VS-192** |

### Pass 30 (W5465–W5488) — One new value stream

Pass 30 adds one further genuinely-unowned operational discipline surfaced by re-running the established gap methodology after twenty-nine prior passes had been judged complete. It is genuinely uncovered and was in fact self-acknowledged as a forward-referenced need inside VS-163 without an owning value stream:

- **VS-192 (Green Fleet Transition, Electric Vehicle (EV) Fleet Operations & Sustainable Transportation)**: Adds 3 process areas and 24 workflows (W5465–W5488) under the Make & Move family to own the multi-year decarbonization of BuildRight's own goods-moving and service fleet — the ~20% owned share of the outbound-distribution fleet (VS-06), the customer self-haul rental fleet (VS-162), the heavy/compact equipment rental fleet (VS-186), the contractor jobsite-delivery fleet (VS-74), and the employee shuttle fleet (VS-141) — plus the charging/alternative-fuel infrastructure, route-network redesign, and EVIDA/DOE/LTO compliance the transition requires (green-fleet strategy & emissions baseline, asset inventory & electrification-readiness, EV/alt-fuel procurement & homologation, depot/DC charging & grid coordination, TCO/lifecycle, RA 11697 EVIDA incentives & registration, capital governance, route re-design, daily charging & smart-load, charger O&M, battery SoH/lifecycle, eco-driving & telematics, range-aware dispatch, alt-fuel operations, charging–renewable integration, EV maintenance/roadside, GHG MRV, DOE/LTO/LTFRB compliance, HV/battery-fire safety, driver/technician training, 3PL green clauses, charging billing, battery second-life/recycling, performance analytics). Genuinely uncovered: 'fleet electrification', 'electric fleet', 'EV fleet', 'green fleet', and 'fleet decarbonization' each appeared in **zero** PA files as dedicated workflow headers, with only a forward-pointer inside VS-163 PA-163.1 step 1 — *"BuildRight's own EV-fleet charging need (VS-06/VS-61 green-fleet transition)"* — explicitly acknowledging the gap and the owner that did not yet exist, plus a single VS-25.3 ESG-reporting example mention. Distinct from VS-06 (operates the current diesel fleet — this transitions it), VS-61 (diesel fuel/cost — this owns electricity/alt-fuel energy), VS-163 (hosts EV charging for *customers* — this owns charging for BuildRight's *own* fleet, though the two share infrastructure), VS-108 (own-generation solar — this matches fleet charging load to it), VS-141 (employee shuttles — this decarbonizes them), and VS-25 (reports the footprint — this reduces it).

The pass strengthens one family (Make & Move +24 via VS-192). The 24 new workflows are **unclassified** and carry a keyword-driven proposed tier in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) (regenerated via `07-methodology/classify-workflows.py`), exactly as prior batches; they will be confirmed into the register during a follow-up criticality review. Several Pass 30 workflows are anticipated Tier 1 (RA 11697 EVIDA registration/incentive and DOE/LTO/LTFRB franchise/inspection compliance controls, BFP Fire-Code/lithium-battery-fire and DOLE-OSH HV-work-permit controls, and GHG-MRV/greenwashing-disclosure-integrity controls).

### Pass 26 (W5129–W5224) — Four new value streams

Pass 26 is a comprehensive pass designed to add four key operational capabilities highly relevant to the model company's business model and the Philippine regulatory context. These are added as Business-As-Usual (BAU) value streams:

- **VS-178 (Landbanking, Site Acquisition & Agrarian/LGU Zoning Conversion Operations)**: Adds 3 process areas and 24 workflows (W5129–W5152) under the Asset & Infrastructure family to govern store-footprint property acquisition, title consolidation, DAR land use conversions, and NCIP clearances.
- **VS-179 (Extended Producer Responsibility (EPR) Compliance & Plastic Recovery Network)**: Adds 3 process areas and 24 workflows (W5153–W5176) under the Governance & Assurance family to manage statutory compliance under the EPR Act of 2022 (RA 11898), including plastic audits, PRO coordination, recovery operations, and NSWMC filings.
- **VS-180 (Disaster Relief Supply Chain Logistics & Humanitarian Aid Coordination)**: Adds 3 process areas and 24 workflows (W5177–W5200) under the Make & Move family to manage emergency material staging, DTI price freeze lockups under a State of Calamity, and NGO/DSWD relief logistics routing.
- **VS-181 (B2B Project Financing, Escrow Account Orchestration & Lien Release)**: Adds 3 process areas and 24 workflows (W5201–W5224) under the Finance family to manage commercial developer bank-escrow draws, Joint Quantity Surveys, and progressive material lien waivers.

### Pass 27 (W5225–W5320) — Four new value streams

Pass 27 adds four further operational capabilities as Business-As-Usual (BAU) value streams, extending the catalog to cover custom import brokerage, vocational training partnerships, post-disaster reconstruction, and cooperative wholesale credit. Each was confirmed genuinely unowned (defining terms in **zero** or near-zero PA files as dedicated workflow headers and no dedicated owner) and scoped to be distinct from adjacent covered capabilities (documented in the §3 rows 96–99 and each VS README):

- **VS-182 (B2B Bulk-Project Custom Import, Indent Sourcing & Brokerage Operations)**: Adds 3 process areas and 24 workflows (W5225–W5248) under the Plan & Source family to own the custom project-specific overseas procurement and logistics lifecycle for large B2B/developer clients — indent contract execution, LC opening and bank trust-receipt coordination, pre-shipment inspection, direct port-to-jobsite container devanning, joint quantity surveys, progressive milestone billing, and landed-cost reconciliation.
- **VS-183 (Dual Training System (DTS) & TESDA Partnership Program)**: Adds 3 process areas and 24 workflows (W5249–W5272) under the People family to own the structured vocational recruitment, training, and store/DC placement model under RA 7686 — TVI partner accreditation, TESDA training-plan design, student-trainee placement, biometric time logging, stipend disbursement, BIR 50% training-expense deduction filing, competency certification, and transition-to-hire.
- **VS-184 (Post-Disaster Store Infrastructure Reconstruction & Rehabilitation)**: Adds 3 process areas and 24 workflows (W5273–W5296) under the Asset & Infrastructure family to own the medium-to-long-term recovery lifecycle for stores/DCs hit by typhoon, earthquake, or fire — damage surveys and geodetic hazard mapping, insurance claim coordination and loss-adjuster audit, CAPA engineering budget approval, contractor mobilization and site safety fencing, BFP/LGU structural re-certification, temporary container-sales-office setup, utility restoration, and site handover.
- **VS-185 (B2B Cooperative Credit & Procurement Partnerships)**: Adds 3 process areas and 24 workflows (W5297–W5320) under the Sell & Serve family to own the wholesale credit and purchasing relationship with cooperative societies (agricultural, consumer, credit cooperatives) — onboarding and board-resolution review, CDA clearance checking, group credit-limit allocation, member verification at POS, purchase tracking, quarterly rebate settlement, and joint community procurement.

The pass strengthens four families (Plan & Source +24 via VS-182; People +24 via VS-183; Asset & Infrastructure +24 via VS-184; Sell & Serve +24 via VS-185). The 96 new workflows are **unclassified** and carry a keyword-driven proposed tier in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md), exactly as prior batches.

### Pass 28 (W5321–W5416) — Four new value streams

Pass 28 adds four further genuinely-unowned operational capabilities surfaced by re-running the established gap methodology (defining terms in **zero** PA files as dedicated workflow headers and in **zero** VS directory names, no dedicated owner, conflated with adjacent covered coverage or reduced to scattered single-workflow slices) after twenty-seven prior passes had been judged complete. Each is distinct from its adjacent covered capabilities (documented in the §3 rows 100–103 and each VS README):

- **VS-186 (Compact & Heavy Construction Equipment Rental Fleet Operations)**: Adds 3 process areas and 24 workflows (W5321–W5344) under the Sell & Serve family to operate BuildRight's *owned* short-term rental fleet of compact/heavy construction equipment (mini-excavators, concrete mixers/pumps, boom/scissor lifts, plate compactors/breakers, generators, light towers, air compressors). A scattered-slice consolidation (the VS-161/171 pattern): the discipline existed only across VS-12.2 *tool* rental (W139), the single scaffolding workflow W1062, and the construction-equipment *brokerage* workflow W1094 — no value stream owned the heavy-equipment own-fleet operating model.
- **VS-187 (Household Hazardous Waste, Paint & Used-Product Stewardship Take-Back Program)**: Adds 3 process areas and 24 workflows (W5345–W5368) under the Governance & Assurance family to own the customer-facing take-back of leftover paint, used oil, batteries, fluorescent/CFL lamps, pesticides/solvents, e-waste, and cylinders — with DENR-EMB (RA 6969) generator/TSD permitting, manifest chain-of-custody, recovery/reblending, and stewardship reporting. Genuinely uncovered: the defining terms appeared in **zero** PA files; VS-73 (store waste), VS-179 (plastic EPR), VS-114 (DG transport), and VS-25 (ESG reporting) cover adjacent ground but none owned the take-back/stewardship operating model.
- **VS-188 (Trade Reseller Floor-Plan & Dealer Inventory Financing)**: Adds 3 process areas and 24 workflows (W5369–W5392) under the Finance family to operate BuildRight as a floor-plan/dealer-inventory lender to its trade reseller base (origination, dual-payee disbursement, unit-level collateral, curtailment, OOT detection, workout/repossession, portfolio analytics, and BSP/SEC/Truth-in-Lending compliance). Genuinely uncovered: 'floor plan'/'dealer financing'/'inventory financing' each appeared in **zero** PA files; VS-105 (own-payables SCF), VS-170 (own-inventory ABL), VS-38 (consumer credit), VS-181 (B2B escrow) cover adjacent ground but none owned BuildRight as a floor-plan lender.
- **VS-189 (Trade Accounts Receivable Factoring, Invoice Discounting & Receivables Securitization)**: Adds 3 process areas and 24 workflows (W5393–W5416) under the Finance family to own BuildRight's sale of its own trade receivables (recourse/non-recourse factoring, invoice discounting, securitization) — eligible-receivable criteria, notification strategy, PFRS 9 true-sale/derecognition, lockbox/cash-application, recourse/buyback, and portfolio analytics. Genuinely uncovered: 'factoring'/'invoice discounting'/'receivable sale'/'securitization' each appeared in **zero** PA files (the lone 'securitization' reference was W3181 lease-portfolio in VS-96); VS-105 (payables reverse factoring), VS-170 (AR pledged as collateral, not sold), VS-18 (cash ops) cover adjacent ground but none owned BuildRight as a *seller* of its receivables.

The pass strengthens three families (Sell & Serve +24 via VS-186; Governance & Assurance +24 via VS-187; Finance +48 via VS-188 + VS-189). The 96 new workflows are **unclassified** and carry a keyword-driven proposed tier in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) (regenerated via `07-methodology/classify-workflows.py`), exactly as prior batches; they will be confirmed into the register during a follow-up criticality review. Several Pass 28 workflows are anticipated Tier 1 (DENR-EMB RA 6969 hazardous-waste permitting/manifest/cradle-to-grave and spill-response controls in VS-187; BSP/SEC/Truth-in-Lending RA 3765 disclosure and out-of-trust/floor-plan-default controls in VS-188/VS-189; LTO/LTFRB/DOLE-OSH equipment-certification availability-gating and CDW/insurance controls in VS-186).

### Pass 29 (W5417–W5464) — Two new value streams

Pass 29 adds two further genuinely-unowned operational capabilities surfaced by re-running the established gap methodology after twenty-eight prior passes had been judged complete. One is genuinely uncovered with **zero** dedicated workflow headers across the entire repository (VS-190); the other is a single-workflow elevation following the Pass-1/5/7/8/10/11/22/23/25 pattern (VS-191). Each is distinct from its adjacent covered capabilities (documented in §3 rows 104–105 and each VS README):

- **VS-190 (Operational Technology (OT) / ICS Cybersecurity & Retail Technology Asset Protection)**: Adds 3 process areas and 24 workflows (W5417–W5440) under the Technology & Data family to own the cross-domain cybersecurity program for the operational technology that physically runs stores, DCs, and energy/logistics assets (BMS, fire/life-safety, access control, CCTV/EAS, generators/fuel, SCADA solar, EV chargers, smart lockers, SCO, POS, WMS/RF, PLCs, IoT sensors) — OT asset inventory and Purdue-model IT/OT segmentation, OT-aware monitoring/detection/vulnerability/patch/incident-response with fail-secure safety-preserving procedures, OT third-party/vendor remote-access governance, OT cyber supply-chain/SBOM, and IEC 62443 / NIST SP 800-82 / BSP / NPC compliance. Genuinely uncovered: the defining terms ('operational technology security', 'OT cybersecurity', 'ICS security', 'SCADA security', 'IEC 62443', 'NIST SP 800-82') each appeared in **zero** PA files as dedicated workflow headers. Distinct from VS-27.3 (IT cybersecurity), VS-138 (operates the BMS — this secures it), VS-163/VS-164/VS-149 (operate their channels — this owns the cross-domain OT security program), VS-115 (calibrates devices — this secures their connected layer), VS-23 (operates CCTV/EAS — this defends the estate), VS-99 (asset lifecycle — this owns cyber-hardening), and VS-21.3/VS-26 (audit and insure the risk — this operates the controls).
- **VS-191 (Customer Construction Debris, Demolition Waste & Site Cleanup Operations)**: Adds 3 process areas and 24 workflows (W5441–W5464) under the Make & Move family to own the customer jobsite debris-hauling and post-installation/post-build site-cleanup service (service product design/pricing, volume/container estimation, pre-job hazard & regulated-material assessment, crew/container dispatch, on-site segregation & load-out, DENR-compliant C&D transporter permitting & manifest, multi-stream routing to recycler/MDRF/landfill, hazardous-discovery rerouting, site handover, diversion/settlement, and ESG/DENR/LGU reporting). A single-workflow elevation: the only dedicated workflow was the single **W1086** (Customer Construction Waste Disposal & Skip/Dumpster Rental Coordination in VS-09.1); 'construction debris hauling', 'demolition waste', 'site cleanup', and 'C&D diversion' each appeared in **zero** PA files as dedicated workflow headers except W1086. Distinct from VS-73 (store's own operational waste), VS-187 (household hazardous take-back at the store counter), VS-143.3 (old-appliance haul-away), VS-111 (own inbound packaging/RTI), VS-179 (EPR plastic packaging compliance), VS-90 (transit damage claims), and VS-109/VS-20 (debris from BuildRight's own store construction).

The pass strengthens two families (Technology & Data +24 via VS-190; Make & Move +24 via VS-191). The 48 new workflows are **unclassified** and carry a keyword-driven proposed tier in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md), exactly as prior batches; they will be confirmed into the register during a follow-up criticality review. Several Pass 29 workflows are anticipated Tier 1 (OT incident-response/fail-secure and IEC 62443/NIST 800-82 compliance and BSP/NPC/BFP regulator-notification controls in VS-190; DENR RA 6969/RA 9003 manifest and accredited-disposer and LGU hauling-permit and demolition-permit and ESG-reporting controls in VS-191).

### Candidate gaps considered but rejected (adequate coverage)

- **Strategic sourcing / RFP** — covered by VS-03 vendor management.
- **Loyalty / coalition partnerships** — covered by VS-13.
- **Tax compliance** — covered by VS-79 / VS-87.
- **Anti-counterfeit / product authentication** — covered by VS-71.
- **Trade credit / AR risk** — covered by VS-16 / VS-68.
- **Treasury / FX / intercompany** — covered by VS-18 / VS-72.
- **Energy & utilities management** — covered by VS-25.1 (W692/W1543) and VS-20.3 (W701/W1563).
- **B2B self-service portal** — covered (W936 portal referenced throughout VS-11/VS-16).
- **NPI / range / product lifecycle** — covered by VS-01.1 (assortment planning & product lifecycle).
- **Affiliate / influencer / referral marketing** — covered by VS-14.2 (W1351/W142/W1184/W1558).
- **In-store concessionaire / kiosk / vending** — covered by VS-07.1 (W177), extended 2026-08-25 by W5505–W5507 (batch 3: concession item catalog/barcode/label governance, concessionaire self-service price change with label-first propagation, concession service-fee billing).
- **Performance management / succession** — covered by VS-19.1 (W72/W178).
- **Software development lifecycle (SDLC)** — covered by VS-27.1 (W132).
- **Data governance / stewardship** — covered by VS-28.2 (W1177).
- **DIY how-to content / knowledge library** — covered by VS-09.1 (W1136) + VS-01.3 (W1346).
- **Refurbishment / open-box / liquidation** — covered by VS-32.3 (W1640) + VS-05.3 (W220).
- **Disaster/BCP / insurance** — covered by VS-26.
- **Field service / installation dispatch** — covered across VS-12 / VS-66 / VS-70 / VS-06 / VS-74.
- **Visual merchandising / display execution** — substantially covered across VS-55 (planogram/space, incl. W2168 cross-merchandising, W2177 endcap compliance, W2180 visual-standards audit, W2187 seasonal display rotation) and VS-62 (sample/display lifecycle, incl. W2347 vendor-funded display).
- **Corporate communications / PR / crisis comms** — covered by VS-14.3 (W134/W143/W1562).
- **Contact center / call-center operations** — covered by VS-13.1 (W258 omnichannel ticketing, W259 call-center daily ops, W597 escalation SLA, W1550 VOC).
- **Import trade finance / LC / freight forwarder** — covered by VS-02.2 (W144/W191/W249/W464/W1233/W1264) and VS-87.
- **Talent management / succession** — covered by VS-19.1 (W72/W178) and the EX/DEI workflows now in VS-103.
- **Property / facility maintenance (landlord-side)** — covered by VS-20.3 and VS-97.2.
- **IT change & release management** — covered by VS-27.1 (service management, W132 SDLC).
- **Continuous improvement / operations excellence** — covered across VS-30 (innovation/automation) and VS-21 (audit).

### Candidate gaps considered but rejected in Pass 6 (adequate coverage)

- **Lumber yard / bulk building materials operations** — covered by VS-07.1 (W1281 Lumber Yard Daily Operations & Inventory Management, W951 bulk material breaking, W1243 lumber grading) and W1488 bulk delivery.
- **Corporate travel, expense & P-card management** — covered by VS-34.3 Expense Monitoring & Control (W1686 Travel & Business Entertainment Expense Management + the corporate-card issuance/audit workflows).
- **Print, signage & POSM production & distribution** — covered by VS-14.1 Campaign Planning & Execution (W1270 Seasonal Promotional Catalog Production/Printing/Store Distribution, W1522 Monthly Flyer & Promotional Catalog, plus the in-store POS-material production/distribution step and W1313 vendor-supplied POP lifecycle).
- **Energy & utilities procurement & contract management** — covered by W111 (utility bill/consumption across ~205 accounts, in VS-07.2/VS-20.3), VS-108 (own generation), and VS-34 (procurement); explicitly noted as covered above.
- **Store fixtures / FF&E procurement** — absorbed into the new VS-109 remodel program (W3481) and VS-37 store opening, with VS-34/VS-03 for transactional procurement.

### Capabilities elevated from single workflows to dedicated value streams (Pass 5)

Pass 5 specifically targeted capabilities that existed only as a single workflow within another value stream (or were conflated with an adjacent covered one) and elevated each to its own end-to-end program — the same pattern used in Pass 1 (VS-89 Product Recall was elevated from the single customer-notification workflow W776 in VS-09):

- **Supply chain finance / dynamic discounting** — *previously* the single workflow W324 in VS-18 PA-18.1; now the dedicated **VS-105** program.
- **Commodity hedging / input-cost risk** — *previously* a single incidental reference; now the dedicated **VS-106** program.
- **Strategic / key account management** — *previously* sprinkled across VS-11/VS-43/VS-46/VS-13; now the dedicated **VS-107** program.
- **Own-generation / prosumer solar** — *previously* the single monitoring workflows W111 (energy) and W173 (solar) in VS-07/VS-20.3; now the dedicated **VS-108** program.

### Candidate gaps considered but rejected in Pass 7 (adequate coverage)

- **Tax controversy / BIR audit defense / CTA appeal** — covered by W77 (BIR Audit Response) in
  VS-22, with a detailed LOA → investigation → FAN → protest → CTA-appeal lifecycle (separate from
  VS-79 tax filing).
- **Real Property Tax (RPT) assessment, payment & appeal** — covered by W119 (RPT Management) in
  VS-79 and referenced across VS-97/VS-42/VS-76 as owner/lessor/LGU.
- **Insurance claims management & subrogation** — covered by the dedicated PA-26.3 (Insurance
  Claims and Policy Management) in VS-26, including adjuster, settlement, and subrogation.
- **Special / custom / made-to-order lifecycle** — covered by W744 (Store-Level Special Order
  Follow-Up), W545 (special orders), and W38 (special order fulfillment) across VS-09/VS-11.
- **Merchandise allocation / initial distribution** — covered for new stores (VS-37 allocation
  planning) and cross-dock (VS-04); replenishment allocation in VS-02.
- **Loyalty points liability / breakage / reward economics** — covered by VS-13 (loyalty) and
  VS-17.4 (W1405 PFRS 15 deferred-revenue allocation, breakage accounting).
- **Market development funds / co-op advertising / vendor-funded marketing** — covered by W513
  (co-op advertising) in VS-39 and VS-14 marketing.
- **Trade show / exhibition / industry-event representation** — covered by W1899 (Trade Show
  Participation & Industry Event Representation) in VS-43.3 and W1292 (Builder's Expo) in VS-07.1.
- **Fire & life-safety systems management** — covered across VS-24 (HSE), VS-20.3 (facilities),
  and VS-07.2 (store facility/safety), including BFP FSIC and suppression inspections.
- **Data platform / data engineering / analytics operations** — covered by VS-28.2 (Data
  Engineering and Quality) and VS-27.2 (Infrastructure and Platform).
- **Management accounting / cost center / profitability analytics** — covered by VS-17.4 FP&A
  (W1405 Store-Level P&L/Contribution Margin, W85 Product Costing & Margin Analysis Review) and
  VS-33.2 corporate performance management (W1655/W1656 store/category performance review).
- **Performance/capacity of PA 53-file 'calibration' mentions** — *considered as elevation*
  (like Pass 5 elevated W324 SCF) but elevated here to a dedicated value stream (VS-115) because the
  references had no owning PA and spanned revenue, quality, compliance, and HSE impact.

### Candidate gaps considered but rejected in Pass 8 (adequate coverage)

- **Product Information Management (PIM) / Digital Asset Management (DAM) / product-content
  production** — covered by PA-01.3 (Product Information & Content: W50 PIM, W1346 multilingual
  localization, W1345 barcode/GS1, W1465 SDS, W1466 seasonal content staging), VS-10 (ecommerce),
  and VS-48 (retail media). The 'content factory' (photo studio, syndication to marketplaces) is
  substantially covered across VS-01.3/VS-10/VS-65.
- **Vendor compliance / routing guide / ASN / inbound appointment / compliance chargeback** —
  covered by VS-110.2 (Freight Execution, Routing Guide & Visibility), W1168 (DSD Receiving & Vendor
  Compliance), VS-04 (DC receiving), VS-03 (vendor mgmt), and VS-67 (vendor scorecard).
- **Fleet asset lifecycle / telematics / vehicle management** — covered comprehensively by VS-06
  (W199 telematics, W799 vehicle acquisition/registration/disposal, W1348 preventive maintenance,
  W1349 tires, W197 driver, W653 accident) and VS-61 (W2310–W2333 fleet cost/TCO).
- **Organized retail crime (ORC) / refund & return fraud / loyalty-points / gift-card fraud** —
  covered comprehensively by VS-23 (W840/W1542/W1337 ORC, W841/W1336 refund fraud, W1475 coupon
  abuse, W1476 gift-card fraud, W1338 employee theft).
- **Product liability / consumer-safety incident / customer-injury claims** — covered by W185
  (Product Liability & Consumer Safety Incident Management) in VS-22.3, W863 (Third-Party Liability
  & Customer Incident Insurance Response) and W1566 (Store-Level Slip-and-Fall/Customer-Injury
  Claims) in VS-26.3, VS-100 (legal/litigation), and VS-89 (recall).
- **B2B project job costing / progress billing / retention money** — covered by VS-11 (W165
  Project Retention & Milestone Billing, W918 Project Budget & Cost-Variance, W1134 Retention
  Release, W1288/W1426 Progress Billing & Milestone Collection, W1024 Material Escrow).
- **Diversity, Equity, Inclusion & Belonging (DEIB)** — covered by dedicated workflows W3343
  (VS-103.2) and W719 (VS-19.1).
- **Carbon / GHG / Scope 1-2-3 / net-zero accounting** — covered by W192 (GHG Tracking in
  VS-25.1) and W3466 (GHG Reduction & Scope 2 Attribution in VS-108.3), within the ESG (VS-25) and
  renewable (VS-108) programs.
- **Pricing / markdown / price optimization** — covered by VS-01.2 (Pricing & Promotions),
  VS-57 (Competitive Price Intelligence), and VS-101 (Merchandise Financial Planning/OTB/Margin).
- **Energy & utilities consumption management / procurement** — covered by W111 (utility bill),
  VS-25.1 (environmental monitoring), VS-108 (own generation); the *RA 11285 statutory
  compliance / ISO-50001 / ECM program* dimension is now filled by VS-120.
- **Tool / equipment repair & service center** — covered by VS-12 (Installation & Repair Services).
- **AI / model-risk governance / responsible AI** — covered by VS-30.2 (AI/ML & Automation) and
  VS-113 (Enterprise Architecture); emerging and not yet a standalone operational program for the
  current model company.

### Candidate gaps considered but rejected in Pass 9 (adequate coverage)

- **In-store events / DIY workshops / community engagement** — covered comprehensively by PA-12.3
  (Workshops & Events, 10 workflows: W147/W906/W1289/W1377/W1378/W1379/W1556/W1557 incl. instructor
  recruitment, registration/waitlist, vendor demo days, TESDA/school career-day participation, and
  seasonal workshop series with conversion-funnel management).
- **Supplier ESG / sustainable sourcing / responsible procurement** — covered by VS-25.2 (W195
  Sustainable Sourcing & Ethical Vendor Audit, W1176 Green Procurement & Sustainable Vendor
  Certification, W1480 Supplier Diversity), VS-78 green-building product curation, and source-side
  audits in VS-122.2/VS-31/VS-41; three dedicated workflows within ESG plus the new global-sourcing
  source-side governance make this substantially covered.
- **Organizational design / capability framework / strategic workforce planning** — covered by
  VS-103.3 (People Analytics, Workforce Planning & HR Technology) for workforce planning and
  VS-102.1 (Job Architecture, Pay Structure & Market Benchmarking) for job architecture/org-design
  inputs, with VS-33.1 corporate planning linkage; the *strategic* org-design layer is owned across
  these rather than as a standalone value stream.
- **B2B punchout / hosted catalog / procurement integration** — covered by W1242 (E-Commerce B2B
  Corporate Punchout Catalog & Procurement Integration, cXML/OCI) in VS-10.1 plus VS-11 trade/B2B
  and VS-65 marketplace integration.
- **Vendor EDI / ASN / B2B integration** — covered by VS-03.4 (Vendor Portal & Collaboration),
  VS-110.2 (Freight Execution/Routing Guide/Visibility), VS-15.1 (Invoice Processing & Matching),
  and the integration architecture in VS-113; EDI/ASN is a system-of-record integration discipline
  distributed across these rather than a standalone operational value stream.
- **Insurance program / risk financing / total cost of risk** — covered by PA-26.3 (Insurance
  Claims & Policy Management, incl. W862 annual renewal and W1565 annual portfolio review/coverage-
  gap analysis/market benchmarking) in VS-26.
- **Construction-site / jobsite HSE (DOLE D.O. 13-98)** — covered by W789 (Construction Safety
  Management & DOLE DO 13 Compliance) in VS-20.2 for BuildRight construction projects, with field
  safety for dispatched crews in VS-12.1/VS-24.
- **Open innovation / R&D / corporate venture / pilot-to-scale** — covered by VS-30.1 (Emerging
  Technology & PoC, incl. W691 scouting/evaluation and W690 digital-transformation portfolio) and
  VS-30.2 (AI/ML & Automation); emerging tech is owned there rather than as a standalone value
  stream.
- **Clienteling-adjacent: personalization / recommendation engine / customer 360** — covered by
  W200 (AI personalization/recommendation) in VS-30.2, VS-13.3 (Customer Data & CRM), and the new
  VS-124 clienteling tool (W3844); the *data/ML* layer is owned across these, while VS-124 owns the
  *associate-side selling* discipline that was the genuine gap.

### Candidate gaps considered in Pass 12 (four elevated to dedicated value streams; remainder rejected as adequately covered)

- **Continuous improvement / process improvement (as part of VS-30 or VS-21)** — *considered*
within VS-30 (innovation/automation) and VS-21 (audit) but elevated here to a dedicated value
stream (VS-133) because the *continuous-improvement operating system* (methodology, pipeline,
process mining, benefit realization, culture) had no owning PA and is distinct from emerging-tech
scouting (VS-30), audit assurance (VS-21), and project delivery (VS-112).
- **Digital adoption / training (as part of VS-19.4 or VS-27.1)** — *considered* within VS-19.4
(L&D) and VS-27.1 (service desk/hypercare) but elevated here (VS-134) because the *people-side-
of-change discipline* (stakeholder mapping, change-impact/readiness, sponsor activation,
resistance, change-saturation, DAP, adoption sustainment) had no owning PA and is distinct from
training content delivery (VS-19.4/VS-124), project delivery (VS-112), HR operations (VS-103),
and IT service management (VS-27.1).
- **Cloud cost optimization / IT budgeting (as part of VS-99 or VS-17.4)** — *considered* within
VS-99 (IT asset lifecycle) and VS-17.4 (corporate FP&A) but elevated here (VS-135) because the
*technology-financial discipline* (TBM taxonomy, FinOps inform/optimize/operate, showback/
chargeback, unit economics, value realization) had no owning PA and is distinct from asset
inventory/disposal (VS-99), application-landscape design (VS-113), platform operations (VS-27),
and enterprise FP&A (VS-17.4/VS-33).
- **Inventory optimization / network review (as part of VS-02)** — *considered* within VS-02
(the single periodic W183 network-review workflow exists) but elevated here (VS-136) because the
*network/inventory-engineering discipline* (network modeling/design, MEIO, safety-stock/service-
level optimization, simulation, continuous re-optimization) had no owning PA beyond the single
periodic review and is distinct from operational replenishment (VS-02), the S&OP consensus cycle
(VS-127), inventory transactions/lifecycle (VS-05), and logistics execution (VS-06).
- **In-store experiential / field / event / brand-activation marketing** — *considered* but
rejected as adequately covered: VS-14 marketing already owns local store marketing (W1551),
builder's expo (W1292), grand-opening events (W1523), DIY workshops/community events (W1260),
and barangay outreach; a dedicated experiential value stream would overlap.
- **Loyalty coalition / partner rewards / redemption-catalog fulfillment** — *considered* but
rejected as adequately covered by VS-13 (loyalty) workflows W674/W902/W926/W1186/W1434 and VS-14
W902 (partner reward catalog) — partner management, cross-promotion, reward fulfillment, and
settlement are comprehensively owned there.
- **Strategic sourcing / category strategy / should-cost (non-merchandise)** — *considered* but
rejected as adequately covered: VS-03 (vendor management) and VS-15 (procure-to-pay) own sourcing
and category management; VS-110 (freight) and VS-122 (global sourcing) own category-specific
sourcing depth.
- **Customer technical product support / after-sales technical service center** — *considered*
but rejected as adequately covered across VS-12 (W440 power-tool service & repair center,
W1170–W1253 installation dispatch/quality), VS-13 (W1363 VIP support hotline, W1364 DIY help
center, W1290 appliance warranty/after-sales coordination), and VS-53 (warranty).
- **Lease accounting / IFRS 16 / right-of-use asset management** — *considered* in Pass 12 and rejected as
adequately covered (W275 (IFRS 16/PFRS 16 lease accounting) in VS-17 and W1872/W1875 (PFRS 16
month-end and lease-accounting policy) in VS-42), then **re-evaluated and filled in Pass 16 as
VS-148** (gap #62) once the dedicated PFRS 16 recognition / measurement / disclosure program was
judged distinct from the existing single-workflow coverage.
- **Supplier risk / supply-chain resilience** — *considered* in Pass 12 and rejected as adequately covered by
VS-02.3 (W558 supplier risk, W729 disruption response, W763 vendor diversification, W250 control
tower), then **re-evaluated and filled in Pass 18 as VS-161** (gap #75, TPRM) once the unified
cross-domain enterprise third-party-risk program was judged distinct from the per-domain slices
(supply-side in VS-21, ABC in VS-86, privacy in VS-91, ethics in VS-119, fraud in VS-125).

### Candidate gaps considered but rejected in Pass 19 (adequate coverage)

- **Heavy / Pro Construction Equipment Rental** — *considered* (the natural extension of VS-12.2
  tool rental) but rejected as adequately covered by the dedicated workflow **W1094** (Customer
  Construction Equipment Rental Partner Coordination & Booking in VS-09.1), which already models
  BuildRight's chosen approach: BuildRight does **not** own heavy equipment but **partners** with
  regional equipment-rental companies (excavator/backhoe/scaffolding/mixer/generator/jackhammer/
  plate compactor) and earns a booking-coordination fee — a model documented as common in Philippine
  hardware retail. **W1062** additionally covers scaffolding rental. An owned heavy-equipment fleet
  value stream would contradict the established partner-coordination model.
- **Customer self-storage / mobile storage container rental** — *considered* but rejected as
  out of BuildRight's retail charter ('self-storage', 'mobile storage', 'container rental' appear
  in zero PA files but are not part of the home-improvement retail operating model — unlike
  self-haul vehicle rental, which directly converts a bulky-merchandise sale).
- **In-store cafe / food & beverage / refreshment kiosk** — *considered* but rejected as
  adequately covered as a partner concession (~10 incidental 'food concession' / 'refreshment' /
  'snack bar' references across VS-07/VS-12.3/VS-138), not a BuildRight-operated discipline.
- **Notary / blueprint-reprographic / passport-photo / coin-machine services** — *considered*
  but rejected as out-of-charter niche services (zero or near-zero PA references; not core to a
  hardware/DIY/home-improvement retailer and most require separate licensing).
- **Pet / aquarium / pharmacy / dry-cleaning services** — *considered* but rejected as
  out-of-charter (zero PA references; not within the home-improvement retail scope).

### Candidate gaps considered but rejected in Pass 20 (adequate coverage)

- **Timber & forest-products legality / FSC-PEFC chain-of-custody / EUDR due diligence** —
  *considered* (lumber & building materials is BuildRight's #1 category at 14% of SKUs) but
  rejected as adequately covered and explicitly cross-referenced to VS-25.2 (Sustainable Sourcing
  & Ethical Vendor Audit — owns responsible raw-material sourcing incl. timber) and VS-131
  (Human Rights & Responsible Supply Chain DD — W in PA-131.1 explicitly owns 'timber/lumber
  legality and deforestation' salient risk and FSC/PEFC certification evidence). A dedicated
  timber-legality value stream would overlap both; the discipline is owned across ESG (VS-25.2)
  and human-rights DD (VS-131) rather than as a standalone value stream.
- **Customer/vendor bankruptcy & insolvency claim management** — *considered* (bankruptcy/
  insolvency each appear in ~11 PA files with **zero** dedicated headers) but rejected as
  adequately covered within VS-16 (Order-to-Cash: W287 step 6 insolvency/bankruptcy claim filing,
  W16.3 write-off documentation with insolvency evidence, quarterly bad-debt root-cause) and
  VS-100 (legal/litigation) — a standalone value stream would overlap AR/collections.
- **Trade promotion management / trade spend / slotting & vendor deductions** — *considered*
  but rejected as adequately covered by VS-39 (vendor rebate & incentive, incl. W513 co-op/
  market-development funds), VS-14 (marketing), and VS-58 (coupon/digital promotions), per the
  prior rejection of 'market development funds / co-op advertising'.
- **BIR e-invoicing / CAS permit-to-use / authority-to-print (ATP)** — *considered* but rejected
  as adequately covered within VS-79 (tax management) and VS-08.3 (POS compliance), which already
  hold 6 dedicated CAS/e-invoicing workflows (W216/W1304/W1525/W1367/W2685/W2760).
- **Energy-supply procurement / RCOA / WESM exposure** — *considered* but rejected as adequately
  covered within VS-120.1 (PA-120.1 steps 1–2 explicitly own the RCOA retail-competition / Retail
  Electricity Supplier strategy and WESM market-tariff monitoring) and VS-20.3 (EPIRA reference).
- **Centralized SEC reportorial / corporate-secretary discipline (GIS, AFS submission,
  beneficial ownership)** — *considered* (SEC filing ~15 mentions, 0 dedicated headers) but
  rejected as adequately covered within VS-36 (corporate governance & board/corporate records)
  and VS-100.3 (corporate legal advisory), with beneficial-ownership already a workflow (W).
- **In-store specialty services (key cutting, locksmithing, engraving, propane/LPG exchange)**
  — *considered* (zero dedicated headers) but rejected as adequately covered within VS-09
  (in-store services: W943 glass cutting, W944 pipe threading, W1049 tool sharpening, W cylinder
  exchange) and VS-114 (DG/hazmat for LPG); too narrow for a standalone value stream.
- **Mechanic's-lien / lien-waiver management** — *considered* (0 dedicated headers) but rejected
  as folded into VS-165 PA-165.2 (W4831 construction payment security — mechanic's-lien rights,
  lien waivers, payment-bond claims) rather than a standalone value stream, since it is a
  contractor-licensing adjacency.
- **Conflict minerals / 3TG responsible-minerals due diligence** — *considered* but rejected as
  adequately covered within VS-131 (human-rights DD, incl. conflict-affected-area minerals) and
  VS-25.2 (responsible sourcing of raw materials incl. minerals).
- **Guest WiFi / captive-portal / in-store WiFi marketing** — *considered* (zero dedicated
  headers) but rejected as out-of-charter/niche, adequately covered within VS-27 (IT) and VS-14
  (marketing).
- **Employee pension / retirement-plan administration; loyalty/gift-card escheatment beyond
  gift cards; lone-worker safety** — *considered* but rejected as adequately covered (pension
  within VS-102 total rewards; gift-card escheat within VS-09.3/VS-54; lone-worker within VS-24
  HSE / VS-138 IFM) or too narrow for a standalone value stream.

---

## 4. New Value Streams Added

**Pass 1** (W2993–W3088): four value streams, 12 process areas, 96 workflows:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-89](VS-89-product-recall-safety-corrective-action/README.md) | Product Recall & Safety Corrective Action Management | Governance & Assurance | 3 | 24 | W2993–W3016 |
| [VS-90](VS-90-damage-claims-freight-recovery/README.md) | Damage, Claims & Freight Recovery Management | Make & Move | 3 | 24 | W3017–W3040 |
| [VS-91](VS-91-consumer-data-privacy-protection/README.md) | Consumer Data Privacy & Data Protection Program | Governance & Assurance | 3 | 24 | W3041–W3064 |
| [VS-92](VS-92-kitting-bundling-build-to-order-assembly/README.md) | Kitting, Bundling & Build-to-Order Assembly Operations | Make & Move | 3 | 24 | W3065–W3088 |

**Pass 2** (W3089–W3184): four value streams, 12 process areas, 96 workflows:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-93](VS-93-dark-store-micro-fulfillment/README.md) | Dark Store & Micro-Fulfillment Operations | Make & Move | 3 | 24 | W3089–W3112 |
| [VS-94](VS-94-cooperative-community-enterprise-procurement/README.md) | Cooperative & Community Enterprise Procurement | Plan & Source | 3 | 24 | W3113–W3136 |
| [VS-95](VS-95-marketplace-operator-third-party-seller/README.md) | Marketplace Operator & Third-Party Seller Management | Sell & Serve | 3 | 24 | W3137–W3160 |
| [VS-96](VS-96-equipment-leasing-capital-equipment-finance/README.md) | Equipment Leasing & Capital Equipment Finance | Finance | 3 | 24 | W3161–W3184 |

**Pass 3** (W3185–W3280): four value streams, 12 process areas, 96 workflows, deliberately
distributed across the four previously-thinnest operating families (Asset & Infrastructure,
People, Technology & Data each had only 3–4 value streams; Governance & Assurance is the natural
home for legal operations):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-97](VS-97-corporate-real-estate-property-portfolio/README.md) | Corporate Real Estate & Property Portfolio Management | Asset & Infrastructure | 3 | 24 | W3185–W3208 |
| [VS-98](VS-98-contingent-contract-outsourced-workforce/README.md) | Contingent, Contract & Outsourced Workforce Management | People | 3 | 24 | W3209–W3232 |
| [VS-99](VS-99-it-asset-technology-lifecycle-management/README.md) | IT Asset & Technology Lifecycle Management | Technology & Data | 3 | 24 | W3233–W3256 |
| [VS-100](VS-100-legal-operations-litigation-ip-management/README.md) | Legal Operations, Litigation & IP Management | Governance & Assurance | 3 | 24 | W3257–W3280 |

**Pass 4** (W3281–W3376): four value streams, 12 process areas, 96 workflows, deliberately
distributed to strengthen the three thinnest operating families (People +2; Plan & Source +1;
Governance & Assurance +1). Each gap had been previously overlooked because it was conflated with
an adjacent covered capability:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-101](VS-101-merchandise-financial-planning-otb-margin-management/README.md) | Merchandise Financial Planning, OTB & Margin Management | Plan & Source | 3 | 24 | W3281–W3304 |
| [VS-102](VS-102-compensation-benefits-total-rewards/README.md) | Compensation, Benefits & Total Rewards Strategy | People | 3 | 24 | W3305–W3328 |
| [VS-103](VS-103-hr-shared-services-employee-experience-people-analytics/README.md) | HR Shared Services, Employee Experience & People Analytics | People | 3 | 24 | W3329–W3352 |
| [VS-104](VS-104-government-affairs-public-policy-industry-relations/README.md) | Government Affairs, Public Policy & Industry Relations | Governance & Assurance | 3 | 24 | W3353–W3376 |

**Pass 5** (W3377–W3472): four value streams, 12 process areas, 96 workflows. Each gap had been
previously overlooked because it was either (a) conflated with an adjacent covered capability or
(b) addressed only as a single workflow within another value stream (the same pattern used in
Pass 1, where VS-89 Product Recall was elevated from the single customer-notification workflow
W776 in VS-09):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-105](VS-105-supply-chain-finance-working-capital-management/README.md) | Supply Chain Finance & Working Capital Management | Finance | 3 | 24 | W3377–W3400 |
| [VS-106](VS-106-commodity-input-cost-risk-management/README.md) | Commodity & Input-Cost Risk Management | Plan & Source | 3 | 24 | W3401–W3424 |
| [VS-107](VS-107-strategic-key-account-enterprise-customer-management/README.md) | Strategic Key Account & Enterprise Customer Management | Sell & Serve | 3 | 24 | W3425–W3448 |
| [VS-108](VS-108-onsite-renewable-energy-prosumer-asset-operations/README.md) | On-Site Renewable Energy & Prosumer Asset Operations | Asset & Infrastructure | 3 | 24 | W3449–W3472 |

**Pass 6** (W3473–W3568): four value streams, 12 process areas, 96 workflows, deliberately
concentrated in the two thinnest-by-workflow operating families (Make & Move and Asset &
Infrastructure). Each gap had been overlooked because it was either (a) genuinely uncovered by any
value stream, (b) sprinkled across multiple value streams without a single owner, or (c) conflated
with an adjacent covered capability:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-109](VS-109-store-remodel-renovation-lifecycle-refurbishment/README.md) | Store Remodel, Renovation & Lifecycle Refurbishment Program | Asset & Infrastructure | 3 | 24 | W3473–W3496 |
| [VS-110](VS-110-freight-procurement-carrier-management-and-freight-audit/README.md) | Freight Procurement, Carrier Management & Freight Audit | Make & Move | 3 | 24 | W3497–W3520 |
| [VS-111](VS-111-packaging-pallet-and-returnable-transport-item-management/README.md) | Packaging, Pallet & Returnable Transport Item (RTI) Management | Make & Move | 3 | 24 | W3521–W3544 |
| [VS-112](VS-112-corporate-project-and-program-management-office/README.md) | Corporate Project & Program Management Office (PMO) | Asset & Infrastructure | 3 | 24 | W3545–W3568 |

**Pass 7** (W3569–W3664): four value streams, 12 process areas, 96 workflows, deliberately
strengthening the thinnest family by workflow count (**Technology & Data** +48) and adding to three
families total (Governance & Assurance, Finance, and Technology & Data). Each gap had been
previously overlooked because it was (a) genuinely uncovered by every value stream, (b) referenced
across many PA files with no dedicated owner, (c) conflated with a fixed-site HSE capability, or
(d) reduced to single steps within B2G/B2B/treasury value streams:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-113](VS-113-enterprise-architecture-application-portfolio-and-technology-strategy/README.md) | Enterprise Architecture, Application Portfolio & Technology Strategy | Technology & Data | 3 | 24 | W3569–W3592 |
| [VS-114](VS-114-dangerous-goods-hazmat-transport-ecommerce-regulatory-compliance/README.md) | Dangerous Goods (DG) & Hazmat Transport, Ecommerce & Regulatory Compliance | Governance & Assurance | 3 | 24 | W3593–W3616 |
| [VS-115](VS-115-calibration-metrology-and-measurement-traceability-management/README.md) | Calibration, Metrology & Measurement Traceability Management | Technology & Data | 3 | 24 | W3617–W3640 |
| [VS-116](VS-116-performance-bond-surety-and-bank-guarantee-management/README.md) | Performance Bond, Surety & Bank Guarantee Management | Finance | 3 | 24 | W3641–W3664 |

**Pass 8** (W3665–W3760): four value streams, 12 process areas, 96 workflows. Three of the four
are elevations of a single workflow within another value stream to a dedicated end-to-end program
(the same pattern used in Pass 1, Pass 5, and Pass 7), and the fourth is a genuinely-uncovered
statutory program referenced only incidentally across multiple value streams. Each gap had been
previously overlooked because it was (a) reduced to a single workflow (W447 DTI-BPS in VS-22.1;
W348 Revenue Assurance in VS-21.3; W2943 ABC-Whistleblower in VS-86.3), or (b) genuinely uncovered
with only incidental references and no dedicated owner (RA 11285 energy-efficiency compliance
across 14 PA files with zero dedicated headers):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-117](VS-117-dti-bps-product-standards-certification-ps-mark-icc-compliance/README.md) | DTI-BPS Product Standards Certification & PS Mark/ICC Compliance | Governance & Assurance | 3 | 24 | W3665–W3688 |
| [VS-118](VS-118-revenue-assurance-pricing-integrity-and-leakage-management/README.md) | Revenue Assurance, Pricing Integrity & Leakage Management | Finance | 3 | 24 | W3689–W3712 |
| [VS-119](VS-119-whistleblower-ethics-and-corporate-integrity-speak-up-program/README.md) | Whistleblower, Ethics & Corporate Integrity (Speak-Up) Program | Governance & Assurance | 3 | 24 | W3713–W3736 |
| [VS-120](VS-120-energy-efficiency-conservation-and-ra-11285-compliance-program/README.md) | Energy Efficiency, Conservation & RA 11285 Compliance Program | Asset & Infrastructure | 3 | 24 | W3737–W3760 |

**Pass 9** (W3761–W3856): four value streams, 12 process areas, 96 workflows, deliberately
strengthening the thinnest family by workflow count (**People** +48, the thinnest at 194 workflows)
while also filling one genuine gap each in **Plan & Source** and **Sell & Serve**. Each gap had been
previously overlooked because it was genuinely uncovered with **zero** PA-file references for its
defining terms and only incidental single-workflow references to the broader capability:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-121](VS-121-talent-acquisition-employer-brand-candidate-experience/README.md) | Talent Acquisition, Employer Brand & Candidate Experience | People | 3 | 24 | W3761–W3784 |
| [VS-122](VS-122-global-sourcing-import-buying-sourcing-agent-management/README.md) | Global Sourcing, Import Buying & Sourcing Agent Management | Plan & Source | 3 | 24 | W3785–W3808 |
| [VS-123](VS-123-skilled-trade-apprenticeship-vocational-education-capability-pipeline/README.md) | Skilled-Trade Apprenticeship, Vocational Education & Capability Pipeline | People | 3 | 24 | W3809–W3832 |
| [VS-124](VS-124-sales-enablement-product-knowledge-clienteling/README.md) | Sales Enablement, Product Knowledge Mastery & Clienteling | Sell & Serve | 3 | 24 | W3833–W3856 |

**Pass 10** (W3857–W3952): four value streams, 12 process areas, 96 workflows, distributed across
three families (Finance, Technology & Data, Plan & Source). Each gap had been
previously overlooked because it was genuinely unowned as a program — its defining terms appeared
in zero or near-zero PA files with only incidental single-step references to the broader capability
scattered across multiple adjacent value streams:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-125](VS-125-cross-channel-fraud-management-payment-fraud-protection/README.md) | Cross-Channel Fraud Management & Payment Fraud Protection | Finance | 3 | 24 | W3857–W3880 |
| [VS-126](VS-126-customer-data-platform-single-customer-view-identity-resolution/README.md) | Customer Data Platform, Single Customer View & Identity Resolution | Technology & Data | 3 | 24 | W3881–W3904 |
| [VS-127](VS-127-sales-operations-planning-integrated-business-planning/README.md) | Sales & Operations Planning (S&OP) & Integrated Business Planning | Plan & Source | 3 | 24 | W3905–W3928 |
| [VS-128](VS-128-ai-ml-governance-responsible-ai/README.md) | AI/ML Governance & Responsible AI | Technology & Data | 3 | 24 | W3929–W3952 |

**Pass 11** (W3953–W4048): four value streams, 12 process areas, 96 workflows, adding one value stream to **Plan & Source** (the supply-chain-DD discipline) and three to **Governance & Assurance** (competition law, corporate development/M&A, and political engagement). Each gap had been previously overlooked because it was either reduced to a single workflow within another value stream (VS-129 elevating the single W2683 competition-law workflow in VS-76.2, following the same Pass-1/Pass-5/Pass-7/Pass-8/Pass-10 single-workflow-elevation pattern) or genuinely uncovered with no dedicated owner (VS-130 M&A/divestiture, VS-131 human-rights/responsible-supply-chain DD, VS-132 political engagement/election compliance — each with zero or only one incidental PA-file reference for its defining terms):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-129](VS-129-competition-and-antitrust-compliance/README.md) | Competition & Antitrust Compliance (RA 10667 / PCC) | Governance & Assurance | 3 | 24 | W3953–W3976 |
| [VS-130](VS-130-corporate-development-ma-divestiture/README.md) | Corporate Development, Mergers, Acquisitions, Divestiture & Strategic Transactions | Governance & Assurance | 3 | 24 | W3977–W4000 |
| [VS-131](VS-131-human-rights-responsible-supply-chain-due-diligence/README.md) | Human Rights, Modern Slavery & Responsible Supply Chain Due Diligence | Plan & Source | 3 | 24 | W4001–W4024 |
| [VS-132](VS-132-corporate-political-engagement-election-compliance/README.md) | Corporate Political Engagement, Election Compliance & Public Affairs Governance | Governance & Assurance | 3 | 24 | W4025–W4048 |

**Pass 12** (W4049–W4144): four value streams, 12 process areas, 96 workflows, deliberately strengthening three of the four thinnest-by-workflow families (**People** +24, **Technology & Data** +24, **Make & Move** +24) and adding the cross-cutting operational-excellence discipline to **Governance & Assurance** (+24). Each gap had been previously overlooked because it was a genuinely-unowned *enterprise-management discipline* whose defining terms appeared in zero PA files as dedicated workflow headers (process mining / operational excellence / continuous improvement; change management / OCM / adoption; finops / cloud cost / TBM / IT financial management; multi-echelon / inventory optimization / network design), with only incidental single-step references to the broader capability scattered across multiple adjacent value streams. None of the four follows the single-workflow-elevation pattern of Passes 1/5/7/8/10/11; all four are genuinely-unowned enterprise-management disciplines with no dedicated owner:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-133](VS-133-operational-excellence-process-mining-continuous-improvement/README.md) | Operational Excellence, Process Mining & Continuous Improvement Program | Governance & Assurance | 3 | 24 | W4049–W4072 |
| [VS-134](VS-134-organizational-change-management-digital-adoption-transformation-enablement/README.md) | Organizational Change Management, Digital Adoption & Transformation Enablement | People | 3 | 24 | W4073–W4096 |
| [VS-135](VS-135-technology-business-management-it-financial-management-cloud-finops/README.md) | Technology Business Management, IT Financial Management & Cloud FinOps | Technology & Data | 3 | 24 | W4097–W4120 |
| [VS-136](VS-136-supply-chain-network-design-multi-echelon-inventory-optimization-flow-engineering/README.md) | Supply Chain Network Design, Multi-Echelon Inventory Optimization & Flow Engineering | Make & Move | 3 | 24 | W4121–W4144 |

The 96 new workflows added in Pass 12 are currently **unclassified** (counted in the unclassified total) and will be tier-assigned in a follow-up criticality review, exactly as the Pass 1–Pass 11 batches were handled. Several Pass 12 workflows are anticipated Tier 1 (process-mining event-log integrity / change-of-state controls in VS-133, go-live-readiness / hypercare / sponsor-activation controls in VS-134, cloud-commit / showback-integrity / budget-gate controls in VS-135, and service-level / safety-stock / network-resilience controls in VS-136).

**Pass 13** (W4145–W4240): four value streams, 12 process areas, 96 workflows, strengthening the two thinnest families by workflow count (**Asset & Infrastructure** and **Technology & Data**) and adding two genuine, B2B-relevant gaps to **Sell & Serve** (the largest family). Each gap had been previously overlooked because it was a genuinely-unowned *shared-service or B2B-growth discipline* whose defining terms appeared in zero or near-zero PA files as dedicated workflow headers ('product information management'/'PIM'/'digital asset management'/'DAM', 'integrated facilities management'/'IFM'/'building automation'/'BMS', 'trade show'/'exhibition'/'field event', 'field sales'/'outside sales'/'route-to-market'), with only incidental references to the broader capability scattered across multiple adjacent value streams. None of the four follows the single-workflow-elevation pattern of Passes 1/5/7/8/10/11; all four are genuinely-unowned disciplines with no dedicated owner:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-137](VS-137-product-information-management-and-digital-asset-management/README.md) | Product Information Management (PIM) & Digital Asset Management (DAM) | Technology & Data | 3 | 24 | W4145–W4168 |
| [VS-138](VS-138-integrated-facilities-management-workplace-services-and-building-automation/README.md) | Integrated Facilities Management, Workplace Services & Building Automation | Asset & Infrastructure | 3 | 24 | W4169–W4192 |
| [VS-139](VS-139-trade-show-exhibition-and-field-event-marketing/README.md) | Trade Show, Exhibition & Field Event Marketing | Sell & Serve | 3 | 24 | W4193–W4216 |
| [VS-140](VS-140-field-sales-outside-sales-and-route-to-market-force-management/README.md) | Field Sales, Outside Sales & Route-to-Market Force Management | Sell & Serve | 3 | 24 | W4217–W4240 |

The 96 new workflows added in Pass 13 are currently **unclassified** (counted in the unclassified total) and will be tier-assigned in a follow-up criticality review, exactly as the Pass 1–Pass 12 batches were handled. Several Pass 13 workflows are anticipated Tier 1 (DG/SDS publication-gating and DTI-BPS labeling content controls in VS-137, fire/life-safety/permit and statutory-system-cert controls in VS-138, lead-capture consent and event/promo-permit and prize-withholding controls in VS-139, and ABC/gift-register and trade-credit/pricing-integrity controls in VS-140).

**Pass 14** (W4241–W4288): two value streams, six process areas, 48 workflows — a deliberately smaller, focused pass closing the two remaining genuinely-clean gaps after thirteen prior passes had covered the operational, statutory, strategic, cross-cutting-management, technology, shared-service, and B2B-growth surface. Each gap had been previously overlooked because its defining terms appeared in **zero** PA files as dedicated workflow headers and it was conflated with an adjacent covered capability (employee transport conflated with business travel / goods fleet / facilities; COD conflated with acquirer settlement / last-mile delivery / in-store cash). Both strengthen operationally-critical, cash-and-people-exposed domains in two families (People +24, Finance +24):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-141](VS-141-employee-transport-shuttle-and-daily-commute-management/README.md) | Employee Transport, Shuttle & Daily Commute Management | People | 3 | 24 | W4241–W4264 |
| [VS-142](VS-142-cash-on-delivery-operations-driver-cash-handling-and-reconciliation/README.md) | Cash-on-Delivery (COD) Operations, Driver Cash Handling & Reconciliation | Finance | 3 | 24 | W4265–W4288 |

The 48 new workflows added in Pass 14 are currently **unclassified** (counted in the unclassified total) and will be tier-assigned in a follow-up criticality review, exactly as the Pass 1–Pass 13 batches were handled. Several Pass 14 workflows are anticipated Tier 1 (LTFRB-franchise/insurance/out-of-service and women-safe/after-dark transport controls in VS-141, and SoD/daily-reconciliation/custody/bonding and BIR cash-receipting/float-provision controls in VS-142).

**Pass 15** (W4289–W4384): four value streams, 12 process areas, 96 workflows — a deliberately balanced pass adding +24 to each of four operating families (Make & Move, People, Sell & Serve, Governance & Assurance) after fourteen prior passes had been judged complete. Re-running the established gap methodology (defining terms appearing in **zero** PA files as dedicated workflow headers, with only incidental mentions, each conflated with an adjacent covered capability) surfaced four further genuinely-unowned operational disciplines that had been overlooked because the surrounding coverage made them appear owned:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-143](VS-143-bulky-white-goods-delivery-installation-haul-away-and-recycling/README.md) | Bulky & White-Goods Delivery, Installation, Haul-Away & Recycling Operations | Make & Move | 3 | 24 | W4289–W4312 |
| [VS-144](VS-144-employee-accommodation-dormitory-and-staff-housing/README.md) | Employee Accommodation, Dormitory & Staff Housing Operations | People | 3 | 24 | W4313–W4336 |
| [VS-145](VS-145-garden-center-live-goods-and-plant-nursery/README.md) | Garden Center, Live Goods & Plant Nursery Operations | Sell & Serve | 3 | 24 | W4337–W4360 |
| [VS-146](VS-146-customer-mystery-shopping-and-service-quality-assurance/README.md) | Customer Mystery Shopping & Service Quality Assurance Program | Governance & Assurance | 3 | 24 | W4361–W4384 |

The 96 new workflows added in Pass 15 are currently **unclassified** (counted in the unclassified total) and will be tier-assigned in a follow-up criticality review, exactly as the Pass 1–Pass 14 batches were handled. Several Pass 15 workflows are anticipated Tier 1 (RA 9275 refrigerant-recovery and DOLE OSH heavy-lifting/customer-premises liability controls in VS-143, BFP fire-safety/DOLE-OSH-housing and welfare/anti-harassment controls in VS-144, FPA pesticide/BPI restricted-species and refrigerant-style safety controls in VS-145, and shopper-integrity/RA 10173 consent and independent-assurance controls in VS-146).

**Pass 16** (W4385–W4480): four value streams, 12 process areas, 96 workflows — a balanced pass adding +24 to each of four operating families (Governance & Assurance, Finance, Sell & Serve, People) after fifteen prior passes had been judged complete. Re-running the established gap methodology (defining terms appearing in **zero** PA files as dedicated workflow headers, with only incidental mentions, each conflated with an adjacent covered capability) surfaced four further genuinely-unowned operational disciplines that had been overlooked because the surrounding coverage made them appear owned:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-147](VS-147-customer-safety-premises-liability-and-in-store-risk-management/README.md) | Customer Safety, Premises Liability & In-Store Risk Management | Governance & Assurance | 3 | 24 | W4385–W4408 |
| [VS-148](VS-148-lease-accounting-pfrs-16-and-right-of-use-asset-management/README.md) | Lease Accounting (PFRS 16/IFRS 16) & Right-of-Use Asset Management | Finance | 3 | 24 | W4409–W4432 |
| [VS-149](VS-149-self-checkout-scan-and-go-and-unattended-retail-technology-operations/README.md) | Self-Checkout, Scan-&-Go & Unattended Retail Technology Operations | Sell & Serve | 3 | 24 | W4433–W4456 |
| [VS-150](VS-150-drug-free-workplace-and-substance-abuse-program/README.md) | Drug-Free Workplace & Substance Abuse Program | People | 3 | 24 | W4457–W4480 |

The 96 new workflows added in Pass 16 are currently **unclassified** (counted in the unclassified total) and will be tier-assigned in a follow-up criticality review, exactly as the Pass 1–Pass 15 batches were handled. Several Pass 16 workflows are anticipated Tier 1 (premises-liability/CAPA/BFP Fire Code/Consumer Act controls in VS-147, PFRS 16 recognition/disclosure/reconciliation controls in VS-148, scan-avoidance/weight-security/BIR CAS/Consumer Act price-integrity controls in VS-149, and DOLE D.O. 53-03/chain-of-custody/MRO/due-process/RA 10173 controls in VS-150).

**Pass 17** (W4481–W4624): six value streams, 18 process areas, 144 workflows — the largest single pass, combining three genuinely-uncovered operational disciplines with the three capabilities explicitly flagged as *future business-model extensions* in §6 of prior passes. Each gap's defining terms appeared in zero or near-zero PA files as dedicated workflow headers with no dedicated owner; the three future-flagged capabilities are activated here *within BuildRight's retail charter* (captive = BuildRight's own risk financing; construction finance = broker/referral not lending; resale = certified pre-owned not an open C2C marketplace). VS numbering was shifted to VS-151–VS-156 (W4481–W4624) to avoid colliding with VS-143–VS-150 / W4289–W4480 allocated by Passes 15–16. The pass strengthens five families (Technology & Data +24, Governance & Assurance +24, Finance +48, Make & Move +24, Sell & Serve +24):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-151](VS-151-auto-id-barcode-rfid-labeling-and-eas-operations/README.md) | Auto-ID, Barcode, RFID, Price-Tag Labeling & EAS Operations | Technology & Data | 3 | 24 | W4481–W4504 |
| [VS-152](VS-152-corporate-social-responsibility-foundation-and-community-investment/README.md) | Corporate Social Responsibility, Foundation & Community Investment | Governance & Assurance | 3 | 24 | W4505–W4528 |
| [VS-153](VS-153-captive-insurance-reinsurance-and-enterprise-risk-financing/README.md) | Captive Insurance, Reinsurance & Enterprise Risk Financing | Finance | 3 | 24 | W4529–W4552 |
| [VS-154](VS-154-home-construction-finance-loan-brokerage-and-mortgage-referral/README.md) | Home Construction Finance, Loan Brokerage & Mortgage Referral Services | Finance | 3 | 24 | W4553–W4576 |
| [VS-155](VS-155-trade-in-buy-back-and-certified-pre-owned-product-resale/README.md) | Trade-In, Buy-Back & Certified Pre-Owned Product Resale | Make & Move | 3 | 24 | W4577–W4600 |
| [VS-156](VS-156-in-store-value-added-services-and-financial-agency-operations/README.md) | In-Store Value-Added Services & Financial Agency Operations | Sell & Serve | 3 | 24 | W4601–W4624 |

The 144 new workflows added in Pass 17 are **unclassified** and carry a keyword-driven proposed tier in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) (regenerated via `07-methodology/classify-workflows.py`), exactly as prior batches; they will be confirmed into the register during a follow-up criticality review. Several Pass 17 workflows are anticipated Tier 1 (RA 7394 price-tag/EAS-cash-integrity and read-rate/labeling-conformance controls in VS-151; Foundation safeguarding/PSEA and fund-use/due-diligence controls in VS-152; captive risk-transfer/capital-adequacy/RBC controls in VS-153; BSP brokerage/anti-predatory/privacy controls in VS-154; safety-screen/data-wipe/warranty-liability controls in VS-155; BSP-agent/KYC-AML/cash-SoD controls in VS-156).

**Pass 18** (W4625–W4744): five value streams, 15 process areas, 120 workflows — a focused pass closing five further genuinely-unowned disciplines that re-running the established gap methodology (defining terms in zero PA files as dedicated workflow headers, no dedicated owner, conflated with adjacent covered coverage) surfaced after seventeen prior passes had been judged complete. Two are *single-workflow elevations* following the Pass 1/5/7/8/10/11 pattern (VS-157 elevates the over-stuffed W487 in VS-15.1; VS-158 elevates the heavily-referenced W85 in VS-17.4), one is a *scattered-slice consolidation* following the Pass 10/12 pattern (VS-161 unifies the TPRM slices spread across VS-21/VS-86/VS-91/VS-119/VS-125), and two are *genuinely uncovered* with zero defining-term references (VS-159 corporate security/executive protection; VS-160 immigration/global mobility). The pass strengthens three families (Finance +48, Governance & Assurance +48, People +24):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-157](VS-157-revenue-recognition-pfrs-15-and-complex-contract-accounting/README.md) | Revenue Recognition (PFRS 15) & Complex Contract Accounting | Finance | 3 | 24 | W4625–W4648 |
| [VS-158](VS-158-product-costing-landed-cost-and-cost-accounting/README.md) | Product Costing, Landed-Cost & Cost Accounting | Finance | 3 | 24 | W4649–W4672 |
| [VS-159](VS-159-corporate-security-executive-protection-and-travel-risk-management/README.md) | Corporate Security, Executive Protection & Travel Risk Management | Governance & Assurance | 3 | 24 | W4673–W4696 |
| [VS-160](VS-160-global-mobility-immigration-and-foreign-worker-compliance/README.md) | Global Mobility, Immigration & Foreign Worker Compliance | People | 3 | 24 | W4697–W4720 |
| [VS-161](VS-161-third-party-and-supplier-risk-management-tprm/README.md) | Third-Party & Supplier Risk Management (TPRM) | Governance & Assurance | 3 | 24 | W4721–W4744 |

The 120 new workflows added in Pass 18 are **unclassified** and carry a keyword-driven proposed tier in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) (regenerated via `07-methodology/classify-workflows.py`), exactly as prior batches; they will be confirmed into the register during a follow-up criticality review. Several Pass 18 workflows are anticipated Tier 1 (PFRS 15 recognition/cut-off/disclosure and go-live-gate controls in VS-157; standard-cost-roll/landed-cost/cost-SoD controls in VS-158; K&R-response/executive-protection/lawful-evidence controls in VS-159; DOLE-AEP/BI-9G/no-work-before-visa/duty-of-care controls in VS-160; TPRM tiering/cyber-attestation/DPA/concentration-limit controls in VS-161).

**Pass 19** (W4745–W4816): three value streams, nine process areas, 72 workflows — a focused pass closing three further genuinely-unowned operational disciplines that re-running the established gap methodology (defining terms in **zero** PA files as dedicated workflow headers, no dedicated owner, conflated with adjacent covered coverage) surfaced after eighteen prior passes had been judged complete. All three are genuinely-uncovered capabilities whose defining terms appeared in zero PA files as dedicated workflow headers ('pickup truck rental'/'cargo van rental'/'self-haul rental' for VS-162; 'EV charging station host'/'EVSE host network'/'OCPI roaming' for VS-163; 'smart locker network'/'automated parcel collection'/'returns locker' for VS-164), each conflated with an adjacent covered capability (goods delivery fleet / tool rental / delivery services / employee transport for VS-162; own-consumption renewable generation / own energy efficiency / own diesel fleet fueling for VS-163; the BOPIS counter transaction / in-store unattended selling tech / fulfillment / returns for VS-164). The pass strengthens three families (Sell & Serve +48 via VS-162 + VS-164; Asset & Infrastructure +24 via VS-163):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-162](VS-162-customer-pickup-truck-and-cargo-van-rental/README.md) | Customer Pickup Truck & Cargo Van Rental (Self-Haul) Operations | Sell & Serve | 3 | 24 | W4745–W4768 |
| [VS-163](VS-163-electric-vehicle-ev-charging-station-host-network-operations/README.md) | Electric Vehicle (EV) Charging Station Host Network Operations | Asset & Infrastructure | 3 | 24 | W4769–W4792 |
| [VS-164](VS-164-smart-locker-and-automated-parcel-collection-network/README.md) | Smart Locker & Automated Parcel Collection Network | Sell & Serve | 3 | 24 | W4793–W4816 |

The 72 new workflows added in Pass 19 are **unclassified** and carry a keyword-driven proposed tier in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) (regenerated via `07-methodology/classify-workflows.py`), exactly as prior batches; they will be confirmed into the register during a follow-up criticality review. Several Pass 19 workflows are anticipated Tier 1 (LTO registration/CTPL/release-gate and deposit-hold/deductible-recovery controls in VS-162; DOE/LGU/RA 11697 site-permit and metering/PFRS-15-tariff and OCPP/OCPI-billing-integrity controls in VS-163; OMS/inventory-desync-recon and access-authentication/anti-fraud and RA 7277-accessibility/RA 10173-consent controls in VS-164).

**Pass 20** (W4817–W4888): three value streams, nine process areas, 72 workflows — a focused pass closing three further genuinely-unowned operational disciplines that re-running the established gap methodology (defining terms in **zero** PA files as dedicated workflow headers, no dedicated owner, conflated with adjacent covered coverage or reduced to a single-domain slice) surfaced after nineteen prior passes had been judged complete. One is a genuinely-uncovered statutory licensing regime (VS-165 PCAB — every existing PCAB reference verifies *someone else's* license, never BuildRight's own), and two are scattered-slice consolidations following the Pass 10/12/18 pattern (VS-166 unifies the license/permit portfolio slices spread across VS-22/76/79/114/117/138/165/46/06; VS-167 unifies the workforce-vetting slices — the single contingent-only W3223 in VS-98, the employee onboarding-step in VS-121, vendor driver checks in W1400, and ad-hoc executive vetting). The pass strengthens two families (Governance & Assurance +48 via VS-165 + VS-166; People +24 via VS-167):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-165](VS-165-pcab-contractor-licensing-and-ra-4566-construction-contractor-compliance/README.md) | PCAB Contractor Licensing & RA 4566 Construction Contractor Compliance | Governance & Assurance | 3 | 24 | W4817–W4840 |
| [VS-166](VS-166-regulatory-license-permit-and-accreditation-portfolio-management/README.md) | Regulatory License, Permit & Accreditation Portfolio Management | Governance & Assurance | 3 | 24 | W4841–W4864 |
| [VS-167](VS-167-workforce-background-screening-credentialing-and-personnel-vetting/README.md) | Workforce Background Screening, Credentialing & Personnel Vetting | People | 3 | 24 | W4865–W4888 |

The 72 new workflows added in Pass 20 are **unclassified** and carry a keyword-driven proposed tier in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) (regenerated via `07-methodology/classify-workflows.py`), exactly as prior batches; they will be confirmed into the register during a follow-up criticality review. Several Pass 20 workflows are anticipated Tier 1 (RA 4566 license-lapse/unlicensed-contracting and project-registration/notice-of-award and license-condition/bond-release controls in VS-165; store-closing/BIR-CAS/PhilGEPS-eligibility and lapse-remediation/inspection-response controls in VS-166; and RA 10173-consent/retention and adverse-action-due-process/NLRC and safety-sensitive-clearance-gate controls in VS-167).

**Pass 21** (W4889–W4936): two value streams, six process areas, 48 workflows — a focused pass closing two further genuinely-unowned operational disciplines that re-running the established gap methodology (defining terms in **zero** PA files as dedicated workflow headers, no dedicated owner, conflated with adjacent covered coverage) surfaced after twenty prior passes had been judged complete. Both are genuinely-uncovered operational disciplines whose defining terms appeared in zero PA files as dedicated workflow headers and each had been conflated with adjacent covered capabilities (in-store audio/music conflated with the single PA-announcement *step* in store daily management plus a single incidental FILSCAP system-list mention; uniform/workwear/PPE conflated with one onboarding-kit step plus the HSE PPE *requirement* plus a total-rewards allowance plus transactional procurement). The pass strengthens two families (Sell & Serve +24 via VS-168; People +24 via VS-169):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-168](VS-168-in-store-audio-ambient-media-and-music-royalty-licensing/README.md) | In-Store Audio, Ambient Media & Music Royalty Licensing | Sell & Serve | 3 | 24 | W4889–W4912 |
| [VS-169](VS-169-employee-uniform-workwear-and-ppe-issuance-program/README.md) | Employee Uniform, Workwear & PPE-Issuance Program | People | 3 | 24 | W4913–W4936 |

The 48 new workflows added in Pass 21 are **unclassified** and carry a keyword-driven proposed tier in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) (regenerated), exactly as prior batches; they will be confirmed into the register during a follow-up criticality review. Several Pass 21 workflows are anticipated Tier 1 (FILSCAP/RA 8293 royalty-license-current/infringement-damages and emergency-override-tested-every-site and RA 7394 price-integrity controls in VS-168; and DOLE-OSH PPE-issued/fit-tested/in-date and certified-PPE and PPE-use-enforced controls in VS-169).

**Pass 22** (W4937–W5008): three value streams, nine process areas, 72 workflows — a focused pass closing three further genuinely-unowned operational disciplines that re-running the established gap methodology surfaced after twenty-one prior passes had been judged complete. One is genuinely-uncovered with **zero** PA-file references for its defining terms (VS-170 — 'borrowing base', 'asset-based lending', 'trust receipt', 'field warehouse', 'notional pool' each appeared in zero PA files; the adjacent coverage was only the single treasury W319 facility/covenant workflow plus import-LC W232 and demurrage W249). Two are single-workflow-elevation / scattered-slice-consolidation candidates following the established patterns: VS-171 consolidates the customer bulky-pickup & loading-bay slices spread across W1193 (VS-07.3), W773 (VS-09.3), and W4805 (VS-164.2); VS-172 elevates the single W1472 (Trade Account Referral Program / Contractor Network in VS-11.1) to the end-to-end installer-network & pro-referral program. The pass strengthens three families (Finance +24 via VS-170; Sell & Serve +48 via VS-171 + VS-172):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-170](VS-170-inventory-pledge-asset-based-lending-and-trust-receipt-financing/README.md) | Inventory Pledge, Asset-Based Lending & Trust-Receipt (Warehouse-Receipt) Financing | Finance | 3 | 24 | W4937–W4960 |
| [VS-171](VS-171-customer-pickup-loading-zone-and-will-call-counter-operations/README.md) | Customer Pickup, Loading Zone & Will-Call Counter Operations | Sell & Serve | 3 | 24 | W4961–W4984 |
| [VS-172](VS-172-third-party-installer-and-contractor-network-pro-referral-management/README.md) | Third-Party Installer & Contractor Network (Pro-Referral) Management | Sell & Serve | 3 | 24 | W4985–W5008 |

The 72 new workflows added in Pass 22 are **unclassified** and carry a keyword-driven proposed tier in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) (regenerated), exactly as prior batches; they will be confirmed into the register during a follow-up criticality review. Several Pass 22 workflows are anticipated Tier 1 (PD 115 trust-receipt/segregation/anti-diversion and borrowing-base-availability/over-advance-gate and covenant/collateral-release controls in VS-170; forklift-in-customer-area/spotter/load-securement and ID/release-integrity and DOLE-OSH-operator-qualification controls in VS-171; and PCAB/RA 4566-license-verified/insurance and vetting/onboarding-gate and consent/RA 10173 and referral-settlement/revenue-assurance controls in VS-172).

**Pass 23** (W5009–W5032): one value stream, three process areas, 24 workflows — a focused pass closing one further genuinely-unowned corporate-finance discipline that re-running the established gap methodology (defining terms in **zero** PA files as dedicated workflow headers, no dedicated owner, conflated with adjacent covered coverage and reduced to scattered single-workflow slices) surfaced after twenty-two prior passes had been judged complete. It is a scattered-slice consolidation (the VS-161 TPRM / VS-166 license-portfolio pattern): the investor-relations & securities-discipline existed only as the scattered single workflows W327 (dividend *payment*, VS-18.1), W482 (ASHM *logistics*, VS-17.1), W4684 (AGM *security*, VS-159), W4524 (foundation *annual report*, VS-152), and W3373 (policy/industry *analyst* relations, VS-104) — no value stream owned the end-to-end investor-relations / capital-markets / securities-disclosure program. The pass strengthens one family (Finance +24 via VS-173):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-173](VS-173-investor-relations-capital-markets-and-securities-disclosure/README.md) | Investor Relations, Capital Markets & Securities Disclosure | Finance | 3 | 24 | W5009–W5032 |

The 24 new workflows added in Pass 23 are **unclassified** and carry a keyword-driven proposed tier in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) (regenerated via `07-methodology/classify-workflows.py`), exactly as prior batches; they will be confirmed into the register during a follow-up criticality review. Several Pass 23 workflows are anticipated Tier 1 (RA 8799/SEC material-event/ad-hoc disclosure-timeliness and selective/fair-disclosure and insider-list/trading-window controls in W5017/W5019/W5022, and ASHM-notice/proxy-integrity and related-party/beneficial-ownership disclosure and annual-report/SEC-filing-deadline controls in W5018/W5020/W5023).

**Pass 24** (W5033–W5104): three value streams, nine process areas, 72 workflows — a focused pass closing three further genuinely-unowned *customer-facing value-added service* disciplines that re-running the established gap methodology (defining terms in **zero** PA files as dedicated workflow headers and in **zero** VS directory names, no dedicated owner, conflated with adjacent covered coverage) surfaced after twenty-three prior passes had been judged complete. All three are genuinely-uncovered operational adjacencies material to BuildRight's mix, each with only a single incidental reference (or none): VS-174 (self-storage — 'self-storage'/'storage unit'/'portable storage'/'mobile storage' each in zero PA files), VS-175 (propane/LPG — 'propane'/'LPG'/'cylinder exchange'/'gas refill' each in zero PA files, with only the single W1063 *welding*-gas workflow in VS-09.1 as the incidental reference), and VS-176 (blueprint/reprographics — 'blueprint'/'reprographics'/'large-format printing'/'plan printing'/'plotter' each in zero PA files). Each is distinct from its adjacent covered capabilities (documented in the §3 rows and each VS README). The pass strengthens one family (Sell & Serve +72 via VS-174 + VS-175 + VS-176):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-174](VS-174-self-storage-portable-container-and-mobile-storage-operations/README.md) | Self-Storage, Portable Container & Mobile-Storage Operations | Sell & Serve | 3 | 24 | W5033–W5056 |
| [VS-175](VS-175-propane-lpg-cylinder-exchange-and-gas-refill-operations/README.md) | Propane, LPG Cylinder Exchange & Gas Refill Operations | Sell & Serve | 3 | 24 | W5057–W5080 |
| [VS-176](VS-176-blueprint-reprographics-and-large-format-plan-printing-services/README.md) | Blueprint, Reprographics & Large-Format Plan Printing Services | Sell & Serve | 3 | 24 | W5081–W5104 |

The 72 new workflows added in Pass 24 are **unclassified** and carry a keyword-driven proposed tier in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) (regenerated via `07-methodology/classify-workflows.py`), exactly as prior batches; they will be confirmed into the register during a follow-up criticality review. Several Pass 24 workflows are anticipated Tier 1 (BFP Fire-Code/FSIC and LPG-cylinder RA 11592/DTI-BPS gating and HAZMAT/leak-detection and emergency-response controls in VS-175; storage BFP/FSIC and lien-disposition and access-control/tenant-safety controls in VS-174; and customer-document RA 10173/copyright/sealed-bid and equipment-calibration/scale-accuracy controls in VS-176).

**Pass 25** (W5105–W5128): one value stream, three process areas, 24 workflows — a focused pass closing one further genuinely-unowned operational discipline that re-running the established gap methodology surfaced after twenty-four prior passes had been judged complete. VS-177 is a **single-workflow-elevation + scattered-slice-consolidation** candidate (the combined Pass-1/5/7/8/10/11/22/23 single-workflow-elevation pattern and the VS-161/166/171 scattered-slice-consolidation pattern): the **Regional Manager** role already appears as the accountable/informed party across **~66 PA files** (VS-07 daily management / delay-incident escalation / delivery review, VS-37 store opening, VS-109 remodel, VS-146 mystery-shopping remediation, VS-23 LP) yet the field-management discipline existed only as the scattered single workflows **W1030** (Multi-Store District Manager Weekly Operations Review & Compliance Audit, buried in VS-07.1 Store Daily Management), **W2369** (Regional Operations Follow-Up, in VS-63.2), **W3836** (Sales Coaching, Field Enablement & Store-Level Reinforcement, in VS-124), and **W1214** (Store Performance Scorecard Weekly Review & Regional Benchmarking); the defining terms 'field retail', 'field operations', 'field execution', 'retail execution', 'multi-store management', 'store operations support', 'store support center', 'store hotline', 'store escalation', 'store operations center', 'district manager', 'field coach', 'store turnaround', and 'new-store stabilization' each appeared in **zero** PA files as dedicated workflow headers — no value stream owned the *field-management operating model*. It is distinct from VS-07 (single-store daily ops — this owns the *multi-store field layer above the store*), VS-33 (corporate strategy/portfolio KPIs — this *executes* strategy store-by-store), VS-63 (HQ→store broadcast/task direction — this also owns the reverse store→HQ *support/escalation* direction and the field-visit/coaching discipline), and VS-146 (independent assurance — this is the *first-line field-management* that acts on those findings). The pass strengthens one family (Sell & Serve +24):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-177](VS-177-field-retail-operations-regional-district-management-and-multi-store-execution/README.md) | Field Retail Operations, Regional/District Management & Multi-Store Retail Execution Network | Sell & Serve | 3 | 24 | W5105–W5128 |

The 24 new workflows added in Pass 25 are **unclassified** and carry a keyword-driven proposed tier in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) (regenerated via `07-methodology/classify-workflows.py`), exactly as prior batches; they will be confirmed into the register during a follow-up criticality review. Several Pass 25 workflows are anticipated Tier 1 (exception/override authorization SoD/abuse-prevention and price-integrity escalation controls in W5123; store-grievance anti-retaliation and ethics-routing controls in W5124; multi-store P&L/standards-compliance integrity and turnaround-governance controls in W5109/W5111; and standards-audit competency/visit-cadence and visit-evidence controls in W5113/W5114).

### Family subtotal impact (cumulative after Pass 1 + Pass 2 + Pass 3 + Pass 4 + Pass 5 + Pass 6 + Pass 7 + Pass 8 + Pass 9 + Pass 10 + Pass 11 + Pass 12 + Pass 13 + Pass 14 + Pass 15 + Pass 16 + Pass 17 + Pass 18 + Pass 19 + Pass 20 + Pass 21 + Pass 22 + Pass 23 + Pass 24 + Pass 25)

| Family | After Pass 3 | After Pass 4 | After Pass 5 | After Pass 6 | After Pass 7 | After Pass 8 | After Pass 9 | After Pass 10 | After Pass 11 | After Pass 12 | After Pass 13 | After Pass 14 | After Pass 15 | After Pass 16 | After Pass 17 | After Pass 18 | After Pass 19 | After Pass 20 | After Pass 21 | After Pass 22 | After Pass 23 | After Pass 24 | After Pass 25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Plan & Source | 308 | 332 | 356 | 356 | 356 | 356 | 380 | 404 | 428 | 428 | 428 | 428 | 428 | 428 | 428 | 428 | 428 | 428 | 428 | 428 | 428 | 428 | 428 |
| Make & Move | 307 | 307 | 307 | 355 | 355 | 355 | 355 | 355 | 355 | 379 | 379 | 379 | 403 | 403 | 427 | 427 | 427 | 427 | 427 | 427 | 427 | 427 | 427 |
| Sell & Serve | 1,098 | 1,098 | 1,122 | 1,122 | 1,122 | 1,122 | 1,146 | 1,146 | 1,146 | 1,146 | 1,194 | 1,194 | 1,218 | 1,242 | 1,266 | 1,266 | 1,314 | 1,314 | 1,338 | 1,386 | 1,386 | 1,458 | **1,482** (+24) |
| Finance | 411 | 411 | 435 | 435 | 459 | 483 | 483 | 507 | 507 | 507 | 507 | 531 | 531 | 555 | 603 | 651 | 651 | 651 | 651 | 675 | 699 | 699 | 699 |
| People | 146 | 194 | 194 | 194 | 194 | 194 | 242 | 242 | 242 | 266 | 266 | 290 | 314 | 338 | 338 | 362 | 362 | 386 | 410 | 410 | 410 | 410 | 410 |
| Asset & Infrastructure | 128 | 128 | 152 | 200 | 200 | 224 | 224 | 224 | 224 | 224 | 248 | 248 | 248 | 248 | 248 | 248 | 272 | 272 | 272 | 272 | 272 | 272 | 272 |
| Governance & Assurance | 552 | 576 | 576 | 576 | 600 | 648 | 648 | 648 | 720 | 744 | 744 | 744 | 768 | 792 | 816 | 864 | 864 | 912 | 912 | 912 | 912 | 912 | 912 |
| Technology & Data | 182 | 182 | 182 | 182 | 230 | 230 | 230 | 278 | 278 | 302 | 326 | 326 | 326 | 326 | 350 | 350 | 350 | 350 | 350 | 350 | 350 | 350 | 350 |
| **Grand total** | **3,132** | **3,228** | **3,324** | **3,420** | **3,516** | **3,612** | **3,708** | **3,804** | **3,900** | **3,996** | **4,092** | **4,140** | **4,236** | **4,332** | **4,476** | **4,596** | **4,668** | **4,740** | **4,788** | **4,860** | **4,884** | **4,956** | **4,980** (+24) |
| Value streams | 96 | 100 | 104 | 108 | 112 | 116 | 120 | 124 | 128 | 132 | 136 | 138 | 142 | 146 | 152 | 157 | 160 | 163 | 165 | 168 | 169 | 172 | **173** (+1) |
| Process areas | 292 | 304 | 316 | 328 | 340 | 352 | 364 | 376 | 388 | 400 | 412 | 418 | 430 | 442 | 460 | 475 | 484 | 493 | 499 | 508 | 511 | 520 | **523** (+3) |

> **Note on the grand-total column:** the progression above records the `## W` header count
> as it stood at the end of each gap-analysis pass, ending at **4,980** after Pass 25. A
> subsequent consistency review (2026-06-20) restored a missing `## W1318.` header on a
> complete Core-block workflow body in VS-12 PA-12.2 (Tool Rental Reservation, Waitlist &
> Scheduling — long referenced by its siblings as W1318 but never counted because its header
> had been lost in generation). The W1318 restoration brought the total to **4,981**; Passes 26–30 (VS-178–VS-192; +96 + 96 + 96 + 48 + 24 = 360 workflows) subsequently extended the canonical grand total to **5,341** (188 value streams, 568 process areas), summarized in the Pass 26–30 progression table below. This table is not retroactively adjusted because W1318 is a Core-block workflow, not a
> gap-analysis addition, so it was never part of any pass's +N increment. See the
> [CHANGELOG](../../CHANGELOG.md) entry for 2026-06-20 and `validate-repo.sh` Check 17.

#### Pass 26–30 progression (subsequent additions)

| Family | After Pass 25 | +W1318 restoration | After Pass 26 | After Pass 27 | After Pass 28 | After Pass 29 | After Pass 30 (current) |
|---|---|---|---|---|---|---|---|
| Plan & Source | 428 | — | 428 | 452 | 452 | 452 | 452 |
| Make & Move | 427 | — | 451 | 451 | 451 | 475 | 499 |
| Sell & Serve | 1,482 | +1 | 1,483 | 1,507 | 1,531 | 1,531 | 1,531 |
| Finance | 699 | — | 723 | 723 | 771 | 771 | 771 |
| People | 410 | — | 410 | 434 | 434 | 434 | 434 |
| Asset & Infrastructure | 272 | — | 296 | 320 | 320 | 320 | 320 |
| Governance & Assurance | 912 | — | 936 | 936 | 960 | 960 | 960 |
| Technology & Data | 350 | — | 350 | 350 | 350 | 374 | 374 |
| **Grand total** | **4,980** | **+1** | **5,077** | **5,173** | **5,269** | **5,317** | **5,341** |
| Value streams | 173 | — | 177 | 181 | 185 | 187 | 188 |
| Process areas | 523 | — | 535 | 547 | 559 | 565 | 568 |

The **+W1318 restoration** column records the single Core-block header restoration (VS-12 PA-12.2 Tool Rental Reservation, a Sell & Serve workflow) applied after Pass 25; it is shown as a separate column so each pass's +96/+48 increment stays cleanly attributable to the gap-analysis passes — Pass 26 (VS-178–VS-181), Pass 27 (VS-182–VS-185), Pass 28 (VS-186–VS-189), Pass 29 (VS-190–VS-191), Pass 30 (VS-192). Every column reconciles to its grand-total cell.

Pass 14 deliberately closed the two remaining genuinely-clean gaps — **People** (266 → 290 via
VS-141 Employee Transport/Shuttle & Daily Commute Management) and **Finance** (507 → 531 via
VS-142 Cash-on-Delivery Operations & Driver Cash Reconciliation) — both operationally-critical,
cash-and-people-exposed disciplines that had been conflated with adjacent covered capabilities
(business travel, goods fleet, and facilities for transport; acquirer settlement, last-mile
delivery, and in-store cash for COD). This is a deliberately smaller pass (2 VS / 48 workflows)
reflecting that the thirteen prior passes had already covered the operational, statutory,
strategic, cross-cutting-management, technology, shared-service, and B2B-growth surface; only
these two genuinely-unowned disciplines remained, each with zero dedicated workflow headers for
its defining terms and no dedicated owner.

Pass 13 deliberately strengthened the two thinnest families by workflow count — **Asset &
Infrastructure** (224 → 248 via VS-138 Integrated Facilities Management) and **Technology & Data**
(302 → 326 via VS-137 PIM/DAM) — and added two genuine, B2B-relevant gaps to **Sell & Serve**
(1,146 → 1,194 via VS-139 Trade Show/Field Event Marketing + VS-140 Field Sales/Route-to-Market
Force Management), the largest family. Each gap had been previously overlooked because it was a
genuinely-unowned *shared-service or B2B-growth discipline* whose defining terms appeared in zero
or near-zero PA files as dedicated workflow headers, with only incidental references to the
broader capability scattered across multiple adjacent value streams. None of the four follows the
single-workflow-elevation pattern of Passes 1/5/7/8/10/11; all four are genuinely-unowned
disciplines with no dedicated owner. After the twelve prior passes had filled the genuinely-
uncovered *operational*, *statutory*, *strategic*, *cross-cutting-management*, and *technology*
capabilities across every family, the remaining genuinely-uncovered capabilities are the
*shared-service and B2B-growth* disciplines (product-content, integrated facilities, B2B
field/event marketing, field-sales force) that naturally live in Technology & Data, Asset &
Infrastructure, and Sell & Serve.

Pass 12 deliberately strengthened three of the four thinnest-by-workflow families — **People**
(242 → 266 via VS-134 OCM), **Technology & Data** (278 → 302 via VS-135 TBM/FinOps), and **Make &
Move** (355 → 379 via VS-136 network design/MEIO) — and added the cross-cutting **Operational
Excellence/CI** discipline to **Governance & Assurance** (720 → 744 via VS-133), where strategic,
cross-cutting management/improvement disciplines (VS-33 strategy, VS-36 governance) naturally
live. Each gap had been previously overlooked because it was a genuinely-unowned *enterprise-
management discipline* whose defining terms appeared in zero PA files as dedicated workflow
headers (process mining / operational excellence / continuous improvement; change management / OCM
/ adoption; finops / cloud cost / TBM / IT financial management; multi-echelon / inventory
optimization / network design), with only incidental single-step references to the broader
capability scattered across multiple adjacent value streams. None of the four follows the single-
workflow-elevation pattern of Passes 1/5/7/8/10/11; all four are genuinely-unowned enterprise-
management disciplines with no dedicated owner.

Pass 4 deliberately strengthened the three thinnest operating families: **People** (the
thinnest at 4 value streams) received +2, and **Plan & Source** and **Governance & Assurance** each
received +1. Pass 5 added one value stream to each of four families (Plan & Source, Sell & Serve,
Finance, and Asset & Infrastructure — the last being the thinnest by value-stream count), targeting
capabilities that existed only as single workflows within another value stream (SCF / commodity
hedging / key account / own-generation) or were conflated with an adjacent covered one. Pass 6
concentrated both new value streams in each of the two thinnest families by *workflow count* —
**Make & Move** (307 → 355, +48 via VS-110 Freight + VS-111 Packaging/RTI) and **Asset &
Infrastructure** (152 → 200, +48 via VS-109 Remodel + VS-112 PMO) — targeting capabilities that were
genuinely uncovered (remodel execution, packaging/pallet/RTI engineering), sprinkled across
multiple value streams (freight-spend/carrier), or conflated with the financial-accounting view
of an asset (capex accounting vs project-portfolio governance).

Pass 7 deliberately strengthened the thinnest family by workflow count — **Technology & Data**
(182 → 230, +48 via VS-113 Enterprise Architecture + VS-115 Calibration/Metrology) — and added one
value stream each to **Governance & Assurance** (576 → 600 via VS-114 DG/Hazmat Compliance) and
**Finance** (435 → 459 via VS-116 Surety/Bank Guarantee). Each gap had been previously overlooked
because it was genuinely uncovered by every value stream ('enterprise architecture' appeared in
zero PA files), referenced across many PA files with no dedicated owner (calibration/metrology
across 53 files), conflated with a fixed-site HSE capability (DG transport/ecommerce/regulatory vs
VS-24.3 storage safety), or reduced to single steps within B2G/B2B/treasury value streams
(performance bonds/surety in VS-46/VS-11/VS-18).

Pass 8 added one value stream each to **Finance** (459 → 483 via VS-118 Revenue Assurance),
**Asset & Infrastructure** (200 → 224 via VS-120 Energy Efficiency/RA 11285), and two to
**Governance & Assurance** (600 → 648 via VS-117 DTI-BPS Certification + VS-119 Ethics/Speak-Up).
This pass concentrates in Governance & Assurance and Finance because the remaining genuinely-
uncovered capabilities — after the thinner families (People, Technology & Data, Make & Move) were
substantially strengthened in Passes 4–7 — are statutory product-certification, revenue-leakage
protection, corporate-ethics/speak-up, and energy-efficiency compliance programs that naturally
live in those two families. Three of the four gaps (VS-117 elevating W447, VS-118 elevating W348,
VS-119 extending W2943) follow the Pass-1/Pass-5/Pass-7 pattern of elevating a single workflow to
a dedicated end-to-end program; the fourth (VS-120) is a genuinely-uncovered statutory program.

The 96 new workflows added in Pass 8 are currently **unclassified** (counted in the
unclassified total) and will be tier-assigned in a follow-up criticality review, exactly as the
Pass 1 (VS-89–VS-92), Pass 2 (VS-93–VS-96), Pass 3 (VS-97–VS-100), Pass 4 (VS-101–VS-104),
Pass 5 (VS-105–VS-108), Pass 6 (VS-109–VS-112), and Pass 7 (VS-113–VS-116) batches were handled.
Several Pass 8 workflows are anticipated Tier 1 (DTI-BPS regulated-product gating/ICC-sticker/
market-surveillance controls, revenue-assurance pricing/promo/loyalty/refund/settlement integrity
and leakage-recovery controls, speak-up confidentiality/retaliation-protection/investigation-
independence controls, and RA 11285 designated-establishment/audit/reporting controls).

Pass 9 deliberately strengthened the thinnest family by workflow count — **People** (194 → 242,
+48 via VS-121 Talent Acquisition/Employer Brand & Candidate Experience + VS-123 Skilled-Trade
Apprenticeship/Vocational Education & Capability Pipeline) — and added one value stream each to
**Plan & Source** (356 → 380 via VS-122 Global Sourcing/Import Buying & Sourcing Agent Management)
and **Sell & Serve** (1,122 → 1,146 via VS-124 Sales Enablement/Product Knowledge Mastery &
Clienteling). Each gap had been previously overlooked because it was genuinely uncovered — the
defining terms 'candidate experience'/'career site'/'talent community', 'global sourcing'/'sourcing
agent'/'overseas buying office', 'apprenticeship program', and 'clienteling' each appeared in **zero**
PA files — with only incidental single-workflow references to the broader capability (employer
brand in 3 PA files, vocational/TESDA participation in 4, product knowledge in 33 with no dedicated
owner). After Passes 1–8 had filled the genuinely-uncovered *operational* and *statutory*
capabilities across Make & Move, Asset & Infrastructure, Technology & Data, Finance, and
Governance & Assurance, the remaining genuinely-uncovered capabilities are the *strategic
people-attraction and selling-effectiveness* disciplines that naturally live in People, Plan &
Source, and Sell & Serve. None of the four follows the single-workflow-elevation pattern; all four
are genuinely-uncovered strategic disciplines with no dedicated owner.

The 96 new workflows added in Pass 9 are currently **unclassified** (counted in the
unclassified total) and will be tier-assigned in a follow-up criticality review, exactly as the
Pass 1–Pass 8 batches were handled. Several Pass 9 workflows are anticipated Tier 1 (candidate
consent/RA 10173 and equal-opportunity controls in VS-121, sourcing sanctions/ABC and
import-vendor trade-compliance gating controls in VS-122, TESDA/DOLE apprenticeship-compliance
and trade-safety controls in VS-123, and clienteling RA 10173/associate-fairness and selling-
quality controls in VS-124).

Pass 10 added value streams to three families — **Finance** (483 → 507 via VS-125 Fraud
Management), **Technology & Data** (230 → 278 via VS-126 Customer Data Platform + VS-128 AI/ML
Governance, strengthening the thinnest-by-workflow family), and **Plan & Source** (380 → 404 via
VS-127 S&OP/IBP). Each gap had been previously overlooked because the capability was genuinely
unowned as a program — its defining terms appeared in zero or near-zero PA files ('fraud
orchestration', 'customer golden record', 'integrated business planning'/'IBP', and 'model risk
management'/'algorithmic fairness' respectively) with only incidental single-step references to the
broader capability scattered across multiple adjacent value streams (VS-23/VS-32/VS-58/VS-80/VS-13.2/
VS-118/VS-86 for fraud; VS-13/VS-29/VS-107/VS-10/VS-75 for the customer view; VS-02/VS-101/VS-33/
VS-106 for planning; VS-30.2/VS-27.3/VS-91/VS-113/VS-21 for AI). None of the four follows the
single-workflow-elevation pattern of Passes 1/5/7/8; all four are genuinely-unowned programs.

The 96 new workflows added in Pass 10 are currently **unclassified** (counted in the
unclassified total) and will be tier-assigned in a follow-up criticality review, exactly as the
Pass 1–Pass 9 batches were handled. Several Pass 10 workflows are anticipated Tier 1 (chargeback
representment/recovery and deduction-authorization/SoD controls in VS-125, identity-resolution/
consent-at-activation/DSAR controls in VS-126, demand-consensus/single-number-plan controls in
VS-127, and model-validation/fairness-testing/human-oversight/GenAI controls in VS-128).

---

## 5. Validation

`07-methodology/validate-repo.sh` passes with **0 errors** after the additions:

- Grand total (5,341) matches actual PA workflow header count (5,341). ✅
- All 2,776 classified workflow IDs resolve to a header. ✅
- All 2,588 unclassified workflows carry a keyword-driven proposed tier (workflow-criticality-proposed.md); 0 unclassified workflows remain without a proposal. ✅
- No dangling workflow references in cross-reference docs. ✅
- No placeholder/skeleton workflow content. ✅
- All cross-document counts reconciled (README, executive-summary, value-stream-index,
  workflows/README, criticality classification, dependency map, touchpoint map,
  requirement-workflow-matrix). ✅

---

## 6. Remaining (deferred) gaps

- **Dark Store & Micro-Fulfillment (former VS-49)** and **Cooperative/Community Procurement (former
  VS-52)** — **filled** by VS-93 and VS-94 (Pass 2). No retired-number gaps remain. The retired VS
  numbers (49, 50, 51, 52) stay unused.
- **Marketplace Operator & Third-Party Seller Management** and **Equipment Leasing & Capital
  Equipment Finance** — **filled** by VS-95 and VS-96 (Pass 2).
- **Corporate Real Estate & Property Portfolio**, **Contingent & Outsourced Workforce**, **IT
  Asset & Technology Lifecycle**, and **Legal Operations/Litigation & IP** — **filled** by VS-97,
  VS-98, VS-99, and VS-100 (Pass 3); these four gaps had been previously overlooked because each
  was conflated with an adjacent covered capability (lease administration, employee HR, fixed-asset
  accounting, and corporate-governance/compliance/records respectively).
- **Merchandise Financial Planning/OTB**, **Compensation/Benefits/Total Rewards**, **HR Shared
  Services/EX/People Analytics**, and **Government Affairs/Industry Relations** — **filled** by
  VS-101, VS-102, VS-103, and VS-104 (Pass 4); as with Pass 3, each had been conflated with an
  adjacent covered capability (assortment/supply/corporate-budget, payroll processing, the
  employee lifecycle, and LGU/regulatory/labor-advocacy respectively).
- **Supply Chain Finance & Working Capital**, **Commodity & Input-Cost Risk**, **Strategic Key
  Account & Enterprise Customer**, and **On-Site Renewable Energy & Prosumer** — **filled** by
  VS-105, VS-106, VS-107, and VS-108 (Pass 5); each had existed only as a single workflow within
  another value stream (W324 SCF in VS-18, the incidental commodity-hedging reference, the
  sprinkled key-account mentions across VS-11/VS-43/VS-46, and the W111/W173 energy/solar
  monitoring workflows) or was conflated with an adjacent covered capability.
- **Store Remodel/Renovation/Lifecycle Refurbishment**, **Freight Procurement/Carrier
  Management/Freight Audit**, **Packaging/Pallet/RTI Management**, and **Corporate Project &
  Program Management Office (PMO)** — **filled** by VS-109, VS-110, VS-111, and VS-112 (Pass 6);
  each had been genuinely uncovered (remodel execution, packaging/pallet/RTI engineering), sprinkled
  across multiple value streams (freight-spend/carrier across VS-02.2/VS-04/VS-06.1/VS-06.3), or
  conflated with the financial-accounting view of an asset (capex accounting in VS-40 vs
  project-portfolio governance).
- **Enterprise Architecture/Application Portfolio/Technology Strategy**, **Dangerous Goods/Hazmat
  Transport/Ecommerce/Regulatory Compliance**, **Calibration/Metrology/Measurement Traceability**, and
  **Performance Bond/Surety/Bank Guarantee Management** — **filled** by VS-113, VS-114, VS-115, and
  VS-116 (Pass 7); each had been genuinely uncovered by every value stream ('enterprise architecture'
  in zero PA files), referenced across many PA files with no dedicated owner (calibration/metrology
  across 53 files), conflated with a fixed-site HSE capability (DG transport vs VS-24.3 storage), or
  reduced to single steps within B2G/B2B/treasury value streams (performance bonds/surety).
- **DTI-BPS Product Standards Certification & PS Mark/ICC Compliance**, **Revenue Assurance/Pricing
  Integrity/Leakage Management**, **Whistleblower/Ethics & Corporate Integrity (Speak-Up) Program**,
  and **Energy Efficiency & Conservation & RA 11285 Compliance** — **filled** by VS-117, VS-118,
  VS-119, and VS-120 (Pass 8); three were elevations of a single workflow to a dedicated program
  (W447 DTI-BPS in VS-22.1, W348 Revenue Assurance in VS-21.3, W2943 ABC-Whistleblower in VS-86.3)
  and one was genuinely uncovered with only incidental references (RA 11285 energy-efficiency
  compliance across 14 PA files with zero dedicated headers).
- **Talent Acquisition/Employer Brand & Candidate Experience**, **Global Sourcing/Import Buying &
  Sourcing Agent Management**, **Skilled-Trade Apprenticeship/Vocational Education & Capability
  Pipeline**, and **Sales Enablement/Product Knowledge Mastery & Clienteling** — **filled** by
  VS-121, VS-122, VS-123, and VS-124 (Pass 9); all four were genuinely uncovered strategic
  disciplines whose defining terms ('candidate experience'/'career site'/'talent community',
  'global sourcing'/'sourcing agent'/'overseas buying office', 'apprenticeship program', and
  'clienteling') each appeared in zero PA files, with only incidental single-workflow references to
  the broader capability (employer brand in 3 files, vocational/TESDA participation in 4, product
  knowledge in 33 with no dedicated owner).
- **Cross-Channel Fraud Management & Payment Fraud Protection**, **Customer Data Platform/Single
  Customer View & Identity Resolution**, **Sales & Operations Planning (S&OP) & Integrated Business
  Planning**, and **AI/ML Governance & Responsible AI** — **filled** by VS-125, VS-126, VS-127, and
  VS-128 (Pass 10); all four were genuinely-unowned programs whose defining terms ('fraud
  orchestration', 'customer golden record', 'integrated business planning'/'IBP', and 'model risk
  management'/'algorithmic fairness') appeared in zero or near-zero PA files, with only incidental
  single-step references to the broader capability scattered across multiple adjacent value
  streams.
- **Competition & Antitrust Compliance (RA 10667/PCC)**, **Corporate Development/M&A/Divestiture**,
  **Human Rights/Responsible Supply Chain DD**, and **Corporate Political Engagement/Election
  Compliance** — **filled** by VS-129, VS-130, VS-131, and VS-132 (Pass 11); one was an elevation
  of a single workflow (W2683 competition-law compliance in VS-76.2 → VS-129) and three were
  genuinely uncovered disciplines whose defining terms ('merger and acquisition'/'divestiture',
  'human rights'/'modern slavery', 'political contribution'/'election compliance'/'COMELEC') each
  appeared in zero (or only one incidental) PA file.
- **Operational Excellence/Process Mining/Continuous Improvement**, **Organizational Change
  Management/Digital Adoption**, **Technology Business Management/FinOps**, and **Supply Chain
  Network Design/Multi-Echelon Inventory Optimization** — **filled** by VS-133, VS-134, VS-135,
  and VS-136 (Pass 12); all four were genuinely-unowned enterprise-management disciplines whose
  defining terms appeared in zero PA files as dedicated workflow headers.
- **PIM/DAM, Integrated Facilities Management, Trade Show/Field Event Marketing, and Field
  Sales/Route-to-Market Force Management** — **filled** by VS-137, VS-138, VS-139, and VS-140
  (Pass 13); all four were genuinely-unowned shared-service/B2B-growth disciplines whose defining
  terms appeared in zero or near-zero PA files as dedicated workflow headers.
- **Employee Transport/Shuttle/Daily Commute Management** and **Cash-on-Delivery (COD)
  Operations/Driver Cash Handling & Reconciliation** — **filled** by VS-141 and VS-142 (Pass 14);
  both were genuinely-unowned disciplines whose defining terms appeared in zero PA files as
  dedicated workflow headers and had been conflated with adjacent covered capabilities (business
  travel/goods fleet/facilities for transport; acquirer settlement/last-mile/in-store cash for COD).
- **Bulky & White-Goods Delivery/Installation/Haul-Away/Recycling**, **Employee Accommodation/
  Dormitory/Staff Housing**, **Garden Center/Live Goods/Plant Nursery**, and **Customer Mystery
  Shopping/Service Quality Assurance** — **filled** by VS-143, VS-144, VS-145, and VS-146 (Pass 15);
  all four were genuinely-unowned operational disciplines whose defining terms appeared in zero
  PA files as dedicated workflow headers and had been conflated with adjacent covered capabilities
  (generic last-mile/install/returns/waste for bulky delivery; daily commute/commercial facilities/
  real estate for housing; hard-goods inventory/standard replenishment/store waste for live goods;
  reactive CX/self-reported store standards/financial audit/process improvement for service-quality
  assurance).
- **Auto-ID/Barcode/RFID/Price-Tag Labeling & EAS Operations**, **Corporate Social
  Responsibility/Foundation & Community Investment**, and **In-Store Value-Added Services &
  Financial Agency Operations** — **filled** by VS-151, VS-152, and VS-156 (Pass 17); three
  genuinely-uncovered operational disciplines whose defining terms appeared in zero or near-zero
  PA files as dedicated workflow headers with no dedicated owner (auto-ID/labeling scattered across
  VS-29/VS-71/VS-08/VS-23/VS-115; CSR referenced ~58 times but never owned; bills-payment/e-money
  at 0–2 references).
- **Captive Insurance/Reinsurance & Enterprise Risk Financing**, **Home Construction Finance/Loan
  Brokerage & Mortgage Referral**, and **Trade-In/Buy-Back & Certified Pre-Owned Product Resale**
  — **filled** by VS-153, VS-154, and VS-155 (Pass 17); the three capabilities previously flagged
  as future business-model extensions in this section, now activated within BuildRight's retail
  charter (captive = own risk-financing vehicle; construction finance = broker/referral not lending;
  resale = certified pre-owned not an open C2C marketplace).
- **Revenue Recognition (PFRS 15) & Complex Contract Accounting**, **Product Costing, Landed-Cost &
  Cost Accounting**, **Corporate Security, Executive Protection & Travel Risk Management**, **Global
  Mobility, Immigration & Foreign Worker Compliance**, and **Third-Party & Supplier Risk Management
  (TPRM)** — **filled** by VS-157, VS-158, VS-159, VS-160, and VS-161 (Pass 18); five further
  genuinely-unowned disciplines surfaced by re-running the gap methodology after Pass 17 — two
  single-workflow elevations (W487 revenue recognition in VS-15.1; W85 product costing in VS-17.4),
  one scattered-slice consolidation (TPRM across VS-21/VS-86/VS-91/VS-119/VS-125), and two
  genuinely-uncovered programs (corporate security/executive protection; immigration/global
  mobility), each with defining terms in zero PA files as dedicated workflow headers.
- **Customer Pickup Truck & Cargo Van Rental (Self-Haul) Operations**, **Electric Vehicle (EV) Charging Station Host Network Operations**, and **Smart Locker & Automated Parcel Collection Network** — **filled** by VS-162, VS-163, and VS-164 (Pass 19); three further genuinely-unowned operational disciplines surfaced by re-running the gap methodology after Pass 18, each with defining terms in zero PA files as dedicated workflow headers and each conflated with an adjacent covered capability (self-haul rental conflated with the goods delivery fleet / tool rental / delivery services / employee transport; EV charging conflated with own-consumption renewable generation / own energy efficiency / own diesel fleet fueling; smart lockers conflated with the BOPIS counter transaction / in-store unattended selling tech / fulfillment / returns).
- **PCAB Contractor Licensing & RA 4566 Construction Contractor Compliance**, **Regulatory License, Permit & Accreditation Portfolio Management**, and **Workforce Background Screening, Credentialing & Personnel Vetting** — **filled** by VS-165, VS-166, and VS-167 (Pass 20); three further genuinely-unowned operational disciplines surfaced by re-running the gap methodology after Pass 19. VS-165 is a genuinely-uncovered statutory licensing regime (every existing PCAB reference verifies *someone else's* license — customer trade-pro W590, vendor/contractor eligibility W162, employee tracking VS-19.4 — never BuildRight's own contractor license under RA 4566). VS-166 is a scattered-slice consolidation following the VS-161 TPRM pattern (each compliance domain owned its permit-execution slice — VS-22/76/79/114/117/138/165/46/06 — but no value stream owned the unified cross-domain license/permit register, renewal calendar, and compliance dashboard across ~205 sites). VS-167 is a scattered-slice consolidation following the same pattern (workforce vetting existed only as the single contingent-only W3223 slice in VS-98, plus an onboarding step in VS-121 and license-only driver checks W1400 — no value stream owned the unified cross-category screening program, screening-vendor governance, consent/RA 10173 compliance, adverse-action due process, and ongoing re-screening).
- **In-Store Audio, Ambient Media & Music Royalty Licensing** and **Employee Uniform, Workwear & PPE-Issuance Program** — **filled** by VS-168 and VS-169 (Pass 21); two further genuinely-unowned operational disciplines surfaced by re-running the gap methodology after Pass 20. VS-168 owns the always-on in-store ambient channel (background music, PA/paging, digital signage content, ambient scent) plus the statutory FILSCAP/RA 8293 music-royalty licensing program — its defining terms appeared in zero PA files as dedicated headers and it had been conflated with the single PA-announcement *step* inside VS-07 store daily management (plus one incidental FILSCAP system-list mention), VS-14 brand/marketing, VS-48 vendor-paid retail media, VS-138 facilities, and VS-27 IT. VS-169 owns the unified uniform/workwear/PPE operating model (standards, branded-apparel sourcing, PPE issuance/fit/laundering, sizing, damage/loss, role-change & separation return, multi-entity, sustainability, analytics) — 'uniform' was referenced incidentally across ~29 PA files with no dedicated owner and it had been conflated with VS-19's one onboarding-kit step, VS-24's PPE *requirement*, VS-102's allowance, VS-98's contingent-worker governance, and VS-34's transactional procurement.
- **Inventory Pledge, Asset-Based Lending & Trust-Receipt (Warehouse-Receipt) Financing**, **Customer Pickup, Loading Zone & Will-Call Counter Operations**, and **Third-Party Installer & Contractor Network (Pro-Referral) Management** — **filled** by VS-170, VS-171, and VS-172 (Pass 22); three further genuinely-unowned operational disciplines surfaced by re-running the gap methodology after Pass 21. VS-170 is genuinely-uncovered — 'borrowing base', 'asset-based lending', 'trust receipt', 'field warehouse', and 'notional pool' each appeared in **zero** PA files, with the only adjacent coverage being the single treasury **W319** (facility/covenant contract in VS-18.1, not the collateral operations beneath it) plus import-LC **W232** and demurrage **W249**; no value stream owned the inventory-pledge / ABL borrowing-base / **PD 115 trust-receipt** / warehouse-receipt collateral-operations discipline. VS-171 is a scattered-slice consolidation (the VS-161 TPRM / VS-166 license-portfolio pattern): the customer bulky-pickup & loading-bay discipline existed only as **W1193** (buried in VS-07.3 Store Receiving & Replenishment), **W773** (VS-09.3 will-call), and **W4805** (VS-164.2 pickup journey) — no value stream owned the end-to-end customer bulky-pickup, loading-bay, and will-call counter operating model. VS-172 is a single-workflow elevation (the Pass 1/5/7/8/10/11 pattern): the only dedicated workflow was **W1472** (Trade Account Referral Program / Contractor Network in VS-11.1), elevated here to the end-to-end installer-network & pro-referral program (vetting, matchmaking, referral economics, performance, warranty, PCAB/insurance monitoring).
- **Investor Relations, Capital Markets & Securities Disclosure** — **filled** by VS-173 (Pass 23); one further genuinely-unowned corporate-finance discipline surfaced by re-running the gap methodology after Pass 22. VS-173 is a scattered-slice consolidation (the VS-161 TPRM / VS-166 license-portfolio pattern): the investor-relations / capital-markets / securities-disclosure program existed only as the scattered single workflows **W327** (dividend *payment* in VS-18.1 — the cash mechanic, not the dividend program or shareholder services), **W482** (ASHM *logistics/admin* in VS-17.1, not the investor/proxy/disclosure content), **W4684** (AGM *security* in VS-159, not the investor-facing event), **W4524** (foundation *annual report* in VS-152, not the group), and **W3373** (policy/industry *analyst* relations in VS-104, not financial-analyst/investor relations); the defining terms ('investor relations', 'SEC reporting', 'securities disclosure', 'sell-side analyst', 'credit rating agency', 'proxy statement', 'cap table') each appeared in **zero** PA files as dedicated headers — no value stream owned the end-to-end IR program, securities/SEC disclosure, insider-trading compliance (RA 8799), share register/cap-table, and dividend/shareholder-services discipline.
- **Self-Storage, Portable Container & Mobile-Storage Operations**, **Propane, LPG Cylinder Exchange & Gas Refill Operations**, and **Blueprint, Reprographics & Large-Format Plan Printing Services** — **filled** by VS-174, VS-175, and VS-176 (Pass 24); three further genuinely-unowned *customer-facing value-added service* disciplines surfaced by re-running the gap methodology after Pass 23. All three had their defining terms appear in **zero** PA files as dedicated workflow headers and in **zero** VS directory names, with only a single incidental reference (or none): VS-174 (self-storage — conflated with VS-04 merchandise warehousing, VS-77 jobsite staging, VS-164 small-parcel lockers, VS-111 BuildRight's own pallets, VS-97 the store/DC portfolio, and VS-162 vehicle rental; no value stream owned the *customer storage-rental operating model*), VS-175 (propane/LPG — only the single **W1063** *welding*-gas workflow in VS-09.1 as the incidental reference, conflated with VS-114 DG, VS-111 RTI, VS-24/VS-147 safety, and VS-12/VS-38; no value stream owned the *LPG cylinder-exchange & refill operating model*), and VS-176 (blueprint/reprographics — conflated with VS-66 design creation, VS-14 BuildRight's own promo print, VS-09 physical fabrication, and VS-46/VS-11 bid-set consumption; no value stream owned the *reprographics service operating model*).
- **Field Retail Operations, Regional/District Management & Multi-Store Retail Execution Network** — **filled** by VS-177 (Pass 25); one further genuinely-unowned operational discipline surfaced by re-running the gap methodology after Pass 24. VS-177 is a single-workflow-elevation + scattered-slice-consolidation candidate (the combined Pass-1/5/7/8/10/11/22/23 and VS-161/166/171 patterns): the **Regional Manager** role already appears as the accountable/informed party across **~66 PA files** (VS-07/VS-37/VS-109/VS-146/VS-23) yet the field-management discipline existed only as the scattered single workflows **W1030** (VS-07.1), **W2369** (VS-63.2), **W3836** (VS-124), and **W1214**; the defining terms 'field retail', 'field operations', 'retail execution', 'multi-store management', 'store operations support', 'store support center', 'store hotline', 'store escalation', 'district manager', 'field coach', 'store turnaround', and 'new-store stabilization' each appeared in **zero** PA files as dedicated workflow headers — no value stream owned the *field-management operating model* (distinct from VS-07 single-store ops, VS-33 strategy, VS-63 HQ→store broadcast, and VS-146 independent assurance).
- **Landbanking (VS-178)**, **EPR Compliance (VS-179)**, **Disaster Relief Logistics (VS-180)**, and **B2B Developer Escrow Financing (VS-181)** — **filled** by VS-178, VS-179, VS-180, and VS-181 (Pass 26) as part of the operational catalog expansion to cover these key corporate capabilities.
- **B2B Bulk-Project Custom Import (Indent Sourcing & Brokerage Operations)**, **Dual Training System (DTS) & TESDA Partnership Program**, **Post-Disaster Store Infrastructure Reconstruction & Rehabilitation**, and **B2B Cooperative Credit & Procurement Partnerships** — **filled** by VS-182, VS-183, VS-184, and VS-185 (Pass 27) as part of the operational catalog expansion to cover custom imports, vocational training partnerships, store reconstruction, and cooperative wholesale credit partnerships.
- **Operational Technology (OT) / ICS Cybersecurity & Retail Technology Asset Protection** — **filled** by VS-190 (Pass 29); genuinely uncovered with **zero** dedicated workflow headers across the entire repository for its defining terms ('operational technology security', 'OT cybersecurity', 'ICS security', 'SCADA security', 'IEC 62443', 'NIST SP 800-82'). VS-27.3 owns IT cybersecurity, VS-138 operates the BMS, VS-163/VS-164/VS-149 operate their connected-device channels, VS-115 calibrates measurement devices, VS-23 operates CCTV/EAS, VS-99 owns IT asset lifecycle — none owned the *cross-domain OT/ICS cybersecurity operating discipline* (asset inventory & IT/OT segmentation, OT-aware monitoring/vulnerability/patch/incident-response with fail-secure safety-preserving procedures, OT third-party remote-access, OT cyber supply-chain/SBOM, IEC 62443/NIST 800-82/BSP/NPC compliance).
- **Customer Construction Debris, Demolition Waste & Site Cleanup Operations** — **filled** by VS-191 (Pass 29); a single-workflow elevation of **W1086** (Customer Construction Waste Disposal & Skip/Dumpster Rental Coordination in VS-09.1) following the Pass-1/5/7/8/10/11/22/23/25 pattern. VS-73 (store's own operational waste), VS-187 (household hazardous take-back at the store counter), VS-143.3 (old-appliance haul-away), VS-111 (own inbound packaging/RTI), VS-179 (EPR plastic packaging), VS-90 (transit damage claims), VS-109/VS-20 (debris from BuildRight's own store construction) cover adjacent ground but none owned the *customer jobsite debris hauling & site cleanup service* (service product/pricing, volume estimation, pre-job hazard & regulated-material assessment, crew/container dispatch, DENR-compliant C&D transporter permitting & manifest, multi-stream diversion routing, settlement, ESG/DENR/LGU reporting).
- **Green Fleet Transition, Electric Vehicle (EV) Fleet Operations & Sustainable Transportation** — **filled** by VS-192 (Pass 30); genuinely uncovered with **zero** dedicated workflow headers across the entire repository for its defining terms ('fleet electrification', 'electric fleet', 'EV fleet', 'green fleet', 'fleet decarbonization'), and in fact self-acknowledged as a forward-referenced need inside VS-163 PA-163.1 step 1 (*"BuildRight's own EV-fleet charging need (VS-06/VS-61 green-fleet transition)"*) without an owning value stream, plus a single VS-25.3 ESG-reporting example mention. VS-06 operates the current diesel fleet, VS-61 owns diesel fuel/cost, VS-163 hosts customer EV charging, VS-108 generates own solar, VS-25 reports the footprint — none owned BuildRight's own *fleet decarbonization transition program* (green-fleet strategy & emissions baseline, electrification-readiness roadmap, EV/alt-fuel procurement & LTO homologation, depot/DC charging & grid coordination, TCO/lifecycle, RA 11697 EVIDA incentives & registration, capital governance, route re-design, daily charging & smart-load, charger O&M, battery SoH/lifecycle, eco-driving & telematics, range-aware dispatch, alt-fuel operations, charging–renewable integration, EV maintenance/roadside, GHG MRV, DOE/LTO/LTFRB compliance, HV/battery-fire DOLE-OSH safety, driver/technician training, 3PL green clauses, charging billing, battery second-life/recycling, performance analytics).
- No further capability gaps are currently outstanding against the model company profile after
  thirty gap-analysis passes. Future business-model changes (e.g., further captive-cell
  expansion beyond the initial risk-financing scope, retail-banking/joint-venture deposit-taking,
  or a full open secondhand C2C marketplace platform) may be re-evaluated in a future revision; the
  three previously-flagged future capabilities (used-material/trade-in resale, customer
  construction-loan brokerage, captive insurance) were **filled in Pass 17** as VS-155, VS-154, and
  VS-153 respectively.

---

*Date: 2026-06-21 · Back to [Workflow Index](README.md) · [Value Stream Index](value-stream-index.md)*

> **Post-batch-13 sweep & item-A charter closure (2026-09-04) — batch 14.** Two passes ran in this
> batch. **(1) A third fresh corpus-wide re-run of the §2 methodology at workflow granularity (~60
> further candidate capabilities across lenses not yet exhausted by batches 8–13 — customer-equipment
> fleets (shopping carts/baskets/flatbeds), corporate communications & media relations, timber/wood
> product chain-of-custody, third-party monetization of store space (concessions/kiosks/cell-sites/
> billboards/subleases), PAS 19 defined-benefit & actuarial program, deemed-sale VAT, ODS/refrigerant
> handling, BFP FSIC & fire-safety organization, PICCS/chemical-control product compliance, raffle &
> promo-permit mechanics, ESL/price-label tech, DC slotting, labor-management systems, cash pooling,
> chargebacks, trade-credit insurance, software-license & open-source compliance, litigation holds,
> BP 344 physical accessibility, lactation accommodation, telco rooftop leases) — found ZERO surviving
> capability gaps**, extending the batch-12/13 corpus-wide verdict: every candidate resolved to a
> dedicated `## W` owner or dissolved under verification (representative adjudications: cart/basket
> fleet lifecycle **W1028**; brand/PR/corporate comms PA-14.3 with W134 crisis communication and W143
> media relations; timber chain-of-custody **W1529**; vending & concessionaire management **W177** +
> concession onboarding/billing **W5505–W5507**; sublease & assignment **W1860** with lessor-side
> accounting **W4421**; signage/billboard permits **W2674**; retirement program design & actuarial
> review PA-102.2 with GL-close pension accounting PA-17.1; deemed-sale output VAT a computed sub-step
> of PA-17.3's VAT reconciliation (W14); ODS recovery standard PA-143.3; multi-site BFP FSIC renewal
> campaigns **W4850**; DTI promo/raffle permits **W427** + the VS-139 event-governance step; telco
> cell-site rooftop leasing = a lessor-side slice of W1860/W177/VS-97 — dissolved; lead-paint =
> construction-waste handling slice of W1086/W236 — dissolved). **(2) The genuine open gap was item A
> on the batch-26 worklist — the ghost-title charter decisions**: 25 uncharted executive/director
> title families cited in workflow Owner/Participants/step cells had no seat in the adopted
> target-state TO. The batch-14 charter sweep ([`07-methodology/fix-ghost-titles-batch14.py`](../../07-methodology/fix-ghost-titles-batch14.py))
> unified **~1,285 occurrences across 137 catalog/model files** on charted seats, each mapping passing
> the two-sided test (charted seat AND remit coverage): trade-sales ghosts (VP Sales 113, Sales
> Director 38, Commercial Director 27, VP Sales & Trade Operations 1) → **Head of Trade / Account
> Management**; legal-compliance ghosts (VP Compliance 75, Legal Head 87) → **VP Legal** (the 864-use
> short form of the charted VP Legal & Compliance); real-estate/engineering ghosts (VP Property 74,
> VP Engineering 53, Director of Real Estate 58, Facilities Director 27, Engineering Director 9,
> Construction Director 5) → **Director, Facilities & Real Estate**; ecommerce ghosts (Ecommerce
> Director 45, VP Ecommerce 27, VP Omnichannel 17, VP Digital Commerce 14, VP Digital 3) → **GM,
> Digital Commerce Inc.**; IT ghosts (VP IT Finance 115 → **FinOps Lead**, IT Director 98 → **CIO**,
> CISO 12 → **IT Security Manager**, VP Innovation 21 → **CIO**); HR/OCM ghosts (HR Director 84, VP
> OCM 68, Chief Transformation Officer 2 → **CHRO**); OpEx ghosts (VP OpEx 45, VP Operational
> Excellence 10 → **COO**); plus Supply Chain Director 56 → **VP Supply Chain**, VP Customer
> Experience 15 → **Head of Customer Service**, VP Govt Affairs 37 → **Government Affairs Manager**,
> Sustainability Director 31 → **Sustainability/ESG Manager**, store-ops variants 13 → **VP Store
> Operations**, Regional Operations Director 4 → **Regional Manager**, and the WSL-003 SVP ladder
> tier → **COO**. The facilities-lead canon is decided (Director, Facilities & Real Estate = the
> seat; Head of Facilities = working-level lead); item F's VP OpEx / VP OCM families closed in the
> same sweep. Ten same-cell executive duplications created by the mapping were hand-trued (the
> batch-26 practice). Canonical totals, classification, required-field completeness and CTL-citation
> coverage are all unchanged — this is an owner-attribution repair, not a structural change; the
> semantic-anchors, matrix-refs and model-docs guards are green, and the validator passes 0 errors /
> 0 warnings across all 68 checks (the new sweep script is listed in the methodology tree).

