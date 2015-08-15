import random
from core import test_cases
from settings import POSSIBLE_TESTS_CASES
from common.mains import ShipList, PortList, ListOfWares
from common.mains import SimulationTime, GlobalShipStatistics, GlobalPortStatistics
from common.classes import Description

class Experiment(ShipList,
        PortList,
        ListOfWares,
        SimulationTime,
        Description,
        GlobalShipStatistics,
        GlobalPortStatistics):
    
    def test1_definition(self, ship_class, port_class, ware_class):
        basic_distance = 25
        self.ports_list = test_cases.ports_test1(port_class, basic_distance)       
        self.ships_list = test_cases.ships_test1(ship_class, self.ports_list)
        self.wares_list = test_cases.wares_test1(ware_class, self.ports_list, basic_distance)
        return 0

    def test2_definition(self, ship_class, port_class, ware_class):
        basic_distance = 20
        self.ports_list = test_cases.ports_test2(port_class, basic_distance)       
        self.ships_list = test_cases.ships_test2(ship_class, self.ports_list)
        self.wares_list = test_cases.wares_test2(ware_class, self.ports_list, basic_distance)
        return 0

    def test3_definition(self, ship_class, port_class, ware_class):
        basic_distance = 20
        self.ports_list = test_cases.ports_test3(port_class, basic_distance)       
        self.ships_list = test_cases.ships_test3(ship_class, self.ports_list)
        self.wares_list = test_cases.wares_test3(ware_class, self.ports_list, basic_distance)
        return 0

    def test4_definition(self, ship_class, port_class, ware_class):
        basic_distance = 40
        self.ports_list = test_cases.ports_test4(port_class, basic_distance)       
        self.ships_list = test_cases.ships_test4(ship_class, self.ports_list)
        self.wares_list = test_cases.wares_test4(ware_class, self.ports_list, basic_distance)
        return 0

    def set_test_case(self, ship_class, port_class, ware_class, case_number=1):
        random.seed(1) # have the same basic situation for all tests
        if case_number > POSSIBLE_TESTS_CASES:
            print("ERROR: test case number is higher than implemented methods")
            return False
        if case_number==1:
            self.test1_definition(ship_class, port_class, ware_class)
            return True
        elif case_number==2:
            self.test2_definition(ship_class, port_class, ware_class)
            return True
        elif case_number==3:
            self.test3_definition(ship_class, port_class, ware_class)
            return True
        elif case_number==4:
            self.test4_definition(ship_class, port_class, ware_class)
            return True
        return False

    def update_global_statistics(self):
        self.update_global_ships_statistics(self.ships_list)
        self.update_global_ports_statistics(self.ports_list)
        return 0

    def work_on_docked_ships(self, current_time, all_ports):
        docked_ships = self.select_ships_by_state(0)
        for ship in docked_ships:
            port_where_ship = self.find_port_at_location(ship.read_coordinates())
            if port_where_ship == 0:
                print("ERROR: main: ship docked with no port destination")
                ship.start_ship(current_time, all_ports)
                continue #jump to another ship
            if len(port_where_ship.wares) == 0:
                #print("WARNING: no wares at port, nothing to load")
                ship.start_ship(current_time, all_ports)
                return 0
            #now we have both: port and ship
            other_ships_going_to_port = self.select_ships_going_to_port(port_where_ship)
            port_where_ship.load_wares_to_ship(ship, other_ships_going_to_port)
            ship.start_ship(current_time, all_ports)
        return 0

    def call_ships_to_ports(self, current_time):
        ports_calling = self.select_ports_calling()
        iddle_ships = self.select_ships_by_state(-1)
        if len(ports_calling)==0 or len(iddle_ships)==0:
            return 0
        for port in ports_calling:
            if len(iddle_ships)==0:
                break
            port.call_ships(iddle_ships, current_time)
            ships_going_to_port = self.select_ships_going_to_port(port)
            port.update_calling_ships(ships_going_to_port)
        return 0

    def put_new_wares_to_ports(self, current_time):
        new_wares = self.find_new_wares(current_time)
        for ware in new_wares:
            port = ware.start_ware_in_simulation()
            port.add_wares_to_list([ware])
            ships_going_to_port = self.select_ships_going_to_port(port)
            port.update_calling_ships(ships_going_to_port)
        return 0

    def dock_ships(self, current_time, all_ports):
        ships_docking = self.select_ships_docking(current_time)
        for ship in ships_docking:
            port = ship.read_next_destination()
            ship.stop_at_port(port, current_time, all_ports)
        return 0

    def simulation_step(self, current_time, all_ports):
        # this order makes docking ships stay STEP_TIME before leave to another port
        self.work_on_docked_ships(current_time, all_ports)
        self.call_ships_to_ports(current_time)
        self.put_new_wares_to_ports(current_time)
        self.dock_ships(current_time, all_ports)
        self.update_global_statistics()
        return 0

    def make_experiment(self, ware_class, port_class, ship_class, test_case=1):
        # ship and port classes are selected
        self.set_test_case(ship_class, port_class, ware_class, test_case)
        self.reset_timer()
        current_time=0
        while not self.all_wares_reached_destinations():
            current_time = self.get_current_time()
            self.simulation_step(current_time, self.ports_list)
            self.add_time_step()
        return True

