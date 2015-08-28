from settings import STEP_TIME
from common.classes import ListOfWares
from core.lists import debug_list, debug_list_all

class ShipList():
    ships_list=[]
    is_iddle_ship=True

    def update_iddle_ships(self):
        for ship in self.ships_list:
            if ship.current_state==-1:
                self.is_iddle_ship=True
        self.is_iddle_ship=False

    def select_ships_by_state(self, state):
        selected_ships = []
        for ship in self.ships_list:
            if ship.is_with_state(state):
                selected_ships.append(ship)
        return selected_ships

    def select_ships_docking(self, simulation_time):
        selected_ships = []
        for ship in self.ships_list:
            if ship.is_destination_reached(simulation_time) and ship.read_current_state()==1:
                selected_ships.append(ship)
        return selected_ships

    def select_ships_going_to_port(self, destination_port):
        selected_ships = []
        for ship in self.ships_list:
            if ship.is_next_destination(destination_port) and ship.read_current_state()==1:
                selected_ships.append(ship)
        return selected_ships

    def ships_list_debug(self):
        return debug_list(self.ships_list)

    def ships_list_debug_all(self):
        return debug_list_all(self.ships_list)

class PortList():
    ports_list=[]

    def select_ports_calling(self):
        selected_ports = []
        for port in self.ports_list:
            if port.is_port_calling():
                selected_ports.append(port)
        return selected_ports

    def find_port_at_location(self, coordinates):
        for port in self.ports_list:
            if port.read_coordinates() == coordinates:
                return port
        return 0

    def ports_list_debug(self):
        return debug_list(self.ports_list)

class SimulationTime():
    simulation_steps = 0
    time_step = STEP_TIME

    def reset_timer(self):
        self.simulation_steps = 0
        return 0

    def get_time_step(self):
        return self.time_step

    def get_current_time(self):
        return self.time_step*self.simulation_steps

    def add_time_step(self):
        self.simulation_steps += 1
        return self.simulation_steps

class GlobalShipStatistics():
    ships_to_ships_statistics=0
    wares_to_ships_statistics=0
    max_wares_taken_by_ship=0

    def read_mean_ships_utilization(self):
        return 1.0*self.wares_to_ships_statistics/self.ships_to_ships_statistics

    def read_max_wares_taken_ship(self):
        return self.max_wares_taken_by_ship

    def update_global_ships_statistics(self, ships_list):
        ships_going=0
        wares_transported=0
        tmp_wares=0
        for ship in ships_list:
            # if ship is going
            if ship.is_with_state(1):
                ships_going += 1
                tmp_wares = ship.number_of_wares()
                wares_transported += tmp_wares
                # update max_wares
                if tmp_wares > self.max_wares_taken_by_ship:
                    self.max_wares_taken_by_ship = tmp_wares
        if ships_going == 0:
            return 0
        self.ships_to_ships_statistics += ships_going
        self.wares_to_ships_statistics += wares_transported
        return 1.0*wares_transported/ships_going

class GlobalPortStatistics():
    ports_to_port_statistics=0
    wares_to_port_statistics=0
    max_wares_waiting_in_port=0

    def read_mean_wares_waiting_in_port(self):
        return 1.0*self.wares_to_port_statistics/self.ports_to_port_statistics

    def read_max_wares_waiting_port(self):
        return self.max_wares_waiting_in_port

    def update_global_ports_statistics(self, port_list):
        total_ports = len(port_list)
        total_wares = 0
        tmp_wares = 0
        for port in port_list:
            tmp_wares = port.number_of_wares()
            total_wares += tmp_wares
            # update max_wares
            if tmp_wares > self.max_wares_waiting_in_port:
                self.max_wares_waiting_in_port = tmp_wares
        self.ports_to_port_statistics += total_ports
        self.wares_to_port_statistics += total_wares
        return 1.0*total_wares/total_ports

