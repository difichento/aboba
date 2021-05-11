import arcade
from Globals import Globals

from button import Button
from level import Level
from path import ChoosePath


class Menu:
    """
    Класс для окна меню, позволяет перейти в редактор или начать игру со стандартным уровнем
    """

    def __init__(self):
        self.start_button = Button(625, 500, 200, 75, arcade.color.BLACK, arcade.color.BLUE, self.start_game, "START")
        self.editor_button = Button(625, 375, 200, 75, arcade.color.BLACK, arcade.color.BLUE, self.start_editor,
                                    "EDITOR")

    def on_draw(self):
        self.draw_background()
        arcade.draw_lrwh_rectangle_textured(110, -30, 900, 900, arcade.load_texture(Globals.enemy_1_img_alive))
        self.start_button.draw()
        self.editor_button.draw()

    def start(self):
        pass

    @staticmethod
    def draw_background():
        arcade.draw_lrwh_rectangle_textured(0, 0, Globals.SCREEN_WIDTH,
                                            Globals.SCREEN_HEIGHT,
                                            Globals.menu_bg)

    def start_game(self):
        Globals.current_level = Level(ChoosePath().choose_path(2))
        Globals.current_window = "game"

    @staticmethod
    def start_editor():
        Globals.current_window = "editor"

    def update(self):
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.start_button.on_mouse_press(x, y, button, modifiers)
        self.editor_button.on_mouse_press(x, y, button, modifiers)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.start_button.on_mouse_motion(x, y, dx, dy)
        self.editor_button.on_mouse_motion(x, y, dx, dy)


class GameEnd:
    def on_draw(self):
        self.draw_background()
        arcade.draw_lrwh_rectangle_textured(100, 0, 1000, 1000, arcade.load_texture(Globals.enemy_1_img_dead))
        arcade.draw_text(
            "XXAXAXAXAXAXAXAXAXAXAXAXAXAXAXAXAXA\n",
            625, 375, arcade.color.BLACK, font_size=30, align="center", anchor_x="center", anchor_y="center")

    def update(self):
        pass

    def draw_background(self):
        arcade.draw_lrwh_rectangle_textured(0, 0, Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT,
                                            arcade.load_texture("image/black_bg.jpg"), alpha=100)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        pass
