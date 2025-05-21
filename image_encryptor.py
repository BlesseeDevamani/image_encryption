from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
import os

def pad(data):
    padding_required = AES.block_size - (len(data) % AES.block_size)
    return data + bytes([padding_required]) * padding_required

def unpad(data):
    return data[:-data[-1]]

def encrypt_image(image_path, key):
    with open(image_path, "rb") as f:
        image_data = f.read()

    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(image_data)
    encrypted_data = cipher.encrypt(padded_data)

    encrypted_path = image_path + ".enc"
    with open(encrypted_path, "wb") as f:
        f.write(iv + encrypted_data)

    print(f"Encrypted image saved to {encrypted_path}")

def decrypt_image(encrypted_path, key, output_path):
    with open(encrypted_path, "rb") as f:
        iv = f.read(16)
        encrypted_data = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(encrypted_data)
    decrypted_data = unpad(decrypted_padded)

    with open(output_path, "wb") as f:
        f.write(decrypted_data)

    print(f"Decrypted image saved to {output_path}")

if __name__ == "_main_":
    import base64

    # Use a 16, 24 or 32 byte key (e.g., 32 bytes = 256-bit AES)
    key = b"This_is_a_32_byte_key_for_AES!!"

    choice = input("Encrypt (E) or Decrypt (D)? ").lower()
    if choice == "e":
        path = input("Enter path to image to encrypt: ")
        encrypt_image(path, key)
    elif choice == "d":
        path = input("Enter path to encrypted image: ")
        output = input("Enter output path (e.g., image.jpg): ")
        decrypt_image(path, key, output)
    else:
        print("Invalid option.")