import pygame


class GUI:
    def __init__(self, game_window):
        self.__game_window = game_window
        self.__white = (255, 255, 255)

        self.__views = []

    def register_view(self, view, view_handle):
        self.__views.append((view, view_handle))

    def trigger_control_logic(self):
        mouse_is_clicking = pygame.mouse.get_pressed()[0] == 1
        if mouse_is_clicking:
            self.__handle_click(pygame.mouse.get_pos())

    def __handle_click(self, mouse_position):
        for view, view_handle in self.__views:
            if view_handle():
                view.handle_click(mouse_position)

    def display(self, game_state):
        self.__game_window.fill(self.__white)

        for view, view_handle in self.__views:
            if view_handle():
                view.display(game_state)
