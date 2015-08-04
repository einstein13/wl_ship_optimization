from common.classes import Description, Coordinates, ListOfWares

class Port(Description, Coordinates, ListOfWares):

    def __init__(self):
        self.description_short = "Very basic port class."
        self.description_full = self.description_short+" Not very useful to play with, but can be a basic for another classes."

    def copy(self, all_wares=None):
        new_port = Port()
        # Description
        self.copy_Description(new_port)
        # Coordinates
        self.copy_Coordinates(new_port)
        # ListOfWares
        self.copy_ListOfWares(new_port, all_wares)
        return new_port

    def load_wares_to_ship(self, ship):
        if not ship.read_coordinates() == self.read_coordinates():
            return 0
        how_many = min(ship.space_left(), self.number_of_wares())
        wares_to_load = self.wares[:how_many]
        for ware in wares_to_load: #set wares properties
            ware.set_current_position(ship)
        ship.add_wares_to_list(wares_to_load) #set ship ware list
        self.delete_wares_from_list(wares_to_load) #delete from port list
        return len(wares_to_load)
