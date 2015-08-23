# ships, wares and ports common classes

from settings import VELOCITY
from core.logic import find_distance
from core.lists import delete_elements_from_list

class Description():
    description_short = ""
    description_full = ""

    def read_full_description(self):
        return self.description_full

    def read_short_description(self):
        return self.description_short

    def copy_Description(self, destination_object):
        destination_object.description_short = self.description_short
        destination_object.description_full = self.description_full
        return destination_object

class Coordinates():
    coordinates = [0,0]

    def read_coordinates(self):
        return self.coordinates

    def set_coordinates(self, new_coordinates):
        self.coordinates[0] = new_coordinates[0]
        self.coordinates[1] = new_coordinates[1]
        return new_coordinates

    def distance_between_point(self, point):
        return find_distance(self.coordinates, point)

    def copy_Coordinates(self, destination_object):
        destination_object.coordinates = list(self.coordinates)
        return destination_object

class TimeDistanceStatistics():
    total_distance_traveling = 0
    total_time_traveling = 0.0

    def reset_statistics(self):
        self.total_time_traveling = 0.0
        self.total_distance_traveling = 0
        return 0

    def add_distance_time(self, distance):
        self.total_time_traveling += distance*VELOCITY
        self.total_distance_traveling += distance
        return distance

    def copy_TimeDistanceStatistics(self, destination_object):
        destination_object.total_distance_traveling = self.total_distance_traveling
        destination_object.total_time_traveling = total_time_traveling
        return destination_object

class ListOfWares():
    wares = []

    def get_next_destination_wares(self):
        # useful for ships
        return self.wares[0].destination_port

    def get_all_destinations_wares(self):
        # useful for ships, ports
        destinations = []
        for ware in self.wares:
            if not ware.destination_port in destinations:
                destinations.append(ware.destination_port)
        return destinations

    def find_wares_with_destination(self, port):
        # useful for ships, ports
        result = []
        for ware in self.wares:
            if ware.destination_port == port:
                result.append(ware)
        return result

    def find_wares_with_destination_list(self, list_ports):
        # useful for ports
        result = []
        for ware in self.wares:
            if ware.destination_port in list_ports:
                result.append(ware)
        return result

    def delete_wares_from_list(self, wares_to_delete):
        # useful for ships, ports
        self.wares=delete_elements_from_list(wares_to_delete, self.wares)
        return wares_to_delete

    def add_wares_to_list(self, wares_to_add):
        # useful for ships, ports
        self.wares.extend(wares_to_add)
        return wares_to_add

    def number_of_wares(self):
        # useful for ships, ports
        return len(self.wares)

    def space_left(self):
        # useful for ships
        # how many wares can be loaded to a ship
        return 30-self.number_of_wares()

    def update_distances_for_wares(self, distance):
        # useful for ships
        for ware in self.wares:
            ware.add_route_length(distance)
        return distance

    def all_wares_reached_destinations(self):
        # useful for main experiment
        for ware in self.wares_list:
            if not ware.read_destination_status():
                return False
        return True

    def find_new_wares(self, simulation_time):
        # useful for main experiment
        new_wares = []
        for ware in self.wares_list:
            if ware.read_current_position()=="" and ware.read_when_begin_exist()<=simulation_time:
                new_wares.append(ware)
        return new_wares

    def copy_ListOfWares(self, destination_object, all_wares=None):
        if all_wares is None:
            for ware in self.wares:
                destination_object.wares.append(ware.copy())
        else:
            for ware in self.wares:
                position = find_first(ware,all_wares)
                destination_object.wares.append(all_wares[position])
        return destination_object
