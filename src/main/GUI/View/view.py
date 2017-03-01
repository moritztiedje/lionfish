from abc import ABCMeta, abstractmethod

from src.main.GUI.BaseComponents.point import Point
from src.main.GUI.View.imageVault import AreaImageEnum, WorldImageEnum, AreaImageVault, WorldImageVault, MenuImageVault
from src.main.constants import HEXAGON_FIELD_WIDTH_SPACING, HEXAGON_FIELD_HEIGHT, SQUARE_FIELD_WIDTH, \
    SQUARE_FIELD_HEIGHT, HEXAGON_FIELD_WIDTH, HEXAGON_FIELD_SIDE_WIDTH, HEXAGON_FIELD_CENTER_WIDTH


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
                if area_map[x][y] == 1:
                    self.__display_hexagon(self._image_vault.get(AreaImageEnum.BORDER), Point(x, y))
                if area_map[x][y] == 0:
                    self.__display_hexagon(self._image_vault.get(AreaImageEnum.WATER), Point(x, y))

    def __display_hexagon(self, sprite, game_field):
        """
        :type game_field: main.GUI.point.Point
        """
        x_coordinate = game_field.get_x() * HEXAGON_FIELD_WIDTH_SPACING * self._camera_zoom
        y_coordinate = game_field.get_y() * HEXAGON_FIELD_HEIGHT * self._camera_zoom
        if game_field.get_x() % 2 != 0:
            y_coordinate += HEXAGON_FIELD_HEIGHT / 2 * self._camera_zoom
        self._game_window.display(sprite, Point(x_coordinate, y_coordinate))

    def handle_relative_click(self, mouse_position):
        print(HexagonClickBox.get_field(mouse_position))

    def __turn_clicked_position_into_game_field_position(self, mouse_clicked_position):
        x_field = mouse_clicked_position[0] / (HEXAGON_FIELD_WIDTH_SPACING * self._camera_zoom)
        if x_field % 2 != 0:
            adjusted_position = mouse_clicked_position[1] - HEXAGON_FIELD_HEIGHT / 2 * self._camera_zoom
        else:
            adjusted_position = 0
        y_field = adjusted_position / (HEXAGON_FIELD_HEIGHT * self._camera_zoom)

        hexagon_side_width = (HEXAGON_FIELD_WIDTH - HEXAGON_FIELD_WIDTH_SPACING) / 2


class HexagonClickBox:
    @staticmethod
    def get_field(mouse_position):
        approximate_field = HexagonClickBox.__get_square(mouse_position)
        if approximate_field[0] % 2 == 1:
            return approximate_field
        else:
            return HexagonClickBox.__correct_approximate(mouse_position, approximate_field)

    @staticmethod
    def __get_square(mouse_clicked_position):
        is_even_square = mouse_clicked_position[0] % (
            HEXAGON_FIELD_WIDTH + HEXAGON_FIELD_CENTER_WIDTH) < HEXAGON_FIELD_WIDTH

        x_position = 2 * int(mouse_clicked_position[0] / (HEXAGON_FIELD_WIDTH + HEXAGON_FIELD_CENTER_WIDTH))

        if is_even_square:
            y_position = int(mouse_clicked_position[1] / HEXAGON_FIELD_HEIGHT)
            return x_position, y_position

        else:
            y_position = int((mouse_clicked_position[1] + HEXAGON_FIELD_SIDE_WIDTH) / HEXAGON_FIELD_HEIGHT)
            return x_position + 1, y_position

    @staticmethod
    def __correct_approximate(mouse_position, approximate_field):
        mouse_position_in_field_x = mouse_position[0] - int((approximate_field[0] * (HEXAGON_FIELD_WIDTH + HEXAGON_FIELD_CENTER_WIDTH)) / 2)
        mouse_position_in_field_y = mouse_position[1] - approximate_field[1] * HEXAGON_FIELD_HEIGHT

        mouse_position_in_field = mouse_position_in_field_x, mouse_position_in_field_y
        if not HexagonClickBox.__is_above_bottom_left_diagonal(mouse_position_in_field):
            return approximate_field[0] - 1, approximate_field[1]
        if not HexagonClickBox.__is_below_top_right_diagonal(mouse_position_in_field):
            return approximate_field[0] + 1, approximate_field[1] + 1
        if not HexagonClickBox.__is_above_bottom_right_diagonal(mouse_position_in_field):
            return approximate_field[0] + 1, approximate_field[1]
        if not HexagonClickBox.__is_below_top_left_diagonal(mouse_position_in_field):
            return approximate_field[0] - 1, approximate_field[1] + 1
        return approximate_field

    @staticmethod
    def __is_above_bottom_left_diagonal(mouse_clicked_position):
        return mouse_clicked_position[0] + mouse_clicked_position[1] > HEXAGON_FIELD_SIDE_WIDTH

    @staticmethod
    def __is_below_top_right_diagonal(mouse_clicked_position):
        return mouse_clicked_position[0] + mouse_clicked_position[1] < HEXAGON_FIELD_SIDE_WIDTH + HEXAGON_FIELD_WIDTH

    @staticmethod
    def __is_above_bottom_right_diagonal(mouse_clicked_position):
        return mouse_clicked_position[0] - mouse_clicked_position[1] < HEXAGON_FIELD_WIDTH_SPACING

    @staticmethod
    def __is_below_top_left_diagonal(mouse_clicked_position):
        return mouse_clicked_position[0] - mouse_clicked_position[1] > -HEXAGON_FIELD_SIDE_WIDTH


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
