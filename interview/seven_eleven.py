

def seven_eleven(number: int) -> str:
    """
    seven_eleven() accepts a number and returns:
        - 'seven' if the number is a multiple of 7
        - 'eleven' if the number is a multiple of 11
        - 'seveneleven' if the number is a multiple of 7 and 11
        - an empty string if the number is not a multiple of 7 or 11
    """

    # TODO implement seven_eleven function
    if number % 11 == 0 and number % 7 == 0:
        return 'seveneleven'
    if number % 7 == 0:
        return 'seven'
    if number % 11 == 0:
        return 'eleven' 
    return ''