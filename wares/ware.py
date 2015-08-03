from core.logic import find_distance_between_ports

class Ware():
    destination_port = "" #destination port
    start_port = "" #start port
    current_position = "" #ship or port
    t_start = 0.0 #ware begin to exist
    t_end = -1.0 #ware at destination port
    route_length = 0 #total length of route
    route_min = 0 #distance between start and destination port
    destination_reached = False #if true, end of route

    def copy(self):
        new_ware=ware()
        new_ware.destination_port = self.destination_port
        new_ware.start_port = self.start_port
        new_ware.current_position = self.current_position
        new_ware.t_start = self.t_start
        new_ware.t_end = self.t_end
        new_ware.route_length = self.route_length
        new_ware.route_min = self.route_min
        return new_ware

    def set_ports(self, start, destination):
        self.start_port = start
        self.destination_port = destination
        self.route_min = find_distance_between_ports(start, destination)
        return

    def set_time_begin(self, time):
        self.t_start = time
        return



        