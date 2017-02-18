from abc import ABCMeta

from main.GUI.point import Point
from main.imageVault import ImageEnum


class View(metaclass=ABCMeta):
    def __init__(self, game_window):
        """
        :type game_window: main.gameWindow.GameWindow
        """
        self._game_window = game_window
        self.__buttons = []

    def register_button(self, button):
        """
        :type button: main.GUI.button.Button
        """
        self.__buttons.append(button)

    def handle_click(self, mouse_clicked_position):
        for button in self.__buttons:
            button.handle_click(mouse_clicked_position)

    def display(self, game_state):
        """
        :type game_state: main.gameState.GameState
        """
        for button in self.__buttons:
            button.display(self._game_window)


class MenuView(View):
    pass


class AreaMapView(View):
    def __init__(self, game_window):
        super().__init__(game_window)

        self.__border = ImageEnum.BORDER
        self.__water = ImageEnum.WATER

    def display(self, game_state):
        super().display(game_state)

        area_map = game_state.area_map
        for x in range(0, len(area_map)):
            for y in range(0, len(area_map[x])):
                if area_map[x][y] == 1:
                    self._game_window.display_hexagon(self.__border, Point(x, y))
                if area_map[x][y] == 0:
                    self._game_window.display_hexagon(self.__water, Point(x, y))


class WorldMapView(View):
    def __init__(self, game_window):
        super().__init__(game_window)

        self.__land = ImageEnum.WORLD_LAND
        self.__water = ImageEnum.WORLD_WATER

    def display(self, game_state):
        """
        :type game_state: main.gameState.GameState
        """
        super().display(game_state)

        world_map = game_state.get_world_map()
        for x in range(0, len(world_map)):
            for y in range(0, len(world_map[x])):
                if world_map[x][y] == 1:
                    self._game_window.display_square(self.__land, Point(x, y))
                if world_map[x][y] == 0:
                    self._game_window.display_square(self.__water, Point(x, y))
