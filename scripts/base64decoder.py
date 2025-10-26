import base64



def b64d(word):
    return base64.b64decode(word.encode())

