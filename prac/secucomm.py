#Generate_keys.py – RSA Key Generation

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

sender_private = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

sender_public = sender_private.public_key()

with open("sender_private_key.pem", "wb") as f:
    f.write(
        sender_private.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

with open("sender_public_key.pem", "wb") as f:
    f.write(
        sender_public.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

receiver_private = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

receiver_public = receiver_private.public_key()

with open("receiver_private_key.pem", "wb") as f:
    f.write(
        receiver_private.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

with open("receiver_public_key.pem", "wb") as f:
    f.write(
        receiver_public.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

print("All RSA keys generated and saved successfully!")


#Sender.py – Message Encryption and Digital Signing

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

with open("receiver_public_key.pem", "rb") as f:
    receiver_public_key = serialization.load_pem_public_key(f.read())

with open("sender_private_key.pem", "rb") as f:
    sender_private_key = serialization.load_pem_private_key(
        f.read(), password=None
    )

user_input = input("Enter the message you want to encrypt and sign: ")

message = user_input.encode("utf-8")

encrypted_message = receiver_public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

signature = sender_private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

with open("encrypted_message.bin", "wb") as f:
    f.write(encrypted_message)

with open("signature.bin", "wb") as f:
    f.write(signature)

print("Message encrypted and signed successfully.")
print("Saved encrypted_message.bin and signature.bin")

#Receiver.py – Message Decryption and Signature Verification

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

with open("receiver_private_key.pem", "rb") as f:
    receiver_private_key = serialization.load_pem_private_key(
        f.read(), password=None
    )

with open("sender_public_key.pem", "rb") as f:
    sender_public_key = serialization.load_pem_public_key(f.read())

with open("encrypted_message.bin", "rb") as f:
    encrypted_message = f.read()

with open("signature.bin", "rb") as f:
    signature = f.read()

decrypted_bytes = receiver_private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

original_message = decrypted_bytes.decode("utf-8")

print("Decrypted Message:", original_message)

print("\n--- Signature Verification Options ---")

choice = input("Do you want to tamper with the message? (y/n): ").strip().lower()

if choice == "y":
    altered_text = input("Enter the new/altered message: ")
    message_to_verify = altered_text.encode("utf-8")
else:
    message_to_verify = decrypted_bytes

try:
    sender_public_key.verify(
        signature,
        message_to_verify,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("Signature Verified: Message is authentic and untampered!")

except InvalidSignature:
    print("SECURITY ALERT: Signature Verification Failed! The message was tampered with!")
