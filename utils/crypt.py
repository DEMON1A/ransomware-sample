'''
This util is created to encrypt and decrypt files  
'''

import secrets
import string
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generate_random_secret_string(length=20):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?/`~"
    random_string = ''.join(secrets.choice(characters) for i in range(length))
    return random_string

def generate_key(passphrase: str) -> str:
    # Derive a key from the passphrase
    secret = generate_random_secret_string()
    salt = f'salt_{secret}'.encode('utf-8')  # Ensure this is kept secret, or generate a new salt for each encryption
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(passphrase.encode()))
    return key

def encrypt_file(filename, key):
    # Initialize Fernet
    fernet = Fernet(key)
    
    # Read the file to encrypt
    with open(filename, 'rb') as file:
        file_data = file.read()
    
    # Encrypt the data
    encrypted_data = fernet.encrypt(file_data)
    
    # Save the encrypted file
    with open(filename + '.rawrr', 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(encrypted_filename, key):
    # Initialize Fernet
    fernet = Fernet(key)
    
    # Read the encrypted data
    with open(encrypted_filename, 'rb') as file:
        encrypted_data = file.read()
    
    # Decrypt the data
    decrypted_data = fernet.decrypt(encrypted_data)
    
    # Save or return the decrypted data
    with open(encrypted_filename[:-6], 'wb') as file:
        file.write(decrypted_data)

# Usage
passphrase = generate_random_secret_string()
key = generate_key(passphrase)

# encrypt_file('sample\\1.txt', key)
# decrypt_file('path_to_your_file.txt.enc', key)
# decrypt_file('sample\\1.txt.rawrr', b'w6ItlCCsD7RlhZJA_5GJtGhDp25N51RpygkU6IXEZ8E=')