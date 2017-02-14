import pygame
from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT


class GameController:
    def __init__(self, game_window):
        """
        :type game_window: main.gameWindow.GameWindow
        """
        self.__game_window = game_window

    def handle_base_logic(self):
        self.__handle_camera_movement()

    def __handle_camera_movement(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.__game_window.camera_up()
        if keys[K_DOWN]:
            self.__game_window.camera_down()
        if keys[K_LEFT]:
            self.__game_window.camera_left()
        if keys[K_RIGHT]:
            self.__game_window.camera_right()

    def mouse_click(self):
        mouse_is_clicking = pygame.mouse.get_pressed()[0] == 1
        if mouse_is_clicking:
            mouse_position = pygame.mouse.get_pos()
            inverted_mouse = mouse_position[0], self.__game_window.get_height() - mouse_position[1]
            return inverted_mouse
