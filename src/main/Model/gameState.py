from src.mapGeneration.tileMap import array_from_file


class GameState:
    def __init__(self):
        self.__area_map = array_from_file('./dummyMap')
        self.__world_map = array_from_file('./dummyWorldMap')

    def get_area_map(self):
        return self.__area_map

    def get_world_map(self):
        return self.__world_map
