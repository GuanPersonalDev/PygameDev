import math

from Game.Commom.AngleCalc import angle_to_rad


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        if other == math.inf:
           return Vector2(math.inf, math.inf)
        return Vector2(self.x / other, self.y / other)

    @staticmethod
    def right():
        return Vector2(1, 0)

    @staticmethod
    def up():
        return Vector2(0, 1)

    def normalize(self):
        return self / self.length()

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    def rotate(self, angle):
        rad = angle_to_rad(angle)
        new_x = math.cos(rad) * self.x - math.sin(rad) * self.y
        new_y = math.sin(rad) * self.x + math.cos(rad) * self.y
        return Vector2(new_x, new_y)
