from src.main.GUI.BaseComponents.button import Button
from src.main.GUI.BaseComponents.geometry import Point
from src.main.GUI.Controller.keyEvent import KeyEventTypes
from src.main.GUI.Controller.mouseEvent import MouseEventTypes
from src.main.GUI.View.Util.hexagonClickBox import HexagonClickBox
from src.main.GUI.View.image import Image
from src.main.GUI.View.imageVaults.areaImageVault import AreaImageVault, AreaImageEnum
from src.main.GUI.View.panels.panel import Panel
from src.main.Model.gameStateChangeEvent import GameStateChangeEvent, GameStateChangeEventTypes
from src.main.constants import HEXAGON_FIELD_WIDTH_SPACING, HEXAGON_FIELD_HEIGHT, SPRITE_IN_HEXAGON_WIDTH, \
    HEXAGON_FIELD_WIDTH, SPRITE_IN_HEXAGON_HEIGHT


class AreaMapPanel(Panel):
    def handle_key_event(self, key_event):
        """
        :type key_event: src.main.GUI.Controller.keyEvent.KeyEventTypes
        """
        if key_event == KeyEventTypes.UP_PRESS:
            self._camera_position += Point(0, 2)
            return GameStateChangeEvent(GameStateChangeEventTypes.InternalGUIChange, None)
        elif key_event == KeyEventTypes.DOWN_PRESS:
            self._camera_position -= Point(0, 2)
            return GameStateChangeEvent(GameStateChangeEventTypes.InternalGUIChange, None)
        elif key_event == KeyEventTypes.RIGHT_PRESS:
            self._camera_position += Point(2, 0)
            return GameStateChangeEvent(GameStateChangeEventTypes.InternalGUIChange, None)
        elif key_event == KeyEventTypes.LEFT_PRESS:
            self._camera_position -= Point(2, 0)
            return GameStateChangeEvent(GameStateChangeEventTypes.InternalGUIChange, None)

    def __init__(self, game_window):
        """
        :type game_window: src.main.GUI.View.gameWindow.GameWindow
        """
        super().__init__(game_window, 0)
        world_map_button = Button(Point(game_window.get_width() - 130, game_window.get_height() - 40),
                                  Point(game_window.get_width() - 50, game_window.get_height() - 10),
                                  Image(0, 0, '../../artwork/images/worldButton.png'),
                                  self.__set_world_map_active)
        self._register_button(world_map_button)

        self.__click_box = HexagonClickBox()
        self.__highlighted_field = None

    @staticmethod
    def __set_world_map_active():
        """
        :rtype: src.main.Model.gameStateChangeEvent.GameStateChangeEvent
        """
        return GameStateChangeEvent(GameStateChangeEventTypes.GoToWorldMap, None)

    def _load_image_vault(self):
        return AreaImageVault()

    def draw(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        super().draw(game_state)

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
                    self.__display_hexagon(self._image_vault.get_sprite(image_code), Point(x, y))

        player = game_state.get_player_position_in_area()
        self.__display_in_hexagon(self._image_vault.get_sprite(AreaImageEnum.PLAYER), player)

    def __display_hexagon(self, sprite, game_field):
        """
        :type game_field: src.main.Util.point.Point
        """
        x_coordinate = game_field.get_x() * HEXAGON_FIELD_WIDTH_SPACING * self._camera_zoom
        y_coordinate = game_field.get_y() * HEXAGON_FIELD_HEIGHT * self._camera_zoom
        if game_field.get_x() % 2 != 0:
            y_coordinate += HEXAGON_FIELD_HEIGHT / 2 * self._camera_zoom
        self._draw_relative_to_camera(sprite, Point(x_coordinate, y_coordinate))

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
        self._draw_relative_to_camera(sprite, Point(x_coordinate, y_coordinate))

    def _handle_mouse_event(self, mouse_event):
        """
        :type mouse_event: src.main.GUI.Controller.mouseEvent.MouseEvent
        """
        relative_mouse_position = self._calculate_relative_position_of(mouse_event.get_position())
        hexagon_point = self.__click_box.get_hexagon(relative_mouse_position)
        self.__highlighted_field = hexagon_point
        if mouse_event.get_type() == MouseEventTypes.DoubleClick:
            return GameStateChangeEvent(GameStateChangeEventTypes.EnterArea, hexagon_point)

    def zoom_in(self):
        super().zoom_in()
        self.__click_box.set_zoom_level(self._camera_zoom)

    def zoom_out(self):
        super().zoom_out()
        self.__click_box.set_zoom_level(self._camera_zoom)