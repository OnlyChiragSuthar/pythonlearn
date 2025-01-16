# in Today Session we study about String slicing where we split output accroding to ourself 

fruit = "Mango"
print(fruit);
print(fruit[0:5]) # in This Line You can Notice That I Insert 6 instead of 5 because the python print end word with n-1 (6-1=5)
print(fruit[0:])
print(fruit[:5])
print(fruit[:])
print(fruit[:len(fruit)])

# if i want To Print Only Ang in Mango

print(fruit[1:4])
print(fruit[:-3]) 
print(fruit[:len(fruit)-3])  # both Are The Same Because Python Understand It 
print(fruit[-1:-3])
t="harry"
print(t[-4:-2])
