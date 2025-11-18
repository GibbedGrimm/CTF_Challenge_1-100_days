from Crypto.Cipher import AES

cipher = AES.new(b'amateursCTF{@3s}', AES.MODE_ECB)
pt = b'\x00' * 16
print(cipher.encrypt(pt).hex())

"""
5aed095b21675ec4ceb770994289f72b
"""