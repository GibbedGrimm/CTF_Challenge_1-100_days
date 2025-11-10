def generate_keystream(i):
    return (i * 3404970675 + 3553295105) % (2 ** 32)


with open('img2.png', 'rb') as f:
    etalon = f.read()[:8]  # 89 50 4E 47 0D 0A 1A 0A


with open("secretpng.txt") as f:
    ct = bytes.fromhex(f.read().strip())


origkey = int.from_bytes(bytes([ct[i] ^ etalon[i] for i in range(4)]), 'big')
print(f"Recovered keystream = {origkey} (0x{origkey:08x})")


keystream = origkey
b = bytearray(ct)
for i in range(0, len(b), 4):
    key = keystream.to_bytes(4, "big")
    for j in range(4):
        if i + j < len(b):
            b[i + j] ^= key[j]
    keystream = generate_keystream(keystream)

with open("result.png", "wb") as f:
    f.write(b)

print("[+] result.png decrypted successfully!")
