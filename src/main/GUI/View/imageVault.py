from abc import ABCMeta, abstractmethod
from enum import Enum

import pygame

from src.main.constants import HEXAGON_FIELD_WIDTH, HEXAGON_FIELD_HEIGHT, SQUARE_FIELD_WIDTH, SQUARE_FIELD_HEIGHT


class ImageVault(metaclass=ABCMeta):
    def __init__(self):
        self.__images = self._load_images()

    @abstractmethod
    def set_camera_zoom(self, camera_zoom):
        pass

    def get(self, image_code):
        return self.__images[image_code]

    @abstractmethod
    def _load_images(self):
        """
        :rtype: dict
        """
        pass

    def _scale_images(self, new_width, new_height):
        for key in self.__images:
            self.__images[key] = pygame.transform.scale(self.__images[key],
                                                        (new_width, new_height))


class ImageVaultWithHighlights(ImageVault):
    def __init__(self):
        super().__init__()
        self.__highlighted_images = self._load_highlighted_images()

    def get_highlighted(self, image_code):
        return self.__highlighted_images[image_code]

    @abstractmethod
    def _load_highlighted_images(self):
        """
        :rtype: dict
        """
        pass

    def _scale_images(self, new_width, new_height):
        super()._scale_images(new_width, new_height)
        for key in self.__highlighted_images:
            self.__highlighted_images[key] = pygame.transform.scale(self.__highlighted_images[key],
                                                                    (new_width, new_height))


class MenuImageVault(ImageVault):
    def set_camera_zoom(self, camera_zoom):
        pass

    def _load_images(self):
        return {}


class AreaImageEnum(Enum):
    EMPTY = 1
    WATER = 2


class AreaImageVault(ImageVaultWithHighlights):
    def _load_highlighted_images(self):
        return {
            AreaImageEnum.EMPTY: pygame.image.load('../../artwork/images/area tiles/highlighted/empty.png'),
            AreaImageEnum.WATER: pygame.image.load('../../artwork/images/area tiles/highlighted/water.png'),
        }

    def _load_images(self):
        return {
            AreaImageEnum.EMPTY: pygame.image.load('../../artwork/images/area tiles/empty.png'),
            AreaImageEnum.WATER: pygame.image.load('../../artwork/images/area tiles/water.png'),
        }

    def set_camera_zoom(self, camera_zoom):
        new_hexagon_width = int(camera_zoom * HEXAGON_FIELD_WIDTH)
        new_hexagon_height = int(camera_zoom * HEXAGON_FIELD_HEIGHT)
        self._scale_images(new_hexagon_width, new_hexagon_height)


class WorldImageVault(ImageVault):
    def __init__(self):
        super().__init__()

    def _load_images(self):
        return {
            WorldImageEnum.LAND: pygame.image.load('../../artwork/images/world tiles/land.png'),
            WorldImageEnum.WATER: pygame.image.load('../../artwork/images/world tiles/water.png')
        }

    def set_camera_zoom(self, camera_zoom):
        new_square_width = int(camera_zoom * SQUARE_FIELD_WIDTH)
        new_square_height = int(camera_zoom * SQUARE_FIELD_HEIGHT)
        self._scale_images(new_square_width, new_square_height)


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
