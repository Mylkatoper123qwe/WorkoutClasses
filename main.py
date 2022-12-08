class Pet:
    def __init__(self,dog,cat,parrot ):
        self.dog = dog
        self.cat = cat
        self.parrot = parrot

class Dog:
    def __int__(self,name,birth,dead,):
        self.name = name
        self.birth = birth
        self.dead = dead

class Cat:
    def __int__(self, name, birth, dead,):
        self.name = name
        self.birth = birth
        self.dead = dead


class Parrot:
    def __int__(self, name, birth, dead,):
        self.name = name
        self.birth = birth
        self.dead = dead
        self.pets = []
    def add_pet(self,pet):
        self.pets.append(pet)

Animal = Pet("Gylf","Zurbik","Garik")
Animal.add_Pet(Pet("Gylf"))

Animal.print.pets()







