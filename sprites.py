from constants import *


class Player(arcade.Sprite):
    '''
    This class represents the player sprite, and defines the bounds of movement for the player.
    '''
    def update(self):
        '''
        This function defines the bounds of movement for the player.
        The player can move off the screen to the right, and the viewport will adjust to their movement.
        The player cannot move off the screen in any other direction.
        '''
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
    '''
    This class represents the building sprite, and moves the buildings upwards on every update.
    This creates a time-based challenge for the player.
    '''
    def update(self):
        '''This function moves the buildings upward by .1 on every update.'''
        self.center_y += .1


class Coin(arcade.Sprite):
    '''This class represents the coin sprite, and creates the falling and rotating coin movement.'''
    def update(self):
        '''This function creates the falling and rotating coin movement.'''
        self.center_y -= 2
        if self.top < 0:
            self.bottom = WINDOW_HEIGHT
        self.angle += self.change_angle




