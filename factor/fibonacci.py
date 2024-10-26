
# sequence() accepts an integer n and returns the value of the
# nth position of a standard fibonacci sequence, starting at 0.
# Recall the fibonacci sequence is defined as follows ...
# 0, 1, 1, 2, 3, 5, 8 ...
# ex: n = 6 -> 8
def sequence(n: int) -> int:
    # returns the given number if the given it is less than or equal to 1
    if n <= 1:
      return n
    # uses the append function to add up the two numbers before the number in position i and then returns that new sum
    result = [0, 1]
    for i in range(2, n+1):
      result.append(result[i-1]+result[i-2])
    return result[n]
