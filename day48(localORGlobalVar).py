''' x = 10 # global variable
def my_function():
  global y,x
  x = 9
  y = 5 # local variable
  print(y)

my_function()
print(x)
print(y) # this will cause an error because y is a local variable and is not accessible outside of the function     

'''

def change():
    global n
    n = int(input("Which Digit It Will BE:"))
    print(f"The Digit In Function {n}")
    



n = int(input(":"))
print(f"Value Of A At Starting {n}")
change()
print(f"Value Of A At ending {n}")