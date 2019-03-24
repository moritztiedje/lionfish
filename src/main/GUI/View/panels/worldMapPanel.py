from src.main.GUI.View.imageVault import WorldImageVault, WorldImageEnum
from src.main.GUI.View.panels.panel import Panel
from src.main.Util.point import Point
from src.main.constants import SQUARE_FIELD_WIDTH, SQUARE_FIELD_HEIGHT


class WorldMapPanel(Panel):
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
