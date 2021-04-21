import arcade
from Globals import Globals


class Tower:  # класс башен
    def __init__(self, cell, t_width, t_height, t_damage,
                 t_attack_range, attack_delay, t_img):
        self.cell = cell
        self.center_x = cell.center_x
        self.center_y = cell.center_y
        self.t_width = t_width
        self.t_height = t_height
        self.t_damage = t_damage
        self.attack_delay = attack_delay
        self.t_attack_range = t_attack_range
        self.t_img = arcade.load_texture(t_img)
        self.frame_after_delay = 0

    def attack(self, enemy_list):
        if Globals.current_frame >= self.frame_after_delay:
            for i, enemy in enumerate(enemy_list):
                if self.center_x - self.t_attack_range <= enemy.position_x <= self.center_x + self.t_attack_range and \
                        self.center_y - self.t_attack_range <= enemy.position_y <= self.center_y + self.t_attack_range:
                    if not enemy.is_dead():
                        enemy_list[i].take_damage(self.t_damage)
                        self.frame_after_delay = Globals.current_frame + self.attack_delay * 60
                        break
        return enemy_list


class TowerFactory:
    def make_default_tower(self, cell):
        return Tower(cell, 60, 60, 100, 200, 1,
                     "image/tower.png")


working_tower_list = []

tower_list = []
tower_list.append(TowerFactory().make_default_tower)
