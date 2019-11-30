from constants import *


class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0:
            self.left = 0
        if self.right > WINDOW_WIDTH * 2:
            self.right = WINDOW_WIDTH * 2
        if self.bottom < 0:
            self.bottom = 0
        if self.top > WINDOW_HEIGHT - 1:
            self.top = WINDOW_HEIGHT - 1


class Building(arcade.Sprite):
    def update(self):
        self.center_y += .1


class Coin(arcade.Sprite):
    def update(self):
        self.center_y -= 2
        if self.top < 0:
            self.bottom = WINDOW_HEIGHT
        self.angle += self.change_angle




