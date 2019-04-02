from src.main.Logic.stateMachine import ChoiceState, SuccessState, FailState


class TextAdventureRandomizer:
    @staticmethod
    def choose_adventure():
        look_around = ChoiceState("You look around.")
        look_around.add_next_state("Proceed.", SuccessState("You completed the area."))
        look_around.add_next_state("Look around some more", look_around)
        look_around.add_next_state("Run Away", FailState("You ran away."))

        dummy_state = ChoiceState("You entered the area. What do you want to do?")
        dummy_state.add_next_state("Proceed.", SuccessState("You completed the area."))
        dummy_state.add_next_state("Look around", look_around)
        dummy_state.add_next_state("Run Away", FailState("You ran away."))

        return dummy_state
