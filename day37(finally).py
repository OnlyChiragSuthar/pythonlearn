# try:
#     l = [1,2,3,4]
#     i = int(input("Enter Any Index:"))
#     print(l[i])

# except:
#     print("Some Error Occured")

# finally:
#     print("Execution Completed!")

def funct1():
    try:
        l = [1,2,3,4]
        i = int(input("Enter Any Index:"))
        print(l[i])
        return 1

    except IndexError:
        print("Some Error Occured")
        return 0

    finally:
        print("Execution Completed!")

x = funct1()
print(x)