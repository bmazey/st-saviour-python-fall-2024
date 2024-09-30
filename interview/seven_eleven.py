

def seven_eleven(number: int) -> str:
    """
    seven_eleven() accepts a number and returns:
        - 'seven' if the number is a multiple of 7
        - 'eleven' if the number is a multiple of 11
        - 'seveneleven' if the number is a multiple of 7 and 11
        - an empty string if the number is not a multiple of 7 or 11
    """

    # TODO implement seven_eleven function
   
   # Check if the number is a multiple of both 7 and 11
    if number % 7 == 0 and number % 11 == 0:
        return 'seveneleven'
    
    # Check if the number is a multiple of 11
    if number % 11 == 0:
        return 'eleven'
    
    # Check if the number is a multiple of 7
    if number % 7 == 0:
        return 'seven'
    
    # Return an empty string if the number is not a multiple of 7 or 11
    return ''