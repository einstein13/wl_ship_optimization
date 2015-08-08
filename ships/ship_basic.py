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
        # Description
        self.description_short = "Very basic ship class."
        self.description_full = self.description_short+" Not very useful to play with, but can be a basic for another classes."
        # Coordinates
        self.coordinates = [0,0]
        # TimeDistanceStatistics
        self.total_distance_traveling = 0
        self.total_time_traveling = 0.0
        # LastNextDestinations
        self.last_destination = "" #port
        self.next_destination = "" #port
        self.time_reach = 0.0 #time when reaching the next destination
        # ShipState
        self.current_state = -1
        # ListOfWares
        self.wares = []
        return None

    def get_next_destination_ship(self):
        # where the ship will go next
        return self.get_next_destination_wares()

    def land_wares_to_port(self, wares_to_land, port, current_time):
        # method used to put correct wares to the port
        wares_to_port = []
        for ware in wares_to_land:
            ware.set_current_position(port)
            ware.update_ware_state(current_time)
            if not ware.read_destination_status():
                # wares landed to port, but not in the correct place
                wares_to_port.append(ware)
        return wares_to_port

    def stop_at_port(self, port, current_time):
        # method used as docking the ship to the port
        land_port = self.read_next_destination()
        if land_port != port:
            print "ERROR: ship: is on the wrong destination"
            self.start_ship(current_time)
            return -1
        #add to all wares distance between last stop and current
        distance = self.distance_between_destinations() #find last trip length
        self.add_distance_time(distance) #update distance to ship statistics
        self.update_distances_for_wares(distance) #update distance to all wares onboard
        self.set_coordinates(port.read_coordinates()) #update position of the ship
        #find wares connected to the port (destination = port)
        wares_to_land = self.find_wares_with_destination(port) #get wares
        if len(wares_to_land)==0 and port.number_of_wares()==0:
            print "ERROR: ship: nothing to land and empty port"
            return self.set_current_state(0)
        if self.number_of_wares()==0 and port.number_of_wares()==0:
            print "ERROR: ship: empty ship is docking to empty port"
            return self.set_current_state(0)
        wares_to_port = self.land_wares_to_port(wares_to_land, port, current_time) #put them to port
        port.load_ware_from_ship(wares_to_port, current_time)
        self.delete_wares_from_list(wares_to_land) #delete from ship
        #stop the ship
        return self.set_current_state(0)

    def start_ship(self, current_time):
        # method used to find next destination and start the journey there
        if self.number_of_wares()==0:
            return self.set_current_state(-1)
        next_destination = self.get_next_destination_ship()
        self.set_next_destination(next_destination)
        self.update_time_reach(current_time)
        return self.set_current_state(1)

    def start_ship_empty(self, destination_port, current_time):
        # method used to start the ship for a call from the port
        self.set_next_destination(destination_port)
        self.update_time_reach(current_time)
        return self.set_current_state(1)

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




