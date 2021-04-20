import arcade


class Path:  # класс пути
    def __init__(self, points):
        self.points = points
        self.current_point = 0
        self.width = 50
        self.height = 50
        self.max_points = len(self.points)

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


class PathFactory:  # паттерн фабрика для пути (пока имеется 3 разных пути)
    def make_path1(self):
        return Path(
            [[-20, 200], [200, 200], [200, 600], [500, 600], [500, 200],
             [900, 200]])

    def make_path2(self):
        return Path(
            [[-20, 500], [300, 500], [300, 100], [100, 100], [100, 500],
             [1024, 500]])

    def make_path3(self):
        return Path(
            [[-20, 100], [150, 100], [150, 600], [400, 600], [400, 100],
             [600, 100], [600, 600],
             [850, 600], [850, 100], [1050, 100], [1050, 400]])
