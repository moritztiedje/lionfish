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
        self.__current_offset = 0

    def _handle_mouse_event(self, mouse_event):
        pass

    def _load_image_vault(self):
        return TextAdventureImageVault(self._game_window)

    def draw(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        super().draw(game_state)

        self._game_window.draw_absolute(self._image_vault.get(TextAdventureImageEnum.BACKGROUND), Point(0, 200))
        self._game_window.draw_absolute(self._image_vault.get(TextAdventureImageEnum.TOP_BORDER), Point(0, 220))

        self.__draw_text(game_state.get_text_adventure_state().get_text())
        for option in game_state.get_text_adventure_state().get_options():
            self.__draw_option(option)

    def __draw_text(self, text):
        font = pygame.font.SysFont("Times New Roman", 20)
        rendered_text = font.render(text, 1, (255, 0, 0))
        self._game_window.draw_absolute(rendered_text, Point(20, 195 - self.__current_offset))
        self.__current_offset += 20

    def __draw_option(self, option):
        font = pygame.font.SysFont("Times New Roman", 20)
        rendered_text = font.render(option, 1, (0, 0, 0))
        self._game_window.draw_absolute(rendered_text, Point(30, 195 - self.__current_offset))
        self.__current_offset += 20
