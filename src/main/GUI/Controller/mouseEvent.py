from abc import ABCMeta
from enum import Enum


class MouseEventEnum(Enum):
    DoubleClick = 2
    LeftClick = 1


class MouseEvent(metaclass=ABCMeta):
    def __init__(self, position, event_type):
        """
        :type position: (int, int)
        :type event_type: MouseEventEnum
        """
        self.__position = position
        self.__type = event_type
        self.__relative_position = (0, 0)

    def get_position(self):
        """
        :rtype: (int, int)
        """
        return self.__position

    def get_relative_position(self):
        """
        :rtype: (int, int)
        """
        return self.__relative_position

    def set_relative_position(self, position):
        """
        :type position: (int, int)
        """
        self.__relative_position = position

    def get_type(self):
        """
        :rtype: MouseEventEnum
        """
        return self.__type


class DoubleClick(MouseEvent):
    def __init__(self, position):
        """
        :type position: (int, int)
        """
        super().__init__(position, MouseEventEnum.DoubleClick)


class LeftClick(MouseEvent):
    def __init__(self, position):
        """
        :type position: (int, int)
        """
        super().__init__(position, MouseEventEnum.LeftClick)
