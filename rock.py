from pyglet.sprite import Sprite


import resources


SCALE = 0.5


class Rock(Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.rock_img, *args, **kwargs)
        self.dead = False
        self.scale_x = SCALE
        self.scale_y = SCALE