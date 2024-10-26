
# summation() accepts a list of integers and returns the sum of all numbers within.
# ex: [0, 2, -1, 15] -> 16
from operator import index


def summation(numbers: list[int]) -> int:
    sum = 0
    # adds each number in the list to sum and returns the new total
    for number in numbers:
        sum += number
    return sum    

# find_negative() accepts a list of integers containing one negative number
# and returns the *position* of the negative number. You may safely assume
# the provided list contains only a single negative number.
# ex: [11, 13, -1, 0, 9] -> 2
def find_negative(numbers: list[int]) -> int:
    # starts from 0
    i = 0
    # finds number that is negative and returns its positon
    while i < len(numbers):
        if numbers[i] < 0:
            return i
        i += 1
    return -1

# remove() accepts a list of integers and an int n. The method removes *all instances*
# of n from the provided list and returns a new list with no instances of n.
# ex: [0, 1, 1, 2, 2, 3], n = 2 -> [0, 1, 1, 3]
def remove(numbers: list[int], n: int) -> list[int]:
    # creates an empty list
    result = []
    # finds all numbers that are not n and adds them to an empty list
    for number in numbers:
        if number != n:
            result.append(number)
    # returns the new list
    return result

def merge(first: list[int], second: list[int]) -> list[int]:
    # uses the append and sort functions to combine first and second into one list and then sort it
    for number in second:
        first.append(number)
    first.sort()
    return first

# round_up() accepts a list of *non-negative* floats and returns a list of
# rounded integers. Floats are rounded up iff the decimal is >= 0.5.
# ex: [1.2, 3.5, 4.2, 0.0] -> [1, 4, 4, 0]
def round_up(floats: list[float]) -> list[int]:
    # creates an empty list
    round = []
    for number in floats:
        # uses modulo and casting to round numbers up or down and adds the rounded numbers to an empty list
        if number % 1 >= 0.5:
            round.append(int(number)+1)
        else:
            round.append(int(number))
    # returns the new list
    return round

# evens_only() accepts a list of integers and returns a new list containing
# only the even numbers found in the provided list, in their original order.
# ex: [3, 4, 7, 8, 12] -> [4, 8, 12]
def evens_only(numbers: list[int]) -> list[int]:
    # starts with position 0
    i = 0
    # creates an empty list
    result = []
    # uses modulo to determine which numbers are even
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            # adds all of the even numbers to the empty list and then returns that list
            result.append(numbers[i])
        i += 1
    return result

# last_of_four_digits() accepts a list of four-digit integers and returns a new
# list containing only the last digit of each number in the original sequence.
# ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]
def last_of_four_digits(numbers: list[int]) -> list[int]:
    # creates an empty list
    result = []
    # uses modulo to find the last digit, appends that digit to an empty list, and then returns that list
    for number in numbers:
        result.append(number%10)
    return result