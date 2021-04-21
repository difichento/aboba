import arcade
from allies import *
from cell import cells


class TowerButton:
    def __init__(self, tower_func, num):
        self.tower_func = tower_func
        self.tower = self.tower_func(0, 0)
        self.num = num
        self.tower.position_x = 25 + self.num * 50
        self.tower.position_y = 25
        self.tower.t_width = 50
        self.tower.t_height = 50
        self.left = self.tower.position_x - 25
        self.right = self.tower.position_x + 25
        self.top = self.tower.position_y + 25
        self.bottom = self.tower.position_y - 25
        self.was_pressed = False
        self.x = 0
        self.y = 0

    def draw(self):
        self.tower.draw()
        arcade.draw_lrtb_rectangle_outline(self.left, self.right,
                                           self.top, self.bottom,
                                           arcade.color.RED)
        if self.was_pressed:
            arcade.draw_lrtb_rectangle_outline(self.x - 25, self.x + 25,
                                               self.y + 25, self.y - 25,
                                               arcade.color.BLUE)
            arcade.draw_circle_outline(self.x, self.y,
                                       self.tower.t_attack_range,
                                       arcade.color.BLUE)

    def on_mouse_press(self, x, y, button, modifiers):
        if not self.was_pressed:
            if button == arcade.MOUSE_BUTTON_LEFT:
                if self.left < x < self.right and self.bottom <= y <= self.top:
                    if not self.was_pressed:
                        self.was_pressed = True
        else:
            if button == arcade.MOUSE_BUTTON_LEFT:
                working_tower_list.append(
                    TowerFactory().make_default_tower(x, y))
            if button == arcade.MOUSE_BUTTON_RIGHT:
                if self.was_pressed:
                    self.was_pressed = False

    def on_mouse_motion(self, x, y, dx, dy):
        self.x = x
        self.y = y


class Hud:
    def __init__(self):
        self.button_list = []
        for num, tower_func in enumerate(tower_list):
            self.button_list.append(TowerButton(tower_func, num))

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
