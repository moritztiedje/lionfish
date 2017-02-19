import pygame
from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT

from main.GUI.Controller.mouseController import MouseController


class GameController:
    def __init__(self, game_window):
        """
        :type game_window: main.gameWindow.GameWindow
        """
        self.__game_window = game_window
        self.__mouse_controller = MouseController(self.__game_window.get_height())

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

    def mouse_left_click(self):
        return self.__mouse_controller.mouse_left_click()


