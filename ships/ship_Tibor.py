from core.lists import find_first
from core.logic import find_distance_between_ports
from ships.ship_basic import Ship as Ship_basic

class Ship(Ship_basic):

    def __init__(self):
        super(Ship, self).__init__()
        # Description
        self.description_short = "Tibor's algorithm for ship"
        self.description_full = "Tibor's algorithm for ships. Based on his python project. This algorithm was used in Widelands for build 19."
        return None

    # THIS METHOD CAN BE MUCH BETTER
    # (f.e. change destination for more wares)
    def get_next_destination_ship(self, all_ports, all_ships):
        # where the ship will go next
        oldest_ware_score = 8  #not lesser then 1
        distance_weight = 2
        wares_list = self.wares
        scoring_table = {}

        # score for oldest ware
        scoring_table[wares_list[0].destination_port] = oldest_ware_score-1

        # score 1 for all wares
        for ware in wares_list:
            if scoring_table.has_key(ware.destination_port):
                scoring_table[ware.destination_port] += 1
            else:
                scoring_table[ware.destination_port] = 1

        # We need to identify ports where no ship is heading and add score based on waiting wares
        for port in all_ports:
            if not port==self.next_destination and len(port.wares)>0:
                any_ship_heading_here=False
                for ship in all_ships:
                    if ship.next_destination==port:
                        any_ship_heading_here=True
                        break

                if not any_ship_heading_here:
                    if scoring_table.has_key(port):
                        scoring_table[port]+=port.number_of_wares()
                    else:
                        scoring_table[port]=port.number_of_wares()
        # adding score if based on distance for ports we consider to visit
        for port,count in scoring_table.iteritems():
            scoring_table[port]+=(5-find_distance_between_ports(port,self.next_destination)/20)*distance_weight

        # find best option
        best_port = None
        best_score = None
        for port,count in scoring_table.iteritems():
            if best_score is None:
                best_port = port
                best_score = count
            if count>best_score:
                best_port=port
                best_score=count
        
        return best_port

    # THIS METHOD CAN BE MUCH BETTER
    # (f.e. decide to go to the port where lots of wares)
    """
    def set_ship_iddle(self, all_ports, all_ships):
        # empty ship after docking
        return self.set_current_state(-1)"""
