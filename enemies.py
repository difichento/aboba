import arcade


def sign(num):  # функция возвращения знака
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0


class Monster:  # класс монстра
    def __init__(self, position_x, position_y, width, height, health, speed,
                 img_alive, img_dead, path):
        self.max_health = health
        self.health = health
        self.speed = speed
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = 0
        self.change_y = 0
        self.dead = False
        self.width = width
        self.height = height
        self.img_alive = arcade.load_texture(img_alive)
        self.img_dead = arcade.load_texture(img_dead)
        self.img = self.img_alive
        self.path = path
        self.move_range = 5
        self.death_timer = 60
        self.curp = 0

    def draw(self):  # функция отрисовки монстра

        if not self.dead:
            arcade.draw_lrwh_rectangle_textured(
                self.position_x - self.width // 2,
                self.position_y - self.height // 2,
                self.width, self.height, self.img)
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
        else:
            if self.death_timer != 0:
                arcade.draw_lrwh_rectangle_textured(
                    self.position_x - self.width // 2,
                    self.position_y - self.height // 2,
                    self.width, self.height, self.img_dead)
                self.speed = 0
                self.death_timer -= 1

    def update(
            self):  # функция обновления статов (здоровье и хождение по пути)
        if self.health <= 0:
            self.health = 0
            self.img = self.img_dead
            self.dead = True

        if self.curp != self.path.max_points - 1:

            self.direction_x = self.path.points[self.curp + 1][0] - \
                               self.path.points[self.curp][0]
            self.direction_y = self.path.points[self.curp + 1][1] - \
                               self.path.points[self.curp][1]

            self.position_x += sign(self.direction_x) * self.speed
            self.position_y += sign(self.direction_y) * self.speed

            if self.path.points[self.curp + 1][
                0] - self.move_range <= self.position_x <= \
                    self.path.points[self.curp + 1][0] + self.move_range and \
                    self.path.points[self.curp + 1][
                        1] - self.move_range <= self.position_y <= \
                    self.path.points[self.curp + 1][1] + self.move_range:
                self.curp += 1

    def get_position_x(self):
        return self.position_x

    def get_position_y(self):
        return self.position_y

    def change_position_x(self, change_x):
        self.position_x += change_x

    def change_position_y(self, change_y):
        self.position_y += change_y

    def get_speed(self):
        return self.speed

    def get_health(self):
        return self.health

    def take_damage(self, damage):
        self.health -= damage

    def take_heal(self, heal):
        self.health += heal

    def is_dead(self):
        return self.dead


class MonsterFactory:  # паттерн фабрика для монстров
    def __init__(self, path):
        self.path = path

    def make_pudge(self):
        # скорость можно поменять изменив    вот        это  |  число
        return Monster(self.path.points[0][0], self.path.points[0][1], 50, 50,
                       1000, 1, "image/pudge.png",
                       "image/pudgedead.png", self.path)
