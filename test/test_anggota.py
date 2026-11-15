from models.anggota_model import AnggotaModel


model = AnggotaModel()

# 1. Menguji fungsi Create (menambah anggota baru)
print("Menambah data anggota...")
if model.create_anggota("Eko Prasetyo", "Jl. Gatot Subroto No. 21"):
    print("Data berhasil disimpan ke Laragon MySQL!")
else:
    print("Gagal menyimpan data.")

# 2. Menguji fungsi Read (menampilkan data)
print("\n=== Daftar Anggota ===")
daftar_anggota = model.get_all_anggota()
for anggota in daftar_anggota:
    print(
        f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}"
    )