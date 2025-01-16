# *****
# *****
# *****
# *****
# *****

# raw = int(input("Enter The Number Of Raw:"))

# for x in range(1,raw+1):
#     print("*"*5,end="")
#     print("\n")

for x in range(1,6):
    for y in range(1,6):
        print("*",end="")
    print("\n")

# *
# **
# ***
# ****
# *****


for x in range(1,6):
    for y in range(1,x+1):
        print("*",end="")
    print()

# *****
# ****
# ***
# **
# *
print("\n")

for x in range(5,0,-1):
    for y in range(1,x+1):
        print("*",end="")
    print()