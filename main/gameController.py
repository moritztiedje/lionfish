import pygame
from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT


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


class MouseController:
    def __init__(self, window_height):
        self.__window_height = window_height
        self.__left_was_pressed = False

    def mouse_left_click(self):
        left_mouse_has_clicked = not self.__left_was_pressed and self.__left_mouse_is_pressed()
        self.__left_was_pressed = self.__left_mouse_is_pressed()

        if left_mouse_has_clicked:
            mouse_position = pygame.mouse.get_pos()
            inverted_mouse = mouse_position[0], self.__window_height - mouse_position[1]
            return inverted_mouse

    @staticmethod
    def __left_mouse_is_pressed():
        return pygame.mouse.get_pressed()[0] == 1
