from abc import ABCMeta
from enum import Enum

from src.main.GUI.BaseComponents.geometry import Point


class MouseEventTypes(Enum):
    LeftClick = 1
    DoubleClick = 2
    Hover = 3


class MouseEvent(metaclass=ABCMeta):
    def __init__(self, position, event_type):
        """
        :type position: src.main.GUI.BaseComponents.geometry.Point
        :type event_type: MouseEventTypes
        """
        self.__position = position
        self.__type = event_type
        self.__relative_position = Point(0, 0)

    def get_position(self):
        """
        :rtype: src.main.GUI.BaseComponents.geometry.Point
        """
        return self.__position

    def get_relative_position(self):
        """
        :rtype: (int, int)
        """
        return self.__relative_position

    def set_relative_position(self, position):
        """
        :type position: src.main.GUI.BaseComponents.geometry.Point
        """
        self.__relative_position = position

    def get_type(self):
        """
        :rtype: MouseEventTypes
        """
        return self.__type


class DoubleClick(MouseEvent):
    def __init__(self, position):
        """
        :type position: src.main.GUI.BaseComponents.geometry.Point
        """
        super().__init__(position, MouseEventTypes.DoubleClick)


class LeftClick(MouseEvent):
    def __init__(self, position):
        """
        :type position: src.main.GUI.BaseComponents.geometry.Point
        """
        super().__init__(position, MouseEventTypes.LeftClick)


class Hover(MouseEvent):
    def __init__(self, position):
        """
        :type position: src.main.GUI.BaseComponents.geometry.Point
        """
        super().__init__(position, MouseEventTypes.Hover)
