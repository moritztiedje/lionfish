import pygame

from src.main.GUI.BaseComponents.geometry import Point
from src.main.GUI.View.imageVaults.gameOverImageVault import GameOverImageVault
from src.main.GUI.View.panels.panel import Panel
from src.main.constants import GameOverImageEnum

HEIGHT_OF_LINE = 60
FONT = 'Arial Black'
TEXT_COLOR = 'darkblue'
SIDE_MARGIN = 100


class GameOverPanel(Panel):
    def __init__(self, game_window):
        super().__init__(game_window, 2)

    def _load_image_vault(self):
        return GameOverImageVault()

    def handle_key_event(self, key_event):
        pass

    def _handle_mouse_event(self, mouse_event):
        pass

    def draw(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        super().draw(game_state)

        background = self._get_image_vault().get_image(GameOverImageEnum.BACKGROUND)
        background.scale_to_height(self._game_window.get_height())
        background.scale_to_width(self._game_window.get_width())
        self._game_window.draw(background.sprite, Point(0, self._game_window.get_height()))

        available_text_width = self._game_window.get_width() - SIDE_MARGIN * 2
        text = RenderedText(game_state.get_game_over_text(), available_text_width)
        draw_coordinate_of_word = Point(
                SIDE_MARGIN,
                (self._game_window.get_height() + text.get_height()) / 2)
        text.draw(draw_coordinate_of_word, self._game_window.draw)


class RenderedText:
    def __init__(self, text, available_width):
        """
        :type text: str
        :type available_width: int
        """
        self.__lines = []
        self.__height = 0

        font = pygame.font.SysFont(FONT, HEIGHT_OF_LINE)
        text_color = pygame.Color(TEXT_COLOR)

        current_line_number = 0
        current_line = RenderedLine(current_line_number)
        words = text.split(' ')
        for word_str in words:
            word = font.render(word_str, 0, text_color)
            if current_line.word_makes_line_too_long(word, available_width):
                current_line.center(available_width)
                self.__lines.append(current_line)
                current_line_number += 1
                current_line = RenderedLine(current_line_number)
            current_line.add(word)

        self.__height = HEIGHT_OF_LINE * (current_line_number + 1)
        current_line.center(available_width)
        self.__lines.append(current_line)

    def draw(self, coordinate, _draw_method):
        for line in self.__lines:
            line.draw(coordinate, _draw_method)

    def get_height(self):
        return self.__height


class RenderedLine:
    def __init__(self, line_number):
        self.__words = []
        self.__current_word_x_position = 0
        self.__y_coordinate = - line_number * HEIGHT_OF_LINE

    def add(self, word_surface):
        word_draw_coordinate = Point(self.__current_word_x_position, self.__y_coordinate)
        word = RenderedWord(word_surface, word_draw_coordinate)
        self.__words.append(word)

        font = pygame.font.SysFont(FONT, HEIGHT_OF_LINE)
        space_width = font.render(" ", 0, pygame.Color('black')).get_width()
        self.__current_word_x_position += word_surface.get_width() + space_width

    def draw(self, coordinate, _draw_method):
        for word in self.__words:
            word.draw(coordinate, _draw_method)

    def center(self, available_width):
        last_word = self.__words[len(self.__words) - 1]
        line_width = last_word.get_right_side()
        for word in self.__words:
            word.shift_right((available_width - line_width) / 2)

    def word_makes_line_too_long(self, rendered_word, available_width):
        word_width = rendered_word.get_width()
        return self.__current_word_x_position + word_width >= available_width


class RenderedWord:
    def __init__(self, word, draw_coordinate):
        self.__rendered_word = word
        self.__draw_coordinate = draw_coordinate

    def draw(self, coordinate, draw_method):
        draw_coordinate = coordinate + self.__draw_coordinate
        print(draw_coordinate.get_x())
        draw_method(self.__rendered_word, draw_coordinate)

    def shift_right(self, shift_by):
        self.__draw_coordinate += Point(shift_by, 0)

    def get_right_side(self):
        return self.__draw_coordinate.get_x() + self.__rendered_word.get_width()

    def get_width(self):
        return self.__rendered_word.get_width()
