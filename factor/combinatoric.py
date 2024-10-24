

def factorial(n: int) -> int:
    # TODO implement for +10 bonus
    #need to know mathamtical and know when the result equals 0, 1. 
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1 
    return result 


def choose(n: int, k: int) -> int:
    # TODO implement for +10 bonus
    #know the same is "factorial"
    result = factorial(n) / (factorial(k) * factorial(n-k))

    return result