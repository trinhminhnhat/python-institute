# 3.4.1.15 Triangle
import math

# Point Class
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from(self, point):
        # Calculate the distance between two points
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())

# Triangle Class
class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        # The vertices of the triangle are three Point objects
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        # Calculate the perimeter of the triangle
        a = self.__vertices[0].distance_from(self.__vertices[1])
        b = self.__vertices[1].distance_from(self.__vertices[2])
        c = self.__vertices[2].distance_from(self.__vertices[0])
        return a + b + c

# Create a triangle with vertices represented by Point objects
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))

# Print the perimeter of the triangle
print(triangle.perimeter())
