from .ui import initialise_cipher
from .utilities import get_input, encrypt_and_display_info, decrypt_and_display_info
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)
key = key.decode('utf-8')

def main():
    initialise_cipher(key)
    encryptOrDecrypt = get_input('Do you wanna encrypt or decrypt text(encrypt, decrypt): ', ['encrypt', 'decrypt'])
    if encryptOrDecrypt.lower() == "encrypt":
        text = get_input('Enter the text to encrypt: ').encode()
        encrypt_and_display_info(fernet, key, text)
        
    elif encryptOrDecrypt.lower() == "decrypt":
        text = get_input('Enter the text to decrypt: ').encode()
        decrypt_and_display_info(text)
