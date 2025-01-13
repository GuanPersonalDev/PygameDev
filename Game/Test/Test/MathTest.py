import math
import unittest

from Game.Commom.AngleCalc import angle_to_rad
from Game.Commom.Vector2 import Vector2


class MathTest(unittest.TestCase):
    def test_angle_convert(self):
        angle = 0
        rad = angle_to_rad(angle)
        self.assertEqual(True, rad == 0)
        angle = 180
        rad = angle_to_rad(angle)
        self.assertEqual(True, rad == math.pi)

    def test_vector2_rotate(self):
        result = Vector2.right().rotate(90)
        self.assertEqual(True, result.x == 0 and result.y == 1)


if __name__ == '__main__':
    unittest.main()
