
# summation() accepts a list of integers and returns the sum of all numbers within.
# ex: [0, 2, -1, 15] -> 16
def summation(numbers: list[int]) -> int:
    # TODO implement
    sum = 0
    for number in numbers:
        sum += number
    return sum

# find_negative() accepts a list of integers containing one negative number
# and returns the *position* of the negative number. You may safely assume
# the provided list contains only a single negative number.
# ex: [11, 13, -1, 0, 9] -> 2
def find_negative(numbers: list[int]) -> int:
    # TODO implement
    i = 0
    while i < len(numbers):
       if numbers[i] < 0:
           return i
       i += 1
    return -1

# remove() accepts a list of integers and an int n. The method removes *all instances*
# of n from the provided list and returns a new list with no instances of n.
# ex: [0, 1, 1, 2, 2, 3], n = 2 -> [0, 1, 1, 3]
def remove(numbers: list[int], n: int) -> list[int]:
    # TODO implement
    results = []
    for number in numbers:
        if numbers /= n:
    
    return []

# merge() accepts two *pre-sorted* lists of integers and returns a new *sorted* list.
# WARNING do not assume lists are of equal length!
# ex: [0, 2, 4, 8] + [1, 3, 5] -> [0, 1, 2, 3, 4, 5, 8]
def merge(first: list[int], second: list[int]) -> list[int]:
    # TODO implement
    # HINT use list.sort()
    return []

# round_up() accepts a list of *non-negative* floats and returns a list of
# rounded integers. Floats are rounded up iff the decimal is >= 0.5.
# ex: [1.2, 3.5, 4.2, 0.0] -> [1, 4, 4, 0]
def round_up(floats: list[float]) -> list[int]:
    # TODO implement
    return []

# evens_only() accepts a list of integers and returns a new list containing
# only the even numbers found in the provided list, in their original order.
# ex: [3, 4, 7, 8, 12] -> [4, 8, 12]
def evens_only(numbers: list[int]) -> list[int]:
    # TODO implement
    return []

# last_of_four_digits() accepts a list of four-digit integers and returns a new
# list containing only the last digit of each number in the original sequence.
# ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]
def last_of_four_digits(numbers: list[int]) -> list[int]:
    # TODO implement
    return []