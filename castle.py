import arcade


def singleton(class_):  # паттерн одиночка для замка (замок у нас только один)
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Castle:  # класс замка
    def __init__(self, path, width, height, health, img_alive):
        self.health = health
        self.position_x = path.points[-1][0]
        self.position_y = path.points[-1][1]
        self.dead = False
        self.width = width
        self.height = height
        self.img_alive = arcade.load_texture(img_alive)
        # self.img_dead = arcade.load_texture(img_dead)
        self.death_timer = 60

    def draw(self):  # функция для отрисовки замка
        arcade.draw_lrwh_rectangle_textured(self.position_x - self.width // 2, self.position_y,
                                            self.width, self.height, self.img_alive)
