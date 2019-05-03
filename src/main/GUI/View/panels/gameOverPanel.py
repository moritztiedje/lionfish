import pygame

from src.main.GUI.BaseComponents.geometry import Point
from src.main.GUI.View.imageVaults.gameOverImageVault import GameOverImageVault
from src.main.GUI.View.panels.panel import Panel
from src.main.GUI.View.panels.textAdventurePanel import RenderedText
from src.main.constants import GameOverImageEnum


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

        sys_font = pygame.font.SysFont('Arial Black', 60)
        rendered_text = sys_font.render(game_state.get_game_over_text(), 0, pygame.Color('darkblue'))
        draw_coordinate_of_word = Point(
                (self._game_window.get_width() - rendered_text.get_width()) / 2,
                (self._game_window.get_height() + rendered_text.get_height()) / 2)
        self._game_window.draw(rendered_text, draw_coordinate_of_word)
