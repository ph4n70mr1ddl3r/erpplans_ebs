# Data Privacy, Records & Master Data Policies (POL-D)

> Domain manual of the [Corporate Policy Manual](README.md). Approval class:
> **CEO** (POL-D01–D04; DPO-owned, NPC-facing per W1735) except POL-D05 Master
> Data Governance (**COO** — operational class). Statutory base: **RA 10173** (Data
> Privacy Act), its IRR and NPC circulars; corporate privacy governance
> executes through **W1735** and the consumer-data-privacy workflows
> ([VS-91](../workflows/VS-91-consumer-data-privacy-protection/), PA-91.1–91.3).

---

## POL-D01 — External Privacy Notice & Consent Management

| | |
|---|---|
| Owner (R) / Approver | Data Protection Officer (DPO) / **CEO** |
| Cadence | 1-year review |
| Anchors | W1735.1(a), W1735.3 (consent program); [PA-91.1](../workflows/VS-91-consumer-data-privacy-protection/) (privacy governance & data-subject rights, W3041–W3046), PA-91.2 (PIA & data mapping, W3049+); the customer-data platform ([VS-126](../workflows/VS-126-customer-data-platform-single-customer-view-identity-resolution/), PA-126.1–126.3) |
| Version | 1.0 — initial issue, 2026-09-25 codification |

**Policy statements.**
1. A plain-language **external privacy notice** governs every personal-data
   collection point: loyalty program, ecommerce checkout (notice + cookie
   consent), CCTV signage at stores/DCs, HR candidate intake, vendor onboarding,
   and Wi-Fi/camera systems — no hidden collection.
2. **Consent is captured, purpose-bound and revocable:** loyalty members
   consent to data collection, marketing communications and profiling at
   enrollment; ecommerce customers see the privacy notice at checkout; consent
   records are timestamped and auditable; withdrawal is as easy as consent and
   honored within statutory timelines.
3. Marketing use of customer data requires the marketing-consent flag — no
   consent, no campaigns; sharing with third parties (marketplaces, logistics
   partners, banks) only under consent or a data-processing agreement
   (POL-D02), never sold. The **CDP/single-customer-view** (VS-126)
   consolidates identity only from consented sources (PA-126.1), and every
   activation/segmentation run (PA-126.2) honors the flag — identity
   resolution never manufactures consent that the source capture lacked.
4. Data-subject rights (access, correction, blocking, complaint) have a
   published intake channel and a DPO-owned response SLA; the log of requests
   and outcomes reports annually.

---

## POL-D02 — Internal Data Protection & NPC Compliance

| | |
|---|---|
| Owner (R) / Approver | DPO / **CEO** |
| Cadence | 1-year review |
| Anchors | W1735.1(b)(c)(d), NPC registration (W1735.2); [PA-91.2](../workflows/VS-91-consumer-data-privacy-protection/) (privacy impact assessment, data mapping & vendor privacy, W3049+) |
| Version | 1.0 — initial issue, 2026-09-25 codification |

**Policy statements.**
1. The DPO is registered with the **National Privacy Commission**; data
   processing systems register and renew annually (W1735.2) — new
   systems/processing undergo **privacy impact assessments** before go-live
   (intake: new ecommerce features, loyalty changes, CCTV rollouts, HR
   analytics, AI agents touching personal data).
2. **Data classification & handling:** personal data (esp. sensitive —
   government IDs, biometrics, health, bank details) is collected only for
   declared purposes, minimized, access-controlled on need-to-know (POL-I02),
   encrypted per POL-I03, and never moved to unmanaged tools (POL-I01).
3. **Data processing agreements** bind every third party processing personal
   data (cloud, logistics, marketplaces, collection agencies, AI platforms):
   purpose limitation, security measures, breach notification duty, subprocessor
   control, deletion on termination (W1735.1(c)).
4. Employee personal data (SSS/PhilHealth/Pag-IBIG, biometrics, CCTV,
   disciplinary records) processes under notified purposes at hire (W1735.3(c));
   HR dashboards and analytics aggregate or mask where individualized access
   is unnecessary.
5. Retention follows POL-D04's schedule — personal data is deleted/anonymized
   when the purpose lapses, not hoarded.

---

## POL-D03 — Personal Data Breach Notification

| | |
|---|---|
| Owner (R) / Approver | DPO / **CEO** (Board notified on material breaches) |
| Cadence | 1-year review + post-breach updates |
| Anchors | W1735 step 4 (72-hour NPC path, 5-day report); [PA-91.3](../workflows/VS-91-consumer-data-privacy-protection/) (breach detection, notification & NPC response, W3057+) |
| Version | 1.0 — initial issue, 2026-09-25 codification |

**Policy statements.**
1. Every suspected personal-data breach reports to the DPO immediately; the
   security-incident track (POL-I05) runs in parallel — containment and privacy
   obligations never wait for each other.
2. **Statutory clock:** within **72 hours** — initial assessment, containment,
   NPC notification if sensitive personal information affects **100+ data
   subjects**; within **5 days** — full breach report to NPC; affected data
   subjects notified when harm is likely; remedial measures documented.
3. The breach log (what, when, scope, subjects, notification, remediation,
   root cause) is DPO-maintained and Audit-Committee-visible; near-misses are
   logged too — they are free lessons.
4. Vendors/processors must notify BuildRight without undue delay per contract
   (POL-D02.3); their delay does not suspend BuildRight's clocks.

---

## POL-D04 — Records Retention, Archiving & Document Control

| | |
|---|---|
| Owner (R) / Approver | Strategy / BPM & Document Control / **CEO** |
| Cadence | 2-year review (schedule re-baselined with BIR/SEC/labor changes) |
| Anchors | [VS-88](../workflows/VS-88-document-control-records-retention/) document control & records retention |
| Version | 1.0 — initial issue, 2026-09-25 codification |

**Policy statements.**
1. A single **retention & disposal schedule** classifies all records (accounting
   books/vouchers: 10 years per BIR practice; contracts: life + limitation
   period; employee 201-files: employment + statutory window; customer data:
   purpose + legal holds) with owner, medium and disposal method per class.
2. Legal-hold rules: litigation, audit, or investigation suspends disposal for
   in-scope records — Legal issues the hold, Document Control enforces it
   centrally.
3. **Document control:** controlled documents (policies, SOPs, work
   instructions, forms) carry version, owner, approval and effective date;
   superseded versions archive (W1729.5(e)); only the portal copy is
   authoritative — printed copies are uncontrolled by default.
4. Disposal is certified (what, when, how — shredding/secure deletion with
   witnesses for sensitive classes); no record leaves retention by personal
   decision, and no record is destroyed under hold.
5. Archiving of system data (EBS fiscal periods, POS journals, email) follows
   the IT archiving runbooks so statutory retrievability survives system
   changes.

---

## POL-D05 — Master Data Governance

| | |
|---|---|
| Owner (R) / Approver | Merch Ops & Master Data Manager / **COO** |
| Cadence | 2-year review |
| Anchors | [VS-29](../workflows/VS-29-master-data/) (item, vendor, customer master); product information & digital assets ([VS-137](../workflows/VS-137-product-information-management-and-digital-asset-management/), PA-137.1–137.3) |
| Version | 1.0 — initial issue, 2026-09-25 codification |

**Policy statements.**
1. Master data (items, vendors, customers, chart of accounts, hierarchies) has
   one system of record and one steward per domain — duplicates and shadow
   lists are defects, not conveniences.
2. **Create/change gates:** new items and vendor/customer changes pass
   data-quality validation (mandatory attributes, tax status, UOM/Barcode,
   hierarchy placement) with maker-checker; the full change audit trail is the
   evidence base for insider-fraud cases (VS-29 canon) and is never disabled.
3. Data quality KPIs (completeness, duplicate rate, hierarchy integrity) report
   monthly; cleansing is scheduled work with root-cause fixes at entry, not
   endless downstream repair.
4. Deletions/merges follow the retention rules (POL-D04) and financial-record
   immutability — transactional history never loses its references.
5. Hierarchy changes (category restructures, store openings/closures) run
   through the governance workflow with downstream-impact checks (pricing,
   replenishment, reporting) before activation.
6. **Product content is master data too** (VS-137): PIM attributes, digital
   assets and SDS/certificate documents follow the same single-steward rule
   (PA-137.1) — channels syndicate from the governed master only (PA-137.3),
   never from local copies; a product page claiming an attribute the master
   does not carry is a data defect, not a marketing convenience.
7. **Customer identity data** obeys the consent chain, not just the steward
   chain: the CDP/single-customer-view consolidation (VS-126) draws only from
   consented sources per POL-D01.3 — master-data merging never manufactures
   consent the source capture lacked, and identity-resolution conflicts
   resolve under this policy's governance workflow like any hierarchy change.
