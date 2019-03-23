import pygame

from src.main.constants import HEXAGON_FIELD_WIDTH, HEXAGON_FIELD_HEIGHT, SQUARE_FIELD_WIDTH, SQUARE_FIELD_HEIGHT, \
    SPRITE_IN_HEXAGON_WIDTH, SPRITE_IN_HEXAGON_HEIGHT


class Image:
    def __init__(self, width, height, path):
        """
        :type width: int
        :type height: int
        :type path: string
        """
        self.__base_width = width
        self.__base_height = height
        self.sprite = pygame.image.load(path)

    def scale_sprite(self, zoom):
        self.sprite = pygame.transform.scale(self.sprite,
                                             (int(self.__base_width * zoom), int(self.__base_height * zoom)))


class HexFieldImage(Image):
    def __init__(self, path):
        """
        :type path: string
        """
        super().__init__(HEXAGON_FIELD_WIDTH, HEXAGON_FIELD_HEIGHT, path)


class SpriteInHexFieldImage(Image):
    def __init__(self, path):
        """
        :type path: string
        """
        super().__init__(SPRITE_IN_HEXAGON_WIDTH, SPRITE_IN_HEXAGON_HEIGHT, path)


class SquareFieldImage(Image):
    def __init__(self, path):
        """
        :type path: string
        """
        super().__init__(SQUARE_FIELD_WIDTH, SQUARE_FIELD_HEIGHT, path)
