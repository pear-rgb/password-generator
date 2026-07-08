from secrets import choice
import string

VERSION = "1.0"

def menu():
    length = ''
    print('Password generator ' + VERSION)
    while type(length) != int:
        length = input('Length: ')
        if length.isnumeric():
            length = int(length)
    return length

def generator(length):
    alphabet = string.ascii_letters + string.digits + '!=+~-_#*()[]?$@'
    password = ''
    for _ in range(length):
        password += choice(alphabet)
    return password

print(generator(menu()))
input('Press enter to close')