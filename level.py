import arcade

from allies import WorkingTowers
from Globals import Globals
from hud import Hud
from spawn import InfiniteSpawner
from path import ChoosePath


class Level:
    """
    Класс для окна уровня игры (фасад)
    все функции назван как стандартные из arcade для удобства
    Отрисовывает задний фон и все клетки

    Монстры:
    В классе хранится список монстров, который добавляется в update через класс spawner и обновляется там же
    Каждые 30 секунд обновляется spawner и в него предается текущий список монстров, т.к. spawner возвращает
    новый список мностров, и без этого каждую волну карта бы очищалась
    """

    def __init__(self, current_path):
        self.enemies = []
        self.towers = []
        self.path = current_path
        self.inf_spawner = InfiniteSpawner(current_path)
        self.spawner = self.inf_spawner.new_wave()
        self.hud = Hud(self)
        self.flag_for_spawner = True

    def setup(self):
        pass

    def on_draw(self):
        if not self.path.castle.is_dead():
            self.draw_background()
            self.draw_cells()
            self.path.draw()
            for en in self.enemies:
                en.draw()
            self.hud.draw()

    def update(self):
        if not self.path.castle.is_dead():
            Globals.current_frame += 1
            self.towers = WorkingTowers.working_tower_list
            for tower in self.towers:
                self.enemies = tower.attack(self.enemies)

            if Globals.current_frame // 60 % 30 == 0 and self.flag_for_spawner is False:
                self.spawner = self.inf_spawner.new_wave(self.enemies)
                self.flag_for_spawner = True
            elif Globals.current_frame // 60 % 30 == 1:
                self.flag_for_spawner = False
            self.enemies = self.spawner.spawn()

            for i, en in enumerate(self.enemies):
                en.update()
                if en.is_absolutely_dead():
                    del self.enemies[i]
                elif en.is_at_the_end():
                    del self.enemies[i]
                    self.path.castle.take_damage(10)

    def on_mouse_press(self, x, y, button, modifiers):
        self.hud.on_mouse_press(x, y, button, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        self.hud.on_mouse_motion(x, y, dx, dy)

    def draw_cells(self):
        for cell in Globals.cells:
            cell.draw_cell()
            cell.draw_borders()

    def draw_background(self):
        arcade.draw_lrwh_rectangle_textured(0, 0, Globals.SCREEN_WIDTH,
                                            Globals.SCREEN_HEIGHT,
                                            Globals.grass_img)


def make_default_level():
    Globals.current_level = Level(ChoosePath().choose_path(2))
