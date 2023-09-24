# Program of the Day: File Encryption and Decryption

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def decrypt(text, key):
    return encrypt(text, -key)

# Example usage
original_text = "Hello, World! 123"
encryption_key = 3

encrypted_text = encrypt(original_text, encryption_key)
decrypted_text = decrypt(encrypted_text, encryption_key)

print(f"Original Text: {original_text}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
