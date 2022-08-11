import os
from .ui import initialise_fernet
from .utilities import validate_input, write_pk, load_pk
from cryptography.exceptions import InvalidSignature
from cryptography.fernet import Fernet

private_key = Fernet.generate_key()
fernet = Fernet(private_key)
private_key = private_key.decode('utf-8')

def main():
    initialise_fernet(private_key)
    encryptOrDecrypt = validate_input('Do you wanna encrypt or decrypt text(encrypt, decrypt): ', ['encrypt', 'decrypt'])
    if encryptOrDecrypt.lower() == "encrypt":
        text = input('Enter the text to encrypt: ').encode()
        encrypted = fernet.encrypt(text)
        print(f'The encrypted text is: {encrypted}')
        write_pk(private_key)
        print('The private key was saved, dont change that of any sort...')
        
    elif encryptOrDecrypt.lower() == "decrypt":
        if not os.path.isfile('key'):
            raise Exception('A private key was not found, exiting the program...')

        pk = load_pk().encode()
        text = input('Enter the ciphertext you wanna decrypt: ')
        decryptor = Fernet(pk)
        try:
            decrypted = decryptor.decrypt(text.encode())
        except Exception as e:
            if isinstance(e, InvalidSignature):
                print('Invalid private key provided')
            else:
                print('The ciphertext you provided wasnt encrypted in the AES encryption algorithm')
        print(decrypted)

main()