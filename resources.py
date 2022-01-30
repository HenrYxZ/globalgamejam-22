import pyglet


pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

bg_img = pyglet.resource.image("background.png")
boat_img = pyglet.resource.image("boat.png")
tree_img = pyglet.resource.image("tree.png")
