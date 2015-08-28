from core.lists import get_nested_elements, find_new_elements
from core.logic import calculate_route_length
from ships.ship_basic import Ship as Ship_basic

class RouteList():
    # all records are lists:
    # [port, status]
    # status can be 0 (major) and 1 (minor)
    route_list=[]

    def get_all_destinations_route(self):
        return get_nested_elements(self.route_list)

    def get_next_destination_route(self):
        return self.route_list[0][0]

    def find_indexes(self, list_of_ports):
        result = []
        for element in list_of_ports:
            for itr in range(len(self.route_list)):
                if element == self.route_list[itr][0]:
                    result.append(itr)
        return result

    def delete_old_destinations(self, list_to_delete):
        if len(list_to_delete) == 0:
            return True
        indexes_to_delete = self.find_indexes(list_to_delete)
        indexes_to_delete.sort(reverse=True)
        for index in indexes_to_delete:
            del self.route_list[index]
        return True

    def get_k_factor(self):
        return 1.2 # now it is a constant

    def add_new_port_inside(self, new_port):
        old_path = []
        new_path = []
        old_length = 0
        new_length = 0
        point1 = 0 # find a port with status "0"
        point2 = 0 # find next port with status "0"
        point3 = 0 # between point1 and point2 try to add a port in route
        while point1<len(self.route_list)-1:
            if self.route_list[point1][1]==0:
                # first port with status "0" found
                # reset all values and lists
                old_path = []
                new_path = []
                old_length = 0
                new_length = 0
                point2 = point1+1
                # find second port with status "0":
                while point2<len(self.route_list):
                    if self.route_list[point2][1]==0:
                        break
                    point2 += 1 # incrememnt point2 in second while
                #PATCH for wrong destinations add/remove method
                if point2 == len(self.route_list):
                    return False
                # copy lists of ports between point1 and point2
                for itr in range(point1, point2+1):
                    old_path.append(self.route_list[itr][0])
                # calculate basic length of route: port on point1 to port on point2
                old_length = calculate_route_length([old_path[0],old_path[-1]])
                # now add point3 inside the list and try all possibilities
                point3 = len(old_path)-1
                while point3 > 0:
                    new_path = list(old_path)
                    new_path.insert(point3, new_port)
                    new_length = calculate_route_length(new_path)
                    k_factor = self.get_k_factor()
                    # if new path is in borders of k_factor
                    if old_length*k_factor > new_length:
                        # add port to route list with status "1"
                        self.route_list.insert(point1+point3,[new_port,1])
                        # end function
                        return True
                    point3 -= 1 # backward: better is to put the port at the end
            point1 += 1 # incrememnt point1 in first While
        return False

    def add_new_ports(self, list_of_ports):
        for port in list_of_ports:
            case = self.add_new_port_inside(port)
            if not case:
                # if adding a port inside the list failed
                # add the port to the end with status "0"
                self.route_list.append([port, 0])
        return list_of_ports

class Ship(Ship_basic, RouteList):

    def __init__(self):
        super(Ship, self).__init__()
        # Description
        self.description_table = "einst1"
        self.description_short = "Einstein's ships algorithm (version 1.01)"
        self.description_full = "Einstein's ships aglorithm (version 1.01). Main explanation file: http://student.agh.edu.pl/~rak/widelands/files/ShipsOptimalization/Ships1.2.pdf"
        return None

    def update_destinations(self):
        destinations_route = self.get_all_destinations_route()
        destinations_wares = self.get_all_destinations_wares()
        # list of ports that are left behind - delete them from list
        old_destinations = find_new_elements(destinations_wares, destinations_route)
        self.delete_old_destinations(old_destinations)
        #---investigation needed: why the ship get to the wrong destination?
        #---why the wares are empty and the destinations aren't?
        #--- next line is a patch. Working, but not perfect. Algorithm needs some checking
        #---if not self.route_list == [] and not self.get_next_destination_route() in destinations_wares:
        #---    del self.route_list[0]
        # list of ports that are new - add them in 
        new_destinations = find_new_elements(destinations_route, destinations_wares)
        self.add_new_ports(new_destinations)
        return 0

    def get_next_destination_ship(self, all_ports, all_ships):
        # where the ship will go next
        self.update_destinations()
        return self.get_next_destination_route()

    # THIS METHOD CAN BE MUCH BETTER
    # (f.e. decide to go to the port where lots of wares)
    """
    def set_ship_iddle(self, all_ports, all_ships):
        # empty ship after docking
        return self.set_current_state(-1)"""
