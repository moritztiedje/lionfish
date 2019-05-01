from src.main.GUI.View.panelsManager import PanelsManager


class GUI:
    def __init__(self, game_window, game_controller):
        """
        :type game_window: src.main.GUI.View.gameWindow.GameWindow
        :type game_controller: src.main.GUI.Controller.gameController.GameController
        """
        self.__game_window = game_window
        self.__game_controller = game_controller
        self.__panels_manager = PanelsManager(game_window)

    def trigger_control_logic(self):
        """
        :rtype: src.main.Model.gameStateChangeEvent.GameStateChangeEvent
        """
        mouse_event = self.__game_controller.get_mouse_event()
        key_event = self.__game_controller.get_key_event()
        if mouse_event:
            game_state_change_event = self.__panels_manager.handle_mouse_event(mouse_event)
            if game_state_change_event:
                return game_state_change_event
        if key_event:
            return self.__panels_manager.handle_key_event(key_event)

    def draw(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        self.__game_window.clear()
        self.__panels_manager.draw(game_state)
