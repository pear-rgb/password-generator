from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits

VERSION = "1.1"

def menu():
    
    length = ''
    config = ''
    alphabet = ''
    
    print('----------------------')
    print('Password generator ' + VERSION)
    print('----------------------')
    print('Config:')
    print('1. ABC...\n2. abc...\n3. 123...\n4. !@#$...')

    while type(config) != int:
        config = input('Enter the numbers without spaces: ')
        if config.isnumeric() and '1' in config or '2' in config or '3' in config or '4' in config:
            config = int(config)
    
    config = list(str(config))

    if '1' in config: alphabet += ascii_uppercase
    if '2' in config: alphabet += ascii_lowercase
    if '3' in config: alphabet += digits
    if '4' in config: alphabet += '!=+~-_#*()[]?$@^'

    while type(length) != int:
        length = input('Length: ')
        if length.isnumeric():
            length = int(length)

    return length, alphabet

def generator(length, alphabet):
    password = ''
    for _ in range(length):
        password += choice(alphabet)

    return password

data = menu()
print(generator(data[0], data[1]))
input('Press enter to close')