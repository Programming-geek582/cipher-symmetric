from typing import Optional, List

def validate_input(prompt, options : Optional[List]):
    while 1:
        text = input(prompt)
        if text.lower() not in options:
            print('Invalid input, retry with a valid input')
            continue
    
        return text

def write_pk(private_key):
    with open('fernetKey', 'w+') as f:
        f.truncate()
        f.write(private_key)

def load_pk():
    with open('fernetKey', 'r') as f:
        content = f.readlines()

    return content[0]