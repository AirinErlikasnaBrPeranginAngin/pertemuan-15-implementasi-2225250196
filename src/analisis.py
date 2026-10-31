def analisis_nilai(data_siswa, kkm=75):
    if not data_siswa:
        return None

    daftar_nilai = [siswa["nilai"] for siswa in data_siswa]

    rata_rata = sum(daftar_nilai) / len(daftar_nilai)
    nilai_tertinggi = max(daftar_nilai)
    nilai_terendah = min(daftar_nilai)

    jumlah_lulus = sum(
        1 for nilai in daftar_nilai if nilai >= kkm
    )

    jumlah_tidak_lulus = len(daftar_nilai) - jumlah_lulus

    return {
        "rata_rata": rata_rata,
        "tertinggi": nilai_tertinggi,
        "terendah": nilai_terendah,
        "jumlah_lulus": jumlah_lulus,
        "jumlah_tidak_lulus": jumlah_tidak_lulus
    }