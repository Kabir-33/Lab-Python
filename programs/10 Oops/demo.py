class Demo:
    var1 = "Hello"
    var2 = "welcome"

    def fun(self):
        print("Hi", self.var1)
        print("Hi", self.var2)

obj = Demo()
print(obj.var1)
obj.fun()
