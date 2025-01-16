# string are immutable(Cant Be Changed)

a="!!! Chirag !!! Chirag !!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.capitalize()) #the capitalized only do to upper case it first letter not all other words first letter'''
#and it change other character into small
print(a.rstrip("!"))
print(a.replace("Chirag","John"))
print(a.split(" "))
str1 = "Hello Everyone"
print(len(str1))
print(str1.center(51))
print(len(str1.center(51))) # It amke Word Or Phrase To Align In Center With The N number of Length it Will show the n length that you stored
print(a.count(" "))
print(a.endswith("!"))
print(a.startswith("!"))
b="Chirag going to japan"
print(b.endswith("to",7,15))
print(b.startswith("g",7,15))
print(b.count("g",7,15))
print(str1.find("Everyone"))
print(str1.find("everyone")) #return -1 because it is not same as in str1 string
print(str1.index("Everyone"))
str1 = "chirag123"
print(str1.isalnum())
str1 = "chiragsuthar"
print(str1.isalpha())
print(str1.islower())
print(str1.isupper())
print(str1.isprintable())
str1 = "Indian Space Research Organization"
print(str1.istitle())
str1=" "
print(str1.isspace())
str1 = "hello everyone it today date"
print(str1.title())
print("Hello Everyone Its My Bday".swapcase())