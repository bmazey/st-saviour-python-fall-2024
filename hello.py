from platypus import Platypus

if __name__ == '__main__':
    # this file is provided for experimentation purposes
    # print('new dawn, new day')
    perry = Platypus('Perry', False, 0)
    perry.swim()
    print('Perry has ' + str(perry.eggs) + ' eggs!')
    perry.lay_egg()
    print('Perry has ' + str(perry.eggs) + ' eggs!')
    perry.lay_eggs(3)
    print('Perry has ' + str(perry.eggs) + ' eggs!')

    bob = Platypus('Bob', True, 5)
    bob.swim()
    print('Bob has ' + str(bob.eggs) + ' eggs!')
    bob.lay_egg()
    print('Bob has ' + str(bob.eggs) + ' eggs!')