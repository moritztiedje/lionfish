import pygame

from main.GUI.button import Button
from main.GUI.point import Point
from main.GUI.gui import GUI
from main.GUI.view import AreaMapView, WorldMapView, MenuView
from main.gameController import GameController
from main.gameState import GameState
from main.gameWindow import GameWindow


class Game:
    def __init__(self):
        pygame.init()

        game_state = GameState()
        game_window = GameWindow()
        game_controller = GameController(game_window)

        window = GUI(game_window, game_controller)
        window.register_view(self.__build_area_map_view(game_state, game_window),
                             game_state.is_area_map_active)
        window.register_view(self.__build_world_map_view(game_window),
                             game_state.is_world_map_active)
        window.register_view(self.__build_main_menu_view(game_window),
                             game_state.is_menu_visible)

        self.__game_state = game_state
        self.__window = window

    @staticmethod
    def __build_area_map_view(game_state, game_window):
        world_map_button = Button(Point(game_window.get_width() - 130, game_window.get_height() - 40),
                                  Point(game_window.get_width() - 50, game_window.get_height() - 10),
                                  pygame.image.load('../artwork/images/worldButton.png'),
                                  game_state.set_world_map_active)
        area_map_view = AreaMapView(game_window)
        area_map_view.register_button(world_map_button)
        return area_map_view

    def __build_main_menu_view(self, game_window):
        main_menu_button = Button(Point(game_window.get_width() - 40, game_window.get_height() - 40),
                                  Point(game_window.get_width() - 10, game_window.get_height() - 10),
                                  pygame.image.load('../artwork/images/menu/gear.png'),
                                  self.__quit_game)
        zoom_in_button = Button(Point(game_window.get_width() - 40, game_window.get_height() - 80),
                                Point(game_window.get_width() - 10, game_window.get_height() - 50),
                                pygame.image.load('../artwork/images/menu/magnify.png'),
                                game_window.camera_zoom_in)
        zoom_out_button = Button(Point(game_window.get_width() - 40, game_window.get_height() - 120),
                                 Point(game_window.get_width() - 10, game_window.get_height() - 90),
                                 pygame.image.load('../artwork/images/menu/reduce.png'),
                                 game_window.camera_zoom_out)
        main_menu_view = MenuView(game_window)
        main_menu_view.register_button(main_menu_button)
        main_menu_view.register_button(zoom_in_button)
        main_menu_view.register_button(zoom_out_button)
        return main_menu_view

    @staticmethod
    def __build_world_map_view(game_window):
        return WorldMapView(game_window)

    @staticmethod
    def __quit_game():
        pygame.quit()
        quit()

    def run(self):
        clock = pygame.time.Clock()
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

            self.__window.trigger_control_logic()
            self.__window.display(self.__game_state)
            pygame.display.update()
            clock.tick(60)

        self.__quit_game()
