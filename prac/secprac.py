#------Practical 8 – Security Practices

#----a. Demonstrating a Hash Collision

# toy_collision_demo.py


def toy_hash(b):
    return sum(b) % 256


def make_base_certs():
    cert1_txt = """-----BEGIN CERTIFICATE-----
Subject: CN=Alice Example
Issuer: Test CA
PublicKey: AAAAB3NzaC1yc2EAAAADAQABAAABAQCu
-----END CERTIFICATE-----
"""

    cert2_txt = """-----BEGIN CERTIFICATE-----
Subject: CN=Bob Example
Issuer: Test CA
PublicKey: AAAAB3NzaC1yc2EAAAADAQABAAABAQCu
-----END CERTIFICATE-----
"""

    return cert1_txt.encode(), cert2_txt.encode()


def pad_to_match(hash_target, current_bytes):
    cur = sum(current_bytes) % 256
    needed = (hash_target - cur) % 256

    if needed == 0:
        return b''

    return bytes([needed])


def main():
    cert1, cert2 = make_base_certs()

    h1 = toy_hash(cert1)
    h2 = toy_hash(cert2)

    print("Initial toy hashes:")
    print("cert1 hash:", h1)
    print("cert2 hash:", h2)

    padding = pad_to_match(h1, cert2)
    cert2_padded = cert2 + b"\n#PAD:" + padding

    h2_after = toy_hash(cert2_padded)

    print("\nAfter padding cert2:")
    print("cert1 length:", len(cert1), "hash:", toy_hash(cert1))
    print("cert2_padded length:", len(cert2_padded), "hash:", h2_after)

    print("\nAre bytes identical?:", cert1 == cert2_padded)

    print("Do they collide under toy_hash?:",
          toy_hash(cert1) == toy_hash(cert2_padded))

    def show_tail(b):
        return b[-40:].hex()

    print("tail(cert1) (hex):", show_tail(cert1))
    print("tail(cert2_p) (hex):", show_tail(cert2_padded))

    with open("cert1_demo.pem", "wb") as f:
        f.write(cert1)

    with open("cert2_demo_padded.pem", "wb") as f:
        f.write(cert2_padded)

    print("\nWrote cert1_demo.pem and cert2_demo_padded.pem to disk.")


if __name__ == "__main__":
    main()

#py toy_collision_demo.py
    
#b. Computing Hash, MAC and HMAC

#hash

import hashlib

message = "Hello Security Students".encode()

hash_digest = hashlib.sha256(message).hexdigest()

print("Message:", message.decode())
print("SHA256 Hash:", hash_digest)

#hmac mac

import hmac, hashlib
 
key = b'super_secret_key'
msg = b'Authenticate this message'
 
hmac_digest = hmac.new(key, msg, hashlib.sha256).hexdigest()
print("HMAC:", hmac_digest)
