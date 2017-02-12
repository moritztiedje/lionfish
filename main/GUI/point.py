class Point:
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
