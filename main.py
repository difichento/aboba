import arcade
from enemies import *
from path import *
from allies import *
from Globals import Globals
from spawn import *
from castle import *
from level import current_level
from hud import *

screen_name = "aboba"
SCREEN_WIDTH = 1240
SCREEN_HEIGHT = 720


class MyGame(arcade.Window):  # класс окна (класс из arcade)

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,
                         screen_name)

    def setup(self):
        current_level.setup()

    def on_draw(self):
        arcade.start_render()
        current_level.on_draw()

    def update(self, delta_time: float):
        current_level.update()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        current_level.on_mouse_press(x, y, button, modifiers)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        current_level.on_mouse_motion(x, y, dx, dy)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
