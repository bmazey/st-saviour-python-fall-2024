

def is_palindrome(word: str) -> bool:
    """
    is_palindrome() accepts a string as input and returns:
        - True if the provided word is a palindrome
        - False if the provided word is NOT a palindrome
    """
    # the cast operator of word allows the computer to check for a palidrome
    # TODO implement is_palindrome function
    return word == word[::-1]
