
class Platypus:
    def __init__(self, name: str, is_aquatic: bool, eggs: int):
        self.name = name
        self.is_aquatic = is_aquatic
        self.eggs = eggs

    def swim(self):
        print(self.name + " swims!")

    def lay_egg(self):
        self.eggs += 1
 
    def lay_eggs(self, eggs: int):
        self.eggs += eggs