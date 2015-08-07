"""
here goes settings used in whole project
"""

# ships classes that can be used in the experiment
SHIPS = ['ships.ship_basic']

# ports classes that can be used in the experiment
PORTS = ['ports.port_basic']

# settings for one test:
# (port_class_number, ship_class_number)
ONE_TEST = (0,0)

# number of wares that can hold a ship
WARES_MAX = 30

# how often can the changes happen
# default value is 1.8 - equal to Widelands model
STEP_TIME = 1.8

# possible error with adding floats
# always less than STEP_TIME
EPSILON_TIME = 0.00001

# how long the ship goes one unit
# it is recommended to be STEP_TIME
VELOCITY = STEP_TIME
