import pyglet


pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

bg_img = pyglet.resource.image("background.png")
boat_right_img = pyglet.resource.image("boat-right.png")
tree_img = pyglet.resource.image("tree.png")
rock_img = pyglet.resource.image("rock.png")
sky_img = pyglet.resource.image("sky.png")
