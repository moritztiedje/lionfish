from src.main.GUI.BaseComponents.geometry import Point


class Player:
    def __init__(self):
        self.__destination = Point(1, 1)
        self.__position_in_world = Point(0, 0)
        self.__position_in_area = Point(4, 4)

    def get_position_in_world(self):
        return self.__position_in_world

    def get_position_in_area(self):
        return self.__position_in_area

    def set_destination(self, destination):
        """
        :type destination: src.main.GUI.BaseComponents.geometry.Point
        """
        self.__destination = destination

    def get_destination(self):
        """
        :rtype: src.main.GUI.BaseComponents.geometry.Point
        """
        return self.__destination

    def move_to_destination(self):
        self.__position_in_area = self.__destination

    def get_absolute_skill_level(self, skill):
        # Empty stub, since there is no skill system yet
        return 1
