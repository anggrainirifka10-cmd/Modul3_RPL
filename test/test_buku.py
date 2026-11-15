from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()
    
    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor
    
    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)
    
    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()


# --- TAMBAHAN UNTUK TUGAS 3 (Disesuaikan dengan format Tuple) ---
def test_get_all_buku():
    # 1. Inisialisasi Model
    model = BukuModel()
    
    # 2. Mock koneksi dan cursor database
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor
    
    # Menentukan data dummy berupa tuple (id_buku, judul, penulis, tahun_terbit)
    dummy_data = [
        (1, "Belajar Python", "Dicky", 2025),
        (2, "Pemrograman RPL", "Admin", 2026)
    ]
    mock_cursor.fetchall.return_value = dummy_data
    
    # 3. Eksekusi fungsi get_all_buku
    hasil = model.get_all_buku()
    
    # 4. Verifikasi hasil pengujian berdasarkan indeks tuple
    assert isinstance(hasil, list)
    assert len(hasil) == 2
    
    # Menggunakan indeks angka karena data berupa tuple:
    # Indeks [0] = id_buku, [1] = judul, [2] = penulis, [3] = tahun_terbit
    assert hasil[0][1] == "Belajar Python"
    assert hasil[1][2] == "Admin"
    
    # Memastikan kueri SELECT dijalankan oleh kursor
    mock_cursor.execute.assert_called_once()