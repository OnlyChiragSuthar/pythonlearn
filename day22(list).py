marks = [45,50,33,5,6,7,8,9,0,33]
print(marks)
print(type(marks))

print(marks[0])
print(marks[:3])

list = ["Blue","Green"]
print(list)

if "Red" in list:
    print("Yes")

else:
    print("No")

con = 0
for x in list:
    if(x=="Red"):
        con= con + 1
    else:
        pass
    
if(con>0):
    print("yes")

else:
    print("No")

l = (1,2,3,"6")

if "6" in l:
    print("y")

else:
    print("N")

list_comprehension = [i for i in range(1,10)]
print(list_comprehension)