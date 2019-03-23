from abc import ABCMeta, abstractmethod

from src.main.GUI.View.Util.hexagonClickBox import HexagonClickBox
from src.main.GUI.View.imageVault import AreaImageEnum, WorldImageEnum, AreaImageVault, WorldImageVault, MenuImageVault
from src.main.Util.point import Point
from src.main.constants import HEXAGON_FIELD_WIDTH_SPACING, HEXAGON_FIELD_HEIGHT, SQUARE_FIELD_WIDTH, \
    SQUARE_FIELD_HEIGHT, HEXAGON_FIELD_WIDTH, SPRITE_IN_HEXAGON_WIDTH, SPRITE_IN_HEXAGON_HEIGHT


class View(metaclass=ABCMeta):
    def __init__(self, game_window):
        """
        :type game_window: src.main.GUI.View.gameWindow.GameWindow
        """
        self._game_window = game_window
        self.__buttons = []
        self.__is_active = False
        self._camera_zoom = 1
        self._image_vault = None

    def is_active(self):
        return self.__is_active

    @abstractmethod
    def _load_image_vault(self):
        """
        :rtype: src.main.GUI.View.imageVault.ImageVault
        """
        return None

    def zoom_in(self):
        self._camera_zoom *= 2
        self._image_vault.set_camera_zoom(self._camera_zoom)

    def zoom_out(self):
        self._camera_zoom /= 2
        self._image_vault.set_camera_zoom(self._camera_zoom)

    def activate(self):
        self.__is_active = True
        self._image_vault = self._load_image_vault()

    def deactivate(self):
        self.__is_active = False
        self._image_vault = None

    def register_button(self, button):
        """
        :type button: main.GUI.button.Button
        """
        self.__buttons.append(button)

    def handle_click(self, mouse_clicked_position):
        for button in self.__buttons:
            button.handle_click(mouse_clicked_position)

    def handle_relative_click(self, relative_mouse_clicked_position):
        pass

    def display(self, game_state):
        """
        :type game_state: main.gameState.GameState
        """
        for button in self.__buttons:
            button.display(self._game_window)


class MenuView(View):
    def _load_image_vault(self):
        return MenuImageVault()


class AreaMapView(View):
    def __init__(self, game_window):
        super().__init__(game_window)
        self.__click_box = HexagonClickBox()
        self.__highlighted_field = None

    def _load_image_vault(self):
        return AreaImageVault()

    def display(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        super().display(game_state)

        area_map = game_state.get_area_map()
        for x in range(0, len(area_map)):
            for y in range(0, len(area_map[x])):
                current_field = Point(x, y)
                if area_map[x][y] == 0:
                    image_code = AreaImageEnum.WATER
                else:
                    image_code = AreaImageEnum.EMPTY

                if current_field == self.__highlighted_field:
                    self.__display_hexagon(self._image_vault.get_highlighted(image_code), Point(x, y))
                else:
                    self.__display_hexagon(self._image_vault.get(image_code), Point(x, y))

        player = game_state.get_player_position_in_area()
        self.__display_in_hexagon(self._image_vault.get(AreaImageEnum.PLAYER), player)

    def __display_hexagon(self, sprite, game_field):
        """
        :type game_field: src.main.Util.point.Point
        """
        x_coordinate = game_field.get_x() * HEXAGON_FIELD_WIDTH_SPACING * self._camera_zoom
        y_coordinate = game_field.get_y() * HEXAGON_FIELD_HEIGHT * self._camera_zoom
        if game_field.get_x() % 2 != 0:
            y_coordinate += HEXAGON_FIELD_HEIGHT / 2 * self._camera_zoom
        self._game_window.display(sprite, Point(x_coordinate, y_coordinate))

    def __display_in_hexagon(self, sprite, game_field):
        """
        :type sprite: pygame.Surface
        :type game_field: src.main.Util.point.Point
        """
        x_coordinate = game_field.get_x() * HEXAGON_FIELD_WIDTH_SPACING
        x_coordinate += (HEXAGON_FIELD_WIDTH - SPRITE_IN_HEXAGON_WIDTH) / 2
        x_coordinate *= self._camera_zoom

        y_coordinate = game_field.get_y() * HEXAGON_FIELD_HEIGHT
        y_coordinate += (SPRITE_IN_HEXAGON_HEIGHT - HEXAGON_FIELD_HEIGHT) / 2
        y_coordinate *= self._camera_zoom

        if game_field.get_x() % 2 != 0:
            y_coordinate += HEXAGON_FIELD_HEIGHT / 2 * self._camera_zoom
        self._game_window.display(sprite, Point(x_coordinate, y_coordinate))

    def handle_relative_click(self, mouse_position):
        hexagon_point = self.__click_box.get_hexagon(mouse_position)
        self.__highlighted_field = hexagon_point

    def zoom_in(self):
        super().zoom_in()
        self.__click_box.set_zoom_level(self._camera_zoom)

    def zoom_out(self):
        super().zoom_out()
        self.__click_box.set_zoom_level(self._camera_zoom)


class WorldMapView(View):
    def _load_image_vault(self):
        return WorldImageVault()

    def __init__(self, game_window):
        super().__init__(game_window)

    def display(self, game_state):
        """
        :type game_state: main.gameState.GameState
        """
        super().display(game_state)

        world_map = game_state.get_world_map()
        for x in range(0, len(world_map)):
            for y in range(0, len(world_map[x])):
                if world_map[x][y] == 1:
                    self.__display_square(self._image_vault.get(WorldImageEnum.LAND), Point(x, y))
                if world_map[x][y] == 0:
                    self.__display_square(self._image_vault.get(WorldImageEnum.WATER), Point(x, y))

    def __display_square(self, sprite, coordinate):
        """
        :type coordinate: main.GUI.point.Point
        """
        display_coordinate = Point(coordinate.get_x() * SQUARE_FIELD_WIDTH * self._camera_zoom,
                                   coordinate.get_y() * SQUARE_FIELD_HEIGHT * self._camera_zoom)
        self._game_window.display(sprite, display_coordinate)
