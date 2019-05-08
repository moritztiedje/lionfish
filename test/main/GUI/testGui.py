import unittest

from src.main.GUI import gui
from src.main.GUI.Controller.gameController import GameController
from src.main.GUI.Controller.keyEvent import KeyEventTypes
from src.main.GUI.Controller.mouseEvent import MouseEvent
from src.main.GUI.View.gameWindow import GameWindow
from src.main.GUI.View.panelsManager import PanelsManager
from src.main.Model.gameState import GameState
from test.util.mockUtil import create_mock


class TestGUI(unittest.TestCase):
    def setUp(self):
        self.__real_views_holder = gui.PanelsManager
        self.__panels_manager = create_mock(PanelsManager)
        gui.PanelsManager = lambda _: self.__panels_manager

        self.__game_window = create_mock(GameWindow)

    def tearDown(self):
        gui.PanelsManager = self.__real_views_holder

    def test_display_clears_and_refills_window(self):
        game_controller = create_mock(GameController)
        gui_under_test = gui.GUI(self.__game_window, game_controller)

        gui_under_test.draw(create_mock(GameState))

        self.__game_window.clear.assert_called_once()
        self.__panels_manager.draw.assert_called_once()

    def test_no_click_or_button_press_produces_no_change_event(self):
        game_controller = create_mock(GameController)
        game_controller.get_mouse_event = lambda: None
        game_controller.get_key_event = lambda: None
        gui_under_test = gui.GUI(self.__game_window, game_controller)
        gui_under_test.draw(create_mock(GameState))

        change_event = gui_under_test.trigger_control_logic()

        self.assertIsNone(change_event)
