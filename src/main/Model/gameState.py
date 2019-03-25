from src.main.Model.player import Player
from src.main.constants import Panels
from src.mapGeneration.tileMap import array_from_file


class GameState:
    def __init__(self):
        self.__area_map = array_from_file('./dummyMap')
        self.__world_map = array_from_file('./dummyWorldMap')
        self.__player = Player()
        self.__activePanels = {
            Panels.AreaMap: True,
            Panels.MainMenuBar: True,
            Panels.TextAdventureBox: False,
            Panels.WorldMap: False
        }

    def activateTextAdventureBox(self):
        self.__activePanels[Panels.TextAdventureBox] = True

    def get_area_map(self):
        return self.__area_map

    def get_world_map(self):
        return self.__world_map

    def get_player_position_in_area(self):
        return self.__player.get_position_in_area()

    def is_panel_active(self, panel_key):
        return self.__activePanels[panel_key]
