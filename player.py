import math
import pyglet
from pyglet.sprite import Sprite
from pyglet.window import key


from constants import *
import resources


SCALE = 0.8
FRICTION_CONST = 1
TIDE = 80 / 1000
Y_MOVEMENT = HEIGHT * 0.05
SECS_PER_SWING = 2
EPSILON_X = 10


class Player(Sprite):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.boat_img, *args, **kwargs)
        self.scale_x = SCALE
        self.scale_y = SCALE
        self.x = WIDTH - self.width - 20
        self.y = TOP_LANE_Y
        self.dx = 0
        self.timer = 0

    def update(self, dt):
        self.timer += dt
        if self.dx > EPSILON_X:
            self.dx -= self.dx * FRICTION_CONST * dt
        elif self.dx > 0:
            self.dx = 0
        delta_x = self.dx * dt
        self.x -= delta_x
        sin_component = self.timer * (2 * math.pi) / SECS_PER_SWING
        self.y += (math.sin(sin_component) * Y_MOVEMENT) * dt
        return delta_x

    def on_key_press(self, symbol, _):
        if symbol == key.UP:
            self.y = TOP_LANE_Y
        elif symbol == key.DOWN:
            self.y = BOTTOM_LANE_Y
        elif symbol == key.SPACE:
            self.dx = X_ACC
