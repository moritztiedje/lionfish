import pygame

from main import AreaMapView


class GUI:
    def __init__(self, display_width, display_height, world_map_button):
        pygame.init()
        self.__game_display = pygame.display.set_mode((display_width, display_height))
        self.__area_map_view = AreaMapView(self.__game_display)
        self.__area_map_view.register_button(world_map_button)

        self.__white = (255, 255, 255)

    def trigger_control_logic(self, game_state):
        mouse_is_clicking = pygame.mouse.get_pressed()[0] == 1
        if mouse_is_clicking:
            self.__handle_click(game_state, pygame.mouse.get_pos())

    def __handle_click(self, game_state, mouse_position):
        if game_state.is_area_map_active():
            self.__area_map_view.handle_click(mouse_position)

    @staticmethod
    def world_map_button_pressed():
        mouse_pos = pygame.mouse.get_pos()
        mouse_is_clicking = pygame.mouse.get_pressed()[0] == 1
        return mouse_is_clicking and mouse_pos[0] > 600 and mouse_pos[1] > 400

    def display(self, game_state):
        self.__game_display.fill(self.__white)

        if game_state.is_area_map_active():
            self.__area_map_view.display(game_state)
