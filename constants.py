import arcade
import random
# Define constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
GAME_TITLE = "Hot Air Adventure"
GAME_SPEED = 1/60
MOVEMENT_SPEED = 5
BUILDING_HEIGHT = random.randint(25, 500)
BUILDING = arcade.make_soft_square_texture(random.randint(200, 300), arcade.color.BLACK)
LEFT_VIEWPORT_MARGIN = 250
COIN = arcade.load_texture("images/coin.png", scale = .1)
COIN_COUNT = 50

