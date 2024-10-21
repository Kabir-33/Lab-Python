from abc import ABC, abstractmethod

class Car(ABC):
    def mileage(self):
        pass

class Tesala(Car):
    def mileage(self):
        print("Mileage is 30 kmph...")

class Suziki(Car):
    def mileage(self):
        print("Mileage is 50 kmph...")

t = Tesala()
t.mileage()

s = Suziki()
s.mileage()
