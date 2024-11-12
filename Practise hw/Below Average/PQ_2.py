# Python program to find largest of two numbers

a,b=input("Enter two number:").split()
print("The 1st number is :",a)
print("The 2nd Number is :",b)

if(a>b):
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")