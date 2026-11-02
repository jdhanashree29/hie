#SQL Injection Prevention

import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
cur.execute("INSERT INTO users VALUES (?, ?)", ("admin", "admin_password"))
conn.commit()

u = input("Enter username: ")
p = input("Enter password: ")

cur.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p))

if cur.fetchone():
    print("Login successful!")
else:
    print("Invalid credentials!")

conn.close()

#Password Hashing using bcrypt

import sqlite3
import bcrypt

conn = sqlite3.connect("secure_users.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password BLOB)")

u = input("Enter username: ")
p = input("Enter password: ")

hashed = bcrypt.hashpw(p.encode(), bcrypt.gensalt())
cur.execute("INSERT INTO users VALUES (?, ?)", (u, hashed))
conn.commit()

u = input("Username to login: ")
p = input("Password to login: ")

cur.execute("SELECT password FROM users WHERE username=?", (u,))
data = cur.fetchone()

if data and bcrypt.checkpw(p.encode(), data[0]):
    print("Login successful!")
else:
    print("Login failed!")

conn.close()
#py -m pip install bcrypt

#Role-Based Access Control (RBAC)

import sqlite3

conn = sqlite3.connect("rbac.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, role TEXT)")

cur.execute("INSERT INTO users VALUES (?, ?, ?)", ("admin", "admin_pwd", "admin"))
cur.execute("INSERT INTO users VALUES (?, ?, ?)", ("john", "john_pwd", "student"))
conn.commit()

u = input("Enter username: ")
p = input("Enter password: ")

cur.execute("SELECT role FROM users WHERE username=? AND password=?", (u, p))
user = cur.fetchone()

if user:
    role = user[0]
    print("Login successful! Role:", role)

    if role == "admin":
        print("Access granted: View, Add, Delete and Modify")
    elif role == "student":
        print("Access granted: View records only")
else:
    print("Invalid credentials!")

conn.close()


#Field Encryption using Fernet

from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

data = "Confidential Information"

encrypted = cipher.encrypt(data.encode())
print("Encrypted data:", encrypted)

decrypted = cipher.decrypt(encrypted).decode()
print("Decrypted data:", decrypted)



