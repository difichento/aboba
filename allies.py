import arcade


class Tower:  # класс башен
    def __init__(self, position_x, position_y, t_width, t_height, t_damage, t_img):
        self.position_x = position_x
        self.position_y = position_y
        self.t_width = t_width
        self.t_height = t_height
        self.t_damage = t_damage
        self.t_img = arcade.load_texture(t_img)

    def draw(self):  # функция для отрисовки башен
        arcade.draw_lrwh_rectangle_textured(self.position_x, self.position_y,
                                            self.t_width, self.t_height, self.t_img)


class TowerFactory: #паттерн фабрика для башен
    def __init__(self, path):
        self.path = path

    def make_tower(self, position_x, position_y):
        return Tower(position_x, position_y, 150, 150, 100, "image/tower.png")
