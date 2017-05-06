import unittest

from src.main.GUI import gui
from src.main.GUI.Controller.gameController import GameController
from src.main.GUI.View.gameWindow import GameWindow
from src.main.GUI.View.viewsHolder import ViewsHolder
from src.main.Model.gameState import GameState
from test.util.mockUtil import create_mock


class TestGUI(unittest.TestCase):
    def setUp(self):
        self.__real_views_holder = gui.ViewsHolder
        self.__views_holder = create_mock(ViewsHolder)
        gui.ViewsHolder = lambda _: self.__views_holder

        self.__game_window = create_mock(GameWindow)

    def tearDown(self):
        gui.ViewsHolder = self.__real_views_holder

    def assertOnlyInitializationRendering(self):
        self.__game_window.clear.assert_called_once()
        self.__views_holder.display.assert_called_once()

    def assertRenderingAfterInitialization(self):
        self.assertEqual(self.__game_window.clear.call_count, 2)
        self.assertEqual(self.__views_holder.display.call_count, 2)

    def test_game_window_displayed_on_start(self):
        game_controller = create_mock(GameController)

        gui.GUI(self.__game_window,
                game_controller,
                create_mock(GameState))

        self.assertOnlyInitializationRendering()

    def test_mouse_click_triggers_re_render(self):
        game_controller = create_mock(GameController)
        game_controller.mouse_left_click = lambda: (1, 1)
        game_controller.handle_base_logic = lambda: False
        gui_under_test = gui.GUI(self.__game_window,
                                 game_controller,
                                 create_mock(GameState))

        gui_under_test.trigger_control_logic()
        gui_under_test.display(create_mock(GameState))

        self.assertRenderingAfterInitialization()

    def test_no_click_or_button_press_triggers_nothing(self):
        game_controller = create_mock(GameController)
        game_controller.mouse_left_click = lambda: (None, None)
        game_controller.handle_base_logic = lambda: False
        gui_under_test = gui.GUI(self.__game_window,
                                 game_controller,
                                 create_mock(GameState))

        gui_under_test.trigger_control_logic()
        gui_under_test.display(create_mock(GameState))

        self.assertOnlyInitializationRendering()

    def test_button_press_triggers_re_render(self):
        game_controller = create_mock(GameController)
        game_controller.mouse_left_click = lambda: (None, None)
        game_controller.handle_base_logic = lambda: True
        gui_under_test = gui.GUI(self.__game_window,
                                 game_controller,
                                 create_mock(GameState))

        gui_under_test.trigger_control_logic()
        gui_under_test.display(create_mock(GameState))

        self.assertRenderingAfterInitialization()
