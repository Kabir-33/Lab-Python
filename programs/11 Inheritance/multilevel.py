class base:
    def car(self):
        print("The car is four wheeler...")

class base2(base):
    def fuel(self):
        print("The car needs fuel for running...")

class child(base2):
    def name(self):
        print("You select Tesla as a car...")

object=child()
object.name()
object.car()
object.fuel()

