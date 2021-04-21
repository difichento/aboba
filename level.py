from abc import abstractmethod
import arcade
from allies import *
from Globals import Globals
from spawn import *
from castle import *
from path import *
from hud import hud
from cell import cells


class Level:
    def __init__(self):
        self.enemies = []
        self.towers = []
        self.spawners = []
        self.path = current_path
        spawner1 = SpawnMonsters(Globals.enemy_1_name, self.path,
                                 Globals.spawner_1_start_time,
                                 Globals.spawner_1_end_time,
                                 Globals.spawner_1_quantity)
        self.spawners.append(spawner1)

    def setup(self):
        pass

    def on_draw(self):
        self.draw_background()
        self.draw_cells()
        self.path.draw()
        for en in self.enemies:
            en.draw()
        hud.draw()

    def update(self):
        Globals.current_frame += 1
        self.towers = working_tower_list
        for tower in self.towers:
            self.enemies = tower.attack(self.enemies)
        for spawner in self.spawners:
            self.enemies = spawner.spawn()
        for i, en in enumerate(self.enemies):
            en.update()
            if en.is_absolutely_dead():
                del self.enemies[i]
            elif en.is_at_the_end():
                del self.enemies[i]
                self.path.castle.take_damage(10)

    def on_mouse_press(self, x, y, button, modifiers):
        hud.on_mouse_press(x, y, button, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        hud.on_mouse_motion(x, y, dx, dy)

    def draw_cells(self):
        for cell in cells:
            cell.draw_cell()
            cell.draw_borders()

    def draw_background(self):
        arcade.draw_lrwh_rectangle_textured(0, 0, Globals.SCREEN_WIDTH,
                                            Globals.SCREEN_HEIGHT,
                                            Globals.grass_img)


current_level = Level()
