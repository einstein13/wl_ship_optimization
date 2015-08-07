"""
here goes one possibility test
"""

from settings import ONE_TEST
from core.modules import import_ship_class, import_port_class
from wares.ware import Ware
from core.main import experiment

def execute_one_experiment(port_class_number=None, ship_class_number=None, test_case=1):
    if port_class_number==None:
        port_class_number=ONE_TEST[0]
    if ship_class_number==None:
        ship_class_number=ONE_TEST[1]
    port_class=import_port_class(port_class_number)
    ship_class=import_ship_class(ship_class_number)
    ware_class=Ware
    one_experiment=experiment()
    one_experiment.make_experiment(ware_class, port_class, ship_class, test_case)

execute_one_experiment()