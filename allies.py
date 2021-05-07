from Globals import Globals


class Tower:
    """
    Класс башен
    Функция attack находит монстра прошедшего дальше всех и наносит ему урон
    Функции отрисовки нет, т.к. они отрисовываются в cells
    """
    def __init__(self, cell, width, height, damage,
                 attack_range, attack_delay, img):
        self.cell = cell
        self.center_x = cell.center_x
        self.center_y = cell.center_y
        self.width = width
        self.height = height
        self.damage = damage
        self.attack_delay = attack_delay
        self.attack_range = attack_range
        self.img = img
        self.frame_after_delay = 0

    def attack(self, enemy_list):
        if Globals.current_frame >= self.frame_after_delay:
            for i, enemy in enumerate(enemy_list):
                if self.center_x - self.attack_range <= enemy.position_x <= self.center_x + self.attack_range and \
                        self.center_y - self.attack_range <= enemy.position_y <= self.center_y + self.attack_range:
                    if not enemy.is_dead():
                        enemy_list[i].take_damage(self.damage)
                        self.frame_after_delay = Globals.current_frame + self.attack_delay * 60
                        break
        return enemy_list


class TowerFactory:
    def make_default_tower(self, cell):
        return Tower(cell, 60, 60, 100, 200, 1, Globals.tower_1_img)


# глобальный список башен установленных на карте
working_tower_list = []

# Список всех видов башен. Нужен для создания кнопок.
tower_list = []
tower_list.append(TowerFactory().make_default_tower)
