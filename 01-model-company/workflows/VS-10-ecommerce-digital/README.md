# VS-10: Ecommerce & Digital Channels

> **Sell & Serve** · [Value Stream Index](../value-stream-index.md)

---

## Overview

Ecommerce & digital channels: platform operations, order fulfillment (pickup-only BOPIS), and marketplace & social commerce.

## Why it matters

~42,900 ecommerce orders/month (~515K/yr), 100% BOPIS under the pickup-only mandate (2026-09-23 (d)) — every ecommerce sale completes as a **regular POS sale at the customer-chosen store** (order recall, Online-Prepaid tender + balance, BIR receipt; revenue/VAT via the POS chain per W11), and marketplace integration (Lazada/Shopee) drives omnichannel revenue and customer acquisition. The home-delivery estate is dormant (BCP-reactivatable, per PA-10.2's mandate banner).

## Owner & participants

- **Owner**: GM, Digital Commerce Inc. / Digital

## Process Areas

| PA | Name | Workflows |
|---|---|---|
| [PA-10.1](PA-10.1-ecommerce-platform-operations.md) | Ecommerce Platform Operations | 32 |
| [PA-10.2](PA-10.2-order-fulfillment-and-delivery.md) | Order Fulfillment & Delivery | 20 |
| [PA-10.3](PA-10.3-marketplace-and-social-commerce.md) | Marketplace & Social Commerce | 11 |
| | **Total** | **63** |

## Key dependencies

VS-60 (order routing — consumes the registry: only ENABLED capabilities are routable), VS-08 (POS completion — every ecommerce sale closes as a regular POS sale), VS-04 (DC/dark store — disabled delivery estate), VS-65 (marketplace — disabled-prepared), VS-126 (CDP), VS-13 (CX), [channel-capability-registry](../../channel-capability-registry.md) (capability state governs what is checkoutable/routable)

## Key controls

CTL-47 (payment recon), W266 fraud, W267 chargeback, W473 BIR e-invoicing

---

*Back to [Value Stream Index](../value-stream-index.md)*
