---title: Acceptance Criteria Glossary
description: Paprika acceptance criteria definition — NLT/NMT limits, AQL sampling plans, pass/fail determination, and specification compliance rules for incoming inspection and batch release decisions.
category: Quality Control
keywords:
- acceptance criteria
- pass fail
- quality limits
- NLT
- NMT---

# Acceptance Criteria

## Definition

Acceptance criteria are the predefined, numerically specified limits (minimum, maximum, or range) and/or qualitative descriptions against which each analytical test result is compared to determine whether a paprika product conforms to the contractual specification and is therefore acceptable for shipment, delivery, and use. The formal framework is defined in **ISO 2859-1:1999** (Sampling procedures for inspection by attributes), **ASTM E2554-18** (Statistical assessment of validation data), and the **AOAC Guidelines for Single-Laboratory Validation of Analytical Methods**. In the spice trade, acceptance criteria operationalize the specification — transforming an abstract target into a deterministic pass/fail decision for every batch.

## Overview

Acceptance criteria bridge the gap between the specification (the "what we want") and the COA (the "what we got"). They provide the binary decision framework that determines whether a shipment is released, rejected, or conditionally accepted. Without explicit acceptance criteria, the same test result can be interpreted differently by buyer and seller, creating disputes. A well-defined acceptance criteria section in the contract specifies not only the limits but also the response actions when limits are violated.

**The Decision Cascade:**

```
Test Result → Compare to Acceptance Criteria → 
  ↓ Within limits → PASS → Release for shipment → OK
  ↓ Marginally outside → Conditional → Discount/Recut/Reinspect → Decision
  ↓ Substantially outside → FAIL → Reject → Hold/CAPA/Return
```

## Technical Explanation

**Types of Acceptance Criteria with Examples:**

| Designation | Meaning | Symbol | Example in Paprika Spec | Implication of Violation |
|-------------|---------|--------|------------------------|--------------------------|
| **NLT (Not Less Than)** | Minimum acceptable value | ≥ | ASTA NLT 160 | Below 160: automatic downgrade or rejection |
| **NMT (Not More Than)** | Maximum acceptable value | ≤ | Moisture NMT 10.0% | Above 10.0%: automatic rejection or weight-adjusted acceptance |
| **Range** | Lower and upper bound | – | pH 4.5–6.0 | Below 4.5 or above 6.0: non-conforming |
| **Target with Tolerance** | Target value ± allowable deviation | ± | ASTA 160 ± 10 (range: 150–170) | Within tolerance: accept at full price. Outside: discount per agreed schedule |
| **Pass/Fail (Qualitative)** | Binary presence/absence | — | Salmonella: Negative / 25g | Positive: immediate rejection, CAPA, quarantine |
| **Limit of Detection (LOD)** | Below analytical detection | < 1 µg/kg | Lead: < LOD by ICP-MS (< 0.01 mg/kg) | Quantifiable level indicates contamination investigation needed |
| **AQL / LQL (Statistical)** | Acceptable/Limiting Quality Level per ISO 2859 | ≤ X% defective | AQL 2.5% for extraneous matter > 1.0 mm | Adjudicated by sampling plan, not individual tests |

**Statistical Framework — Normalized Acceptance Decision:**

For continuous numeric criteria (ASTA, moisture, particle size), the standard approach is:

> **Z-score = (Measured_Value − Acceptance_Limit) / Historical_Standard_Deviation**

| Z-score | Interpretation | Recommended Action |
|---------|---------------|-------------------|
| > +2.0 | Well within limits (high confidence pass) | Release without restrictions |
| +1.0 to +2.0 | Within limits (pass with margin) | Normal release |
| 0 to +1.0 | Within limits (tight pass) | Flag for monitoring during next batch |
| −1.0 to 0 | Marginally below NMT limit or above NLT limit | Conditional acceptance with discount |
| < −1.0 | Outside limits (fail with high confidence) | Reject or hold for supplier CAPA |

**Effect of Sampling Error on Acceptance Decisions:**

Acceptance criteria are only as meaningful as the sampling process. A batch may truly be within spec but fail due to a non-representative sample, or vice versa.

| Sampling Condition | Probability of False Rejection (Producer's Risk, α) | Probability of False Acceptance (Consumer's Risk, β) |
|--------------------|-----------------------------------------------------|-----------------------------------------------------|
| Single sample (1 × 500 g from top of bag) | 10–20% (high risk) | 15–25% (high risk) |
| Composite of 5 sub-samples from 5 different bags | 2–5% | 3–8% |
| Composite of 10 sub-samples (per ISO 948:2007) | 1–2% | 1–3% |
| ISO 2859 normal inspection level II | < 1% (negotiated) | 5–10% (AQL-dependent) |

**Decision Rules for Multi-Parameter Acceptance:**

A shipment passes only if **ALL parameters** are within their individual acceptance criteria. The "one failure = lot failure" principle applies in the spice trade.

| Scenario | Result | Action |
|----------|--------|--------|
| ASTA OK, Moisture OK, SHU OK, Salmonella Negative | **PASS** | Release |
| ASTA OK, Moisture FAIL (12.5% vs NMT 10%), SHU OK | **FAIL** | Reject or negotiate discount |
| ASTA OK, Moisture OK, SHU FAIL (1,200 vs NMT 500) | **FAIL** | Can reclassify as semi-hot grade; negotiate discount |
| ASTA OK, Moisture OK, SHU OK, *Salmonella* POSITIVE | **FAIL (Critical)** | Immediate rejection, hold, quarantine, CAPA |

**Action Plans for Specific Out-of-Spec Scenarios:**

| Parameter | Deviation | Action Option 1 | Action Option 2 | Action Option 3 |
|-----------|-----------|----------------|-----------------|-----------------|
| ASTA | 5–15% below NLT | Accept at discounted price (sliding scale: 1–3% discount per ASTA point) | Blend with higher-ASTA lot (seller's cost) | Reject at seller's cost |
| ASTA | > 15% below NLT | Reject | Reject (no economic recovery possible) | — |
| Moisture | 10.1–12.0% (vs. NMT 10%) | Accept with weight adjustment for water | Request price discount (2–5%) | Accept with reduced shelf-life warranty |
| Moisture | > 12.0% | Reject — microbial risk | Accept only if re-dried and retested at seller's cost | — |
| SHU | 100–500 vs. NMT 100 (sweet) | Reclassify as "mild" grade; negotiate discount | Accept if buyer has mild-grade application | — |
| SHU | > 500 vs. NMT 100 | Reject for sweet application | Accept only as hot-chili-grade product (significant discount) | — |
| *Salmonella* | POSITIVE | **REJECT — Mandatory.** Notify regulatory agency if batch entered commerce. | — | — |
| Heavy metals | Exceeds EU limit | **REJECT for EU market** | May be saleable in non-EU market with different limits | — |

## Industrial / Commercial Importance

**Economic Impact of Acceptance Criteria Design:**

| Acceptance Criteria Approach | Impact on Cost & Risk | Typical Industry |
|-----------------------------|----------------------|------------------|
| Single point limit ("ASTA 160") | Strictest interpretation; zero tolerance for measurement uncertainty | High-end EU food processors |
| Limit with allowance ("ASTA NLT 160, allow –5 for inter-lab variation") | Pragmatic; avoids disputes over measurement uncertainty | Common in bulk commodity trade |
| Multiple parameter with full AQL plan | Complex but statistically robust; low dispute rate | ISO 9001 / FSSC 22000 certified suppliers |
| Single sample + single parameter test | Fastest; highest risk for both parties | Small traders, spot market purchases |

**Quality Agreements and Acceptance Criteria as Legal Documents:**
For recurring supply relationships, the **Quality Agreement (QA)** formalizes the acceptance criteria. A typical QA for bulk paprika includes:
- Sampling plan (ISO 948:2007 for spices)
- Laboratory qualification requirements (ISO 17025 accreditation)
- Acceptance limits for every parameter
- Statistical tolerance (AQL levels per ISO 2859)
- Dispute resolution mechanism (third-party laboratory, arbitration body)
- Corrective action procedure for non-conformance
- Shelf-life warranty (e.g., "90% of ASTA retained for 12 months from shipment under specified storage")

## Application Guidance

**For Procurement:**
- Ensure every acceptance criterion specifies: (1) the parameter, (2) the numerical limit, (3) the test method reference, (4) the sampling plan, and (5) the action on non-conformance.
- Avoid ambiguous criteria like "ASTA ~160" or "moisture about 10%." These are not legally enforceable acceptance criteria.
- For critical parameters (Salmonella, aflatoxin, heavy metals), acceptance criteria should specify "Negative/25g" or the regulatory limit for the destination country, not just the supplier's internal limit.
- Include a **mutual tolerance clause**: e.g., "Acceptance criteria are considered met when the test result, including the measurement uncertainty (±5 ASTA units, ±0.3% moisture), falls within the specified limits."

**For Quality Control:**
- Record the date, time, sampler name, sample location, sample quantity, and container IDs for every sample used to verify acceptance criteria. This creates an auditable chain.
- Never accept or reject a batch based on a single out-of-spec result without retesting: obtain a new sample from a different location in the lot.
- Apply the **"TARES PTA"** principle for disputes: Test → Analyze → Review → Evaluate → Sample → Propose → Test → Agree. Both parties' laboratories test replicate samples and meet to agree.

**For Sales/Contracts:**
- Do not "widen" acceptance criteria to accept a borderline batch without documenting the justification and getting the buyer's agreement in writing.
- Standard COA language: "This lot meets the acceptance criteria specified in Contract #[Number], dated [Date]. For each parameter, the reported result conforms to the stated NLT/NMT limit per the referenced test method."

## Cross-References

- [Specification](./specification.md) — Acceptance criteria derive directly from the specification parameters
- [Grade](./grade.md) — Grade thresholds provide the acceptance criteria boundaries
- [Batch Number](./batch-number.md) — Each batch is accepted/rejected based on its COA and acceptance criteria
- [ASTA](../spice-science/asta.md) — ASTA acceptance criteria: NLT values
- [Moisture](../spice-science/moisture.md) — Moisture acceptance criteria: NMT values
- [SHU](../spice-science/shu.md) — SHU acceptance criteria: NMT or range
- [Microbiology](./microbiology.md) — Microbiological acceptance criteria: Negative/25g or CFU limits
- [Heavy Metals](./heavy-metals.md) — Heavy metal acceptance criteria: NMT regulatory limits
- [ISO 2859] — Statistical sampling and acceptance
- [ISO 17025] — Laboratory qualification requirement for acceptance testing
- [CAPA] — Corrective and Preventive Action procedure triggered by rejection

## Frequently Asked Questions

**Q: Can acceptance criteria be the same for all destination countries?**
A: No. EU, US, China, and Japan each have different regulatory limits for critical parameters. For example, EU limits for aflatoxin B₁ = 5 µg/kg, US FDA action level = 20 µg/kg. If you are shipping to both markets, you need separate acceptance criteria for each destination. A shipment meeting US acceptance criteria but not EU criteria must be redirected or relabeled. The contract should specify which regulatory framework's limits apply, or use the strictest of all relevant limits to ensure multi-market flexibility.

**Q: What does "Acceptable Quality Level (AQL)" mean in the context of paprika acceptance?**
A: AQL (ISO 2859-1) is the maximum percentage of defective units in a lot that is considered acceptable as a process average. For paprika, AQL is primarily applied to **visual defects** — extraneous matter, insect-damaged particles, moldy pieces. A typical AQL for paprika is 2.5% (meaning up to 2.5% of units may be defective and the lot is still acceptable). AQL is *not* typically applied to continuous variables like ASTA or moisture — those are evaluated by direct measurement against a single limit. For continuous variables with a tolerance range, the equivalent concept is the **capability index (Cpk)** which must be ≥ 1.33 for "capable" processes.

**Q: How are acceptance criteria established for a new paprika product or new supplier?**
A: Through a four-stage process: (1) **Specification development** — Buyer defines target parameters based on application needs. (2) **Supplier qualification** — Supplier's historical data (minimum 3 seasons of production) establishes natural process variation. (3) **Trial order** — 3–5 production lots are tested to confirm that the process consistently meets acceptance criteria. (4) **Contractual acceptance** — Limits are finalized with agreed tolerances. The process typically takes 2–6 months for an established supplier relationship. The key metric is Cpk ≥ 1.33 for continuous parameters, meaning the process spread occupies no more than 75% of the specification tolerance.

**Q: What happens when both buyer and seller have valid test results that disagree?**
A: This is resolved by the **arbitration clause** in the contract. Standard procedure: (1) Both parties compare their test methods, sample handling, and instrument calibration records. (2) A third, mutually agreed ISO 17025-accredited laboratory receives replicate samples blind-coded from both labs and conducts independent testing. (3) The third-party results are binding on both parties. (4) The cost of arbitration is typically borne by the party whose result is found to be in error. Arbitration turnaround: 5–10 business days for routine parameters; 10–15 days for full HPLC pesticide/mycotoxin screening.

**Q: Can a shipment be accepted if it meets microbiological acceptance criteria but fails ASTA?**
A: Yes — the acceptance criteria are parameter-specific. A shipment may pass microbiology (safe to consume) but fail ASTA (insufficient coloring power). The remedy for an ASTA failure is typically a price discount or relabeling for a lower-color-grade application, not destruction. Conversely, a shipment that passes ASTA but fails *Salmonella* acceptance criteria is *not* acceptable under any circumstances — food safety concerns override quality concerns. The priority order is: Critical food safety (Salmonella, E. coli, aflatoxin) > Regulatory (heavy metals, pesticide MRLs) > Commercial quality (ASTA, moisture, particle size).

**Q: What is the typical shelf-life acceptance criterion for paprika?**
A: The standard shelf-life acceptance criterion is: "**Product shall retain ≥ 90% of the initial ASTA color value for 12 months from the date of shipment, when stored under the following conditions: ≤ 25°C, ≤ 60% RH, in original sealed packaging, protected from direct light.**" Some premium contracts require ≥ 90% retention for 18 months, or ≥ 85% for 24 months. The supplier provides a projected degradation curve based on accelerated shelf-life testing (ASLT, typically 40°C/75% RH for 6 months, modeled to 25°C using the Arrhenius equation with Ea ≈ 72 kJ/mol). This criterion is separate from the acceptance criteria at the point of shipment — it is a *post-shipment warranty* that effective at the buyer's facility.

---

*This document is part of the official technical documentation library for **paprikabulk.com** operated by Dinweys (Qingdao).Co.,Ltd. All rights reserved. For the latest version, visit https://paprikabulk.com.*
