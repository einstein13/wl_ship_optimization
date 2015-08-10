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

# stats that are interesting
# commented lines aren't used
STATISTICS_TO_DO = (
    "general: total simulation time",
    "ships: mean utilization",
    "ships: max utilization",
    "ports: mean wares waiting",
    "ports: max wares waiting",
    "wares: min distance of journey",
    "wares: mean distance of journey",
    "wares: max distance of journey",
    "wares: min time of existence",
    "wares: mean time of existence",
    "wares: max time of existence",
    "wares: max journey efficiency",
    "wares: mean journey efficiency",
    "wares: min journey efficiency",
    )

# stats display
# all of them are True/False
STATISTICS_DISPLAYS = {
    "short class descriptions" : True,
    "separate lines" : True,
    "help text" : True,
    }

# stats optimization (used for execute_all.py)
STATISTICS_TO_OPTIMIZE = "general: total simulation time"