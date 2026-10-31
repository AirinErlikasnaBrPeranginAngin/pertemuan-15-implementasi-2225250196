Program Rekap dan Analisis Nilai Matematika Siswa

1. Deskripsi Proyek

Program Rekap dan Analisis Nilai Matematika Siswa merupakan proyek sederhana menggunakan bahasa pemrograman Python untuk membantu mengolah data nilai siswa secara otomatis.

Program ini dapat menghitung rata-rata nilai, menentukan nilai tertinggi dan terendah, serta menghitung jumlah siswa yang lulus dan tidak lulus berdasarkan Kriteria Ketuntasan Minimal (KKM).

2. Tujuan

1. Mempermudah pengolahan nilai matematika siswa.
2. Mengurangi kesalahan dalam perhitungan nilai.
3. Menampilkan hasil analisis nilai secara sederhana.
4. Menerapkan implementasi, pengujian, dan debugging program Python.

3. Fitur Program

- Membaca data nilai siswa dari file.
- Memvalidasi nilai dalam rentang 0 sampai 100.
- Menghitung rata-rata nilai siswa.
- Menentukan nilai tertinggi dan terendah.
- Menghitung jumlah siswa lulus dan tidak lulus.
- Menampilkan laporan hasil analisis.
- Menyimpan laporan ke dalam file.

4. Teknologi yang Digunakan

- Python
- Visual Studio Code
- Git
- GitHub

5. Struktur Folder

pertemuan-15-implementasi-2225250196/
├── README.md
├── proposal.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
└── output/
    ├── .gitkeep
    └── laporan_nilai.txt

6. Cara Menjalankan Program

Pastikan Python sudah terpasang pada komputer.

Buka terminal VS Code, kemudian jalankan perintah:

python src/main.py

Program akan membaca data siswa dari folder "data", melakukan analisis, menampilkan hasil di terminal, dan menyimpan laporan ke folder "output".

7. Pengujian Program

Pengujian dilakukan menggunakan enam skenario:

1. Menguji nilai normal.
2. Menguji nilai minimum (0).
3. Menguji nilai maksimum (100).
4. Menguji nilai melebihi batas (105).
5. Menguji kondisi file data tidak ditemukan.
6. Menguji kondisi seluruh siswa lulus.

Hasil pengujian dicatat dalam file "tests/test_case.md".

Berdasarkan pengujian yang dilakukan, keenam skenario berhasil dijalankan sesuai hasil yang diharapkan.

8. Hasil Program

Berdasarkan data contoh yang terdiri dari 10 siswa, diperoleh hasil:

- Rata-rata nilai: 75,80
- Nilai tertinggi: 95
- Nilai terendah: 50
- Jumlah siswa lulus: 6
- Jumlah siswa tidak lulus: 4

Laporan hasil analisis disimpan dalam file "output/laporan_nilai.txt".

9. Dokumentasi

Proyek ini dilengkapi dengan:

- Dokumentasi program melalui README.
- Rancangan proyek melalui proposal.
- Test case untuk pengujian program.
- File laporan hasil analisis nilai.

10. Status Proyek

Proyek telah melalui tahap implementasi, integrasi, pengujian, dan debugging sesuai kegiatan Pertemuan 15.

11. Identitas Pembuat

- Nama: Airin Erlikasna Br Perangin Angin
- NIM: 2225250196
- Program Studi: Pendidikan Matematika
- Mata Kuliah: Algoritma dan Pemrograman
- Pertemuan: 15

12. Repository GitHub

URL repository: Akan ditambahkan setelah repository GitHub khusus Pertemuan 15 dibuat.