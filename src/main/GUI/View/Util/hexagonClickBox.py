import math

from src.main.Util.point import Point
from src.main.constants import HEXAGON_FIELD_WIDTH, HEXAGON_FIELD_CENTER_WIDTH, HEXAGON_FIELD_SIDE_WIDTH, \
    HEXAGON_FIELD_HEIGHT


class HexagonClickBox:
    def __init__(self):
        self.__width_of_two_adjacent_hexagons = (HEXAGON_FIELD_WIDTH + HEXAGON_FIELD_CENTER_WIDTH)
        self.__width_of_hexagon = HEXAGON_FIELD_WIDTH
        self.__width_of_hexagon_side = HEXAGON_FIELD_SIDE_WIDTH
        self.__width_of_hexagon_center = HEXAGON_FIELD_CENTER_WIDTH
        self.__height_of_hexagon = HEXAGON_FIELD_HEIGHT
        self.__hexagon_middle_stub = (HEXAGON_FIELD_HEIGHT - 2 * HEXAGON_FIELD_SIDE_WIDTH) / 2

    def set_zoom_level(self, zoom_level):
        self.__width_of_two_adjacent_hexagons = (HEXAGON_FIELD_WIDTH + HEXAGON_FIELD_CENTER_WIDTH) * zoom_level
        self.__width_of_hexagon = HEXAGON_FIELD_WIDTH * zoom_level
        self.__width_of_hexagon_side = HEXAGON_FIELD_SIDE_WIDTH * zoom_level
        self.__width_of_hexagon_center = HEXAGON_FIELD_CENTER_WIDTH * zoom_level
        self.__height_of_hexagon = HEXAGON_FIELD_HEIGHT * zoom_level
        self.__hexagon_middle_stub = (HEXAGON_FIELD_HEIGHT - 2 * HEXAGON_FIELD_SIDE_WIDTH) / 2 * zoom_level
    
    def get_hexagon(self, mouse_position):
        """
        :type mouse_position: (int, int)
        """
        approximate_field = self.__get_square(mouse_position)
        if approximate_field[0] % 2 == 1:
            return Point(approximate_field[0], approximate_field[1])
        else:
            exact_field = self.__correct_approximate(mouse_position, approximate_field)
            return Point(exact_field[0], exact_field[1])

    def __get_square(self, mouse_clicked_position):
        is_even_square = mouse_clicked_position[0] % self.__width_of_two_adjacent_hexagons < self.__width_of_hexagon
        x_position = 2 * math.floor(mouse_clicked_position[0] / self.__width_of_two_adjacent_hexagons)

        if is_even_square:
            y_position = math.floor(mouse_clicked_position[1] / self.__height_of_hexagon) + 1
            return x_position, y_position
        else:
            y_position = math.floor(mouse_clicked_position[1] / self.__height_of_hexagon + 0.5)
            return x_position + 1, y_position
    
    def __correct_approximate(self, mouse_position, approximate_field):
        mouse_position_in_field_x = mouse_position[0] - int((approximate_field[0] * self.__width_of_two_adjacent_hexagons) / 2)
        mouse_position_in_field_y = mouse_position[1] - (approximate_field[1] - 1) * self.__height_of_hexagon

        mouse_position_in_field = mouse_position_in_field_x, mouse_position_in_field_y
        if not self.__is_above_bottom_left_diagonal(mouse_position_in_field):
            return approximate_field[0] - 1, approximate_field[1] - 1
        if not self.__is_below_top_right_diagonal(mouse_position_in_field):
            return approximate_field[0] + 1, approximate_field[1] + 1
        if not self.__is_above_bottom_right_diagonal(mouse_position_in_field):
            return approximate_field[0] + 1, approximate_field[1] - 1
        if not self.__is_below_top_left_diagonal(mouse_position_in_field):
            return approximate_field[0] - 1, approximate_field[1] + 1
        return approximate_field
    
    def __is_above_bottom_left_diagonal(self, mouse_clicked_position):
        return mouse_clicked_position[0] + mouse_clicked_position[1] > self.__width_of_hexagon_side
    
    def __is_below_top_right_diagonal(self, mouse_clicked_position):
        return mouse_clicked_position[0] + mouse_clicked_position[1] < self.__height_of_hexagon + self.__width_of_hexagon + self.__hexagon_middle_stub
    
    def __is_above_bottom_right_diagonal(self, mouse_clicked_position):
        return mouse_clicked_position[0] - mouse_clicked_position[1] < self.__width_of_hexagon_side + self.__width_of_hexagon_center
    
    def __is_below_top_left_diagonal(self, mouse_clicked_position):
        return mouse_clicked_position[0] - mouse_clicked_position[1] > -self.__height_of_hexagon / 2 - self.__hexagon_middle_stub
