import random
from settings import STEP_TIME

def ports_test1(port_class, basic_distance):
    port_list=[]
    for itr in range(-1,2):
        port_to_add=port_class()
        port_to_add.set_coordinates([basic_distance*itr,0])
        port_list.append(port_to_add)
    return port_list

def ships_test1(ship_class, ports_list):
    ships_list=[]
    ship_test=ship_class()
    port_near_ship=ports_list[0]
    ship_test.set_coordinates(port_near_ship.read_coordinates())
    ship_test.set_next_destination(port_near_ship)
    ship_test.set_next_destination(port_near_ship)
    ship_test.set_current_state(-1) # iddle
    ships_list.append(ship_test)
    return ships_list

def wares_test1(ware_class, ports_list, basic_distance):
    random.seed(1) # have the same basic situation for all tests
    wares_list = []
    total_time_iterations = 0
    port_list_last = len(ports_list)-1
    # max delta time between "expected" and "real"
    max_delta = 5
    if max_delta*2 > basic_distance:
        # all wares are in time-sequence
        max_delta = 0
    # generate "random" events
    for itr in range(200):
        # for STEP_TIME = 1.8 & basic_distance = 25
        # approximate time = 2.5 hours (to start all wares)
        new_ware = ware_class()
        # first: ports (start and destination)
        tmp1 = 0
        tmp2 = 0
        while tmp1 == tmp2:
            tmp1 = random.randint(0,port_list_last)
            tmp2 = random.randint(0,port_list_last)
        new_ware.set_ports(ports_list[tmp1],ports_list[tmp2])
        # then: time
        total_time_iterations += random.randint(basic_distance-max_delta, basic_distance+max_delta)
        new_ware.set_time_begin(total_time_iterations*STEP_TIME)
        wares_list.append(new_ware)
    return wares_list






