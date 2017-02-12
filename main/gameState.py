from main.tileMap import array_from_file
from enum import Enum


class GameState:
    def __init__(self):
        self.area_map = array_from_file('./dummyMap')
        self.__world_map = array_from_file('./dummyWorldMap')
        self.__display_mode = self.DisplayMode.AREA_MAP

    def set_world_map_active(self):
        self.__display_mode = self.DisplayMode.WORLD_MAP

    def is_area_map_active(self):
        return self.__display_mode == self.DisplayMode.AREA_MAP

    def is_world_map_active(self):
        return self.__display_mode == self.DisplayMode.WORLD_MAP

    class DisplayMode(Enum):
        AREA_MAP = 1
        WORLD_MAP = 2

    def get_world_map(self):
        return self.__world_map
