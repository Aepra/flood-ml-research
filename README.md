# Flood Prediction Research using Machine Learning and Geospatial Data

## Overview

This project focuses on evaluating the **generalization** and **interpretability** of machine learning models for flood prediction using geospatial data.

Unlike typical projects that aim to achieve the highest accuracy, this research emphasizes:

* Understanding how models behave across different regions
* Identifying limitations and failure cases
* Analyzing whether models truly learn physical patterns or just memorize spatial data

---

## Research Objective

The main objective of this project is to:

* Evaluate model performance in both **in-domain** (same region) and **out-of-domain** (different region) scenarios
* Analyze feature importance and model decision-making
* Identify when and why models fail
* Provide insights for real-world deployment of flood prediction systems

---

## Study Areas

* **Training Region:** Makassar, Indonesia
* **Testing Region:** Jakarta, Indonesia (and optionally other regions)

This setup allows evaluation of model generalization across different geographic conditions.

---

## Dataset

The dataset is constructed from multiple geospatial data sources:

### Features:

* Rainfall
* Elevation (DEM)
* Slope
* Land use / land cover
* Distance to river

### Target:

* Flood occurrence (0 = no flood, 1 = flood)

### Data Sources:

* Rainfall: CHIRPS / NASA
* Elevation: SRTM (DEM)
* Land Use: ESA WorldCover
* Rivers: OpenStreetMap
* Flood labels: reports, news, or manual labeling

---

## Project Structure

```
flood-ml-research/
│
├── data/
│   ├── raw/            # Raw geospatial data
│   ├── processed/      # Cleaned dataset
│   └── external/       # Additional data sources
│
├── notebooks/          # Jupyter notebooks for experiments
│
├── src/
│   ├── data/           # Data loading & processing scripts
│   ├── features/       # Feature engineering
│   ├── models/         # Model training
│   └── visualization/  # Visualization tools
│
├── results/
│   ├── figures/        # Plots and maps
│   └── metrics/        # Evaluation results
│
├── docs/
│   └── research_proposal.md
│
├── models/             # Saved models
│
├── requirements.txt
├── README.md
└── main.py
```

---

## Methodology

### 1. Data Collection

Collect multi-source geospatial data.

### 2. Preprocessing

* Data cleaning
* Handling missing values
* Spatial alignment

### 3. Feature Engineering

* Slope calculation
* Distance to river
* Land use encoding

### 4. Modeling

* Random Forest
* XGBoost

### 5. Evaluation

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC

---

## Experiments

* **Baseline Test** (train & test on same region)
* **Generalization Test** (train on Makassar, test on other regions)
* **Feature Importance Analysis**
* **Data Sensitivity Analysis**
* **Error Analysis**
* **Bias Analysis**

---

## Key Focus

This project does NOT aim to build the best-performing model.

Instead, it focuses on:

* Model generalization
* Model interpretability
* Failure analysis
* Real-world applicability

---

## Installation

Clone the repository:

```
git clone https://github.com/your-username/flood-ml-research.git
cd flood-ml-research
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Usage

Run main pipeline:

```
python main.py
```

Or use notebooks:

```
notebooks/
```

---

## Expected Outputs

* Trained machine learning models
* Evaluation metrics
* Feature importance analysis
* Flood risk maps
* Insight into model behavior

---

## Limitations

* Flood data availability may be limited
* Model performance depends heavily on data quality
* Cross-region generalization is inherently challenging

---

## Future Work

* Use deep learning models
* Incorporate temporal data (time-series rainfall)
* Expand to more regions
* Improve flood labeling accuracy

---

## Author

* Name: Abel Eka Putra
* Program: Information Systems
* University: Universitas Hasanuddin

---

## Notes

The most challenging part of this project is not coding, but:

* Interpreting results
* Extracting meaningful insights
* Explaining model behavior

---

## License

This project is for academic and research purposes.
