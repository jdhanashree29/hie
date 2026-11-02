## 1. User Registration and Login using SQLite + Hashlib

#File name: `user_auth.py`

import sqlite3
import hashlib
import secrets

def init_db():
    conn = sqlite3.connect("users.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            salt TEXT,
            password_hash TEXT
        )
    """)
    conn.commit()
    conn.close()

def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)

    hashed = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), salt.encode(), 100000
    )
    return salt, hashed.hex()

def register_user(username, password):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=?", (username,))

    if cur.fetchone():
        conn.close()
        return "Username already exists!"

    salt, password_hash = hash_password(password)

    cur.execute("INSERT INTO users VALUES (?, ?, ?)",
                (username, salt, password_hash))

    conn.commit()
    conn.close()
    return "User registered successfully!"

def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("SELECT salt, password_hash FROM users WHERE username=?",
                (username,))

    result = cur.fetchone()
    conn.close()

    if not result:
        return False

    salt, stored_hash = result
    _, entered_hash = hash_password(password, salt)

    return entered_hash == stored_hash

# Main
init_db()
print(register_user("alice", "secret_password"))
print(authenticate_user("alice", "secret_password"))
```

## 2. Timestamp-Based Replay Attack Detection

#File name: `server.py`

import socket
import time
from datetime import datetime
from user_auth import authenticate_user, init_db

init_db()

s = socket.socket()
s.bind(("localhost", 9999))
s.listen(1)

print("Server waiting...")
conn, addr = s.accept()

username = conn.recv(1024).decode()
password = conn.recv(1024).decode()

if not authenticate_user(username, password):
    conn.sendall(b"Login Failed")
    conn.close()
    s.close()
    exit()

conn.sendall(b"Login Successful")

last_timestamp = None

for i in range(2):
    message = conn.recv(1024).decode()

    try:
        timestamp, data = message.split("|", 1)
        current = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        now = datetime.now()

        if abs((now - current).total_seconds()) > 30:
            print("Old message rejected!")
        elif last_timestamp == timestamp:
            print("Replay Attack Detected!")
        else:
            print("Message Accepted:", data)
            last_timestamp = timestamp

    except:
        print("Invalid message!")

conn.close()
s.close()

#File name: `client.py`

import socket
import time
from datetime import datetime

s = socket.socket()
s.connect(("localhost", 9999))

username = input("Username: ")
password = input("Password: ")

s.sendall(username.encode())
time.sleep(0.2)
s.sendall(password.encode())

print(s.recv(1024).decode())

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
message = timestamp + "|Hello Server"

s.sendall(message.encode())
time.sleep(1)

# Sending same message again to simulate replay attack
s.sendall(message.encode())

s.close()

## 3. Encrypted File Transfer using AES-GCM

#File name: `file_server.py`

import socket
import struct
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from user_auth import authenticate_user

key = bytes.fromhex("054f0c5c692ffa3e0d0fa7d156966812")

def receive(conn, size):
    data = b""
    while len(data) < size:
        part = conn.recv(size - len(data))
        if not part:
            raise ConnectionError("Connection closed")
        data += part
    return data

s = socket.socket()
s.bind(("localhost", 8888))
s.listen(1)

print("Waiting for client...")
conn, addr = s.accept()

username = conn.recv(1024).decode()
password = conn.recv(1024).decode()

if not authenticate_user(username, password):
    conn.sendall(b"0")
    conn.close()
    s.close()
    exit()

conn.sendall(b"1")
print("Login successful!")

nonce = receive(conn, 12)

name_length = struct.unpack("!I", receive(conn, 4))[0]
filename = receive(conn, name_length).decode()

data_length = struct.unpack("!Q", receive(conn, 8))[0]
encrypted_data = receive(conn, data_length)

aes = AESGCM(key)
data = aes.decrypt(nonce, encrypted_data, None)

with open("received_" + filename, "wb") as f:
    f.write(data)

print("File received and decrypted successfully!")

conn.close()
s.close()

#File name: `file_client.py`

import socket
import os
import struct
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = bytes.fromhex("054f0c5c692ffa3e0d0fa7d156966812")

s = socket.socket()
s.connect(("localhost", 8888))

username = input("Username: ")
password = input("Password: ")

s.sendall(username.encode())
import time
time.sleep(0.2)
s.sendall(password.encode())

if s.recv(1024) != b"1":
    print("Login failed!")
    s.close()
    exit()

filename = "sample.txt"

with open(filename, "rb") as f:
    data = f.read()

aes = AESGCM(key)
nonce = os.urandom(12)
encrypted_data = aes.encrypt(nonce, data, None)

s.sendall(nonce)
s.sendall(struct.pack("!I", len(filename)))
s.sendall(filename.encode())
s.sendall(struct.pack("!Q", len(encrypted_data)))
s.sendall(encrypted_data)

print("Encrypted file sent successfully!")

s.close()

## 4. RSA Key Generation

#File name: `key_generation.py`

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

with open("client_private.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("client_public.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("RSA keys generated successfully!")

## 5. RSA Public-Key Authentication

#File name: `rsa_server.py`

import socket
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

with open("client_public.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

s = socket.socket()
s.bind(("localhost", 7777))
s.listen(1)

print("Waiting for client...")
conn, addr = s.accept()

import secrets
challenge = secrets.token_bytes(32)

conn.sendall(challenge)

signature = conn.recv(1024)

try:
    public_key.verify(
        signature,
        challenge,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print("Authentication Successful!")
except:
    print("Authentication Failed!")

conn.close()
s.close()

#File name: `rsa_client.py`

import socket
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

with open("client_private.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(), password=None
    )

s = socket.socket()
s.connect(("localhost", 7777))

challenge = s.recv(1024)

signature = private_key.sign(
    challenge,
    padding.PKCS1v15(),
    hashes.SHA256()
)

s.sendall(signature)

print("Challenge signed and sent!")

s.close()

##py -m pip install cryptography
