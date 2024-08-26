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

# Set difference +

set5=set1-set2
print("Set difference is :",set5)
