# unit tests for classes.py
ERROR = "\tERR: common.classes: "
BEGIN_TEXT = "common.classes."
END_TEXT =  " TESTS FINISHED"
from settings import VELOCITY
from common.classes import Description, Coordinates, TimeDistanceStatistics, ListOfWares

def test_Description():
    des = Description()
    des.description_short="short"
    des.description_full="long"

    if des.read_full_description()!="long":
        print(ERROR+"Description (1): read_full_description wrong result")
    if des.read_short_description()!="short":
        print(ERROR+"Description (2): read_short_description wrong result")

    des_copy = Description()
    des.copy_Description(des_copy)

    if des_copy.read_full_description()!="long":
        print(ERROR+"Description (3): read_full_description wrong result")
    if des_copy.read_short_description()!="short":
        print(ERROR+"Description (4): read_short_description wrong result")

    des.description_full+=" change"
    des.description_short+=" change"

    if des.read_full_description()!="long change":
        print(ERROR+"Description (5): read_full_description wrong result")
    if des.read_short_description()!="short change":
        print(ERROR+"Description (6): read_short_description wrong result")
    if des_copy.read_full_description()!="long":
        print(ERROR+"Description (7): read_full_description wrong result")
    if des_copy.read_short_description()!="short":
        print(ERROR+"Description (8): read_short_description wrong result")
    if des_copy.read_short_description()==des.read_short_description():
        print(ERROR+"Description (9): read_short_description wrong result")
    if des_copy.read_full_description()==des.read_full_description():
        print(ERROR+"Description (10): read_full_description wrong result")
    print(BEGIN_TEXT+"Description"+END_TEXT)

def test_Coordinates():
    coord = Coordinates()
    coord.coordinates[0]=10
    coord.coordinates[1]=-19

    if coord.read_coordinates()!=[10,-19]:
        print(ERROR+"Coordinates (1): read_coordinates wrong result")

    if coord.set_coordinates([-1,1])!=[-1,1]:
        print(ERROR+"Coordinates (2): set_coordinates wrong result")
    if coord.read_coordinates()!=[-1,1]:
        print(ERROR+"Coordinates (3): read_coordinates wrong result")

    if coord.distance_between_point([0,-1])!=2:
        print(ERROR+"Coordinates (4): distance_between_point wrong result")

    coord2 = Coordinates()
    coord.copy_Coordinates(coord2)

    if coord.read_coordinates()!=coord2.read_coordinates():
        print(ERROR+"Coordinates (5): read_coordinates wrong result")
    if coord.distance_between_point(coord2.read_coordinates())!=0:
        print(ERROR+"Coordinates (6): distance_between_point wrong result")

    coord2.set_coordinates([0,-1])

    if coord.read_coordinates()==coord2.read_coordinates():
        print(ERROR+"Coordinates (7): read_coordinates wrong result")
    if coord.distance_between_point(coord2.read_coordinates())!=2:
        print(ERROR+"Coordinates (8): distance_between_point wrong result")

    print(BEGIN_TEXT+"Coordinates"+END_TEXT)

def test_TimeDistanceStatistics():
    tim = TimeDistanceStatistics()
    tim.total_distance_traveling = 10
    tim.total_time_traveling = 10*VELOCITY

    print(BEGIN_TEXT+"TimeDistanceStatistics"+END_TEXT)

def test_ListOfWares():

    print(BEGIN_TEXT+"ListOfWares"+END_TEXT)

def test_all():
    test_Description()
    test_Coordinates()
    test_TimeDistanceStatistics()
    test_ListOfWares()