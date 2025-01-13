import math

from Game.Commom.Vector2 import Vector2


class Car:
    def __init__(self):
        self.__position = Vector2(0, 0)
        self.__velocity = 1
        self.__forward_angle = 0
        self.__steer_angle = 0
        self.__center_to_head = Vector2(1, 0)
        self.__center_to_tail = Vector2(-1, 0)

    def get_position(self):
        return self.__position
    def get_velocity(self):
        return self.__velocity
    def get_steer_angle(self):
        return self.__steer_angle
    def update_frame(self):
        move_offset = self._get_move_offset()
        self.__position += move_offset

    def _get_move_offset(self):
        head_position = self._get_head_position()
        new_forward = self.__forward_angle + self.__steer_angle
        head_move_offset = Vector2.right().rotate(new_forward) * self.__velocity
        new_head_position = head_position + head_move_offset

        tail_position = self._get_tail_position()
        actual_forward_vector = new_head_position - tail_position

        self.__forward_angle = math.atan2(actual_forward_vector.y, actual_forward_vector.x)
        center_to_head = self.__center_to_head.rotate(self.__forward_angle)
        self.__position = new_head_position - center_to_head

        return Vector2(self.__velocity, 0)

    def _get_head_position(self):
        offset = self.__center_to_head.rotate(self.__forward_angle)
        return self.__position + offset
    def _get_tail_position(self):
        offset = self.__center_to_tail.rotate(self.__forward_angle)
        return self.__position + offset

    def set_steer_angle(self, angle):
        self.__steer_angle = angle
