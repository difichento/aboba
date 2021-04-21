import arcade
from Globals import Globals


class Cell:
    def __init__(self, num):
        self.object = "background"
        self.num = num
        self.num_x = num % 25
        self.num_y = num // 25
        self.left = self.num_x * 50
        self.right = self.left + 50
        self.bottom = self.num_y * 50
        self.top = self.bottom + 50
        self.center_x = self.left + 25
        self.center_y = self.bottom + 25

    def draw_borders(self):
        arcade.draw_lrtb_rectangle_outline(self.left, self.right, self.top,
                                           self.bottom, arcade.color.BLACK)

    def draw_cell(self):
        if self.object == "background":
            pass
        if self.object == "path":
            arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top,
                                              self.bottom, arcade.color.BRONZE)
        if self.object == "tower":
            arcade.draw_lrwh_rectangle_textured(
                self.left,
                self.bottom,
                Globals.tower_1_width, Globals.tower_1_height,
                Globals.tower_1_img)
        if self.object == "button":
            arcade.draw_lrwh_rectangle_textured(
                self.left,
                self.bottom,
                50, 50,
                Globals.tower_1_img)

    def set_object(self, obj):
        self.object = obj


cells = [Cell(i) for i in range(25 * 15)]
