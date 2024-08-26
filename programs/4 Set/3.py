# Sets Examples
# output of these question is randomly arranges in the solution
days={"monday","tuesday","wednesday","thrusday","friday","saturday","sunday"}
print(days)
print(type(days))
print("Eelements are : ")
for i in days:
    print(i)

# union program
fruit1={"Apple","Banana","Melon"}
fruit2={"Mango","Jackfruit","Watermelon"}
print("\nBy using union function :",fruit1.union(fruit2))
fruit=fruit1|fruit2
print("\n\n By using operator: ",fruit) 

# Frozenset
fs=frozenset([1,2,3,4])
print("\n",fs)
for i in fs:
    print(i)