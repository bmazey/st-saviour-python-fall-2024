

def is_palindrome(word: str) -> str:
    """
    is_palindrome() accepts a string as input and returns:
        - True if the provided word is a palindrome
        - False if the provided word is NOT a palindrome
    """

    # TODO implement is_palindrome function

    # Check if the word is equal to its reverse
    return word == word[::-1]
