import pygame

from src.main.GUI.BaseComponents.geometry import Point, Rectangle
from src.main.GUI.Controller.keyEvent import KeyEventTypes
from src.main.GUI.Controller.mouseEvent import MouseEventTypes
from src.main.GUI.View.image import Image
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
        self.__options = []
        self.__lines = []
        self.__height = MINIMUM_HEIGHT
        border_height = 20
        self.__max_height = game_window.get_height() - border_height - 50
        self.__close_button = CloseButton()

    def handle_key_event(self, key_event):
        """
        :type key_event: src.main.GUI.Controller.keyEvent.KeyEventTypes
        """
        if self.__height == self.__max_height:
            top_of_displayed_text = self.__max_height - self.__y_offset - BOTTOM_BORDER
            if key_event == KeyEventTypes.DOWN_PRESS and self._camera_position.get_y() >= top_of_displayed_text:
                self._camera_position -= Point(0, 10)
                self.__draw_rendered_content()
            elif key_event == KeyEventTypes.UP_PRESS and self._camera_position.get_y() <= -10:
                self._camera_position += Point(0, 10)
                self.__draw_rendered_content()

    def _handle_mouse_event(self, mouse_event):
        """
        :type mouse_event: src.main.GUI.Controller.mouseEvent.MouseEvent
        """
        if mouse_event.get_type() is MouseEventTypes.LeftClick:
            close_panel_change_event = self.__close_button.handle_mouse_click(mouse_event.get_position())
            if close_panel_change_event:
                return close_panel_change_event
            option_selected_change_event = self.__handle_mouse_click(mouse_event.get_position())
            if option_selected_change_event:
                return option_selected_change_event
        elif mouse_event.get_type() is MouseEventTypes.Hover:
            relative_mouse_position = self._calculate_relative_position_of(mouse_event.get_position())
            self.__highlight_hovered_option(relative_mouse_position)

    def __handle_mouse_click(self, mouse_position):
        for index in range(len(self.__options)):
            relative_mouse_position = self._calculate_relative_position_of(mouse_position)
            if self.__options[index].get_hitbox().contains(relative_mouse_position):
                return GameStateChangeEvent(GameStateChangeEventTypes.SelectTextAdventureOption, index)

    def __highlight_hovered_option(self, mouse_position):
        """
        :type mouse_position: src.main.GUI.BaseComponents.geometry.Point
        """
        highlighting_has_changed = False
        for index in range(len(self.__options)):
            if self.__options[index].get_hitbox().contains(mouse_position):
                if not self.__options[index].is_highlighted():
                    self.__options[index].highlight()
                    highlighting_has_changed = True
            elif self.__options[index].is_highlighted():
                self.__options[index].un_highlight()
                highlighting_has_changed = True
        if highlighting_has_changed:
            self.__draw_rendered_content()

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
        self.__render(game_state)
        self.__draw_rendered_content()

    def __render(self, game_state):
        self.__height = MINIMUM_HEIGHT
        self.__reset_rendered_content()
        self.__render_content(game_state)

        if self.__y_offset > self.__max_height:
            self.__height = self.__max_height
            self.__resize_panel()
            self._camera_position = Point(0, self.__max_height - self.__y_offset - HEIGHT_OF_LINE)
        elif self.__y_offset > self.__height - TOP_BORDER - BOTTOM_BORDER:
            self.__height = self.__y_offset + TOP_BORDER + BOTTOM_BORDER
            self.__resize_panel()

        if game_state.get_text_adventure_state().is_completed():
            self.__close_button.render(self._game_window.get_width(), self.__height)

    def __resize_panel(self):
        self._get_image_vault().get_image(TextAdventureImageEnum.BACKGROUND).scale_to_height(self.__height)
        for line in self.__lines:
            line.shift_upwards(self.__height - MINIMUM_HEIGHT)
        for option in self.__options:
            option.shift_upwards(self.__height - MINIMUM_HEIGHT)

    def __reset_rendered_content(self):
        self.__y_offset = 0
        self.__options = []
        self.__lines = []

    def __render_content(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        for selection in game_state.get_text_adventure_state().get_old_selections():
            self.__render_paragraphs(selection.text, color=pygame.Color('darkgray'))
            for option in selection.options:
                self.__lines.append(self.__render_new_line(option.text, line_offset=10, color=pygame.Color('darkgray')))
            self.__lines.append(self.__render_new_line(""))

        current_selection = game_state.get_text_adventure_state().get_current_selection()
        self.__render_paragraphs(current_selection.text)
        for option in current_selection.options:
            text_color = self.__determine_color_of(option.success_chance)
            self.__options.append(self.__render_new_line(option.text, line_offset=10, color=text_color))

    def __draw_rendered_content(self):
        self.__draw_background()
        for line in self.__lines:
            line.draw(self._draw_relative_to_camera, self._draw_rectangle_relative_to_camera)
        for option in self.__options:
            option.draw(self._draw_relative_to_camera, self._draw_rectangle_relative_to_camera)
        self.__draw_border()
        self.__close_button.draw(self._game_window.draw)

    def _draw_relative_to_camera(self, sprite, point):
        is_inside_text_adventure_panel = (point - self._camera_position).get_y() < self.__height
        if is_inside_text_adventure_panel:
            super()._draw_relative_to_camera(sprite, point)

    def __draw_background(self):
        self._game_window.draw(
                self._get_image_vault().get_sprite(TextAdventureImageEnum.BACKGROUND),
                Point(0, self.__height)
        )

    def __draw_border(self):
        border_height = self._get_image_vault().get_image(TextAdventureImageEnum.TOP_BORDER).get_height()
        self._game_window.draw(
                self._get_image_vault().get_sprite(TextAdventureImageEnum.TOP_BORDER),
                Point(0, self.__height + border_height)
        )

    def __render_paragraphs(self, text, line_offset=0, color=pygame.Color('black')):
        for paragraph in text.split('\n'):
            self.__lines.append(self.__render_new_line(paragraph, line_offset, color))

    def __render_new_line(self, text, line_offset=0, color=pygame.Color('black')):
        """
        :type text: str
        :type line_offset: int
        :type color: pygame.Color
        :rtype: src.main.GUI.View.panels.textAdventurePanel.RenderedText
        """
        rendered_text = RenderedText(text,
                                     Point(LEFT_BORDER + line_offset, self.__height - TOP_BORDER - self.__y_offset),
                                     self._game_window.get_width() - RIGHT_BORDER,
                                     color=color)
        self.__y_offset += rendered_text.get_hitbox().get_height()
        return rendered_text

    @staticmethod
    def __determine_color_of(success_chance):
        """
        :type success_chance: float
        """
        if not success_chance:
            return pygame.Color('black')
        elif success_chance > 0.75:
            return pygame.Color('green')
        elif success_chance > 0.25:
            return pygame.Color('yellow')
        return pygame.Color('red')


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
        self.__is_highlighted = False
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
                draw_coordinate_of_word = Point(draw_coordinate.get_x(),
                                                draw_coordinate_of_word.get_y() - HEIGHT_OF_LINE)
            draw_coordinate_of_next_word = draw_coordinate_of_word + Point(word_width + space_width, 0)
            self.__words.append(RenderedWord(rendered_word, draw_coordinate_of_word))

            draw_coordinate_of_word = draw_coordinate_of_next_word

        if draw_coordinate_of_word.get_y() == draw_coordinate.get_y():
            self.__hitbox = Rectangle.from_upper_left_and_lower_right(
                    draw_coordinate,
                    draw_coordinate_of_next_word - Point(space_width, HEIGHT_OF_LINE))
        else:
            self.__hitbox = Rectangle.from_upper_left_and_lower_right(
                    draw_coordinate,
                    Point(right_border, draw_coordinate_of_next_word.get_y() - HEIGHT_OF_LINE))

    def draw(self, _draw_relative_to_camera, _draw_rectangle_relative_to_camera):
        if self.is_highlighted():
            _draw_rectangle_relative_to_camera(self.get_hitbox(), 'darkgrey')
        for word in self.__words:
            word.draw(_draw_relative_to_camera)

    def shift_upwards(self, shift_by):
        """
        :type shift_by: int
        """
        self.__hitbox += Point(0, shift_by)
        for word in self.__words:
            word.shift_upwards(shift_by)

    def highlight(self):
        self.__is_highlighted = True

    def is_highlighted(self):
        """
        :rtype: bool
        """
        return self.__is_highlighted

    def un_highlight(self):
        self.__is_highlighted = False

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

    def shift_upwards(self, shift_by):
        """
        :type shift_by: int
        """
        self.__draw_coordinate += Point(0, shift_by)


class CloseButton:
    def __init__(self):
        self.__close_button_hitbox = None
        self.__sprite = Image(30, 30, '../../artwork/images/menu/close.png').sprite

    def render(self, text_adventure_panel_width, text_adventure_panel_height):
        """
        :type text_adventure_panel_width: int
        :type text_adventure_panel_height: int
        """
        self.__close_button_hitbox = Rectangle(
                Point(text_adventure_panel_width - 40, text_adventure_panel_height - 40),
                Point(text_adventure_panel_width - 10, text_adventure_panel_height - 10)
        )

    def draw(self, draw_absolute):
        if self.__close_button_hitbox:
            draw_absolute(self.__sprite,
                          Point(self.__get_close_button_hitbox().get_left(),
                                self.__get_close_button_hitbox().get_top()))

    def handle_mouse_click(self, mouse_coordinate):
        """
        :type point:
        """
        if self.__get_close_button_hitbox() and self.__get_close_button_hitbox().contains(mouse_coordinate):
            self.__close_button_hitbox = None
            return GameStateChangeEvent(GameStateChangeEventTypes.CloseTextAdventure, None)

    def __get_close_button_hitbox(self):
        """
        :rtype: src.main.GUI.BaseComponents.geometry.Rectangle
        """
        return self.__close_button_hitbox
