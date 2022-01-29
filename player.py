import numpy as np
import pyglet
from pyglet.sprite import Sprite
from pyglet.window import key


from constants import *
import resources


class Player(Sprite):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.boat_img, *args, **kwargs)
        self.x = WIDTH - self.width - 20
        self.y = TOP_LANE_Y
        self.dx = 0

    def update(self, dt):
        pass

    def on_key_press(self, symbol, _):
        if symbol == key.UP:
            self.y = TOP_LANE_Y
        elif symbol == key.DOWN:
            self.y = BOTTOM_LANE_Y
