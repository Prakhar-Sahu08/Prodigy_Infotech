def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
            continue
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (a positive integer): "))
        if choice == 'encrypt':
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        else:
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        
        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
