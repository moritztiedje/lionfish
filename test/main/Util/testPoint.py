import unittest

from src.main.GUI.BaseComponents.geometry import Point


class TestPoint(unittest.TestCase):
    def testPointEqualityPointAndNone(self):
        self.assertNotEqual(Point(0, 0), None)

    def testPointEqualityNoneAndPoint(self):
        self.assertNotEqual(None, Point(0, 0))

    def testPointEqualityPointAndDifferentPoint(self):
        self.assertNotEqual(Point(0, 0), Point(1, 0))

    def testPointEqualitySamePoint(self):
        self.assertEqual(Point(0, 0), Point(0, 0))
