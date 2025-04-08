s1 = {2,5,8,7}
s2 = {6,2,3}

# s1.update(s2)
# print(s1,s2)
# print(s1.intersection(s2))
# print(s1.union(s2))

# s3 = s1.symmetric_difference(s2)
# print(s3)

# s1.symmetric_difference_update(s2)
# print(s1)

# s4 =s2.difference(s1)
# print(s4)

s1.difference_update(s2)
print(s1)

# Some Operation For Sets-->

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Youtube"}
# .isdisjoint() Check If All Element Are Not Common If Any One Element Is Common In Both Set Then It Return False Either True
print(cities.isdisjoint(cities2)) 

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Tokyo"}
# .issuperset
print(cities.issuperset(cities2))
cities3 = {"Berlin", "Delhi", "Madrid"}
print(cities.issuperset(cities3))

print(cities3.issubset(cities))

cities.add("Chirag")
print(cities)

cities.remove("Chirag")
print(cities)

# The main difference between remove and discard is that,
#  if we try to delete an item which is not present in set, 
# then remove() raises an error, whereas discard() does not raise any error.
cities.discard("Delhei")
print(cities)

# This method removes the last item of the set but the catch is that
#  we don’t know which item gets popped as sets are unordered.
#  However, you can access the popped item if you assign the pop() method to a variable.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# This method clears all items in the set and prints an empty set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

# del is not a method, rather it is a keyword which deletes the set entirely.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)