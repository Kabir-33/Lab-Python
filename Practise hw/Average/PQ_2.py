# Python program to check Weather the year is leep year...

a=int(input("Enter a year:"))

if(a%400==0 or a%100!=0 and a%4==0):
    print(f"{a} is leap year... ")

else:
    print(f"{a} is not a leep year")