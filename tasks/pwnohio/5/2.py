import string
from itertools import product

# Зашифрованный блок
encrypted_hex = '754477f367633676ef02347641d63d65529663b6007360f40f0ebe'
encrypted = bytes.fromhex(encrypted_hex)

# Допустимые символы в ASCII
readable = string.ascii_letters + string.digits + '_{}'

# Флаг должен начинаться с bctf{ и заканчиваться }
flag_start = b'bctf{'
flag_end = b'}'

# Максимальная длина флага (с учётом паддинга)
max_flag_len = 27

# Функция: допустимые байты для каждой позиции
def valid_bytes_for_cipher_byte(b):
    # Включаем читаемые символы и нулевой байт
    return [ord(c) for c in readable] + [0]

# Для каждого байта составляем список возможных значений
candidates = [valid_bytes_for_cipher_byte(b) for b in encrypted]

# Перебор всех подпоследовательностей длины max_flag_len
for start in range(len(encrypted) - max_flag_len + 1):
    sub_candidates = candidates[start:start + max_flag_len]

    # Product для генерации всех комбинаций
    for combo in product(*sub_candidates):
        s = bytes(combo)

        # Убираем нулевые байты в конце
        s_trimmed = s.rstrip(b'\x00')

        if s_trimmed.startswith(flag_start) and s_trimmed.endswith(flag_end):
            print(s_trimmed)
