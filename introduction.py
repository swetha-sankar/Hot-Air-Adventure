import arcade


# Define constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = arcade.color.BLUE
GAME_TITLE = "Hot Air Adventure"
GAME_SPEED = 1/60


class Introduction(arcade.Window):
    start = arcade.Sprite("images/coin.jpg", .25)
    intro = arcade.Sprite("images/intro.jpg", 1)

    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)

    def start_new_game(self):
        self.on_draw()

    def on_draw(self):
        arcade.start_render()
        self.intro.center_x = WINDOW_WIDTH / 2
        self.intro.center_y = WINDOW_HEIGHT / 2
        self.intro.draw()

        self.start.center_x = WINDOW_WIDTH / 2
        self.start.center_y = WINDOW_HEIGHT / 4
        self.start.draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        pass


def main():
    window = Introduction()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()