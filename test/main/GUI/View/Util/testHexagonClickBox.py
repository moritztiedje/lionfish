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

        for hexagon, points_in_hexagon in hexagons_with_points_in_them:
            for point in points_in_hexagon:
                self.assertEqual(HexagonClickBox.get_hexagon(point),
                                 hexagon,
                                 "Point: " + str(point) + " is not in hexagon: " + str(hexagon))

    def testClicksOutsideOfGame(self):
        points_outside_of_game = [[153, -53], [105, -105], [47, -105], [-1, -52], [47, 0]]

        for point in points_outside_of_game:
            hexagon = HexagonClickBox.get_hexagon(point)
            assert_that(hexagon[0] == -1 or hexagon[1] == -1,
                        "Point: " + str(point) + " should be outside of game board.")
