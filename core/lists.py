def find_first(element,list):
    for itr in range(len(list)):
        if element == list[itr]:
            return itr
    return -1 #if none of elements

def delete_elements_from_list(elements, list):
    numbers = []
    for itr in range(len(list)):
        if list[itr] in elements:
            numbers.append(itr)
    numbers.reverse()
    for num in numbers:
        del list[num]
    return list
