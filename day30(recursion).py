def Factorial(n):
    if (n==0):
        return 1
    elif (n==1):
        return 1
    else:
        return n*Factorial(n-1)

def Fibonacci(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

Fact = Factorial(4)
print(Fact)

fib = Fibonacci(4)
print(fib)