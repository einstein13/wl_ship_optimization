from core.lists import find_first
from common.classes import Description, Coordinates, TimeDistanceStatistics, ListOfWares
from common.ships import LastNextDestinations, ShipState

class Ship(Description,
        Coordinates,
        TimeDistanceStatistics,
        LastNextDestinations,
        ShipState,
        ListOfWares):

    def __init__(self):
        self.description_short = "Very basic ship class."
        self.description_full = self.description_short+" Not very useful to play with, but can be a basic for another classes."

    def copy(self, all_wares=None, all_ports=None):
        # all_wares and all_ports are the lists of copied ports & wares
        # useful when we want to save class dependences for them
        new_ship = Ship()
        #Description
        self.copy_Descrpition(new_ship)
        #Coordinates
        self.copy_Coordinates(new_ship)
        #TimeDistanceStatistics
        self.copy_TimeDistanceStatistics(new_ship)
        #LastNextDestinations
        self.copy_LastNextDestinations(new_ship, all_ports)
        #ShipState
        self.copy_ShipState(new_ship)
        #ListOfWares
        self.copy_ListOfWares(new_ship, all_wares)
        return new_ship

    def get_next_destination_ship(self):
        # where the ship will go next
        return get_next_destination_wares()

