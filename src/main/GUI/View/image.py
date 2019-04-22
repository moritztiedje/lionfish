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
        self.__width = width
        self.__height = height
        self.sprite = pygame.image.load(path)

    def zoom(self, zoom_level):
        self.sprite = pygame.transform.scale(self.sprite,
                                             (
                                                 int(self.__base_width * zoom_level),
                                                 int(self.__base_height * zoom_level)))

    def scale_to_width(self, width):
        self.__width = width
        self.sprite = pygame.transform.scale(self.sprite, (width, self.__height))

    def scale_to_height(self, height):
        self.__height = height
        self.sprite = pygame.transform.scale(self.sprite, (self.__width, height))

    def get_height(self):
        """
        :rtype: int
        """
        return self.__height

    def get_width(self):
        """
        :rtype: int
        """
        return self.__width

    def set_alpha(self, alpha):
        """
        :type alpha: int
        """
        self.sprite.set_alpha(alpha)


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
