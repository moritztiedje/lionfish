from enum import Enum

import pygame


class ImageEnum(Enum):
    BORDER = 1
    WATER = 2
    WORLD_LAND = 3
    WORLD_WATER = 4


class ImageVault:
    def __init__(self):
        self.__images = {
            ImageEnum.BORDER: pygame.image.load('../artwork/images/border.png'),
            ImageEnum.WATER: pygame.image.load('../artwork/images/water.png'),
            ImageEnum.WORLD_LAND: pygame.image.load('../artwork/images/world tiles/land.png'),
            ImageEnum.WORLD_WATER: pygame.image.load('../artwork/images/world tiles/water.png')
        }
        self.__camera_zoom = 1

    def get(self, image_code):
        return self.__images[image_code]
