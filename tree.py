from pyglet.sprite import Sprite


import resources


SCALE = 0.7


class Tree(Sprite):
    def __init__(self, *args, **kwargs):
        super(Tree, self).__init__(img=resources.tree_img, *args, **kwargs)
        self.dead = False
        self.scale_x = SCALE
        self.scale_y = SCALE
