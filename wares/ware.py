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





        