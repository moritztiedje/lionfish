import pygame


class MouseController:
    def __init__(self, window_height):
        """
        :type window_height: int
        """
        self.__window_height = window_height
        self.__left_was_pressed = False

    def mouse_left_click(self):
        left_mouse_has_clicked = not self.__left_was_pressed and self.__left_mouse_is_pressed()
        self.__left_was_pressed = self.__left_mouse_is_pressed()

        if left_mouse_has_clicked:
            mouse_position = pygame.mouse.get_pos()
            inverted_mouse = mouse_position[0], self.__window_height - mouse_position[1]
            return inverted_mouse

    @staticmethod
    def __left_mouse_is_pressed():
        return pygame.mouse.get_pressed()[0] == 1