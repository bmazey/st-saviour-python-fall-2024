
# summation() accepts a list of integers and returns the sum of all numbers within.
# ex: [0, 2, -1, 15] -> 16
def summation(numbers: list[int]) -> int:
    # TODO implement
    #set sum equal to 0 so that the list start at a right position
    sum = 0
    for number in numbers:
        sum += number
    return sum
        
    return 0

# find_negative() accepts a list of integers containing one negative number
# and returns the *position* of the negative number. You may safely assume
# the provided list contains only a single negative number.
# ex: [11, 13, -1, 0, 9] -> 2
def find_negative(numbers: list[int]) -> int:
    # TODO implement
    # know that we have to put an empety string if you do the while loop
    for index in range(len(numbers)) :
        if numbers [index] < 0 :
           return index    
    return 0

# remove() accepts a list of integers and an int n. The method removes *all instances*
# of n from the provided list and returns a new list with no instances of n.
# ex: [0, 1, 1, 2, 2, 3], n = 2 -> [0, 1, 1, 3]
def remove(numbers: list[int], n: int) -> list[int]:
    # TODO implement
    # result = []
    # for number in numbers:
    #     if number != n:
    #         number.append(result)
    # return result
    # know that n means number not position

    while n in numbers:
        numbers.remove(n)
        
    return numbers
  

# merge() accepts two *pre-sorted* lists of integers and returns a new *sorted* list.
# WARNING do not assume lists are of equal length!
# ex: [0, 2, 4, 8] + [1, 3, 5] -> [0, 1, 2, 3, 4, 5, 8]
def merge(first: list[int], second: list[int]) -> list[int]:
    # TODO implement
    # HINT use list.sort()
    # know the what does fuction do-smallest to greatest in the list
    for number in second:
        first.append(number)
    first.sort()
    return first
    

    return []

# round_up() accepts a list of *non-negative* floats and returns a list of
# rounded integers. Floats are rounded up iff the decimal is >= 0.5.
# ex: [1.2, 3.5, 4.2, 0.0] -> [1, 4, 4, 0]
def round_up(floats: list[float]) -> list[int]:
    # TODO implement
    # know that we could go striaght up to put equation in a function
    result = []
    for number in floats:
        if number % 1 >= 0.5:
            result.append(int(number) + 1)
        else:
            result.append(int(number))
    return result

# evens_only() accepts a list of integers and returns a new list containing
# only the even numbers found in the provided list, in their original order.
# ex: [3, 4, 7, 8, 12] -> [4, 8, 12]
def evens_only(numbers: list[int]) -> list[int]:
    # TODO implement
    # need to figure out what to put in the list
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

# last_of_four_digits() accepts a list of four-digit integers and returns a new
# list containing only the last digit of each number in the original sequence.
# ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]
def last_of_four_digits(numbers: list[int]) -> list[int]:
    # TODO implement
    # nned to know .append is a function and has its own meaning fv 
    result =[]
    for number in numbers:
        result.append(number % 10)
    return result
