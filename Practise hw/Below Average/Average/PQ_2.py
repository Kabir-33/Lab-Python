# Python program to check Weather the year is leep year...

a=int(input("Enter a year:"))

if(a%400==0 or a%100!=0 and a%4==0): # all conditions should be written at same line with "proper logical operator"
    print(f"{a} is Leap year... ")

else:
    print(f"{a} is not a Leap year")
print("Keep learining")