import pygame

from src.main.GUI.View.Util.hexagonClickBox import HexagonClickBox
from src.main.GUI.View.imageVaults.textAdventureImageVault import TextAdventureImageVault, TextAdventureImageEnum
from src.main.GUI.View.panels.panel import Panel
from src.main.Util.point import Point


class TextAdventurePanel(Panel):
    def _load_image_vault(self):
        return TextAdventureImageVault(self._game_window)

    def __init__(self, game_window):
        super().__init__(game_window)
        self.__click_box = HexagonClickBox()
        self.__highlighted_field = None

    def draw(self, game_state):
        super().draw(game_state)
        font = pygame.font.SysFont("Times New Roman", 20)
        something = font.render("Something", 1, (255, 0, 0))
        self._game_window.draw_absolute(self._image_vault.get(TextAdventureImageEnum.BACKGROUND), Point(0, 200))
        self._game_window.draw_absolute(self._image_vault.get(TextAdventureImageEnum.TOP_BORDER), Point(0, 220))
        self._game_window.draw_absolute(something, Point(20, 195))
