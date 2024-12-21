# 11. program for Method overridding

class bird:
    def flight(self):
        print("All birds fly but some can't...")

class parrot(bird):
    def flight(self):
        print("Parrot can fly...")

par=parrot()
par.flight()