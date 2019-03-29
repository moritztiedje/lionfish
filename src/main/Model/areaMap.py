from src.main.GUI.BaseComponents.geometry import Point
from src.main.constants import AreaImageEnum


class AreaMap:
    def __init__(self, path_to_file):
        """
        :type path_to_file: str
        """
        self.__area_map = self.__init_area_map(path_to_file)

    def __init_area_map(self, path_to_file):
        file = open(path_to_file, mode="rb")
        content = file.readline()
        content_lines = content.split(b'\x02')
        area_map = []
        for line in content_lines:
            area_map.append(list(map(self.__convert_string_to_area_element, line)))
        return area_map

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

    def destination_accessible_from_origin(self, destination, origin):
        """
        :type destination: src.main.GUI.BaseComponents.geometry.Point
        :type origin: src.main.GUI.BaseComponents.geometry.Point
        :rtype: bool
        """
        if self.get_tile(destination) == AreaImageEnum.WATER:
            return False

        return self.__coordinates_are_adjacent(destination, origin)

    @staticmethod
    def __coordinates_are_adjacent(destination, origin):
        distance = origin - destination
        if distance.get_x() == 0:
            return distance.get_y() in (-1, 0, 1)
        elif distance.get_x() in (1, -1):
            if origin.get_x() % 2 == 0:
                return distance.get_y() in (0, 1)
            else:
                return distance.get_y() in (0, -1)
        return False
