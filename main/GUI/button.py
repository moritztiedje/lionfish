from main.GUI.point import Point
from main.constants import WINDOW_HEIGHT


class Button:
    def __init__(self, bottom_left, top_right, image, action):
        """
        :type bottom_left: main.GUI.point.Point
        :type top_right: main.GUI.point.Point
        :type action: function
        """
        self.__bottom_left = bottom_left
        self.__top_right = top_right
        self.__image = image
        self.__action = action

    def handle_click(self, mouse_position):
        if mouse_position[0] >= self.__bottom_left.get_x() and \
                        mouse_position[0] <= self.__top_right.get_x() and \
                        WINDOW_HEIGHT - mouse_position[1] >= self.__bottom_left.get_y() and \
                        WINDOW_HEIGHT - mouse_position[1] <= self.__top_right.get_y():
            self.__action()

    def display(self, game_window):
        coordinate = Point(self.__bottom_left.get_x(), self.__top_right.get_y())
        game_window.display(self.__image, coordinate)
