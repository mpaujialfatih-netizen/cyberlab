from auth import register, login

while True:
    print("\n=== LOGIN SYSTEM ===")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        register()

    elif pilih == "2":
        login()

    elif pilih == "3":
        break

    else:
        print("Pilihan tidak valid.")
