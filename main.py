class pet:
    def __init__(self, name):
        self.name = name
        self.pets = []
class Dog:
    def __init__(self,CharacteristicDog, name,birth,wool,died ):
        self.CharacteristicDog = CharacteristicDog
        self.name = name
        self.birth = birth
        self.wool = wool
        self.died = died
        self.pets = []
    def info(self):
        print(f"CharacteristicDog: {self.CharacteristicDog}\nNameDog: {self.name}\nDateBirth: {self.birth}\nWool: {self.wool}\nDied: {self.died}")

class Cat:
    def __init__(self,CharacteristicCat,name,birth,wool,died):
        self.CharacteristicCat = CharacteristicCat
        self.name = name
        self.birth = birth
        self.wool = wool
        self.died = died
        self.pets = []
    def info(self):
        print(f"CharacteristicCat: {self.CharacteristicCat}\nName: {self.name}\nDateBirth: {self.birth}\nWool: {self.wool}\nDied: {self.died}")

class Parrot:
    def __init__(self,CharacteristicParrot,name,birth,wool,died):
        self.CharacteristicParrot = CharacteristicParrot
        self.name = name
        self.birth = birth
        self.wool = wool
        self.died = died
        self.pets = []
    def info(self):
        print(f"CharacteristicParrot: {self.CharacteristicParrot}\nName: {self.name}\nDateBirth: {self.birth}\nWool: {self.wool}\nDied: {self.died}")

    def for_pet(self, animal):
        self.pets.append(animal)


s = Dog("","Patron","20/09/2019","Brown","20/01/2024")
s.info()

b = Cat("","Smasik","1/01/2015","Orange","15/06/2024")
b.info()

d = Parrot("","Papygaya","24/02/2010","Red","20/12/2030")
d.info()


