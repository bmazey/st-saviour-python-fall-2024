

def factorial(n: int) -> int:
    # If n is 1, return 1
    if n == 1:
        return 1
    # Otherwise, return n times factorial of (n - 1)
    return n * factorial(n - 1)

def choose(n: int, k: int) -> int:
    # If k is more than half of n, use n - k instead
    if k > n - k:
        k = n - k
    # Start with result as 1
    result = 1
    # Loop to calculate the combination
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    # Return the final result
    return result