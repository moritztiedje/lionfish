from unittest import TestCase

import pygame

from src.main.GUI.BaseComponents.geometry import Point
from src.main.GUI.View.panels.textAdventurePanel import RenderedText, HEIGHT_OF_LINE


class TestRenderedText(TestCase):
    def test_get_hitbox_of_single_line_text(self):
        pygame.init()
        right_border_wide = 180
        rendered_text = RenderedText("dummy text", Point(1, 1), right_border_wide)
        hitbox = rendered_text.get_hitbox()

        self.assertEqual(hitbox.get_draw_coordinate(), Point(1, 1))
        self.assertEqual(hitbox.get_height(), HEIGHT_OF_LINE)
        sys_font = pygame.font.SysFont("Times New Roman", HEIGHT_OF_LINE)
        self.assertAlmostEqual(hitbox.get_width(),
                               sys_font.render("dummy text", 0, pygame.Color('black')).get_width(),
                               places=-1)

    def test_get_hitbox_of_double_line_text(self):
        pygame.init()
        right_border_narrow = 80
        rendered_text = RenderedText("dummy text", Point(1, 1), right_border_narrow)
        hitbox = rendered_text.get_hitbox()

        self.assertEqual(hitbox.get_draw_coordinate(), Point(1, 1))
        self.assertEqual(hitbox.get_height(), 2 * HEIGHT_OF_LINE)
        self.assertEqual(hitbox.get_width(), right_border_narrow - 1)
