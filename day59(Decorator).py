def greet(fx):
    print("HelloMorning")

@greet
def hello():
    print("Hii")

def add(a,b):
    print(a+b)

greet(hello)()
