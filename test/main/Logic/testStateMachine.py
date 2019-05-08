from unittest import TestCase

from src.main.Logic import stateMachine
from src.main.Logic.stateMachine import StateMachine, AdvanceState, ResultTypes, GoBackState, ChoiceState, State, \
    ForwardingState, AttemptState, SkillCheckState
from src.main.Model.gameState import GameState
from src.main.constants import PlayerSkills
from test.util.mockUtil import create_mock


class TestStateMachine(TestCase):
    def test_returns_success_when_success_state_is_reached(self):
        proceed_state = AdvanceState("You did it!")
        state_machine = StateMachine(proceed_state, None)

        state_machine_result = state_machine.run_until_next_result()

        self.assertEqual(state_machine_result.text, "You did it!")
        self.assertEqual(state_machine_result.result_type, ResultTypes.SUCCESS)
        self.assertEqual(len(state_machine_result.selection), 0)

    def test_returns_fail_when_fail_state_is_reached(self):
        proceed_state = GoBackState("You messed it up!")
        state_machine = StateMachine(proceed_state, None)

        state_machine_result = state_machine.run_until_next_result()

        self.assertEqual(state_machine_result.text, "You messed it up!")
        self.assertEqual(state_machine_result.result_type, ResultTypes.FAIL)
        self.assertEqual(len(state_machine_result.selection), 0)

    def test_returns_selections_when_choice_state_is_reached(self):
        proceed_state = ChoiceState("Pick One:")
        proceed_state.add_next_state("Some Option", create_mock(State))
        state_machine = StateMachine(proceed_state, None)

        state_machine_result = state_machine.run_until_next_result()

        self.assertEqual(state_machine_result.text, "Pick One:")
        self.assertIsNone(state_machine_result.result_type)
        self.assertEqual(state_machine_result.selection[0].text, "Some Option")

    def test_proceeds_to_next_state_when_option_is_picked(self):
        final_state = AdvanceState("You made it to the end of the test.")
        proceed_state = ChoiceState("Pick One:")
        proceed_state.add_next_state("Some Option", final_state)
        state_machine = StateMachine(proceed_state, None)
        state_machine.run_until_next_result()

        state_machine_result = state_machine.pick(0)

        self.assertEqual(state_machine_result.text, "You made it to the end of the test.")

    def test_appends_text_of_forwarding_state(self):
        final_state = AdvanceState("You made it to the end of the test.")
        forwarding_state = ForwardingState("Do Something First. ")
        forwarding_state.set_next_state(final_state)
        state_machine = StateMachine(forwarding_state, None)

        state_machine_result = state_machine.run_until_next_result()

        self.assertEqual(state_machine_result.text, "Do Something First. You made it to the end of the test.")

    def test_adds_probabilities_to_choice_state_results(self):
        choice_state = ChoiceState("")
        choice_state.add_next_state("", AttemptState("", 0.7))
        choice_state.add_next_state("", AttemptState("", 0.3))
        state_machine = StateMachine(choice_state, None)

        state_machine_result = state_machine.run_until_next_result()

        self.assertEqual(state_machine_result.selection[0].success_chance, 0.7)
        self.assertEqual(state_machine_result.selection[1].success_chance, 0.3)

    def test_calculates_success_chance_for_skill_check(self):
        skill_check_state = SkillCheckState("", PlayerSkills.COMPREHEND, 2)
        skill_check_state.set_success_state(AdvanceState("Dummy"))
        skill_check_state.set_fail_state(AdvanceState("Dummy"))
        dummy_game_state = create_mock(GameState)
        # TODO


class TestAttemptState(TestCase):
    def setUp(self):
        self.real_random = stateMachine.random
        stateMachine.random = lambda: 0.5

    def tearDown(self):
        stateMachine.random = self.real_random

    def test_get_next_state_can_return_success(self):
        dummy_state = State(None, "dummy")

        attempt_state = AttemptState("", 0.9)
        attempt_state.set_success_state(dummy_state)

        self.assertEqual(attempt_state.get_next_state(), dummy_state)

    def test_get_next_state_can_return_fail(self):
        dummy_state = State(None, "dummy")

        attempt_state = AttemptState("", 0.1)
        attempt_state.set_fail_state(dummy_state)

        self.assertEqual(attempt_state.get_next_state(), dummy_state)
