from abc import abstractmethod
import arcade
from allies import *
from Globals import Globals
from spawn import *
from castle import *
from path import *


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
        arcade.draw_lrwh_rectangle_textured(Globals.grass_pos_x,
                                            Globals.grass_pos_y,
                                            Globals.SCREEN_WIDTH,
                                            Globals.SCREEN_HEIGHT,
                                            Globals.grass_img)
        self.path.draw()
        for en in self.enemies:
            en.draw()
        for tower in self.towers:
            tower.draw()

    def update(self):
        Globals.current_frame += 1
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

    def add_tower(self, tower):
        self.towers.append(tower)


current_level = Level()
current_level.add_tower(TowerFactory().make_tower(225, 100))
