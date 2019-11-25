from constants import *


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

class Player(arcade.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.texture = arcade.load_texture("images/player.png", scale=.15)

    def update(self):
        super().update()


class Buildings(arcade.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.texture = BUILDING
        self.center_x = x
        self.center_y = y

    def on_update(self):
        self.center_x = self.center_x + 1


class LevelOne(arcade.View):
    def __init__(self):
        super().__init__()
        self.timer = 0
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2
        self.texture = Player()
        self.building_list = Buildings()
        self.texture.drag = .05
        self.texture.center_x = 0
        self.texture.center_y = 250


    def setup(self):
        self.building_list = arcade.SpriteList()
        self.building_list.append(Buildings(random.randint(300, 250), random.randint(300, 250)))

    def on_show(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        arcade.start_render()
        self.texture.draw()
        self.building_list.draw()

    def on_update(self, delta_time):
        self.texture.update()
        self.building_list.update()

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