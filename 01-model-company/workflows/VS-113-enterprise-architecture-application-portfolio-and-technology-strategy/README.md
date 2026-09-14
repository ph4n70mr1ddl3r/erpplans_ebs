# VS-113: Enterprise Architecture, Application Portfolio & Technology Strategy

> **Technology & Data** · [Value Stream Index](../value-stream-index.md)

---

## Overview

Enterprise Architecture, Application Portfolio & Technology Strategy workflows for BuildRight Depot
Corp. — governing the **enterprise design discipline** that keeps the unified ERP platform of record
(Oracle E-Business Suite 12.2) and
its surrounding application landscape coherent, integrated, secure, standards-compliant, and aligned
to business strategy as BuildRight grows from 200 to 300+ stores, expands ecommerce and
marketplace operations, and executes major transformation programs. The model company profile
(§14.1) declares "all legacy systems decommissioned and consolidated" into a single optimized ERP,
yet consolidation is not a one-time event: ~10+ active integration touchpoints (POS ↔ ERP,
Ecommerce ↔ ERP, Payment Gateway, Bank, BIR eFPS, SSS/PhilHealth/Pag-IBIG, Delivery Partners,
Loyalty Engine, WMS RF Guns, Supplier Portal), the surrounding application estate (loyalty
engine, payment gateway, BI, WMS, CRM, retail media, marketplace, storefront, MDM, the 600-POS
estate), the cloud/SaaS commodity portfolio (links to VS-99), and the steady pipeline of digital and
regulatory change (e-invoicing, AI/ML, net-zero, omnichannel evolution) require a continuous
enterprise-architecture discipline. No existing value stream owns this: VS-27 operates and secures
the platforms (IT operations/service management, infrastructure, cybersecurity), VS-28 consumes
data (analytics/BI), VS-30 evaluates emerging tech and runs innovation POCs, and VS-99 manages the
hardware/software asset lifecycle — none designs and governs the enterprise application landscape,
the integration architecture, the technology standards, the solution architecture for new
initiatives, or the multi-year technology strategy. This value stream owns that discipline:
architecture framework, principles, standards and reference architecture; the Architecture Review
Board and solution-architecture review process; application portfolio management and
rationalization, technical-debt management, and application lifecycle/retirement; integration and
API architecture; solution architecture for new projects (links to VS-112 PMO); data, cloud,
infrastructure and security architecture in partnership with the domain owners; the multi-year
technology strategy and roadmap; emerging-technology adoption governance; technology investment
governance and ROI; vendor/platform strategy for enterprise systems; architecture for resilience and
DR; and architecture metrics, portfolio health and continuous improvement.

This is distinct from **VS-27 (IT Operations & Security)** which *runs and secures* the platforms
(service management, infrastructure/platform operations, cybersecurity — this value stream *designs*
the landscape that VS-27 operates). It is distinct from **VS-28 (Data, Analytics & BI)** which
*delivers insight and analytics products* from data (this value stream defines the data architecture
and information strategy in partnership with VS-28.2 data governance). It is distinct from **VS-30
(Innovation & Digital)** which *evaluates emerging technology and runs innovation/POC/AI-ML* (this
value stream governs which emerging tech enters the standard landscape and architects the
transformation programs). It is distinct from **VS-99 (IT Asset & Technology Lifecycle)** which
manages the *hardware/software asset* lifecycle and SAM/license compliance (this value stream
governs the *application portfolio* and whether an application should exist at all). It is distinct
from **VS-112 (Corporate PMO)** which *governs project delivery* (this value stream provides the
solution architecture and standards each project must conform to), and from **VS-33 (Strategic
Planning)** which sets *business strategy* (this value stream translates business strategy into
technology strategy). Enterprise architecture is the *design and governance of the enterprise
technology landscape* — distinct from IT operations, data analytics, innovation, ITAM, project
delivery, and business strategy.

BuildRight's exposure is structural and growing: as a 5-entity, 200-store, PHP 62.3B-revenue
retailer on a unified ERP with an expanding digital perimeter (ecommerce, marketplace, retail
media, mobile app, payments, BIR e-invoicing), the absence of an enterprise-architecture discipline
produces integration sprawl, duplicate/overlapping applications, technical debt, fragile
point-to-point integrations, security gaps from inconsistent patterns, inflated IT spend, project
rework (each project re-decides architecture), and strategic mis-alignment between technology
investment and business capability — risks that no existing value stream owns.

---

## Process Areas

| PA | Name | Workflows |
|---|---|---|
| [PA-113.1](PA-113.1-enterprise-architecture-framework-standards-and-governance.md) | Enterprise Architecture Framework, Standards & Governance | 9 |
| [PA-113.2](PA-113.2-application-portfolio-integration-and-solution-architecture.md) | Application Portfolio, Integration & Solution Architecture | 10 |
| [PA-113.3](PA-113.3-technology-strategy-innovation-governance-and-architecture-analytics.md) | Technology Strategy, Innovation Governance & Architecture Analytics | 9 |
| | **Total** | **28** |

---

*Back to [Value Stream Index](../value-stream-index.md)*
