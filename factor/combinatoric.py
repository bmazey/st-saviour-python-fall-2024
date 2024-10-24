

def factorial(n: int) -> int:
    # TODO implement for +10 bonus
    index = 1
    product = 1
    while index <= n:
        product *= index
        index += 1
    return product

def choose(n: int, k: int) -> int:
    # TODO implement for +10 bonus
    return factorial(n)/(factorial(k)*factorial(n-k))