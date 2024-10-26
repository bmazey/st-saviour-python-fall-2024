
# sequence() accepts an integer n and returns the value of the
# nth position of a standard fibonacci sequence, starting at 0.
# Recall the fibonacci sequence is defined as follows ...
# 0, 1, 1, 2, 3, 5, 8 ...
# ex: n = 6 -> 8
def sequence(n: int) -> int:
    # If n is 0 or 1, return n
    if n <= 1:
        return n
    # Start the list with the first two Fibonacci numbers
    result = [0,1]
    # Calculate the rest of the Fibonacci numbers up to n
    for i in range(2,n+1):
        result.append(result[i-1] + result[i-2])
    return result[n]