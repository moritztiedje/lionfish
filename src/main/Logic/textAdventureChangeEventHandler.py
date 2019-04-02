from src.main.Logic.stateMachine import StateMachine, ResultTypes
from src.main.Model.textAdventureState import TextAdventureSelection, TextAdventureState
from src.main.constants import Panels


class TextAdventureChangeEventHandler:
    def __init__(self):
        self.__state_machine = None

    def select_option(self, game_state, option):
        """
        :type game_state: src.main.Model.gameState.GameState
        :type option: int
        """
        result = self.__state_machine.pick(option)
        if result.selection is not None:
            game_state.get_text_adventure_state().define_next_selection(
                    TextAdventureSelection(
                            result.text,
                            result.selection
                    )
            )
        else:
            game_state.get_panel_state(Panels.TextAdventureBox).hide()
            game_state.get_panel_state(Panels.AreaMap).activate()
            if result.result == ResultTypes.SUCCESS:
                game_state.get_player().move_to_destination()

    def set_initial_adventure_state(self, initial_state, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        :type initial_state:
        """
        self.__state_machine = StateMachine(initial_state)
        initial_result = self.__state_machine.advance()
        game_state.set_text_adventure_state(TextAdventureState(initial_result))
