class CaesarCipher:
    def __init__(self, key=3):
        self.key = key

    def encrypt(self, plaintext_bytes: bytes) -> bytes:
        plaintext = plaintext_bytes.decode()
        encrypted = ""
        for char in plaintext:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                encrypted += chr((ord(char) + self.key - ascii_offset) % 26 + ascii_offset)
            else:
                encrypted += char
        return encrypted.encode()

    def decrypt(self, ciphertext_bytes: bytes) -> bytes:
        ciphertext = ciphertext_bytes.decode()
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted += chr((ord(char) - self.key - ascii_offset) % 26 + ascii_offset)
            else:
                decrypted += char
        return decrypted.encode()

class VignereCipher:
    def __init__(self, key="KOSEKIBIBOONINE"):
        self.key = key
        
    def extend_key(self, text: str) -> str:
        extended_key = ""
        key_pointer = 0
        
        for char in text:
            if char.isalpha():
                extended_key += self.key[key_pointer]
                key_pointer = (key_pointer + 1) % len(self.key)
            else:
                extended_key += char
        
        return extended_key

    def encrypt(self, plaintext_bytes: bytes) -> bytes:
        plaintext = plaintext_bytes.decode()
        extended_key = self.extend_key(plaintext)
        encrypted = ""
        index = 0
        
        while index < len(plaintext):
            char = plaintext[index]
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                encrypted += chr((ord(char) + ord(extended_key[index]) - ascii_offset) % 26 + ascii_offset)
            else:
                encrypted += char
            index += 1
        
        return encrypted.encode()

    def decrypt(self, ciphertext_bytes: bytes) -> bytes:
        ciphertext = ciphertext_bytes.decode()
        extended_key = self.extend_key(ciphertext)
        decrypted = ""
        index = 0
        
        while index < len(ciphertext):
            char = ciphertext[index]
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted += chr((ord(char) - ord(extended_key[index]) - ascii_offset) % 26 + ascii_offset)
            else:
                decrypted += char
            index += 1

        return decrypted.encode()


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

    def encrypt(self, plaintext_bytes: bytes) -> bytes:
        plaintext = plaintext_bytes.decode()
        encryptedtext = ""
        for char in plaintext:
            encryptedtext += self.subsdict.get(char, char)
            # print(self.subsdict.get(char, char))
            # print(encryptedtext)
        return encryptedtext.encode()

    def decrypt(self, ciphertext_bytes: bytes) -> bytes:
        ciphertext = ciphertext_bytes.decode()
        decryptedtext = ""
        for char in ciphertext:
            if char in self.subsdict.values():
                for key, value in self.subsdict.items():
                    if value == char:
                        # print(char)
                        decryptedtext += key
                        break
            else:
                decryptedtext += char
        return decryptedtext.encode()

if __name__ == "__main__":
    plaintext = input("Masukkan plain text: ")
    cipher = SubstitutionCipher()
    print("Plain Text: ", plaintext)

    ciphertext = cipher.encrypt(plaintext.encode())
    print("Encrypted Text: ", ciphertext)

    decryptedtext = cipher.decrypt(ciphertext)
    print("Decrypted Text: ", decryptedtext)
