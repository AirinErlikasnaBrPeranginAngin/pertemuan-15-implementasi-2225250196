from pathlib import Path


def baca_data():
    lokasi_file = Path(__file__).resolve().parent.parent / "data" / "nilai_contoh.txt"

    data_siswa = []

    try:
        with open(lokasi_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                if not baris:
                    continue

                bagian = baris.split(",")

                if len(bagian) != 2:
                    print(f"Format data tidak sesuai: {baris}")
                    continue

                nama = bagian[0].strip()

                try:
                    nilai = float(bagian[1].strip())
                except ValueError:
                    print(f"Nilai tidak valid: {baris}")
                    continue

                if 0 <= nilai <= 100:
                    data_siswa.append({
                        "nama": nama,
                        "nilai": nilai
                    })
                else:
                    print(f"Nilai di luar rentang: {baris}")

    except FileNotFoundError:
        print("File data tidak ditemukan.")

    return data_siswa