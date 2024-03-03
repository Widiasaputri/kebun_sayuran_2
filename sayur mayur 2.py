class Node:
    def __init__(self, nomor_sayuran, nama, teknik, jumlah, hari, harga):
        self.nomor_sayuran = nomor_sayuran
        self.data = {
            'nama': nama,
            'teknik': teknik,
            'jumlah': jumlah,
            'hari': hari,
            'harga': harga
        }
        self.next = None

class Kebun:
    def __init__(self):
        self.head = None
        self.tail = None
        self.banyak_jenis_sayur = 0

    def create_sayuran(self, nama, teknik, jumlah, hari, harga, posisi='akhir', posisi_nomor=None):
        self.banyak_jenis_sayur += 1
        new_node = Node(self.banyak_jenis_sayur, nama, teknik, jumlah, hari, harga)
        
        if self.head is None or posisi == 'awal':
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        elif posisi == 'akhir':
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            while current is not None and current.nomor_sayuran != posisi_nomor:
                prev = current
                current = current.next
            if current is not None:
                new_node.next = current.next
                current.next = new_node
            else:
                print("Posisi nomor tidak ditemukan. Sayuran ditambah di akhir")
                self.tail.next = new_node
                self.tail = new_node
        
        print(f"Sayuran {nama} berhasil ditambahkan\n")

    def read_sayuran(self, nomor_sayuran):
        current = self.head
        while current is not None:
            if current.nomor_sayuran == nomor_sayuran:
                print(f"\nNama: {current.data['nama']}")
                print(f"Teknik: {current.data['teknik']}")
                print(f"Jumlah: {current.data['jumlah']}")
                print(f"Hari: {current.data['hari']}")
                print(f"Harga: {current.data['harga']}\n")
                return
            current = current.next
        print(f"Sayuran dengan nomor {nomor_sayuran} tidak ditemukan\n")
    
    def update_sayuran(self, nomor_sayuran, nama, teknik, jumlah, hari, harga):
        current = self.head
        while current is not None:
            if current.nomor_sayuran == nomor_sayuran:
                current.data = {
                    'nama': nama,
                    'teknik': teknik,
                    'jumlah': jumlah,
                    'hari': hari,
                    'harga': harga
                }
                print(f"Sayuran dengan nomor {nomor_sayuran} berhasil diperbarui\n")
                return
            current = current.next
        print(f"Sayuran dengan nomor {nomor_sayuran} tidak ditemukan\n")
    
    def delete_sayuran(self, posisi):
        if self.head is None:
            print("Tidak ada sayuran untuk dihapus\n")
            return

        if posisi == 'awal':
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        elif posisi == 'akhir':
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                current.next = None
                self.tail = current
        else:
            current = self.head
            prev = None
            while current is not None and current.nomor_sayuran != posisi:
                prev = current
                current = current.next
            if current is None:
                print(f"Sayuran dengan nomor {posisi} tidak ditemukan\n")
                return
            if prev is None:
                self.head = current.next
            else:
                prev.next = current.next
            if current.next is None:
                self.tail = prev

        print("Sayuran berhasil dihapus\n")

    def menu(self):
        while True:
            print("=== Menu Kebun Sayuran ===")
            print("1. Tambah Sayuran")
            print("2. Lihat Sayuran")
            print("3. Ubah Sayuran")
            print("4. Hapus Sayuran")
            print("5. Keluar")
            pilihan = input("Pilih aksi: ")

            if pilihan == '1':
                nama = input("Masukkan nama sayuran: ")
                teknik = input("Masukkan teknik penanaman: ")
                jumlah = int(input("Masukkan jumlah: "))
                hari = input("Masukkan lama tanam: ")
                harga = int(input("Masukkan harga: "))
                print("Pilih posisi penambahan: 1. Awal 2. Akhir 3. Di antara")
                posisi_pilihan = input("Masukkan pilihan (1/2/3): ")  
                if posisi_pilihan == '1':
                    posisi = 'awal'
                elif posisi_pilihan == '2':
                    posisi = 'akhir'
                elif posisi_pilihan == '3':
                    posisi = 'antara'
                    posisi_nomor = int(input("Masukkan nomor sayuran setelah posisi penambahan: "))
                self.create_sayuran(nama, teknik, jumlah, hari, harga, posisi, posisi_nomor)
                
            elif pilihan == '2':
                print()
                nomor_sayuran = int(input("Masukkan nomor sayuran yang ingin dilihat: "))
                self.read_sayuran(nomor_sayuran)
                
            elif pilihan == '3':
                print()
                nomor_sayuran = int(input("Masukkan nomor sayuran yang ingin diubah: "))
                nama = input("Masukkan nama sayuran: ")
                teknik = input("Masukkan teknik penanaman: ")
                jumlah = int(input("Masukkan jumlah: "))
                hari = input("Masukkan lama tanam: ")
                harga = int(input("Masukkan harga: "))
                self.update_sayuran(nomor_sayuran, nama, teknik, jumlah, hari, harga)
                
            elif pilihan == '4':
                print("Hapus sayuran di: 1. Awal 2. Akhir 3. Nomor spesifik")
                posisi = input("Pilih posisi: ")
                if posisi == '1':
                    posisi = 'awal'
                elif posisi == '2':
                    posisi = 'akhir'
                else:
                    posisi = int(posisi)
                self.delete_sayuran(posisi)
                
            elif pilihan == '5':
                print("Terima kasih telah menggunakan menu kebun sayuran")
                break
            else:
                print("Pilihan tidak tersedia, silakan coba lagi\n")

kebun = Kebun()
kebun.menu()
