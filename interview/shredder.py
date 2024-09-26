

def shred_first_character(word: str) -> str:
    """
    shred_first_character() accepts a string and returns 
    a new string with the first character removed.
    """

    # TODO implement shred_first_character function
    # know the structure
    return word[1::]

    return ''

def shred_last_character(word: str) -> str:
    """
    shred_last_character() accepts a string and returns 
    a new string with the last character removed.
    """

    # TODO implement shred_last_character function
    # direction and len
    return word[:len(word) - 1:1]