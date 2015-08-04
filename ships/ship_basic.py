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

    def land_wares_to_port(self, wares_to_land, port, current_time):
        wares_to_port = []
        for ware in wares_to_land:
            ware.set_current_position(port)
            ware.update_ware_state(time)
            if not ware.read_destination_status():
                wares_to_port.append(ware)
        return wares_to_port

    def stop_at_port(self, port, current_time):
        land_port = self.read_next_destination()
        if land_port != port:
            return -1
        #add to all wares distance between last stop and current
        distance = self.distance_between_destinations() #find last trip length
        self.add_distance_time(distance) #update distance to ship statistics
        self.update_distances_for_wares(distance) #update distance to all wares onboard
        self.set_coordinates(port.read_coordinates()) #update position of the ship
        #find wares connected to the port (destination = port)
        wares_to_land = self.find_wares_with_destination(port) #get wares
        wares_to_port = self.land_wares_to_port(wares_to_land, port, current_time) #put them to port
        self.delete_wares_from_list(wares_to_land) #delete from ship
        #stop the ship
        return self.set_current_state(0)

    def start_ship(self, current_time):
        if self.number_of_wares()==0:
            return self.set_current_state(-1)
        next_destination = self.get_next_destination_ship()
        self.set_next_destination(next_destination)
        self.update_time_reach(current_time)
        self.set_current_state(1)
        return self.read_current_state()





