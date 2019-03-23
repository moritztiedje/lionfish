from src.main.Util.point import Point


class Player:
    def __init__(self):
        self.__position_in_world = Point(0, 0)
        self.__position_in_area = Point(0, 0)

    def get_position_in_world(self):
        return self.__position_in_world

    def get_position_in_area(self):
        return self.__position_in_area