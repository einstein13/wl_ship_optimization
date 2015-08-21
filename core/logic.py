def find_distance(point1, point2):
    """
    this function finds the min distance between two points in triangle-shaped map:
     2: 0   1   2
     1:   0   1
     0: 0   1   2
    -1:   0   1
    -2: 0   1   2
    main idea is to go top-right y-times to reach the correct height
    then go right to the second point
    when going down, first direction is to the left.
    To solve the problem basic geometry is needed.
    """
    starting_point=[point1[0],point1[1]]
    y_distance = point2[1]-point1[1]
    x_distance = point2[0]-point1[0]
    if y_distance > 0:
        x_tmp = y_distance // 2
        if (y_distance % 2 == 1) and (starting_point[1] % 2 == 1):
            x_tmp += 1
        if x_tmp-y_distance <= x_distance and x_distance <= x_tmp:
            # second point is above first one 
            # between top-right and top-left lines
            return y_distance
        if x_distance > 0:
            # second poitn is to the right
            return y_distance + x_distance - x_tmp
        # second point is to the left
        return - x_distance + x_tmp
    if y_distance < 0:
        x_tmp = y_distance // 2
        if (y_distance % 2 == 1) and (starting_point[1] % 2 == 1):
            x_tmp += 1
        if x_tmp <= x_distance and x_distance <= x_tmp-y_distance:
            # second point is below the first one
            return -y_distance
        if x_distance < 0:
            # second point is to the left
            return - y_distance - x_distance + x_tmp
        # second point is to the right
        return x_distance - x_tmp
    # this point is reached when y_distance == 0
    return abs(x_distance)

def find_distance_between_ports(port1, port2):
    coordinates1 = port1.read_coordinates()
    coordinates2 = port2.read_coordinates()
    return find_distance(coordinates1, coordinates2)

def calculate_route_length(list_of_ports):
    if len(list_of_ports)<2:
        return 0
    length=0
    for itr in range(len(list_of_ports)-1):
        length += find_distance_between_ports(list_of_ports[itr], list_of_ports[itr+1])
    return length
