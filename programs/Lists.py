# List programs where list is showed in the rectangualr brackets []

names=["Kabir","Anuj","Raj"]
print(names)
print(names[0])
print("\n**********\n\n")

# multidimentional list 
surname=[["Patil","Sonwalkar"],["Ulape","Dhenge"]]
print(surname[0][0])
print(surname[0][1])
print(surname[1][0])
print(surname[1][1])

print("\n\n***********\n\n")
# By using for loop 
print("By using for loop:")
for i in names :
    print(i)

print("\n\n***********\n\n")
# By negative index
print("Accessing by negative index :")  # Its shows the last name of the list 
print(names[-1])

print("\n\n***********\n\n")
#  String conversion into list by using Split
str=("Tony Stark")
l1=str.split()
print("String Becames List :",l1)

print("\n\n***********\n\n")
# Append (To add the elements in list )
names.append("Aditya")
print(names)