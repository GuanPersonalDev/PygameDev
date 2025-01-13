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
       return Vector2(self.__velocity, 0)

    def set_steer_angle(self, angle):
        self.__steer_angle = angle
