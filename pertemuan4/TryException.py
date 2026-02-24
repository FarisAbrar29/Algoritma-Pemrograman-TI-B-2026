print("--- Kalkulator Pembagian Aman ---")

try:
    # Mengambil input dari user
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka pembagi: "))
    
    # Operasi pembagian
    hasil = angka1 / angka2   
    print(f"Hasilnya adalah: {hasil}")

except ValueError:
    
    print("Error: Tolong masukkan angka yang valid, jangan huruf")

except ZeroDivisionError:
    print("Error: Angka tidak bisa dibagi dengan nol")

except Exception as N:
    print(f"Terjadi kesalahan: {N}")

finally:
    print("Terima kasih telah menggunakan program ini.")
