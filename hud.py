import arcade

from allies import working_tower_list, TowerFactory, tower_list
from cell import cells
from Globals import Globals


class TowerButton:
    def __init__(self, tower_func, num, button_cell_num):
        self.tower_func = tower_func
        self.tower = self.tower_func(cells[0])
        self.num = num
        self.tower.center_x = 25 + self.num * 50
        self.tower.center_y = 25
        self.tower.width = 50
        self.tower.height = 50
        self.left = self.tower.center_x - 25
        self.right = self.tower.center_x + 25
        self.top = self.tower.center_y + 25
        self.bottom = self.tower.center_y - 25
        self.was_pressed = False
        self.x = 0
        self.y = 0
        self.cell_num = 0
        self.current_cell = cells[0]
        self.button_cell = cells[button_cell_num]
        cells[button_cell_num].set_object("button")

    def draw(self):
        arcade.draw_lrtb_rectangle_outline(self.left, self.right,
                                           self.top, self.bottom,
                                           arcade.color.RED)
        if self.was_pressed:
            if self.current_cell.object == "background":
                color = arcade.color.BLUE
            else:
                color = arcade.color.RED
            arcade.draw_lrtb_rectangle_outline(self.current_cell.left,
                                               self.current_cell.right,
                                               self.current_cell.top,
                                               self.current_cell.bottom,
                                               color)
            arcade.draw_circle_outline(self.current_cell.center_x,
                                       self.current_cell.center_y,
                                       self.tower.attack_range,
                                       color)

    def on_mouse_press(self, x, y, button, modifiers):
        if not self.was_pressed:
            if button == arcade.MOUSE_BUTTON_LEFT:
                if self.left < x < self.right and self.bottom <= y <= self.top:
                    self.was_pressed = True
        else:
            if button == arcade.MOUSE_BUTTON_LEFT:
                if cells[self.cell_num].object == "background" and \
                        Globals.coins >= 10:
                    working_tower_list.append(
                        TowerFactory().make_default_tower(self.current_cell))
                    cells[self.cell_num].set_object("tower")
                    Globals.coins -= 10
            if button == arcade.MOUSE_BUTTON_RIGHT:
                if self.was_pressed:
                    self.was_pressed = False

    def on_mouse_motion(self, x, y, dx, dy):
        self.x = x
        self.y = y
        try:
            self.cell_num = self.find_cell_num(self.x, self.y)
            self.current_cell = cells[self.cell_num]
        except IndexError:
            self.current_cell = cells[0]

    def find_cell(self, x, y):
        return [x // 50, y // 50]

    def find_cell_num(self, x, y):
        return x // 50 + y // 50 * 25


class Hud:
    def __init__(self):
        self.button_list = []
        for num, tower_func in enumerate(tower_list):
            self.button_list.append(TowerButton(tower_func, num, 0))

    def draw(self):
        self.draw_tower_buttons()

    def draw_tower_buttons(self):  # отрисовка кнопки
        for tower_button in self.button_list:
            tower_button.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        for tower_button in self.button_list:
            tower_button.on_mouse_press(x, y, button, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        for tower_button in self.button_list:
            tower_button.on_mouse_motion(x, y, dx, dy)


hud = Hud()
