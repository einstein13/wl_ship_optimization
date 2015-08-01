def find_distance(point1, point2):
    """
    this function finds the min distance between two points in triangle-shaped map:
    2: 0   1   2
    1:   0   1
    0: 0   1   2
    """
    starting_point=[point1[0],point1[1]]
    y_distance = point2[1]-point1[1]
    x_distance = point2[0]-point1[0]
    return abs(x_distance)+abs(y_distance)