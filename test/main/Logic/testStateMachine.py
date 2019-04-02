from unittest import TestCase

from src.main.Logic.stateMachine import StateMachine, SuccessState, ResultTypes


class TestStateMachine(TestCase):
    def test_returns_success_when_success_state_is_reached(self):
        proceed_state = SuccessState("You did it!")
        state_machine = StateMachine(proceed_state)

        state_machine_result = state_machine.advance()

        self.assertEqual(state_machine_result.text, "You did it!")
        self.assertEqual(state_machine_result.result, ResultTypes.SUCCESS)
        self.assertIsNone(state_machine_result.selection)
