# VS-110: Freight Procurement, Carrier Management & Freight Audit

> **Make & Move** · [Value Stream Index](../value-stream-index.md)

---

## Overview

Freight Procurement, Carrier Management & Freight Audit workflows for BuildRight Depot Corp. —
governing the **transportation-spend and carrier-relationship discipline** across every leg of the
supply chain: import ocean freight and drayage (~400–600 TEUs/month, profile §7.1), inbound
vendor→DC and direct-store delivery (~72K receipts/year, ~500–600 DSD/month), inter-DC/inter-island
line-haul (W66, ~30–40 transfers/month), DC→store replenishment (~50,000 replenishment orders/month
across a ~80% third-party fleet, profile §7.2), and last-mile/customer delivery (~42.9K ecommerce
orders/month, profile §8). At BuildRight's scale, freight is a major cost line (typically 3–5% of
revenue at PHP-hundreds-of-millions to low-billions annually) and the carrier base, contracts,
rates, routing guides, freight execution, freight audit/payment, landed-cost capture, and freight
analytics span multiple value streams without a single owner. This value stream consolidates the
freight-procurement and freight-financial-management discipline end-to-end: freight category
strategy and sourcing, carrier/3PL contracting and rate management, routing guide and lane
assignment, freight tendering and capacity booking, freight execution and visibility across all
legs, demurrage/detention/accessorial management, inter-island coordination, freight claims,
carrier performance, freight invoice audit and payment, freight cost allocation/chargeback to
entities and landed cost, freight cost-to-serve analytics, fuel/index volatility, and freight risk
and continuity.

This is distinct from **VS-06 (Logistics & Fleet)** which *executes* outbound distribution,
fleet/driver management, and last-mile/3PL daily operations (and where the single workflows W1164
inter-island, W1165 last-mile dispatch, and W1166 carrier-rate/freight-audit today introduce the
freight-financial discipline at a single-workflow level; this value stream decomposes the full
freight-procurement program). It is distinct from **VS-56 (Third-Party Delivery Partner)** which
manages the *3PL delivery-partner relationship* for last-mile customer delivery (a subset of the
broader carrier base) and from **VS-02.2 (Import & Customs)** which handles *customs/compliance and
import documentation* (W66 inter-island, W249 demurrage appear there as import-execution
workflows). It is distinct from **VS-04 (DC & Warehouse)** which *receives/ships* freight at the DC
and from **VS-87 (Customs Trade Compliance)** which handles *tariff/duty compliance*. It is also
distinct from **VS-15 (Procure-to-Pay)** which *processes* the freight invoice as an AP item and
from **VS-72 (Cross-Entity Shared Services)** which *allocates* shared cost. Freight procurement &
carrier management is the *transportation-spend and carrier-relationship* discipline — distinct
from logistics execution, 3PL partner management, import customs, DC operations, customs
compliance, AP processing, and shared-services allocation.

BuildRight's exposure is material and fragmented: import ocean freight, drayage, line-haul, and
last-mile across ~80% third-party carriers and multiple legs/regions/islands; freight spend in the
PHP-hundreds-of-millions-to-low-billions range; and freight cost directly affects landed cost,
gross margin (links to VS-101), and EBITDA. The carrier base, rate structures, routing guides,
freight-audit discipline, and landed-cost analytics required to control this spend are scattered
today across VS-02.2 (import), VS-04 (DC), VS-06.1 (outbound), and VS-06.3 (last-mile) without a
single freight-procurement owner — the same "sprinkled across value streams" pattern that VS-107
(Strategic Key Account) elevated for the customer side.

---

## Process Areas

| PA | Name | Workflows |
|---|---|---|
| [PA-110.1](PA-110.1-freight-sourcing-carrier-contracting-and-rate-management.md) | Freight Sourcing, Carrier Contracting & Rate Management | 8 |
| [PA-110.2](PA-110.2-freight-execution-routing-guide-and-visibility.md) | Freight Execution, Routing Guide & Visibility | 8 |
| [PA-110.3](PA-110.3-freight-audit-payment-and-freight-cost-analytics.md) | Freight Audit, Payment & Freight Cost Analytics | 8 |
| | **Total** | **24** |

---

*Back to [Value Stream Index](../value-stream-index.md)*
