

def round(number: float) -> int:
    """
    round() accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    # TODO implement round function
    if number - int(number) >= 0.5:
        # round up by adding 1 to the integer
        return int(number) + 1
    else:
        # round down by just taking the integer
        return int(number)
