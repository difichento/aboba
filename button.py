import arcade


class Button:

    def __init__(self, x, y, width, height, inactive_color, active_color,
                 action, text=""):
        self.x = x
        self.y = y
        self.mouse_x = 0
        self.mouse_y = 0
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.color = inactive_color
        self.was_pressed = False
        self.action = action
        self.text = text

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height,
                                     self.color)
        arcade.draw_text(self.text, self.x, self.y, arcade.color.RED,
                         align="center", anchor_x="center", anchor_y="center", font_size=20)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.x - self.width / 2 < x < self.x + self.width / 2 and self.y - self.height / 2 <= y <= self.y + self.height / 2:
            self.action()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if self.x - self.width / 2 < x < self.x + self.width / 2 and self.y - self.height / 2 <= y <= self.y + self.height / 2:
            self.color = self.active_color
        else:
            self.color = self.inactive_color
