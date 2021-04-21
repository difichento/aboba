import arcade
from Globals import Globals
from cell import cells
from path import current_path


def sign(num):  # функция возвращения знака
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0


class Monster:  # класс монстра
    def __init__(self, width, height, health, speed, coast,
                 img_alive, img_dead):
        self.max_health = health
        self.health = health
        self.speed = speed
        self.position_x = cells[current_path.cells_to_num(0)].center_x
        self.position_y = cells[current_path.cells_to_num(0)].center_y
        self.change_x = 0
        self.change_y = 0
        self.dead = False
        self.absolutely_dead = False
        self.at_the_end = False
        self.width = width
        self.height = height
        self.img_alive = arcade.load_texture(img_alive)
        self.img_dead = arcade.load_texture(img_dead)
        self.img = self.img_alive
        self.move_range = 5
        self.death_timer = 60
        self.coin_timer = 60
        self.current_point = 0
        self.coast = coast

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
            else:
                
                self.absolutely_dead = True


    def update(self):  # функция обновления статов
        if self.health <= 0:
            self.health = 0
            self.img = self.img_dead
            self.dead = True
        if self.current_point != len(current_path.cell_list) - 1:
            self.direction_x = cells[current_path.cells_to_num(
                self.current_point + 1)].center_x - cells[
                                   current_path.cells_to_num(
                                       self.current_point)].center_x
            self.direction_y = cells[current_path.cells_to_num(
                self.current_point + 1)].center_y - cells[
                                   current_path.cells_to_num(
                                       self.current_point)].center_y

            self.position_x += sign(self.direction_x) * self.speed
            self.position_y += sign(self.direction_y) * self.speed

            if self.is_at_point():
                self.current_point += 1
        else:
            self.at_the_end = True


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


    def is_absolutely_dead(self):
        return self.absolutely_dead


    def is_at_the_end(self):
        return self.at_the_end


    def is_at_point(self):
        return cells[current_path.cells_to_num(
            self.current_point + 1)].center_x - \
               self.move_range <= self.position_x <= \
               cells[current_path.cells_to_num(
                   self.current_point + 1)].center_x + self.move_range and \
               cells[current_path.cells_to_num(
                   self.current_point + 1)].center_y - self.move_range <= self.position_y <= \
               cells[current_path.cells_to_num(
                   self.current_point + 1)].center_y + self.move_range


class MonsterFactory:
    def __init__(self, path):
        self.path = path

    def make_pudge(self):
        return Monster(
            Globals.enemy_1_width, Globals.enemy_1_height,
            Globals.enemy_1_health, Globals.enemy_1_speed, 10,
            Globals.enemy_1_img_alive,
            Globals.enemy_1_img_dead)
