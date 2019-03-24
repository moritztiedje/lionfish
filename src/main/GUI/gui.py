from src.main.GUI.View.viewsHolder import ViewsHolder


class GUI:
    def __init__(self, game_window, game_controller):
        """
        :type game_window: src.main.GUI.View.gameWindow.GameWindow
        :type game_controller: src.main.GUI.Controller.gameController.GameController
        """
        self.__game_window = game_window
        self.__game_controller = game_controller
        self.__views_holder = ViewsHolder(game_window)

        self.__display_has_changed = True

    def trigger_control_logic(self):
        mouse_click, mouse_relative_click = self.__game_controller.get_mouse_left_click()
        if mouse_click:
            mouse_was_clicked = True
            self.__views_holder.handle_click(mouse_click, mouse_relative_click)
        else:
            mouse_was_clicked = False

        base_logic_has_changed_display = self.__game_controller.handle_base_logic()
        self.__display_has_changed = mouse_was_clicked or base_logic_has_changed_display

    def has_something_changed(self):
        return self.__display_has_changed

    def draw(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        self.__game_window.clear()
        self.__views_holder.display(game_state)
        self.__display_has_changed = False
