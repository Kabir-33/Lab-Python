# Set intersection program
set1=set()
set2=set()

for i in range(7):
    set1.add(i)

for i in range(5,9):
    set2.add(i)

set3=set1.intersection(set2)        # output is {5,6}
print("Intersection using function :")
print(set3)

set4=set1 & set2
print("\nBy using operator: ",set4)

# Set difference -

set5=set1-set2      # By function we can also use as [ set1.difference(set2) ]
print("Set difference is :",set5)

# union program
fruit1={"Apple","Banana","Melon"}
fruit2={"Mango","Jackfruit","Watermelon"}
print("\nBy using union function :",fruit1.union(fruit2))
fruit=fruit1|fruit2
print("\n\n By using operator: ",fruit) 