from database import load_data, save_data

while True:
    print("\n=== DATABASE MAHASISWA ===")
    print("1. Tambah Mahasiswa")
    print("2. Lihat Mahasiswa")
    print("3. Keluar")

    pilih = input("Pilih: ")

    data = load_data()

    if pilih == "1":
        nama = input("Nama : ")
        umur = input("Umur : ")
        jurusan = input("Jurusan : ")

        data.append({
            "nama": nama,
            "umur": umur,
            "jurusan": jurusan
        })

        save_data(data)
        print("Data berhasil disimpan.")

    elif pilih == "2":
        if not data:
            print("Belum ada data.")
        else:
            for i, mhs in enumerate(data, start=1):
                print(f"{i}. {mhs['nama']} | {mhs['umur']} | {mhs['jurusan']}")

    elif pilih == "3":
        break

    else:
        print("Pilihan tidak valid.")
