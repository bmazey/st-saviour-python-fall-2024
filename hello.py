
from operator import index


if __name__ == '__main__':
    # this file is provided for experimentation purposes
    print('new dawn, new day')


    numbers = [0, 1, -2, 3, 4]
    i = 0
    while i < len(numbers):
        if numbers < 0:
            print (index(numbers))
    i+=1