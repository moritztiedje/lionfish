class GUI:
    def __init__(self, game_window, game_controller):
        """
        :type game_window: main.gameWindow.GameWindow
        :type game_controller: main.gameController.GameController
        """
        self.__game_window = game_window
        self.__game_controller = game_controller

        self.__views = []

    def register_view(self, view, view_handle):
        self.__views.append((view, view_handle))

    def trigger_control_logic(self):
        mouse_click = self.__game_controller.mouse_click()
        if mouse_click:
            self.__handle_click(mouse_click)

        self.__game_controller.handle_base_logic()

    def __handle_click(self, mouse_position):
        for view, view_handle in self.__views:
            if view_handle():
                view.handle_click(mouse_position)

    def display(self, game_state):
        self.__game_window.clear()

        for view, view_handle in self.__views:
            if view_handle():
                view.display(game_state)
