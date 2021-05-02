import arcade
from menu import Menu, GameEnd
from editor import Editor
from Globals import Globals

menu = Menu()
editor = Editor()
game_end = GameEnd()


class MyGame(arcade.Window):  # класс окна (класс из arcade)

    def __init__(self):
        super().__init__(Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT,
                         Globals.screen_name)
        self.window_list = {"menu": menu, "game": Globals.current_level, "editor": editor, "end": game_end}

    def setup(self):
        pass

    def on_draw(self):
        self.window_list = {"menu": menu, "game": Globals.current_level, "editor": editor, "end": game_end}
        arcade.start_render()
        self.window_list[Globals.current_window].on_draw()

    def update(self, delta_time: float):
        self.window_list = {"menu": menu, "game": Globals.current_level, "editor": editor, "end": game_end}
        self.window_list[Globals.current_window].update()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.window_list[Globals.current_window].on_mouse_press(x, y, button, modifiers)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.window_list[Globals.current_window].on_mouse_motion(x, y, dx, dy)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
