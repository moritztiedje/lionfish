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

        self.__display_has_changed = True
        self.display(game_state)

    def trigger_control_logic(self):
        mouse_click, mouse_relative_click = self.__game_controller.mouse_left_click()
        if mouse_click:
            mouse_was_clicked = True
            self.__views_holder.handle_click(mouse_click, mouse_relative_click)
        else:
            mouse_was_clicked = False

        base_logic_has_changed_display = self.__game_controller.handle_base_logic()
        self.__display_has_changed = mouse_was_clicked or base_logic_has_changed_display

    def display(self, game_state):
        if self.__display_has_changed:
            self.__game_window.clear()
            self.__views_holder.display(game_state)
            self.__display_has_changed = False
