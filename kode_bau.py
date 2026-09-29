"""Modul contoh kode berkualitas baik setelah perbaikan."""


def hitung_total(nilai_awal, nilai_tambahan):
    """Menghitung total dari dua nilai.

    Args:
        nilai_awal: Nilai pertama.
        nilai_tambahan: Nilai kedua.

    Returns:
        Hasil penjumlahan kedua nilai.
    """
    return nilai_awal + nilai_tambahan


def main():
    """Fungsi utama program."""
    hasil = hitung_total(10, 5)
    print(f"Hasil: {hasil}")


if __name__ == "__main__":
    main()
