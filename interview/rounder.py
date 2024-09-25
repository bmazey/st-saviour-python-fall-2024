

def round(number: float) -> int:
    """
    round() accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    # TODO implement round function
    # 2.5%1=0.5
    # 2.1%1 = 0.1

    # returns the same number if the given number is whole
    if number % 1 == 0:
        return number
    # returns a rounded down version of given number if decimal is below 0.5
    if number % 1 <= 0.4: 
        return int(number)
    # returns a rounded up version of given number if decimal exceeds 0.4
    elif number % 1 >= 0.5:
        return int(number) + 1
    return 0