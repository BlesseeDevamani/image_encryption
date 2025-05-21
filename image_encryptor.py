from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
import os

def pad(data):
    padding_len = 16 - (len(data) % 16)
    return data + bytes([padding_len]) * padding_len

def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]

def encrypt_image(image_path, key):
    try:
        with open(image_path, 'rb') as f:
            data = f.read()

        data = pad(data)
        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted = iv + cipher.encrypt(data)

        encrypted_path = image_path + ".enc"
        with open(encrypted_path, 'wb') as f:
            f.write(encrypted)

        print(f"\n[+] Encrypted image saved to: {encrypted_path}")

    except Exception as e:
        print(f"[!] Error during encryption: {e}")

def decrypt_image(encrypted_path, key, output_path):
    try:
        with open(encrypted_path, 'rb') as f:
            encrypted = f.read()

        iv = encrypted[:16]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(encrypted[16:])
        decrypted = unpad(decrypted)

        with open(output_path, 'wb') as f:
            f.write(decrypted)

        print(f"\n[+] Decrypted image saved to: {output_path}")

    except Exception as e:
        print(f"[!] Error during decryption: {e}")

def main():
    print("=== Image Encryptor ===")
    choice = input("Encrypt (E) or Decrypt (D)? ").strip().lower()

    # 32-byte (256-bit) encryption key
    key = b'This_is_a_32_byte_secret_key_for_AES!'

    if choice == 'e':
        image_path = input("Enter full path to image to encrypt: ").strip()
        if not os.path.isfile(image_path):
            print("[!] File does not exist.")
            return
        encrypt_image(image_path, key)

    elif choice == 'd':
        encrypted_path = input("Enter path to encrypted image (.enc): ").strip()
        output_path = input("Enter output path for decrypted image (e.g., image.jpg): ").strip()
        decrypt_image(encrypted_path, key, output_path)

    else:
        print("[!] Invalid option. Use 'E' for encrypt or 'D' for decrypt.")

if __name__ == "_main_":
    main()