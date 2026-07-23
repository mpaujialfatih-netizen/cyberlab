passwords = {}

while True:
    print("\n=== PASSWORD MANAGER ===")
    print("1. Tambah Password")
    print("2. Lihat Password")
    print("3. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        akun = input("Nama akun: ")
        password = input("Password: ")
        passwords[akun] = password
        print("Password disimpan.")

    elif pilih == "2":
        if passwords:
            for akun, password in passwords.items():
                print(f"{akun} : {password}")
        else:
            print("Belum ada password.")

    elif pilih == "3":
        print("Keluar...")
        break

    else:
        print("Pilihan tidak valid.")
