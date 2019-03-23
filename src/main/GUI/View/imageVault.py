from abc import ABCMeta, abstractmethod
from enum import Enum

from src.main.GUI.View.image import HexFieldImage, SquareFieldImage, Image


class ImageVault(metaclass=ABCMeta):
    def __init__(self):
        self.__images = self._load_images()

    @abstractmethod
    def set_camera_zoom(self, camera_zoom):
        pass

    def get(self, image_code):
        return self.__images[image_code].sprite

    @abstractmethod
    def _load_images(self):
        """
        :rtype: dict
        """
        pass

    def _scale_images(self, zoom):
        for key in self.__images:
            self.__images[key].scale_sprite(zoom)


class ImageVaultWithHighlights(ImageVault):
    def __init__(self):
        super().__init__()
        self.__highlighted_images = self._load_highlighted_images()

    def get_highlighted(self, image_code):
        return self.__highlighted_images[image_code].sprite

    @abstractmethod
    def _load_highlighted_images(self):
        """
        :rtype: dict
        """
        pass

    def _scale_images(self, zoom):
        super()._scale_images(zoom)
        for key in self.__highlighted_images:
            self.__highlighted_images[key].scale_sprite(zoom)


class MenuImageVault(ImageVault):
    def set_camera_zoom(self, camera_zoom):
        pass

    def _load_images(self):
        return {}


class AreaImageEnum(Enum):
    EMPTY = 1
    WATER = 2
    PLAYER = 0


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
            AreaImageEnum.PLAYER: Image(40, 40, '../../artwork/images/dummyPlayer.png'),
        }

    def set_camera_zoom(self, camera_zoom):
        self._scale_images(camera_zoom)


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


class MenuImageVault(ImageVault):
    def _load_images(self):
        return {}

    def __init__(self):
        super().__init__()

    def set_camera_zoom(self, camera_zoom):
        pass
