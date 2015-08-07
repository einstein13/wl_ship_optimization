"""
here goes one possibility test
"""

from settings import ONE_TEST
from core.modules import import_ship_class, import_port_class
from wares.ware import Ware

def execute_one_experiment(port_class_number=None, ship_class_number=None):
    if port_class_number==None:
        port_class_number=ONE_TEST[0]
    if ship_class_number==None:
        ship_class_number=ONE_TEST[1]
    port_class=import_port_class(port_class_number)
    ship_class=import_ship_class(ship_class_number)
    ware_class=Ware

execute_one_experiment()