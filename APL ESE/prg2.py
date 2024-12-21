# 2. Find the factorial of a number in python.

a=int(input("Enter a number to find a factorial of a number : "))
fact=1
if(a==0):
    print("factorial is 1")
else:
    for i in range(1,a+1):
        fact=fact*i

print("Factorial of a number is ",fact)