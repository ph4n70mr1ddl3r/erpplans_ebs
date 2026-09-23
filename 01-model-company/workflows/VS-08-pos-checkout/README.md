# VS-08: POS & Checkout

> **Sell & Serve** · [Value Stream Index](../value-stream-index.md)

---

## Overview

POS & checkout: transaction processing, payment & cash management, and POS compliance & controls across 600 terminals.

**Returns routing:** in-store return *decisions* (eligibility, approval tiers, disposition) live in VS-32 (W1622–W1630); this value stream executes the POS refund mechanics (W1538) and fraud screening (W605) — see the [Event Custody & Precedence Register](../event-custody-and-precedence-register.md) (E-09).

**BOPIS completion routing:** ecommerce (BOPIS) orders complete at the pickup store as **regular POS sales** through PA-08.1's standard chain (order recall, Online-Prepaid tender + balance tender, BIR receipt; CTL-47 gateway reconciliation) — the POS tender confirmation closes the online order per W11 (pickup-only mandate, 2026-09-23 (d)).

## Why it matters

2.8M monthly POS transactions / ~PHP 60.5B in-store revenue (of ~PHP 62.3B total company revenue) flow through 600 terminals; pricing/promo/loyalty/discount execution, payment integrity, and BIR e-invoicing originate here.

## Owner & participants

- **Owner**: VP Store Operations / IT Store Systems & POS (SSP)

## Process Areas

| PA | Name | Workflows |
|---|---|---|
| [PA-08.1](PA-08.1-transaction-processing.md) | Transaction Processing | 38 |
| [PA-08.2](PA-08.2-payment-and-cash-management.md) | Payment & Cash Management | 11 |
| [PA-08.3](PA-08.3-pos-compliance-and-controls.md) | POS Compliance & Controls | 12 |
| | **Total** | **61** |

## Key dependencies

VS-07 (stores), VS-29 (pricing master W289), VS-13 (loyalty), VS-32 (returns decisioning — W1622–W1630), VS-58 (coupon campaigns — W539 redemption), VS-79 (BIR), VS-118 (revenue assurance)

## Key controls

CTL-47 (payment recon), CTL-44, W537/541 settlement, W540 BIR credit notes, W553 price-error detection

---

*Back to [Value Stream Index](../value-stream-index.md)*
