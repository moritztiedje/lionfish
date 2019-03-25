from abc import ABCMeta, abstractmethod


class Panel(metaclass=ABCMeta):
    def __init__(self, game_window, z_index):
        """
        :type game_window: src.main.GUI.View.gameWindow.GameWindow
        """
        self._game_window = game_window
        self.__buttons = []
        self.__is_active = False
        self._camera_zoom = 1
        self._image_vault = None
        self.__z_index = z_index

    def is_active(self):
        return self.__is_active

    def has_z_index(self, z_index):
        return self.__z_index == z_index

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
        if not self.__is_active:
            self.__is_active = True
            self._image_vault = self._load_image_vault()

    def deactivate(self):
        self.__is_active = False
        self._image_vault = None

    def register_button(self, button):
        """
        :type button: src.main.GUI.BaseComponents.button.Button
        """
        self.__buttons.append(button)

    def handle_mouse_event(self, mouse_event):
        """
        :type mouse_event: src.main.GUI.Controller.mouseEvent.MouseEvent
        """
        for button in self.__buttons:
            game_state_change_event = button.handle_mouse_event(mouse_event)
            if game_state_change_event:
                return game_state_change_event

        return self._handle_mouse_event(mouse_event)

    @abstractmethod
    def _handle_mouse_event(self, mouse_event):
        """
        :type mouse_event: src.main.GUI.Controller.mouseEvent.MouseEvent
        """

    def draw(self, game_state):
        """
        :type game_state: main.gameState.GameState
        """
        for button in self.__buttons:
            button.draw(self._game_window)
