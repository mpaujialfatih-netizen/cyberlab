import json

FILE = "users.json"

def load_users():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f, indent=4)

def register():
    users = load_users()

    username = input("Username: ")

    if username in users:
        print("Username sudah ada.")
        return

    password = input("Password: ")

    users[username] = password
    save_users(users)

    print("Registrasi berhasil.")

def login():
    users = load_users()

    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print("Login berhasil.")
    else:
        print("Username atau password salah.")
