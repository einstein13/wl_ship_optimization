from core.logic import find_distance_between_ports

class DestinationPoints():
    destination_port = "" #destination port
    start_port = "" #start port
    route_min = 0 #distance between start and destination port

    def copy_DestinationPoints(self, destination_ware):
    	destination_ware.destination_port = self.destination_port
    	destination_ware.start_port = self.start_port
    	destination_ware.route_min = self.route_min
    	return destination_ware

    def set_ports(self, start, destination):
        self.start_port = start
        self.destination_port = destination
        self.route_min = find_distance_between_ports(start, destination)
        return

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

class WareState():
    current_position = "" #ship or port
    destination_reached = False #if true then end of route

    def copy_WareState(self, destination_ware):
    	destination_ware.current_position = self.current_position
    	destination_ware.destination_reached = self.destination_reached
    	return destination_ware