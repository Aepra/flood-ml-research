# Flood Prediction Research Proposal (Revised & Strengthened)

---

## 1. Title

**Evaluating the Generalization, Temporal Dynamics, and Spatial Bias of Machine Learning Models for Flood Prediction Using Multi-Source Geospatial Data: A Spatio-Temporal Study of Makassar with Cross-Regional Validation**

---

## 2. Research Positioning

Most existing flood prediction studies prioritize predictive accuracy within a specific region and time period. However, such approaches often fail to address deeper scientific questions:

> Do machine learning models truly capture the physical processes of flooding, or do they rely on spatio-temporal shortcuts such as location and seasonality?

This research focuses on:

- Spatial generalization (cross-region)
- Temporal generalization (cross-year)
- Model reliance on physical vs spatio-temporal correlations
- Behavior under distribution shift

---

## 3. Research Objectives

### Main Objective

To evaluate whether machine learning models truly learn physical flooding processes or rely on spatio-temporal shortcuts.

### Specific Objectives

- Evaluate in-domain performance
- Measure cross-region performance degradation
- Measure cross-year performance degradation
- Analyze feature importance
- Detect spatial bias
- Identify failure patterns
- Evaluate robustness

---

## 4. Research Questions

### RQ1 — In-Domain Performance  
Seberapa baik model memprediksi banjir pada wilayah training?

### RQ2 — Cross-Region Generalization  
Seberapa besar penurunan performa pada wilayah lain?

### RQ3 — Temporal Generalization  
Seberapa stabil performa antar tahun?

### RQ4 — Feature Importance  
Fitur apa yang paling mempengaruhi model?

### RQ5 — Spatial Bias (Core)  
Apakah model bergantung pada lokasi (lat/lon)?

### RQ6 — Failure Analysis  
Dalam kondisi apa model gagal?

---

## 5. Hypotheses

- H1: Model tinggi di in-domain  
- H2: Performa turun di cross-region  
- H3: Performa turun antar tahun  
- H4: Rainfall & elevation dominan  
- H5: Model bergantung pada lokasi  
- H6: Model gagal pada kondisi ekstrem tertentu  

---

## 6. Data Design

### 6.1 Spatio-Temporal Concept

Satu baris data merepresentasikan kombinasi lokasi dan waktu:

(lokasi, waktu) = 1 observasi

---

### 6.2 Features

**Environmental**
- rainfall
- rainfall_3day
- rainfall_7day

**Topographic**
- elevation
- slope

**Land**
- landuse

**Hydrological**
- distance_river

**Spatial (for bias testing)**
- lat
- lon

---

### 6.3 Target

flood = 0 (tidak banjir) / 1 (banjir)

---

### 6.4 Dataset Structure

| lat | lon | date | rainfall | rainfall_3day | rainfall_7day | elevation | slope | landuse | distance_river | flood | region |

Primary key:
lat + lon + date

---

### 6.5 Temporal Sampling Strategy

Event-based sampling:

- Identifikasi event banjir
- Ambil periode sebelum banjir (pre-flood)
- Ambil periode saat banjir

Dynamic window:
pre-flood period + flood period

---

### 6.6 Seasonal Bias Control

- Tidak menggunakan fitur month
- Campurkan data flood dan non-flood dalam musim hujan
- Tambahkan sebagian data dari musim kering

---

### 6.7 Temporal Coverage

2018 – 2022

---

## 7. Data Sources

- Rainfall: CHIRPS / NASA  
- Elevation: SRTM (DEM)  
- Land use: ESA WorldCover  
- River data: OpenStreetMap  
- Flood labeling: Sentinel-1 (Google Earth Engine)  

---

## 8. Methodology Pipeline

### Step 1 — Data Collection
Mengumpulkan seluruh data geospasial

### Step 2 — Flood Label Generation
- Sentinel-1 SAR imagery  
- Perbandingan sebelum vs saat banjir  
- Thresholding untuk deteksi air  

### Step 3 — Preprocessing
- Cleaning  
- Missing value handling  
- Normalization  
- Spatial alignment  

### Step 4 — Feature Engineering
- Rainfall aggregation (3-day, 7-day)  
- Slope calculation  
- Distance to river  
- Encoding land use  

### Step 5 — Data Splitting

Temporal split:
Train: 2018–2020  
Test: 2021–2022  

Spatial split:
Train: Makassar  
Test: Jakarta  

---

### Step 6 — Modeling

- Random Forest  
- XGBoost  

---

### Step 7 — Evaluation

- Accuracy  
- Precision  
- Recall  
- F1-score  
- ROC-AUC  
- Confusion Matrix  

---

## 9. Experimental Design

### Experiment 1 — Baseline
Train dan test di Makassar  

---

### Experiment 2 — Cross Region
Train Makassar → Test Jakarta  

---

### Experiment 3 — Temporal Generalization
Train tahun lama → Test tahun baru  

---

### Experiment 4 — Feature Importance
- Random Forest / XGBoost  
- SHAP analysis  

---

### Experiment 5 — Spatial Bias Test (Core)

- Model A: dengan lat/lon  
- Model B: tanpa lat/lon  

---

### Experiment 6 — Error Analysis
- False Positive  
- False Negative  
- Distribusi spasial error  

---

### Experiment 7 — Sensitivity Analysis
- Pengurangan data training  
- Penambahan noise  
- Perubahan distribusi data  

---

## 10. Analysis Focus

- Penurunan performa lintas wilayah  
- Stabilitas antar tahun  
- Konsistensi feature importance  
- Indikasi spatial bias  
- Pola kegagalan model  
- Robustness terhadap perubahan data  

---

## 11. Expected Outputs

### Technical
- Dataset spatio-temporal  
- Model machine learning  
- Pipeline eksperimen  

### Scientific
- Insight tentang generalisasi model  
- Bukti adanya/tidaknya spatial bias  
- Pemahaman keterbatasan model  

### Visual
- Peta banjir  
- Grafik performa  
- Feature importance plot  
- Peta distribusi error  

---

## 12. Contributions

- Evaluasi generalisasi model geospasial  
- Identifikasi spatial bias dalam ML  
- Framework spatio-temporal dataset  
- Insight interpretability lintas wilayah  

---

## 13. Risks and Mitigation

### Risks
- Noise pada label Sentinel-1  
- Data imbalance  
- Missing data  

### Mitigation
- Filtering noise  
- Balanced sampling  
- Multi-source validation  

---

## 14. Timeline

- Week 1–2: Data collection  
- Week 3–4: Flood labeling  
- Week 5–6: Feature engineering  
- Week 7–8: Modeling & experiments  
- Week 9: Analysis  
- Week 10: Writing  

---

## 15. Core Insight

Penelitian ini tidak bertujuan membuat model terbaik, tetapi:

- Menguji kemampuan generalisasi  
- Memahami perilaku model  
- Mengidentifikasi kegagalan  
- Menentukan apakah model belajar fisika atau hanya lokasi  

---

## 16. Honest Assessment

### Strengths
- Fokus riset kuat (generalization + bias)  
- Bukan sekadar implementasi ML  
- Potensi publishable  

### Limitations
- Bergantung pada kualitas data  
- Kompleks secara implementasi  
- Insight tidak dijamin muncul  

---

## Final Note

The hardest part of this research is not building the model,  
but understanding what the model actually learns.