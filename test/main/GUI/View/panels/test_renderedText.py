from unittest import TestCase

import pygame

from src.main.GUI.BaseComponents.geometry import Point
from src.main.GUI.View.panels.renderedText import RenderedParagraph

HEIGHT_OF_LINE = 20


class TestRenderedText(TestCase):
    def test_get_hitbox_of_single_line_text(self):
        pygame.init()
        right_border_wide = 180
        font = pygame.font.SysFont("Times New Roman", HEIGHT_OF_LINE)
        color = pygame.Color('black')
        rendered_paragraph = RenderedParagraph("dummy text", Point(1, 1), right_border_wide, font, HEIGHT_OF_LINE, color)
        hitbox = rendered_paragraph.get_hitbox()

        self.assertEqual(hitbox.get_draw_coordinate(), Point(1, 1))
        self.assertEqual(hitbox.get_height(), HEIGHT_OF_LINE)
        self.assertAlmostEqual(hitbox.get_width(),
                               font.render("dummy text", 0, color).get_width(),
                               places=-1)

    def test_get_hitbox_of_double_line_text(self):
        pygame.init()
        right_border_narrow = 80
        font = pygame.font.SysFont("Times New Roman", HEIGHT_OF_LINE)
        color = pygame.Color('black')
        rendered_text = RenderedParagraph("dummy text", Point(1, 1), right_border_narrow, font, HEIGHT_OF_LINE, color)
        hitbox = rendered_text.get_hitbox()

        self.assertEqual(hitbox.get_draw_coordinate(), Point(1, 1))
        self.assertEqual(hitbox.get_height(), 2 * HEIGHT_OF_LINE)
        self.assertEqual(hitbox.get_width(), right_border_narrow - 1)
