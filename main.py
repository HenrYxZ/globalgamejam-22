import pyglet


from constants import *
from player import Player
from resources import bg_img

window = pyglet.window.Window(WIDTH, HEIGHT, caption="BackToSchool")
batch = pyglet.graphics.Batch()

bg = pyglet.sprite.Sprite(bg_img, batch=batch)
bg.scale_y = HEIGHT / bg.height

player = Player(batch=batch)


def update(dt):
    player.update(dt)


@window.event
def on_draw():
    window.clear()
    batch.draw()


@window.event
def on_key_press(symbol, _):
    player.on_key_press(symbol, _)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / FPS)
    pyglet.app.run()
