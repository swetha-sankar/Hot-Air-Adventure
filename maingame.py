from sprites import *


class Introduction(arcade.View):
    '''
    This is a class for the first view that the user sees. It transitions to the How to Play view when the user clicks
    on the screen.
    '''
    start = arcade.Sprite("images/intro_screen.png")

    def on_draw(self):
        ''' Defines position of the introduction image and sets up screen'''
        arcade.start_render()
        self.start.center_x = WINDOW_WIDTH / 2
        self.start.center_y = WINDOW_HEIGHT / 2
        self.start.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        ''' Function that transitions the view to the How to Play screen when the user clicks on the screen '''
        playing = HowToPlay()
        self.window.show_view(playing)


class HowToPlay(arcade.View):
    '''
    This is a class for the second view that the user sees. It transitions to the main game view (MainGame())
    when the user clicks anywhere on the screen.
    '''
    play = arcade.Sprite("images/instructions.png")

    def on_draw(self):
        ''' Function that positions instructions image and sets up screen'''
        arcade.start_render()
        self.play.center_x = WINDOW_WIDTH / 2
        self.play.center_y = WINDOW_HEIGHT / 2
        self.play.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        '''Function that transitions game view to the first level when the user clicks on the screen'''
        level_one = MainGame()
        self.window.show_view(level_one)


class GameOver(arcade.View):
    '''
    This is a class that represents the Game Over view. It appears when the user has less than 25 points after
    1 minute has elapsed.
    '''
    game_over = arcade.Sprite("images/game_over.png")

    def on_draw(self):
        '''Function that positions game over image on screen and sets up view.'''
        arcade.start_render()
        self.game_over.center_x = WINDOW_WIDTH / 2
        self.game_over.center_y = WINDOW_HEIGHT / 2
        self.game_over.draw()


class GameWon(arcade.View):
    '''
    This is a class that represents the screen that appears if a user wins the game. This screen appears
    if the user is able to obtain 25 points in under a minute for all three levels.
    '''
    game_won = arcade.Sprite("images/game_won.png")

    def on_draw(self):
        '''This function sets up the game won image and positions it on the screen.'''
        arcade.start_render()
        self.game_won.center_x = WINDOW_WIDTH / 2
        self.game_won.center_y = WINDOW_HEIGHT / 2
        self.game_won.draw()


class MainGame(arcade.View):
    '''
    This class represents the main game view. It consists of three levels, and transitions to either the GameWon() or
    GameOver() class depending on the user's score and performance.
    '''
    def __init__(self):
        '''
        This function initializes variables used throughout the course of main game
        '''
        super().__init__()
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2
        self.view_left = 0
        self.view_top = 2
        self.view_bottom = 0
        self.game_over = False
        self.game_won = False
        self.level = 1
        self.total_time = 0.0
        # Sounds
        self.level_1_music = arcade.load_sound('sounds/theme.wav')
        self.level_3_music = arcade.load_sound('sounds/theme2.wav')
        self.level_up = arcade.load_sound('sounds/levelup.wav')
        # Sprite lists
        self.building_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = Player("images/player.png", scale=.15)

    def on_show(self):
        '''This function calls the level_1 function when the game begins.'''
        self.level_1()

    def level_1(self):
        '''This function sets up the first level. It puts the coins, buildings, and background color onto the screen.'''
        self.total_time = 0.0
        arcade.set_background_color(arcade.color.SKY_BLUE)
        arcade.play_sound(self.level_1_music)
        for i in range(60):
            coin = Coin("images/coin.png", .15)
            coin.center_x = random.randrange(WINDOW_WIDTH * 1.75)
            coin.center_y = random.randrange(WINDOW_HEIGHT, WINDOW_HEIGHT * 1.75)
            coin.angle = random.randrange(360)
            coin.change_angle = random.randrange(-5, 6)
            self.coin_list.append(coin)
        for x in range(20):
            building = Building("images/building.png", scale=1)
            building.center_x = random.randrange(WINDOW_WIDTH * 1.75)
            building.center_y = 0
            building.height = random.randint(400, 700)
            self.building_list.append(building)

    def level_2(self):
        '''
        This function sets up the second level of the game.
        It changes the background color, adds coins, and resets the player sprite's position.
        '''
        self.total_time = 0.0
        arcade.set_background_color(arcade.color.SUNSET_ORANGE)
        self.player_sprite.center_x = 0
        self.player_sprite.center_y = 0
        self.score = 0
        for i in range(30):
            coin = Coin("images/coin.png", .15)
            coin.center_x = random.randrange(WINDOW_WIDTH * 1.75)
            coin.center_y = random.randrange(WINDOW_HEIGHT, WINDOW_HEIGHT * 1.75)
            coin.angle = random.randrange(360)
            coin.change_angle = random.randrange(-5, 6)
            self.coin_list.append(coin)

    def level_3(self):
        ''' This function sets up the screen for the third level. It resets the player's position, score, and time.
        It also adds coins and buildings to the screen, and changes the background color.
        '''
        self.total_time = 0.0
        arcade.set_background_color(arcade.color.BLACK)
        self.player_sprite.center_x = 0
        self.player_sprite.center_y = 0
        self.score = 0
        arcade.play_sound(self.level_3_music)
        for i in range(20):
            coin = Coin("images/coin.png", .15)
            coin.center_x = random.randrange(WINDOW_WIDTH * 1.75)
            coin.center_y = random.randrange(WINDOW_HEIGHT, WINDOW_HEIGHT * 1.75)
            coin.angle = random.randrange(360)
            coin.change_angle = random.randrange(-5, 6)
            self.coin_list.append(coin)
        for x in range(10):
            building = Building("images/building.png", scale=1)
            building.center_x = random.randrange(WINDOW_WIDTH * 1.75)
            building.center_y = 0
            building.height = random.randint(400, 600)
            self.building_list.append(building)

    def setup(self):
        '''This function sets up the game.'''
        self.level = 1
        self.building_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        ''' This function places the score, coins, buildings, timer, player, and level onto the screen.'''
        arcade.start_render()
        self.player_sprite.draw()
        self.building_list.draw()
        self.coin_list.draw()
        arcade.draw_rectangle_outline(self.player_sprite.center_x + 50, 45, 100, 50, arcade.color.WHITE)
        output = f"Score: {self.score}"
        arcade.draw_text(output, self.player_sprite.center_x, 20, arcade.color.WHITE, 20)
        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        output = f"Time: {minutes:02d}: {seconds:02d}"
        arcade.draw_text(output, self.player_sprite.center_x, 300, arcade.color.WHITE, 30)
        output = f"Level: {self.level}"
        arcade.draw_text(output, self.player_sprite.center_x, 45, arcade.color.WHITE, 20)

    def on_update(self, delta_time):
        '''
        This function is called for every frame of the game (1/GAME_SPEED times per second).
        It updates the score and level according to user performance.
        It also updates the viewport depending on how far right the user has positioned the sprite.
        It calls the GameOver() and GameWon() classes depending on the state of the user's score.
        '''
        self.player_sprite.update()
        self.building_list.update()
        self.coin_list.update()
        self.total_time += delta_time
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
        if self.score < 25 and self.total_time > 60:
            self.game_over = True
        if self.game_over:
            arcade.set_viewport(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
            game_over = GameOver()
            self.window.show_view(game_over)
        if self.score == 25 and self.level == 1:
            arcade.set_viewport(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
            self.level += 1
            arcade.play_sound(self.level_up)
            self.level_2()
        if self.score == 25 and self.level == 2:
            arcade.set_viewport(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
            self.level += 1
            arcade.play_sound(self.level_up)
            self.level_3()
        if self.score == 25 and self.level == 3:
            self.game_won = True
        if self.game_won:
            arcade.set_viewport(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
            game_won = GameWon()
            self.window.show_view(game_won)

    def on_key_press(self, key, modifiers):
        '''
        This function is called whenever the user presses an arrow key. It moves the balloon sprite by the
        movement speed (6).
        '''
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        '''
        This function is called whenever the user releases one of the arrow keys.
        It ceases movement of the balloon sprite.
        '''
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    ''' This main function sets up the window, and calls the Introduction() class. '''
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, "Hot Air Adventure")
    introduction = Introduction()
    window.show_view(introduction)
    arcade.run()


if __name__ == "__main__":
    main()
