Oke! Aku akan buatkan `README.md` yang lebih profesional dan matang, dengan bahasa yang menarik tapi tetap jelas dan rapi, cocok untuk dipajang di GitHub. Berikut hasil akhirnya:

---

### 📄 `README.md`

````markdown
# 🕷️ Web Spider v2.1

**Web Spider v2.1** adalah tool sederhana berbasis Python yang berfungsi untuk melakukan crawling pada daftar URL yang kamu miliki. Tool ini akan membantu kamu menemukan:

- Halaman-halaman tersembunyi (*hidden pages*)
- Parameter yang terdeteksi dari link
- Redirect URL
- Sumber gambar (`<img src>`) pada halaman

Cocok digunakan untuk kegiatan **reconnaissance** saat melakukan pentesting secara legal dan etis.

---

## ✨ Fitur Utama

- 🔎 Menelusuri semua link (`<a href>`) di halaman web
- 🌐 Mengidentifikasi internal & external link
- 🖼️ Mendapatkan URL gambar (`<img src>`)
- ⚡ Menampilkan hasil secara cepat dan real-time
- 🎭 Tampilan khas script underground lengkap dengan ASCII art dan running text

---

## 🧰 Kebutuhan Sistem

- Python 3.x
- Library:
  - `requests`
  - `beautifulsoup4`

Install dependencies dengan:

```bash
pip install -r requirements.txt
````

Atau secara manual:

```bash
pip install requests beautifulsoup4
```

---

## ▶️ Cara Menggunakan

1. Siapkan file `.txt` yang berisi daftar URL target, satu per baris:

   ```
   https://example.com
   https://subdomain.example.com
   ```

2. Jalankan script:

   ```bash
   python web_spider.py
   ```

3. Masukkan nama file saat diminta:

   ```
   File: target.txt
   ```

4. Hasil crawling akan ditampilkan di terminal, termasuk halaman yang ditemukan, redirect, dan gambar.

---

## 🧑‍💻 Tentang Developer

* 👨‍💻 **Nama:** SidabutarXCode as  ZEUSSEC1337
* 💬 **GitHub:** [sidabutar1337](https://github.com/sidabutar1337)

---

## ☕ Dukung Pengembangan

Kalau kamu suka dengan tool ini dan ingin mendukung saya untuk terus berkarya, kamu bisa memberikan dukungan melalui:

[![Donate via Saweria](https://img.shields.io/badge/Donate-Saweria-orange?style=for-the-badge\&logo=ko-fi)](https://saweria.co/zeussec1337)

---

## ⚠️ Disclaimer

> Tool ini dibuat **hanya untuk pembelajaran dan tujuan etis**.
> Segala bentuk penyalahgunaan terhadap tool ini merupakan tanggung jawab pribadi pengguna.
> Jangan gunakan pada situs tanpa izin eksplisit dari pemiliknya.

---

```

---

Kalau kamu ingin sekalian dibuatkan `requirements.txt` atau ingin script-nya dibungkus jadi package CLI, tinggal bilang. Saya bisa bantu bikin versi upgrade-nya juga!
```
