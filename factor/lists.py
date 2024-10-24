def summation(numbers: list[int]) -> int:
    # slime rancher (adds everything in list "numbers" together and gives what that sum is)
    sum = 0
    for number in numbers:
        sum += number
    return sum

def find_negative(numbers: list[int]) -> int:
    # frostpunk thermometer simulator (finds a negative number and displays it. if there isn't a negative number in the list, it resorts to showing -1)
    i = 0
    while i < len(numbers):
       if numbers[i] < 0:
           return i
       i += 1
    return -1

def remove(numbers: list[int], n: int) -> list[int]:
    # calls a hitman on "n" (takes every number that isn't "n" and moves it to a separate list, and displays that separate list)
    result = []
    for number in numbers:
        if number != n:
            result.append(number)
    return result

def merge(first: list[int], second: list[int]) -> list[int]:
    # creates a power rangers megazord (takes list "first" and list "second", shoves all the numbers into "first", and sorts the numbers in order)
    for number in second:
        first.append(number)
    first.sort()
    return first
 
def round_up(floats: list[float]) -> list[int]:
    # cowboy's gambit (similar code to "rounder" in the interview lab- takes a number, turns it into an integer, and adds one if the remainder's greater than five)
    result = []
    for number in floats:
        if number % 1 >= .5:
            result.append(int(number)+1) 
        else:
            result.append(int(number))
    return result

def evens_only(numbers: list[int]) -> list[int]:
    # sends odd numbers to hell before they die (only displays numbers that can be cleanly divised by 2, i.e. even numbers)
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

def last_of_four_digits(numbers: list[int]) -> list[int]:
    # steals your parents' credit card (displays placement of a number [specifically the tens place])
    digits = []
    for number in numbers:
        digits.append(number % 10)
    return digits