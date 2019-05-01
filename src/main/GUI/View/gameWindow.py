import pygame


class GameWindow:
    def __init__(self):
        self.__window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.__width = self.__window.get_width()
        self.__height = self.__window.get_height()

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def draw(self, sprite, point):
        """
        :type sprite: pygame.Surface
        :type point: src.main.GUI.BaseComponents.geometry.Point
        """
        inverted_coordinate = (point.get_x(), self.__height - point.get_y())
        self.__window.blit(sprite, inverted_coordinate)

    def draw_rectangle(self, rectangle, color):
        """
        :type rectangle: src.main.GUI.BaseComponents.geometry.Rectangle
        :type draw_coordinate: src.main.GUI.BaseComponents.geometry.Point
        :type color: str
        """
        pycolor = pygame.Color(color)
        pyrectangle = pygame.Rect(rectangle.get_left(), self.__height - rectangle.get_top(), rectangle.get_width(), rectangle.get_height())
        pygame.draw.rect(self.__window, pycolor, pyrectangle)

    def clear(self):
        self.__window.fill((255, 255, 255))
