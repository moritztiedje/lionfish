from src.main.GUI.BaseComponents.geometry import Point
from src.main.GUI.View.imageVaults.worldImageVault import WorldImageVault, WorldImageEnum
from src.main.GUI.View.panels.panel import Panel
from src.main.constants import SQUARE_FIELD_WIDTH, SQUARE_FIELD_HEIGHT


class WorldMapPanel(Panel):
    def handle_key_event(self, key_event):
        pass

    def __init__(self, game_window):
        """
        :type game_window: src.main.GUI.View.gameWindow.GameWindow
        """
        super().__init__(game_window, 0)

    def _handle_mouse_event(self, mouse_event):
        pass

    def _load_image_vault(self):
        return WorldImageVault()

    def draw(self, game_state):
        """
        :type game_state: main.gameState.GameState
        """
        super().draw(game_state)

        world_map = game_state.get_world_map()
        for x in range(0, len(world_map)):
            for y in range(0, len(world_map[x])):
                if world_map[x][y] == 1:
                    self.__display_square(self._get_image_vault().get_sprite(WorldImageEnum.LAND), Point(x, y))
                if world_map[x][y] == 0:
                    self.__display_square(self._get_image_vault().get_sprite(WorldImageEnum.WATER), Point(x, y))

    def __display_square(self, sprite, coordinate):
        """
        :type sprite: pygame.Surface
        :type coordinate: src.main.GUI.BaseComponents.geometry.Point
        """
        display_coordinate = Point(coordinate.get_x() * SQUARE_FIELD_WIDTH * self._camera_zoom,
                                   coordinate.get_y() * SQUARE_FIELD_HEIGHT * self._camera_zoom)
        self._draw_relative_to_camera(sprite, display_coordinate)
