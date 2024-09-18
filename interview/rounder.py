

def round(number: float) -> int:
    """
    round() accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    # TODO implement round function
    if number % 1 >= .5:
        # int(number)
        return int(number)+1
    if number % 1 < .5:
        int(number)
        return int(number)