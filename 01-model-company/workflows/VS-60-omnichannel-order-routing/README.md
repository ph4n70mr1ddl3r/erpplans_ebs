# VS-60: Omnichannel Order Routing & Fulfillment Orchestration

> **Sell & Serve** · [Value Stream Index](../value-stream-index.md)

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
