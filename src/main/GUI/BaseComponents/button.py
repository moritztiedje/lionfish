from src.main.GUI.BaseComponents.geometry import Point, Rectangle
from src.main.GUI.Controller.mouseEvent import MouseEventTypes


class Button:
    def __init__(self, bottom_left, top_right, image, action):
        """
        :type bottom_left: src.main.GUI.BaseComponents.geometry.Point
        :type top_right: src.main.GUI.BaseComponents.geometry.Point
        :type action: function
        """
        self.__button_area = Rectangle(bottom_left, top_right)
        self.__image = image
        self.__action = action

    def handle_mouse_event(self, mouse_event):
        """
        :type mouse_event: src.main.GUI.Controller.mouseEvent.MouseEvent
        :rtype: src.main.Model.gameStateChangeEvent.GameStateChangeEvent
        """
        if self.__button_clicked(mouse_event):
            return self.__action()

    def __button_clicked(self, mouse_event):
        """
        :type mouse_event: src.main.GUI.Controller.mouseEvent.MouseEvent
        """
        if mouse_event.get_type() != MouseEventTypes.LeftClick:
            return False
        return self.__button_area.is_inside(mouse_event.get_position())

    def draw(self, game_window):
        game_window.draw(self.__image.sprite, self.__button_area.get_draw_coordinate())
