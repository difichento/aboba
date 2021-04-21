import arcade
import random


class Globals(object):
    """
    Глобальные переменные
    """
    # ----------Настройки окна------------
    screen_name = "aboba"
    SCREEN_WIDTH = 1250
    SCREEN_HEIGHT = 750
    current_frame = 0

    # ------------Замок-------------------
    castle_width = 150
    castle_height = 150
    castle_health = 100
    castle_img = "image/castle.png"

    # -------------Спавны-----------------
    spawner_1_quantity = 10
    spawner_1_start_time = 1
    spawner_1_end_time = 20

    # --------------Башни-----------------
    tower_1_x = 500
    tower_1_y = 500
    tower_1_width = 50
    tower_1_height = 50
    tower_1_img = arcade.load_texture("image/tower.png")

    # ------------Монстры-----------------
    enemy_1_name = "pudge"
    enemy_1_img_alive = "image/pudge.png"
    enemy_1_img_dead = "image/pudgedead.png"
    enemy_1_width = 50
    enemy_1_height = 50
    enemy_1_health = 1000
    enemy_1_speed = 1
    # ---------------Путь-----------------
    path_width = 50
    path_height = 50
    path_1_dots = [[-20, 200], [200, 200], [200, 600], [500, 600], [500, 200],
                   [900, 200]]
    path_2_dots = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [5, 4],
                   [5, 3], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]]
    path_3_dots = [[-20, 100], [150, 100], [150, 600], [400, 600], [400, 100],
                   [600, 100], [600, 600],
                   [850, 600], [850, 100], [1050, 100], [1050, 400]]

    # -----------Задний фон---------------
    grass_img = arcade.load_texture("image/grass.png")
    cell_bg = arcade.load_texture("image/cell_bg.jpg")
    grass_pos_x = 0
    grass_pos_y = 0

    default_coins = 20
    coins = default_coins
