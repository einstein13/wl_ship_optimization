import random
from settings import STEP_TIME

# every function has port/ship/ware class to make correct instances
# ships and wares functions have ports_list to be sure that objects are implemented correctly
# basic_distance is to define correct coordinates (ports) and timing (wares)
# test_type is a value in range 1..3:
#    1 - easy tests
#    2 - moderate tests
#    3 - extreme tests

# ===========
#   TEST 1
# ===========
# ports: single line A --- B --- C
# ships: one ship
# wares: 200 wares, low speed

def ports_test1(port_class, basic_distance=25, test_type=1):
    port_list=[]
    # for test_type = 3: distance is multiplied by 2
    distance = basic_distance
    if test_type > 2:
        distance *= 2
    for itr in range(-1,2):
        port_to_add=port_class()
        port_to_add.set_coordinates([distance*itr,0])
        port_to_add.description_debug+=str(itr)
        port_list.append(port_to_add)
    return port_list

def ships_test1(ship_class, ports_list, test_type=1):
    ships_list=[]
    # number of ships used in test
    # the number is always = 1
    number_of_ships = 1
    for itr in range(number_of_ships):
        ship_test=ship_class()
        port_near_ship=ports_list[random.randint(0,len(ports_list)-1)]
        ship_test.set_coordinates(port_near_ship.read_coordinates())
        ship_test.set_next_destination(port_near_ship)
        ship_test.set_next_destination(port_near_ship)
        ship_test.set_current_state(-1) # iddle
        ship_test.description_debug+=str(itr+1)
        ships_list.append(ship_test)
    return ships_list

def wares_test1(ware_class, ports_list, basic_distance=25, test_type=1):
    wares_list = []
    total_time_iterations = 0
    port_list_last = len(ports_list)-1
    # max delta time between "expected" and "real"
    # for test_type greater than 1, delta time is lower
    time_distance = basic_distance
    if test_type == 2:
        time_distance = max(1, time_distance // 8)
    elif test_type == 3:
        time_distance = max(1, time_distance // 15)
    max_delta = 5
    if max_delta*2 > time_distance:
        # all wares are in time-sequence
        max_delta = 0
    # number of wares: higher test_type number  more wares
    number_of_wares = 200
    if test_type == 2:
        number_of_wares *= 4
    elif test_type == 3:
        number_of_wares *= 8
    # generate "random" events
    for itr in range(number_of_wares):
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
        total_time_iterations += time_distance
        total_time_iterations += random.randint(max_delta, max_delta)
        new_ware.set_time_begin(total_time_iterations*STEP_TIME)
        new_ware.description_debug+=str(itr+1)
        wares_list.append(new_ware)
    return wares_list

# ===========
#   TEST 2
# ===========
# ports: regular triangle A /B\ C
# ships: one ship
# wares: lots of wares at once, 500 wares

def ports_test2(port_class, basic_distance=20, test_type=1):
    port_list=[]
    # for test_type = 3: distance is multiplied by 2
    distance = basic_distance
    if test_type > 2:
        distance *= 2
    for itr in range(3):
        port_to_add=port_class()
        if itr == 0:
            port_to_add.set_coordinates([distance,0])
        elif itr == 1:
            port_to_add.set_coordinates([distance//2,distance])
        elif itr == 2:
            port_to_add.set_coordinates([0,0])
        port_to_add.description_debug+=str(itr+1)
        port_list.append(port_to_add)
    return port_list

def ships_test2(ship_class, ports_list, test_type=1):
    ships_list=[]
    # number of ships used in test
    # the number is always = 1
    number_of_ships = 1
    for itr in range(number_of_ships):
        ship_test=ship_class()
        port_near_ship=ports_list[random.randint(0,len(ports_list)-1)]
        ship_test.set_coordinates(port_near_ship.read_coordinates())
        ship_test.set_next_destination(port_near_ship)
        ship_test.set_next_destination(port_near_ship)
        ship_test.set_current_state(-1) # iddle
        ship_test.description_debug+=str(itr+1)
        ships_list.append(ship_test)
    return ships_list

def wares_test2(ware_class, ports_list, basic_distance=20, test_type=1):
    wares_list = []
    total_time_iterations = 0
    port_list_last = len(ports_list)-1
    # max delta time between "expected" and "real"
    # for test_type greater than 1, delta time is lower
    time_distance = basic_distance
    if test_type == 2:
        time_distance = max(1, time_distance // 8)
    elif test_type == 3:
        time_distance = max(1, time_distance // 15)
    max_delta = 5
    if max_delta*2 > time_distance:
        # all wares are in time-sequence
        max_delta = 0
    # number of wares: higher test_type number  more wares
    number_of_wares = 300
    if test_type == 2:
        number_of_wares *= 4
    elif test_type == 3:
        number_of_wares *= 6
    # generate "random" events
    for itr in range(number_of_wares):
        # for STEP_TIME = 1.8 & basic_distance = 20
        # approximate time = 1.25 hours (to start all wares)
        new_ware = ware_class()
        # first: ports (start and destination)
        tmp1 = 0
        tmp2 = 0
        while tmp1 == tmp2:
            tmp1 = random.randint(0,port_list_last)
            tmp2 = random.randint(0,port_list_last)
        new_ware.set_ports(ports_list[tmp1],ports_list[tmp2])
        # then: time
        total_time_iterations += time_distance
        total_time_iterations += random.randint(-max_delta, max_delta)
        new_ware.set_time_begin(total_time_iterations*STEP_TIME)
        new_ware.description_debug+=str(itr+1)
        wares_list.append(new_ware)
    return wares_list

# ===========
#   TEST 3
# ===========
# ports: 6 ports, regular hexagon
# ships: two
# wares: middle speed, 300 wares
def ports_test3(port_class, basic_distance=20, test_type=1):
    port_list=[]
    # for test_type = 3: distance is multiplied by 2
    distance = basic_distance
    if test_type > 2:
        distance *= 2
    for itr in range(6):
        port_to_add=port_class()
        if itr == 0:
            port_to_add.set_coordinates([distance,0])
        elif itr == 1:
            port_to_add.set_coordinates([distance//2,distance])
        elif itr == 2:
            port_to_add.set_coordinates([distance//2-distance,distance])
        elif itr == 3:
            port_to_add.set_coordinates([-distance,0])
        elif itr == 4:
            port_to_add.set_coordinates([distance//2-distance,-distance])
        elif itr == 5:
            port_to_add.set_coordinates([distance//2,-distance])
        port_to_add.description_debug+=str(itr+1)
        port_list.append(port_to_add)
    return port_list

def ships_test3(ship_class, ports_list, test_type=1):
    ships_list=[]
    # the number is always = 2
    number_of_ships = 2
    for itr in range(number_of_ships):
        ship_test=ship_class()
        port_near_ship=ports_list[random.randint(0,len(ports_list)-1)]
        ship_test.set_coordinates(port_near_ship.read_coordinates())
        ship_test.set_next_destination(port_near_ship)
        ship_test.set_next_destination(port_near_ship)
        ship_test.set_current_state(-1) # iddle
        ship_test.description_debug+=str(itr+1)
        ships_list.append(ship_test)
    return ships_list

def wares_test3(ware_class, ports_list, basic_distance=20, test_type=1):
    wares_list = []
    total_time_iterations = 0
    port_list_last = len(ports_list)-1
    # max delta time between "expected" and "real"
    # for test_type greater than 1, delta time is lower
    time_distance = basic_distance
    if test_type == 2:
        time_distance = max(1, time_distance // 8)
    elif test_type == 3:
        time_distance = max(1, time_distance // 15)
    max_delta = 3
    if max_delta*2 > time_distance:
        # all wares are in time-sequence
        max_delta = 0
    # number of wares: higher test_type number  more wares
    number_of_wares = 300
    if test_type == 2:
        number_of_wares *= 4
    elif test_type == 3:
        number_of_wares *= 6
    # generate "random" events
    for itr in range(number_of_wares):
        # for STEP_TIME = 1.8 & basic_distance = 20
        # approximate time = 1.5 hours (to start all wares)
        new_ware = ware_class()
        # first: ports (start and destination)
        tmp1 = 0
        tmp2 = 0
        while tmp1 == tmp2:
            tmp1 = random.randint(0,port_list_last)
            tmp2 = random.randint(0,port_list_last)
        new_ware.set_ports(ports_list[tmp1],ports_list[tmp2])
        # then: time
        total_time_iterations += time_distance
        total_time_iterations += random.randint(-max_delta, max_delta)
        new_ware.set_time_begin(total_time_iterations*STEP_TIME)
        new_ware.description_debug+=str(itr+1)
        wares_list.append(new_ware)
    return wares_list

# ===========
#   TEST 4
# ===========
# ports: 4 ports, long rectangle
# ships: two
# wares: middle speed, 300 wares
def ports_test4(port_class, basic_distance=20, test_type=1):
    port_list=[]
    # for test_type = 3: distance is multiplied by 2
    distance = basic_distance
    if test_type > 2:
        distance *= 2
    for itr in range(4):
        port_to_add=port_class()
        if itr == 0:
            port_to_add.set_coordinates([distance,0])
        elif itr == 1:
            port_to_add.set_coordinates([distance,10])
        elif itr == 2:
            port_to_add.set_coordinates([-distance,10])
        elif itr == 3:
            port_to_add.set_coordinates([-distance,0])
        port_to_add.description_debug+=str(itr+1)
        port_list.append(port_to_add)
    return port_list

def ships_test4(ship_class, ports_list, test_type=1):
    ships_list=[]
    # number of ships used in test
    # the number = 2, except test_type=3
    number_of_ships = 2
    if test_type == 3:
        number_of_ships = 1
    for itr in range(number_of_ships):
        ship_test=ship_class()
        port_near_ship=ports_list[random.randint(0,len(ports_list)-1)]
        ship_test.set_coordinates(port_near_ship.read_coordinates())
        ship_test.set_next_destination(port_near_ship)
        ship_test.set_next_destination(port_near_ship)
        ship_test.set_current_state(-1) # iddle
        ship_test.description_debug+=str(itr+1)
        ships_list.append(ship_test)
    return ships_list

def wares_test4(ware_class, ports_list, basic_distance=20, test_type=1):
    wares_list = []
    total_time_iterations = 0
    port_list_last = len(ports_list)-1
    # max delta time between "expected" and "real"
    # for test_type greater than 1, delta time is lower
    time_distance = basic_distance
    if test_type == 2:
        time_distance = max(1, time_distance // 8)
    elif test_type == 3:
        time_distance = max(1, time_distance // 15)
    max_delta = 3
    if max_delta*2 > time_distance:
        # all wares are in time-sequence
        max_delta = 0
    # number of wares: higher test_type number  more wares
    number_of_wares = 200
    if test_type == 2:
        number_of_wares *= 4
    elif test_type == 3:
        number_of_wares *= 6
    # generate "random" events
    for itr in range(number_of_wares):
        # for STEP_TIME = 1.8 & basic_distance = 20
        # approximate time = 1.5 hours (to start all wares)
        new_ware = ware_class()
        # first: ports (start and destination)
        tmp1 = 0
        tmp2 = 0
        while tmp1 == tmp2:
            tmp1 = random.randint(0,port_list_last)
            tmp2 = random.randint(0,port_list_last)
        new_ware.set_ports(ports_list[tmp1],ports_list[tmp2])
        # then: time
        total_time_iterations += time_distance
        total_time_iterations += random.randint(-max_delta, max_delta)
        new_ware.set_time_begin(total_time_iterations*STEP_TIME)
        new_ware.description_debug+=str(itr+1)
        wares_list.append(new_ware)
    return wares_list

# ===========
#   TEST 5
# ===========
# first test not symmetrical
# ports: 7 ports, long distances, "random" position
# ships: two
# wares: high speed, 1200 wares
def ports_test5(port_class, basic_distance=40, test_type=1):
    port_list=[]
    # for test_type = 2 or 3: distance is multiplied by 2
    distance = basic_distance
    if test_type > 1:
        distance *= 2
    for itr in range(7):
        port_to_add=port_class()
        if itr == 0:
            port_to_add.set_coordinates([-distance//2,distance])# high production
        elif itr == 1:
            port_to_add.set_coordinates([-3*distance//2,0])# high production
        elif itr == 2:
            port_to_add.set_coordinates([0, -distance])# weak absorbtion
        elif itr == 3:
            port_to_add.set_coordinates([distance-3,-distance-3])# high absorption -> processing
        elif itr == 4:
            port_to_add.set_coordinates([distance+3,-distance+3])# high absorption -> processing
        elif itr == 5:
            port_to_add.set_coordinates([3*distance//2,distance])
        elif itr == 6:
            port_to_add.set_coordinates([0,0]) # central port
        port_to_add.description_debug+=str(itr+1)
        port_list.append(port_to_add)
    return port_list

def ships_test5(ship_class, ports_list, test_type=1):
    ships_list=[]
    # the number = 4, except test_type=3
    number_of_ships = 4
    if test_type == 3:
        number_of_ships = 2
    for itr in range(number_of_ships):
        ship_test=ship_class()
        port_near_ship=ports_list[random.randint(0,len(ports_list)-1)]
        ship_test.set_coordinates(port_near_ship.read_coordinates())
        ship_test.set_next_destination(port_near_ship)
        ship_test.set_next_destination(port_near_ship)
        ship_test.set_current_state(-1) # iddle
        ship_test.description_debug+=str(itr+1)
        ships_list.append(ship_test)
    return ships_list

def wares_test5(ware_class, ports_list, basic_distance=40, test_type=1):
    wares_list = []
    total_time_iterations = 0
    # for test_type greater than 1, delta time is lower
    time_distance = basic_distance
    if test_type == 2:
        time_distance = max(1, time_distance // 20)
    elif test_type == 3:
        time_distance = max(1, time_distance // 40)
    max_delta = 2
    if max_delta*2 > time_distance:
        # all wares are in time-sequence
        max_delta = 0
    # number of wares: higher test_type number  more wares
    number_of_wares = 200
    if test_type == 2:
        number_of_wares *= 2
    elif test_type == 3:
        number_of_wares *= 7
    # generate "random" events
    for itr1 in range(number_of_wares):
        # for STEP_TIME = 1.8
        # approximate time = 0.6 hours (to start all wares)
        new_ware = ware_class()
        port_check1 = random.randint(0,200)
        port_check2 = random.randint(0,200)
        tmp1 = 0
        if port_check1 < 80: # 40%
            tmp1 = 0
            if port_check2 < 90: # 45%
                tmp2 = 3
            elif port_check2 < 180: # 45%
                tmp2 = 4
            else: # 10%
                tmp2 = 5
        elif port_check1 < 160: # 40%
            tmp1 = 1
            if port_check2 < 90: # 45%
                tmp2 = 3
            elif port_check2 < 180: # 45%
                tmp2 = 4
            elif port_check2 < 194: # 7%
                tmp2 = 2
            else: # 3%
                tmp2 = 6
        elif port_check1 < 175: # 7.5%
            tmp1 = 3
            if port_check2 < 40: # 20%
                tmp2 = 0
            elif port_check2 < 80: # 20%
                tmp2 = 1
            elif port_check2 < 120: # 20%
                tmp2 = 2
            elif port_check2 < 160: # 20%
                tmp2 = 5
            else: # 10%
                tmp2 = 6
        elif port_check1 < 190: # 7.5%
            tmp1 = 4
            if port_check2 < 40: # 20%
                tmp2 = 0
            elif port_check2 < 80: # 20%
                tmp2 = 1
            elif port_check2 < 120: # 20%
                tmp2 = 2
            elif port_check2 < 160: # 20%
                tmp2 = 5
            else: # 10%
                tmp2 = 6
        else: # 5%
            tmp1 = 6
            if port_check2 < 40: # 20%
                tmp2 = 0
            elif port_check2 < 80: # 20%
                tmp2 = 1
            elif port_check2 < 120: # 20%
                tmp2 = 2
            elif port_check2 < 140: # 10%
                tmp2 = 3
            elif port_check2 < 160: # 10%
                tmp2 = 4
            else: # 10%
                tmp2 = 5
        if tmp1 == tmp2:
            print("ERROR: wrong start and destination settings for ware")
        new_ware.set_ports(ports_list[tmp1],ports_list[tmp2])
        # then: time
        total_time_iterations += time_distance
        total_time_iterations += random.randint(-max_delta, max_delta)
        new_ware.set_time_begin(total_time_iterations*STEP_TIME)
        new_ware.description_debug+=str(itr1+1)
        wares_list.append(new_ware)
    return wares_list