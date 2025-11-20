from Crypto.Cipher import AES


known = b'amateursCTF{'
known2 = b'}'
for i in range(256):
    for j in range(256):
        for k in range(256):
            key = known + int.to_bytes(i) + int.to_bytes(j) + int.to_bytes(k)+known2

            cipher = AES.new(key, AES.MODE_ECB)
            pt = b'\x00' * 16
            if cipher.encrypt(pt).hex() == '5aed095b21675ec4ceb770994289f72b':
                print(key)
                break