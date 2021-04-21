import arcade
from Globals import Globals


class Tower:  # класс башен
    def __init__(self, position_x, position_y, t_width, t_height, t_damage,
                 t_attack_range, attack_delay, t_img):
        self.position_x = position_x
        self.position_y = position_y
        self.t_width = t_width
        self.t_height = t_height
        self.t_damage = t_damage
        self.attack_delay = attack_delay
        self.t_attack_range = t_attack_range
        self.t_img = arcade.load_texture(t_img)
        self.frame_after_delay = 0

    def draw(self):  # функция для отрисовки башен
        arcade.draw_lrwh_rectangle_textured(self.position_x, self.position_y,
                                            self.t_width, self.t_height,
                                            self.t_img)

    def attack(self, enemy_list):
        if Globals.current_frame >= self.frame_after_delay:
            for i, enemy in enumerate(enemy_list):
                if self.position_x - self.t_attack_range <= enemy.position_x <= self.position_x + self.t_attack_range and \
                        self.position_y - self.t_attack_range <= enemy.position_y <= self.position_y + self.t_attack_range:
                    if not enemy.is_dead():
                        enemy_list[i].take_damage(self.t_damage)
                        self.frame_after_delay = Globals.current_frame + self.attack_delay * 60
                        break
        return enemy_list


class TowerFactory:  # паттерн фабрика для башен

    def make_tower(self, position_x, position_y):
        return Tower(position_x, position_y, 150, 150, 100, 200, 1,
                     "image/tower.png")
