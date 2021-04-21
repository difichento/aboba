from enemies import *
from random import randint
from Globals import Globals


class SpawnMonsters:  # класс для спавна монстров
    def __init__(self, name, path, start_time, end_time, quantity):
        self.path = path
        self.start_time = start_time
        self.end_time = end_time
        self.quantity = quantity
        self.name = name
        self.monsters_list = []
        self.monsters_factory = MonsterFactory(path)
        self.current_second = 0
        self.available_monsters = {"pudge": self.monsters_factory.make_pudge}

        time_period = self.end_time - self.start_time + 1
        self.monster_quantity_per_second = []
        self.monster_per_frame_list = []
        self.particles_number = int(sum(
            [1.1 ** i for i in range(time_period)]))
        self.extra_monsters = self.quantity % self.particles_number
        self.quantity -= self.extra_monsters

        for i in range(time_period):
            self.monster_quantity_per_second.append(
                max(1, int(quantity / self.particles_number * (1.1 ** i))))

        for i in range(time_period):
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
        current_second = Globals.current_frame // 60
        if self.start_time <= current_second <= self.end_time:
            second = current_second - self.start_time
            current_frame = Globals.current_frame % 60
            for _ in range(self.monster_per_frame_list[second][current_frame]):
                self.monsters_list.append(self.available_monsters[self.name]())

        # self.monsters_list = sorted(self.monsters_list,
        #                             key=lambda monster: monster.position_y,
        #                             reverse=True)
        return self.monsters_list
