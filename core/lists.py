def find_first(element,list):
    for itr in range(list):
        if element == list[itr]:
            return itr
    return -1 #if none of elements

def delete_elements_from_list(elements, list):
	for itr in range(list):
		if list[range(list)-itr] in elements:
			del list[range(list)-itr]
	return list
