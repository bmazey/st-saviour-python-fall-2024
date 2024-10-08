import random

def generate_password() -> str:
    """
    generate_password() takes no arguments and produces a string
    which meets the following password complexity requirements:
        - the length of the password is 10
        - the first 5 characters are lower case letters
        - the next 4 characters are digits [0-9]
        - the final character is a symbol [!@#$%^&*]
        - it's relatively uncommon to generate the same password twice 
    """

    # HINT you will require the use of a random number generator for this function
    # https://docs.python.org/3/library/random.html#random.randint

    # TODO implement generate_password function

    password = ''

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    digits = '12345678910'
    symbol = '!@#$%^&*'
    
    # alphabet[0]
    password += alphabet[random.randint(0, len(alphabet) - 1)]
    password += alphabet[random.randint(0, len(alphabet) - 1)]
    password += alphabet[random.randint(0, len(alphabet) - 1)]
    password += alphabet[random.randint(0, len(alphabet) - 1)]
    password += alphabet[random.randint(0, len(alphabet) - 1)]

    password += digits[random.randint(0, len(digits) - 1)]
    password += digits[random.randint(0, len(digits) - 1)]
    password += digits[random.randint(0, len(digits) - 1)]
    password += digits[random.randint(0, len(digits) - 1)]

    password += symbol[random.randint(0, len(symbol) - 1)]
    
    return password