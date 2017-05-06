import math

from src.main.constants import HEXAGON_FIELD_WIDTH, HEXAGON_FIELD_CENTER_WIDTH, HEXAGON_FIELD_SIDE_WIDTH, \
    HEXAGON_FIELD_HEIGHT


class HexagonClickBox:
    __width_of_two_adjacent_hexagons = (HEXAGON_FIELD_WIDTH + HEXAGON_FIELD_CENTER_WIDTH)
    __width_of_hexagon = HEXAGON_FIELD_WIDTH
    __width_of_hexagon_side = HEXAGON_FIELD_SIDE_WIDTH
    __width_of_hexagon_center = HEXAGON_FIELD_CENTER_WIDTH
    __height_of_hexagon = HEXAGON_FIELD_HEIGHT
    
    @staticmethod
    def get_hexagon(mouse_position):
        approximate_field = HexagonClickBox.__get_square(mouse_position)
        if approximate_field[0] % 2 == 1:
            return approximate_field
        else:
            return HexagonClickBox.__correct_approximate(mouse_position, approximate_field)

    @staticmethod
    def __get_square(mouse_clicked_position):
        is_even_square = mouse_clicked_position[0] % HexagonClickBox.__width_of_two_adjacent_hexagons < HexagonClickBox.__width_of_hexagon
        x_position = 2 * math.floor(mouse_clicked_position[0] / HexagonClickBox.__width_of_two_adjacent_hexagons)

        if is_even_square:
            y_position = math.floor(mouse_clicked_position[1] / HexagonClickBox.__height_of_hexagon) + 1
            return x_position, y_position
        else:
            y_position = math.floor(mouse_clicked_position[1] / HexagonClickBox.__height_of_hexagon + 0.5)
            return x_position + 1, y_position
    
    @staticmethod
    def __correct_approximate(mouse_position, approximate_field):
        mouse_position_in_field_x = mouse_position[0] - int((approximate_field[0] * HexagonClickBox.__width_of_two_adjacent_hexagons) / 2)
        mouse_position_in_field_y = mouse_position[1] - (approximate_field[1] - 1) * HexagonClickBox.__height_of_hexagon

        mouse_position_in_field = mouse_position_in_field_x, mouse_position_in_field_y
        if not HexagonClickBox.__is_above_bottom_left_diagonal(mouse_position_in_field):
            return approximate_field[0] - 1, approximate_field[1] - 1
        if not HexagonClickBox.__is_below_top_right_diagonal(mouse_position_in_field):
            return approximate_field[0] + 1, approximate_field[1] + 1
        if not HexagonClickBox.__is_above_bottom_right_diagonal(mouse_position_in_field):
            return approximate_field[0] + 1, approximate_field[1] - 1
        if not HexagonClickBox.__is_below_top_left_diagonal(mouse_position_in_field):
            return approximate_field[0] - 1, approximate_field[1] + 1
        return approximate_field
    
    @staticmethod
    def __is_above_bottom_left_diagonal(mouse_clicked_position):
        return mouse_clicked_position[0] + mouse_clicked_position[1] > HexagonClickBox.__width_of_hexagon_side
    
    @staticmethod
    def __is_below_top_right_diagonal(mouse_clicked_position):
        return mouse_clicked_position[0] + mouse_clicked_position[1] < HexagonClickBox.__height_of_hexagon + HexagonClickBox.__width_of_hexagon + 4
    
    @staticmethod
    def __is_above_bottom_right_diagonal(mouse_clicked_position):
        return mouse_clicked_position[0] - mouse_clicked_position[1] < HexagonClickBox.__width_of_hexagon_side + HexagonClickBox.__width_of_hexagon_center
    
    @staticmethod
    def __is_below_top_left_diagonal(mouse_clicked_position):
        return mouse_clicked_position[0] - mouse_clicked_position[1] > -HexagonClickBox.__height_of_hexagon / 2 - 4
