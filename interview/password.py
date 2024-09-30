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

    # Define the characters
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    symbols = '!@#$%^&*'

    # Generate the first 5 lowercase letters
    first_five_letters = ''
    for _ in range(5):
        first_five_letters += random.choice(alphabet)

    # Generate the next 4 digits
    next_four_digits = ''
    for _ in range(4):
        next_four_digits += random.choice(digits)

    # Generate the final character as a symbol
    final_symbol = random.choice(symbols)

    # Combine all parts to form the password
    password = first_five_letters + next_four_digits + final_symbol

    return password