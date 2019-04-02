from unittest import TestCase

from src.main.GUI.BaseComponents.geometry import Point
from src.main.Logic.areaMapChangeEventHandler import AreaMapChangeEventHandler
from src.main.Logic.stateMachine import StateMachine, SuccessState, ResultTypes
from src.main.Model.areaMap import AreaMap
from src.main.Model.gameState import GameState
from test.util.mockUtil import create_mock


class TestStateMachine(TestCase):
    def test_returns_success_when_success_state_is_reached(self):
        proceed_state = SuccessState("You did it!")
        state_machine = StateMachine(proceed_state)

        state_machine_result = state_machine.advance()

        self.assertEqual(state_machine_result.text, "You did it!")
        self.assertEqual(state_machine_result.result, ResultTypes.SUCCESS)
        self.assertIsNone(state_machine_result.selection)
