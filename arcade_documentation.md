TITLE: Importing Arcade Library - Python
DESCRIPTION: Imports the `arcade` library, which provides the necessary classes and functions for game development, including controller handling. This is a fundamental step before using any Arcade features.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/controller.rst#_snippet_6

LANGUAGE: Python
CODE:
```
import arcade
```

----------------------------------------

TITLE: Initializing Simple Arcade Window - Python
DESCRIPTION: This snippet provides a basic template for setting up a simple window using the Arcade library. It includes the necessary imports, window class definition, and the main run function to start the application.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/framebuffer/index.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Simple Window"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()

    def update(self, delta_time):
        pass

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Basic Arcade Window Template - Python
DESCRIPTION: This snippet provides a complete, runnable template for an Arcade application. It defines a custom `MyGame` class inheriting from `arcade.Window`, sets up basic window properties, initializes sprites, implements `setup`, `on_draw`, and `update` methods for the game loop, and includes a standard `main` function to run the application.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/starting_template.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer for the window
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # Variable that will hold the player sprite
        self.player_sprite = None

        # Sprite list with all the sprites
        self.all_sprites = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites = arcade.SpriteList()

        # Create the player sprite
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)

        # Position the player sprite
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = SCREEN_HEIGHT // 2

        # Add the player sprite to the list
        self.all_sprites.append(self.player_sprite)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        self.clear()

        # Draw all the sprites.
        self.all_sprites.draw()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        # Update all the sprites
        self.all_sprites.update()


def main():
    """ Main function """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Creating a Simple Arcade Game - Python
DESCRIPTION: This Python code snippet defines a minimal Arcade application. It opens a window, clears it, draws a blue circle, renders the drawing commands, and then starts the event loop, serving as a basic example to test the bundling process.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/bundling_with_pyinstaller/index.rst#_snippet_1

LANGUAGE: python
CODE:
```
import arcade

window = arcade.open_window(400, 400, "My Game")

window.clear()
arcade.draw_circle_filled(200, 200, 100, arcade.color.BLUE)
arcade.finish_render()

arcade.run()
```

----------------------------------------

TITLE: Original Window Initialization Call - Arcade Python
DESCRIPTION: Shows the constructor call for a class inheriting from `arcade.Window`. It initializes the window with specific dimensions and a title, typical when the main class serves as the window itself.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/views/index.rst#_snippet_2

LANGUAGE: python
CODE:
```
super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
```

----------------------------------------

TITLE: Drawing the Game State - Arcade Python
DESCRIPTION: Handles rendering the current game state to the screen. This method is called automatically by Arcade. It clears the screen, draws all sprite lists (walls, coins, player, etc.), and then draws any GUI elements or text overlays.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_move_animation.rst#_snippet_3

LANGUAGE: Python
CODE:
```
    def on_draw(self):
        """
        Render the screen.
        """

        # Clear the screen to the background color
        self.clear()

        # Draw our sprites
        self.wall_list.draw()
        self.coin_list.draw()
        self.dont_touch_list.draw()
        self.background_list.draw()
        self.foreground_list.draw()
        self.player_list.draw()
```

----------------------------------------

TITLE: Game Window Class Definition - Arcade Python
DESCRIPTION: Defines the main game window class, `MyGame`, which inherits from `arcade.Window`. This class holds the game state, including sprite lists, the player sprite, the physics engine, and view scrolling variables. It initializes these components and sets up the game environment.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_move_animation.rst#_snippet_1

LANGUAGE: Python
CODE:
```
class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,
                         SCREEN_TITLE)

        # These are 'lists' that hold our sprites. Each sprite in the program goes into
        # a list. For example, we'll have a list of coins, a list of puddles, and another
        # list of walls.
        self.coin_list = None
        self.wall_list = None
        self.foreground_list = None
        self.background_list = None
        self.dont_touch_list = None
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        self.end_of_map = 0

        # Load sounds
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.game_over_sound = arcade.load_sound(":resources:sounds/gameover1.wav")

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
```

----------------------------------------

TITLE: Main Execution Block - Arcade Python
DESCRIPTION: The entry point of the script. It creates an instance of the `MyGame` window class, calls its `setup` method to initialize the game, and then starts the Arcade game loop using `arcade.run()`. This function keeps the window open and running until the user closes it.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_move_animation.rst#_snippet_7

LANGUAGE: Python
CODE:
```
def main():
    """
    Main function
    """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Initializing Basic Arcade Window - Python
DESCRIPTION: This is a basic Arcade program that opens a window with a specified title. It serves as the starting point before adding any shader functionality.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_toy_glow/index.rst#_snippet_0

LANGUAGE: python
CODE:
```
import arcade

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
SCREEN_TITLE = "ShaderToy demo 1"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def on_draw(self):
        self.clear()


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Original Game Window Class - Arcade Python
DESCRIPTION: Defines the initial game class structure, inheriting directly from `arcade.Window`. This is the starting point before refactoring to use `arcade.View` for multi-screen management.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/views/index.rst#_snippet_0

LANGUAGE: python
CODE:
```
class MyGame(arcade.Window):
```

----------------------------------------

TITLE: Drawing with Cameras - Python Arcade
DESCRIPTION: This method demonstrates how to use different cameras for drawing. The scrolling camera is used for game sprites, while the GUI camera is used for static elements like text. Note the adjustment needed for shader positions when using a scrolling camera.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/raycasting/index.rst#_snippet_8

LANGUAGE: Python
CODE:
```
def on_draw(self):
    self.clear()

    # Draw scrolling elements using the sprite camera
    self.camera_sprites.use()
    # Adjust shader position based on camera position
    shader_position = self.camera_sprites.position
    self.shader_program['camera_position'] = shader_position

    # ... draw sprites, walls, etc. ...

    # Draw GUI elements using the GUI camera
    self.camera_gui.use()
    self.gui_text.draw()

    # ... draw other GUI elements ...

```

----------------------------------------

TITLE: Loading Multi-Layer Tilemap in Arcade Python
DESCRIPTION: This snippet shows how to load a different Tiled map file ('map2_level_1.json') in the `setup` function. This specific map contains more layers than previous examples, which are used for various game elements like platforms, coins, decorations, and hazards.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_13.rst#_snippet_0

LANGUAGE: Python
CODE:
```
self.tile_map = arcade.load_tilemap(":resources:tiled_maps/map2_level_1.json", scaling=TILE_SCALING, layer_options=layer_options)
```

----------------------------------------

TITLE: Implementing Sprite Health and Health Bars in Arcade (Python)
DESCRIPTION: This Python code uses the arcade library to create a simple game demonstrating sprite health and a visual health bar. It defines custom Player, Enemy, and Bullet classes, manages sprite lists, handles drawing, updates game state based on collisions, and draws a dynamic health bar above the player sprite. The game ends when the player's health drops to zero.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_health.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Health Example"

PLAYER_MOVEMENT_SPEED = 5
BULLET_SPEED = 5
ENEMY_SHOOT_RATE = 0.5 # seconds

PLAYER_START_HEALTH = 100
HEALTHBAR_WIDTH = 25
HEALTHBAR_HEIGHT = 3
HEALTHBAR_OFFSET_Y = 10

class Player(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.health = PLAYER_START_HEALTH
        self.max_health = PLAYER_START_HEALTH

    def draw_health_bar(self):
        # Draw the background
        if self.health < self.max_health:
            arcade.draw_rectangle_filled(self.center_x,
                                         self.center_y + HEALTHBAR_OFFSET_Y,
                                         HEALTHBAR_WIDTH,
                                         HEALTHBAR_HEIGHT,
                                         arcade.color.RED)

        # Draw the current health
        health_width = HEALTHBAR_WIDTH * (self.health / self.max_health)
        arcade.draw_rectangle_filled(self.center_x - 0.5 * (HEALTHBAR_WIDTH - health_width),
                                     self.center_y + HEALTHBAR_OFFSET_Y,
                                     health_width,
                                     HEALTHBAR_HEIGHT,
                                     arcade.color.GREEN)

class Enemy(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.time_since_last_shot = 0

    def update(self, delta_time):
        self.time_since_last_shot += delta_time
        # Add logic to shoot at player

class Bullet(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        self.player_list = None
        self.enemy_list = None
        self.bullet_list = None

        self.player_sprite = None
        self.enemy_sprite = None

        self.game_over = False

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Create player
        self.player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player_sprite.center_x = SCREEN_WIDTH // 4
        self.player_sprite.center_y = SCREEN_HEIGHT // 2
        self.player_list.append(self.player_sprite)

        # Create enemy
        self.enemy_sprite = Enemy(":resources:images/animated_characters/male_person/malePerson_idle.png", 0.5)
        self.enemy_sprite.center_x = 3 * SCREEN_WIDTH // 4
        self.enemy_sprite.center_y = SCREEN_HEIGHT // 2
        self.enemy_list.append(self.enemy_sprite)

    def on_draw(self):
        arcade.start_render()

        self.player_list.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()

        # Draw health bar
        self.player_sprite.draw_health_bar()

        if self.game_over:
            arcade.draw_text("Game Over", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                             arcade.color.WHITE, 50, anchor_x="center")

    def on_update(self, delta_time):
        if self.game_over:
            return

        self.bullet_list.update()
        self.enemy_list.update(delta_time) # Enemy shoots logic would be here

        # Check for bullet collisions with player
        player_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bullet_list)

        for bullet in player_hit_list:
            bullet.remove_from_sprite_lists()
            self.player_sprite.health -= 10 # Reduce health
            if self.player_sprite.health <= 0:
                self.game_over = True

        # Remove bullets that go off screen
        for bullet in self.bullet_list:
            if bullet.bottom > SCREEN_HEIGHT or bullet.top < 0 or \
               bullet.right < 0 or bullet.left > SCREEN_WIDTH:
                bullet.remove_from_sprite_lists()

    def on_mouse_motion(self, x, y, dx, dy):
        # Move player with mouse
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Sprite Coin Collection Across Levels (Arcade Python)
DESCRIPTION: This snippet provides the core implementation of an arcade game view where a player navigates levels, collects coins using sprite collision detection, and advances to the next level upon clearing all coins. It sets up sprite lists for player, coins, and walls, integrates a platformer physics engine, handles keyboard input for movement and jumping, and manages the game state including score and level progression.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_collect_coins_diff_levels.rst#_snippet_0

LANGUAGE: Python
CODE:
```
# Simplified example based on sprite_collect_coins_diff_levels.py
import arcade
import os

SPRITE_SCALING = 0.5
COIN_SCALING = 0.25
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 0.5
PLAYER_JUMP_SPEED = 15

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Collect Coins Different Levels"

class GameView(arcade.View):
    """
    Main game view for different levels of coin collection.
    """

    def __init__(self):
        super().__init__()

        # These lists will hold different types of sprites
        self.player_list = None
        self.coin_list = None
        self.wall_list = None

        # Player sprite
        self.player_sprite = None

        # Physics engine
        self.physics_engine = None

        # Game state
        self.score = 0
        self.level = 1
        
        # Placeholder list of levels - could be Tiled maps or custom structures
        self.levels = [
            {"walls": [(400, 300)], "coins": [(200, 100), (300, 100)]},
            {"walls": [(200, 400), (600, 400)], "coins": [(100, 200), (700, 200), (400, 150)]}
        ]

    def setup(self):
        """ Set up the game for the current level. Call this to restart or change levels. """
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player sprite
        self.player_sprite = arcade.Sprite("player.png", SPRITE_SCALING) # Placeholder asset
        # Position player - could be level-dependent
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        # Load level data
        if self.level - 1 < len(self.levels):
            current_level_data = self.levels[self.level - 1]

            # Add walls for the current level
            for x, y in current_level_data.get("walls", []):
                wall = arcade.Sprite("wall.png", SPRITE_SCALING) # Placeholder asset
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)

            # Add coins for the current level
            for x, y in current_level_data.get("coins", []):
                coin = arcade.Sprite("coin.png", COIN_SCALING) # Placeholder asset
                coin.center_x = x
                coin.center_y = y
                self.coin_list.append(coin)
        else:
             print("Reached beyond available levels!")
             # Handle game completion/end state
             return

        # Create the physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)

    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.setup()

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        # Draw score
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, 10, arcade.csscolor.WHITE, 18)

        # Draw level
        level_text = f"Level: {self.level}"
        arcade.draw_text(level_text, SCREEN_WIDTH - 100, 10, arcade.csscolor.WHITE, 18)

    def on_key_press(self, key, modifiers):
        """ Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called when the user releases a key. """

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Update the physics engine
        self.physics_engine.update()

        # Check for coin collisions
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.coin_list)

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        # Check if level is complete (all coins collected)
        if len(self.coin_list) == 0:
            self.level += 1
            if self.level - 1 < len(self.levels):
                print(f"Starting Level {self.level}")
                self.setup() # Load the next level
            else:
                print("Game Complete!")
                # Optionally switch to a win screen view
                # game_complete_view = GameCompleteView()
                # self.window.show_view(game_complete_view)

def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game_view = GameView()
    window.show_view(game_view)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Draw Card Sprites - Python
DESCRIPTION: Implements the `on_draw` method in `MyGame` to handle rendering. It clears the screen and then draws all the sprites currently in the `card_list`.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_5

LANGUAGE: Python
CODE:
```
    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        arcade.start_render()

        # Draw the card list
        self.card_list.draw()

    # ... rest of the class ...
```

----------------------------------------

TITLE: Loading Tiled Map in Arcade Python
DESCRIPTION: This Python code snippet demonstrates how to create a basic arcade window, load a Tiled map file (.tmx), and display the map layers as sprite lists. It sets up the game window, loads a specific map file, accesses a layer (like 'Walls') as a sprite list, and includes basic drawing logic.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_tiled_map.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Tiled Map Example"

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer for the game """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.wall_list = None
        self.player_list = None

        # Set up the player
        self.player_sprite = None

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Load the map
        map_name = ":resources:tiled_maps/map.tmx" # Example map path
        layer_options = {
            "Walls": {
                "use_spatial_hash": True,
            },
        }
        self.tile_map = arcade.load_tilemap(map_name, 1, layer_options)

        # Get the wall list
        self.wall_list = self.tile_map.sprite_lists["Walls"]

        # Set up the player (example)
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_adventurer/female_adventurer_idle.png", 0.5)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        # Set the viewport
        self.setup_viewport()

    def setup_viewport(self):
        """ Set up the viewport """
        # Center the viewport on the player (or map origin for simplicity)
        # For this simple example, let's just show the map
        pass # Or implement scrolling if needed

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        self.clear()

        # Draw our sprites
        self.wall_list.draw()
        self.player_list.draw() # Draw player if added

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Update player movement (example)
        # self.player_list.update()

        # Update viewport (if scrolling)
        # self.setup_viewport()
        pass

def main():
    """ Main function """
    window = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Update Camera Position to Follow Player (Arcade Python)
DESCRIPTION: Updates the camera's position in the update loop to match the player's position. This causes the camera to follow the player, keeping them centered on the screen.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_07.rst#_snippet_3

LANGUAGE: python
CODE:
```
self.camera.position = self.player_sprite.position
```

----------------------------------------

TITLE: Setting up a Basic Arcade Window in Python
DESCRIPTION: This snippet demonstrates the fundamental structure for creating and running a basic window in the Arcade library. It defines a custom window class inheriting from `arcade.Window`, sets up constants for dimensions and title, initializes the window, and includes a basic drawing method. The `main` function instantiates the window and starts the Arcade event loop.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/gui_0_basic_setup.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Basic GUI Setup"

class MyWindow(arcade.Window):
    """ Main application window. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """ Render the screen. """
        self.clear()
        # Drawing code goes here

def main():
    """ Main function """
    window = MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Implementing Platformer with Enemies - Python Arcade
DESCRIPTION: This snippet contains the complete source code for a platformer game example built with the arcade library. It includes setup for the game window, player, enemies, and game loop logic.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_enemies_in_platformer.rst#_snippet_0

LANGUAGE: Python
CODE:
```
# This is a placeholder for the code in sprite_enemies_in_platformer.py
# It would typically contain classes for the game window, player, enemies, etc.
# Example:
# import arcade
#
# class MyGame(arcade.Window):
#     def __init__(self):
#         super().__init__(800, 600, "Platformer with Enemies")
#         # Setup game elements here
#
#     def setup(self):
#         # Initialize game state
#         pass
#
#     def on_draw(self):
#         arcade.start_render()
#         # Draw game elements
#         pass
#
#     def on_update(self, delta_time):
#         # Update game state
#         pass
#
# def main():
#     window = MyGame()
#     window.setup()
#     arcade.run()
#
# if __name__ == "__main__":
#     main()
```

----------------------------------------

TITLE: Updating Game State and Animation - Arcade Python
DESCRIPTION: Updates the position of the player and checks for collisions using the physics engine. It also handles scrolling the camera view to follow the player and updates the player's animation texture based on their current movement speed and direction.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_move_animation.rst#_snippet_6

LANGUAGE: Python
CODE:
```
    def on_update(self, delta_time):
        """
        Movement and game logic
        """

        # Update the physics engine
        self.physics_engine.update()

        # Update player animation
        if self.physics_engine.can_jump():
            self.player_sprite.can_jump = False
        else:
            self.player_sprite.can_jump = True

        # Update animation
        if self.player_sprite.change_x < 0 and self.player_sprite.character_face_direction == RIGHT_FACING:
            self.player_sprite.character_face_direction = LEFT_FACING
        elif self.player_sprite.change_x > 0 and self.player_sprite.character_face_direction == LEFT_FACING:
            self.player_sprite.character_face_direction = RIGHT_FACING

        self.player_sprite.cur_texture += 1
        if self.player_sprite.cur_texture > 7:
            self.player_sprite.cur_texture = 0

        if self.player_sprite.change_x == 0:
            self.player_sprite.texture = self.player_sprite.idle_texture_pair[self.player_sprite.character_face_direction]
        else:
            self.player_sprite.texture = self.player_sprite.walk_textures[self.player_sprite.cur_texture]

        # --- Manage Scrolling ---

        # Track if we need to scroll

        changed = False

        # Scroll left
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= (left_boundary - self.player_sprite.left)
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += (self.player_sprite.right - right_boundary)
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += (self.player_sprite.top - top_boundary)
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= (bottom_boundary - self.player_sprite.bottom)
            changed = True

        # If we scrolled, do it
        if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left, 
                                SCREEN_WIDTH + self.view_left, 
                                self.view_bottom, 
                                SCREEN_HEIGHT + self.view_bottom)
```

----------------------------------------

TITLE: Game Setup Method - Arcade Python
DESCRIPTION: Initializes the game state for a new level or game. This includes resetting sprite lists, creating the player sprite and loading its animated textures, setting the player's starting position, and setting up the physics engine with walls and the player.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_move_animation.rst#_snippet_2

LANGUAGE: Python
CODE:
```
    def setup(self):
        """
        Set up the game here. Call this function to restart the game.
        """

        # Reset the viewport, necessary if we scrolled during a previous game
        self.view_bottom = 0
        self.view_left = 0

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        image_source = ":resources:images/animated_characters/female_adventurer/female_adventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128

        # -- Load textures for player animation --

        # Load textures for idle standing
        self.player_sprite.idle_texture_pair = arcade.load_texture_pair(
            ":resources:images/animated_characters/female_adventurer/female_adventurer_idle.png")

        # Load textures for walking
        self.player_sprite.walk_textures = []
        for i in range(8):
            texture = arcade.load_texture(
                f":resources:images/animated_characters/female_adventurer/female_adventurer_walk{i}.png")
            self.player_sprite.walk_textures.append(texture)

        self.player_sprite.texture = self.player_sprite.idle_texture_pair[0]
        self.player_sprite.character_face_direction = RIGHT_FACING

        self.player_list.append(self.player_sprite)

        # Create the ground
        # This shows using a loop to place multiple sprites on our wall_list
        self.wall_list = arcade.SpriteList()

        # Create the physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                              self.wall_list,
                                                              GRAVITY)
```

----------------------------------------

TITLE: Opening a Window
DESCRIPTION: This snippet shows the basic setup for starting an Arcade window and defining a main view for the application.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import arcade.gui

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Menu Example"

class MainView(arcade.View):
    def __init__(self):
        super().__init__()
        # Initialize UI Manager here later
        self.manager = None

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLUE_GRAY)
        # Enable manager here later

    def on_hide_view(self):
        # Disable manager here later
        pass

    def on_draw(self):
        self.clear()
        # Draw UI here later

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_key_press(self, key, modifiers):
        pass

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Initializing Basic Window Python Arcade
DESCRIPTION: Sets up a basic Arcade window with predefined dimensions and a title. This is the standard starting point for an Arcade application.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/gpu_particle_burst/index.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Particle Burst"

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

window = MyWindow()
arcade.run()
```

----------------------------------------

TITLE: Loading a Texture in Arcade (Python)
DESCRIPTION: Loads an image file into an Arcade Texture object using `arcade.load_texture`. The example uses a resource handle (`:resources:`) to access built-in assets. The resulting texture is stored as a class instance variable (`self.player_texture`) for later use.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_02.rst#_snippet_0

LANGUAGE: Python
CODE:
```
self.player_texture = arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
```

----------------------------------------

TITLE: Detecting Layer Collision and Resetting Game in Arcade Python
DESCRIPTION: This snippet, intended for the `on_update` function, checks for collision between the player sprite and any sprites in the 'Don't Touch' layer of the loaded tilemap. If a collision occurs, it plays the loaded game over sound and calls the `setup` function to reset the game state.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_13.rst#_snippet_2

LANGUAGE: Python
CODE:
```
if arcade.check_for_collision_with_list(
    self.player_sprite, self.scene["Don't Touch"]
):
    arcade.play_sound(self.gameover_sound)
    self.setup()
```

----------------------------------------

TITLE: Install Arcade using pip (bash)
DESCRIPTION: Installs the latest stable version of the Arcade library from PyPI using the pip package manager.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/get_started/install.rst#_snippet_0

LANGUAGE: bash
CODE:
```
pip install arcade
```

----------------------------------------

TITLE: Implementing Instruction, Game, and Game Over Views in Arcade Python
DESCRIPTION: This code provides a complete example demonstrating the use of `arcade.View` subclasses to manage different game states: an initial instruction screen, the main game loop, and a game over screen. It shows how to define separate classes for each view, handle drawing and input within each view, and transition between views using `self.window.show_view()`. The example includes basic game elements like a player, collectibles, scoring, and collision detection.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/view_instructions_and_game_over.rst#_snippet_0

LANGUAGE: python
CODE:
```
import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Instruction and Game Over Views"

class InstructionView(arcade.View):
    def on_show_view(self):
        """ This is run once when switching to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to scroll back to the start so we can see nothing but the menu.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        arcade.draw_text("Instructions Screen", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = GameView()
        self.window.show_view(game_view)


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        # Set up the game variables. These are set in the setup() method
        self.player_sprite = None
        self.coin_list = None
        self.score = 0

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128

        self.coin_list = arcade.SpriteList()
        for i in range(10):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", 0.5)
            coin.center_x = 150 + i * 50
            coin.center_y = 200
            self.coin_list.append(coin)

        self.score = 0

        # Set the background color
        arcade.set_background_color(arcade.csscolor.AMAZON)

    def on_show_view(self):
        """ This is run once when switching to this view """
        self.setup()

    def on_draw(self):
        """ Render the screen. """
        self.clear()
        # Draw our sprites
        self.coin_list.draw()
        self.player_sprite.draw()

        # Draw score
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        """ Movement and game logic """
        # Check for collisions
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each coin we hit, remove it, and add to the score.
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        # Check if all coins are collected
        if len(self.coin_list) == 0:
            game_over_view = GameOverView()
            game_over_view.score = self.score # Pass score to game over view
            self.window.show_view(game_over_view)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
        elif key == arcade.key.UP:
            self.player_sprite.change_y = 5
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -5

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0


class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when switching to this view """
        super().__init__()
        self.texture = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        self.score = 0 # Placeholder for score

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

        output = "Game Over"
        arcade.draw_text(output, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.WHITE, 50, anchor_x="center")

        output = f"Final Score: {self.score}"
        arcade.draw_text(output, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, 20, anchor_x="center")

        output = "Click to restart"
        arcade.draw_text(output, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50,
                         arcade.color.WHITE, 20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, restart the game. """
        game_view = GameView()
        self.window.show_view(game_view)


def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Tank Movement and Turret Rotation Example (Python)
DESCRIPTION: This Python snippet contains a full Arcade example demonstrating player-controlled tank movement via keyboard and turret rotation via mouse. It defines classes for the tank base and barrel, handles input events, updates sprite positions, and calculates the correct angle for the barrel to face the mouse while pivoting around the tank base. Requires the 'arcade' library.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_rotate_around_tank.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import math
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Tank Movement and Turret Rotation"

CHARACTER_SCALING = 0.25
TANK_MOVEMENT_SPEED = 5
BARREL_ROTATION_SPEED = 5 # Degrees per frame

class TankBarrel(arcade.Sprite):
    """ Sprite for the tank barrel """
    def __init__(self, image_file, center_x, center_y, scale=1.0):
        super().__init__(image_file, scale)
        self.center_x = center_x
        self.center_y = center_y

    def update(self):
        # Barrel position stays relative to tank base
        pass # This is handled in the TankBase update


class TankBase(arcade.Sprite):
    """ Sprite for the tank base """
    def __init__(self, image_file, center_x, center_y, scale=1.0):
        super().__init__(image_file, scale)
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = 0
        self.change_y = 0
        self.barrel = None # Will hold the barrel sprite

    def update(self):
        # Update base position
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Update barrel position relative to the base
        # The barrel's rotation point is NOT its center!
        # It rotates around a point at the base of the barrel image.
        # Let's assume the base of the barrel is at -BARREL_LENGTH relative to its center.
        # We need to calculate the rotated position.
        # For simplicity, let's just place it relative to the tank base center
        # This example focuses on barrel rotation, not precise attachment point calculation.
        if self.barrel:
            self.barrel.center_x = self.center_x
            self.barrel.center_y = self.center_y
            # The barrel's rotation logic is in the main window class


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """ Initializer """

        # Call the parent class and set up the window
        super().__init__(width, height, title)

        # Sprite lists
        self.player_list = None

        # Player sprite
        self.player_base = None
        self.player_barrel = None

        # Track key presses for movement
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this to restart the game. """

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()

        # Create the tank base
        self.player_base = TankBase(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
                                  SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, CHARACTER_SCALING)
        self.player_list.append(self.player_base)

        # Create the tank barrel
        # Use a different image to make the rotation point clear
        self.player_barrel = TankBarrel(":resources:images/enemies/slimeBlock.png",
                                       self.player_base.center_x, self.player_base.center_y, CHARACTER_SCALING * 0.8)
        self.player_list.append(self.player_barrel)
        self.player_base.barrel = self.player_barrel # Link base to barrel

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.player_list.draw()

        # Draw instructions
        arcade.draw_text("Move with Arrow Keys", 10, SCREEN_HEIGHT - 20,
                         arcade.csscolor.WHITE, 14)
        arcade.draw_text("Barrel follows mouse cursor", 10, SCREEN_HEIGHT - 40,
                         arcade.csscolor.WHITE, 14)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate player movement based on keys pressed
        self.player_base.change_x = 0
        self.player_base.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_base.change_y = TANK_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_base.change_y = -TANK_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_base.change_x = -TANK_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_base.change_x = TANK_MOVEMENT_SPEED

        # Call update on all sprites (only tank base has movement logic)
        self.player_list.update()

        # --- Barrel Rotation Logic ---
        # Get the angle from the tank base to the mouse cursor
        mouse_x, mouse_y = self.get_mouse_coordinates()

        # Calculate the angle in radians from the base to the mouse
        x_diff = mouse_x - self.player_base.center_x
        y_diff = mouse_y - self.player_base.center_y
        desired_angle_rad = math.atan2(y_diff, x_diff)

        # Convert to degrees and adjust for Arcade's coordinate system (0 is right, rotates counter-clockwise)
        # We want 0 degrees to point right, 90 up, 180 left, 270 down.
        # atan2 gives -pi to pi. 0 is right, pi/2 is up, pi is left, -pi/2 is down.
        # In Arcade, 0 is right, 90 is up, 180 is left, 270 is down. This matches atan2 positive half.
        # For negative atan2 results (below x-axis), we add 360.
        desired_angle_deg = math.degrees(desired_angle_rad)
        if desired_angle_deg < 0:
            desired_angle_deg += 360

        # --- CORRECT Way to Rotate a Barrel around an attachment point ---
        # The barrel sprite rotates around its *center*.
        # To make it look like it rotates around the tank base,
        # we calculate the desired angle from the tank base to the mouse.
        # Then, we set the barrel's angle to this desired angle.
        # This example does not simulate complex physics or limits,
        # it just directly sets the angle to face the mouse.

        # Calculate rotation difference
        current_angle = self.player_barrel.angle
        angle_diff = desired_angle_deg - current_angle

        # Normalize angle difference to be between -180 and 180
        while angle_diff > 180:
            angle_diff -= 360
        while angle_diff < -180:
            angle_diff += 360

        # Limit rotation speed (optional, but good for smoother movement)
        if abs(angle_diff) > BARREL_ROTATION_SPEED:
            angle_diff = math.copysign(BARREL_ROTATION_SPEED, angle_diff)

        # Apply rotation
        self.player_barrel.angle += angle_diff

        # --- WRONG Way (Example of rotating around sprite center when you shouldn't) ---
        # If we were just rotating the barrel sprite directly without considering the tank base,
        # it would rotate around its own center point, which would look incorrect
        # for a turret attached to a tank. The above code demonstrates
        # calculating the angle relative to the *tank base* and setting the barrel's angle.
        # The Barrel sprite's center_x/y is updated in the TankBase update to stay with the tank base.

    def on_key_press(self, key, modifiers):
        """Called when a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when a key is released. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

    def get_mouse_coordinates(self):
        """Helper to get mouse coordinates relative to window."""
        return self._mouse_x, self._mouse_y

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ Mouse motion handler. """
        # Mouse coordinates are tracked by the window automatically,
        # but this method can be used for more complex mouse handling.
        # We store them just for clarity, but self._mouse_x, self._mouse_y
        # are available directly.
        # self._mouse_x = x
        # self._mouse_y = y
        pass # Arcade Window already tracks mouse pos


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

```

----------------------------------------

TITLE: Using 3-Byte Tuple (RGB) (Python)
DESCRIPTION: Specify a color using a tuple of three integers representing Red, Green, and Blue values (0-255).
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/api_docs/arcade.csscolor.rst#_snippet_2

LANGUAGE: Python
CODE:
```
(255, 0, 0)
```

----------------------------------------

TITLE: Handling Runtime Paths in Bundled Code - Python
DESCRIPTION: This crucial Python snippet should be placed at the beginning of your script. It checks if the code is running from a PyInstaller bundle (`sys.frozen`) and, if so, changes the current working directory to the temporary location where the bundle's contents have been extracted (`sys._MEIPASS`). This allows relative paths for data files to work correctly whether the script is run normally or from the bundled executable.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/bundling_with_pyinstaller/index.rst#_snippet_3

LANGUAGE: python
CODE:
```
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
```

----------------------------------------

TITLE: Implement Periodic Enemy Shooting in Arcade (Python)
DESCRIPTION: This snippet demonstrates how to create a custom EnemySprite class with attributes to track the time since the last shot and a defined shooting interval. The update method of the sprite increments the timer and triggers a shooting action when the interval is reached, resetting the timer afterwards. This allows enemies to shoot at regular intervals.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_bullets_periodic.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

# Lines 14-48 (Simulated based on description)
class EnemySprite(arcade.Sprite):
    """ Sprite that represents an enemy, with periodic shooting logic. """
    def __init__(self, filename, scale):
        """ Set up the enemy. """
        super().__init__(filename, scale)

        # Attributes for periodic shooting
        self.time_since_last_shot = 0.0
        self.shoot_interval = 2.0  # Shoot every 2 seconds

    def update(self, delta_time):
        """ Update the enemy's state, including shooting timer. """
        # Update position, etc. (assuming base class handles movement)
        super().update(delta_time)

        # Update shooting timer
        self.time_since_last_shot += delta_time

        # Check if it's time to shoot
        if self.time_since_last_shot >= self.shoot_interval:
            self.shoot() # Call a method to handle the actual shooting
            self.time_since_last_shot = 0.0  # Reset timer

    def shoot(self):
        """ Placeholder method for shooting logic. """
        # This method would typically create a bullet sprite
        # and add it to a bullet list.
        print("Enemy shooting!") # Example action

# Lines 76-79, 86-89, 107-108 (Simulated main game update context)
# In the main game window's on_update method:
# def on_update(self, delta_time):
#     # ... other game logic ...
#     self.enemy_list.update(delta_time) # This calls update on each enemy
#     # ... collision detection, etc. ...

```

----------------------------------------

TITLE: Minimal Sprite and SpriteList Drawing in Arcade (Python)
DESCRIPTION: This minimal example demonstrates the basic steps to draw a sprite using a SpriteList in the Arcade library. It involves creating a window, setting up a SpriteList, creating a Sprite (a colored square in this case), adding the sprite to the list, and drawing the list within the on_draw method.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/sprites/spritelists.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Minimal Sprite Example"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        self.sprite_list = None
        self.player_sprite = None

    def setup(self):
        # Create your sprites and sprite lists here
        self.sprite_list = arcade.SpriteList()

        # Create a sprite
        # For a minimal example, let's just use a colored square
        self.player_sprite = arcade.SpriteSolidColor(50, 50, arcade.color.RED)

        # Position the sprite
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = SCREEN_HEIGHT // 2

        # Add the sprite to the sprite list
        self.sprite_list.append(self.player_sprite)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        # Draw all the sprites.
        self.sprite_list.draw()

    def update(self, delta_time):
        """ Movement and game logic """
        # No movement in this minimal example
        pass

def main():
    """ Main function """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Loading Data from a Root Resource Directory - Python
DESCRIPTION: These snippets show how to load data files from a centralized `resources` directory using relative paths, assuming all game assets are organized within this root. This method simplifies data loading in code and pairs well with bundling the entire `resources` directory.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/bundling_with_pyinstaller/index.rst#_snippet_9

LANGUAGE: python
CODE:
```
sprite = arcade.Sprite("resources/images/player.jpg")
text = open("resources/text/names.txt").read()
```

----------------------------------------

TITLE: Simulating Pegboard Physics with Pymunk in Arcade (Python)
DESCRIPTION: This Python code sets up an Arcade window and uses the Pymunk physics engine to create a pegboard simulation. It initializes the physics space, adds static pegs and dynamic balls, and handles the simulation steps and drawing.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/pymunk_pegboard.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import pymunk
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pymunk Pegboard"

# Physics constants
GRAVITY = (0, -900)
ELASTICITY = 0.8
FRICTION = 0.9

class PegboardWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Pymunk space
        self.space = pymunk.Space()
        self.space.gravity = GRAVITY

        # Lists to hold sprites and physics bodies
        self.all_sprites = arcade.SpriteList()
        self.static_sprites = arcade.SpriteList()
        self.dynamic_sprites = arcade.SpriteList()

        # Add ground
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape = pymunk.Segment(body, (0, 10), (SCREEN_WIDTH, 10), 0)
        shape.friction = FRICTION
        self.space.add(body, shape)

        # Add pegs
        peg_radius = 10
        peg_spacing_x = 50
        peg_spacing_y = 50
        start_x = 50
        start_y = 100

        for row in range(8):
            for col in range(14):
                x = start_x + col * peg_spacing_x + (peg_spacing_x / 2 if row % 2 == 1 else 0)
                y = start_y + row * peg_spacing_y

                body = pymunk.Body(body_type=pymunk.Body.STATIC)
                body.position = x, y
                shape = pymunk.Circle(body, peg_radius)
                shape.friction = FRICTION
                self.space.add(body, shape)

                sprite = arcade.Sprite(":resources:images/pinball/bumper.png", 0.5)
                sprite.center_x = x
                sprite.center_y = y
                self.static_sprites.append(sprite)

        # Add a ball
        self.add_ball()

    def add_ball(self):
        mass = 1
        radius = 15
        moment = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
        body = pymunk.Body(mass, moment)
        x = random.uniform(50, SCREEN_WIDTH - 50)
        y = SCREEN_HEIGHT - 50
        body.position = x, y
        shape = pymunk.Circle(body, radius)
        shape.friction = FRICTION
        shape.elasticity = ELASTICITY
        self.space.add(body, shape)

        sprite = arcade.Sprite(":resources:images/pinball/ball.png", 0.5)
        sprite.pymunk_shape = shape
        sprite.center_x = body.position.x
        sprite.center_y = body.position.y
        self.dynamic_sprites.append(sprite)
        self.all_sprites.append(sprite)

    def on_draw(self):
        arcade.start_render()
        self.static_sprites.draw()
        self.dynamic_sprites.draw()

    def on_update(self, delta_time):
        # Step the physics simulation
        self.space.step(delta_time)

        # Update sprite positions based on physics bodies
        for sprite in self.dynamic_sprites:
            sprite.center_x = sprite.pymunk_shape.body.position.x
            sprite.center_y = sprite.pymunk_shape.body.position.y
            sprite.angle = sprite.pymunk_shape.body.angle * 180 / 3.14159 # Convert radians to degrees

        # Add a new ball occasionally
        if random.random() < 0.005:
             self.add_ball()

def main():
    window = PegboardWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()

```

----------------------------------------

TITLE: Example: Using Sprite Properties for Coin Collection in Arcade
DESCRIPTION: This Python code provides a complete example demonstrating how to use Arcade sprites. It sets up a game window, creates a player sprite and a list of coin sprites, implements simple physics for player movement, handles drawing, updates game logic (including collision detection), and processes keyboard input for player control. The example shows how to manage sprite lists and remove sprites upon collision.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_properties.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Properties Example"

# Player constants
PLAYER_START_X = 50
PLAYER_START_Y = 50
PLAYER_MOVEMENT_SPEED = 5

# Coin constants
COIN_SCALING = 0.5

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """ Initializer """
        super().__init__(width, height, title)

        # Sprite lists
        self.player_list = None
        self.coin_list = None

        # Player sprite
        self.player_sprite = None

        # Physics engine
        self.physics_engine = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.player_list.append(self.player_sprite)

        # Create coins
        for i in range(10):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", COIN_SCALING)
            coin.center_x = 100 + i * 70
            coin.center_y = 300
            self.coin_list.append(coin)

        # Create the physics engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.coin_list)

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()

        # Draw all the sprites.
        self.coin_list.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (especially important for physics engines)
        self.physics_engine.update()

        # Check for collisions
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each coin we hit, remove it, and add to the score
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            # Add score logic here if needed

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()

```

----------------------------------------

TITLE: Handling Coin Collection and Updating Score (Python)
DESCRIPTION: Implements the logic within the game's `on_update` method to process coin collection. It iterates through a list of collided coins, removes them from sprite lists, plays a sound, and increments the player's `score` by 75 points for each coin collected.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_10.rst#_snippet_1

LANGUAGE: Python
CODE:
```
# Within on_update
for coin in coin_hit_list:
    coin.remove_from_sprite_lists()
    arcade.play_sound(self.collect_coin_sound)
    self.score += 75
```

----------------------------------------

TITLE: Shoot Bullets - Mouse Press Handler - Python/Arcade/Pymunk
DESCRIPTION: Implements the on_mouse_press method to handle shooting. It creates a bullet sprite, calculates the trajectory based on the mouse position, positions the bullet slightly away from the player, adds it to the Pymunk space, and applies an impulse to propel it.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/pymunk_platformer/index.rst#_snippet_9

LANGUAGE: python
CODE:
```
def on_mouse_press(self, x, y, button, modifiers):
    # Create bullet sprite
    bullet_sprite = arcade.Sprite(":/misc/bullet.png", 0.5)

    # Position the bullet slightly away from the player
    start_x = self.player_sprite.center_x
    start_y = self.player_sprite.center_y
    bullet_sprite.center_x = start_x
    bullet_sprite.center_y = start_y

    # Calculate angle to mouse
    # Adjust mouse coordinates if camera is scrolling
    camera_x = self.camera.position.x
    camera_y = self.camera.position.y
    adjusted_x = x + camera_x
    adjusted_y = y + camera_y

    angle = arcade.get_angle_degrees(start_x, start_y, adjusted_x, adjusted_y)
    bullet_sprite.angle = angle

    # Add bullet to sprite list
    self.bullet_list.append(bullet_sprite)

    # Create pymunk body and shape
    body = pymunk.Body(BULLET_MASS, pymunk.moment_for_circle(BULLET_MASS, 0, bullet_sprite.width / 2, (0, 0)))
    body.position = pymunk.Vec2d(start_x, start_y)
    shape = pymunk.Circle(body, bullet_sprite.width / 2)
    shape.filter = pymunk.ShapeFilter(categories=BITMASK_BULLET)
    shape.collision_type = COLLISION_TYPE_BULLET

    # Add to physics engine
    self.physics_engine.add_sprite(bullet_sprite, body, shape=shape, gravity=BULLET_GRAVITY)

    # Apply impulse
    force = (BULLET_FORCE, 0)
    self.physics_engine.apply_force(bullet_sprite, force)
```

----------------------------------------

TITLE: Creating and Positioning a Sprite in Arcade (Python)
DESCRIPTION: Creates an `arcade.Sprite` instance from a previously loaded texture. Sprites represent an instance of an image that can be drawn on the screen. The code then sets the sprite's position using its `center_x` and `center_y` properties.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_02.rst#_snippet_1

LANGUAGE: Python
CODE:
```
self.player_sprite = arcade.Sprite(self.player_texture)
self.player_sprite.center_x = 64
self.player_sprite.center_y = 128
```

----------------------------------------

TITLE: Implementing Following Behavior Arcade Python
DESCRIPTION: This Python code snippet uses the arcade library to create a window with a player-controlled sprite and multiple follower sprites. The follower sprites update their positions each frame to move towards the player sprite, demonstrating a simple following behavior. It requires the arcade library.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_follow_simple_2.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import random

SPRITE_SCALING = 0.5
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Follow Simple 2"

MOVEMENT_SPEED = 5

class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

class FollowingSprite(arcade.Sprite):
    def update(self, player_sprite):
        # Simple following logic: move towards the player
        if self.center_y < player_sprite.center_y:
            self.center_y += min(MOVEMENT_SPEED, player_sprite.center_y - self.center_y)
        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(MOVEMENT_SPEED, self.center_y - player_sprite.center_y)

        if self.center_x < player_sprite.center_x:
            self.center_x += min(MOVEMENT_SPEED, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(MOVEMENT_SPEED, self.center_x - player_sprite.center_x)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        self.player_list = None
        self.follower_list = None
        self.player_sprite = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.follower_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = SCREEN_HEIGHT // 2
        self.player_list.append(self.player_sprite)

        # Create follower sprites
        for i in range(10):
            follower = FollowingSprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)
            follower.center_x = random.randrange(SCREEN_WIDTH)
            follower.center_y = random.randrange(SCREEN_HEIGHT)
            self.follower_list.append(follower)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.follower_list.draw()

    def on_update(self, delta_time):
        self.player_list.update()
        self.follower_list.update(self.player_sprite) # Pass player to update method

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
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Implementing Pymunk Box Stacks in Arcade (Python)
DESCRIPTION: This Python code demonstrates how to set up and manage stacks of boxes using the Pymunk physics engine within an Arcade window. It includes initialization of the physics space, creation of static and dynamic bodies (ground and boxes), drawing, physics updates, and handling mouse interactions for dragging boxes. It requires the 'arcade' and 'pymunk' libraries.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/pymunk_box_stacks.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import pymunk
import pymunk.arcade_util

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pymunk Box Stacks"

# Physics constants
GRAVITY = (0, -900)
BOX_SIZE = 40
STACK_HEIGHT = 10

class Game(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """ Initializer """
        super().__init__(width, height, title)

        self.background_color = arcade.color.DARK_BLUE_GRAY

        # -- Pymunk
        self.space = None

        # -- Lists for sprites and physics bodies
        self.box_list = None
        self.static_lines = []

        # -- Mouse interaction
        self.mouse_joint = None
        self.mouse_body = None

    def setup(self):
        """ Set up the game and initialize the physics engine """

        # Create the pymunk space
        self.space = pymunk.Space()
        self.space.gravity = GRAVITY

        # Create lists
        self.box_list = arcade.SpriteList()

        # Create the ground
        ground_points = [(0, 50), (SCREEN_WIDTH, 50)]
        ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        ground_shape = pymunk.Segment(ground_body, ground_points[0], ground_points[1], 0)
        ground_shape.friction = 1.0
        self.space.add(ground_body, ground_shape)
        self.static_lines.append(ground_shape)

        # Create stacks of boxes
        for stack_no in range(5):
            for i in range(STACK_HEIGHT):
                # Create a box sprite
                box_sprite = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", 0.5)
                box_sprite.center_x = 100 + stack_no * 100
                box_sprite.center_y = 50 + BOX_SIZE / 2 + i * BOX_SIZE
                self.box_list.append(box_sprite)

                # Create a physics body for the box
                mass = 1
                moment = pymunk.moment_for_box(mass, (BOX_SIZE, BOX_SIZE))
                body = pymunk.Body(mass, moment)
                body.position = pymunk.Vec2d(box_sprite.center_x, box_sprite.center_y)
                shape = pymunk.Poly.create_box(body, (BOX_SIZE, BOX_SIZE))
                shape.friction = 0.8
                shape.elasticity = 0.1
                self.space.add(body, shape)

                # Store the shape on the sprite for easy access
                box_sprite.pymunk_shape = shape

        # Create a mouse body for interactive dragging
        self.mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.box_list.draw()

        # Draw static shapes (ground)
        for line in self.static_lines:
             body = line.body
             pv1 = body.position + line.a.rotated(body.angle)
             pv2 = body.position + line.b.rotated(body.angle)
             arcade.draw_line(pv1.x, pv1.y, pv2.x, pv2.y, arcade.color.BLACK, 3)

        # Draw mouse joint if active
        if self.mouse_joint:
            arcade.draw_line(self.mouse_joint.anchor_a.x, self.mouse_joint.anchor_a.y,
                             self.mouse_joint.anchor_b.x, self.mouse_joint.anchor_b.y,
                             arcade.color.RED, 2)

    def on_update(self, delta_time):
        """ Physics step """
        # Update physics
        self.space.step(delta_time)

        # Update sprite positions based on physics bodies
        for box_sprite in self.box_list:
            box_sprite.center_x = box_sprite.pymunk_shape.body.position.x
            box_sprite.center_y = box_sprite.pymunk_shape.body.position.y
            box_sprite.angle = box_sprite.pymunk_shape.body.angle * 180 / 3.14159

        # Update mouse body position
        if self.mouse_joint:
            self.mouse_body.position = self.mouse_joint.anchor_a

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """
        if button == arcade.MOUSE_BUTTON_LEFT:
            # Check if we clicked on a box
            hit_sprites = arcade.get_sprites_at_point((x, y), self.box_list)
            if hit_sprites:
                # Pick up the first box found
                shape = hit_sprites[0].pymunk_shape
                body = shape.body

                # Create a mouse joint to drag the body
                self.mouse_joint = pymunk.PivotJoint(self.mouse_body, body, (x, y), body.world_to_local((x, y)))
                self.mouse_joint.max_force = 50000 # Adjust force as needed
                self.mouse_joint.error_bias = pow(1 - 0.15, 60)
                self.space.add(self.mouse_joint)

    def on_mouse_release(self, x, y, button, modifiers):
        """ Called when the user releases a mouse button. """
        if button == arcade.MOUSE_BUTTON_LEFT and self.mouse_joint:
            # Release the mouse joint
            self.space.remove(self.mouse_joint)
            self.mouse_joint = None

    def on_mouse_motion(self, x, y, dx, dy):
        """ User moves mouse """
        if self.mouse_joint:
            # Update the target position of the mouse joint
            self.mouse_joint.anchor_a = (x, y)


def main():
    """ Main function """
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

```

----------------------------------------

TITLE: Basic Arcade Program - Python
DESCRIPTION: A minimal Arcade window setup serving as a starting template for projects. It initializes a window with a specified size and title and sets a background color.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_inputs/index.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Empty Project"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()
        # Drawing code goes here

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Implement Scrolling Camera with Margins in Arcade
DESCRIPTION: This Python code snippet demonstrates how to create a game window using the Arcade library with a scrolling camera. The camera follows the player character but only activates scrolling when the player moves within predefined margin distances from the edges of the current viewport. It includes setup for sprites, physics, and handling player movement and camera updates.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_move_scrolling_box.rst#_snippet_0

LANGUAGE: python
CODE:
```
import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move with a Scrolling Screen - Margins"

CHARACTER_SCALING = 0.5
TILE_SCALING = 0.5

PLAYER_MOVEMENT_SPEED = 5

# Scrolling margins
LEFT_VIEWPORT_MARGIN = 200
RIGHT_VIEWPORT_MARGIN = 200
BOTTOM_VIEWPORT_MARGIN = 150
TOP_VIEWPORT_MARGIN = 150

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Set up the game and initialize the variables. """

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are lists that hold our sprites. Each list
        # needs to be created so we can add sprites to it.
        self.coin_list = None
        self.wall_list = None
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Physics engine
        self.physics_engine = None

        # Camera
        self.camera = None

        # Keep track of the score
        self.score = 0

        # Keep track of the current viewport. This maps to
        # the lower left corner of the screen.
        self.view_bottom = 0
        self.view_left = 0

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # Set up the Camera
        self.camera = arcade.Camera(self.width, self.height)

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        image_source = ":resources:images/animated_characters/female_adventurer/female_adventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        # Create the ground
        # This shows using a loop to place multiple sprites
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        # Put some boxes on the ground
        # This shows using a coordinate list to place multiple sprites
        coordinate_list = [[512, 96],
                           [256, 96],
                           [768, 96]]

        for coordinate in coordinate_list:
            # Add a box for the top row
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Create coins
        for x in range(128, 1250, 256):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", TILE_SCALING)
            coin.center_x = x
            coin.center_y = 128
            self.coin_list.append(coin)

        # Create the physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=1)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        self.clear()

        # Activate the game camera
        self.camera.use()

        # Draw our sprites
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, self.view_left + 10, self.view_bottom + 10,
                         arcade.csscolor.WHITE, 18)

    def on_key_press(self, key, modifiers):
        """ Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = 20
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called when the user releases a key. """

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Update the physics engine
        self.physics_engine.update()

        # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.coin_list)

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            # Remove the coin
            coin.remove_from_sprite_lists()
            # Add one to the score
            self.score += 1

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # If we scrolled, update our viewport and the camera
        if changed:
            # Only scroll to levels that make sense
            self.view_left = int(self.view_left)
            self.view_bottom = int(self.view_bottom)

            # Do the scrolling
            self.camera.move( (self.view_left, self.view_bottom) )


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Minimal arcade.View Implementation (Python)
DESCRIPTION: This snippet shows a basic implementation of an arcade.View class and how to display it in a window. It includes methods for showing the view, drawing content, and handling mouse input.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/view_screens_minimal.rst#_snippet_0

LANGUAGE: python
CODE:
```
import arcade

class MyView(arcade.View):
    def on_show_view(self):
        """ This is called when the view is first shown. """
        arcade.set_background_color(arcade.color.BLUE)

    def on_draw(self):
        """ Render the screen. """
        self.clear()
        arcade.draw_text("Minimal View", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """
        print("Mouse pressed!")

def main():
    """ Main function """
    window = arcade.Window(800, 600, "Minimal View Example")
    start_view = MyView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Create Card Sprite Class - Python
DESCRIPTION: Defines a custom `Card` class that inherits from `arcade.Sprite`. It stores the card's suit and value, automatically loads the correct image, and disables hit box calculation for performance.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_2

LANGUAGE: Python
CODE:
```
class Card(arcade.Sprite):
    """ Card sprite """

    def __init__(self, suit, value, face_up=False):
        """ Card constructor """

        # Attributes for suit and value
        self.suit = suit
        self.value = value

        # Image to use for the sprite when face up
        self.image_file_name = f":resources:images/card/{self.suit}/{self.value}.png"

        # Call the parent class constructor
        super().__init__(self.image_file_name, CARD_SCALE, hit_box_algorithm="None")

        # By default, face card down
        self.face_up = face_up

    @property
    def is_face_down(self):
        """ Is this card face down? """
        return not self.face_up

    def face_down(self):
        """ Turn card face-down """
        self.texture = arcade.load_texture(FACE_DOWN_IMAGE)
        self.face_up = False

    def face_up(self):
        """ Turn card face-up """
        self.texture = arcade.load_texture(self.image_file_name)
        self.face_up = True
```

----------------------------------------

TITLE: Initializing Score and GUI Camera Variables (Python)
DESCRIPTION: Initializes variables for a GUI camera (`gui_camera`) and the player's score (`score`) in the class constructor (`__init__`) and setup method. The `gui_camera` is set to `None` initially and then created as an `arcade.Camera2D` in `setup`. The score is an integer initialized to 0. These variables are essential for tracking the player's points and managing the screen-space display.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_10.rst#_snippet_0

LANGUAGE: Python
CODE:
```
# Within __init__
self.gui_camera = None
self.score = 0
```

LANGUAGE: Python
CODE:
```
# Within setup
self.gui_camera = arcade.Camera2D()
self.score = 0
```

----------------------------------------

TITLE: Activate Camera for Drawing (Arcade Python)
DESCRIPTION: Activates the camera before drawing elements that should be affected by its position and zoom. This line should typically come before drawing SpriteLists.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_07.rst#_snippet_2

LANGUAGE: python
CODE:
```
self.camera.use()
```

----------------------------------------

TITLE: Initializing Arcade InputManager and Defining Actions/Axes - Python
DESCRIPTION: This snippet demonstrates how to initialize an `arcade.InputManager` instance and define custom game actions ('Jump') and axes ('Move'). It shows how to map various inputs like keyboard keys (`arcade.Keys`) and controller buttons/axes (`arcade.ControllerButtons`, `arcade.ControllerAxes`) to these actions and axes, including scaling for axis inputs. It sets up a basic input configuration for a platformer game.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/arcade/future/input/README.md#_snippet_0

LANGUAGE: Python
CODE:
```
input_manager = arcade.InputManager()

input_manager.new_action("Jump")
input_manager.add_action_input("Jump", arcade.Keys.SPACE)
input_manager.add_action_input("Jump", arcade.ControllerButtons.BOTTOM_FACE)

input_manager.new_axis("Move")
input_manager.add_axis_input("Move", arcade.Keys.LEFT, scale=-1.0)
input_manager.add_axis_input("Move", arcade.Keys.RIGHT, scale=1.0)
input_manager.add_axis_input("Move", arcade.ControllerAxes.LEFT_STICK_X, scale=1.0)
```

----------------------------------------

TITLE: Updating the InputManager State - Python
DESCRIPTION: This snippet shows the necessary call to update the state of the `arcade.InputManager`. This method should be invoked regularly, typically within the game's update loop (e.g., an `on_update` function), to process raw input events and update axis values based on the current state of connected devices.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/arcade/future/input/README.md#_snippet_3

LANGUAGE: Python
CODE:
```
input_manager.update()
```

----------------------------------------

TITLE: Run Built-in Arcade Example - Bash
DESCRIPTION: Execute a specific example module directly from the installed Arcade library using the Python interpreter in module mode. This verifies the installation and opens a basic window.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_01.rst#_snippet_0

LANGUAGE: bash
CODE:
```
python -m arcade.examples.platform_tutorial.01_open_window
```

----------------------------------------

TITLE: Initialize Card SpriteList - Python
DESCRIPTION: Adds an attribute `card_list` to the `MyGame` class constructor to create and store an `arcade.SpriteList` which will hold all the card sprites in the game.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_3

LANGUAGE: Python
CODE:
```
class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # Sprite list with all the cards
        self.card_list = None

    # ... rest of the class ...
```

----------------------------------------

TITLE: Using Analog Stick Values in Update - Arcade Python
DESCRIPTION: Demonstrates how to access the raw analog stick values (`leftx`, `lefty`) from a connected controller (`self.controller`) within a game's `update` loop. It shows how to use these values to potentially change an object's position or velocity, noting the y-axis inversion.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/controller.rst#_snippet_4

LANGUAGE: Python
CODE:
```
    def update(self, delta_time):
          # Update the position according to the game controller
          if self.controller:
              print(self.controller.leftx, self.controller.lefty)

              self.object.change_leftx = self.controller.leftx
              self.object.change_lefty = -self.controller.lefty
```

----------------------------------------

TITLE: Run an Arcade Example (bash)
DESCRIPTION: Executes a specific example script included with the Arcade library using the Python interpreter's module execution flag (-m) to verify installation and see basic usage.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/get_started/install.rst#_snippet_4

LANGUAGE: bash
CODE:
```
python -m arcade.examples.sprite_explosion_bitmapped
```

----------------------------------------

TITLE: Arcade Game: Collect Bouncing Coins (Python)
DESCRIPTION: This Python code implements a simple 2D game using the arcade library. It sets up a game window, creates a player sprite and multiple coin sprites with bouncing physics, handles player movement, detects collisions between the player and coins, and removes collected coins.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_collect_coins_move_bouncing.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Collect Bouncing Coins"

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

MOVEMENT_SPEED = 5
BOUNCE_SPEED = 3

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Variable that will hold the sprite lists
        self.player_list = None
        self.coin_list = None

        # Set up the player info
        self.player_sprite = None

        # Set the background color
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """
        Set up the game here. Call this to restart the game.
        """

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Create the player sprite
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Give the coin a random initial velocity for bouncing
            coin.change_x = random.choice([-1, 1]) * BOUNCE_SPEED
            coin.change_y = random.choice([-1, 1]) * BOUNCE_SPEED

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        """
        Render the screen.
        """

        # Clear the screen to the background color
        self.clear()

        # Draw our sprites
        self.coin_list.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """

        # Move the player
        self.player_list.update()

        # Move the coins and handle bouncing off edges
        self.coin_list.update()

        for coin in self.coin_list:
            # Bounce off left/right
            if coin.left < 0 or coin.right > SCREEN_WIDTH:
                coin.change_x *= -1

            # Bounce off top/bottom
            if coin.bottom < 0 or coin.top > SCREEN_HEIGHT:
                coin.change_y *= -1

        # Generate a list of all sprites that hit the player.
        coins_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.coin_list
        )

        # Loop through each coin we hit, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

def main():
    """
    Main function
    """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

```

----------------------------------------

TITLE: Detecting Player Collision with Coins and Removing in Arcade
DESCRIPTION: Demonstrates how to detect collisions between the player sprite and any sprite in the `coin_list` using `arcade.check_for_collision_with_list`. It then iterates through the resulting list of hit coins and calls `remove_from_sprite_lists` on each one to remove them from all associated sprite lists.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_08.rst#_snippet_2

LANGUAGE: Python
CODE:
```
coin_hit_list = arcade.check_for_collision_with_list(
    self.player_sprite, self.coin_list
)

for coin in coin_hit_list:
    coin.remove_from_sprite_lists()
```

----------------------------------------

TITLE: Install Arcade for user using pip (bash)
DESCRIPTION: Installs the Arcade library for the current user only, useful when not using a virtual environment or lacking system-wide permissions.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/get_started/install.rst#_snippet_1

LANGUAGE: bash
CODE:
```
pip install arcade --user
```

----------------------------------------

TITLE: Implementing Sections with UI in Arcade (Python)
DESCRIPTION: This Python code demonstrates how to use `arcade.Section` to create a simple application with a main menu and a game state. It defines two section classes, `MainMenuSection` and `GameSection`, and uses `arcade.gui` for buttons in the menu. The main function sets up the window and view, starting with the menu section and allowing transitions between sections.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sections_demo_3.rst#_snippet_0

LANGUAGE: python
CODE:
```
import arcade
import arcade.gui

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sections Demo 3"

# --- Section 1: Main Menu ---
class MainMenuSection(arcade.Section):
    def __init__(self, view: arcade.View):
        super().__init__(view)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a vertical box container for buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        @start_button.event("on_click")
        def on_click_start(event):
            self.view.window.show_section(GameSection(self.view))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        @quit_button.event("on_click")
        def on_click_quit(event):
            arcade.exit()

        # Add buttons to the box layout
        self.v_box.add(start_button)
        self.v_box.add(quit_button)

        # Create a UIManager to handle the UI
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_draw(self):
        self.view.clear()
        self.manager.draw()

    def on_hide(self):
        self.manager.disable()

    def on_show(self):
        self.manager.enable()

# --- Section 2: Game ---
class GameSection(arcade.Section):
    def __init__(self, view: arcade.View):
        super().__init__(view)
        # Game state variables would go here
        self.score = 0

    def on_draw(self):
        self.view.clear(arcade.color.DARK_BLUE_GRAY)
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30,
                         arcade.color.WHITE, 20)
        arcade.draw_text("Press ESC to return to Menu", SCREEN_WIDTH // 2, 50,
                         arcade.color.WHITE, 16, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.view.window.show_section(MainMenuSection(self.view))
        elif symbol == arcade.key.SPACE:
            self.score += 10 # Example game logic

# --- Main View and Window ---
class MyView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        # This view doesn't draw anything itself, sections handle drawing
        pass

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = MyView(window)
    window.show_view(view)
    # Start with the main menu section
    window.show_section(MainMenuSection(view))
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Implementing Mouse Handling Using Arcade Sections (Python)
DESCRIPTION: This example shows how to use `arcade.Section` to handle mouse events in distinct areas of the screen. Separate classes `Map` and `Side` inherit from `arcade.Section` and manage their own `on_mouse_release` logic. The `MyView` class utilizes `arcade.SectionManager` to add and enable these sections, allowing the manager to automatically dispatch mouse events based on the sections' defined positions.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/sections.rst#_snippet_1

LANGUAGE: Python
CODE:
```
import arcade

class Map(arcade.Section):

    # ...

    def on_mouse_release(x: int, y: int, *args, **kwargs):
        # clicks on the map are handled here
        pass


class Side(arcade.Section):

    # ...

    def on_mouse_release(x: int, y: int, *args, **kwargs):
        # clicks on the side of the screen are handled here
        pass


class MyView(arcade.View):

    def __init__(self, *args, **kwargs):
        self.map_section = Map(0, 0, 700, self.window.height)
        self.side_section = Side(700, 0, 100, self.window.height)

        self.sm = arcade.SectionManager()
        self.sm.add_section(self.map_section)
        self.sm.add_section(self.side_section)

    def on_show_view(self) -> None:
        self.sm.enable()

    def on_hide_view(self) -> None:
        self.sm.disable()

    # ...
```

----------------------------------------

TITLE: Initialize Arcade Scene Object Python
DESCRIPTION: Creates a new instance of the `arcade.Scene` class and assigns it to the `self.scene` variable, typically done within the game's `setup` method. This object will manage all game sprites and layers.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_11.rst#_snippet_1

LANGUAGE: Python
CODE:
```
self.scene = arcade.Scene()
```

----------------------------------------

TITLE: Implementing scroll_to_player - Python Arcade
DESCRIPTION: This method calculates the target position for the scrolling camera based on the player's location and smoothly moves the camera towards that target using vector interpolation.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/raycasting/index.rst#_snippet_11

LANGUAGE: Python
CODE:
```
def scroll_to_player(self):
    # Calculate the center of the screen relative to the player
    screen_center_x = self.player_sprite.center_x - self.camera_sprites.viewport_width / 2
    screen_center_y = self.player_sprite.center_y - self.camera_sprites.viewport_height / 2

    # Create a target position vector
    player_center = math.Vec2(screen_center_x, screen_center_y)

    # Smoothly interpolate the camera position towards the target
    self.camera_sprites.move_to(player_center, 0.1)

```

----------------------------------------

TITLE: Implementing Game Structure and Player - Python
DESCRIPTION: This snippet provides the basic structure for an arcade game window, including initialization, drawing the player character as a circle, and placeholder methods for updates and input handling. It sets up the main game loop.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/raycasting/step_07.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Raycasting Step 7"

PLAYER_SPEED = 5

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT // 2

    def on_draw(self):
        arcade.start_render()
        # Draw player
        arcade.draw_circle_filled(self.player_x, self.player_y, 10, arcade.color.BLUE)

    def on_update(self, delta_time):
        # Placeholder for movement logic
        pass

    def on_key_press(self, key, modifiers):
        # Placeholder for input handling
        pass

    def on_key_release(self, key, modifiers):
        # Placeholder for input handling
        pass

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Loading a Sound File into a Variable in Python
DESCRIPTION: This snippet demonstrates loading a specific sound file using `arcade.load_sound` and assigning the resulting `Sound` object to a variable named `COIN_SOUND`. This variable is then used in subsequent examples to show how to play the loaded sound data. Requires the `arcade` library.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/sound.rst#_snippet_2

LANGUAGE: python
CODE:
```
COIN_SOUND = arcade.load_sound(":resources:sounds/coin1.wav")
```

----------------------------------------

TITLE: Using Default Resource Handle with Sprite
DESCRIPTION: This snippet demonstrates how to load an image asset using a default resource handle (`:assets:`) when creating an `arcade.Sprite`. Resource handles simplify paths to common asset locations.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/resource_handlers.rst#_snippet_0

LANGUAGE: python
CODE:
```
SPRITE_SCALE = 0.5
FEMALE_PERSON_IDLE = ":assets:images/animated_characters/female_person/femalePerson_idle.png"

my_sprite = arcade.Sprite(FEMALE_PERSON_IDLE, SPRITE_SCALE)
```

----------------------------------------

TITLE: Drawing an Arcade SpriteList (Python)
DESCRIPTION: Draws all sprites contained within the specified SpriteList. This method iterates through the list and calls the draw method on each sprite. It is typically invoked within the main drawing function (e.g., `on_draw`) of an Arcade window.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_03.rst#_snippet_5

LANGUAGE: Python
CODE:
```
self.wall_list.draw()
```

----------------------------------------

TITLE: Initialize Simple Physics Engine - Python Arcade
DESCRIPTION: Creates an instance of `arcade.PhysicsEngineSimple` in the `__init__` method of the Window class. This engine is configured to manage the movement and collision detection for the player sprite against a list of wall sprites. It uses the sprite's `change_x` and `change_y` attributes to determine intended movement.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_04.rst#_snippet_2

LANGUAGE: Python
CODE:
```
self.physics_engine = arcade.PhysicsEngineSimple(
    self.player_sprite, self.wall_list
)
```

----------------------------------------

TITLE: Initialise the Menu View
DESCRIPTION: This defines a basic structure for the MenuView, which will be used to display the main menu options.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_7

LANGUAGE: Python
CODE:
```
class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        self.clear()
        self.manager.draw()

    # Add button setup and event handlers later
```

----------------------------------------

TITLE: Polling an Input Axis Value - Python
DESCRIPTION: This snippet demonstrates how to retrieve the current combined value of a registered input axis from the `InputManager`. The `axis()` method returns a float representing the calculated value based on the state and scaling of all inputs mapped to that axis. This value can be used for continuous input effects, such as applying movement speed based on an analog stick's position.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/arcade/future/input/README.md#_snippet_4

LANGUAGE: Python
CODE:
```
# This returns a float
player.change_x = input_manager.axis("Move") * PLAYER_MOVEMENT_SPEED
```

----------------------------------------

TITLE: Using arcade.color Name
DESCRIPTION: Specifies a color using a named color provided directly within the arcade.color package.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/api_docs/arcade.color.rst#_snippet_1

LANGUAGE: Python
CODE:
```
arcade.color.RED
```

----------------------------------------

TITLE: Handling Keyboard Input (Release) - Arcade Python
DESCRIPTION: Processes keyboard key release events. When a movement key (left/right arrow or 'A'/'D') is released, it checks if the corresponding direction is still being held down by the other key. If not, it sets the player's horizontal movement speed (`change_x`) to zero, stopping movement.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_move_animation.rst#_snippet_5

LANGUAGE: Python
CODE:
```
    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """

        if key == arcade.key.LEFT or key == arcade.key.A:
            if self.player_sprite.change_x < 0:
                self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            if self.player_sprite.change_x > 0:
                self.player_sprite.change_x = 0
```

----------------------------------------

TITLE: Implementing a 2D Grid with Sprites and Data Array in Arcade
DESCRIPTION: This Python code uses the Arcade library to create a graphical grid. It maintains two parallel 2D arrays: one for the numerical data representing the state of each cell, and another holding the `arcade.Sprite` object for that cell. This structure allows for quick updates to the visual representation of a cell by directly changing the color of the corresponding sprite when the data changes, as demonstrated in the `on_update` and `on_mouse_press` methods. Dependencies include the `arcade` library.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/array_backed_grid_sprites_2.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_PIXEL_SIZE = 30
GRID_MARGIN = 50

# Derived constants
GRID_WIDTH = (SCREEN_WIDTH - 2 * GRID_MARGIN) // GRID_PIXEL_SIZE
GRID_HEIGHT = (SCREEN_HEIGHT - 2 * GRID_MARGIN) // GRID_PIXEL_SIZE

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        # Create a 2D array for the grid data
        self.grid_data = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

        # Create a 2D array to hold the sprites
        self.grid_sprites = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

        # Create a SpriteList to draw all sprites
        self.all_sprites = arcade.SpriteList()

        # Populate the grid data and create initial sprites
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                # Initialize data randomly (0 or 1)
                self.grid_data[row][col] = random.randint(0, 1)

                # Create a sprite for this grid cell
                sprite = arcade.SpriteSolidColor(GRID_PIXEL_SIZE, GRID_PIXEL_SIZE, arcade.color.WHITE if self.grid_data[row][col] == 1 else arcade.color.DARK_GRAY)
                sprite.center_x = GRID_MARGIN + col * GRID_PIXEL_SIZE + GRID_PIXEL_SIZE // 2
                sprite.center_y = SCREEN_HEIGHT - (GRID_MARGIN + row * GRID_PIXEL_SIZE + GRID_PIXEL_SIZE // 2)

                # Store the sprite in the 2D sprite grid
                self.grid_sprites[row][col] = sprite

                # Add the sprite to the master list
                self.all_sprites.append(sprite)

    def on_draw(self):
        """ Render the screen. """
        self.clear()
        self.all_sprites.draw()

    def on_update(self, delta_time):
        """ Update the grid data and corresponding sprites. """
        # Example: Randomly flip a cell and update its sprite color
        if random.random() < 0.1: # Small chance to update each frame
            row = random.randint(0, GRID_HEIGHT - 1)
            col = random.randint(0, GRID_WIDTH - 1)

            # Flip the data value
            self.grid_data[row][col] = 1 - self.grid_data[row][col]

            # Update the corresponding sprite's color
            sprite = self.grid_sprites[row][col]
            sprite.color = arcade.color.WHITE if self.grid_data[row][col] == 1 else arcade.color.DARK_GRAY

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """
        # Convert screen coordinates to grid coordinates
        col = (x - GRID_MARGIN) // GRID_PIXEL_SIZE
        row = (SCREEN_HEIGHT - y - GRID_MARGIN) // GRID_PIXEL_SIZE

        # Check if the click is within the grid bounds
        if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:
            # Flip the data value
            self.grid_data[row][col] = 1 - self.grid_data[row][col]

            # Update the corresponding sprite's color
            sprite = self.grid_sprites[row][col]
            sprite.color = arcade.color.WHITE if self.grid_data[row][col] == 1 else arcade.color.DARK_GRAY


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Grid Using Sprites v2")
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Drawing Player SpriteList in Arcade
DESCRIPTION: Draws all sprites contained within the `self.player_list` SpriteList. This is the recommended and more performant way to render sprites in Arcade, leveraging GPU batching.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_03.rst#_snippet_2

LANGUAGE: Python
CODE:
```
self.player_list.draw()
```

----------------------------------------

TITLE: Creating SpriteList with Spatial Hashing - Python
DESCRIPTION: This snippet demonstrates how to create an arcade.SpriteList object with spatial hashing enabled. This optimization is best applied to lists of mostly non-moving sprites to significantly speed up collision checks.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/performance_tips.rst#_snippet_0

LANGUAGE: python
CODE:
```
# Inside a Window or View, and often inside a setup() method
self.spritelist_with_hashing = arcade.SpriteList(use_spatial_hash=True)
```

----------------------------------------

TITLE: Adding Wall Sprites to SpriteList in Arcade
DESCRIPTION: Demonstrates adding multiple wall sprites to the `self.wall_list`. It includes creating a row of grass tiles using a loop and starting to add box sprites from a coordinate list. The code snippet is incomplete in the source text.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_03.rst#_snippet_4

LANGUAGE: Python
CODE:
```
for x in range(0, 1250, 64):
    wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=TILE_SCALING)
    wall.center_x = x
    wall.center_y = 32
    self.wall_list.append(wall)

coordinate_list = [[512, 96], [256, 96], [768, 96]]
for coordinate in coordinate_list:
    wall = arcade.Sprite(
```

----------------------------------------

TITLE: Loading Tiled Map and Creating Scene (Arcade, Python)
DESCRIPTION: This code block, intended for the `setup` function, loads a Tiled map file (`map.json`) using `arcade.load_tilemap`. It applies scaling and uses `layer_options` to enable spatial hashing for the 'Platforms' layer. It then creates a new `arcade.Scene` directly from the loaded `tile_map`.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_12.rst#_snippet_2

LANGUAGE: python
CODE:
```
layer_options = {
    "Platforms": {
        "use_spatial_hash": True
    }
}

self.tile_map = arcade.load_tilemap(
    ":resources:tiled_maps/map.json",
    scaling=TILE_SCALING,
    layer_options=layer_options
)

self.scene = arcade.Scene.from_tilemap(self.tile_map)
```

----------------------------------------

TITLE: Defining and Initializing Arcade Sections in a View - Python
DESCRIPTION: This Python snippet demonstrates how to define custom `arcade.Section` subclasses (Map, Menu, Panel, PopUp) and instantiate them within an `arcade.View`. It shows how to configure sections with specific coordinates, dimensions, names, draw orders, and event acceptance flags (keyboard/mouse). It also illustrates how to add these sections to an `arcade.SectionManager` instance within the View's initializer and enable/disable the manager during view transitions.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/sections.rst#_snippet_2

LANGUAGE: python
CODE:
```
import arcade


class Map(arcade.Section):
    #... define all the section logic


class Menu(arcade.Section):
    #... define all the section logic


class Panel(arcade.Section):
    #... define all the section logic


class PopUp(arcade.Section):
    def __init__(self, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message

    # define draw logic, etc...


class MyView(arcade.View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Call super().__init__
        self.map = Map(left=0, bottom=0, width=600, height=550,
                       name='Map', draw_order=2)
        self.menu = Menu(left=0, bottom=550, width=800, height=50,
                         name='Menu', accept_keyboard_keys=False,
                         accept_mouse_events={'on_mouse_press'})
        self.panel = Panel(left=600, bottom=0, width=200, height=550,
                            name='Panel', accept_keyboard_keys=False,
                            accept_mouse_events=False)

        popup_left = (self.window.width // 2) - 200 # Use self.window
        popup_bottom = (self.window.height // 2) - 100 # Use self.window
        popup_width = 400
        popup_height = 200
        self.popup = PopUp(message='', left=popup_left, bottom=popup_bottom, width=popup_width,
                           height=popup_height, enabled=False, modal=True)

        self.sm = arcade.SectionManager(self) # Pass self (the view) to SectionManager
        self.sm.add_section(self.map)
        self.sm.add_section(self.menu)
        self.sm.add_section(self.panel)
        self.sm.add_section(self.popup)

    def on_show_view(self) -> None:
        self.sm.enable()

    def on_hide_view(self) -> None:
        self.sm.disable()

    def close(self):
        self.popup.message = 'Are you sure you want to close the view?'
        self.popup.enabled = True
```

----------------------------------------

TITLE: Installing Arcade Development Dependencies - Bash
DESCRIPTION: This command installs the Arcade library in editable mode, along with all development dependencies specified in the pyproject.toml file. It requires pip version 21.1 or later for pyproject.toml support.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/CONTRIBUTING.md#_snippet_0

LANGUAGE: bash
CODE:
```
pip install -e '.[dev]'
```

----------------------------------------

TITLE: Locating Arcade Resources in Bundled Apps (Python)
DESCRIPTION: This snippet calculates the absolute path to an 'assets' directory located relative to the current file. This method is crucial for locating resources correctly when the Python application is packaged into a single-file executable, as `__file__` resolves to the temporary unbundled directory. The calculated path is then registered with the `arcade` resource manager.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/resource_handlers.rst#_snippet_9

LANGUAGE: Python
CODE:
```
asset_dir = os.path.join(Path(__file__).parent.resolve(), "assets")
arcade.resources.add_resource_handle("assets", asset_dir)
```

----------------------------------------

TITLE: Handle Keyboard Input - Python Arcade
DESCRIPTION: Implements event handlers for key press and release events within an Arcade Window class. When specific arrow keys or WASD keys are pressed, the player sprite's change in x or y is updated. When released, the corresponding change is set back to zero, stopping movement in that direction. This relies on the Arcade event loop calling these methods.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_04.rst#_snippet_1

LANGUAGE: Python
CODE:
```
def on_key_press(self, key, modifiers):
    """Called whenever a key is pressed."""

    if key == arcade.key.UP or key == arcade.key.W:
        self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
    elif key == arcade.key.DOWN or key == arcade.key.S:
        self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
    elif key == arcade.key.LEFT or key == arcade.key.A:
        self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
    elif key == arcade.key.RIGHT or key == arcade.key.D:
        self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

def on_key_release(self, key, modifiers):
    """Called whenever a key is released."""

    if key == arcade.key.UP or key == arcade.key.W:
        self.player_sprite.change_y = 0
    elif key == arcade.key.DOWN or key == arcade.key.S:
        self.player_sprite.change_y = 0
    elif key == arcade.key.LEFT or key == arcade.key.A:
        self.player_sprite.change_x = 0
    elif key == arcade.key.RIGHT or key == arcade.key.D:
        self.player_sprite.change_x = 0
```

----------------------------------------

TITLE: Initializing Player SpriteList in Arcade
DESCRIPTION: Creates an `arcade.SpriteList` to manage the player sprite and adds the existing player sprite instance to this list. This is typically done in the game's initialization (`__init__`) method.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_03.rst#_snippet_0

LANGUAGE: Python
CODE:
```
self.player_list = arcade.SpriteList()
self.player_list.append(self.player_sprite)
```

----------------------------------------

TITLE: Draw Arcade Scene Python
DESCRIPTION: Renders all sprite layers managed by the scene object in their specified order. This single call replaces individual draw calls for each separate sprite list, simplifying the `on_draw` method.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_11.rst#_snippet_7

LANGUAGE: Python
CODE:
```
self.scene.draw()
```

----------------------------------------

TITLE: Add Player Jumping - Left/Right Force Selection - Python/Pymunk
DESCRIPTION: This code adjusts the horizontal movement force applied to the player based on whether they are currently grounded or in the air, allowing for different movement characteristics.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/pymunk_platformer/index.rst#_snippet_3

LANGUAGE: python
CODE:
```
def update_movement(self, left_pressed, right_pressed):
    # Determine desired horizontal velocity
    target_velocity_x = 0
    if left_pressed and not right_pressed:
        target_velocity_x = -self.MOVE_SPEED
    elif right_pressed and not left_pressed:
        target_velocity_x = self.MOVE_SPEED

    # Apply force/set velocity based on grounded state
    if self.physics_engine.is_on_ground(self):
        # Grounded movement (might use friction)
        self.physics_engine.set_velocity(self, (target_velocity_x, self.body.velocity.y))
    else:
        # Air movement (less control)
        # Apply a smaller force or limit air speed
        air_force = (target_velocity_x - self.body.velocity.x) * self.AIR_ACCELERATION
        self.physics_engine.apply_force(self, (air_force, 0))
```

----------------------------------------

TITLE: Compile Standalone Executable with Nuitka Bash
DESCRIPTION: This command uses the Nuitka module (`python -m nuitka`) to compile the specified Python script (`17_views.py`). The `--standalone` flag creates a distribution folder containing the executable and necessary dependencies. The `--enable-plugin=numpy` flag is used to ensure compatibility with the numpy library if used by the script.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/compiling_with_nuitka/index.rst#_snippet_1

LANGUAGE: bash
CODE:
```
python -m nuitka 17_views.py --standalone --enable-plugin=numpy
```

----------------------------------------

TITLE: Check Collisions with Arcade Scene Layer Python
DESCRIPTION: Performs collision detection between the player sprite and the "Coins" layer retrieved directly from the scene object using dictionary-like access (`self.scene["Coins"]`). This shows how to use a specific layer from the scene with collision functions.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_11.rst#_snippet_6

LANGUAGE: Python
CODE:
```
coin_hit_list = arcade.check_for_collision_with_list(
    self.player_sprite, self.scene["Coins"]
)
```

----------------------------------------

TITLE: Handling Escape Key for Game Reset (Python)
DESCRIPTION: This snippet demonstrates how to handle a key press event in an `arcade` game to trigger a reset. Inside the `on_key_press` function, it checks if the pressed `key` is the Escape key (`arcade.key.ESCAPE`). If it is, it calls the `self.setup()` method, which is responsible for resetting the game state to its initial condition.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_06.rst#_snippet_1

LANGUAGE: Python
CODE:
```
if key == arcade.key.ESCAPE:
        self.setup()
```

----------------------------------------

TITLE: Initializing Platformer Physics Engine - Python
DESCRIPTION: Creates an instance of `arcade.PhysicsEnginePlatformer`, replacing the simpler `PhysicsEngineSimple`. This engine handles gravity and collision with `walls` and `platforms` for platformer games, linking the player sprite and wall list and applying the gravity constant.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_05.rst#_snippet_1

LANGUAGE: python
CODE:
```
self.physics_engine = arcade.PhysicsEnginePlatformer(
    self.player_sprite, walls=self.wall_list, gravity_constant=GRAVITY
)
```

----------------------------------------

TITLE: Basic GUI Layout Setup - Python
DESCRIPTION: This snippet demonstrates the fundamental steps to create a window, initialize the UI manager, define a layout container (UIBoxLayout), add UI elements (UITextArea, UIFlatButton), and position the layout using UIAnchorLayout in the arcade library.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/gui_1_layouts.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import arcade.gui

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "GUI Layout Example")
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a simple layout container
        self.v_box = arcade.gui.UIBoxLayout()

        # Add some widgets (placeholders)
        text_area = arcade.gui.UITextArea(text="Hello, GUI!", width=400, height=50, font_size=24, font_name="Arial")
        self.v_box.add(text_area.with_space_around(bottom=20))

        button = arcade.gui.UIFlatButton(text="Click Me", width=200)
        self.v_box.add(button)

        # Create a UIManager to handle the UI
        self.manager.add(
            arcade.gui.UIAnchorLayout()
            .add(
                self.v_box,
                anchor_x="center_x",
                anchor_y="center_y"
            )
        )

    def on_draw(self):
        arcade.start_render()
        self.manager.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        pass # Handle key presses if needed

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        pass # Handle mouse presses if needed

if __name__ == "__main__":
    window = MyWindow()
    arcade.run()
```

----------------------------------------

TITLE: Initializing the Button
DESCRIPTION: This snippet shows how to create a button, position it using a layout (UIAnchorLayout), and add it to the UIManager.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_6

LANGUAGE: Python
CODE:
```
class MainView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()

        # Create a button
        menu_button = arcade.gui.UIFlatButton(text="Show Menu", width=200)

        # Add button to the manager using an anchor layout
        self.manager.add(
            arcade.gui.UIAnchorLayout().add(
                menu_button,
                anchor_x="center_x",
                anchor_y="center_y"
            )
        )

        # Set up button click handler later
```

----------------------------------------

TITLE: Populate Arcade Scene Layers Python
DESCRIPTION: Iterates through coordinates and adds wall and coin sprites to their respective, pre-initialized layers ("Walls" and "Coins") using `self.scene.add_sprite()`. This shows populating scene layers with multiple sprites based on game data.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_11.rst#_snippet_4

LANGUAGE: Python
CODE:
```
# Create the ground
for x in range(0, 1250, 64):
    wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=TILE_SCALING)
    wall.center_x = x
    wall.center_y = 32
    self.scene.add_sprite("Walls", wall)

# Putting Crates on the Ground
coordinate_list = [[512, 96], [256, 96], [768, 96]]

for coordinate in coordinate_li
    wall = arcade.Sprite(
        ":resources:images/tiles/boxCrate_double.png", scale=TILE_SCALING
    )
    wall.position = coordinate
    self.scene.add_sprite("Walls", wall)

# Add coins to the world
for x in range(128, 1250, 256):
    coin = arcade.Sprite(":resources:images/items/coinGold.png", scale=COIN_SCALING)
    coin.center_x = x
    coin.center_y = 96
    self.scene.add_sprite("Coins", coin)
```

----------------------------------------

TITLE: Initialize Arcade Scene Layers Python
DESCRIPTION: Creates empty layers named "Walls" and "Coins" within the scene using `self.scene.add_sprite_list()`. This method allows specifying layer-specific options like `use_spatial_hash`, which is beneficial for collision detection with many sprites.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_11.rst#_snippet_3

LANGUAGE: Python
CODE:
```
self.scene.add_sprite_list("Walls", use_spatial_hash=True)
self.scene.add_sprite_list("Coins", use_spatial_hash=True)
```

----------------------------------------

TITLE: Update Game Logic and Physics - Python Arcade
DESCRIPTION: Implements the `on_update` method within the Window class, which is called periodically by Arcade to update game state. This method is responsible for advancing the physics engine, which processes sprite movement, handles collisions based on the initialized engine, and updates the sprite's position.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_04.rst#_snippet_3

LANGUAGE: Python
CODE:
```
def on_update(self, delta_time):
    """Movement and Game Logic"""

    self.physics_engine.update()
```

----------------------------------------

TITLE: Loading Sound Files with arcade.load_sound in Python
DESCRIPTION: This snippet demonstrates how to load sound files using the `arcade.load_sound` function. It shows that the `path` argument accepts resource handle prefixes, raw strings with backslashes, and `pathlib.Path` objects, providing flexibility in specifying file locations. Requires the `arcade` library and `pathlib`.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/sound.rst#_snippet_0

LANGUAGE: python
CODE:
```
from pathlib import Path
import arcade

# The path argument accepts paths prefixed with resources handle,
from_handle_prefix = arcade.load_sound(":resources:sounds/hurt1.wav")
# Windows-style backslash paths,
from_windows_path = arcade.load_sound(Path(r"sounds\\windows\\file.wav"))
# or pathlib.Path objects:
from_pathlib_path = arcade.load_sound(Path("imaginary/mac/style/path.wav"))
```

----------------------------------------

TITLE: Registering Action Handler Callbacks - Python
DESCRIPTION: This snippet illustrates two ways to register custom callback functions (like `self.on_action`) with the `arcade.InputManager` to handle action events. Handlers can be passed during initialization via the `action_handlers` argument or added later using the `register_action_handler` method. Both methods can accept a single callable or a list of callables.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/arcade/future/input/README.md#_snippet_2

LANGUAGE: Python
CODE:
```
def on_action(self, action: str, state: arcade.ActionState):
    # Do something based on action name and state

# Set it during the constructor. Can pass a single callable here or a list of them
input_manager = arcade.InputManager(action_handlers=self.on_action)

# Set it after creation. Can also take a single callable or a list here
input_manager.register_action_handler(self.on_action)
```

----------------------------------------

TITLE: Loading Tiled Map with Levels in Arcade (Python)
DESCRIPTION: This Python script demonstrates how to initialize an arcade game window, load a tiled map using `arcade.load_tilemap`, create a scene from the map, set up player and wall sprites, and configure a platformer physics engine. It includes basic event handlers for player movement.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_tiled_map_with_levels.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Work with Levels and a Tiled Map"

# Layer Names
LAYER_NAME_WALLS = "Walls"
LAYER_NAME_COINS = "Coins"
LAYER_NAME_PLAYER = "Player"

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        # Set up the player
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # Load the map
        self.tile_map = None
        self.scene = None

        # Level
        self.level = 1

        # Set the background color
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Load the Tiled map
        map_name = f":resources:tmx_maps/level_{self.level}.tmx"
        layer_options = {
            LAYER_NAME_WALLS: {
                "use_spatial_hash": True,
            },
        }

        # Read the Tiled map
        self.tile_map = arcade.load_tilemap(map_name, 1, layer_options)

        # Initialize Scene with our TileMap, this will automatically add all layers
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Set up the player sprite
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, 0.5)
        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 128
        self.scene.add_sprite(LAYER_NAME_PLAYER, self.player_sprite)

        # Create the physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.scene.get_sprite_list(LAYER_NAME_WALLS), gravity_constant=1
        )

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        self.clear()

        # Draw our Scene
        self.scene.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Update the physics engine
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 5
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -5
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -5
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 5

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Defining an Action Handler Method - Python
DESCRIPTION: This snippet shows the signature for a method intended to handle action events dispatched by the `InputManager`. This method is typically placed on an `arcade.Window`, `arcade.View`, or `arcade.Section`. It receives the action name as a string and the action state (`arcade.ActionState.PRESSED` or `RELEASED`) as parameters.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/arcade/future/input/README.md#_snippet_1

LANGUAGE: Python
CODE:
```
def on_action(self, action: str, state: arcade.ActionState):
    # Do something based on action name and state
```

----------------------------------------

TITLE: Implementing Room Transitions with Sprites in Arcade
DESCRIPTION: This Python code defines a basic game structure using the Arcade library to manage multiple game 'rooms'. It includes a `Room` class to hold room-specific sprites and a `GameView` class to handle game setup, drawing, updates, and player movement, including logic for transitioning the player between different rooms when they reach the screen boundaries.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_rooms.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Moving Between Rooms"

PLAYER_MOVEMENT_SPEED = 5

class Room:
    """ This class holds all the information about the
    different rooms. """
    def __init__(self):
        # Sprites we use to barriers, like walls or fences.
        self.wall_list = None

        # This holds the background images. If you don't have a background
        # image, set this to 'None'.
        self.background = None

        # List of enemies in this room
        self.enemy_list = None

class GameView(arcade.View):
    """ Main application class. """

    def __init__(self):
        """ Initializer for the game """

        # Call the parent class and set up the window
        super().__init__()

        # Sprite lists
        self.player_list = None

        # Set up the player
        self.player_sprite = None

        # Our list of rooms
        self.room_list = []

        # Our starting room number
        self.current_room_no = 0

        # Set background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Set up the player
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create rooms
        room1 = Room()
        room1.wall_list = arcade.SpriteList()
        # Add walls for room 1
        for x in range(0, 800, 32):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 0
            room1.wall_list.append(wall)
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 600
            room1.wall_list.append(wall)
        for y in range(32, 600, 32):
             wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALING)
             wall.center_x = 0
             wall.center_y = y
             room1.wall_list.append(wall)
             wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALING)
             wall.center_x = 800
             wall.center_y = y
             room1.wall_list.append(wall)
        self.room_list.append(room1)

        room2 = Room()
        room2.wall_list = arcade.SpriteList()
        # Add walls for room 2 (different layout)
        for x in range(0, 800, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneMid.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 300
            room2.wall_list.append(wall)
        self.room_list.append(room2)

        # Set the player in the first room
        self.current_room = self.room_list[self.current_room_no]

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.current_room.wall_list.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.window.key_is_pressed(arcade.key.UP):
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.window.key_is_pressed(arcade.key.DOWN):
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.window.key_is_pressed(arcade.key.LEFT):
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.window.key_is_pressed(arcade.key.RIGHT):
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Call update on all sprites
        self.player_list.update()

        # --- Manage Room Transitions ---

        # Did the player hit a wall?
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.current_room.wall_list)

        # If so, move them back
        if len(hit_list) > 0:
            self.player_sprite.center_x -= self.player_sprite.change_x
            self.player_sprite.center_y -= self.player_sprite.change_y

        # Check for room transitions
        if self.player_sprite.center_x > SCREEN_WIDTH:
            self.current_room_no += 1
            if self.current_room_no < len(self.room_list):
                self.current_room = self.room_list[self.current_room_no]
                self.player_sprite.center_x = 10
            else:
                # Wrap around or end game
                self.current_room_no = 0
                self.current_room = self.room_list[self.current_room_no]
                self.player_sprite.center_x = 10

        elif self.player_sprite.center_x < 0:
            self.current_room_no -= 1
            if self.current_room_no >= 0:
                self.current_room = self.room_list[self.current_room_no]
                self.player_sprite.center_x = SCREEN_WIDTH - 10
            else:
                # Wrap around or end game
                self.current_room_no = len(self.room_list) - 1
                self.current_room = self.room_list[self.current_room_no]
                self.player_sprite.center_x = SCREEN_WIDTH - 10

        # Add similar checks for top/bottom transitions if needed

def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game_view = GameView()
    game_view.setup()
    window.show_view(game_view)
    arcade.run()

if __name__ == "__main__":
    main()

```

----------------------------------------

TITLE: Updating Score Text After Coin Collection (Python)
DESCRIPTION: Modifies the coin collection logic in the `on_update` method to dynamically update the content of the `score_text` object whenever the player's score changes. After incrementing the score, it sets the `text` property of the `score_text` object to a new f-string reflecting the updated score value. This ensures the displayed score remains current.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_10.rst#_snippet_4

LANGUAGE: Python
CODE:
```
for coin in coin_hit_list:
    coin.remove_from_sprite_lists()
    arcade.play_sound(self.collect_coin_sound)
    self.score += 75
    self.score_text.text = f"Score: {self.score}"
```

----------------------------------------

TITLE: Implementing Player Jump - Python
DESCRIPTION: Modifies the `on_key_press` method to handle the UP or W key press. It checks if the player is currently able to jump (typically if they are on the ground) using `self.physics_engine.can_jump()` before setting the player's vertical velocity to `PLAYER_JUMP_SPEED`.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_05.rst#_snippet_2

LANGUAGE: python
CODE:
```
if key == arcade.key.UP or key == arcade.key.W:
    if self.physics_engine.can_jump():
        self.player_sprite.change_y = PLAYER_JUMP_SPEED
```

----------------------------------------

TITLE: Defining Game View Class - Arcade Python
DESCRIPTION: Defines the class responsible for containing the main game logic when using the views system. By inheriting from `arcade.View`, this class can represent the active game state and be easily switched to or from.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/views/index.rst#_snippet_1

LANGUAGE: python
CODE:
```
class GameView(arcade.View):
```

----------------------------------------

TITLE: Advancing Level on Reaching Map End | Arcade Python
DESCRIPTION: Adds logic to the `on_update` function to check if the player's horizontal position (`center_x`) has reached or exceeded `self.end_of_map`. If the end is reached, it increments the `self.level` and calls `self.setup()` to reload the game state for the next level.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_14.rst#_snippet_3

LANGUAGE: Python
CODE:
```
# Check if the player got to the end of the level
if self.player_sprite.center_x >= self.end_of_map:
    # Advance to the next level
    self.level += 1

    # Reload game with new level
    self.setup()
```

----------------------------------------

TITLE: Defining Custom Style Dictionary for UIFlatButton in Python
DESCRIPTION: This snippet shows how to create a style dictionary for an Arcade UIFlatButton widget. The dictionary maps widget states like "normal", "hover", "press", and "disabled" to UIStyle objects, allowing customization of appearance attributes like colors and borders based on the widget's state. The defined style is then passed to the UIFlatButton constructor.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/gui/style.rst#_snippet_0

LANGUAGE: Python
CODE:
```
# Styles are dictionaries of UIStyle objects
new_style = {
    # You should provide a style for each widget state
    "normal": UIFlatButton.UIStyle(), # use default values for `normal` state
    "hover": UIFlatButton.UIStyle(
        font_color=arcade.color.BLACK,
        bg=arcade.color.WHITE,
    ),
    "press": UIFlatButton.UIStyle(
        font_color=arcade.color.BLACK,
        bg=arcade.color.WHITE,
        border=arcade.color.WHITE,
    ),
    "disabled": UIFlatButton.UIStyle(
        bg=arcade.color.GRAY,
    )
}

# Pass the style dictionary when creating a UI element
UIFlatButton(style=new_style)
```

----------------------------------------

TITLE: Loading Ladder Layer in GameWindow Setup - Python
DESCRIPTION: Loads the tilemap layer designated for ladders and creates a SpriteList from it. This list is then used for collision detection and drawing the ladders.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/pymunk_platformer/index.rst#_snippet_13

LANGUAGE: Python
CODE:
```
class GameWindow(...):
    def setup(self):
        # ... other setup
        # Load the ladder layer
        self.ladder_list = arcade.tilemap.tilemap_to_spritelist(
            self.tile_map, "Ladders", TILE_SCALING
        )
        # ...
```

----------------------------------------

TITLE: Full Shader Toy Demo Program - Python
DESCRIPTION: A complete Arcade program demonstrating how to set up a window, load a ShaderToy GLSL file, and render it. This serves as a general template for running any ShaderToy shader.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_toy_glow/index.rst#_snippet_12

LANGUAGE: python
CODE:
```
import arcade
from arcade.experimental.shadertoy import Shadertoy

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
SCREEN_TITLE = "Shader Toy"


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.shadertoy: Shadertoy | None = None
        self.time = 0.0

    def setup(self):
        self.shadertoy = Shadertoy.from_file(self.get_size(), "circle_6.glsl")

    def on_draw(self):
        self.clear()
        mouse_position = self.mouse_x, self.mouse_y
        if self.shadertoy:
            self.shadertoy.render(self.time, mouse_position)

    def on_update(self, delta_time: float):
        self.time += delta_time

    def on_resize(self, width: int, height: int):
        super().on_resize(width, height)
        if self.shadertoy:
            self.shadertoy.resize((width, height))

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Enabling the Manager
DESCRIPTION: This method is called when the view is shown. It enables the UIManager to start processing UI events.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_3

LANGUAGE: Python
CODE:
```
class MainView(arcade.View):
    # ... __init__ and other methods

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLUE_GRAY)
        # Enable manager
        self.manager.enable()
```

----------------------------------------

TITLE: Add Player Animation - Player Class - Python/Arcade
DESCRIPTION: Defines a custom PlayerSprite class inheriting from arcade.Sprite. It loads various textures for different states (idle, walking, jumping, falling) and handles animation updates based on the player's movement and physics state via the pymunk_moved method.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/pymunk_platformer/index.rst#_snippet_5

LANGUAGE: python
CODE:
```
class PlayerSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()

        # Load textures
        self.idle_textures = [
            arcade.load_texture(":/characters/playerIdle.png"),
            arcade.load_texture(":/characters/playerIdle.png", flipped_left_right=True)
        ]
        self.walk_textures = []
        for i in range(8):
            texture = arcade.load_texture(f":/characters/playerWalk{i}.png")
            self.walk_textures.append(texture)
            self.walk_textures.append(arcade.load_texture(f":/characters/playerWalk{i}.png", flipped_left_right=True))

        self.jump_textures = [
            arcade.load_texture(":/characters/playerJump.png"),
            arcade.load_texture(":/characters/playerJump.png", flipped_left_right=True)
        ]
        self.fall_textures = [
            arcade.load_texture(":/characters/playerFall.png"),
            arcade.load_texture(":/characters/playerFall.png", flipped_left_right=True)
        ]

        # Set initial texture
        self.texture = self.idle_textures[0]

        # Animation state
        self.cur_texture_index = 0
        self.character_face_direction = RIGHT_FACING
        self.change_x = 0 # Track change for animation
        self.change_y = 0 # Track change for animation
        self.pymunk_moved_distance = 0

    def pymunk_moved(self, physics_engine, dx, dy):
        # Update animation based on movement and state
        self.pymunk_moved_distance += abs(dx) # Use dx from physics engine

        is_on_ground = physics_engine.is_on_ground(self)

        # Change direction
        if dx < -DEAD_ZONE and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif dx > DEAD_ZONE and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Idle animation
        if abs(dx) <= DEAD_ZONE:
            self.texture = self.idle_textures[self.character_face_direction]
            self.pymunk_moved_distance = 0 # Reset walk animation progress
            return

        # Jumping animation
        if not is_on_ground and dy > DEAD_ZONE:
             self.texture = self.jump_textures[self.character_face_direction]
             return

        # Falling animation
        if not is_on_ground and dy < -DEAD_ZONE:
             self.texture = self.fall_textures[self.character_face_direction]
             return

        # Walking animation
        if self.pymunk_moved_distance > DISTANCE_TO_CHANGE_TEXTURE:
            self.pymunk_moved_distance = 0
            self.cur_texture_index += 1
            if self.cur_texture_index >= 8:
                self.cur_texture_index = 0

        frame = self.cur_texture_index
        self.texture = self.walk_textures[frame * 2 + self.character_face_direction]
```

----------------------------------------

TITLE: Add Player Jumping - Jump Force - Python/Pymunk
DESCRIPTION: This snippet demonstrates how to apply a vertical force or impulse to the player's physics body to simulate jumping. It typically checks if the player is grounded before applying the force.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/pymunk_platformer/index.rst#_snippet_2

LANGUAGE: python
CODE:
```
def jump(self):
    # Check if player is grounded
    if self.physics_engine.is_on_ground(self):
        # Apply vertical impulse for jump
        impulse = (0, self.JUMP_FORCE)
        self.physics_engine.apply_impulse(self, impulse)
```

----------------------------------------

TITLE: Handling Window Resize - Python Arcade
DESCRIPTION: This method is called when the window is resized. It updates the viewport dimensions for both the scrolling and GUI cameras to match the new window size, ensuring correct rendering.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/raycasting/index.rst#_snippet_12

LANGUAGE: Python
CODE:
```
def on_resize(self, width, height):
    super().on_resize(width, height)
    # Resize both cameras to match the new window size
    self.camera_sprites.resize(width, height)
    self.camera_gui.resize(width, height)

```

----------------------------------------

TITLE: Add Sprite to Arcade Scene Layer Python
DESCRIPTION: Creates a player sprite and adds it to the scene using `self.scene.add_sprite()`. The first argument, "Player", names the layer, creating it if it doesn't exist. This demonstrates adding a single sprite directly to a scene layer.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_11.rst#_snippet_2

LANGUAGE: Python
CODE:
```
self.player_sprite = arcade.Sprite(self.player_texture)
self.player_sprite.center_x = 64
self.player_sprite.center_y = 128
self.scene.add_sprite("Player", self.player_sprite)
```

----------------------------------------

TITLE: Adding callback for button events 1
DESCRIPTION: This code adds event listeners (on_click callbacks) for the Resume, Start New Game, and Exit buttons.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_11

LANGUAGE: Python
CODE:
```
class MenuView(arcade.View):
    # ... __init__ and other methods

    def on_show_view(self):
        # ... enable manager
        self.resume_button.on_click = self.on_click_resume
        self.new_game_button.on_click = self.on_click_new_game
        self.exit_button.on_click = self.on_click_exit

    def on_click_resume(self, event):
        print("Resume clicked")
        # Code to switch back to game view

    def on_click_new_game(self, event):
        print("New Game clicked")
        # Code to start a new game

    def on_click_exit(self, event):
        print("Exit clicked")
        arcade.exit()
```

----------------------------------------

TITLE: Enabling VSync on Existing Arcade Window (Python)
DESCRIPTION: This snippet shows how to enable vertical synchronization on an existing Arcade window instance after it has been created. The 'set_vsync' method can be called with a boolean value to control vsync behavior during application runtime.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/event_loop.rst#_snippet_1

LANGUAGE: Python
CODE:
```
window.set_vsync(True)
```

----------------------------------------

TITLE: Initialising the Manager
DESCRIPTION: This code initializes the UIManager, which is essential for handling UI elements and their events within an Arcade view.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_2

LANGUAGE: Python
CODE:
```
class MainView(arcade.View):
    def __init__(self):
        super().__init__()
        # Initialize UI Manager
        self.manager = arcade.gui.UIManager()
```

----------------------------------------

TITLE: Accessing SpriteList from Arcade Scene by Indexing (Python)
DESCRIPTION: Demonstrates the new method introduced in Arcade 2.6.4 for accessing a SpriteList within a Scene object using dictionary-style indexing with the layer name as the key. This provides a more direct alternative to using `Scene.name_mapping` or `Scene.get_sprite_list`.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/CHANGELOG_HISTORY.rst#_snippet_0

LANGUAGE: Python
CODE:
```
spritelist = my_scene["My Layer"]
```

----------------------------------------

TITLE: Demonstrating Advanced GUI Buttons in Arcade (Python)
DESCRIPTION: This Python code snippet provides an example of how to implement and use advanced GUI buttons within the arcade library. It likely sets up a window, a UI manager, creates custom or styled buttons, and handles button events.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/gui_3_buttons.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import arcade.gui

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Advanced Button Example")
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a button (example of a simple button, actual code might be more complex)
        button = arcade.gui.UIFlatButton(text="Click Me", width=200)

        # Add button to manager
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=button
            )
        )

    def on_draw(self):
        arcade.start_render()
        self.manager.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        # Handle button clicks (this is where "advanced" logic might go)
        # Example: Check if a specific button was clicked and perform an action
        pass # Placeholder for advanced logic

if __name__ == "__main__":
    window = MyWindow()
    arcade.run()
```

----------------------------------------

TITLE: Handling Key Release for Ladder Climbing - Python
DESCRIPTION: Modifies the on_key_release method to set the `up_pressed` and `down_pressed` flags to `False` when the corresponding keys are released. This stops the vertical climbing movement input.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/pymunk_platformer/index.rst#_snippet_16

LANGUAGE: Python
CODE:
```
class GameWindow(...):
    def on_key_release(self, key, modifiers):
        # ... other key releases
        if key == arcade.key.UP or key == arcade.key.W:
            if self.player_sprite.is_on_ladder: # Only release if on ladder (or was)
                 self.up_pressed = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            if self.player_sprite.is_on_ladder: # Only release if on ladder (or was)
                self.down_pressed = False
        # ...
```

----------------------------------------

TITLE: Updating Camera Position - Python Arcade
DESCRIPTION: Called every frame, this method updates the game state. It includes a call to `scroll_to_player` to ensure the scrolling camera follows the player's movement.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/raycasting/index.rst#_snippet_9

LANGUAGE: Python
CODE:
```
def on_update(self, delta_time):
    # ... update player, physics, etc. ...

    # Scroll the camera to the player
    self.scroll_to_player()

    # ... rest of on_update ...

```

----------------------------------------

TITLE: Initializing Game Window Python Arcade
DESCRIPTION: Initializes the main game window, setting up the OpenGL context. It creates an empty list to manage active particle bursts and loads the GLSL shader program responsible for rendering and animating particles.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/gpu_particle_burst/index.rst#_snippet_3

LANGUAGE: Python
CODE:
```
def __init__(self):
    super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    self.burst_list: list[Burst] = []

    # Create the shader program
    self.program = self.ctx.load_program(
        vertex_shader="vertex_shader_v2.glsl",
        fragment_shader="fragment_shader.glsl"
    )
```

----------------------------------------

TITLE: Checking Arcade Keyboard Modifiers (Python)
DESCRIPTION: Shows how to implement the `on_key_press` method in an Arcade Window or View subclass to check if specific keyboard modifiers (like Shift or Capslock) are active using bitwise AND operations with constants from `arcade.key`. It takes the key symbol and modifiers integer as input and prints a message if the corresponding modifier bit is set. Requires inheriting from `arcade.Window` or `arcade.View`.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/keyboard.rst#_snippet_1

LANGUAGE: python
CODE:
```
# this should be implemented on a subclass of Window or View
def on_key_press(self, symbol, modifiers):

    if modifiers & arcade.key.MOD_SHIFT:
        print("The shift key is held down")

    if modifiers & arcade.key.MOD_CAPSLOCK:
        print("Capslock is on")
```

----------------------------------------

TITLE: Handling Keyboard Input (Press) - Arcade Python
DESCRIPTION: Processes keyboard key press events. When a key is pressed (e.g., arrow keys or 'A'/'D'), it updates the player's intended horizontal movement speed (`change_x`). Pressing the up arrow or 'W' makes the player jump if they are currently on the ground.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_move_animation.rst#_snippet_4

LANGUAGE: Python
CODE:
```
    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
```

----------------------------------------

TITLE: Initializing Arcade Window with VSync Enabled (Python)
DESCRIPTION: This snippet demonstrates how to create an Arcade window instance and enable vertical synchronization by setting the 'vsync' argument to True during initialization. VSync helps prevent screen tearing by synchronizing frame drawing with the monitor's refresh rate.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/event_loop.rst#_snippet_0

LANGUAGE: Python
CODE:
```
arcade.Window(800, 600, "Window Title", vsync=True)
```

----------------------------------------

TITLE: Loading Sound with Streaming Enabled in Python
DESCRIPTION: This snippet shows how to enable streaming mode when loading sound files. It demonstrates passing the `streaming=True` keyword argument to both the `arcade.load_sound` function and the `arcade.Sound` class constructor, suitable for long audio tracks like music or ambiance. Requires the `arcade` library.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/sound.rst#_snippet_9

LANGUAGE: python
CODE:
```
# Both loading approaches accept the streaming keyword.
classical_music_track = arcade.load_sound(":resources:music/1918.mp3", streaming=True)
funky_music_track = arcade.Sound(":resources/music/funkyrobot.mp3", streaming=True)
```

----------------------------------------

TITLE: Initializing Wall SpriteList with Spatial Hashing in Arcade
DESCRIPTION: Creates an `arcade.SpriteList` specifically for wall or obstacle sprites. The `use_spatial_hash=True` argument enables spatial hashing, optimizing collision detection for static or infrequently moving sprites within this list.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_03.rst#_snippet_3

LANGUAGE: Python
CODE:
```
self.wall_list = arcade.SpriteList(use_spatial_hash=True)
```

----------------------------------------

TITLE: Using 4-Byte Tuple (RGBA) (Python)
DESCRIPTION: Specify a color using a tuple of four integers representing Red, Green, Blue, and Alpha values (0-255). Alpha 0 is transparent, 255 is opaque.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/api_docs/arcade.csscolor.rst#_snippet_3

LANGUAGE: Python
CODE:
```
(255, 0, 0, 255)
```

----------------------------------------

TITLE: Initialize Camera in setup (Arcade Python)
DESCRIPTION: Initializes the 2D camera instance in the setup method. Using the default settings is suitable for drawing to the entire screen.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_07.rst#_snippet_1

LANGUAGE: python
CODE:
```
self.camera = arcade.Camera2D()
```

----------------------------------------

TITLE: Creating a Simple Arcade GUI Window and Button (Python)
DESCRIPTION: This snippet demonstrates how to set up a basic arcade window with a UIManager, create a simple button, and add it to the UI using a layout and anchor widget. It shows the minimal structure required to display GUI elements.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/gui_2_widgets.rst#_snippet_0

LANGUAGE: python
CODE:
```
import arcade.gui

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "GUI Widget Gallery")
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a simple button
        button = arcade.gui.UIFlatButton(text="Click Me", width=200)

        # Add button to a layout
        box = arcade.gui.UIBoxLayout()
        box.add(button)

        # Add layout to the manager
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=box)
        )

    def on_draw(self):
        self.clear()
        self.manager.draw()

if __name__ == "__main__":
    window = MyWindow()
    arcade.run()
```

----------------------------------------

TITLE: Initializing Score Text Object (Python)
DESCRIPTION: Initializes the `score_text` variable in the class constructor (`__init__`) and creates an `arcade.Text` object in the setup method. The text object displays the score, formatted as "Score: [current score]". It's positioned near the bottom-left corner of the screen using `start_x` and `start_y`. This object will be used to draw the score.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_10.rst#_snippet_2

LANGUAGE: Python
CODE:
```
# Within __init__
self.score_text = None
```

LANGUAGE: Python
CODE:
```
# Within setup
self.score_text = arcade.Text(f"Score: {self.score}", start_x = 0, start_y = 5)
```

----------------------------------------

TITLE: Applying Dead Zone to Controller Input - Arcade Python
DESCRIPTION: Modifies the `update` method to incorporate a dead zone check (`DEAD_ZONE`) for the controller's analog stick values (`self.controller.x`, `self.controller.y`). If the absolute value of the input is below the dead zone threshold, the object's change in position is set to zero; otherwise, it is updated based on the stick value and a `MOVEMENT_SPEED` constant.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/controller.rst#_snippet_8

LANGUAGE: Python
CODE:
```
def update(self, delta_time):

            # Update the position according to the game controller
            if self.controller:

                # Set a "dead zone" to prevent drive from a centered controller
                if abs(self.controller.x) < DEAD_ZONE:
                    self.object.change_x = 0
                else:
                    self.object.change_x = self.controller.x * MOVEMENT_SPEED

                # Set a "dead zone" to prevent drive from a centered controller
                if abs(self.controller.y) < DEAD_ZONE:
                    self.object.change_y = 0
                else:
                    self.object.change_y = -self.controller.y * MOVEMENT_SPEED
```

----------------------------------------

TITLE: Adding a Title Label - Python/Arcade
DESCRIPTION: This snippet creates a `arcade.gui.UILabel` instance to serve as the title for the menu. It sets the text content, color, and font size for the label.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_16

LANGUAGE: Python
CODE:
```
title_label = arcade.gui.UILabel(
    text="Menu Title",
    text_color=arcade.color.WHITE,
    font_size=20
)
```

----------------------------------------

TITLE: Setting Up Arcade Controller Support
DESCRIPTION: Demonstrates how to create a basic application window and view that supports game controller input using ControllerWindow and MyControllerView (inheriting from ControllerView and UIView). Includes example callbacks for various controller events.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/gui/controller_support.rst#_snippet_0

LANGUAGE: python
CODE:
```
import arcade
from arcade.gui import UIView
from arcade.experimental.controller_window import ControllerWindow, ControllerView


class MyControllerView(ControllerView, UIView):
    def __init__(self):
        super().__init__()

        # Initialize your GUI elements here

    # react to controller events for your game
    def on_connect(self, controller):
        print(f"Controller connected: {controller}")

    def on_disconnect(self, controller):
        print(f"Controller disconnected: {controller}")

    def on_stick_motion(self, controller, stick, value):
        print(f"Stick {stick} moved to {value} on controller {controller}")

    def on_trigger_motion(self, controller, trigger, value):
        print(f"Trigger {trigger} moved to {value} on controller {controller}")

    def on_button_press(self, controller, button):
        print(f"Button {button} pressed on controller {controller}")

    def on_button_release(self, controller, button):
        print(f"Button {button} released on controller {controller}")

    def on_dpad_motion(self, controller, value):
        print(f"D-Pad moved to {value} on controller {controller}")


if __name__ == "__main__":
    window = ControllerWindow(title="Controller Support Example")
    view = MyControllerView()
    window.show_view(view)
    arcade.run()
```

----------------------------------------

TITLE: Implementing Bouncing Coins in Arcade (Python)
DESCRIPTION: This Python code sets up an Arcade window, creates a list of coin sprites with random initial positions and velocities, and updates their positions each frame. It includes logic to reverse the sprite's velocity when it hits the window edges, causing a bouncing effect.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_bouncing_coins.rst#_snippet_0

LANGUAGE: python
CODE:
```
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bouncing Coins"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.coin_list = None

    def setup(self):
        """ Set up the game variables. Call to restart the game. """
        self.coin_list = arcade.SpriteList()

        # Create the coins
        for i in range(10):
            # Create the coin instance
            # We use the ":resources:" prefix to access resources provided by arcade
            coin = arcade.Sprite(":resources:images/items/coinGold.png", 0.5)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Give the coin a random speed
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        self.clear()

        # Draw our sprites
        self.coin_list.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update() on all the sprites
        self.coin_list.update()

        # Loop through each coin
        for coin in self.coin_list:

            # See if the coin hits the edge of the screen.
            # If it does, reverse the speed
            if coin.left < 0 or coin.right > SCREEN_WIDTH:
                coin.change_x *= -1

            if coin.bottom < 0 or coin.top > SCREEN_HEIGHT:
                coin.change_y *= -1

def main():
    """ Main function """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Implementing an On-Screen Timer in Arcade (Python)
DESCRIPTION: This code snippet provides a complete example of how to create, update, and display a simple timer on the screen within an arcade application. It demonstrates setting up a window, handling updates based on delta time, and drawing text to show the elapsed time.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/timer.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.timer = 0.0

    def on_update(self, delta_time):
        """ Update the game state. Called every frame. """
        self.timer += delta_time

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        # Draw the timer
        output = f"Time: {self.timer:.2f}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

def main():
    """ Main function """
    game = MyGame(800, 600, "Timer Example")
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Drawing Score Text with GUI Camera (Python)
DESCRIPTION: Configures the drawing process within the game's `on_draw` method to display the score text using the GUI camera. It activates the `gui_camera` to render elements in screen space, then calls the `draw()` method on the `score_text` object to render it at its specified position, independent of the world camera's movement.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_10.rst#_snippet_3

LANGUAGE: Python
CODE:
```
# Within on_draw
self.gui_camera.use()
self.score_text.draw()
```

----------------------------------------

TITLE: Playing arcade.Sound with arcade.play_sound in Python
DESCRIPTION: This snippet demonstrates playing a loaded `arcade.Sound` object using the `arcade.play_sound` function. It stores the returned playback object (which is a pyglet `Player`) in `self.coin_playback` to allow for later control over this specific playback instance. Requires an `arcade.Sound` object.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/sound.rst#_snippet_3

LANGUAGE: python
CODE:
```
self.coin_playback = arcade.play_sound(COIN_SOUND)
```

----------------------------------------

TITLE: Passing Uniform Data to Shader - Arcade Python
DESCRIPTION: This snippet builds upon the previous example by demonstrating how to pass uniform data from the Python code to the GLSL shader program. This allows dynamic control over shader behavior, such as changing a color or threshold value.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/framebuffer/index.rst#_snippet_3

LANGUAGE: Python
CODE:
```
import arcade
import arcade.gl as gl

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "FrameBuffer Uniform Example"

# Shader that uses a uniform color
SHADER_CODE = """
#version 330 core

in vec2 in_uv;
out vec4 out_color;
uniform sampler2D myTexture;
uniform vec3 highlight_color;

void main()
{
    vec4 tex_color = texture(myTexture, in_uv);
    if (tex_color.a > 0.0) {
        out_color = vec4(highlight_color, tex_color.a); // Use uniform color
    } else {
        out_color = tex_color;
    }
}
"""

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

        # Create a FrameBuffer
        self.fbo = self.ctx.framebuffer(
            color_attachments=[self.ctx.texture((width, height), components=4)]
        )

        # Create a shader program with a uniform
        self.program = self.ctx.program(vertex_shader="#version 330 core\nin vec2 in_vert;\nin vec2 in_uv;\nout vec2 out_uv;\nvoid main() {\n    gl_Position = vec4(in_vert, 0.0, 1.0);\n    out_uv = in_uv;\n}", fragment_shader=SHADER_CODE)

        # Create a geometry object for drawing the texture
        self.quad = gl.geometry.quad_2d_fs()

        # Define a uniform value
        self.highlight_color = (1.0, 0.0, 0.0) # Red

    def on_draw(self):
        # Render to the FrameBuffer
        with self.fbo.activate():
            self.clear()
            arcade.draw_circle_filled(100, 100, 50, arcade.color.RED)
            arcade.draw_rectangle_filled(300, 300, 100, 50, arcade.color.BLUE)

        # Render the FrameBuffer texture using the shader and uniform
        self.clear()
        self.fbo.color_attachments[0].use(0)
        self.program['highlight_color'] = self.highlight_color # Set the uniform
        self.quad.render(self.program)

    def update(self, delta_time):
        # Example: Change the uniform color over time
        # self.highlight_color = (abs(math.sin(self.get_time())), 0.0, 0.0)
        pass

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Adding an Input Field - Python/Arcade
DESCRIPTION: This snippet creates an `arcade.gui.UIInputText` widget. It initializes the input field with a default text value and applies a border using the `with_border` method.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_18

LANGUAGE: Python
CODE:
```
input_text = arcade.gui.UIInputText(text=self.input_text_default).with_border()
```

----------------------------------------

TITLE: Defining Gravity and Jump Constants - Python
DESCRIPTION: Defines constants for the gravitational acceleration and the player's jump speed. These constants are used to configure the physics engine and control the player's vertical movement during a jump.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_05.rst#_snippet_0

LANGUAGE: python
CODE:
```
GRAVITY = 1
PLAYER_JUMP_SPEED = 20
```

----------------------------------------

TITLE: Loading Game Over Sound in Arcade Python
DESCRIPTION: This code adds a sound effect for the game over event by loading a .wav file. It is typically placed in the `__init__` function of the game class to ensure the sound is loaded when the game starts.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_13.rst#_snippet_1

LANGUAGE: Python
CODE:
```
self.gameover_sound = arcade.load_sound(":resources:sounds/gameover1.wav")
```

----------------------------------------

TITLE: Constants and Setup Variables - Arcade Python
DESCRIPTION: Defines constants used throughout the example for screen dimensions, movement speed, gravity, and sprite scaling. These values configure the game window size, the player's speed, the effect of gravity on the player, and the size of the player sprite.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_move_animation.rst#_snippet_0

LANGUAGE: Python
CODE:
```
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Move with a Sprite Animation Example"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 0.5
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

# How many pixels to keep the player away from the edge of the screen.
# Used for scrolling.
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100

RIGHT_FACING = 0
LEFT_FACING = 1
```

----------------------------------------

TITLE: Sending Custom Uniforms from Python - Python
DESCRIPTION: Demonstrates how to pass custom uniform variables (like position and color) from the Python Arcade application to the GLSL shader. It adds attributes to the class and updates them (e.g., from mouse position) for rendering.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_toy_glow/index.rst#_snippet_9

LANGUAGE: python
CODE:
```
import arcade
from arcade.experimental.shadertoy import Shadertoy

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
SCREEN_TITLE = "ShaderToy demo 3"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Load the shader
        file_name = "circle_6.glsl"
        shader_source = open(file_name).read()
        self.shadertoy = Shadertoy(size=self.get_size(),
                                   main_source=shader_source)

        # Custom uniforms
        self.center_x = 0.0
        self.center_y = 0.0
        self.glow_color = (1.0, 0.5, 0.0)

    def on_draw(self):
        self.clear()
        # Pass uniforms during render
        self.shadertoy.render(center_x=self.center_x,
                              center_y=self.center_y,
                              glow_color=self.glow_color)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        # Update center position based on mouse (normalized)
        self.center_x = x / self.width
        self.center_y = y / self.height


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Initialize Arcade Physics Engine with Scene Python
DESCRIPTION: Configures the `arcade.PhysicsEnginePlatformer` to use the player sprite and the "Walls" layer from the scene object. This demonstrates how to access specific layers (which are `SpriteList` instances internally) from the scene by their name using dictionary-like access (`self.scene["Walls"]`).
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_11.rst#_snippet_5

LANGUAGE: Python
CODE:
```
self.physics_engine = arcade.PhysicsEnginePlatformer(
    self.player_sprite, walls=self.scene["Walls"], gravity_constant=GRAVITY
)
```

----------------------------------------

TITLE: Enable Alpha Blending in Arcade (Python)
DESCRIPTION: Configure the OpenGL context within the window's initialization method to enable alpha blending. This is necessary for particles that have an alpha component and need to fade out or be transparent.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/gpu_particle_burst/index.rst#_snippet_17

LANGUAGE: Python
CODE:
```
self.ctx.enable_only(self.ctx.BLEND)
```

----------------------------------------

TITLE: Draw Card Mat Sprites (Arcade, Python)
DESCRIPTION: Adds the necessary drawing call within the `on_draw` method to render the mat sprites on the screen.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_15

LANGUAGE: python
CODE:
```
# Placeholder for code from solitaire_04.py MyGame.on_draw emphasize-lines 6-7
# Example: self.mat_list.draw()
```

----------------------------------------

TITLE: Mapping Keyboard Keys to Values - Python
DESCRIPTION: Defines constants for various keyboard keys and modifiers, mapping them to integer values. These constants are used within the Arcade library for handling keyboard input.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/api_docs/arcade.key.rst#_snippet_0

LANGUAGE: Python
CODE:
```
"""
Mapping of keyboard keys to values.
"""

# fmt: off

# --- Modifier Keys ---
MOD_SHIFT = 0x0001
MOD_CTRL = 0x0002
MOD_ALT = 0x0004
MOD_COMMAND = 0x0008
MOD_NUMLOCK = 0x0010
MOD_CAPSLOCK = 0x0020

# --- Standard Keys ---
SPACE = 32
APOSTROPHE = 39
COMMA = 44
MINUS = 45
PERIOD = 46
SLASH = 47

A = 65
B = 66
Z = 90

KEY_0 = 48
KEY_1 = 49
KEY_9 = 57

F1 = 256
F2 = 257
F12 = 267

LEFT = 263
RIGHT = 262
UP = 265
DOWN = 264

ESCAPE = 256
ENTER = 257
TAB = 258
BACKSPACE = 259
INSERT = 260
DELETE = 261

# fmt: on
```

----------------------------------------

TITLE: Updating Player State and Movement for Ladders - Python
DESCRIPTION: Updates the game state, including checking for collisions between the player and ladders to determine if the player is on a ladder. If on a ladder, it adjusts the player's vertical velocity based on the `up_pressed` and `down_pressed` flags.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/pymunk_platformer/index.rst#_snippet_17

LANGUAGE: Python
CODE:
```
class GameWindow(...):
    def on_update(self, delta_time):
        # ... other updates

        # Check for ladder collision
        ladder_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.ladder_list
        )

        if len(ladder_hit_list) > 0:
            self.player_sprite.is_on_ladder = True
        else:
            self.player_sprite.is_on_ladder = False

        # Handle vertical movement on ladder
        if self.player_sprite.is_on_ladder:
            if self.up_pressed and not self.down_pressed:
                self.player_sprite.climb_movement = 1 # Move up
            elif self.down_pressed and not self.up_pressed:
                self.player_sprite.climb_movement = -1 # Move down
            else:
                self.player_sprite.climb_movement = 0 # Stop vertical movement

            # Apply vertical velocity based on climb_movement
            self.player_sprite.body.velocity = (
                self.player_sprite.body.velocity.x,
                self.player_sprite.climb_movement * self.player_sprite.max_vertical_climb_speed,
            )
        else:
             self.player_sprite.climb_movement = 0 # Reset climb movement off ladder

        # Update physics engine (handles horizontal movement and gravity when off ladder)
        self.physics_engine.step()

        # ... other updates
```

----------------------------------------

TITLE: Updating Physics Engine with Map Layer (Arcade, Python)
DESCRIPTION: This snippet updates the initialization of the `arcade.PhysicsEnginePlatformer`. Instead of referencing a manually created 'Walls' sprite list, it now uses the 'Platforms' layer loaded from the Tiled map, accessed via `self.scene["Platforms"]`, to define the terrain for player collisions.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_12.rst#_snippet_3

LANGUAGE: python
CODE:
```
self.physics_engine = arcade.PhysicsEnginePlatformer(
    self.player_sprite, walls=self.scene["Platforms"], gravity_constant=GRAVITY
)
```

----------------------------------------

TITLE: Initialising the Buttons
DESCRIPTION: This part of the MenuView's __init__ method creates the individual buttons for the menu options like Resume, New Game, Volume, Options, and Exit.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_8

LANGUAGE: Python
CODE:
```
class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()

        # Create buttons
        self.resume_button = arcade.gui.UIFlatButton(text="Resume", width=200)
        self.new_game_button = arcade.gui.UIFlatButton(text="New Game", width=200)
        self.volume_button = arcade.gui.UIFlatButton(text="Volume", width=200)
        self.options_button = arcade.gui.UIFlatButton(text="Options", width=200)
        self.exit_button = arcade.gui.UIFlatButton(text="Exit", width=200)

        # Add buttons to a layout later
```

----------------------------------------

TITLE: Loading Level-Specific Tilemap | Arcade Python
DESCRIPTION: Modifies the map loading call within the `setup` function to use an f-string. This allows the game to dynamically load a different tilemap file based on the current value of the `self.level` variable.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_14.rst#_snippet_1

LANGUAGE: Python
CODE:
```
# Load our TileMap
self.tile_map = arcade.load_tilemap(f":resources:tiled_maps/map2_level_{self.level}.json", scaling=TILE_SCALING, layer_options=layer_options)
```

----------------------------------------

TITLE: Accessing Textures in Shaders - Python/GLSL
DESCRIPTION: Illustrates how to pass textures to a shader as uniform sampler objects. It creates two textures and associated framebuffers, draws initial content to them, assigns them to texture units, and binds them before rendering the main quad with a shader that samples from both textures.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_inputs/index.rst#_snippet_3

LANGUAGE: Python
CODE:
```
import arcade
import arcade.gl as gl
import numpy as np

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Shader Textures"

vertex_shader_source = """
#version 330 core
in vec2 in_vert;
out vec2 v_uv;

void main() {
    gl_Position = vec4(in_vert, 0.0, 1.0);
    v_uv = (in_vert + 1.0) / 2.0;
}
"""

fragment_shader_source = """
#version 330 core
in vec2 v_uv;
out vec4 out_color;

// --- Declare uniform samplers ---
uniform sampler2D texture1;
uniform sampler2D texture2;

void main() {
    // --- Access textures in shader ---
    vec4 color1 = texture(texture1, v_uv);
    vec4 color2 = texture(texture2, v_uv);

    // Mix the colors based on horizontal position
    out_color = mix(color1, color2, v_uv.x);
}
"""

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

        # --- Create textures/framebuffers ---
        self.texture1 = self.ctx.texture((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.fbo1 = self.ctx.framebuffer(color_attachments=[self.texture1])

        self.texture2 = self.ctx.texture((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.fbo2 = self.ctx.framebuffer(color_attachments=[self.texture2])

        self.program = self.ctx.program(
            vertex_shader=
```

----------------------------------------

TITLE: Initializing MyGame with Cameras - Python Arcade
DESCRIPTION: This snippet shows how to initialize the game class, creating two arcade.Camera instances: one for scrolling game elements and another for static GUI elements. It also initializes a TextLabel for the GUI.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/raycasting/index.rst#_snippet_7

LANGUAGE: Python
CODE:
```
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # ... other initializations ...

        # Cameras
        self.camera_sprites = arcade.Camera(width, height)
        self.camera_gui = arcade.Camera(width, height)

        # GUI text
        self.gui_text = arcade.Text(
            text="Hello GUI!",
            start_x=10,
            start_y=10,
            color=arcade.color.WHITE,
            font_size=20
        )

        # ... rest of __init__ ...

```

----------------------------------------

TITLE: Rendering Mini-Map to Screen (Python)
DESCRIPTION: Demonstrates how to render the game world elements (walls, player) to the mini-map's frame buffer using its dedicated camera within a context manager, clears the buffer before drawing, and finally draws the resulting mini-map texture onto the main screen using the mini-map sprite.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/minimap.rst#_snippet_3

LANGUAGE: Python
CODE:
```
        # --- Draw the mini-map ---
        # Line 134: Activate the mini-map buffer
        with self.minimap_buffer:
            # Line 135: Clear the mini-map buffer
            self.ctx.clear(arcade.color.DARK_BLUE)
            # Line 136: Activate the mini-map camera
            with self.minimap_camera.activate():
                # Line 137: Draw the elements you want on the mini-map
                self.wall_list.draw()
                self.player_list.draw()
        # Line 138: Draw the mini-map sprite onto the main screen
        self.minimap_sprite.draw()
```

----------------------------------------

TITLE: Implementing Sound Demo with Arcade (Python)
DESCRIPTION: This code snippet provides a basic example of how to initialize an arcade window, load a sound file, and play the sound when a specific event occurs, such as a key press or mouse click. It demonstrates the fundamental steps for integrating audio into an arcade application.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sound_demo.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sound Demo"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # Load the sound
        # Replace 'sound.wav' with your actual sound file path
        self.sound = arcade.load_sound(":resources:sounds/hit4.wav")

    def on_draw(self):
        arcade.start_render()
        # Drawing code goes here

    def on_key_press(self, key, modifiers):
        # Play the sound when a key is pressed
        arcade.play_sound(self.sound)

    def on_mouse_press(self, x, y, button, modifiers):
        # Play the sound when the mouse is clicked
        arcade.play_sound(self.sound)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Initializing Arcade Game Attributes (Python)
DESCRIPTION: This code snippet defines the `__init__` method for an `arcade` Window class. Its purpose is to declare essential game attributes (`player_texture`, `player_sprite`, `player_list`, `wall_list`) and initialize them to default "empty" values like `None`. This ensures the attributes exist on the class instance before the `setup` method assigns actual objects to them, which is a Python requirement.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_06.rst#_snippet_0

LANGUAGE: Python
CODE:
```
def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.player_texture = None
        self.player_sprite = None
        self.player_list = None

        self.wall_list = None
```

----------------------------------------

TITLE: Setting UIWidget size_hint Property
DESCRIPTION: Demonstrates how to set the size_hint property of an arcade.gui.UIWidget. This tuple of normalized floats (width_hint, height_hint) provides a suggestion to layout managers on the widget's preferred size relative to its parent, enabling responsive design.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/gui/concepts.rst#_snippet_0

LANGUAGE: python
CODE:
```

    # Prefer to take up all space within the parent
    widget.size_hint = (1.0, 1.0)

    # Prefer to take up the full width & half the height of the parent
    widget.size_hint = (1.0, 0.5)
    # Prefer using 1/10th of the available width & height
    widget.size_hint = (0.1, 0.1)
```

----------------------------------------

TITLE: Bring Sprite to Top of Draw Order - Python
DESCRIPTION: Defines a helper method `pull_to_top` for `MyGame` that takes a sprite and moves it to the end of its `SpriteList`, ensuring it is drawn on top of other sprites.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_8

LANGUAGE: Python
CODE:
```
    def pull_to_top(self, card: arcade.Sprite):
        """ Pull card to top of rendering order (last to draw) """

        # Remove, and append to the end
        self.card_list.remove(card)
        self.card_list.append(card)
```

----------------------------------------

TITLE: Adding a Dropdown - Python/Arcade
DESCRIPTION: This snippet creates an `arcade.gui.UIDropdown` widget. It defines the list of options available in the dropdown and sets a default selected value.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_22

LANGUAGE: Python
CODE:
```
dropdown = arcade.gui.UIDropdown(
    options=["Option 1", "Option 2", "Option 3"],
    default_value="Option 1"
)
```

----------------------------------------

TITLE: Defining Custom Directional Focus with UIFocusable in Python
DESCRIPTION: This snippet demonstrates how to create custom focusable buttons by inheriting from UIFlatButton and UIFocusable. It shows how to explicitly set the neighbor_up, neighbor_down, neighbor_left, and neighbor_right properties for each button to define a custom navigation grid. The buttons are then added to a UIGridLayout within a UIFocusGroup, and the initial focus is set. Requires the arcade.gui and arcade.gui.experimental.focus modules.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/gui/controller_support.rst#_snippet_3

LANGUAGE: python
CODE:
```
from arcade.gui import UIFlatButton, UIGridLayout
from arcade.gui.experimental.focus import UIFocusGroup, UIFocusable

class MyButton(UIFlatButton, UIFocusable):
    def __init__(self, text, width):
        super().__init__(text=text, width=width)


# Create focusable buttons
button1 = MyButton(text="Button 1", width=200)
button2 = MyButton(text="Button 2", width=200)
button3 = MyButton(text="Button 3", width=200)
button4 = MyButton(text="Button 4", width=200)

# Set directional neighbors
button1.neighbor_right = button2
button1.neighbor_down = button3
button2.neighbor_left = button1
button2.neighbor_down = button4
button3.neighbor_up = button1
button3.neighbor_right = button4
button4.neighbor_up = button2
button4.neighbor_left = button3

# Add buttons to a focus group
fg = UIFocusGroup()

grid_layout = UIGridLayout(column_count=2, row_count=2, vertical_spacing=10)
grid_layout.add(button1, col_num=0, row_num=0)
grid_layout.add(button2, col_num=1, row_num=0)
grid_layout.add(button3, col_num=0, row_num=1)
grid_layout.add(button4, col_num=1, row_num=1)

fg.add(grid_layout)

# Detect focusable widgets and set the initial focus
fg.detect_focusable_widgets()
fg.set_focus(button1)
```

----------------------------------------

TITLE: Snap Card to Nearest Pile on Release (Arcade, Python)
DESCRIPTION: Modifies the `on_mouse_release` method to check if a released card is dropped onto a valid pile mat and snaps it into position or returns it to its origin.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_16

LANGUAGE: python
CODE:
```
# Placeholder for code from solitaire_05.py MyGame.on_mouse_release emphasize-lines 9-29
# Example: Logic to check collision with mats and update card position
```

----------------------------------------

TITLE: Declare Scene Variable Python Arcade
DESCRIPTION: Declares a class member variable `self.scene` in the `__init__` method. It is initialized to `None` and will hold the `arcade.Scene` object, replacing individual `SpriteList` variables for better organization.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_11.rst#_snippet_0

LANGUAGE: Python
CODE:
```
self.scene = None
```

----------------------------------------

TITLE: Decorating Widget Event Handler in Arcade Python
DESCRIPTION: This snippet illustrates how to register an additional listener for the `on_event` event type on an `arcade.gui.UIWidget` using the `@UIWidget.event` decorator. This allows developers to add custom event handling logic without overwriting the default `on_event` method of the widget.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/gui/concepts.rst#_snippet_2

LANGUAGE: python
CODE:
```
@UIWidget.event("on_event")
```

----------------------------------------

TITLE: Playing Jump Sound in Arcade on_key_press
DESCRIPTION: Plays the previously loaded jump sound when the player presses the UP or W key, but only if the physics engine confirms the player can currently jump. This snippet is placed inside the keyboard event handler.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_09.rst#_snippet_2

LANGUAGE: python
CODE:
```
# Within on_key_press
if key == arcade.key.UP or key == arcade.key.W:
    if self.physics_engine.can_jump():
        self.player_sprite.change_y = PLAYER_JUMP_SPEED
        arcade.play_sound(self.jump_sound)
```

----------------------------------------

TITLE: Creating a Pymunk Joint in Arcade - Python
DESCRIPTION: This snippet initializes an Arcade window, sets up a Pymunk space with gravity, adds static and dynamic physics bodies, and connects them with a pivot joint for simulation.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/pymunk_joint_builder.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import pymunk

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pymunk Joint Builder Example"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

        # Pymunk space
        self.space = pymunk.Space()
        self.space.gravity = (0, -900) # Standard gravity

        # Add a static ground body
        ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        ground_shape = pymunk.Segment(ground_body, (0, 50), (SCREEN_WIDTH, 50), 5)
        ground_shape.friction = 1.0
        self.space.add(ground_body, ground_shape)

        # Add a dynamic box body
        mass = 1
        moment = pymunk.moment_for_box(mass, (50, 50))
        box_body = pymunk.Body(mass, moment)
        box_body.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        box_shape = pymunk.Poly.create_box(box_body, (50, 50))
        box_shape.friction = 0.8
        self.space.add(box_body, box_shape)

        # Add a pivot joint between the box and the ground
        # Anchor points are relative to the body's center
        joint = pymunk.PivotJoint(ground_body, box_body, (SCREEN_WIDTH // 2, 50))
        self.space.add(joint)

    def on_draw(self):
        arcade.start_render()
        # Drawing code would go here (e.g., drawing the shapes)
        # For this example, we'll just show the background

    def on_update(self, delta_time):
        # Step the physics simulation
        self.space.step(delta_time)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Include Data File During Compilation with Nuitka Bash
DESCRIPTION: This command compiles the Python script and includes a single specified data file (`my_image.png`). The `--include-data-file` flag takes the source path of the file and the target path within the distribution (``.`` refers to the root). This is used to bundle assets like images or sounds.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/compiling_with_nuitka/index.rst#_snippet_2

LANGUAGE: bash
CODE:
```
python -m nuitka 17_views.py --standalone --enable-plugin=numpy --include-data-file=C:/Users/Hunter/Desktop/my_game/my_image.png=.
```

----------------------------------------

TITLE: Using Standard CSS Named Color (Python)
DESCRIPTION: Specify a color using a standard CSS name provided by the arcade.csscolor package.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/api_docs/arcade.csscolor.rst#_snippet_0

LANGUAGE: Python
CODE:
```
arcade.csscolor.RED
```

----------------------------------------

TITLE: Handle Card Drop on Mouse Release (Arcade, Python)
DESCRIPTION: Updates the mouse release logic to handle dropping cards onto piles, including checking if the drop is valid and updating the card's position and pile list.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_24

LANGUAGE: python
CODE:
```
# Placeholder for code from solitaire_07.py MyGame.on_mouse_release lines 1-22 emphasize-lines 16-22
# Example: Logic to check if drop is on the original pile or a new valid pile, then update state.
```

----------------------------------------

TITLE: Passing Ladder List to Player in GameWindow Setup - Python
DESCRIPTION: Assigns the loaded list of ladder sprites to the player sprite instance. This allows the player sprite to check for collisions with ladders and determine if it is currently on a ladder.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/pymunk_platformer/index.rst#_snippet_14

LANGUAGE: Python
CODE:
```
class GameWindow(...):
    def setup(self):
        # ... load player and ladders
        # Pass the ladder list to the player
        self.player_sprite.ladder_list = self.ladder_list
        # ...
```

----------------------------------------

TITLE: Playing arcade.Sound via .play() Method in Python
DESCRIPTION: This snippet demonstrates an alternative way to play a loaded `arcade.Sound` object by calling its built-in `.play()` method. Similar to `arcade.play_sound`, it stores the returned playback object (a pyglet `Player`) for potential later control of this specific sound instance. Requires an `arcade.Sound` object.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/sound.rst#_snippet_4

LANGUAGE: python
CODE:
```
self.coin_playback = COIN_SOUND.play()
```

----------------------------------------

TITLE: Handle Mouse Press for Drag - Python
DESCRIPTION: Implements the `on_mouse_press` method in `MyGame`. It checks if a card was clicked, adds it to the `held_cards` list, saves its original position, and brings it to the top of the drawing order.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_9

LANGUAGE: Python
CODE:
```
    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get list of cards we've clicked on
        cards = arcade.get_sprites_at_point((x, y), self.card_list)

        # Have we clicked on a card?
        if len(cards) > 0:

            # Might be a stack of cards, get the top one
            primary_card = cards[-1]

            # See if the card is face up. If not, flip it.
            if primary_card.is_face_down:
                primary_card.face_up()
            else:
                # All other cards in the stack go face down
                for card in cards:
                    if card != primary_card:
                        card.face_down()

                # Add the card to the list of held cards
                self.held_cards = [primary_card]
                # Save the original position
                self.held_cards_original_position = [self.held_cards[0].position]
                # Pull card to top of rendering order
                self.pull_to_top(self.held_cards[0])

    # ... rest of the class ...
```

----------------------------------------

TITLE: Specifying Color using CSS Name (Python)
DESCRIPTION: Demonstrates how to specify a color using a standard CSS color name imported from the arcade.csscolor module. This method uses predefined constants for common colors.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/api_docs/arcade.uicolor.rst#_snippet_0

LANGUAGE: Python
CODE:
```
arcade.csscolor.RED
```

----------------------------------------

TITLE: Initializing Coin SpriteList in Arcade
DESCRIPTION: Declares a variable `self.coin_list` to hold the coin sprites and initializes it as an `arcade.SpriteList` within the game class setup method, enabling spatial hashing for potentially improved collision performance with static or mostly static sprites.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_08.rst#_snippet_0

LANGUAGE: Python
CODE:
```
# Inside __init__
self.coin_list = None

# Inside setup
self.coin_list = arcade.SpriteList(use_spatial_hash=True)
```

----------------------------------------

TITLE: Initializing Texture Atlas with Existing Textures in Arcade (Python)
DESCRIPTION: Shows how to create a DefaultTextureAtlas with initial textures provided as a list during construction. It also illustrates how to add individual textures to the atlas at any time using the `atlas.add(texture)` method. This helps pre-populate the atlas before rendering starts.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/texture_atlas.rst#_snippet_1

LANGUAGE: python
CODE:
```
# List of arcade.Texture instances
list_of_textures = ...

# Create an atlas with a specific size and initial textures
atlas = DefaultTextureAtlas((256, 256), textures=list_of_textures)

# We can also pre-add textures at any time using:
# (can also be done with the default texture atlas)
atlas.add(texture)
```

----------------------------------------

TITLE: Bundling a Root Resource Directory - Bash
DESCRIPTION: This PyInstaller command is the recommended approach for handling multiple data files and directories by organizing them under a single root directory (`resources`). The `--add-data` flag copies the entire `resources` directory tree into the bundle, preserving its structure.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/bundling_with_pyinstaller/index.rst#_snippet_10

LANGUAGE: bash
CODE:
```
pyinstaller main.py --add-data "resources;resources"
```

----------------------------------------

TITLE: Editing Sub Menu Arguments in Event Listeners - Python/Arcade
DESCRIPTION: This code demonstrates how the sub-menu class is instantiated and added to the UI manager within `on_click` event listeners for different buttons (options and volume). It shows how specific arguments are passed to the sub-menu constructor based on the context, including setting the `layer` parameter to ensure the sub-menu is drawn on top.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_15

LANGUAGE: Python
CODE:
```
def on_options_click(self, event):
    # ... other logic
    self.sub_menu = SubMenu(text="Options", input_text_default="Default Option", layer=1)
    self.manager.add(self.sub_menu)

def on_volume_click(self, event):
    # ... other logic
    self.sub_menu = SubMenu(text="Volume", input_text_default="50", layer=1)
    self.manager.add(self.sub_menu)
```

----------------------------------------

TITLE: Setting Mouse Visibility in View - Arcade Python
DESCRIPTION: Shows how to control mouse cursor visibility when the class is an `arcade.View`. The `set_mouse_visible` method must be accessed through the `self.window` attribute, which references the parent window object.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/views/index.rst#_snippet_5

LANGUAGE: python
CODE:
```
self.window.set_mouse_visible(False)
```

----------------------------------------

TITLE: Stopping Specific Playback with Sound.stop() in Python
DESCRIPTION: This snippet demonstrates an alternative way to stop a specific sound playback instance by calling the `stop()` method on the original `arcade.Sound` object that was played. It requires passing the specific playback object (obtained from `arcade.play_sound` or the `.play()` method) as an argument to the `stop()` method. Requires an `arcade.Sound` object and a playback object.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/sound.rst#_snippet_7

LANGUAGE: python
CODE:
```
self.COIN_SOUND.stop(self.coin_playback_1)
```

----------------------------------------

TITLE: Drawing a Sprite in Arcade (Python)
DESCRIPTION: Renders a sprite onto the screen using the `arcade.draw_sprite` function. This function is typically called within the `on_draw` method of your game view or window to perform the actual drawing during each frame.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_02.rst#_snippet_2

LANGUAGE: Python
CODE:
```
arcade.draw_sprite(self.player_sprite)
```

----------------------------------------

TITLE: Drawing UI on screen
DESCRIPTION: This method is responsible for drawing the UI elements managed by the UIManager onto the screen.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_5

LANGUAGE: Python
CODE:
```
class MainView(arcade.View):
    # ... __init__ and other methods

    def on_draw(self):
        self.clear()
        # Draw UI
        self.manager.draw()
```

----------------------------------------

TITLE: Setting Initial Focus for UIFocusGroup
DESCRIPTION: Provides a concise example of how to explicitly set the initial focus for a UIFocusGroup instance using the set_focus() method. This is necessary to enable controller navigation within the group.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/gui/controller_support.rst#_snippet_2

LANGUAGE: python
CODE:
```
            # Set the initial focus
            self.focus_group.set_focus()
```

----------------------------------------

TITLE: Drawing Coin SpriteList in Arcade
DESCRIPTION: Adds the drawing command for the `coin_list` within the `on_draw` function of the game class to render all coin sprites to the screen each frame.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_08.rst#_snippet_1

LANGUAGE: Python
CODE:
```
self.coin_list.draw()
```

----------------------------------------

TITLE: Loading Data from a Directory - Python
DESCRIPTION: These examples show how to load data files located within a subdirectory (`images/`) using relative paths. This relies on the `os.chdir()` code setting the working directory to the bundle's temporary extraction path, allowing access to files within bundled directories.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/bundling_with_pyinstaller/index.rst#_snippet_6

LANGUAGE: python
CODE:
```
sprite = arcade.Sprite("images/player.jpg")
sprite = arcade.Sprite("images/enemy.jpg")
```

----------------------------------------

TITLE: Simulating Falling Snow with Arcade
DESCRIPTION: This Python script uses the arcade library to create a window and simulate falling snow. It defines a Snowflake class for individual particles and a main game window class to manage and draw them.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/snow.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Falling Snow"

SNOWFLAKE_COUNT = 200
SNOWFLAKE_SIZE = 5
SNOWFLAKE_SPEED = 1

class Snowflake:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, arcade.color.WHITE)

    def update(self):
        self.y -= self.speed
        if self.y < 0:
            self.y = SCREEN_HEIGHT
            self.x = random.randrange(SCREEN_WIDTH)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.snowflakes = []
        for _ in range(SNOWFLAKE_COUNT):
            x = random.randrange(SCREEN_WIDTH)
            y = random.randrange(SCREEN_HEIGHT)
            size = random.randrange(SNOWFLAKE_SIZE // 2, SNOWFLAKE_SIZE)
            speed = random.randrange(SNOWFLAKE_SPEED, SNOWFLAKE_SPEED * 3)
            self.snowflakes.append(Snowflake(x, y, size, speed))

    def on_draw(self):
        arcade.start_render()
        for snowflake in self.snowflakes:
            snowflake.draw()

    def update(self, delta_time):
        for snowflake in self.snowflakes:
            snowflake.update()

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Loading Sounds in Arcade __init__
DESCRIPTION: Loads sound files for coin collection and jumping using `arcade.load_sound`. These sounds are loaded once during game initialization as they are static assets, improving performance by avoiding repeated loading.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_09.rst#_snippet_0

LANGUAGE: python
CODE:
```
self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
```

----------------------------------------

TITLE: Initialize Arcade Window - Python
DESCRIPTION: Sets up a basic Arcade program by opening a blank window and includes placeholder methods for game logic that will be implemented later.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Solitaire"

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game here. Call this to restart the game. """
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Drawing code goes here

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        """ User moves mouse """
        pass

    def on_mouse_release(self, x, y, button):
        """ Called when a user releases a mouse button. """
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Using Four-Byte Tuple (RGBA)
DESCRIPTION: Specifies a color using a tuple of four integers representing the Red, Green, Blue, and Alpha (transparency) components (0-255). Alpha 0 is fully transparent, 255 is fully opaque.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/api_docs/arcade.color.rst#_snippet_3

LANGUAGE: Python
CODE:
```
(255, 0, 0, 255)
```

----------------------------------------

TITLE: Create and Position Card Mat Sprites (Arcade, Python)
DESCRIPTION: Creates the actual mat sprites and positions them on the screen according to the defined constants within the game's setup method.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_14

LANGUAGE: python
CODE:
```
# Placeholder for code from solitaire_04.py MyGame.setup emphasize-lines 11-35
# Example: Create sprites for each mat and set their position
# mat = arcade.Sprite(...)
# mat.center_x = ...
# mat.center_y = ...
# self.mat_list.append(mat)
```

----------------------------------------

TITLE: Conditional Score Reset in Setup | Arcade Python
DESCRIPTION: Replaces the unconditional score reset in the `setup` function with a conditional check. The score is reset to 0 only if `self.reset_score` is True. After the check, `self.reset_score` is set back to True, making score resetting the default for subsequent `setup` calls.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_14.rst#_snippet_5

LANGUAGE: Python
CODE:
```
# Reset the score if we should
if self.reset_score:
    self.score = 0
self.reset_score = True
```

----------------------------------------

TITLE: Creating Arcade GUI Hidden Password Input (Python)
DESCRIPTION: This Python snippet sets up an Arcade window and a UIManager. It creates a UIInputText widget configured to hide the input characters (like a password field) and adds it to a layout box centered on the screen. It also includes a basic button and handles drawing the UI.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/gui_exp_hidden_password.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import arcade.gui

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Hidden Password Example"

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)

        # Create a UIManager to handle the UI
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a vertical box container
        self.v_box = arcade.gui.UIBoxLayout()

        # Create a hidden password input widget
        self.password_input = arcade.gui.UIInputText(
            text="Enter password",
            width=300,
            text_color=(0, 0, 0, 255),
            font_size=14,
            # This is the key part for hidden password
            multiline=False,
            password=True # Assuming a 'password' parameter exists
        )
        self.v_box.add(self.password_input.with_space_around(bottom=20))

        # Create a button to show/hide or submit (optional)
        self.submit_button = arcade.gui.UIFlatButton(text="Submit", width=200)
        self.v_box.add(self.submit_button)

        # Add the v_box to the manager, centered
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box
            )
        )

    def on_draw(self):
        arcade.start_render()
        self.manager.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        # Example: print password on Enter key press
        if symbol == arcade.key.ENTER:
             print(f"Entered password: {self.password_input.text}")


if __name__ == "__main__":
    window = MyWindow()
    arcade.run()

```

----------------------------------------

TITLE: Preventing Score Reset on Level Advance | Arcade Python
DESCRIPTION: Adds a line of code within the level advancement conditional block in `on_update`. Setting `self.reset_score` to False before calling `self.setup()` prevents the score from being reset when the player successfully completes a level and advances to the next.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_14.rst#_snippet_6

LANGUAGE: Python
CODE:
```
# Turn off score reset when advancing level
self.reset_score = False
```

----------------------------------------

TITLE: Handling Ladder Physics and Animation in PlayerSprite - Python
DESCRIPTION: Modifies the pymunk_moved method to adjust the player's physics properties (gravity, damping, vertical velocity) when on a ladder. It also updates the player's texture to display climbing animation if they are on a ladder and not on the ground.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/pymunk_platformer/index.rst#_snippet_11

LANGUAGE: Python
CODE:
```
class PlayerSprite(...):
    def pymunk_moved(self, physics_engine, dx, dy):
        # ... other movement logic
        if self.is_on_ladder:
            self.body.gravity = (0, 0) # Turn off gravity
            self.body.damping = 0.1 # Increase damping
            self.body.velocity = (self.body.velocity.x, max(-self.max_vertical_climb_speed, min(self.max_vertical_climb_speed, self.body.velocity.y))) # Limit vertical speed
        else:
            # Reset physics properties when off ladder
            self.body.gravity = (0, -self.game_window.physics_engine.gravity[1]) # Restore gravity
            self.body.damping = 1.0 # Restore damping
            # Vertical speed is handled by jump/fall physics

        # Update texture for climbing
        if self.is_on_ladder and not self.is_on_ground:
            # Logic to cycle through climbing_textures based on time or movement
            pass # Placeholder for texture update logic
        # ... other texture updates
```

----------------------------------------

TITLE: Adding Multiple Directories to a Resource Handle
DESCRIPTION: Shows how to associate multiple directories with a single resource handle by calling `add_resource_handle` multiple times with the same handle name but different absolute paths. Arcade searches these directories in reverse order of addition.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/resource_handlers.rst#_snippet_4

LANGUAGE: python
CODE:
```
# Adding multiple resources folders to the same resource handler:
arcade.resources.add_resource_handle("my_resources", "/home/users/username/my_game/my_first_res_folder/")
arcade.resources.add_resource_handle("my_resources", "/home/users/username/my_game/my_second_res_folder/")
```

----------------------------------------

TITLE: Initializing Sound Object with Streaming in Python
DESCRIPTION: This snippet shows how to load sound data directly by creating an instance of the `arcade.Sound` class. It demonstrates passing `streaming=True` to enable streaming, which is recommended for long music or ambiance tracks to save memory. Requires the `arcade` library.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/sound.rst#_snippet_1

LANGUAGE: python
CODE:
```
from arcade import Sound  # You can also use arcade.Sound directly

# For music files and ambiance tracks, streaming=True is usually best
streaming_music_file = Sound(":resources:music/1918.mp3", streaming=True)
```

----------------------------------------

TITLE: Initialize Card Pile Tracking Lists (Arcade, Python)
DESCRIPTION: Adds an attribute to the `MyGame` class to store lists representing the state and contents of each card pile.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_19

LANGUAGE: python
CODE:
```
# Placeholder for code from solitaire_07.py MyGame.__init__ lines 19-20
# Example: self.piles = None
```

----------------------------------------

TITLE: Adding Custom Handle with pathlib.Path.resolve()
DESCRIPTION: Demonstrates adding a custom resource handle by using `pathlib.Path` to resolve a relative path (`assets/my_res_folder`) into the required absolute path before passing it to `add_resource_handle`. This is useful for paths relative to your project directory.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/resource_handlers.rst#_snippet_3

LANGUAGE: python
CODE:
```
from pathlib import Path
...
arcade.resources.add_resource_handle("my_resources", Path("assets/my_res_folder").resolve())
```

----------------------------------------

TITLE: Control Music Playback in Arcade (Python)
DESCRIPTION: This Python code snippet demonstrates how to implement music control functionality in an arcade application. It uses the `arcade.Sound` class to load and stream music files, providing methods for playing, pausing, stopping, and adjusting the volume. It also includes logic to switch between multiple music tracks and handle key presses for user interaction.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/music_control_demo.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import os

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Music Control Demo"

class MusicControlView(arcade.View):
    def __init__(self):
        super().__init__()
        self.music = None
        self.current_song_index = 0
        self.music_list = []
        self.volume = 0.5

        # Load music files (assuming they are in a 'music' subdirectory relative to the script)
        music_folder = os.path.join(os.path.dirname(__file__), "music")
        if os.path.exists(music_folder):
            for root, dirs, files in os.walk(music_folder):
                for file in files:
                    if file.lower().endswith((".mp3", ".wav", ".ogg")):
                        self.music_list.append(os.path.join(root, file))

        if self.music_list:
            self.play_song()
        else:
            print("No music files found in the 'music' subdirectory.")

    def play_song(self):
        if self.music:
            self.music.stop()

        if not self.music_list:
            print("No music files available to play.")
            return

        song_path = self.music_list[self.current_song_index]
        print(f"Playing: {os.path.basename(song_path)}")
        try:
            self.music = arcade.Sound(song_path, streaming=True)
            self.music.play(volume=self.volume)
        except Exception as e:
            print(f"Error loading or playing {os.path.basename(song_path)}: {e}")
            self.music = None # Ensure music is None if loading fails

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            if self.music:
                if self.music.is_playing():
                    self.music.pause()
                    print("Music paused")
                else:
                    self.music.play(volume=self.volume)
                    print("Music resumed")
        elif key == arcade.key.RIGHT:
            if self.music_list:
                self.current_song_index = (self.current_song_index + 1) % len(self.music_list)
                self.play_song()
        elif key == arcade.key.LEFT:
            if self.music_list:
                self.current_song_index = (self.current_song_index - 1 + len(self.music_list)) % len(self.music_list)
                self.play_song()
        elif key == arcade.key.UP:
            self.volume = min(1.0, self.volume + 0.1)
            if self.music:
                self.music.set_volume(self.volume)
            print(f"Volume: {self.volume:.1f}")
        elif key == arcade.key.DOWN:
            self.volume = max(0.0, self.volume - 0.1)
            if self.music:
                self.music.set_volume(self.volume)
            print(f"Volume: {self.volume:.1f}")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Press SPACE to pause/resume", 10, 50, arcade.color.WHITE, 18)
        arcade.draw_text("Press LEFT/RIGHT to change song", 10, 30, arcade.color.WHITE, 18)
        arcade.draw_text("Press UP/DOWN to change volume", 10, 10, arcade.color.WHITE, 18)
        if self.music_list and self.current_song_index < len(self.music_list):
             arcade.draw_text(f"Now Playing: {os.path.basename(self.music_list[self.current_song_index])}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 18)
        elif not self.music_list:
             arcade.draw_text("No music files found.", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 18)

    def on_update(self, delta_time):
        # Check if music has finished playing
        if self.music and not self.music.is_playing() and self.music.get_time() > 0:
             print("Song finished")
             if self.music_list:
                 self.current_song_index = (self.current_song_index + 1) % len(self.music_list)
                 self.play_song()


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = MusicControlView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Handle Mouse Motion for Drag - Python
DESCRIPTION: Implements the `on_mouse_motion` method in `MyGame`. If any cards are currently being held (`held_cards` is not empty), it updates their position to follow the mouse cursor.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_10

LANGUAGE: Python
CODE:
```
    def on_mouse_motion(self, x, y, dx, dy):
        """ User moves mouse """

        # If we are holding cards, move them with the mouse
        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy

    # ... rest of the class ...
```

----------------------------------------

TITLE: Drawing Text with Batches (Python)
DESCRIPTION: This snippet demonstrates the recommended way to draw multiple `arcade.Text` objects efficiently by associating them with a `pyglet.graphics.Batch`. Text objects are created and linked to the batch, and the batch's draw method handles rendering them all in one go, significantly reducing drawing overhead compared to drawing each text object individually. Requires the 'arcade' library.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/drawing_text_objects_batch.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import pyglet.graphics

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Drawing Text with Batches"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

        # Create a Batch object
        self.batch = pyglet.graphics.Batch()

        # Create multiple text objects, adding them to the batch
        # Text objects added to a batch are automatically drawn when batch.draw() is called
        self.text_objects = []
        for i in range(10):
            text = arcade.Text(
                f"Hello Batch! {i}",
                x=100,
                y=SCREEN_HEIGHT - 50 - i * 30,
                color=arcade.color.WHITE,
                font_size=20,
                anchor_x="left",
                anchor_y="top",
                batch=self.batch # IMPORTANT: Add text to the batch
            )
            self.text_objects.append(text)

    def on_draw(self):
        arcade.start_render()
        # Draw the batch containing all text objects
        self.batch.draw()

    def update(self, delta_time):
        pass

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Creating a Resizable Arcade Window (Python)
DESCRIPTION: This code snippet demonstrates how to create a basic window using the arcade library that can be resized by the user. It sets up the window, defines drawing logic, and includes an event handler for window resizing.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/resizable_window.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Resizable Window Example"

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to start the drawing process
        arcade.start_render()

        # Draw the text
        arcade.draw_text(
            "Window is resizable!",
            self.width / 2,
            self.height / 2,
            arcade.color.BLACK,
            font_size=30,
            anchor_x="center",
            anchor_y="center",
        )

    def on_resize(self, width, height):
        """
        Called when the window is resized.
        """
        # Update the viewport to match the new window size
        super().on_resize(width, height)
        print(f"Window resized to: {width}x{height}")


def main():
    """
    Main function
    """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Removing Manual Sprite Creation (Arcade, Python)
DESCRIPTION: This code block, previously used to manually create and add 'Walls' and 'Coins' sprites to the scene, is marked for removal. This functionality will be replaced by loading sprites and objects directly from a Tiled map file.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_12.rst#_snippet_0

LANGUAGE: python
CODE:
```
self.scene.add_sprite_list("Walls", use_spatial_hash=True)
self.scene.add_sprite_list("Coins", use_spatial_hash=True)

for x in range(0, 1250, 64):
    wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=TILE_SCALING)
    wall.center_x = x
    wall.center_y = 32
    self.scene.add_sprite("Walls", wall)

coordinate_list = [[512, 96], [256, 96], [768, 96]]

for coordinate in coordinate_list:
    wall = arcade.Sprite(
        ":resources:images/tiles/boxCrate_double.png", scale=TILE_SCALING
    )
    wall.position = coordinate
    self.scene.add_sprite("Walls", wall)

for x in range(128, 1250, 256):
    coin = arcade.Sprite(":resources:images/items/coinGold.png", scale=COIN_SCALING)
    coin.center_x = x
    coin.center_y = 96
    self.scene.add_sprite("Coins", coin)
```

----------------------------------------

TITLE: Calculating Map End Boundary | Arcade Python
DESCRIPTION: Calculates the rightmost pixel coordinate of the currently loaded map. This is done by multiplying the map's width (in tiles) by the tile width and then by the tile scaling factor. The result is stored in `self.end_of_map`.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_14.rst#_snippet_2

LANGUAGE: Python
CODE:
```
# Calculate the right edge of the map in pixels
self.end_of_map = (self.tile_map.width * self.tile_map.tile_width) * self.tile_map.scaling
```

----------------------------------------

TITLE: Implement Random Enemy Shooting in Arcade (Python)
DESCRIPTION: This Python code snippet demonstrates how to make enemy sprites randomly shoot bullets in the arcade library. It typically involves checking a random chance for each enemy during the game's update cycle and creating a new bullet sprite if the chance succeeds. This approach avoids tracking timers for each enemy.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_bullets_random.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Random Shooting Example"

PLAYER_SPEED = 5
ENEMY_SPEED = 2
BULLET_SPEED = 7

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.player_list = None
        self.enemy_list = None
        self.player_bullet_list = None
        self.enemy_bullet_list = None

        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()

        # Create player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create enemies
        for i in range(5):
            enemy = arcade.Sprite(":resources:images/animated_characters/robot/robot_idle.png", 0.5)
            enemy.center_x = random.randrange(50, SCREEN_WIDTH - 50)
            enemy.center_y = random.randrange(SCREEN_HEIGHT / 2, SCREEN_HEIGHT - 50)
            self.enemy_list.append(enemy)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.enemy_list.draw()
        self.player_bullet_list.draw()
        self.enemy_bullet_list.draw()

    def on_update(self, delta_time):
        self.player_bullet_list.update()
        self.enemy_bullet_list.update()

        # --- Random Enemy Shooting Logic (Simulated lines 66-81) ---
        for enemy in self.enemy_list:
            # Randomly decide if the enemy shoots
            if random.random() < 0.005: # Adjust probability as needed
                # Create a bullet
                bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", 0.5)

                # Position the bullet at the enemy's location
                bullet.center_x = enemy.center_x
                bullet.center_y = enemy.center_y

                # Calculate bullet direction towards player (simplified)
                # In a real game, you'd calculate angle/vector
                bullet.change_y = -BULLET_SPEED # Shoot downwards for simplicity

                # Add the bullet to the enemy bullet list
                self.enemy_bullet_list.append(bullet)
        # --- End of Simulated lines 66-81 ---

        # Remove bullets that go off-screen
        for bullet in self.player_bullet_list:
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

        for bullet in self.enemy_bullet_list:
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_SPEED
        elif key == arcade.key.SPACE:
            # Player shoots
            bullet = arcade.Sprite(":resources:images/space_shooter/laserRed01.png", 0.5)
            bullet.center_x = self.player_sprite.center_x
            bullet.center_y = self.player_sprite.center_y + 20
            bullet.change_y = BULLET_SPEED
            self.player_bullet_list.append(bullet)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Creating Custom Stylable Widget with State Logic in Python
DESCRIPTION: This snippet demonstrates how to build a custom stylable widget MyColorBox by inheriting from UIStyledWidget. It defines a nested UIStyle class with specific attributes (like color), sets a DEFAULT_STYLE, and implements the get_current_state method to return the widget's current state based on properties like disabled, pressed, and hovered. The do_render method then retrieves and uses the style corresponding to the current state.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/gui/style.rst#_snippet_2

LANGUAGE: Python
CODE:
```
class MyColorBox(UIStyledWidget, UIInteractiveWidget, UIWidget):
    """
    A colored box, which changes on mouse interaction
    """

    # create the style class, which will be used to define style for any widget state
    @dataclass
    class UIStyle(UIStyleBase):
        color: RGBA255 = arcade.color.GREEN

    DEFAULT_STYLE = {
        "normal": UIStyle(),
        "hover": UIStyle(color=arcade.color.YELLOW),
        "press": UIStyle(color=arcade.color.RED),
        "disabled": UIStyle(color=arcade.color.GRAY)
    }

    def get_current_state(self) -> str:
        """Returns the current state of the widget i.e.disabled, press, hover or normal."""
        if self.disabled:
            return "disabled"
        elif self.pressed:
            return "press"
        elif self.hovered:
            return "hover"
        else:
            return "normal"

    def do_render(self, surface: Surface):
        self.prepare_render(surface)

        # get current style
        style: MyColorBox.UIStyle = self.get_current_style()

        # Get color from current style, it is a good habit to be
        # bullet proven for missing values in case a dict is provided instead of a UIStyle
        color = style.get("color", MyColorBox.UIStyle.bg)

        # render
        if color: # support for not setting a color at all
            surface.clear(bg_color)
```

----------------------------------------

TITLE: Configuring Tiled Map Layers for Spatial Hashing - Python
DESCRIPTION: This code shows how to define layer options when loading a Tiled map to enable spatial hashing specifically for certain layers containing static sprites like ground or platforms. This improves collision performance for those layers.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/performance_tips.rst#_snippet_1

LANGUAGE: python
CODE:
```
layer_options = {
    "ground": {
        "use_spatial_hash": True
    },
    "non_moving_platforms": {
        "use_spatial_hash": True
    }
}
```

----------------------------------------

TITLE: Specifying Color using RGBA Tuple (Python)
DESCRIPTION: Explains how to specify a color using a four-byte tuple including Red, Green, Blue, and Alpha (transparency) components. Alpha ranges from 0 (fully transparent) to 255 (fully opaque).
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/api_docs/arcade.uicolor.rst#_snippet_3

LANGUAGE: Python
CODE:
```
(255, 0, 0, 255)
```

----------------------------------------

TITLE: Passing Data with Uniforms - Python/GLSL
DESCRIPTION: Shows how to pass data from Python to a shader using uniforms. It defines a 'time' uniform in the GLSL fragment shader and updates its value from the Python `on_update` method, causing the shader's output (alpha) to change over time.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_inputs/index.rst#_snippet_2

LANGUAGE: Python
CODE:
```
import arcade
import arcade.gl as gl

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Shader Uniforms"

vertex_shader_source = """
#version 330 core
in vec2 in_vert;
out vec2 v_uv;

void main() {
    gl_Position = vec4(in_vert, 0.0, 1.0);
    v_uv = (in_vert + 1.0) / 2.0;
}
"""

fragment_shader_source = """
#version 330 core
in vec2 v_uv;
out vec4 out_color;

// --- Declare a uniform ---
uniform float time;

void main() {
    // Use the uniform 'time' to vary color or alpha
    float alpha = abs(sin(time + v_uv.x * 5.0));
    out_color = vec4(1.0, 0.5, 0.0, alpha); // Orange color, alpha varies with time and position
}
"""

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

        self.program = self.ctx.program(
            vertex_shader=vertex_shader_source,
            fragment_shader=fragment_shader_source,
        )

        vertices = [-1.0, -1.0, 1.0, -1.0, -1.0, 1.0, 1.0, 1.0]
        indices = [0, 1, 2, 1, 3, 2]
        self.vbo = self.ctx.buffer(data=bytes(arcade.utils.flatten_list(vertices)))
        self.ibo = self.ctx.buffer(data=bytes(indices))
        self.quad_fs = self.ctx.geometry([
            gl.BufferDescription(self.vbo, '2f', ['in_vert'])
        ], index_buffer=self.ibo)

        # --- Get uniform location ---
        # The uniform is accessed directly as an attribute of the program
        # self.program['time'] # This is how you'd access it

        # --- Set initial uniform value ---
        self.program['time'] = 0.0 # Set initial value

        self.total_time = 0.0

    def on_update(self, delta_time):
        self.total_time += delta_time
        # --- Update uniform value ---
        self.program['time'] = self.total_time

    def on_draw(self):
        arcade.start_render()
        self.quad_fs.render(self.program)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Making a Fake Window.
DESCRIPTION: This defines a class (SubMenu) that acts like a modal window by using UIMouseFilterMixin to block events from reaching elements behind it.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_12

LANGUAGE: Python
CODE:
```
class SubMenu(arcade.gui.UIMouseFilterMixin, arcade.gui.UILayout):
    def __init__(self, center_x, center_y, width, height, **kwargs):
        super().__init__(center_x=center_x, center_y=center_y, width=width, height=height, **kwargs)
        # Add UI elements for the sub-menu here
```

----------------------------------------

TITLE: Rendering Content Directly Into Texture Atlas Region in Arcade (Python)
DESCRIPTION: Demonstrates how to use a context manager (`with atlas.render_into(texture)`) to acquire a framebuffer for the texture's allocated area in the atlas. Inside the `with` block, standard Arcade drawing commands (like `draw_rectangle_filled`) can be used to render directly onto the texture's data within the atlas, providing a highly dynamic way to update sprite textures.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/texture_atlas.rst#_snippet_4

LANGUAGE: python
CODE:
```
# -- Rendering ---
# Let's render something into our texture directly.
# All operations will only affect the allocated portion of the atlas for texture.
# We are given a framebuffer instance representing this area
with spritelist.atlas.render_into(texture) as framebuffer:
    # Clear the allocated region in the atlas (if you need it)
    framebuffer.clear()
    # From here on we can draw using any Arcade draw functionality
    arcade.draw_rectangle_filled(128, 128, 160, 160, arcade.color.WHITE, rotation)
```

----------------------------------------

TITLE: Shader: Using Custom Uniforms for Position and Color - GLSL
DESCRIPTION: Incorporates custom uniform variables (`center_x`, `center_y`, `glow_color`) sent from the Python application. It adjusts the calculation of the distance and the final color based on these incoming values, allowing dynamic control of the glow's position and appearance.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_toy_glow/index.rst#_snippet_10

LANGUAGE: glsl
CODE:
```
#version 330

uniform vec3 iResolution;
out vec4 fracColor;

// Custom uniforms
uniform float center_x;
uniform float center_y;
uniform vec3 glow_color;

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    // Normalized pixel coordinates (from -0.5 to 0.5)
    vec2 uv = fragCoord/iResolution.xy - 0.5;

    // Adjust for aspect ratio
    uv.x *= iResolution.x / iResolution.y;

    // Adjust UV based on custom center position (normalized 0..1)
    uv.x -= (center_x - 0.5);
    uv.y -= (center_y - 0.5);

    // Calculate the distance from center
    float d = length(uv);

    // Calculate color based on distance
    // Inverse distance, scaled down.
    // Adjust exponent (1.0=same, 0.5=slower, 1.5=faster fade)
    float fade_exponent = 1.5;
    vec3 col = glow_color * pow(1.0 / (d * 2.0), fade_exponent);

    // Tone mapping
    col = col / (col + 1.0);

    fragColor = vec4(col,1.0);
}
```

----------------------------------------

TITLE: Using Three-Byte Tuple (RGB)
DESCRIPTION: Specifies a color using a tuple of three integers representing the Red, Green, and Blue components (0-255).
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/api_docs/arcade.color.rst#_snippet_2

LANGUAGE: Python
CODE:
```
(255, 0, 0)
```

----------------------------------------

TITLE: Specifying Color using RGB Tuple (Python)
DESCRIPTION: Illustrates specifying a color using a three-byte tuple representing Red, Green, and Blue components. Each component is an integer between 0 and 255.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/api_docs/arcade.uicolor.rst#_snippet_2

LANGUAGE: Python
CODE:
```
(255, 0, 0)
```

----------------------------------------

TITLE: Adding a Toggle Button - Python/Arcade
DESCRIPTION: This snippet creates a `arcade.gui.UITextureToggle` widget, which switches between two textures when clicked. It also creates a label and arranges both horizontally using a `UIBoxLayout` to pair the toggle with its description.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_20

LANGUAGE: Python
CODE:
```
toggle_label = arcade.gui.UILabel(text="Toggle Feature:")
toggle_button = arcade.gui.UITextureToggle(
    on_texture=arcade.load_texture(":resources:gui_basic_assets/toggle/switch_green_on.png"),
    off_texture=arcade.load_texture(":resources:gui_basic_assets/toggle/switch_red_off.png"),
    value=True # or some initial value
)
toggle_hbox = arcade.gui.UIBoxLayout(vertical=False)
toggle_hbox.add(toggle_label)
toggle_hbox.add(toggle_button)
```

----------------------------------------

TITLE: Adjusting Sprite List Drawing Order in Arcade Python
DESCRIPTION: This code snippet, typically placed in the `setup` function before creating the player sprite, modifies the drawing order of sprite lists within the scene. It ensures that the 'Foreground' sprite list is drawn *after* the 'Player' sprite list, making foreground objects appear in front of the player.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_13.rst#_snippet_3

LANGUAGE: Python
CODE:
```
self.scene.add_sprite_list_after("Player", "Foreground")
```

----------------------------------------

TITLE: Setting up the Grid
DESCRIPTION: This snippet shows how to arrange the created buttons within a UIGridLayout for an organized display in the menu.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_9

LANGUAGE: Python
CODE:
```
class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()

        self.resume_button = arcade.gui.UIFlatButton(text="Resume", width=200)
        self.new_game_button = arcade.gui.UIFlatButton(text="New Game", width=200)
        self.volume_button = arcade.gui.UIFlatButton(text="Volume", width=200)
        self.options_button = arcade.gui.UIFlatButton(text="Options", width=200)
        self.exit_button = arcade.gui.UIFlatButton(text="Exit", width=200)

        # Create a grid layout
        button_grid = arcade.gui.UIGridLayout(
            column_count=1,
            row_count=5,
            vertical_spacing=20,
            align_horizontal="center",
            align_vertical="middle"
        )

        # Add buttons to the grid
        button_grid.add(self.resume_button)
        button_grid.add(self.new_game_button)
        button_grid.add(self.volume_button)
        button_grid.add(self.options_button)
        button_grid.add(self.exit_button)

        # Add the grid to the manager using an anchor layout
        self.manager.add(
            arcade.gui.UIAnchorLayout().add(
                button_grid,
                anchor_x="center_x",
                anchor_y="center_y"
            )
        )

        # Set up button click handlers later
```

----------------------------------------

TITLE: Using a Custom Resource Handle
DESCRIPTION: Shows how to load a texture using a custom resource handle (`:my_resources:`) that was previously added. Arcade searches the directories associated with the handle to find the specified file.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/resource_handlers.rst#_snippet_2

LANGUAGE: python
CODE:
```
self.texture = arcade.load_texture(":my_resources:images/characters/my_character.png")
```

----------------------------------------

TITLE: Define Player Movement Speed - Python Arcade
DESCRIPTION: Sets a constant value representing the number of pixels the player character moves per game update cycle. This is a fundamental setting for controlling player movement speed.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_04.rst#_snippet_0

LANGUAGE: Python
CODE:
```
PLAYER_MOVEMENT_SPEED = 5
```

----------------------------------------

TITLE: Change Coins with Sprites in Python
DESCRIPTION: This snippet shows a basic structure for an arcade program that involves sprites representing coins. It would typically include setting up the game window, loading coin sprites, and implementing logic to collect or change the state of coins, potentially updating a score display.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_change_coins.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Change Coins Example"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        self.coin_list = None
        self.player_sprite = None
        self.score = 0

    def setup(self):
        self.coin_list = arcade.SpriteList()

        # Create coins
        for i in range(10):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", 0.5)
            coin.center_x = (i * 70) + 50
            coin.center_y = 500
            self.coin_list.append(coin)

        # Create player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 100

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.player_sprite.draw()

        # Draw score
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        # Check for collisions with coins
        coins_hit = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coins_hit:
            coin.remove_from_sprite_lists()
            self.score += 1

    def on_key_press(self, key, modifiers):
        # Basic movement for demonstration
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Loading and Running ShaderToy Shader - Python
DESCRIPTION: This program loads a GLSL shader source from a file and initializes a `Shadertoy` object to display it. It extends the basic window setup by adding shader rendering.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_toy_glow/index.rst#_snippet_1

LANGUAGE: python
CODE:
```
import arcade
from arcade.experimental.shadertoy import Shadertoy

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
SCREEN_TITLE = "ShaderToy demo 2"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Load the shader
        file_name = "circle_1.glsl"
        shader_source = open(file_name).read()
        self.shadertoy = Shadertoy(size=self.get_size(),
                                   main_source=shader_source)

    def on_draw(self):
        self.clear()
        self.shadertoy.render()


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Updating Texture Image Data in Arcade Atlas (Python)
DESCRIPTION: Explains how to update the pixel data of a texture that is already in an atlas. It involves modifying the `image` attribute of the `arcade.Texture` instance (which must maintain the same size) and then calling `atlas.update_texture_image(texture)` to write the modified image data back into the atlas's allocated region for that texture.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/texture_atlas.rst#_snippet_2

LANGUAGE: python
CODE:
```
# Change the internal image in a texture
texture.image  # <- Modify or crate a new image with the same size

# Write the new image data to the atlas
atlas.update_texture_image(texture)
```

----------------------------------------

TITLE: Creating Custom Texture Atlas and SpriteList in Arcade (Python)
DESCRIPTION: Demonstrates how to instantiate a custom DefaultTextureAtlas with a specified size (256x256) and associate it with a SpriteList by passing the atlas instance to the `atlas` argument during SpriteList initialization. This allows the sprite list to use a dedicated atlas instead of the default global one.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/texture_atlas.rst#_snippet_0

LANGUAGE: python
CODE:
```
# Create an empty 256 x 256 texture atlas
my_atlas = DefaultTextureAtlas((256, 256))
spritelist = SpriteList(atlas=my_atlas)
```

----------------------------------------

TITLE: Playing Multiple Instances of a Sound in Python
DESCRIPTION: This snippet illustrates how a single loaded `arcade.Sound` object can be played multiple times concurrently, either via `arcade.play_sound` or the `.play()` method. Each playback returns a unique playback object, allowing independent control over volume, stopping, etc., for each instance. Requires an `arcade.Sound` object.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/sound.rst#_snippet_5

LANGUAGE: python
CODE:
```
# We can play the same Sound one, two, or many more times at once
self.coin_playback_1 = arcade.play_sound(COIN_SOUND)
self.coin_playback_2 = COIN_SOUND.play()
self.coin_playback_3 = COIN_SOUND.play()
...
```

----------------------------------------

TITLE: Simple Shader Program - Python/GLSL
DESCRIPTION: Demonstrates adding a basic shader to an Arcade program. It includes vertex and fragment shader source code (GLSL) and Python code to compile the shader, create a quad geometry, and render the quad using the shader. The fragment shader varies pixel alpha based on the horizontal coordinate.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_inputs/index.rst#_snippet_1

LANGUAGE: Python
CODE:
```
import arcade
import arcade.gl as gl

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Basic Shader"

# --- Vertex Shader ---
# Passes position to fragment shader
vertex_shader_source = """
#version 330 core
in vec2 in_vert;
out vec2 v_uv;

void main() {
    gl_Position = vec4(in_vert, 0.0, 1.0);
    v_uv = (in_vert + 1.0) / 2.0; // Convert from [-1, 1] to [0, 1]
}
"""

# --- Fragment Shader ---
# Sets color and alpha based on horizontal position
fragment_shader_source = """
#version 330 core
in vec2 v_uv;
out vec4 out_color;

void main() {
    // Vary alpha based on horizontal coordinate (v_uv.x)
    out_color = vec4(1.0, 0.0, 0.0, v_uv.x); // Red color, alpha varies
}
"""

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

        # --- Create Shader Program ---
        self.program = self.ctx.program(
            vertex_shader=vertex_shader_source,
            fragment_shader=fragment_shader_source,
        )

        # --- Create Quad VBO and VAO ---
        # A simple quad covering the screen [-1, -1] to [1, 1]
        vertices = [-1.0, -1.0, 1.0, -1.0, -1.0, 1.0, 1.0, 1.0]
        indices = [0, 1, 2, 1, 3, 2]

        self.vbo = self.ctx.buffer(data=bytes(arcade.utils.flatten_list(vertices)))
        self.ibo = self.ctx.buffer(data=bytes(indices))

        self.quad_fs = self.ctx.geometry([
            gl.BufferDescription(self.vbo, '2f', ['in_vert'])
        ], index_buffer=self.ibo)


    def on_draw(self):
        arcade.start_render()
        # --- Draw the quad with the shader ---
        self.quad_fs.render(self.program)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Adding Toggle Button to Layout - Python/Arcade
DESCRIPTION: This code adds the horizontal box containing the toggle button and its label to the main vertical box layout (`self.v_box`), placing it after the input field.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_21

LANGUAGE: Python
CODE:
```
self.v_box.add(toggle_hbox)
```

----------------------------------------

TITLE: Adding Input Field to Layout - Python/Arcade
DESCRIPTION: This code adds the created input field widget to the vertical box layout (`self.v_box`), placing it below the previously added title label.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_19

LANGUAGE: Python
CODE:
```
self.v_box.add(input_text)
```

----------------------------------------

TITLE: Creating Custom Arcade Texture from PIL Image (Python)
DESCRIPTION: This snippet demonstrates how to create an `arcade.Texture` directly from a PIL/Pillow `Image` object, rather than loading from a file. It shows creating a PIL image (e.g., from raw data) and then passing it, along with a unique name and a specified hit box algorithm, to the `arcade.Texture` constructor. This method allows for creating textures programmatically or integrating with other image processing libraries.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/textures.rst#_snippet_1

LANGUAGE: python
CODE:
```
# Create a image from raw pixel data from some source
image = PIL.Image.frombuffer(raw_data)

# NOTE: Also make sure you use a sane hit_box_algorithm
texture = arcade.Texture("unique_name", image, hit_box_algorithm=...)
```

----------------------------------------

TITLE: Defining Particle Burst Dataclass Python
DESCRIPTION: Defines a dataclass `Burst` to hold the data associated with a single particle explosion. It includes a `VertexArray` (`vao`) for storing particle data on the GPU and a `time` attribute (added later) to track the burst's creation time.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/gpu_particle_burst/index.rst#_snippet_2

LANGUAGE: Python
CODE:
```
@dataclass
class Burst:
    vao: arcade.gl.VertexArray
    time: float = field(default=0.0)
```

----------------------------------------

TITLE: Drawing Ladders in GameWindow On Draw - Python
DESCRIPTION: Draws the sprite list containing all the ladder sprites onto the screen as part of the game's rendering process.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/pymunk_platformer/index.rst#_snippet_18

LANGUAGE: Python
CODE:
```
class GameWindow(...):
    def on_draw(self):
        # ... other drawing
        # Draw the ladders
        self.ladder_list.draw()
        # ...
```

----------------------------------------

TITLE: Create & Initialize Shader Variables (Python)
DESCRIPTION: Initializes instance variables within the `MyGame` class constructor (`__init__`) to hold the `Shadertoy` object and four `Frame Buffer Objects` (FBOs) representing the shader channels. These variables are placeholders that will be assigned actual objects later.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/raycasting/index.rst#_snippet_1

LANGUAGE: python
CODE:
```
self.shadertoy = None
self.channel0 = None
self.channel1 = None
self.channel2 = None
self.channel3 = None
```

----------------------------------------

TITLE: Initializing PlayerSprite for Ladders - Python
DESCRIPTION: Adds attributes to the PlayerSprite class constructor to manage ladder interaction, including a list to hold ladder sprites, textures for climbing animation, a variable for vertical climbing movement, and a boolean flag to track if the player is currently on a ladder.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/pymunk_platformer/index.rst#_snippet_10

LANGUAGE: Python
CODE:
```
class PlayerSprite(...):
    def __init__(self, ...):
        # ... other initializations
        self.ladder_list = None # Reference to the list of ladder sprites
        self.climbing_textures = [] # Textures for climbing animation
        self.climb_movement = 0 # Keep track of vertical movement input
        self.is_on_ladder = False # Boolean to track if on a ladder
        # ...
```

----------------------------------------

TITLE: Demonstrating Arcade Texture Caching (Python)
DESCRIPTION: This snippet illustrates Arcade's texture caching behavior. When creating sprites with the same texture name and parameters, the texture is loaded and cached only once. Changing parameters like `flipped_vertically` forces a new load and cache entry because it requires transformed pixel data for accurate hit box detection, but subsequent calls with the same parameters will then be cached.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/textures.rst#_snippet_0

LANGUAGE: python
CODE:
```
# The texture will only be loaded during the first sprite creation
tex_name = "path/to/sprite.png"
sprite_1 = arcade.Sprite(tex_name)
sprite_2 = arcade.Sprite(tex_name)
sprite_3 = arcade.Sprite(tex_name)
# Will be loaded and cached because we need fresh pixel data for hit box detection
sprite_4 = arcade.Sprite(tex_name, flipped_vertically=True)
# Fetched from cache
sprite_5 = arcade.Sprite(tex_name, flipped_vertically=True)
```

----------------------------------------

TITLE: Defining Instruction View Class - Arcade Python
DESCRIPTION: Defines a new class specifically for handling an instruction screen, inheriting from `arcade.View`. This class will contain the necessary logic for drawing the instruction display and responding to input to transition to the game.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/views/index.rst#_snippet_6

LANGUAGE: python
CODE:
```
class InstructionView(arcade.View):
```

----------------------------------------

TITLE: Getting Connected Controllers - Arcade Python
DESCRIPTION: Retrieves a list of connected game controllers using `arcade.get_controllers()`. If controllers are found, it opens the first one and stores it in `self.controller`. Otherwise, it prints a message and sets `self.controller` to `None`.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/controller.rst#_snippet_0

LANGUAGE: Python
CODE:
```
      controllers = arcade.get_controllers()
      if controllers:
          self.controller = controllers[0]
          self.controller.open()
      else:
          print("There are no controllers.")
          self.controller = None
```

----------------------------------------

TITLE: Managing GUI Focus with UIFocusGroup
DESCRIPTION: Shows how to use UIFocusGroup to group interactive GUI elements (like buttons) within a ControllerView. This allows controller navigation by cycling focus among the elements in the group. It also demonstrates adding the group to the UI manager and detecting/setting initial focus.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/gui/controller_support.rst#_snippet_1

LANGUAGE: python
CODE:
```
from arcade.experimental.controller_window import ControllerView, ControllerWindow
from arcade.gui import UIFlatButton, UIBoxLayout, UIView
from arcade.gui.experimental.focus import UIFocusGroup


class MyControllerView(ControllerView, UIView):
    def __init__(self):
        super().__init__()

        # Create buttons and add them to the focus group
        fg = UIFocusGroup()
        self.ui.add(fg)

        box = UIBoxLayout()
        fg.add(box)

        button1 = UIFlatButton(text="Button 1", width=200)
        button2 = UIFlatButton(text="Button 2", width=200)

        box.add(button1)
        box.add(button2)

        # initialize the focus group, detect focusable widgets and set the initial focus
        fg.detect_focusable_widgets()
        fg.set_focus()


if __name__ == "__main__":
    window = ControllerWindow(title="Controller Support Example")
    view = MyControllerView()
    window.show_view(view)
    window.run()
```

----------------------------------------

TITLE: Create the Shader and FBOs (Python)
DESCRIPTION: Defines a method `load_shader` that creates the `Shadertoy` object by loading a GLSL program from "step_01.glsl". It also initializes `channel0` and `channel1` as new frame buffer objects (FBOs) associated with the shader, which will be used to pass data to the shader.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/raycasting/index.rst#_snippet_2

LANGUAGE: python
CODE:
```
def load_shader(self):
    self.shadertoy = arcade.experimental.Shadertoy.from_file("step_01.glsl")
    self.channel0 = self.shadertoy.new_buffer()
    self.channel1 = self.shadertoy.new_buffer()
```

----------------------------------------

TITLE: GLSL Shader with Glowing Particles
DESCRIPTION: This GLSL shader enhances the particle appearance by adding a glow effect. The alpha value is now calculated based on the distance from the particle's center, creating a soft, fading edge, combined with the time-based fade-out.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_toy_particles/index.rst#_snippet_4

LANGUAGE: GLSL
CODE:
```
#version 330 core

out vec4 FragColor;
in vec2 TexCoords;

uniform vec2 iResolution;
uniform float iTime;

// Pseudo-random number generator 1
float random(vec2 st) {
    return fract(sin(dot(st.xy, vec2(12.9898,78.233))) * 43758.5453123);
}

// Pseudo-random number generator 2
float random2(vec2 st) {
    return fract(sin(dot(st.xy, vec2(14.159, 65.359))) * 98765.4321);
}

void main() {
    vec2 uv = FragCoord.xy / iResolution.xy;
    vec3 color = vec3(0.0);
    float alpha = 0.0;

    // Center UV coordinates
    vec2 centered_uv = uv - 0.5;

    // Use a grid for particle ID
    vec2 grid_uv = floor(uv * 50.0) / 50.0;
    float particle_id_r = random(grid_uv);

    if (particle_id_r < 0.05) { // This grid cell contains a particle
        // Calculate initial angle and speed
        float angle = random2(grid_uv) * 6.283185;
        float speed = 0.1 + random(grid_uv + vec2(1.0, 0.0)) * 0.2;

        // Calculate the expected position
        vec2 direction = vec2(cos(angle), sin(angle));
        vec2 expected_pos = (grid_uv - 0.5) + direction * speed * iTime;

        // Calculate distance from the current fragment to the particle center
        float dist = length(centered_uv - expected_pos);

        // Add glow effect: alpha decreases with distance from the center
        float glow_radius = 0.02; // Radius of the glow effect
        alpha = max(0.0, 1.0 - (dist / glow_radius)); // Alpha is 1 at center, 0 at glow_radius

        // Combine glow alpha with time-based fade-out
        float life_time = 3.0;
        float time_ratio = clamp(iTime / life_time, 0.0, 1.0);
        alpha *= (1.0 - time_ratio); // Multiply glow alpha by fade-out factor

        color = vec3(1.0); // White particle color
    }

    FragColor = vec4(color, alpha); // Output color with combined alpha
}
```

----------------------------------------

TITLE: Adding Custom Resource Handle (Absolute Path)
DESCRIPTION: Illustrates how to register a new custom resource handle (`:my_resources:`) mapping it to a specific absolute directory path on the file system using `arcade.resources.add_resource_handle`. This allows using the handle prefix instead of the full path.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/resource_handlers.rst#_snippet_1

LANGUAGE: python
CODE:
```
arcade.resources.add_resource_handle("my_resources", "/home/users/username/my_game/my_res_folder")
```

----------------------------------------

TITLE: Setting Up Mini-Map Resources (Python)
DESCRIPTION: Configures the mini-map camera with its viewport size, creates the frame buffer object (FBO) for rendering the mini-map content, creates a sprite to display the FBO's texture at a specific screen position, assigns the texture from the FBO to the sprite, and sets texture filtering/wrapping properties.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/minimap.rst#_snippet_2

LANGUAGE: Python
CODE:
```
        # --- Mini-map setup ---
        # Line 99: Create a camera for the mini-map
        self.minimap_camera = arcade.Camera(MINIMAP_VIEWPORT_WIDTH, MINIMAP_VIEWPORT_HEIGHT)
        # Line 100: Create a frame buffer for the mini-map
        self.minimap_buffer = self.ctx.framebuffer(
            color_attachments=[self.ctx.texture((MINIMAP_VIEWPORT_WIDTH, MINIMAP_VIEWPORT_HEIGHT), components=4)]
        )
        # Line 105: Create a sprite to display the mini-map texture
        self.minimap_sprite = arcade.Sprite(center_x=SCREEN_WIDTH - MINIMAP_WIDTH / 2 - MINIMAP_MARGIN,
                                            center_y=SCREEN_HEIGHT - MINIMAP_HEIGHT / 2 - MINIMAP_MARGIN)
        self.minimap_sprite.width = MINIMAP_WIDTH
        self.minimap_sprite.height = MINIMAP_HEIGHT
        # Line 111: Get the texture from the frame buffer
        self.minimap_texture = self.minimap_buffer.color_attachments[0]
        # Line 113: Assign the texture to the sprite
        self.minimap_sprite.texture = self.minimap_texture
        # Line 114: Configure texture filtering/wrapping (often done after getting the texture)
        self.minimap_texture.filter = self.ctx.LINEAR, self.ctx.LINEAR
        self.minimap_texture.repeat_y = False # Prevent tiling
```

----------------------------------------

TITLE: Adding Dropdown to Layout - Python/Arcade
DESCRIPTION: This code adds the created dropdown widget to the main vertical box layout (`self.v_box`), placing it after the toggle button.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_23

LANGUAGE: Python
CODE:
```
self.v_box.add(dropdown)
```

----------------------------------------

TITLE: Playing Coin Collection Sound in Arcade on_update
DESCRIPTION: Plays the previously loaded coin collection sound whenever a coin is collected. This occurs within the game's update loop after detecting collisions and removing the collected coin sprite.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_09.rst#_snippet_1

LANGUAGE: python
CODE:
```
# Within on_update
for coin in coin_hit_list:
    coin.remove_from_sprite_lists()
    arcade.play_sound(self.collect_coin_sound)
```

----------------------------------------

TITLE: Implementing Sprite Rotation Around a Point in Arcade
DESCRIPTION: This Python code provides a base class `RotatingSprite` and subclasses (`SpinningBeam`, `RotatingPlatform`) to demonstrate rotating sprites around a fixed point. The `update` method calculates the new position based on an updated angle around the rotation point. The example sets up two sprites using this logic.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/sprite_rotate_around_point.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import math

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Rotation Around Point Example"

# Base class for rotating sprites
class RotatingSprite(arcade.Sprite):
    def __init__(self, filename, center_x, center_y, rotation_point_x, rotation_point_y, speed, initial_angle=0):
        super().__init__(filename, center_x=center_x, center_y=center_y)
        self.rotation_point_x = rotation_point_x
        self.rotation_point_y = rotation_point_y
        self.speed = speed # degrees per update
        self.angle = initial_angle # current angle relative to rotation point

    def update(self):
        # Calculate distance and current angle from rotation point
        dx = self.center_x - self.rotation_point_x
        dy = self.center_y - self.rotation_point_y
        distance = math.sqrt(dx**2 + dy**2)
        # Note: math.atan2 returns radians, convert to degrees
        current_angle_rad = math.atan2(dy, dx)
        current_angle_deg = math.degrees(current_angle_rad)

        # Update angle
        self.angle = (current_angle_deg + self.speed) % 360

        # Calculate new position based on updated angle and distance
        new_angle_rad = math.radians(self.angle)
        self.center_x = self.rotation_point_x + distance * math.cos(new_angle_rad)
        self.center_y = self.rotation_point_y + distance * math.sin(new_angle_rad)

        # Update sprite's visual rotation (optional, depends on effect)
        # self.angle = self.angle # This would make the sprite rotate with the path

# Example 1: Spinning Beam
class SpinningBeam(RotatingSprite):
     def update(self):
         super().update()
         # Make the sprite itself spin
         self.angle += self.speed # Add sprite's own rotation

# Example 2: Rotating Platform (stays flat)
class RotatingPlatform(RotatingSprite):
    def update(self):
        super().update()
        # The sprite's visual angle stays fixed (or set to 0)
        self.angle = 0 # Keep the platform flat

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        self.sprite_list = arcade.SpriteList()

    def setup(self):
        # Create the spinning beam
        # Assuming a placeholder image 'beam.png'
        beam = SpinningBeam("beam.png", 350, 300, 200, 300, 2) # Start at (350,300), rotate around (200,300)
        self.sprite_list.append(beam)

        # Create the rotating platform
        # Assuming a placeholder image 'platform.png'
        platform = RotatingPlatform("platform.png", 650, 300, 700, 300, 1) # Start at (650,300), rotate around (700,300)
        self.sprite_list.append(platform)

    def on_draw(self):
        arcade.start_render()
        self.sprite_list.draw()

    def on_update(self, delta_time):
        self.sprite_list.update()

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Stopping Specific Playback with arcade.stop_sound in Python
DESCRIPTION: This snippet demonstrates stopping a specific, currently active sound playback instance by passing its playback object (obtained from `arcade.play_sound` or the `.play()` method) to the `arcade.stop_sound` function. This only stops the designated instance, not all playbacks of the sound data. Requires the `arcade` library and a playback object.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/sound.rst#_snippet_6

LANGUAGE: python
CODE:
```
arcade.stop_sound(self.coin_playback_1)
```

----------------------------------------

TITLE: Drawing Particles Python Arcade (v2)
DESCRIPTION: Updates the drawing method to calculate the current time and the elapsed time for each burst. The elapsed time is then passed as a uniform variable (`time`) to the shader program before rendering the burst.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/gpu_particle_burst/index.rst#_snippet_12

LANGUAGE: Python
CODE:
```
def on_draw(self):
    self.clear()
    current_time = time.time()
    for burst in self.burst_list:
        self.program['time'] = current_time - burst.time
        burst.vao.render(self.program, mode=arcade.gl.POINTS)
```

----------------------------------------

TITLE: Initialize Drag/Drop Attributes in setup - Python
DESCRIPTION: Initializes the `held_cards` and `held_cards_original_position` attributes as empty lists within the `MyGame` setup method, preparing them for use in drag-and-drop operations.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_7

LANGUAGE: Python
CODE:
```
    def setup(self):
        """ Set up the game here. Call this to restart the game. """

        # List of cards we are dragging with the mouse
        self.held_cards = []

        # Original location of cards we are dragging with the mouse
        self.held_cards_original_position = []

        # Create the sprite lists
        self.card_list = arcade.SpriteList()

        # Create every card
        for suit in ALL_SUITS:
            for value in RANKS:
                card = Card(suit, value)
                card.position = START_X, BOTTOM_Y
                self.card_list.append(card)

    # ... rest of the class ...
```

----------------------------------------

TITLE: GLSL Program for Step 1
DESCRIPTION: This is the initial GLSL shader program. The `mainImage` function is executed for each pixel (`fragCoord`) and determines its output color (`fragColor`). This simple version samples the color from `iChannel0` (channel 0) at the corresponding normalized coordinate and outputs it directly, effectively just displaying the content of channel 0.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/raycasting/index.rst#_snippet_3

LANGUAGE: glsl
CODE:
```
void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    // Normalize the coordinate
    vec2 normalizedCoord = fragCoord/iResolution.xy;

    // Sample the color from channel 0 at the normalized coordinate
    vec4 color = texture(iChannel0, normalizedCoord);

    // Output the color
    fragColor = color;
}
```

----------------------------------------

TITLE: GLSL Shader with Particle Movement
DESCRIPTION: This GLSL shader adds movement to the particles. It calculates an initial direction and speed for each particle using pseudo-randomness based on its ID and updates its position over time using the `iTime` uniform.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_toy_particles/index.rst#_snippet_2

LANGUAGE: GLSL
CODE:
```
#version 330 core

out vec4 FragColor;
in vec2 TexCoords;

uniform vec2 iResolution;
uniform float iTime;

// Pseudo-random number generator 1
float random(vec2 st) {
    return fract(sin(dot(st.xy, vec2(12.9898,78.233))) * 43758.5453123);
}

// Pseudo-random number generator 2 (for different random values)
float random2(vec2 st) {
    return fract(sin(dot(st.xy, vec2(14.159, 65.359))) * 98765.4321);
}

void main() {
    vec2 uv = FragCoord.xy / iResolution.xy;
    vec3 color = vec3(0.0);

    // Center UV coordinates around 0.0
    vec2 centered_uv = uv - 0.5;

    // Use a grid for particle ID
    vec2 grid_uv = floor(uv * 50.0) / 50.0;
    float particle_id_r = random(grid_uv);

    if (particle_id_r < 0.05) { // This grid cell contains a particle
        // Calculate initial angle and speed using random values based on ID
        float angle = random2(grid_uv) * 6.283185; // 0 to 2*PI
        float speed = 0.1 + random(grid_uv + vec2(1.0, 0.0)) * 0.2; // Random speed

        // Calculate the expected position of the particle center at the current time
        vec2 direction = vec2(cos(angle), sin(angle));
        vec2 expected_pos = (grid_uv - 0.5) + direction * speed * iTime;

        // Check if the current fragment is close to the expected particle position
        float dist = length(centered_uv - expected_pos);

        if (dist < 0.01) { // If fragment is within a small radius of the particle center
             color = vec3(1.0); // White particle
        }
    }

    FragColor = vec4(color, 1.0);
}
```

----------------------------------------

TITLE: Using pathlib Objects with Arcade Loading
DESCRIPTION: Shows how to use the result of `arcade.resources.resolve` (which is a `pathlib.Path` object) and `pathlib`'s `/` operator to construct file paths. This provides a cleaner syntax for accessing files within a directory obtained via a resource handle.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/resource_handlers.rst#_snippet_8

LANGUAGE: python
CODE:
```
SPRITE_SCALE = 0.5
ANN_TEXTURE_PATH = arcade.resources.resolve(":assets:images/animated_characters/female_person/")

my_sprite = arcade.Sprite(ANN_TEXTURE_PATH / "femalePerson_idle.png" , SPRITE_SCALE)
```

----------------------------------------

TITLE: Initializing GameWindow for Ladder Input - Python
DESCRIPTION: Adds boolean variables to the GameWindow class constructor to keep track of whether the up or down keys are currently being pressed, which are used to control vertical movement when the player is on a ladder.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/pymunk_platformer/index.rst#_snippet_12

LANGUAGE: Python
CODE:
```
class GameWindow(...):
    def __init__(self, ...):
        # ... other initializations
        self.up_pressed = False # Track if up key is pressed
        self.down_pressed = False # Track if down key is pressed
        # ...
```

----------------------------------------

TITLE: Pausing Sound Playback via Pyglet Player in Python
DESCRIPTION: This snippet demonstrates how to pause a sound playback by directly accessing the underlying pyglet `Player` object (which is what `arcade.play_sound` or `Sound.play()` return). Calling the player's `.pause()` method temporarily halts the playback. Requires a pyglet `Player` object instance.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/sound.rst#_snippet_10

LANGUAGE: python
CODE:
```
# Assume this is inside a class which stores a pyglet Player
self.current_player.pause()
```

----------------------------------------

TITLE: Shader: Adding Fade Effect - GLSL
DESCRIPTION: Introduces a fade effect based on the distance from the center. The inverse distance is calculated and scaled down to modulate the color intensity, creating a smooth transition from the shape's edge.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_toy_glow/index.rst#_snippet_6

LANGUAGE: glsl
CODE:
```
#version 330

uniform vec3 iResolution;
out vec4 fracColor;

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    // Normalized pixel coordinates (from -0.5 to 0.5)
    vec2 uv = fragCoord/iResolution.xy - 0.5;

    // Adjust for aspect ratio
    uv.x *= iResolution.x / iResolution.y;

    // Calculate the distance from center
    float d = length(uv);

    // Calculate color based on distance
    // Inverse distance, scaled down.
    vec3 col = vec3(1.0, 1.0, 1.0) * (1.0 / (d * 2.0));

    fragColor = vec4(col,1.0);
}
```

----------------------------------------

TITLE: Add Player Animation - Creating the Player Class Instance - Python/Arcade
DESCRIPTION: This snippet shows the correct way to instantiate the custom PlayerSprite class in the game's setup method, replacing the default arcade.Sprite instance.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/pymunk_platformer/index.rst#_snippet_6

LANGUAGE: python
CODE:
```
# Create the player sprite
self.player_sprite = PlayerSprite()
```

----------------------------------------

TITLE: Custom Window Headless Drawing and Closing (Python)
DESCRIPTION: Presents an example using a custom class inheriting from arcade.Window. It shows how on_draw is called to render content and save the framebuffer, and how on_update can be used for logic and to programmatically close the window (e.g., after a certain number of frames) in headless mode.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/headless.rst#_snippet_4

LANGUAGE: python
CODE:
```
import os
os.environ["ARCADE_HEADLESS"] = "true"
import arcade

class App(arcade.Window):

    def __init__(self):
        super().__init__(200, 200)
        self.frame = 0
        self.sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            center_x=self.width / 2,
            center_y=self.height / 2,
        )

    def on_draw(self):
        self.clear()
        arcade.draw_sprite(self.sprite)

        # Dump the window framebuffer to disk
        image = arcade.get_image(0, 0, *self.get_size())
        image.save("framebuffer.png")

    def on_update(self, delta_time: float):
        # Close the window on the second frame
        if self.frame == 2:
            self.close()

        self.frame += 1

App().run()
```

----------------------------------------

TITLE: Wrapping Text for Localization in Arcade (Python)
DESCRIPTION: This snippet modifies the original text drawing code by wrapping the translatable string with the `_()` function. This signals to localization tools like `pygettext.py` that the string should be extracted for translation. The `_()` function is a convention used with `gettext`.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/text_loc_example.rst#_snippet_1

LANGUAGE: Python
CODE:
```
arcade.draw_text(
    _("Simple line of text in 12 point"), start_x, start_y, arcade.color.BLACK, 12
)
```

----------------------------------------

TITLE: Sample Texture from Channel 0 (GLSL)
DESCRIPTION: This GLSL snippet shows the use of the built-in `texture` function. It samples a color value from `iChannel0` (shader channel 0) at the specified coordinate `curPoint`. The coordinate should typically be normalized (between 0.0 and 1.0).
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/raycasting/index.rst#_snippet_5

LANGUAGE: glsl
CODE:
```
texture(iChannel0, curPoint)
```

----------------------------------------

TITLE: Deleting Sound Playback via Pyglet Player in Python
DESCRIPTION: This snippet demonstrates permanently stopping a specific sound playback instance and releasing its system resources by calling the `.delete()` method on the underlying pyglet `Player` object. This action is irreversible for that specific player instance, although new playbacks of the sound data can still be started. Requires a pyglet `Player` object instance.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/sound.rst#_snippet_11

LANGUAGE: python
CODE:
```
# Permanently deletes the operating system half of this playback.
self.current_player.delete()
```

----------------------------------------

TITLE: Loading User's Preferred Language Translation Automatically (Python)
DESCRIPTION: This Python code shows how to automatically load the appropriate translation based on the user's system language settings using `gettext.install`. It searches for the message catalog within the specified `localedir` using the domain name. This simplifies loading compared to specifying a language explicitly.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/text_loc_example.rst#_snippet_6

LANGUAGE: Python
CODE:
```
gettext.install('text_loc_example', localedir='text_loc_example_locale')
```

----------------------------------------

TITLE: Initial GLSL Shader for Static Particles
DESCRIPTION: This initial GLSL fragment shader sets up the basic structure and uses a pseudo-random number generator to determine which fragments represent the center of a particle, rendering them white.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_toy_particles/index.rst#_snippet_1

LANGUAGE: GLSL
CODE:
```
#version 330 core

out vec4 FragColor;
in vec2 TexCoords;

uniform vec2 iResolution; // Screen resolution
uniform float iTime;      // Time elapsed

// Pseudo-random number generator based on fragment coordinates
float random(vec2 st) {
    return fract(sin(dot(st.xy, vec2(12.9898,78.233))) * 43758.5453123);
}

void main() {
    vec2 uv = FragCoord.xy / iResolution.xy;
    vec3 color = vec3(0.0);

    // Use a grid based on UV coordinates to create distinct particle 'IDs'
    vec2 grid_uv = floor(uv * 50.0) / 50.0; // Example: 50x50 grid
    float r = random(grid_uv);

    // If the random value for this grid cell is below a threshold, draw a particle center
    if (r < 0.05) {
        color = vec3(1.0); // White particle
    }

    FragColor = vec4(color, 1.0);
}
```

----------------------------------------

TITLE: Handling Controller Button Press - Arcade Python
DESCRIPTION: Defines a function `on_button_press` decorated with `@controller.event` to handle button press events for a specific controller instance. The callback receives the `controller` object and the `button_name` string, allowing conditional logic based on which button was pressed.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/controller.rst#_snippet_5

LANGUAGE: Python
CODE:
```
      @controller.event
      def on_button_press(controller, button_name):
          if button_name == 'a':
              # start firing
          elif button_name == 'b':
              # do something else
```

----------------------------------------

TITLE: Shuffle Cards in Game Setup (Arcade, Python)
DESCRIPTION: Adds code to the `setup` method to randomize the order of the cards before the game starts, requiring the `random` module.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_17

LANGUAGE: python
CODE:
```
# Placeholder for code from solitaire_06.py MyGame.setup lines 49-52
# Example: random.shuffle(self.card_list)
```

----------------------------------------

TITLE: Assign Output Color from Texture Sample (GLSL)
DESCRIPTION: This GLSL snippet assigns the color sampled from `iChannel0` at the `normalizedCoord` to the output pixel color variable `fragColor`. This is the final step in the basic shader, determining the color of the current pixel based on the input texture data.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/raycasting/index.rst#_snippet_6

LANGUAGE: glsl
CODE:
```
fragColor = texture(iChannel0, normalizedCoord);
```

----------------------------------------

TITLE: Enabling Headless Mode via Code (Python)
DESCRIPTION: Explains how to configure Arcade for headless operation by setting the ARCADE_HEADLESS environment variable or the pyglet.options.headless flag to True. This must be done before the arcade module is imported.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/headless.rst#_snippet_0

LANGUAGE: python
CODE:
```
# Before Arcade is imported
import os
os.environ["ARCADE_HEADLESS"] = "True"

# The above is a shortcut for
import pyglet
pyglet.options.headless = True
```

----------------------------------------

TITLE: Generating Recursive Maze with Arcade
DESCRIPTION: This Python code implements a recursive backtracking algorithm to generate a random maze within an Arcade window. It initializes a grid, recursively carves paths, and then draws the maze using Arcade sprites.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/maze_recursive.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
WALL_SIZE = 2
MAZE_WIDTH = (SCREEN_WIDTH - WALL_SIZE) // CELL_SIZE
MAZE_HEIGHT = (SCREEN_HEIGHT - WALL_SIZE) // CELL_SIZE

class Maze(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.grid = [[1 for _ in range(MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)] # 1 for wall, 0 for path
        self.wall_list = arcade.SpriteList()
        self.generate_maze(0, 0)
        self.draw_maze()

    def generate_maze(self, cx, cy):
        # Directions: (dx, dy)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = cx + dx * 2, cy + dy * 2
            if 0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT and self.grid[ny][nx] == 1:
                # Carve path
                self.grid[cy + dy][cx + dx] = 0
                self.grid[ny][nx] = 0
                self.generate_maze(nx, ny)

    def draw_maze(self):
        for y in range(MAZE_HEIGHT):
            for x in range(MAZE_WIDTH):
                if self.grid[y][x] == 1:
                    wall = arcade.SpriteSolidColor(CELL_SIZE, CELL_SIZE, arcade.color.WHITE)
                    wall.center_x = x * CELL_SIZE + CELL_SIZE / 2 + WALL_SIZE / 2
                    wall.center_y = y * CELL_SIZE + CELL_SIZE / 2 + WALL_SIZE / 2
                    self.wall_list.append(wall)

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()

def main():
    game = Maze(SCREEN_WIDTH, SCREEN_HEIGHT, "Recursive Maze")
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Adding callback for button events 2
DESCRIPTION: This code adds event listeners for the Volume and Options buttons, which will likely trigger the display of the SubMenu.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_13

LANGUAGE: Python
CODE:
```
class MenuView(arcade.View):
    # ... __init__ and other methods

    def on_show_view(self):
        # ... enable manager and other button handlers
        self.volume_button.on_click = self.on_click_volume
        self.options_button.on_click = self.on_click_options

    def on_click_volume(self, event):
        print("Volume clicked")
        # Code to show the volume sub-menu

    def on_click_options(self, event):
        print("Options clicked")
        # Code to show the options sub-menu
```

----------------------------------------

TITLE: Loading Specific Language Translation (Python)
DESCRIPTION: This Python code demonstrates how to explicitly load a translation for a specific language (Spanish, 'es') using `gettext.translation`. It specifies the domain name, the directory containing locale data (`localedir`), and the target languages. `es.install()` makes the `_()` function available globally to use the loaded translation.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/text_loc_example.rst#_snippet_5

LANGUAGE: Python
CODE:
```
...
import arcade
import gettext
es = gettext.translation('text_loc_example', localedir='text_loc_example_locale', languages=['es'])
es.install()

SCREEN_WIDTH = 500
...
```

----------------------------------------

TITLE: Creating and Using FrameBuffer - Arcade Python
DESCRIPTION: This code demonstrates how to create a simple FrameBuffer object using Arcade's OpenGL context. It shows how to activate the FrameBuffer to render content into it and then draw the FrameBuffer's texture to the main window.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/framebuffer/index.rst#_snippet_1

LANGUAGE: Python
CODE:
```
import arcade
import arcade.gl as gl

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "FrameBuffer Example"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

        # Create a FrameBuffer
        self.fbo = self.ctx.framebuffer(
            color_attachments=[self.ctx.texture((width, height), components=4)]
        )

    def on_draw(self):
        # Render to the FrameBuffer
        with self.fbo.activate():
            self.clear()
            arcade.draw_circle_filled(100, 100, 50, arcade.color.RED)

        # Render the FrameBuffer texture to the screen
        self.clear()
        self.fbo.color_attachments[0].use(0)
        self.ctx.copy_framebuffer(self.fbo, self.ctx.screen)

    def update(self, delta_time):
        pass

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Basic Vertex Shader GLSL
DESCRIPTION: A simple vertex shader that takes a 2D position (`in_pos`) as input. It transforms this position into the final clip space position (`gl_Position`) and sets the output color (`out_color`) to solid white.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/gpu_particle_burst/index.rst#_snippet_4

LANGUAGE: GLSL
CODE:
```
#version 330 core

in vec2 in_pos;
out vec4 out_color;

void main() {
    gl_Position = vec4(in_pos, 0.0, 1.0);
    out_color = vec4(1.0, 1.0, 1.0, 1.0);
}
```

----------------------------------------

TITLE: Drawing Gradients with Arcade (Python)
DESCRIPTION: This Python script demonstrates how to draw rectangles filled with linear color gradients using the arcade library. It initializes a window, sets up the drawing context, and uses `arcade.draw_lrtb_rectangle_filled_with_gradient` to render gradients with different directions and colors.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/gradients.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Gradients Example"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

        # Example gradient
        arcade.draw_lrtb_rectangle_filled_with_gradient(
            0, SCREEN_WIDTH // 2, 0, SCREEN_HEIGHT,
            arcade.color.RED, arcade.color.BLUE,
            'left_to_right'
        )

        arcade.draw_lrtb_rectangle_filled_with_gradient(
            SCREEN_WIDTH // 2, SCREEN_WIDTH, 0, SCREEN_HEIGHT,
            arcade.color.GREEN, arcade.color.YELLOW,
            'bottom_to_top'
        )

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

----------------------------------------

TITLE: Extracting Translatable Strings with pygettext.py (Command Line)
DESCRIPTION: This command executes the `pygettext.py` script to scan a Python file (`text_loc_example.py`) for strings wrapped with `_()` and extracts them into a `.pot` (Portable Object Template) file. The `-d` option sets the domain name for the message catalog. This file serves as a template for translations.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/text_loc_example.rst#_snippet_2

LANGUAGE: Command Line
CODE:
```
python ./pygettext.py -d text_loc_example text_loc_example.py
```

----------------------------------------

TITLE: GLSL Shader with Particle Fade-out
DESCRIPTION: This GLSL shader adds a fade-out effect to the particles. It calculates an alpha value based on the particle's age (derived from `iTime`) and applies it, making particles gradually disappear.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_toy_particles/index.rst#_snippet_3

LANGUAGE: GLSL
CODE:
```
#version 330 core

out vec4 FragColor;
in vec2 TexCoords;

uniform vec2 iResolution;
uniform float iTime;

// Pseudo-random number generator 1
float random(vec2 st) {
    return fract(sin(dot(st.xy, vec2(12.9898,78.233))) * 43758.5453123);
}

// Pseudo-random number generator 2
float random2(vec2 st) {
    return fract(sin(dot(st.xy, vec2(14.159, 65.359))) * 98765.4321);
}

void main() {
    vec2 uv = FragCoord.xy / iResolution.xy;
    vec3 color = vec3(0.0);
    float alpha = 0.0; // Initialize alpha to 0

    // Center UV coordinates
    vec2 centered_uv = uv - 0.5;

    // Use a grid for particle ID
    vec2 grid_uv = floor(uv * 50.0) / 50.0;
    float particle_id_r = random(grid_uv);

    if (particle_id_r < 0.05) { // This grid cell contains a particle
        // Calculate initial angle and speed
        float angle = random2(grid_uv) * 6.283185;
        float speed = 0.1 + random(grid_uv + vec2(1.0, 0.0)) * 0.2;

        // Calculate the expected position
        vec2 direction = vec2(cos(angle), sin(angle));
        vec2 expected_pos = (grid_uv - 0.5) + direction * speed * iTime;

        // Check if the current fragment is close to the expected particle position
        float dist = length(centered_uv - expected_pos);

        if (dist < 0.01) { // If fragment is within particle radius
             color = vec3(1.0); // White particle

             // Calculate fade-out based on time
             float life_time = 3.0; // Example: particle lives for 3 seconds
             float time_ratio = clamp(iTime / life_time, 0.0, 1.0);
             alpha = 1.0 - time_ratio; // Alpha goes from 1 to 0 over life_time
        }
    }

    FragColor = vec4(color, alpha); // Output color with calculated alpha
}
```

----------------------------------------

TITLE: Handle Mouse Release for Drop - Python
DESCRIPTION: Implements the `on_mouse_release` method in `MyGame`. When the mouse button is released, it clears the `held_cards` list, effectively dropping any cards that were being dragged.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_11

LANGUAGE: Python
CODE:
```
    def on_mouse_release(self, x, y, button):
        """ Called when a user releases a mouse button. """

        # If we are holding cards, release them
        if len(self.held_cards) > 0:
            self.held_cards = []

    # ... rest of the class ...
```

----------------------------------------

TITLE: Handling Mouse Clicks Without Arcade Sections (Python)
DESCRIPTION: This snippet demonstrates a traditional approach to handling mouse events by checking the mouse coordinates within a single `on_mouse_release` method of an `arcade.View`. It shows how logic becomes conditional based on manual spatial checks, which can lead to complex code in a single view class.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/sections.rst#_snippet_0

LANGUAGE: Python
CODE:
```
class MyView(arcade.View):
    # ...

    def on_mouse_release(x: int, y: int, *args, **kwargs):
        if x > 700:
            # click in the side
            do_some_logic_when_side_clicking()
        else:
            # click on the game map
            do_something_in_the_game_map()
```

----------------------------------------

TITLE: Define Card Pile Type Constants (Arcade, Python)
DESCRIPTION: Defines constants representing the different types of card piles (e.g., deal pile, play piles, foundation piles) for better code readability and management.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_18

LANGUAGE: python
CODE:
```
# Placeholder for code from solitaire_07.py lines 48-65
# Example: Constants like PILE_DEAL, PILE_PLAY_1, PILE_FOUNDATION_1, etc.
```

----------------------------------------

TITLE: Generating Depth First Maze with Arcade (Python)
DESCRIPTION: This script implements a maze generation algorithm based on depth-first search using the Arcade library. It initializes a grid, iteratively carves paths by visiting cells and removing walls, and renders the maze using Arcade's drawing functions. The `MazeGenerator` class handles the game window, grid state, and the generation logic within its `update` method.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/maze_depth_first.rst#_snippet_0

LANGUAGE: Python
CODE:
```
"""
Example of generating a maze using a depth-first algorithm.
"""
import arcade
import random

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

class MazeGenerator(arcade.Window):
    def __init__(self, width, height, cell_size):
        super().__init__(width, height, "Depth First Maze")
        self.cell_size = cell_size
        self.grid_width = width // cell_size
        self.grid_height = height // cell_size
        self.grid = [[1 for _ in range(self.grid_width)] for _ in range(self.grid_height)] # 1 for wall, 0 for path
        self.visited = [[False for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        self.stack = []
        self.current_cell = (0, 0)
        self.grid[0][0] = 0 # Start cell is path
        self.visited[0][0] = True
        self.stack.append((0, 0))

    def on_draw(self):
        arcade.start_render()
        # Draw the maze
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if self.grid[row][col] == 1:
                    arcade.draw_rectangle_filled(
                        col * self.cell_size + self.cell_size // 2,
                        row * self.cell_size + self.cell_size // 2,
                        self.cell_size,
                        self.cell_size,
                        arcade.color.DARK_BLUE
                    )
                else:
                     arcade.draw_rectangle_filled(
                        col * self.cell_size + self.cell_size // 2,
                        row * self.cell_size + self.cell_size // 2,
                        self.cell_size,
                        self.cell_size,
                        arcade.color.BLACK
                    )

    def update(self, delta_time):
        if not self.stack:
            return # Maze generation complete

        current_row, current_col = self.current_cell

        # Find unvisited neighbors
        neighbors = []
        # Up
        if current_row > 1 and not self.visited[current_row - 2][current_col]:
            neighbors.append(((current_row - 2, current_col), (current_row - 1, current_col)))
        # Down
        if current_row < self.grid_height - 2 and not self.visited[current_row + 2][current_col]:
            neighbors.append(((current_row + 2, current_col), (current_row + 1, current_col)))
        # Left
        if current_col > 1 and not self.visited[current_row][current_col - 2]:
            neighbors.append(((current_row, current_col - 2), (current_row, current_col - 1)))
        # Right
        if current_col < self.grid_width - 2 and not self.visited[current_row][current_col + 2]:
            neighbors.append(((current_row, current_col + 2), (current_row, current_col + 1)))

        if neighbors:
            # Pick a random neighbor
            next_cell, wall_to_remove = random.choice(neighbors)
            next_row, next_col = next_cell
            wall_row, wall_col = wall_to_remove

            # Remove the wall
            self.grid[wall_row][wall_col] = 0
            # Mark the next cell as visited and make it a path
            self.visited[next_row][next_col] = True
            self.grid[next_row][next_col] = 0

            # Push the current cell to the stack and move to the next cell
            self.stack.append(next_cell)
            self.current_cell = next_cell
        elif self.stack:
            # If no unvisited neighbors, pop from the stack
            self.current_cell = self.stack.pop()

def main():
    window = MazeGenerator(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE)
    arcade.run()

if __name__ == "__main__":
    main()

```

----------------------------------------

TITLE: Drawing with Arcade CRT Filter (Python)
DESCRIPTION: Illustrates the process for rendering game elements using the CRT filter within the on_draw method. Game content is first drawn to the filter's internal buffer by activating the filter with `use()`, then the filter's processed output is drawn to the main screen context after switching back with `use()` (or implicit screen context use).
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/crt_filter/index.rst#_snippet_1

LANGUAGE: python
CODE:
```
# Draw our stuff into the CRT filter instead of on screen
self.crt_filter.use()
self.crt_filter.clear()
self.sprite_list.draw()

# Next, switch back to the screen and dump the contents of the CRT filter
# to it.
self.use()
self.clear()
self.crt_filter.draw()
```

----------------------------------------

TITLE: Initializing Arcade CRT Filter (Python)
DESCRIPTION: Demonstrates how to create an instance of the CRTFilter class in Arcade. The constructor requires screen dimensions (width, height) and accepts numerous optional parameters to fine-tune the CRT effect, such as downscaling, scanline intensity, pixel shape, display warp, and mask appearance.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/crt_filter/index.rst#_snippet_0

LANGUAGE: python
CODE:
```
# Create the crt filter
self.crt_filter = CRTFilter(width, height,
                                resolution_down_scale=6.0,
                                hard_scan=-8.0,
                                hard_pix=-3.0,
                                display_warp = Vec2(1.0 / 32.0, 1.0 / 24.0),
                                mask_dark=0.5,
                                mask_light=1.5)
```

----------------------------------------

TITLE: Disabling the Manager
DESCRIPTION: This method is called when the view is hidden. It disables the UIManager to stop processing UI events.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_4

LANGUAGE: Python
CODE:
```
class MainView(arcade.View):
    # ... __init__ and other methods

    def on_hide_view(self):
        # Disable manager
        self.manager.disable()
```

----------------------------------------

TITLE: Include Data Directory During Compilation with Nuitka Bash
DESCRIPTION: This command compiles the Python script and includes an entire directory (`assets`). The `--include-data-dir` flag takes the source path of the directory and the target path within the distribution (``.`` refers to the root). This is useful for bundling multiple assets organized in folders.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/compiling_with_nuitka/index.rst#_snippet_3

LANGUAGE: bash
CODE:
```
python -m nuitka 17_views.py --standalone --enable-plugin=numpy --include-data-dir=C:/Users/Hunter/Desktop/my_game/assets=.
```

----------------------------------------

TITLE: Simple Headless Drawing and Saving Image (Python)
DESCRIPTION: Shows a basic headless script that initializes Arcade in headless mode, creates a window, performs drawing operations (a filled rectangle), and then captures the window's framebuffer content using arcade.get_image and saves it to a PNG file.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/headless.rst#_snippet_3

LANGUAGE: python
CODE:
```
# Configure headless before importing arcade
import os
os.environ["ARCADE_HEADLESS"] = "true"
import arcade

# Create a 100 x 100 headless window
window = arcade.open_window(100, 100)

# Draw a quick rectangle
arcade.draw_rectangle_filled(50, 50, 50, 50, color=arcade.color.AMAZON)

# Dump the framebuffer to a png
image = arcade.get_image(0, 0, *window.get_size())
image.save(f"framebuffer.png")
```

----------------------------------------

TITLE: Add Gravity to Particle Velocity (GLSL)
DESCRIPTION: Modify the vertex shader code to apply a downward force (gravity) to particle velocities over time. The vertical component of the velocity is adjusted based on the elapsed time and a gravity constant.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/gpu_particle_burst/index.rst#_snippet_18

LANGUAGE: GLSL
CODE:
```
// Adjust velocity based on gravity
vec2 new_vel = in_vel;
new_vel[1] -= time * 1.1;

// Calculate a new position
vec2 new_pos = in_pos + (time * new_vel);
```

----------------------------------------

TITLE: Initializing Mini-Map Attributes (Python)
DESCRIPTION: Initializes the instance variables within the game class (__init__ method) that will hold the mini-map camera, frame buffer object (FBO), sprite, and texture, setting them to None initially.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/minimap.rst#_snippet_1

LANGUAGE: Python
CODE:
```
        # --- Mini-map ---
        self.minimap_camera = None
        self.minimap_buffer = None
        self.minimap_sprite = None
        self.minimap_texture = None
```

----------------------------------------

TITLE: Bundling a Simple Game with PyInstaller - Bash
DESCRIPTION: This command runs PyInstaller on the main game script (`main.py`) to create a standalone executable bundle. The `--onefile` flag instructs PyInstaller to package everything into a single executable file in the `dist/` directory.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/bundling_with_pyinstaller/index.rst#_snippet_2

LANGUAGE: bash
CODE:
```
pyinstaller main.py --onefile
```

----------------------------------------

TITLE: Create All Card Sprites - Python
DESCRIPTION: Implements the `setup` method in `MyGame` to initialize the `card_list` and create all 52 card sprites (Ace through King for each suit), adding them to the list.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_4

LANGUAGE: Python
CODE:
```
    def setup(self):
        """ Set up the game here. Call this to restart the game. """

        # List of cards we are dragging with the mouse
        self.held_cards = None

        # Original location of cards we are dragging with the mouse
        self.held_cards_original_position = None

        # Create the sprite lists
        self.card_list = arcade.SpriteList()

        # Create every card
        for suit in ALL_SUITS:
            for value in RANKS:
                card = Card(suit, value)
                card.position = START_X, BOTTOM_Y
                self.card_list.append(card)

    # ... rest of the class ...
```

----------------------------------------

TITLE: Drawing Particles Python Arcade (v1)
DESCRIPTION: This method handles drawing on the screen. It first clears the drawing buffer and then iterates through the list of active bursts, rendering each particle burst using its associated `VertexArray` and the loaded shader program.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/gpu_particle_burst/index.rst#_snippet_7

LANGUAGE: Python
CODE:
```
def on_draw(self):
    self.clear()
    for burst in self.burst_list:
        burst.vao.render(self.program, mode=arcade.gl.POINTS)
```

----------------------------------------

TITLE: Shader: Applying Tone Mapping - GLSL
DESCRIPTION: Adds a basic tone mapping function to the final color calculation. This mathematical operation can adjust the overall brightness and contrast of the rendered output, potentially improving the visual appearance of glowing effects.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_toy_glow/index.rst#_snippet_8

LANGUAGE: glsl
CODE:
```
#version 330

uniform vec3 iResolution;
out vec4 fracColor;

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    // Normalized pixel coordinates (from -0.5 to 0.5)
    vec2 uv = fragCoord/iResolution.xy - 0.5;

    // Adjust for aspect ratio
    uv.x *= iResolution.x / iResolution.y;

    // Calculate the distance from center
    float d = length(uv);

    // Calculate color based on distance
    // Inverse distance, scaled down.
    // Adjust exponent (1.0=same, 0.5=slower, 1.5=faster fade)
    float fade_exponent = 1.5;
    vec3 col = vec3(1.0, 0.5, 0.0) * pow(1.0 / (d * 2.0), fade_exponent);

    // Tone mapping
    col = col / (col + 1.0);

    fragColor = vec4(col,1.0);
}
```

----------------------------------------

TITLE: Rendering into Texture Atlas with Custom Projection in Arcade (Python)
DESCRIPTION: Illustrates how to control the projection used when rendering into an atlas texture region. By providing a `projection` tuple (left, right, bottom, top) to `render_into`, you can map a specific coordinate space (e.g., the entire game window coordinates) onto the texture's dimensions, enabling use cases like rendering a minimap or a mirror effect.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/texture_atlas.rst#_snippet_5

LANGUAGE: python
CODE:
```
# Assuming your window is 800 x 600 we could draw the entire game into this atlas region
projection = 0, 800, 0, 600
with spritelist.atlas.render_into(texture, projection=projection) as framebuffer:
    framebuffer.clear()
    # Draw your game here
```

----------------------------------------

TITLE: Load Shader and Track Time in Python
DESCRIPTION: This Python program sets up an Arcade window, loads a GLSL shader, and keeps track of the elapsed time. The elapsed time is crucial for driving the animation within the shader.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_toy_particles/index.rst#_snippet_0

LANGUAGE: Python
CODE:
```
import arcade
import time

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Assume load_shader is a method that compiles and links the shader
        self.shader_program = self.load_shader("explosion_1.glsl")
        self.start_time = time.time()

    def load_shader(self, filename):
        # Placeholder for actual shader loading logic
        print(f"Loading shader: {filename}")
        # In a real application, load, compile, and link the shader
        # Return a shader program object
        return "Simulated Shader Program"

    def on_draw(self):
        arcade.start_render()
        current_time = time.time() - self.start_time
        # Pass current_time to the shader uniform 'iTime'
        # self.shader_program.use()
        # self.shader_program['iTime'] = current_time
        # Draw geometry (e.g., a fullscreen quad) using the shader
        print(f"Drawing with time: {current_time:.2f}")

    def update(self, delta_time):
        pass # No per-frame updates needed in this simple example

if __name__ == "__main__":
    game = MyGame(800, 600, "Shader Toy Particles")
    arcade.run()
```

----------------------------------------

TITLE: Handling Controller Connect Event - Arcade Python
DESCRIPTION: Defines a function `on_connect` decorated with `@manager.event` to serve as a callback for controller connection events. When a controller connects, this function is called with the `controller` object as an argument.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/controller.rst#_snippet_2

LANGUAGE: Python
CODE:
```
      @manager.event
      def on_connect(controller):
          print(f"Connected:  {controller}")
```

----------------------------------------

TITLE: Using CSS Color Name (arcade.csscolor)
DESCRIPTION: Specifies a color using a standard CSS color name accessed through the arcade.csscolor module.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/api_docs/arcade.color.rst#_snippet_0

LANGUAGE: Python
CODE:
```
arcade.csscolor.RED
```

----------------------------------------

TITLE: Original Mouse Visibility Setting - Arcade Python
DESCRIPTION: Demonstrates how to control mouse cursor visibility when the class is an `arcade.Window`. The `set_mouse_visible` method is called directly on `self`.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/views/index.rst#_snippet_4

LANGUAGE: python
CODE:
```
self.set_mouse_visible(False)
```

----------------------------------------

TITLE: Passthrough Fragment Shader GLSL
DESCRIPTION: A basic fragment shader. It receives an interpolated color (`color`) from the vertex shader and outputs it directly as the final pixel color (`fragColor`) for rendering.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/gpu_particle_burst/index.rst#_snippet_5

LANGUAGE: GLSL
CODE:
```
#version 330 core

in vec4 color;
out vec4 fragColor;

void main() {
    fragColor = color;
}
```

----------------------------------------

TITLE: Setting Built-in Uniforms during Render - Python
DESCRIPTION: Shows how to pass the standard built-in ShaderToy uniform values (`iTime`, `iTimeDelta`, `iMouse`, `iFrame`) to the shader when calling the `render()` method on the `Shadertoy` object. This allows the shader to react to application state.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_toy_glow/index.rst#_snippet_11

LANGUAGE: python
CODE:
```
my_shader.render(time=self.time, mouse_position=mouse_position)
```

----------------------------------------

TITLE: Implementing SpriteList Draw Order Sorting with Python
DESCRIPTION: Demonstrates how to sort a SpriteList based on a custom key function (like a sprite's bottom edge) to control draw order. This example sorts sprites so those higher on the screen draw first, simulating depth in a top-down view. Note that sorting is CPU-intensive and often inefficient for large numbers of sprites; this is presented as a prototype example requiring the arcade library.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/sprites/advanced.rst#_snippet_0

LANGUAGE: python
CODE:
```
import random
import arcade


# Warning: the bottom property is extra slow compared to other attributes!
def bottom_edge_as_sort_key(sprite):
    return sprite.bottom


class InefficientTopDownGame(arcade.Window):
    """
    Uses sorting to allow the player to move in front of & behind shrubs

    For non-prototyping purposes, other approaches will be better.
    """

    def __init__(self, num_shrubs=50):
        super().__init__(800, 600, "Inefficient Top-Down Game")

        self.background_color = arcade.color.SAND
        self.shrubs = arcade.SpriteList()
        self.drawable = arcade.SpriteList()

        # Randomly place pale green shrubs around the screen
        for i in range(num_shrubs):
            shrub = arcade.SpriteSolidColor(20, 40, color=arcade.color.BUD_GREEN)
            shrub.position = random.randrange(self.width), random.randrange(self.height)
            self.shrubs.append(shrub)
            self.drawable.append(shrub)

        self.player = arcade.SpriteSolidColor(16, 30, color=arcade.color.RED)
        self.drawable.append(self.player)

    def on_mouse_motion(self, x, y, dx, dy):
        # Update the player position
        self.player.position = x, y
        # Sort the sprites so the highest on the screen draw first
        self.drawable.sort(key=bottom_edge_as_sort_key, reverse=True)

    def on_draw(self):
        self.clear()
        self.drawable.draw()


game = InefficientTopDownGame()
game.run()
```

----------------------------------------

TITLE: Editing Sub Menu Parameters - Python/Arcade
DESCRIPTION: This snippet shows how parameters for a sub-menu class are defined, likely within the class constructor. These parameters, such as `text` and `input_text_default`, are designed to allow the sub-menu to be reused for different purposes (e.g., options vs. volume) with context-specific initial values.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_14

LANGUAGE: Python
CODE:
```
class SubMenu(arcade.gui.UIMixedWidget):
    def __init__(self, text: str, input_text_default: str, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.input_text_default = input_text_default
        # ... other parameter handling
```

----------------------------------------

TITLE: Define Card Positioning Constants - Python
DESCRIPTION: Defines various constants used for calculating the size and position of cards and the 'mat' areas where cards can be placed, facilitating organized layout.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_1

LANGUAGE: Python
CODE:
```
# Constants for sizing
CARD_SCALE = 0.6

# Card dimensions
CARD_WIDTH = 140 * CARD_SCALE
CARD_HEIGHT = 190 * CARD_SCALE

# Card spacing
CARD_VERTICAL_OFFSET = CARD_HEIGHT * 0.3
CARD_HORIZONTAL_OFFSET = CARD_WIDTH * 0.3

# Mat dimensions
MAT_PERCENT_OVERSIZE = 1.25
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENT_OVERSIZE)
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENT_OVERSIZE)

# The Y position for the top row of mats
TOP_Y = SCREEN_HEIGHT - MAT_HEIGHT / 2 - 30

# The X position for the left column of mats
START_X = MAT_WIDTH / 2 + 30

# The Y position for the bottom row of mats
BOTTOM_Y = MAT_HEIGHT / 2 + 30

# The X position for the right columns of mats
END_X = SCREEN_WIDTH - MAT_WIDTH / 2 - 30

# Distance between mats on the top row
TOP_X_SPACING = MAT_WIDTH + 10

# Distance between mats on the bottom row
BOTTOM_X_SPACING = MAT_WIDTH + 10

# Card suits
FACE_DOWN_IMAGE = ":resources:images/card/back.png"

# Card suits
HEART = "Heart"
DIAMOND = "Diamond"
CLUB = "Club"
SPADE = "Spade"
ALL_SUITS = [HEART, DIAMOND, CLUB, SPADE]

# Card values
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# How far apart to stack cards
CARD_PILE_VERTICAL_OFFSET = 25
```

----------------------------------------

TITLE: Reading File Properly with 'with' - Python
DESCRIPTION: Demonstrates the recommended Python practice for reading file content into a string using a 'with' statement, ensuring the file is properly closed afterwards. This is shown as an alternative to simply using `open().read()`.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/shader_toy_glow/index.rst#_snippet_2

LANGUAGE: python
CODE:
```
file_name = "circle_1.glsl"
with open(file_name) as file:
    shader_source = file.read()
self.shadertoy = Shadertoy(size=self.get_size(),
                           main_source=shader_source)
```

----------------------------------------

TITLE: Initializing Setup for Rendering into Texture Atlas in Arcade (Python)
DESCRIPTION: Sets up the components needed to render directly into a texture within the atlas. It involves creating an empty texture of a specific size, creating a sprite using this texture, creating a sprite list, and appending the sprite to the list, which automatically adds the texture to the list's atlas.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/texture_atlas.rst#_snippet_3

LANGUAGE: python
CODE:
```
# --- Initialization ---
# Create an empty texture so we can allocate some space in the atlas
texture = arcade.Texture.create_empty("render_area_1", size=(256, 256))

# Assign the texture to a sprite
sprite = arcade.Sprite(center_x=200, center_y=300, texture=texture)

# Create the spritelist and add the sprite
spritelist = arcade.SpriteList()
# Adding the sprite will also add the texture to the atlas
spritelist.append(sprite)
```

----------------------------------------

TITLE: Upgrade/Reinstall Arcade from URL (bash)
DESCRIPTION: Forces a complete reinstallation of Arcade from a specified URL, ignoring the currently installed version. This is often used for installing development builds.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/get_started/install.rst#_snippet_2

LANGUAGE: bash
CODE:
```
pip install -I https://github.com/pythonarcade/arcade/archive/refs/heads/development.zip
```

----------------------------------------

TITLE: Redirect Console Output to Files with Nuitka Bash
DESCRIPTION: This command compiles the script and redirects its standard error (`stderr`) and standard output (`stdout`) streams to specified log files (`logs.txt` and `output.txt`) relative to the executable directory (`%PROGRAM%`). This hides the console window and logs output to files.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/compiling_with_nuitka/index.rst#_snippet_4

LANGUAGE: bash
CODE:
```
python -m nuitka 17_views.py --standalone --windows-force-stderr-spec=%PROGRAM%logs.txt --windows-force-stdout-spec=%PROGRAM%output.txt
```

----------------------------------------

TITLE: Handling Controller Disconnect Event - Arcade Python
DESCRIPTION: Defines a function `on_disconnect` decorated with `@manager.event` to serve as a callback for controller disconnection events. When a controller disconnects, this function is called with the `controller` object as an argument.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/controller.rst#_snippet_3

LANGUAGE: Python
CODE:
```
      @manager.event
      def on_disconnect(controller):
          print(f"Disconnected:  {controller}")
```

----------------------------------------

TITLE: Initialize Card Mat Sprite List (Arcade, Python)
DESCRIPTION: Initializes the sprite list that will hold the visual guides (mats) for the card piles within the game class's constructor.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_13

LANGUAGE: python
CODE:
```
# Placeholder for code from solitaire_04.py MyGame.__init__ emphasize-lines 16-17
# Example: self.mat_list = arcade.SpriteList()
```

----------------------------------------

TITLE: Set Custom Icon from Executable with Nuitka Bash
DESCRIPTION: This command compiles the script and sets a custom icon for the Windows executable by extracting it from an existing executable file. The `--windows-icon-from-exe` flag specifies the path to the source executable file (`python.exe` in this example).
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/compiling_with_nuitka/index.rst#_snippet_6

LANGUAGE: bash
CODE:
```
python -m nuitka 17_views.py --standalone --windows-icon-from-exe=C:\Users\Hunter\AppData\Local\Programs\Python\Python310/python.exe
```

----------------------------------------

TITLE: Setup Initial Card Piles (Arcade, Python)
DESCRIPTION: Initializes the lists for each card pile and populates the initial deal pile with all the cards within the game's setup method.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/card_game/index.rst#_snippet_20

LANGUAGE: python
CODE:
```
# Placeholder for code from solitaire_07.py MyGame.setup lines 54-59
# Example: Create lists for each pile and add cards to the deal pile
```

----------------------------------------

TITLE: Handling Mouse Press Python Arcade (v3)
DESCRIPTION: Further updates the mouse press handler to generate more realistic particle velocities. Instead of random x/y deltas, it picks a random angle and speed, then calculates `delta_x` and `delta_y` using `math.cos` and `math.sin`.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/gpu_particle_burst/index.rst#_snippet_15

LANGUAGE: Python
CODE:
```
def on_mouse_press(self, x, y, button, modifiers):
    # Need to convert to normalized device coordinates (0-1, 0-1)
    norm_x = x / self.width
    norm_y = y / self.height

    def _gen_initial_data(count: int):
        for i in range(count):
            # Pick a random angle and speed
            angle = random.random() * 2 * math.pi
            speed = random.random() * .02
            # speed = random.gauss(0.0, .01) # Alternative for splat look

            # x, y
            yield norm_x
            yield norm_y

            # delta_x, delta_y
            yield math.cos(angle) * speed
            yield math.sin(angle) * speed

    # Create the buffer
    # We have two floats for pos (x, y) and two for velocity (dx, dy)
    # 2f 2f stands for 4 floats per particle
    # We have PARTICLE_COUNT particles
    # in_pos and in_vel reference the variable names in the vertex shader
    vao = self.ctx.buffer(
        data=list(_gen_initial_data(PARTICLE_COUNT)))
    buffer_description = arcade.gl.BufferDescription(vao, '2f 2f',
                                                      ['in_pos', 'in_vel'])
    new_burst = Burst(self.ctx.geometry([buffer_description]), time.time())
    self.burst_list.append(new_burst)
```

----------------------------------------

TITLE: Google Style Docstring Args Example - Python
DESCRIPTION: This snippet illustrates the required Google Style format for the 'Args:' block within a Python docstring. It lists function parameters with their descriptions.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/CONTRIBUTING.md#_snippet_3

LANGUAGE: python
CODE:
```
Args:
    width: The width of something
    height: The height of something
    title: The title of something
```

----------------------------------------

TITLE: Building & Serving Docs with Live Reload - Bash
DESCRIPTION: This command builds the project's documentation and starts a local web server that automatically rebuilds and refreshes the browser when source files are changed. It's useful for previewing documentation changes.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/CONTRIBUTING.md#_snippet_13

LANGUAGE: bash
CODE:
```
python make.py serve
```

----------------------------------------

TITLE: Instantiating Controller Manager - Arcade Python
DESCRIPTION: Creates an instance of the `ControllerManager` class, which is used to manage controller connections and disconnections, facilitating hot-plugging functionality in Arcade applications.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/example_code/controller.rst#_snippet_1

LANGUAGE: Python
CODE:
```
      manager = arcade.input.ControllerManager()
```

----------------------------------------

TITLE: Enabling Headless Mode via Environment Variable (Bash)
DESCRIPTION: Demonstrates how to enable Arcade's headless mode by exporting the ARCADE_HEADLESS environment variable as True in a bash shell before running a Python script that uses Arcade.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/headless.rst#_snippet_1

LANGUAGE: bash
CODE:
```
export ARCADE_HEADLESS=True
```

----------------------------------------

TITLE: Defining Optional SpriteList Attribute in Python
DESCRIPTION: This snippet demonstrates how to define an instance variable `player_list` using Python's type hinting. It indicates that the attribute can be either an `arcade.SpriteList` instance or `None`. This is useful for static analysis and clarity.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/pymunk_platformer/index.rst#_snippet_0

LANGUAGE: Python
CODE:
```
self.player_list: Optional[arcade.SpriteList] = None
```

----------------------------------------

TITLE: Running Linting Tools - Bash
DESCRIPTION: This command executes the project's linting process using the make.py script. It typically runs tools like MyPy and Ruff to check code for style issues, potential errors, and type correctness.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/CONTRIBUTING.md#_snippet_8

LANGUAGE: bash
CODE:
```
python make.py lint
```

----------------------------------------

TITLE: Rendering into Texture Atlas with Scrolling Projection in Arcade (Python)
DESCRIPTION: Shows how to apply scrolling or zooming effects when rendering into an atlas texture region by adjusting the `projection` coordinates based on variables like `scroll_x` and `scroll_y`. This allows the rendered content within the texture to represent a different view of the scene, similar to camera movement.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/programming_guide/texture_atlas.rst#_snippet_6

LANGUAGE: python
CODE:
```
# Scroll projection (or even zoom)
projection = 0 + scroll_x, 800 + scroll_x, 0 + scroll_y, 600 + scroll_y
```

----------------------------------------

TITLE: Adding a Slider - Python/Arcade
DESCRIPTION: This snippet creates an `arcade.gui.UISlider` widget. It sets the minimum and maximum values, an initial value, and the width. It also includes optional styling for the slider's appearance.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/menu/index.rst#_snippet_24

LANGUAGE: Python
CODE:
```
slider_label = arcade.gui.UILabel(text="Volume:")
slider = arcade.gui.UISlider(
    min_value=0,
    max_value=100,
    initial_value=50,
    width=200
)
# Styling example (optional, based on description)
slider.with_style(
    arcade.gui.UIStyle(
        filled_bar=arcade.color.GREEN,
        unfilled_bar=arcade.color.GRAY,
        bar_height=5,
        border_color=arcade.color.BLACK,
        border_width=1,
        handle_color=arcade.color.BLUE,
        handle_width=10,
        handle_height=20
    )
)
slider_hbox = arcade.gui.UIBoxLayout(vertical=False)
slider_hbox.add(slider_label)
slider_hbox.add(slider)
```

----------------------------------------

TITLE: Initializing Score Reset Trigger | Arcade Python
DESCRIPTION: Adds a new boolean instance variable `self.reset_score` to the `__init__` function. This variable acts as a flag to determine whether the player's score should be reset when the `setup` function is executed.
SOURCE: https://github.com/pythonarcade/arcade/blob/development/doc/tutorials/platform_tutorial/step_14.rst#_snippet_4

LANGUAGE: Python
CODE:
```
# Should we reset the score?
self.reset_score = True
```