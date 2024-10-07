import re 
string ="Hello  $ kaby its 2.30 what are u dealing with there is something special for you at 4 o'clock"
# find occurences of the number and print the number indivdually...
regex='\d'
match=re.findall(regex,string)
print(match)

# find number and print the number at the one go ...
regex='\d+'
match=re.findall(regex,string)
print(match)

# It deletes all the number in the string...
regex='\D+'
match=re.findall(regex,string)
print(match)

# It counts all the white spaces...
regex='\s'
match=re.findall(regex,string)
print(match)

# Matches all the characters other than space ...
regex='\S'
match=re.findall(regex,string)
print(match)

# Matcehs all the alpha numeric characters (a..z , A...Z , 0...9)
regex='\w'
match=re.findall(regex,string)
print(match)

# Matches all the non-alpha characters ...
regex='\W'
match=re.findall(regex,string)
print(match)
