import arcade


# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.WHITE
GAME_TITLE = "Hot Air Adventure"
GAME_SPEED = 1/60


class Introduction(arcade.Window):
    start = arcade.Sprite("images/intro_screen.png")

    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)

    def setup(self):
        arcade.set_background_color(BACKGROUND_COLOR)

    def start_new_game(self):
        self.on_draw()

    def on_draw(self):
        arcade.start_render()
        self.start.center_x = WINDOW_WIDTH / 2
        self.start.center_y = WINDOW_HEIGHT / 2
        self.start.draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        pass


def main():
    window = Introduction()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()