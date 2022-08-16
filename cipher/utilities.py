import os
import time
from typing import Optional, List
from cryptography.exceptions import InvalidSignature, InvalidKey
from cryptography.fernet import Fernet

def get_input(prompt, options : Optional[List] = None):
    while 1:
        text = input(prompt)
        if options and text.lower() not in options:
            print('Invalid input, retry with a valid input')
            continue
    
        return text

def write_key(key):
    with open('fernetKey', 'w+') as f:
        f.truncate()
        f.write(key)

def load_key():
    if not os.path.isfile('fernetKey'):
        print('A key was not found, exiting the program...')
        time.sleep(2)
        exit()

    with open('fernetKey', 'r') as f:
        content = f.readlines()

    return content[0].encode()

def encrypt_and_display_info(fernet_object : Fernet, key, text : bytes):
    encrypted = fernet_object.encrypt(text)
    print(f'The encrypted text is: \n{encrypted.decode("utf-8")}')
    write_key(key)
    print('The private key was saved, dont change that of any sort...')

def decrypt_and_display_info(ciphertext : bytes):
    key = load_key()
    decryptor = Fernet(key)
    try:
        decrypted = decryptor.decrypt(ciphertext)
        print(f'Decrypted version is: {decrypted.decode("utf-8")}')
    except Exception as e:
        if isinstance(e, InvalidKey):
            print('Invalid key provided')
            return

        elif isinstance(e, InvalidSignature):
            print('The private key doesnt match the digitally signed key of the ciphertext provided.')
            return
    
        else:
            raise e