info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

ep1 = {
    22 : "Chirag",
    "DOB":"Sept"
}

ep2 = {
    "DOB":"Oct"
}
# ep1.update(ep2)
# ep1.clear()   #.clear() Will Remove all Datafrom  The dict.
# ep1.pop(22)   #.pop() Will pop User based data From The Dictionary
# ep1.popitem()   #.popitem() will pop last dict item from The Dictionary 
del ep1['DOB']
# del ep1
print(ep1)