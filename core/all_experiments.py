
from settings import TEST_CASES, SHIPS, PORTS, POSSIBLE_TESTS_CASES, STATISTICS_DISPLAYS, STATISTICS_TO_DO
from core.one_experiment import execute_one_experiment
from core.statistics import Statistics, DESCRIPTIONS
from core.modules import import_ship_class, import_port_class

class MultiexperimentsStatistics(Statistics):
    statistics_to_save=[]

    def add_statistics(self, experiment, one_test=[1,1,1]):
        for itr in range(len(STATISTICS_TO_DO)):
            stats_to_do=STATISTICS_TO_DO[itr]
            value = self.calculate_one_statistics(experiment, stats_to_do)
            self.statistics_to_save[itr][one_test[0]-1][one_test[1]-1]=value
        return True

    def prepare_statistics(self, test_case=[[0,0,0],[1,1,0]]):
        ships_range = 1
        ports_range = 1
        for case in test_case:
            if ships_range < case[1]:
                ships_range = case[1]
            if ports_range < case[0]:
                ports_range = case[0]
        base = [[["" for dim1 in range(ships_range)]
            for dim2 in range(ports_range)]
            for dim3 in range(len(STATISTICS_TO_DO))
            ]
        self.statistics_to_save = base
        return base

    def round_value(self, value):
        decimals = 0.0001
        while decimals < abs(value):
            decimals *= 10
        decimals /= 10000 #here is approximation
        new_value = round(value/decimals)
        return new_value*decimals

    def print_one_table(self, table):
        port_range = len(table)
        ship_range = len(table[0])
        text = "| P\\S |"
        for itrS in range(ship_range):
            ship_class = import_ship_class(itrS+1)
            ship_instance = ship_class()
            text += " "+ship_instance.read_table_description()+" |"
        text += "\n|----|"
        for itrS in range(ship_range):
            text += "----|"
        for itrP in range(port_range):
            for itrS in range(ship_range+1):
                if itrS==0:
                    port_class = import_port_class(itrP+1)
                    port_instance = port_class()
                    text += "\n| "+port_instance.read_table_description()+" |"
                else:
                    value = table[itrP][itrS-1]
                    text += " "+str(self.round_value(value))+" |"
        print(text+"\n")

    def print_tables(self):
        for itr in range(len(STATISTICS_TO_DO)):
            stats_key = STATISTICS_TO_DO[itr]
            stats_name = DESCRIPTIONS[stats_key][2]
            table_to_print = self.statistics_to_save[itr]
            print("\n"+str(stats_name)+"\n")
            self.print_one_table(table_to_print)


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
    for itr in range(len(all_tests)):
        test_case = test_list.list_of_test[itr]
        stats = MultiexperimentsStatistics()
        stats.prepare_statistics(test_case)
        if test_case == []:
            continue
        print("======\nTEST CASE "+str(itr+1)+"\n======")
        for test in test_case:
            experiment = execute_one_experiment(
                port_class_number=test[0],
                ship_class_number=test[1],
                test_case=test[2],
                do_stats=STATISTICS_DISPLAYS["show statistics for experiments"])
            if STATISTICS_DISPLAYS["show markdown tables"]:
                stats.add_statistics(experiment, test)
        if STATISTICS_DISPLAYS["show markdown tables"]:
            stats.print_tables()
    return all_tests