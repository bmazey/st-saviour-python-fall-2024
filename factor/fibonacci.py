
# sequence() accepts an integer n and returns the value of the
# nth position of a standard fibonacci sequence, starting at 0.
# Recall the fibonacci sequence is defined as follows ...
# 0, 1, 1, 2, 3, 5, 8 ...
# ex: n = 6 -> 8

# we're trying to find the value of the position expressed by the combination of int and n.
# using fibonacci itself would not work in this code.
def sequence(n: int) -> int:
    if n == 0:
        return 0
    if  n == 1:
        return 1
    return sequence(n - 1) + sequence(n - 2)
# to fibonacci or to not fibonacci, that is the question
        
