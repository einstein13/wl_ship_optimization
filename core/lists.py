
def find_first(element,list):
    for itr in range(list):
        if element == list[itr]:
            return itr
    return -1 #if none of elements