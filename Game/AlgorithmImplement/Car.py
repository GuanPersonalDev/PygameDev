from Game.Commom.Vector2 import Vector2


class Car:
    def __init__(self):
        self.position = Vector2(0, 0)
        self.velocity = 1
        self.forward_angle = 0
        self.steer_angle = 0
        self.center_to_head = Vector2(1, 0)
        self.center_to_tail = Vector2(-1, 0)

    def update_frame(self):
        move_offset = self._get_move_offset()
        self.position += move_offset

    def _get_move_offset(self):
       return Vector2(self.velocity,0)

