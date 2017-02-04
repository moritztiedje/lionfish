from enum import Enum


class TileMap(Enum):
    WATER = 0
    LAND = 1

def arrayFromFile(filepath):
    dummyMapFile = open(filepath, mode="rb")
    content = dummyMapFile.readline()
    contentLines = content.split(b'\x02')

    area_map = []
    for line in contentLines:
        area_map.append(list(map(int, line)))

    return area_map

arrayFromFile("./dummyMap")
