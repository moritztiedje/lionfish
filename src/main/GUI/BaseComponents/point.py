class Point:
    def __eq__(self, other_point):
        """
        :type other_point: Point or None
        """
        return other_point is not None and self.__x == other_point.get_x() and self.__y == other_point.get_y()

    def __init__(self, x, y):
        """
        :type x: int
        :type y: int
        """
        self.__x = x
        self.__y = y

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
