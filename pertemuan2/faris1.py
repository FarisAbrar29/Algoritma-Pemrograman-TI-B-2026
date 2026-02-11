def rata_rata(nilai):
    if len(nilai) == 0:
        return "Data kosong"
    
  
    total = sum(nilai)
    rata = total / len(nilai)
    return rata


nilai_mahasiswa = [80, 75, 90, 60, 85]
hasil_rata_rata = rata_rata(nilai_mahasiswa)


print(f"Nilai mahasiswa: {nilai_mahasiswa}")
print(f"Rata-rata nilai: {hasil_rata_rata}")
print()

nilai_kosong = []
hasil_kosong = rata_rata(nilai_kosong)
print(f"Nilai mahasiswa: {nilai_kosong}")
print(f"Rata-rata nilai: {hasil_kosong}")