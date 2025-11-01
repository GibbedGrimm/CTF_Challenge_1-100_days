
from scripts import base64decoder,rotBrutForce
brut = rotBrutForce.rotCracker()
with open("enc_flag.txt") as f:
    b64 = f.read()


b64Second = base64decoder.b64d(b64).decode("utf-8")[2:-2]
pt = base64decoder.b64d(b64Second).decode("utf-8")
rots = brut.brute_force(pt)
print(rots)