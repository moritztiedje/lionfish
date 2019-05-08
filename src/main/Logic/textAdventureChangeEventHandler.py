from src.main.Logic.introTextAdventureState import IntroTextAdventureState
from src.main.Logic.stateMachine import StateMachine, ResultTypes
from src.main.Model.textAdventureState import TextAdventureSelection, TextAdventureState
from src.main.constants import Panels


class TextAdventureChangeEventHandler:
    def __init__(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        self.__state_machine = None
        self.__game_state = game_state
        self.set_initial_adventure_state(IntroTextAdventureState())

    def __get_state_machine(self):
        """
        :rtype: src.main.Logic.stateMachine.StateMachine
        """
        return self.__state_machine

    def select_option(self, option):
        """
        :type option: int
        """
        result = self.__get_state_machine().pick(option)
        self.__game_state.get_text_adventure_state().define_next_selection(
                TextAdventureSelection(
                        result.text,
                        result.selection
                ))
        if result.result_type is ResultTypes.FAIL:
            self.__game_state.get_text_adventure_state().complete()
        elif result.result_type == ResultTypes.SUCCESS:
            self.__game_state.get_text_adventure_state().complete()
            self.__game_state.get_player().move_to_destination()
        elif result.result_type == ResultTypes.GAME_OVER:
            self.__game_state.get_panel_state(Panels.GameOverPanel).show()
            final_text = self.__game_state.get_text_adventure_state().get_current_selection().text
            self.__game_state.set_game_over_text(final_text + "\nGame Over.")
            self.__game_state.get_panel_state(Panels.TextAdventureBox).deactivate()

    def set_initial_adventure_state(self, initial_state):
        """
        :type initial_state:
        """
        self.__state_machine = StateMachine(initial_state, self.__game_state)
        initial_result = self.__state_machine.run_until_next_result()
        self.__game_state.set_text_adventure_state(TextAdventureState(initial_result))

    def close(self):
        self.__game_state.get_panel_state(Panels.TextAdventureBox).hide()
        self.__game_state.get_panel_state(Panels.AreaMap).show()
