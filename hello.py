# a fibonachi sequence is a spiral. it looks like this: 
# 0 1 1 2 3 5 8 13 21 
#every number starting at 1 is the sum of the 2 that came before it. it grows quickly. 
# its done with a pure loop which is difficult 
# to write a function that could compute a fibinachi sequence, you would : 

# def fibonachi (n:int): 
    # if n == 0 : 
        # return 0 
    # if n == 1 : 
        # return 1
     # fibonachi(n-1)+fibonachi(n-2)

    # the recursive call for fibinachi, is where the function will call itself.
    # it will look like : 

   # return fibonachi(n-1)+fibonachi(n-2)

   # how can we make this fibonachi better? the problem is its doing the same thing
   # over and over again. 
   # we need to make this faster, so we needd to use a list. we need to remember 
   # what happened previosuly so we don't need to repeat it when we did it recursively. 
   # lets do a 2nd fibonachi 

def fibonacci (n:int) :
    if n <= 1 : 
     return n 
result = [0, 1 ]
for i in range (2, n + 1) :
     result.append (result [i-1] + result [i-2])
     # return result [n]

# your getting the very last element in the list from that. 
#this is called a dynamic fibonachi because it never computes the same thing twice
#your only ever moving foward. 



# how many total unique combination of 2 can you get from 3 marbles? 
# the combination formula : (n) =   n!
                #           (k)    k!(n-k)!

# 3 !
# 2! (3-2) !

# 3!= 3 * 2 * 1 = 6/2 = 3 
# so we get three. 

# - -- - --- - - - - --- - - - - -

# if n = 5 and k = 2 

# --------------------------------------------------------------------------------

# def sequence(n: int) -> int:
    # TODO implement
   # return 0 
   # if n < 0: 
      #  return 0 
   # if n == 0: 
      #  return 0

            
    # last_of_four_digits() accepts a list of four-digit integers and returns a new
# list containing only the last digit of each number in the original sequence.
# ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]





# def last_of_four_digits(numbers: list[int]) -> list[int]:
    # TODO implement
    # return [] 
#for number in numbers: 
 #   number % 10 
  #  return result

# -- --- --- -- --- --- -- --- --- -- 

# This function accepts a list called numbers. 
# The numbers within this list are always 0 inclusive 
# to 100 exclusive. You pick the smallest and 
# largest number . Write a function that returns the 
# smallest number inside of the list every time. 
# Ex. [2,2,3,1]
#You’d give him 99,98,96,91,92
# Any collection of 0’s up to 100 and find the 
# smallest number from this and return it. 


# def least (numbers: list [int]) :
#    small = 100 
#    for number in numbers : 
#       if number > small : 
#          small + number 
#     return small 