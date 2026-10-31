from pathlib import Path


def tampilkan_laporan(data_siswa, hasil):
    laporan = []

    laporan.append("===== LAPORAN NILAI MATEMATIKA =====")
    laporan.append("\nDaftar Nilai Siswa:")

    for siswa in data_siswa:
        laporan.append(f"{siswa['nama']} : {siswa['nilai']}")

    laporan.append("\nHasil Analisis:")
    laporan.append(f"Rata-rata nilai        : {hasil['rata_rata']:.2f}")
    laporan.append(f"Nilai tertinggi        : {hasil['tertinggi']}")
    laporan.append(f"Nilai terendah         : {hasil['terendah']}")
    laporan.append(f"Jumlah siswa lulus     : {hasil['jumlah_lulus']}")
    laporan.append(f"Jumlah siswa tidak lulus: {hasil['jumlah_tidak_lulus']}")
    laporan.append("====================================")

    # Menampilkan laporan di terminal
    isi_laporan = "\n".join(laporan)
    print(isi_laporan)

    # Menyimpan laporan ke folder output
    lokasi_file = Path(__file__).resolve().parent.parent / "output" / "laporan_nilai.txt"

    with open(lokasi_file, "w", encoding="utf-8") as file:
        file.write(isi_laporan)

    print("\nLaporan berhasil disimpan di output/laporan_nilai.txt")