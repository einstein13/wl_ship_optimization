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
        new_ship.description_short = self.description_short
        new_ship.description_full = self.description_full
        #Coordinates
        new_ship.coordinates[0] = self.coordinates[0]
        new_ship.coordinates[1] = self.coordinates[1]
        #TimeDistanceStatistics
        new_ship.total_distance_traveling = self.total_distance_traveling
        new_ship.total_time_traveling = self.total_time_traveling
        #LastNextDestinations
        if all_ports is None:
            new_ship.last_destination = self.last_destination
            new_ship.next_destination = self.next_destination
        else:
            new_ship.last_destination = ""
            new_ship.next_destination = ""
            if self.last_destination != "":
                position = find_first(self.last_destination, all_ports)
                new_ship.last_destination = ports[position]
            if self.next_destination != "":
                position = find_first(self.next_destination, all_ports)
                new_ship.next_destination = ports[position]
        new_ship.time_reach = self.time_reach
        #ShipState
        new_ship.current_state = self.current_state
        #ListOfWares
        if all_wares is None:
            for ware in self.wares:
                new_ship.wares.append(ware.copy())
        else:
            for ware in self.wares:
                position = find_first(ware,all_wares)
                new_ship.wares.append(all_wares[position])
        return new_ship

    def get_next_destination_ship(self):
        # where the ship will go next
        return get_next_destination_wares()

