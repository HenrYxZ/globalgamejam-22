from pyglet.sprite import Sprite
import random


import resources


SCALE = 0.5


class Rock(Sprite):
    def __init__(self, *args, **kwargs):
        r = random.random()
        if r < 0.2:
            img = resources.r3_img
        elif r < 0.6:
            img = resources.r2_img
        else:
            img = resources.rock_img
        super().__init__(img=img, *args, **kwargs)
        self.dead = False
        r2 = random.random()
        self.scale_x = SCALE + r2 * 0.1
        self.scale_y = SCALE + r2 * 0.1