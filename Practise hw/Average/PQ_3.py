#Company insures its drivers in the following cases
# 1 If the driver is married 
# 2 if the driver is unmarried ,male and above 30 years pf age
# 3 If driver is unmarried ,female and above 25 years of age 

# In all other cases the driver is not insured .

print("Enter 1. If driver is male")
print("Enter 2. If driver is female\n")
gender=int(input("Enter your  choice :"))

age =int(input("Enter age of Driver :"))
print(" 1 for married\n 2 for unmarried")
status=int(input("Enter maratial status :" ))

if(gender==1 and age>30 and status==1):
    print("\nCongralutation...\nDriver is insurred.")
elif(gender==2 and age>25 and status==2):
    print("\nCongralutation...\nDriver is insurred.")
else:
    print("Driver is not insurred...")
