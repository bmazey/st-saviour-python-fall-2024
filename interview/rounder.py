

def round(number: float) -> int:
    """
    round() accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    # TODO implement round function
    # know that the fianl result should ne an interger
    if number % 1 ==0:
       return number
    if number % 1 <=0.4:
        return int (number)
    if number % 1 >=0.5:
        return int (number) + 1 

    return 0