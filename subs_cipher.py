class SubstitutionCipher:
    def __init__(self):
        self.subsdict = {
            'a': 'g', 'b': 'e', 'c': 'x', 'd': 'n', 'e': 'z',
            'f': 'y', 'g': 'h', 'h': 't', 'i': 'w', 'j': 'q',
            'k': 'o', 'l': 'r', 'm': 'j', 'n': 'f', 'o': 'd',
            'p': 'u', 'q': 'c', 'r': 'a', 's': 'p', 't': 'k',
            'u': 's', 'v': 'l', 'w': 'v', 'x': 'i', 'y': 'b', 'z': 'm',
            'A': 'G', 'B': 'E', 'C': 'X', 'D': 'N', 'E': 'Z',
            'F': 'Y', 'G': 'H', 'H': 'T', 'I': 'W', 'J': 'Q',
            'K': 'O', 'L': 'R', 'M': 'J', 'N': 'F', 'O': 'D',
            'P': 'U', 'Q': 'C', 'R': 'A', 'S': 'P', 'T': 'K',
            'U': 'S', 'V': 'L', 'W': 'V', 'X': 'I', 'Y': 'B', 'Z': 'M'
        }

    def encrypt(self, text):
        encryptedtext = ""
        for char in text:
            encryptedtext += self.subsdict.get(char, char)
            # print(self.subsdict.get(char, char))
            # print(encryptedtext)
        return encryptedtext

    def decrypt(self, text):
        decryptedtext = ""
        for char in text:
            if char in self.subsdict.values():
                for key, value in self.subsdict.items():
                    if value == char:
                        # print(char)
                        decryptedtext += key
                        break
            else:
                decryptedtext += char
        return decryptedtext

if __name__ == "__main__":
    plaintext = input("Masukkan plain text: ")
    cipher = SubstitutionCipher()
    print("Plain Text: ", plaintext)

    ciphertext = cipher.encrypt(plaintext)
    print("Encrypted Text: ", ciphertext)

    decryptedtext = cipher.decrypt(ciphertext)
    print("Decrypted Text: ", decryptedtext)