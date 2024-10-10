
if __name__ == '__main__':
    # this file is provided for experimentation purposes
    #Casting is taking a variable of one data type and converting it to another data type.
    # x=10.9
    # y=int(x)
    # print(y)
    #float and int have different bit values. An int is 2^32 bits, and a float is 2^64 bits. There isn't enough space to represent the number and so the decimal is chopped off.

    #Main Operators: Addition(+), Subtraction(-), Multiplication(*), Division(/), Modulo(%)
    #Modulo is a division operator that gives the remainder instead of the quotient.
    # print(8%5)
    #Modulo and division by 0 is not possible, so it will create errors.


    # s = "hallo"
    # s += "ween"
    # print('value of s: '+s)

    # h = "Halloween"
    # for i in range(9):
    #    print('i: ' + str(i) + ' h: ' + h[i])

    # taking content in a list and storing it in an iterative loop is called unpacking
    # for character in h: 
    #    print(character)

    # while loops do not keep track of their own iterations
    # i = 0 
    # #terminating condition: tells us when loop is supposed to finish
    # while i<len(h):
    # #gives infinite loop as long as i is less than len(h) or 9
    #     print(h[i])
    #     #increments i by 1 until it stops being less than 9
    #     i+=1

    # the two sets of code below each print every multiple of 5 from 0 - 100 (inclusive)
    # i = 0
    # while i <= 1000:
    #     if i % 3 == 0:
    #         print(i)
    #     i += 1

    # for i in range(0,101):
    #     if i % 5 == 0:
    #         print(i)
    # while i<=100:
    #     print(i)
    #     i+=5

    # the following code consists of a nested loop (aka a loop within a loop) which prints the numbers 0 - 9 ten separate times (indicating when one iteration ends and the next iteration begins)
    # for i in range(10):
    #     for j in range(10):
    #         print(j)
    #     print('iteration ' + str(i) + 'done!')

    # The following code is an alternate way to solve the palindrome assignment from earlier.
    # r = "racecar"
    # reverse = ''

    # # unpacking
    # for character in r:
    #     reverse = character + reverse
    # print('reverse is: ' + reverse)

    # i = len(r) - 1
    # while i >=0:
    #     reverse+=r[i]
    #     i -= 1
    # print(reverse)

    # i = 0 
    # while i<len(h):
    #     reverse+= h[len(h) - 1 - i]
    #     i += 1

    # numbers = [0, 1, 3, 3, 7, 14, -5]
    # print(numbers) # returns [0, 1, 3, 3, 7, 14, -5]
    # print(numbers[len(numbers)- 2]) # returns 14 because the length of the list is 6 and 6-2=4 and 14 is position 4
    # for number in numbers:
    #     print(number) # returns each individual item in the list one after the other
    # # the difference between a list and a set is that a set can not contain any duplicates while lists are arbitrary
    # # numbers[7] = 6 # gives an out of bounds error because the sixth position does not exist
    # # use the following code to add something to the end of a list
    # numbers.append(6)
    # print(numbers) # returns the list with 6 added to the end of it.

    # numbers.remove(3) # removes the first 3 and shifts everything after it one position over to the left.
   
    # # mixed types are bad
    # things = ['we', 'started', 'out', 'as', 'friends', 7]
    # for thing in things:
    #     print("here's the thing" + things) # returns an error because the list has a number in it and cannot be concatonated with a string

    # numbers.insert(2, -4) # inserts a -4 at the second position of the list and moves everything after it one position over to the right.

    # numbers.pop(0) # removes and returns the item at the specified index and removes the last item if no index is provided

    numbers = [0, 2, 2, 2, 3, 1]
    result = []
    print(numbers)
    for number in numbers:
        if number !=2:
            result.append(number) # basically says "if the number im on in the list is not 2, add it to result"
    print(result) # prints a list that was once empty but is now full of all items if the numbers list that are not 2

    # tuples are lists of data with mixed types
            