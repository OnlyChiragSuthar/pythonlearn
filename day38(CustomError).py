a = int(input("Enter Any Numberr Between 5 To 10:"))

if(a<5 or a>10):
    raise ValueError("Value Should Be Under 5 To 10")

# define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Invalid Age")