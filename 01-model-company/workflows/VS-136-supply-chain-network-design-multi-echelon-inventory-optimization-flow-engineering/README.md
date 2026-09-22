# VS-136: Supply Chain Network Design, Multi-Echelon Inventory Optimization & Flow Engineering

> **Make & Move** · [Value Stream Index](../value-stream-index.md)

---

## Overview

Supply Chain Network Design, Multi-Echelon Inventory Optimization (MEIO) & Flow Engineering
workflows for BuildRight Depot Corp. — owning the enterprise **analytical/engineering discipline**
that determines *where* inventory sits, *how much* to hold at each of 4 DCs and 200 stores, and
*how* goods flow across an archipelago with ~40% imports (45–90-day lead times), 35,000 active
SKUs, a 6–8x inventory-turn target, and ~50,000 monthly store-replenishment orders (production-calibrated, per data-volumes §1.1). This is the
discipline that decides whether BuildRight hits its inventory-investment, service-level
(fill-rate, OTIF), and total-landed-cost targets — a 1% inventory reduction releases ~PHP 0.4B of
working capital, and a 1% fill-rate gain materially lifts comp sales.

Today this discipline is **entirely unowned as a program**: VS-02.3 has a single *periodic* network
"review" workflow (W183) and supplier-risk/disruption workflows; VS-02.1 runs operational
*demand forecasting & S&OP*; VS-127 owns the *consensus planning cycle*; VS-05 runs the inventory
*lifecycle*; VS-06 runs *logistics execution* — but no value stream owns the **network-design &
inventory-optimization engineering discipline**: network strategy & modeling, DC footprint/location/
capacity optimization, inbound sourcing-lane & outbound distribution-flow architecture, network
resilience & redundancy design, inventory strategy (postponement, pooling), **multi-echelon
inventory optimization**, safety-stock & service-level optimization, ABC/XYZ-differentiated policy,
slow-mover/obsolescence optimization, network cost-to-serve, simulation/digital-twin stress
testing, and a continuous re-optimization cycle. The defining terms 'multi-echelon', 'inventory
optimization', 'network design', 'safety stock optimization', and 'postponement' appeared in
**zero** PA files as dedicated workflow headers (only the single W183 periodic-review workflow
exists); the discipline is genuinely unowned.

This is distinct from **VS-02 (Supply Planning)** which runs *operational* replenishment and the
S&OP feed (this value stream owns the *analytical network/inventory-engineering* that sets the
parameters those operations consume). It is distinct from **VS-127 (S&OP/IBP)** which owns the
*monthly consensus cycle* (this value stream owns the *structural design* of the network and
inventory policy that the cycle governs). It is distinct from **VS-05 (Inventory Lifecycle)** which
runs inventory *transactions/disposition* (this value stream owns *how much/where* structurally).
It is distinct from **VS-06 (Logistics & Fleet)** which *executes* transportation (this value
stream owns the *lane/flow/network design* those operations run on). Supply chain network design &
MEIO is the *structural-engineering* discipline — distinct from operational planning, consensus
planning, inventory transactions, and logistics execution.

BuildRight's exposure is structural: Philippine island geography, long import lead times, a 4-DC
footprint with one deliberately oversized DC (Clark), and a curated 35K-SKU assortment make
network/inventory positioning the single largest controllable lever on working capital, service
level, and total landed cost — and sub-optimal positioning directly threatens the 6–8x turn and
≥95% on-time-replenishment targets.

---

## Process Areas

| PA | Name | Workflows |
|---|---|---|
| [PA-136.1](PA-136.1-supply-chain-network-strategy-modeling-and-design.md) | Supply Chain Network Strategy, Modeling & Design | 8 |
| [PA-136.2](PA-136.2-multi-echelon-inventory-optimization-and-service-level-engineering.md) | Multi-Echelon Inventory Optimization & Service-Level Engineering | 8 |
| [PA-136.3](PA-136.3-network-and-inventory-performance-analytics-and-re-optimization.md) | Network & Inventory Performance Analytics, Simulation & Continuous Re-Optimization | 8 |
| | **Total** | **24** |

---

*Back to [Value Stream Index](../value-stream-index.md)*
