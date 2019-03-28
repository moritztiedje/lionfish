import pygame
from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT

from src.main.GUI.Controller.keyEvent import KeyEventTypes
from src.main.GUI.Controller.mouseController import MouseController


class GameController:
    def __init__(self, game_window):
        """
        :type game_window: src.main.GUI.View.gameWindow.GameWindow
        """
        self.__game_window = game_window
        self.__mouse_controller = MouseController(self.__game_window.get_height())

    def get_mouse_event(self):
        """
        :rtype: src.main.GUI.Controller.mouseEvent.MouseEvent
        """
        return self.__mouse_controller.get_mouse_state()

    @staticmethod
    def get_key_event():
        """
        :rtype: src.main.GUI.Controller.keyEvent.KeyEventTypes
        """
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            return KeyEventTypes.UP_PRESS
        elif keys[K_DOWN]:
            return KeyEventTypes.DOWN_PRESS
        elif keys[K_LEFT]:
            return KeyEventTypes.LEFT_PRESS
        elif keys[K_RIGHT]:
            return KeyEventTypes.RIGHT_PRESS
