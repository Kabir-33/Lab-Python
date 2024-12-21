# 10. program for class, object and constructor using suitable data

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

person1 = Person("John Doe", 30, "Mumbai")

person1.display_details()
