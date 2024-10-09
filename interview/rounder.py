

def round(number: float ) -> int:
    remainder = number % 1
    if remainder >= .5:
        return int(number) + 1
    return int(number)