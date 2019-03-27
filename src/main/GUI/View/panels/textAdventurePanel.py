import pygame

from src.main.GUI.View.imageVaults.textAdventureImageVault import TextAdventureImageVault, TextAdventureImageEnum
from src.main.GUI.View.panels.panel import Panel
from src.main.Util.point import Point

BOTTOM_BORDER = 10
TOP_BORDER = 10
RIGHT_BORDER = 20
LEFT_BORDER = 20
HEIGHT_OF_LINE = 20


class TextAdventurePanel(Panel):

    def __init__(self, game_window):
        """
        :type game_window: src.main.GUI.View.gameWindow.GameWindow
        """
        super().__init__(game_window, 1)
        self.__y_offset = 0
        self.__height = 200

    def _handle_mouse_event(self, mouse_event):
        pass

    def _load_image_vault(self):
        """
        :rtype: src.main.GUI.View.imageVaults.textAdventureImageVault.TextAdventureImageVault
        """
        return TextAdventureImageVault(self._game_window)

    def draw(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        super().draw(game_state)
        self.__draw_background()
        self.__draw_content(game_state)

        if self.__y_offset > self.__height - TOP_BORDER - BOTTOM_BORDER:
            self.__height = self.__y_offset + TOP_BORDER + BOTTOM_BORDER
            background = self._image_vault.get_image(TextAdventureImageEnum.BACKGROUND)
            background.scale_to_height(self.__height)
            self.__draw_background()
            self.__draw_content(game_state)

    def __draw_background(self):
        self.__y_offset = 0

        self._game_window.draw_absolute(
                self._image_vault.get_sprite(TextAdventureImageEnum.BACKGROUND),
                Point(0, self.__height)
        )
        border_height = self._image_vault.get_image(TextAdventureImageEnum.TOP_BORDER).get_height()
        self._game_window.draw_absolute(
                self._image_vault.get_sprite(TextAdventureImageEnum.TOP_BORDER),
                Point(0, self.__height + border_height)
        )

    def __draw_content(self, game_state):
        self.__draw_string(game_state.get_text_adventure_state().get_text())
        for option in game_state.get_text_adventure_state().get_options():
            self.__draw_string(option, line_offset=10)

    def __draw_string(self, text, line_offset=0):
        font = pygame.font.SysFont("Times New Roman", HEIGHT_OF_LINE)
        width_of_space = font.size(' ')[0]
        max_width = self._game_window.get_width() - RIGHT_BORDER - LEFT_BORDER - line_offset

        length_of_current_line = 0
        words = text.split(' ')
        for word in words:
            rendered_word = font.render(word, 0, pygame.Color('black'))
            word_width = rendered_word.get_width()
            if length_of_current_line + word_width >= max_width:
                length_of_current_line = 0
                self.__y_offset += HEIGHT_OF_LINE
            self._game_window.draw_absolute(rendered_word,
                                            Point(LEFT_BORDER + line_offset + length_of_current_line,
                                                  self.__height - TOP_BORDER - self.__y_offset
                                                  )
                                            )
            length_of_current_line += word_width + width_of_space
        self.__y_offset += HEIGHT_OF_LINE
