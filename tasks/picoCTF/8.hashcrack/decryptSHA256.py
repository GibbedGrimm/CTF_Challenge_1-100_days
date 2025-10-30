import hashlib

target = "b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3"


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


