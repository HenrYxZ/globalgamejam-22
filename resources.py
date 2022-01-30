import pyglet


from constants import *


pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

bg_img = pyglet.resource.image("background.png")
boat_right_img = pyglet.resource.image("boat-right.png")
tree_img = pyglet.resource.image("tree.png")
rock_img = pyglet.resource.image("rock.png")
sky_img = pyglet.resource.image("sky.png")
sounds = {
    MUSIC: pyglet.resource.media("song.wav"),
    PADDLE: pyglet.resource.media("paddle.wav", streaming=False),
    HIT: pyglet.resource.media("hit.wav", streaming=False),
    BACKGROUND: pyglet.resource.media("birds.wav")
}

t2_img = pyglet.resource.image("tree2.png")
t3_img = pyglet.resource.image("tree3.png")
r2_img = pyglet.resource.image("rock2.png")
r3_img = pyglet.resource.image("rock3.png")