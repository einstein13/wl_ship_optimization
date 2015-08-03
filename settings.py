"""
here goes settings used in whole project
"""

# ships classes that can be used in the experiment
SHIPS = (ships.ship_basic.Ship,)

# ports classes that can be used in the experiment
PORTS = (ports.port_basic.Port,)

# how often can the changes happen
# default value is 1.8 - equal to Widelands model
STEP_TIME = 1.8

# how long the ship goes one unit
# it is recommended to be STEP_TIME
VELOCITY = STEP_TIME

