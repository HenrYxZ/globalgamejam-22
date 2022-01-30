import pyglet


from camera import Camera
from constants import *
from level_maker import LevelMaker
from player import Player
from resources import bg_img
from tree import Tree

window = pyglet.window.Window(WIDTH, HEIGHT, caption="BackToSchool")
camera = Camera()
batch = pyglet.graphics.Batch()
objects_batch = pyglet.graphics.Batch()

bg = pyglet.sprite.Sprite(bg_img, batch=batch)
bg.scale_y = HEIGHT / bg.height

player = Player(batch=objects_batch)
current_partition = 1
trees = []
obstacles = []
cursor = 0


def update(dt):
    global current_partition
    delta_x = player.update(dt)
    if delta_x != 0:
        camera.move(-delta_x, 0)
        player.x += delta_x
        for tree in trees:
            tree.x += delta_x

    if -player.x > current_partition * PARTITION_SIZE * MTS_TO_PIXELS:
        # delete old stuff
        for tree in trees:
            if -tree.x < current_partition * PARTITION_SIZE * MTS_TO_PIXELS:
                tree.dead = True
        for tree in [tree for tree in trees if tree.dead]:
            trees.remove(tree)
            tree.delete()
        # load new stuff
        for x, y in tree_pos[current_partition]:
            trees.append(Tree(x=-x * MTS_TO_PIXELS, y=y, batch=objects_batch))
        current_partition += 1
    if -player.x >= LVL_LENGTH * MTS_TO_PIXELS:
        print("WIN!")
        pyglet.app.exit()


@window.event
def on_draw():
    window.clear()
    batch.draw()

    # with camera:
    #     objects_batch.draw()
    objects_batch.draw()


@window.event
def on_key_press(symbol, _):
    player.on_key_press(symbol, _)


if __name__ == '__main__':
    tree_pos = LevelMaker.create_trees(
        TREE_FOOTPRINT, LVL_LENGTH, TREE_PROB, TREE_OFFSET, PARTITION_SIZE
    )
    for x, y in tree_pos[0]:
        trees.append(Tree(x=-x * MTS_TO_PIXELS, y=y, batch=batch))
    pyglet.clock.schedule_interval(update, 1 / FPS)
    pyglet.app.run()
