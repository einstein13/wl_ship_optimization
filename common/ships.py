# ship-only common classes

from core.logic import find_distance_between_ports
from settings import VELOCITY

class LastNextDestinations():
    last_destination = "" #port
    next_destination = "" #port
    time_reach = 0.0 #time when reaching the next destination

    def set_next_destination(self, port=""):
        self.last_destination = self.next_destination
        self.next_destination = port
        return port

    def read_next_destination(self):
        return self.next_destination

    def distance_between_destinations(self):
    	if self.last_destination == "":
    		return 0
    	return find_distance_between_ports(self.last_destination, self.next_destination)

    def update_time_reach(self, current_time=0.0):
    	self.time_reach = current_time + VELOCITY*self.distance_between_destinations
    	return self.time_reach

    def copy_LastNextDestinations(self, destination_ship, all_ports=None):
        if all_ports is None:
            destination_ship.last_destination = self.last_destination
            destination_ship.next_destination = self.next_destination
        else:
            destination_ship.last_destination = ""
            destination_ship.next_destination = ""
            if self.last_destination != "":
                position = find_first(self.last_destination, all_ports)
                destination_ship.last_destination = ports[position]
            if self.next_destination != "":
                position = find_first(self.next_destination, all_ports)
                destination_ship.next_destination = ports[position]
        destination_ship.time_reach = self.time_reach
        return destination_ship

class ShipState():
    current_state = -1
    """
    current state can be:
        -1 - iddle (stay at coordinates; default)
        0 - dock to the port (stay at coordinates)
        1 - going to the port (next destination)
    """
    def set_current_state(self, state=-1):
        self.current_state = state
        return state

    def read_current_state(self):
        return self.current_state

    def copy_ShipState(self, destination_ship):
        destination_ship.current_state = self.current_state
        return destination_ship