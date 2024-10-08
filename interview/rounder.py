

def round(number: float) -> int:
    """
    round() accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    # TODO implement round function
    remainder = number % 1
    if remainder >= 0.5:
        return int(number) + 1
    return int(number)