# Image Encryption Project

## Description
This project encrypts image files using AES encryption to ensure secure transmission/storage. The image is unreadable without the correct key.

## Features
- AES 256-bit encryption using CBC mode
- Image padding and IV handling
- Simple CLI interface
- Easily extendable

## Requirements
- Python 3.x
- pycryptodome
- Pillow

## Usage

### Encrypt an image:
```bash
python image_encryptor.py
# Select Encrypt, enter image path
