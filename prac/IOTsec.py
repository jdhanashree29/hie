#  AES ENCRYPTION FOR IoT SENSOR DATA File name: aes_sensor.py

#AES Encryption for IoT Sensor Data

from Crypto.Cipher import AES
import base64

key = b"ThisIsA16ByteKey"
cipher = AES.new(key, AES.MODE_EAX)

sensor_data = "Temperature: 28C"

ciphertext, tag = cipher.encrypt_and_digest(sensor_data.encode())
nonce = cipher.nonce

print("Encrypted Data:", base64.b64encode(ciphertext).decode())

cipher_dec = AES.new(key, AES.MODE_EAX, nonce=nonce)
decrypted_data = cipher_dec.decrypt(ciphertext).decode()

print("Decrypted Data:", decrypted_data)

#Install: py -m pip install pycryptodome

#Run: py aes_sensor.py

##2HMAC FOR DATA INTEGRITY File name: hmac_integrity.py

#HMAC for Data Integrity

import hmac
import hashlib

secret_key = b"iot_secret_key"

message = b"Humidity: 70%"

hmac_digest = hmac.new(
    secret_key, message, hashlib.sha256
).hexdigest()

print("Message:", message.decode())
print("Generated HMAC:", hmac_digest)

received_hmac = hmac.new(
    secret_key, message, hashlib.sha256
).hexdigest()

if hmac.compare_digest(hmac_digest, received_hmac):
    print("Message is authentic")
else:
    print("Message tampered!")

#Run: py hmac_integrity.py

##3.  MQTT COMMUNICATION WITH TLS SECURITY File name: mqtt_tls.py

##MQTT Communication with TLS Security

import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected with result code", reason_code)
    client.subscribe("iot/device1")

def on_message(client, userdata, msg):
    print("Received:", msg.topic, msg.payload.decode())

client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_start()
time.sleep(2)

client.publish("iot/device1", "Temperature Data: 25C")
print("Message published successfully")

time.sleep(2)
client.loop_stop()
client.disconnect()

#Install: py -m pip install scapy

#Run terminal as Administrator, then: py packet_sniff.py


#py -m pip install pycryptodome paho-mqtt scapy

##4. PACKET SNIFFING IN IoT TRAFFIC
#File name: packet_sniff.py

from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):
        src = packet["IP"].src
        dst = packet["IP"].dst

        print("[IP Packet]", src, "->", dst)

        if packet.haslayer("Raw"):
            payload = packet["Raw"].load
            print("Payload:", payload)

print("Sniffing IoT traffic... Press Ctrl+C to stop")

sniff(prn=packet_callback, count=10)

#py -m pip install scapy
#py packet_sniff.py
