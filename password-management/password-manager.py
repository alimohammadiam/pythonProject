import sqlite3
import getpass
import secrets
import string
from cryptography.fernet import Fernet

encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

conn = sqlite3.connect('password_manager.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS passwords(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
    )
''')

conn.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
    )
''')

conn.commit()


def login():
    global username
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    stored_password = user[2]

    if user:
        decrypted_password = cipher_suite.decrypt(stored_password.encode()).decode()
        if password == decrypted_password:
            print('Login Successful')
            return True
    print("Login failed. Please try again.")
    return False


def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    strong_password = ''.join(secrets.choice(characters) for _ in range(length))
    return strong_password


def change_password():
    if not login():
        return
    new_password = getpass.getpass('Enter new password (or leave blank to generate strong password): ')
    if not new_password:
        new_password = generate_strong_password()
        print(f'your password is ({new_password})')
    encrypted_password = cipher_suite.encrypt(new_password.encode()).decode()
    cursor.execute("UPDATE users SET password=? WHERE username=?", (encrypted_password, username))
    conn.commit()
    print('your new password changed successfully.')


def register_user():
    username = input('Enter your username: ')
    password = getpass.getpass('Enter your password:')
    password_2 = getpass.getpass('Enter password again: ')
    if password_2 == password:
        encrypted_password = cipher_suite.encrypt(password.encode()).decode()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, encrypted_password))
        conn.commit()
        print('\n\tUser registration successful!')
    else:
        print('\n\tpassword is wrong!')


while True:
    print('\nPassword Manager')
    print('\t1. Register')
    print('\t2. Change Password')
    print('\t3. Add Password')
    print('\t4. View Password')
    print('\t5. Delete Password')
    print('\t6. Exit')

    choice = input('Select an option: ')
    if choice == '1':
        register_user()
