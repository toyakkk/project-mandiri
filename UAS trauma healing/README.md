# UAS Trauma Healing Counseling CLI

## 📌 Deskripsi Project
Project ini merupakan mini project Ujian Akhir Semester (UAS) mata kuliah **Pemrograman Web Berbasis Objek**.  
Aplikasi dibuat menggunakan **Python berbasis Command Line Interface (CLI)** dengan menerapkan konsep:

- Object Oriented Programming (OOP)
- SOLID Principles
- Logging
- Error Handling
- Unit Testing
- Dokumentasi

Aplikasi ini mensimulasikan sistem sederhana **Trauma Healing Counseling** untuk mencatat data survivor yang akan mengikuti sesi konseling.

---

## 📂 Struktur Folder

UAS_Trauma_Healing/
│
├── models/
│ └── users.py
├── repositories/
│ └── survivor_repo.py
├── services/
│ └── counseling.py
├── utils/
│ ├── logger.py
│ └── notifications.py
├── tests/
│ └── test_service.py
├── main.py
└── README.md



---

## 🎯 Tujuan Project
- Menerapkan konsep **OOP** dalam pembuatan aplikasi
- Mengimplementasikan prinsip **SOLID**
- Menangani error dan logging dengan baik
- Menyediakan **unit testing** untuk memastikan reliabilitas program
- Membuat aplikasi CLI yang terstruktur dan mudah dipahami

---

## 🧩 Implementasi Konsep

### 1️⃣ Object Oriented Programming (OOP)
File: `models/users.py`

- Class `User` sebagai class induk
- Class `Survivor` sebagai turunan dari `User`
- Menerapkan:
  - Class & Object
  - Inheritance
  - Polymorphism (method overriding)

---

### 2️⃣ SOLID Principles
#### a. Interface Segregation Principle
File: `repositories/survivor_repo.py`

- Menggunakan abstract class `SurvivorRepository`
- Memisahkan interface dan implementasi repository

#### b. Dependency Injection
File: `services/counseling.py`

- Repository di-*inject* ke dalam `CounselingService`
- Service tidak bergantung pada implementasi konkret

---

### 3️⃣ Logging
File: `utils/logger.py`

- Menggunakan modul `logging`
- Mencatat aktivitas penting seperti:
  - Registrasi survivor
  - Penampilan data survivor

---

### 4️⃣ Error Handling & CLI
File: `main.py`

- Aplikasi berbasis menu CLI
- Menggunakan `try-except` untuk menangani error input pengguna
- Mencegah program berhenti secara tiba-tiba

---

### 5️⃣ Unit Testing
File: `tests/test_service.py`

- Menggunakan modul `unittest`
- Menguji fungsi registrasi survivor
- Memastikan data berhasil disimpan di repository

---

## ▶️ Cara Menjalankan Program
1. Pastikan Python sudah terinstal
2. Buka terminal pada folder project
3. Jalankan perintah:
   ```bash
   python main.py


## **Contoh Output Program**
=== Trauma Healing Counseling CLI ===
1. Register Survivor
2. List Survivors
3. Exit
Choose menu: 1
User ID: 1
Name: Athaya
Trauma Type: Trauma Emosional
✅ Survivor registered successfully
