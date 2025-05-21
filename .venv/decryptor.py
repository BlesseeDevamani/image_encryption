from Crypto.Cipher import AES

def unpad(data):
    return data.rstrip(b"\0")

def decrypt_image(encrypted_path='encrypted_image.enc', key_path='key.txt', output_path='decrypted_image.png'):
    # Load key and iv
    with open(key_path, 'rb') as f:
        key_iv = f.read()
        key = key_iv[:16]
        iv = key_iv[16:]

    # Load encrypted image
    with open(encrypted_path, 'rb') as f:
        encrypted_data = f.read()

    # Decrypt
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data))

    # Write image
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)

    print("[+] Image decrypted and saved as 'decrypted_image.png'")

decrypt_image()
