from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits

VERSION = "1.6"
MAX_LIMIT = 256
MIN_LIMIT = 12

def menu():
    
    length = ''
    config = ''
    alphabet = ''
    
    print('----------------------')
    print('Password generator ' + VERSION)
    print('----------------------')
    print('Config:')
    print('1. ABC...\n2. abc...\n3. 123...\n4. !@#$...')

    while True:
        config = input('Enter the numbers (1-4) without spaces: ')
        if len(config) != 0 and all(i in '1234' for i in config):
            if len(''.join(dict.fromkeys(config))) <= 2:
                if warning('The password has a small character set, making it insecure.'):
                    break
            else:
                break
    
    config = list(config)

    if '1' in config: alphabet += ascii_uppercase
    if '2' in config: alphabet += ascii_lowercase
    if '3' in config: alphabet += digits
    if '4' in config: alphabet += '''!=+~-_#*()[]<>?$@^&.,:;'"/'''

    while True:
        length = input('Length: ')
        if length.isnumeric() and int(length) > 0:
            length = int(length)
            if length > MAX_LIMIT:
                if warning('Excessive length may overload the device.'):
                    break
            elif MIN_LIMIT > length:
                if warning('A short password length is highly insecure.'):
                    break
            else:
                break

    return length, alphabet

def generator(length, alphabet):
    return ''.join(choice(alphabet) for _ in range(length))

def warning(text):
    print(text + '\nType "I understand" to ignore this.')
    if input().strip().lower() == 'i understand':
        return True
    else:
        return False

data = menu()
print(generator(data[0], data[1]))
input('Press enter to close')