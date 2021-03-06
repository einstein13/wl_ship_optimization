from core.logic import find_distance_between_ports

class DestinationPoints():
    destination_port = "" #destination port
    start_port = "" #start port
    route_min = 0 #distance between start and destination port

    def set_ports(self, start, destination):
        self.start_port = start
        self.destination_port = destination
        self.route_min = find_distance_between_ports(start, destination)
        return

    def read_starting_point(self):
        return self.start_port

    def read_route_min(self):
        return self.route_min

    def copy_DestinationPoints(self, destination_ware):
        destination_ware.destination_port = self.destination_port
        destination_ware.start_port = self.start_port
        destination_ware.route_min = self.route_min
        return destination_ware

class WareStatistics():
    t_start = 0.0 #ware begin to exist
    t_end = -1.0 #ware at destination port
    route_length = 0 #total length of route

    def copy_WareStatistics(self, destination_ware):
        destination_ware.t_start = self.t_start
        destination_ware.t_end = self.t_end
        destination_ware.route_length = self.route_length
        return destination_ware

    def set_time_begin(self, time):
        self.t_start = time
        t_end = -1.0 #ware at destination port
        return

    def set_time_end(self, time):
        self.t_end = time
        return time

    def add_route_length(self, distance):
        self.route_length += distance
        return self.route_length

    def read_when_begin_exist(self):
        return self.t_start

    def read_route_length(self):
        return self.route_length

    def read_time_existence(self):
        return self.t_end-self.t_start


class WareState():
    current_position = "" #ship or port
    destination_reached = False #if true then end of route

    def set_destination_status(self, state=False):
        self.destination_reached = state
        return state

    def set_current_position(self, current_object=""):
        self.current_position = current_object
        return current_object

    def read_destination_status(self):
        return self.destination_reached

    def read_current_position(self):
        return self.current_position

    def copy_WareState(self, destination_ware):
        destination_ware.current_position = self.current_position
        destination_ware.destination_reached = self.destination_reached
        return destination_ware
