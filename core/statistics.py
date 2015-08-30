from settings import STATISTICS_TO_DO, STATISTICS_DISPLAYS, STATISTICS_TO_OPTIMIZE
from core.modules import import_ship_class, import_port_class

# DESCRIPTIONS dictionary describes all text used by Statistics class
# name : [
#   long_description (separate lines),
#   short_description (inline),
#   help_text
#   ]
DESCRIPTIONS = {
    "general: total simulation time" : ["Total time: ", "tot_tim: ", "Game time when last ware reach destination"],
    "ships: mean utilization" : ["Mean utilization: ", "mean_util: ", "Mean ship utilization (how many wares are onboard)"],
    "ships: max utilization" : ["Max utilization: ", "max_util: ", "Maximum ship utilization (how many wares are onboard)"],
    "ports: mean wares waiting" : ["Mean wares waiting: ", "mean_wait: ", "Mean number of wares waiting in ports"],
    "ports: max wares waiting" : ["Max wares waiting: ", "max_wait: ", "Maximum number of wares waiting in ports"],
    "wares: min distance of journey" : ["Min journey distance: ", "min_dist: ", "Minimum length of journey for any ware"],
    "wares: mean distance of journey" : ["Mean journey distance: ", "mean_dist: ", "Mean length of journey for any ware"],
    "wares: max distance of journey" : ["Max journey distance: ", "max_dist: ", "Maximum length of journey for any ware"],
    "wares: min time of existence" : ["Min existence time: ", "min_tim: ", "Minimum time of existence for any ware (start at port, end at destination)"],
    "wares: mean time of existence" : ["Mean existence time: ", "mean_tim: ", "Mean time of existence for any ware (start at port, end at destination)"],
    "wares: max time of existence" : ["Max existence time: ", "max_tim: ", "Maximum time of existence for any ware  (start at port, end at destination)"],
    "wares: min journey efficiency" : ["Min journey efficiency: ", "min_eff: ", "Minimum value of efficiency (length_journey/minimum_possible_length) for any ware"],
    "wares: mean journey efficiency" : ["Mean journey efficiency: ", "mean_eff: ", "Mean value of efficiency (length_journey/minimum_possible_length) for any ware"],
    "wares: max journey efficiency" : ["Max journey efficiency: ", "max_eff: ", "Maximum value of efficiency (length_journey/minimum_possible_length) for any ware"],
    "wares: max time waiting" : ["Max time waiting: ", "max_wait: ", "Maximum time waiting for ware in port to take by a ship"],
    "wares: mean time waiting" : ["Mean time waiting: ", "mean_wait: ", "Mean time waiting for ware in port to take by a ship"],
    "wares: min time waiting" : ["Min time waiting: ", "min_wait: ", "Minimum time waiting for ware in port to take by a ship"],
    }

KEYS = [
    "general: total simulation time",
    "ships: mean utilization",
    "ships: max utilization",
    "ports: mean wares waiting",
    "ports: max wares waiting",
    "wares: min distance of journey",
    "wares: mean distance of journey",
    "wares: max distance of journey",
    "wares: min time of existence",
    "wares: mean time of existence",
    "wares: max time of existence",
    "wares: max journey efficiency",
    "wares: mean journey efficiency",
    "wares: min journey efficiency",
    "wares: max time waiting",
    "wares: mean time waiting",
    "wares: min time waiting"
    ]

class Statistics():
    value_to_remember = -1

    def __init__(self):
        self.value_to_remember = -1
        self.print_help_text()
        return None

    def read_descritpion(self, statistics_type):
        if STATISTICS_DISPLAYS["separate lines"]:
            return DESCRIPTIONS[statistics_type][0]
        return DESCRIPTIONS[statistics_type][1]

    def read_help_text(self, statistics_type):
        return DESCRIPTIONS[statistics_type][2]

    def print_help_text(self):
        if STATISTICS_DISPLAYS["help text"]:
            for statistics_type in STATISTICS_TO_DO:
                text = "\"" + statistics_type
                text += "\"/\""
                text += self.read_descritpion(statistics_type)
                text += "\" : "
                text += self.read_help_text(statistics_type)
                print(text)
        return 0

    def get_statistics_total_simulation_time(self, experiment):
        return experiment.get_current_time()

    def get_statistics_mean_utilization(self, experiment):
        return experiment.read_mean_ships_utilization()

    def get_statistics_max_utilization(self, experiment):
        return experiment.read_max_wares_taken_ship()

    def get_statistics_mean_wares_waiting(self, experiment):
        return experiment.read_mean_wares_waiting_in_port()

    def get_statistics_max_wares_waiting(self, experiment):
        return experiment.read_max_wares_waiting_port()

    def get_statistics_min_distance_for_wares(self, experiment):
        wares_list = experiment.wares
        variable = wares_list[0].read_route_length()
        for ware in wares_list:
            tmp_variable = ware.read_route_length()
            if tmp_variable < variable:
                variable = tmp_variable
        return variable

    def get_statistics_mean_distance_for_wares(self, experiment):
        wares_list = experiment.wares
        variable = 0
        for ware in wares_list:
            variable += ware.read_route_length()
        return 1.0*variable/len(wares_list)

    def get_statistics_max_distance_for_wares(self, experiment):
        wares_list = experiment.wares
        variable = wares_list[0].read_route_length()
        for ware in wares_list:
            tmp_variable = ware.read_route_length()
            if tmp_variable > variable:
                variable = tmp_variable
        return variable

    def get_statistics_min_time_for_wares(self, experiment):
        wares_list = experiment.wares
        variable = wares_list[0].read_time_existence()
        for ware in wares_list:
            tmp_variable = ware.read_time_existence()
            if tmp_variable < variable:
                variable = tmp_variable
        return variable

    def get_statistics_mean_time_for_wares(self, experiment):
        wares_list = experiment.wares
        variable = 0
        for ware in wares_list:
            variable += ware.read_time_existence()
        return 1.0*variable/len(wares_list)

    def get_statistics_max_time_for_wares(self, experiment):
        wares_list = experiment.wares
        variable = wares_list[0].read_time_existence()
        for ware in wares_list:
            tmp_variable = ware.read_time_existence()
            if tmp_variable > variable:
                variable = tmp_variable
        return variable

    def get_statistics_max_efficiency_wares(self, experiment):
        wares_list = experiment.wares
        variable = wares_list[0].calculate_route_efficiency()
        for ware in wares_list:
            tmp_variable = ware.calculate_route_efficiency()
            if tmp_variable < variable:
                variable = tmp_variable
        return variable

    def get_statistics_mean_efficiency_wares(self, experiment):
        wares_list = experiment.wares
        variable = 0
        for ware in wares_list:
            variable += ware.calculate_route_efficiency()
        return variable/len(wares_list)

    def get_statistics_min_efficiency_wares(self, experiment):
        wares_list = experiment.wares
        variable = wares_list[0].calculate_route_efficiency()
        for ware in wares_list:
            tmp_variable = ware.calculate_route_efficiency()
            if tmp_variable > variable:
                variable = tmp_variable
        return variable

    def get_statistics_max_time_waiting_wares(self, experiment):
        wares_list = experiment.wares
        variable = wares_list[0].calculate_total_time_waiting()
        for ware in wares_list:
            tmp_variable = ware.calculate_total_time_waiting()
            if tmp_variable > variable:
                variable = tmp_variable
        return variable

    def get_statistics_mean_time_waiting_wares(self, experiment):
        wares_list = experiment.wares
        variable = 0
        total_wares = len(wares_list)
        for ware in wares_list:
            tmp_variable = ware.calculate_total_time_waiting()
            if tmp_variable == -1: # add only valid records
                total_wares -= 1
                continue
            variable += tmp_variable
        return 1.0*variable/total_wares

    def get_statistics_min_time_waiting_wares(self, experiment):
        wares_list = experiment.wares
        variable = wares_list[0].calculate_total_time_waiting()
        for ware in wares_list:
            tmp_variable = ware.calculate_total_time_waiting()
            if tmp_variable<variable and tmp_variable!=-1:
                variable = tmp_variable
        return variable

    def calculate_one_statistics(self, experiment, statistics_type):
        if statistics_type == KEYS[0]:
            return self.get_statistics_total_simulation_time(experiment)
        elif statistics_type == KEYS[1]:
            return self.get_statistics_mean_utilization(experiment)
        elif statistics_type == KEYS[2]:
            return self.get_statistics_max_utilization(experiment)
        elif statistics_type == KEYS[3]:
            return self.get_statistics_mean_wares_waiting(experiment)
        elif statistics_type == KEYS[4]:
            return self.get_statistics_max_wares_waiting(experiment)
        elif statistics_type == KEYS[5]:
            return self.get_statistics_min_distance_for_wares(experiment)
        elif statistics_type == KEYS[6]:
            return self.get_statistics_mean_distance_for_wares(experiment)
        elif statistics_type == KEYS[7]:
            return self.get_statistics_max_distance_for_wares(experiment)
        elif statistics_type == KEYS[8]:
            return self.get_statistics_min_time_for_wares(experiment)
        elif statistics_type == KEYS[9]:
            return self.get_statistics_mean_time_for_wares(experiment)
        elif statistics_type == KEYS[10]:
            return self.get_statistics_max_time_for_wares(experiment)
        elif statistics_type == KEYS[11]:
            return self.get_statistics_max_efficiency_wares(experiment)
        elif statistics_type == KEYS[12]:
            return self.get_statistics_mean_efficiency_wares(experiment)
        elif statistics_type == KEYS[13]:
            return self.get_statistics_min_efficiency_wares(experiment)
        elif statistics_type == KEYS[14]:
            return self.get_statistics_max_time_waiting_wares(experiment)
        elif statistics_type == KEYS[15]:
            return self.get_statistics_mean_time_waiting_wares(experiment)
        elif statistics_type == KEYS[16]:
            return self.get_statistics_min_time_waiting_wares(experiment)
        return None

    def get_one_statistics(self, experiment, statistics_type):
        if statistics_type in STATISTICS_TO_DO:
            # basic information
            text_to_return = self.read_descritpion(statistics_type)
            text_to_return += str(self.calculate_one_statistics(experiment, statistics_type))
            # end of information
            if STATISTICS_DISPLAYS["separate lines"]:
                text_to_return += "\n"
            else:
                text_to_return += "; "
            return text_to_return
        return ""

    def get_class_description(self, instance):
        if STATISTICS_DISPLAYS["short class descriptions"]:
            return instance.read_short_description()
        return instance.read_full_description()

    def print_classes_descriptions(self, experiment):
        port_class=experiment.ports_list[0]
        ship_class=experiment.ships_list[0]
        text = "\nPORTS:\n"
        text += self.get_class_description(port_class)
        text += "\nSHIPS:\n"
        text += self.get_class_description(ship_class)
        print(text)
        return 0

    def print_statistics(self, experiment):
        self.print_classes_descriptions(experiment)
        text = "------\n"
        for key in KEYS:
            text += self.get_one_statistics(experiment, key)
        print(text)
        return 0

class MultiexperimentsStatistics(Statistics):
    statistics_to_save=[]

    def add_statistics(self, experiment, one_test=[1,1,1]):
        if not STATISTICS_DISPLAYS["show markdown tables"]:
            return False
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
        if value=="":
            return " - "
        if type(value) is int:
            return value
        decimals = 0.0001
        while decimals < abs(value):
            decimals *= 10
        decimals /= 10000 #here is approximation
        new_value = round(value/decimals)
        return new_value*decimals

    def get_port_table_description(self, number):
        port_class = import_port_class(number)
        port_instance = port_class()
        return port_instance.read_table_description()

    def get_ship_table_description(self, number):
        ship_class = import_ship_class(number)
        ship_instance = ship_class()
        return ship_instance.read_table_description()

    def print_one_table(self, table):
        port_range = len(table)
        ship_range = len(table[0])
        text = "| P\\S |"
        for itrS in range(ship_range):
            text += " "
            text += self.get_ship_table_description(itrS+1)
            text += " |"
        text += "\n|----|"
        for itrS in range(ship_range):
            text += "----|"
        for itrP in range(port_range):
            for itrS in range(ship_range+1):
                if itrS==0:
                    text += "\n| "
                    text += self.get_port_table_description(itrP+1)
                    text += " |"
                else:
                    value = table[itrP][itrS-1]
                    text += " "+str(self.round_value(value))+" |"
        print(text+"\n")

    def print_tables(self):
        if not STATISTICS_DISPLAYS["show markdown tables"]:
            return False
        for itr in range(len(STATISTICS_TO_DO)):
            stats_key = STATISTICS_TO_DO[itr]
            stats_name = DESCRIPTIONS[stats_key][2]
            table_to_print = self.statistics_to_save[itr]
            print("\n"+str(stats_name)+"\n")
            self.print_one_table(table_to_print)
        return True

class BestStatistics(MultiexperimentsStatistics):
    statistics_to_save=[]

    def get_port_full_description(self, number):
        port_class = import_port_class(number)
        port_instance = port_class()
        return self.get_class_description(port_instance)

    def get_ship_full_description(self, number):
        ship_class = import_ship_class(number)
        ship_instance = ship_class()
        return self.get_class_description(ship_instance)

    def add_best_statistics(self, experiment, one_test):
        if not STATISTICS_DISPLAYS["get optimized statistics"]:
            return False
        value = self.calculate_one_statistics(experiment, STATISTICS_TO_OPTIMIZE)
        self.statistics_to_save.append([value, one_test[0], one_test[1]])
        return True

    def print_best_results(self):
        if not STATISTICS_DISPLAYS["get optimized statistics"]:
            return False
        self.statistics_to_save.sort()
        text = "\nSTATISTICS OPTIMIZATION\n"
        text += "Optimized with: \""+STATISTICS_TO_OPTIMIZE+"\"\n"
        text += "Best results:\nPort: "
        best_stats = self.statistics_to_save[0]
        text += self.get_port_full_description(best_stats[1])
        text += "\nShip: "
        text += self.get_ship_full_description(best_stats[2])
        text += "\n"
        text += "Best value: "
        text += str(self.round_value(best_stats[0]))
        print text
        return True

    def print_table(self):
        if not STATISTICS_DISPLAYS["get optimized statistics"]:
            return False
        self.statistics_to_save.sort()
        text = "\nAll results in table:\n\n"
        text += "| Value | Port class | Ship class |\n"
        text += "|----|----|----|\n"
        old_value = self.statistics_to_save[0][0]*2+1
        for score in self.statistics_to_save:
            rounded =self.round_value(score[0])
            if rounded != old_value:
                text += "| "+str(score[0])+" | "
            else:
                text += "| `` | "
            text += self.get_port_table_description(score[1])
            text += " | "
            text += self.get_ship_table_description(score[2])
            text += " |\n"
            old_value = rounded
        print text
        return True