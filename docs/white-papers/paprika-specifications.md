---title: Paprika Specifications Guide
description: Comprehensive paprika specification guide covering physical, chemical, and microbiological parameters for all grades.
category: White Paper
keywords:
- paprika specification
- spec sheet
- quality parameter
- what to check
- procurement---

# Paprika Specifications: A Complete Guide to Reading and Understanding Spec Sheets

## 1. Introduction

A paprika specification sheet (spec sheet or Certificate of Analysis, COA) contains all the technical information needed to evaluate a product. But the numbers only tell half the story — understanding what each parameter means, how it's tested, why it matters, and what constitutes a pass or fail is essential for informed procurement.

This guide walks through every parameter on a typical paprika spec sheet, provides regulatory limit comparisons across major markets, offers a detailed inspection protocol, and explains how to spot inconsistencies or red flags. It covers physical, chemical, microbiological, and contaminant specifications with real-world implications.

---

## 2. Physical Parameters

### 2.1 ASTA Color Value

| Spec Line | Example | Meaning | Pass/Fail |
|-----------|---------|---------|-----------|
| Specification | ASTA 160 min | Product must have at least ASTA 160 | — |
| Test Result | ASTA 178 | This batch: ASTA 178 | ✅ Passes |

**Why It Matters:** The primary quality parameter. Determines coloring power and pricing. See [ASTA Color Value Guide](./asta-color-value-guide.md) for comprehensive methodology.

**Test Method:** ASTA 20.1 / ISO 7541 (acetone extraction, spectrophotometry at 460 nm)
**Typical Tolerance:** ±10 ASTA units from declared value
**Common Specification:** 80–260 ASTA depending on grade

### 2.2 Moisture Content

| Spec Line | Example | Meaning | Pass/Fail |
|-----------|---------|---------|-----------|
| Specification | ≤10% | Product must not exceed 10% moisture | — |
| Test Result | 7.2% | This batch: 7.2% | ✅ Passes |

**Why It Matters:** High moisture promotes microbial growth (mold, yeast), caking, color degradation via enzymatic reactions, and reduced shelf life. Moisture is a Critical Control Point (CCP) under HACCP.

**Test Method:** Loss on Drying (LOD) at 105°C for 3–4 hours (ISO 939, AOAC 925.10)
**Typical Specification:** ≤10% for powder; ≤12% for whole dried pods
**Acceptable Range:** 5–10% (below 5% = over-dried, may have ASTA loss)

**Moisture Impact on Shelf Life:**
| Moisture Content | Mold Risk | ASTA Loss Rate (per year at 20°C) | Recommended Storage |
|-----------------|-----------|----------------------------------|-------------------|
| <5% | Very low | 4–7% | Any sealed container |
| 5–8% | Low | 5–10% | Standard packaging |
| 8–10% | Moderate | 7–12% | Use within 12 months |
| 10–12% | High | 10–18% | Accelerated use, monitor mold |
| >12% | Critical | 15–25% | Reject or process immediately |

**Price Adjustment:** Some contracts include a moisture adjustment formula:
$$\text{Price}_{\text{adjusted}} = \text{Price}_{\text{base}} \times \frac{1 - M_{\text{actual}}}{1 - M_{\text{spec}}}$$

Where M = moisture fraction. For example, if spec is 10% but actual is 12%, the buyer pays for less paprika solids — a 2.2% price reduction.

### 2.3 Particle Size (Mesh/Sieve Analysis)

| Spec Line | Example | Meaning |
|-----------|---------|---------|
| Specification | 95% through 40 mesh | 95% of particles must pass through a 40-mesh sieve (420 μm opening) |
| Test Result | 97.5% | This batch: 97.5% passes |

**Test Method:** Ro-Tap sieve shaker with stacked ASTM E11 sieves (20–100 mesh), 10-minute shaking
**Why It Matters:** Determines dispersion rate, visual appearance, application performance, and processing behavior.

**Mesh Conversion Table:**
| Mesh (US Std) | Opening (μm) | Opening (in) | Classification |
|--------------|--------------|--------------|---------------|
| 4 | 4,750 | 0.187 | Extra coarse (flakes) |
| 8 | 2,360 | 0.0937 | Coarse (flakes) |
| 14 | 1,400 | 0.0555 | Medium flakes |
| 20 | 841 | 0.0331 | Fine flakes / coarse powder |
| 30 | 595 | 0.0234 | Standard powder |
| 40 | 420 | 0.0165 | Standard powder |
| 60 | 250 | 0.0098 | Fine powder |
| 80 | 177 | 0.0070 | Extra fine |
| 100 | 149 | 0.0059 | Ultrafine |
| 140 | 105 | 0.0041 | Very fine |
| 200 | 74 | 0.0029 | Microfine |

**Typical Particle Size Specifications:**
| Product Form | Mesh Requirement | Application |
|-------------|-----------------|-------------|
| Bulk powder | 95% through 40 mesh | General industrial use |
| Fine powder | 95% through 60 mesh | Seasoning blends, sauces |
| Extra fine | 95% through 100 mesh | Smooth sauces, instant mixes |
| Paprika flakes (coarse) | 85% between 4–14 mesh | Surface decoration, dry rubs |
| Paprika flakes (fine) | 85% between 14–40 mesh | Seasoning mixes |

### 2.4 Bulk Density

| Spec Line | Example | Meaning |
|-----------|---------|---------|
| Specification | 0.4–0.6 g/mL | Packing density range |
| Test Result | 0.52 g/mL | Report value |

**Test Method:** Loose bulk density per EN 1236 (free-fall into graduated cylinder, no compaction)
**Why It Matters:** Affects packaging volume (and thus bag count per container), shipping costs, and mixing characteristics.

**Practical Impact:**
- Lower density (0.35–0.45 g/mL): Less compacted, flows easily, more bag volume per MT
- Higher density (0.50–0.65 g/mL): Better packing efficiency, lower shipping volume

**Container Loading Calculator (20 GP container, ~28 m³ internal):**
| Bulk Density | Net Weight per Container | Bags (25 kg) |
|-------------|------------------------|--------------|
| 0.40 g/mL | 11,200 kg | 448 |
| 0.50 g/mL | 14,000 kg | 560 |
| 0.60 g/mL | 16,800 kg | 672 |

---

## 3. Chemical Parameters

### 3.1 Pungency (SHU / Capsaicin Content)

| Spec Line | Example | Meaning |
|-----------|---------|---------|
| Specification | ≤500 SHU | Must be sweet (non-pungent) |
| Test Result | 180 SHU | Mildly pungent (passes) |

**Why It Matters:** Determines heat level. Sweet paprika buyers require low SHU. Pungency level affects application suitability for different cuisines.

**Test Methods:**
| Method | Standard | Principle | Precision | Unit |
|--------|----------|-----------|-----------|------|
| HPLC | ISO 3513 (7503-1) | Direct capsaicinoid quantification | High (±5%) | mg/kg capsaicin = SHU/15 |
| Sensory | ASTM E1083 | Scoville panel | Low (±30%) | SHU |
| HPLC-Sensory correlation | — | 1 mg/kg capsaicin = 15 SHU | Approximate | Conversion |

**Conversion Formula:** SHU = Total Capsaicinoids (mg/kg) × 15

**Pungency Classification for Paprika:**
| Classification | SHU Range | Capsaicin Content (mg/kg) | Typical Use |
|---------------|-----------|--------------------------|-------------|
| Sweet | 0–500 | 0–33 | General sweet paprika |
| Mildly sweet | 500–1,500 | 33–100 | Mild seasoning |
| Semi-hot | 1,500–5,000 | 100–333 | Spicy blends |
| Hot | 5,000–15,000 | 333–1,000 | Hot paprika varieties |
| Very hot | 15,000+ | 1,000+ | Cayenne-type, not paprika |

### 3.2 Total Ash

| Spec Line | Example | Meaning |
|-----------|---------|---------|
| Specification | ≤8% | Total mineral content limit |
| Test Result | 5.3% | Normal for paprika (passes) |

**Test Method:** ISO 763 / AOAC 944.09 — incineration at 525°C until constant weight
**Why It Matters:** High ash may indicate contamination with sand, soil, or mineral adulterants.

**Normal Range:** 5–8% for pure paprika (varies by origin: Xinjiang 4.5–6.5%, Inner Mongolia 5.5–7.5%)
**Warning Zone:** 8–10% borderline; >10% investigate for soil contamination or adulteration

### 3.3 Acid-Insoluble Ash

| Spec Line | Example | Meaning |
|-----------|---------|---------|
| Specification | ≤1.0% | Sand/silica content limit |
| Test Result | 0.3% | Low (passes) |

**Test Method:** ISO 763 / AOAC 944.09 — treat total ash with HCl, filter, and weigh insoluble residue
**Why It Matters:** Direct indicator of soil contamination or poor cleaning during processing.

**Interpretation:**
| AIA Value | Assessment | Action |
|-----------|-----------|--------|
| ≤0.5% | Excellent | Meets all market standards |
| 0.5–1.0% | Acceptable | Meets most regulatory limits |
| 1.0–1.5% | Borderline | Investigate; reject for EU market |
| >1.5% | Poor | Likely soil contamination; reject |

### 3.4 Heavy Metals

| Parameter | EU Limit (EC 1881/2006) | US Limit (CFR 21) | China Limit (GB 2762) | Test Method |
|-----------|------------------------|-------------------|---------------------|-------------|
| Lead (Pb) | ≤3.0 mg/kg | ≤5.0 mg/kg | ≤1.0 mg/kg | ICP-MS / AAS |
| Cadmium (Cd) | ≤0.3 mg/kg | ≤0.5 mg/kg | ≤0.5 mg/kg | ICP-MS / AAS |
| Arsenic (As) | ≤1.0 mg/kg | ≤5.0 mg/kg | ≤0.5 mg/kg | ICP-MS / AAS |
| Mercury (Hg) | ≤0.1 mg/kg | — | ≤0.01 mg/kg | Cold vapor AAS |
| Tin (Sn, canned) | ≤50 mg/kg | — | — | ICP-MS |

**Why It Matters:** Heavy metals are bioaccumulative toxins regulated in all major markets. EU limits are most restrictive.

**Testing Frequency:** Industry best practice: every 6 months or with every season's new crop. Some buyers require every batch for high-value contracts.

### 3.5 Pesticide Residues

**Regulatory Frameworks:**
| Market | Regulation | Screening Panels |
|--------|-----------|-----------------|
| EU | EC 396/2005 | Default 500+ substances; MRL for paprika typically 0.01–0.05 mg/kg |
| US | 40 CFR 180 | EPA tolerance; typically 0.1–50 ppm depending on pesticide |
| Japan | Positive List System | Uniform limit 0.01 ppm for unlisted substances |
| China | GB 2763 | Varies by pesticide; typically 5–50 limits monitored |

**Common Paprika Pesticide Concerns:**
| Pesticide | Category | EU MRL (mg/kg) | Risk Level During Import |
|-----------|---------|----------------|------------------------|
| Chlorpyrifos | Insecticide | 0.01 (effectively banned) | High (banned in EU since 2020) |
| Cypermethrin | Insecticide | 0.05 | Moderate |
| Lambda-cyhalothrin | Insecticide | 0.02 | Moderate |
| Carbendazim | Fungicide | 0.05 | High |
| Dimethoate | Insecticide | 0.02 | Moderate |
| Glyphosate | Herbicide | 0.10 | Low (not commonly used on peppers) |

**Recommended Practice:** Request a multi-residue screen (>200 substances) at least annually. Use GC-MS/MS and LC-MS/MS for comprehensive coverage.

### 3.6 Mycotoxins (Aflatoxins, Ochratoxin A)

| Mycotoxin | EU Limit | US Limit | Test Method | Risk Level for Paprika |
|-----------|---------|---------|-------------|-----------------------|
| Aflatoxin B1 | ≤5.0 μg/kg | — | HPLC-FD / LC-MS/MS | High (especially in warm climates) |
| Total Aflatoxins (B1+B2+G1+G2) | ≤10.0 μg/kg | ≤20 μg/kg | HPLC-FD / LC-MS/MS | High |
| Ochratoxin A | ≤15.0 μg/kg | — | HPLC-FD / LC-MS/MS | Moderate |

**Risk Factors:**
- High humidity (>70%) during storage
- Poor drying practices (slow sun drying)
- Insect damage during growth
- Improper storage in tropical climates

**Testing Recommendation:** Every batch for EU-destined products; at least quarterly monitoring for other markets.

---

## 4. Microbiological Parameters

| Parameter | EU Standard (EC 2073/2005) | US Standard (FDA) | China Standard (GB 29921) | Test Method |
|-----------|---------------------------|-------------------|-------------------------|-------------|
| Salmonella | Negative/25g (n=5,c=0) | Negative/25g | Negative/25g | ISO 6579-1 |
| E. coli | <10 CFU/g | <10 CFU/g | <10 CFU/g | ISO 16649-2 |
| Yeast & Mold | <1,000 CFU/g | <10,000 CFU/g | — | ISO 21527-1 |
| Aerobic Plate Count (APC) | <100,000 CFU/g | <100,000 CFU/g | — | ISO 4833-1 |
| Bacillus cereus | <1,000 CFU/g | — | — | ISO 7932 |
| Clostridium perfringens | <100 CFU/g | — | — | ISO 7937 |
| Coliforms | — | <100 CFU/g | <100 CFU/g | ISO 4832 |
| Enterobacteriaceae | — | — | — | ISO 21528-2 |

> **Note:** EU standards are generally more stringent. "n=5,c=0" means 5 samples must be tested with zero positive results allowed.

**Microbiological Risk Factors:**
| Factor | Risk | Mitigation |
|--------|------|------------|
| High moisture (>10%) | Mold, yeast, bacterial growth | Strict moisture control (CCP) |
| Sun drying (open air) | Environmental contamination | Covered drying platforms |
| Poor hygiene in grinding | E. coli, APC elevation | GMP implementation |
| Cross-contamination in shared facilities | Salmonella | Dedicated lines or validated cleaning |
| Prolonged storage in humid conditions | Mycotoxin development | Climate-controlled warehouse |

**Sterilization Options:**
| Method | Effectiveness | ASTA Impact | Regulatory Status |
|--------|--------------|------------|------------------|
| Steam sterilization (thermal) | High for bacteria, moderate for spores | −5 to −10% | Allowed globally |
| Irradiation (gamma, e-beam) | High, also extends shelf life | −2 to −5% | EU restricts; US: up to 30 kGy allowed |
| Ethylene oxide (EtO) | High | Minimal | **Banned in EU** since 1991; US limits apply |
| Propylene oxide (PPO) | High | Minimal | US allowed with limits; Japan: banned |

---

## 5. Reading a Spec Sheet: Step-by-Step

```
Step 1: ✅ Verify header information
        └─ Product name, grade, lot/batch number, supplier name, COA date
        └─ CONFIRM: product matches your purchase order
        │
Step 2: ✅ Check ASTA color value
        └─ Does it meet the contract minimum?
        └─ Is it within expected tolerance for the grade?
        │
Step 3: ✅ Review moisture content
        └─ Is it ≤10%? If >10%, flag for rejection or price adjustment
        └─ Note: powder can absorb moisture during storage
        │
Step 4: ✅ Verify particle size
        └─ Is it suitable for your application?
        └─ Flakes product: check dust ratio (<20 mesh)
        │
Step 5: ✅ Examine chemical parameters
        └─ Total ash, AIA within limits
        └─ Heavy metals: compare with destination market's limits
        │
Step 6: ✅ Review microbiology
        └─ Salmonella: MUST be negative
        └─ Yeast & mold, APC: must meet destination requirements
        │
Step 7: ✅ Check mycotoxins (if provided)
        └─ Aflatoxin: crucial for EU and US imports
        │
Step 8: ✅ Verify certification status
        └─ Organic, Kosher, Halal — are certificates current and valid?
        └─ Certifier name and expiration date
```

---

## 6. Red Flags on Spec Sheets

| Red Flag | Likely Cause | Risk Level | Action Required |
|----------|-------------|------------|-----------------|
| No batch/lot number | Poor traceability | 🔴 High | Reject; request batch-specific COA |
| Missing microbiology data | Incomplete or no testing | 🔴 High | Request full microbial panel before shipment |
| Vague specs ("typical," "representative") | No quality commitment | 🔴 High | Clarify: is this a batch COA or a generic spec? |
| No expiry or revision date | Outdated document | 🟡 Medium | Request current COA |
| ASTA suspiciously high for price | Possible adulteration | 🔴 High | Commission third-party testing for Sudan dyes |
| Different grade names than industry | Mislabeling possible | 🟡 Medium | Verify via third-party ASTA testing |
| "No heavy metals tested" | Cost-cutting on testing | 🟡 Medium | Request heavy metals panel |
| Result values at exactly the limit (e.g., ASTA 160.0) | Possible data manipulation | 🟡 Medium | Confirm with retest |
| Same COA number as previous shipment | Copy-paste without new batch testing | 🔴 High | Demand new batch-specific COA |
| Origin stated as "China" without province | Opaque sourcing | 🟡 Medium | Ask for province-level origin |

---

## 7. Specification Sheet Template: What to Require from Suppliers

### Minimum Spec Sheet Requirements
```
1. HEADER
   - Supplier name & address
   - Product name & grade
   - Lot/Batch number (unique per batch)
   - COA date
   - Customer reference

2. PHYSICAL PARAMETERS
   - ASTA Color Value: ____ (min), Result: ____
   - Moisture: ____ (max), Result: ____
   - Particle Size: ____% through ____ mesh, Result: ____
   - Bulk Density: ____ g/mL (typical)

3. CHEMICAL PARAMETERS
   - Pungency: ____ SHU (max), Result: ____
   - Total Ash: ____% (max), Result: ____
   - Acid-Insoluble Ash: ____% (max), Result: ____
   - Heavy Metals: Pb ___, Cd ___, As ___, Hg ___ (each with max limit)

4. MICROBIOLOGICAL PARAMETERS
   - Salmonella: Negative/25g
   - E. coli: <____ CFU/g
   - Yeast & Mold: <____ CFU/g
   - APC: <____ CFU/g

5. MYCOTOXINS (if applicable)
   - Aflatoxin B1: ≤____ μg/kg
   - Total Aflatoxins: ≤____ μg/kg
   - Ochratoxin A: ≤____ μg/kg

6. CERTIFICATION STATUS
   - [ ] Organic (certifier: ____, expiry: ____)
   - [ ] Kosher (agency: ____, expiry: ____)
   - [ ] Halal (body: ____, expiry: ____)
   - [ ] HACCP-certified facility

7. ADDITIONAL (optional)
   - Pesticide residue screen (attach report)
   - GMO status: Non-GMO verified
   - PDO/PGI status (if applicable)
```

---

## 8. Frequently Asked Questions

**Q: What is the most important specification to check?**
A: ASTA color value — it's the primary quality and pricing parameter. Second: microbiological results for your destination market. Third: verify that heavy metals meet your market's regulatory limits.

**Q: How much variation is normal between batches?**
A: For a consistent supplier: ASTA ±10, moisture ±1%, particle size ±3%. Larger variation suggests inadequate quality control.

**Q: Should I use a third-party lab for verification?**
A: For critical purchases (first-time supplier, non-standard spec, high-value contract), independent third-party testing is strongly recommended. Many buyers split samples with suppliers as a quality assurance practice.

**Q: What is the "dry weight basis" and why does it matter?**
A: Some specs report ASTA on dry weight basis (corrected for moisture). This removes the dilution effect of water. Always check whether your spec sheet reports ASTA on an "as-is" or "dry weight" basis.

**Q: How do I handle a spec sheet that shows ASTA 160 but the product looks weak?**
A: Possible causes: (1) particle size too coarse (appears lighter), (2) high moisture content, (3) different carotenoid profile (more beta-carotene = less red), (4) the spec sheet may not match the batch. Request HPLC carotenoid profiling and moisture-adjusted ASTA.

**Q: My contract specifies "Premium" but the COA says ASTA 155. Is this a breach?**
A: Yes, if ASTA 160 minimum was specified. "Premium" is not a legally defined term — the numerical ASTA minimum is what matters. Enforce the contract specification.

---

## 9. Cross-References

| Related Document | Key Linkage |
|----------------|-------------|
| [ASTA Color Value Guide](./asta-color-value-guide.md) | Detailed ASTA methodology, degradation kinetics |
| [Paprika Grades Explained](./paprika-grades-explained.md) | How spec parameters define grade boundaries |
| [Paprika Supply Chain Guide](./paprika-supply-chain.md) | QC test frequency, shipping documentation |
| [Paprika Origin Guide (Chinese)](./paprika-origin-guide.md) | Origin-specific spec variations |
| [Glossary - Paprika Quality Parameters](../glossary/index.md) | Definitions of all spec terms |
| HACCP Certification | Moisture as CCP; microbial verification |
| ISO 22000:2018 | Testing frequency, traceability |
| Organic Certification | Additional organic-specific spec requirements |

---

*This document is part of the official technical documentation library for **paprikabulk.com** operated by Dinweys (Qingdao).Co.,Ltd. All rights reserved. For the latest version, visit https://paprikabulk.com.*
