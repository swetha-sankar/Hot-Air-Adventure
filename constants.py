import arcade
import random
# Define constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
GAME_TITLE = "Hot Air Adventure"
GAME_SPEED = 1/60
MOVEMENT_SPEED = 5
BUILDING_HEIGHT = random.randint(25, 500)
LEFT_VIEWPORT_MARGIN = 350
COIN = arcade.load_texture("images/coin.png", scale = .1)
COIN_COUNT = 50

