

def factorial(n: int) -> int:
    # TODO implement for +10 bonus
    if n == 1:
        return 1
    return n * factorial(n - 1)








    # iterative
    # result = 1
    # i = 1
    # while i <= n:
    #     result *= i
    #     i += 1
    # return result

    # recursive
    # if n == 1:
    #     return 1
    # return n * factorial(n - 1)
    return 0

def choose(n: int, k: int) -> int:
    # TODO implement for +10 bonus
    return 0