
# summation() accepts a list of integers and returns the sum of all numbers within.
# ex: [0, 2, -1, 15] -> 16
# List gives sum
def summation(numbers: list[int]) -> int:
    # TODO implement
    sum=0
    for number in numbers:
        sum += number
    return sum 
    
# find_negative() accepts a list of integers containing one negative number
# and returns the *position* of the negative number. You may safely assume
# the provided list contains only a single negative number.
# ex: [11, 13, -1, 0, 9] -> 2
# Put in place of number not the number itself
def find_negative(numbers: list[int]) -> int:
    # TODO implement
    for index in range (len(numbers)):
        if numbers [index] <0:
            return index


# remove() accepts a list of integers and an int n. The method removes *all instances*
# of n from the provided list and returns a new list with no instances of n.
# ex: [0, 1, 1, 2, 2, 3], n = 2 -> [0, 1, 1, 3]
# add new number
def remove(numbers: list[int], n: int) -> list[int]:
    # TODO implement
   new_list = [number for number in numbers if number !=n]
   return new_list
# merge() accepts two *pre-sorted* lists of integers and returns a new *sorted* list.
# WARNING do not assume lists are of equal length!
# ex: [0, 2, 4, 8] + [1, 3, 5] -> [0, 1, 2, 3, 4, 5, 8]
 # for every number in second list add it in the first list 
#  first.sort() to put it in order 
# Gives a new list 
def merge(first: list[int], second: list[int]) -> list[int]:
    # TODO implement
    # HINT use list.sort()
     for number in second:
         first.append (number)
     first.sort()
     return first 

# round_up() accepts a list of *non-negative* floats and returns a list of
# rounded integers. Floats are rounded up iff the decimal is >= 0.5.
# ex: [1.2, 3.5, 4.2, 0.0] -> [1, 4, 4, 0]
# less than one greater than or equal to 0.5
def round_up(floats: list[float]) -> list[int]:
    # TODO implement
    result = []
    for number in floats:
        if number % 1>=0.5:
            result.append(int(number) +1)
        else:
            result.append(int(number))
    return result
# evens_only() accepts a list of integers and returns a new list containing
# only the even numbers found in the provided list, in their original order.
# ex: [3, 4, 7, 8, 12] -> [4, 8, 12]
# get even numbers in exact place
def evens_only(numbers: list[int]) -> list[int]: 
# TODO implement
    return [number for number in numbers if number %2 == 0]

# last_of_four_digits() accepts a list of four-digit integers and returns a new
# list containing only the last digit of each number in the original sequence.
# ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]
# only last number in a new list in same order
def last_of_four_digits(numbers: list[int]) -> list[int]:
    # TODO implement
    result = []
    for number in numbers:
        result.append (number % 10)
    return result 