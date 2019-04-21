from src.main.Logic.stateMachine import ChoiceState, AdvanceState, GoBackState, ForwardingState


class TextAdventureRandomizer:
    @staticmethod
    def choose_adventure():
        ## This method currently only returns one dummy text adventure that is only useful for manual testing.
        pick_nose_and_then_look_around = ForwardingState("You pick your nose. ")
        look_around = ChoiceState("You look around.")

        look_around.add_next_state("Proceed.", AdvanceState("You completed the area."))
        look_around.add_next_state("Look around some more", look_around)
        look_around.add_next_state("Pick your nose first", pick_nose_and_then_look_around)
        look_around.add_next_state("Run Away", GoBackState("You ran away."))

        pick_nose_and_then_look_around.set_next_state(look_around)

        initial_state = ChoiceState("You entered the area. What do you want to do?")
        initial_state.add_next_state("Proceed.", AdvanceState("You completed the area."))
        initial_state.add_next_state("Look around", look_around)
        initial_state.add_next_state("Run Away", GoBackState("You ran away."))

        return initial_state
