from settings import SHIPS, PORTS
from wares.ware import Ware
from core import test_cases
from common.mains import ShipList, PortList, ListOfWares, SimulationTime
from common.classes import Description

class experiment(ShipList, PortList, ListOfWares, SimulationTime, Description):
    
    def test1_definition(self, ship_class, port_class, ware_class):
        basic_distance = 25
        self.ports_list = test_cases.ports_test1(port_class, basic_distance)       
        self.ships_list = test_cases.ships_test1(ship_class, self.ports_list)
        self.wares_list = test_cases.wares_test1(ware_class, self.ports_list, basic_distance)
        return 0

    def work_on_docked_ships(self, current_time):
        docked_ships = self.select_ships_by_state(0)
        for ship in docked_ships:
            port_where_ship = self.find_port_at_location(ship.read_coordinates())
            if port_where_ship == 0:
                print("ERROR: no port where docked ship\n")
                ship.start_ship()
                continue #jump to another ship
            #now we have both: port and ship
            port_where_ship.load_wares_to_ship(ship)
            ship.start_ship(current_time)
        return 0

    def call_ships_to_ports(self, current_time):
        ports_calling = self.select_ports_calling()
        iddle_ships = self.select_ships_by_state(-1)
        for port in ports_calling:
            if len(iddle_ships)==0:
                break
            port.call_ships(iddle_ships, current_time)
        return 0

    def put_new_wares_to_ports(self, current_time):
        new_wares = self.find_new_wares(current_time)
        for ware in new_wares:
            port = ware.start_ware_in_simulation()
            port.add_wares_to_list([ware])
        return 0

    def dock_ships(self, current_time):
        ships_docking = self.select_ships_docking(current_time)
        for ship in ships_docking:
            port = ship.read_next_destination()
            ship.stop_at_port(port, current_time)
        return 0

    def simulation_step(self, current_time):
        # this order makes docking ships stay STEP_TIME before leave to another port
        self.work_on_docked_ships(current_time)
        self.call_ships_to_ports(current_time)
        self.put_new_wares_to_ports(current_time)
        self.dock_ships(current_time)
        return 0

    def set_test_case(self, ship_class, port_class, ware_class, case_number=1):
        if number==1:
            self.test1_definition(ship_class, port_class, ware_class)
            return True
        return False

    def make_experiment(self, ship_number=0, port_number=0, test_case=1):
        ship=SHIPS[ship_number]
        port=PORTS[port_number]
        ware=Ware
        # ship and port classes are selected
        self.set_test_case(ship, port, ware, test_case)
        self.reset_timer()
        while not self.all_wares_reached_destinations():
            current_time = self.get_current_time()
            self.simulation_step(current_time)
            self.add_time_step()
        print self.wares_list
        print self.ports_list
        print self.ships_list
        return True

