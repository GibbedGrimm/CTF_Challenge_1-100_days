

class rotCracker:
    def __init__(self, alphabet="abcdefghijklmnopqrstuvwxyz"):
        self.alphabet = alphabet
        self.char_to_index = {char: i for i, char in enumerate(alphabet)}

    def decrypt(self, text, shift):

        result = []
        for char in text.lower():
            if char in self.char_to_index:
                new_index = (self.char_to_index[char] - shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                result.append(char)  # Сохраняем пробелы и другие символы
        return ''.join(result)

    def brute_force(self, ciphertext):

        results = []
        for shift in range(1, len(self.alphabet)):
            decrypted = self.decrypt(ciphertext, shift)
            results.append((shift, decrypted))
        return results


