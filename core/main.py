from settings import SHIPS, PORTS, STEP_TIME
from wares.ware import Ware
import test_cases

class experiment():
    wares_list=[]
    ports_list=[]
    ships_list=[]
    current_time=0.0
    time_step=STEP_TIME
    is_iddle_ship=True
    test_description=""

    def end_simulation(self):
        for itr in range(len(wares_list)):
            if not wares_list[-itr].destination_reached:
                return False
        return True

    def update_iddle_ships(self):
        for ship in self.ships_list:
            if ship.current_state==-1:
                self.is_iddle_ship=True
        self.is_iddle_ship=False

    def test1_definition(self, ship, port):
        basic_distance = 25
        self.ports_list = test_cases.ports_test1(port, basic_distance)       
        self.ships_list = test_cases.ships_test1(ship, self.ports_list)
        self.wares_list = test_cases.wares_test1(Ware, self.ports_list, basic_distance)
        return

    def make_experiment(self, ship_number=0, port_number=0):
        ship=SHIPS[ship_number]
        port=PORTS[port_number]
        # ship and port classes are selected