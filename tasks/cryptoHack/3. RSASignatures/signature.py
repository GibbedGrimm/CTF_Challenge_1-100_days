import hashlib

with open("private_0a1880d1fffce9403686130a1f932b10.key") as key:
    N = int(key.readline()[4:])
    d = int(key.readline()[4:])

plaintext = "crypto{Immut4ble_m3ssag1ng}".encode()
h = hashlib.sha256(plaintext).digest()
i = int.from_bytes(h)

print(pow(i,d,N))
