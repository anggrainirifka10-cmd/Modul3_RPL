from config.database import Database


class BukuModel:

    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()

    def create_buku(self, judul, penulis, tahun_terbit):
        if not self.conn:
            return False

        try:
            cursor = self.conn.cursor()

            query = """
                INSERT INTO buku (judul, penulis, tahun_terbit)
                VALUES (%s, %s, %s)
            """

            values = (judul, penulis, tahun_terbit)

            cursor.execute(query, values)
            self.conn.commit()
            cursor.close()

            return True

        except Exception as e:
            print("Gagal menambahkan buku:", e)
            return False

    def get_all_buku(self):
        if not self.conn:
            return []

        try:
            # Perbaikan di sini: ditambahkan dictionary=True agar format data sesuai dengan controller
            cursor = self.conn.cursor(dictionary=True)

            query = """
                SELECT id_buku, judul, penulis, tahun_terbit
                FROM buku
            """

            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()

            return result

        except Exception as e:
            print("Gagal mengambil data buku:", e)
            return []

    # Fungsi menghapus data buku
    def hapus_buku(self, id_buku):
        if not self.conn:
            return False

        try:
            cursor = self.conn.cursor()

            query = "DELETE FROM buku WHERE id_buku = %s"
            cursor.execute(query, (id_buku,))

            self.conn.commit()
            cursor.close()

            return True

        except Exception as e:
            print("Gagal menghapus buku:", e)
            return False