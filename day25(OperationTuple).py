tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(311)
# res = tuple1.index(3, 4, 8)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)

tup1 = (10,20,30,40)
tup2 = ("harry","Chirag","Vikram")

lis1 = list(tup1)
lis2 = list(tup2)

lis1.insert(1,50)
lis1.append(6)
lis1.remove(30)

lis1.extend(lis2)

tup1 = tuple(lis1)
print(tup1)
print(type(tup1))