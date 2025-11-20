hexed = '48495E4C516E1B4E75531A5F757F5919756B447519475F461E5E1A58756558754E19491A475A1B466F585724'
key = 0x2A

# Разбиваем на байты (по 2 символа)
bytes_list = [hexed[i:i+2] for i in range(0, len(hexed), 2)]

# Декодируем каждый байт XOR с 0x2A
decoded_bytes = []
for byte_hex in bytes_list:
    byte_val = int(byte_hex, 16)
    if byte_val == 0x24:  # Если встретили '$' - останавливаемся
        break
    decoded_bytes.append(byte_val ^ key)

# Преобразуем в строку
flag = ''.join(chr(b) for b in decoded_bytes)
print(flag)