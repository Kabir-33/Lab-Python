# 3. Find factorial of a number using recursion in python.


def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter a number to find factorial : "))
result =factorial(n)
print(f"The factorial of a {n} is {result}")