import arcade
import random


# Define constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.WHITE
GAME_TITLE = "Hot Air Adventure"
GAME_SPEED = 1/60
MOVEMENT_SPEED = 6
PLAYER = arcade.load_texture("images/player.png")
BUILDING_HEIGHT = random.randint(25, 500)
BUILDING = arcade.make_soft_square_texture(BUILDING_HEIGHT, arcade.color.GRAY, 255, 128)

class Introduction(arcade.View):
    start = arcade.Sprite("images/intro_screen.png")

    def on_draw(self):
        arcade.start_render()
        self.start.center_x = WINDOW_WIDTH / 2
        self.start.center_y = WINDOW_HEIGHT / 2
        self.start.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        playing = HowToPlay()
        self.window.show_view(playing)


class HowToPlay(arcade.View):
    play = arcade.Sprite("images/instructions.png")

    def on_draw(self):
        arcade.start_render()
        self.play.center_x = WINDOW_WIDTH / 2
        self.play.center_y = WINDOW_HEIGHT / 2
        self.play.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        level_one = LevelOne()
        self.window.show_view(level_one)


class Balloon(arcade.Sprite):
    def __init__(self):
        self.texture = "images/player.png"



class Buildings(arcade.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.texture = BUILDING
        self.center_x = x
        self.center_y = y

    def update(self):
        super().update()
        if self.right > WINDOW_WIDTH:
            self.change_x *= -1
        if self.left < 0:
            self.change_x *= -1
        if self.top > WINDOW_HEIGHT:
            self.change_y *= -1
        if self.bottom < 0:
            self.change_y *= -1

class LevelOne(arcade.View):
    def __init__(self):
        super().__init__()
        self.timer = 0
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2
        self.texture = arcade.Sprite("images/player.png")

    def on_show(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        arcade.start_render()
        self.texture.draw()
        arcade.draw_text("Welcome to Level 1", WINDOW_WIDTH/2, WINDOW_HEIGHT/2,
                         arcade.color.BLACK)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.texture.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.texture.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.texture.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.texture.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.texture.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.texture.change_x = 0


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, "Hot Air Adventure")
    introduction = Introduction()
    window.show_view(introduction)
    arcade.run()


if __name__ == "__main__":
    main()