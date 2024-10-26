

def factorial(n: int) -> int:
    # TODO implement for +10 bonus
    result=1
    i=1
    while i <=n:
        result *=i
        return result 

def choose(n: int, k: int) -> int:
    # TODO implement for +10 bonus
    result = factorial(n) / (factorial(k) * factorial(n*k))