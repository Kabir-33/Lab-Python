# 11 method overloading

class Example:
    def display(self, a=None, b=None):
        if a is not None and b is not None:
            print(a, b)
        elif a is not None:
            print(a)
        else:
            print("No arguments passed")

obj = Example()

obj.display(1, 2)  # Output: 1 2
obj.display(1)     # Output: 1
obj.display()      # Output: No arguments passed
