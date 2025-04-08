for i in range(1,6):
    print(i)

else:
    print('Sorry')

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
    if(x==3):
        break
else:
    print ("else block in loop")
print ("Out of loop")