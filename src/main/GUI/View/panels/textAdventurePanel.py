from src.main.GUI.BaseComponents.geometry import Point, Rectangle
from src.main.GUI.Controller.keyEvent import KeyEventTypes
from src.main.GUI.Controller.mouseEvent import MouseEventTypes
from src.main.GUI.View.image import Image
from src.main.GUI.View.imageVaults.textAdventureImageVault import TextAdventureImageVault, TextAdventureImageEnum
from src.main.GUI.View.panels.panel import Panel
from src.main.GUI.View.panels.renderedText import ParagraphRenderer
from src.main.Model.gameStateChangeEvent import GameStateChangeEvent, GameStateChangeEventTypes

MINIMUM_HEIGHT = 200
BOTTOM_MARGIN = 10
TOP_BORDER = 10
RIGHT_MARGIN = 20
LEFT_MARGIN = 20
HEIGHT_OF_LINE = 20
FONT_NAME = 'Berlin Sans FB'


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
            top_of_displayed_text = self.__max_height - self.__y_offset - BOTTOM_MARGIN
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
        elif self.__y_offset > self.__height - TOP_BORDER - BOTTOM_MARGIN:
            self.__height = self.__y_offset + TOP_BORDER + BOTTOM_MARGIN
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
            self.__render_paragraphs(selection.text, color='darkgray')
            for option in selection.options:
                self.__lines.append(self.__render_new_line(option.text, line_offset=10, color='darkgray'))
            self.__lines.append(self.__render_new_line(""))

        current_selection = game_state.get_text_adventure_state().get_current_selection()
        self.__render_paragraphs(current_selection.text)
        for option in current_selection.options:
            text_color = self.__determine_color_of(option.success_chance)
            self.__options.append(self.__render_new_line(option.text, top_offset=5, line_offset=10, color=text_color))

    def __render_paragraphs(self, text, line_offset=0, color='black'):
        for paragraph in text.split('\n'):
            self.__lines.append(self.__render_new_line(paragraph, line_offset=line_offset, color=color))

    def __render_new_line(self, text, top_offset=0, line_offset=0, color='black'):
        """
        :type text: str
        :type top_offset: int
        :type line_offset: int
        :type color: pygame.Color
        :rtype: src.main.GUI.View.panels.textAdventurePanel.RenderedText
        """
        renderer = ParagraphRenderer(font_name=FONT_NAME, font_size=HEIGHT_OF_LINE, color=color)
        rendered_text = renderer.render_paragraph(text,
                                                  Point(LEFT_MARGIN + line_offset,
                                                        self.__height - TOP_BORDER - self.__y_offset - top_offset),
                                                  self._game_window.get_width() - RIGHT_MARGIN)
        self.__y_offset += rendered_text.get_height() + top_offset
        return rendered_text

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

    @staticmethod
    def __determine_color_of(success_chance):
        """
        :type success_chance: float
        """
        if not success_chance:
            return 'black'
        elif success_chance > 0.75:
            return 'green'
        elif success_chance > 0.25:
            return 'yellow'
        return 'red'


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
        :type mouse_coordinate: src.main.GUI.BaseComponents.geometry.Point
        """
        if self.__get_close_button_hitbox() and self.__get_close_button_hitbox().contains(mouse_coordinate):
            self.__close_button_hitbox = None
            return GameStateChangeEvent(GameStateChangeEventTypes.CloseTextAdventure, None)

    def __get_close_button_hitbox(self):
        """
        :rtype: src.main.GUI.BaseComponents.geometry.Rectangle
        """
        return self.__close_button_hitbox
