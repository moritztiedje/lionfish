from src.main.GUI.BaseComponents.geometry import Point
from src.main.constants import AreaImageEnum


class AreaMap:
    def __init__(self, path_to_file):
        """
        :type path_to_file: str
        """
        area_map = open(path_to_file, mode="rb")
        content = area_map.readline()
        content_lines = content.split(b'\x02')

        self.__area_map = []
        for line in content_lines:
            self.__area_map.append(list(map(self.__convert_string_to_area_element, line)))

    @staticmethod
    def __convert_string_to_area_element(bytecode):
        """
        :type bytecode: int
        """
        if bytecode == 0:
            return AreaImageEnum.WATER
        if bytecode == 1:
            return AreaImageEnum.EMPTY

    def get_map(self):
        """
        :rtype: list of (list of src.main.GUI.View.imageVaults.areaImageVault.AreaImageEnum)
        """
        return self.__area_map

    def get_tile(self, coordinate):
        """
        :type coordinate: src.main.GUI.BaseComponents.geometry.Point
        :rtype: src.main.GUI.View.imageVaults.areaImageVault.AreaImageEnum
        """
        return self.__area_map[coordinate.get_x()][coordinate.get_y()]

    def get_all_coordinates(self):
        """
        :rtype: list of src.main.GUI.BaseComponents.geometry.Point
        """
        coordinates = []
        for x in range(0, len(self.__area_map)):
            for y in range(0, len(self.__area_map[x])):
                coordinates.append(Point(x, y))
        return coordinates

    def fields_are_connected(self, destination, origin):
        """
        :type destination: src.main.GUI.BaseComponents.geometry.Point
        :type origin: src.main.GUI.BaseComponents.geometry.Point
        :rtype: bool
        """
        if self.get_tile(destination) == AreaImageEnum.WATER:
            return False
        return True
