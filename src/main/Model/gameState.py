from src.main.Model.player import Player
from src.main.Model.textAdventureState import TextAdventureState
from src.main.constants import Panels
from src.mapGeneration.tileMap import array_from_file


class GameState:
    def __init__(self):
        self.__text_adventure_state = TextAdventureState()
        self.__area_map = array_from_file('./dummyMap')
        self.__world_map = array_from_file('./dummyWorldMap')
        self.__player = Player()
        self.__activePanels = {
            Panels.AreaMap: True,
            Panels.MainMenuBar: True,
            Panels.TextAdventureBox: False,
            Panels.WorldMap: False
        }

    def get_area_map(self):
        return self.__area_map

    def get_world_map(self):
        return self.__world_map

    def get_player_position_in_area(self):
        return self.__player.get_position_in_area()

    def is_panel_active(self, panel_key):
        return self.__activePanels[panel_key]

    def deactivate_panel(self, panel_key):
        """
        :type panel_key: src.main.constants.Panels
        """
        self.__activePanels[panel_key] = False

    def activate_panel(self, panel_key):
        """
        :type panel_key: src.main.constants.Panels
        """
        self.__activePanels[panel_key] = True

    def get_text_adventure_state(self):
        """
        :rtype: src.main.Model.textAdventureState.TextAdventureState
        """
        return self.__text_adventure_state
