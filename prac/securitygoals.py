#Confidentiality – Using Encryption (AES)

from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = "Top Secret message!"

encrypted = cipher.encrypt(message.encode())
decrypted = cipher.decrypt(encrypted).decode()

print("Key:", key.decode())
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

#Integrity – Using Hashing (SHA-256)

import hashlib

data = "This is important"

hash1 = hashlib.sha256(data.encode()).hexdigest()

tampered = "this is important"

hash2 = hashlib.sha256(tampered.encode()).hexdigest()

print("Hash1:", hash1)
print("Hash2:", hash2)
print("Integrity verified?", hash1 == hash2)

#Availability – Simple Backup Script

import shutil

original_file = r"C:\Users\student\Downloads\data.txt"
backup_file = r"C:\Users\student\Downloads\backup_data.txt"

shutil.copyfile(original_file, backup_file)

print("Backup completed!")

#Authentication – Username and Password Check

users = {
    "admin": "password123",
    "user1": "hello123"
}

username = input("Enter username: ")
password = input("Enter password: ")

if users.get(username) == password:
    print("Access granted")
else:
    print("Access denied")

#Non-Repudiation – Digital Signature Simulation

import hashlib

message = "Approve $5000 transfer"

signature = hashlib.sha256(message.encode()).hexdigest()

received_message = "Approve $5000 transfer"

received_signature = hashlib.sha256(
    received_message.encode()
).hexdigest()

print("Signature verified:", signature == received_signature)

#Accountability – Logging User Actions

import datetime

def log_action(user, action):
    with open("audit_log.txt", "a") as log:
        timestamp = datetime.datetime.now()
        log.write(f"{timestamp} - {user}: {action}\n")

log_action("admin", "Logged in")
log_action("user1", "Viewed report")

print("Actions logged successfully!")
