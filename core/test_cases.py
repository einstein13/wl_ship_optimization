import random
from settings import STEP_TIME

# ===========
#   TEST 1
# ===========
# ports: single line A --- B --- C
# ships: one ship
# wares: 200 wares, low speed

def ports_test1(port_class, basic_distance):
    port_list=[]
    for itr in range(-1,2):
        port_to_add=port_class()
        port_to_add.set_coordinates([basic_distance*itr,0])
        port_to_add.description_debug+=str(itr)
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
    ship_test.description_debug+="1"
    ships_list.append(ship_test)
    return ships_list

def wares_test1(ware_class, ports_list, basic_distance):
    wares_list = []
    total_time_iterations = 0
    port_list_last = len(ports_list)-1
    # max delta time between "expected" and "real"
    time_distance = basic_distance
    max_delta = 5
    if max_delta*2 > time_distance:
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

def ports_test2(port_class, basic_distance):
    port_list=[]
    for itr in range(3):
        port_to_add=port_class()
        if itr == 0:
            port_to_add.set_coordinates([basic_distance,0])
        elif itr == 1:
            port_to_add.set_coordinates([basic_distance//2,basic_distance])
        elif itr == 2:
            port_to_add.set_coordinates([0,0])
        port_to_add.description_debug+=str(itr+1)
        port_list.append(port_to_add)
    return port_list

def ships_test2(ship_class, ports_list):
    ships_list=[]
    ship_test=ship_class()
    port_near_ship=ports_list[0]
    ship_test.set_coordinates(port_near_ship.read_coordinates())
    ship_test.set_next_destination(port_near_ship)
    ship_test.set_next_destination(port_near_ship)
    ship_test.set_current_state(-1) # iddle
    ship_test.description_debug+="1"
    ships_list.append(ship_test)
    return ships_list

def wares_test2(ware_class, ports_list, basic_distance):
    wares_list = []
    total_time_iterations = 0
    port_list_last = len(ports_list)-1
    # max delta time between "expected" and "real"
    time_distance = basic_distance//4
    max_delta = 5
    if max_delta*2 > basic_distance:
        # all wares are in time-sequence
        max_delta = 0
    # generate "random" events
    for itr in range(500):
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
def ports_test3(port_class, basic_distance):
    port_list=[]
    for itr in range(6):
        port_to_add=port_class()
        if itr == 0:
            port_to_add.set_coordinates([basic_distance,0])
        elif itr == 1:
            port_to_add.set_coordinates([basic_distance//2,basic_distance])
        elif itr == 2:
            port_to_add.set_coordinates([basic_distance//2-basic_distance,basic_distance])
        elif itr == 3:
            port_to_add.set_coordinates([-basic_distance,0])
        elif itr == 4:
            port_to_add.set_coordinates([basic_distance//2-basic_distance,-basic_distance])
        elif itr == 5:
            port_to_add.set_coordinates([basic_distance//2,-basic_distance])
        port_to_add.description_debug+=str(itr+1)
        port_list.append(port_to_add)
    return port_list

def ships_test3(ship_class, ports_list):
    ships_list=[]
    for itr in range(2):
        ship_test=ship_class()
        port_near_ship=ports_list[random.randint(0,len(ports_list)-1)]
        ship_test.set_coordinates(port_near_ship.read_coordinates())
        ship_test.set_next_destination(port_near_ship)
        ship_test.set_next_destination(port_near_ship)
        ship_test.set_current_state(-1) # iddle
        ship_test.description_debug+=str(itr+1)
        ships_list.append(ship_test)
    return ships_list

def wares_test3(ware_class, ports_list, basic_distance):
    wares_list = []
    total_time_iterations = 0
    port_list_last = len(ports_list)-1
    # max delta time between "expected" and "real"
    time_distance = basic_distance//2
    max_delta = 3
    # generate "random" events
    for itr in range(300):
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
def ports_test4(port_class, basic_distance):
    port_list=[]
    for itr in range(4):
        port_to_add=port_class()
        if itr == 0:
            port_to_add.set_coordinates([basic_distance,0])
        elif itr == 1:
            port_to_add.set_coordinates([basic_distance,10])
        elif itr == 2:
            port_to_add.set_coordinates([-basic_distance,10])
        elif itr == 3:
            port_to_add.set_coordinates([-basic_distance,0])
        port_to_add.description_debug+=str(itr+1)
        port_list.append(port_to_add)
    return port_list

def ships_test4(ship_class, ports_list):
    ships_list=[]
    for itr in range(2):
        ship_test=ship_class()
        port_near_ship=ports_list[random.randint(0,len(ports_list)-1)]
        ship_test.set_coordinates(port_near_ship.read_coordinates())
        ship_test.set_next_destination(port_near_ship)
        ship_test.set_next_destination(port_near_ship)
        ship_test.set_current_state(-1) # iddle
        ship_test.description_debug+=str(itr+1)
        ships_list.append(ship_test)
    return ships_list

def wares_test4(ware_class, ports_list, basic_distance):
    wares_list = []
    total_time_iterations = 0
    port_list_last = len(ports_list)-1
    # max delta time between "expected" and "real"
    time_distance = basic_distance//4
    max_delta = 3
    if max_delta > time_distance:
        max_delta = 0
    # generate "random" events
    for itr in range(300):
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
def ports_test5(port_class, basic_distance):
    port_list=[]
    for itr in range(7):
        port_to_add=port_class()
        if itr == 0:
            port_to_add.set_coordinates([-basic_distance//2,basic_distance])# high production
        elif itr == 1:
            port_to_add.set_coordinates([-3*basic_distance//2,0])# high production
        elif itr == 2:
            port_to_add.set_coordinates([0, -basic_distance])# weak absorbtion
        elif itr == 3:
            port_to_add.set_coordinates([basic_distance-3,-basic_distance-3])# high absorption -> processing
        elif itr == 4:
            port_to_add.set_coordinates([basic_distance+3,-basic_distance+3])# high absorption -> processing
        elif itr == 5:
            port_to_add.set_coordinates([3*basic_distance//2,basic_distance])
        elif itr == 6:
            port_to_add.set_coordinates([0,0]) # central port
        port_to_add.description_debug+=str(itr+1)
        port_list.append(port_to_add)
    return port_list

def ships_test5(ship_class, ports_list):
    ships_list=[]
    for itr in range(2):
        ship_test=ship_class()
        port_near_ship=ports_list[random.randint(0,len(ports_list)-1)]
        ship_test.set_coordinates(port_near_ship.read_coordinates())
        ship_test.set_next_destination(port_near_ship)
        ship_test.set_next_destination(port_near_ship)
        ship_test.set_current_state(-1) # iddle
        ship_test.description_debug+=str(itr+1)
        ships_list.append(ship_test)
    return ships_list

def wares_test5(ware_class, ports_list, basic_distance):
    wares_list = []
    total_time_iterations = 0
    time_distance = 1
    max_delta = 0
    # generate "random" events
    for itr1 in range(1200):
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