from src.main.Logic.stateMachine import StateMachine, State, ChoiceState, ProceedState, FailState, ResultTypes
from src.main.Model.textAdventureState import TextAdventureSelection
from src.main.constants import Panels


class TextAdventureChangeEventHandler:
    def __init__(self):
        look_around = ChoiceState("You look around.")
        look_around.add_next_state("Proceed.", ProceedState("You completed the area."))
        look_around.add_next_state("Look around some more", look_around)
        look_around.add_next_state("Run Away", FailState("You ran away."))

        first_state = ChoiceState("You entered the area. What do you want to do?")
        first_state.add_next_state("Proceed.", ProceedState("You completed the area."))
        first_state.add_next_state("Look around", look_around)
        first_state.add_next_state("Run Away", FailState("You ran away."))
        self.__state_machine = StateMachine(first_state)

    def select_option(self, game_state, option):
        """
        :type game_state: src.main.Model.gameState.GameState
        :type option: int
        """
        result = self.__state_machine.advance(option)
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
            game_state.get_text_adventure_state().adventure_completed()
            if result.result == ResultTypes.SUCCESS:
                game_state.get_player().move_to_destination()
