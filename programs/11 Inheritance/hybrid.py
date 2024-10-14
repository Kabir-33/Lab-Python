class Animal:
    def speak(self):
        print("The animal speaks...")

class Mammal(Animal):
    def birth(self):
        print("It gives Birth...")

class Bird:
    def eggs(self):
        print("It lays eggs...")

class Platypus(Mammal,Bird):
    pass

p=Platypus()
p.speak()
p.birth()
p.eggs()