import pygame

from src.main.GUI.BaseComponents.button import Button
from src.main.GUI.BaseComponents.geometry import Point
from src.main.GUI.View.image import Image
from src.main.GUI.View.imageVaults.menuImageVault import MenuImageVault
from src.main.GUI.View.panels.panel import Panel


class MenuPanel(Panel):
    def __init__(self, game_window, zoom_in, zoom_out):
        """
        :type game_window: src.main.GUI.View.gameWindow.GameWindow
        """
        super().__init__(game_window, 1)
        main_menu_button = Button(Point(game_window.get_width() - 40, game_window.get_height() - 40),
                                  Point(game_window.get_width() - 10, game_window.get_height() - 10),
                                  Image(0, 0, '../../artwork/images/menu/gear.png'),
                                  self.__quit_game)
        zoom_in_button = Button(Point(game_window.get_width() - 40, game_window.get_height() - 80),
                                Point(game_window.get_width() - 10, game_window.get_height() - 50),
                                Image(0, 0, '../../artwork/images/menu/magnify.png'),
                                zoom_in)
        zoom_out_button = Button(Point(game_window.get_width() - 40, game_window.get_height() - 120),
                                 Point(game_window.get_width() - 10, game_window.get_height() - 90),
                                 Image(0, 0, '../../artwork/images/menu/reduce.png'),
                                 zoom_out)
        self._register_button(main_menu_button)
        self._register_button(zoom_in_button)
        self._register_button(zoom_out_button)

    @staticmethod
    def __quit_game():
        pygame.quit()
        quit()

    def _handle_mouse_event(self, mouse_event):
        pass

    def _load_image_vault(self):
        return MenuImageVault()
