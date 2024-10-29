
# summation() accepts a list of integers and returns the sum of all numbers within.
# ex: [0, 2, -1, 15] -> 16
#making sum += to numbers allows the system to combine all the sumbers in the list
#additionally, sum = 0 allows you to add whatever value to it

#sum must equal zero so we can add whatever number to it
def summation(numbers: list[int]) -> int:
    sum = 0 
    for number in numbers:
        sum += number
    return sum

# find_negative() accepts a list of integers containing one negative number
# and returns the *position* of the negative number. You may safely assume
# the provided list contains only a single negative number.
# ex: [11, 13, -1, 0, 9] -> 2

# in the third line of code, we have to find the number less than zero to find NEGATIVE!!! woah!!
def find_negative(numbers: list[int]) -> int:
    for index in range (len(numbers)):
        if numbers [index] < 0:
            return index

# remove() accepts a list of integers and an int n. The method removes *all instances*
# of n from the provided list and returns a new list with no instances of n.
# ex: [0, 1, 1, 2, 2, 3], n = 2 -> [0, 1, 1, 3]

# beep boop numbers.remove(n) removes the number you want from the list beep boop morp
def remove(numbers: list[int], n: int) -> list[int]:
    while n in numbers:
        numbers.remove(n)
    return numbers
  
# merge() accepts two *pre-sorted* lists of integers and returns a new *sorted* list.
# WARNING do not assume lists are of equal length!
# ex: [0, 2, 4, 8] + [1, 3, 5] -> [0, 1, 2, 3, 4, 5, 8]
def merge(first: list[int], second: list[int]) -> list[int]:
    # TODO implement
    # HINT use list.sort()

    # the use of the function sort brings this code all together!!
    for number in second:
        first.append(number)
        first.sort()
    return first

# round_up() accepts a list of *non-negative* floats and returns a list of
# rounded integers. Floats are rounded up iff the decimal is >= 0.5.
# ex: [1.2, 3.5, 4.2, 0.0] -> [1, 4, 4, 0]
def round_up(floats: list[float]) -> list[int]:
    # TODO implement

    #put the equation with the function for quicker results!!
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

# two is like the IT girl of even numbers, so it would only make sense to mod by two
# (actual reason: all evens can be divided by two, so two mod all even numbers will always end in zero)
def evens_only(numbers: list[int]) -> list[int]:
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

# last_of_four_digits() accepts a list of four-digit integers and returns a new
# list containing only the last digit of each number in the original sequence.
# ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]

#EVEYTHING IS MODULO
def last_of_four_digits(numbers: list[int]) -> list[int]:
    result = []
    for number in numbers:
        result.append(number % 10)
    return result
