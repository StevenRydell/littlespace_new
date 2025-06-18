import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 360
SCREEN_SCALE = 2
SCREEN_TITLE = "Simple Circle Game"

CIRCLE_RADIUS = 10
MOVEMENT_SPEED = 3

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH * SCREEN_SCALE, SCREEN_HEIGHT * SCREEN_SCALE, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        
        # Circle position (start in center)
        self.circle_x = SCREEN_WIDTH // 2
        self.circle_y = SCREEN_HEIGHT // 2
        
        # Key states for smooth movement
        self.key_up = False
        self.key_down = False
        self.key_left = False
        self.key_right = False
        
        # FPS tracking
        self.frame_delta_time = 0.0
        
        # Create Text object for FPS display (much faster than draw_text)
        self.fps_text = arcade.Text("FPS: --", 
                                   (SCREEN_WIDTH * SCREEN_SCALE) - 100, 
                                   20, 
                                   arcade.color.GREEN, 
                                   16)

    def on_draw(self):
        self.clear()
        
        # Draw the circle (scaled coordinates)
        arcade.draw_circle_filled(
            self.circle_x * SCREEN_SCALE, 
            self.circle_y * SCREEN_SCALE, 
            CIRCLE_RADIUS * SCREEN_SCALE, 
            arcade.color.WHITE
        )
        
        # Draw FPS in bottom-right corner
        self.fps_text.draw()

    def on_update(self, delta_time):
        # Store delta_time for FPS calculation
        self.frame_delta_time = delta_time
        
        # Update FPS text
        fps_value = f"FPS: {1/self.frame_delta_time:.1f}" if self.frame_delta_time > 0 else "FPS: --"
        self.fps_text.text = fps_value
        
        # Update circle position based on key states
        if self.key_up and self.circle_y < SCREEN_HEIGHT - CIRCLE_RADIUS:
            self.circle_y += MOVEMENT_SPEED
        if self.key_down and self.circle_y > CIRCLE_RADIUS:
            self.circle_y -= MOVEMENT_SPEED
        if self.key_left and self.circle_x > CIRCLE_RADIUS:
            self.circle_x -= MOVEMENT_SPEED
        if self.key_right and self.circle_x < SCREEN_WIDTH - CIRCLE_RADIUS:
            self.circle_x += MOVEMENT_SPEED

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.key_up = True
        elif key == arcade.key.DOWN:
            self.key_down = True
        elif key == arcade.key.LEFT:
            self.key_left = True
        elif key == arcade.key.RIGHT:
            self.key_right = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.key_up = False
        elif key == arcade.key.DOWN:
            self.key_down = False
        elif key == arcade.key.LEFT:
            self.key_left = False
        elif key == arcade.key.RIGHT:
            self.key_right = False

def main():
    window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()