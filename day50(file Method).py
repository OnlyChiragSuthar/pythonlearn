# --> Merged With myline.txt

# f = open("myline.txt", 'a')
# text = f.read()
# f.write("Hii Buddy Python Couse Is Great")
# print()
# f.close()

# f = open("myline.txt","r")
# i = 0
# while True:

#     line = f.readline()
#     if not line:
#         break

#     m1 =line.split(",")[0]
#     m2 =line.split(",")[1]
#     m3 =line.split(",")[2]
    
#     print(f"Student {i} Marks In Math Is {m1}")
#     print(f"Student {i} Marks In SST Is {m2}")
#     print(f"Student {i} Marks In Drawing Is {m3}")
#     print(line)
#     i = i+1

# --> .readlines() read all lines and make them in list
f = open("myline.txt","r")
line = f.readlines()
print(line[0][0:2].strip())
# print(line)

# --> .writeline() for write context or overwrite
f = open('myline2.txt','w')
lines = ["line1\n","line2\n","line3\n"]
f.writelines(lines)


# -->writeline() at a specific location 
with open("myline2.txt", "r") as f:
    lines = f.readlines()
lines.insert(2 - 1, "New Line Bolte\n") 
f = open('myline2.txt','w')

# lines = ["line1\n","line2\n","line3\n"]
f.writelines(lines)

