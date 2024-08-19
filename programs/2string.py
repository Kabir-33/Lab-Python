# Different forms of declare string
str= "Best football players :"
str1='Nyemar Jr'
str2='''Mabpee'''
print(type(str))    # Print type of entered element
print(str)
print(str1)
print(str2)

print("\n\n***********************************\n\n")

# initialisation and accesing the  character by string index 
a="Hey whats going on"
print("The initialised string is :",a)

print(len(a))
print(a[2])         # Which index u want
print(a[2:])        # From start to the end
print(a[2:8])       # get sting from which index you want and where you wanna end
print(a[-1])        # Access last index because negative index string starts from last index .

 # Reverse the string by 2 formats 
print(a[::-1])      
rev="".join(reversed(a))
print(rev)

print("\n\n**********************************\n\n")

# Upadating a string ...
b="Welcome to college"
print("1st string you Entered :",b)
b="Welcome to DYP College "
print("Same string upadated later becomes :",b)

# upadating a string
string1="Hello Kabir What are you doing"
update_string=string1[0:2]+'p'+string1[3:]  # 3rd index character "l" is replaced by "p"
print(update_string)

string2=string1[0:2]+string1[3:]    # word at second position is deleted
print(string2)

# Formating of integer 

k="{0:b}".format(16)        # To convert the string in binary format
print("Binary form of 16 :")
print(k)

l="{0:.2f}".format(1/6)     # upto 2 decimal point only it print the digit 
print(l)