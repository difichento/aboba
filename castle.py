import arcade
from Globals import Globals


def singleton(class_):  # паттерн одиночка для замка (замок у нас только один)
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Castle:
    """
    Класс замка
    Замок может быть только один, поэтому используем синглтон
    Создается в path
    """

    def __init__(self, width, height, health, img_alive):
        self.health = health
        self.max_health = health
        self.dead = False

        self.position_x = 0
        self.position_y = 0
        self.width = width
        self.height = height
        self.img_alive = arcade.load_texture(img_alive)
        # self.img_dead = arcade.load_texture(img_dead)

    def draw(self):  # функция для отрисовки замка
        arcade.draw_lrwh_rectangle_textured(self.position_x - self.width // 2,
                                            self.position_y,
                                            self.width, self.height,
                                            self.img_alive)
        if not self.dead:
            arcade.draw_lrtb_rectangle_filled(
                self.position_x - self.width // 2,
                self.position_x + self.width // 2,
                self.position_y + int(self.height * 1.2) - self.height // 2,
                self.position_y + int(self.height * 1.1) - self.height // 2,
                arcade.color.WHITE)
            arcade.draw_lrtb_rectangle_filled(
                self.position_x - self.width // 2,
                self.position_x + int(
                    self.width * self.health / self.max_health) - self.width // 2,
                self.position_y + int(self.height * 1.2) - self.height // 2,
                self.position_y - self.height // 2 + int(self.height * 1.1),
                arcade.color.RED)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.dead = True
            Globals.current_window = "end"

    def is_dead(self):
        return self.dead

    def set_full_hp(self):
        self.health = self.max_health
        self.dead = False
