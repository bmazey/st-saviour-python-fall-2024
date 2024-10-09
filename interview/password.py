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
    
    return ''
    dog = 'abcdefghijklmnopqrstuvwxyz'
    cat = '0123456789' 
    rat = '!@#$%^&'
    letters = dog[random.randint(0,len(dog) - 1 )]
    numbers = cat[random.randint(0,len(cat) - 1 )]
    symbols = rat[random.randint(0,len(rat) - 1 )]

return letters + letter + letters + letters 