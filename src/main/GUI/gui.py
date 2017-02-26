from src.main.GUI.View.viewsHolder import ViewsHolder


class GUI:
    def __init__(self, game_window, game_controller, game_state):
        """
        :type game_window: main.gameWindow.GameWindow
        :type game_controller: main.gameController.GameController
        """
        self.__game_window = game_window
        self.__game_controller = game_controller
        self.__views_holder = ViewsHolder(game_window)

    def trigger_control_logic(self):
        mouse_click = self.__game_controller.mouse_left_click()
        if mouse_click:
            self.__views_holder.handle_click(mouse_click)

        self.__game_controller.handle_base_logic()

    def display(self, game_state):
        self.__game_window.clear()
        self.__views_holder.display(game_state)
