from core.lists import find_first

class Ship():
    last_destination = "" #port
    next_destination = "" #port
    current_state = -1
    """
    current state can be:
        -1 - iddle
        0 - dock to the port
        1 - going to the port
    """
    wares = [] #list of wares
    time_reach = 0.0 #time when reaching the next destination

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
                position=find_first(ware,all_wares)
                new_ship.wares.append(all_wares[position])
        new_ship.time_reach = self.time_reach

    def get_next_destination(self):
        if len(wares)==0:
            return ""
        return wares[0].destination_port
