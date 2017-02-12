import pygame

from main.GUI.button import Button
from main.GUI.point import Point
from main.GUI.gui import GUI
from main.GUI.view import AreaMapView
from main.gameState import GameState


class Game:
    def __init__(self):
        pygame.init()

        game_state = GameState()
        world_map_button = Button(Point(720, 570),
                                  Point(800, 600),
                                  pygame.image.load('../artwork/images/worldButton.png'),
                                  game_state.set_world_map_active)

        display_width = 800
        display_height = 600
        game_display = pygame.display.set_mode((display_width, display_height))

        area_map_view = AreaMapView(game_display)
        area_map_view.register_button(world_map_button)

        window = GUI(game_display)
        window.register_view(area_map_view, game_state.is_area_map_active)

        self.__game_state = game_state
        self.__window = window

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

        pygame.quit()
        quit()
