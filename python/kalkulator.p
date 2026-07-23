print("=== KALKULATOR SEDERHANA ===")

a = float(input("Angka pertama : "))
b = float(input("Angka kedua   : "))

print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

pilihan = input("Pilih (1-4): ")

if pilihan == "1":
    print("Hasil =", a + b)
elif pilihan == "2":
    print("Hasil =", a - b)
elif pilihan == "3":
    print("Hasil =", a * b)
elif pilihan == "4":
    if b != 0:
        print("Hasil =", a / b)
    else:
        print("Tidak bisa membagi dengan nol!")
else:
    print("Pilihan tidak valid.")
