import arcade


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
    enemy_1_width = 70
    enemy_1_height = 70
    enemy_1_health = 1000
    enemy_1_speed = 1
    enemy_1_coast = 15
    # ---------------Путь-----------------
    path_width = 50
    path_height = 50
    path_1_dots = [[-20, 200], [200, 200], [200, 600], [500, 600], [500, 200],
                   [900, 200]]
    # path_2_dots = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [5, 4],
    #                [5, 3], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]]
    path_2_dots = [[0, 3], [1, 3], [2, 3], [3, 3], [3, 4], [3, 5], [3, 6],
                   [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [4, 12],
                   [5, 12], [6, 12], [7, 12], [7, 11], [7, 10], [7, 9], [7, 8],
                   [7, 7], [7, 6], [7, 5], [7, 4], [7, 3], [8, 3], [9, 3],
                   [10, 3], [11, 3], [11, 4], [11, 5], [11, 6], [11, 7],
                   [11, 8], [11, 9], [11, 10], [11, 11], [11, 12], [12, 12],
                   [13, 12], [14, 12], [15, 12], [15, 11], [15, 10], [15, 9],
                   [15, 8], [15, 7], [15, 6], [15, 5], [15, 4], [15, 3],
                   [16, 3], [17, 3], [18, 3], [18, 4], [18, 5], [18, 6],
                   [19, 6], [20, 6], [21, 6]]

    # -----------Задний фон---------------
    grass_img = arcade.load_texture("image/grass.png")
    cell_bg = arcade.load_texture("image/cell_bg.jpg")
    menu_bg = arcade.load_texture("image/menu.png")
    grass_pos_x = 0
    grass_pos_y = 0

    default_coins = 20
    coins = default_coins
