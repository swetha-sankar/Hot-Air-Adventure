from constants import *


class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0:
            self.left = 0
        if self.right > WINDOW_WIDTH - 1:
            self.right = WINDOW_WIDTH - 1
        if self.bottom < 0:
            self.bottom = 0
        if self.top > WINDOW_HEIGHT - 1:
            self.top = WINDOW_HEIGHT - 1


class Buildings(arcade.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.texture = BUILDING
        self.center_x = x
        self.center_y = y


class Coin(arcade.Sprite):
    def update(self):
        self.center_y -= 1


