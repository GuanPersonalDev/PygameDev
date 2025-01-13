import unittest

from Game.AlgorithmImplement.Car import Car
from string import Template


class CarTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here
        print('Hello Test')

    def test_generate_car(self):
        car = Car()
        self.assertEqual(True, car.get_velocity() == 1)

    def test_car_update(self):
        car = Car()
        self.assertEqual(True, car.get_position().x == 0)
        car.set_steer_angle(10)
        self.assertEqual(True, car.get_steer_angle() == 10)
        car.update_frame()
        print(f'car new position: {car.get_position().x} , {car.get_position().y}')


if __name__ == '__main__':
    unittest.main()
