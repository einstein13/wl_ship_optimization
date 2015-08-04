from core.logic import find_distance_between_ports
from common.wares import DestinationPoints, WareStatistics, WareState
from common.classes import TimeDistanceStatistics

class Ware(DestinationPoints,
        WareStatistics,
        WareState,
        TimeDistanceStatistics):

    def copy(self):
        new_ware=ware()
        #DestinationPoints
        self.copy_DestinationPoints(new_ware)
        #WareStatistics
        self.copy_WareStatistics(new_ware)
        #WareState
        self.copy_WareState(new_ware)
        #TimeDistanceStatistics
        self.copy_TimeDistanceStatistics(new_ware)
        return new_ware

    def update_ware_state(self, current_time):
        if self.current_position == self.destination_port:
            self.set_time_end(current_time)
            return self.set_destination_status(True)
        return self.set_destination_status(False)





        