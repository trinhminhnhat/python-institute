# 3.4.1.14 Points on a plane
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        # Private attributes for the coordinates
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        # Return the x-coordinate
        return self.__x

    def gety(self):
        # Return the y-coordinate
        return self.__y

    def distance_from_xy(self, x, y):
        # Calculate and return the distance between the current point and the given (x, y)
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        # Calculate and return the distance between the current point and another Point object
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())

# Test cases
point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))  # Expected: 1.4142135623730951
print(point2.distance_from_xy(2, 0))      # Expected: 1.4142135623730951
