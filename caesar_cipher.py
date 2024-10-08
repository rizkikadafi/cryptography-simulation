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

if __name__ == "__main__":
    cipher = CaesarCipher()
    plaintext = "hello"
    encrypted = cipher.encrypt(plaintext.encode())
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    decrypted = cipher.decrypt(encrypted).decode()
    print(f"Decrypted: {decrypted}")
