import unittest

from hamcrest import assert_that

from src.main.GUI.BaseComponents.geometry import Point
from src.main.GUI.View.Util.hexagonClickBox import HexagonClickBox


class TestHexagonClickBox(unittest.TestCase):
    def testEveryHexagonHasCorrectClickBox(self):
        hexagons_with_points_in_them = [
            (Point(0, 0), [
                Point(1, -52),
                Point(49, -1),
                Point(103, -1),
                Point(151, -52),
                Point(103, -103),
                Point(49, -103)
            ]),
            (Point(0, 1), [
                Point(1, 52),
                Point(49, 103),
                Point(103, 103),
                Point(151, 52),
                Point(103, 1),
                Point(49, 1)
            ]),
            (Point(1, 0), [
                Point(105, 0),
                Point(153, 51),
                Point(207, 51),
                Point(255, 0),
                Point(207, -51),
                Point(153, -51)
            ]),
            (Point(1, 1), [
                Point(105, 104),
                Point(153, 155),
                Point(207, 155),
                Point(255, 104),
                Point(207, 53),
                Point(153, 53)
            ]),
        ]

        click_box = HexagonClickBox()

        for hexagon, points_in_hexagon in hexagons_with_points_in_them:
            for point in points_in_hexagon:
                self.assertEqual(click_box.get_hexagon(point),
                                 hexagon,
                                 "Point: " + str(point) + " is not in hexagon: " + str(hexagon))

    def testClicksOutsideOfGame(self):
        points_outside_of_game = [
            Point(153, -53),
            Point(105, -105),
            Point(47, -105),
            Point(-1, -52),
            Point(47, 0)
        ]

        click_box = HexagonClickBox()

        for point in points_outside_of_game:
            hexagon = click_box.get_hexagon(point)
            assert_that(hexagon.get_x() == -1 or hexagon.get_y() == -1,
                        "Point: " + str(point) + " should be outside of game board.")

    def testEveryHexagonHasCorrectClickBoxAfter1ZoomIn(self):
        hexagons_with_points_in_them = [
            (Point(0, 0), [
                Point(1, -104),
                Point(97, -1),
                Point(207, -1),
                Point(303, -104),
                Point(207, -207),
                Point(97, -207)]),
            (Point(0, 1), [
                Point(1, 104),
                Point(97, 207),
                Point(207, 207),
                Point(303, 104),
                Point(207, 1),
                Point(97, 1)]),
            (Point(1, 0), [
                Point(209, 0),
                Point(305, 103),
                Point(415, 103),
                Point(511, 0),
                Point(415, -103),
                Point(305, -103)]),
            (Point(1, 1), [
                Point(209, 208),
                Point(305, 307),
                Point(415, 307),
                Point(511, 208),
                Point(415, 105),
                Point(305, 105)]),
        ]

        click_box = HexagonClickBox()
        click_box.set_zoom_level(2)

        for hexagon, points_in_hexagon in hexagons_with_points_in_them:
            for point in points_in_hexagon:
                self.assertEqual(click_box.get_hexagon(point),
                                 hexagon,
                                 "Point: " + str(point) + " is not in hexagon: " + str(hexagon))
