PROPOSAL PROYEK

Program Rekap dan Analisis Nilai Matematika Siswa

1. Judul Proyek

Program Rekap dan Analisis Nilai Matematika Siswa.

2. Latar Belakang

Pengolahan nilai siswa sering dilakukan secara manual sehingga membutuhkan waktu dan berisiko terjadi kesalahan perhitungan. Oleh karena itu, dibuat program sederhana menggunakan Python untuk membantu mengolah dan menganalisis nilai matematika siswa secara lebih mudah dan cepat.

3. Pengguna dan Tujuan

Pengguna: Guru matematika atau pengguna yang membutuhkan pengolahan nilai siswa.

Tujuan:

- Mempermudah proses rekapitulasi nilai siswa.
- Menghitung rata-rata, nilai tertinggi, dan nilai terendah.
- Mengetahui jumlah siswa yang lulus dan tidak lulus berdasarkan KKM.

4. Ruang Lingkup

Program memiliki ruang lingkup:

- Membaca data nilai siswa dari file.
- Memeriksa validitas nilai.
- Menghitung statistik nilai.
- Menentukan status kelulusan berdasarkan KKM.
- Menampilkan dan menyimpan hasil analisis.

5. Kebutuhan Fungsional dan Nonfungsional

Kebutuhan fungsional:

1. Program dapat membaca data nilai siswa.
2. Program dapat memvalidasi nilai antara 0 sampai 100.
3. Program dapat menghitung rata-rata nilai.
4. Program dapat menentukan nilai tertinggi dan terendah.
5. Program dapat menghitung jumlah siswa lulus dan tidak lulus.
6. Program dapat menyimpan laporan hasil analisis.

Kebutuhan nonfungsional:

1. Program dibuat menggunakan bahasa Python.
2. Program dijalankan melalui terminal.
3. Program memiliki tampilan teks yang sederhana.
4. Program mudah digunakan dan dipahami.

6. IPO (Input, Process, Output)

Input:

- Nama siswa.
- Nilai matematika siswa.
- Nilai KKM.

Process:

- Membaca data siswa.
- Memeriksa validitas nilai.
- Menghitung rata-rata nilai.
- Menentukan nilai tertinggi dan terendah.
- Menghitung jumlah siswa yang lulus dan tidak lulus.

Output:

- Daftar nilai siswa.
- Rata-rata nilai.
- Nilai tertinggi dan terendah.
- Jumlah siswa lulus dan tidak lulus.
- Laporan hasil analisis.

7. Algoritma atau Pseudocode

MULAI
Baca data nilai siswa
Tentukan nilai KKM
Periksa setiap nilai siswa
Jika nilai berada antara 0 dan 100:
    Simpan nilai
Jika tidak:
    Tampilkan pesan kesalahan

Jika data nilai tersedia:
    Hitung rata-rata
    Cari nilai tertinggi
    Cari nilai terendah
    Hitung jumlah siswa lulus
    Hitung jumlah siswa tidak lulus
    Tampilkan hasil analisis
    Simpan laporan
Jika tidak:
    Tampilkan pesan bahwa data kosong
SELESAI

8. Struktur Program dan Folder

pertemuan-14-blueprint-2225250196/
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
    └── .gitkeep

9. Struktur Data

Struktur data yang digunakan:

- List untuk menyimpan kumpulan data siswa.
- Dictionary untuk menyimpan nama dan nilai setiap siswa.
- Variabel numerik untuk menyimpan hasil perhitungan.

Contoh data:

[
    {"nama": "Ani", "nilai": 80},
    {"nama": "Budi", "nilai": 70},
    {"nama": "Citra", "nilai": 90}
]

10. Rencana Pengujian (Test Case)

No.| Kondisi Pengujian| Hasil yang Diharapkan
1| Nilai 80, 70, 90| Rata-rata 80
2| Nilai 0| Diterima sebagai nilai valid
3| Nilai 100| Diterima sebagai nilai valid
4| Nilai 105| Ditolak karena di luar rentang
5| File data tidak ditemukan| Program menampilkan pesan kesalahan
6| Semua nilai di atas atau sama dengan KKM| Semua siswa dinyatakan lulus

11. Pembagian Tugas (PIC)

Proyek dikerjakan secara individu.

No.| Tugas| Penanggung Jawab
1| Perancangan proyek| Diri sendiri
2| Pembuatan program Python| Diri sendiri
3| Pengujian program| Diri sendiri
4| Dokumentasi proyek| Diri sendiri
5| Pengelolaan GitHub| Diri sendiri

12. Jadwal dan Milestone

Pertemuan| Kegiatan
14| Perancangan blueprint dan proposal proyek
15| Implementasi, pengujian, dan dokumentasi program
16| Penyelesaian dan presentasi proyek

13. URL Repository GitHub

https://github.com/USERNAME/pertemuan-14-blueprint-2225250196