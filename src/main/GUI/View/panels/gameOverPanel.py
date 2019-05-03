import pygame

from src.main.GUI.BaseComponents.geometry import Point
from src.main.GUI.View.imageVaults.gameOverImageVault import GameOverImageVault
from src.main.GUI.View.panels.panel import Panel
from src.main.GUI.View.panels.textAdventurePanel import RenderedText
from src.main.constants import GameOverImageEnum

HEIGHT_OF_LINE = 60
FONT = 'Arial Black'
TEXT_COLOR = 'darkblue'


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

        available_text_width = self._game_window.get_width() - 200
        text = RenderedLine(game_state.get_game_over_text(), available_text_width)
        draw_coordinate_of_word = Point(
                (self._game_window.get_width() - text.get_width()) / 2,
                (self._game_window.get_height() + text.get_height()) / 2)
        text.draw(draw_coordinate_of_word, self._game_window.draw)


class RenderedLine:
    def __init__(self, text, available_width):
        """
        :type text: str
        :type available_width: int
        """
        self.__words = []
        self.__height = 0
        self.__width = available_width

        font = pygame.font.SysFont(FONT, HEIGHT_OF_LINE)
        text_color = pygame.Color(TEXT_COLOR)

        words = text.split(' ')
        draw_coordinate_of_word = Point(0, 0)
        draw_coordinate_of_next_word = Point(0, 0)
        space_width = font.render(" ", 0, pygame.Color('black')).get_width()
        for word in words:
            rendered_word = font.render(word, 0, text_color)
            word_width = rendered_word.get_width()
            if draw_coordinate_of_word.get_x() + word_width >= available_width:
                draw_coordinate_of_word = Point(0, draw_coordinate_of_word.get_y() - HEIGHT_OF_LINE)
            draw_coordinate_of_next_word = draw_coordinate_of_word + Point(word_width + space_width, 0)
            self.__words.append(RenderedWord(rendered_word, draw_coordinate_of_word))
            self.__width = max(draw_coordinate_of_word.get_x(), self.__width)

            draw_coordinate_of_word = draw_coordinate_of_next_word

        self.__height = HEIGHT_OF_LINE - draw_coordinate_of_next_word.get_y()

    def draw(self, coordinate, _draw_method):
        for word in self.__words:
            word.draw(coordinate, _draw_method)

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width


class RenderedWord:
    def __init__(self, word, draw_coordinate):
        """
        :type word: pygame.ftfont.Font
        :type draw_coordinate: src.main.GUI.BaseComponents.geometry.Point
        """
        self.__rendered_word = word
        self.__draw_coordinate = draw_coordinate

    def draw(self, coordinate, _draw_relative_to_camera):
        draw_coordinate = coordinate + self.__draw_coordinate
        _draw_relative_to_camera(self.__rendered_word, draw_coordinate)
