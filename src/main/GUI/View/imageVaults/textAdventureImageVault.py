from enum import Enum

from src.main.GUI.View.image import Image
from src.main.GUI.View.imageVaults.imageVault import ImageVault


class TextAdventureImageVault(ImageVault):
    def __init__(self, game_window):
        """
        :type game_window: src.main.GUI.View.gameWindow.GameWindow
        """
        self.__game_window = game_window
        super().__init__()

    def _load_images(self):
        background = Image(800, 200, '../../artwork/images/textAdventureBoxBackground.png')
        background.scale_to_width(self.__game_window.get_width())
        top_border = Image(800, 20, '../../artwork/images/textAdventureBoxTopBorder.png')
        top_border.scale_to_width(self.__game_window.get_width())
        return {
            TextAdventureImageEnum.BACKGROUND: background,
            TextAdventureImageEnum.TOP_BORDER: top_border,
        }

    def set_camera_zoom(self, camera_zoom):
        pass


class TextAdventureImageEnum(Enum):
    BACKGROUND = 0
    TOP_BORDER = 1
