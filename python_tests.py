"""
print("test: how // and % works")
for itr in range(-10,10):
    print(str(itr)+" => "+str(itr//2)+" r "+str(itr%2))
"""

"""
print("basic test if find_distance works")
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
print("more complex test how find_distance works")
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