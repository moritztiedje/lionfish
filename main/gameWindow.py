import pygame

from main.constants import WINDOW_HEIGHT, WINDOW_WIDTH


class GameWindow:
    def __init__(self):
        self.__window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def display(self, image, point):
        inverted_coordinate = (point.get_x(), WINDOW_HEIGHT - point.get_y())
        self.__window.blit(image, inverted_coordinate)

    def clear(self):
        self.__window.fill((255, 255, 255))
