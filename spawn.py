from enemies import MonsterFactory
from Globals import Globals
from random import randint


class Spawner:
    """
    Класс для создания монстров
    получает текущий список монстров и дополняет его новыми, одновременно сортирую по пройденному пути
    спавнит quantity монстров за time секунд. Монстры распределяются как коэф^i/коэф^time, где i - номер текущей секунды
    """
    def __init__(self, name, path, time, quantity, current_monster_list):
        self.path = path
        self.time = time
        self.quantity = quantity
        self.name = name
        self.monsters_list = current_monster_list
        self.current_monster_list = current_monster_list
        self.monsters_factory = MonsterFactory(path)
        self.available_monsters = {"pudge": self.monsters_factory.make_pudge}
        self.monster_quantity_per_second = []
        self.monster_per_frame_list = []
        self.particles_number = int(sum(
            [1.1 ** i for i in range(self.time)]))
        self.extra_monsters = self.quantity % self.particles_number
        self.quantity -= self.extra_monsters

        for i in range(self.time):
            self.monster_quantity_per_second.append(
                max(1, int(quantity / self.particles_number * (1.1 ** i))))

        for i in range(self.time):
            tmp_list = []
            quantity = self.monster_quantity_per_second[i]
            for _ in range(60):
                default_amount_per_frame = quantity // 60
                tmp_list.append(default_amount_per_frame)
            used_frame_list = []
            temp_quantity = quantity
            while temp_quantity != 0:
                frame = randint(0, 59)
                if frame not in used_frame_list:
                    tmp_list[frame] += 1
                    used_frame_list.append(frame)
                    temp_quantity -= 1
            self.monster_per_frame_list.append(tmp_list)

    def spawn(self):  # функция, которая спавнит монстров
        current_second = Globals.current_frame // 60 % 30
        if current_second <= self.time - 1:
            current_frame = Globals.current_frame % 60
            for _ in range(self.monster_per_frame_list[current_second][current_frame]):
                self.monsters_list.append(self.available_monsters[self.name]())

        self.monsters_list = sorted(self.monsters_list,
                                    key=lambda monster: monster.percent,
                                    reverse=True)
        return self.monsters_list


class InfiniteSpawner:
    """
    Класс для создания бесконечных волн врагов
    создается один экземпляр и при каждом вызове new_wave увеличивает количество монстров
    """
    def __init__(self, path):
        self.wave = 0
        self.path = path

    def new_wave(self, current_monster_list=[]):
        spawner = Spawner(Globals.enemy_1_name, self.path,
                          Globals.spawner_1_time,
                          Globals.spawner_1_quantity + self.wave * 10, current_monster_list)
        self.wave += 1
        return spawner
