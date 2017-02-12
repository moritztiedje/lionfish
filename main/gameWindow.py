import pygame

from main.constants import WINDOW_HEIGHT, WINDOW_WIDTH


class GameWindow:
    def __init__(self):
        self.__window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.__camera_position = [0, 0]

    def display(self, image, point):
        inverted_coordinate = (point.get_x() - self.__camera_position[0],
                               WINDOW_HEIGHT - point.get_y() + self.__camera_position[1])
        self.__window.blit(image, inverted_coordinate)

    def display_absolute(self, image, point):
        inverted_coordinate = (point.get_x(), WINDOW_HEIGHT - point.get_y())
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
