from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size
    encrypted_image = Image.new(image.mode, (width, height))

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            encrypted_image.putpixel((x, y), encrypted_pixel)

    encrypted_image.save("encrypted_image.png")
    print("Image encrypted successfully.")

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size
    decrypted_image = Image.new(image.mode, (width, height))

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            decrypted_pixel = tuple((p - key) % 256 for p in pixel)
            decrypted_image.putpixel((x, y), decrypted_pixel)

    decrypted_image.save("decrypted_image.png")
    print("Image decrypted successfully.")

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt an image? (encrypt/decrypt): ").lower()
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
            continue

        image_path = input("Enter the path of the image file: ")
        key = int(input("Enter the encryption/decryption key (an integer): "))

        if choice == 'encrypt':
            encrypt_image(image_path, key)
        else:
            decrypt_image(image_path, key)

        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
