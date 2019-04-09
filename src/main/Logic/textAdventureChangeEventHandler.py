from src.main.Logic.introTextAdventureState import IntroTextAdventureState
from src.main.Logic.stateMachine import StateMachine, ResultTypes
from src.main.Model.textAdventureState import TextAdventureSelection, TextAdventureState
from src.main.constants import Panels


class TextAdventureChangeEventHandler:
    def __init__(self, game_state):
        self.__state_machine = None
        self.__game_state = game_state
        self.set_initial_adventure_state(IntroTextAdventureState())

    def select_option(self, option):
        """
        :type game_state: src.main.Model.gameState.GameState
        :type option: int
        """
        result = self.__state_machine.pick(option)
        if result.selection is not None:
            self.__game_state.get_text_adventure_state().define_next_selection(
                    TextAdventureSelection(
                            result.text,
                            result.selection
                    )
            )
        else:
            self.__game_state.get_panel_state(Panels.TextAdventureBox).hide()
            self.__game_state.get_panel_state(Panels.AreaMap).show()
            if result.result == ResultTypes.SUCCESS:
                self.__game_state.get_player().move_to_destination()

    def set_initial_adventure_state(self, initial_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        :type initial_state:
        """
        self.__state_machine = StateMachine(initial_state)
        initial_result = self.__state_machine.advance()
        self.__game_state.set_text_adventure_state(TextAdventureState(initial_result))
