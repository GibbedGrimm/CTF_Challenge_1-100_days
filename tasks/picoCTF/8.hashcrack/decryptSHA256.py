import hashlib

target = "916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745"


with open("rockyou.txt","rb") as f:
    for i,passhash in enumerate(f,1):
        pwd_bytes = passhash.rstrip(b"\r\n")
        if hashlib.sha256(pwd_bytes).hexdigest() == target:
            try:
                print("Найден пароль (utf-8):", pwd_bytes.decode("utf-8"))
            except Exception:
                # если байты невалидны для utf-8 — покажем байтовое представление
                print("Найден пароль (raw bytes):", pwd_bytes)
            print("Строка в словаре — номер:", i)
            break
        else:
            print("Пароль не найден в файле.")


#916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745