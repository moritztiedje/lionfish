import pygame

from src.main.GUI.BaseComponents.geometry import Point, Rectangle
from src.main.GUI.Controller.keyEvent import KeyEventTypes
from src.main.GUI.Controller.mouseEvent import MouseEventTypes
from src.main.GUI.View.imageVaults.textAdventureImageVault import TextAdventureImageVault, TextAdventureImageEnum
from src.main.GUI.View.panels.panel import Panel
from src.main.Model.gameStateChangeEvent import GameStateChangeEvent, GameStateChangeEventTypes

MINIMUM_HEIGHT = 200
BOTTOM_BORDER = 10
TOP_BORDER = 10
RIGHT_BORDER = 20
LEFT_BORDER = 20
HEIGHT_OF_LINE = 20


class TextAdventurePanel(Panel):
    def __init__(self, game_window):
        """
        :type game_window: src.main.GUI.View.gameWindow.GameWindow
        """
        super().__init__(game_window, 1)
        self.__y_offset = 0
        self.__selection_hitboxes = []
        self.__height = MINIMUM_HEIGHT
        border_height = 20
        self.__max_height = game_window.get_height() - border_height - 50

    def handle_key_event(self, key_event):
        """
        :type key_event: src.main.GUI.Controller.keyEvent.KeyEventTypes
        """
        if self.__height == self.__max_height:
            top_of_displayed_text = self.__max_height - self.__y_offset - BOTTOM_BORDER
            if key_event == KeyEventTypes.DOWN_PRESS and self._camera_position.get_y() >= top_of_displayed_text:
                self._camera_position -= Point(0, 10)
            elif key_event == KeyEventTypes.UP_PRESS and self._camera_position.get_y() <= -10:
                self._camera_position += Point(0, 10)

    def _handle_mouse_event(self, mouse_event):
        """
        :type mouse_event: src.main.GUI.Controller.mouseEvent.MouseEvent
        """
        if mouse_event.get_type() is MouseEventTypes.LeftClick:
            for index in range(len(self.__selection_hitboxes)):
                relative_mouse_position = self._calculate_relative_position_of(mouse_event.get_position())
                if self.__selection_hitboxes[index].is_inside(relative_mouse_position):
                    return GameStateChangeEvent(GameStateChangeEventTypes.SelectTextAdventureOption, index)

    def _load_image_vault(self):
        """
        :rtype: src.main.GUI.View.imageVaults.textAdventureImageVault.TextAdventureImageVault
        """
        return TextAdventureImageVault(self._game_window)

    def draw(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        super().draw(game_state)
        self.__height = MINIMUM_HEIGHT
        self.__draw_once(game_state)

        if self.__y_offset > self.__max_height:
            self.__height = self.__max_height
            self._image_vault.get_image(TextAdventureImageEnum.BACKGROUND).scale_to_height(self.__height)
            self.__draw_once(game_state)
        elif self.__y_offset > self.__height - TOP_BORDER - BOTTOM_BORDER:
            self.__height = self.__y_offset + TOP_BORDER + BOTTOM_BORDER
            self._image_vault.get_image(TextAdventureImageEnum.BACKGROUND).scale_to_height(self.__height)
            self.__draw_once(game_state)

    def __draw_once(self, game_state):
        self.__reset()
        self.__draw_background()
        self.__draw_content(game_state)
        self.__draw_border()

    def __reset(self):
        self.__y_offset = 0
        self.__selection_hitboxes = []

    def __draw_background(self):
        self._game_window.draw(
                self._image_vault.get_sprite(TextAdventureImageEnum.BACKGROUND),
                Point(0, self.__height)
        )

    def __draw_border(self):
        border_height = self._image_vault.get_image(TextAdventureImageEnum.TOP_BORDER).get_height()
        self._game_window.draw(
                self._image_vault.get_sprite(TextAdventureImageEnum.TOP_BORDER),
                Point(0, self.__height + border_height)
        )

    def __draw_content(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        for selection in game_state.get_text_adventure_state().get_old_selections():
            self.__print_paragraphs(selection.text, color=pygame.Color('darkgray'))
            for option in selection.options:
                self.__print_new_line(option, line_offset=10, color=pygame.Color('darkgray'))
            self.__print_new_line("")

        current_selection = game_state.get_text_adventure_state().get_current_selection()
        self.__print_paragraphs(current_selection.text)
        for option in current_selection.options:
            self.__selection_hitboxes.append(self.__print_new_line(option, line_offset=10))

    def __print_paragraphs(self, text, line_offset=0, color=pygame.Color('black')):
        for paragraph in text.split('\n'):
            self.__print_new_line(paragraph, line_offset, color)

    def __print_new_line(self, text, line_offset=0, color=pygame.Color('black')):
        """
        :type text: str
        :type line_offset: int
        :type color: pygame.Color
        :rtype: src.main.GUI.BaseComponents.geometry.Rectangle
        """
        font = pygame.font.SysFont("Times New Roman", HEIGHT_OF_LINE)
        width_of_space = font.size(' ')[0]
        max_width = self._game_window.get_width() - RIGHT_BORDER - LEFT_BORDER - line_offset

        top_left_of_first_word = None
        bottom_right_of_last_word = None

        length_of_current_line = 0
        words = text.split(' ')
        for word in words:
            rendered_word = font.render(word, 0, color)
            word_width = rendered_word.get_width()
            if length_of_current_line + word_width >= max_width:
                length_of_current_line = 0
                self.__y_offset += HEIGHT_OF_LINE
            draw_coordinate = Point(LEFT_BORDER + line_offset + length_of_current_line,
                                    self.__height - TOP_BORDER - self.__y_offset)
            if not top_left_of_first_word:
                top_left_of_first_word = draw_coordinate
            bottom_right_of_last_word = draw_coordinate + Point(rendered_word.get_width(), -HEIGHT_OF_LINE)
            if self.__is_inside_panel(draw_coordinate):
                self._draw_relative_to_camera(rendered_word, draw_coordinate)
            length_of_current_line += word_width + width_of_space
        self.__y_offset += HEIGHT_OF_LINE

        return Rectangle.from_upper_left_and_lower_right(top_left_of_first_word, bottom_right_of_last_word)

    def __is_inside_panel(self, draw_coordinate):
        border_height = self._image_vault.get_image(TextAdventureImageEnum.TOP_BORDER).get_height()
        return (draw_coordinate - self._camera_position).get_y() < self.__max_height + border_height
