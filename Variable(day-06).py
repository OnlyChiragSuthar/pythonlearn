# a= 1  <int>
# b= True  <bool>
# c="harry" <str>
# d= None <NULL>

a=1123
b="chirag"
c="123"

print(type(a))
print(type(b))
print(type(c))
print(str(a)+b)
print(b+c)
# print(a+b)  #error Will Be Occurs

# Complex Number (a+bi)

x=complex(4,3)
print(x)
y=complex(2,6)
print(y)
print(x-y)

list1=[1,3.5,-2,[-4,5],["apple","banana"]]
print(list1)

#List Are Mutables(Can Be Changed)

# Syntax: list1[0]="9"

list1[1]=9
print(list1)
list1.remove(-2)
print(list1)
list1.insert(1,"banana")
print(list1)
print(len(list1))
tuple1=[["banana","apple"],["chikku","vikku"]]
print(tuple1)

# Dictonary Attribute Or Key

dict1={"Name":"Chirag","Age":"20","canVote":"Yes"}
print(dict1)