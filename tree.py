from pyglet.sprite import Sprite


import resources


class Tree(Sprite):
    def __init__(self, *args, **kwargs):
        super(Tree, self).__init__(img=resources.tree_img, *args, **kwargs)
        self.dead = False