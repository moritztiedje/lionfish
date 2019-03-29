from src.main.GUI.BaseComponents.geometry import Point


class Player:
    def __init__(self):
        self.__destination = None
        self.__position_in_world = Point(0, 0)
        self.__position_in_area = Point(1, 1)

    def get_position_in_world(self):
        return self.__position_in_world

    def get_position_in_area(self):
        return self.__position_in_area

    def set_destination(self, destination):
        self.__destination = destination

    def get_destination(self):
        return self.__destination

    def move_to_destination(self):
        self.__position_in_area = self.__destination
