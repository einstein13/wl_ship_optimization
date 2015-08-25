# unit tests for lists.py
ERROR = "\tERR: core.lists: "
BEGIN_TEXT = "core.lists."
END_TEXT =  " TESTS FINISHED"

from core.lists import find_first, delete_elements_from_list, get_nested_elements, find_new_elements

def all_tests():
	test_find_first()
	test_delete_elements_from_list()
	test_get_nested_elements()
	test_find_new_elements()