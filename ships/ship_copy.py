from core.lists import find_first
from ships.ship_basic import Ship as Ship_basic

class Ship(Ship_basic):

    def __init__(self):
        super(Ship, self).__init__()
        # Description
        self.description_table = "New1"
        self.description_short = "New short description"
        self.description_full = "New long descpription"
        return None

    # THIS METHOD CAN BE MUCH BETTER
    # (f.e. change destination for more wares)
    """
    def get_next_destination_ship(self, all_ports, all_ships):
        # where the ship will go next
        return self.get_next_destination_wares()"""

    # THIS METHOD CAN BE MUCH BETTER
    # (f.e. decide to go to the port where lots of wares)
    """
    def set_ship_iddle(self, all_ports, all_ships):
        # empty ship after docking
        return self.set_current_state(-1)"""
