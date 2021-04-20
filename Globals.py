import arcade


class Globals(object):
    """
    Глобальные переменные
    """
    # ----------Настройки окна------------
    screen_name = "aboba"

    # ------------Замок-------------------
    castle_width = 150
    castle_height = 150
    castle_health = 100
    castle_img = "image/castle.png"

    # -------------Спавны-----------------
    spawner_1_quantity = 100
    spawner_1_start_time = 1
    spawner_1_end_time = 2

    # --------------Башни-----------------
    tower_1_x = 500
    tower_1_y = 500

    # -----------Задний фон---------------
    grass_img = arcade.load_texture("image/grass.png")
    grass_pos_x = 0
    grass_pos_y = 0
