---title: "Case Study 1: ASTA Color Value Discrepancy at Port"
description: Real-world ASTA color value discrepancy case study — how a paprika shipment with ASTA deviation was resolved through re-testing, root cause analysis, supplier communication, and negotiated settlement.
category: Case Study
keywords:
- ASTA
- color value
- port inspection
- discrepancy
- root cause
- retest---

# Case Study 1: ASTA Color Value Discrepancy at Port

## Background

- **Product:** Paprika Powder, Standard Grade
- **Specified ASTA:** 80–120
- **Quantity:** 1 × 40' FCL (20 MT)
- **Shipment Route:** Qingdao, China → Rotterdam, Netherlands
- **Incoterm:** CIF Rotterdam
- **Shipping Date:** March 2025

## The Issue

The shipment arrived at Rotterdam port on schedule. The buyer's appointed third-party lab (Eurofins) performed incoming inspection on April 2, 2025. Result: **ASTA 71.3** — below the minimum specification of 80.

The buyer immediately filed a formal complaint and requested price compensation of 15%, citing the ASTA shortfall.

## Immediate Response

**Timeline:**

| Time | Action |
|------|--------|
| April 2, 14:30 CET | Buyer emailed COA showing ASTA 71.3 |
| April 3, 09:00 CST | Dinweys QC team acknowledged and initiated CAPA |
| April 3, 10:30 CST | Retained retention samples retrieved from warehouse (same batch) |
| April 4, 09:00 CST | Retention samples sent to SGS Qingdao for independent re-test |
| April 5, 14:00 CST | SGS result: **ASTA 83.7** — within specification |

## Root Cause Analysis

### Hypothesis A: Lab Methodology Difference
Eurofins used **ISO 7541** (aqueous acetone extraction, spectrophotometric at 460 nm). Dinweys and SGS used **ASTA 20.1** (same principle but different solvent-to-sample ratio). Both methods are equivalent per ASTA-ESA reciprocity agreements. Cross-validation found only ±1.5 ASTA points difference between methods — not enough to explain the gap.

**Verdict:** Not the root cause.

### Hypothesis B: Sample Degradation During Transit
The buyer's sampling procedure was reviewed:

1. Samples taken from the **top layer** of the container only
2. Samples placed in a **standard Ziploc bag** (not light-protected or vacuum-sealed)
3. Samples sat in the buyer's receiving office for **4 days at ~22°C** before being sent to Eurofins

**ASTA color value degrades when exposed to:**
- **Light** — carotenoid photo-degradation accelerates rapidly
- **Oxygen** — oxidation of capsanthin and capsorubin
- **Temperature** — rate doubles for every 10°C increase above 15°C

A reconstruction test was performed:

| Condition | ASTA (Day 0) | ASTA (Day 5) | Degradation |
|-----------|:-----------:|:-----------:|:-----------:|
| Control (vacuum-sealed, 4°C, dark) | 85.2 | 83.9 | -1.5% |
| Ziploc bag, 22°C, indirect light | 85.2 | 77.4 | **-9.2%** |
| Ziploc bag, 22°C, direct desk light | 85.2 | 72.1 | **-15.4%** |

### Root Cause Confirmed
**Improper sample handling by the buyer post-sampling** caused accelerated ASTA degradation. The product at time of loading was 85.2 ASTA (above spec minimum of 80). By the time the buyer tested, the sample had degraded 9–15%.

## Corrective Actions

| Action | Owner | Status |
|--------|-------|--------|
| 1. Updated sampling SOP to require **vacuum-sealed, light-protected bags** for all port samples | QC Manager | Implemented April 2025 |
| 2. Added **sampling instruction insert** (bilingual CN/EN) to every export shipment | Warehouse | Implemented May 2025 |
| 3. Included **pre-printed sampling and storage guide** in commercial invoice package | Logistics | Implemented May 2025 |
| 4. Updated sales terms to reference **ASTA 20.1** as the sole dispute-resolution method | Legal | Implemented June 2025 |

## Resolution

After presenting the reconstruction test data and the retention sample SGS report, the buyer accepted that the product met specification **at time of shipment**. A commercial settlement was reached:

- Buyer paid the **full contract price**
- Dinweys provided a **1% volume overrun** (200 kg free goods) in the next order
- Both parties agreed on a **joint sampling protocol** for future shipments

## Lessons Learned

1. **ASTA claims must specify which lab method and sampling protocol were used.** Always reference ASTA 20.1 and request the buyer's sampling procedure upfront.
2. **Retain triple retention samples** (one for seller, one for buyer, one for third-party arbitrator) — this case was won because of the sealed retention sample.
3. **Educate buyers on proper sample handling** — most quality disputes arise from sampling error, not product defect.
4. **Shipping 20 MT to Rotterdam** — the cost of independent re-test (~$180 USD) vs the potential compensation claim (~$4,200 at 15%) made the retention sample program well worth it.

## Supporting Documents

- CAPA Report: [CAPA-2025-004](../quality-control/capa-report.md)
- Retention Sample Log: maintained in QC Archive
- SGS Test Report: SGS-QD-2025-0411
- Customer Correspondence: DIN-2025-0037-CORR

---

> *This case study is based on a real incident. Customer and supplier details have been anonymized. Test data is representative.*
