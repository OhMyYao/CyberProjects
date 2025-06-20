import string
import random

def generate(length: int = 12): #setting length input. Default to lenth of 12 if no inputed length
    #creates a variable with all the letters, numbers and symbols
    alphabet = string.ascii_letters + string.digits + string.punctuation
    #using the variable alphabet, generate a password of requested length
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password

length = int(input('How long do you need the password to be: '))
print(f'Your password is: {generate(length)}')
