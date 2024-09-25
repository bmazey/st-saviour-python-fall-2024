

def is_palindrome(word: str) -> bool:
    """
    is_palindrome() accepts a string as input and returns:
        - True if the provided word is a palindrome
        - False if the provided word is NOT a palindrome
    """

    # TODO implement is_palindrome function
    
    # use an increment of -1 to return the string backwards
    return word == word[::-1]
