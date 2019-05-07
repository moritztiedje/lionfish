import pygame

from src.main.GUI.BaseComponents.geometry import Point


class LineRenderer:
    def __init__(self, font_name, font_size=10, color='black'):
        self.__font = pygame.font.SysFont(font_name, font_size)
        self.__color = pygame.Color('black')

    def render_line(self, draw_coordinate):
        return RenderedLine(draw_coordinate, self.__font)


class RenderedLine:
    def __init__(self, draw_coordinate, font):
        self.__words = []
        self.__current_word_x_position = 0
        self.__coordinate = draw_coordinate
        self.__space_width = font.render(" ", 0, pygame.Color('black')).get_width()

    def add(self, word_surface):
        word_draw_coordinate = Point(self.__current_word_x_position, 0) + self.__coordinate
        word = RenderedWord(word_surface, word_draw_coordinate)
        self.__words.append(word)

        self.__current_word_x_position += word_surface.get_width() + self.__space_width

    def draw(self, _draw_method):
        for word in self.__words:
            word.draw(_draw_method)

    def center(self, available_width):
        for word in self.__words:
            word.shift_right((available_width - self.get_width()) / 2)

    def word_makes_line_too_long(self, rendered_word, available_width):
        word_width = rendered_word.get_width()
        return self.__current_word_x_position + word_width >= available_width

    def get_width(self):
        width = 0
        for word in self.__words:
            width += word.get_width() + self.__space_width
        width -= self.__space_width
        return width

    def shift_right(self, shift_by):
        for rendered_word in self.__words:
            rendered_word.shift_right(shift_by)

    def shift_upwards(self, shift_by):
        for rendered_word in self.__words:
            rendered_word.shift_upwards(shift_by)


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
