from src.main.Logic.areaMapChangeEventHandler import AreaMapChangeEventHandler
from src.main.Logic.textAdventureChangeEventHandler import TextAdventureChangeEventHandler
from src.main.Model.gameStateChangeEvent import GameStateChangeEventTypes
from src.main.constants import Panels


class ChangeEventHandler:
    @staticmethod
    def process(game_state, game_state_change_event):
        """
        :type game_state: src.main.Model.gameState.GameState
        :type game_state_change_event: src.main.Model.gameStateChangeEvent.GameStateChangeEvent
        """
        if game_state_change_event.event_type == GameStateChangeEventTypes.EnterArea:
            AreaMapChangeEventHandler.enter_area(
                    game_state,
                    game_state_change_event.payload
            )
        elif game_state_change_event.event_type == GameStateChangeEventTypes.GoToWorldMap:
            game_state.get_panel_state(Panels.AreaMap).hide()
            game_state.get_panel_state(Panels.WorldMap).show()
        elif game_state_change_event.event_type == GameStateChangeEventTypes.SelectTextAdventureOption:
            TextAdventureChangeEventHandler.select_option(
                    game_state,
                    game_state_change_event.payload
            )
