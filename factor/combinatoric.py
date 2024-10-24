

def factorial(n: int) -> int:
    # TODO implement for +10 bonus
    # need to know the math and when resut equal 0, 1, kust return themselves
    result = 1 
    i = 1
    while i <= n:
        result *= i 
        i += 1 
    return result

def choose(n: int, k: int) -> int:
    # TODO implement for +10 bonus
    # need to know the name of the lust
    result = factorial(n) / (factorial(k) * factorial(n - k))

    return result
