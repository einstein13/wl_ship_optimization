from settings import SHIPS, PORTS

def import_ship_class(number=0):
    # number: 1- first, 2-second
    module = __import__('ships')
    module = getattr(module, SHIPS[number-1])
    return getattr(module, 'Ship')

def import_port_class(number=0):
    # number: 1- first, 2-second
    module = __import__('ports')
    module = getattr(module, PORTS[number-1])
    return getattr(module, 'Port')