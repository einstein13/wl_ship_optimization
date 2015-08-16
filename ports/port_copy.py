from ports.port_basic import Port as Port_basic
from settings import WARES_MAX
from core.lists import delete_elements_from_list

class Port(Port_basic):

    def __init__(self):
        super(Port, self).__init__()
        # Description
        self.description_short = "New short description"
        self.description_full = "New long descpription"
        return None

    """
    def load_wares_to_ship(self, ship, ships_going_to_port):
        if not ship.read_coordinates() == self.read_coordinates():
            return 0
        how_many = min(ship.space_left(), self.number_of_wares())
        wares_to_load = self.wares[:how_many]
        for ware in wares_to_load: #set wares properties
            ware.set_current_position(ship)
        ship.add_wares_to_list(wares_to_load) #set ship ware list
        self.delete_wares_from_list(wares_to_load) #delete from port list
        self.update_calling_ships(ships_going_to_port)
        return len(wares_to_load)"""

    """
    def update_calling_ships(self, ships_going_to_port):
        # consider how many ships we need
        number_of_wares = self.number_of_wares()
        # we need one ship for WARES_MAX wares
        ships_to_call = int(ceil(number_of_wares*1.0/WARES_MAX))
        # some ships can go to the port- let's use them
        ships_to_call = ships_to_call-len(ships_going_to_port)
        # there can't be less than 0:
        ships_to_call = max(ships_to_call, 0)
        self.set_ships_to_call(ships_to_call)
        return 0"""