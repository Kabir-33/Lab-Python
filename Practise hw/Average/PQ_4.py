# Print sum of odd numbers upto n

a=int(input("Enter number upto where you want to sum :"))
sum=0

for i in range(1,a+1,2):
    sum+=i
print("Sum of odd numbers is :",sum)

# By using logic formula we know that Sum of odd natural numbers is= (n*n+1)
a=int(input("enter 1st how many odd numbers you want to calculate :"))
print(a**2)