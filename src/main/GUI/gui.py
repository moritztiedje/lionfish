from src.main.GUI.Controller.mouseEvent import MouseEventEnum
from src.main.GUI.View.panelsManager import PanelsManager


class GUI:
    def __init__(self, game_window, game_controller):
        """
        :type game_window: src.main.GUI.View.gameWindow.GameWindow
        :type game_controller: src.main.GUI.Controller.gameController.GameController
        """
        self.__game_window = game_window
        self.__game_controller = game_controller
        self.__views_holder = PanelsManager(game_window)

        self.__display_has_changed = True

    def trigger_control_logic(self):
        """
        :rtype: src.main.Model.gameStateChangeEvent.GameStateChangeEvent
        """
        mouse_event = self.__game_controller.get_mouse_event()
        base_logic_has_changed_display = self.__game_controller.handle_base_logic()
        if mouse_event:
            self.__display_has_changed = True
            return self.__views_holder.handle_mouse_event(mouse_event)
        else:
            self.__display_has_changed = base_logic_has_changed_display

    def has_something_changed(self):
        return self.__display_has_changed

    def draw(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        self.__game_window.clear()
        self.__views_holder.draw(game_state)
        self.__display_has_changed = False
