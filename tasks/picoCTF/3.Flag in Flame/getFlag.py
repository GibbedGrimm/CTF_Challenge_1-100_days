from scripts import base64decoder

with open("logs.txt") as f:
    b64 = f.read()


print(base64decoder.b64d(b64)[:16].hex())

with open("result.png","wb") as im:
    im.write(base64decoder.b64d(b64))

print(bytes.fromhex("7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F32346431363839357D"))