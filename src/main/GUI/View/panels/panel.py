from abc import ABCMeta, abstractmethod

from src.main.GUI.BaseComponents.geometry import Point


class Panel(metaclass=ABCMeta):
    def __init__(self, game_window, z_index):
        """
        :type game_window: src.main.GUI.View.gameWindow.GameWindow
        """
        self._game_window = game_window
        self.__buttons = []
        self._camera_zoom = 1
        self._camera_position = Point(0, 0)
        self.__image_vault = None
        self.__z_index = z_index
        self.__is_active = False

    def _draw_relative_to_camera(self, sprite, point):
        """
        :type sprite: pygame.Surface
        :type point: src.main.GUI.BaseComponents.geometry.Point
        """
        self._game_window.draw(sprite, point - self._camera_position)

    def _draw_rectangle_relative_to_camera(self, area, color):
        """
        :type area: src.main.GUI.BaseComponents.geometry.Rectangle
        :type coordinate: src.main.GUI.BaseComponents.geometry.Point
        :type color: str
        """
        self._game_window.draw_rectangle(area - self._camera_position, color)

    def _calculate_relative_position_of(self, absolute_position):
        """
        :type absolute_position: src.main.GUI.BaseComponents.geometry.Point
        :rtype: src.main.GUI.BaseComponents.geometry.Point
        """
        return absolute_position + self._camera_position

    def _get_image_vault(self):
        """
        :rtype: src.main.GUI.View.imageVaults.imageVault.ImageVault
        """
        return self.__image_vault

    def is_active(self):
        return self.__is_active

    def activate(self):
        self.__is_active = True

    def deactivate(self):
        self.__is_active = False

    def load_images(self):
        if not self.__image_vault:
            self.__image_vault = self._load_image_vault()

    def discard_images(self):
        self.__image_vault = None

    def has_z_index(self, z_index):
        return self.__z_index == z_index

    @abstractmethod
    def _load_image_vault(self):
        """
        :rtype: src.main.GUI.View.imageVaults.imageVault.ImageVault
        """
        return None

    def zoom_in(self):
        self._camera_zoom *= 2
        self.__image_vault.set_camera_zoom(self._camera_zoom)

    def zoom_out(self):
        self._camera_zoom /= 2
        self.__image_vault.set_camera_zoom(self._camera_zoom)

    def _register_button(self, button):
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
    def handle_key_event(self, key_event):
        """
        :type key_event: src.main.GUI.Controller.keyEvent.KeyEventTypes
        """

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
