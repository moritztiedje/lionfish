import pygame

from src.main.GUI.View.imageVaults.textAdventureImageVault import TextAdventureImageVault, TextAdventureImageEnum
from src.main.GUI.View.panels.panel import Panel
from src.main.Util.point import Point


class TextAdventurePanel(Panel):
    def __init__(self, game_window):
        """
        :type game_window: src.main.GUI.View.gameWindow.GameWindow
        """
        super().__init__(game_window, 1)
        self.__y_offset = 0

    def _handle_mouse_event(self, mouse_event):
        pass

    def _load_image_vault(self):
        return TextAdventureImageVault(self._game_window)

    def draw(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        super().draw(game_state)
        self.__y_offset = 0

        self._game_window.draw_absolute(self._image_vault.get(TextAdventureImageEnum.BACKGROUND), Point(0, 200))
        self._game_window.draw_absolute(self._image_vault.get(TextAdventureImageEnum.TOP_BORDER), Point(0, 220))

        self.__draw_text(game_state.get_text_adventure_state().get_text())
        for option in game_state.get_text_adventure_state().get_options():
            self.__draw_text(option, left_border=30)

    def __draw_text(self, text, left_border=20):
        height_of_line = 20
        font = pygame.font.SysFont("Times New Roman", height_of_line)
        right_border = 20
        width_of_space = font.size(' ')[0]
        max_width = self._game_window.get_width() - right_border - left_border

        length_of_current_line = 0
        words = text.split(' ')
        for word in words:
            rendered_word = font.render(word, 0, pygame.Color('black'))
            word_width = rendered_word.get_width()
            if length_of_current_line + word_width >= max_width:
                length_of_current_line = 0
                self.__y_offset += height_of_line
            self._game_window.draw_absolute(rendered_word,
                                            Point(left_border + length_of_current_line,
                                                  195 - self.__y_offset
                                                  )
                                            )
            length_of_current_line += word_width + width_of_space
        self.__y_offset += height_of_line
