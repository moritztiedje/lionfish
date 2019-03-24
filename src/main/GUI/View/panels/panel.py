from abc import ABCMeta, abstractmethod


class Panel(metaclass=ABCMeta):
    def __init__(self, game_window):
        """
        :type game_window: src.main.GUI.View.gameWindow.GameWindow
        """
        self._game_window = game_window
        self.__buttons = []
        self.__is_active = False
        self._camera_zoom = 1
        self._image_vault = None

    def is_active(self):
        return self.__is_active

    @abstractmethod
    def _load_image_vault(self):
        """
        :rtype: src.main.GUI.View.imageVault.ImageVault
        """
        return None

    def zoom_in(self):
        self._camera_zoom *= 2
        self._image_vault.set_camera_zoom(self._camera_zoom)

    def zoom_out(self):
        self._camera_zoom /= 2
        self._image_vault.set_camera_zoom(self._camera_zoom)

    def activate(self):
        self.__is_active = True
        self._image_vault = self._load_image_vault()

    def deactivate(self):
        self.__is_active = False
        self._image_vault = None

    def register_button(self, button):
        """
        :type button: main.GUI.button.Button
        """
        self.__buttons.append(button)

    def handle_click(self, mouse_clicked_position):
        for button in self.__buttons:
            button.handle_click(mouse_clicked_position)

    def handle_relative_click(self, relative_mouse_clicked_position):
        pass

    def display(self, game_state):
        """
        :type game_state: main.gameState.GameState
        """
        for button in self.__buttons:
            button.display(self._game_window)
