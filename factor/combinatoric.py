

def factorial(n: int) -> int:
    # TODO implement for +10 bonus
    result = n
    i = 1
    if i <= n:
       i += 1  
    result *= i
   
    return result 

def choose(n: int, k: int) -> int:
    # TODO implement for +10 bonus
    result = factorial(n) / factorial(k) * factorial(n-k)
    return result