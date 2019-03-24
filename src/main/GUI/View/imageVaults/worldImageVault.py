from enum import Enum

from src.main.GUI.View.image import SquareFieldImage
from src.main.GUI.View.imageVaults.imageVault import ImageVault


class WorldImageVault(ImageVault):
    def __init__(self):
        super().__init__()

    def _load_images(self):
        return {
            WorldImageEnum.LAND: SquareFieldImage('../../artwork/images/world tiles/land.png'),
            WorldImageEnum.WATER: SquareFieldImage('../../artwork/images/world tiles/water.png')
        }

    def set_camera_zoom(self, camera_zoom):
        self._scale_images(camera_zoom)


class WorldImageEnum(Enum):
    LAND = 1
    WATER = 2
