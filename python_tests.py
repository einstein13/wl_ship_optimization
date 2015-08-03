"""
print("================================")
print("test: how // and % works")
print("================================")
for itr in range(-10,10):
    print(str(itr)+" => "+str(itr//2)+" r "+str(itr%2))
"""

"""
print("================================")
print("basic test if find_distance works")
print("================================")
from core.logic import find_distance

for itr1 in range(-5,5):
    made=""
    if itr1 % 2 == 1:
        made += "  "
    for itr2 in range(-5,5):
        made+=str(find_distance([0,0],[itr2,itr1]))+"   "
    print(made)
"""

"""
print("================================")
print("more complex test how find_distance works")
print("================================")
from core.logic import find_distance

for itp1 in range(-2,2):
    for itp2 in range(-2,2):
        for itr1 in range(-5,5):
            made=""
            if itr1 % 2 == 1:
                made += "  "
            for itr2 in range(-5,5):
                made+=str(find_distance([itp2,itp1],[itr2,-itr1]))+"   "
            print(made)
        print("")

for itr1 in range(-5,5):
    made=""
    if itr1 % 2 == 1:
        made += "       "
    for itr2 in range(-5,5):
        if itr2 >= 0:
            made+="( "+str(itr2)+","
        else:
            made+="("+str(itr2)+","
        if -itr1 >= 0:
            made+=" "+str(-itr1)+")"
        else:
            made+=str(-itr1)+")"
        made+="       "
    print(made)
print("")
"""

"""
print("================================")
print("let's try how deleting from the list works:")
print("================================")
class character():
    ch = ""
    def __init__(self, char=""):
        if char!="":
            self.ch=char
        return
    def set(self, char=""):
        if char!="":
            self.ch=char
        return char
    def __str__(self):
        return self.ch
    def __repr__(self):
        return self.ch
list1 = [character('a'),character('b'),character('c'),character('d'),character('e'),character('f'),character('g'),character('h'),character('i')]
list2 = []
list2.append(list1[4])
list2.append(list1[3])
list2.append(list1[7])
list2.append(list1[1])
list2.append(list1[0])
list2.append(list1[2])
print(list1)
print(list2)
print("")
list1[1].set('x')
list1[2].set('y')
list1[3].set('z')
print(list1)
print(list2)
print("")
del list2[1]
del list2[2]
del list2[3]
print(list1)
print(list2)
"""

