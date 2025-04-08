# --> MAP

def cube(n):
    return n*n*n

a = [1,2,3,4]
new_a = list(map(cube,a))
new_a = list(map(lambda x:x**3,a))
# new_a = [cube(i) for i in a]
# new_a = []
# for i in a:
    # new_a.append(cube(i))
print(new_a)

# --> FILTER

def positive(n):
    return n>0

new = list(filter(positive,a))
print(new)


# REDUCE-->
from functools import reduce

numbers = [1,2,3,4,5]

sum = reduce(lambda x,y:x*y,numbers)
print(sum)