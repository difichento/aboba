import arcade
from enemies import *
from path import *
from allies import *
from spawn import *
from castle import *
import time

SCREEN_WIDTH = 1240
SCREEN_HEIGHT = 720


class MyGame(arcade.Window):  # класс окна (класс из arcade)

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "aboba")
        self.pathes = PathFactory()
        self.path1 = self.pathes.make_path3()
        self.enemy = []
        self.tower = []
        self.castle = Castle(self.path1, 150, 150, 100, "image/castle.png")

        self.monsters = MonsterFactory(self.path1)
        self.towers = TowerFactory(self.path1)
        self.spawner1 = SpawnMonsters("pudge", self.path1, 1, 30, 100)
        self.current_frame = 0

    def setup(self):
        self.enemy.append(self.monsters.make_pudge())
        self.tower.append(self.towers.make_tower(500, 500))

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
                                            arcade.load_texture(
                                                "image/grass.png"))
        self.path1.draw()
        self.castle.draw()
        arcade.draw_text(str(self.current_frame), 200, 200, arcade.color.WHITE)
        arcade.draw_text(str(self.current_frame // 60), 200, 300,
                         arcade.color.WHITE)

        for en in self.enemy:  # отрисовка монстров
            en.draw()
        self.tower[0].draw()

    def update(self, delta_time: float):
        self.current_frame += 1
        self.enemy = self.spawner1.spawn(self.current_frame)
        for en in self.enemy:
            en.update()
        print(len(self.enemy))


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
