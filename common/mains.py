from settings import STEP_TIME
from common.classes import ListOfWares

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
            if ship.is_destination_reached(simulation_time):
                selected_ships.append(ship)
        return selected_ships

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