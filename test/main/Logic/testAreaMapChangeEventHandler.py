from unittest import TestCase

from src.main.GUI.BaseComponents.geometry import Point
from src.main.Logic.areaMapChangeEventHandler import AreaMapChangeEventHandler
from src.main.Model.areaMap import AreaMap
from src.main.Model.gameState import GameState
from test.util.mockUtil import create_mock


class TestAreaMapChangeEventHandler(TestCase):
    def test_returns_true_when_change_event_points_to_accessible_area(self):
        area_map = create_mock(AreaMap)
        area_map.destination_accessible_from_origin = lambda coordinate, player_position: True

        game_state = create_mock(GameState)
        game_state.get_area_map = lambda: area_map

        self.assertTrue(AreaMapChangeEventHandler.enter_area(game_state, Point(0, 0)))
