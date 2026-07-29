---
title: Datasets — Structured Quality Data & Reference Tables
description: Comprehensive structured datasets for paprika quality — ASTA conversion charts, grade comparison tables, regulatory limit databases, microbiological limits, heavy metals, pesticide MRLs, mycotoxin limits, storage conditions, shelf life, particle size distribution, and bulk density reference tables.
keywords:
- paprika datasets
- quality data
- reference tables
- ASTA conversion
- MRL database
- regulatory limits
- microbiological limits paprika
- heavy metals limits
- pesticide residue limits
- mycotoxin limits
- storage conditions
- shelf life data
- particle size distribution
- bulk density data
- paprika grade comparison
- spice analytical data
datePublished: 2025-06-01
dateModified: 2026-07-21
---

# Datasets — Structured Quality Data & Reference Tables

This section provides structured, machine-readable reference datasets for paprika quality parameters, regulatory limits, and conversion tables. These datasets are designed for use by QC laboratories, procurement teams, data-driven quality systems, and AI/LLM retrieval applications.

## Using These Datasets

Each dataset includes:

- **Data table** — Structured tabular data with clear column headers, ready for direct use or import into spreadsheets
- **Reference method** — The analytical method used to generate the reference data
- **Regulatory source** — Where applicable, the regulatory body and standard reference document
- **Update frequency** — How often the data is reviewed and updated (critical for regulatory datasets)
- **Data format** — Markdown tables compatible with conversion to CSV, Excel, or database import

## Dataset Catalog

| Dataset | Format | Content | Update Frequency | Section |
|:--------|:------:|:--------|:----------------:|:--------|
| [ASTA Color Value Method](../glossary/spice-science/asta.md) | Structured tables | Formula, range definitions, grade correlation, inter-laboratory reproducibility data (RSD%), conversion to CIELAB | Annual | Spice Science |
| [Grade Comparison](../specifications/grade-comparison.md) | Comparison table | All grades side-by-side (9 parameters: ASTA, moisture, ash totals, acid-insoluble ash, particle size, bulk density, APC, Yeast & Mold, color CIELAB) | Per grade change | Specifications |
| [Microbiological Limits](../glossary/quality-control/microbiology.md) | Lookup table | EU / US / China limits for all relevant pathogens: APC, Yeast & Mold, Salmonella, E. coli, Bacillus cereus, Listeria monocytogenes, Clostridium perfringens | Biannual | Quality Control |
| [Heavy Metals Limits](../glossary/quality-control/heavy-metals.md) | Lookup table | Pb, Cd, As, Hg limits across 6 markets (EU EC 1881/2006, US FDA, China GB 2762, Japan MHLW, India FSSAI, Codex) | Biannual | Quality Control |
| [Pesticide MRL Database](../quality-control/pesticide-residue-management.md) | Reference table | EU / US / CN / JP limits for 40+ high-risk active substances relevant to paprika cultivation | Quarterly | Quality Control |
| [Mycotoxin Limits](../quality-control/mycotoxin-monitoring.md) | Lookup table | Aflatoxin B1, total aflatoxins (B1+B2+G1+G2), Ochratoxin A — 5 regulatory systems with regulatory references | Annual | Quality Control |
| [Storage Conditions](../quality-control/storage.md) | Data table | Degradation rates × temperature × packaging combinations; Arrhenius model parameters (Ea, A, Q10) | Annual | Quality Control |
| [Shelf Life](../regulatory/shelf-life.md) | Reference table | Typical shelf life by product form (powder, flakes, whole pods) and packaging type (poly bag, vacuum, foil) | Annual | Regulatory |
| [Particle Size Distribution](../quality-control/sieve-analysis.md) | Data table | Mesh size × grade retention percentages (target % retained per sieve for each grade) | Per standard revision | Quality Control |
| [Bulk Density](../quality-control/bulk-density.md) | Data table | Loose/tapped density, Carr Index, Hausner Ratio — by grade and particle size | Per standard revision | Quality Control |

## Detailed Dataset Descriptions

### Microbiological Limits Dataset

Comprehensive reference table covering pathogen limits across three major regulatory systems:

| Pathogen | EU (EC 2073/2005) | US (FDA) | China (GB 29921) |
|:---------|:-----------------:|:--------:|:----------------:|
| Aerobic Plate Count | ≤ 10⁵ CFU/g | ≤ 10⁵ CFU/g | ≤ 10⁵ CFU/g |
| Yeast & Mold | ≤ 10⁴ CFU/g | ≤ 10⁴ CFU/g | ≤ 10⁴ CFU/g |
| Salmonella | Negative / 25 g | Negative / 25 g | Negative / 25 g |
| E. coli | ≤ 10² CFU/g | ≤ 10² CFU/g | ≤ 10² CFU/g |
| Bacillus cereus | ≤ 10⁴ CFU/g | — | ≤ 10⁴ CFU/g |
| Listeria monocytogenes | Negative / 25 g | — | — |
| Clostridium perfringens | ≤ 10⁴ CFU/g | — | — |

**Note:** EU limits are mandatory per EC 2073/2005. US limits are FDA compliance guidelines. China limits are from GB 29921-2021.

### Heavy Metals Limits Dataset

| Metal | EU (EC 1881/2006) | US (FDA) | China (GB 2762) | Japan (MHLW) |
|:------|:-----------------:|:--------:|:---------------:|:------------:|
| Lead (Pb) | ≤ 3.0 mg/kg | ≤ 5.0 mg/kg | ≤ 3.0 mg/kg | ≤ 5.0 mg/kg |
| Cadmium (Cd) | ≤ 0.2 mg/kg | — | ≤ 0.5 mg/kg | ≤ 0.5 mg/kg |
| Arsenic (As inorganic) | ≤ 1.0 mg/kg | — | ≤ 0.5 mg/kg | — |
| Mercury (Hg) | ≤ 0.1 mg/kg | — | ≤ 0.02 mg/kg | — |

### Storage Conditions Dataset — ASTA Degradation Rates

First-order kinetic degradation data for ASTA color value under different storage conditions:

| Storage Temp | Packaging Type | Half-Life (ASTA 160→80) | Yearly Loss | Degradation Rate k (month⁻¹) |
|:-----------:|:--------------:|:----------------------:|:-----------:|:---------------------------:|
| 5°C (cold storage) | Vacuum-sealed foil | 24 months | < 5% | 0.029 |
| 5°C (cold storage) | Poly-lined bag | 18 months | ~7% | 0.039 |
| 15°C (cool) | Vacuum-sealed foil | 15 months | ~10% | 0.046 |
| 15°C (cool) | Poly-lined bag | 12 months | 8–12% | 0.058 |
| 25°C (ambient) | Vacuum-sealed foil | 9 months | ~18% | 0.077 |
| 25°C (ambient) | Poly-lined bag | 6 months | 15–25% | 0.116 |
| 35°C (tropical) | Poly-lined bag | 3 months | 30–50% | 0.231 |
| 45°C (extreme) | Any packaging | 1 month | > 80% | 0.693 |

**Arrhenius Parameters:** Ea = 70 kJ/mol, A = 2.5 × 10¹⁰ month⁻¹, Q₁₀ = 2.0

### Pesticide MRL Database — Sample Entries

| Active Substance | EU MRL (mg/kg) | US MRL (mg/kg) | China MRL (mg/kg) | Common Use |
|:----------------|:--------------:|:--------------:|:-----------------:|:-----------|
| Chlorpyrifos | 0.01 (default) | 0.5 | 0.1 | Insecticide |
| Cypermethrin | 0.5 | 5.0 | 0.5 | Insecticide |
| Metalaxyl | 0.05 | 0.2 | 0.5 | Fungicide |
| Lambda-cyhalothrin | 0.1 | 2.0 | 0.2 | Insecticide |
| Imidacloprid | 0.05 | 1.5 | 0.5 | Insecticide |

**Full database:** See [Pesticide Residue Management](../quality-control/pesticide-residue-management.md) for complete 40+ substance listing.

## Data Update Protocol

| Dataset | Update Trigger | Responsibility |
|:--------|:---------------|:---------------|
| Pesticide MRL database | Quarterly — when EU publishes new MRLs | Regulatory Affairs |
| Microbiological limits | Biannually — when regulations change | Quality Manager |
| Heavy metals limits | Biannually — when regulations change | Quality Manager |
| Mycotoxin limits | Annually — when regulations change | Quality Manager |
| Storage conditions data | Annually — when new research available | R&D |
| Shelf life data | Annually — per validation studies | Quality Manager |
| Particle size data | Per equipment or standard change | QC Supervisor |
| Bulk density data | Per product grade change | QC Supervisor |

## Data Format Conversion

All datasets are published in Markdown table format. To convert for your own use:

| Target Format | Method |
|:--------------|:-------|
| CSV | Copy table → paste into spreadsheet → save as CSV |
| Excel (.xlsx) | Copy table → paste into Excel → format as needed |
| JSON | Use Pandoc: `pandoc dataset.md -t json` |
| SQL INSERT | Write a simple parser to generate INSERT statements |
| Database import | Most databases accept CSV import |

## Related Documentation

- [Quality Control](../quality-control/index.md) — Testing procedures and SOPs
- [Regulatory Compliance](../regulatory/index.md) — Standards and regulations by market
- [Specifications](../specifications/index.md) — Product-level specification sheets
- [Research Library](../research/index.md) — Scientific studies behind these datasets

---

*This document is part of the official technical documentation library for **paprikabulk.com** operated by Dinweys (Qingdao).Co.,Ltd. All rights reserved. For the latest version, visit [paprikabulk.com](https://paprikabulk.com).*
