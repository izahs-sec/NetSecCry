import string
import random


chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)




def encrypt(plain_text):
    cipher_text = ""
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]
    return cipher_text

def decrypt(cipher_text):
    plain_text = ""
    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]
    return plain_text

# --- Menu ---
while True:
    print("\nChoose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        message = input("Enter message to encrypt: ")
        encrypted = encrypt(message)
        print(f"Encrypted message: {encrypted}")

    elif choice == "2":
        message = input("Enter message to decrypt: ")
        decrypted = decrypt(message)
        print(f"Decrypted message: {decrypted}")

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
