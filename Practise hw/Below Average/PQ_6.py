# Print odd number and even number upto n

n= int(input("Enter upto where you want to print the number :"))

print("Even Numbers :")
for i in range(2,n,2):
    print(i)

print("Odd numbers :")
for i in range(1,n,2):
    print(i)