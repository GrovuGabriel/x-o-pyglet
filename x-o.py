import pyglet
import window
from pyglet.window import key

if __name__ == '__main__':
    pyglet.resource.path = ['resources']
    window = window.GameWindow()
    pyglet.app.run()


    