# Flood Prediction Research Proposal

## 1. Judul Penelitian

**Evaluating the Generalization and Interpretability of Machine Learning Models for Flood Prediction Using Geospatial Data: A Case Study of Makassar with Cross-Regional Validation**

---

## 2. Tujuan Penelitian

### Tujuan Utama

Mengevaluasi kemampuan generalisasi dan interpretabilitas model machine learning dalam prediksi banjir berbasis data geospasial, serta memahami batasan penggunaannya dalam konteks lintas wilayah.

### Tujuan Spesifik

* Mengukur performa model pada data lokal (in-domain)
* Menguji performa model pada wilayah berbeda (out-of-domain)
* Menganalisis faktor yang mempengaruhi keputusan model
* Mengidentifikasi kondisi di mana model gagal
* Mengevaluasi stabilitas model terhadap perubahan data
* Memberikan rekomendasi penggunaan model dalam skenario nyata

---

## 3. Research Questions

* **RQ1**
  Seberapa baik model machine learning memprediksi banjir pada wilayah tempat model dilatih?

* **RQ2**
  Seberapa besar penurunan performa model ketika diterapkan pada wilayah dengan karakteristik geografis berbeda?

* **RQ3**
  Fitur apa yang paling mempengaruhi keputusan model dalam prediksi banjir?

* **RQ4**
  Dalam kondisi apa model gagal memberikan prediksi yang akurat?

* **RQ5**
  Apakah model benar-benar belajar hubungan fisik (misalnya elevasi, curah hujan), atau hanya memanfaatkan pola lokasi tertentu?

* **RQ6 (Tambahan)**
  Seberapa stabil performa model terhadap perubahan distribusi data dan ukuran dataset?

---

## 4. Hipotesis Awal

* **H1**: Model akan memiliki performa tinggi pada data lokal (in-domain)
* **H2**: Performa model akan menurun signifikan pada wilayah berbeda (out-of-domain)
* **H3**: Elevasi dan curah hujan merupakan fitur dominan dalam prediksi banjir
* **H4**: Model sensitif terhadap perubahan distribusi data
* **H5**: Model cenderung mengalami penurunan interpretabilitas saat diterapkan pada wilayah baru

---

## 5. Desain Data

### 5.1 Variabel

**Fitur:**

* Curah hujan (rainfall intensity)
* Elevasi (elevation)
* Kemiringan (slope)
* Penggunaan lahan (land use / land cover)
* Jarak ke sungai (distance to river)

**Target:**

* Flood (0 = tidak banjir, 1 = banjir)

---

### 5.2 Struktur Dataset

| lat | lon | rainfall | elevation | slope | landuse | distance_river | flood |
| --- | --- | -------- | --------- | ----- | ------- | -------------- | ----- |

---

### 5.3 Sumber Data

* Curah hujan: CHIRPS / NASA
* Elevasi: SRTM (DEM)
* Land use: ESA WorldCover
* Sungai: OpenStreetMap
* Data banjir: laporan pemerintah, berita, atau labeling manual

---

### 5.4 Metode Pembuatan Dataset

* Wilayah dibagi menjadi grid (misalnya 1 km x 1 km)
* Setiap grid menjadi satu baris data
* Nilai fitur diambil berdasarkan posisi geografis grid
* Label banjir ditentukan berdasarkan histori kejadian

---

## 6. Pipeline Penelitian

### Step 1: Data Collection

Mengumpulkan seluruh layer geospasial dari berbagai sumber

**Output:** raw dataset multi-layer

---

### Step 2: Preprocessing

* Cleaning data
* Handling missing values
* Normalisasi
* Penyamaan resolusi spasial (resampling)

**Output:** cleaned & aligned dataset

---

### Step 3: Feature Engineering

* Menghitung slope dari DEM
* Menghitung jarak ke sungai
* Encoding kategori land use
* (Opsional) agregasi temporal curah hujan

**Output:** final feature set

---

### Step 4: Data Splitting

**In-domain:**

* Train: Makassar
* Test: Makassar

**Out-of-domain:**

* Train: Makassar
* Test: Jakarta / wilayah lain

---

### Step 5: Modeling

**Model:**

* Random Forest
* XGBoost

**Alasan:**

* Robust terhadap data tabular
* Tidak membutuhkan resource besar
* Interpretability relatif baik

---

### Step 6: Evaluation

**Metrik:**

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC

**Tambahan:**

* Confusion Matrix (untuk error analysis)

---

## 7. Eksperimen Detail

### Eksperimen 1: Baseline Performance

Mengukur performa model pada data lokal

---

### Eksperimen 2: Generalization Test

Mengukur kemampuan model lintas wilayah

**Fokus:**

* Penurunan performa
* Perubahan pola prediksi

---

### Eksperimen 3: Feature Importance

Menentukan fitur paling berpengaruh

**Tambahan:**

* Bandingkan antar wilayah

---

### Eksperimen 4: Data Sensitivity

Mengukur robustness model

**Variasi:**

* Pengurangan data
* Penambahan noise
* Perubahan distribusi

---

### Eksperimen 5: Error Analysis

Analisis mendalam kesalahan model

**Tambahan:**

* Analisis spasial error (lokasi kesalahan)

---

### Eksperimen 6: Bias Analysis

Mengidentifikasi apakah model bias terhadap lokasi tertentu

**Tambahan:**

* Uji tanpa fitur koordinat
* Bandingkan perubahan performa

---

## 8. Analisis (Bagian Paling Penting)

Fokus utama:

* Apakah model overfit pada wilayah tertentu?
* Seberapa besar penurunan performa lintas wilayah?
* Apakah fitur dominan konsisten antar wilayah?
* Apakah model benar-benar belajar hubungan fisik?
* Kapan dan di mana model gagal?
* Apakah model robust terhadap perubahan data?

---

## 9. Output Penelitian

### Output Teknis

* Dataset geospasial terstruktur
* Model machine learning
* Script eksperimen

### Output Ilmiah

* Insight tentang generalisasi model
* Analisis faktor penyebab banjir
* Pemahaman keterbatasan model

### Output Visual

* Peta risiko banjir
* Grafik performa
* Visualisasi feature importance
* Peta distribusi error

---

## 10. Kontribusi Penelitian

* Evaluasi generalisasi model flood prediction
* Analisis interpretabilitas model berbasis geospasial
* Identifikasi keterbatasan model dalam kondisi nyata
* Framework eksperimen untuk studi lanjutan

---

## 11. Risiko dan Mitigasi

* **Risiko 1:** Data banjir terbatas

  * Solusi: kombinasi beberapa sumber + manual labeling

* **Risiko 2:** Model performa rendah

  * Solusi: fokus pada analisis, bukan performa

* **Risiko 3:** Insight tidak signifikan

  * Solusi: eksplorasi eksperimen lebih dalam

* **Risiko 4:** Data antar wilayah tidak seimbang

  * Solusi: normalisasi dan analisis distribusi data

---

## 12. Timeline

* Minggu 1–2: pengumpulan data
* Minggu 3–4: preprocessing & feature engineering
* Minggu 5–6: modeling
* Minggu 7–8: eksperimen
* Minggu 9: analisis
* Minggu 10: penulisan

---

## 13. Inti Penelitian (Ringkasan)

Penelitian ini tidak bertujuan untuk menghasilkan model terbaik, tetapi untuk:

* Mengevaluasi kemampuan generalisasi model
* Memahami perilaku model
* Mengidentifikasi kondisi kegagalan
* Menghasilkan insight yang dapat digunakan dalam pengembangan model di masa depan

---

## 14. Penilaian Jujur

### Kekuatan:

* Fokus pada problem nyata (generalization)
* Tidak sekadar implementasi
* Memiliki nilai ilmiah

### Kelemahan:

* Sangat bergantung pada kualitas data
* Insight tidak selalu muncul
* Membutuhkan analisis mendalam

---

## Catatan Penting

Versi ini sudah:

* Level penelitian serius
* Siap dijadikan proposal
* Memiliki arah publishable

Namun:

* Bagian tersulit bukan coding
* Melainkan analisis dan interpretasi hasil

---
