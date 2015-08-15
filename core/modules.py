from settings import SHIPS, PORTS

def import_ship_class(number=0):
	# number: 1- first, 2-second
    module = __import__(SHIPS[number-1])
    return getattr(module, 'Ship')

def import_port_class(number=0):
	# number: 1- first, 2-second
    module = __import__(PORTS[number-1])
    return getattr(module, 'Port')