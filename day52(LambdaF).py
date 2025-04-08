# def double(x):
#     return x*2

# or

double = lambda x: x*2
check = lambda x,y: print(x) if(x>y) else print(y)
cube = lambda x: x*x*x

def appl(fx,value):
    return 10 + fx(value)

# print(double(5))
check(25,15)
print(appl(cube,2)) 