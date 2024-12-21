# 14 program for multilevel inheritance

class Animal:
    def __init__(self):
        print("object from animal class...")
        
    def speak(self):
        print("Animal makes a sound")

class Mammal(Animal):
    def speak(self):
        print("Mammal makes a sound")

class Dog(Mammal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()
