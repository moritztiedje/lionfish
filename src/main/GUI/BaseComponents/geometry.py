class Point:
    def __init__(self, x, y):
        """
        :type x: int
        :type y: int
        """
        self.__x = x
        self.__y = y

    def __eq__(self, other_point):
        """
        :type other_point: Point or None
        """
        return other_point is not None and self.__x == other_point.get_x() and self.__y == other_point.get_y()

    def __add__(self, other_point):
        """
        :type other_point: Point
        """
        return Point(self.get_x() + other_point.get_x(), self.get_y() + other_point.get_y())

    def __sub__(self, other_point):
        """
        :type other_point: Point
        """
        return Point(self.get_x() - other_point.get_x(), self.get_y() - other_point.get_y())

    def get_x(self):
        """
        :rtype: int
        """
        return self.__x

    def get_y(self):
        """
        :rtype: int
        """
        return self.__y


class Rectangle:
    def __init__(self, lower_left, upper_right):
        """
        :type lower_left: Point
        :type upper_right: Point
        """
        self.__lower_left = lower_left
        self.__upper_right = upper_right

    def __sub__(self, point):
        """
        :type point: Point
        """
        return Rectangle(self.__lower_left - point, self.__upper_right - point)

    @staticmethod
    def from_upper_left_and_lower_right(upper_left, lower_right):
        """
        :type upper_left: Point
        :type lower_right: Point
        :rtype: Rectangle
        """
        lower_left = Point(upper_left.get_x(), lower_right.get_y())
        upper_right = Point(lower_right.get_x(), upper_left.get_y())
        return Rectangle(lower_left, upper_right)

    def is_inside(self, point):
        """
        :type point: Point
        :rtype: bool
        """
        return self.__lower_left.get_x() <= point.get_x() <= self.__upper_right.get_x() and \
               self.__lower_left.get_y() <= point.get_y() <= self.__upper_right.get_y()

    def get_draw_coordinate(self):
        """
        :rtype: Point
        """
        return Point(self.__lower_left.get_x(), self.__upper_right.get_y())

    def get_height(self):
        """
        :rtype: int
        """
        return self.__upper_right.get_y() - self.__lower_left.get_y()

    def get_width(self):
        """
        :rtype: int
        """
        return self.__upper_right.get_x() - self.__lower_left.get_x()

    def get_left(self):
        """
        :rtype: int
        """
        return self.__lower_left.get_x()

    def get_top(self):
        """
        :rtype: int
        """
        return self.__upper_right.get_y()