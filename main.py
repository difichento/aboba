import arcade
from enemies import *
from path import *
from allies import *
from Globals import Globals
from spawn import *
from castle import *
from level import current_level

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


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
