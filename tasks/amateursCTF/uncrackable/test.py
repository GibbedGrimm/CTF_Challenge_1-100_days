import hashlib


def xor(a, b):
    return bytes(i ^ j for i, j in zip(a, b))


def main():
    with open("out.txt", "r") as f:
        data = f.read().strip()

    flag_len = 47
    flag_hex_len = flag_len * 2
    total_hex_len = len(data)
    random_hex_len = total_hex_len - flag_hex_len
    R = random_hex_len // 2  # Number of bytes in random part

    random_ciphertext = bytes.fromhex(data[:random_hex_len])
    flag_ciphertext = bytes.fromhex(data[random_hex_len:])

    # Define set of non-space bytes
    S = set(range(256)) - {9, 10, 11, 12, 13, 32}

    # Initialize sets for each s_j
    sets = [set(range(256)) for _ in range(32)]

    # Process each byte in random_ciphertext
    for i, c in enumerate(random_ciphertext):
        j = i % 32
        k = i // 32
        allowed_y = {c ^ s for s in S}
        allowed_s = {(y - k) % 256 for y in allowed_y}
        sets[j] &= allowed_s
        if len(sets[j]) == 0:
            print(f"Error: no possible values for s_{j} at i={i}")
            return

    # Reconstruct state0
    state0 = [next(iter(s)) for s in sets]

    # Decrypt flag
    flag_bytes = bytearray()
    for i in range(R, R + flag_len):
        j = i % 32
        k = i // 32
        y_i = (state0[j] + k) % 256
        flag_byte = flag_ciphertext[i - R] ^ y_i
        flag_bytes.append(flag_byte)

    print("Decrypted flag:", flag_bytes.decode())


if __name__ == "__main__":
    main()