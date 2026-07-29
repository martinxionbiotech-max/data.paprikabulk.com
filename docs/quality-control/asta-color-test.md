---title: ASTA Color Test Record Template
description: ASTA color value test record template — spectrophotometer test log for color quality documentation.
category: Quality Control
keywords:
- ASTA test
- color test
- spectrophotometer
- quality record---

# ASTA Color Value Test — Standard Operating Procedure & Record

## 1. Purpose & Scope

This document describes the procedure for determining the ASTA (American Spice Trade Association) color value of paprika powder, flakes, and ground whole-pod subsamples using the ASTA 20.1 spectrophotometric method. The ASTA color value is the primary quality parameter for grading paprika and must be measured for every production batch.

**Scope:** All paprika products (powder, flakes, whole pods tested as ground subsamples) at all grade levels.

---

## 2. Equipment & Consumables

| Item | Specification | Notes |
|------|---------------|-------|
| UV-Vis Spectrophotometer | Wavelength accuracy ±1 nm at 460 nm | Recommended: Shimadzu UV-1900, Thermo GENESYS, or equivalent |
| Cuvettes | Quartz or optical glass, 1 cm path length | Matched pair recommended; check optical clarity before use |
| Analytical Balance | ±0.001 g precision | Calibrated daily |
| Acetone | ACS grade, ≥99.5% purity | Store in airtight container; expires 3 months after opening |
| Volumetric Flasks | Class A, 50 mL, 100 mL, 250 mL | Clean, dry, acetone-rinsed |
| Volumetric Pipettes | Class A, 1–10 mL range | Calibrated annually |
| Filtration | Whatman No. 1 filter paper or 0.45 µm syringe filter | For cloudy extracts |
| Mortar and Pestle | Porcelain or agate | For grinding whole pods or coarse flakes |
| Thermometer | ±0.5°C accuracy | Measure acetone temperature |
| Vortex Mixer / Shaker | Sufficient for 10 min extraction | Mechanical shaker or vortex |
| Timer | ±1 second | For extraction timing |

---

## 3. Detailed Procedure — Step by Step

### 3.1 Sampling
1. Obtain a representative sample from the batch in accordance with the [Incoming Inspection Procedure](incoming-inspection.md).
2. For powder: use as-is. For flakes or whole pods: grind a subsample in mortar and pestle until it passes through a 40 mesh sieve.
3. Store the prepared sample in an airtight, light-protected container until analysis.

### 3.2 Sample Preparation
1. Weigh accurately **0.100 ± 0.010 g** of prepared sample into a clean 100 mL volumetric flask. Record weight (m) to 0.001 g.
2. Add approximately 70 mL of ACS-grade acetone at room temperature (20–25°C).
3. Secure the stopper and shake vigorously by hand for 1 minute, then place on mechanical shaker for **10 minutes ± 30 seconds** at moderate speed.
4. Remove from shaker and dilute to volume (100 mL) with acetone. Invert to mix thoroughly.
5. If the solution is cloudy, filter through Whatman No. 1 filter paper, discarding the first 5 mL of filtrate.

### 3.3 Measurement
1. Turn on the spectrophotometer and allow to warm up for **minimum 15 minutes**.
2. Set wavelength to **460 nm**.
3. Zero the instrument with a cuvette filled with **pure acetone** (blank).
4. Rinse the sample cuvette with a small portion of the extract, then fill.
5. Measure absorbance (A) at 460 nm. Record the reading.
6. If absorbance exceeds 0.8 AU, dilute the extract with acetone (record dilution factor D) and re-measure.

### 3.4 Calculation

**Formula:**  
**ASTA Color Value = (A × D × V × 16.4) / (m × L × 100)**

Where:
- **A** = Absorbance reading at 460 nm
- **D** = Dilution factor (D = 1 if no dilution; D = final volume / aliquot volume if diluted)
- **V** = Volume of extract (mL) — typically 100 mL
- **16.4** = ASTA conversion factor (extinction coefficient constant)
- **m** = Sample mass (g)
- **L** = Cuvette path length (cm) — typically 1 cm

**Simplified (standard conditions: V = 100 mL, L = 1 cm):**  
**ASTA = (A × D × 1,640) / m**

### 3.5 Replicates
Perform the test in **triplicate** using three independently prepared extracts from the same sample. Report the **mean** of the three results.

---

## 4. Test Record Form

| **Lab Information** | |
|---------------------|---|
| Sample ID | |
| Product Name | |
| Grade | |
| Batch/Lot Number | |
| Test Date | |
| Operator | |
| Ambient Temperature | |

### 4.1 Equipment Verification

| Check | Pass/Fail | Notes |
|-------|-----------|-------|
| Spectrophotometer warmed ≥15 min | | |
| Wavelength set to 460 nm | | |
| Blank absorbance ≤0.010 AU | | |
| Acetone lot and expiry | | |

### 4.2 Test Parameters

| Parameter | Value |
|-----------|-------|
| Spectrophotometer Model | |
| Wavelength | 460 nm |
| Cuvette Path Length | 1 cm |
| Solvent | Acetone (ACS grade) |
| Sample Weight (g) | [Replicate 1] / [Rep 2] / [Rep 3] |
| Extraction Volume (mL) | 100 |
| Absorbance Reading | [Rep 1] / [Rep 2] / [Rep 3] |
| Dilution Factor | [Rep 1] / [Rep 2] / [Rep 3] |

### 4.3 Calculation

| Parameter | Rep 1 | Rep 2 | Rep 3 |
|-----------|-------|-------|-------|
| A (Absorbance) | | | |
| D (Dilution factor) | | | |
| V (Volume, mL) | 100 | 100 | 100 |
| m (Mass, g) | | | |
| L (Path length, cm) | 1 | 1 | 1 |
| **ASTA Result** | | | |
| **Mean ASTA** | | | |
| **Standard Deviation** | | | |
| **% RSD** | | | |

**Acceptance:** % RSD between replicates must be ≤5%. If exceeded, repeat the entire test.

### 4.4 Specification Check

| Specification | Mean ASTA Result | Pass / Fail |
|---------------|------------------|-------------|
| Grade ASTA minimum [___]: [spec value] | | |

---

## 5. Acceptance Criteria & Decision Rules

| Condition | Action |
|-----------|--------|
| Mean ASTA ≥ specification minimum | **PASS** — batch meets color specification |
| Mean ASTA < specification minimum by ≤5% | **HOLD** — review by QC Manager; may reclassify to lower grade |
| Mean ASTA < specification minimum by >5% | **FAIL** — batch cannot ship as stated grade. Reclassify or reject. |
| RSD between replicates >5% | Repeat entire test; investigate technique or equipment issue |

---

## 6. Calibration & Verification

| Frequency | Activity | Standard / Reference |
|-----------|----------|---------------------|
| Daily | Zero/baseline check with acetone blank | Absorbance must be <0.010 AU |
| Weekly | Wavelength accuracy check | Holmium oxide / didymium standard |
| Monthly | Full photometric accuracy | NIST-traceable neutral density filter |
| Annually | Manufacturer calibration service | As per spectro. manufacturer SOP |
| Per new lot | Acetone blank check | Verify no interfering absorbance at 460 nm |

---

## 7. Troubleshooting

| Symptom | Probable Cause | Corrective Action |
|---------|---------------|-------------------|
| Absorbance >0.8 AU without dilution | Sample mass too high | Reduce sample mass to ~0.050 g and re-test |
| Absorbance <0.1 AU | Sample mass too low, or very low color | Increase sample mass; confirm sample is representative |
| Cloudy extract after filtration | Incomplete grinding or moisture contamination | Grind finer; use 0.45 µm syringe filter |
| Poor replicate precision (RSD >5%) | Inconsistent weighing, extraction time, or cuvette handling | Re-train operator; ensure 10.0 min shake time; clean cuvettes |
| Blank absorbance >0.010 AU | Dirty cuvette or contaminated acetone | Clean cuvette with acetone; use fresh acetone |
| Negative absorbance reading | Cuvette mis-match or dirty reference | Use matched cuvettes; clean both cuvettes |
| ASTA value seems too low vs visual color | Possible capsaicin interference or old sample | Check SHU; re-sample from fresh, sealed lot |

---

## 8. Recording Requirements

- All raw data (weights, absorbance readings, calculations) must be recorded in ink in the QC lab logbook **immediately** — no loose paper.
- Digital records: enter results into LIMS within 24 hours.
- Each entry must be dated and signed by the operator.
- A second QC technician must review calculations for each COA release.

---

## 9. Method References

- **ASTA 20.1** — "Extractable Color in Capsicum Spices" — Official Analytical Methods of the American Spice Trade Association, 5th Edition
- **ISO 7543-2** — Chillies and capsicum oleoresins — Determination of total capsaicinoid content
- **ASTM D7481** — Standard Test Methods for Bulk Density

---

*This document is part of the official technical documentation library for **paprikabulk.com** operated by Dinweys (Qingdao).Co.,Ltd. All rights reserved. For the latest version, visit https://paprikabulk.com.*
