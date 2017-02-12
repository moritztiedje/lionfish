import pygame
from pygame.constants import K_UP, K_RIGHT, K_LEFT, K_DOWN


class GUI:
    def __init__(self, game_window):
        """
        :type game_window: main.gameWindow.GameWindow
        """
        self.__game_window = game_window

        self.__views = []

    def register_view(self, view, view_handle):
        self.__views.append((view, view_handle))

    def trigger_control_logic(self):
        mouse_is_clicking = pygame.mouse.get_pressed()[0] == 1
        if mouse_is_clicking:
            self.__handle_click(pygame.mouse.get_pos())

        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.__game_window.camera_up()
        if keys[K_DOWN]:
            self.__game_window.camera_down()
        if keys[K_LEFT]:
            self.__game_window.camera_left()
        if keys[K_RIGHT]:
            self.__game_window.camera_right()

    def __handle_click(self, mouse_position):
        for view, view_handle in self.__views:
            if view_handle():
                view.handle_click(mouse_position)

    def display(self, game_state):
        self.__game_window.clear()

        for view, view_handle in self.__views:
            if view_handle():
                view.display(game_state)
