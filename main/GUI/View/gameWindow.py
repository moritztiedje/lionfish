import pygame

from main.GUI.BaseComponents.point import Point
from main.GUI.View.imageVault import ImageVault
from main.constants import HEXAGON_FIELD_WIDTH_SPACING, HEXAGON_FIELD_HEIGHT, SQUARE_FIELD_WIDTH, SQUARE_FIELD_HEIGHT


class GameWindow:
    def __init__(self):
        self.__window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.__camera_position = [0, 0]
        self.__width = self.__window.get_width()
        self.__height = self.__window.get_height()
        self.__camera_zoom = 1
        self.__image_vault = ImageVault()

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def display(self, image, point):
        """
        :type image: main.imageVault.ImageEnum
        :type point: main.GUI.point.Point
        """
        inverted_coordinate = (point.get_x() - self.__camera_position[0],
                               self.__height - point.get_y() + self.__camera_position[1])
        self.__window.blit(self.__image_vault.get(image), inverted_coordinate)

    def display_absolute(self, image, point):
        inverted_coordinate = (point.get_x(), self.__height - point.get_y())
        self.__window.blit(image, inverted_coordinate)

    def clear(self):
        self.__window.fill((255, 255, 255))

    def camera_up(self):
        self.__camera_position[1] += 2

    def camera_down(self):
        self.__camera_position[1] -= 2

    def camera_left(self):
        self.__camera_position[0] -= 2

    def camera_right(self):
        self.__camera_position[0] += 2

    def camera_zoom_in(self):
        self.__camera_zoom *= 2
        self.__image_vault.set_camera_zoom(self.__camera_zoom)

    def camera_zoom_out(self):
        self.__camera_zoom /= 2
        self.__image_vault.set_camera_zoom(self.__camera_zoom)

    def display_hexagon(self, sprite, coordinate):
        """
        :type coordinate: main.GUI.point.Point
        """
        x_coordinate = coordinate.get_x() * HEXAGON_FIELD_WIDTH_SPACING * self.__camera_zoom
        y_coordinate = coordinate.get_y() * HEXAGON_FIELD_HEIGHT * self.__camera_zoom
        if coordinate.get_x() % 2 != 0:
            y_coordinate += HEXAGON_FIELD_HEIGHT / 2 * self.__camera_zoom
        self.display(sprite, Point(x_coordinate, y_coordinate))

    def display_square(self, sprite, coordinate):
        """
        :type coordinate: main.GUI.point.Point
        """
        display_coordinate = Point(coordinate.get_x() * SQUARE_FIELD_WIDTH * self.__camera_zoom,
                                   coordinate.get_y() * SQUARE_FIELD_HEIGHT * self.__camera_zoom)
        self.display(sprite, display_coordinate)