import pyglet
from random import randrange
window = pyglet.window.Window(728, 528) #rozměry + 128 kvůli velikosti obrázku

def tik(t):
    if had.x >= 600:
        had.x = 0
        had.y = had.y + 80
        # return had.y
        if had.y >= 400:
            had.y = 0
    else:
        had.x = had.x + t*300 #300 abych nezdržovala a had letěl ;)
        print(had.x)

pyglet.clock.schedule_interval(tik, 1/40)

obrazek = pyglet.image.load('had.png')
obrazek2 = pyglet.image.load('had2.png')
had = pyglet.sprite.Sprite(obrazek)

def zmen(t):
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 0.2)

def zmen_zpatky(t):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen, 0.2)

pyglet.clock.schedule_once(zmen, 1)

def vykresli():
    window.clear()
    had.draw()

window.push_handlers(
    on_draw=vykresli,
)

pyglet.app.run()
