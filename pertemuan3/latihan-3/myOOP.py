#A. INHERITANCE (Pewarisan)
print()
class Produk :
    def __init__(self, nama_produk, harga):
        self.nama_produk = nama_produk
        self.harga = harga
    def info_produk(self):
      return f"{self.nama_produk} Seharga: {self.harga}"

class Elektronik(Produk):
    def __init__(self, nama_produk, harga, garansi):
        super().__init__(nama_produk, harga)
        self.garansi = garansi
    def info_produk(self):
            return f"{self.nama_produk} Seharga:  {self.harga} Bergaransi {self.garansi}"

class Makanan(Produk) :
    def __init__(self, nama_produk, harga, tanggal_kadaluarsa) :
        super().__init__(nama_produk, harga) 
        self.tanggal_kadaluarsa = tanggal_kadaluarsa
    def info_produk(self) :
        return f"{self.nama_produk} Seharga  {self.harga} Berkadaluarsa  {self.tanggal_kadaluarsa}"
    

#B.POLYMORPHISM
print()
class Notifikasi :
    def __init__(self, pesan) :
        self.pesan = pesan
    def kirim(self) :
      return f"Notifikasi: {self.pesan}"
class NotifikasiEmail(Notifikasi) :
    def kirim(self) :
        return f"Mengirim notifikasi melalui Email: {self.pesan}"
class NotifikasiSMS(Notifikasi) :
    def kirim(self) :
         return f"Mengirim notifikasi melalui SMS: {self.pesan}"



#C. ENCAPSUATION

print()
class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.__nilai = nilai

    def set_nilai(self, nilai):
        self.__nilai = nilai

    def get_nilai(self):
        if 0 <= self.__nilai <= 100:
            return f"{self.nama} mendapatkan nilai {self.__nilai}"
        else:
            return "Nilai tidak valid"



m1 = Mahasiswa("iput", 98)
m1.set_nilai(40)

print()