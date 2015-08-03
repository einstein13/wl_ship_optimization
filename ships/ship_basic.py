from core.lists import find_first

class Ship():
    #class descriptions
    description_short = "Very basic ship class."
    description_full = description_short+" Not very useful to play with, but can be a basic for another classes."
    #destinations and coordinates
    last_destination = "" #port
    next_destination = "" #port
    coordinates = [0,0]
    #state of the ship
    current_state = -1
    """
    current state can be:
        -1 - iddle (stay at coordinates)
        0 - dock to the port (stay at coordinates)
        1 - going to the port (next destination)
    """
    wares = [] #list of wares
    time_reach = 0.0 #time when reaching the next destination
    #stats for the ship
    total_distance_traveling = 0
    total_time_traveling = 0.0

    def copy(self, all_wares=None):
        new_ship = Ship()
        new_ship.last_destination = self.last_destination
        new_ship.next_destination = self.next_destination
        new_ship.current_state = self.current_state
        if all_wares is None:
            for ware in self.wares:
                new_ship.wares.append(ware.copy())
        else:
            for ware in self.wares:
                position = find_first(ware,all_wares)
                new_ship.wares.append(all_wares[position])
        new_ship.time_reach = self.time_reach

    def get_next_destination(self):
        # where the ship will go next
        if len(wares)==0:
            return ""
        return wares[0].destination_port

    def space_left(self):
        # how many wares can be loaded
        return 30-len(wares)

    def set_coordinates(self, new_coordinates):
        self.coordinates[0] = new_coordinates[0]
        self.coordinates[1] = new_coordinates[1]
        return

    def set_next_destination(self, port):
        self.last_destination = self.next_destination
        self.next_destination = port
        return

    def read_next_destination(self):
        return self.next_destination

    def set_current_state(self, state):
        self.current_state = state
        return

    def read_state(self):
        return self.current_state
