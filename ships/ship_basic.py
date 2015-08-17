from core.lists import find_first
from common.classes import Description, Coordinates, TimeDistanceStatistics, ListOfWares
from common.ships import LastNextDestinations, ShipState

class Ship(Description,
        Coordinates,
        TimeDistanceStatistics,
        LastNextDestinations,
        ShipState,
        ListOfWares,
        object):

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

    # THIS METHOD CAN BE MUCH BETTER
    # (f.e. change destination for more wares)
    def get_next_destination_ship(self, all_ports, all_ships):
        # where the ship will go next
        return self.get_next_destination_wares()

    # THIS METHOD CAN BE MUCH BETTER
    # (f.e. decide to go to the port where lots of wares)
    def set_ship_iddle(self, all_ports, all_ships):
        # empty ship after docking
        return self.set_current_state(-1)

    # this method can be overriden when ships are working together
    def stop_at_port(self, port, current_time, all_ports, all_ships):
        # method used as docking the ship to the port
        land_port = self.read_next_destination()
        if land_port != port:
            print("ERROR: ship: is on the wrong destination")
            self.start_ship(current_time, all_ports, all_ships)
            return -1
        #add to all wares distance between last stop and current
        distance = self.distance_between_destinations() #find last trip length
        self.add_distance_time(distance) #update distance to ship statistics
        self.update_distances_for_wares(distance) #update distance to all wares onboard
        self.set_coordinates(port.read_coordinates()) #update position of the ship
        #find wares connected to the port (destination = port)
        wares_to_land = self.find_wares_with_destination(port) #get wares
        if len(wares_to_land)==0 and port.number_of_wares()==0:
            print("ERROR: ship: nothing to land and empty port")
            return self.set_current_state(0)
        if self.number_of_wares()==0 and port.number_of_wares()==0:
            print("ERROR: ship: empty ship is docking to empty port")
        #wares_to_port = self.land_wares_to_port(wares_to_land, port, current_time) #put them to port
        port.load_wares_from_ship(wares_to_land, current_time)
        self.delete_wares_from_list(wares_to_land) #delete from ship
        #stop the ship
        return self.set_current_state(0)

    def start_ship(self, current_time, all_ports, all_ships):
        # method used to find next destination and start the journey there
        if self.number_of_wares()==0:
            return self.set_ship_iddle(all_ports, all_ships)
        next_destination = self.get_next_destination_ship(all_ports, all_ships)
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




