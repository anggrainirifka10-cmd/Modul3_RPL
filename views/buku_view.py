import tkinter as tk
from tkinter import messagebox, ttk

class BukuView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("850x550")
        
        # --- FRAME FORM (Kiri) ---
        form_frame = tk.LabelFrame(self, text=" Form Data Buku ", font=("Arial", 11, "bold"))
        form_frame.place(x=20, y=20, width=320, height=500)
        
        tk.Label(form_frame, text="Judul Buku", font=("Arial", 9)).pack(anchor="w", padx=15, pady=(15, 5))
        self.entry_judul = tk.Entry(form_frame, font=("Arial", 10))
        self.entry_judul.pack(fill="x", padx=15, pady=5)
        
        tk.Label(form_frame, text="Nama Penulis", font=("Arial", 9)).pack(anchor="w", padx=15, pady=(10, 5))
        self.entry_penulis = tk.Entry(form_frame, font=("Arial", 10))
        self.entry_penulis.pack(fill="x", padx=15, pady=5)
        
        tk.Label(form_frame, text="Tahun Terbit", font=("Arial", 9)).pack(anchor="w", padx=15, pady=(10, 5))
        self.entry_tahun = tk.Entry(form_frame, font=("Arial", 10))
        self.entry_tahun.pack(fill="x", padx=15, pady=5)
        
        # Tombol-tombol aksi (Disimpan ke variabel agar bisa di-bind atau langsung panggil command)
        self.btn_simpan = tk.Button(form_frame, text="Simpan Data", bg="green", fg="white", font=("Arial", 10, "bold"), command=self.aksi_simpan)
        self.btn_simpan.pack(fill="x", padx=15, pady=(25, 10))
        
        self.btn_update = tk.Button(form_frame, text="Perbarui Data (Update)", bg="blue", fg="white", font=("Arial", 10, "bold"), command=self.aksi_perbarui)
        self.btn_update.pack(fill="x", padx=15, pady=10)
        
        self.btn_delete = tk.Button(form_frame, text="Hapus Data (Delete)", bg="red", fg="white", font=("Arial", 10, "bold"), command=self.aksi_hapus)
        self.btn_delete.pack(fill="x", padx=15, pady=10)

        # --- FRAME TABEL (Kanan) ---
        table_frame = tk.LabelFrame(self, text=" Daftar Koleksi Buku ", font=("Arial", 11, "bold"))
        table_frame.place(x=360, y=20, width=470, height=500)
        
        columns = ("id", "judul", "penulis", "tahun")
        
        # Menggunakan self.tabel agar sinkron dengan pemanggilan di Controller
        self.tabel = ttk.Treeview(table_frame, columns=columns, show="headings")
        
        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun")
        
        self.tabel.column("id", width=40, anchor="center")
        self.tabel.column("judul", width=160)
        self.tabel.column("penulis", width=140)
        self.tabel.column("tahun", width=80, anchor="center")
        
        self.tabel.pack(fill="both", expand=True, padx=10, pady=10)
        self.tabel.bind("<<TreeviewSelect>>", self.isi_form_dari_tabel)

    def tampilkan_data(self, data_buku):
        """Memasukkan data langsung dengan ID asli database ke kolom pertama tabel"""
        for item in self.tabel.get_children():
            self.tabel.delete(item)
            
        for row in data_buku:
            # row[0] adalah ID asli dari database (misal: 1, 2, 5, dst.)
            self.tabel.insert("", "end", values=row)

    def isi_form_dari_tabel(self, event):
        """Mengambil data dari baris tabel yang diklik untuk dimasukkan ke form"""
        selected_item = self.tabel.selection()
        if selected_item:
            item = self.tabel.item(selected_item)
            values = item['values']
            
            # Ambil langsung ID dari kolom pertama tabel (indeks ke-0)
            self.selected_id = values[0]
            
            # Masukkan ke input form
            self.entry_judul.delete(0, tk.END)
            self.entry_judul.insert(0, values[1])
            self.entry_penulis.delete(0, tk.END)
            self.entry_penulis.insert(0, values[2])
            self.entry_tahun.delete(0, tk.END)
            self.entry_tahun.insert(0, values[3])

    def aksi_simpan(self):
        judul = self.entry_judul.get()
        penulis = self.entry_penulis.get()
        tahun = self.entry_tahun.get()
        if self.controller.tambah_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil ditambahkan!")
            self.clear_form()

    def aksi_perbarui(self):
        if hasattr(self, 'selected_id'):
            judul = self.entry_judul.get()
            penulis = self.entry_penulis.get()
            tahun = self.entry_tahun.get()
            if self.controller.perbarui_buku(self.selected_id, judul, penulis, tahun):
                messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
                self.clear_form()
        else:
            messagebox.showwarning("Peringatan", "Pilih data buku pada tabel terlebih dahulu!")

    def aksi_hapus(self):
        if hasattr(self, 'selected_id'):
            if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?"):
                if self.controller.hapus_buku(self.selected_id):
                    messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                    self.clear_form()
        else:
            messagebox.showwarning("Peringatan", "Pilih data buku pada tabel terlebih dahulu!")

    def clear_form(self):
        self.entry_judul.delete(0, tk.END)
        self.entry_penulis.delete(0, tk.END)
        self.entry_tahun.delete(0, tk.END)
        if hasattr(self, 'selected_id'):
            del self.selected_id