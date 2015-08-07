from settings import SHIPS, PORTS

def import_ship_class(number=0):
    module = __import__(SHIPS[number])
    return getattr(module, 'Ship')

def import_port_class(number=0):
    module = __import__(PORTS[number])
    return getattr(module, 'Port')