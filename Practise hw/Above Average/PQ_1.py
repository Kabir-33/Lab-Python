#Student evaluation of exam details 

a=int(input("Enter percentaile :"))

if(a>=90):
    print("Congralution you are passed with Distinction... ")
elif(a>=70 and a<90):
    print("Congralution you got First class Grade...")
elif(a>=50 and a<70):
    print("Congralution you got Average Grade...")
elif(a>=0 and a<50):
    print("Poor Performance you have to study Hard ...")
else:
    print("Enter valid Percentaile...")