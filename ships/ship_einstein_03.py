from core.lists import get_nested_elements, find_new_elements
from core.logic import calculate_route_length
from ships.ship_einstein_02 import Ship as Ship_basic

class Ship(Ship_basic):

    def __init__(self):
        super(Ship, self).__init__()
        # Description
        self.description_table = "einst3"
        self.description_short = "Einstein's ships algorithm (version 1.03)"
        self.description_full = "Einstein's ships aglorithm (version 1.03). Change introduced here: https://wl.widelands.org/forum/topic/1762/?page=6#post-14255"
        return None

    def get_k_factor(self, old_path, new_path):
        old_path_count = 0
        new_path_count = 0
        for ware in self.wares:
            if ware.destination_port in old_path:
                old_path_count += 1
            if ware.destination_port in new_path:
                new_path_count += 1
        if old_path_count == 0:
            print "ERROR: ship: destination in list with no wares onboard"
            return 1.0
        if new_path_count == 0:
            return 1.0
        result = 1.0*new_path_count/old_path_count
        return result

    """
    def update_destinations(self):
        destinations_route = self.get_all_destinations_route()
        destinations_wares = self.get_all_destinations_wares()
        # list of ports that are left behind - delete them from list
        old_destinations = find_new_elements(destinations_wares, destinations_route)
        self.delete_old_destinations(old_destinations)
        #---investigation needed: why the ship get to the wrong destination?
        #---why the wares are empty and the destinations aren't?
        #--- next line is a patch. Working, but not perfect. Algorithm needs some checking
        #---if not self.route_list == [] and not self.get_next_destination_route() in destinations_wares:
        #---    del self.route_list[0]
        # list of ports that are new - add them in 
        new_destinations = find_new_elements(destinations_route, destinations_wares)
        self.add_new_ports(new_destinations)
        return 0"""

    # THIS METHOD CAN BE MUCH BETTER
    # (f.e. decide to go to the port where lots of wares)
    """
    def set_ship_iddle(self, all_ports, all_ships):
        # empty ship after docking
        return self.set_current_state(-1)"""
