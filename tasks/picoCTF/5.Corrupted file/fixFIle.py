
f = open('file', 'rb').read()
recovered = "ffd8ff"+f.hex()[6:]
print(recovered[:16])
print(bytes.hex(f[:8]))
with open('img.jpeg','wb') as img:
    img.write(bytes.fromhex(recovered))

