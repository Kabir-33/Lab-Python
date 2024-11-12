# Print sum of natural numbers upto  n 

a=int(input("Enter the number upto where you want to add :"))
sum=0

for i in range(1,a+1): # a+1 is used because the last number is always n-1 
    sum+=i
print("The sum is :",sum)
