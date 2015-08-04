from common.classes import Description, Coordinates, ListOfWares

class Port(Description, Coordinates, ListOfWares):
    coordinates = [0,0]
    wares = []

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
