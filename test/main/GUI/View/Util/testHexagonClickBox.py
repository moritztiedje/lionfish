import unittest

from src.main.GUI.View.Util.hexagonClickBox import HexagonClickBox
from hamcrest import assert_that


class TestHexagonClickBox(unittest.TestCase):
    def testEveryHexagonHasCorrectClickBox(self):
        hexagons_with_points_in_them = [
            ((0, 0), [[1, -52], [49, -1], [103, -1], [151, -52], [103, -103], [49, -103]]),
            ((0, 1), [[1, 52], [49, 103], [103, 103], [151, 52], [103, 1], [49, 1]]),
            ((1, 0), [[105, 0], [153, 51], [207, 51], [255, 0], [207, -51], [153, -51]]),
            ((1, 1), [[105, 104], [153, 155], [207, 155], [255, 104], [207, 53], [153, 53]]),
        ]

        click_box = HexagonClickBox()

        for hexagon, points_in_hexagon in hexagons_with_points_in_them:
            for point in points_in_hexagon:
                self.assertEqual(click_box.get_hexagon(point),
                                 hexagon,
                                 "Point: " + str(point) + " is not in hexagon: " + str(hexagon))

    def testClicksOutsideOfGame(self):
        points_outside_of_game = [[153, -53], [105, -105], [47, -105], [-1, -52], [47, 0]]

        click_box = HexagonClickBox()

        for point in points_outside_of_game:
            hexagon = click_box.get_hexagon(point)
            assert_that(hexagon[0] == -1 or hexagon[1] == -1,
                        "Point: " + str(point) + " should be outside of game board.")

    def testEveryHexagonHasCorrectClickBoxAfter1ZoomIn(self):
        hexagons_with_points_in_them = [
            ((0, 0), [[1, -104], [97, -1], [207, -1], [303, -104], [207, -207], [97, -207]]),
            ((0, 1), [[1, 104], [97, 207], [207, 207], [303, 104], [207, 1], [97, 1]]),
            ((1, 0), [[209, 0], [305, 103], [415, 103], [511, 0], [415, -103], [305, -103]]),
            ((1, 1), [[209, 208], [305, 307], [415, 307], [511, 208], [415, 105], [305, 105]]),
        ]

        click_box = HexagonClickBox()
        click_box.set_zoom_level(2)

        for hexagon, points_in_hexagon in hexagons_with_points_in_them:
            for point in points_in_hexagon:
                self.assertEqual(click_box.get_hexagon(point),
                                 hexagon,
                                 "Point: " + str(point) + " is not in hexagon: " + str(hexagon))
