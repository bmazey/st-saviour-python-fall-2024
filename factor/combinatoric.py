

def factorial(n: int) -> int:
    # sets up a factorial
    index = 1
    product = 1
    while index <= n:
        product *= index
        index += 1
    return product

def choose(n: int, k: int) -> int:
    # does that complicated equation to find possibilities (in a sense)
    return factorial(n)/(factorial(k)*factorial(n-k))