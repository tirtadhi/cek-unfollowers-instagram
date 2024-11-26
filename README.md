# Instagram Follow-Back Checker

Script Python ini digunakan untuk memeriksa siapa saja yang tidak mem-follow back akun Instagram Anda, berdasarkan data followers dan following yang diekspor dari Instagram.

## Fitur
- Mengekstrak data username dari file `followers.json` dan `following.json`.
- Membandingkan data followers dan following untuk menemukan akun yang tidak mem-follow back.

## Persiapan

1. Ekspor data followers dan following dari Instagram:
   - Masuk ke akun Instagram Anda.
   - Buka **Settings** → **Privacy and Security** → **Download Data**.
   - Unduh data dan ekstrak file ZIP.
   - Cari file `followers.json` dan `following.json` di folder hasil ekstrak.

2. Simpan kedua file tersebut (`followers.json` dan `following.json`) untuk diunggah pada langkah selanjutnya.

## Langkah-Langkah Menggunakan Google Colab

1. **Buka Google Colab**
   - Akses [Google Colab](https://colab.research.google.com) melalui browser.

2. **Buat Notebook Baru**
   - Klik **New Notebook** untuk membuat notebook baru.

3. **Unggah File JSON**
   - Di panel kiri, klik ikon **Folder** untuk membuka file explorer.
   - Klik ikon **Upload** dan unggah file `followers.json` dan `following.json`.

4. **Salin Script**
   - Salin dan tempel kode Python berikut ke dalam sel kode di Colab
     
5. **Jalankan Script**
   - Klik tombol Run (ikon ▶️) di atas sel untuk menjalankan kode.
7. **Lihat Hasil**
   - Daftar akun yang tidak mem-follow back Anda akan ditampilkan di output sel kode.
