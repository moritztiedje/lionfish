import pygame

from src.main.GUI.Controller.gameController import GameController
from src.main.GUI.View.gameWindow import GameWindow
from src.main.GUI.gui import GUI
from src.main.Logic.changeEventHandler import ChangeEventHandler
from src.main.Model.gameState import GameState


class Game:
    def __init__(self):
        pygame.init()

        game_state = GameState()
        game_window = GameWindow()
        game_controller = GameController(game_window)

        gui = GUI(game_window, game_controller)

        self.__game_state = game_state
        self.__gui = gui
        self.__change_event_handler = ChangeEventHandler(self.__game_state)
        self.__gui.draw(game_state)

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

            game_state_change_event = self.__gui.trigger_control_logic()
            if game_state_change_event:
                self.__change_event_handler.process(game_state_change_event)
                self.__gui.draw(self.__game_state)
            pygame.display.update()
            clock.tick(60)

        self.__quit_game()
