from abc import ABCMeta
from enum import Enum

import pygame


class Click(metaclass=ABCMeta):
    def __init__(self, position, type):
        self.__position = position
        self.__type = type

    def getPosition(self):
        return self.__position

    def getType(self):
        return self.__type


class DoubleClick(Click):
    def __init__(self, position):
        super().__init__(position, MouseEventEnum.DoubleClick)


class LeftClick(Click):
    def __init__(self, position):
        super().__init__(position, MouseEventEnum.LeftClick)


class MouseEventEnum(Enum):
    DoubleClick = 2
    LeftClick = 1


class MouseController:
    def __init__(self, window_height):
        """
        :type window_height: int
        """
        self.__window_height = window_height

        self.__left_was_pressed = False
        self.__timestamp_of_last_click = 0

    def get_mouse_state(self):
        """
        :rtype: Click
        """
        left_mouse_is_pressed = self.__left_mouse_is_pressed()
        left_mouse_has_clicked = self.__left_was_pressed and not left_mouse_is_pressed
        left_mouse_has_double_clicked = self.__timestamp_of_last_click and left_mouse_has_clicked

        current_timestamp = pygame.time.get_ticks()

        if left_mouse_has_double_clicked:
            self.__reset()
            return DoubleClick(self.__get_inverted_mouse_position())

        if self.__timestamp_of_last_click:
            if current_timestamp - self.__timestamp_of_last_click > 150:
                self.__reset()
                return LeftClick(self.__get_inverted_mouse_position())

        if left_mouse_has_clicked:
            self.__timestamp_of_last_click = current_timestamp
        self.__left_was_pressed = self.__left_mouse_is_pressed()

    def __reset(self):
        self.__timestamp_of_last_click = 0
        self.__left_was_pressed = False

    @staticmethod
    def __left_mouse_is_pressed():
        return pygame.mouse.get_pressed()[0] == 1

    def __get_inverted_mouse_position(self):
        mouse_position = pygame.mouse.get_pos()
        inverted_mouse = mouse_position[0], self.__window_height - mouse_position[1]
        return inverted_mouse
