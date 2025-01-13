import unittest

from Game.AlgorithmImplement.Car import Car


class CarTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_generate_car(self):
        car = Car()
        self.assertEqual(True, car.velocity == 1)

    def test_car_update(self):
        car = Car()
        self.assertEqual(True, car.position.x == 0)
        car.update_frame()
        self.assertEqual(True, car.position.x == 1)


if __name__ == '__main__':
    unittest.main()
