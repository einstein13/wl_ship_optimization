from settings import SHIPS, PORTS

def import_ship_class(number=0):
    return getattr(SHIPS[number], 'Ship')

def import_port_class(number=0):
    return getattr(PORTS[number], 'Port')