# Sum of 1st even natural numbers 

a=int(input("Enter number upto where you want to calculate :"))
sum=0
for i in range(2,a+1,2):
    sum+=i
print("Sum is :",sum)

# By Formula 
# Sum of 1st n natural numbers is : n*(n+1)

if(a%2==0):
    add=a/2
    print("Addition is :",add*(add+1))
else:
    add=(a-1)/2 
    print("Addition is :",add*(add+1))