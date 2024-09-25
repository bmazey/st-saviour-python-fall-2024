

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
    
    import random

    password = ''

    # arrays
    alphabetLower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','@','#','$','%','^','&','*']

    # alphabetical
    password += alphabetLower[random.randint(0,len(alphabetLower)-1)]
    password += alphabetLower[random.randint(0,len(alphabetLower)-1)]
    password += alphabetLower[random.randint(0,len(alphabetLower)-1)]
    password += alphabetLower[random.randint(0,len(alphabetLower)-1)]
    password += alphabetLower[random.randint(0,len(alphabetLower)-1)]

    # numbers NUMBERS numbeRS NUMbers
    password += numbers[random.randint(0,len(numbers)-1)]
    password += numbers[random.randint(0,len(numbers)-1)]
    password += numbers[random.randint(0,len(numbers)-1)]
    password += numbers[random.randint(0,len(numbers)-1)]

    # symbol
    password += symbols[random.randint(0,len(symbols)-1)]

    return password
