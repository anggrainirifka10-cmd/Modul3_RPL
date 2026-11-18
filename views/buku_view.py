import tkinter as tk
from tkinter import ttk

class BukuView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("850x550")
        self.resizable(False, False)

        # --- FRAME FORM (Kiri) ---
        form_frame = tk.LabelFrame(self, text=" Form Data Buku ")
        form_frame.place(x=20, y=20, width=320, height=480)

        tk.Label(form_frame, text="Judul Buku").pack(anchor="w", padx=15, pady=(15, 0))
        self.entry_judul = tk.Entry(form_frame)
        self.entry_judul.pack(fill="x", padx=15, pady=5)

        tk.Label(form_frame, text="Nama Penulis").pack(anchor="w", padx=15, pady=(10, 0))
        self.entry_penulis = tk.Entry(form_frame)
        self.entry_penulis.pack(fill="x", padx=15, pady=5)

        tk.Label(form_frame, text="Tahun Terbit").pack(anchor="w", padx=15, pady=(10, 0))
        self.entry_tahun = tk.Entry(form_frame)
        self.entry_tahun.pack(fill="x", padx=15, pady=5)

        self.btn_simpan = tk.Button(form_frame, text="Simpan Data", bg="green", fg="white")
        self.btn_simpan.pack(fill="x", padx=15, pady=(15, 5))

        self.btn_update = tk.Button(form_frame, text="Perbarui Data (Update)", bg="blue", fg="white")
        self.btn_update.pack(fill="x", padx=15, pady=5)

        self.btn_delete = tk.Button(form_frame, text="Hapus Data (Delete)", bg="red", fg="white")
        self.btn_delete.pack(fill="x", padx=15, pady=5)

        # --- TABEL KOLEKSI BUKU (Kanan) ---
        table_frame = tk.LabelFrame(self, text=" Daftar Koleksi Buku ")
        table_frame.place(x=360, y=20, width=470, height=480)

        # Membuat Treeview untuk Tabel
        columns = ("ID", "Judul Buku", "Penulis", "Tahun")
        self.tabel = ttk.Treeview(table_frame, columns=columns, show="headings", height=18)
        
        # Mengatur judul kolom
        self.tabel.heading("ID", text="ID")
        self.tabel.heading("Judul Buku", text="Judul Buku")
        self.tabel.heading("Penulis", text="Penulis")
        self.tabel.heading("Tahun", text="Tahun")

        # Mengatur lebar kolom
        self.tabel.column("ID", width=30, anchor="center")
        self.tabel.column("Judul Buku", width=160)
        self.tabel.column("Penulis", width=140)
        self.tabel.column("Tahun", width=70, anchor="center")

        self.tabel.pack(fill="both", expand=True, padx=10, pady=10)