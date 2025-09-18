# Capstone Project 1  
**Purwadhika Data Engineering Bootcamp — by Alfian Febiyanto**

Project ini merupakan bagian dari tugas akhir (Capstone Project 1) dalam rangkaian **Purwadhika Data Engineering Bootcamp**. Repository ini saya gunakan untuk mendemonstrasikan keterampilan fundamental dalam **ETL pipeline**: data ingestion, cleaning, dan transformation menggunakan **Python (Pandas)**.  

---

## Project Overview  
Project ini berfokus pada dua dataset utama:  
- **data_products.csv**  
- **data_requirements.csv**  

Tahapan yang saya kerjakan meliputi:  
1. **Data Ingestion** → membaca file `.csv` ke dalam Python.  
2. **Data Cleaning & Transformation** → menghapus data tidak valid, mengubah tipe data, serta melakukan standarisasi.  
3. **Exploratory Analysis** → menampilkan **Data Demography** sebagai gambaran umum dataset menggunakan teknik dasar analisis data.  

---

## Deliverables  
- Notebook utama: **`capstone.ipynb`** (menjelaskan langkah-langkah analisis dan transformasi).  
- Folder **data** tidak ditampilkan karena ukurannya melebihi 100MB (batas GitHub).  
- **Alternatif**: penggunaan Git LFS sudah dicoba, namun saat ini masih terkendala upload.  

**Video Penjelasan Project**: [Link Video di sini](https://youtu.be/xnvgH0_mnNQ?si=pw7cn6tE89XfsGQ4) 

**Dataset & File Lengkap**: [Link File di sini](https://drive.google.com/drive/folders/1jbq8w5T_DyiR2mW-pH1Qfv3kB7LEBIuC?usp=drive_link)

---

## Tech Stack  
- **Python** (Pandas, NumPy, Matplotlib/Seaborn)  
- **Jupyter Notebook**  
- **Git & GitHub**  

## 🗂️ Struktur Repository  
```bash
etl-project-capstone-1-alfian-febiyanto/
  ├─ config/                  ← konfigurasi global, path
  │   └─ settings.py
  │	
  ├─ data/                    ← semua data
  │   ├─ input/               ← Folder data CSV mentah
  │   │   ├─ product/
  │   │   └─ requirement/
  │   └─ output/              ← hasil akhir ETL
  │
  ├─ src/                     ← modul Python
  │   ├─ transforms.py        ← fungsi cleaning
  │   └─ utils.py             ← helper (extract, load) 
  │
  ├─ main.py                  ← main pipeline
  ├─ Product_clean.ipynb      ← eksplorasi data product
  ├─ Requirement_clean.ipynb  ← eksplorasi data requirement
  ├─ requirements.txt         ← dependencies
  └─ README.md                ← dokumentasi project


