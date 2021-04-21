import arcade
from Globals import Globals
from castle import Castle


class Path:  # класс пути
    def __init__(self, points):
        self.points = points
        self.current_point = 0
        self.width = Globals.path_width
        self.height = Globals.path_height
        self.max_points = len(self.points)
        self.castle = Castle(self, Globals.castle_width,
                             Globals.castle_height, Globals.castle_health,
                             Globals.castle_img)

    def draw(self):  # функция отрисовки пути
        for i, point in enumerate(self.points):
            arcade.draw_lrtb_rectangle_filled(point[0] - self.width // 2,
                                              point[0] + self.width // 2,
                                              point[1] + self.height // 2,
                                              point[1] - self.height // 2,
                                              arcade.color.BRONZE)
        for i, point in enumerate(self.points):
            if point != self.points[-1]:
                if point[0] == self.points[i + 1][0]:
                    arcade.draw_lrtb_rectangle_filled(
                        point[0] - self.width // 2, point[0] + self.width // 2,
                        max(point[1], self.points[i + 1][1]),
                        min(point[1], self.points[i + 1][1]),
                        arcade.color.BRONZE)
                elif point[1] == self.points[i + 1][1]:
                    arcade.draw_lrtb_rectangle_filled(
                        min(point[0], self.points[i + 1][0]),
                        max(point[0], self.points[i + 1][0]),
                        point[1] + self.height // 2,
                        point[1] - self.height // 2,
                        arcade.color.BRONZE)
        self.castle.draw()


class ChoosePath:  # паттерн фабрика для пути (пока имеется 3 разных пути)
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

    def _make_path3(self):
        return Path(Globals.path_3_dots)


current_path = ChoosePath().choose_path(2)
