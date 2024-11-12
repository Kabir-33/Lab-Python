# Find largest of three numbers...

a,b,c=input("Enter three numbers :").split()

if(a>b and a>c):
    print(f"{a} is greator than {b} and {c}")
elif(b>a and b>c):
    print(f"{b} is greator than {a} and {c} ")
else:
    print(f"{c} is greator than {a} and {b} ")

# Find Smallest of three number Entered Above


if(a<b and a<c):
    print(f"{a} is Smaller than {b} and {c}")
elif(b<a and b<c):
    print(f"{b} is Smaller than {a} and {c} ")
else:
    print(f"{c} is Smaller than {a} and {b} ")
