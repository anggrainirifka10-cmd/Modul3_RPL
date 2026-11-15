import sys
from pathlib import Path

# Menambahkan root directory (Modul3 RPL) ke sys.path agar modul 'config' dan 'models' terbaca
sys.path.append(str(Path(__file__).resolve().parent.parent))

from models.buku_model import BukuModel

model = BukuModel()

# 1. Menguji fungsi Create (menambah buku baru)
print("Menambah data buku...")
model.create_buku(
    "Pemrograman Python MVC",
    "Guido van Rossum", 
    2023
)
print("Data berhasil disimpan ke Laragon MySQL!")

# 2. Menguji fungsi Read (menampilkan data)
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(
        f"[{buku['id_buku']}] "
        f"{buku['judul']} - "
        f"{buku['penulis']} "
        f"({buku['tahun_terbit']})"
    )

# 3. Menguji fungsi Update (mengubah buku yang terakhir ditambahkan)
if daftar_buku:
    id_target = daftar_buku[-1]['id_buku']

    print(f"\nMengubah data buku dengan ID {id_target}...")
    if model.update_buku(
        id_target,
        "Pemrograman Python MVC (Edisi Revisi)",
        "Guido van Rossum",
        2024
    ):
        print("Data berhasil diubah!")
    else:
        print("Gagal mengubah data (ID tidak ditemukan).")

    print("\n=== Daftar Buku Setelah Update ===")
    for buku in model.get_all_buku():
        print(
            f"[{buku['id_buku']}] "
            f"{buku['judul']} - "
            f"{buku['penulis']} "
            f"({buku['tahun_terbit']})"
        )

    # 4. Menguji fungsi Delete (menghapus buku yang tadi diubah)
    print(f"\nMenghapus data buku dengan ID {id_target}...")
    if model.delete_buku(id_target):
        print("Data berhasil dihapus!")
    else:
        print("Gagal menghapus data (ID tidak ditemukan).")

    print("\n=== Daftar Buku Setelah Delete ===")
    for buku in model.get_all_buku():
        print(
            f"[{buku['id_buku']}] "
            f"{buku['judul']} - "
            f"{buku['penulis']} "
            f"({buku['tahun_terbit']})"
        )
else:
    print("\nTidak ada data untuk diuji update/delete.")