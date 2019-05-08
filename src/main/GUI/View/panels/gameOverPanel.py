from src.main.GUI.BaseComponents.geometry import Point
from src.main.GUI.View.imageVaults.gameOverImageVault import GameOverImageVault
from src.main.GUI.View.panels.panel import Panel
from src.main.GUI.View.panels.renderedText import ParagraphRenderer
from src.main.constants import GameOverImageEnum

HEIGHT_OF_LINE = 50
FONT = 'Arial Black'
TEXT_COLOR = 'darkblue'
SIDE_MARGIN = 100


class GameOverPanel(Panel):
    def __init__(self, game_window):
        super().__init__(game_window, 2)

    def _load_image_vault(self):
        return GameOverImageVault()

    def handle_key_event(self, key_event):
        pass

    def _handle_mouse_event(self, mouse_event):
        pass

    def draw(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        super().draw(game_state)

        background = self._get_image_vault().get_image(GameOverImageEnum.BACKGROUND)
        background.scale_to_height(self._game_window.get_height())
        background.scale_to_width(self._game_window.get_width())
        self._game_window.draw(background.sprite, Point(0, self._game_window.get_height()))

        right_border = self._game_window.get_width() - SIDE_MARGIN
        text = RenderedText(game_state.get_game_over_text(), right_border)
        text.shift_upwards((self._game_window.get_height() + text.get_height()) / 2)
        text.draw(self._game_window.draw)


class RenderedText:
    def __init__(self, text, right_border):
        """
        :type text: str
        """
        paragraph_renderer = ParagraphRenderer(font_name=FONT, font_size=HEIGHT_OF_LINE, color=TEXT_COLOR)
        self.__rendered_paragraphs = []

        paragraphs = text.split('\n')
        coordinate_of_paragraph = Point(SIDE_MARGIN, 0)
        for paragraph in paragraphs:
            rendered_paragraph = paragraph_renderer.render_paragraph(paragraph, coordinate_of_paragraph, right_border)
            rendered_paragraph.align_text_center()
            self.__rendered_paragraphs.append(rendered_paragraph)

            coordinate_of_paragraph -= Point(0, rendered_paragraph.get_height())

    def get_height(self):
        height = 0
        for rendered_paragraph in self.__rendered_paragraphs:
            height += rendered_paragraph.get_height()
        return height

    def draw(self, draw_method):
        for rendered_paragraph in self.__rendered_paragraphs:
            rendered_paragraph.draw(draw_method)

    def shift_right(self, shift_by):
        for rendered_paragraph in self.__rendered_paragraphs:
            rendered_paragraph.shift_right(shift_by)

    def shift_upwards(self, shift_by):
        for rendered_paragraph in self.__rendered_paragraphs:
            rendered_paragraph.shift_upwards(shift_by)
