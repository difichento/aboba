import arcade

from editor import Editor
from Globals import Globals
from menu import Menu, GameEnd

menu = Menu()
editor = Editor()
game_end = GameEnd()


class MyGame(arcade.Window):  # класс окна (класс из arcade)
    """
    Основной класс игры
    все функции стандартные из arcade
    """
    def __init__(self):
        super().__init__(Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT,
                         Globals.screen_name)
        self.window_list = {"menu": menu, "game": Globals.current_level, "editor": editor, "end": game_end}

    def setup(self):
        """
        Выполняется 1 раз при запуске окна
        """
        pass

    def on_draw(self):
        """
        Функция для отрисовки (запускается каждый кадр)
        """
        self.window_list = {"menu": menu, "game": Globals.current_level, "editor": editor, "end": game_end}
        arcade.start_render()
        self.window_list[Globals.current_window].on_draw()

    def update(self, delta_time: float):
        """
        Функция для обновления данных (запускается каждый кадр)
        """
        self.window_list = {"menu": menu, "game": Globals.current_level, "editor": editor, "end": game_end}
        self.window_list[Globals.current_window].update()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        """
        Вызывается при нажатии кнопки мыши
        """
        self.window_list[Globals.current_window].on_mouse_press(x, y, button, modifiers)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """
        Вызывается при движении мыши
        """
        self.window_list[Globals.current_window].on_mouse_motion(x, y, dx, dy)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
