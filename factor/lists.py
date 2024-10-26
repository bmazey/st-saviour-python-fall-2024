
# summation() accepts a list of integers and returns the sum of all numbers within.
# ex: [0, 2, -1, 15] = -> 16
def summation(numbers: list[int]) -> int:
    #
    sum = 0
    # Loop through each number in the list
    for number in numbers:
        # Add the current number to the sum
        sum += number
    # Return the total sum
    return sum

# find_negative() accepts a list of integers containing one negative number
# and returns the *position* of the negative number. You may safely assume
# the provided list contains only a single negative number.
# ex: [11, 13, -1, 0, 9] -> 2
def find_negative(numbers: list[int]) -> int:
    # Loop through the list with an index
    for index in range(len(numbers)):
        # Check if the current number is negative
        if numbers[index] < 0:
             # Return the index of the negative number
            return index

# remove() accepts a list of integers and an int n. The method removes *all instances*
# of n from the provided list and returns a new list with no instances of n.
# ex: [0, 1, 1, 2, 2, 3], n = 2 -> [0, 1, 1, 3]
def remove(numbers: list[int], n: int) -> list[int]:
    # Create a new list excluding all instances of n
    result = [number for number in numbers if number != n]
    # Return the new list
    return result

# merge() accepts two *pre-sorted* lists of integers and returns a new *sorted* list.
# WARNING do not assume lists are of equal length!
# ex: [0, 2, 4, 8] + [1, 3, 5] -> [0, 1, 2, 3, 4, 5, 8]
def merge(first: list[int], second: list[int]) -> list[int]:
    # Combine both lists into one
    combined = first + second
    # Sort the combined list
    combined.sort()
    # Return the sorted list
    return combined

# round_up() accepts a list of *non-negative* floats and returns a list of
# rounded integers. Floats are rounded up iff the decimal is >= 0.5.
# ex: [1.2, 3.5, 4.2, 0.0] -> [1, 4, 4, 0]
def round_up(floats: list[float]) -> list[int]:
    # List to store rounded integers
    rounded_integers = []
    # Loop through each float
    for number in floats:
        # Check if decimal part is >= 0.5
        if number - int(number) >= 0.5:
            # Round up
            rounded_integers.append(int(number) + 1)
        else:
            # Just take integer part
            rounded_integers.append(int(number))
    # Return the list
    return rounded_integers

# evens_only() accepts a list of integers and returns a new list containing
# only the even numbers found in the provided list, in their original order.
# ex: [3, 4, 7, 8, 12] -> [4, 8, 12]
def evens_only(numbers: list[int]) -> list[int]:
    # List to store even numbers
    evens = []
    # Loop through each number
    for number in numbers:
        # Check if number is even
        if number % 2 == 0:
            # Add to list
            evens.append(number)
    # Return the list
    return evens

# last_of_four_digits() accepts a list of four-digit integers and returns a new
# list containing only the last digit of each number in the original sequence.
# ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]
def last_of_four_digits(numbers: list[int]) -> list[int]:
    # List to store last digits
    last_digits = []
    # Loop through each number
    for number in numbers:
        # Get last digit
        last_digits.append(number % 10)
    # Return the list
    return last_digits
