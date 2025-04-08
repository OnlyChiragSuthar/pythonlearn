dict = {
    "Name":"Chirag",
    "Country":"India"
}

print(dict)
print(dict["Country"])

# dic1 = {
#     344 : "Chirag",
#     26 : "Chirag",
#     3 : "Akshay",
#     10 : "Vijay"
# }

# roll = int(input("Enter Roll No:"))
# print(dic1[roll])

print(dict.get('Name'))

print(dict.keys())
print(dict.values())

for key in dict.keys():
    print(dict.get(key))

print((dict.items()))

for key,value in dict.items():
    print(f"For Key {key}, Value Is {value}")