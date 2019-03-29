from enum import Enum

from src.main.GUI.View.image import HexFieldImage, SpriteInHexFieldImage
from src.main.GUI.View.imageVaults.imageVaultWithHighlightings import ImageVaultWithHighlights
from src.main.constants import AreaImageEnum


class AreaImageVault(ImageVaultWithHighlights):
    def _load_highlighted_images(self):
        return {
            AreaImageEnum.EMPTY:
                HexFieldImage('../../artwork/images/area tiles/highlighted/empty.png'),
            AreaImageEnum.WATER:
                HexFieldImage('../../artwork/images/area tiles/highlighted/water.png'),
        }

    def _load_images(self):
        return {
            AreaImageEnum.EMPTY: HexFieldImage('../../artwork/images/area tiles/empty.png'),
            AreaImageEnum.WATER: HexFieldImage('../../artwork/images/area tiles/water.png'),
            AreaImageEnum.PLAYER: SpriteInHexFieldImage('../../artwork/images/dummyPlayer.png'),
        }

    def set_camera_zoom(self, camera_zoom):
        self._scale_images(camera_zoom)
