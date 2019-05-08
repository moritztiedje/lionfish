import pygame

from src.main.GUI.BaseComponents.geometry import Point


class ParagraphRenderer:
    def __init__(self, font_name='Times New Roman', font_size=10, color='black'):
        self.__font_size = font_size
        self.__font = pygame.font.SysFont(font_name, font_size)

        self.__color = pygame.Color(color)

    def render_paragraph(self, text, draw_coordinate, right_border):
        return RenderedParagraph(text, draw_coordinate, right_border, self.__font, self.__font_size, self.__color)


class RenderedParagraph:
    def __init__(self, text, coordinate, right_border, font, font_size, color):
        """
        :type text: str
        """
        self.__lines = []
        self.__height = 0

        line_renderer = LineRenderer(font)

        current_line_coordinate = coordinate
        current_line = line_renderer.create_empty_line(current_line_coordinate, right_border)
        words = text.split(' ')
        for word_str in words:
            word = font.render(word_str, 0, color)
            if current_line.word_makes_line_too_long(word):
                self.__lines.append(current_line)
                current_line_coordinate -= Point(0, font_size)
                current_line = line_renderer.create_empty_line(current_line_coordinate, right_border)
            current_line.add(word)

        self.__height = coordinate.get_y() - current_line_coordinate.get_y() + font_size
        self.__lines.append(current_line)

    def align_text_center(self):
        for line in self.__lines:
            line.center()

    def draw(self, _draw_method):
        for line in self.__lines:
            line.draw(_draw_method)

    def get_height(self):
        return self.__height

    def shift_right(self, shift_by):
        for line in self.__lines:
            line.shift_right(shift_by)

    def shift_upwards(self, shift_by):
        for rendered_line in self.__lines:
            rendered_line.shift_upwards(shift_by)


class LineRenderer:
    def __init__(self, font):
        self.__font = font

    def create_empty_line(self, draw_coordinate, right_border):
        return RenderedLine(draw_coordinate, right_border, self.__font)


class RenderedLine:
    def __init__(self, draw_coordinate, right_border, font):
        self.__words = []
        self.__current_word_x_position = 0
        self.__coordinate = draw_coordinate
        self.__available_width = right_border - draw_coordinate.get_x()
        self.__space_width = font.render(" ", 0, pygame.Color('black')).get_width()

    def add(self, word_surface):
        word_draw_coordinate = Point(self.__current_word_x_position, 0) + self.__coordinate
        word = RenderedWord(word_surface, word_draw_coordinate)
        self.__words.append(word)

        self.__current_word_x_position += word_surface.get_width() + self.__space_width

    def draw(self, _draw_method):
        for word in self.__words:
            word.draw(_draw_method)

    def center(self):
        for word in self.__words:
            word.shift_right((self.__available_width - self.get_width()) / 2)

    def word_makes_line_too_long(self, rendered_word):
        word_width = rendered_word.get_width()
        return self.__current_word_x_position + word_width >= self.__available_width

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
