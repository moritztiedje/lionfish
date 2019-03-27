from src.main.Model.textAdventureState import TextAdventureSelection


class TextAdventureChangeEventHandler:
    @staticmethod
    def select_option(text_adventure_game_state, option):
        """
        :type text_adventure_game_state: src.main.Model.textAdventureState.TextAdventureState
        :type option: int
        """
        text_adventure_game_state.define_next_selection(
                TextAdventureSelection(
                        "You chose option: " + str(option),
                        "leave2",
                        "keep going2",
                        "run away2",
                )
        )
