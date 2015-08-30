from core.lists import find_first
from core.logic import find_distance_between_ports
from ships.ship_basic import Ship as Ship_basic
from settings import WARES_MAX
from common.mains import ShipList

class Ship(Ship_basic):

    def __init__(self):
        super(Ship, self).__init__()
        # Description
        self.description_table = "Tibor2"
        self.description_short = "Tibor's algorithm for ship (C++)"
        self.description_full = "Tibor's algorithm for ships. Based on his branch for Widelands, merged before build 19."
        return None

    # THIS METHOD CAN BE MUCH BETTER
    # (f.e. change destination for more wares)
    def get_next_destination_ship(self, all_ports, all_ships):
        # where the ship will go next
        # http://bazaar.launchpad.net/~widelands-dev/widelands/ship_scheduling/view/head:/src/economy/fleet.cc#L650
        # first: all ports in list with score=0
        port_list = []
        for port in all_ports:
            port_list.append([port, 0])

        oldest_ware_score = 8  #not lesser then 1
        wares_list = self.wares

        # line 713 - loop (calculating scores for wares onboard)
        # score 1 for all wares, oldest_ware_score for first
        all_destinations_wares = self.get_all_destinations_wares()
        for port in port_list:
            if not (port[0] in all_destinations_wares):
                continue
            for ware in wares_list:
                if port[0] == ware.destination_port:
                    if ware == wares_list[0]:
                        port[1] += 8
                    else:
                        port[1] += 1

        # line 735 - loop (wares waiting in ports)
        for port in port_list:
            if port[0].number_ships_to_call() == 0:
                continue
            if self.number_of_wares() > WARES_MAX//2:
                port[1] += 1
            else:
                port[1] += 3
            port[1] += min(self.space_left(), port[0].number_of_wares())//3

        # line 773 - loop (calculate score for distances)
        for port in port_list:
            route_length = find_distance_between_ports(port[0], self.next_destination)
            score_for_distance = 0
            # line 805 - decision what type of distance it is
            if route_length < 3:
                score_for_distance = 10
            else:
                score_for_distance = 8 - route_length//50
            if score_for_distance < 0:
                score_for_distance = 0
            port[1] += score_for_distance

        # line 817 - loop (find best port)
        best_port = port_list[0][0]
        best_score = port_list[0][1]
        for port in port_list:
            if best_score < port[1]:
                best_port = port[0]
                best_score = port[1]

        # line 872 - updating port needs
        ships = ShipList()
        ships.ships_list = all_ships
        ships_going_to_port = ships.select_ships_going_to_port(best_port)
        ships_going_to_port.append(self)
        best_port.update_calling_ships(ships_going_to_port)

        # end:
        return best_port

    # THIS METHOD CAN BE MUCH BETTER
    # (f.e. decide to go to the port where lots of wares)
    """
    def set_ship_iddle(self, all_ports, all_ships):
        # empty ship after docking
        return self.set_current_state(-1)"""
