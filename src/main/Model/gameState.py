from src.main.Model.player import Player
from src.mapGeneration.tileMap import array_from_file


class GameState:
    def __init__(self):
        self.__area_map = array_from_file('./dummyMap')
        self.__world_map = array_from_file('./dummyWorldMap')
        self.__player = Player()

    def get_area_map(self):
        return self.__area_map

    def get_world_map(self):
        return self.__world_map

    def get_player_position_in_area(self):
        return self.__player.get_position_in_area()
