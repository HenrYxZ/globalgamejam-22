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
current_partition = 2
trees = []
obstacles = []
traveled = 0
tree_pos = LevelMaker.create_trees(
    TREE_FOOTPRINT, LVL_LENGTH, TREE_PROB, TREE_OFFSET, PARTITION_SIZE
)
timer = 0


def init_lvl():
    for x, y in (tree_pos[0] + tree_pos[1]):
        trees.append(Tree(x=x * MTS_TO_PIXELS, y=y, batch=objects_batch))


def update(dt):
    global current_partition, timer,  traveled
    timer += dt
    delta_x = player.update(dt)
    if delta_x != 0:
        traveled += delta_x
        camera.move(delta_x, 0)

        # Do this if camera doesn't work
        # move trees

    if traveled > (current_partition - 1) * PARTITION_SIZE * MTS_TO_PIXELS:
        # delete old stuff
        for tree in trees:
            if tree.x < 0:
                tree.dead = True
        for tree in [tree for tree in trees if tree.dead]:
            trees.remove(tree)
            tree.delete()
        # load new stuff
        for x, y in tree_pos[current_partition]:
            trees.append(Tree(x=x * MTS_TO_PIXELS, y=y, batch=objects_batch))
        current_partition += 1

    # Wining condition
    if traveled >= LVL_LENGTH * MTS_TO_PIXELS:
        print(f"WIN! It took you {timer} seconds to travel {LVL_LENGTH}mts")
        pyglet.app.exit()


@window.event
def on_draw():
    window.clear()
    batch.draw()

    with camera:
        objects_batch.draw()
    # objects_batch.draw()


@window.event
def on_key_press(symbol, _):
    player.on_key_press(symbol, _)


if __name__ == '__main__':
    init_lvl()
    pyglet.clock.schedule_interval(update, 1 / FPS)
    pyglet.app.run()
