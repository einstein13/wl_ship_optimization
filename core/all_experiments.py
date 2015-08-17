
from settings import TEST_CASES, SHIPS, PORTS, POSSIBLE_TESTS_CASES, STATISTICS_DISPLAYS
from core.one_experiment import execute_one_experiment

def check_correctness(case_list):
    # port class
    if case_list[0] > len(PORTS):
        return False
    # ship class
    if case_list[1] > len(SHIPS):
        return False
    # test case
    if case_list[2] > POSSIBLE_TESTS_CASES:
        return False
    return True

def translate_integers(simple_order):
    result = []
    for itr in range(3):
        if type(simple_order[itr]) == list:
            result.append(simple_order[itr])
        elif simple_order[itr] == -1:
            if itr == 0:
                result.append(range(1,len(PORTS)+1))
            elif itr == 1:
                result.append(range(1,len(SHIPS)+1))
            elif itr == 2:
                result.append(range(1,POSSIBLE_TESTS_CASES+1))
        else:
            result.append([simple_order[itr]])
    return result

def explain_list(list_to_explain):
    result = []
    translated = translate_integers(list_to_explain)
    for port_class_number in translated[0]:
        for ship_class_number in translated[1]:
            for test_case_number in translated[2]:
                case_list = [port_class_number, ship_class_number, test_case_number]
                if check_correctness(case_list):
                    result.append(case_list)
    return result


def create_list_of_tests():
    list_of_test = []
    # create empty lists, one for each test case type
    for itr in range(POSSIBLE_TESTS_CASES):
        list_of_test.append([])
    # fill in the lists with TEST_CASES orders
    for order in TEST_CASES:
        explained = explain_list(order)
        for simple_order in explained:
            test_case_index = simple_order[2]-1
            if not (simple_order in list_of_test[test_case_index]):
                list_of_test[test_case_index].append(simple_order)
    # sort created lists of orders
    for itr in range(len(list_of_test)):
        list_of_test[itr].sort()
    # return result
    return list_of_test

def execute_all():
    STATISTICS_DISPLAYS["help text"]=False
    all_tests = create_list_of_tests()
    for itr in range(len(all_tests)):
        test_case = all_tests[itr]
        if test_case == []:
            continue
        print("======\nTEST CASE "+str(itr+1)+"\n======")
        for test in test_case:
            execute_one_experiment(
                port_class_number=test[0],
                ship_class_number=test[1],
                test_case=test[2],
                do_stats=True)
    return all_tests