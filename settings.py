"""
here goes settings used in whole project
"""

# ships classes that can be used in the experiment
# please add only file names in ships folder, no ".py" needed
SHIPS = ['ship_basic',
    'ship_Tibor',
    'ship_Tibor_cpp',
    'ship_einstein_01',
    'ship_einstein_02',
    'ship_einstein_03']

# ports classes that can be used in the experiment
# please add only file names in ships folder, no ".py" needed
PORTS = ['port_basic',
    'port_patch_einstein']

# number of possible tests cases
# all tests should be hardcoded first
POSSIBLE_TESTS_CASES = 5

# settings for one test:
# (port_class_number, ship_class_number)
# 1- first, 2-second, ...
ONE_TEST = (1,3)

# test cases to do with execute_all command
# lists are [port_class, ship_class, test_case]
# '-1' means all possibilities
# examples:
#    [-1, -1, -1] (all possible tests)
#    [-1, -1, 1] (all possible classes for first test)
#    [1, 1, [1,2,3]] (first port and ship classes for test cases 1, 2, 3)
#    [[1,2],[1,2,3], 1] (all pairs port-ship for 1 & 2 ports and 1, 2 & 3 ships, all for first test case)
TEST_CASES = [
    [-1, -1, -1]
    ]

# How difficult tests are.
# Higher number - more wares, shorter time, longer distances.
# Possible values:
#    1 - Slow mode - long time between appearing wares,
#        mostly to see if algorithms aren't working in very strange way
#    2 - Standard mode - middle time between appearing wares, middle distances,
#        mostly to see if everything is working fine with more complex problems,
#        plus if the algorithm is just wrong (much worse than basic one)
#    3 - Stressed mode - lots of wares at once, long distances,
#        mostly to see the difference in very complex situations
TEST_MODE = 2

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
    #"ships: max utilization",
    "ports: mean wares waiting",
    "ports: max wares waiting",
    #"wares: min distance of journey",
    "wares: mean distance of journey",
    #"wares: max distance of journey",
    #"wares: min time of existence",
    "wares: mean time of existence",
    #"wares: max time of existence",
    #"wares: max journey efficiency",
    "wares: mean journey efficiency",
    "wares: min journey efficiency",
    "wares: max time waiting",
    "wares: mean time waiting",
    #"wares: min time waiting",
    )

# stats display
# all of them are True/False
STATISTICS_DISPLAYS = {
    "short class descriptions" : True,
    "separate lines" : True,
    "help text" : False,
    "show statistics for experiments": True, #for execute_all.py only, shows experiments results
    "show markdown tables": True, #for execute_all.py only, show all experiments results at once
    "get optimized statistics": True, #for execute_all.py only, STATISTICS_TO_OPTIMIZE value needed
    }

# stats optimization (used for execute_all.py)
STATISTICS_TO_OPTIMIZE = "wares: mean journey efficiency"