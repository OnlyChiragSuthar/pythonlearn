# a  = input("Enter Any Number:")
# print(f"The Table Of {a} is:")
# try:
#     for i in range(1,11):
#         print(f"{int(a)}*{i} = {int(a)*i}")
    
# except:
#     print('Invalid Literals')

# print("SuccessFully Executed!")
# print('End Of Code')

# try:
#     num = int(input("Enter an integer: "))
#     a = [6,4]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
# except IndexError:
#     print("Index Invalid")
# except SyntaxError:
#     print()

# It Used For Program Begin Not Held!

try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError: 
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")
