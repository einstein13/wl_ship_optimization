from ports.port_basic import Port as Port_basic
from settings import WARES_MAX
from core.lists import delete_elements_from_list

class Port(Port_basic):

    def __init__(self):
        super(Port, self).__init__()
        # Description
        self.description_table = "einst1"
        self.description_short = "First einstein's patch"
        self.description_full = "Simple einstein's patch. Wares going to existing location goes first. Based on explanation here: https://wl.widelands.org/forum/topic/1762/?page=5#post-14225."
        return None

    def load_wares_to_ship(self, ship, ships_going_to_port):
        if not ship.read_coordinates() == self.read_coordinates():
            print("ERROR: port: ship in wrong location")
            return 0
        existing_locations = ship.get_all_destinations_wares()
        empty_space = ship.space_left()
        wares_to_load = []
        # add wares that have destinations in locations
        for ware in self.wares:
            if empty_space <= 0:
                break
            if ware.destination_port in existing_locations:
                wares_to_load.append(ware)
                empty_space -= 1
        # if no more space- end the method
        if empty_space==0 or self.number_of_wares()==0:
            self.load_prepared_ware_list_to_ship(ship, ships_going_to_port, wares_to_load)
            return len(wares_to_load)
        # add wares that are not in locations
        for ware in self.wares:
            if empty_space <= 0:
                break
            if ware in wares_to_load:
                continue
            wares_to_load.append(ware)
            empty_space -= 1
        # end method: add wares list
        self.load_prepared_ware_list_to_ship(ship, ships_going_to_port, wares_to_load)
        return len(wares_to_load)

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