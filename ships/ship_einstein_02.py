from core.lists import get_nested_elements, find_new_elements
from core.logic import calculate_route_length
from ships.ship_einstein_01 import Ship as Ship_basic

class Ship(Ship_basic):

    def __init__(self):
        super(Ship, self).__init__()
        # Description
        self.description_table = "einst2"
        self.description_short = "Einstein's ships algorithm (version 1.02)"
        self.description_full = "Einstein's ships aglorithm (version 1.02). Main explanation file: http://student.agh.edu.pl/~rak/widelands/files/ShipsOptimalization/Ships1.2.pdf"
        return None

    def update_destinations(self):
        destinations_route = self.get_all_destinations_route()
        destinations_wares = self.get_all_destinations_wares()
        # list of ports that are new - add them in 
        new_destinations = find_new_elements(destinations_route, destinations_wares)
        self.add_new_ports(new_destinations)
        # list of ports that are left behind - delete them from list
        # the lines were switched: new algorithm can set the port BEFORE next destination
        # the only condition is "0" state of current port
        old_destinations = find_new_elements(destinations_wares, destinations_route)
        self.delete_old_destinations(old_destinations)
        #---investigation needed: why the ship get to the wrong destination?
        #---why the wares are empty and the destinations aren't?
        #--- next line is a patch. Working, but not perfect. Algorithm needs some checking
        #---if not self.route_list == [] and not self.get_next_destination_route() in destinations_wares:
        #---    del self.route_list[0]
        return 0

    """
    def get_next_destination_ship(self, all_ports, all_ships):
        # where the ship will go next
        self.update_destinations()
        return self.get_next_destination_route()"""

    # THIS METHOD CAN BE MUCH BETTER
    # (f.e. decide to go to the port where lots of wares)
    """
    def set_ship_iddle(self, all_ports, all_ships):
        # empty ship after docking
        return self.set_current_state(-1)"""
