from datetime import timedelta
import pyglet

import resources
from camera import Camera
from constants import *
from level_maker import LevelMaker
from player import Player
from rock import Rock
from tree import Tree
import utils

window = pyglet.window.Window(WIDTH, HEIGHT, caption="BackToSchool")
camera = Camera()
batch = pyglet.graphics.Batch()
objects_batch = pyglet.graphics.Batch()

sky = pyglet.sprite.Sprite(resources.sky_img)
sky.scale_y = HEIGHT / sky.height
sky.scale_x = HEIGHT / sky.height


bg = pyglet.sprite.Sprite(resources.bg_img)
bg.scale_y = HEIGHT / bg.height
bg.scale_x = HEIGHT / bg.height

player = Player()
current_partition = 2
trees = []
rocks = []
traveled = 0
tree_pos = LevelMaker.create_trees(
    TREE_FOOTPRINT, LVL_LENGTH, TREE_PROB, TREE_OFFSET, PARTITION_SIZE
)
rocks_pos = LevelMaker.create_obstacles(
    ROCKS_FOOTPRNT, LVL_LENGTH, ROCKS_PROB, ROCKS_OFFSET, PARTITION_SIZE
)
timer = 0
scrolled = 0
sky_scrolled = 0

time_label = pyglet.text.Label(font_size=24, x=WIDTH - 200, y=20)
win_label = pyglet.text.Label(
    font_size=18, x=WIDTH/2, y=HEIGHT/2, anchor_x='center', anchor_y='center'
)
esc_label = pyglet.text.Label(
    "Press [Esc] to quit", font_size=14, x=WIDTH/2, y=HEIGHT/2-100,
    anchor_x='center',
    anchor_y='center'
)
won = False


def init_lvl():
    for x, y in (tree_pos[0] + tree_pos[1]):
        trees.append(Tree(x=x * MTS_TO_PIXELS, y=y, batch=objects_batch))
    for x, y in (rocks_pos[0] + rocks_pos[1]):
        rocks.append(Rock(x=x * MTS_TO_PIXELS, y=y, batch=objects_batch))
    music_player = utils.play(resources.sounds[MUSIC], MUSIC_VOLUME)
    music_player.loop = True
    bg_player = utils.play(resources.sounds[BACKGROUND], 0.4)
    bg_player.loop = True


def update(dt):
    global current_partition, scrolled, sky_scrolled, timer,  traveled, won
    if won:
        return
    timer += dt
    elapsed = utils.humanize_time(timer)
    time_label.text = elapsed
    delta_x = player.update(dt)
    if delta_x != 0:
        # Detect collision with rocks
        for rock in rocks:
            if player.collides_with(rock):
                utils.play(resources.sounds[HIT])
                player.x -= delta_x
                player.dx = -abs(player.dx * 0.6)
                delta_x = player.update(dt)

        # Move everything
        traveled += delta_x
        scrolled += delta_x
        delta_sky = delta_x * SKY_PARALLAX
        sky_scrolled += delta_sky
        sky.x -= delta_sky
        camera.move(delta_x, 0)
        if scrolled > BG_LOOP_POINT:
            # move bg again
            bg.x += BG_LOOP_POINT
            scrolled -= BG_LOOP_POINT
        if sky_scrolled > SKY_LOOP_POINT:
            sky.x += SKY_LOOP_POINT
            sky_scrolled -= SKY_LOOP_POINT

        # World Partition
        if traveled > (current_partition - 1) * PARTITION_SIZE * MTS_TO_PIXELS:
            # delete old stuff
            for tree in trees:
                if tree.x < 0:
                    tree.dead = True
            for tree in [tree for tree in trees if tree.dead]:
                trees.remove(tree)
                tree.delete()

            for rock in rocks:
                if rock.x < 0:
                    rock.dead = True
            for rock in [rock for rock in rocks if rock.dead]:
                rocks.remove(rock)
                rock.delete()
            # load new stuff
            if current_partition < LVL_LENGTH / PARTITION_SIZE:
                for x, y in tree_pos[current_partition]:
                    trees.append(
                        Tree(x=x * MTS_TO_PIXELS, y=y, batch=objects_batch)
                    )
                for x, y in rocks_pos[current_partition]:
                    rocks.append(
                        Rock(x=x * MTS_TO_PIXELS, y=y, batch=objects_batch)
                    )
                current_partition += 1

        # Wining condition
        if traveled >= LVL_LENGTH * MTS_TO_PIXELS:
            won = True


@window.event
def on_draw():
    window.clear()

    sky.draw()
    with camera:
        bg.draw()
        objects_batch.draw()
        player.draw()
    # objects_batch.draw()
    # draw UI

    if won:
        elapsed = utils.humanize_time(timer)
        win_txt = (
            f"WIN! It took you {elapsed} to travel {LVL_LENGTH}mts\n"
        )
        win_label.text = win_txt
        win_label.draw()
        esc_label.draw()
    else:
        time_label.draw()


@window.event
def on_key_press(symbol, _):
    utils.play(resources.sounds[PADDLE])
    player.on_key_press(symbol, _)


if __name__ == '__main__':
    init_lvl()
    pyglet.clock.schedule_interval(update, 1 / FPS)
    pyglet.app.run()
