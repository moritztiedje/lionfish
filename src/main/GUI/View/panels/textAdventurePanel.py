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
        rendered_text = RenderedText(text,
                                     Point(LEFT_BORDER + line_offset, self.__height - TOP_BORDER - self.__y_offset),
                                     self._game_window.get_width() - RIGHT_BORDER,
                                     color=color)
        self.__y_offset += rendered_text.get_hitbox().get_height()
        rendered_text.draw(self._draw_relative_to_camera)
        return rendered_text.get_hitbox()


class RenderedText:
    def __init__(self, text, draw_coordinate, right_border,
                 font="Times New Roman",
                 color=pygame.Color('black')):
        """
        :type text: str
        :type draw_coordinate: src.main.GUI.BaseComponents.geometry.Point
        :type right_border: int
        :type color: pygame.color.Color
        :type font: str
        """
        self.__draw_coordinate = draw_coordinate
        self.__words = []

        sys_font = pygame.font.SysFont(font, HEIGHT_OF_LINE)
        words = text.split(' ')
        draw_coordinate_of_word = draw_coordinate
        draw_coordinate_of_next_word = draw_coordinate
        space_width = sys_font.render(" ", 0, color).get_width()
        for word in words:
            rendered_word = sys_font.render(word, 0, color)
            word_width = rendered_word.get_width()
            if draw_coordinate_of_word.get_x() + word_width >= right_border:
                draw_coordinate_of_word = Point(draw_coordinate.get_x(), draw_coordinate_of_word.get_y() - HEIGHT_OF_LINE)
            draw_coordinate_of_next_word = draw_coordinate_of_word + Point(word_width + space_width, 0)
            self.__words.append(RenderedWord(rendered_word, draw_coordinate_of_word))

            draw_coordinate_of_word = draw_coordinate_of_next_word

        self.__hitbox = Rectangle.from_upper_left_and_lower_right(
                draw_coordinate,
                draw_coordinate_of_next_word - Point(0, HEIGHT_OF_LINE))

    def draw(self, _draw_relative_to_camera):
        for word in self.__words:
            word.draw(_draw_relative_to_camera)

    def get_hitbox(self):
        """
        :rtype: src.main.GUI.BaseComponents.geometry.Rectangle
        """
        return self.__hitbox


class RenderedWord:
    def __init__(self, word, draw_coordinate):
        """
        :type word: pygame.ftfont.Font
        :type draw_coordinate: src.main.GUI.BaseComponents.geometry.Point
        """
        self.__rendered_word = word
        self.__draw_coordinate = draw_coordinate

    def draw(self, _draw_relative_to_camera):
        _draw_relative_to_camera(self.__rendered_word, self.__draw_coordinate)
