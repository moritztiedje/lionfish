import pygame

from src.main.GUI.BaseComponents.geometry import Point


class GameWindow:
    def __init__(self):
        self.__window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.__camera_position = Point(0, 0)
        self.__width = self.__window.get_width()
        self.__height = self.__window.get_height()

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_camera_position(self):
        """
        :rtype:  src.main.GUI.BaseComponents.geometry.Point
        """
        return self.__camera_position

    def draw(self, image, point):
        """
        :type image: main.imageVault.ImageEnum
        :type point: main.GUI.point.Point
        """
        inverted_coordinate = (point.get_x() - self.__camera_position.get_x(),
                               self.__height - point.get_y() + self.__camera_position.get_y())
        self.__window.blit(image, inverted_coordinate)

    def draw_absolute(self, image, point):
        inverted_coordinate = (point.get_x(), self.__height - point.get_y())
        self.__window.blit(image, inverted_coordinate)

    def clear(self):
        self.__window.fill((255, 255, 255))

    def camera_up(self):
        self.__camera_position += Point(0, 2)

    def camera_down(self):
        self.__camera_position -= Point(0, 2)

    def camera_left(self):
        self.__camera_position -= Point(2, 0)

    def camera_right(self):
        self.__camera_position += Point(2, 0)
