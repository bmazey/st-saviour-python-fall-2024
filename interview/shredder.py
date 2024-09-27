

def shred_first_character(word: str) -> str:
    """
    shred_first_character() accepts a string and returns 
    a new string with the first character removed.
    """

    # TODO implement shred_first_character function
    # the first spot means the start 
    return word [1::]

def shred_last_character(word: str) -> str:
    """
    shred_last_character() accepts a string and returns 
    a new string with the last character removed.
    """

    # TODO implement shred_last_character function
    # know the difference between len and the actual position
    return word[:len(word) - 1:1]
