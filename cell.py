import arcade
from Globals import Globals


class Cell:
    def __init__(self, num):
        self.object = "background"
        self.num = num
        self.left = num % 31 * 40
        self.right = self.left + 40
        self.bottom = num % 18 * 40
        self.top = self.bottom + 40

    def draw_borders(self):
        arcade.draw_lrtb_rectangle_outline(self.left, self.right, self.top,
                                           self.bottom, arcade.color.BLACK)

    def draw_cell(self):
        if self.object == "background":
            pass


cells = [Cell(i) for i in range(558)]
