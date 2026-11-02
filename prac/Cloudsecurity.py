# TIME-LIMITED SECURE FILE ACCESS USING FLASK File name:
#secure_file.py

#Time-Limited Secure File Access

from flask import Flask, send_file, request, abort from datetime import
datetime, timedelta import secrets

app = Flask(name) TOKENS = {}

@app.route(“/generate_link”) def generate_link(): token =
secrets.token_urlsafe(16) expiry = datetime.now() +
timedelta(seconds=30) TOKENS[token] = expiry return f’’’ Temporary link
created. Valid for 30 seconds: Download Link ’’’

@app.route(“/download”) def download(): token =
request.args.get(“token”) if token in TOKENS: if datetime.now() <
TOKENS[token]: return send_file(“sample.txt”, as_attachment=True) else:
return “Link expired!” abort(403)

if name == “main”: app.run(debug=True)

#Install: py -m pip install flask

#Run: py secure_file.py

#Open: http://127.0.0.1:5000/generate_link

#CLIENT-SIDE ENCRYPTED BACKUP TO CLOUD (ZERO TRUST)
#File name:cloud_backup.py

#Client-Side Encrypted Backup to Cloud

from cryptography.fernet import Fernet import os import shutil

os.makedirs(“cloud_backup”, exist_ok=True)

key = Fernet.generate_key() cipher = Fernet(key)

with open(“aes.key”, “wb”) as f: f.write(key)

def encrypt_file(file_path): with open(file_path, “rb”) as f: data =
f.read()

    encrypted = cipher.encrypt(data)
    encrypted_file = "enc_" + os.path.basename(file_path)

    with open(encrypted_file, "wb") as f:
        f.write(encrypted)

    shutil.copy(encrypted_file, "cloud_backup/" + encrypted_file)
    print("Encrypted and uploaded:", encrypted_file)

if name == “main”: file = “sample_file.txt” if not os.path.exists(file):
with open(file, “w”) as f: f.write(“Confidential Cloud Backup File”)
encrypt_file(file)

#Install: py -m pip install cryptography

#Run: py cloud_backup.py

#INTRUSION DETECTION SYSTEM (IDS) FOR CLOUD ACCESS LOGS
#File name:ids.py

#Intrusion Detection System for Cloud Access Logs

import json from datetime import datetime

blacklisted_ips = [“192.168.1.10”, “10.0.0.5”]

with open(“access_logs.json”) as f: logs = json.load(f)

failed_attempts = {} print(“Detection Log Analysis:”)

for entry in logs: user = entry[“user”] ip = entry[“ip”] time =
datetime.strptime(entry[“timestamp”], “%Y-%m-%d %H:%M:%S”) status =
entry[“status”]

    if ip in blacklisted_ips:
        print("ALERT: Blacklisted IP:", ip, "User:", user)

    if not (8 <= time.hour <= 18):
        print("Off-hour login:", user, time.strftime("%H:%M"))

    if status == "failed":
        failed_attempts[user] = failed_attempts.get(user, 0) + 1
        if failed_attempts[user] >= 2:
            print("Multiple failed attempts by:", user)

print(“scan completed.”)

#Create another file: access_logs.json

[ { “user”: “Alice”, “ip”: “192.168.1.10”, “timestamp”: “2026-08-11
10:30:00”, “status”: “success” }, { “user”: “Bob”, “ip”: “10.0.0.5”,
“timestamp”: “2026-08-11 22:15:00”, “status”: “failed” }, { “user”:
“Bob”, “ip”: “192.168.1.20”, “timestamp”: “2026-08-11 23:00:00”,
“status”: “failed” }]

#Run: py ids.py

#INVISIBLE WATERMARKING FOR DATA LEAKAGE PREVENTION
#File name:watermark.py

#Invisible Watermarking for Data Leakage Prevention

import hashlib import os import shutil

os.makedirs(“cloud_upload”, exist_ok=True)

def watermark_text(file_path, user_id): with open(file_path, “r”) as f:
content = f.read()

    watermark = (
        "\n<!--USER-ID: "
        + hashlib.sha256(user_id.encode()).hexdigest()
        + "-->"
    )

    watermarked_file = "wm_" + os.path.basename(file_path)
    with open(watermarked_file, "w") as f:
        f.write(content + watermark)

    cloud_path = os.path.join("cloud_upload", watermarked_file)
    shutil.copy(watermarked_file, cloud_path)
    print("File watermarked and uploaded:", cloud_path)

if name == “main”: file = “sample_file.txt” if not os.path.exists(file):
with open(file, “w”) as f: f.write(“This is confidential content for
cloud storage.”) watermark_text(file, user_id=“user123”)

#REQUIRED FILES Program 1: secure_file.py and sample.txtZ
#Program 2:cloud_backup.py Program 3: ids.py and access_logs.json
#Program 4:watermark.py
