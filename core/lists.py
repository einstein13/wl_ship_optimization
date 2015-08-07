def find_first(element,list):
    for itr in range(len(list)):
        if element == list[itr]:
            return itr
    return -1 #if none of elements

def delete_elements_from_list(elements, list):
    for itr in range(len(list)):
        if list[len(list)-itr-1] in elements:
            del list[len(list)-itr-1]
    return list
