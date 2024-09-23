import random

if __name__ == '__main__':
    # this file is provided for experimentation purposes
    # print('new dawn, new day')

    h = 'abcdefghijklmnopqrstuvwxyz'

    r = random.randint(0, len(h) - 1)
    l = h[r]

    s = 'xoxoxoxoxoxoxoxo'
    print(s[::])
    print(s[::2])
    print(s[1::2])
