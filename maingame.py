from sprites import *


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


class GameOver(arcade.View):
    game_over = arcade.Sprite("images/game_over.png")

    def on_draw(self):
        arcade.start_render()
        self.game_over.center_x = WINDOW_WIDTH / 2
        self.game_over.center_y = WINDOW_HEIGHT / 2
        self.game_over.draw()


class LevelOne(arcade.View):
    def __init__(self):
        super().__init__()
        self.timer = 0
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2
        self.view_left = 0
        self.view_top = 2
        self.view_bottom = 0
        self.game_over = False
        self.game_won = False
        self.level = 1

        # Sprite lists
        self.building_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = Player("images/player.png", scale=.2)

    def on_show(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.level_1()

    def level_1(self):
        arcade.set_background_color(arcade.color.BLACK)
        for i in range(60):
            coin = Coin("images/coin.png", .15)
            coin.center_x = random.randrange(WINDOW_WIDTH * 1.75)
            coin.center_y = random.randrange(WINDOW_HEIGHT, WINDOW_HEIGHT * 1.75)
            self.coin_list.append(coin)
        for x in range(50):
            building = arcade.Sprite("images/building.png", scale=.5)
            building.center_x = random.randrange(WINDOW_WIDTH * 2)
            building.center_y = 0
            building.height = random.randint(500, 800)
            self.building_list.append(building)

    def level_2(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)
        for i in range(60):
            coin = Coin("images/coin.png", .15)
            coin.center_x = random.randrange(WINDOW_WIDTH * 1.75)
            coin.center_y = random.randrange(WINDOW_HEIGHT, WINDOW_HEIGHT * 1.75)
            self.coin_list.append(coin)

        for x in range(50):
            building = arcade.Sprite("images/building.png", scale=.5)
            building.center_x = random.randrange(WINDOW_WIDTH * 2)
            building.center_y = 0
            building.height = random.randint(500, 800)
            self.building_list.append(building)

    def setup(self):
        self.level = 1
        self.building_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()
        self.building_list.draw()
        self.coin_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 700, 20, arcade.color.WHITE, 20)

        output = f"Level: {self.level}"
        arcade.draw_text(output, 700, 45, arcade.color.WHITE, 20)

    def on_update(self, delta_time):
        self.player_sprite.update()
        self.building_list.update()
        self.coin_list.update()
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
        building_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.building_list)
        for building in building_hit_list:
            building.remove_from_sprite_lists()
            self.score -= 5
        changed = False
        right_boundary = self.view_left + WINDOW_WIDTH - LEFT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True
        if changed:
            arcade.set_viewport(self.view_left, WINDOW_WIDTH + self.view_left, self.view_bottom, WINDOW_HEIGHT)
        if self.score == 25 and self.level == 1:
            self.level += 1
            self.level_2()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, "Hot Air Adventure")
    introduction = Introduction()
    window.show_view(introduction)
    arcade.run()


if __name__ == "__main__":
    main()
