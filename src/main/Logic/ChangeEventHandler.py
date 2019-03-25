from src.main.Model.gameStateChangeEvent import GameStateChangeEventTypes


class ChangeEventHandler:
    @staticmethod
    def process(game_state, game_state_change_event):
        """
        :type game_state: src.main.Model.gameState.GameState
        :type game_state_change_event: src.main.Model.gameStateChangeEvent.GameStateChangeEvent
        """
        if game_state_change_event.event_type == GameStateChangeEventTypes.EnterArea:
            game_state.activateTextAdventureBox()