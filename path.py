import arcade

from castle import Castle
from cell import cells
from Globals import Globals


class Path:
    def __init__(self, cells_list):
        self.cell_list = cells_list
        self.current_point = 0
        for cell_num in range(len(cells_list)):
            cells[self.cells_to_num(cell_num)].set_object("path")
        self.init_castle()

    def init_castle(self):
        self.castle = Castle(Globals.castle_width,
                             Globals.castle_height, Globals.castle_health,
                             Globals.castle_img)
        self.castle.position_x = cells[self.cells_to_num(-1)].center_x
        self.castle.position_y = cells[self.cells_to_num(-1)].center_y

    def draw(self):  # функция отрисовки пути
        self.castle.draw()

    def cells_to_num(self, num):
        return self.cell_list[num][0] + self.cell_list[num][1] * 25


class ChoosePath:
    def choose_path(self, level):
        if level == 1:
            return self._make_path1()
        elif level == 2:
            return self._make_path2()
        else:
            return self._make_path3()

    def _make_path1(self):
        return Path(Globals.path_1_dots)

    def _make_path2(self):
        return Path(Globals.path_2_dots)


