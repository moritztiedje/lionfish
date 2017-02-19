from enum import Enum

import pygame

from main.constants import HEXAGON_FIELD_WIDTH, HEXAGON_FIELD_HEIGHT


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
        self.__hexagon_size = (156, 104)
        self.__square_size = (50, 50)

    def get(self, image_code):
        return self.__images[image_code]

    def set_camera_zoom(self, camera_zoom):
        new_hexagon_size = (int(camera_zoom * HEXAGON_FIELD_WIDTH),
                            int(camera_zoom * HEXAGON_FIELD_HEIGHT))
        self.__images[ImageEnum.BORDER] = pygame.transform.scale(self.__images[ImageEnum.BORDER],
                                                                 new_hexagon_size)
        self.__images[ImageEnum.WATER] = pygame.transform.scale(self.__images[ImageEnum.WATER],
                                                                new_hexagon_size)
