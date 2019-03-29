from src.main.Model.areaMap import AreaMap
from src.main.Model.panelState import PanelState
from src.main.Model.player import Player
from src.main.Model.textAdventureState import TextAdventureState
from src.main.constants import Panels
from src.mapGeneration.tileMap import array_from_file


class GameState:
    def __init__(self):
        self.__text_adventure_state = TextAdventureState()
        self.__area_map = AreaMap('./dummyMap')
        self.__world_map = array_from_file('./dummyWorldMap')
        self.__player = Player()
        self.__panelStates = {
            Panels.AreaMap: PanelState(True, True),
            Panels.MainMenuBar: PanelState(True, True),
            Panels.TextAdventureBox: PanelState(False, False),
            Panels.WorldMap: PanelState(False, False)
        }

    def get_area_map(self):
        """
        :rtype: src.main.Model.areaMap.AreaMap
        """
        return self.__area_map

    def get_world_map(self):
        return self.__world_map

    def get_panel_state(self, panel_key):
        return self.__panelStates[panel_key]

    def get_text_adventure_state(self):
        """
        :rtype: src.main.Model.textAdventureState.TextAdventureState
        """
        return self.__text_adventure_state

    def get_player(self):
        """
        :rtype: src.main.Model.player.Player
        """
        return self.__player
