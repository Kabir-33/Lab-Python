class base:
    def eating(self):
        print("The animal is barking ...")

class child(base):
    def animal(self):
        print("The animal name is dog ...")

object=child()
object.animal()
object.eating() 