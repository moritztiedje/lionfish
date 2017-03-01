import pygame
from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT

from src.main.GUI.Controller.mouseController import MouseController


class GameController:
    def __init__(self, game_window):
        """
        :type game_window: main.gameWindow.GameWindow
        """
        self.__game_window = game_window
        self.__mouse_controller = MouseController(self.__game_window.get_height())

    def handle_base_logic(self):
        return self.__handle_camera_movement()

    def __handle_camera_movement(self):
        keys = pygame.key.get_pressed()

        key_action_map = {
            K_UP: self.__game_window.camera_up,
            K_DOWN: self.__game_window.camera_down,
            K_LEFT: self.__game_window.camera_left,
            K_RIGHT: self.__game_window.camera_right,
        }

        any_key_was_pressed = False
        for key in key_action_map.keys():
            if keys[key]:
                action = key_action_map.get(key)
                action()
                any_key_was_pressed = True

        return any_key_was_pressed

    def mouse_left_click(self):
        return self.__mouse_controller.mouse_left_click()


