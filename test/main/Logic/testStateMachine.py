from unittest import TestCase

from src.main.Logic import stateMachine
from src.main.Logic.stateMachine import StateMachine, SuccessState, ResultTypes, FailState, ChoiceState, State, \
    ForwardingState, AttemptState
from test.util.mockUtil import create_mock


class TestStateMachine(TestCase):
    def test_returns_success_when_success_state_is_reached(self):
        proceed_state = SuccessState("You did it!")
        state_machine = StateMachine(proceed_state)

        state_machine_result = state_machine.advance()

        self.assertEqual(state_machine_result.text, "You did it!")
        self.assertEqual(state_machine_result.result, ResultTypes.SUCCESS)
        self.assertEqual(len(state_machine_result.selection), 0)

    def test_returns_fail_when_fail_state_is_reached(self):
        proceed_state = FailState("You messed it up!")
        state_machine = StateMachine(proceed_state)

        state_machine_result = state_machine.advance()

        self.assertEqual(state_machine_result.text, "You messed it up!")
        self.assertEqual(state_machine_result.result, ResultTypes.FAIL)
        self.assertEqual(len(state_machine_result.selection), 0)

    def test_returns_selections_when_choice_state_is_reached(self):
        proceed_state = ChoiceState("Pick One:")
        proceed_state.add_next_state("Some Option", create_mock(State))
        state_machine = StateMachine(proceed_state)

        state_machine_result = state_machine.advance()

        self.assertEqual(state_machine_result.text, "Pick One:")
        self.assertIsNone(state_machine_result.result)
        self.assertEqual(state_machine_result.selection[0], "Some Option")

    def test_proceeds_to_next_state_when_option_is_picked(self):
        final_state = SuccessState("You made it to the end of the test.")
        proceed_state = ChoiceState("Pick One:")
        proceed_state.add_next_state("Some Option", final_state)
        state_machine = StateMachine(proceed_state)
        state_machine.advance()

        state_machine_result = state_machine.pick(0)

        self.assertEqual(state_machine_result.text, "You made it to the end of the test.")

    def test_appends_text_of_forwarding_state(self):
        final_state = SuccessState("You made it to the end of the test.")
        forwarding_state = ForwardingState("Do Something First. ")
        forwarding_state.set_next_state(final_state)
        state_machine = StateMachine(forwarding_state)

        state_machine_result = state_machine.advance()

        self.assertEqual(state_machine_result.text, "Do Something First. You made it to the end of the test.")


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
