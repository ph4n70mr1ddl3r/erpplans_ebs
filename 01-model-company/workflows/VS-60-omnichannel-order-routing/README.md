# VS-60: Omnichannel Order Routing & Fulfillment Orchestration

> **Sell & Serve** · [Value Stream Index](../value-stream-index.md)

---

> **Workload dormant — prepared (CAP-F01/CAP-F04–F09, [capability-sourcing register §4](../../../07-methodology/capability-sourcing-and-engineering-model.md)):** this value stream is the Order Orchestration product's multi-source routing/fulfillment-orchestration workload — with BOPIS store pickup (2026-09-23 (t)/(u), [Online Channel & Capability Registry](../../channel-capability-registry.md) CAP-F01) the only enabled online fulfillment option, every sale completes as a regular POS sale at the customer-selected store and order routing is deterministic (checkout pins the store; no source-selection decision exists). By direction the OMO build squad's 7 seats are **deferred — prepared** (2026-09-23 (ah); sourcing register §4 — the platform's prepared design retained, re-evaluation/stand-up trigger = any second online fulfillment origin (CAP-F04–F09) or a marketplace channel (CAP-C03/C04) enabled) and the multi-source orchestration estate below is the **prepared design held at designed capacity**; the live BOPIS path rides the already-built ecommerce platform's capability-configuration service (registry rule 3) and in-suite order flows; stand-up rides the sourcing register's trigger through W5580 — never a rebuild.

---
## Overview

Manages intelligent routing and orchestration of customer orders across multiple fulfillment sources: stores, DCs, vendor drop-ship, and dark stores. Covers order source selection, split-order management, fulfillment tracking, and optimization. Critical for mixed-basket orders containing items from multiple origins.

> **Routing consumes the capability registry (CAP-F01 enabled):** the routing engine offers only registry-ENABLED fulfillment targets — today that is **store pickup (BOPIS) alone**; disabled capabilities are not routable and their intake endpoints reject. The multi-source orchestration below (DC, vendor drop-ship, dark stores, split orders) is the prepared design for the DISABLED—PREPARED fulfillment options and activates with them per the [Online Channel & Capability Registry](../../channel-capability-registry.md).

## Process Areas

| PA | Name | Workflows |
|---|---|---|
| [PA-60.1](PA-60.1-intelligent-order-routing.md) | Intelligent Order Routing & Source Selection | 8 |
| [PA-60.2](PA-60.2-split-order-fulfillment.md) | Split-Order & Mixed-Basket Fulfillment | 8 |
| [PA-60.3](PA-60.3-fulfillment-performance-analytics.md) | Fulfillment Performance & Optimization Analytics | 8 |
| | **Total** | **24** |

---

*Back to [Value Stream Index](../value-stream-index.md)*
