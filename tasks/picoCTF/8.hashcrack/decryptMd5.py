import hashlib

target = "482c811da5d5b4bc6d497ffa98491e38"

# читаем файл в бинарном режиме, чтобы не было ошибок декодирования
with open("rockyou.txt", "rb") as f:
    for i, line in enumerate(f, 1):
        pwd_bytes = line.rstrip(b"\r\n")
        if hashlib.md5(pwd_bytes).hexdigest() == target:
            try:
                print("Найден пароль (utf-8):", pwd_bytes.decode("utf-8"))
            except Exception:
                # если байты невалидны для utf-8 — покажем байтовое представление
                print("Найден пароль (raw bytes):", pwd_bytes)
            print("Строка в словаре — номер:", i)
            break
    else:
        print("Пароль не найден в файле.")
