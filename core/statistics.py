from settings import STATISTICS_TO_DO, STATISTICS_DISPLAYS, STATISTICS_TO_OPTIMIZE

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
        wares_list = experiment.wares_list
        variable = wares_list[0].read_route_length()
        for ware in wares_list:
            tmp_variable = ware.read_route_length()
            if tmp_variable < variable:
                variable = tmp_variable
        return variable

    def get_statistics_mean_distance_for_wares(self, experiment):
        wares_list = experiment.wares_list
        variable = 0
        for ware in wares_list:
            variable += ware.read_route_length()
        return 1.0*variable/len(wares_list)

    def get_statistics_max_distance_for_wares(self, experiment):
        wares_list = experiment.wares_list
        variable = wares_list[0].read_route_length()
        for ware in wares_list:
            tmp_variable = ware.read_route_length()
            if tmp_variable > variable:
                variable = tmp_variable
        return variable

    def get_statistics_min_time_for_wares(self, experiment):
        wares_list = experiment.wares_list
        variable = wares_list[0].read_time_existence()
        for ware in wares_list:
            tmp_variable = ware.read_time_existence()
            if tmp_variable < variable:
                variable = tmp_variable
        return variable

    def get_statistics_mean_time_for_wares(self, experiment):
        wares_list = experiment.wares_list
        variable = 0
        for ware in wares_list:
            variable += ware.read_time_existence()
        return 1.0*variable/len(wares_list)

    def get_statistics_max_time_for_wares(self, experiment):
        wares_list = experiment.wares_list
        variable = wares_list[0].read_time_existence()
        for ware in wares_list:
            tmp_variable = ware.read_time_existence()
            if tmp_variable > variable:
                variable = tmp_variable
        return variable

    def get_statistics_max_efficiency_wares(self, experiment):
        wares_list = experiment.wares_list
        variable = wares_list[0].calculate_route_efficiency()
        for ware in wares_list:
            tmp_variable = ware.calculate_route_efficiency()
            if tmp_variable < variable:
                variable = tmp_variable
        return variable

    def get_statistics_mean_efficiency_wares(self, experiment):
        wares_list = experiment.wares_list
        variable = 0
        for ware in wares_list:
            variable += ware.calculate_route_efficiency()
        return variable/len(wares_list)

    def get_statistics_min_efficiency_wares(self, experiment):
        wares_list = experiment.wares_list
        variable = wares_list[0].calculate_route_efficiency()
        for ware in wares_list:
            tmp_variable = ware.calculate_route_efficiency()
            if tmp_variable > variable:
                variable = tmp_variable
        return variable

    def get_statistics_max_time_waiting_wares(self, experiment):
        wares_list = experiment.wares_list
        variable = wares_list[0].calculate_total_time_waiting()
        for ware in wares_list:
            tmp_variable = ware.calculate_total_time_waiting()
            if tmp_variable > variable:
                variable = tmp_variable
        return variable

    def get_statistics_mean_time_waiting_wares(self, experiment):
        wares_list = experiment.wares_list
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
        wares_list = experiment.wares_list
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

    def print_classes_descriptions(self, experiment):
        port_class=experiment.ports_list[0]
        ship_class=experiment.ships_list[0]
        text = "\nPORTS:\n"
        text += port_class.read_short_description()
        text += "\nSHIPS:\n"
        text += ship_class.read_short_description()
        print(text)
        return 0

    def print_statistics(self, experiment):
        self.print_classes_descriptions(experiment)
        text = "------\n"
        for key in KEYS:
            text += self.get_one_statistics(experiment, key)
        print(text)
        return 0

