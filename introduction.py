import arcade


# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.WHITE
GAME_TITLE = "Hot Air Adventure"
GAME_SPEED = 1/60


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
    play = arcade.make_soft_circle_texture(6, arcade.color.BLUE, 4, 5)

    def on_draw(self):
        arcade.start_render()
        self.play.center_x = WINDOW_WIDTH / 2
        self.play.center_y = WINDOW_HEIGHT / 2
        self.play.draw(5, 500, 5, 6)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        level_one = LevelOne()
        self.window.show_view(level_one)


class LevelOne(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Game - press SPACE to advance", WINDOW_WIDTH/2, WINDOW_HEIGHT/2,
                         arcade.color.BLACK)


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, "Hot Air Adventure")
    introduction = Introduction()
    window.show_view(introduction)
    arcade.run()


if __name__ == "__main__":
    main()