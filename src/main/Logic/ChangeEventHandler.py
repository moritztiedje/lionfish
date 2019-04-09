from src.main.GUI.BaseComponents.geometry import Point
from src.main.Logic.areaMapChangeEventHandler import AreaMapChangeEventHandler
from src.main.Logic.textAdventureChangeEventHandler import TextAdventureChangeEventHandler
from src.main.Logic.textAdventureRandomizer import TextAdventureRandomizer
from src.main.Model.gameStateChangeEvent import GameStateChangeEventTypes
from src.main.constants import Panels


class ChangeEventHandler:
    def __init__(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        self.__game_state = game_state
        self.__text_adventure_handler = TextAdventureChangeEventHandler(game_state)

    def process(self, game_state_change_event):
        """
        :type game_state_change_event: src.main.Model.gameStateChangeEvent.GameStateChangeEvent
        """
        if game_state_change_event.event_type == GameStateChangeEventTypes.EnterArea:
            if AreaMapChangeEventHandler.enter_area(
                    self.__game_state,
                    game_state_change_event.payload
            ):
                initial_state = TextAdventureRandomizer().choose_adventure()
                self.__text_adventure_handler.set_initial_adventure_state(initial_state)
        elif game_state_change_event.event_type == GameStateChangeEventTypes.GoToWorldMap:
            self.__game_state.get_panel_state(Panels.AreaMap).hide()
            self.__game_state.get_panel_state(Panels.WorldMap).show()
        elif game_state_change_event.event_type == GameStateChangeEventTypes.SelectTextAdventureOption:
            self.__text_adventure_handler.select_option(game_state_change_event.payload)
