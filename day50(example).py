with open("day50.txt","r") as f:
    print(f.read(10))
    # print(f.seek())
    print(f.tell())
    f.seek(10)
    print(f.tell())
    print(f.read(2))


# double=lambda x: x*x
# print(double(4))

# a = [1,2,3,4]
# print(list(map(double,a)))