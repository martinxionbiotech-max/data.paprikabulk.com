---title: Spectrophotometer — Quality Control Instrument
description: Paprika spectrophotometer guide for color measurement — instrument types, calibration standards, sample preparation, ASTA method 20.1 procedure, and result interpretation for quality assurance laboratories.
category: Quality Control
keywords:
- spectrophotometer
- UV-Vis
- ASTA measurement
- color measurement
- calibration
- wavelength accuracy
- photometric accuracy
- stray light
- ISO 7541
- holmium oxide
- neutral density filter---

# Spectrophotometer — Calibration and Use for ASTA Measurement

## Purpose

A UV-Vis spectrophotometer is the core instrument for ASTA color value measurement (ASTA Method 20.1 / ISO 7541). The instrument measures the absorbance (optical density) of acetone-extracted carotenoids at the principal absorption maximum of 460 nm. Reliable ASTA results depend entirely on proper instrument selection, calibration, and maintenance.

## Background — Measurement Principle

Spectrophotometric ASTA determination is based on the Beer-Lambert law:

```
A = ε × c × l
```

Where:
- A = absorbance (no units) at 460 nm
- ε = molar attenuation coefficient of capsanthin in acetone (L·mol⁻¹·cm⁻¹)
- c = concentration of extracted carotenoids (mol·L⁻¹)
- l = path length of cuvette (typically 1.0 cm)

The sample is prepared by extracting a precisely weighed mass of paprika (0.10–0.25 g) in acetone, filtering (or centrifuging), diluting to a known volume, and measuring the absorbance at 460 nm in a 1.0 cm quartz cuvette against an acetone blank. The ASTA value is calculated as:

```
ASTA = A × dilution × 16.4 × I₄₆₀ / m
```

Where A = measured absorbance, dilution = factor for the volume of extract, 16.4 = constant incorporating the extinction coefficient, I₄₆₀ = instrument correction factor (see calibration), and m = sample mass in grams.

## Calibration Requirements

| Parameter | Requirement | Standard Reference | Acceptable Tolerance | Calibration Frequency |
|:---------:|:-----------:|:------------------:|:-------------------:|:---------------------:|
| Wavelength accuracy | ± 1 nm at 460 nm | Holmium oxide filter (peak at 460.0 nm) or didymium filter | ± 0.5 nm preferred, ± 1.0 nm max | Monthly |
| Photometric accuracy | ± 0.005 A at 1.0 A | Neutral density glass filter (NIST-traceable) | ± 0.005 A at 1 A; ± 0.002 A at 0.3 A | Monthly |
| Stray light | < 0.05% at 340 nm | Cut-off filter (e.g., 220 nm cut-off, measured at 340 nm) | < 0.05% T | Monthly |
| Baseline flatness | ± 0.003 A across 200–800 nm | Empty beam path (air vs air) | ± 0.003 A | Weekly |
| Noise | < 0.0005 A RMS at 500 nm | Dark current measurement | < 0.0005 A | Weekly |
| Wavelength reproducibility | ± 0.1 nm | Repeated scan of holmium oxide | ± 0.1 nm | Quarterly |

### Instrument Correction Factor (I₄₆₀)

For ASTA measurement, each instrument must be characterized with an **Instrument Correction Factor (I₄₆₀)** that compensates for systematic bias from wavelength indexing and stray light. This is determined by:

1. Measuring a reference paprika sample of known ASTA (certified by reference lab).
2. Calculating:
   ```
   I₄₆₀ = ASTA_reference / ASTA_measured
   ```
3. Applying I₄₆₀ to all subsequent measurements.
   A new I₄₆₀ should be determined after any lamp replacement, stray light correction, or major service.

## Recommended Models

| Model | Manufacturer | Detector Type | Bandwidth | Stray Light | Typical I₄₆₀ Range |
|:-----:|:------------:|:-------------:|:---------:|:-----------:|:-------------------:|
| Genesys 150 | Thermo Scientific | Silicon photodiode | 2 nm | < 0.1% at 340 nm | 0.97–1.03 |
| UV-1900i | Shimadzu | Photomultiplier | 1 nm | < 0.02% at 340 nm | 0.98–1.02 |
| Cary 60 | Agilent | Silicon photodiode (xenon flash) | 1.5 nm | < 0.05% at 340 nm | 0.97–1.03 |
| Lambda 365 | PerkinElmer | Silicon photodiode | 2 nm | < 0.05% at 340 nm | 0.97–1.03 |
| BioMate 160 | Thermo Scientific | Silicon photodiode | 2 nm | < 0.1% at 340 nm | 0.96–1.04 |

**Selection Criteria:**
- **Essential:** Wavelength accuracy ≤ ±1 nm; photometric accuracy ≤ ±0.005 A; built-in stray light correction.
- **Preferred:** Double-beam optics (compensates for lamp drift during measurement sequences).
- **Nice-to-have:** Pre-programmed ASTA method; autosampler for high-throughput labs.

## Quality Control Checks

### Daily Checks (Before Use)

| Check | Procedure | Pass/Fail Criteria |
|:------|:---------|:-------------------|
| Warm-up | Turn on 30 min before use | Allow lamp to thermally stabilize |
| Wavelength calibration | Measure holmium oxide 460 nm peak | Within ± 0.5 nm of 460.0 nm |
| Photometric calibration | Measure NIST-traceable 1.0 A neutral density filter | 1.000 ± 0.005 A |
| Baseline | Scan air vs air (200–800 nm) | ± 0.003 A flat |
| Blank absorbance | Measure acetone against air at 460 nm | < 0.010 A |
| System suitability — ASTA standard | Measure working reference paprika (known ASTA) | Within ± 5% of certified value |

### Weekly Checks

| Check | Procedure | Pass/Fail Criteria |
|:------|:---------|:-------------------|
| Stray light | Measure at 340 nm with cut-off filter | < 0.05% T |
| Wavelength reproducibility | 3× holmium oxide scans | Max deviation < 0.1 nm |
| Cuvette check | Water vs water at 460 nm (matched pair) | < 0.005 A difference |

### Monthly / Quarterly Checks

| Check | Frequency | Procedure |
|:------|:---------:|:---------:|
| Full wavelength calibration | Monthly | Full spectral scan of holmium oxide; verify all peaks |
| Photometric linearity | Quarterly | Measure filter set (0.3, 0.5, 1.0, 1.5 A) — linearity must be r² > 0.9999 |
| I₄₆₀ recalculation | Quarterly | Re-measure reference paprika; recalculate I₄₆₀ |
| Lamp replacement | As needed (typically 1,000–2,000 h) | Replace when energy at 460 nm drops to <50% of baseline |

## Cuvette Selection and Care

| Cuvette Type | Spectral Range | Suitable for ASTA | Care Instructions |
|:------------:|:--------------:|:----------------:|:-----------------:|
| Quartz (fused silica) | 190–2,500 nm | Yes — required for 460 nm work | Clean with acetone between samples; never scratch optical faces |
| UV-grade plastic (PMMA) | 380–780 nm | Acceptable (transparent above 380 nm) | Single-use preferred; check lot-to-lot variation |
| Glass | 320–2,500 nm | Yes | Clean with mild detergent; rinse with DI water; avoid scratches |
| Polystyrene | 340–750 nm | Acceptable | Single-use only for ASTA |

**Critical practice:** Use matched pair cuvettes (optical path length matched to within ±0.01 mm). Always handle cuvettes by the frosted or ribbed sides — fingerprints on optical faces introduce 0.01–0.05 A error.

## Troubleshooting

| Issue | Symptom | Possible Cause | Corrective Action |
|:------|:--------|:--------------|:------------------|
| Absorbance drifts upward during measurement | Reading climbs over 30 s | Sample not fully dissolved; acetone evaporation | Vortex sample before filling cuvette; cap the cuvette during measurement |
| Repeated ASTA values differ by >10% | Poor CV | Incomplete extraction; non-homogeneous sample | Reduce particle size; increase extraction time to 60 min with periodic shaking |
| Negative absorbance at 460 nm | Blank reads higher than sample | Dirty cuvette or contaminated blank acetone | Replace acetone; clean or replace cuvettes |
| ASTA values consistently low vs reference | Systematic bias | I₄₆₀ out of date; aging lamp | Recalculate I₄₆₀; check lamp energy |
| High baseline noise (>0.002 A) | Erratic readings | Lamp aging; detector degradation | Replace lamp; if persists, service detector |
| Stray light test fails (>0.05% at 340 nm) | Bias at low wavelengths | Dust on monochromator; degradation of optical coating | Clean monochromator; factory service as needed |
| Wavelength 460 nm peak is shifted | Scan shows peak > 461 or < 459 nm | Mechanical wear on monochromator drive | Factory recalibration; do not adjust wavelength offset in software |

## Frequently Asked Questions

**Q: Can a filter-based colorimeter be used instead of a spectrophotometer for ASTA?**

A: Filter instruments with a narrow band-pass filter at 460 nm (± 10 nm) can be used for routine screening, but they lack the wavelength accuracy verification required to meet ISO 7541 compliance. A spectrophotometer with a monochromator is required for certified ASTA results.

**Q: Why does the ASTA method specify exactly 460 nm?**

A: The 460 nm wavelength corresponds to the principal absorption maximum of capsanthin, the dominant carotenoid in paprika. The extinction coefficient has been standardized at this wavelength across all reference methods (ASTA 20.1, ISO 7541, and AOAC 958.05).

**Q: How do I know when to replace the deuterium lamp?**

A: Most instruments have a lamp energy test. Replace when: (1) energy at 460 nm drops to <50% of baseline, (2) the photometric accuracy test fails at 1.0 A, or (3) after the manufacturer's recommended service life (typically 1,000–2,000 hours).

**Q: What is the acceptable CV between replicate ASTA measurements?**

A: For the same well-mixed sample: CV ≤ 2% for a trained analyst, ≤ 5% for routine production QC. If CV exceeds 5%, investigate extraction technique or sample homogeneity.

**Q: Is a double-beam instrument necessary for ASTA measurement?**

A: Strongly recommended but not strictly required. Double-beam geometry continuously compares the sample beam against a reference beam, automatically compensating for lamp intensity drift, temperature effects, and detector nonlinearity. Single-beam instruments can be used if the analyst blanks frequently (every 5–10 samples) and the instrument has good baseline stability.

## Cross-References

- [ASTA Color Value](../glossary/spice-science/asta.md) — Full method description and calculation
- [ASTA Color Test Record](./asta-color-test.md) — Test log template
- [Color Science](./color-science.md) — CIELAB color measurement instrumentation
- [HPLC](./hplc.md) — Alternative carotenoid analysis by chromatography
- [Acceptance Criteria](../glossary/quality-control/acceptance-criteria.md) — ASTA specification limits
- [Quality Manual](../glossary/quality-control/acceptance-criteria.md) — Instrument management SOPs

---

*This document is part of the official technical documentation library for **paprikabulk.com** operated by Dinweys (Qingdao).Co.,Ltd.

## Related Product

**Product:** [All Bulk Paprika Products](https://paprikabulk.com/product/)

[View product details, grades, and pricing →](https://paprikabulk.com/product/)



All rights reserved. For the latest version, visit [paprikabulk.com](https://paprikabulk.com).*
