from src.main.Model.textAdventureState import TextAdventureSelection
from src.main.constants import Panels


class TextAdventureChangeEventHandler:
    @staticmethod
    def select_option(game_state, option):
        """
        :type game_state: src.main.Model.gameState.GameState
        :type option: int
        """
        if option == 0:
            game_state.get_panel_state(Panels.TextAdventureBox).hide()
            game_state.get_panel_state(Panels.AreaMap).activate()
            game_state.get_player().move_to_destination()
            game_state.get_text_adventure_state().adventure_completed()
        elif option == 1:
            game_state.get_text_adventure_state().define_next_selection(
                    TextAdventureSelection(
                            "You chose option: " + str(option),
                            "finish area",
                            "look around",
                            "run away",
                    )
            )
        elif option == 2:
            game_state.get_panel_state(Panels.TextAdventureBox).hide()
            game_state.get_panel_state(Panels.AreaMap).activate()
            game_state.get_text_adventure_state().adventure_completed()
