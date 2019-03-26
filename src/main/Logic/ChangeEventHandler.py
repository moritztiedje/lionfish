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
            game_state.get_panel_state(Panels.TextAdventureBox).show()
            game_state.get_panel_state(Panels.AreaMap).deactivate()
        elif game_state_change_event.event_type == GameStateChangeEventTypes.GoToWorldMap:
            game_state.get_panel_state(Panels.AreaMap).hide()
            game_state.get_panel_state(Panels.WorldMap).show()
