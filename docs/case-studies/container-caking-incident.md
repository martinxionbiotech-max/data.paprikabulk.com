---title: "Case Study 2: Caking and Clumping in Container Shipment"
description: Container caking incident case study in paprika shipments — root cause analysis of moisture migration, temperature differentials, preventive measures, and quality protocol updates for bulk spice logistics.
category: Case Study
keywords:
- caking
- clumping
- moisture
- container
- condensation
- logistics---

# Case Study 2: Caking and Clumping in Container Shipment

## Background

- **Product:** Paprika Powder, Premium Grade (ASTA 160–200)
- **Quantity:** 1 × 20' FCL (10 MT)
- **Packaging:** 25 kg PP laminated bags, 400 bags on 10 pallets
- **Shipment Route:** Qingdao, China → Lagos, Nigeria
- **Incoterm:** CIF Lagos
- **Shipping Date:** August 2024 (peak summer, high humidity season)

## The Issue

Upon arrival at Lagos port (35 days transit), the buyer reported that **~60% of bags showed visible caking**. The product could not be emptied freely from the bags — large clumps of 10–20 cm diameter had formed. The buyer declared the shipment partially unfit for use and demanded 30% compensation.

## Initial Assessment

The QC team reviewed documentation:

| Document | Result |
|----------|--------|
| Pre-shipment moisture test | 7.2% (well within ≤10% spec) |
| Pre-shipment packaging inspection | Pass: all bags sealed, pallets stretch-wrapped |
| Container pre-loading inspection | Clean, dry, no odor |
| Bill of Lading | No remarks on container condition |
| Temperature log | **Not available** — container was not equipped with data loggers |

The product left the factory **at specification**. Something happened during the 35-day voyage.

## Root Cause Investigation

### Step 1: Climate Analysis

August–September 2024 shipping route conditions:

| Segment | Duration | Typical Temp | Typical RH |
|---------|:-------:|:-----------:|:----------:|
| Qingdao → Shanghai (loading) | 2 days | 28–32°C | 75–85% |
| Shanghai → Singapore | 7 days | 29–33°C | 75–90% |
| Singapore → Cape Town | 12 days | 22–28°C | 70–80% |
| Cape Town → Lagos | 14 days | 24–30°C | 80–95% |

The route passed through **two high-humidity zones** (East China Sea and Gulf of Guinea) with a total transit of 35 days through tropical conditions.

### Step 2: Container Dew Point Analysis

A standard 20' container experiences **diurnal temperature cycling**:

- Daytime metal container wall temp: up to **45–50°C** in direct sun
- Nighttime: cools to **25–28°C**
- This creates a **dew point breach** — moisture condenses on container walls and the top layer of bags

**The physics:**
The air inside the container at 35°C and 80% RH holds ~32 g/m³ of water vapor. When the container cools to 25°C at night, saturation drops to 23 g/m³. The excess **9 g/m³ condenses as liquid water**. In a standard 20' container (33 m³ airspace), that's ~**300 mL of liquid water per night** — equivalent to pouring a can of soda onto the cargo every night for 35 nights.

Caking is a known phenomenon when paprika powder absorbs just **1.5–2% additional moisture** above its baseline. At 7.2% initial moisture, absorption to 9%+ triggers caking. The condensed water wetted the bag surfaces, moisture migrated inward, and the powder rehydrated enough to bridge particle surfaces.

### Step 3: Packaging Assessment

The PP laminated bags used had:
- Outer PP weave: water-resistant but not waterproof
- Inner PE liner: 0.05 mm thickness
- **Result:** The PE liner proved insufficient under sustained condensation exposure. Moisture vapor migrated through the PP weave and condensed between the liner and the powder surface.

### Root Cause Confirmed

**Thermal cycling in tropical shipping combined with insufficient moisture barrier packaging** caused gradual moisture ingress and powder caking. The primary factor was not pre-shipment quality but logistics conditions.

## Corrective Actions

| Action | Detail | Owner | Status |
|--------|--------|-------|--------|
| 1. **Desiccant protocol** | Add 2× 500g silica gel desiccant bags per pallet, secured inside stretch wrap | Warehouse | Implemented Sep 2024 |
| 2. **Laminated bag upgrade** | Increase PE liner from 0.05 mm to 0.08 mm with metallized outer layer | Procurement | Implemented Oct 2024 |
| 3. **Container pre-cooling** | Pre-cool empty container to 20°C for 2 hours before loading (reduces initial temperature differential) | Logistics | Implemented Sep 2024 |
| 4. **Ventilation protocol** | Reefer container recommendation for tropical destinations (surcharge ~$500); ventilated container as fallback | Sales | Implemented Nov 2024 |
| 5. **Moisture indicator cards** | Place 3M humidity indicator cards at front, middle, and rear of each container | QC | Implemented Oct 2024 |

## Results After Corrective Actions

Monitoring data for subsequent tropical shipments (n=12):

| Metric | Before (Jan–Aug 2024) | After (Sep 2024–Jun 2025) |
|--------|:---------------------:|:------------------------:|
| Caking incidents | 3 of 7 shipments (43%) | **1 of 12 shipments (8%)** |
| Customer complaints re: moisture | 4 | 1 |
| Cost per shipment for desiccants + packaging upgrade | $0 | ~$180 |
| Cost savings per potential claim avoided | $0 | ~$3,000–$6,000 |

The lone post-improvement incident was traced to a container with a **damaged door seal** — now added to the pre-loading checklist.

## Lessons Learned

1. **Never underestimate tropical trade lane risks.** A product that ships fine to Europe or North America may fail on West African or Southeast Asian routes.
2. **Packaging decisions should be route-specific,** not one-size-fits-all. The marginal cost of upgraded packaging + desiccants ($0.02/kg) is trivial compared to claim risk.
3. **Moisture indicator cards cost pennies and provide definitive evidence.** In the single post-fix incident, the indicator cards showed "wet" at the rear door area (near the damaged seal), proving the failure was container-related, not product-related.
4. **Pre-cool the container** — this single step was credited by the logistics partner with reducing the temperature differential by ~60%.

## Supporting Documents

- CAPA Report: [CAPA-2024-012](../quality-control/capa-report.md)
- Container Pre-Loading Inspection Checklist: [container-loading-inspection.md](../quality-control/container-loading-inspection.md)
- Moisture Indicator Card Reading Guide (internal SOP-DIN-QC-024)
- Packaging Specification Revision v3.1 (Oct 2024)
- Shipper's Temperature Data for Route QIN-LOS (China Shipping Logistics, Reference R021-2024)

---

> *This case study is based on a composite of real incidents experienced by Dinweys across multiple tropical trade lanes. Specific details have been generalized.*
