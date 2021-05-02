import arcade
from Globals import Globals
from button import Button
from level import Level
from path import Path
from hud import Hud
from cell import cells


class Editor:
    def __init__(self):
        self.points = []
        self.available_points = []
        self.last_cell = None
        self.x = 0
        self.y = 0
        self.start_button = Button(1150, 38, 200, 75, arcade.color.BLACK, arcade.color.BLUE, self.start_game, "START")
        self.clear_cells()

    def on_draw(self):
        self.draw_background()
        for cell in cells:
            cell.draw_cell()
            cell.draw_borders(arcade.color.BLACK)
        if len(self.points) == 0:
            try:
                cells[self.find_cell_num(self.x, self.y)].draw_borders(arcade.color.GREEN)
            except:
                pass
        else:
            for point in self.available_points:
                cells[point].draw_borders(arcade.color.BLUE)

        self.start_button.draw()

    def update(self):
        self.available_points = []
        if len(self.points) != 0:
            for i in [1, -1, 25, -25]:
                try:
                    if cells[self.points[-1] + i].object == "background":
                        self.available_points.append(self.points[-1] + i)
                except:
                    pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.start_button.on_mouse_press(x, y, button, modifiers)
        if button == arcade.MOUSE_BUTTON_LEFT:
            if self.find_cell_num(x, y) in self.available_points or len(self.points) == 0:
                if cells[self.find_cell_num(x, y)].object == "background":
                    cells[self.find_cell_num(x, y)].object = "path"
                    self.points.append(self.find_cell_num(x, y))
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            if cells[self.find_cell_num(x, y)].object == "path":
                if len(self.points) != 0:
                    if self.find_cell_num(x, y) == self.points[0]:
                        cells[self.find_cell_num(x, y)].object = "background"
                        self.points = self.points[1:]
                    if self.find_cell_num(x, y) == self.points[-1]:
                        cells[self.find_cell_num(x, y)].object = "background"
                        self.points = self.points[:-1]

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.start_button.on_mouse_motion(x, y, dx, dy)
        self.x = x
        self.y = y

    @staticmethod
    def draw_background():
        arcade.draw_lrwh_rectangle_textured(0, 0, Globals.SCREEN_WIDTH,
                                            Globals.SCREEN_HEIGHT,
                                            Globals.grass_img)

    @staticmethod
    def clear_cells():
        for i in range(len(cells)):
            cells[i].object = "background"

    @staticmethod
    def find_cell(x, y):
        return [x // 50, y // 50]

    @staticmethod
    def find_cell_num(x, y):
        return x // 50 + y // 50 * 25

    def start_game(self):
        if len(self.points) >= 2:
            current_path = Path(list(map(self.points_num2points, self.points)))
            Globals.current_level = Level(current_path)
            Globals.current_window = "game"

    @staticmethod
    def points_num2points(num):
        return [num % 25, num // 25]
