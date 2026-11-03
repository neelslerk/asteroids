from constants import SHOT_RADIUS
from circleshape import CircleShape


class Shot(CircleShape):

    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)
