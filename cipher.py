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
