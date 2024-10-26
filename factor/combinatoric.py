# 5! --> 5 * 4 * 3 * 2 * 1 = 120 possible rearrangements 
# 3! --> 3 * 2 * 1

# from factor.combinatoric import factorial

def factorial(n: int) -> int:
    # uses a while loop to multiply all numbers that are greater than 0 and less than/equal to n, stores that product in the variable num, and then returns num
    num = 1
    i = 1
    while i <= n:
        num *= i
        i += 1
    return num

def choose(n: int, k: int) -> int:
    # uses comination formula to find and return the number of possible combinations
    result = factorial(n) / (factorial(k) * factorial(n-k))
    return result
