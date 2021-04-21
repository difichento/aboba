import arcade
import random

class Globals(object):
    """
    Глобальные переменные
    """
    # ----------Настройки окна------------
    screen_name = "aboba"
    SCREEN_WIDTH = 1240
    SCREEN_HEIGHT = 720
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

    # ------------Монстры-----------------
    enemy_1_name = "pudge"
    enemy_1_img_alive = "image/pudge.png"
    enemy_1_img_dead = "image/pudgedead.png"
    enemy_1_width = 50
    enemy_1_height = 50
    enemy_1_health = 1000
    enemy_1_speed = random.randint(1,3)
    # ---------------Путь-----------------
    path_width = 50
    path_height = 50
    path_1_dots = [[-20, 200], [200, 200], [200, 600], [500, 600], [500, 200],
                   [900, 200]]
    path_2_dots = [[-20, 500], [300, 500], [300, 100], [100, 100], [100, 500],
                   [1024, 500]]
    path_3_dots = [[-20, 100], [150, 100], [150, 600], [400, 600], [400, 100],
                   [600, 100], [600, 600],
                   [850, 600], [850, 100], [1050, 100], [1050, 400]]

    # -----------Задний фон---------------
    grass_img = arcade.load_texture("image/grass.png")
    cell_bg = arcade.load_texture("image/cell_bg.jpg")
    grass_pos_x = 0
    grass_pos_y = 0



