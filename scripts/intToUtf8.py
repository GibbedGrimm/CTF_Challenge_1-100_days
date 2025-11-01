def itu(number):
    return number.to_bytes((number.bit_length()+7)//8).decode("utf-8")