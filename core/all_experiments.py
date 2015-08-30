
from settings import TEST_CASES, SHIPS, PORTS, POSSIBLE_TESTS_CASES, STATISTICS_DISPLAYS
from core.one_experiment import execute_one_experiment
from core.statistics import Statistics, DESCRIPTIONS, MultiexperimentsStatistics, BestStatistics


class TestsList():
    list_of_test = []

    def check_correctness(self, case_list):
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

    def translate_integers(self, simple_order):
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

    def explain_list(self, list_to_explain):
        result = []
        translated = self.translate_integers(list_to_explain)
        for port_class_number in translated[0]:
            for ship_class_number in translated[1]:
                for test_case_number in translated[2]:
                    case_list = [port_class_number, ship_class_number, test_case_number]
                    if self.check_correctness(case_list):
                        result.append(case_list)
        return result

    def create_list_of_tests(self):
        list_of_test = []
        # create empty lists, one for each test case type
        for itr in range(POSSIBLE_TESTS_CASES):
            list_of_test.append([])
        # fill in the lists with TEST_CASES orders
        for order in TEST_CASES:
            explained = self.explain_list(order)
            for simple_order in explained:
                test_case_index = simple_order[2]-1
                if not (simple_order in list_of_test[test_case_index]):
                    list_of_test[test_case_index].append(simple_order)
        # sort created lists of orders
        for itr in range(len(list_of_test)):
            list_of_test[itr].sort()
        # return result
        self.list_of_test = list_of_test
        return self.list_of_test

def execute_all():
    STATISTICS_DISPLAYS["help text"]=False
    test_list=TestsList()
    all_tests=test_list.create_list_of_tests()
    stats = MultiexperimentsStatistics()
    optimization = BestStatistics()
    for itr in range(len(all_tests)):
        test_case = test_list.list_of_test[itr]
        stats.prepare_statistics(test_case)
        optimization.prepare_statistics()
        if test_case == []:
            continue
        print("======\nTEST CASE "+str(itr+1)+"\n======")
        for test in test_case:
            experiment = execute_one_experiment(
                port_class_number=test[0],
                ship_class_number=test[1],
                test_case=test[2],
                do_stats=STATISTICS_DISPLAYS["show statistics for experiments"])
            stats.add_statistics(experiment, test)
            optimization.add_best_statistics(experiment, test)
        stats.print_tables()
        optimization.print_best_results()
        optimization.print_table()
    return all_tests