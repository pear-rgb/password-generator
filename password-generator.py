from secrets import choice, SystemRandom
from string import ascii_lowercase, ascii_uppercase, digits

_random = SystemRandom()

VERSION = "1.8"
MAX_LIMIT = 256
MIN_LIMIT = 12

def menu():
    
    length = ''
    config = ''
    charsets = []
    
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

    if '1' in config: charsets.append(ascii_uppercase)
    if '2' in config: charsets.append(ascii_lowercase)
    if '3' in config: charsets.append(digits)
    if '4' in config: charsets.append("""!=+~-_#*()[]<>?$@^&.,:;'"/|\\""")

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

    return length, charsets

def generator(length, charsets):
    alphabet = ''.join(charsets)
    password = [choice(cs) for cs in charsets]
    password += [choice(alphabet) for _ in range(length - len(charsets))]
    _random.shuffle(password)
    return ''.join(password)

def warning(text):
    print(text + '\nType "I understand" to ignore this.')
    if input().strip().lower() == 'i understand':
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        data = menu()
        print(generator(data[0], data[1]))
        input('Press enter to close')
    except (KeyboardInterrupt, EOFError):
        print('\nCancelled.')