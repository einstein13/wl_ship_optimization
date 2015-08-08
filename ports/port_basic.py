from math import ceil
from settings import WARES_MAX
from core.lists import delete_elements_from_list
from common.classes import Description, Coordinates, ListOfWares
from common.ports import CallingShip

class Port(Description, Coordinates, ListOfWares, CallingShip):

    def __init__(self):
        # Description
        self.description_short = "Very basic port class."
        self.description_full = self.description_short+" Not very useful to play with, but can be a basic for another classes."
        # Coordinates
        self.coordinates = [0,0]
        # ListOfWares
        self.wares = []
        # CallingShip
        self.ships_to_call = 0
        return None

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
        return len(wares_to_load)

    def update_calling_ships(self, ships_going_to_port):
        number_of_wares = self.number_of_wares()
        # we need one ship for WARES_MAX wares
        ships_to_call = ceil(number_of_wares*1.0/WARES_MAX)
        # some ships can go to the port- let's use them
        ships_to_call = ships_to_call-len(ships_going_to_port)
        # there can't be less than 0:
        ships_to_call = max(ships_to_call, 0)
        self.set_ships_to_call(ships_to_call)
        return 0

    def call_ships(self, iddle_ships, current_time):
        number_of_calls = self.number_ships_to_call()
        for ship in iddle_ships:
            if number_of_calls <= 0:
                break
            ship.start_ship_empty(self, current_time)
            delete_elements_from_list([ship], iddle_ships)
            number_of_calls -= 1
        return number_of_calls

    def load_ware_from_ship(self, wares_list, current_time):
        # this method is useful for wares that are loaded from ship to port,
        # but their destination is not the port
        # 1. add wares to self list
        self.add_wares_to_list(wares_list)
        # 2. update statistics for wares
        for ware in wares_list:
            ware.set_coordinates(self.read_coordinates())
            ware.set_current_position(self)
            ware.update_ware_state(current_time)
        return wares_list

    def copy(self, all_wares=None):
        new_port = Port()
        # Description
        self.copy_Description(new_port)
        # Coordinates
        self.copy_Coordinates(new_port)
        # ListOfWares
        self.copy_ListOfWares(new_port, all_wares)
        return new_port