# 📄 Research Proposal (FINAL VERSION)
## Spatio-Temporal Flood Shortcut Learning Diagnosis Framework (ST-FSLD v1.0)

**Version:** 1.0 – Final Q1 Submission Ready  
**Last Updated:** April 2026  
**Domain:** Geospatial Machine Learning / Environmental AI / Model Robustness  
**Core Focus:** Shortcut Learning under Spatio-Temporal Distribution Shift

---

# 1. Research Positioning

Modern machine learning models in environmental prediction (e.g., flood forecasting) often achieve high in-domain performance but fail under distribution shifts. This raises a critical concern: models may not learn physical processes, but instead rely on **shortcut features** such as spatial coordinates or temporal correlations.

This research positions itself in the intersection of:
- Geospatial Machine Learning
- Out-of-Distribution (OOD) Generalization
- Shortcut Learning Diagnosis
- Environmental Risk Modeling (Floods)

The core objective is not prediction accuracy, but **diagnosis of model behavior under spatio-temporal shifts**.

---

# 2. Problem Statement

Despite strong predictive performance of ML models in flood prediction tasks, there is limited understanding of:

> Whether models learn physically meaningful relationships or rely on spurious spatial-temporal shortcuts.

Current literature lacks:
- Systematic evaluation under spatial AND temporal shift simultaneously
- Quantitative metrics for shortcut learning severity
- Multi-layer diagnostic frameworks combining behavioral, intervention, and causal tests
- Controlled geospatial perturbation experiments

This leads to unreliable models when deployed outside training regions or time periods.

---

# 3. Research Objectives

## Primary Objective
To develop a diagnostic framework for identifying shortcut learning in spatio-temporal flood prediction models under distribution shift.

## Specific Objectives
1. Measure model degradation under spatial and temporal shift conditions
2. Quantify reliance on spatial coordinates (latitude/longitude)
3. Evaluate physical consistency of model predictions
4. Identify and categorize failure modes in OOD conditions
5. Develop a unified Shortcut Learning Score
6. Propose causal consistency evaluation for geospatial ML models

---

# 4. Research Questions

- RQ1: How significantly do flood prediction models degrade under spatial shift?
- RQ2: How sensitive are models to temporal distribution changes?
- RQ3: Do models rely on geographic coordinates as predictive shortcuts?
- RQ4: Do predictions follow physically consistent hydrological rules?
- RQ5: What types of failure modes dominate under distribution shift?
- RQ6: Can shortcut learning be quantified into a single diagnostic score?

---

# 5. Hypotheses

- H1: Models exhibit significant performance degradation under spatial shift
- H2: Temporal shift reveals hidden seasonal shortcut dependencies
- H3: Latitude/longitude are dominant proxy features in model decisions
- H4: Models violate physical monotonicity constraints in flood processes
- H5: Failure modes cluster into spatial, temporal, and physical inconsistency types
- H6: A unified shortcut score can reliably measure model robustness

---

# 6. Dataset Design

## Fundamental Unit
Each data point is defined as:

> (latitude, longitude, date) → feature vector → flood label

## Spatial Design
- Grid resolution: 250m × 250m
- Regions: Makassar, Jakarta (Indonesia)
- CRS: WGS84 / UTM Zone 50S

## Temporal Design
- Daily resolution
- Time span: 2018–2022
- Strict temporal separation for testing (no leakage)

## Label Definition
Flood event derived from Sentinel-1 SAR backscatter:
- Threshold-based classification (-3 dB change)

---

# 7. Data Sources

- CHIRPS: precipitation data
- SRTM: elevation model
- ESA WorldCover: land use classification
- OpenStreetMap: river network
- Sentinel-1: flood event detection (SAR)

---

# 8. Methodology Pipeline

1. Data acquisition from multi-source geospatial datasets
2. Spatial alignment and CRS normalization
3. Resampling to unified 250m grid
4. Feature engineering (hydrological + topographic + spatial)
5. Train-test splitting (spatial + temporal)
6. Model training (Random Forest, XGBoost)
7. Evaluation under multiple distribution shift scenarios
8. Diagnostic analysis (feature, physical, causal)

---

# 9. Experimental Design

## Layer 1: In-Domain Evaluation
- Train and test within same region
- Establish performance baseline

## Layer 2: Distribution Shift
- Spatial shift: Makassar → Jakarta
- Temporal shift: 2018–2020 → 2021–2022

## Layer 3: Intervention Tests
- Spatial perturbation (noise injection)
- Spatial shuffle (structure destruction)
- Feature ablation (lat/lon removal)
- Counterfactual modification

## Layer 4: Causal & Physical Validation
- Monotonicity testing
- Physical law consistency
- Causal consistency scoring

---

# 10. Shortcut Learning Score

A unified metric:

\[
S = \frac{AUC_{in-domain} - AUC_{shift}}{AUC_{in-domain}}
\]

Where:
- Higher S → stronger shortcut dependency
- S ≈ 0 → robust generalization
- S → 1 → complete failure under shift

---

# 11. Failure Mode Taxonomy

1. Spatial Memorization Failure  
   → reliance on latitude/longitude encoding

2. Temporal Shortcut Failure  
   → seasonal correlation exploitation

3. Hydrological Inconsistency  
   → violation of rainfall-flood relationship

4. Feature Proxy Dominance  
   → non-physical feature over-dependence

---

# 12. Analysis Framework

## Layered Diagnostic Structure

### Layer A: Behavioral
- AUC degradation under shift

### Layer B: Feature Dependency
- SHAP importance
- Permutation analysis
- Ablation sensitivity

### Layer C: Intervention Response
- Perturbation tests
- Feature removal impact
- Counterfactual response

### Layer D: Mechanistic Consistency
- Physical monotonicity
- Causal alignment score

---

# 13. Expected Findings

- Significant performance drop under spatial shift
- Strong dependency on spatial coordinates
- Weak generalization to unseen regions
- Violation of physical hydrological constraints
- Emergence of spatial memorization patterns
- Clear dominance of shortcut features over physical variables

---

# 14. Contributions

1. A unified diagnostic framework for shortcut learning in geospatial ML
2. A multi-layer evaluation system (behavioral → causal)
3. A new Shortcut Learning Score (S)
4. Empirical evidence of spatial memorization in flood models

---

# 15. Risks & Mitigation

| Risk | Mitigation |
|------|-----------|
| Data leakage | Strict spatial-temporal splitting |
| Overfitting | Cross-region validation |
| Raster misalignment | CRS normalization (GeoPandas pipeline) |
| Feature bias | Ablation + SHAP analysis |
| Model instability | Multiple model comparison |

---

# 16. Core Insight

This research reframes flood prediction from:

> “How accurate is the model?”

to

> “What does the model actually learn?”

The central claim is that high performance does not imply physical understanding. Instead, many geospatial ML models rely on **shortcut learning mechanisms that fail under distribution shift**.

---

# END OF DOCUMENT