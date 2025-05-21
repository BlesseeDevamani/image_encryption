from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
import os

def pad(data):
    return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

def encrypt_image(image_path, key_path='key.txt'):
    # Read image
    with open(image_path, 'rb') as f:
        data = f.read()

    # Pad data
    padded_data = pad(data)

    # Generate key and iv
    key = get_random_bytes(16)
    iv = get_random_bytes(16)

    # Save key
    with open(key_path, 'wb') as f:
        f.write(key + iv)

    # Encrypt
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(padded_data)

    # Save encrypted image
    with open('encrypted_image.enc', 'wb') as f:
        f.write(encrypted_data)

    print("[+] Image encrypted and saved as 'encrypted_image.enc'")
    print("[+] Key saved in 'key.txt'")

encrypt_image('sample.png')