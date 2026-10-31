from data_io import baca_data
from analisis import analisis_nilai
from utilitas import tampilkan_laporan


def main():
    print("PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA")

    # Membaca data siswa
    data_siswa = baca_data()

    # Memeriksa apakah data tersedia
    if not data_siswa:
        print("Tidak ada data siswa yang dapat dianalisis.")
        return

    # Melakukan analisis nilai
    hasil = analisis_nilai(data_siswa, kkm=75)

    # Menampilkan laporan
    tampilkan_laporan(data_siswa, hasil)


if __name__ == "__main__":
    main()