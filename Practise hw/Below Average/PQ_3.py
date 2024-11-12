# check number is positive or negative



num=int(input("Enter Number to check Weather it is positive or negative:"))
# As  python language take input directly as string so...
# "int" is must in this statement to typecast string value to the integer 
print(num)

if(num>0):
    print("The Number is positive...")
else:
    print("The Number is negative....")
