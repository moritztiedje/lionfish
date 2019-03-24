from src.main.Util.point import Point


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
        if self.__bottom_left.get_x() <= mouse_position[0] <= self.__top_right.get_x() and \
                                self.__bottom_left.get_y() <= mouse_position[1] <= self.__top_right.get_y():
            self.__action()

    def display(self, game_window):
        coordinate = Point(self.__bottom_left.get_x(), self.__top_right.get_y())
        game_window.display_absolute(self.__image.sprite, coordinate)
