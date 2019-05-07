from src.main.GUI.BaseComponents.geometry import Point


class RenderedWord:
    def __init__(self, word, draw_coordinate):
        self.__rendered_word = word
        self.__draw_coordinate = draw_coordinate

    def draw(self, draw_method):
        draw_method(self.__rendered_word, self.__draw_coordinate)

    def shift_right(self, shift_by):
        self.__draw_coordinate += Point(shift_by, 0)

    def shift_upwards(self, shift_by):
        """
        :type shift_by: int
        """
        self.__draw_coordinate += Point(0, shift_by)

    def get_width(self):
        return self.__rendered_word.get_width()
