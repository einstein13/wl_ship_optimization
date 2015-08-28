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

def get_nested_elements(list, nested_index=0):
    result = []
    for element in list:
        result.append(element[nested_index])
    return result

def find_new_elements(old_list, new_list):
    result=[]
    for element in new_list:
        if not element in old_list:
            result.append(element)
    return result

def debug_list(list_to_debug):
    result = "[ "
    for element in list_to_debug:
        result += element.debug()+" "
    result += "]"
    return result

def debug_list_all(list_to_debug):
    result = "[ "
    for element in list_to_debug:
        result += element.debug_all()+" "
    result += "]"
    return result